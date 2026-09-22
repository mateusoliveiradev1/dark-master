#!/usr/bin/env python3
"""channel_scan.py — a skill 'entende' um canal: le o projeto e reporta o contexto.

Uso:
  python scripts/channel_scan.py "C:/Users/Liiiraa/Downloads/canal dark1"
  python scripts/channel_scan.py --channel "D:/dark-forense"

O que reporta:
  - estrutura e arquivos de contexto (calendario, branding, regras)
  - estado de cada video (roteiro, tease, imagens, audio, final, thumbs, pacote)
  - a CORRENTE DE TEASER: qual caso cada video anuncia no fim (o do dia seguinte)
  - alertas: buracos na corrente / videos faltando / proximo a produzir

Serve para a skill operar DENTRO do fluxo do canal, sem quebrar o encadeamento.
"""
import argparse
import re
from pathlib import Path

VIDEO_RE = re.compile(r"^(video|ep|episode)[ _-]?(\d+)", re.IGNORECASE)


def find_calendar(root):
    cands = list(root.rglob("CALENDARIO*.txt")) + list(root.rglob("calendar*.txt")) \
        + list(root.rglob("CALENDARIO*"))
    return cands[0] if cands else None


def video_dirs(root):
    out = []
    for p in root.rglob("*"):
        if p.is_dir() and VIDEO_RE.match(p.name):
            out.append(p)
    # tambem EP01_* em 01_EPISODES
    for p in root.rglob("EP*"):
        if p.is_dir() and re.match(r"^EP\d+", p.name):
            out.append(p)
    return sorted(set(out), key=lambda x: (x.parent.as_posix(), x.name))


def state(vdir):
    def has(*names):
        for n in names:
            if list(vdir.rglob(n)):
                return True
        return False
    f = {
        "roteiro": has("narration*.txt", "script.py"),
        "tease": has("tease.txt"),
        "pesquisa": has("PESQUISA_FONTE.md", "case-brief.md"),
        "imagens": bool(list(vdir.rglob("*.jpg")) + list(vdir.rglob("*.png"))),
        "audio": has("voice_FINAL.wav", "*.wav", "*.mp3"),
        "final": has("*_YOUTUBE.mp4", "*_FINAL.mp4", "*.mp4"),
        "thumbs": has("thumb*.png", "thumb*.jpg"),
        "pacote": has("youtube_package.txt", "PACOTE_PUBLICACAO.txt"),
    }
    return f


def teaser_line(vdir):
    """Extrai a frase 'tomorrow/next' do fim do roteiro (a corrente)."""
    for n in ("narration_v3.txt", "narration.txt"):
        matches = list(vdir.rglob(n))
        if matches:
            txt = matches[0].read_text(encoding="utf-8", errors="replace")
            tail = txt[-1200:]
            m = re.search(r"([^\n]*(?:tomorrow|next case|next file|coming next)[^\n]*)",
                          tail, re.IGNORECASE)
            if m:
                return re.sub(r"\s+", " ", m.group(1)).strip()[:220]
    return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?", help="caminho do projeto do canal")
    ap.add_argument("--channel", dest="channel")
    a = ap.parse_args()
    root = Path(a.channel or a.path or ".").expanduser()
    if not root.exists():
        print(f"[!] caminho nao existe: {root}")
        return

    print(f"# Contexto do canal\n\nProjeto: {root}\n")
    cal = find_calendar(root)
    print(f"Calendario: {cal.relative_to(root) if cal else 'NAO ENCONTRADO'}")

    # arquivos de contexto
    ctx = []
    for pat in ("BRANDING*", "REGRA_METADATA*", "PIPELINE*", "TEMPLATE_ROTEIRO*",
                "PROTOCOLO*", "CHECKLIST*", "FOCUS*"):
        ctx += [p for p in root.rglob(pat)][:1]
    if ctx:
        print("Contexto encontrado:")
        for p in sorted(set(ctx)):
            print(f"  - {p.relative_to(root)}")

    vids = video_dirs(root)
    print(f"\nVideos: {len(vids)}\n")
    print(f"{'video':<26} {'roteiro':<7} {'tease':<5} {'imgs':<4} {'audio':<5} {'final':<5} {'thumb':<5} {'pacote':<6}")
    for v in vids:
        s = state(v)
        mk = lambda b: "ok" if b else "-"
        print(f"{v.name:<26} {mk(s['roteiro']):<7} {mk(s['tease']):<5} {mk(s['imagens']):<4} "
              f"{mk(s['audio']):<5} {mk(s['final']):<5} {mk(s['thumbs']):<5} {mk(s['pacote']):<6}")

    # corrente de teaser
    print("\n## Corrente de teaser (o que cada video anuncia no fim)")
    any_tease = False
    for v in vids:
        t = teaser_line(v)
        if t:
            any_tease = True
            print(f"  {v.name} -> {t}")
    if not any_tease:
        print("  (nenhuma frase de 'tomorrow/next' encontrada nos roteiros)")

    # proximo a produzir
    pend = [v.name for v in vids if not state(v)["final"]]
    print("\n## Proximos a produzir (sem final)")
    print("  " + (", ".join(pend[:15]) if pend else "todos produzidos"))
    print("\n[!] REGRA DA CORRENTE: mudar a ORDEM dos casos exige regerar o")
    print("    outro/teaser do video anterior (que ja cita o caso seguinte) e o tease.txt.")


if __name__ == "__main__":
    main()
