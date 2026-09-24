#!/usr/bin/env python3
"""yt_metrics.py — coleta métricas próprias, metadados, tráfego e retenção."""
import argparse
import csv
import difflib
import json
import re
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SECRETS = Path.home() / ".config" / "opencode" / "secrets"
TOKEN = SECRETS / "yt-token.json"
CSV_PATH = ROOT / "data" / "metrics.csv"

SCOPES = [
    "https://www.googleapis.com/auth/youtube.readonly",
    "https://www.googleapis.com/auth/yt-analytics.readonly",
]

METRICS = ",".join([
    "views",
    "engagedViews",
    "estimatedMinutesWatched",
    "averageViewDuration",
    "averageViewPercentage",
    "likes",
    "comments",
    "shares",
    "subscribersGained",
    "subscribersLost",
    "dislikes",
])

CSV_COLUMNS = [
    "channel", "snapshot_date", "video_id", "video_tag", "case_name", "series",
    "scheduled_date", "match_status", "title", "format", "published", "views",
    "engaged_views", "engagement_rate_percent", "duration_seconds", "avd_seconds",
    "avp_percent", "ctr_percent", "impressions", "shown_in_feed",
    "chose_to_view_percent", "likes", "comments", "shares", "subscribers_gained",
    "subscribers_lost", "dislikes", "watch_hours", "revenue_usd", "traffic_source", "notes",
]


def creds():
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    if not TOKEN.exists():
        print("[!] Token não encontrado. Rode antes: python scripts/yt_auth.py")
        sys.exit(2)
    credentials = Credentials.from_authorized_user_file(str(TOKEN), SCOPES)
    if not credentials.valid and credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())
        TOKEN.write_text(credentials.to_json(), encoding="utf-8")
    return credentials


def parse_duration(value):
    match = re.match(r"^P(?:(\d+)D)?T(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?$", value or "")
    if not match:
        return None
    days, hours, minutes, seconds = [int(part or 0) for part in match.groups()]
    return days * 86400 + hours * 3600 + minutes * 60 + seconds


