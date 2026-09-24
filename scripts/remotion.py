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
        if len(lines) < 3 or "-->" not in lines[1]:
            continue
        start, end = [part.strip() for part in lines[1].split("-->", 1)]
        start_seconds = srt_seconds(start)
        end_seconds = srt_seconds(end)
        if start_seconds is None or end_seconds is None or end_seconds <= start_seconds:
            continue
        captions.append({"startSeconds": start_seconds, "endSeconds": end_seconds, "text": " ".join(lines[2:])})
    return captions


def srt_seconds(value: str) -> float | None:
    match = re.fullmatch(r"(\d{2}):(\d{2}):(\d{2})[,.](\d{3})", value)
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
        if candidate.is_dir() and (candidate / "profile.md").exists():
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
    required = ("style.json", "motion.json", "voice.json", "roteiro.json", "visual.json")
    for name in required:
        path = channel_dir / name if channel_dir else None
        if path and path.exists():
            contracts[name.removesuffix(".json")] = read_json(path)
        elif not allow_defaults and name == "visual.json" and contracts.get("motion", {}).get("engine") != "remotion":
            continue
        elif not allow_defaults:
            raise FileNotFoundError(f"missing_contract:{name}:{channel_dir}")
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
        key=lambda path: int(re.search(r"(\d+)", path.stem).group(1)) if re.search(r"(\d+)", path.stem) else 999,
    )


def audio_file(episode: Path, format_name: str) -> Path | None:
    audio_dir = episode / "02_audio"
    if not audio_dir.exists():
        return None
    names = ("voice_FINAL_SHORT.wav", "voice_SHORT.wav", "voice_FINAL.wav", "voice_V3_FINAL.wav")
    if format_name == "short":
        names = ("voice_SHORT.wav", "voice_FINAL_SHORT.wav", "voice_FINAL.wav", "voice_V3_FINAL.wav")
    for name in names:
        candidate = audio_dir / name
        if candidate.exists():
            return candidate
    return next(iter(sorted(audio_dir.glob("voice*.wav"))), None)


def caption_file(episode: Path, format_name: str) -> Path | None:
    audio_dir = episode / "02_audio"
    names = ("captions.srt", "captions_full.srt") if format_name == "long" else ("captions_SHORT.srt", "captions_KARA.ass", "captions.srt")
    for name in names:
        candidate = audio_dir / name
        if candidate.exists() and candidate.suffix.lower() == ".srt":
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


def load_visual_bible(contracts: dict) -> dict:
    visual = contracts.get("visual")
    return visual if isinstance(visual, dict) else {}


