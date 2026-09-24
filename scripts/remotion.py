#!/usr/bin/env python3
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

import asset_manifest as asset_tools
import run_ledger

HERE = Path(__file__).resolve().parent
SKILL_ROOT = HERE.parent
REMOTION_ROOT = SKILL_ROOT / "remotion"
DEFAULT_PLAYBOOKS = Path(os.environ.get("DARK_MASTER_PLAYBOOKS", SKILL_ROOT / "playbooks"))
DEFAULT_STYLE = {
    "background": "#0A0A0C",
    "surface": "#17171B",
    "text": "#F5F5F4",
    "muted": "#A1A1AA",
    "accent": "#B91C1C",
    "headingFont": "Arial",
    "bodyFont": "Arial",
}
BEAT_TYPES = {
    "HOOK": "cinematic-photo",
    "COLD OPEN": "cinematic-photo",
    "CONTEXT": "geographic-location",
    "CONTEXTO": "geographic-location",
    "O DIA": "timeline",
    "O MUNDO": "concept-diagram",
    "INVESTIGACAO": "investigation-board",
    "INVESTIGACAO/PERICIA": "investigation-board",
    "PERICIA": "evidence-table",
    "EVIDENCIAS": "evidence-reveal",
    "LINHA DO TEMPO": "timeline",
    "RECONSTRUCAO": "timeline-detail",
    "FAMILIA": "portrait-investigation",
    "TEORIAS": "compare-contrast",
    "CONTRADICAO": "split-screen",
    "MONEY": "data-visualization",
    "OUTRO": "chapter-break",
    "CHAVES": "chapter-break",
}
MEDIA_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".mp4", ".wav", ".mp3", ".m4a", ".ttf", ".otf", ".woff", ".woff2"}
IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp"}
REVIEW_MIN_SCORE = 92
REQUIRED_REVIEW_SAMPLES = ("F0", "F50", "F100")
REQUIRED_GATES = (
    "research",
    "map",
    "claims",
    "shotSpecs",
    "promptPlan",
    "manifest",
    "imageAudit",
    "rights",
    "assets",
    "captions",
    "timing",
    "audio",
    "visualProfile",
    "review",
)


def read_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise ValueError(f"invalid_json:{path}:{exc}") from exc


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def hash_json(value) -> str:
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def read_optional_json(path: Path):
    if not path.exists():
        return None
    try:
        return read_json(path)
    except ValueError:
        return None


def relative_to_episode(path: Path, episode: Path) -> str:
    try:
        return path.resolve().relative_to(episode.resolve()).as_posix()
    except ValueError:
        return path.name


def explicit_lane_value(contracts: dict, keys: tuple[str, ...], format_name: str):
    sources = []
    for value in contracts.values():
        if not isinstance(value, dict):
            continue
        for key in ("lane", "lanes", "audio", "voice", "render", "production"):
            if key in value:
                sources.append(value[key])
        sources.append(value)
    for source in sources:
        if isinstance(source, dict):
            for key in keys:
                if key in source:
                    return source[key]
            lane = source.get("lane")
            if isinstance(lane, dict) and format_name in lane:
                candidate = lane[format_name]
                if isinstance(candidate, dict):
                    for key in keys:
                        if key in candidate:
                            return candidate[key]
                else:
                    return candidate
    return None


def lane_requires_audio(contracts: dict, format_name: str) -> bool:
    value = explicit_lane_value(contracts, ("requiresAudio", "audioRequired", "requiresVoice", "voiceRequired", "required"), format_name)
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() not in {"false", "no", "off", "none", "silent", "visual-only", "visual_only"}
    lane = explicit_lane_value(contracts, ("lane",), format_name)
    if isinstance(lane, str):
        return lane.strip().lower() not in {"silent", "visual", "visual-only", "visual_only", "none"}
    return True


def visual_profile(episode: Path, contracts: dict) -> tuple[dict, Path | None, str]:
    path = episode / "01_roteiro" / "VISUAL_BIBLE.json"
    if path.exists():
        value = read_json(path)
        if not isinstance(value, dict):
            raise ValueError("invalid_visual_profile")
        return value, path, sha256(path)
    value = contracts.get("visual")
    if isinstance(value, dict) and value:
        return value, None, hash_json(value)
    return {}, None, hash_json({})


def asset_path_is_safe(images_dir: Path, value: str) -> bool:
    raw = str(value or "")
    if not raw or re.match(r"^[a-z]+://", raw, re.IGNORECASE):
        return False
    candidate = Path(raw).expanduser()
    if not candidate.is_absolute():
        candidate = images_dir / candidate
    try:
        resolved = candidate.resolve()
        root = images_dir.resolve()
    except OSError:
        return False
    return resolved.is_relative_to(root) and resolved.is_file() and resolved.suffix.lower() in IMAGE_SUFFIXES


def image_audit_gate(images_dir: Path) -> dict:
    candidates = (
        images_dir / "IMAGE_AUDIT.json",
        images_dir / "AUDITORIA_IMAGENS.json",
        images_dir / "IMAGE_AUDIT_RESULT.json",
        images_dir.parent / "01_roteiro" / "IMAGE_AUDIT.json",
    )
    for path in candidates:
        data = read_optional_json(path)
        if isinstance(data, dict):
            status = str(data.get("status", "")).upper()
            if status in {"PASS", "PASSED", "OK"}:
                return {"status": "PASS", "path": str(path), "errors": []}
            return {"status": "FAIL", "path": str(path), "errors": [f"image_audit_status:{status or 'MISSING'}"]}
    report = images_dir / "AUDITORIA_IMAGENS.md"
    if report.exists():
        text = report.read_text(encoding="utf-8", errors="replace")
        if "RESULTADO: PASSOU" in text or ("- [ok]" in text and "- [FALHA]" not in text):
            return {"status": "PASS", "path": str(report), "errors": []}
        return {"status": "FAIL", "path": str(report), "errors": ["image_audit_not_passed"]}
    return {"status": "FAIL", "path": "", "errors": ["image_audit_missing"]}


def gate(name: str, status: str, errors: list[str] | None = None, **details) -> dict:
    return {"name": name, "status": status, "errors": sorted(set(str(value) for value in (errors or []))), **details}


def gate_passes(result: dict) -> bool:
    return result.get("status") == "PASS"


def review_manifest_path(episode: Path, format_name: str) -> Path:
    return episode / "01_roteiro" / f"VISUAL_REVIEW_{format_name.upper()}.json"


def review_receipt_path(episode: Path, format_name: str) -> Path:
    return episode / "01_roteiro" / f"VISUAL_REVIEW_RECEIPT_{format_name.upper()}.json"


def plan_hash(path: Path) -> str:
    return sha256(path) if path.exists() else ""


def run_dir_from_plan(plan: dict, episode: Path) -> Path:
    staging = plan.get("staging", {}) if isinstance(plan.get("staging"), dict) else {}
    raw = staging.get("path") or staging.get("publicDir") or ""
    if raw:
        value = Path(str(raw))
        public = (value if value.is_absolute() else episode / value).resolve()
        root = (episode / "04_video_final" / "_remotion" / "runs").resolve()
        if not public.is_relative_to(root):
            raise ValueError("render_staging_outside_run_root")
        return public.parent
    run_id = str(plan.get("runId") or "")
    if not run_id:
        raise FileNotFoundError("render_plan_staging_missing")
    candidate = (episode / "04_video_final" / "_remotion" / "runs" / run_id).resolve()
    root = (episode / "04_video_final" / "_remotion" / "runs").resolve()
    if not candidate.is_relative_to(root):
        raise ValueError("render_run_outside_run_root")
    return candidate


def plan_run_info(plan_path: Path, episode: Path | None = None) -> tuple[dict, Path, dict]:
    plan = read_json(plan_path)
    episode = episode or plan_path.parent.parent
    run_dir = run_dir_from_plan(plan, episode)
    try:
        run = run_ledger.load_run(run_dir)
    except (FileNotFoundError, ValueError) as exc:
        raise ValueError(str(exc)) from exc
    return plan, run_dir, run


