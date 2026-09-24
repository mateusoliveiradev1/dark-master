from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import run_ledger

HERE = Path(__file__).resolve().parent
REMOTION_ROOT = HERE.parent / "remotion"
COMPOSITIONS = {"long": "DarkMasterLong", "short": "DarkMasterShort"}
MIN_SCORE = 92
CAMERA_ONLY_MOTION = {
    "slow-push",
    "lateral-drift",
    "crop-shift",
    "detail-inspection",
    "controlled-crop",
    "pull-out",
    "negative-space-pullout",
    "archive-title-object",
    "match-cut",
    "static-hold",
}
MOTION_ALIASES = {
    "push-in": "slow-push",
    "drift": "lateral-drift",
    "drift-with-purpose": "lateral-drift",
    "detail-reveal": "detail-inspection",
    "hold": "static-hold",
    "hold-and-transition": "static-hold",
    "track-left": "lateral-drift",
    "track-right": "lateral-drift",
    "negative-space": "negative-space-pullout",
    "archive-title": "archive-title-object",
}


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def npm_command():
    return shutil.which("npm.cmd") or shutil.which("npm") or "npm"


def frame_at(scene, position, fps):
    start = float(scene["startSeconds"])
    duration = float(scene["durationSeconds"])
    return max(0, round((start + duration * position) * fps))


def plan_public_dir(plan, episode):
    staging = plan.get("staging", {}) if isinstance(plan.get("staging"), dict) else {}
    raw = staging.get("publicDir") or staging.get("path")
    if not raw:
        raise ValueError("render_plan_staging_missing")
    value = Path(str(raw))
    public = (value if value.is_absolute() else episode / value).resolve()
    run_root = (episode / "04_video_final" / "_remotion" / "runs").resolve()
    if not public.is_relative_to(run_root):
        raise ValueError("render_staging_outside_run_root")
    return public


def run_still(plan_path, public_dir, composition_id, frame, output):
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    env = {
        **os.environ,
        "DARK_MASTER_RENDER_PLAN": str(plan_path),
        "DARK_MASTER_PUBLIC_DIR": str(public_dir),
        "DARK_MASTER_STILL": str(output),
    }
    command = [npm_command(), "--prefix", str(REMOTION_ROOT), "run", "render:still", "--", composition_id, str(frame)]
    result = subprocess.run(command, cwd=REMOTION_ROOT, env=env, text=True, capture_output=True)
    if result.returncode != 0:
        raise RuntimeError(result.stdout + result.stderr)
    if not output.exists() or output.stat().st_size <= 0:
        raise RuntimeError(f"still_not_written:{output}")
    return output


def make_120(path, output):
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        return None
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([
        ffmpeg,
        "-y",
        "-i",
        str(path),
        "-vf",
        "scale=120:120:force_original_aspect_ratio=decrease,pad=120:120:(ow-iw)/2:(oh-ih)/2:color=black",
        str(output),
    ], check=True, capture_output=True)
    return output


def make_contact_sheet(paths, output):
    paths = [Path(path) for path in paths]
    if not paths:
        raise ValueError("contact_sheet_empty")
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        ffmpeg = shutil.which("ffmpeg")
        if not ffmpeg:
            raise RuntimeError("contact_sheet_renderer_unavailable")
        command = [ffmpeg, "-y"]
        for path in paths:
            command.extend(["-i", str(path)])
        filters = "".join(f"[{index}:v]" for index in range(len(paths))) + f"hstack=inputs={len(paths)}[out]"
        command.extend(["-filter_complex", filters, "-map", "[out]", "-frames:v", "1", str(output)])
        subprocess.run(command, check=True, capture_output=True)
        return output
    cell_width = 320
    cell_height = 220
    sheet = Image.new("RGB", (cell_width * len(paths), cell_height), (10, 10, 12))
    draw = ImageDraw.Draw(sheet)
    for index, path in enumerate(paths):
        with Image.open(path) as image:
            image = image.convert("RGB")
            image.thumbnail((cell_width - 12, cell_height - 36), Image.Resampling.LANCZOS)
            x = index * cell_width + (cell_width - image.width) // 2
            y = 4
            sheet.paste(image, (x, y))
        draw.text((index * cell_width + 8, cell_height - 24), path.stem, fill=(220, 220, 220))
    sheet.save(output, format="JPEG", quality=88)
    return output


def motion_token(value):
    token = str(value or "").strip().lower().replace("_", "-")
    return MOTION_ALIASES.get(token, token)


