#!/usr/bin/env python3
"""prompt_builder.py — gera PROMPTS.md perfeitos (consistentes) para as imagens.

Uso:
  # esqueleto com N imagens distribuidas pelos beats (para preencher as cenas)
  python scripts/prompt_builder.py --style truecrime-cfd --count 34 --title "video27 Hoffa" --out PROMPTS.md

  # a partir das cenas (uma por linha; opcional "BEAT | descricao")
  python scripts/prompt_builder.py --style photoreal --scenes cenas.txt --out PROMPTS.md

  # (opcional) renderizar de verdade via Pollinations
  python scripts/prompt_builder.py --style truecrime-cfd --scenes cenas.txt --render --outdir "<videoNN>/03_imagens"

O estilo (sufixo) e travado por preset -> consistencia visual. Descricoes com termos
proibidos (gore, sangue, etc.) sao bloqueadas.
"""
import argparse
import json
import re
import urllib.parse
import urllib.request
from pathlib import Path

PRESETS = {
    "truecrime-cfd": "cinematic documentary still, moody, desaturated, film grain, volumetric light, ultra detailed, no text, no watermark, no gore, no real face, 16:9",
    "photoreal": "photoreal cinematic film still, deep blacks, film grain, desaturated cold with one warm practical light, dusk or night, no text, no signage, no letters, no readable paper, no watermark, no people close-up, faces never visible backs only, no border, no vignette frame, no gore, no real photo, 16:9",
    "financial": "photorealistic documentary reconstruction, natural proportions, plausible lighting, no teal-orange, no lens flare, documentary photo language, believable lens, no text, no watermark, 16:9",
    "forense": "dark cinematic forensic illustration, desaturated cold tones, deep blacks, subtle red accent, volumetric fog, no text, no watermark, no blood, no gore, no real face, silhouettes from behind, 16:9",
    "dark-history": "moody dark history documentary still, painterly muted palette, volumetric haze, film grain, no text, no watermark, no gore, 16:9",
}

BEATS = ["ESTABELECEDOR", "COTIDIANO", "PRESSAO", "O DIA", "DESCOBERTA", "BUSCA",
         "PISTA", "PERICIA", "INVESTIGACAO", "FAMILIA", "MIDIA",
         "TEORIA 1", "TEORIA 2", "TEORIA 3", "LAUDO", "LEGADO", "TEASER"]

BEAT_HINT = {
    "ESTABELECEDOR": "vista ampla do lugar, epoca e clima",
    "COTIDIANO": "rotina das pessoas (de costas), ambiente domestico",
    "PRESSAO": "tensao antes do fato (dividas, brigas, telefonema)",
    "O DIA": "a cena-chave, sem gore — foco em objetos/ambiente",
    "DESCOBERTA": "o que foi encontrado, em plano de detalhe",
    "BUSCA": "equipes/busca em campo, silhuetas ao longe",
    "PISTA": "evidencia fisica isolada (objeto, marca, documento sem texto)",
    "PERICIA": "laboratorio/pericia, luvas, equipamento",
    "INVESTIGACAO": "mesa de investigacao, mapa, arquivo, lampada",
    "FAMILIA": "retrato respeitoso — objetos, retrato sem rosto, cadeira vazia",
    "MIDIA": "jornal/manchete sem texto legivel, radio, TV desligada",
    "TEORIA 1": "cena simbolica da teoria 1",
    "TEORIA 2": "cena simbolica da teoria 2",
    "TEORIA 3": "cena simbolica da teoria 3",
    "LAUDO": "documento/laudo sem texto legivel, selo, lupa",
    "LEGADO": "memorial, lugar hoje, homenagem sobria",
    "TEASER": "gancho do proximo caso (visual forte, sem entregar)",
}

FORBIDDEN = ["blood", "sangue", "gore", "corpse", "dead body", "dismember", "mutilat",
             "wound", "guts", "torture", "bloody"]


