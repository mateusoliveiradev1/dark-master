#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path


def read_json(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError, AttributeError):
        return None


def source_rows(text):
    rows = {}
    headers = []
    for line in (text or "").splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if not headers and cells and cells[0].lower() in {"id", "source_id", "fonte"}:
            headers = [cell.lower() for cell in cells]
            continue
        if headers and cells and re.fullmatch(r"S\d+", cells[0]):
            rows[cells[0]] = {headers[index] if index < len(headers) else f"field_{index}": value for index, value in enumerate(cells)}
    return rows


def audit(root):
    script_dir = Path(root).expanduser()
    if script_dir.name != "01_roteiro":
        script_dir = script_dir / "01_roteiro"
    claims_data = read_json(script_dir / "CLAIMS.json")
    claims = claims_data.get("claims", []) if isinstance(claims_data, dict) else []
    source_text = ""
    try:
        source_text = (script_dir / "PESQUISA_FONTE.md").read_text(encoding="utf-8", errors="replace")
    except OSError:
        pass
    sources = source_rows(source_text)
    errors = []
    review = []
    source_ids = set()
    for index, claim in enumerate(claims, 1):
        if not isinstance(claim, dict):
            errors.append(f"claim_{index}:invalid")
            continue
        claim_id = claim.get("id")
        if not claim_id:
            errors.append(f"claim_{index}:missing_id")
        layer = str(claim.get("layer", "")).upper()
        claim_sources = claim.get("source_ids") or []
        if not isinstance(claim_sources, list) or not claim_sources:
            if layer not in {"LENDA", "HIPOTESE"}:
                errors.append(f"claim_{claim_id or index}:missing_source_ids")
        source_ids.update(str(value) for value in claim_sources)
        if layer in {"FATO", "REPORTADO"}:
            if not str(claim.get("locator", "")).strip():
                review.append(f"claim_{claim_id or index}:locator_missing")
            if not claim.get("primary_source"):
                review.append(f"claim_{claim_id or index}:primary_source_missing")
            if str(claim.get("confidence", "")).upper() not in {"ALTA", "MEDIA", "BAIXA"}:
                review.append(f"claim_{claim_id or index}:confidence_missing")
    for source_id in sorted(source_ids):
        if source_id not in sources:
            errors.append(f"source_missing:{source_id}")
    for source_id, row in sources.items():
        source_value = row.get("fonte") or row.get("source") or row.get("field_3") or ""
        locator = row.get("trecho/localizador") or row.get("localizador") or row.get("field_6") or ""
        if not source_value:
            review.append(f"source_{source_id}:source_missing")
        if not locator:
            review.append(f"source_{source_id}:locator_missing")
        if not row.get("url"):
            review.append(f"source_{source_id}:url_missing")
        if not row.get("depende de") and not row.get("depende_de") and not row.get("field_4"):
            review.append(f"source_{source_id}:independence_unknown")
    timeline = script_dir / "LINHA_DO_TEMPO.md"
    timeline_events = 0
    if timeline.exists():
        timeline_events = len([
            line for line in timeline.read_text(encoding="utf-8", errors="replace").splitlines()
            if line.strip().startswith("|") and "preencher" not in line.lower()
        ])
    if timeline_events < 3:
        review.append("timeline_events_insufficient")
    status = "FAIL" if errors else "REVIEW" if review else "PASS"
    return {
        "status": status,
        "claims": len(claims),
        "sources": len(sources),
        "timeline_events": timeline_events,
        "errors": sorted(set(errors)),
        "review": sorted(set(review)),
        "human_review_required": bool(review),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--out")
    args = parser.parse_args()
    result = audit(args.root)
    if args.out:
        output = Path(args.out)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if args.strict:
        return 0 if result.get("status") == "PASS" else 1
    return 0 if result.get("status") in {"PASS", "REVIEW"} else 1


if __name__ == "__main__":
    sys.exit(main())