def state_delta(previous, current):
    if not isinstance(previous, dict) or not isinstance(current, dict):
        return []
    deltas = []
    if set(previous.get("assetIds", [])) != set(current.get("assetIds", [])):
        deltas.append("asset")
    if set(previous.get("visibleLayers", [])) != set(current.get("visibleLayers", [])):
        deltas.append("layer")
    if set(previous.get("hiddenLayers", [])) != set(current.get("hiddenLayers", [])):
        deltas.append("layer")
    if str(previous.get("annotation") or "") != str(current.get("annotation") or ""):
        deltas.append("annotation")
    if motion_token(previous.get("motion")) not in CAMERA_ONLY_MOTION or motion_token(current.get("motion")) not in CAMERA_ONLY_MOTION:
        deltas.append("semantic-operator")
    return deltas


def audit_scene_motion(scene):
    states = scene.get("states", [])
    if not isinstance(states, list) or not states:
        return {"status": "FAIL", "reason": "states_missing", "changes": []}
    deltas = []
    for previous, current in zip(states, states[1:]):
        deltas.append({
            "from": previous.get("id", ""),
            "to": current.get("id", ""),
            "kinds": state_delta(previous, current),
        })
    static_exception = scene.get("motionPrompt", {}).get("staticException", {})
    meaningful = [item for item in deltas if any(kind in {"asset", "layer", "annotation", "semantic-operator"} for kind in item["kinds"])]
    if static_exception.get("allowed") is True:
        return {"status": "STATIC_EXCEPTION", "changes": deltas, "meaningfulChanges": len(meaningful)}
    if len(meaningful) < 2:
        return {"status": "FAIL", "reason": "static_frame_guard", "changes": deltas, "meaningfulChanges": len(meaningful)}
    if not any(item["kinds"] for item in deltas):
        return {"status": "FAIL", "reason": "no_visual_state_change", "changes": deltas, "meaningfulChanges": 0}
    return {"status": "PASS", "changes": deltas, "meaningfulChanges": len(meaningful)}


def validate_scene(scene, plan):
    required = (
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
        "imagePrompt",
        "motionPrompt",
        "assets",
    )
    missing = [field for field in required if field not in scene or scene[field] in (None, "", [], {})]
    if missing:
        raise ValueError(f"visual_contract_missing:{scene.get('id')}:{','.join(missing)}")
    motion = scene["motionPrompt"]
    intensity = motion.get("intensity")
    states = motion.get("states", [])
    if isinstance(intensity, bool) or not isinstance(intensity, int) or not 0 <= intensity <= 4:
        raise ValueError(f"motion_intensity_invalid:{scene['shotId']}")
    if not isinstance(states, list) or not states:
        raise ValueError(f"motion_states_invalid:{scene['shotId']}")
    for state in states:
        if not isinstance(state, dict):
            raise ValueError(f"motion_states_invalid:{scene['shotId']}")
        time_range = state.get("timeRange")
        if not isinstance(time_range, list) or len(time_range) != 2:
            raise ValueError(f"motion_states_invalid:{scene['shotId']}")
    if states[0].get("timeRange", [None])[0] != 0 or states[-1].get("timeRange", [None, None])[1] != 100:
        raise ValueError(f"motion_states_invalid:{scene['shotId']}")
    static_exception = motion.get("staticException")
    camera_path = motion.get("cameraPath")
    if not isinstance(static_exception, dict) or "allowed" not in static_exception or not static_exception.get("reason"):
        raise ValueError(f"motion_static_exception_invalid:{scene['shotId']}")
    motion_audit = audit_scene_motion(scene)
    if motion_audit.get("status") == "FAIL":
        raise ValueError(f"{motion_audit.get('reason')}:{scene['shotId']}")
    if not isinstance(camera_path, dict) or scene["subject"] not in str(camera_path.get("description", "")) or scene["stateChange"] not in str(camera_path.get("description", "")):
        raise ValueError(f"motion_camera_unbound:{scene['shotId']}")
    blocked = {str(value) for value in plan.get("blockedAssetIds", [])}
    for asset in scene.get("assets", []):
        if not isinstance(asset, dict) or asset.get("blocked") is True or str(asset.get("assetId")) in blocked:
            raise ValueError(f"blocked_asset_in_scene:{scene['shotId']}:{asset.get('assetId') if isinstance(asset, dict) else ''}")


