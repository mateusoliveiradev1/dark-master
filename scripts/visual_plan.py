import argparse
import hashlib
import json
import re
import sys
import unicodedata
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

REQUIRED_SCENE_FIELDS = (
    "shotId",
    "promptId",
    "sourceBlockIds",
    "claimIds",
    "sourceIds",
    "purpose",
    "question",
    "stateChange",
    "classification",
    "subject",
    "setting",
    "composition",
    "layers",
    "cropPolicy",
    "safeAreas",
    "negativeGuards",
    "continuity",
    "states",
)

RESEARCH_FILES = (
    "PESQUISA_BRIEF.md",
    "PESQUISA_FONTE.md",
    "CLAIMS.json",
    "LINHA_DO_TEMPO.md",
    "ROTEIRO_MAP.json",
)

PLACEHOLDER_TOKENS = (
    "[preencher",
    "a preencher",
    "<preencher",
    "{{",
    "{case}",
    "a definir",
    "(definir)",
    "a concrete documentary subject",
    "the correct time of day",
    "a purposeful documentary camera",
)

CLASSIFICATION_GUARDS = {
    "FATO": "documented reconstruction only; do not add unsupported factual details",
    "REPORTADO": "reported account; do not present disputed details as confirmed fact",
    "HIPOTESE": "hypothetical visualization; do not depict an accusation as fact",
    "LENDA": "legend visualization only; do not present the legend as evidence",
    "MIXED": "preserve each claim's documented certainty; never merge fact, report and hypothesis",
}

MOTION_PROFILES = {
    "forensic-reveal": ("detail-reveal", 2),
    "evidence-focus": ("controlled-crop", 2),
    "investigation-board": ("track-left", 2),
    "timeline-build": ("line-drawing", 2),
    "hypothesis-comparator": ("track-right", 3),
    "document-dive": ("push-in", 1),
    "negative-space-beat": ("hold-and-transition", 1),
    "archive-end-card": ("pull-out", 1),
    "location-sequence": ("drift-with-purpose", 1),
}


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def compact(value, limit=None):
    text = " ".join(str(value or "").split())
    if limit and len(text) > limit:
        return text[: limit - 1].rstrip() + "…"
    return text


def normalize_text(value):
    normalized = unicodedata.normalize("NFD", str(value or "").upper())
    return "".join(character for character in normalized if not unicodedata.combining(character))


def slug(value):
    cleaned = re.sub(r"[^A-Z0-9]+", "-", normalize_text(value)).strip("-")
    return cleaned or "UNSPECIFIED"


def unique(values):
    seen = set()
    result = []
    for value in values:
        if value is None:
            continue
        text = str(value).strip()
        if text and text not in seen:
            seen.add(text)
            result.append(text)
    return result


def contains_placeholder(value):
    if isinstance(value, dict):
        return any(contains_placeholder(item) for item in value.values())
    if isinstance(value, list):
        return any(contains_placeholder(item) for item in value)
    lowered = str(value or "").lower()
    return any(token in lowered for token in PLACEHOLDER_TOKENS) or bool(re.search(r"\b(?:placeholder|tbd|todo)\b", lowered))


def clean_value(value):
    text = compact(value)
    return "" if contains_placeholder(text) else text


def first_value(data, *names, default=""):
    if not isinstance(data, dict):
        return default
    for name in names:
        value = data.get(name)
        if value not in (None, "", []):
            return value
    return default


def as_list(value):
    if value in (None, ""):
        return []
    if isinstance(value, (list, tuple, set)):
        return unique(value)
    return [str(value)]


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def parse_table(text):
    rows = []
    headers = []
    for line in str(text or "").splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if not headers:
            if cells and normalize_text(cells[0]) in {"ID", "DATA", "FONTE"}:
                headers = [normalize_text(cell).lower() for cell in cells]
            continue
        if cells and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            continue
        if len(cells) == len(headers) and not contains_placeholder(" ".join(cells)):
            rows.append({header: clean_value(cell) for header, cell in zip(headers, cells)})
    return rows


def table_value(row, *names):
    for name in names:
        for key, value in row.items():
            if normalize_text(key) == normalize_text(name):
                return value
    return ""


def source_ids_in(value):
    return unique(re.findall(r"\bS\d+\b", str(value or ""), flags=re.IGNORECASE))


def source_label(row):
    return table_value(row, "Fonte", "Source") or next(iter(row.values()), "")


def timeline_label(row):
    date = table_value(row, "Data", "data")
    fact = table_value(row, "Fato", "Evento", "fato")
    return " — ".join(value for value in (date, fact) if value)


def meaningful_text(text):
    cleaned = compact(text)
    return len(cleaned) >= 20 and not contains_placeholder(cleaned)


def extract_brief_phrase(text):
    for line in str(text or "").splitlines():
        if "pergunta central" in normalize_text(line):
            return compact(line.split(":", 1)[-1])
    for line in str(text or "").splitlines():
        candidate = compact(line)
        if meaningful_text(candidate) and not candidate.startswith("#") and not candidate.startswith("|"):
            return candidate
    return ""


def extract_case_name(map_data, brief, episode):
    for key in ("case_id", "case", "title", "episode_title"):
        value = clean_value(first_value(map_data, key))
        if value:
            return value
    for line in str(brief or "").splitlines():
        if line.startswith("# ") and "BRIEF DE PESQUISA" in normalize_text(line):
            return compact(re.split(r"[-—:]", line, maxsplit=1)[-1])
    return episode.name


