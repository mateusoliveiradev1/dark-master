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
            rows = list(csv.DictReader(handle))
    except (OSError, csv.Error):
        return []
    return [row for row in rows if row.get("channel") == channel and row.get("video_tag") == video_tag]


def audit(metrics_path, channel, video_tag):
    rows = load_rows(metrics_path, channel, video_tag)
    if not rows:
        return {"status": "INCONCLUSIVO", "reason": "metrics_missing", "proposals": []}
    formats = sorted({row.get("format") for row in rows if row.get("format")})
    baselines = {}
    for video_format in formats:
        same = [row for row in rows if row.get("format") == video_format]
        if len(same) >= 2:
            baselines[video_format] = {
                metric: median([number(row.get(metric)) for row in same])
                for metric in ("views", "avd_seconds", "avp_percent", "ctr_percent", "subscribers_gained")
            }
    current = rows[-1]
    video_format = current.get("format", "")
    baseline = baselines.get(video_format)
    if not baseline:
        return {"status": "INCONCLUSIVO", "reason": "baseline_insufficient", "proposals": []}
    proposals = []
    current_avp = number(current.get("avp_percent"))
    current_avd = number(current.get("avd_seconds"))
    current_views = number(current.get("views"))
    baseline_avp = baseline.get("avp_percent")
    baseline_avd = baseline.get("avd_seconds")
    baseline_views = baseline.get("views")
    if current_avp is not None and baseline_avp and current_avp < baseline_avp:
        proposals.append({
            "area": "retencao",
            "proposal": "testar rehooks e estados de informação antes de alterar o tema",
            "evidence": {"current_avp": current_avp, "baseline_avp": baseline_avp},
        })
    if current_avd is not None and baseline_avd and current_avd < baseline_avd:
        proposals.append({
            "area": "estrutura",
            "proposal": "revisar blocos longos e antecipar a próxima pergunta",
            "evidence": {"current_avd": current_avd, "baseline_avd": baseline_avd},
        })
    if current_views is not None and baseline_views and current_views < baseline_views:
        proposals.append({
            "area": "acquisition",
            "proposal": "produzir variações de Short com uma claim e bridge diferentes",
            "evidence": {"current_views": current_views, "baseline_views": baseline_views},
        })
    return {
        "status": "PASS" if not proposals else "REVIEW",
        "channel": channel,
        "video_tag": video_tag,
        "format": video_format,
        "current": current,
        "baseline": baseline,
        "proposals": proposals,
        "propose_only": True,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--metrics", default="data/metrics.csv")
    parser.add_argument("--channel", required=True)
    parser.add_argument("--video-tag", required=True)
    parser.add_argument("--out")
    args = parser.parse_args()
    result = audit(args.metrics, args.channel, args.video_tag)
    if args.out:
        output = Path(args.out)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(result, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2, default=str))
    return 0 if result.get("status") in {"PASS", "REVIEW"} else 1


if __name__ == "__main__":
    sys.exit(main())
