#!/usr/bin/env python3
"""learn_loop.py — orquestra o loop de aprendizado 24h (coleta -> analise -> propostas).

Filosofia propose-only: o loop COLETA dados, ANALISA e PROPOE. Nunca reescreve
regras, thresholds ou contratos sozinho — mudanca de regra exige aprovacao
humana explicita. Sem OAuth/rede, cada etapa degrada para diagnostico.

Etapas e custo aproximado de quota (Data API, 10k un/dia, reseta meia-noite Pacifico):
  collect  ~300 un/canal proprio (yt_metrics: videos + trafego + retencao)
  watch    ~3 un/canal monitorado (yt_scan_outliers --watch: so channels+playlist+videos)
  analyze  0 un (le banco local/CSV)
  revalidate ~150 un/tema vencido (niche_scan --cluster)

Uso local:  python scripts/learn_loop.py --all [--dry-run]
Uso CI:     ver .github/workflows/learn-loop.yml + docs/deploy-24h.md
"""
import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
COST = {"collect_per_channel": 300, "watch_per_channel": 50, "revalidate_per_theme": 150}
QUOTA_DAILY = 10000


def sh(command, timeout=1200):
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=timeout,
                                errors="replace", cwd=str(ROOT))
    except subprocess.TimeoutExpired:
        return 124, "", "timeout"
    return result.returncode, result.stdout[-4000:], result.stderr[-2000:]