def load_shot_specs(episode: Path) -> list[dict]:
    path = episode / "01_roteiro" / "SHOT_SPECS.json"
    if not path.exists():
        return []
    data = read_json(path)
    shots = data.get("shots", []) if isinstance(data, dict) else data
    return [shot for shot in shots if isinstance(shot, dict)] if isinstance(shots, list) else []


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
        for block_id in spec.get("sourceBlockIds", []):
            specs_by_block[str(block_id)] = spec
    scenes = []
    for index, (block, measure) in enumerate(zip(blocks, measures), 1):
        beat = str(block.get("beat", ""))
        question = short_text(block.get("question"), 86)
        state_change = short_text(block.get("state_change"), 140)
        block_id = str(block.get("id") or f"scene-{index:03d}")
        spec = specs_by_block.get(block_id, {})
        editorial = spec.get("editorial", {}) if isinstance(spec, dict) else {}
        visual = spec.get("visual", {}) if isinstance(spec, dict) else {}
        scene_type = visual.get("sceneType") or editorial.get("function") or block_type(block)
        claims = spec.get("claimIds") or block.get("claim_ids") or []
        states = spec.get("states") or []
        scene = {
            "id": block_id,
            "type": scene_type,
            "purpose": editorial.get("function") or beat.lower().replace(" ", "-") or "editorial",
            "startSeconds": round(max(0.0, float(measure["start"])), 3),
            "durationSeconds": round(max(0.5, float(measure["end"] - measure["start"])), 3),
            "sourceBlockIds": [block_id],
            "claimIds": [str(value) for value in claims],
            "sourceIds": [str(value) for value in spec.get("sourceIds", [])],
            "promptId": str(spec.get("promptId")) if spec.get("promptId") else None,
            "headline": short_text(visual.get("headline") or question, 86) or "Uma mudança no arquivo",
            "body": state_change or "A evidência reorganiza a leitura.",
            "metadata": {"label": beat or "DOCUMENTARY", "source": "SHOT_SPECS.json" if spec else "ROTEIRO_MAP.json", "stateCount": str(len(states))},
            "motionVariant": str(spec.get("motionVariant") or ("timeline" if "timeline" in scene_type else "push-in")),
            "motionIntent": str(spec.get("motionIntent") or editorial.get("stateChange") or "purposeful editorial movement"),
            "transitionIn": str(spec.get("transitionIn") or "dissolve"),
            "transitionOut": str(spec.get("transitionOut") or "dissolve"),
            "states": states,
        }
        if spec.get("cropPolicy"):
            scene["cropPolicy"] = spec["cropPolicy"]
        scenes.append({key: value for key, value in scene.items() if value is not None})
    if scenes and scenes[-1]["startSeconds"] + scenes[-1]["durationSeconds"] < total:
        scenes[-1]["durationSeconds"] = round(total - scenes[-1]["startSeconds"], 3)
    return scenes


def stage_assets(episode: Path, public_dir: Path, audio: Path | None, style: dict) -> tuple[dict, list[Path], list[Path]]:
    public_dir.mkdir(parents=True, exist_ok=True)
    staged = []
    for image in image_files(episode):
        target = public_dir / "images" / f"{len(staged) + 1:03d}{image.suffix.lower()}"
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists() or target.stat().st_size != image.stat().st_size:
            shutil.copy2(image, target)
        staged.append(target)
    audio_target = None
    if audio:
        audio_target = public_dir / "audio" / audio.name
        audio_target.parent.mkdir(parents=True, exist_ok=True)
        if not audio_target.exists() or audio_target.stat().st_size != audio.stat().st_size:
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
        if not target.exists():
            shutil.copy2(font, target)
    return ({"audio": audio_target} if audio_target else {}), staged, font_sources