def load_research(episode):
    episode = Path(episode)
    script_dir = episode / "01_roteiro"
    paths = {name: script_dir / name for name in RESEARCH_FILES}
    texts = {}
    for name, path in paths.items():
        if path.suffix == ".json":
            try:
                texts[name] = read_json(path) if path.exists() else {}
            except (OSError, ValueError):
                texts[name] = {}
        else:
            try:
                texts[name] = path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""
            except OSError:
                texts[name] = ""
    map_data = texts["ROTEIRO_MAP.json"] if isinstance(texts["ROTEIRO_MAP.json"], dict) else {}
    claims_data = texts["CLAIMS.json"] if isinstance(texts["CLAIMS.json"], dict) else {}
    claims = [claim for claim in claims_data.get("claims", []) if isinstance(claim, dict)]
    blocks = [block for block in map_data.get("blocks", []) if isinstance(block, dict)]
    sources = {}
    for row in parse_table(texts["PESQUISA_FONTE.md"]):
        source_id = table_value(row, "ID", "Source ID")
        if re.fullmatch(r"S\d+", source_id, flags=re.IGNORECASE):
            sources[source_id.upper()] = row
    timeline = [row for row in parse_table(texts["LINHA_DO_TEMPO.md"]) if timeline_label(row)]
    errors = []
    if not paths["ROTEIRO_MAP.json"].exists() or not blocks:
        errors.append("research_missing:ROTEIRO_MAP")
    if not meaningful_text(texts["PESQUISA_BRIEF.md"]):
        errors.append("research_missing:PESQUISA_BRIEF")
    if not sources:
        errors.append("research_missing:PESQUISA_FONTE")
    if not claims:
        errors.append("research_missing:CLAIMS")
    if not timeline:
        errors.append("research_missing:LINHA_DO_TEMPO")
    claim_index = {str(claim.get("id")): claim for claim in claims if clean_value(claim.get("id"))}
    source_index = set(sources)
    for claim_id, claim in sorted(claim_index.items()):
        claim_sources = {value.upper() for value in as_list(first_value(claim, "source_ids", "sourceIds"))}
        for source_id in sorted(claim_sources - source_index):
            errors.append(f"source_missing:{source_id}:{claim_id}")
    block_ids = []
    for index, block in enumerate(blocks, 1):
        block_id = clean_value(block.get("id")) or f"block-{index}"
        block_ids.append(block_id)
        for claim_id in as_list(first_value(block, "claim_ids", "claimIds")):
            if claim_id not in claim_index:
                errors.append(f"claim_missing:{claim_id}:{block_id}")
    if len(block_ids) != len(set(block_ids)):
        errors.append("duplicate_block_ids")
    brief = texts["PESQUISA_BRIEF.md"]
    case_name = extract_case_name(map_data, brief, episode)
    context = {
        "episode": episode,
        "scriptDir": script_dir,
        "paths": paths,
        "map": map_data,
        "blocks": blocks,
        "claims": claims,
        "claimIndex": claim_index,
        "sources": sources,
        "timeline": timeline,
        "brief": brief,
        "briefPhrase": extract_brief_phrase(brief),
        "caseName": case_name,
        "errors": sorted(set(errors)),
    }
    context["artifacts"] = {
        name: {"path": path.relative_to(episode).as_posix(), "sha256": sha256(path)}
        for name, path in paths.items()
        if path.exists()
    }
    return context


def load_visual(visual_path=None, episode=None):
    if visual_path and Path(visual_path).exists():
        return read_json(visual_path), True
    if episode:
        bible = Path(episode) / "01_roteiro" / "VISUAL_BIBLE.json"
        if bible.exists():
            return read_json(bible), True
    return DEFAULT_VISUAL, False


def block_type(beat):
    normalized = normalize_text(beat)
    for key, value in SCENE_TYPES.items():
        if normalize_text(key) in normalized:
            return value
    return "forensic-reveal"


def selected_claims(block, research):
    claim_ids = as_list(first_value(block, "claim_ids", "claimIds"))
    return [research["claimIndex"][claim_id] for claim_id in claim_ids if research and claim_id in research["claimIndex"]]


def selected_sources(block, claims):
    values = as_list(first_value(block, "source_ids", "sourceIds"))
    for claim in claims:
        values.extend(as_list(first_value(claim, "source_ids", "sourceIds")))
    return unique(value.upper() for value in values)


def classification_for(block, claims):
    explicit = clean_value(first_value(block, "classification", "classificacao"))
    if explicit:
        return explicit.upper()
    layers = {clean_value(claim.get("layer")).upper() for claim in claims}
    for layer in ("LENDA", "HIPOTESE", "HYPOTHESIS", "REPORTADO", "FATO"):
        if layer in layers:
            return "HIPOTESE" if layer == "HYPOTHESIS" else layer
    return "MIXED" if layers else ""


def continuity_for(block, visual, research, subject, classification):
    explicit = first_value(block, "continuity", default={})
    base = explicit if isinstance(explicit, dict) else {}
    timeline_values = [timeline_label(row) for row in research["timeline"][:3]] if research else []
    source_values = [source_label(row) for row in list(research["sources"].values())[:3]] if research else []
    era = clean_value(first_value(block, "era", "period", "periodo")) or compact(" | ".join(timeline_values))
    geography = clean_value(first_value(block, "geography", "location", "local")) or subject
    continuity = {
        "palette": base.get("palette", visual.get("palette", {})),
        "typography": base.get("typography", visual.get("typography", {})),
        "era": base.get("era", era),
        "geography": base.get("geography", geography),
        "recurringSubjects": base.get("recurringSubjects", [subject] if subject else []),
        "evidenceTreatment": base.get("evidenceTreatment", CLASSIFICATION_GUARDS.get(classification, CLASSIFICATION_GUARDS["MIXED"])),
        "sourceContext": base.get("sourceContext", unique(source_values)),
    }
    return {key: value for key, value in continuity.items() if value not in (None, "", [])}


def default_crop_policy(block, visual):
    explicit = first_value(block, "cropPolicy", "crop_policy", default={})
    if isinstance(explicit, dict) and explicit:
        return explicit
    long_safe = visual.get("safeAreas", DEFAULT_VISUAL["safeAreas"]).get("long", DEFAULT_VISUAL["safeAreas"]["long"])
    return {
        "masterAspect": "16:9",
        "long": {"focalPoint": [0.5, 0.5], "actionSafe": long_safe.get("action"), "captionAvoid": long_safe.get("captions")},
        "short": {"focalPoint": [0.5, 0.42], "actionSafe": visual.get("safeAreas", {}).get("short", {}).get("action"), "captionAvoid": visual.get("safeAreas", {}).get("short", {}).get("captions"), "dedicatedReframeRequired": True},
    }