def review_gate(episode: Path, format_name: str, render_plan: Path | None = None, minimum_score: int = REVIEW_MIN_SCORE) -> dict:
    episode = Path(episode)
    manifest_path = review_manifest_path(episode, format_name)
    selected_plan = Path(render_plan) if render_plan is not None else plan_path(episode, format_name)
    errors = []
    manifest = read_optional_json(manifest_path)
    if not isinstance(manifest, dict):
        return {"status": "FAIL", "errors": ["visual_review_manifest_missing"], "path": str(manifest_path)}
    actual_plan_hash = plan_hash(selected_plan)
    manifest_plan_hash = str(manifest.get("planHash") or "")
    manifest_run_id = str(manifest.get("runId") or "")
    plan_data = read_optional_json(selected_plan) if selected_plan.exists() else {}
    if isinstance(plan_data, dict) and manifest_run_id and manifest_run_id != str(plan_data.get("runId") or ""):
        errors.append("visual_review_run_id_mismatch")
    if not actual_plan_hash:
        errors.append("render_plan_missing_for_review")
    if manifest.get("status") != "REVIEW_REQUIRED":
        errors.append("visual_review_manifest_not_required_state")
    if manifest_plan_hash != actual_plan_hash:
        errors.append("visual_review_plan_hash_mismatch")
    receipt_ref = manifest.get("receipt")
    receipt_path = Path(str(receipt_ref)) if receipt_ref else review_receipt_path(episode, format_name)
    if not receipt_path.is_absolute():
        receipt_path = manifest_path.parent / receipt_path
        if not receipt_path.exists() and receipt_path.parts and receipt_path.parts[0] == "01_roteiro":
            receipt_path = episode / receipt_path.relative_to("01_roteiro")
    receipt = read_optional_json(receipt_path)
    if not isinstance(receipt, dict):
        errors.append("visual_review_receipt_missing")
        receipt = {}
    if receipt:
        if str(receipt.get("planHash") or "") != actual_plan_hash:
            errors.append("visual_review_receipt_plan_hash_mismatch")
        if manifest_run_id and str(receipt.get("runId") or "") != manifest_run_id:
            errors.append("visual_review_receipt_run_id_mismatch")
        if receipt.get("manifest") and Path(str(receipt["manifest"])).resolve() != manifest_path:
            errors.append("visual_review_receipt_manifest_mismatch")
        if receipt.get("status") != "PASS":
            errors.append("visual_review_receipt_not_passed")
        reviewer = str(receipt.get("reviewer") or "").strip()
        if not reviewer or reviewer.lower() in {"self", "same", "artdirector", "dark-artdirector"}:
            errors.append("visual_review_reviewer_invalid")
        try:
            score = float(receipt.get("score", -1))
        except (TypeError, ValueError):
            score = -1
        if score < minimum_score:
            errors.append("visual_review_score_below_minimum")
        findings = receipt.get("findings", [])
        if not isinstance(findings, list):
            errors.append("visual_review_findings_invalid")
        elif any(str(item).upper().startswith(("BLOCKER", "MAJOR")) for item in findings):
            errors.append("visual_review_blocking_findings")
    samples = manifest.get("samples", [])
    if not isinstance(samples, list) or not samples:
        errors.append("visual_review_samples_missing")
    else:
        labels_by_scene = {}
        for sample in samples:
            if not isinstance(sample, dict):
                errors.append("visual_review_sample_invalid")
                continue
            scene_id = str(sample.get("sceneId") or "")
            label = str(sample.get("sample") or "")
            labels_by_scene.setdefault(scene_id, set()).add(label)
            sample_path = Path(str(sample.get("path") or ""))
            if not sample_path.is_absolute():
                sample_path = manifest_path.parent / sample_path
            if not sample_path.exists():
                errors.append("visual_review_sample_missing_file")
            elif sample.get("hash") and sha256(sample_path) != sample["hash"]:
                errors.append("visual_review_sample_hash_mismatch")
            derived_path = Path(str(sample.get("derived120") or ""))
            if sample.get("derived120"):
                if not derived_path.is_absolute():
                    derived_path = manifest_path.parent / derived_path
                if not derived_path.exists():
                    errors.append("visual_review_derived120_missing")
                elif sample.get("derived120Hash") and sha256(derived_path) != sample["derived120Hash"]:
                    errors.append("visual_review_derived120_hash_mismatch")
        for scene_id, labels in labels_by_scene.items():
            if set(REQUIRED_REVIEW_SAMPLES) - labels:
                errors.append(f"visual_review_samples_incomplete:{scene_id}")
        planned_scene_ids = {
            str(scene.get("shotId") or scene.get("id") or "")
            for scene in (plan_data.get("scenes", []) if isinstance(plan_data, dict) else [])
            if isinstance(scene, dict)
        }
        if planned_scene_ids and set(labels_by_scene) != planned_scene_ids:
            errors.append("visual_review_scene_set_mismatch")
        contact_sheets = manifest.get("contactSheets")
        if not isinstance(contact_sheets, list) or not contact_sheets:
            errors.append("visual_review_contact_sheet_missing")
        else:
            scene_sheets = {str(item.get("sceneId")) for item in contact_sheets if isinstance(item, dict) and item.get("sceneId")}
            for scene_id in labels_by_scene:
                if scene_id not in scene_sheets:
                    errors.append(f"visual_review_scene_contact_sheet_missing:{scene_id}")
            if not any(isinstance(item, dict) and item.get("sequence") for item in contact_sheets):
                errors.append("visual_review_sequence_contact_sheet_missing")
            for item in contact_sheets:
                if not isinstance(item, dict):
                    errors.append("visual_review_contact_sheet_invalid")
                    continue
                sheet_path = Path(str(item.get("path") or ""))
                if not sheet_path.is_absolute():
                    sheet_path = manifest_path.parent / sheet_path
                if not sheet_path.exists():
                    errors.append("visual_review_contact_sheet_file_missing")
                elif item.get("hash") and sha256(sheet_path) != item["hash"]:
                    errors.append("visual_review_contact_sheet_hash_mismatch")
    errors = sorted(set(errors))
    return {"status": "FAIL" if errors else "PASS", "errors": errors, "path": str(manifest_path), "receipt": str(receipt_path), "score": receipt.get("score")}


def npm_command() -> str:
    return shutil.which("npm.cmd") or shutil.which("npm") or "npm"


def run_command(command: list[str], cwd: Path, env: dict[str, str] | None = None, check: bool = True):
    merged = {**os.environ, **(env or {})}
    return subprocess.run(command, cwd=cwd, env=merged, check=check, text=True, capture_output=True)


