import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

PROMPT_HEADING_RE = re.compile(r"^\s*##\s+((?:PROMPT|P)-[A-Z0-9][A-Z0-9._-]*)\b", re.MULTILINE)
PROMPT_TOKEN_RE = re.compile(r"\b(?:PROMPT|P)-[A-Z0-9][A-Z0-9._-]*\b", re.IGNORECASE)
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
MANIFEST_NAMES = ("ASSET_MANIFEST.json", "asset_manifest.json")
PENDING_RIGHTS = {"", "pending", "unknown", "unverified", "unclear"}


def read_prompt_ids(path):
    try:
        text = Path(path).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []
    headings = [match.group(1).upper() for match in PROMPT_HEADING_RE.finditer(text)]
    return headings or [match.group(0).upper() for match in PROMPT_TOKEN_RE.finditer(text)]


def read_prompt_plan(path):
    if not path or not Path(path).exists():
        return None
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {"status": "INVALID", "prompts": []}
    return data if isinstance(data, dict) else {"status": "INVALID", "prompts": []}


def read_images(path):
    root = Path(path).expanduser()
    if not root.exists():
        return {}
    return {
        image.stem: image
        for image in sorted(root.iterdir(), key=lambda value: value.name)
        if image.is_file() and image.suffix.lower() in IMAGE_EXTENSIONS
    }


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def manifest_records(data):
    if not isinstance(data, dict):
        return [], ["asset_manifest_invalid"]
    raw = data.get("assets", data.get("records", []))
    records = []
    errors = []
    if isinstance(raw, list):
        candidates = raw
    elif isinstance(raw, dict):
        candidates = []
        for asset_id, value in raw.items():
            if isinstance(value, dict):
                candidates.append({"assetId": asset_id, **value})
            else:
                errors.append(f"asset_manifest_record_invalid:{asset_id}")
    else:
        candidates = []
        errors.append("asset_manifest_assets_invalid")
    for index, value in enumerate(candidates, 1):
        if not isinstance(value, dict):
            errors.append(f"asset_manifest_record_invalid:{index}")
            continue
        records.append(dict(value))
    return records, errors


def find_manifest(images_path, manifest_path=None):
    if manifest_path:
        path = Path(manifest_path).expanduser()
        return path, [] if path.exists() else [f"asset_manifest_missing:{path}"]
    root = Path(images_path).expanduser()
    for name in MANIFEST_NAMES:
        candidate = root / name
        if candidate.exists():
            return candidate, []
    return None, ["identity_manifest_required"]


def load_asset_records(images_path, plan_path=None, manifest_path=None):
    errors = []
    records = []
    manifest, manifest_errors = find_manifest(images_path, manifest_path)
    errors.extend(manifest_errors)
    if manifest and manifest.exists():
        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return [], errors + ["asset_manifest_invalid"]
        records, record_errors = manifest_records(data)
        errors.extend(record_errors)
        return records, errors
    plan = read_prompt_plan(plan_path)
    if plan:
        for prompt in plan.get("prompts", []):
            if not isinstance(prompt, dict):
                continue
            for asset in prompt.get("assetBindings", []) or []:
                if isinstance(asset, dict) and str(asset.get("path") or "").strip():
                    records.append(dict(asset))
    return records, errors


def expected_prompts(plan, expected=None):
    errors = []
    prompts = []
    seen = set()
    for index, record in enumerate((plan or {}).get("prompts", []), 1):
        if not isinstance(record, dict):
            errors.append(f"prompt_plan_record_invalid:{index}")
            continue
        prompt_id = str(record.get("promptId") or "").strip()
        shot_id = str(record.get("shotId") or "").strip()
        if not prompt_id or not shot_id:
            errors.append(f"prompt_identity_missing:{index}")
            continue
        if prompt_id in seen:
            errors.append(f"prompt_identity_duplicate:{prompt_id}")
            continue
        seen.add(prompt_id)
        prompts.append({
            "promptId": prompt_id,
            "shotId": shot_id,
            "sourceBlockIds": [str(value) for value in record.get("sourceBlockIds", [])],
        })
    if expected is not None and expected != len(prompts):
        errors.append(f"prompt_count_mismatch:{expected}:{len(prompts)}")
    return prompts, errors


def resolve_asset_path(images_path, value):
    raw = Path(str(value)).expanduser()
    if re.match(r"^[a-z]+://", str(raw), flags=re.IGNORECASE):
        return None, "asset_path_remote"
    path = raw if raw.is_absolute() else Path(images_path).expanduser() / raw
    try:
        resolved = path.resolve()
    except OSError:
        return None, "asset_path_invalid"
    if not resolved.exists() or not resolved.is_file():
        return resolved, "asset_missing"
    if resolved.suffix.lower() not in IMAGE_EXTENSIONS:
        return resolved, "asset_type_invalid"
    return resolved, None


def hash_matches(recorded, computed):
    value = str(recorded or "").strip().lower().removeprefix("sha256:")
    return bool(value) and value == computed.lower()