def default_states(state_change, classification, layers, scene_type="forensic-reveal"):
    focus_layers = [layer for layer in layers if layer in {"subject", "state-change", "evidence"}] or layers
    profiles = {
        "cinematic-photo": ("masked-reveal", "lateral-drift", "evidence-lens", "detail-inspection", "negative-space-pullout"),
        "photo-reconstruction": ("masked-reveal", "lateral-drift", "evidence-lens", "detail-inspection", "archive-title-object"),
        "evidence-reveal": ("masked-reveal", "evidence-lens", "line-draw", "document-dive", "negative-space-pullout"),
        "forensic-reveal": ("masked-reveal", "evidence-lens", "detail-inspection", "document-dive", "negative-space-pullout"),
        "evidence-focus": ("masked-reveal", "evidence-lens", "controlled-crop", "detail-inspection", "pull-out"),
        "investigation-board": ("masked-reveal", "lateral-drift", "line-draw", "match-cut", "archive-title-object"),
        "timeline": ("masked-reveal", "timeline-build", "line-draw", "evidence-lens", "negative-space-pullout"),
        "timeline-build": ("masked-reveal", "timeline-build", "line-draw", "evidence-lens", "negative-space-pullout"),
        "geographic-location": ("masked-reveal", "lateral-drift", "evidence-lens", "detail-inspection", "negative-space-pullout"),
        "location-sequence": ("masked-reveal", "lateral-drift", "evidence-lens", "detail-inspection", "negative-space-pullout"),
        "animated-map": ("masked-reveal", "route-draw", "evidence-lens", "line-draw", "negative-space-pullout"),
        "evidence-map": ("masked-reveal", "route-draw", "evidence-lens", "line-draw", "negative-space-pullout"),
        "document-report": ("masked-reveal", "document-dive", "typewriter-interference", "evidence-lens", "archive-title-object"),
        "newspaper-archive": ("masked-reveal", "document-dive", "typewriter-interference", "evidence-lens", "archive-title-object"),
        "document-dive": ("masked-reveal", "document-dive", "typewriter-interference", "evidence-lens", "archive-title-object"),
        "portrait-investigation": ("masked-reveal", "lateral-drift", "evidence-lens", "detail-inspection", "negative-space-pullout"),
        "object-detail": ("masked-reveal", "detail-inspection", "evidence-lens", "line-draw", "archive-title-object"),
        "detail-extraction": ("masked-reveal", "detail-inspection", "evidence-lens", "line-draw", "archive-title-object"),
        "split-screen": ("masked-reveal", "lateral-drift", "evidence-lens", "typewriter-interference", "negative-space-pullout"),
        "compare-contrast": ("masked-reveal", "lateral-drift", "evidence-lens", "typewriter-interference", "negative-space-pullout"),
        "split-evidence": ("masked-reveal", "lateral-drift", "evidence-lens", "typewriter-interference", "negative-space-pullout"),
        "hypothesis-comparator": ("masked-reveal", "lateral-drift", "evidence-lens", "typewriter-interference", "negative-space-pullout"),
        "quote": ("masked-reveal", "typewriter-interference", "archive-title-object", "evidence-lens", "negative-space-pullout"),
        "data-visualization": ("masked-reveal", "line-draw", "evidence-lens", "typewriter-interference", "negative-space-pullout"),
        "concept-diagram": ("masked-reveal", "line-draw", "evidence-lens", "match-cut", "archive-title-object"),
        "chapter-break": ("static-hold", "static-hold", "static-hold", "static-hold", "static-hold"),
        "negative-space-beat": ("static-hold", "static-hold", "negative-space-pullout", "static-hold", "static-hold"),
        "end-card-cta": ("static-hold", "static-hold", "static-hold", "static-hold", "static-hold"),
        "archive-end-card": ("static-hold", "static-hold", "static-hold", "static-hold", "static-hold"),
        "surveillance-footage": ("masked-reveal", "evidence-lens", "detail-inspection", "typewriter-interference", "negative-space-pullout"),
        "security-camera": ("masked-reveal", "evidence-lens", "detail-inspection", "typewriter-interference", "negative-space-pullout"),
    }
    operators = profiles.get(scene_type, profiles["forensic-reveal"])
    state_specs = [
        ("entry", [0, 0.15], operators[0], layers[:2], [0.5, 0.42], "entrada editorial"),
        ("establish", [0.15, 0.4], operators[1], layers[:3], [0.5, 0.44], "contexto espacial"),
        ("focus", [0.4, 0.7], operators[2], focus_layers, [0.62, 0.38], "evidência em foco"),
        ("emphasis", [0.7, 0.9], operators[3], focus_layers, [0.7, 0.32], "destaque editorial"),
        ("exit", [0.9, 1], operators[4], focus_layers, [0.56, 0.4], "encerramento visual"),
    ]
    return [
        {
            "id": state_id,
            "timeRange": time_range,
            "intent": compact(f"{label}: {state_change or classification}", 120),
            "visibleLayers": visible,
            "hiddenLayers": [layer for layer in layers if layer not in visible],
            "assetIds": [],
            "motion": motion,
            "focalPoint": focal_point,
            "annotation": f"{label}: {state_change or classification}" if state_id in {"focus", "emphasis"} else "",
        }
        for state_id, time_range, motion, visible, focal_point, label in state_specs
    ]


def bind_state_assets(states, assets, layers):
    if not isinstance(states, list):
        return states
    available = [asset for asset in assets or [] if isinstance(asset, dict) and asset.get("assetId")]
    primary = next((asset for asset in available if asset.get("role") == "primary"), None)
    supporting = next((asset for asset in available if asset.get("role") == "supporting"), None)
    bound = []
    for index, state in enumerate(states):
        if not isinstance(state, dict):
            bound.append(state)
            continue
        current = dict(state)
        explicit = [str(value) for value in current.get("assetIds", []) if value]
        if explicit:
            current["assetIds"] = explicit
            bound.append(current)
            continue
        visible_layers = set(current.get("visibleLayers") or layers or [])
        selected = [asset for asset in available if asset.get("layer") in visible_layers]
        if not selected and primary:
            selected = [primary]
        if index >= 2 and supporting and supporting not in selected:
            selected.append(supporting)
        current["assetIds"] = [str(asset["assetId"]) for asset in selected]
        bound.append(current)
    return bound


def default_layers():
    return ["environment", "subject", "state-change", "continuity"]


