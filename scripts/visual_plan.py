import argparse
import json
import re
import sys
from pathlib import Path

SCENE_TYPES = {
    "HOOK": "forensic-reveal",
    "COLD OPEN": "forensic-reveal",
    "CONTEXTO": "location-sequence",
    "CONTEXT": "location-sequence",
    "PERICIA": "evidence-focus",
    "EVIDENCIAS": "evidence-focus",
    "EVIDÊNCIAS": "evidence-focus",
    "INVESTIGACAO": "investigation-board",
    "INVESTIGAÇÃO": "investigation-board",
    "LINHA DO TEMPO": "timeline-build",
    "CRONOLOGIA": "timeline-build",
    "TEORIAS": "hypothesis-comparator",
    "TEORIA": "hypothesis-comparator",
    "LAUDO": "document-dive",
    "FAMILIA": "negative-space-beat",
    "FAMÍLIA": "negative-space-beat",
    "CHAVES": "archive-end-card",
    "TEASER": "negative-space-beat",
}

DEFAULT_VISUAL = {
    "channel": "new-channel",
    "version": 2,
    "identity": {"mood": ["documentary", "investigative", "restrained"], "tone": ["calm", "precise"]},
    "palette": {"background": "#0A0A0C", "surface": "#17171B", "text": "#F5F5F4", "muted": "#A1A1AA", "accent": "#B91C1C", "evidence": "#EBB41E"},
    "typography": {"heading": "Bebas Neue", "body": "Inter"},
    "safeAreas": {"long": {"action": [0.05, 0.05, 0.9, 0.78], "captions": [0.06, 0.78, 0.88, 0.16], "watermark": [0.88, 0.04, 0.08, 0.08]}, "short": {"action": [0.1, 0.1, 0.8, 0.72], "captions": [0.08, 0.78, 0.84, 0.16], "watermark": [0.84, 0.04, 0.1, 0.08]}},
    "image": {"suffix": "dark cinematic documentary illustration, desaturated cold tones, deep blacks, subtle red accent, volumetric fog, no text, no watermark, no blood, no gore, no real face, silhouettes from behind, 16:9", "negativeGuards": ["no gore", "no blood", "no body", "no readable text", "no signage", "no invented logo", "no watermark", "no identifiable real person"]},
    "motion": {"intensity": "controlled", "defaultTransition": "cut-or-dissolve-by-meaning", "forbid": ["generic-slideshow", "image-plus-fade-plus-zoom", "static-frame", "unintentional-parallax"]},
    "qa": {"minimumScore": 92, "requiredVisualChanges": [2, 4], "forbid": ["crop-ruined", "text-outside-safe-area", "caption-overlap", "untraceable-asset", "static-scene"]},
}

DEFAULT_STATES = [
    {"id": "entry", "timeRange": [0, 0.15], "intent": "entry", "visibleLayers": ["background"], "motion": "slow-spatial-entry"},
    {"id": "establish", "timeRange": [0.15, 0.4], "intent": "establishment", "visibleLayers": ["background", "subject"], "motion": "drift-with-purpose"},
    {"id": "focus", "timeRange": [0.4, 0.7], "intent": "information", "visibleLayers": ["background", "subject", "evidence-marker"], "motion": "controlled-crop"},
    {"id": "emphasis", "timeRange": [0.7, 0.9], "intent": "emphasis", "visibleLayers": ["background", "subject", "annotation"], "motion": "detail-reveal"},
    {"id": "exit", "timeRange": [0.9, 1], "intent": "exit", "visibleLayers": ["subject", "annotation"], "motion": "hold-and-transition"},
]


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_visual(visual_path=None):
    if visual_path and Path(visual_path).exists():
        return read_json(visual_path)
    return DEFAULT_VISUAL


def block_type(beat):
    normalized = str(beat or "").upper()
    for key, value in SCENE_TYPES.items():
        if key in normalized:
            return value
    return "forensic-reveal"


