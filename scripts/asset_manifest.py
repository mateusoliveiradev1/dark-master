import argparse
import json
import re
import sys
from pathlib import Path

PROMPT_RE = re.compile(r"^\s*(\d+)\.jpg\b", re.MULTILINE)
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}

def read_prompt_ids(path):
    try:
        text = Path(path).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []
    return [int(value) for value in PROMPT_RE.findall(text)]

def read_images(path):
    root = Path(path).expanduser()
    if not root.exists():
        return {}
    result = {}
    for image in root.iterdir():
        if not image.is_file() or image.suffix.lower() not in IMAGE_EXTENSIONS:
            continue
        match = re.search(r"(\d+)", image.stem)
        if match:
            result[int(match.group(1))] = image
    return result

def audit(images_path, prompts_path=None, expected=None):
    images_root = Path(images_path).expanduser()
    if prompts_path is None:
        candidates = [path for path in images_root.iterdir() if path.is_file()] if images_root.exists() else []
        prompts_path = next((path for path in candidates if path.name.upper() == "PROMPTS.MD"), images_root / "PROMPTS.md")
    prompts = read_prompt_ids(prompts_path)
    if expected is not None:
        prompt_ids = list(range(1, expected + 1))
    else:
        prompt_ids = sorted(set(prompts))
    if not prompt_ids:
        return {"status": "INCONCLUSIVO", "reason": "prompts_missing", "expected": 0, "assets": []}
    images = read_images(images_root)
    assets = []
    for prompt_id in prompt_ids:
        path = images.get(prompt_id)
        assets.append({
            "prompt_id": prompt_id,
            "asset": str(path) if path else None,
            "status": "PRESENT" if path else "MISSING",
            "bytes": path.stat().st_size if path else 0,
        })
    missing = [item["prompt_id"] for item in assets if item["status"] != "PRESENT"]
    return {
        "status": "FAIL" if missing else "PASS",
        "prompts": str(prompts_path),
        "expected": len(prompt_ids),
        "present": len(prompt_ids) - len(missing),
        "missing": missing,
        "assets": assets,
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--images", required=True)
    parser.add_argument("--prompts")
    parser.add_argument("--expected", type=int)
    parser.add_argument("--out")
    args = parser.parse_args()
    result = audit(args.images, args.prompts, args.expected)
    if args.out:
        output = Path(args.out).expanduser()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["status"] == "FAIL" else 0

if __name__ == "__main__":
    sys.exit(main())