def load_scenes(path):
    out = []
    for line in Path(path).read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "|" in line:
            beat, desc = line.split("|", 1)
            out.append((beat.strip().upper(), desc.strip()))
        else:
            out.append((None, line))
    return out


def check(desc):
    if desc.strip().startswith("[preencher:"):
        return []
    low = desc.lower()
    return [w for w in FORBIDDEN if w in low]


def render(prompt, out_path):
    url = ("https://image.pollinations.ai/prompt/" + urllib.parse.quote(prompt)
           + "?width=1920&height=1080&nologo=true&model=flux")
    try:
        data = urllib.request.urlopen(url, timeout=120).read()
        if len(data) > 10000:
            Path(out_path).write_bytes(data)
            return True
    except Exception as e:  # noqa
        print(f"    [!] falha ao renderizar {out_path}: {e}")
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--style", default="truecrime-cfd", choices=list(PRESETS))
    ap.add_argument("--suffix", help="sufixo do canal (playbooks/<canal>/style.json > image_suffix); sobrepoe o preset")
    ap.add_argument("--scenes")
    ap.add_argument("--count", type=int, default=0)
    ap.add_argument("--title", default="")
    ap.add_argument("--out", required=True)
    ap.add_argument("--episode")
    ap.add_argument("--visual")
    ap.add_argument("--specs")
    ap.add_argument("--render", action="store_true")
    ap.add_argument("--outdir")
    a = ap.parse_args()

    if a.episode:
        from visual_plan import compile_prompt_plan
        result = compile_prompt_plan(a.episode, a.visual, a.specs)
        print(json.dumps({"status": result["status"], "prompts": len(result["prompts"]), "plan": str(Path(a.episode) / "01_roteiro" / "PROMPT_PLAN.json")}, ensure_ascii=False))
        return 0 if result["status"] == "PROMPTS_READY" else 1

    suffix = a.suffix or PRESETS[a.style]
    style_label = f"{a.style} + sufixo do canal" if a.suffix else a.style

    # monta a lista (beat, descricao)
    items = []
    if a.scenes:
        items = load_scenes(a.scenes)
    elif a.count > 0:
        for i in range(a.count):
            beat = BEATS[i % len(BEATS)]
            items.append((beat, f"[preencher: {BEAT_HINT.get(beat, beat)}]"))
    # se sem scenes e sem count -> cabecalho so (usado pelo new_video)

    header = [
        f"# {a.title or 'PROMPTS'} ",
        f"# Estilo travado ({style_label}):",
        f'# "{suffix}"',
        "# Nomes exatos 01.jpg ... NN.jpg. Cole a descricao + sufixo no seu gerador.",
        "# Guarda-corpos: sem gore, sem rosto real, sem texto legivel, sem watermark, sem anacronismo.",
        "",
    ]
    lines = list(header)
    blocked = 0
    for i, (beat, desc) in enumerate(items, 1):
        bad = check(desc)
        if bad:
            blocked += 1
            desc = desc + f"  [BLOQUEADO: remover {bad}]"
        label = f"{beat}: " if beat else ""
        lines.append(f"{i:02d}.jpg — {label}{desc}, {suffix}")

    out = Path(a.out).expanduser()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[OK] {len(items)} prompt(s) -> {out}")
    if blocked:
        print(f"[!] {blocked} descricao(oes) com termos proibidos (marcadas).")

    if a.render and a.outdir and items:
        od = Path(a.outdir).expanduser(); od.mkdir(parents=True, exist_ok=True)
        ok = 0
        for i, (beat, desc) in enumerate(items, 1):
            if check(desc):
                continue
            p = f"{desc}, {suffix}"
            dst = od / f"{i:02d}.jpg"
            print(f"  render {dst.name} ...")
            if render(p, dst):
                ok += 1
        print(f"[OK] {ok}/{len(items)} imagens renderizadas em {od}")
        print("  valide com: python scripts/image_audit.py \"%s\" --sheet" % od)


if __name__ == "__main__":
    main()