def default_shot(block, index, claims, visual):
    block_id = str(block.get("id") or f"scene-{index:03d}")
    beat = str(block.get("beat") or "HOOK")
    claim_ids = [str(value) for value in (block.get("claim_ids") or block.get("claimIds") or [])]
    available_claims = {str(claim.get("id")): claim for claim in claims if isinstance(claim, dict) and claim.get("id")}
    selected_claims = [available_claims[value] for value in claim_ids if value in available_claims]
    purpose = str(block.get("question") or block.get("purpose") or "Mostrar uma mudança de estado")
    state_change = str(block.get("state_change") or block.get("stateChange") or "A informação reorganiza a leitura")
    image_suffix = visual.get("image", {}).get("suffix", DEFAULT_VISUAL["image"]["suffix"])
    return {
        "shotId": f"S-{index:03d}",
        "promptId": f"P-{index:03d}",
        "sourceBlockIds": [block_id],
        "claimIds": claim_ids,
        "editorial": {"beat": beat, "function": block_type(beat), "purpose": purpose, "stateChange": state_change},
        "visual": {"sceneType": block_type(beat), "visualRole": block_type(beat), "subject": "[preencher]", "action": state_change, "location": "[preencher]", "timeOfDay": "[preencher]", "camera": "[preencher]", "grade": "deep blacks, low saturation, fine film grain", "headline": purpose, "body": "", "overlayRole": "evidence marker or metadata only"},
        "assets": {"primary": [], "supporting": [], "excluded": []},
        "continuity": {"palette": visual.get("palette", {}), "typography": visual.get("typography", {}), "series": str(block.get("series") or "default")},
        "states": DEFAULT_STATES,
        "cropPolicy": {"masterAspect": "16:9", "long": {"focalPoint": [0.5, 0.5], "captionAvoid": visual.get("safeAreas", DEFAULT_VISUAL["safeAreas"])["long"]["captions"]}, "short": {"focalPoint": [0.5, 0.42], "dedicatedReframeRequired": True}},
        "prompt": {"full": "", "negativeGuards": list(visual.get("image", {}).get("negativeGuards", DEFAULT_VISUAL["image"]["negativeGuards"])), "expectedOutput": "16:9 master with caption-safe lower band and watermark-safe corner"},
        "selectedClaims": selected_claims,
        "status": "needs-art-direction",
    }


def load_specs(path):
    data = read_json(path)
    if isinstance(data, dict):
        specs = data.get("shots") or data.get("shotSpecs") or []
    else:
        specs = data
    return specs if isinstance(specs, list) else []


def build_shot_specs(episode, visual_path=None):
    episode = Path(episode)
    script_dir = episode / "01_roteiro"
    map_data = read_json(script_dir / "ROTEIRO_MAP.json")
    claims = read_json(episode / "01_roteiro" / "CLAIMS.json") if (episode / "01_roteiro" / "CLAIMS.json").exists() else {}
    blocks = map_data.get("blocks", []) if isinstance(map_data, dict) else []
    visual = load_visual(visual_path)
    return [default_shot(block, index, claims.get("claims", []) if isinstance(claims, dict) else [], visual) for index, block in enumerate(blocks, 1)]


def prompt_from_shot(shot, visual):
    prompt = str(shot.get("prompt", {}).get("full") or "").strip()
    if prompt:
        return prompt
    visual_spec = shot.get("visual", {})
    parts = [
        shot.get("editorial", {}).get("beat", "DOCUMENTARY"),
        visual_spec.get("subject", "a concrete documentary subject"),
        visual_spec.get("action", "a visible state change"),
        visual_spec.get("location", "a specific place and era"),
        visual_spec.get("timeOfDay", "the correct time of day"),
        visual_spec.get("camera", "a purposeful documentary camera"),
        visual_spec.get("grade", "a coherent restrained grade"),
    ]
    return ", ".join(str(value) for value in parts if value and not str(value).startswith("[")) + f", {visual.get('image', {}).get('suffix', DEFAULT_VISUAL['image']['suffix'])}"


