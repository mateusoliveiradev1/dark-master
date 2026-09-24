from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

VERSION = 1


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def canonical_bytes(value) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def hash_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def hash_json(value) -> str:
    return hash_bytes(canonical_bytes(value))


def hash_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def file_hashes(paths: dict[str, Path]) -> dict[str, str]:
    return {key: hash_file(path) for key, path in sorted(paths.items()) if path.exists() and path.is_file()}


def tool_version(executable: str, args: list[str] | None = None) -> str:
    path = shutil.which(executable)
    if not path:
        return ""
    try:
        result = subprocess.run([path, *(args or ["-version"])], capture_output=True, text=True, errors="replace", check=False)
    except OSError:
        return ""
    output = (result.stdout or result.stderr or "").strip().splitlines()
    return output[0].strip() if output else ""


def versions(remotion_root: Path) -> dict[str, str]:
    package = {}
    try:
        package = json.loads((remotion_root / "package.json").read_text(encoding="utf-8"))
    except (OSError, ValueError, TypeError):
        package = {}
    return {
        "node": tool_version("node", ["--version"]),
        "remotion": str((package.get("dependencies", {}) or {}).get("remotion", "")),
        "ffmpeg": tool_version("ffmpeg"),
    }


def relative(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.name


def safe_gate_value(value):
    if isinstance(value, dict):
        return {str(key): safe_gate_value(item) for key, item in value.items() if not any(token in str(key).lower() for token in ("secret", "token", "password", "api_key"))}
    if isinstance(value, list):
        return [safe_gate_value(item) for item in value]
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    return str(value)


def run_root(episode: Path) -> Path:
    return Path(episode) / "04_video_final" / "_remotion" / "runs"


def run_identity(episode: Path, format_name: str, input_hash: str, profile_hash: str) -> str:
    return hash_json({
        "episode": Path(episode).name,
        "format": format_name,
        "inputHash": input_hash,
        "profileHash": profile_hash,
    })[:24]


def reserve_run_dir(episode: Path, run_id: str) -> Path:
    base = run_root(episode) / run_id
    candidate = base
    suffix = 2
    while candidate.exists():
        candidate = run_root(episode) / f"{run_id}-{suffix}"
        suffix += 1
    candidate.mkdir(parents=True, exist_ok=False)
    return candidate


def write_exclusive_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def append_event(run_dir: Path, event: str, status: str | None = None, output_hashes: dict | None = None, gates: dict | None = None) -> dict:
    record = {"event": event, "at": now()}
    if status is not None:
        record["status"] = status
    if output_hashes is not None:
        record["outputHashes"] = safe_gate_value(output_hashes)
    if gates is not None:
        record["gates"] = safe_gate_value(gates)
    path = Path(run_dir) / "run.events.jsonl"
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")
    return record


def create_run(
    episode: Path,
    format_name: str,
    run_id: str,
    run_dir: Path | None,
    input_hashes: dict,
    output_hashes: dict | None,
    plan_hash: str,
    profile_hash: str,
    gates: dict,
    plan_path: Path,
    staging: Path,
    remotion_root: Path,
) -> tuple[Path, dict]:
    target = Path(run_dir) if run_dir is not None else reserve_run_dir(Path(episode), run_id)
    target.mkdir(parents=True, exist_ok=True)
    record = {
        "version": VERSION,
        "runId": run_id,
        "episode": Path(episode).name,
        "format": format_name,
        "status": "PLANNED",
        "createdAt": now(),
        "inputHashes": safe_gate_value(input_hashes),
        "outputHashes": safe_gate_value(output_hashes or {}),
        "versions": versions(remotion_root),
        "gates": safe_gate_value(gates),
        "planHash": plan_hash,
        "profileHash": profile_hash,
        "plan": relative(Path(plan_path), Path(episode)),
        "staging": relative(Path(staging), Path(episode)),
        "events": "run.events.jsonl",
    }
    write_exclusive_json(target / "run.json", record)
    append_event(target, "created", status="PLANNED", gates=gates)
    return target, record


def load_run(run_dir: Path) -> dict:
    path = Path(run_dir) / "run.json"
    if not path.exists():
        raise FileNotFoundError(f"run_ledger_missing:{path}")
    record = json.loads(path.read_text(encoding="utf-8"))
    events = []
    events_path = Path(run_dir) / "run.events.jsonl"
    if events_path.exists():
        for line in events_path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                try:
                    events.append(json.loads(line))
                except ValueError:
                    continue
    record["events"] = events
    if events:
        latest = events[-1]
        if latest.get("status") is not None:
            record["status"] = latest["status"]
        merged_outputs = dict(record.get("outputHashes", {}))
        for event in events:
            merged_outputs.update(event.get("outputHashes", {}))
        record["outputHashes"] = merged_outputs
        if latest.get("gates") is not None:
            record["gates"] = latest["gates"]
    return record


def append_run_event(run_dir: Path, event: str, status: str | None = None, output_hashes: dict | None = None, gates: dict | None = None) -> dict:
    record = load_run(run_dir)
    effective_outputs = record.get("outputHashes", {}) if output_hashes is None else output_hashes
    effective_gates = record.get("gates", {}) if gates is None else gates
    return append_event(Path(run_dir), event, status=status, output_hashes=effective_outputs, gates=effective_gates)


def file_hash_map(root: Path, paths: list[Path]) -> dict[str, str]:
    return {relative(path, root): hash_file(path) for path in paths if path.exists() and path.is_file()}