def receipt_path_for(manifest, manifest_path, episode):
    raw = manifest.get("receipt")
    if raw:
        path = Path(str(raw))
        if path.is_absolute():
            return path
        candidate = manifest_path.parent / path
        if candidate.exists() or not path.parts or path.parts[0] != "01_roteiro":
            return candidate
        return episode / path
    return episode / "01_roteiro" / f"VISUAL_REVIEW_RECEIPT_{str(manifest.get('format', 'long')).upper()}.json"


def register_receipt(manifest_path, receipt_path=None, reviewer=None, status=None, score=None, findings=None):
    manifest_path = Path(manifest_path).resolve()
    manifest = read_json(manifest_path)
    episode = manifest_path.parent.parent
    plan_path = Path(str(manifest.get("plan") or ""))
    if not plan_path.is_absolute():
        plan_path = episode / plan_path
    if not plan_path.exists():
        raise ValueError("visual_review_plan_missing")
    source = read_json(receipt_path) if receipt_path else {}
    if not isinstance(source, dict):
        raise ValueError("visual_review_receipt_invalid")
    if manifest.get("staticGuard") != "SEMANTIC_MOTION_BOUND" or manifest.get("motionAudit", {}).get("status") != "PASS":
        raise ValueError("visual_review_motion_audit_not_passed")
    actual_plan_hash = sha256(plan_path)
    if manifest.get("runId"):
        run_dir = episode / "04_video_final" / "_remotion" / "runs" / str(manifest["runId"])
        run_record = run_ledger.load_run(run_dir)
        if run_record.get("runId") != manifest.get("runId") or run_record.get("planHash") != actual_plan_hash:
            raise ValueError("visual_review_run_hash_mismatch")
    recorded_plan_hash = str(source.get("planHash") or "")
    if recorded_plan_hash and recorded_plan_hash != actual_plan_hash:
        raise ValueError("visual_review_receipt_plan_hash_mismatch")
    final_reviewer = reviewer if reviewer is not None else source.get("reviewer")
    final_status = status if status is not None else source.get("status", "PASS")
    final_score = score if score is not None else source.get("score")
    final_findings = findings if findings is not None else source.get("findings", [])
    if not str(final_reviewer or "").strip():
        raise ValueError("visual_review_reviewer_required")
    if final_status != "PASS":
        raise ValueError("visual_review_receipt_not_passed")
    try:
        final_score = float(final_score)
    except (TypeError, ValueError) as exc:
        raise ValueError("visual_review_score_invalid") from exc
    if final_score < MIN_SCORE:
        raise ValueError("visual_review_score_below_minimum")
    if not isinstance(final_findings, list):
        raise ValueError("visual_review_findings_invalid")
    if any(str(item).upper().startswith(("BLOCKER", "MAJOR")) for item in final_findings):
        raise ValueError("visual_review_blocking_findings")
    output = receipt_path_for(manifest, manifest_path, episode)
    payload = {
        "version": 1,
        "status": "PASS",
        "reviewer": str(final_reviewer),
        "score": final_score,
        "findings": final_findings,
        "planHash": actual_plan_hash,
        "runId": manifest.get("runId", ""),
        "manifest": str(manifest_path),
    }
    write_json(output, payload)
    if manifest.get("runId"):
        run_dir = episode / "04_video_final" / "_remotion" / "runs" / str(manifest["runId"])
        if run_dir.exists():
            run_ledger.append_event(run_dir, "review_receipt_registered", status="REVIEW_REQUIRED", output_hashes={str(output): sha256(output)})
    return payload


