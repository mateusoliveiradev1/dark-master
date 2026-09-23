#!/usr/bin/env python3
"""timeline_kit.py — linha do tempo do caso: plate PNG + datestamps ASS para a edicao.

Uso:
  python scripts/timeline_kit.py video01 --root "<canal>" --channel laudo-final
  python scripts/timeline_kit.py video01 --root "<canal>" --plate-only --to-imagens
  python scripts/timeline_kit.py video01 --root "<canal>" --stamps-only --lang pt

Entradas:
  <videoNN>/01_roteiro/LINHA_DO_TEMPO.md   (tabela | data | fato | camada | fonte |)
  <videoNN>/02_audio/captions.srt          (timing real da narracao -> datestamps)

Saidas:
  <videoNN>/04_video_final/timeline_plate.png   (--to-imagens: 03_imagens/38_timeline.png, estilo Money)
  <videoNN>/04_video_final/datestamps.ass       (data corrente na tela, carry-forward)
  + comando ffmpeg pronto para queimar o ASS no video final.

Formato da data aceito: 2010 | 2010-06 | 2010-06-09 | 09/06/2010 | "?" (sem data).
"""
import argparse
import os
import re
import sys
from pathlib import Path

MONTHS = {
    "pt": ["JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ"],
    "en": ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"],
}
MONTH_NAMES = {
    "pt": {"janeiro": 1, "fevereiro": 2, "marco": 3, "março": 3, "abril": 4, "maio": 5, "junho": 6,
           "julho": 7, "agosto": 8, "setembro": 9, "outubro": 10, "novembro": 11, "dezembro": 12},
    "en": {"january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6, "july": 7,
           "august": 8, "september": 9, "october": 10, "november": 11, "december": 12},
}


def parse_cell(s):
    """'2010-06-09' | '2010-06' | '2010' | '09/06/2010' | '?' -> (y,m,d,prec) ou None."""
    s = (s or "").strip()
    if not s or s in ("?", "-"):
        return None
    m = re.match(r"^(\d{4})-(\d{1,2})-(\d{1,2})$", s)
    if m:
        return int(m.group(1)), int(m.group(2)), int(m.group(3)), "d"
    m = re.match(r"^(\d{4})-(\d{1,2})$", s)
    if m:
        return int(m.group(1)), int(m.group(2)), 0, "m"
    m = re.match(r"^(\d{1,2})/(\d{1,2})/(\d{2,4})$", s)
    if m:
        y = int(m.group(3))
        y = y + 2000 if y < 100 else y
        return y, int(m.group(2)), int(m.group(1)), "d"
    m = re.match(r"^(\d{4})$", s)
    if m:
        return int(m.group(1)), 0, 0, "y"
    return None


def fmt_label(dt, lang="pt", precision=None):
    y, mo, d, prec = dt
    prec = precision or prec
    if prec == "d" and d and mo:
        return f"{d} {MONTHS[lang][mo-1]} {y}"
    if prec in ("m",) and mo:
        return f"{MONTHS[lang][mo-1]} {y}"
    return f"{y}"


def read_timeline(path):
    """Le a tabela markdown e devolve [(sort_key, label, fato, camada, fonte)]."""
    rows = []
    if not os.path.exists(path):
        return rows
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2 or cells[0].lower() in ("data", "date", ":---", "---", "") or set(cells[0]) <= set("-: "):
            continue
        dt = parse_cell(cells[0])
        if dt is None:
            rows.append(((9999, 99, 99), cells[0] or "?", cells[1], cells[2] if len(cells) > 2 else "",
                         cells[3] if len(cells) > 3 else ""))
            continue
        rows.append(((dt[0], dt[1] or 99, dt[2] or 99), fmt_label(dt, "pt", "d" if dt[3] == "d" else dt[3]),
                     cells[1], cells[2] if len(cells) > 2 else "", cells[3] if len(cells) > 3 else ""))
    rows.sort(key=lambda r: r[0])
    return rows


