#!/usr/bin/env python3
"""packaging_audit.py — gate 10/10 de PROCESSO do par titulo+thumb+hook (qualquer nicho, PT+EN).

Nao preve CTR. So audita estrutura, pareamento e completude:
- 3..5 pares, winner humano valido, 1..2 alternativos para Test & Compare;
- titulo PT/EN 10..100 chars (REVIEW se >60, FAIL se >100 ou <10);
- thumb text <=4 palavras por idioma e SEM repetir palavras do titulo (FAIL);
- formula Y1..Y11 + goal browse|search;
- hook long30s presente e short3s <=8 palavras (FAIL);
- evidencia: >=1 URL por par (FAIL se vazio).

Uso:
  python scripts/packaging_audit.py --packaging <video>/01_roteiro/PACKAGING.json [--out ...]
Sai com codigo 1 se FAIL.
"""
import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

FORMULAS = {"Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y11"}
GOALS = {"browse", "search"}


def normalize(value):
    text = unicodedata.normalize("NFKD", str(value or "")).encode("ascii", "ignore").decode("ascii").lower()
    return " ".join(re.findall(r"[a-z0-9]+", text))


def words(value):
    return [w for w in normalize(value).split() if w]


def audit_pair(pair):
    errors = []
    warnings = []
    pid = pair.get("id", "?")

    formula = pair.get("formula")
    if formula not in FORMULAS:
        errors.append(f"{pid}:formula_invalida({formula})")
    goal = pair.get("goal")
    if goal not in GOALS:
        errors.append(f"{pid}:goal_invalido({goal})")

    title = pair.get("title", {})
    for lang in ("pt", "en"):
        text = title.get(lang, "")
        size = len(text)
        if size < 10 or size > 100:
            errors.append(f"{pid}:title_{lang}_chars({size})")
        elif size > 60:
            warnings.append(f"{pid}:title_{lang}_acima_60({size})")
        if not re.search(r"\d", text or ""):
            warnings.append(f"{pid}:title_{lang}_sem_numero")

    thumb = pair.get("thumb", {})
    for lang, key in (("pt", "text_pt"), ("en", "text_en")):
        overlay = thumb.get(key, "")
        count = len(words(overlay))
        if count == 0:
            warnings.append(f"{pid}:thumb_{key}_vazio")
        elif count > 4:
            errors.append(f"{pid}:thumb_{key}_palavras({count}>4)")
        title_words = set(words(title.get(lang, "")))
        overlap = sorted(title_words & set(words(overlay)))
        if overlap:
            errors.append(f"{pid}:thumb_repete_titulo_{lang}({','.join(overlap)})")

    for field in ("concept", "focal", "background", "composition"):
        if not str(thumb.get(field, "")).strip():
            errors.append(f"{pid}:thumb_{field}_ausente")

    hook = pair.get("hook", {})
    if not str(hook.get("long30s", "")).strip():
        errors.append(f"{pid}:hook_long30s_ausente")
    short = str(hook.get("short3s", ""))
    if not short.strip():
        errors.append(f"{pid}:hook_short3s_ausente")
    elif len(words(short)) > 8:
        errors.append(f"{pid}:hook_short3s_longo({len(words(short))}>8)")

    evidence = pair.get("evidence", {})
    urls = evidence.get("urls", [])
    if not urls:
        errors.append(f"{pid}:evidencia_sem_url")

    return errors, warnings


def audit(data):
    errors = []
    warnings = []
    pairs = data.get("pairs", []) if isinstance(data, dict) else []
    if not isinstance(pairs, list) or not 3 <= len(pairs) <= 5:
        errors.append(f"pares_invalido({len(pairs) if isinstance(pairs, list) else 'nao-lista'};esperado_3_a_5)")
    for pair in pairs if isinstance(pairs, list) else []:
        entry_errors, entry_warnings = audit_pair(pair if isinstance(pair, dict) else {})
        errors.extend(entry_errors)
        warnings.extend(entry_warnings)

    decision = data.get("decision", {}) if isinstance(data, dict) else {}
    winner = decision.get("winner_id")
    ids = [p.get("id") for p in pairs if isinstance(p, dict)]
    if winner not in ids:
        errors.append(f"winner_invalido({winner})")
    alternatives = decision.get("alternatives", [])
    if not isinstance(alternatives, list) or not 1 <= len(alternatives) <= 2:
        errors.append(f"alternativas_invalidas({alternatives};esperado_1_a_2_para_Test_Compare)")
    elif winner in alternatives:
        errors.append("winner_nas_alternativas")
    if not str(decision.get("human", "")).strip():
        errors.append("decisao_sem_humano")
    if not str(decision.get("date", "")).strip():
        warnings.append("decisao_sem_data")

    if errors:
        status = "FAIL"
    elif warnings:
        status = "REVIEW"
    else:
        status = "PASS"
    return {"status": status, "confidence": "heuristic", "pair_count": len(pairs) if isinstance(pairs, list) else 0,
            "errors": errors, "warnings": warnings,
            "notes": ["Process gate only; does not predict CTR.",
                      "Title+thumb must not share words in either language."]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--packaging", required=True)
    parser.add_argument("--out")
    args = parser.parse_args()
    try:
        data = json.loads(Path(args.packaging).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        result = {"status": "FAIL", "confidence": "heuristic", "pair_count": 0,
                  "errors": [f"packaging_ilegivel:{exc}"], "warnings": []}
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1
    result = audit(data)
    if args.out:
        output = Path(args.out)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["status"] == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main())
