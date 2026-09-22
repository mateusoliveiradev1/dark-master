#!/usr/bin/env python3
"""new_video.py — cria a pasta padrao de um video novo.

Uso:
  python scripts/new_video.py 27 "Hoffa" HEISTS --root "C:/.../canal dark1"
  python scripts/new_video.py 03 "D.B. Cooper" HEISTS --root "<canal>" --style truecrime-cfd

Cria:
  <root>/videoNN/{01_roteiro,02_audio,03_imagens,04_video_final}
  01_roteiro/narration_v3.txt     (cabecalho + placeholder)
  01_roteiro/TEMPLATE.txt         (copiado de 00_CANAL/TEMPLATE_ROTEIRO*.txt, se existir)
  01_roteiro/tease.txt            (placeholder)
  03_imagens/PROMPTS.md           (esqueleto via prompt_builder, se disponivel)
  youtube_package.txt             (template de publicacao)
"""
import argparse
import re
import shutil
from pathlib import Path

SUBS = ["01_roteiro", "02_audio", "03_imagens", "04_video_final"]

PACKAGE_TMPL = """# {title}
TITULO (40-60 chars, keyword nas 3 primeiras):
1.
2.
3.

DESCRICAO (5 blocos: hook 150 chars | expansao | chapters | fontes+disclaimer IA | CTA+hashtags)
B1:
B2:
B3 CHAPTERS:
B4 FONTES:
B5 CTA:

TAGS (8-12):
THUMB L1 / L2 / SUB:
SHORT (title + desc + pinned):
"""


def find_template(root: Path):
    for pat in ("TEMPLATE_ROTEIRO*.txt", "TEMPLATE_ROTEIRO*.md"):
        for p in (root / "00_CANAL").glob(pat) if (root / "00_CANAL").exists() else []:
            return p
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("number")
    ap.add_argument("case")
    ap.add_argument("series", nargs="?", default="")
    ap.add_argument("--root", required=True)
    ap.add_argument("--style", default="truecrime-cfd")
    a = ap.parse_args()

    root = Path(a.root).expanduser()
    root.mkdir(parents=True, exist_ok=True)
    num = re.sub(r"\D", "", a.number).zfill(2) if re.sub(r"\D", "", a.number) else a.number
    vid = root / f"video{num}"
    if vid.exists():
        print(f"[!] ja existe: {vid}")
    for s in SUBS:
        (vid / s).mkdir(parents=True, exist_ok=True)

    case = a.case.strip()
    title = f"video{num} - {case}" + (f" ({a.series})" if a.series else "")

    # roteiro
    rot = vid / "01_roteiro" / "narration_v3.txt"
    if not rot.exists():
        rot.write_text(
            f"# {title}\n# Roteiro (blocos: HOOK, CONTEXTO, PRESSAO, O DIA, INVESTIGACAO, "
            f"FAMILIA, TEORIAS, CHAVES+OUTRO+TEASER)\n# Preencha um paragrafo por bloco de TTS.\n\n",
            encoding="utf-8")
    # template
    tmpl = find_template(root)
    if tmpl:
        shutil.copy(tmpl, vid / "01_roteiro" / "TEMPLATE.txt")
    # tease
    tease = vid / "01_roteiro" / "tease.txt"
    if not tease.exists():
        tease.write_text("TEASE-A | para NN | \nTEASE-B | para NN | \nCTA | especifico | \n", encoding="utf-8")
    # pacote
    pkg = vid / "youtube_package.txt"
    if not pkg.exists():
        pkg.write_text(PACKAGE_TMPL.format(title=title), encoding="utf-8")
    # prompts (via prompt_builder, se existir)
    pb = Path(__file__).resolve().parent / "prompt_builder.py"
    prompts = vid / "03_imagens" / "PROMPTS.md"
    if pb.exists() and not prompts.exists():
        import subprocess, sys
        subprocess.run([sys.executable, str(pb), "--style", a.style, "--count", "0",
                        "--title", title, "--out", str(prompts)], capture_output=True, text=True)

    print(f"[OK] criado: {vid}")
    for s in SUBS:
        print(f"     {s}/")
    print("     youtube_package.txt")
    print("\nProximos passos:")
    print(f"  1. escreva o roteiro em 01_roteiro/narration_v3.txt")
    print(f"  2. gere/complete os prompts: python scripts/prompt_builder.py --style {a.style} --scenes cenas.txt --out \"{prompts}\"")
    print(f"  3. gere as imagens e valide: python scripts/image_audit.py \"{vid/'03_imagens'}\" --sheet")


if __name__ == "__main__":
    main()
