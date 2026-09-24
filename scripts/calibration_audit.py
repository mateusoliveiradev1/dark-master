#!/usr/bin/env python3
import argparse
import csv
import json
import statistics
import sys
from pathlib import Path


def number(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def median(values):
    clean = [value for value in values if value is not None]
    return round(statistics.median(clean), 2) if clean else None


def load_rows(path, channel, video_tag):
    try:
        with Path(path).open(encoding="utf-8-sig", newline="") as handle:
            return [row for row in csv.DictReader(handle)
                    if row.get("channel") == channel and row.get("video_tag") == video_tag]
    except (OSError, csv.Error):
        return []


def audit(metrics_path, scorecard_path, channel, video_tag):
    try:
        scorecard = json.loads(Path(scorecard_path).read_text(encoding="utf-8"))
    except (OSError, ValueError, AttributeError):
        return {"status": "INCONCLUSIVO", "reason": "scorecard_missing", "proposals": []}
    rows = load_rows(metrics_path, channel, video_tag)
    if not rows:
        return {"status": "INCONCLUSIVO", "reason": "metrics_missing", "proposals": []}
    current = rows[-1]
    video_format = current.get("format", "")
    same_format = [row for row in rows if row.get("format") == video_format]
    if len(same_format) < 2:
        return {"status": "INCONCLUSIVO", "reason": "baseline_insufficient", "proposals": []}
    baseline = {
        metric: median([number(row.get(metric)) for row in same_format])
        for metric in ("views", "avd_seconds", "avp_percent", "subscribers_gained")
    }
    score = number(scorecard.get("score"))
    avp = number(current.get("avp_percent"))
    avd = number(current.get("avd_seconds"))
    views = number(current.get("views"))
    above = lambda value, base: value is not None and base is not None and value >= base
    performance = sum([
        int(above(views, baseline["views"])),
        int(above(avd, baseline["avd_seconds"])),
        int(above(avp, baseline["avp_percent"])),
    ])
    if score is None:
        result = "INCONCLUSIVO"
        proposals = [{"area": "scorecard", "proposal": "gerar scorecard antes de calibrar"}]
    elif score >= 85 and performance >= 2:
        result = "PASS"
        proposals = []
    elif score < 85 and performance >= 2:
        result = "REVIEW"
        proposals = [{"area": "scorecard", "proposal": "score baixo apesar de performance acima da baseline; revisar dimensões do scorecard"}]
    elif score >= 85 and performance <= 1:
        result = "REVIEW"
        proposals = [{"area": "calibracao", "proposal": "score alto com performance abaixo da baseline; revisar pesos e dados, não baixar regra automaticamente"}]
    else:
        result = "REVIEW"
        proposals = [{"area": "calibracao", "proposal": "coletar mais amostras D+2/D+7 antes de ajustar thresholds"}]
    return {
        "status": result,
        "channel": channel,
        "video_tag": video_tag,
        "format": video_format,
        "score": score,
        "performance_signals": performance,
        "baseline": baseline,
        "current": current,
        "proposals": proposals,
        "propose_only": True,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--metrics", default="data/metrics.csv")
    parser.add_argument("--scorecard", required=True)
    parser.add_argument("--channel", required=True)
    parser.add_argument("--video-tag", required=True)
    parser.add_argument("--out")
    args = parser.parse_args()
    result = audit(args.metrics, args.scorecard, args.channel, args.video_tag)
    if args.out:
        output = Path(args.out)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(result, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2, default=str))
    return 0 if result.get("status") in {"PASS", "REVIEW"} else 1


if __name__ == "__main__":
    sys.exit(main())