def load_channels():
    try:
        data = json.loads((ROOT / "monitor" / "channels.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return []
    return data.get("channels", []) if isinstance(data, dict) else []


def due_themes():
    try:
        sys.path.insert(0, str(HERE))
        from niche_scan import WATCHLIST, watchlist_due
        items = json.loads(WATCHLIST.read_text(encoding="utf-8"))
        return watchlist_due(items)
    except (OSError, ValueError, ImportError):
        return []


def estimate(own_channels, watched_channels, themes, quota_budget):
    total = (len(own_channels) * COST["collect_per_channel"]
             + len(watched_channels) * COST["watch_per_channel"]
             + len(themes) * COST["revalidate_per_theme"])
    plan = {"collect": list(own_channels), "watch": list(watched_channels),
            "revalidate": [item["theme"] for item in themes]}
    if total > quota_budget and plan["revalidate"]:
        dropped = plan["revalidate"]
        plan["revalidate"] = []
        total -= len(dropped) * COST["revalidate_per_theme"]
        plan["skipped_quota"] = dropped
    return total, plan


def run_step(name, command, dry_run):
    if dry_run:
        return {"step": name, "status": "DRY_RUN", "command": " ".join(command)}
    code, out, err = sh(command)
    return {"step": name, "status": "OK" if code == 0 else "FAIL",
            "returncode": code, "stdout": out, "stderr": err}


def loop(channels, themes, steps, dry_run, quota_budget, out_dir, no_dashboard=False):
    own = [c.get("handle", "") for c in channels if c.get("mine") and c.get("handle")]
    watched = [c.get("handle", "") for c in channels if c.get("handle")]
    total, plan = estimate(own, watched, themes, quota_budget)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    report = {"date": today, "quota": {"budget": quota_budget, "daily_limit": QUOTA_DAILY,
                                       "estimated": total, "steps": []}}
    run_all = "all" in steps
    if ("collect" in steps or run_all) and plan["collect"]:
        for handle in plan["collect"]:
            report["quota"]["steps"].append(run_step(
                f"collect:{handle}",
                [sys.executable, str(HERE / "yt_metrics.py"), "--channel", handle, "--days", "30"], dry_run))
    if ("watch" in steps or run_all) and plan["watch"]:
        report["quota"]["steps"].append(run_step(
            "watch", [sys.executable, str(HERE / "yt_scan_outliers.py"), "--watch"], dry_run))
    if ("analyze" in steps or run_all) and plan["collect"]:
        for handle in plan["collect"]:
            report["quota"]["steps"].append(run_step(
                f"analyze:{handle}",
                [sys.executable, str(HERE / "yt_analysis.py"), "--channel", handle, "--today", today], dry_run))
    if ("revalidate" in steps or run_all) and plan["revalidate"]:
        for theme in plan["revalidate"]:
            report["quota"]["steps"].append(run_step(
                f"revalidate:{theme}",
                [sys.executable, str(HERE / "niche_scan.py"), "--cluster", theme], dry_run))
    if plan.get("skipped_quota"):
        report["quota"]["steps"].append({"step": "quota_guard", "status": "SKIPPED",
                                         "detail": plan["skipped_quota"]})
    fails = [step["step"] for step in report["quota"]["steps"] if step["status"] == "FAIL"]
    report["status"] = "OK" if not fails else "DEGRADED"
    report["failed_steps"] = fails
    report["notes"] = ["Loop propose-only: propostas em learnings/outliers; regra so muda com aprovacao humana.",
                       "Sem OAuth/rede, etapas falham como diagnostico — nunca zeros, nunca causalidade inventada."]
    out = Path(out_dir) if out_dir else ROOT / "data" / "learn_loop"
    out.mkdir(parents=True, exist_ok=True)
    (out / f"{today}.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if not dry_run and out == ROOT / "data" / "learn_loop" and not no_dashboard:
        try:
            build_dashboard()
        except Exception as exc:
            report.setdefault("warnings", []).append(f"dashboard:{exc}")
    return report


def channel_details(handle, name):
    """Metricas do Neon por canal: 30d, top videos, serie diaria p/ sparkline.
    Sem captura = status unknown (nunca zero inventado)."""
    try:
        import yt_db
        yt_db.init(quiet=True)
        conn = yt_db.conn()
        rows = yt_db._rows(conn, "SELECT * FROM snapshots WHERE channel=? OR channel=? ORDER BY ts", (handle, name))
        conn.close()
    except Exception:
        return {"status": "unknown"}
    if not rows:
        return {"status": "unknown"}
    latest = {}
    for row in rows:
        latest[row.get("video_id")] = row
    videos = sorted(latest.values(), key=lambda r: float(r.get("views") or 0), reverse=True)
    by_day = {}
    for row in rows:
        day = str(row.get("snapshot_date") or (row.get("ts") or "")[:10])
        try:
            by_day[day] = by_day.get(day, 0) + int(float(row.get("views") or 0))
        except (TypeError, ValueError):
            continue
    series = [{"date": day, "views": by_day[day]} for day in sorted(by_day)[-14:]]
    total_views = sum(int(float(v.get("views") or 0)) for v in videos)
    total_engaged = sum(int(float(v.get("engaged_views") or 0)) for v in videos)
    last_ts = max(str(r.get("ts") or "") for r in rows)
    return {"status": "ok", "videos": len(videos), "views_30d": total_views,
            "engaged_30d": total_engaged,
            "engaged_rate": round(total_engaged / total_views * 100, 1) if total_views else 0.0,
            "top": [{"title": v.get("title"), "views": v.get("views"),
                     "format": v.get("format")} for v in videos[:5]],
            "series": series, "last_capture": last_ts[:10]}


def build_dashboard():
    """Agregado multi-canal para o painel: canais + detalhes Neon + loops + alertas + YPP."""
    try:
        channels = json.loads((ROOT / "monitor" / "channels.json").read_text(encoding="utf-8")).get("channels", [])
    except (OSError, ValueError):
        channels = []
    loop_dir = ROOT / "data" / "learn_loop"
    reports = []
    if loop_dir.exists():
        for path in sorted(loop_dir.glob("????-??-??.json"))[-7:]:
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
                reports.append({"date": data.get("date"), "status": data.get("status"),
                                "failed_steps": data.get("failed_steps", [])})
            except ValueError:
                continue
    alerts = []
    research_dir = ROOT / "data" / "research"
    for latest in sorted(research_dir.glob("latest-*.json")):
        try:
            alerts.extend(json.loads(latest.read_text(encoding="utf-8")).get("alerts", []))
        except (OSError, ValueError):
            continue
    ypp_inputs = {}
    try:
        ypp_inputs = json.loads((ROOT / "data" / "ypp_input.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        pass
    ypp = {}
    if ypp_inputs:
        from ypp_check import check as ypp_check_fn
        for handle, numbers in ypp_inputs.items():
            try:
                result = ypp_check_fn(int(numbers.get("subs", 0)), float(numbers.get("hours", 0)),
                                      int(numbers.get("short_views", 0)), int(numbers.get("longs_90d", 0)),
                                      int(numbers.get("shorts_90d", 0)), 300)
                ypp[handle] = {"eligible_2026": result["regimes"]["2026"]["eligible_long"] or result["regimes"]["2026"]["eligible_shorts"],
                               "eligible_2027": result["regimes"]["2027"]["eligible_long"] or result["regimes"]["2027"]["eligible_shorts"],
                               "hours_gap_2027": result["regimes"]["2027"]["hours_gap"],
                               "daily_needed": result["regimes"]["2027"]["daily_watch_hours_needed"],
                               "maintenance_safe": result["maintenance"]["safe"]}
            except (TypeError, ValueError, KeyError):
                continue
    details = {}
    for channel in channels:
        handle = channel.get("handle", "")
        if handle:
            details[handle] = channel_details(handle, channel.get("name", ""))
    dashboard = {"generated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
                 "channels": [{"handle": c.get("handle"), "name": c.get("name"),
                               "mine": bool(c.get("mine")), "nota": c.get("nota", "")} for c in channels],
                 "details": details,
                 "loop_reports": reports, "alerts": alerts[:20], "ypp": ypp}
    out = ROOT / "data" / "dashboard.json"
    out.write_text(json.dumps(dashboard, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return dashboard


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--collect", action="store_true")
    parser.add_argument("--watch", action="store_true")
    parser.add_argument("--analyze", action="store_true")
    parser.add_argument("--revalidate", action="store_true")
    parser.add_argument("--dashboard", action="store_true", help="so (re)gera data/dashboard.json")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--quota-budget", type=int, default=8000)
    parser.add_argument("--out-dir", default="")
    parser.add_argument("--no-dashboard", action="store_true",
                        help="nao reescreve data/dashboard.json (dono: job de pesquisa)")
    args = parser.parse_args()
    if args.dashboard:
        dashboard = build_dashboard()
        print(json.dumps({"dashboard": "data/dashboard.json", "channels": len(dashboard["channels"]),
                          "alerts": len(dashboard["alerts"])}, ensure_ascii=False, indent=2))
        return 0
    steps = {name for name, on in (("collect", args.collect), ("watch", args.watch),
                                   ("analyze", args.analyze), ("revalidate", args.revalidate)) if on}
    if args.all or not steps:
        steps = {"all"}
    report = loop(load_channels(), due_themes(), steps, args.dry_run, args.quota_budget,
                  args.out_dir or None, args.no_dashboard)
    print(json.dumps({key: value for key, value in report.items() if key != "quota"}, ensure_ascii=False, indent=2))
    print(f"quota estimada: {report['quota']['estimated']}/{report['quota']['budget']} | status: {report['status']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
