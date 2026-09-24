import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

STOP = {
    "a", "as", "ao", "aos", "à", "às", "de", "do", "da", "dos", "das", "e", "em", "no", "na", "nos", "nas",
    "para", "por", "que", "com", "um", "uma", "uns", "umas", "the", "of", "and", "to", "in", "on", "for", "a", "an",
}

def normalize(value):
    text = unicodedata.normalize("NFKD", str(value or "")).encode("ascii", "ignore").decode("ascii").lower()
    return " ".join(re.findall(r"[a-z0-9]+", text))

def words(value):
    return [word for word in normalize(value).split() if word not in STOP]

def ngrams(tokens, size=3):
    if not tokens:
        return set()
    size = min(size, len(tokens))
    return {tuple(tokens[index:index + size]) for index in range(len(tokens) - size + 1)}

def similarity(left, right):
    if not left or not right:
        return 0.0
    return len(left & right) / len(left | right)

def title_formula(title):
    value = normalize(title)
    tags = []
    if re.search(r"\b\d+\b", value):
        tags.append("numero")
    if value.endswith("?") or re.match(r"^(por que|porque|como|qual|quais|why|how|what)\b", value):
        tags.append("pergunta")
    if re.search(r"\b(how|como|passo a passo|tutorial|guia)\b", value):
        tags.append("processo")
    if re.search(r"\b(vs|versus|comparacao|comparação|diferenca|diferença)\b", value):
        tags.append("comparacao")
    if re.search(r"\b(antes|depois|transformacao|transformação|mudou|mudanca|mudança)\b", value):
        tags.append("transformacao")
    if re.search(r"\b(segredo|verdade|revelado|ninguem|impossivel|impossível|proibido)\b", value):
        tags.append("curiosidade")
    return tags

def extract_titles(path, include_alternatives=True):
    path = Path(path).expanduser()
    if not path.exists():
        return []
    values = []
    if path.suffix.lower() == ".json":
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return []
        if isinstance(data, dict):
            selected = data.get("selected_title")
            if selected and "[preencher" not in str(selected).lower():
                values.append(str(selected))
            for item in data.get("candidates", []):
                if isinstance(item, dict) and item.get("title") and "[preencher" not in str(item["title"]).lower():
                    values.append(str(item["title"]))
                elif isinstance(item, str) and "[preencher" not in item.lower():
                    values.append(item)
        return values
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith("|"):
            continue
        if not include_alternatives and re.match(r"^ALT\b", line, re.IGNORECASE):
            continue
        match = re.match(r"^(?:TITLE(?: \d+)?|ALT(?: \d+)?|TITULO(?: \d+)?|TÍTULO(?: \d+)?)\s*:\s*(.+)$", line, re.IGNORECASE)
        if match:
            value = match.group(1).strip()
        elif line.startswith("- ") or line.startswith("* ") or len(words(line)) < 2:
            continue
        else:
            value = line
        if value and "[preencher" not in value.lower() and value not in values:
            values.append(value)
    return values

def history_sort_key(path):
    match = re.search(r"(?:video|ep|episode)[ _-]?(\d+)", str(path).lower())
    return (int(match.group(1)) if match else -1, str(path).lower())


def load_history(value, limit=3, exclude=None):
    if not value:
        return []
    root = Path(value).expanduser()
    if not root.exists():
        return []
    paths = [root] if root.is_file() else sorted(
        [path for path in root.rglob("*") if path.is_file() and path.name in {
            "youtube_package.txt", "youtube_package.md", "PACOTE_PUBLICACAO.txt", "TITLE_RESEARCH.json"
        }],
        key=history_sort_key,
    )
    titles = []
    excluded = Path(exclude).expanduser().resolve() if exclude else None
    for path in paths:
        if excluded:
            try:
                path.resolve().relative_to(excluded)
                continue
            except ValueError:
                pass
        for title in extract_titles(path, include_alternatives=False):
            if title not in titles:
                titles.append(title)
    return titles[-limit:] if limit > 0 else titles

