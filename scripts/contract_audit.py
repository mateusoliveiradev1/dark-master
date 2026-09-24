#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILL_ROOT = HERE.parent
PLAYBOOKS = SKILL_ROOT / "playbooks"
REQUIRED = ("profile.md", "voice.json", "roteiro.json")


def read(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--channel", required=True)
    parser.add_argument("--root")
    args = parser.parse_args()
    root = Path(args.root).expanduser().resolve() if args.root else SKILL_ROOT
    candidates = [root / "playbooks" / args.channel, PLAYBOOKS / args.channel]
    channel_dir = next((path for path in candidates if path.exists()), None)
    errors = []
    if channel_dir is None:
        errors.append("channel_not_found")
    else:
        for name in REQUIRED:
            if not (channel_dir / name).exists():
                errors.append(f"missing:{name}")
        style = read(channel_dir / "style.json") or {}
        motion = read(channel_dir / "motion.json")
        voice = read(channel_dir / "voice.json") or {}
        if motion:
            if motion.get("engine") not in {"remotion", "legacy", None}:
                errors.append("invalid_motion_engine")
            if motion.get("engine") == "remotion" and motion.get("fps", 0) <= 0:
                errors.append("invalid_fps")
            if motion.get("engine") == "remotion" and not (channel_dir / "visual.json").exists():
                errors.append("missing:visual.json")
        if style.get("language") and voice.get("language") and style["language"] != voice["language"]:
            errors.append("language_mismatch")
        if style and not style.get("image_suffix"):
            errors.append("missing_image_suffix")
    result = {"status": "PASS" if not errors else "FAIL", "channel": args.channel, "path": str(channel_dir) if channel_dir else "", "errors": errors}
    print(json.dumps(result, ensure_ascii=False))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
