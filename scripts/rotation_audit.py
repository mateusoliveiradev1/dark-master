import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

VIDEO_RE = re.compile(r"^(?:video|ep|episode)[ _-]?(\d+)$", re.IGNORECASE)

def normalize(value):
    text = unicodedata.normalize("NFKD", str(value or "")).encode("ascii", "ignore").decode("ascii").lower()
    return " ".join(re.findall(r"[a-z0-9]+", text))

def words(value):
    return normalize(value).split()

def ngrams(tokens, size=3):
    if not tokens:
        return set()
    size = min(size, len(tokens))
    return {tuple(tokens[index:index + size]) for index in range(len(tokens) - size + 1)}

def similarity(left, right):
    if not left or not right:
        return 0.0
    return len(left & right) / len(left | right)

def sequence_similarity(left, right):
    if not left or not right:
        return 0.0
    set_score = similarity(set(left), set(right))
    rows = [[0] * (len(right) + 1) for _ in range(len(left) + 1)]
    for index, left_item in enumerate(left, 1):
        for right_index, right_item in enumerate(right, 1):
            if left_item == right_item:
                rows[index][right_index] = rows[index - 1][right_index - 1] + 1
            else:
                rows[index][right_index] = max(rows[index - 1][right_index], rows[index][right_index - 1])
    lcs = rows[-1][-1]
    return round((set_score + lcs / max(len(left), len(right))) / 2, 4)

def read_text(path):
    try:
        return Path(path).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""

def clean_narration(text):
    paragraphs = []
    for raw in re.split(r"\n\s*\n", text):
        lines = [line.strip() for line in raw.splitlines() if line.strip() and not line.lstrip().startswith("#")]
        value = " ".join(lines).strip()
        if value:
            paragraphs.append(value)
    return paragraphs

def title_from_episode(episode):
    for name in ("youtube_package.txt", "youtube_package.md", "PACOTE_PUBLICACAO.txt"):
        text = read_text(episode / name)
        for line in text.splitlines():
            match = re.match(r"^\s*(?:TITLE|TITULO|TÍTULO)\s*:\s*(.+)$", line, re.IGNORECASE)
            if match:
                value = match.group(1).strip()
                if value:
                    return value
    data_path = episode / "01_roteiro" / "TITLE_RESEARCH.json"
    try:
        data = json.loads(data_path.read_text(encoding="utf-8"))
        value = data.get("selected_title") if isinstance(data, dict) else ""
        if value:
            return str(value)
    except (OSError, ValueError):
        pass
    return ""

def map_data(episode):
    try:
        return json.loads((episode / "01_roteiro" / "ROTEIRO_MAP.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}

def episode_signature(episode):
    narration_path = episode / "01_roteiro" / "narration_v3.txt"
    narration = clean_narration(read_text(narration_path))
    data = map_data(episode)
    blocks = data.get("blocks", []) if isinstance(data, dict) else []
    beats = [normalize(block.get("beat", "")) for block in blocks if isinstance(block, dict) and block.get("beat")]
    hook = " ".join(narration[:2])
    cta = " ".join(narration[-2:])
    return {
        "title": title_from_episode(episode),
        "hook": hook,
        "cta": cta,
        "beats": beats,
        "narration_paragraphs": len(narration),
    }

def previous_episodes(previous, current, limit=3):
    root = Path(previous).expanduser()
    if not root.exists():
        return []
    if root.is_file():
        root = root.parent
    candidates = []
    for path in root.iterdir():
        match = VIDEO_RE.fullmatch(path.name)
        if path.is_dir() and match and path.resolve() != current.resolve():
            candidates.append((int(match.group(1)), path))
    return [path for _, path in sorted(candidates)[-limit:]]

def compare(current, prior):
    current_title = words(current["title"])
    prior_title = words(prior["title"])
    current_hook = words(current["hook"])
    prior_hook = words(prior["hook"])
    current_cta = words(current["cta"])
    prior_cta = words(prior["cta"])
    return {
        "title_similarity": round(similarity(ngrams(current_title), ngrams(prior_title)), 4),
        "title_token_similarity": round(similarity(set(current_title), set(prior_title)), 4),
        "shared_title_words": sorted(set(current_title) & set(prior_title)),
        "hook_similarity": round(similarity(ngrams(current_hook), ngrams(prior_hook)), 4),
        "beat_similarity": sequence_similarity(current["beats"], prior["beats"]),
        "cta_similarity": round(similarity(ngrams(current_cta), ngrams(prior_cta)), 4),
    }

def audit(current, previous, limit=3, thresholds=None):
    current = Path(current).expanduser().resolve()
    thresholds = thresholds or {"title": 0.72, "hook": 0.8, "beats": 0.9, "cta": 0.8}
    current_signature = episode_signature(current)
    if not current_signature["title"]:
        return {"status": "INCONCLUSIVO", "reason": "current_title_missing", "current": str(current), "history": []}
    if not current_signature["beats"]:
        return {"status": "INCONCLUSIVO", "reason": "current_map_missing", "current": str(current), "history": []}
    history_paths = previous_episodes(previous, current, limit)
    if not history_paths:
        return {"status": "INCONCLUSIVO", "reason": "previous_episodes_missing", "current": str(current), "history": []}
    history = []
    comparisons = []
    issues = []
    for path in history_paths:
        prior = episode_signature(path)
        record = {"episode": path.name, "title": prior["title"], "beats": prior["beats"]}
        history.append(record)
        if not prior["title"] or not prior["beats"]:
            continue
        values = compare(current_signature, prior)
        record["comparison"] = values
        comparisons.append({"episode": path.name, **values})
        if values["title_similarity"] >= thresholds["title"]:
            issues.append({"episode": path.name, "area": "title", "value": values["title_similarity"]})
        if values["hook_similarity"] >= thresholds["hook"]:
            issues.append({"episode": path.name, "area": "hook", "value": values["hook_similarity"]})
        if values["beat_similarity"] >= thresholds["beats"]:
            issues.append({"episode": path.name, "area": "beats", "value": values["beat_similarity"]})
        if values["cta_similarity"] >= thresholds["cta"]:
            issues.append({"episode": path.name, "area": "cta", "value": values["cta_similarity"]})
    if not comparisons:
        return {"status": "INCONCLUSIVO", "reason": "previous_metadata_missing", "current": str(current), "history": history}
    review_thresholds = {"title": 0.55, "hook": 0.6, "beats": 0.75, "cta": 0.65}
    review_issues = []
    for item in comparisons:
        for area in ("title", "hook", "beats", "cta"):
            key = "beat_similarity" if area == "beats" else f"{area}_similarity"
            if item[key] >= review_thresholds[area] and item[key] < thresholds[area]:
                review_issues.append({"episode": item["episode"], "area": area, "value": item[key]})
    status = "FAIL" if issues else "REVIEW" if review_issues else "PASS"
    return {
        "status": status,
        "current": str(current),
        "history": history,
        "comparisons": comparisons,
        "issues": issues,
        "review_issues": review_issues,
        "thresholds": thresholds,
        "scope": "last_three_episodes",
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--current", required=True)
    parser.add_argument("--previous", required=True)
    parser.add_argument("--limit", type=int, default=3)
    parser.add_argument("--out")
    args = parser.parse_args()
    result = audit(args.current, args.previous, args.limit)
    if args.out:
        output = Path(args.out).expanduser()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["status"] == "FAIL" else 0

if __name__ == "__main__":
    sys.exit(main())
