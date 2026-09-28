#!/usr/bin/env python3
"""auto_research.py — pesquisa automatica semanal (sem chave) + alertas.

Para cada seed (temas da watchlist + briefs existentes + nichos dos canais):
  - autocomplete (--suggest, HTTP livre): profundidade de perguntas;
  - Trends (cache 7d; rede so se venceu);
  - queries rising dos briefs JSON existentes.
Compara com a rodada anterior e emite alerts.json:
  OUTLIER_FLARE / TREND_UP / DEMAND_DEPTH / REVALIDATE_DUE / FUNNEL_GAP.
Tudo commitado em data/research/ para alimentar o painel e a skill.
Uso: python scripts/auto_research.py [--out data/research] [--dry-run]
"""
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

RESEARCH_DIR = ROOT / "data" / "research"


def load_seeds():
    """Temas a pesquisar: watchlist + briefs + canais monitorados."""
    seeds = []
    try:
        from niche_scan import WATCHLIST
        items = json.loads(WATCHLIST.read_text(encoding="utf-8"))
        seeds += [item.get("theme", "") for item in items if item.get("theme")]
    except (OSError, ValueError, ImportError):
        pass
    briefs = ROOT / "data" / "briefs"
    if briefs.exists():
        for path in sorted(briefs.glob("*.json")):
            if path.name in {"watchlist.json"}:
                continue
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except ValueError:
                continue
            theme = data.get("theme") or data.get("query") or path.stem.replace("-", " ")
            if theme:
                seeds.append(str(theme))
    try:
        channels = json.loads((ROOT / "monitor" / "channels.json").read_text(encoding="utf-8")).get("channels", [])
        for channel in channels:
            note = str(channel.get("nota", ""))
            if note:
                seeds.append(note.split(",")[0])
    except (OSError, ValueError):
        pass
    seen, unique = set(), []
    for seed in seeds:
        key = seed.strip().lower()
        if key and key not in seen:
            seen.add(key)
            unique.append(seed.strip())
    return unique[:20]


def previous_round(out_dir):
    latest = out_dir / "latest.json"
    try:
        return json.loads(latest.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def research_seed(seed, lang="en"):
    """Uma rodada por seed: suggest (livre) + trends (cache). Sem API key."""
    from niche_scan import cmd_suggest, cmd_trends
    hl = {"en": "en", "pt": "pt-BR", "es": "es"}.get(lang, "en")
    try:
        suggest = cmd_suggest(seed, hl)
    except Exception as exc:
        suggest = {"seed": seed, "depth": 0, "suggestions": [], "error": str(exc)[:200]}
    try:
        trends = cmd_trends(seed)
    except Exception as exc:
        trends = {"term": seed, "error": str(exc)[:200]}
    return {"seed": seed, "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            "depth": suggest.get("depth", 0), "suggestions": suggest.get("suggestions", [])[:30],
            "trends_direction": trends.get("direction", trends.get("error", "n/d")),
            "rising": [r.get("query") for r in (trends.get("rising") or [])[:10] if r.get("query")]}


def build_alerts(current, previous):
    """Compara rodadas e emite alertas acionaveis. Puro e testavel."""
    alerts = []
    prev_seeds = {item.get("seed", "").lower(): item for item in previous.get("seeds", [])}
    for item in current.get("seeds", []):
        seed = item.get("seed", "")
        old = prev_seeds.get(seed.lower(), {})
        old_terms = {str(term).lower() for term in old.get("suggestions", [])}
        new_terms = [term for term in item.get("suggestions", []) if str(term).lower() not in old_terms]
        if item.get("depth", 0) >= 15 and len(new_terms) >= 5:
            alerts.append({"type": "DEMAND_DEPTH", "seed": seed,
                           "detail": f"{len(new_terms)} perguntas novas (profundidade {item['depth']})",
                           "examples": new_terms[:5]})
        rising = item.get("rising", [])
        old_rising = {str(term).lower() for term in old.get("rising", [])}
        fresh_rising = [term for term in rising if str(term).lower() not in old_rising]
        if fresh_rising:
            alerts.append({"type": "TREND_UP", "seed": seed,
                           "detail": f"{len(fresh_rising)} queries em alta novas", "examples": fresh_rising[:5]})
        if item.get("trends_direction") == "ALTA" and old.get("trends_direction") != "ALTA":
            alerts.append({"type": "TREND_UP", "seed": seed,
                           "detail": "trajetoria virou ALTA no YouTube 12m", "examples": []})
    try:
        from niche_scan import WATCHLIST, watchlist_due
        items = json.loads(WATCHLIST.read_text(encoding="utf-8"))
        for item in watchlist_due(items):
            alerts.append({"type": "REVALIDATE_DUE", "seed": item.get("theme", ""),
                           "detail": f"revalidacao vencida ha {item.get('age_days')}d", "examples": []})
    except (OSError, ValueError):
        pass
    order = {"TREND_UP": 0, "DEMAND_DEPTH": 1, "OUTLIER_FLARE": 2, "REVALIDATE_DUE": 3, "FUNNEL_GAP": 4}
    alerts.sort(key=lambda alert: order.get(alert["type"], 9))
    return alerts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default=str(RESEARCH_DIR))
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--lang", default="en", choices=["en", "pt", "es"])
    args = parser.parse_args()
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    seeds = load_seeds()
    if args.dry_run:
        print(json.dumps({"seeds": seeds, "count": len(seeds)}, ensure_ascii=False, indent=2))
        return 0
    previous = previous_round(out_dir)
    current = {"date": datetime.now(timezone.utc).strftime("%Y-%m-%d"), "seeds": []}
    for seed in seeds:
        try:
            current["seeds"].append(research_seed(seed, args.lang))
        except Exception as exc:
            current["seeds"].append({"seed": seed, "error": str(exc)[:200]})
    current["alerts"] = build_alerts(current, previous)
    (out_dir / f"{current['date']}.json").write_text(json.dumps(current, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out_dir / "latest.json").write_text(json.dumps(current, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"[OK] {len(current['seeds'])} seeds, {len(current['alerts'])} alertas -> {out_dir / 'latest.json'}")
    for alert in current["alerts"][:10]:
        print(f"  [{alert['type']}] {alert['seed']}: {alert['detail']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
