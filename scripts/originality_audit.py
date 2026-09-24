#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path


def tokens(text):
    return re.findall(r"\w+", (text or "").lower(), flags=re.UNICODE)


def ngrams(text, size=5):
    values = tokens(text)
    return {tuple(values[index:index + size]) for index in range(max(0, len(values) - size + 1))}


def similarity(left, right):
    if not left or not right:
        return 0.0
    return len(left & right) / len(left | right)


def previous_files(value, current):
    if not value:
        return []
    root = Path(value).expanduser()
    if root.is_file():
        return [root.resolve()] if root.resolve() != current.resolve() else []
    if not root.is_dir():
        return []
    files = []
    for path in root.rglob("*.txt"):
        if path.name.startswith("narration") and path.resolve() != current.resolve():
            files.append(path.resolve())
    return sorted(files)


def audit(narration, previous, threshold=0.45):
    current_path = Path(narration).expanduser()
    if not current_path.exists():
        return {"status": "FAIL", "error": "narration_missing"}
    current_text = current_path.read_text(encoding="utf-8", errors="replace")
    current_grams = ngrams(current_text)
    comparisons = []
    repeated = set()
    for path in previous_files(previous, current_path):
        prior_grams = ngrams(path.read_text(encoding="utf-8", errors="replace"))
        score = similarity(current_grams, prior_grams)
        shared = current_grams & prior_grams
        repeated.update(shared)
        comparisons.append({"file": str(path), "similarity": round(score, 4), "shared_ngrams": len(shared)})
    comparisons.sort(key=lambda item: item["similarity"], reverse=True)
    maximum = comparisons[0]["similarity"] if comparisons else 0.0
    if maximum >= threshold:
        status = "FAIL"
    elif maximum >= threshold * 0.65:
        status = "REVIEW"
    else:
        status = "PASS"
    return {
        "status": status,
        "current": str(current_path),
        "previous_count": len(comparisons),
        "max_similarity": maximum,
        "threshold": threshold,
        "repeated_ngrams": [" ".join(value) for value in sorted(repeated)][:20],
        "comparisons": comparisons[:20],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--narration", required=True)
    parser.add_argument("--previous")
    parser.add_argument("--threshold", type=float, default=0.45)
    parser.add_argument("--out")
    args = parser.parse_args()
    result = audit(args.narration, args.previous, args.threshold)
    if args.out:
        output = Path(args.out)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("status") in {"PASS", "REVIEW"} else 1


if __name__ == "__main__":
    sys.exit(main())
