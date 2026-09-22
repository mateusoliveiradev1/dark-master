#!/usr/bin/env python3
"""notion_pack.py — gera o PACOTE NOTION do canal (CSVs importáveis + guia de setup).

Lê a pasta real do canal e produz, em <canal>/notion/:
  VIDEOS.csv      — 1 linha por vídeo: caso, série, status do pipeline, títulos, arquivos
  CALENDARIO.csv  — a grade do 00_CANAL/CALENDARIO_30.txt (data, dia, short 12:00, long 21:00)
  IDEIAS.csv      — banco de posts/ideias (00_CANAL/POSTS_BANCO_30DIAS.txt)
  OUTLIERS.csv    — outliers reais (data/outliers.json da skill), com padrão/lição
  NOTION_SETUP.md — passo a passo de import + views (Kanban, Calendar) + rotina

Uso:
  python scripts/notion_pack.py "<pasta do canal>" [--out "<pasta>/notion"]

Nada é publicado no Notion automaticamente: o import é manual (CSV), sem token/API.
"""
import argparse
import csv
import json
import re
import sys
from datetime import date
from pathlib import Path

MEDIA_EXT = (".jpg", ".jpeg", ".png", ".webp")
SKILL_DATA = Path(__file__).resolve().parent.parent / "data" / "outliers.json"


def video_dirs(root):
    out = []
    for p in root.iterdir():
        if p.is_dir() and (re.fullmatch(r"video\d+", p.name) or re.fullmatch(r"EP\d+.*", p.name)):
            out.append(p)
    return sorted(out, key=lambda p: (len(p.name), p.name))


def words_of(p):
    try:
        return len(re.findall(r"\w+", p.read_text(encoding="utf-8", errors="replace"), flags=re.UNICODE))
    except OSError:
        return 0


def pipeline_status(v):
    """Backlog -> Roteiro -> Voz -> Imagens -> Montagem -> Pronto."""
    rot = v / "01_roteiro" / "narration_v3.txt"
    aud = v / "02_audio"
    imgs = [f for f in (v / "03_imagens").glob("*") if f.suffix.lower() in MEDIA_EXT] \
        if (v / "03_imagens").exists() else []
    fin = v / "04_video_final"
    has = lambda *names: any((fin / n).exists() for n in names)
    yt = has(f"{v.name}_YOUTUBE.mp4", f"{v.name}_FINAL.mp4")
    short = has(f"{v.name}_SHORT.mp4")
    thumb = any(fin.glob("thumb*.png")) if fin.exists() else False
    voz = any(aud.glob("voice*FINAL*")) if aud.exists() else False
    if yt and short and thumb:
        return "Pronto", len(imgs)
    if voz and len(imgs) >= 26:
        return "Montagem", len(imgs)
    if voz:
        return "Imagens", len(imgs)
    if words_of(rot) >= 50:
        return "Voz", len(imgs)
    return "Backlog", len(imgs)


SERIES_HINT = ("VANISHED", "SMALL TOWN SECRETS", "SMALL TOWN", "HEISTS & LIES", "HEISTS",
               "KILLERS UNKNOWN", "KILLERS", "HEIST/KILLER")


def parse_package(v):
    pkg = v / "youtube_package.txt"
    caso = serie = titulo = ""
    if not pkg.exists():
        return caso, serie, titulo
    txt = pkg.read_text(encoding="utf-8", errors="replace")
    for line in txt.splitlines():
        s = line.strip()
        if s.upper().startswith("CASO:") and not caso:
            caso = re.split(r"\s*\|\s*", s.split(":", 1)[1].strip())[0].strip()
    m = re.search(r"SERIE:\s*([^|\n]+)", txt)
    if m:
        serie = m.group(1).strip()
    m = re.search(r"TITLE[^\n]*\n\s*1\.\s*(.+)", txt)
    if m and m.group(1).strip():
        titulo = m.group(1).strip()
    return caso, serie, titulo


def parse_calendar(root):
    """Linhas no formato: 'D1 14/09 SEG video01 Sodder 1945 VANISHED | nota...'."""
    f = root / "00_CANAL" / "CALENDARIO_30.txt"
    rows = []
    if not f.exists():
        return rows
    for line in f.read_text(encoding="utf-8", errors="replace").splitlines():
        s = line.strip()
        if not re.match(r"^D\d+\s+\d{2}/\d{2}\s+\w{3}\s+(video|EP)\S*", s):
            continue
        pre, _, post = s.partition("|")
        toks = pre.split()
        dia, data, wd, vid = toks[0], toks[1], toks[2], toks[3]
        rest = " ".join(toks[4:]).strip()
        serie, pos = "", -1
        for cand in SERIES_HINT:
            p = rest.upper().rfind(cand)
            if p > pos:
                pos, serie = p, cand
        caso = rest[:pos].strip() if pos >= 0 else rest
        rows.append([dia, data, wd, vid, caso, serie, post.strip()])
    return rows


def parse_ideas(root):
    f = root / "00_CANAL" / "POSTS_BANCO_30DIAS.txt"
    ideas = []
    if not f.exists():
        return ideas
    for line in f.read_text(encoding="utf-8", errors="replace").splitlines():
        s = line.strip()
        if not s or s.startswith("#") or s.isupper() and len(s) > 40:
            continue
        if s.startswith(("- ", "• ")) or re.match(r"^\d+[.)]\s", s):
            ideas.append(re.sub(r"^(\d+[.)]|[-•])\s*", "", s))
    return ideas