def source_hash_map(episode: Path, contracts: dict, audio: Path | None, assets: list[Path] | None = None) -> dict:
    result = {}
    for relative in ("01_roteiro/ROTEIRO_MAP.json", "01_roteiro/CLAIMS.json", "01_roteiro/SHOT_SPECS.json", "01_roteiro/PROMPT_PLAN.json", "01_roteiro/TIMING_AUDIT.json", "02_audio/voice_FINAL.wav", "02_audio/captions.srt"):
        path = episode / relative
        if path.exists():
            result[relative] = sha256(path)
    if audio and audio.exists():
        result[str(audio.relative_to(episode)).replace("\\", "/")] = sha256(audio)
    for name, data in contracts.items():
        result[f"contract:{name}"] = hashlib.sha256(json.dumps(data, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()
    for asset in assets or []:
        result[f"asset:{asset.name}"] = sha256(asset)
    return result


def build_plan(episode: Path, channel: str | None, format_name: str, contracts: dict, allow_incomplete: bool = False) -> dict:
    style = contracts.get("style", {})
    motion = contracts.get("motion", {})
    visual = load_visual_bible(contracts)
    shot_specs = load_shot_specs(episode)
    if motion.get("engine") == "remotion" and not allow_incomplete:
        if not shot_specs:
            raise FileNotFoundError(f"missing_visual_plan:{episode / '01_roteiro' / 'SHOT_SPECS.json'}")
        if prompt_plan_status(episode) != "PROMPTS_READY":
            raise FileNotFoundError(f"visual_gate_not_ready:{prompt_plan_status(episode)}:{episode / '01_roteiro' / 'PROMPT_PLAN.json'}")
    size = motion.get("size", [1920, 1080])
    width, height = (size if format_name == "long" else [1080, 1920])
    audio = audio_file(episode, format_name)
    audio_seconds = ffprobe_duration(audio) if audio else 0.0
    captions_path = caption_file(episode, format_name)
    captions = parse_srt(captions_path) if captions_path else []
    if audio_seconds <= 0 and captions:
        audio_seconds = max(caption["endSeconds"] for caption in captions)
    scenes = scene_blocks(episode, audio_seconds, format_name, shot_specs)
    total = audio_seconds or max(scene["startSeconds"] + scene["durationSeconds"] for scene in scenes)
    public_dir = episode / "04_video_final" / "_remotion" / "public"
    _, staged, _ = stage_assets(episode, public_dir, audio, style)
    branding = dict(visual.get("branding", {})) if isinstance(visual.get("branding", {}), dict) else {}
    watermark_source = branding.get("watermark")
    if watermark_source:
        source = Path(str(watermark_source)).expanduser()
        if not source.is_absolute():
            source = episode.parent.parent / source
        if source.exists():
            watermark_target = public_dir / "brand" / f"watermark{source.suffix.lower()}"
            watermark_target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, watermark_target)
            branding["watermark"] = watermark_target.relative_to(public_dir).as_posix()
        else:
            branding.pop("watermark", None)
    render_config = motion.get("remotion", {}).get("render", {}) if isinstance(motion.get("remotion", {}), dict) else {}
    render_plan = {"codec": render_config.get("codec", "h264"), "audioCodec": render_config.get("audio_codec", render_config.get("audioCodec", "aac")), "crf": int(render_config.get("crf", 18)), "imageFormat": "jpeg", "jpegQuality": 92}
    asset_ledger = []
    for index, scene in enumerate(scenes):
        if staged:
            asset_path = staged[index % len(staged)].relative_to(public_dir).as_posix()
            asset_id = f"A-{index + 1:03d}"
            scene["asset"] = asset_path
            scene["assets"] = [{"assetId": asset_id, "path": asset_path, "role": "primary", "kind": staged[index % len(staged)].suffix.lstrip("."), "origin": "synthetic-or-licensed", "rightsStatus": "pending"}]
            for state in scene.get("states", []):
                if not state.get("assetIds"):
                    state["assetIds"] = [asset_id]
            asset_ledger.append(scene["assets"][0])
    audio_plan = None
    if audio:
        audio_plan = {"src": f"audio/{audio.name}", "volume": 1.0}
    plan = {
        "version": 2,
        "channel": channel or episode.parent.name,
        "episode": episode.name,
        "format": format_name,
        "video": {"width": int(width), "height": int(height), "fps": int(motion.get("fps", 30)), "durationSeconds": round(total, 3)},
        "captions": captions,
        "theme": theme_from_style(style, visual),
        "visualBible": visual,
        "render": render_plan,
        "branding": branding,
        "contractVersions": {name: hashlib.sha256(json.dumps(data, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest() for name, data in contracts.items()},
        "assetLedger": asset_ledger,
        "scenes": scenes,
        "sources": source_hash_map(episode, contracts, audio, staged),
    }
    if audio_plan:
        plan["audio"] = audio_plan
    if captions_path:
        plan["sources"]["captions"] = f"captions/{captions_path.name}"
    return plan


def plan_path(episode: Path, format_name: str) -> Path:
    return episode / "01_roteiro" / f"RENDER_PLAN_{format_name.upper()}.json"


def plan_command(args) -> int:
    root = Path(args.root).expanduser().resolve()
    episode = (root / args.episode).resolve()
    contracts = load_contract(root, args.channel, args.allow_defaults)
    plan = build_plan(episode, args.channel, args.format, contracts, args.allow_incomplete)
    destination = plan_path(episode, args.format)
    write_json(destination, plan)
    print(json.dumps({"status": "PASS", "plan": str(destination), "scenes": len(plan["scenes"]), "assets": len(plan["sources"])}, ensure_ascii=False))
    return 0


def plan_env(episode: Path, format_name: str) -> dict[str, str]:
    plan = plan_path(episode, format_name)
    public = episode / "04_video_final" / "_remotion" / "public"
    return {"DARK_MASTER_RENDER_PLAN": str(plan), "DARK_MASTER_PUBLIC_DIR": str(public)}


def remotion_command(command: str, args: list[str], episode: Path, format_name: str, extra: dict[str, str] | None = None) -> subprocess.CompletedProcess:
    env = {**plan_env(episode, format_name), **(extra or {})}
    return run_command([npm_command(), "--prefix", str(REMOTION_ROOT), "run", command, "--", *args], REMOTION_ROOT, env)


def still_command(args) -> int:
    root = Path(args.root).expanduser().resolve()
    episode = (root / args.episode).resolve()
    format_name = args.format
    plan = plan_path(episode, format_name)
    if not plan.exists():
        print(json.dumps({"status": "FAIL", "error": "render_plan_missing"}))
        return 1
    frames = args.frame or [0.5, 2.5, 5.0, max(0.0, read_json(plan)["video"]["durationSeconds"] - 0.1)]
    fps = int(read_json(plan)["video"]["fps"])
    for value in frames:
        frame = max(0, round(value * fps))
        output = episode / "04_video_final" / "_remotion" / "stills" / f"{format_name}-{value:.2f}.png"
        result = remotion_command("render:still", [format_name, str(frame)], episode, format_name, {"DARK_MASTER_STILL": str(output)})
        print(result.stdout.strip())
    return 0


def render_command(args) -> int:
    root = Path(args.root).expanduser().resolve()
    episode = (root / args.episode).resolve()
    format_name = args.format
    plan = plan_path(episode, format_name)
    if not plan.exists():
        print(json.dumps({"status": "FAIL", "error": "render_plan_missing"}))
        return 1
    final = episode / "04_video_final" / f"{episode.name}_{format_name.upper()}_REMOTION.mp4"
    if final.exists() and not args.overwrite:
        print(json.dumps({"status": "FAIL", "error": "output_exists", "output": str(final)}))
        return 1
    result = remotion_command("render", [format_name], episode, format_name, {"DARK_MASTER_OUTPUT": str(final)})
    report = {
        "status": "PASS",
        "engine": "remotion",
        "format": format_name,
        "episode": episode.name,
        "output": str(final),
        "plan": str(plan),
        "planHash": sha256(plan),
        "outputHash": sha256(final),
        "command": result.stdout.strip(),
        "versions": {
            "node": os.environ.get("NODE_VERSION", ""),
            "remotion": read_json(REMOTION_ROOT / "package.json").get("dependencies", {}).get("remotion", ""),
        },
    }
    write_json(episode / "01_roteiro" / f"RENDER_REPORT_{format_name.upper()}.json", report)
    print(json.dumps(report, ensure_ascii=False))
    return 0


def audit_command(args) -> int:
    root = Path(args.root).expanduser().resolve()
    episode = (root / args.episode).resolve()
    report_path = episode / "01_roteiro" / f"RENDER_REPORT_{args.format.upper()}.json"
    output = episode / "04_video_final" / f"{episode.name}_{args.format.upper()}_REMOTION.mp4"
    plan = plan_path(episode, args.format)
    errors = []
    if not plan.exists():
        errors.append("render_plan_missing")
    if not report_path.exists():
        errors.append("render_report_missing")
    if not output.exists():
        errors.append("render_output_missing")
    if plan.exists() and report_path.exists():
        report = read_json(report_path)
        if report.get("planHash") and report["planHash"] != sha256(plan):
            errors.append("render_plan_hash_mismatch")
    duration = ffprobe_duration(output)
    if output.exists() and duration <= 0:
        errors.append("render_duration_invalid")
    result = {"status": "FAIL" if errors else "PASS", "errors": errors, "output": str(output), "durationSeconds": round(duration, 3)}
    print(json.dumps(result, ensure_ascii=False))
    return 1 if errors else 0


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
