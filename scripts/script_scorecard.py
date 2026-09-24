#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


def load_json(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError, AttributeError):
        return None


def read_text(path):
    try:
        return Path(path).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def status(path):
    data = load_json(path)
    return data.get("status", "MISSING") if isinstance(data, dict) else "MISSING"


def score_facts(claims, source_text, map_data, timeline_text):
    points = 0
    details = []
    claim_items = claims if isinstance(claims, list) else []
    if claim_items:
        points += 10
        details.append("claims_present")
    sourced = [item for item in claim_items if item.get("source_ids")]
    if claim_items and len(sourced) == len(claim_items):
        points += 8
        details.append("claims_sourced")
    if len(source_text.strip()) > 120:
        points += 4
        details.append("source_ledger_present")
    blocks = map_data.get("blocks", []) if isinstance(map_data, dict) else []
    mapped = sum(1 for block in blocks if block.get("claim_ids"))
    if blocks and mapped == len(blocks):
        points += 3
        details.append("blocks_mapped")
    if len(timeline_text.splitlines()) >= 8:
        points += 3
        details.append("timeline_present")
    return min(25, points), details


def score_structure(map_data, target_rehooks=3):
    blocks = map_data.get("blocks", []) if isinstance(map_data, dict) else []
    if not blocks:
        return 0, ["map_missing"]
    complete = sum(
        1 for block in blocks
        if block.get("text") and block.get("question") and block.get("state_change")
    )
    points = int(20 * complete / len(blocks))
    rehooks = sum(1 for block in blocks if block.get("rehook"))
    if rehooks >= target_rehooks:
        points += 0
    else:
        points = max(0, points - (target_rehooks - rehooks) * 2)
    if any(block.get("payoff") for block in reversed(blocks)):
        points += 0
    else:
        points = max(0, points - 4)
    return min(20, points), ["blocks_complete", f"rehooks:{rehooks}", "payoff_final"]


def score_retention(map_data, timing_status):
    points = 8 if timing_status == "PASS" else 0
    blocks = map_data.get("blocks", []) if isinstance(map_data, dict) else []
    rehooks = sum(1 for block in blocks if block.get("rehook"))
    points += min(7, rehooks)
    return min(15, points), [f"rehooks:{rehooks}", f"timing:{timing_status}"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, help="pasta videoNN ou 01_roteiro")
    parser.add_argument("--lane", choices=["long", "mixed"], default="mixed")
    parser.add_argument("--out")
    args = parser.parse_args()
    root = Path(args.root).expanduser()
    script_dir = root if root.name == "01_roteiro" else root / "01_roteiro"
    claims = load_json(script_dir / "CLAIMS.json")
    claim_items = claims.get("claims", []) if isinstance(claims, dict) else []
    map_data = load_json(script_dir / "ROTEIRO_MAP.json") or {}
    source_text = read_text(script_dir / "PESQUISA_FONTE.md")
    timeline_text = read_text(script_dir / "LINHA_DO_TEMPO.md")
    timing = status(script_dir / "TIMING_AUDIT.json")
    originality = status(script_dir / "ORIGINALITY_AUDIT.json")
    rotation = status(script_dir / "ROTATION_AUDIT.json")
    compliance = status(script_dir / "COMPLIANCE_AUDIT.json")
    short_qa = status(script_dir / "SHORT_QA.json")
    short_plan = (script_dir / "SHORT_FUNNEL.md").exists()
    facts, fact_details = score_facts(claim_items, source_text, map_data, timeline_text)
    rehooks = max(3, int(4000 / 700)) if args.lane == "mixed" else 3
    structure, structure_details = score_structure(map_data, rehooks)
    retention, retention_details = score_retention(map_data, timing)
    originality_points = {"PASS": 10, "REVIEW": 6, "MISSING": 0}.get(originality, 0)
    compliance_points = {"PASS": 10, "REVIEW": 5, "MISSING": 0}.get(compliance, 0)
    production_points = (6 if timing == "PASS" else 0) + (4 if short_qa in {"PASS", "REVIEW"} else 0)
    funnel_points = 0
    if args.lane == "mixed":
        funnel_points = 8 if short_qa == "PASS" else 4 if short_qa == "REVIEW" else 0
        if short_plan:
            funnel_points = min(10, funnel_points + 2)
    maximum = 90 if args.lane == "long" else 100
    total = facts + structure + retention + originality_points + compliance_points + production_points + funnel_points
    if args.lane == "long":
        production_points = min(10, production_points + 4)
        total = facts + structure + retention + originality_points + compliance_points + production_points
    threshold = 80 if args.lane == "long" else 85
    status_value = "PASS" if total >= threshold else "REVIEW" if total >= 70 else "FAIL"
    result = {
        "status": status_value,
        "score": total,
        "maximum": maximum,
        "threshold": threshold,
        "human_review_required": originality == "REVIEW" or rotation == "REVIEW" or compliance == "REVIEW" or short_qa == "REVIEW",
        "dimensions": {
            "facts": {"points": facts, "max": 25, "details": fact_details},
            "structure": {"points": structure, "max": 20, "details": structure_details},
            "retention_design": {"points": retention, "max": 15, "details": retention_details},
            "originality": {"points": originality_points, "max": 10, "details": [originality]},
            "compliance": {"points": compliance_points, "max": 10, "details": [compliance]},
            "production": {"points": production_points, "max": 10, "details": [timing, short_qa]},
            "funnel": {"points": funnel_points, "max": 10 if args.lane == "mixed" else 0, "details": [short_qa, short_plan]},
        },
    }
    if args.out:
        output = Path(args.out)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] in {"PASS", "REVIEW"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
