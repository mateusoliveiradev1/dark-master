#!/usr/bin/env python3
import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from script_builder import validate_funnel_plan, words


def narration_blocks(path):
    text = Path(path).read_text(encoding="utf-8", errors="replace")
    return [block.strip() for block in re.split(r"\n\s*\n", text) if block.strip()]


def video_duration(path):
    ffprobe = shutil.which("ffprobe")
    if not ffprobe or not Path(path).exists():
        return None, "ffprobe_or_video_missing"
    result = subprocess.run(
        [ffprobe, "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        capture_output=True,
        text=True,
    )
    if result.returncode:
        return None, result.stderr.strip() or "ffprobe_failed"
    try:
        return float(result.stdout.strip()), ""
    except ValueError as exc:
        return None, f"ffprobe_invalid:{exc}"


def frame_similarity(video):
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg or not Path(video).exists():
        return None, "ffmpeg_or_video_missing"
    with tempfile.TemporaryDirectory(prefix="short-qa-") as temp:
        first = Path(temp) / "first.png"
        last = Path(temp) / "last.png"
        first_cmd = [ffmpeg, "-y", "-ss", "0.1", "-i", str(video), "-frames:v", "1", str(first)]
        last_cmd = [ffmpeg, "-y", "-sseof", "-0.2", "-i", str(video), "-frames:v", "1", str(last)]
        if subprocess.run(first_cmd, capture_output=True).returncode or subprocess.run(last_cmd, capture_output=True).returncode:
            return None, "frame_extract_failed"
        result = subprocess.run(
            [ffmpeg, "-i", str(first), "-i", str(last), "-lavfi", "ssim", "-f", "null", "-"],
            capture_output=True,
            text=True,
        )
        match = re.search(r"All:([0-9.]+)", result.stderr or "")
        if not match:
            return None, "ssim_unavailable"
        return float(match.group(1)), ""


def first_words_overlap(short_path, long_path):
    short = narration_blocks(short_path)
    long = narration_blocks(long_path)
    if not short or not long:
        return 0
    short_words = re.findall(r"\w+", short[0].lower(), flags=re.UNICODE)[:10]
    long_words = set(re.findall(r"\w+", long[0].lower(), flags=re.UNICODE)[:10])
    return len(set(short_words) & long_words)


def run(narration, plan, video=None, long_form=None):
    errors = []
    if not Path(narration).exists():
        errors.append("narration_missing")
        blocks = []
    else:
        blocks = narration_blocks(narration)
    if not blocks:
        errors.append("short_narration_empty")
    elif words(blocks[0]) > 8:
        errors.append(f"hook_short_longo({words(blocks[0])}>8)")
    if len(blocks) > 4:
        errors.append(f"muitos_blocos({len(blocks)}>4)")
    errors.extend(validate_funnel_plan(plan))
    overlap = first_words_overlap(narration, long_form) if long_form and Path(long_form).exists() else 0
    if overlap >= 5:
        errors.append(f"short_long_overlap({overlap}>=5)")
    duration, duration_error = video_duration(video) if video else (None, "")
    similarity, similarity_error = frame_similarity(video) if video else (None, "")
    video_checks = {}
    if video:
        if duration is None:
            errors.append(duration_error or "video_duration_unavailable")
        else:
            video_checks["duration_seconds"] = round(duration, 3)
            if duration < 8 or duration > 90:
                errors.append(f"short_duration_invalida({duration:.3f})")
        if similarity is None:
            errors.append(similarity_error or "loop_visual_unavailable")
        else:
            video_checks["frame_similarity"] = round(similarity, 4)
            if similarity < 0.55:
                errors.append(f"loop_visual_fraco({similarity:.3f})")
    else:
        video_checks["status"] = "REVIEW"
        errors.append("video_missing_for_full_qa")
    if errors:
        status = "REVIEW" if video is None and errors == ["video_missing_for_full_qa"] else "FAIL"
    else:
        status = "PASS"
    return {
        "status": status,
        "narration_words": words(Path(narration).read_text(encoding="utf-8", errors="replace")) if Path(narration).exists() else 0,
        "hook_words": words(blocks[0]) if blocks else 0,
        "blocks": len(blocks),
        "first_words_overlap_with_long": overlap,
        "video": video_checks,
        "errors": errors,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--narration", required=True)
    parser.add_argument("--plan", required=True)
    parser.add_argument("--video")
    parser.add_argument("--long")
    parser.add_argument("--out")
    args = parser.parse_args()
    result = run(args.narration, args.plan, args.video, args.long)
    if args.out:
        output = Path(args.out)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] in {"PASS", "REVIEW"} else 1


if __name__ == "__main__":
    sys.exit(main())