def run(plan_path, format_name, make_120_mode=None):
    plan_path = Path(plan_path).resolve()
    plan = read_json(plan_path)
    episode = plan_path.parent.parent
    fps = int(plan["video"]["fps"])
    public_dir = plan_public_dir(plan, episode)
    if not public_dir.exists():
        raise FileNotFoundError(f"render_staging_missing:{public_dir}")
    run_dir = public_dir.parent
    run_record = run_ledger.load_run(run_dir)
    if run_record.get("runId") != plan.get("runId") or run_record.get("planHash") != sha256(plan_path):
        raise ValueError("visual_review_run_hash_mismatch")
    output_dir = run_dir / "review" / format_name
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    records = []
    contact_sheets = []
    ffmpeg_available = shutil.which("ffmpeg") is not None
    should_make_120 = ffmpeg_available if make_120_mode is None else bool(make_120_mode and ffmpeg_available)
    for scene in plan.get("scenes", []):
        validate_scene(scene, plan)
        scene_id = str(scene["shotId"])
        scene_samples = []
        for label, position in (("F0", 0.0), ("F50", 0.5), ("F100", 0.995)):
            frame = frame_at(scene, position, fps)
            output = output_dir / scene_id / f"{label}.png"
            run_still(plan_path, public_dir, COMPOSITIONS[format_name], frame, output)
            item = {
                "sceneId": scene_id,
                "shotId": scene_id,
                "promptId": scene["promptId"],
                "motionIntensity": scene["motionPrompt"].get("intensity"),
                "staticException": scene["motionPrompt"].get("staticException", {}),
                "motionAudit": audit_scene_motion(scene),
                "sample": label,
                "frame": frame,
                "path": str(output),
                "hash": sha256(output),
                "status": "REVIEW_REQUIRED",
            }
            if should_make_120:
                derived = make_120(output, output.with_name(f"{label}_120.png"))
                if derived:
                    item["derived120"] = str(derived)
                    item["derived120Hash"] = sha256(derived)
            records.append(item)
            scene_samples.append(output)
        scene_sheet = make_contact_sheet(scene_samples, output_dir / scene_id / "CONTACT_SHEET.jpg")
        contact_sheets.append({"sceneId": scene_id, "path": str(scene_sheet), "hash": sha256(scene_sheet), "status": "REVIEW_REQUIRED"})
    sequence_sheet = make_contact_sheet([output_dir / str(scene["shotId"]) / f"{label}.png" for scene in plan.get("scenes", []) for label in ("F0", "F50", "F100")], output_dir / "CONTACT_SHEET_SEQUENCE.jpg")
    contact_sheets.append({"sequence": True, "path": str(sequence_sheet), "hash": sha256(sequence_sheet), "status": "REVIEW_REQUIRED"})
    manifest = {
        "status": "REVIEW_REQUIRED",
        "version": 4,
        "plan": str(plan_path),
        "planHash": sha256(plan_path),
        "runId": plan.get("runId", ""),
        "format": format_name,
        "reviewer": None,
        "receipt": str(receipt_path_for({}, Path(episode / "01_roteiro" / f"VISUAL_REVIEW_{format_name.upper()}.json"), episode)),
        "staticGuard": "SEMANTIC_MOTION_BOUND",
        "motionAudit": {
            "status": "PASS",
            "sceneCount": len(plan.get("scenes", [])),
            "meaningfulChangeCount": sum(
                next(item for item in records if item["sceneId"] == scene_id).get("motionAudit", {}).get("meaningfulChanges", 0)
                for scene_id in {item["sceneId"] for item in records}
            ),
        },
        "ffmpegAvailable": ffmpeg_available,
        "samples": records,
        "contactSheets": contact_sheets,
    }
    output = episode / "01_roteiro" / f"VISUAL_REVIEW_{format_name.upper()}.json"
    write_json(output, manifest)
    output_hashes = {}
    for item in records:
        if item.get("path") and Path(item["path"]).exists():
            output_hashes[item["path"]] = sha256(item["path"])
    for item in contact_sheets:
        if item.get("path") and Path(item["path"]).exists():
            output_hashes[item["path"]] = sha256(item["path"])
    run_ledger.append_event(run_dir, "visual_review_generated", status="REVIEW_REQUIRED", output_hashes=output_hashes)
    return manifest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--plan", required=True)
    parser.add_argument("--format", choices=["long", "short"], default="long")
    parser.add_argument("--no-120", action="store_true")
    parser.add_argument("--receipt")
    parser.add_argument("--reviewer")
    parser.add_argument("--review-status")
    parser.add_argument("--score", type=float)
    parser.add_argument("--finding", action="append")
    args = parser.parse_args()
    try:
        if args.receipt:
            manifest_path = Path(args.plan).resolve().parent / f"VISUAL_REVIEW_{args.format.upper()}.json"
            receipt = register_receipt(manifest_path, args.receipt, args.reviewer, args.review_status, args.score, args.finding)
            print(json.dumps({"status": receipt["status"], "receipt": str(receipt_path_for(read_json(manifest_path), manifest_path, manifest_path.parent.parent)), "planHash": receipt["planHash"]}, ensure_ascii=False))
            return 0
        manifest = run(Path(args.plan), args.format, False if args.no_120 else None)
        print(json.dumps({"status": manifest["status"], "samples": len(manifest["samples"]), "contactSheets": len(manifest["contactSheets"]), "manifest": str(Path(args.plan).parent / f"VISUAL_REVIEW_{args.format.upper()}.json")}, ensure_ascii=False))
        return 0
    except (OSError, ValueError, RuntimeError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    sys.exit(main())