def composition_for(scene_type, classification, state_change):
    anchor = compact(state_change or classification, 160)
    layouts = {
        "forensic-reveal": "single decisive forensic composition with foreground obstruction and a narrow path to the evidence",
        "evidence-focus": "evidence-led close composition with the physical trace at the optical center and context receding into shadow",
        "investigation-board": "asymmetrical relationship composition with source materials separated from the central inference",
        "timeline-build": "horizontal chronological composition with a strong left-to-right reading path and one visual anchor per event",
        "hypothesis-comparator": "balanced split composition that keeps competing interpretations visibly distinct without implying equivalence of certainty",
        "document-dive": "document-centered composition with the source object dominant and all identifying text outside the baked image",
        "negative-space-beat": "restrained negative-space composition that isolates absence or human consequence without inventing a person",
        "archive-end-card": "closed archival composition that preserves the case identity while keeping the frame free of generated text",
        "location-sequence": "geographic establishing composition with a clear approach axis and no unrelated landmarks",
    }
    return f"{layouts.get(scene_type, 'case-specific documentary composition')}; {anchor}"


def default_shot(block, index, claims, visual, research=None):
    block = block if isinstance(block, dict) else {}
    visual = visual if isinstance(visual, dict) else DEFAULT_VISUAL
    nested_visual = block.get("visual") if isinstance(block.get("visual"), dict) else {}
    nested_editorial = block.get("editorial") if isinstance(block.get("editorial"), dict) else {}
    block_text = clean_value(first_value(block, "text", "guide"))
    question = clean_value(first_value(block, "question", default=nested_editorial.get("question")))
    state_change = clean_value(first_value(block, "state_change", "stateChange", default=nested_editorial.get("stateChange")))
    selected = selected_claims(block, research) if research else [claim for claim in claims if isinstance(claim, dict) and clean_value(claim.get("id")) in set(as_list(first_value(block, "claim_ids", "claimIds")))]
    classification = classification_for(block, selected)
    block_id = clean_value(block.get("id")) or f"B-{slug(first_value(block, 'beat', default=block_text))}-{hashlib.sha1(block_text.encode('utf-8')).hexdigest()[:8]}"
    shot_id = clean_value(block.get("shotId")) or f"SHOT-{slug(block_id)}"
    prompt_id = clean_value(block.get("promptId")) or f"PROMPT-{slug(block_id)}"
    claim_ids = as_list(first_value(block, "claim_ids", "claimIds")) or [clean_value(claim.get("id")) for claim in selected]
    source_ids = selected_sources(block, selected)
    case_name = research["caseName"] if research else clean_value(first_value(block, "case", "case_id"))
    claim_text = compact(" ".join(clean_value(first_value(claim, "text", "statement")) for claim in selected), 300)
    timeline_context = compact(" | ".join(timeline_label(row) for row in research["timeline"][:3]), 300) if research else ""
    source_context = compact(" | ".join(source_label(row) for row in list(research["sources"].values())[:3]), 240) if research else ""
    subject = clean_value(first_value(block, "subject", default=nested_visual.get("subject"))) or claim_text or block_text or (research["briefPhrase"] if research else "")
    setting = clean_value(first_value(block, "setting", "location", default=nested_visual.get("location"))) or compact(" | ".join(value for value in (case_name, source_context, timeline_context) if value), 360)
    scene_type = block_type(first_value(block, "beat", default=nested_editorial.get("beat")))
    purpose = clean_value(first_value(block, "purpose", default=nested_editorial.get("purpose"))) or compact(f"Responder {question} e tornar visível {state_change}", 240)
    layers = as_list(block.get("layers")) or default_layers()
    crop_policy = default_crop_policy(block, visual)
    safe_areas = block.get("safeAreas") if isinstance(block.get("safeAreas"), dict) else visual.get("safeAreas", DEFAULT_VISUAL["safeAreas"])
    negative_guards = unique(as_list(block.get("negativeGuards")) + as_list(visual.get("image", {}).get("negativeGuards")) + [CLASSIFICATION_GUARDS.get(classification, CLASSIFICATION_GUARDS["MIXED"]), "no baked-in text; captions and labels are added later in Remotion"])
    continuity = continuity_for(block, visual, research, subject, classification)
    states = block.get("states") if isinstance(block.get("states"), list) and block.get("states") else default_states(state_change, classification, layers, scene_type)
    composition = clean_value(first_value(block, "composition", default=nested_visual.get("composition"))) or composition_for(scene_type, classification, state_change)
    assets = normalize_assets(first_value(block, "assets", default={}), shot_id, prompt_id, [block_id])
    states = bind_state_assets(states, assets, layers)
    shot = {
        "shotId": shot_id,
        "promptId": prompt_id,
        "sourceBlockIds": [block_id],
        "claimIds": unique(claim_ids),
        "sourceIds": source_ids,
        "purpose": purpose,
        "question": question,
        "stateChange": state_change,
        "classification": classification,
        "subject": subject,
        "setting": setting,
        "composition": composition,
        "layers": layers,
        "cropPolicy": crop_policy,
        "safeAreas": safe_areas,
        "negativeGuards": negative_guards,
        "continuity": continuity,
        "states": states,
        "assets": assets,
        "selectedClaims": selected,
        "status": "needs-art-direction",
    }
    shot["imagePrompt"] = build_image_prompt(shot)
    shot["motionPrompt"] = build_motion_prompt(shot)
    shot["prompt"] = {"full": shot["imagePrompt"]["full"], "negativeGuards": shot["negativeGuards"], "expectedOutput": "16:9 master with caption-safe lower band and watermark-safe corner"}
    shot["editorial"] = {**nested_editorial, "beat": clean_value(block.get("beat")), "function": scene_type, "purpose": purpose, "stateChange": state_change}
    shot["visual"] = {**nested_visual, "sceneType": scene_type, "visualRole": scene_type, "subject": subject, "action": state_change, "location": setting, "timeOfDay": clean_value(first_value(block, "timeOfDay", default=nested_visual.get("timeOfDay"))), "camera": clean_value(first_value(block, "camera", default=nested_visual.get("camera"))), "grade": clean_value(nested_visual.get("grade")) or "channel-defined restrained documentary grade", "headline": question or purpose, "body": "", "overlayRole": "evidence marker or metadata only"}
    if all(shot.get(field) not in (None, "", []) for field in REQUIRED_SCENE_FIELDS) and not contains_placeholder(shot):
        shot["status"] = "ready"
    return shot


