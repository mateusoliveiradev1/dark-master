#!/usr/bin/env python3
"""inauthentic_audit.py — os 3 baldes nao-monetizaveis do YouTube (Help 16/07/2026).

Por video, com historico do canal:
  1. template/generico — swap-test: 5-gram max vs narracoes anteriores
     (mesmo motor do originality_audit) + hook (100 chars) + sequencia de beats;
  2. pesquisa primaria — PESQUISA_FONTE com fonte primaria OU claim com
     primary_source; senao REVIEW;
  3. persona IA em tema sensivel — topico (saude/financas/direito/politica) +
     voz sintetica (voice_contract engine) sem arquivo de disclosure;
     senao REVIEW para decisao humana.

Uso:
  python scripts/inauthentic_audit.py <videoNN> [--previous <pasta-do-canal>] [--out ...]
Sai com codigo 1 se FAIL. INCONCLUSIVO (sem historico) nao bloqueia o 1o video.
"""
import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from originality_audit import ngrams, previous_files, similarity

SENSITIVE_TOPICS = {
    "saude": [r"\bdoen[cç]a\b", r"\bsintoma\b", r"\btratamento\b", r"\brem[eé]dio\b", r"\bdisease\b", r"\bsymptom\b"],
    "financas": [r"\binvestimento\b", r"\bjuros\b", r"\bacoes\b", r"\bcarteira\b", r"\binvestment\b", r"\bstocks?\b"],
    "direito": [r"\bprocesso\b", r"\badvogado\b", r"\bsenten[cç]a\b", r"\blawsuit\b", r"\battorney\b"],
    "politica": [r"\belei[cç][aã]o\b", r"\bgoverno\b", r"\bpresidente\b", r"\belection\b", r"\bgovernment\b"],
}
THRESHOLD, REVIEW_FACTOR = 0.45, 0.65


def normalize(value):
    text = unicodedata.normalize("NFKD", str(value or "")).encode("ascii", "ignore").decode("ascii").lower()
    return " ".join(re.findall(r"[a-z0-9]+", text))


def hook_signature(narration_path):
    try:
        text = Path(narration_path).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip() and not p.strip().startswith("#")]
    return normalize((paras[0] if paras else "")[:300])


def beats_signature(map_path):
    try:
        data = json.loads(Path(map_path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return []
    return [str(b.get("beat", "")) for b in data.get("blocks", []) if isinstance(b, dict)]


def beat_similarity(left, right):
    if not left or not right:
        return 0.0
    matches = sum(1 for a, b in zip(left, right) if a == b)
    return round(matches / max(len(left), len(right)), 4)


def voice_is_synthetic(video_dir):
    contract = video_dir / "02_audio" / "voice_contract.json"
    try:
        engine = str(json.loads(contract.read_text(encoding="utf-8")).get("engine", "")).lower()
    except (OSError, ValueError):
        return None
    return engine not in {"human", "humana", "studio"}


def disclosure_present(video_dir):
    for name in ("DISCLOSURE_IA.txt", "DISCLOSURE_AI.txt"):
        if (video_dir / name).exists() or (video_dir / "01_roteiro" / name).exists():
            return True
    return False


def primary_research_present(script_dir):
    try:
        claims = json.loads((script_dir / "CLAIMS.json").read_text(encoding="utf-8")).get("claims", [])
    except (OSError, ValueError):
        claims = []
    if any(isinstance(c, dict) and c.get("primary_source") for c in claims):
        return True
    try:
        source_text = (script_dir / "PESQUISA_FONTE.md").read_text(encoding="utf-8", errors="replace").lower()
    except OSError:
        return False
    return "primaria" in source_text or "primary" in source_text or "independente" in source_text


def audit(video, previous=None):
    video_dir = Path(video).expanduser()
    script_dir = video_dir / "01_roteiro"
    narration = script_dir / "narration_v3.txt"
    errors, review = [], []
    if not narration.exists():
        return {"status": "FAIL", "errors": ["narration_missing"], "review": []}
    current_text = narration.read_text(encoding="utf-8", errors="replace")
    current_grams = ngrams(current_text)
    current_hook = hook_signature(narration)
    current_beats = beats_signature(script_dir / "ROTEIRO_MAP.json")
    comparisons = []
    if previous:
        for path in previous_files(previous, narration.resolve() if hasattr(narration, "resolve") else narration):
            try:
                prior_text = path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            score = similarity(current_grams, ngrams(prior_text))
            hook_score = similarity(set(current_hook.split()), set(hook_signature(path).split()))
            comparisons.append({"file": str(path), "similarity": round(score, 4), "hook_similarity": round(hook_score, 4)})
    comparisons.sort(key=lambda item: item["similarity"], reverse=True)
    maximum = comparisons[0]["similarity"] if comparisons else 0.0
    hook_max = max([item["hook_similarity"] for item in comparisons], default=0.0)
    if comparisons:
        if maximum >= THRESHOLD:
            errors.append(f"swap_test_template({maximum}>=0.45)")
        elif maximum >= THRESHOLD * REVIEW_FACTOR:
            review.append(f"swap_test_review({maximum})")
        if hook_max >= 0.8:
            errors.append(f"hook_intercambiavel({hook_max})")
    else:
        review.append("sem_historico_primeiro_video")
    if previous:
        root = Path(previous).expanduser()
        beat_scores = []
        maps = sorted(root.glob("video*/01_roteiro/ROTEIRO_MAP.json")) + sorted(root.glob("ep*/01_roteiro/ROTEIRO_MAP.json"))
        for other in maps[-3:]:
            if other.resolve() == (script_dir / "ROTEIRO_MAP.json").resolve():
                continue
            beat_scores.append(beat_similarity(current_beats, beats_signature(other)))
        if beat_scores and max(beat_scores) >= 1.0 and maximum >= THRESHOLD * REVIEW_FACTOR:
            errors.append("estrutura_identica_3_ultimos")
    if not primary_research_present(script_dir):
        review.append("sem_pesquisa_primaria")
    low = current_text.lower()
    topics = sorted(topic for topic, patterns in SENSITIVE_TOPICS.items()
                    if any(re.search(p, low) for p in patterns))
    if topics:
        synthetic = voice_is_synthetic(video_dir)
        if synthetic and not disclosure_present(video_dir):
            review.append(f"persona_ia_tema_sensivel({','.join(topics)}):exigir_disclosure_ou_voz_humana")
        elif synthetic is None:
            review.append(f"tema_sensivel({','.join(topics)}):confirmar_voz_e_disclosure")
    status = "FAIL" if errors else ("REVIEW" if review else "PASS")
    if not comparisons and not errors:
        status = "REVIEW" if review else "PASS"
    return {"status": status, "confidence": "heuristic",
            "max_similarity": maximum, "hook_max": hook_max,
            "comparisons": comparisons[:10], "sensitive_topics": topics,
            "errors": errors, "review": sorted(set(review)),
            "notes": ["Enforcement e no canal; este gate e por video com historico.",
                      "Troque o roteiro A pelo B: se fizer sentido, e template."]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("video")
    parser.add_argument("--previous", default="")
    parser.add_argument("--out", default="")
    args = parser.parse_args()
    result = audit(args.video, args.previous or None)
    if args.out:
        output = Path(args.out)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["status"] == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main())