def validate_shots(shots, visual):
    errors = []
    ids = set()
    prompt_ids = set()
    for shot in shots:
        if not isinstance(shot, dict):
            errors.append("shot_not_object")
            continue
        shot_id = str(shot.get("shotId") or "")
        prompt_id = str(shot.get("promptId") or "")
        if not shot_id or shot_id in ids:
            errors.append(f"invalid_shot_id:{shot_id}")
        if not prompt_id or prompt_id in prompt_ids:
            errors.append(f"invalid_prompt_id:{prompt_id}")
        ids.add(shot_id)
        prompt_ids.add(prompt_id)
        if not shot.get("editorial", {}).get("purpose"):
            errors.append(f"missing_purpose:{shot_id}")
        if not shot.get("states"):
            errors.append(f"missing_states:{shot_id}")
        if not shot.get("cropPolicy"):
            errors.append(f"missing_crop_policy:{shot_id}")
        if not shot.get("prompt", {}).get("negativeGuards"):
            errors.append(f"missing_negative_guards:{shot_id}")
    return errors


def compile_prompt_plan(episode, visual_path=None, specs_path=None):
    episode = Path(episode)
    script_dir = episode / "01_roteiro"
    visual = load_visual(visual_path)
    specs_file = Path(specs_path) if specs_path else script_dir / "SHOT_SPECS.json"
    if specs_file.exists():
        shots = load_specs(specs_file)
    else:
        shots = build_shot_specs(episode, visual_path)
    records = []
    for shot in shots:
        prompt = prompt_from_shot(shot, visual)
        shot["prompt"] = {**shot.get("prompt", {}), "full": prompt}
        records.append({"promptId": shot.get("promptId"), "shotId": shot.get("shotId"), "sourceBlockIds": shot.get("sourceBlockIds", []), "claimIds": shot.get("claimIds", []), "prompt": prompt, "negativeGuards": shot.get("prompt", {}).get("negativeGuards", []), "expectedOutput": shot.get("prompt", {}).get("expectedOutput", "16:9"), "status": shot.get("status", "planned")})
    errors = validate_shots(shots, visual)
    if not records:
        errors.append("shots_missing")
    plan = {"version": 1, "episode": episode.name, "channel": visual.get("channel", episode.parent.name), "status": "NEEDS_ART_DIRECTION" if errors or any(record["status"] != "ready" for record in records) else "PROMPTS_READY", "visualVersion": visual.get("version", 2), "shots": shots, "prompts": records, "errors": errors}
    write_json(script_dir / "PROMPT_PLAN.json", plan)
    lines = ["# PROMPTS DE IMAGEM", "", f"# Visual: {visual.get('channel', episode.parent.name)}", "# Estado: planejado; cada linha exige QA humana antes de gerar voz.", ""]
    for record in records:
        lines.append(f"## {record['promptId']} — {record['shotId']}")
        lines.append(f"BLOCKS: {', '.join(record['sourceBlockIds']) or '-'}")
        lines.append(f"CLAIMS: {', '.join(record['claimIds']) or '-'}")
        lines.append(record["prompt"])
        lines.append("NEGATIVE GUARDS: " + ", ".join(record["negativeGuards"]))
        lines.append("")
    (episode / "03_imagens" / "PROMPTS.md").parent.mkdir(parents=True, exist_ok=True)
    (episode / "03_imagens" / "PROMPTS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return plan


def init_artifacts(episode, visual_path=None):
    episode = Path(episode)
    script_dir = episode / "01_roteiro"
    visual = load_visual(visual_path)
    specs_path = script_dir / "SHOT_SPECS.json"
    if not specs_path.exists():
        write_json(specs_path, {"version": 1, "episode": episode.name, "status": "NEEDS_ART_DIRECTION", "shots": build_shot_specs(episode, visual_path)})
    bible_path = script_dir / "VISUAL_BIBLE.json"
    if not bible_path.exists():
        write_json(bible_path, visual)
    return compile_prompt_plan(episode, visual_path, specs_path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["init", "compile", "validate"])
    parser.add_argument("--episode", required=True)
    parser.add_argument("--visual")
    parser.add_argument("--specs")
    args = parser.parse_args()
    if args.command == "init":
        result = init_artifacts(args.episode, args.visual)
    elif args.command == "compile":
        result = compile_prompt_plan(args.episode, args.visual, args.specs)
    else:
        result = compile_prompt_plan(args.episode, args.visual, args.specs)
    print(json.dumps({"status": result["status"], "episode": result["episode"], "prompts": len(result["prompts"]), "errors": result["errors"]}, ensure_ascii=False))
    return 0 if result["status"] == "PROMPTS_READY" else 1


if __name__ == "__main__":
    sys.exit(main())