def resolve_assets(images_path, plan_path=None, manifest_path=None, expected=None):
    images_root = Path(images_path).expanduser()
    plan = read_prompt_plan(plan_path)
    errors = []
    if not plan:
        return {"status": "INCONCLUSIVO", "reason": "prompt_plan_missing", "assets": []}
    if plan.get("status") != "PROMPTS_READY":
        return {"status": "INCONCLUSIVO", "reason": "prompt_plan_not_ready", "planStatus": plan.get("status", "MISSING"), "assets": []}
    prompts, prompt_errors = expected_prompts(plan, expected)
    errors.extend(prompt_errors)
    if not prompts:
        errors.append("prompts_missing")
    records, manifest_errors = load_asset_records(images_root, plan_path, manifest_path)
    errors.extend(manifest_errors)
    if not records:
        errors.append("identity_manifest_required")
    expected_by_prompt = {record["promptId"]: record for record in prompts}
    grouped = {record["promptId"]: [] for record in prompts}
    seen_asset_ids = set()
    output = []
    for index, source in enumerate(records, 1):
        asset_id = str(source.get("assetId") or "").strip()
        prompt_id = str(source.get("promptId") or "").strip()
        shot_id = str(source.get("shotId") or "").strip()
        source_blocks = [str(value) for value in source.get("sourceBlockIds", [])]
        prompt = expected_by_prompt.get(prompt_id)
        record = {
            "assetId": asset_id,
            "promptId": prompt_id,
            "shotId": shot_id,
            "sourceBlockIds": source_blocks,
            "path": str(source.get("path") or source.get("file") or ""),
            "layer": source.get("layer"),
            "hash": source.get("hash"),
            "rightsStatus": source.get("rightsStatus"),
            "blocked": source.get("blocked"),
            "role": str(source.get("role") or "primary"),
            "kind": str(source.get("kind") or "image"),
            "origin": str(source.get("origin") or "pending"),
        }
        if not asset_id:
            errors.append(f"asset_id_missing:{index}")
        elif asset_id in seen_asset_ids:
            errors.append(f"asset_id_duplicate:{asset_id}")
        seen_asset_ids.add(asset_id)
        if not prompt:
            errors.append(f"asset_prompt_unbound:{asset_id or index}:{prompt_id or 'missing'}")
            record["status"] = "UNBOUND"
            record["bytes"] = 0
            output.append(record)
            continue
        if shot_id != prompt["shotId"]:
            errors.append(f"asset_shot_mismatch:{asset_id}:{shot_id}:{prompt['shotId']}")
        if not source_blocks:
            errors.append(f"asset_source_blocks_missing:{asset_id}")
        elif prompt["sourceBlockIds"] and not set(source_blocks).issuperset(set(prompt["sourceBlockIds"])):
            errors.append(f"asset_source_blocks_mismatch:{asset_id}")
        if "blocked" not in source or not isinstance(source.get("blocked"), bool):
            errors.append(f"asset_blocked_invalid:{asset_id}")
        if "rightsStatus" not in source:
            errors.append(f"asset_rights_status_missing:{asset_id}")
        path, path_error = resolve_asset_path(images_root, record["path"])
        computed_hash = None
        if path_error:
            record["status"] = "MISSING" if path_error == "asset_missing" else path_error.upper()
            errors.append(f"{path_error}:{asset_id}")
        else:
            record["bytes"] = path.stat().st_size
            computed_hash = sha256(path)
            if source.get("hash") and not hash_matches(source.get("hash"), computed_hash):
                record["status"] = "HASH_MISMATCH"
                errors.append(f"asset_hash_mismatch:{asset_id}")
            elif source.get("blocked") is True:
                record["status"] = "BLOCKED"
            elif str(source.get("rightsStatus") or "").strip().lower() in PENDING_RIGHTS:
                record["status"] = "RIGHTS_PENDING"
            else:
                record["status"] = "PRESENT"
        record["computedHash"] = computed_hash
        grouped.setdefault(prompt_id, []).append(record)
        output.append(record)
    missing = []
    unresolved = []
    for prompt in prompts:
        records_for_prompt = grouped.get(prompt["promptId"], [])
        usable = [record for record in records_for_prompt if record.get("status") == "PRESENT"]
        if not records_for_prompt or not usable:
            missing.append(prompt["promptId"])
            unresolved.append(prompt["promptId"])
    blocked = [record["assetId"] for record in output if record.get("blocked") is True]
    hash_mismatches = [record["assetId"] for record in output if record.get("status") == "HASH_MISMATCH"]
    rights_pending = [record["assetId"] for record in output if record.get("status") == "RIGHTS_PENDING"]
    errors = sorted(set(errors))
    failed = bool(errors or missing or blocked or hash_mismatches or rights_pending)
    status = "FAIL" if failed else "PASS"
    resolved_manifest, _ = find_manifest(images_root, manifest_path)
    reason = None
    if failed:
        reason = "identity_resolution_failed" if errors else "asset_gate_failed"
    return {
        "status": status,
        "reason": reason,
        "prompts": str(plan_path) if plan_path else None,
        "manifest": str(resolved_manifest) if resolved_manifest else None,
        "expected": len(prompts),
        "present": sum(1 for record in output if record.get("status") == "PRESENT"),
        "missing": missing,
        "unresolved": unresolved,
        "blocked": blocked,
        "hashMismatches": hash_mismatches,
        "rightsPending": rights_pending,
        "errors": errors,
        "assets": output,
    }


def audit(images_path, prompts_path=None, expected=None, plan_path=None, manifest_path=None):
    if plan_path is None:
        script_dir = Path(images_path).expanduser().parent / "01_roteiro"
        candidate = script_dir / "PROMPT_PLAN.json"
        plan_path = candidate if candidate.exists() else None
    return resolve_assets(images_path, plan_path, manifest_path, expected)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--images", required=True)
    parser.add_argument("--prompts")
    parser.add_argument("--plan")
    parser.add_argument("--manifest")
    parser.add_argument("--expected", type=int)
    parser.add_argument("--out")
    args = parser.parse_args()
    result = audit(args.images, args.prompts, args.expected, args.plan, args.manifest)
    if args.out:
        output = Path(args.out).expanduser()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
