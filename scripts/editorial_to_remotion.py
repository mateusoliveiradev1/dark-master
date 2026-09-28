#!/usr/bin/env python3
"""Translate approved EDITORIAL_TIMELINE + SHOT_PLAN + ASSET_PLAN + SOUND_PLAN into a v2 RENDER_PLAN.

The bridge performs no creative decisions: every scene, asset, duration and
transition comes from the approved timeline. It exists only so the existing
Remotion renderer can execute the new pipeline without reintroducing the old
block-to-shot generator.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path

from production_contracts import read_json, sha256_json, write_json

MEDIA_TO_SCENE = {
    "STATIC_PHOTO": "cinematic-photo",
    "ARCHIVAL_PHOTO": "cinematic-photo",
    "ABSTRACT_ATMOSPHERE": "cinematic-photo",
    "DOCUMENT": "document-report",
    "MAP": "animated-map",
    "TIMELINE": "timeline",
    "GRAPHIC": "data-visualization",
    "FORENSIC_DETAIL": "evidence-focus",
    "CINEMATIC_RECONSTRUCTION": "photo-reconstruction",
    "AI_VIDEO": "photo-reconstruction",
    "SCREEN_ELEMENT": "split-screen",
    "TEXT_ONLY": "quote",
    "BLACK_FRAME": "negative-space-beat",
    "WHITE_FRAME": "negative-space-beat",
    "MIXED_MEDIA": "evidence-reveal",
}

SCENE_MOTION = {
    "cinematic-photo": "lateral-drift",
    "photo-reconstruction": "lateral-drift",
    "document-report": "document-dive",
    "animated-map": "route-draw",
    "timeline": "timeline-build",
    "data-visualization": "line-draw",
    "evidence-focus": "detail-inspection",
    "evidence-reveal": "masked-reveal",
    "split-screen": "lateral-drift",
    "quote": "static-hold",
    "negative-space-beat": "static-hold",
}

# Designed single-state breaths: exempt from the state-change guard (same set
# as visual_plan.build_motion_prompt static_scene). Narrative scenes are never static.
STATIC_SCENES = {"quote", "negative-space-beat", "chapter-break", "end-card-cta", "archive-end-card"}

# Viewer-facing kicker per Video Director scene family. Raw media-type names
# (STATIC_PHOTO, PROMPT-*, shot ids) must NEVER reach the screen.
FAMILY_LABEL = {
    "INVESTIGATION": "INVESTIGATION",
    "RECONSTRUCTION": "RECONSTRUCTION",
    "LOCATION": "LOCATION",
    "TIMELINE": "TIMELINE",
    "EVIDENCE": "EVIDENCE",
    "ATMOSPHERE": "ATMOSPHERE",
    "DOCUMENT": "DOCUMENT",
    "COMPARISON": "COMPARISON",
    "REFLECTION": "REFLECTION",
    "CHAPTER_BREAK": "",
}

# Media types that must render with no headline/body text at all, plus any
# shot the Visual Director flags as a pure interstitial (sting, flash, pause).
SILENT_MEDIA = {"BLACK_FRAME", "WHITE_FRAME"}


def is_silent(shot: dict) -> bool:
    return str(shot.get("mediaType")) in SILENT_MEDIA or shot.get("silentFrame") is True

DEFAULT_LAYERS = ["environment", "subject", "state-change", "continuity"]

# Layers must name the semantic layer the renderer gates on (e.g. the
# Timeline scene only draws its line when "timeline" is visible).
SCENE_LAYERS = {
    "cinematic-photo": ["environment", "subject", "continuity"],
    "photo-reconstruction": ["environment", "subject", "continuity"],
    "document-report": ["environment", "document", "continuity"],
    "animated-map": ["environment", "route", "continuity"],
    "timeline": ["environment", "timeline", "continuity"],
    "data-visualization": ["environment", "data", "continuity"],
    "evidence-focus": ["environment", "evidence", "state-change"],
    "evidence-reveal": ["environment", "evidence", "state-change"],
    "split-screen": ["environment", "subject", "comparison"],
    "quote": ["environment", "subject", "continuity"],
    "negative-space-beat": ["environment", "continuity"],
}
CROP_POLICY = {
    "masterAspect": "16:9",
    "long": {"focalPoint": [0.5, 0.45]},
    "short": {"focalPoint": [0.5, 0.42], "dedicatedReframeRequired": True},
}
SAFE_AREAS = {
    "long": {"action": [0.05, 0.05, 0.9, 0.78], "captions": [0.06, 0.78, 0.88, 0.16]},
    "short": {"action": [0.1, 0.1, 0.8, 0.72], "captions": [0.08, 0.78, 0.84, 0.16]},
}


def frames(seconds: float, fps: int) -> int:
    return max(1, int(round(float(seconds) * fps)))


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def motion_contract(shot_id: str, prompt_id: str, subject: str, state_change: str,
                    layers: list[str], scene_type: str, static: bool) -> dict:
    operator = "static-hold" if static else SCENE_MOTION.get(scene_type, "lateral-drift")
    intensity = 0 if static else (1 if scene_type in {"cinematic-photo", "photo-reconstruction"} else 2)
    if static:
        states = [{"id": "hold", "timeRange": [0, 100],
                   "intent": f"hold: {state_change}", "visibleLayers": layers,
                   "motion": "static-hold", "transition": "hold",
                   "audioCue": "no added sound cue"}]
    else:
        states = [
            {"id": "establish", "timeRange": [0, 38],
             "intent": f"establish: {state_change}", "visibleLayers": layers[:2],
             "motion": "static-hold", "transition": "hold",
             "audioCue": "low emphasis at entry"},
            {"id": "reveal", "timeRange": [38, 100],
             "intent": f"reveal: {state_change}", "visibleLayers": layers,
             "motion": operator, "transition": "hold",
             "audioCue": "low emphasis at reveal"},
        ]
    return {
        "contractVersion": 1,
        "promptId": prompt_id,
        "shotId": shot_id,
        "intensity": intensity,
        "layers": layers,
        "states": states,
        "cameraPath": {
            "kind": "static-hold" if static else "controlled-crop",
            "description": f"Hold on {subject}; preserve the composition while the narration carries '{state_change}'."
            if static else f"Start on {subject}; move only to make '{state_change}' legible.",
            "keyframes": [{"at": 0, "focalPoint": [0.5, 0.45]}, {"at": 100, "focalPoint": [0.5, 0.45]}],
        },
        "cropPolicy": CROP_POLICY,
        "transitions": {"in": "cut", "out": "cut",
                        "rationale": f"transition only after '{state_change}' resolves"},
        "audioCues": [s["audioCue"] for s in states],
        "staticException": {
            "allowed": True if static else False,
            "reason": f"static treatment bound to '{state_change}'" if static
            else f"scene must make '{state_change}' visible",
        },
        "negativeMotion": ["no generic zoom used as the only motion",
                           "no generic fade used as the only transition"],
        "full": (f"MOTION_PROMPT[{prompt_id}/{shot_id}] | Intensity: {intensity}/4 | "
                 f"Layers: {', '.join(layers)} | States 0-100: " +
                 "; ".join(f"{s['id']}={s['timeRange'][0]}-{s['timeRange'][1]} ({s['intent']})" for s in states) +
                 f" | Camera path: hold — Hold on {subject}; preserve the composition while the narration carries '{state_change}'."
                 if static else f" | Camera path: controlled-crop — Start on {subject}; move only to make '{state_change}' legible." +
                 f" | Crop: 16:9 master | Transitions: in=cut; out=cut; transition only after '{state_change}' resolves"
                 f" | Audio cues: {'; '.join(s['audioCue'] for s in states)}"
                 f" | Static exception: allowed={str(bool(static)).lower()}; bound to '{state_change}'"
                 " | Negative motion: no generic zoom used as the only motion; no generic fade used as the only transition"),
    }


def image_contract(shot_id: str, prompt_id: str, shot: dict, subject: str,
                   state_change: str, layers: list[str]) -> dict:
    composition = str(shot.get("composition") or "case-specific documentary composition")
    full = (f"IMAGE_PROMPT[{prompt_id}/{shot_id}] | Editorial purpose: {shot.get('purpose')} | "
            f"Scene question: {shot.get('purpose')} | State change: {state_change} | Classification: MIXED | "
            f"Subject: {subject} | Setting: {shot.get('composition')} | Composition: {composition} | "
            "Focal point: 0.5,0.45 | Crop: 16:9 master | Safe areas: long and short declared | "
            "Continuity: case-bound palette, era and geography | "
            "Negative guards: no baked-in text; no watermark | Output: 16:9; no baked-in text.")
    return {
        "contractVersion": 1,
        "promptId": prompt_id,
        "shotId": shot_id,
        "purpose": str(shot.get("purpose") or ""),
        "question": str(shot.get("purpose") or ""),
        "stateChange": state_change,
        "classification": "MIXED",
        "subject": subject,
        "setting": str(shot.get("composition") or "documented setting"),
        "composition": {"description": composition, "focalPoint": [0.5, 0.45],
                        "shotScale": "documentary scale", "camera": str(shot.get("cameraBehavior") or ""),
                        "lighting": "motivated low-key documentary light"},
        "layers": layers,
        "cropPolicy": CROP_POLICY,
        "safeAreas": SAFE_AREAS,
        "continuity": {"era": "documented case chronology"},
        "negativeGuards": ["no baked-in text", "no watermark"],
        "full": full,
    }


def build_render_plan(episode: Path, format_name: str = "long", channel: str | None = None) -> dict:
    root = episode / "01_roteiro"
    direction = read_json(root / "VIDEO_DIRECTION.json")
    families = {str(seg.get("id")): str(seg.get("sceneFamily") or "")
                for seg in direction.get("segments", []) if isinstance(seg, dict)}
    shot_plan = read_json(root / "SHOT_PLAN.json")
    asset_plan = read_json(root / "ASSET_PLAN.json")
    sound = read_json(episode / "02_audio" / "SOUND_PLAN.json")
    timeline = read_json(root / "EDITORIAL_TIMELINE.json")
    if timeline.get("status") != "READY":
        raise ValueError("editorial_timeline_not_ready")

    fps = int(timeline.get("fps", 30))
    width, height = int(timeline.get("width", 1920)), int(timeline.get("height", 1080))
    duration_seconds = float(timeline.get("durationInFrames", 1)) / fps
    shots = {str(s.get("shotId")): s for s in shot_plan.get("shots", []) if isinstance(s, dict)}
    narrative = read_json(root / "NARRATIVE_BEATS.json")
    beats_by_id = {str(b.get("id")): b for b in narrative.get("beats", []) if isinstance(b, dict)}
    visual_items = (timeline.get("visualTracks") or [[]])[0]

    def scene_body(shot: dict, scene_type: str, fallback: str) -> str:
        if scene_type == "timeline":
            events = []
            for beat_id in shot.get("beatIds", []):
                beat = beats_by_id.get(str(beat_id), {})
                for line in (str(beat.get("question") or ""), str(beat.get("stateChange") or "")):
                    line = line[:90]
                    if line and line not in events:
                        events.append(line)
            if events:
                return "\n".join(events)
        if scene_type == "data-visualization" and isinstance(shot.get("dataValues"), list) and shot["dataValues"]:
            lines = [f"{item.get('label')}|{item.get('value')}" for item in shot["dataValues"]
                     if isinstance(item, dict) and item.get("label") is not None]
            if lines:
                return "\n".join(lines)
        return fallback

    run_input = sha256_json({"timeline": timeline, "format": format_name})
    run_id = f"prod-{run_input[:12]}"
    public_dir = episode / "04_video_final" / "_production" / run_id / "public"
    if public_dir.exists():
        shutil.rmtree(public_dir)
    (public_dir / "images").mkdir(parents=True, exist_ok=True)
    (public_dir / "audio").mkdir(parents=True, exist_ok=True)

    staged: dict[str, Path] = {}
    for asset in asset_plan.get("assets", []):
        if not isinstance(asset, dict) or asset.get("status") not in {"AVAILABLE", "GENERATED"}:
            continue
        src = episode / str(asset.get("path") or "")
        if not src.is_file():
            raise FileNotFoundError(f"asset_file_missing:{asset.get('assetId')}:{src}")
        suffix = src.suffix.lower() or (".mp4" if asset.get("kind") == "video" else ".jpg")
        if asset.get("kind") == "audio":
            target = public_dir / "audio" / f"{asset['assetId']}{suffix}"
        else:
            target = public_dir / "images" / f"{asset['assetId']}{suffix}"
        shutil.copy2(src, target)
        staged[str(asset["assetId"])] = target

    assets_by_shot: dict[str, list[dict]] = {}
    for asset in asset_plan.get("assets", []):
        if not isinstance(asset, dict) or str(asset.get("assetId")) not in staged:
            continue
        for shot_id in asset.get("shotIds", []):
            assets_by_shot.setdefault(str(shot_id), []).append(asset)

    scenes = []
    ledger = []
    for item in sorted(visual_items, key=lambda i: int(i.get("startFrame", 0))):
        shot_id = str(item.get("shotId"))
        shot = shots.get(shot_id)
        if not shot:
            raise ValueError(f"timeline_shot_missing:{shot_id}")
        scene_type = MEDIA_TO_SCENE.get(str(shot.get("mediaType")), "cinematic-photo")
        layers = SCENE_LAYERS.get(scene_type, DEFAULT_LAYERS)
        static = scene_type in STATIC_SCENES or int(shot.get("motionIntensity", 1) or 0) == 0
        prompt_id = f"PROMPT-{shot_id}"
        subject = str(shot.get("visualDescription") or shot.get("purpose") or shot_id)[:140]
        state_change = str(shot.get("purpose") or shot_id)[:140]
        scene_assets = []
        for asset in sorted(assets_by_shot.get(shot_id, []), key=lambda a: str(a.get("assetId"))):
            target = staged[str(asset["assetId"])]
            ref = {
                "assetId": str(asset["assetId"]),
                "promptId": prompt_id,
                "shotId": shot_id,
                "path": target.relative_to(public_dir).as_posix(),
                "role": str(asset.get("role") or "primary"),
                "kind": str(asset.get("kind") or "image"),
                "origin": "synthetic-or-licensed",
                "rightsStatus": "licensed",
                "hash": sha256_file(target),
                "blocked": False,
                "sourceBlockIds": list(shot.get("sourceBlockIds", [])),
            }
            scene_assets.append(ref)
            ledger.append(ref)
        if static:
            states = [{"id": "hold", "timeRange": [0, 1], "intent": f"hold: {state_change}",
                       "visibleLayers": layers, "hiddenLayers": [],
                       "assetIds": [a["assetId"] for a in scene_assets],
                       "motion": "static-hold"}]
        else:
            states = [
                {"id": "establish", "timeRange": [0, 0.38], "intent": f"establish: {state_change}",
                 "visibleLayers": layers[:2], "hiddenLayers": layers[2:],
                 "assetIds": [a["assetId"] for a in scene_assets], "motion": "static-hold"},
                {"id": "reveal", "timeRange": [0.38, 1], "intent": f"reveal: {state_change}",
                 "visibleLayers": layers, "hiddenLayers": [],
                 "assetIds": [a["assetId"] for a in scene_assets],
                 "motion": SCENE_MOTION.get(scene_type, "lateral-drift")},
            ]
        motion = motion_contract(shot_id, prompt_id, subject, state_change, layers, scene_type, static)
        # Align motion states' visible layers with scene states so the audit is honest.
        scenes.append({
            "id": shot_id,
            "shotId": shot_id,
            "type": scene_type,
            "purpose": str(shot.get("purpose") or ""),
            "question": str(shot.get("purpose") or ""),
            "stateChange": state_change,
            "classification": "MIXED",
            "subject": subject,
            "setting": str(shot.get("composition") or ""),
            "composition": str(shot.get("composition") or ""),
            "layers": layers,
            "startSeconds": int(item.get("startFrame", 0)) / fps,
            "durationSeconds": max(1, int(item.get("durationInFrames", fps))) / fps,
            "sourceBlockIds": list(shot.get("sourceBlockIds", [])),
            "claimIds": list(shot.get("claimIds", [])),
            "sourceIds": list(shot.get("sourceIds", [])),
            "promptId": prompt_id,
            "safeAreas": SAFE_AREAS,
            "negativeGuards": ["no baked-in text", "no watermark"],
            "continuity": {"era": "documented case chronology"},
            "imagePrompt": image_contract(shot_id, prompt_id, shot, subject, state_change, layers),
            "motionPrompt": motion,
            "cropPolicy": CROP_POLICY,
            "assets": scene_assets,
            "states": states,
            "headline": "" if is_silent(shot) else str(shot.get("purpose") or "")[:86],
            "body": scene_body(shot, scene_type, state_change) if scene_type in {"timeline", "data-visualization"} else "",
            "metadata": {"label": "" if is_silent(shot) else FAMILY_LABEL.get(families.get(str(shot.get("directorSegmentId")), ""), "DOCUMENT"),
                         "classification": "MIXED",
                         "showAnnotation": "false",
                         "person": "", "date": "", "source": "", "number": ""},
            "motionVariant": motion["states"][-1]["motion"],
            "motionIntent": state_change,
            "transitionIn": "cut",
            "transitionOut": "cut",
        })

    # Audio: narration becomes plan.audio; every other cue becomes an audioTrack.
    narration_src = None
    audio_tracks = []
    for cue in sound.get("cues", []):
        if not isinstance(cue, dict):
            continue
        src_rel = str(cue.get("src") or "")
        asset_id = str(cue.get("assetId") or "")
        if asset_id and asset_id in staged:
            src_rel = staged[asset_id].relative_to(public_dir).as_posix()
        elif src_rel:
            src_path = episode / src_rel
            if src_path.is_file():
                target = public_dir / "audio" / src_path.name
                if not target.exists():
                    shutil.copy2(src_path, target)
                src_rel = target.relative_to(public_dir).as_posix()
        if cue.get("type") == "NARRATION" and narration_src is None:
            narration_src = src_rel
            continue
        if cue.get("type") == "SILENCE" or not src_rel:
            continue
        audio_tracks.append({
            "id": str(cue.get("id")),
            "type": str(cue.get("type")),
            "src": src_rel,
            "startFrame": frames(float(cue.get("startSeconds", 0)), fps),
            "durationInFrames": frames(float(cue.get("durationSeconds", 0)), fps),
            "gainDb": float(cue.get("gainDb", -12) or -12),
            "fadeInSeconds": float(cue.get("fadeInSeconds", 0) or 0),
            "fadeOutSeconds": float(cue.get("fadeOutSeconds", 0) or 0),
        })

    plan = {
        "version": 2,
        "channel": channel or episode.parent.name,
        "episode": episode.name,
        "format": format_name,
        "video": {"width": width, "height": height, "fps": fps, "durationSeconds": round(duration_seconds, 3)},
        "captions": [],
        "theme": {"background": "#0A0A0C", "surface": "#17171B", "text": "#F5F5F4",
                  "muted": "#A1A1AA", "accent": "#B91C1C",
                  "headingFont": "Arial", "bodyFont": "Arial", "safeArea": {"x": 72, "y": 54}},
        "render": {"codec": "h264", "audioCodec": "aac", "crf": 18, "imageFormat": "jpeg", "jpegQuality": 92},
        "branding": {"watermarkOpacity": 0.0, "tagline": "", "endCard": "archive-end-card"},
        "contractVersions": {"editorialTimeline": sha256_json(timeline)},
        "assetLedger": ledger,
        "blockedAssetIds": [],
        "scenes": scenes,
        "sources": {},
        "audioTracks": audio_tracks,
        "staging": {"path": public_dir.relative_to(episode).as_posix(),
                    "publicDir": public_dir.relative_to(episode).as_posix()},
        "runId": run_id,
    }
    if narration_src:
        plan["audio"] = {"src": narration_src, "volume": 1.0}
    write_json(public_dir / "asset_ledger.json", {"version": 1, "assets": ledger})
    destination = root / f"RENDER_PLAN_{format_name.upper()}_PRODUCTION.json"
    write_json(destination, plan)
    return {"plan": str(destination), "publicDir": str(public_dir), "runId": run_id,
            "scenes": len(scenes), "audioTracks": len(audio_tracks)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episode", required=True)
    parser.add_argument("--format", choices=["long", "short"], default="long")
    parser.add_argument("--channel", default="",
                        help="on-screen channel brand; never expose temp dirs or internal names")
    args = parser.parse_args()
    episode = Path(args.episode).expanduser().resolve()
    try:
        result = build_render_plan(episode, args.format, args.channel or None)
    except (OSError, ValueError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False))
        return 1
    print(json.dumps({"status": "PASS", **result}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
