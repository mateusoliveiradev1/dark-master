#!/usr/bin/env python3
"""ypp_check.py — matematica do YPP 2026/2027 a partir de numeros declarados.

Nao consulta API: recebe inscritos/horas/views (do Studio) e responde onde o
canal esta, o que falta e em que ritmo. Limiares [OFICIAL] (blog YouTube
10/08/2026 + Help): ate 31/01/2027 vale 4.000h/10M; de 01/02/2027, novos
precisam 8.000h/20M. Manutencao minima [PRATICANTE relatando OFICIAL].

Uso:
  python scripts/ypp_check.py --subs 800 --hours 2500 [--short-views 2000000]
      [--longs-90d 6 --shorts-90d 10] [--horizon 300]
"""
import argparse
import json
import sys
from datetime import datetime, timezone

REGIMES = {
    "2026": {"subs": 1000, "hours": 4000, "shorts": 10_000_000, "label": "ate 31/01/2027"},
    "2027": {"subs": 1000, "hours": 8000, "shorts": 20_000_000, "label": "de 01/02/2027 (novos)"},
}
MAINTENANCE = {"hours_365d": 1000, "shorts_90d": 1_000_000, "longs_90d": 2, "shorts_posts_90d": 5}


def check(subs, hours, short_views, longs_90d, shorts_90d, horizon):
    regimes = {}
    for name, limits in REGIMES.items():
        hours_gap = max(0, limits["hours"] - hours)
        shorts_gap = max(0, limits["shorts"] - short_views)
        long_ok = subs >= limits["subs"] and hours_gap == 0
        short_ok = subs >= limits["subs"] and shorts_gap == 0
        regimes[name] = {
            "eligible_long": long_ok, "eligible_shorts": short_ok,
            "subs_gap": max(0, limits["subs"] - subs),
            "hours_gap": hours_gap, "shorts_gap": shorts_gap,
            "daily_watch_hours_needed": round(hours_gap / horizon, 2) if hours_gap else 0.0,
            "daily_shorts_needed": round(shorts_gap / 90, 1) if shorts_gap else 0.0,
        }
    maintenance = {
        "hours_ok": hours >= MAINTENANCE["hours_365d"],
        "shorts_ok": short_views >= MAINTENANCE["shorts_90d"],
        "activity_ok": longs_90d >= MAINTENANCE["longs_90d"] or shorts_90d >= MAINTENANCE["shorts_posts_90d"],
    }
    maintenance["safe"] = maintenance["hours_ok"] or maintenance["shorts_ok"] or maintenance["activity_ok"]
    return {"status": "DIAGNOSTIC", "confidence": "official-thresholds",
            "as_of": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            "regimes": regimes, "maintenance": maintenance,
            "notes": ["Shorts nao contam para as 4.000/8.000h; so videos publicos contam.",
                      "Vale engaged views, nao view bruta; janela rolante expira.",
                      "~22h/dia de watch acumulado na janela miram 8.000h em 365d."]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--subs", type=int, required=True)
    parser.add_argument("--hours", type=float, required=True)
    parser.add_argument("--short-views", type=int, default=0)
    parser.add_argument("--longs-90d", type=int, default=0)
    parser.add_argument("--shorts-90d", type=int, default=0)
    parser.add_argument("--horizon", type=int, default=300, help="dias de planejamento p/ ritmo")
    parser.add_argument("--out", default="")
    args = parser.parse_args()
    result = check(args.subs, args.hours, args.short_views, args.longs_90d, args.shorts_90d, args.horizon)
    if args.out:
        Path_out = __import__("pathlib").Path(args.out)
        Path_out.parent.mkdir(parents=True, exist_ok=True)
        Path_out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
