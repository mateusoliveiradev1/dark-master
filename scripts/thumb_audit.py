#!/usr/bin/env python3
"""thumb_audit.py — gate visual do par titulo+thumb (qualquer nicho).

Audita THUMB_BRIEF.json (+ imagem opcional):
- 2..3 conceitos, cada um com os 6 campos (angle, focal, text_pt/text_en+posicao,
  background, composition, note_120px) e 1 eixo variante entre conceitos;
- overlay <=4 palavras por idioma e SEM repetir o titulo (FAIL);
- imagem (quando informada): existe, <=2MB, 1280x720 recomendado;
- downscale 120px: se PIL disponivel, verifica legibilidade minima
  (nao-solida); sem PIL/file = REVIEW, nunca PASS silencioso;
- gore/policy: sinaliza termos graficos como REVIEW (humano decide, ver ref 09).

Uso:
  python scripts/thumb_audit.py --brief <video>/01_roteiro/THUMB_BRIEF.json [--titles "Titulo PT | Title EN"] [--out ...]
Sai com codigo 1 se FAIL.
"""
import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

REQUIRED_FIELDS = ("angle", "focal", "text_pt", "text_en", "position", "background", "composition", "note_120px")
GORE_HINTS = ("sangue", "blood", "gore", "corpo", "cadaver", "corpse", "ferimento", "wound", "decapitat")


def normalize(value):
    text = unicodedata.normalize("NFKD", str(value or "")).encode("ascii", "ignore").decode("ascii").lower()
    return " ".join(re.findall(r"[a-z0-9]+", text))


def words(value):
    return [w for w in normalize(value).split() if w]


def parse_titles(raw):
    if not raw:
        return []
    return [part.strip() for part in re.split(r"\|", raw) if part.strip()]


def audit_brief(data, titles):
    errors = []
    warnings = []
    concepts = data.get("concepts", []) if isinstance(data, dict) else []
    if not isinstance(concepts, list) or not 2 <= len(concepts) <= 3:
        errors.append(f"conceitos_invalidos({len(concepts) if isinstance(concepts, list) else 'nao-lista'};esperado_2_a_3)")
        concepts = concepts if isinstance(concepts, list) else []
    title_words = set()
    for title in titles:
        title_words |= set(words(title))
    axes = set()
    for index, concept in enumerate(concepts):
        label = concept.get("id", f"C{index + 1}") if isinstance(concept, dict) else f"C{index + 1}"
        if not isinstance(concept, dict):
            errors.append(f"{label}:conceito_ilegivel")
            continue
        for field in REQUIRED_FIELDS:
            if not str(concept.get(field, "")).strip():
                errors.append(f"{label}:{field}_ausente")
        axis = str(concept.get("variant_axis", "")).strip().lower()
        if axis:
            axes.add(axis)
        for lang, key in (("pt", "text_pt"), ("en", "text_en")):
            overlay = str(concept.get(key, ""))
            count = len(words(overlay))
            if count == 0:
                warnings.append(f"{label}:{key}_vazio")
            elif count > 4:
                errors.append(f"{label}:{key}_palavras({count}>4)")
            overlap = sorted(title_words & set(words(overlay)))
            if overlap and title_words:
                errors.append(f"{label}:repete_titulo_{lang}({','.join(overlap)})")
        blob = normalize(" ".join(str(concept.get(k, "")) for k in ("angle", "focal", "background", "composition", "note_120px")))
        if any(hint in blob for hint in GORE_HINTS):
            warnings.append(f"{label}:possivel_gore_policy_REVIEW_humano")
    if concepts and not axes:
        warnings.append("variant_axis_ausente (A/B ilegivel: varie 1 eixo por vez)")
    return errors, warnings


def audit_image(image_ref, root):
    errors = []
    warnings = []
    checks = {}
    if not image_ref:
        return {"status": "REVIEW", "checks": {"image": "nao_informada"}}, errors, warnings
    path = (root / str(image_ref)).resolve() if not Path(str(image_ref)).is_absolute() else Path(str(image_ref))
    if not path.exists():
        errors.append(f"imagem_ausente({image_ref})")
        return {"status": "FAIL", "checks": {"image": "ausente"}}, errors, warnings
    size = path.stat().st_size
    checks["bytes"] = size
    if size > 2 * 1024 * 1024:
        errors.append(f"imagem_acima_2MB({size})")
    try:
        from PIL import Image
    except ImportError:
        warnings.append("PIL_ausente_120px_nao_verificado")
        return {"status": "REVIEW", "checks": checks}, errors, warnings
    try:
        with Image.open(path) as image:
            checks["size"] = list(image.size)
            if tuple(image.size) != (1280, 720):
                warnings.append(f"imagem_fora_1280x720({image.size})")
            small = image.convert("L").resize((120, 68))
            pixels = list(small.getdata())
            spread = max(pixels) - min(pixels)
            checks["spread_120px"] = spread
            if spread < 12:
                errors.append(f"imagem_quase_solida_120px(spread={spread})")
    except Exception as exc:
        errors.append(f"imagem_ilegivel:{exc}")
    return {"status": "FAIL" if errors else ("REVIEW" if warnings else "PASS"), "checks": checks}, errors, warnings


def audit(data, titles, root):
    errors, warnings = audit_brief(data, titles)
    image_result, image_errors, image_warnings = audit_image(
        (data.get("image") if isinstance(data, dict) else None), root)
    errors.extend(image_errors)
    warnings.extend(image_warnings)
    if errors or image_result.get("status") == "FAIL":
        status = "FAIL"
    elif warnings or image_result.get("status") == "REVIEW":
        status = "REVIEW"
    else:
        status = "PASS"
    return {"status": status, "confidence": "heuristic",
            "concept_count": len(data.get("concepts", [])) if isinstance(data, dict) else 0,
            "image": image_result, "errors": errors, "warnings": warnings,
            "notes": ["Thumbnail must read at 120px next to real competitors.",
                      "Overlay never repeats title words. Gore flags need human review (ref 09)."]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--brief", required=True)
    parser.add_argument("--titles", default="")
    parser.add_argument("--root", default="")
    parser.add_argument("--out")
    args = parser.parse_args()
    brief_path = Path(args.brief)
    try:
        data = json.loads(brief_path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        result = {"status": "FAIL", "confidence": "heuristic", "concept_count": 0,
                  "errors": [f"brief_ilegivel:{exc}"], "warnings": []}
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1
    root = Path(args.root) if args.root else brief_path.parent
    result = audit(data, parse_titles(args.titles), root)
    if args.out:
        output = Path(args.out)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["status"] == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main())
