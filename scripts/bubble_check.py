#!/usr/bin/env python3
"""bubble_check.py — classifica o estagio de distribuicao de um video (D+2/D+7).

Modelo mental das bolhas [PRATICANTE], sem limiar oficial: o YouTube expande
em ondas quando ha resposta e retesta quando ha sinal tardio. Este script nao
preve distribuicao; ele le capturas existentes e diz em que estagio o video
PARECE estar + proxima acao (1 variavel por vez, nunca reup em spam).

Fontes (primeira que existir vence; sem OAuth):
  1. yt_db snapshots do canal (leitura local, sem API);
  2. --csv com snapshot_date,views[,engaged_views,likes,comments] (export Studio);
  3. data/metrics.csv (1 ponto -> estagio single_capture).

Uso:
  python scripts/bubble_check.py --channel <canal> --video <tag|id> [--published AAAA-MM-DD] [--csv exp.csv] [--out BUBBLE_CHECK.json]
"""
import argparse
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


def parse_date(value):
    for pattern in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%d/%m/%Y"):
        try:
            return datetime.strptime(str(value or "")[:10], pattern).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


def load_db_captures(channel, video):
    try:
        import yt_db
    except ImportError:
        return [], "yt_db_indisponivel"
    try:
        yt_db.init(quiet=True)
        conn = yt_db.conn()
        rows = yt_db._rows(conn, "SELECT * FROM snapshots WHERE channel=? ORDER BY ts", (channel,))
        conn.close()
    except Exception as exc:
        return [], f"banco_indisponivel:{exc}"
    captures = []
    for row in rows:
        if str(row.get("video_id", "")) != video and str(row.get("video_tag", "")) != video:
            continue
        date = parse_date(row.get("snapshot_date") or (row.get("ts") or "")[:10])
        try:
            views = int(float(row.get("views") or 0))
        except (TypeError, ValueError):
            continue
        captures.append({"date": date, "views": views,
                         "engaged": row.get("engaged_views"), "likes": row.get("likes")})
    captures.sort(key=lambda item: (item["date"] is None, item["date"]))
    return captures, ""


def load_csv_captures(path):
    captures = []
    try:
        with Path(path).open(encoding="utf-8-sig", newline="") as handle:
            for row in csv.DictReader(handle):
                date = parse_date(row.get("snapshot_date") or row.get("date"))
                try:
                    views = int(float(row.get("views") or 0))
                except (TypeError, ValueError):
                    continue
                captures.append({"date": date, "views": views,
                                 "engaged": row.get("engaged_views"), "likes": row.get("likes")})
    except OSError as exc:
        return [], f"csv_ilegivel:{exc}"
    captures.sort(key=lambda item: (item["date"] is None, item["date"]))
    return captures, ""


def classify(captures, published):
    today = datetime.now(timezone.utc)
    age_days = (today - published).days if published else None
    points = [(item["date"], item["views"]) for item in captures if item["date"] is not None]
    undated = [item["views"] for item in captures if item["date"] is None]
    views = points[-1][1] if points else (undated[-1] if undated else 0)
    if not captures:
        return {"stage": "COLD", "views": 0, "age_days": age_days,
                "next": "pre-bolha: frame1 + hook3s + loop (SHORT_QA PASS) antes de concluir qualquer coisa"}
    if len(captures) == 1:
        hint = "bolha 1 provavel" if age_days is not None and age_days <= 1 else "amostra insuficiente"
        return {"stage": "SEED", "views": views, "age_days": age_days,
                "next": f"{hint}: nao decidir nada antes de 48-72h (lag do Analytics); proxima captura amanha"}
    deltas = [b - a for (_, a), (_, b) in zip(points, points[1:])] if len(points) >= 2 else []
    if not deltas:
        return {"stage": "SEED", "views": views, "age_days": age_days,
                "next": "capturas sem data: exporte o Studio com snapshot_date para serie temporal"}
    if views < 100:
        return {"stage": "SEED", "views": views, "age_days": age_days, "deltas": deltas,
                "next": "amostra pequena (<100 views): sem leitura de tendencia; aguardar"}
    last, previous = deltas[-1], deltas[-2] if len(deltas) >= 2 else None
    flat = [abs(d) <= max(20, views * 0.05) for d in deltas[-3:]]
    if len(deltas) >= 3 and all(flat[-3:-1]) and last > max(50, views * 0.2):
        return {"stage": "LATE_SPIKE", "views": views, "age_days": age_days, "deltas": deltas,
                "next": "reteste tardio: identificar o gatilho (comentario/related) e replicar o eixo, nao reupar"}
    if all(flat):
        return {"stage": "STALLED", "views": views, "age_days": age_days, "deltas": deltas,
                "next": "travou: esperar 7d; depois 1 variavel por vez (frame1 OU hook OU loop); checar demanda nos comentarios"}
    if previous is not None and last > previous and last > 0:
        return {"stage": "EXPANDING", "views": views, "age_days": age_days, "deltas": deltas,
                "next": "expandindo: nao mexer em nada; preparar o proximo do mesmo eixo"}
    if last > 0:
        return {"stage": "COASTING", "views": views, "age_days": age_days, "deltas": deltas,
                "next": "desacelerando com saldo positivo: observar; re-hook/thumb so com 2 capturas frias seguidas"}
    return {"stage": "FADED", "views": views, "age_days": age_days, "deltas": deltas,
            "next": "em queda: post-mortem (frame1? corpo? loop?) e re-otimizar back catalog em vez de insistir"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--channel", required=True)
    parser.add_argument("--video", required=True)
    parser.add_argument("--published", default="")
    parser.add_argument("--csv", default="")
    parser.add_argument("--out", default="")
    args = parser.parse_args()
    captures, error = load_db_captures(args.channel, args.video)
    source = "yt_db"
    if not captures and args.csv:
        captures, error = load_csv_captures(args.csv)
        source = "csv"
    if not captures and not args.csv:
        data_csv = HERE.parent / "data" / "metrics.csv"
        if data_csv.exists():
            with data_csv.open(encoding="utf-8-sig", newline="") as handle:
                for row in csv.DictReader(handle):
                    if row.get("video_id") == args.video or row.get("video_tag") == args.video:
                        try:
                            captures = [{"date": None, "views": int(float(row.get("views") or 0)),
                                         "engaged": row.get("engaged_views"), "likes": row.get("likes")}]
                        except (TypeError, ValueError):
                            pass
                        source = "metrics.csv"
                        break
    result = classify(captures, parse_date(args.published))
    result.update({"channel": args.channel, "video": args.video, "source": source,
                   "captures": len(captures), "confidence": "heuristic",
                   "load_error": error or "",
                   "notes": ["Sem OAuth: shown-in-feed/chose-to-view sao desconhecidos, nunca zero.",
                             "Bolhas sao modelo [PRATICANTE]; este script nao preve distribuicao."]})
    if args.out:
        output = Path(args.out)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(result, ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(main())
