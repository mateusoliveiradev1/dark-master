#!/usr/bin/env python3
import argparse
import hashlib
import json
import re
import sys
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

BEATS = ["ESTABELECEDOR", "COTIDIANO", "PRESSAO", "O DIA", "DESCOBERTA", "BUSCA", "PISTA", "PERICIA", "INVESTIGACAO", "FAMILIA", "MIDIA", "TEORIA 1", "TEORIA 2", "TEORIA 3", "LAUDO", "LEGADO", "TEASER"]

BEAT_HINT = {
    "ESTABELECEDOR": "local, época e clima",
    "COTIDIANO": "rotina das pessoas ao fundo",
    "PRESSAO": "tensão antes do fato",
    "O DIA": "momento central sem violência gráfica",
    "DESCOBERTA": "descoberta material em plano de detalhe",
    "BUSCA": "equipes vistas à distância",
    "PISTA": "evidência física isolada",
    "PERICIA": "laboratório e equipe sem rosto identificável",
    "INVESTIGACAO": "mesa de investigação e relações",
    "FAMILIA": "objetos e ausência respeitosa",
    "MIDIA": "mídia sem texto legível",
    "TEORIA 1": "hipótese um em imagem simbólica",
    "TEORIA 2": "hipótese dois em imagem simbólica",
    "TEORIA 3": "hipótese três em imagem simbólica",
    "LAUDO": "documento sem texto legível",
    "LEGADO": "memorial ou lugar atual",
    "TEASER": "gancho visual do próximo caso",
}

FORBIDDEN = ["blood", "sangue", "gore", "corpse", "dead body", "dismember", "mutilat", "wound", "guts", "torture", "bloody"]
NEGATION_RE = re.compile(r"(?:\bno\b|\bsem\b|\bwithout\b|\bnever\b)\s*$", re.IGNORECASE)


def load_scenes(path):
    scenes = []
    for line in Path(path).read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "|" in line:
            beat, description = line.split("|", 1)
            scenes.append((beat.strip().upper(), description.strip()))
        else:
            scenes.append((None, line))
    return scenes


def check(description):
    if description.strip().startswith("[preencher:"):
        return []
    lowered = description.lower()
    found = []
    for term in FORBIDDEN:
        for match in re.finditer(re.escape(term), lowered):
            prefix = lowered[max(0, match.start() - 20):match.start()]
            if not NEGATION_RE.search(prefix):
                found.append(term)
                break
    return sorted(set(found))


def draft_identity(beat, description):
    payload = f"{beat or 'UNTITLED'}\n{description}".encode("utf-8")
    return f"DRAFT-PROMPT-{hashlib.sha256(payload).hexdigest()[:12].upper()}"


def render(prompt, out_path):
    url = "https://image.pollinations.ai/prompt/" + urllib.parse.quote(prompt) + "?width=1920&height=1080&nologo=true&model=flux"
    try:
        data = urllib.request.urlopen(url, timeout=120).read()
        if len(data) > 10000:
            Path(out_path).write_bytes(data)
            return True
    except Exception as exc:
        print(f"[!] falha ao renderizar {out_path}: {exc}")
    return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--style", default="truecrime-cfd", choices=list(PRESETS))
    parser.add_argument("--suffix")
    parser.add_argument("--scenes")
    parser.add_argument("--count", type=int, default=0)
    parser.add_argument("--title", default="")
    parser.add_argument("--out", required=True)
    parser.add_argument("--episode")
    parser.add_argument("--visual")
    parser.add_argument("--specs")
    parser.add_argument("--render", action="store_true")
    parser.add_argument("--outdir")
    args = parser.parse_args()

    if args.episode:
        from visual_plan import compile_prompt_plan
        result = compile_prompt_plan(args.episode, args.visual, args.specs)
        print(json.dumps({"status": result["status"], "prompts": len(result["prompts"]), "plan": str(Path(args.episode) / "01_roteiro" / "PROMPT_PLAN.json")}, ensure_ascii=False))
        return 0 if result["status"] == "PROMPTS_READY" else 1

    suffix = args.suffix or PRESETS[args.style]
    items = []
    if args.scenes:
        items = load_scenes(args.scenes)
    elif args.count > 0:
        for index in range(args.count):
            beat = BEATS[index % len(BEATS)]
            items.append((beat, f"[preencher: {BEAT_HINT.get(beat, beat)}]"))

    lines = [
        f"# {args.title or 'RASCUNHO DE PROMPTS'}",
        "MODE: DRAFT",
        f"STYLE: {args.suffix or args.style}",
        f"SUFFIX: {suffix}",
        "Production requires --episode and a complete research-backed PROMPT_PLAN.",
        "",
    ]
    blocked = 0
    contracts = []
    for beat, description in items:
        prompt_id = draft_identity(beat, description)
        bad = check(description)
        if bad:
            blocked += 1
        contracts.append({"promptId": prompt_id, "beat": beat, "description": description, "negativeGuards": bad, "suffix": suffix})
        label = f"{beat}: " if beat else ""
        lines.append(f"{prompt_id} — {label}{description}, {suffix}")
        if bad:
            lines.append(f"NEGATIVE GUARDS REQUIRED: {', '.join(bad)}")
    out = Path(args.out).expanduser()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"mode": "DRAFT", "status": "INCOMPLETE", "prompts": len(items), "out": str(out), "blocked": blocked}, ensure_ascii=False))

    if args.render and args.outdir and items:
        output_dir = Path(args.outdir).expanduser()
        output_dir.mkdir(parents=True, exist_ok=True)
        rendered = 0
        for contract in contracts:
            if contract["negativeGuards"]:
                continue
            prompt = f"{contract['description']}, {contract['suffix']}"
            destination = output_dir / f"{contract['promptId']}.jpg"
            if render(prompt, destination):
                rendered += 1
        print(json.dumps({"mode": "DRAFT", "rendered": rendered, "expected": len(items), "outdir": str(output_dir)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