def ffprobe_duration(path: Path) -> float:
    executable = shutil.which("ffprobe")
    if not executable or not path.exists():
        return 0.0
    result = subprocess.run(
        [executable, "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        capture_output=True,
        text=True,
    )
    if result.returncode:
        return 0.0
    try:
        return float(result.stdout.strip())
    except ValueError:
        return 0.0


def parse_srt(path: Path) -> list[dict]:
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    blocks = re.split(r"\n\s*\n", text.strip()) if text.strip() else []
    captions = []
    for block in blocks:
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        timing_index = next((index for index, line in enumerate(lines[:3]) if "-->" in line), -1)
        if timing_index < 0 or len(lines) <= timing_index + 1:
            continue
        start, end = [part.strip() for part in lines[timing_index].split("-->", 1)]
        start_seconds = srt_seconds(start)
        end_seconds = srt_seconds(end)
        if start_seconds is None or end_seconds is None or end_seconds <= start_seconds:
            continue
        captions.append({"startSeconds": start_seconds, "endSeconds": end_seconds, "text": " ".join(lines[timing_index + 1:])})
    return captions


def srt_seconds(value: str) -> float | None:
    normalized = str(value or "").strip().split()[0].replace(".", ",") if str(value or "").strip() else ""
    if re.fullmatch(r"\d{2}:\d{2},\d{3}", normalized):
        normalized = "00:" + normalized
    match = re.fullmatch(r"(\d{2}):(\d{2}):(\d{2})[,](\d{3})", normalized)
    if not match:
        return None
    hours, minutes, seconds, millis = match.groups()
    return int(hours) * 3600 + int(minutes) * 60 + int(seconds) + int(millis) / 1000


def parse_timing(path: Path) -> tuple[float, list[dict]]:
    if not path.exists():
        return 0.0, []
    try:
        data = read_json(path)
    except ValueError:
        return 0.0, []
    blocks = data.get("blocos") or data.get("blocks") or []
    rows = []
    for block in blocks:
        if not isinstance(block, dict):
            continue
        start = float(block.get("start", 0) or 0)
        end = float(block.get("end", block.get("start", 0) + block.get("dur", 0)) or 0)
        if end > start:
            rows.append({"start": start, "end": end, "dur": end - start})
    total = float(data.get("total") or 0)
    return total, rows


def resolve_channel(root: Path, channel: str | None) -> Path | None:
    if channel:
        candidate = Path(channel).expanduser()
        if candidate.is_dir() and any((candidate / name).exists() for name in ("profile.md", "style.json", "motion.json", "voice.json", "visual.json")):
            return candidate
        candidate = DEFAULT_PLAYBOOKS / channel
        if candidate.exists():
            return candidate
    local = root / "playbooks" / (channel or "")
    if local.exists():
        return local
    return None


def load_contract(root: Path, channel: str | None, allow_defaults: bool = False) -> dict:
    channel_dir = resolve_channel(root, channel)
    contracts = {}
    required = ("style.json", "motion.json", "voice.json", "roteiro.json")
    for name in required:
        path = channel_dir / name if channel_dir else None
        if path and path.exists():
            contracts[name.removesuffix(".json")] = read_json(path)
        elif not allow_defaults:
            raise FileNotFoundError(f"missing_contract:{name}:{channel_dir}")
    visual_path = channel_dir / "visual.json" if channel_dir else None
    if visual_path and visual_path.exists():
        contracts["visual"] = read_json(visual_path)
    return contracts


def theme_from_style(style: dict, visual: dict | None = None) -> dict:
    source = style.get("remotion", {}).get("theme", {}) if isinstance(style.get("remotion"), dict) else {}
    colors = source.get("colors", source) if isinstance(source, dict) else {}
    palette = visual.get("palette", {}) if isinstance(visual, dict) else {}
    typography = visual.get("typography", {}) if isinstance(visual, dict) else {}
    safe = visual.get("safeAreas", {}).get("long", {}) if isinstance(visual, dict) else {}
    action = safe.get("action", [72 / 1920, 54 / 1080, 0.9, 0.78]) if isinstance(safe, dict) else [72 / 1920, 54 / 1080, 0.9, 0.78]
    return {
        "background": palette.get("background", colors.get("background", style.get("background", DEFAULT_STYLE["background"]))),
        "surface": palette.get("surface", colors.get("surface", style.get("surface", DEFAULT_STYLE["surface"]))),
        "text": palette.get("text", colors.get("text", style.get("text", DEFAULT_STYLE["text"]))),
        "muted": palette.get("muted", colors.get("muted", style.get("muted", DEFAULT_STYLE["muted"]))),
        "accent": palette.get("accent", colors.get("accent", style.get("accent", DEFAULT_STYLE["accent"]))),
        "headingFont": typography.get("heading", colors.get("headingFont", style.get("headingFont", DEFAULT_STYLE["headingFont"]))),
        "bodyFont": typography.get("body", colors.get("bodyFont", style.get("bodyFont", DEFAULT_STYLE["bodyFont"]))),
        "safeArea": {"x": round(float(action[0]) * 1920), "y": round(float(action[1]) * 1080)},
    }


def image_files(episode: Path) -> list[Path]:
    image_dir = episode / "03_imagens"
    if not image_dir.exists():
        return []
    return sorted(
        [path for path in image_dir.iterdir() if path.is_file() and path.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg"}],
        key=lambda path: path.name,
    )


def audio_file(episode: Path, format_name: str) -> Path | None:
    audio_dir = episode / "02_audio"
    if not audio_dir.exists():
        return None
    names = ("voice_FINAL_SHORT.wav", "voice_SHORT.wav", "voice_FINAL.wav", "voice_V3_FINAL.wav", "voice_FINAL.mp3", "voice_SHORT.mp3", "voice_FINAL.m4a", "voice_SHORT.m4a")
    if format_name == "short":
        names = ("voice_SHORT.wav", "voice_FINAL_SHORT.wav", "voice_FINAL.wav", "voice_V3_FINAL.wav", "voice_SHORT.mp3", "voice_FINAL.mp3", "voice_SHORT.m4a", "voice_FINAL.m4a")
    for name in names:
        candidate = audio_dir / name
        if candidate.exists():
            return candidate
    return next(iter(sorted(audio_dir.glob("voice*.wav"))), None) or next(iter(sorted(audio_dir.glob("voice*.mp3"))), None)


def caption_file(episode: Path, format_name: str) -> Path | None:
    audio_dir = episode / "02_audio"
    names = ("captions.srt", "captions_full.srt", "captions.vtt") if format_name == "long" else ("captions_SHORT.srt", "captions_KARA.ass", "captions.srt", "captions_SHORT.vtt")
    for name in names:
        candidate = audio_dir / name
        if candidate.exists() and candidate.suffix.lower() in {".srt", ".vtt"}:
            return candidate
    return None


def map_blocks(episode: Path) -> list[dict]:
    path = episode / "01_roteiro" / "ROTEIRO_MAP.json"
    if not path.exists():
        return []
    data = read_json(path)
    blocks = data.get("blocks", []) if isinstance(data, dict) else []
    return [block for block in blocks if isinstance(block, dict) and str(block.get("beat", "")).strip()]


def block_type(block: dict) -> str:
    raw_beat = str(block.get("beat", ""))
    beat = "".join(character for character in unicodedata.normalize("NFD", raw_beat.upper()) if not unicodedata.combining(character))
    for key, scene_type in BEAT_TYPES.items():
        if key in beat:
            return scene_type
    return "cinematic-photo"


def short_text(value: object, limit: int = 110) -> str:
    text = " ".join(str(value or "").split())
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def load_visual_bible(contracts: dict, episode: Path | None = None) -> dict:
    if episode:
        profile = episode / "01_roteiro" / "VISUAL_BIBLE.json"
        if profile.exists():
            value = read_json(profile)
            if not isinstance(value, dict):
                raise ValueError("invalid_visual_profile")
            return value
    visual = contracts.get("visual")
    return visual if isinstance(visual, dict) else {}


def load_shot_specs(episode: Path) -> list[dict]:
    path = episode / "01_roteiro" / "SHOT_SPECS.json"
    plan_path = episode / "01_roteiro" / "PROMPT_PLAN.json"
    specs_data = read_json(path) if path.exists() else {}
    plan_data = read_json(plan_path) if plan_path.exists() else {}
    specs = specs_data.get("shots", []) if isinstance(specs_data, dict) else specs_data
    planned = plan_data.get("shots", []) if isinstance(plan_data, dict) else []
    if not isinstance(specs, list):
        specs = []
    if not isinstance(planned, list):
        planned = []
    planned_by_prompt = {str(shot.get("promptId")): shot for shot in planned if isinstance(shot, dict) and shot.get("promptId")}
    planned_by_shot = {str(shot.get("shotId")): shot for shot in planned if isinstance(shot, dict) and shot.get("shotId")}
    merged = []
    for shot in specs:
        if not isinstance(shot, dict):
            continue
        prompt_id = str(shot.get("promptId") or "")
        shot_id = str(shot.get("shotId") or "")
        overlay = planned_by_prompt.get(prompt_id) or planned_by_shot.get(shot_id)
        merged.append({**shot, **overlay} if isinstance(overlay, dict) else shot)
    known = {(str(shot.get("promptId")), str(shot.get("shotId"))) for shot in merged}
    for shot in planned:
        if not isinstance(shot, dict):
            continue
        identity = (str(shot.get("promptId")), str(shot.get("shotId")))
        if identity not in known:
            merged.append(shot)
            known.add(identity)
    return merged


def prompt_plan_status(episode: Path) -> str:
    path = episode / "01_roteiro" / "PROMPT_PLAN.json"
    if not path.exists():
        return "MISSING"
    try:
        return str(read_json(path).get("status", "MISSING"))
    except ValueError:
        return "INVALID"


def scene_blocks(episode: Path, total: float, format_name: str, shot_specs: list[dict] | None = None) -> list[dict]:
    blocks = map_blocks(episode)
    if not blocks:
        images = image_files(episode)
        if not images:
            raise FileNotFoundError(f"no_visual_or_map:{episode}")
        motion = read_json(episode / "motion.json") if (episode / "motion.json").exists() else {}
        duration = float(motion.get("default_clip_len", 7.0))
        blocks = [{"id": f"IMG{index:03d}", "beat": "HOOK" if index == 1 else "CONTEXTO", "question": "O que este beat mostra?", "state_change": "A imagem revela uma mudança.", "target_seconds": duration} for index in range(1, len(images) + 1)]
    if total <= 0:
        total = sum(float(block.get("target_seconds", 0) or 0) for block in blocks) or 8.0
    timings, timed_blocks = parse_timing(episode / "02_audio" / "captions_times.json")
    if timings > 0 and len(timed_blocks) == len(blocks):
        measures = timed_blocks
    else:
        targets = [max(1.0, float(block.get("target_seconds", 0) or 0)) for block in blocks]
        scale = total / sum(targets)
        measures = [{"start": sum(targets[:index]) * scale, "end": sum(targets[: index + 1]) * scale, "dur": target * scale} for index, target in enumerate(targets)]
    specs_by_block = {}
    for spec in shot_specs or []:
        if not isinstance(spec, dict):
            continue
        source_block_ids = [str(value) for value in spec.get("sourceBlockIds", [])]
        for block_id in source_block_ids:
            existing = specs_by_block.get(block_id)
            if existing and existing.get("promptId") != spec.get("promptId"):
                raise ValueError(f"conflicting_shot_spec:{block_id}")
            specs_by_block[block_id] = spec
    scenes = []
    for index, (block, measure) in enumerate(zip(blocks, measures), 1):
        beat = str(block.get("beat", ""))
        block_id = str(block.get("id") or f"scene-{index:03d}")
        spec = specs_by_block.get(block_id, {})
        editorial = spec.get("editorial", {}) if isinstance(spec, dict) else {}
        visual = spec.get("visual", {}) if isinstance(spec, dict) else {}
        scene_type = visual.get("sceneType") or editorial.get("function") or block_type(block)
        motion_contract = spec.get("motionPrompt", {}) if isinstance(spec.get("motionPrompt"), dict) else {}
        states = spec.get("states") or []
        state_motion = next((str(state.get("motion")) for state in states if isinstance(state, dict) and state.get("motion")), "controlled-crop")
        transitions = motion_contract.get("transitions", {}) if isinstance(motion_contract.get("transitions"), dict) else {}
        source_block_ids = [str(value) for value in spec.get("sourceBlockIds", [block_id])] or [block_id]
        scene_id = str(spec.get("shotId") or block_id)
        question = str(spec.get("question") or block.get("question") or "")
        state_change = str(spec.get("stateChange") or block.get("state_change") or block.get("stateChange") or "")
        scene = {
            "id": scene_id,
            "shotId": scene_id,
            "type": scene_type,
            "purpose": str(spec.get("purpose") or editorial.get("purpose") or beat),
            "question": question,
            "stateChange": state_change,
            "classification": str(spec.get("classification") or "MIXED"),
            "subject": str(spec.get("subject") or ""),
            "setting": str(spec.get("setting") or ""),
            "composition": spec.get("composition") or "",
            "layers": [str(value) for value in spec.get("layers", [])],
            "startSeconds": round(max(0.0, float(measure["start"])), 3),
            "durationSeconds": round(max(0.5, float(measure["end"] - measure["start"])), 3),
            "sourceBlockIds": source_block_ids,
            "claimIds": [str(value) for value in spec.get("claimIds", block.get("claim_ids", []))],
            "sourceIds": [str(value) for value in spec.get("sourceIds", [])],
            "promptId": str(spec.get("promptId")) if spec.get("promptId") else "",
            "safeAreas": spec.get("safeAreas", {}),
            "negativeGuards": [str(value) for value in spec.get("negativeGuards", [])],
            "continuity": spec.get("continuity", {}),
            "imagePrompt": spec.get("imagePrompt", {}),
            "motionPrompt": motion_contract,
            "cropPolicy": spec.get("cropPolicy", {}),
            "assets": [dict(asset) for asset in spec.get("assets", []) if isinstance(asset, dict)],
            "headline": short_text(visual.get("headline") or question or spec.get("purpose"), 86),
            "body": state_change,
            "metadata": {
                "label": beat or "DOCUMENTARY",
                "source": "PROMPT_PLAN.json" if spec else "ROTEIRO_MAP.json",
                "stateCount": str(len(states)),
                "classification": str(spec.get("classification") or "MIXED"),
                "claimIds": ",".join(str(value) for value in spec.get("claimIds", [])),
                "sourceIds": ",".join(str(value) for value in spec.get("sourceIds", [])),
            },
            "motionVariant": state_motion,
            "motionIntent": state_change or str(motion_contract.get("cameraPath", {}).get("description", "")),
            "transitionIn": str(transitions.get("in") or spec.get("transitionIn") or "cut"),
            "transitionOut": str(transitions.get("out") or spec.get("transitionOut") or "cut"),
            "states": states,
        }
        scenes.append(scene)
    if scenes and scenes[-1]["startSeconds"] + scenes[-1]["durationSeconds"] < total:
        scenes[-1]["durationSeconds"] = round(total - scenes[-1]["startSeconds"], 3)
    return scenes


def stage_assets(episode: Path, public_dir: Path, audio: Path | None, style: dict, records: list[dict] | None = None, clean: bool = True) -> tuple[dict, dict[str, Path], list[Path]]:
    if clean and public_dir.exists():
        shutil.rmtree(public_dir)
    public_dir.mkdir(parents=True, exist_ok=True)
    staged = {}
    ledger = []
    for record in sorted(records or [], key=lambda value: str(value.get("assetId") or "")):
        asset_id = str(record.get("assetId") or "")
        prompt_id = str(record.get("promptId") or "")
        shot_id = str(record.get("shotId") or "")
        raw_path = str(record.get("path") or record.get("file") or "")
        if not asset_id or not prompt_id or not shot_id or not raw_path or record.get("blocked") is True:
            continue
        if not asset_path_is_safe(episode / "03_imagens", raw_path):
            raise ValueError(f"asset_path_unsafe:{asset_id}")
        source = Path(raw_path).expanduser()
        if not source.is_absolute():
            source = episode / "03_imagens" / source
        if not source.exists() or not source.is_file():
            raise FileNotFoundError(f"asset_file_missing:{asset_id}:{source}")
        source_hash = sha256(source)
        recorded_hash = str(record.get("hash") or "").strip().lower().removeprefix("sha256:")
        if recorded_hash and recorded_hash != source_hash:
            raise ValueError(f"asset_hash_mismatch:{asset_id}")
        target = public_dir / "images" / f"{asset_id}{source.suffix.lower()}"
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists() or target.stat().st_size != source.stat().st_size or sha256(target) != source_hash:
            shutil.copy2(source, target)
        staged[asset_id] = target
        ledger.append({
            "assetId": asset_id,
            "promptId": prompt_id,
            "shotId": shot_id,
            "path": target.relative_to(public_dir).as_posix(),
            "layer": record.get("layer"),
            "role": record.get("role") or "primary",
            "kind": record.get("kind") or source.suffix.lstrip("."),
            "sourceHash": source_hash,
            "hash": source_hash,
            "rightsStatus": record.get("rightsStatus"),
            "origin": record.get("origin"),
            "blocked": False,
            "sourceBlockIds": [str(value) for value in record.get("sourceBlockIds", [])],
        })
        if not ledger[-1].get("layer"):
            ledger[-1].pop("layer", None)
    audio_target = None
    if audio:
        if not audio.exists() or not audio.is_file():
            raise FileNotFoundError(f"audio_file_missing:{audio}")
        audio_target = public_dir / "audio" / audio.name
        audio_target.parent.mkdir(parents=True, exist_ok=True)
        if not audio_target.exists() or audio_target.stat().st_size != audio.stat().st_size or sha256(audio_target) != sha256(audio):
            shutil.copy2(audio, audio_target)
    font_sources = []
    remotion_fonts = style.get("remotion", {}).get("fonts", []) if isinstance(style.get("remotion"), dict) else []
    for value in remotion_fonts:
        if isinstance(value, str):
            candidate = Path(value).expanduser()
            if not candidate.is_absolute():
                candidate = episode.parent / value
            if candidate.exists() and candidate.suffix.lower() in {".ttf", ".otf", ".woff", ".woff2"}:
                font_sources.append(candidate)
    for index, font in enumerate(font_sources, 1):
        target = public_dir / "fonts" / f"{index:02d}-{font.name}"
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists() or sha256(target) != sha256(font):
            shutil.copy2(font, target)
    write_json(public_dir / "asset_ledger.json", {"version": 1, "assets": ledger})
    return ({"audio": audio_target} if audio_target else {}), staged, font_sources


def source_hash_map(episode: Path, contracts: dict, audio: Path | None, assets: dict[str, Path] | None = None, records: list[dict] | None = None) -> dict:
    result = {}
    for relative_path in (
        "01_roteiro/PESQUISA_BRIEF.md",
        "01_roteiro/PESQUISA_FONTE.md",
        "01_roteiro/CLAIMS.json",
        "01_roteiro/LINHA_DO_TEMPO.md",
        "01_roteiro/ROTEIRO_MAP.json",
        "01_roteiro/SHOT_SPECS.json",
        "01_roteiro/PROMPT_PLAN.json",
        "01_roteiro/TIMING_AUDIT.json",
        "01_roteiro/VISUAL_BIBLE.json",
        "01_roteiro/IMAGE_AUDIT.json",
        "01_roteiro/AUDIO_AUDIT.json",
        "02_audio/voice_FINAL.wav",
        "02_audio/captions.srt",
        "03_imagens/ASSET_MANIFEST.json",
    ):
        path = episode / relative_path
        if path.exists():
            result[relative_path] = sha256(path)
    if audio and audio.exists():
        result[relative_to_episode(audio, episode)] = sha256(audio)
    for name, data in contracts.items():
        result[f"contract:{name}"] = hash_json(data)
    for asset_id, asset in sorted((assets or {}).items()):
        result[f"asset:{asset_id}"] = sha256(asset)
    for record in records or []:
        asset_id = str(record.get("assetId") or "")
        raw_path = str(record.get("path") or record.get("file") or "")
        if asset_id and raw_path and not record.get("blocked"):
            source = Path(raw_path).expanduser()
            if not source.is_absolute():
                source = episode / "03_imagens" / source
            if source.exists() and source.is_file():
                result[f"source_asset:{asset_id}"] = sha256(source)
    return result


def research_gate(episode: Path) -> tuple[dict, dict, dict, dict]:
    try:
        import visual_plan
        context = visual_plan.load_research(episode)
        errors = list(context.get("errors", []))
        blocks = context.get("blocks", [])
        claims = context.get("claims", [])
    except (ImportError, OSError, ValueError, TypeError):
        context = {}
        errors = ["research_context_invalid"]
        blocks = []
        claims = []
    research_errors = [error for error in errors if any(token in error for token in ("PESQUISA_BRIEF", "PESQUISA_FONTE", "LINHA_DO_TEMPO", "research_context"))]
    map_errors = [error for error in errors if "ROTEIRO_MAP" in error or "block" in error]
    claim_errors = [error for error in errors if "CLAIMS" in error or "claim" in error or "source" in error]
    if not research_errors and not blocks:
        research_errors.append("research_map_missing")
    if not claims:
        claim_errors.append("claims_missing")
    if not blocks:
        map_errors.append("map_blocks_missing")
    return (
        gate("research", "PASS" if not research_errors else "FAIL", research_errors),
        gate("map", "PASS" if not map_errors else "FAIL", map_errors),
        gate("claims", "PASS" if not claim_errors else "FAIL", claim_errors),
        context,
    )


def shot_spec_gate(episode: Path) -> dict:
    path = episode / "01_roteiro" / "SHOT_SPECS.json"
    data = read_optional_json(path)
    shots = data.get("shots", []) if isinstance(data, dict) else data
    errors = []
    if not isinstance(shots, list) or not shots:
        errors.append("shot_specs_missing")
    else:
        try:
            import visual_plan
            for index, shot in enumerate(shots, 1):
                if not isinstance(shot, dict):
                    errors.append(f"shot_spec_invalid:{index}")
                    continue
                for field in ("shotId", "promptId", "sourceBlockIds", "claimIds", "sourceIds", "imagePrompt", "motionPrompt", "states"):
                    if field not in shot or shot[field] in (None, "", [], {}):
                        errors.append(f"shot_spec_missing:{index}:{field}")
                errors.extend(f"shot_spec_invalid:{index}:{error}" for error in visual_plan.validate_shot(shot))
        except ImportError:
            pass
    return gate("shotSpecs", "PASS" if not errors else "FAIL", sorted(set(errors)), path=str(path))


def prompt_plan_gate(episode: Path) -> tuple[dict, dict]:
    path = episode / "01_roteiro" / "PROMPT_PLAN.json"
    data = read_optional_json(path)
    errors = []
    if not isinstance(data, dict):
        errors.append("prompt_plan_missing")
        return gate("promptPlan", "FAIL", errors, path=str(path)), {}
    if data.get("status") != "PROMPTS_READY":
        errors.append(f"prompt_plan_status:{data.get('status', 'MISSING')}")
    errors.extend(str(error) for error in data.get("errors", []) if error)
    prompts = data.get("prompts", [])
    shots = data.get("shots", [])
    if not isinstance(prompts, list) or not prompts:
        errors.append("prompt_plan_prompts_missing")
    if not isinstance(shots, list) or not shots:
        errors.append("prompt_plan_shots_missing")
    if isinstance(prompts, list):
        for index, prompt in enumerate(prompts, 1):
            if not isinstance(prompt, dict) or prompt.get("status") != "ready":
                errors.append(f"prompt_not_ready:{index}")
    if isinstance(shots, list) and shots:
        try:
            import visual_plan
            errors.extend(f"prompt_shot_invalid:{error}" for error in visual_plan.validate_shots(shots))
        except ImportError:
            pass
    errors = sorted(set(errors))
    return gate("promptPlan", "PASS" if not errors else "FAIL", errors, path=str(path)), data if isinstance(data, dict) else {}


def manifest_gates(episode: Path, prompt_data: dict) -> tuple[dict, dict, dict, list[dict]]:
    images_dir = episode / "03_imagens"
    prompt_path = episode / "01_roteiro" / "PROMPT_PLAN.json"
    prompts = prompt_data.get("prompts", []) if isinstance(prompt_data, dict) else []
    expected = len(prompts) if isinstance(prompts, list) else None
    try:
        records, load_errors = asset_tools.load_asset_records(images_dir, prompt_path)
        resolution = asset_tools.resolve_assets(images_dir, prompt_path, expected=expected)
    except (OSError, ValueError, TypeError, KeyError) as exc:
        records, load_errors = [], [f"asset_resolution_error:{exc}"]
        resolution = {"status": "FAIL", "errors": load_errors, "assets": []}
    errors = [str(error) for error in load_errors] + [str(error) for error in resolution.get("errors", [])]
    manifest_path = images_dir / "ASSET_MANIFEST.json"
    if not manifest_path.exists():
        errors.append("asset_manifest_missing")
    rights_errors = []
    asset_errors = []
    for record in resolution.get("assets", []):
        if record.get("blocked") is True:
            asset_errors.append(f"blocked_asset:{record.get('assetId')}")
        rights = str(record.get("rightsStatus") or "").strip().lower()
        if not rights or rights in {"pending", "unknown", "unverified", "unclear"}:
            rights_errors.append(f"rights_pending:{record.get('assetId')}")
        if record.get("status") != "PRESENT":
            asset_errors.append(f"asset_not_present:{record.get('assetId')}:{record.get('status')}")
    if not records:
        errors.append("asset_records_missing")
    manifest_result = gate("manifest", "PASS" if not errors and resolution.get("status") == "PASS" else "FAIL", errors, path=str(manifest_path))
    rights_result = gate("rights", "PASS" if not rights_errors else "FAIL", rights_errors)
    assets_result = gate("assets", "PASS" if not asset_errors and resolution.get("status") == "PASS" else "FAIL", asset_errors)
    return manifest_result, rights_result, assets_result, records


def captions_gate(episode: Path, format_name: str) -> tuple[dict, list[dict]]:
    path = caption_file(episode, format_name)
    errors = []
    captions = parse_srt(path) if path else []
    if not path:
        errors.append("captions_missing")
    if not captions:
        errors.append("captions_empty")
    if captions:
        if captions[0]["startSeconds"] > 1.0:
            errors.append("captions_start_late")
        for index, caption in enumerate(captions, 1):
            if caption["endSeconds"] <= caption["startSeconds"]:
                errors.append(f"caption_invalid:{index}")
    return gate("captions", "PASS" if not errors else "FAIL", errors, path=str(path) if path else ""), captions


def timing_gate(episode: Path) -> dict:
    path = episode / "01_roteiro" / "TIMING_AUDIT.json"
    data = read_optional_json(path)
    errors = [] if isinstance(data, dict) and data.get("status") == "PASS" else ["timing_audit_not_passed"]
    return gate("timing", "PASS" if not errors else "FAIL", errors, path=str(path))


def audio_gate(episode: Path, contracts: dict, format_name: str, required: bool | None = None) -> tuple[dict, Path | None]:
    if required is None:
        required = lane_requires_audio(contracts, format_name)
    if not required:
        return gate("audio", "PASS", [], notRequired=True), None
    audio = audio_file(episode, format_name)
    errors = []
    if not isinstance(contracts.get("voice"), dict) or not contracts.get("voice"):
        errors.append("voice_contract_missing")
    if not audio:
        errors.append("audio_missing")
    elif ffprobe_duration(audio) <= 0:
        errors.append("audio_duration_invalid")
    for name in ("AUDIO_AUDIT.json", "VOICE_AUDIT.json"):
        path = episode / "01_roteiro" / name
        if path.exists():
            data = read_optional_json(path)
            if not isinstance(data, dict) or data.get("status") != "PASS":
                errors.append(f"audio_audit_not_passed:{name}")
    return gate("audio", "PASS" if not errors else "FAIL", errors, path=str(audio) if audio else ""), audio


def visual_profile_gate(episode: Path, contracts: dict) -> tuple[dict, dict, str, Path | None]:
    errors = []
    try:
        visual, path, profile_hash = visual_profile(episode, contracts)
    except ValueError:
        visual, path, profile_hash = {}, None, ""
        errors.append("visual_profile_invalid")
    if not visual:
        errors.append("visual_profile_missing")
    else:
        try:
            version = int(visual.get("version", 0) or 0)
        except (TypeError, ValueError):
            version = 0
        if version < 2:
            errors.append("visual_profile_version_invalid")
    if not any(key in visual for key in ("palette", "theme", "safeAreas", "image", "motion")):
        errors.append("visual_profile_incomplete")
    return gate("visualProfile", "PASS" if not errors else "FAIL", errors, path=str(path) if path else ""), visual, profile_hash, path


def review_gate_for_plan(episode: Path, format_name: str, required: bool) -> dict:
    if not required:
        return gate("review", "REVIEW_REQUIRED", ["review_pending"])
    result = review_gate(episode, format_name)
    return gate("review", result.get("status", "FAIL"), result.get("errors", []), path=result.get("path", ""), receipt=result.get("receipt", ""))


def validate_production_gates(episode: Path, format_name: str = "long", contracts: dict | None = None, require_review: bool = True, audio_required: bool | None = None) -> dict:
    episode = Path(episode)
    contracts = contracts or {}
    results = {}
    research, map_result, claims, _ = research_gate(episode)
    results["research"] = research
    results["map"] = map_result
    results["claims"] = claims
    results["shotSpecs"] = shot_spec_gate(episode)
    prompt_result, prompt_data = prompt_plan_gate(episode)
    results["promptPlan"] = prompt_result
    manifest_result, rights_result, assets_result, records = manifest_gates(episode, prompt_data)
    results["manifest"] = manifest_result
    results["rights"] = rights_result
    results["assets"] = assets_result
    image_result = image_audit_gate(episode / "03_imagens")
    results["imageAudit"] = gate("imageAudit", image_result.get("status", "FAIL"), image_result.get("errors", []), path=image_result.get("path", ""))
    caption_result, captions = captions_gate(episode, format_name)
    results["captions"] = caption_result
    results["timing"] = timing_gate(episode)
    audio_result, audio = audio_gate(episode, contracts, format_name, audio_required)
    results["audio"] = audio_result
    visual_result, visual, profile_hash, profile_path = visual_profile_gate(episode, contracts)
    results["visualProfile"] = visual_result
    results["review"] = review_gate_for_plan(episode, format_name, require_review)
    errors = []
    for result in results.values():
        errors.extend(result.get("errors", []))
    release_names = [name for name in REQUIRED_GATES if name != "review"]
    release_pass = all(results.get(name, {}).get("status") == "PASS" for name in release_names)
    release_pass = release_pass and (results["review"].get("status") == "PASS" if require_review else True)
    return {
        "status": "PASS" if not errors or (not require_review and all(not results.get(name, {}).get("errors") for name in release_names)) else "FAIL",
        "releaseEligible": release_pass,
        "errors": sorted(set(errors)),
        "gates": results,
        "promptData": prompt_data,
        "records": records,
        "audio": str(audio) if audio else None,
        "captions": captions,
        "visual": visual,
        "profileHash": profile_hash,
        "profilePath": str(profile_path) if profile_path else "",
    }


def validate_release_gates(episode: Path, format_name: str = "long", contracts: dict | None = None, audio_required: bool | None = None) -> dict:
    return validate_production_gates(episode, format_name, contracts, require_review=True, audio_required=audio_required)


def build_plan(episode: Path, channel: str | None, format_name: str, contracts: dict, allow_incomplete: bool = False) -> dict:
    episode = Path(episode).resolve()
    for name in ("style", "motion", "voice", "roteiro"):
        if name in contracts and not isinstance(contracts.get(name), dict):
            raise ValueError(f"{name}_contract_invalid")
    style = contracts.get("style") if isinstance(contracts.get("style"), dict) else {}
    raw_motion = contracts.get("motion") if isinstance(contracts.get("motion"), dict) else {}
    engine = str(raw_motion.get("engine", "remotion") or "remotion").lower()
    if engine == "legacy":
        raise ValueError("legacy_visual_renderer_forbidden")
    if engine != "remotion":
        raise ValueError(f"invalid_visual_renderer:{engine}")
    motion = dict(raw_motion)
    motion["engine"] = "remotion"
    visual, profile_path, profile_hash = visual_profile(episode, contracts)
    gate_report = validate_production_gates(episode, format_name, contracts, require_review=False)
    if not gate_report.get("releaseEligible") and not allow_incomplete:
        raise ValueError("production_gates_failed:" + ",".join(gate_report.get("errors", [])))
    shot_specs = load_shot_specs(episode)
    audio_value = gate_report.get("audio")
    audio = Path(str(audio_value)) if audio_value else None
    audio_seconds = ffprobe_duration(audio) if audio else 0.0
    captions = gate_report.get("captions") or []
    if not audio_seconds and captions:
        audio_seconds = max(caption["endSeconds"] for caption in captions)
    scenes = []
    if map_blocks(episode) and shot_specs:
        scenes = scene_blocks(episode, audio_seconds, format_name, shot_specs)
    elif allow_incomplete and not map_blocks(episode):
        images = image_files(episode)
        if images:
            duration = float(motion.get("default_clip_len", 7.0) or 7.0)
            scenes = [{"id": f"DIAGNOSTIC-{index:03d}", "shotId": f"DIAGNOSTIC-{index:03d}", "type": "cinematic-photo", "purpose": "diagnostic", "question": "", "stateChange": "", "classification": "MIXED", "subject": "", "setting": "", "composition": "", "layers": [], "startSeconds": 0.0, "durationSeconds": duration, "sourceBlockIds": [], "claimIds": [], "sourceIds": [], "promptId": "", "safeAreas": {}, "negativeGuards": [], "continuity": {}, "imagePrompt": {}, "motionPrompt": {}, "cropPolicy": {}, "assets": [], "states": []} for index, _ in enumerate(images, 1)]
    total = audio_seconds or (max((scene["startSeconds"] + scene["durationSeconds"] for scene in scenes), default=8.0))
    records = gate_report.get("records") or []
    if not records:
        records, _ = asset_tools.load_asset_records(episode / "03_imagens", episode / "01_roteiro" / "PROMPT_PLAN.json")
    input_hashes = source_hash_map(episode, contracts, audio, None, records)
    input_hashes["visualProfile"] = profile_hash
    input_hash = hash_json({"episode": episode.name, "format": format_name, "inputs": input_hashes})
    run_id = run_ledger.run_identity(episode, format_name, input_hash, profile_hash)
    run_dir = run_ledger.reserve_run_dir(episode, run_id)
    run_id = run_dir.name
    public_dir = run_dir / "public"
    _, staged, _ = stage_assets(episode, public_dir, audio, style, records)
    branding = dict(visual.get("branding", {})) if isinstance(visual.get("branding", {}), dict) else {}
    watermark_source = branding.get("watermark")
    if watermark_source:
        source = Path(str(watermark_source)).expanduser()
        if not source.is_absolute():
            source = episode.parent.parent / source
        if source.exists() and source.is_file():
            watermark_target = public_dir / "brand" / f"watermark{source.suffix.lower()}"
            watermark_target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, watermark_target)
            branding["watermark"] = watermark_target.relative_to(public_dir).as_posix()
        else:
            branding.pop("watermark", None)
    size = motion.get("size", [1920, 1080])
    width, height = (size if format_name == "long" else [1080, 1920])
    render_config = motion.get("remotion", {}).get("render", {}) if isinstance(motion.get("remotion"), dict) else {}
    render_plan = {"codec": render_config.get("codec", "h264"), "audioCodec": render_config.get("audio_codec", render_config.get("audioCodec", "aac")), "crf": int(render_config.get("crf", 18)), "imageFormat": "jpeg", "jpegQuality": 92}
    asset_ledger_by_id = {}
    blocked_asset_ids = [str(record.get("assetId")) for record in records if record.get("blocked") is True and record.get("assetId")]
    for scene in scenes:
        matches = [record for record in records if str(record.get("promptId") or "") == str(scene.get("promptId") or "") and str(record.get("shotId") or "") == str(scene.get("shotId") or "") and record.get("blocked") is not True and str(record.get("path") or record.get("file") or "")]
        scene_assets = []
        for record in sorted(matches, key=lambda value: str(value.get("assetId") or "")):
            asset_id = str(record.get("assetId") or "")
            staged_path = staged.get(asset_id)
            if not staged_path:
                continue
            asset_ref = {
                "assetId": asset_id,
                "promptId": str(record.get("promptId") or ""),
                "shotId": str(record.get("shotId") or ""),
                "path": staged_path.relative_to(public_dir).as_posix(),
                "role": str(record.get("role") or "primary"),
                "layer": record.get("layer"),
                "kind": str(record.get("kind") or staged_path.suffix.lstrip(".")),
                "origin": str(record.get("origin") or "synthetic-or-licensed"),
                "rightsStatus": record.get("rightsStatus"),
                "hash": sha256(staged_path),
                "blocked": False,
                "sourceBlockIds": [str(value) for value in record.get("sourceBlockIds", scene.get("sourceBlockIds", []))],
            }
            if not asset_ref.get("layer"):
                asset_ref.pop("layer", None)
            scene_assets.append(asset_ref)
            asset_ledger_by_id.setdefault(asset_id, asset_ref)
        scene["assets"] = scene_assets
        primary = next((asset for asset in scene_assets if asset.get("role") == "primary"), None)
        supporting = next((asset for asset in scene_assets if asset.get("role") == "supporting"), None)
        if primary:
            scene["asset"] = primary["path"]
            for state in scene.get("states", []):
                available = {asset["assetId"] for asset in scene_assets}
                requested = [asset_id for asset_id in state.get("assetIds", []) if asset_id in available]
                if requested:
                    state["assetIds"] = requested
                elif allow_incomplete:
                    state["assetIds"] = [primary["assetId"]]
                else:
                    raise ValueError(f"state_asset_binding_missing:{scene.get('promptId')}:{scene.get('shotId')}:{state.get('id')}")
        if supporting:
            scene["secondaryAsset"] = supporting["path"]
        if not allow_incomplete and not primary:
            raise FileNotFoundError(f"primary_asset_missing:{scene.get('promptId')}:{scene.get('shotId')}")
    audio_plan = {"src": f"audio/{audio.name}", "volume": 1.0} if audio else None
    release_eligible = bool(gate_report.get("releaseEligible")) and not allow_incomplete
    plan = {
        "version": 2,
        "engine": "remotion",
        "diagnostic": bool(allow_incomplete),
        "releaseEligible": release_eligible,
        "runId": run_id,
        "profileHash": profile_hash,
        "inputHash": input_hash,
        "audioRequired": lane_requires_audio(contracts, format_name),
        "voiceContractHash": hash_json(contracts["voice"]) if isinstance(contracts.get("voice"), dict) and contracts.get("voice") else "",
        "staging": {"path": relative_to_episode(public_dir, episode), "publicDir": relative_to_episode(public_dir, episode), "assetLedger": "public/asset_ledger.json"},
        "runLedger": relative_to_episode(run_dir / "run.json", episode),
        "visualProfile": {"path": relative_to_episode(profile_path, episode) if profile_path else "", "hash": profile_hash},
        "gates": gate_report.get("gates", {}),
        "gateErrors": gate_report.get("errors", []),
        "channel": channel or episode.parent.name,
        "episode": episode.name,
        "format": format_name,
        "video": {"width": int(width), "height": int(height), "fps": int(motion.get("fps", 30) or 30), "durationSeconds": round(max(0.1, float(total)), 3)},
        "captions": captions,
        "theme": theme_from_style(style, visual),
        "visualBible": visual,
        "render": render_plan,
        "branding": branding,
        "contractVersions": {name: hash_json(data) for name, data in contracts.items()},
        "assetLedger": list(asset_ledger_by_id.values()),
        "blockedAssetIds": blocked_asset_ids,
        "scenes": scenes,
        "sources": source_hash_map(episode, contracts, audio, staged, records),
    }
    if audio_plan:
        plan["audio"] = audio_plan
    captions_path = caption_file(episode, format_name)
    if captions_path:
        plan["sources"]["captions"] = f"captions/{captions_path.name}"
    destination = plan_path(episode, format_name)
    write_json(destination, plan)
    run_ledger.create_run(episode, format_name, run_id, run_dir, input_hashes, {}, sha256(destination), profile_hash, {name: result.get("status", "FAIL") for name, result in gate_report.get("gates", {}).items()}, destination, public_dir, REMOTION_ROOT)
    run_ledger.append_event(run_dir, "plan_created", status="PLANNED", gates={name: result.get("status", "FAIL") for name, result in gate_report.get("gates", {}).items()})
    return plan


def plan_path(episode: Path, format_name: str) -> Path:

    return episode / "01_roteiro" / f"RENDER_PLAN_{format_name.upper()}.json"


def plan_command(args) -> int:
    root = Path(args.root).expanduser().resolve()
    episode = (root / args.episode).resolve()
    contracts = load_contract(root, args.channel, args.allow_defaults or args.allow_incomplete)
    plan = build_plan(episode, args.channel, args.format, contracts, args.allow_incomplete)
    destination = plan_path(episode, args.format)
    write_json(destination, plan)
    print(json.dumps({"status": "DIAGNOSTIC" if plan.get("diagnostic") else "PASS", "plan": str(destination), "scenes": len(plan["scenes"]), "assets": len(plan["sources"])}, ensure_ascii=False))
    return 0


def plan_env(episode: Path, format_name: str) -> dict[str, str]:
    plan_file = plan_path(episode, format_name)
    plan = read_json(plan_file)
    run_dir = run_dir_from_plan(plan, episode)
    public = run_dir / "public"
    if not public.exists():
        raise FileNotFoundError(f"render_staging_missing:{public}")
    return {"DARK_MASTER_RENDER_PLAN": str(plan_file), "DARK_MASTER_PUBLIC_DIR": str(public)}


def remotion_command(command: str, args: list[str], episode: Path, format_name: str, extra: dict[str, str] | None = None) -> subprocess.CompletedProcess:
    env = {**plan_env(episode, format_name), **(extra or {})}
    return run_command([npm_command(), "--prefix", str(REMOTION_ROOT), "run", command, "--", *args], REMOTION_ROOT, env)


def staging_integrity(plan: dict, episode: Path) -> dict:
    errors = []
    try:
        run_dir = run_dir_from_plan(plan, episode)
        public = run_dir / "public"
        run = run_ledger.load_run(run_dir)
    except (FileNotFoundError, ValueError, OSError) as exc:
        return {"status": "FAIL", "errors": [str(exc)], "public": "", "run": {}}
    if not public.exists():
        errors.append("staging_missing")
    if run.get("runId") != plan.get("runId"):
        errors.append("run_id_mismatch")
    if run.get("planHash") != plan_hash(plan_path(episode, str(plan.get("format") or "long"))):
        errors.append("run_plan_hash_mismatch")
    ledger_path = public / "asset_ledger.json"
    ledger = read_optional_json(ledger_path)
    assets = ledger.get("assets", []) if isinstance(ledger, dict) else []
    if not isinstance(assets, list):
        assets = []
        errors.append("staging_asset_ledger_invalid")
    blocked = {str(value) for value in plan.get("blockedAssetIds", [])}
    staged_paths = set()
    for asset in assets:
        if not isinstance(asset, dict):
            errors.append("staging_asset_invalid")
            continue
        asset_id = str(asset.get("assetId") or "")
        if not asset_id or asset.get("blocked") is True or asset_id in blocked:
            errors.append(f"blocked_asset_in_staging:{asset_id}")
            continue
        raw_path = str(asset.get("path") or "")
        path = public / raw_path
        if not raw_path or Path(raw_path).is_absolute() or ".." in Path(raw_path).parts:
            errors.append(f"staging_asset_path_invalid:{asset_id}")
            continue
        if not path.exists() or not path.is_file():
            errors.append(f"staging_asset_file_missing:{asset_id}")
            continue
        expected_hash = str(asset.get("hash") or asset.get("sourceHash") or "")
        if not expected_hash or sha256(path) != expected_hash:
            errors.append(f"staging_asset_hash_mismatch:{asset_id}")
        staged_paths.add(path.resolve())
    for asset in plan.get("assetLedger", []):
        if not isinstance(asset, dict):
            continue
        asset_id = str(asset.get("assetId") or "")
        raw_path = str(asset.get("path") or "")
        path = public / raw_path
        if asset_id in blocked or not raw_path or not path.exists() or not path.is_file():
            errors.append(f"plan_asset_not_staged:{asset_id}")
        elif str(asset.get("hash") or "") != sha256(path):
            errors.append(f"plan_asset_hash_mismatch:{asset_id}")
    images_dir = public / "images"
    actual_paths = {path.resolve() for path in images_dir.rglob("*") if path.is_file()} if images_dir.exists() else set()
    if actual_paths != staged_paths:
        errors.append("staging_unlisted_asset")
    if blocked & {path.stem for path in actual_paths}:
        errors.append("blocked_asset_filename_in_staging")
    return {"status": "FAIL" if errors else "PASS", "errors": sorted(set(errors)), "public": str(public), "run": run, "runDir": str(run_dir), "assets": assets}


def release_validation(episode: Path, format_name: str, contracts: dict | None = None) -> dict:
    plan_file = plan_path(episode, format_name)
    errors = []
    if not plan_file.exists():
        return {"status": "FAIL", "errors": ["render_plan_missing"]}
    try:
        plan = read_json(plan_file)
    except ValueError:
        return {"status": "FAIL", "errors": ["render_plan_invalid"]}
    if plan.get("engine") != "remotion":
        errors.append("renderer_not_remotion")
    if plan.get("diagnostic") or not plan.get("releaseEligible"):
        errors.append("diagnostic_plan_not_renderable")
    validation_contracts = contracts
    if validation_contracts is None and plan.get("voiceContractHash"):
        validation_contracts = {"voice": {"contractHash": plan["voiceContractHash"]}}
    gate_report = validate_production_gates(episode, format_name, validation_contracts, require_review=True, audio_required=plan.get("audioRequired") if isinstance(plan.get("audioRequired"), bool) else None)
    if gate_report.get("status") != "PASS" or not gate_report.get("releaseEligible"):
        errors.extend(gate_report.get("errors", []))
    review = review_gate(episode, format_name, plan_file)
    if review.get("status") != "PASS":
        errors.extend(review.get("errors", []))
    staging = staging_integrity(plan, episode)
    errors.extend(staging.get("errors", []))
    return {"status": "FAIL" if errors else "PASS", "errors": sorted(set(errors)), "plan": plan, "staging": staging, "review": review, "gates": gate_report.get("gates", {})}


def expected_output_path(episode: Path, format_name: str) -> Path:
    return episode / "04_video_final" / f"{episode.name}_{format_name.upper()}_REMOTION.mp4"


def file_contains_token(path: Path, token: str) -> bool:
    if not token or not path.exists():
        return False
    needle = token.encode("utf-8")
    with path.open("rb") as handle:
        carry = b""
        while True:
            chunk = handle.read(1024 * 1024)
            if not chunk:
                return False
            data = carry + chunk
            if needle in data:
                return True
            carry = data[-max(1, len(needle) - 1):]


def audit_render_outputs(episode: Path, format_name: str | None = None) -> dict:
    script_dir = episode / "01_roteiro"
    formats = [format_name] if format_name else [path.stem.removeprefix("RENDER_PLAN_").lower() for path in sorted(script_dir.glob("RENDER_PLAN_*.json"))]
    errors = []
    checked = []
    if not formats:
        return {"status": "FAIL", "errors": ["render_plan_missing"], "formats": []}
    for current_format in formats:
        plan_file = plan_path(episode, current_format)
        report_file = script_dir / f"RENDER_REPORT_{current_format.upper()}.json"
        output = expected_output_path(episode, current_format)
        current_errors = []
        if not plan_file.exists():
            current_errors.append("render_plan_missing")
            plan = {}
        else:
            try:
                plan = read_json(plan_file)
            except ValueError:
                plan = {}
                current_errors.append("render_plan_invalid")
        if not report_file.exists():
            current_errors.append("render_report_missing")
            report = {}
        else:
            try:
                report = read_json(report_file)
            except ValueError:
                report = {}
                current_errors.append("render_report_invalid")
        if not output.exists():
            current_errors.append("render_output_missing")
        if plan:
            if plan.get("engine") != "remotion":
                current_errors.append("renderer_not_remotion")
            if plan.get("diagnostic") or not plan.get("releaseEligible"):
                current_errors.append("diagnostic_plan_in_output")
            if any(isinstance(asset, dict) and asset.get("blocked") is True for asset in plan.get("assetLedger", [])):
                current_errors.append("blocked_asset_in_plan")
            staging = staging_integrity(plan, episode)
            current_errors.extend(staging.get("errors", []))
            if staging.get("run", {}).get("profileHash") != plan.get("profileHash"):
                current_errors.append("run_profile_hash_mismatch")
            if staging.get("run", {}).get("planHash") != (sha256(plan_file) if plan_file.exists() else ""):
                current_errors.append("run_plan_hash_mismatch")
            validation_contracts = {"voice": {"contractHash": plan["voiceContractHash"]}} if plan.get("voiceContractHash") else None
            gate_report = validate_production_gates(episode, current_format, validation_contracts, require_review=True, audio_required=plan.get("audioRequired") if isinstance(plan.get("audioRequired"), bool) else None)
            if gate_report.get("status") != "PASS" or not gate_report.get("releaseEligible"):
                current_errors.extend(gate_report.get("errors", []))
            current_errors.extend(review_gate(episode, current_format, plan_file).get("errors", []))
        if report:
            if report.get("planHash") != (sha256(plan_file) if plan_file.exists() else ""):
                current_errors.append("render_plan_hash_mismatch")
            if report.get("plan") != str(plan_file):
                current_errors.append("render_plan_path_mismatch")
            if report.get("runId") != plan.get("runId"):
                current_errors.append("render_run_id_mismatch")
            if report.get("profileHash") != plan.get("profileHash"):
                current_errors.append("render_profile_hash_mismatch")
            if report.get("inputHash") != plan.get("inputHash"):
                current_errors.append("render_input_hash_mismatch")
            if report.get("output") != str(output):
                current_errors.append("render_output_path_mismatch")
            if output.exists() and report.get("outputHash") != sha256(output):
                current_errors.append("render_output_hash_mismatch")
            outputs = report.get("outputs") if isinstance(report.get("outputs"), dict) else {}
            for output_path, output_hash in outputs.items():
                path = Path(str(output_path))
                if not path.is_absolute():
                    path = episode / path
                if not path.resolve().is_relative_to((episode / "04_video_final").resolve()):
                    current_errors.append("render_output_outside_final")
                elif not path.exists() or sha256(path) != str(output_hash):
                    current_errors.append("render_output_artifact_hash_mismatch")
            if not report.get("engine") or report.get("engine") != "remotion":
                current_errors.append("render_report_engine_invalid")
        if output.exists() and ffprobe_duration(output) <= 0:
            current_errors.append("render_duration_invalid")
        if output.exists() and any(blocked and (blocked in output.name or file_contains_token(output, blocked)) for blocked in plan.get("blockedAssetIds", [])):
            current_errors.append("blocked_asset_in_output")
        checked.append({"format": current_format, "plan": str(plan_file), "report": str(report_file), "output": str(output), "runId": plan.get("runId")})
        errors.extend(f"{current_format}:{error}" for error in current_errors)
    run_ids = {item.get("runId") for item in checked if item.get("runId")}
    if len(run_ids) > 1:
        errors.append("outputs_from_multiple_runs")
    tracked_outputs = {Path(item["output"]).resolve() for item in checked}
    final_dir = episode / "04_video_final"
    if final_dir.exists():
        for candidate in final_dir.glob("*_REMOTION.mp4"):
            if candidate.resolve() not in tracked_outputs:
                errors.append(f"untracked_render_output:{candidate.name}")
    return {"status": "FAIL" if errors else "PASS", "errors": sorted(set(errors)), "formats": checked, "runIds": sorted(run_ids)}


def still_command(args) -> int:
    root = Path(args.root).expanduser().resolve()
    episode = (root / args.episode).resolve()
    format_name = args.format
    plan_file = plan_path(episode, format_name)
    if not plan_file.exists():
        print(json.dumps({"status": "FAIL", "error": "render_plan_missing"}))
        return 1
    try:
        plan = read_json(plan_file)
        if plan.get("engine") != "remotion":
            raise ValueError("renderer_not_remotion")
        staging = staging_integrity(plan, episode)
        if staging.get("status") != "PASS":
            raise ValueError(";".join(staging.get("errors", [])))
    except (ValueError, KeyError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False))
        return 1
    frames = args.frame or [0.5, 2.5, 5.0, max(0.0, plan["video"]["durationSeconds"] - 0.1)]
    fps = int(plan["video"]["fps"])
    run_dir = run_dir_from_plan(plan, episode)
    output_dir = run_dir / "stills" / format_name
    for value in frames:
        frame = max(0, round(value * fps))
        output = output_dir / f"{value:.2f}.png"
        result = remotion_command("render:still", [format_name, str(frame)], episode, format_name, {"DARK_MASTER_STILL": str(output)})
        print(result.stdout.strip())
    return 0


