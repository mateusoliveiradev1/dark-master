#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path

META = [
    r"\besse canal\b", r"\bneste canal\b", r"\bthis channel\b", r"\bnesse v[íi]deo\b", r"\bin this video\b",
    r"\bassista o short\b", r"\bdeixe o like\b", r"\binscreva-se agora\b",
]
GORE = [
    r"\bsangue\b", r"\bgore\b", r"\bcorpo mutilado\b", r"\bdesmembers?\b", r"\bmutilad[oa]s?\b",
]
RISK = [
    r"\bfoi culpad[oa]\b", r"\bcometeu o crime\b", r"\bmatou\b", r"\bassassinou\b",
    r"\bviolou\b", r"\bcorrompeu\b", r"\bconfessou\b",
]
HEDGE = [r"\bsuspeit[oa]s?\b", r"\bacusad[oa]s?\b", r"\balegad[oa]s?\b", r"\bcondenad[oa]s?\b", r"\binculpad[oa]s?\b"]


def words(text):
    return len(re.findall(r"\w+", text or "", flags=re.UNICODE))


def audit(narration, claims=None):
    if not Path(narration).exists():
        return {"status": "FAIL", "errors": ["narration_missing"]}
    text = Path(narration).read_text(encoding="utf-8", errors="replace")
    low = text.lower()
    errors = []
    reviews = []
    for pattern in META:
        if re.search(pattern, low):
            errors.append("meta_language")
    for pattern in GORE:
        if re.search(pattern, low):
            reviews.append("graphic_detail")
    for pattern in RISK:
        if re.search(pattern, low):
            reviews.append("legal_status_or_attribution:" + pattern)
    if not any(re.search(pattern, low) for pattern in HEDGE) and re.search(r"\b(suspeito|acusado|investigação|laudo|processo)\b", low):
        reviews.append("living_or_case_status_review")
    claim_status = "not_provided"
    if claims:
        try:
            claim_data = json.loads(Path(claims).read_text(encoding="utf-8"))
            claim_items = claim_data.get("claims", []) if isinstance(claim_data, dict) else []
            claim_status = "present"
            if not claim_items:
                errors.append("claims_empty")
            for claim in claim_items:
                if not isinstance(claim, dict) or not claim.get("id") or not claim.get("text"):
                    errors.append("claim_incomplete")
        except (OSError, ValueError, AttributeError):
            errors.append("claims_invalid")
    status = "FAIL" if errors else "REVIEW" if reviews else "PASS"
    return {
        "status": status,
        "words": words(text),
        "claims": claim_status,
        "errors": sorted(set(errors)),
        "review": sorted(set(reviews)),
        "human_review_required": bool(reviews),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--narration", required=True)
    parser.add_argument("--claims")
    parser.add_argument("--out")
    args = parser.parse_args()
    result = audit(args.narration, args.claims)
    if args.out:
        output = Path(args.out)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("status") in {"PASS", "REVIEW"} else 1


if __name__ == "__main__":
    sys.exit(main())
