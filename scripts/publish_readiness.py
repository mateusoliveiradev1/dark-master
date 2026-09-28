#!/usr/bin/env python3
"""publish_readiness.py — veredito unico pre-publicacao (todos os gates).

Agrega audit_all.audit_video + par estrito titulo/thumb (com os titulos do
PACKAGING vencedor) + disclosure IA. Emite READINESS.json; sai 1 se bloqueado.
Uso: python scripts/publish_readiness.py <videoNN> [--previous <canal>] [--out ...]
"""
import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from audit_all import audit_video
from thumb_audit import audit as thumb_audit_fn, parse_titles as thumb_parse_titles


def winner_titles(packaging_path):
    try:
        data = json.loads(Path(packaging_path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return []
    pairs = data.get("pairs", []) if isinstance(data, dict) else []
    winner = (data.get("decision", {}) or {}).get("winner_id") if isinstance(data, dict) else None
    for pair in pairs:
        if isinstance(pair, dict) and pair.get("id") == winner:
            title = pair.get("title", {})
            return [title.get("pt", ""), title.get("en", "")]
    return []


def disclosure_status(video_dir):
    for name in ("DISCLOSURE_IA.txt", "DISCLOSURE_AI.txt"):
        if (video_dir / name).exists() or (video_dir / "01_roteiro" / name).exists():
            return "declared"
    try:
        contract = json.loads((video_dir / "02_audio" / "voice_contract.json").read_text(encoding="utf-8"))
        engine = str(contract.get("engine", "")).lower()
    except (OSError, ValueError):
        return "unknown"
    if engine in {"human", "humana", "studio"}:
        return "human_voice"
    return "synthetic_undeclared"


def readiness_from(audit_result, strict_pair, disclosure):
    blockers = list(audit_result.get("flags", []))
    if strict_pair.get("status") == "FAIL":
        blockers.append("strict_pair")
    if disclosure == "synthetic_undeclared":
        blockers.append("disclosure")
    elif disclosure == "unknown":
        blockers.append("disclosure_unknown")
    return {"status": "READY" if not blockers else "BLOCKED",
            "audit_veredito": audit_result.get("veredito"),
            "strict_pair": strict_pair.get("status"),
            "disclosure": disclosure,
            "blockers": sorted(set(blockers))}


def readiness(video):
    video_dir = Path(video).expanduser()
    script_dir = video_dir / "01_roteiro"
    audit_result = audit_video(video_dir)
    brief_path = script_dir / "THUMB_BRIEF.json"
    try:
        brief = json.loads(brief_path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        brief = {}
    titles = winner_titles(script_dir / "PACKAGING.json")
    strict_pair = thumb_audit_fn(brief, titles, script_dir) if brief else {"status": "FAIL", "errors": ["brief_missing"]}
    disclosure = disclosure_status(video_dir)
    result = {"video": video_dir.name, **readiness_from(audit_result, strict_pair, disclosure),
              "gates": audit_result.get("gates", {})}
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("video")
    parser.add_argument("--previous", default="")
    parser.add_argument("--out", default="")
    args = parser.parse_args()
    result = readiness(args.video)
    if args.out:
        output = Path(args.out)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    else:
        default = Path(args.video).expanduser() / "01_roteiro" / "READINESS.json"
        default.parent.mkdir(parents=True, exist_ok=True)
        default.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "READY" else 1


if __name__ == "__main__":
    sys.exit(main())
