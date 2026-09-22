#!/usr/bin/env python3
"""yt_metrics.py — puxa metricas por video (canal proprio) e grava no banco + CSV.

Uso:
  python scripts/yt_metrics.py                 # ultimos 30 dias
  python scripts/yt_metrics.py --days 90
  python scripts/yt_metrics.py --channel cold-file-diaries

Pre-requisito: ter rodado antes `python scripts/yt_auth.py`.

Nota: CTR (impressions click-through) NAO e exposto pela Analytics API v2 —
e dado do Studio. Este script puxa o que a API oferece; CTR continua manual.
"""
import argparse
import csv
import sys
from datetime import date, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SECRETS = Path.home() / ".config" / "opencode" / "secrets"
TOKEN = SECRETS / "yt-token.json"
CSV = ROOT / "data" / "metrics.csv"

SCOPES = ["https://www.googleapis.com/auth/yt-analytics.readonly"]

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
])


def creds():
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    if not TOKEN.exists():
        print("[!] Token nao encontrado. Rode antes: python scripts/yt_auth.py")
        sys.exit(2)
    c = Credentials.from_authorized_user_file(str(TOKEN), SCOPES)
    if not c.valid and c.expired and c.refresh_token:
        c.refresh(Request())
        TOKEN.write_text(c.to_json(), encoding="utf-8")
    return c


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=30)
    ap.add_argument("--channel", default="cold-file-diaries")
    a = ap.parse_args()

    from googleapiclient.discovery import build
    yt = build("youtubeAnalytics", "v2", credentials=creds())

    end = date.today().isoformat()
    start = (date.today() - timedelta(days=a.days)).isoformat()

    resp = yt.reports().query(
        ids="channel==MINE",
        startDate=start,
        endDate=end,
        metrics=METRICS,
        dimensions="video",
        sort="-views",
        maxResults=200,
    ).execute()

    cols = [h["name"] for h in resp.get("columnHeaders", [])]
    rows = resp.get("rows", [])
    print(f"[i] {len(rows)} video(s) | {start} -> {end}")

    # grava no banco (Neon Postgres se DATABASE_URL, senao SQLite)
    sys.path.insert(0, str(HERE))
    import yt_db
    from datetime import datetime
    ts = datetime.now().isoformat(timespec="seconds")

    idx = {name: i for i, name in enumerate(cols)}

    def g(row, name):
        return row[idx[name]] if name in idx else None

    # resolve titulos via Data API (mesmo token, escopo youtube.readonly)
    titles = {}
    try:
        from googleapiclient.discovery import build as _build
        ytdata = _build("youtube", "v3", credentials=creds())
        ids = [row[idx["video"]] for row in rows]
        for i in range(0, len(ids), 50):
            v = ytdata.videos().list(part="snippet,contentDetails", id=",".join(ids[i:i+50])).execute()
            for it in v.get("items", []):
                titles[it["id"]] = it["snippet"]["title"]
    except Exception as e:  # noqa
        print(f"[i] (sem titulos: {e})")

    inserted = 0
    for row in rows:
        vid = row[idx["video"]]
        yt_db.save_snapshot({
            "ts": ts, "channel": a.channel, "video_id": vid,
            "title": titles.get(vid, ""),
            "views": g(row, "views"), "engaged_views": g(row, "engagedViews"),
            "avd_seconds": g(row, "averageViewDuration"),
            "avp_percent": g(row, "averageViewPercentage"),
            "likes": g(row, "likes"), "comments": g(row, "comments"),
            "shares": g(row, "shares"), "subs_gained": g(row, "subscribersGained"),
            "watch_hours": round((g(row, "estimatedMinutesWatched") or 0) / 60.0, 2),
            "traffic_source": "api",
        })
        inserted += 1
    print(f"[OK] {inserted} snapshot(s) gravados no banco ({yt_db.backend()})")

    # regenera o CSV a partir do snapshot mais recente por video (legivel)
    if not CSV.exists():
        CSV.write_text(
            "channel,video_id,title,format,published,views,engaged_views,avd_seconds,"
            "avp_percent,ctr_percent,shown_in_feed,chose_to_view_percent,likes,comments,"
            "shares,subs_gained,watch_hours,revenue_usd,traffic_source,notes\n",
            encoding="utf-8",
        )
    latest = yt_db._rows(yt_db.conn(), """
        SELECT channel, video_id, title, views, engaged_views, avd_seconds, avp_percent,
               likes, comments, shares, subs_gained, watch_hours, traffic_source
        FROM snapshots s
        WHERE ts = (SELECT MAX(ts) FROM snapshots s2 WHERE s2.video_id = s.video_id AND s2.channel = s.channel)
        ORDER BY views DESC NULLS LAST
    """) if yt_db.backend() == "postgres" else yt_db._rows(yt_db.conn(), """
        SELECT channel, video_id, title, views, engaged_views, avd_seconds, avp_percent,
               likes, comments, shares, subs_gained, watch_hours, traffic_source
        FROM snapshots s
        WHERE ts = (SELECT MAX(ts) FROM snapshots s2 WHERE s2.video_id = s.video_id AND s2.channel = s.channel)
        ORDER BY views DESC
    """)
    with CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["channel", "video_id", "title", "format", "published", "views",
                    "engaged_views", "avd_seconds", "avp_percent", "ctr_percent",
                    "shown_in_feed", "chose_to_view_percent", "likes", "comments", "shares",
                    "subs_gained", "watch_hours", "revenue_usd", "traffic_source", "notes"])
        for r in latest:
            fmt = "short" if (r["avd_seconds"] or 0) and (r["avd_seconds"] or 0) < 70 and (r["views"] or 0) > 200 else "long"
            w.writerow([r["channel"], r["video_id"], r["title"], fmt, "", r["views"],
                        r["engaged_views"], r["avd_seconds"], r["avp_percent"], "", "", "",
                        r["likes"], r["comments"], r["shares"], r["subs_gained"],
                        r["watch_hours"], "", r["traffic_source"], ""])
    print(f"[OK] CSV regenerado (ultimo snapshot por video): {CSV}")


if __name__ == "__main__":
    main()