def render_command(args) -> int:
    root = Path(args.root).expanduser().resolve()
    episode = (root / args.episode).resolve()
    format_name = args.format
    plan_file = plan_path(episode, format_name)
    final = expected_output_path(episode, format_name)
    report_file = episode / "01_roteiro" / f"RENDER_REPORT_{format_name.upper()}.json"
    if final.exists() or report_file.exists():
        conflict = final if final.exists() else report_file
        print(json.dumps({"status": "FAIL", "error": "output_exists", "output": str(conflict)}, ensure_ascii=False))
        return 1
    contracts = None
    if args.channel:
        try:
            contracts = load_contract(root, args.channel, getattr(args, "allow_defaults", False))
        except FileNotFoundError as exc:
            print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False))
            return 1
    validation = release_validation(episode, format_name, contracts)
    if validation.get("status") != "PASS":
        print(json.dumps({"status": "FAIL", "error": "release_gates_failed", "errors": validation.get("errors", [])}, ensure_ascii=False))
        return 1
    plan = validation["plan"]
    run_dir = run_dir_from_plan(plan, episode)
    try:
        result = remotion_command("render", [format_name], episode, format_name, {"DARK_MASTER_OUTPUT": str(final)})
    except (OSError, subprocess.CalledProcessError) as exc:
        run_ledger.append_run_event(run_dir, "render_failed", status="FAIL", output_hashes={}, gates=validation.get("gates", {}))
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False))
        return 1
    report = {
        "status": "PASS",
        "engine": "remotion",
        "format": format_name,
        "episode": episode.name,
        "runId": plan.get("runId"),
        "output": str(final),
        "outputs": {str(final): sha256(final)},
        "plan": str(plan_file),
        "planHash": sha256(plan_file),
        "profileHash": plan.get("profileHash", ""),
        "inputHash": plan.get("inputHash", ""),
        "outputHash": sha256(final),
        "command": result.stdout.strip(),
        "versions": run_ledger.versions(REMOTION_ROOT),
        "gates": validation.get("gates", {}),
    }
    report_file = episode / "01_roteiro" / f"RENDER_REPORT_{format_name.upper()}.json"
    write_json(report_file, report)
    run_ledger.append_run_event(run_dir, "render_completed", status="PASS", output_hashes={str(final): sha256(final)}, gates=validation.get("gates", {}))
    print(json.dumps(report, ensure_ascii=False))
    return 0