def write_csv(path, header, rows):
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)
    print(f"[OK] {path.name}: {len(rows)} linha(s)")


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("channel")
    ap.add_argument("--out")
    ap.add_argument("--skill-data", default=str(SKILL_DATA))
    a = ap.parse_args()

    root = Path(a.channel).expanduser().resolve()
    if not root.is_dir():
        print(f"[!] pasta nao encontrada: {root}"); return 1
    out = Path(a.out).expanduser() if a.out else root / "notion"
    out.mkdir(parents=True, exist_ok=True)

    # VIDEOS
    cal_list = parse_calendar(root)
    cal = {c[3]: c for c in cal_list}
    rows = []
    for v in video_dirs(root):
        caso, serie, titulo = parse_package(v)
        st, nimg = pipeline_status(v)
        c = cal.get(v.name)
        rows.append([v.name, caso or (c[4] if c else ""), serie or (c[5] if c else ""),
                     c[1] if c else "", st, titulo, "", "",
                     nimg, "sim" if (v / "youtube_package.txt").exists() else "nao",
                     c[6] if c else ""])
    write_csv(out / "VIDEOS.csv",
              ["ID", "Caso", "Serie", "Data", "Status", "TituloLong", "TituloShort",
               "Link", "Imagens", "Pacote", "Nota"], rows)

    # CALENDARIO
    write_csv(out / "CALENDARIO.csv",
              ["Data", "Dia", "ID", "Caso", "Serie", "Short12h", "Long21h", "Nota"],
              [[c[1], c[0], c[3], c[4], c[5], "12:00 BRT", "21:00 BRT", c[6]] for c in cal_list])

    # IDEIAS
    ideas = parse_ideas(root)
    write_csv(out / "IDEIAS.csv", ["Ideia", "Tipo", "Status", "Fonte"],
              [[i, "post", "backlog", "POSTS_BANCO_30DIAS.txt"] for i in ideas])

    # OUTLIERS
    orows = []
    sk = Path(a.skill_data)
    if sk.exists():
        try:
            d = json.loads(sk.read_text(encoding="utf-8"))
            for o in d.get("outliers", []):
                orows.append([o.get("caso", o.get("video", "")), o.get("format", ""),
                              o.get("views", ""), o.get("avp_percent", ""),
                              o.get("hook", ""), o.get("padrao", ""), o.get("licao", "")])
        except ValueError:
            pass
    write_csv(out / "OUTLIERS.csv",
              ["Caso", "Formato", "Views", "AVP%", "Hook", "Padrao", "Licao"], orows)

    setup = f"""# NOTION — {root.name} (setup)

> Gerado por `scripts/notion_pack.py` em {date.today().isoformat()}. Import manual (sem API/token).

## 1) Importar (5 min)
1. Notion → nova página **{root.name} — Central**.
2. Para cada CSV desta pasta: arraste o arquivo para a página → **Import** → escolha **CSV** → cria um database.
3. Renomeie os databases: **Vídeos**, **Calendário**, **Ideias**, **Outliers**.

## 2) Propriedades recomendadas (edite 1x)
- **Vídeos:** `Status` → *Select* (Backlog, Voz, Imagens, Montagem, Pronto, Publicado); `Data` → *Date*; `Caso`/`Série` → *Select*; `Link` → *URL*.
- **Calendário:** `Data` → *Date*; `Status` → *Select* (Agendado, Publicado, Atrasado).
- **Ideias:** `Status` → *Select* (backlog, aprovada, feita).
- **Outliers:** `Views` → *Number*; `AVP%` → *Number*.

## 3) Views (criar 1x)
- Vídeos → **Kanban** por `Status` (o pipeline vira um board).
- Calendário → **Calendar** por `Data` (a grade dos 30 dias).
- Vídeos → **Table** filtrada em `Status = Pronto` (fila de agendamento).
- Outliers → **Gallery** ordenada por `Views` desc (padrões a replicar).

## 4) Relações (opcional, 1x)
- No database **Calendário**, crie `Relation` → **Vídeos** (ligue `ID` ↔ `ID`).
- No **Vídeos**, crie `Rollup` do Calendário (data alvo).

## 5) Rotina
- **Domingo:** revisar Ideias → mover aprovadas para o Calendário.
- **Diário:** atualizar `Status` do vídeo do dia (Voz → Imagens → Montagem → Pronto → Publicado).
- **D+2/D+7:** registrar views no Outliers (ou rodar `/dark-revisar` e re-importar o CSV).
- Regenerar: `python scripts/notion_pack.py "{root}"` (sobrescreve os CSVs; re-importe como *Merge*).

## Observações
- Nada de segredo/token aqui: import é manual por design.
- Se quiser automação futura via API do Notion, crie uma integração interna e use um database de destino — a skill só precisa do token (fora do repositório).
"""
    (out / "NOTION_SETUP.md").write_text(setup, encoding="utf-8")
    print(f"[OK] {out / 'NOTION_SETUP.md'}")
    print(f"\nPacote Notion pronto em: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
