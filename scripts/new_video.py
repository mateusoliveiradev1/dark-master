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
import json
import os
import re
import shutil
from pathlib import Path

SUBS = ["01_roteiro", "02_audio", "03_imagens", "04_video_final"]

PLAYBOOKS = Path(os.environ.get(
    "DARK_MASTER_PLAYBOOKS",
    str(Path.home() / ".config" / "opencode" / "skills" / "dark-master" / "playbooks")))


def resolve_playbook(channel):
    """--channel <nome|pasta> -> pasta do playbook (contrato voice/motion/style.json)."""
    if not channel:
        return None
    p = Path(channel).expanduser()
    if p.is_dir():
        return p
    p = PLAYBOOKS / channel
    if p.is_dir():
        return p
    print(f"[AVISO] canal '{channel}' nao encontrado em {PLAYBOOKS} — seguindo sem contrato de canal.")
    return None


def channel_suffix(pb):
    """Sufixo travado do canal (style.json > image_suffix)."""
    if not pb:
        return None
    try:
        d = json.loads((pb / "style.json").read_text(encoding="utf-8"))
        return d.get("image_suffix")
    except (OSError, ValueError):
        return None

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
    ap.add_argument("--channel", help="playbook do canal (usa style.json/image_suffix no PROMPTS.md)")
    a = ap.parse_args()

    pb_dir = resolve_playbook(a.channel)
    suffix = channel_suffix(pb_dir)
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
    # template (nao sobrescrever)
    tmpl = find_template(root)
    if tmpl and not (vid / "01_roteiro" / "TEMPLATE.txt").exists():
        shutil.copy(tmpl, vid / "01_roteiro" / "TEMPLATE.txt")
    # tease (nao sobrescrever)
    tease = vid / "01_roteiro" / "tease.txt"
    if not tease.exists():
        tease.write_text("TEASE-A | para NN | \nTEASE-B | para NN | \nCTA | especifico | \n", encoding="utf-8")
    # pesquisa/fontes (nao sobrescrever) — camadas [FATO]/[REPORTADO]/[LENDA]
    pesq = vid / "01_roteiro" / "PESQUISA_FONTE.md"
    if not pesq.exists():
        pesq.write_text(
            f"# PESQUISA/FONTES — {case}\n\n"
            "> Uma camada por linha: [FATO] / [REPORTADO] / [LENDA]. 2+ fontes por caso. Nada sem fonte.\n\n"
            "- [FATO] \n- [REPORTADO] \n- [LEGENDA/LENDA a evitar] \n- Fontes (links): \n",
            encoding="utf-8")
    # pacote
    pkg = vid / "youtube_package.txt"
    if not pkg.exists():
        pkg.write_text(PACKAGE_TMPL.format(title=title), encoding="utf-8")
    # prompts (via prompt_builder, se existir)
    pb = Path(__file__).resolve().parent / "prompt_builder.py"
    prompts = vid / "03_imagens" / "PROMPTS.md"
    if pb.exists() and not prompts.exists():
        import subprocess, sys
        cmd = [sys.executable, str(pb), "--style", a.style, "--count", "0",
               "--title", title, "--out", str(prompts)]
        if suffix:
            cmd += ["--suffix", suffix]
        subprocess.run(cmd, capture_output=True, text=True)

    print(f"[OK] criado: {vid}" + (f" (canal: {a.channel})" if a.channel else ""))
    for s in SUBS:
        print(f"     {s}/")
    print("     youtube_package.txt")
    print("\nProximos passos (scaffold completo = pastas + stubs + PROMPTS + package + voz):")
    print("  1. escreva o roteiro em 01_roteiro/narration_v3.txt e as fontes em PESQUISA_FONTE.md")
    print(f"  2. complete os prompts por PORTE (header ja com o sufixo do canal): {prompts}")
    print(f"  3. voz liberada (so depende da narracao); MOTION so com GATE 100% das imagens")
    print(f"  4. gere as imagens e valide: python scripts/image_audit.py \"{vid/'03_imagens'}\" --sheet")


if __name__ == "__main__":
    main()