def audit_command(args) -> int:
    root = Path(args.root).expanduser().resolve()
    episode = (root / args.episode).resolve()
    result = audit_render_outputs(episode, args.format)
    output = expected_output_path(episode, args.format)
    result["output"] = str(output)
    result["durationSeconds"] = round(ffprobe_duration(output), 3) if output.exists() else 0.0
    print(json.dumps(result, ensure_ascii=False))
    return 1 if result.get("status") != "PASS" else 0


def doctor_command(args) -> int:
    root = Path(args.root).expanduser().resolve() if args.root else SKILL_ROOT
    try:
        load_contract(root, args.channel, args.allow_defaults)
        contract_status = "PASS"
    except FileNotFoundError as exc:
        contract_status = f"FAIL:{exc}"
    result = run_command([npm_command(), "--prefix", str(REMOTION_ROOT), "run", "doctor"], REMOTION_ROOT, check=False)
    print(result.stdout or result.stderr)
    print(json.dumps({"contract": contract_status, "remotionRoot": str(REMOTION_ROOT)}, ensure_ascii=False))
    return 0 if contract_status == "PASS" and result.returncode == 0 else 1


def add_common(parser):
    parser.add_argument("episode")
    parser.add_argument("--root", required=True)
    parser.add_argument("--channel")
    parser.add_argument("--format", choices=["long", "short"], default="long")


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    doctor = sub.add_parser("doctor")
    doctor.add_argument("--root")
    doctor.add_argument("--channel")
    doctor.add_argument("--allow-defaults", action="store_true")
    doctor.set_defaults(handler=doctor_command)
    plan = sub.add_parser("plan")
    add_common(plan)
    plan.add_argument("--allow-defaults", action="store_true")
    plan.add_argument("--allow-incomplete", action="store_true")
    plan.set_defaults(handler=plan_command)
    stills = sub.add_parser("stills")
    add_common(stills)
    stills.add_argument("--frame", action="append", type=float)
    stills.set_defaults(handler=still_command)
    render = sub.add_parser("render")
    add_common(render)
    render.add_argument("--overwrite", action="store_true")
    render.set_defaults(handler=render_command)
    audit = sub.add_parser("audit")
    add_common(audit)
    audit.set_defaults(handler=audit_command)
    args = parser.parse_args()
    try:
        return args.handler(args)
    except (FileNotFoundError, ValueError, subprocess.CalledProcessError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    sys.exit(main())
