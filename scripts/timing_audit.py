#!/usr/bin/env python3
import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path


def target_bounds(value):
    match = re.fullmatch(r"(\d{1,3})(?:-(\d{1,3}))?", (value or "").strip())
    if not match:
        raise ValueError("target-minutes deve ser 30 ou 30-35")
    first = int(match.group(1))
    last = int(match.group(2) or first)
    if first < 1 or last < first or last > 180:
        raise ValueError("target-minutes fora do intervalo")
    return first * 60, last * 60


def words(text):
    return len(re.findall(r"\w+", text or "", flags=re.UNICODE))


def audio_seconds(path):
    ffprobe = shutil.which("ffprobe")
    if not ffprobe:
        return None, "ffprobe_not_found"
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


def timing_from_file(path):
    if not path or not Path(path).exists():
        return None, "timing_file_missing", {}
    source = Path(path)
    if source.suffix.lower() == ".json":
        try:
            data = json.loads(source.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            return None, f"timing_json_invalid:{exc}", {}
        blocks = data.get("blocos") or data.get("blocks") or []
        total = data.get("total")
        if total is None:
            ends = [float(block.get("end", block.get("dur", 0)) or 0) for block in blocks if isinstance(block, dict)]
            total = max(ends) if ends else 0
        block_times = [
            {
                "start": float(block.get("start", 0) or 0),
                "end": float(block.get("end", 0) or 0),
                "dur": float(block.get("dur", 0) or 0),
            }
            for block in blocks if isinstance(block, dict)
        ]
        return float(total or 0), "", {"blocks": len(blocks), "total": float(total or 0), "block_times": block_times}
    seconds, error = audio_seconds(source)
    return seconds, error, {}


def audit(narration, captions_times, target_minutes, voice=None, map_path=None):
    lo, hi = target_bounds(target_minutes)
    seconds, error, details = timing_from_file(captions_times)
    if error:
        return {"status": "FALHA", "error": error, "target_minutes": target_minutes}
    voice_seconds = None
    if voice:
        voice_seconds, voice_error = audio_seconds(Path(voice))
        if voice_error:
            return {"status": "FALHA", "error": f"voice_{voice_error}", "target_minutes": target_minutes}
    actual = voice_seconds if voice_seconds is not None else seconds
    actual_minutes = actual / 60 if actual is not None else 0
    narration_path = Path(narration)
    if not narration_path.exists():
        return {"status": "FALHA", "error": "narration_missing", "target_minutes": target_minutes}
    narration_words = words(narration_path.read_text(encoding="utf-8", errors="replace"))
    wpm = narration_words / actual_minutes if actual_minutes else 0
    beat_timing = []
    beat_errors = []
    if map_path:
        try:
            map_data = json.loads(Path(map_path).read_text(encoding="utf-8"))
            map_blocks = map_data.get("blocks", [])
        except (OSError, ValueError, AttributeError) as exc:
            map_blocks = []
            beat_errors.append(f"map_invalid:{exc}")
        block_times = details.get("block_times", [])
        if not block_times:
            beat_errors.append("map_timing_blocks_missing")
        elif len(map_blocks) != len(block_times):
            beat_errors.append(f"map_timing_count_mismatch({len(map_blocks)}!={len(block_times)})")
        else:
            for block, actual_block in zip(map_blocks, block_times):
                target = float(block.get("target_seconds", 0) or 0)
                measured = float(actual_block.get("dur", 0) or 0)
                tolerance = max(30, target * 0.5)
                passed = measured > 0 and abs(measured - target) <= tolerance
                beat_timing.append({
                    "id": block.get("id"),
                    "beat": block.get("beat"),
                    "target_seconds": target,
                    "actual_seconds": measured,
                    "status": "PASS" if passed else "FALHA",
                })
                if not passed:
                    beat_errors.append(f"beat_timing:{block.get('id')}")
    status = "PASS" if lo <= (actual or 0) <= hi and not beat_errors else "FALHA"
    return {
        "status": status,
        "target_minutes": target_minutes,
        "target_seconds": [lo, hi],
        "actual_seconds": round(actual or 0, 3),
        "actual_minutes": round(actual_minutes, 3),
        "narration_words": narration_words,
        "words_per_minute": round(wpm, 1),
        "captions": {key: value for key, value in details.items() if key != "block_times"},
        "beat_timing": beat_timing,
        "beat_errors": beat_errors,
        "voice_checked": bool(voice),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--narration", required=True)
    parser.add_argument("--captions-times", required=True)
    parser.add_argument("--target-minutes", required=True)
    parser.add_argument("--voice")
    parser.add_argument("--map")
    parser.add_argument("--out")
    args = parser.parse_args()
    result = audit(args.narration, args.captions_times, args.target_minutes, args.voice, args.map)
    if args.out:
        output = Path(args.out)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("status") == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