def load_style(pb):
    import json
    try:
        return json.loads((Path(pb) / "style.json").read_text(encoding="utf-8"))
    except (OSError, ValueError, TypeError):
        return {}


def style_colors(st):
    th = (st.get("thumb") or {})
    c = th.get("colors") or {}
    white = tuple(c.get("white") or (245, 245, 244))
    red = tuple(c.get("red") or (220, 38, 38))
    black = tuple(c.get("black") or (8, 9, 11))
    return black, white, red


def font_path(st, bold=True):
    f = ((st.get("thumb") or {}).get("font") or "")
    if f and os.path.exists(f):
        return f
    for cand in ("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
                 "C:/Windows/Fonts/arial.ttf"):
        if os.path.exists(cand):
            return cand
    return None


def make_plate(rows, out, st, title="LINHA DO TEMPO", subtitle="reconstruida a partir de fontes publicas"):
    from PIL import Image, ImageDraw, ImageFont
    BG, PAPER, ACCENT = style_colors(st)
    MUTED = tuple(min(255, c + 70) for c in BG)
    W, H = 1920, 1080
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    def font(sz, bold=True):
        p = font_path(st, bold)
        try:
            return ImageFont.truetype(p, sz) if p else ImageFont.load_default()
        except OSError:
            return ImageFont.load_default()

    def wrap(text, max_chars):
        words, lines, cur = (text or "").split(), [], ""
        for w in words:
            if len(cur + " " + w) <= max_chars:
                cur = (cur + " " + w).strip()
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        return lines

    def draw_row(evs, y, big=False):
        n = len(evs)
        if not n:
            return
        d.line([140, y, W - 140, y], fill=MUTED, width=4)
        step = (W - 280) // max(1, n - 1) if n > 1 else 0
        col = step if n > 1 else (W - 280)
        fs_label, fs_txt = (40, 30) if big else (34, 26)
        max_chars = max(10, min(26, int(col / (fs_txt * 0.55))))
        for i, (_, label, fato, camada, _f) in enumerate(evs):
            x = 140 + i * step if n > 1 else W // 2
            unknown = label in ("?", "-")
            r = 12 if big else 10
            d.ellipse([x - r, y - r, x + r, y + r],
                      fill=BG if unknown else ACCENT, outline=ACCENT, width=4)
            bb = d.textbbox((0, 0), label, font=font(fs_label))
            d.text((x - (bb[2] - bb[0]) // 2, y - (86 if big else 74)), label, font=font(fs_label), fill=ACCENT)
            for j, ln in enumerate(wrap(fato, max_chars)[:4 if not big else 3]):
                b2 = d.textbbox((0, 0), ln, font=font(fs_txt, False))
                d.text((x - (b2[2] - b2[0]) // 2, y + (36 if big else 30) + j * (fs_txt + 10)),
                       ln, font=font(fs_txt, False), fill=PAPER)

    d.text((120, 60), title, font=font(54), fill=PAPER)
    d.text((120, 130), subtitle, font=font(28, False), fill=MUTED)
    evs = rows[:12]
    if len(evs) <= 6:
        draw_row(evs, 560, big=True)
    else:
        half = (len(evs) + 1) // 2
        draw_row(evs[:half], 380)
        draw_row(evs[half:], 780)
    d.text((120, H - 80), "LINHA DO TEMPO - reconstruida com fontes; ver descricao", font=font(24, False),
           fill=MUTED)
    img.save(out)
    return out


def read_srt(path):
    """[(start_s, end_s, texto)] simples (sem \n internos)."""
    if not os.path.exists(path):
        return []
    txt = Path(path).read_text(encoding="utf-8", errors="replace")
    cues = []
    for block in re.split(r"\n\s*\n", txt):
        lines = [l.strip() for l in block.splitlines() if l.strip()]
        if len(lines) < 2:
            continue
        m = re.match(r"(\d+):(\d\d):(\d\d)[,.](\d+)\s*-->\s*(\d+):(\d\d):(\d\d)[,.](\d+)", lines[1] if "-->" in lines[1] else lines[0])
        if not m:
            continue
        g = [int(x) for x in m.groups()]
        t0 = g[0] * 3600 + g[1] * 60 + g[2] + g[3] / 1000.0
        t1 = g[4] * 3600 + g[5] * 60 + g[6] + g[7] / 1000.0
        cues.append((t0, t1, " ".join(lines[2:]) if "-->" in lines[1] else " ".join(lines[1:])))
    return cues


def date_in_text(text, lang="pt"):
    """Primeira data falada no texto -> (y,m,d,prec) ou None."""
    t = text.lower()
    m = re.search(r"\b(\d{1,2}) de (" + "|".join(MONTH_NAMES[lang]) + r")(?: de (\d{4}))?\b", t)
    if m:
        mo = MONTH_NAMES[lang][m.group(2)]
        y = int(m.group(3)) if m.group(3) else None
        return (y or 0, mo, int(m.group(1)), "d")
    m = re.search(r"\b(" + "|".join(MONTH_NAMES[lang]) + r") de (\d{4})\b", t)
    if m:
        return (int(m.group(2)), MONTH_NAMES[lang][m.group(1)], 0, "m")
    m = re.search(r"\b(\d{1,2})/(\d{1,2})/(\d{2,4})\b", t)
    if m:
        y = int(m.group(3))
        return (y + 2000 if y < 100 else y, int(m.group(2)), int(m.group(1)), "d")
    m = re.search(r"\b(19|20)\d{2}\b", t)
    if m:
        return (int(m.group(0)), 0, 0, "y")
    return None


def ass_time(s):
    h = int(s // 3600)
    m = int((s % 3600) // 60)
    sec = s % 60
    return f"{h}:{m:02d}:{sec:05.2f}"


def make_datestamps(cues, out, lang="pt", font_name="Arial", margin_v=130, min_show=1.5, skip_first=0.0):
    events, cur = [], None
    for t0, t1, txt in cues:
        if t0 < skip_first:
            continue
        dt = date_in_text(txt, lang)
        if dt:
            cur = dt
        if cur is None:
            continue
        events.append([t0, t1, cur])
    # fecha cada evento no inicio do proximo; aplica duracao minima
    merged = []
    for i, ev in enumerate(events):
        end = events[i + 1][0] if i + 1 < len(events) else ev[1] + 1.0
        if end - ev[0] < min_show and merged:
            continue
        merged.append([ev[0], max(end, ev[0] + min_show), ev[2]])
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
ScaledBorderAndShadow: yes
[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Datestamp,{font_name},54,&H00FFFFFF,&H000000FF,&H00000000,&H96000000,-1,0,0,0,100,100,1.5,0,1,3,1,9,40,60,{margin_v},1
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    lines = []
    for t0, t1, dt in merged:
        label = fmt_label(dt, lang, "d" if dt[2] else ("m" if dt[1] else "y"))
        lines.append(f"Dialogue: 0,{ass_time(t0)},{ass_time(t1)},Datestamp,,0,0,0,,{label}")
    Path(out).write_text(head + "\n".join(lines) + "\n", encoding="utf-8")
    return out, len(merged)


def main():
    ap = argparse.ArgumentParser(description="Linha do tempo: plate PNG + datestamps ASS")
    ap.add_argument("video")
    ap.add_argument("--root", default=os.getcwd())
    ap.add_argument("--channel", help="playbook do canal (paleta/fonte do style.json)")
    ap.add_argument("--timeline", help="arquivo da linha do tempo (default 01_roteiro/LINHA_DO_TEMPO.md)")
    ap.add_argument("--captions", help="SRT (default 02_audio/captions.srt)")
    ap.add_argument("--lang", choices=["pt", "en"], default=None)
    ap.add_argument("--font-name", help="nome da fonte no ASS (default: do style.json/arial)")
    ap.add_argument("--margin-v", type=int, default=130)
    ap.add_argument("--skip-first", type=float, default=0.0, help="segundos iniciais sem datestamp")
    ap.add_argument("--plate-only", action="store_true")
    ap.add_argument("--stamps-only", action="store_true")
    ap.add_argument("--to-imagens", action="store_true",
                    help="plate vai para 03_imagens/38_timeline.png (estilo Money; entra no motion)")
    a = ap.parse_args()

    root = Path(a.root)
    vdir = Path(a.video) if os.path.isabs(a.video) else root / a.video
    if not vdir.is_dir():
        alt = root / "videos" / Path(a.video).name
        if alt.is_dir():
            vdir = alt
    if not vdir.is_dir():
        raise SystemExit(f"[ERRO] video nao encontrado: {vdir}")

    pb = None
    if a.channel:
        p = Path(a.channel)
        if p.is_dir():
            pb = p
        else:
            p = Path(os.environ.get(
                "DARK_MASTER_PLAYBOOKS",
                str(Path.home() / ".config" / "opencode" / "skills" / "dark-master" / "playbooks"))) / a.channel
            if p.is_dir():
                pb = p
        if pb is None:
            print(f"[AVISO] canal '{a.channel}' nao encontrado - usando estilo neutro")
    st = load_style(pb) if pb else {}
    lang = a.lang or (st.get("language") if st else None) or "pt"
    if lang not in ("pt", "en"):
        lang = "pt"

    outdir = vdir / "04_video_final"
    outdir.mkdir(parents=True, exist_ok=True)
    tl = Path(a.timeline) if a.timeline else vdir / "01_roteiro" / "LINHA_DO_TEMPO.md"
    srt = Path(a.captions) if a.captions else vdir / "02_audio" / "captions.srt"

    if not a.stamps_only:
        rows = read_timeline(str(tl))
        if not rows:
            print(f"[AVISO] linha do tempo vazia/ausente: {tl}")
        else:
            title = "LINHA DO TEMPO"
            try:
                first = tl.read_text(encoding="utf-8").splitlines()[0]
                if first.startswith("#"):
                    title = first.lstrip("# ").strip().upper()
            except OSError:
                pass
            out_png = (vdir / "03_imagens" / "38_timeline.png") if a.to_imagens else (outdir / "timeline_plate.png")
            out_png.parent.mkdir(parents=True, exist_ok=True)
            make_plate(rows, str(out_png), st, title=title)
            print(f"plate ok ({len(rows)} eventos) -> {out_png}")

    if not a.plate_only:
        cues = read_srt(str(srt))
        if not cues:
            print(f"[AVISO] sem captions em {srt} - rode a voz primeiro (gera captions.srt)")
        else:
            fname = a.font_name
            if not fname:
                f = (st.get("thumb") or {}).get("font") or ""
                base = os.path.splitext(os.path.basename(f))[0] if f else "Arial"
                fname = re.sub(r"(?<!^)(?=[A-Z])", " ", base) if base.lower().startswith("bebas") else "Arial"
            out_ass, n = make_datestamps(cues, str(outdir / "datestamps.ass"), lang, fname,
                                         a.margin_v, skip_first=a.skip_first)
            print(f"datestamps ok ({n} marcas, {lang}, fonte {fname}) -> {out_ass}")
            rel = str(outdir / "datestamps.ass").replace("\\", "/")
            print("\nQueimar no video final (apos o motion):")
            print(f'  ffmpeg -y -i "<videoNN>_FINAL.mp4" -vf "ass=\'{rel}\'" '
                  f'-c:v libx264 -preset veryfast -crf 19 -c:a copy "<videoNN>_DATADO.mp4"')


if __name__ == "__main__":
    main()