def normalize_assets(value, shot_id, prompt_id, source_block_ids):
    records = []
    if isinstance(value, list):
        candidates = value
    elif isinstance(value, dict):
        candidates = []
        for role in ("primary", "supporting", "excluded"):
            entries = value.get(role, [])
            if not isinstance(entries, list):
                entries = [entries]
            for entry in entries:
                if isinstance(entry, dict):
                    candidates.append({"role": role, **entry})
                elif clean_value(entry):
                    candidates.append({"role": role, "path": clean_value(entry)})
    else:
        candidates = []
    for candidate in candidates:
        if not isinstance(candidate, dict):
            continue
        role = clean_value(candidate.get("role")) or ("supporting" if any(record["role"] == "primary" for record in records) else "primary")
        asset_fingerprint = hashlib.sha256(json.dumps(candidate, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()[:8]
        asset_id = clean_value(candidate.get("assetId")) or f"A-{slug(prompt_id)}-{slug(role)}-{asset_fingerprint}"
        record = {
            "assetId": asset_id,
            "promptId": clean_value(candidate.get("promptId")) or prompt_id,
            "shotId": clean_value(candidate.get("shotId")) or shot_id,
            "role": role,
            "path": clean_value(candidate.get("path")),
            "layer": clean_value(candidate.get("layer")) or None,
            "kind": clean_value(candidate.get("kind")) or "image",
            "origin": clean_value(candidate.get("origin")) or "pending",
            "rightsStatus": clean_value(candidate.get("rightsStatus")) or "pending",
            "hash": candidate.get("hash"),
            "blocked": bool(candidate.get("blocked", False)),
            "sourceBlockIds": as_list(candidate.get("sourceBlockIds")) or source_block_ids,
        }
        if record["layer"] is None:
            record.pop("layer")
        records.append(record)
    if not records:
        records.append({
            "assetId": f"A-{slug(prompt_id)}-PRIMARY",
            "promptId": prompt_id,
            "shotId": shot_id,
            "role": "primary",
            "path": "",
            "kind": "image",
            "origin": "pending",
            "rightsStatus": "pending",
            "hash": None,
            "blocked": False,
            "sourceBlockIds": source_block_ids,
        })
    return records


def normalize_shot(shot, research, visual):
    if not isinstance(shot, dict):
        return shot
    merged = dict(shot)
    source_blocks = as_list(first_value(shot, "sourceBlockIds", default=[]))
    block = next((candidate for candidate in research["blocks"] if clean_value(candidate.get("id")) in source_blocks), {})
    if not block and len(research["blocks"]) == 1:
        block = research["blocks"][0]
    defaults = default_shot(block, 0, research["claims"], visual, research)
    for key, value in defaults.items():
        if key not in merged or merged[key] in (None, "", [], {}):
            merged[key] = value
    if isinstance(merged.get("visual"), dict):
        for key in ("subject", "location", "composition", "camera", "timeOfDay"):
            if merged.get(key) in (None, "", {}) and merged["visual"].get(key) not in (None, "", {}):
                merged[key] = merged["visual"][key]
    merged["sourceBlockIds"] = source_blocks or defaults["sourceBlockIds"]
    merged["shotId"] = clean_value(merged.get("shotId")) or defaults["shotId"]
    merged["promptId"] = clean_value(merged.get("promptId")) or defaults["promptId"]
    merged["claimIds"] = as_list(merged.get("claimIds")) or defaults["claimIds"]
    merged["sourceIds"] = as_list(merged.get("sourceIds")) or defaults["sourceIds"]
    merged["layers"] = as_list(merged.get("layers")) or defaults["layers"]
    merged["negativeGuards"] = unique(as_list(merged.get("negativeGuards")) + defaults["negativeGuards"])
    merged["assets"] = normalize_assets(merged.get("assets"), merged["shotId"], merged["promptId"], merged["sourceBlockIds"])
    if not isinstance(merged.get("states"), list) or not merged.get("states"):
        merged["states"] = defaults["states"]
    merged["states"] = bind_state_assets(merged["states"], merged["assets"], merged.get("layers", []))
    if not isinstance(merged.get("safeAreas"), dict) or not merged.get("safeAreas"):
        merged["safeAreas"] = defaults["safeAreas"]
    if not isinstance(merged.get("continuity"), dict) or not merged.get("continuity"):
        merged["continuity"] = defaults["continuity"]
    if not isinstance(merged.get("cropPolicy"), dict) or not merged.get("cropPolicy"):
        merged["cropPolicy"] = defaults["cropPolicy"]
    if not isinstance(merged.get("editorial"), dict) or not merged.get("editorial"):
        merged["editorial"] = defaults.get("editorial", {})
    if not isinstance(merged.get("visual"), dict) or not merged.get("visual"):
        merged["visual"] = defaults.get("visual", {})
    old_prompt = merged.get("prompt") if isinstance(merged.get("prompt"), dict) else {}
    image_input = dict(merged.get("imagePrompt")) if isinstance(merged.get("imagePrompt"), dict) else {}
    image_input.setdefault("full", old_prompt.get("full", ""))
    merged["imagePrompt"] = build_image_prompt(merged, image_input)
    motion_input = dict(merged.get("motionPrompt")) if isinstance(merged.get("motionPrompt"), dict) else {}
    merged["motionPrompt"] = build_motion_prompt(merged, motion_input)
    merged["prompt"] = {**old_prompt, "full": merged["imagePrompt"]["full"], "negativeGuards": merged["negativeGuards"], "expectedOutput": old_prompt.get("expectedOutput", "16:9 master with caption-safe lower band and watermark-safe corner")}
    merged["selectedClaims"] = defaults.get("selectedClaims", [])
    merged["editorial"] = defaults.get("editorial", {})
    merged["visual"] = defaults.get("visual", {})
    errors = validate_shot(merged)
    merged["status"] = "ready" if not errors else "needs-art-direction"
    return merged


def safe_area_text(safe_areas):
    parts = []
    for format_name in ("long", "short"):
        area = safe_areas.get(format_name, {}) if isinstance(safe_areas, dict) else {}
        for name in ("action", "captions", "watermark"):
            value = area.get(name)
            if isinstance(value, list) and len(value) == 4:
                parts.append(f"{format_name}.{name}={value}")
    return "; ".join(parts)


def continuity_text(continuity):
    return json.dumps(continuity, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def build_image_prompt(shot, existing=None):
    existing = existing if isinstance(existing, dict) else {}
    composition_value = shot.get("composition")
    if isinstance(composition_value, dict):
        composition_description = clean_value(composition_value.get("description"))
        focal_point = composition_value.get("focalPoint", [0.5, 0.45])
        shot_scale = clean_value(composition_value.get("shotScale"))
        camera = clean_value(composition_value.get("camera"))
        lighting = clean_value(composition_value.get("lighting"))
    else:
        composition_description = clean_value(composition_value)
        crop_long = shot.get("cropPolicy", {}).get("long", {}) if isinstance(shot.get("cropPolicy"), dict) else {}
        focal_point = existing.get("focalPoint") or crop_long.get("focalPoint") or [0.5, 0.45]
        shot_scale = clean_value(existing.get("shotScale"))
        camera = clean_value(existing.get("camera"))
        lighting = clean_value(existing.get("lighting"))
    crop = "16:9 master; preserve the declared long and short focal points through dedicated reframing"
    guards = unique(as_list(existing.get("negativeGuards")) + as_list(shot.get("negativeGuards")))
    classification_guard = CLASSIFICATION_GUARDS.get(shot.get("classification"), CLASSIFICATION_GUARDS["MIXED"])
    guards = unique(guards + [classification_guard, "no baked-in text; captions and labels are added later in Remotion"])
    parts = [
        f"IMAGE_PROMPT[{shot.get('promptId')}/{shot.get('shotId')}]",
        f"Editorial purpose: {shot.get('purpose')}",
        f"Scene question: {shot.get('question')}",
        f"State change: {shot.get('stateChange')}",
        f"Classification: {shot.get('classification')}",
        f"Subject: {shot.get('subject')}",
        f"Setting: {shot.get('setting')}",
        f"Composition: {composition_description}",
        f"Shot scale: {shot_scale or 'scene-specific documentary scale derived from the declared composition'}",
        f"Camera: {camera or 'purposeful camera position declared by the composition, with no unmotivated perspective distortion'}",
        f"Lighting: {lighting or 'motivated low-key documentary light consistent with the setting and continuity contract'}",
        f"Focal point: {focal_point}",
        f"Crop: {crop}",
        f"Safe areas: {safe_area_text(shot.get('safeAreas', {}))}",
        f"Layers: {', '.join(as_list(shot.get('layers')))}",
        f"Continuity: {continuity_text(shot.get('continuity', {}))}",
        "Render one complete cinematic documentary image with physically coherent depth, restrained editorial treatment and classification-safe evidence.",
        f"Negative guards: {'; '.join(guards)}",
        "Output: 16:9 master; absolutely no baked-in text, readable signage, generated captions or watermark.",
    ]
    full = clean_value(existing.get("full")) or " | ".join(compact(part) for part in parts if compact(part))
    return {
        "contractVersion": 1,
        "promptId": shot.get("promptId"),
        "shotId": shot.get("shotId"),
        "purpose": shot.get("purpose"),
        "question": shot.get("question"),
        "stateChange": shot.get("stateChange"),
        "classification": shot.get("classification"),
        "subject": shot.get("subject"),
        "setting": shot.get("setting"),
        "composition": {"description": composition_description, "focalPoint": focal_point, "shotScale": shot_scale, "camera": camera, "lighting": lighting},
        "layers": as_list(shot.get("layers")),
        "cropPolicy": shot.get("cropPolicy", {}),
        "safeAreas": shot.get("safeAreas", {}),
        "continuity": shot.get("continuity", {}),
        "negativeGuards": guards,
        "full": full,
    }


def motion_intensity(shot):
    existing = shot.get("motionPrompt", {}).get("intensity") if isinstance(shot.get("motionPrompt"), dict) else None
    if isinstance(existing, bool):
        return None
    if isinstance(existing, int) and 0 <= existing <= 4:
        return existing
    scene_type = clean_value(first_value(shot.get("editorial", {}), "function")) or "forensic-reveal"
    return MOTION_PROFILES.get(scene_type, ("controlled-crop", 1))[1]


def build_motion_prompt(shot, existing=None):
    existing = existing if isinstance(existing, dict) else {}
    intensity = motion_intensity({**shot, "motionPrompt": existing})
    layers = as_list(existing.get("layers")) or as_list(shot.get("layers"))
    states = []
    for state in shot.get("states", []):
        if not isinstance(state, dict):
            continue
        time_range = state.get("timeRange", [0, 1])
        start, end = float(time_range[0]), float(time_range[1])
        if max(start, end) > 1:
            percent = [int(round(start)), int(round(end))]
        else:
            percent = [int(round(start * 100)), int(round(end * 100))]
        intent = clean_value(state.get("intent"))
        states.append({
            "id": clean_value(state.get("id")) or f"state-{len(states) + 1:02d}",
            "timeRange": percent,
            "intent": intent,
            "visibleLayers": as_list(state.get("visibleLayers")) or layers,
            "hiddenLayers": as_list(state.get("hiddenLayers")),
            "assetIds": as_list(state.get("assetIds")),
            **({"focalPoint": state["focalPoint"]} if isinstance(state.get("focalPoint"), (list, tuple)) else {}),
            **({"annotation": clean_value(state["annotation"])} if clean_value(state.get("annotation")) else {}),
            "motion": clean_value(state.get("motion")) or "controlled-crop",
            "transition": "hold",
            "audioCue": f"low, non-diegetic emphasis at {intent}" if intent else "low, non-diegetic emphasis at the state boundary",
        })
    if not states:
        states = [{"id": "state-01", "timeRange": [0, 100], "intent": shot.get("stateChange", ""), "visibleLayers": layers, "motion": "controlled-crop", "transition": "hold", "audioCue": f"low emphasis aligned to {shot.get('question', '')}"}]
    scene_type = (
        clean_value(first_value(shot.get("editorial", {}), "function"))
        or clean_value(first_value(shot.get("visual", {}), "sceneType"))
        or "forensic-reveal"
    )
    camera_kind, _ = MOTION_PROFILES.get(scene_type, ("controlled-crop", 1))
    camera_description = compact(f"Start on {shot.get('subject')}; move only to make '{shot.get('stateChange')}' legible while answering '{shot.get('question')}'; preserve the {shot.get('classification')} evidence boundary.")
    camera_path = existing.get("cameraPath") if isinstance(existing.get("cameraPath"), dict) else {"kind": camera_kind, "description": camera_description, "keyframes": [{"at": 0, "focalPoint": [0.5, 0.45]}, {"at": 50, "focalPoint": [0.5, 0.44]}, {"at": 100, "focalPoint": [0.5, 0.45]}]}
    if not clean_value(camera_path.get("description")):
        camera_path["description"] = camera_description
    transitions = existing.get("transitions") if isinstance(existing.get("transitions"), dict) else {
        "in": clean_value(shot.get("transitionIn")) or ("cut" if shot.get("classification") in {"FATO", "REPORTADO"} else "dissolve"),
        "out": clean_value(shot.get("transitionOut")) or "cut",
        "rationale": f"transition only after the visible state '{shot.get('stateChange')}' resolves the question '{shot.get('question')}'",
    }
    audio_cues = as_list(existing.get("audioCues")) or [state["audioCue"] for state in states]
    static_scene = scene_type in {"chapter-break", "negative-space-beat", "end-card-cta", "archive-end-card"}
    static_exception = existing.get("staticException") if isinstance(existing.get("staticException"), dict) else {
        "allowed": intensity == 0 or static_scene,
        "reason": f"static treatment is explicitly bound to '{shot.get('stateChange')}'" if intensity == 0 or static_scene else f"the scene must make '{shot.get('stateChange')}' visible rather than remain a generic hold",
    }
    negative_motion = unique(as_list(existing.get("negativeMotion")) + [
        "no generic zoom used as the only motion",
        "no generic fade used as the only transition",
        "no random parallax or floating layers",
        "no motion that changes the depicted evidence or classification",
        "no camera move that crosses a crop or safe-area boundary",
    ])
    full = clean_value(existing.get("full")) or " | ".join([
        f"MOTION_PROMPT[{shot.get('promptId')}/{shot.get('shotId')}]",
        f"Intensity: {intensity}/4",
        f"Layers: {', '.join(layers)}",
        "States 0-100: " + "; ".join(f"{state['id']}={state['timeRange'][0]}-{state['timeRange'][1]} ({state['intent']})" for state in states),
        f"Camera path: {camera_path.get('kind')} — {camera_path.get('description')}",
        f"Crop: {json.dumps(shot.get('cropPolicy', {}), ensure_ascii=False, sort_keys=True, separators=(',', ':'))}",
        f"Transitions: in={transitions.get('in')}; out={transitions.get('out')}; {transitions.get('rationale')}",
        "Audio cues: " + "; ".join(audio_cues),
        f"Static exception: allowed={str(bool(static_exception.get('allowed'))).lower()}; {static_exception.get('reason')}",
        "Negative motion: " + "; ".join(negative_motion),
    ])
    return {
        "contractVersion": 1,
        "promptId": shot.get("promptId"),
        "shotId": shot.get("shotId"),
        "intensity": intensity,
        "layers": layers,
        "states": states,
        "cameraPath": camera_path,
        "cropPolicy": shot.get("cropPolicy", {}),
        "transitions": transitions,
        "audioCues": audio_cues,
        "staticException": static_exception,
        "negativeMotion": negative_motion,
        "full": full,
    }


def load_specs(path):
    data = read_json(path)
    if isinstance(data, dict):
        specs = data.get("shots") or data.get("shotSpecs") or []
    else:
        specs = data
    return specs if isinstance(specs, list) else []


def prompt_from_shot(shot, visual=None):
    image = shot.get("imagePrompt") if isinstance(shot.get("imagePrompt"), dict) else {}
    prompt = clean_value(image.get("full") or (shot.get("prompt", {}) or {}).get("full"))
    return prompt


def valid_intensity(value):
    return isinstance(value, int) and not isinstance(value, bool) and 0 <= value <= 4


def valid_motion_states(states):
    if not isinstance(states, list) or not states:
        return False
    previous = 0.0
    for state in states:
        if not isinstance(state, dict) or not isinstance(state.get("timeRange"), list) or len(state["timeRange"]) != 2:
            return False
        start, end = state["timeRange"]
        if not isinstance(start, (int, float)) or not isinstance(end, (int, float)) or not 0 <= start < end <= 100 or start < previous:
            return False
        previous = end
    return states[0]["timeRange"][0] == 0 and states[-1]["timeRange"][1] == 100


def validate_shot(shot):
    errors = []
    if not isinstance(shot, dict):
        return ["shot_not_object"]
    for field in REQUIRED_SCENE_FIELDS:
        if field not in shot:
            errors.append(f"missing_{field}")
        elif shot[field] in (None, "", [], {}):
            errors.append(f"missing_{field}")
    for field in ("sourceBlockIds", "claimIds", "sourceIds", "layers", "negativeGuards", "states"):
        if not isinstance(shot.get(field), list):
            errors.append(f"invalid_{field}")
    for field in ("cropPolicy", "safeAreas", "continuity"):
        if not isinstance(shot.get(field), dict):
            errors.append(f"invalid_{field}")
    if contains_placeholder(shot):
        errors.append("placeholder_detected")
    image = shot.get("imagePrompt")
    if not isinstance(image, dict):
        errors.append("missing_image_prompt")
    else:
        image_text = str(image.get("full") or "")
        lowered = image_text.lower()
        for required in ("editorial purpose", "composition", "focal point", "crop", "safe areas", "negative guards", "continuity", "classification", "16:9"):
            if required not in lowered:
                errors.append(f"image_prompt_missing:{required}")
        for field in ("subject", "question", "stateChange", "classification"):
            if str(shot.get(field) or "") not in image_text:
                errors.append(f"image_prompt_unbound:{field}")
        if "no baked-in text" not in lowered:
            errors.append("image_prompt_missing:no_baked_in_text")
    motion = shot.get("motionPrompt")
    if not isinstance(motion, dict):
        errors.append("missing_motion_prompt")
    else:
        if not valid_intensity(motion.get("intensity")):
            errors.append("invalid_motion_intensity")
        if not valid_motion_states(motion.get("states")):
            errors.append("invalid_motion_states")
        if not as_list(motion.get("layers")):
            errors.append("missing_motion_layers")
        camera = motion.get("cameraPath")
        if not isinstance(camera, dict) or not clean_value(camera.get("description")):
            errors.append("missing_camera_path")
        elif shot.get("subject") not in str(camera.get("description")) or shot.get("stateChange") not in str(camera.get("description")):
            errors.append("generic_camera_path")
        if not isinstance(motion.get("transitions"), dict):
            errors.append("missing_transitions")
        if not as_list(motion.get("audioCues")):
            errors.append("missing_audio_cues")
        if not isinstance(motion.get("staticException"), dict) or "allowed" not in motion["staticException"]:
            errors.append("missing_static_exception")
        if not as_list(motion.get("negativeMotion")):
            errors.append("missing_negative_motion")
        motion_text = str(motion.get("full") or "").lower()
        for required in ("intensity", "states 0-100", "camera path", "crop", "transitions", "audio cues", "static exception", "negative motion"):
            if required not in motion_text:
                errors.append(f"motion_prompt_missing:{required}")
        if str(image.get("full") or "") == str(motion.get("full") or ""):
            errors.append("motion_prompt_not_separate")
    assets = shot.get("assets")
    if not isinstance(assets, list) or not assets:
        errors.append("missing_asset_bindings")
    else:
        asset_ids = set()
        for asset in assets:
            if not isinstance(asset, dict) or not clean_value(asset.get("assetId")):
                errors.append("invalid_asset_binding")
                continue
            asset_id = clean_value(asset["assetId"])
            if asset_id in asset_ids:
                errors.append(f"duplicate_asset_id:{asset_id}")
            asset_ids.add(asset_id)
            if clean_value(asset.get("promptId")) != clean_value(shot.get("promptId")) or clean_value(asset.get("shotId")) != clean_value(shot.get("shotId")):
                errors.append(f"asset_identity_mismatch:{asset_id}")
    return sorted(set(errors))


def validate_shots(shots, visual=None, research=None):
    errors = []
    shot_ids = set()
    prompt_ids = set()
    for shot in shots:
        shot_errors = validate_shot(shot)
        errors.extend(shot_errors)
        if not isinstance(shot, dict):
            continue
        shot_id = str(shot.get("shotId") or "")
        prompt_id = str(shot.get("promptId") or "")
        if not shot_id or shot_id in shot_ids:
            errors.append(f"invalid_shot_id:{shot_id}")
        if not prompt_id or prompt_id in prompt_ids:
            errors.append(f"invalid_prompt_id:{prompt_id}")
        shot_ids.add(shot_id)
        prompt_ids.add(prompt_id)
    if research:
        errors.extend(research["errors"])
    return sorted(set(errors))


def compile_prompt_plan(episode, visual_path=None, specs_path=None):
    episode = Path(episode)
    script_dir = episode / "01_roteiro"
    research = load_research(episode)
    visual, visual_explicit = load_visual(visual_path, episode)
    specs_file = Path(specs_path) if specs_path else script_dir / "SHOT_SPECS.json"
    if specs_file.exists():
        raw_shots = load_specs(specs_file)
    else:
        raw_shots = [default_shot(block, index, research["claims"], visual, research) for index, block in enumerate(research["blocks"], 1)]
    shots = [normalize_shot(shot, research, visual) for shot in raw_shots]
    records = []
    for shot in shots:
        image = shot["imagePrompt"]
        motion = shot["motionPrompt"]
        records.append({
            "promptId": shot.get("promptId"),
            "shotId": shot.get("shotId"),
            "sourceBlockIds": shot.get("sourceBlockIds", []),
            "claimIds": shot.get("claimIds", []),
            "sourceIds": shot.get("sourceIds", []),
            "purpose": shot.get("purpose"),
            "question": shot.get("question"),
            "stateChange": shot.get("stateChange"),
            "classification": shot.get("classification"),
            "imagePrompt": image,
            "motionPrompt": motion,
            "prompt": image.get("full", ""),
            "negativeGuards": image.get("negativeGuards", []),
            "expectedOutput": "16:9",
            "assetBindings": shot.get("assets", []),
            "status": shot.get("status", "needs-art-direction"),
        })
    errors = validate_shots(shots, visual, research)
    if not visual_explicit:
        errors.append("visual_contract_missing")
    if not records:
        errors.append("shots_missing")
    errors = sorted(set(errors))
    ready = not errors and all(record["status"] == "ready" for record in records)
    plan = {
        "version": 2,
        "episode": episode.name,
        "channel": visual.get("channel", episode.parent.name),
        "status": "PROMPTS_READY" if ready else "NEEDS_ART_DIRECTION",
        "visualVersion": visual.get("version", 2),
        "research": {
            "caseName": research["caseName"],
            "artifacts": research["artifacts"],
            "claimIds": sorted(research["claimIndex"]),
            "sourceIds": sorted(research["sources"]),
            "timelineEvents": len(research["timeline"]),
        },
        "shots": shots,
        "prompts": records,
        "errors": errors,
    }
    write_json(script_dir / "PROMPT_PLAN.json", plan)
    lines = ["# CONTRATOS VISUAIS DETERMINÍSTICOS", "", f"CASE: {research['caseName']}", f"STATUS: {plan['status']}", ""]
    for record in records:
        lines.extend([
            f"## {record['promptId']} — {record['shotId']}",
            f"BLOCKS: {', '.join(record['sourceBlockIds']) or '-'}",
            f"CLAIMS: {', '.join(record['claimIds']) or '-'}",
            f"SOURCES: {', '.join(record['sourceIds']) or '-'}",
            f"CLASSIFICATION: {record['classification']}",
            "",
            "### IMAGE_PROMPT",
            record["imagePrompt"]["full"],
            "",
            "### MOTION_PROMPT",
            record["motionPrompt"]["full"],
            "",
        ])
    prompts_path = episode / "03_imagens" / "PROMPTS.md"
    prompts_path.parent.mkdir(parents=True, exist_ok=True)
    prompts_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return plan


def build_shot_specs(episode, visual_path=None):
    research = load_research(episode)
    visual, _ = load_visual(visual_path, episode)
    return [default_shot(block, index, research["claims"], visual, research) for index, block in enumerate(research["blocks"], 1)]


def init_artifacts(episode, visual_path=None):
    episode = Path(episode)
    script_dir = episode / "01_roteiro"
    visual, visual_explicit = load_visual(visual_path, episode)
    specs_path = script_dir / "SHOT_SPECS.json"
    if not specs_path.exists():
        write_json(specs_path, {"version": 2, "episode": episode.name, "status": "NEEDS_ART_DIRECTION", "shots": build_shot_specs(episode, visual_path)})
    bible_path = script_dir / "VISUAL_BIBLE.json"
    if visual_explicit and not bible_path.exists():
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
    else:
        result = compile_prompt_plan(args.episode, args.visual, args.specs)
    print(json.dumps({"status": result["status"], "episode": result["episode"], "prompts": len(result["prompts"]), "errors": result["errors"]}, ensure_ascii=False))
    return 0 if result["status"] == "PROMPTS_READY" else 1


if __name__ == "__main__":
    sys.exit(main())
