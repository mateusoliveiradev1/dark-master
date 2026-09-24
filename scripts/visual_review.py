import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REMOTION_ROOT = HERE.parent / "remotion"
COMPOSITIONS = {"long": "DarkMasterLong", "short": "DarkMasterShort"}


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def frame_at(scene, position, fps):
    start = float(scene["startSeconds"])
    duration = float(scene["durationSeconds"])
    return max(0, round((start + duration * position) * fps))


def run_still(plan_path, public_dir, composition_id, frame, output):
    output.parent.mkdir(parents=True, exist_ok=True)
    env = {**os.environ, "DARK_MASTER_RENDER_PLAN": str(plan_path), "DARK_MASTER_PUBLIC_DIR": str(public_dir), "DARK_MASTER_STILL": str(output)}
    command = ["npm", "--prefix", str(REMOTION_ROOT), "run", "render:still", "--", composition_id, str(frame)]
    result = subprocess.run(command, cwd=REMOTION_ROOT, env=env, text=True, capture_output=True)
    if result.returncode != 0:
        raise RuntimeError(result.stdout + result.stderr)
    return output


def make_120(path, output):
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise RuntimeError("ffmpeg_not_found")
    output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([ffmpeg, "-y", "-i", str(path), "-vf", "scale=213:120:force_original_aspect_ratio=decrease,pad=213:120:(ow-iw)/2:(oh-ih)/2:color=black", str(output)], check=True, capture_output=True)
    return output


def run(plan_path, format_name, make_120_mode):
    plan = read_json(plan_path)
    fps = int(plan["video"]["fps"])
    episode = plan_path.parent.parent
    public_dir = episode / "04_video_final" / "_remotion" / "public"
    output_dir = episode / "04_video_final" / "_remotion" / "stills" / format_name
    records = []
    for scene in plan.get("scenes", []):
        scene_id = str(scene["id"])
        samples = [("F0", 0.0), ("F50", 0.5), ("F100", 0.995)]
        for label, position in samples:
            frame = frame_at(scene, position, fps)
            output = output_dir / scene_id / f"{label}.png"
            run_still(plan_path, public_dir, COMPOSITIONS[format_name], frame, output)
            item = {"sceneId": scene_id, "sample": label, "frame": frame, "path": str(output), "status": "REVIEW_REQUIRED"}
            if make_120_mode:
                derived = output.with_name(f"{label}_120.png")
                make_120(output, derived)
                item["derived120"] = str(derived)
            records.append(item)
    manifest = {"status": "REVIEW_REQUIRED", "version": 1, "plan": str(plan_path), "format": format_name, "reviewer": None, "staticGuard": "PENDING", "samples": records}
    output = episode / "01_roteiro" / f"VISUAL_REVIEW_{format_name.upper()}.json"
    output.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--plan", required=True)
    parser.add_argument("--format", choices=["long", "short"], default="long")
    parser.add_argument("--make-120", action="store_true")
    args = parser.parse_args()
    manifest = run(Path(args.plan), args.format, args.make_120)
    print(json.dumps({"status": manifest["status"], "samples": len(manifest["samples"]), "manifest": str(Path(args.plan).parent / f"VISUAL_REVIEW_{args.format.upper()}.json")}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