def analyze_title(title, history, threshold):
    current_words = words(title)
    current_grams = ngrams(current_words)
    comparisons = []
    for prior in history:
        prior_words = words(prior)
        prior_grams = ngrams(prior_words)
        shared = sorted(set(current_words) & set(prior_words))
        comparisons.append({
            "title": prior,
            "similarity": round(similarity(current_grams, prior_grams), 4),
            "token_similarity": round(similarity(set(current_words), set(prior_words)), 4),
            "shared_words": shared,
        })
    comparisons.sort(key=lambda item: item["similarity"], reverse=True)
    maximum = comparisons[0]["similarity"] if comparisons else 0.0
    return {
        "title": title,
        "characters": len(title),
        "words": len(current_words),
        "has_number": bool(re.search(r"\d", title)),
        "has_question": "?" in title,
        "formulas": title_formula(title),
        "history_similarity": maximum,
        "history_matches": comparisons[:3],
        "status": "FAIL" if maximum >= 1.0 else "REVIEW" if maximum >= threshold else "PASS",
    }

def audit(candidates, history, threshold=0.72):
    normalized = {}
    for title in candidates:
        key = normalize(title)
        if key:
            normalized.setdefault(key, title)
    unique = list(normalized.values())
    analyses = [analyze_title(title, history, threshold) for title in unique]
    statuses = [item["status"] for item in analyses]
    status = "INCONCLUSIVO" if not unique else "FAIL" if "FAIL" in statuses else "REVIEW" if "REVIEW" in statuses else "PASS"
    return {
        "status": status,
        "confidence": "heuristic",
        "candidate_count": len(unique),
        "history_count": len(history),
        "history": history,
        "candidates": analyses,
        "demand_evidence": "not_inferred",
        "notes": [
            "Heuristics compare title structure and historical overlap only.",
            "Demand, saturation and availability require dated YouTube/Data API evidence.",
        ],
    }

def markdown(result):
    lines = [
        "# Pesquisa de títulos",
        "",
        f"Status: {result['status']}",
        f"Confiança: {result['confidence']}",
        f"Demanda: {result['demand_evidence']}",
        "",
        "## Candidatos",
        "| Título | Fórmula | Histórico | Status |",
        "|---|---|---:|---|",
    ]
    for item in result["candidates"]:
        lines.append(f"| {item['title']} | {', '.join(item['formulas']) or '—'} | {item['history_similarity']:.2f} | {item['status']} |")
    lines.extend(["", "## Histórico consultado", ""])
    for title in result["history"] or ["Nenhum título anterior encontrado."]:
        lines.append(f"- {title}")
    lines.extend([
        "",
        "## Evidência obrigatória antes da escolha",
        "",
        "- Preencher tema, subtema, ângulo e idioma em `TITLE_RESEARCH.md`.",
        "- Registrar URLs, datas, busca, autocomplete, concorrência e espaço disponível.",
        "- Não converter contagem de resultados ou heurística em promessa de demanda.",
        "- A escolha final do título é humana e fica em `youtube_package.txt`.",
    ])
    return "\n".join(lines) + "\n"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidates", required=True)
    parser.add_argument("--history")
    parser.add_argument("--current")
    parser.add_argument("--limit", type=int, default=3)
    parser.add_argument("--threshold", type=float, default=0.72)
    parser.add_argument("--out")
    parser.add_argument("--markdown")
    args = parser.parse_args()
    candidates = extract_titles(args.candidates)
    history = load_history(args.history, args.limit, args.current)
    result = audit(candidates, history, args.threshold)
    if args.out:
        output = Path(args.out).expanduser()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.markdown:
        output = Path(args.markdown).expanduser()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(markdown(result), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["status"] == "FAIL" else 0

if __name__ == "__main__":
    sys.exit(main())