def normalize_title(value):
    value = (value or "").lower().replace("&", " and ")
    value = re.sub(r"#shorts\b", "", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def case_tokens(value):
    ignored = {"the", "case", "murder", "murders", "of"}
    return [token for token in normalize_title(value).split() if len(token) > 2 and token not in ignored]


def title_similarity(left, right):
    return difflib.SequenceMatcher(None, normalize_title(left), normalize_title(right)).ratio()


def infer_format(content_type, duration_seconds, avd_seconds=None, avp_percent=None):
    if content_type == "SHORTS":
        return "short"
    if content_type in {"VIDEO_ON_DEMAND", "LIVE_STREAM", "STORY"}:
        return "long"
    if duration_seconds is not None:
        return "short" if duration_seconds <= 180 else "long"
    avd = number_or_none(avd_seconds)
    avp = number_or_none(avp_percent)
    if avd is not None and avp is not None and avd > 0 and 0 < avp <= 100:
        inferred_duration = avd * 100 / avp
        return "short" if inferred_duration <= 180 else "long"
    if avd is not None and avp is not None and avd < 70 and avp > 100:
        return "short"
    if avd is not None and avd >= 70:
        return "long"
    return "unknown"


def number_or_none(value):
    try:
        return float(value) if value not in (None, "") else None
    except (TypeError, ValueError):
        return None


def load_csv_index():
    if not CSV_PATH.exists():
        return {}
    with CSV_PATH.open(encoding="utf-8-sig", newline="") as handle:
        return {row["video_id"]: row for row in csv.DictReader(handle) if row.get("video_id")}


def load_db_index(channel):
    sys.path.insert(0, str(HERE))
    import yt_db
    yt_db.init(quiet=True)
    c = yt_db.conn()
    videos = yt_db._rows(c, "SELECT * FROM videos WHERE channel=?", (channel,))
    all_snapshots = yt_db._rows(c, "SELECT * FROM snapshots WHERE channel=? ORDER BY ts", (channel,))
    snapshots = []
    history = {}
    for row in all_snapshots:
        if row["ts"] == max(item["ts"] for item in all_snapshots if item["video_id"] == row["video_id"]):
            snapshots.append(row)
        current = history.setdefault(row["video_id"], {})
        for key in ("title", "format", "published", "duration_seconds", "subscribers_gained", "subscribers_lost"):
            if row.get(key) not in (None, "") and key not in current:
                current[key] = row[key]
    c.close()
    return {row["video_id"]: row for row in videos}, {row["video_id"]: row for row in snapshots}, history


def calendar_context(project):
    sys.path.insert(0, str(HERE))
    import channel_scan
    root = channel_scan.find_project_root(project)
    calendar_path = channel_scan.find_calendar(root)
    calendar = channel_scan.parse_calendar(calendar_path)
    videos = []
    for row in calendar:
        state = channel_scan.strict_state(root / row["video_tag"])
        videos.append({**state, **row})
    return root, calendar_path, videos


def match_video(video_id, title, content_type, published_at, local_videos, registered, avd_seconds=None, avp_percent=None):
    cached = registered.get(video_id, {})
    if cached.get("video_tag") and cached.get("match_status") == "matched" and cached.get("case_name"):
        return {**cached, "match_status": "matched", "match_confidence": float(cached.get("match_confidence") or 1)}
    fmt = infer_format(content_type, None, avd_seconds, avp_percent)
    candidates = []
    for local in local_videos:
        expected_title = local["short_title"] if fmt == "short" else local["long_title"]
        if not expected_title:
            expected_title = local["long_title"]
        wanted_tokens = case_tokens(local["case_name"])
        published_title = normalize_title(title)
        case_score = 1.0 if wanted_tokens and " ".join(wanted_tokens[:2]) in published_title else 0.0
        similarity = title_similarity(title, expected_title)
        score = similarity * 0.75 + case_score * 0.25
        if fmt != "unknown" and local.get("expected_format") and local["expected_format"] != fmt:
            continue
        candidates.append((score, local, similarity))
    candidates.sort(key=lambda item: item[0], reverse=True)
    if not candidates or not title:
        return {
            "channel": cached.get("channel"), "video_id": video_id, "title": title,
            "format": fmt or cached.get("format", "unknown"), "case_name": "",
            "series": "", "scheduled_date": "", "published_at": published_at or "",
            "duration_seconds": cached.get("duration_seconds"), "match_status": "unmatched",
            "match_confidence": 0,
        }
    best_score, best, best_similarity = candidates[0]
    runner_similarity = candidates[1][2] if len(candidates) > 1 else 0
    confidence = round(best_score, 3)
    status = "matched" if best_similarity >= 0.9 and best_similarity - runner_similarity >= 0.05 else "ambiguous"
    candidate_tags = [item[1]["video_tag"] for item in candidates[:3]]
    return {
        "channel": cached.get("channel"), "video_id": video_id, "title": title,
        "video_tag": best["video_tag"] if status == "matched" else "",
        "format": fmt, "case_name": best["case_name"] if status == "matched" else "",
        "series": best["series"] if status == "matched" else "",
        "scheduled_date": best["date"] if status == "matched" else "",
        "published_at": published_at or "", "duration_seconds": cached.get("duration_seconds"),
        "match_status": status, "match_confidence": confidence, "candidate_tags": candidate_tags,
    }


def fetch_metadata(youtube, video_ids, fallback):
    metadata = {}
    if not video_ids:
        return metadata
    try:
        for index in range(0, len(video_ids), 50):
            chunk = video_ids[index:index + 50]
            response = youtube.videos().list(part="snippet,contentDetails,status", id=",".join(chunk)).execute()
            for item in response.get("items", []):
                metadata[item["id"]] = {
                    "title": item.get("snippet", {}).get("title", ""),
                    "published_at": item.get("snippet", {}).get("publishedAt", ""),
                    "published": item.get("snippet", {}).get("publishedAt", "")[:10],
                    "duration_seconds": parse_duration(item.get("contentDetails", {}).get("duration", "")),
                    "privacy_status": item.get("status", {}).get("privacyStatus", ""),
                }
    except Exception as exc:
        print(f"[i] Data API indisponível: {exc}")
    for video_id in video_ids:
        if video_id not in metadata:
            old = fallback.get(video_id, {})
            metadata[video_id] = {
                "title": old.get("title", ""),
                "published_at": old.get("published") or old.get("published_at", ""),
                "published": old.get("published", ""),
                "duration_seconds": int(old.get("duration_seconds") or 0) or None,
                "privacy_status": old.get("privacy_status", ""),
            }
    return metadata


def collect_video_rows(analytics, start_date, end_date):
    response = analytics.reports().query(
        ids="channel==MINE", startDate=start_date, endDate=end_date,
        metrics=METRICS, dimensions="video", sort="-views", maxResults=200,
    ).execute()
    headers = [header["name"] for header in response.get("columnHeaders", [])]
    return [dict(zip(headers, raw)) for raw in response.get("rows", [])]


def collect_traffic(analytics, captured_ts, channel, start_date, end_date, video_ids, write):
    sys.path.insert(0, str(HERE))
    import yt_db
    rows = []
    for video_id in video_ids:
        try:
            response = analytics.reports().query(
                ids="channel==MINE", startDate=start_date, endDate=end_date,
                metrics="views,engagedViews,estimatedMinutesWatched",
                dimensions="insightTrafficSourceType", filters=f"video=={video_id}",
                sort="-views", maxResults=200,
            ).execute()
            headers = [header["name"] for header in response.get("columnHeaders", [])]
            aggregate = [dict(zip(headers, raw)) for raw in response.get("rows", [])]
        except Exception as exc:
            print(f"[i] traffic source indisponível para {video_id}: {exc}")
            continue
        detailed = []
        try:
            detail = analytics.reports().query(
                ids="channel==MINE", startDate=start_date, endDate=end_date,
                metrics="views,engagedViews,estimatedMinutesWatched",
                dimensions="insightTrafficSourceDetail",
                filters=f"video=={video_id};insightTrafficSourceType==RELATED_VIDEO",
                sort="-views", maxResults=25,
            ).execute()
            detail_headers = [header["name"] for header in detail.get("columnHeaders", [])]
            detailed = [dict(zip(detail_headers, raw)) for raw in detail.get("rows", [])]
        except Exception as exc:
            print(f"[i] RELATED_VIDEO detalhado indisponível para {video_id}: {exc}")
        has_related = any(row.get("insightTrafficSourceType") == "RELATED_VIDEO" for row in aggregate)
        for row in aggregate:
            if row.get("insightTrafficSourceType") == "RELATED_VIDEO" and detailed and has_related:
                continue
            rows.append({"video": video_id, **row})
        for row in detailed:
            rows.append({
                "video": video_id, "insightTrafficSourceType": "RELATED_VIDEO",
                "insightTrafficSourceDetail": row.get("insightTrafficSourceDetail", "") or "", **row,
            })
    count = 0
    for row in rows:
        record = {
            "captured_ts": captured_ts, "channel": channel, "video_id": row.get("video", ""),
            "source_type": row.get("insightTrafficSourceType", ""),
            "source_detail": row.get("insightTrafficSourceDetail", "") or "",
            "views": row.get("views"), "engaged_views": row.get("engagedViews"),
            "watch_hours": round((row.get("estimatedMinutesWatched") or 0) / 60, 4),
            "period_start": start_date, "period_end": end_date,
        }
        if write:
            yt_db.save_traffic_source(record)
        count += 1
    return count


def collect_retention(analytics, captured_ts, channel, start_date, end_date, video_ids, write):
    sys.path.insert(0, str(HERE))
    import yt_db
    count = 0
    for video_id in video_ids:
        try:
            response = analytics.reports().query(
                ids="channel==MINE", startDate=start_date, endDate=end_date,
                metrics="audienceWatchRatio,relativeRetentionPerformance",
                dimensions="elapsedVideoTimeRatio", filters=f"video=={video_id};audienceType==ORGANIC",
                sort="-audienceWatchRatio", maxResults=100,
            ).execute()
        except Exception as exc:
            print(f"[i] retenção indisponível para {video_id}: {exc}")
            continue
        headers = [header["name"] for header in response.get("columnHeaders", [])]
        for raw in response.get("rows", []):
            row = dict(zip(headers, raw))
            record = {
                "captured_ts": captured_ts, "channel": channel, "video_id": video_id,
                "elapsed_ratio": row.get("elapsedVideoTimeRatio"),
                "audience_watch_ratio": row.get("audienceWatchRatio"),
                "relative_retention": row.get("relativeRetentionPerformance"),
                "period_start": start_date, "period_end": end_date,
            }
            if write:
                yt_db.save_retention(record)
            count += 1
    return count


def latest_snapshots(channel):
    sys.path.insert(0, str(HERE))
    import yt_db
    c = yt_db.conn()
    rows = yt_db._rows(c, """SELECT s.* FROM snapshots s
        WHERE s.channel=? AND s.ts=(SELECT MAX(s2.ts) FROM snapshots s2
        WHERE s2.channel=s.channel AND s2.video_id=s.video_id)
        ORDER BY s.video_id""", (channel,))
    mappings = yt_db._rows(c, "SELECT * FROM videos WHERE channel=?", (channel,))
    c.close()
    return {row["video_id"]: row for row in rows}, {row["video_id"]: row for row in mappings}


def write_csv(channel, csv_index, mappings):
    snapshots, latest_mappings = latest_snapshots(channel)
    with CSV_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        for video_id, row in sorted(snapshots.items(), key=lambda item: (item[1].get("views") or 0), reverse=True):
            mapping = {**mappings.get(video_id, {}), **latest_mappings.get(video_id, {})}
            old = csv_index.get(video_id, {})
            views = row.get("views")
            engaged = row.get("engaged_views")
            engagement_rate = round((engaged or 0) / views * 100, 2) if views else None
            record = {
                "channel": channel,
                "snapshot_date": row.get("snapshot_date") or (row.get("ts") or "")[:10],
                "video_id": video_id,
                "video_tag": mapping.get("video_tag", ""),
                "case_name": mapping.get("case_name", ""),
                "series": mapping.get("series", ""),
                "scheduled_date": mapping.get("scheduled_date", ""),
                "match_status": mapping.get("match_status", ""),
                "title": row.get("title") or old.get("title") or mapping.get("title", ""),
                "format": row.get("format") or mapping.get("format") or old.get("format", "unknown"),
                "published": row.get("published") or old.get("published", ""),
                "views": row.get("views"),
                "engaged_views": row.get("engaged_views"),
                "engagement_rate_percent": engagement_rate,
                "duration_seconds": row.get("duration_seconds") or mapping.get("duration_seconds") or old.get("duration_seconds", ""),
                "avd_seconds": row.get("avd_seconds"),
                "avp_percent": row.get("avp_percent"),
                "ctr_percent": row.get("ctr_percent") or old.get("ctr_percent", ""),
                "impressions": row.get("impressions") or old.get("impressions", ""),
                "shown_in_feed": row.get("shown_in_feed") or old.get("shown_in_feed", ""),
                "chose_to_view_percent": row.get("chose_to_view_percent") or old.get("chose_to_view_percent", ""),
                "likes": row.get("likes"), "comments": row.get("comments"), "shares": row.get("shares"),
                "subscribers_gained": row.get("subscribers_gained"),
                "subscribers_lost": row.get("subscribers_lost"),
                "dislikes": row.get("dislikes"), "watch_hours": row.get("watch_hours"),
                "revenue_usd": row.get("revenue_usd") or old.get("revenue_usd", ""),
                "traffic_source": row.get("traffic_source") or old.get("traffic_source", ""),
                "notes": old.get("notes", ""),
            }
            writer.writerow(record)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--days", type=int, default=30)
    parser.add_argument("--channel", default="cold-file-diaries")
    parser.add_argument("--project")
    parser.add_argument("--lag-days", type=int, default=3)
    parser.add_argument("--no-write", action="store_true")
    parser.add_argument("--no-traffic", action="store_true")
    parser.add_argument("--no-retention", action="store_true")
    parser.add_argument("--retention-videos", type=int, default=10)
    args = parser.parse_args()

    from googleapiclient.discovery import build
    credentials = creds()
    analytics = build("youtubeAnalytics", "v2", credentials=credentials)
    try:
        youtube = build("youtube", "v3", credentials=credentials)
    except Exception as exc:
        print(f"[i] YouTube Data API indisponível: {exc}")
        youtube = None

    today = date.today()
    end = today - timedelta(days=args.lag_days)
    start = end - timedelta(days=max(args.days - 1, 0))
    start_date = start.isoformat()
    end_date = end.isoformat()
    captured_ts = datetime.now().isoformat(timespec="seconds")
    rows = collect_video_rows(analytics, start_date, end_date)
    video_ids = [row.get("video", "") for row in rows if row.get("video")]
    csv_index = load_csv_index()
    registered, previous, history = load_db_index(args.channel)
    fallback = {video_id: dict(values) for video_id, values in history.items()}
    for source in (previous, csv_index):
        for video_id, values in source.items():
            fallback.setdefault(video_id, {})
            fallback[video_id].update({key: value for key, value in values.items() if value not in (None, "")})
    metadata = fetch_metadata(youtube, video_ids, fallback) if youtube else {
        video_id: {
            "title": fallback.get(video_id, {}).get("title", ""),
            "published_at": fallback.get(video_id, {}).get("published", ""),
            "published": fallback.get(video_id, {}).get("published", ""),
            "duration_seconds": int(fallback.get(video_id, {}).get("duration_seconds") or 0) or None,
            "privacy_status": "",
        } for video_id in video_ids
    }
    local_videos = []
    project_path = None
    calendar_path = None
    if args.project:
        project_path, calendar_path, local_videos = calendar_context(args.project)

    saved = 0
    matches = defaultdict(list)
    formats = {}
    for row in rows:
        video_id = row.get("video", "")
        info = metadata.get(video_id, {})
        content_type = row.get("creatorContentType")
        duration = info.get("duration_seconds")
        fmt = infer_format(content_type, duration, row.get("averageViewDuration"), row.get("averageViewPercentage"))
        old = fallback.get(video_id, {})
        if fmt == "unknown":
            fmt = old.get("format") or registered.get(video_id, {}).get("format") or "unknown"
        title = info.get("title") or old.get("title") or ""
        published_at = info.get("published_at") or old.get("published") or ""
        mapping = match_video(
            video_id, title, content_type, published_at, local_videos, registered,
            row.get("averageViewDuration"), row.get("averageViewPercentage"),
        )
        formats[video_id] = fmt
        mapping.update({
            "channel": args.channel, "title": title, "format": fmt,
            "published_at": published_at, "duration_seconds": duration,
            "updated_at": captured_ts,
        })
        if mapping.get("match_status") in {"matched", "ambiguous"}:
            matches[mapping["match_status"]].append({"video_id": video_id, "title": title, "candidates": [mapping]})
        record = {
            "ts": captured_ts, "channel": args.channel, "video_id": video_id,
            "title": title, "format": fmt, "published": published_at[:10],
            "views": row.get("views"), "engaged_views": row.get("engagedViews"),
            "avd_seconds": row.get("averageViewDuration"),
            "avp_percent": row.get("averageViewPercentage"),
            "ctr_percent": old.get("ctr_percent") or None,
            "shown_in_feed": old.get("shown_in_feed") or None,
            "chose_to_view_percent": old.get("chose_to_view_percent") or None,
            "likes": row.get("likes"), "comments": row.get("comments"), "shares": row.get("shares"),
            "subscribers_gained": row.get("subscribersGained"),
            "subscribers_lost": row.get("subscribersLost"), "dislikes": row.get("dislikes"),
            "watch_hours": round((row.get("estimatedMinutesWatched") or 0) / 60, 4),
            "revenue_usd": old.get("revenue_usd") or None,
            "impressions": int(old.get("impressions") or 0) or None,
            "duration_seconds": duration, "traffic_source": "api",
            "snapshot_date": captured_ts[:10], "period_start": start_date, "period_end": end_date,
            "match_status": mapping.get("match_status", "unmatched"), "notes": old.get("notes", ""),
        }
        if not args.no_write:
            import yt_db
            yt_db.save_video(mapping)
            yt_db.save_snapshot(record)
            saved += 1

    if not args.no_write:
        write_csv(args.channel, csv_index, registered)

    traffic_count = 0
    retention_count = 0
    if not args.no_traffic:
        traffic_count = collect_traffic(analytics, captured_ts, args.channel, start_date, end_date, video_ids, not args.no_write)
    if not args.no_retention:
        long_ids = []
        for row in rows:
            video_id = row.get("video", "")
            if formats.get(video_id) == "long":
                long_ids.append(video_id)
        retention_count = collect_retention(
            analytics, captured_ts, args.channel, start_date, end_date,
            long_ids[:max(args.retention_videos, 0)], not args.no_write,
        )
    if not args.no_write:
        import yt_db
        yt_db.compact_capture(args.channel, captured_ts, start_date, end_date)

    print(f"[i] {len(rows)} vídeos | {start_date} -> {end_date} | API com defasgem de {args.lag_days}d")
    print(f"[i] mapeamentos: {len(matches['matched'])} confirmados, {len(matches['ambiguous'])} pendentes")
    if matches["ambiguous"]:
        print(json.dumps(matches["ambiguous"], ensure_ascii=False, indent=2))
    if not args.no_write:
        print(f"[OK] {saved} snapshots gravados; {traffic_count} fontes de tráfego; {retention_count} pontos de retenção")
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    sys.exit(main())
