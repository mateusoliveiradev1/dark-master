#!/usr/bin/env python3
"""yt_scan_outliers.py — acha OUTLIERS (video >= N x a mediana do canal) e alerta.

Uso:
  python scripts/yt_scan_outliers.py --mine                       # seu canal (cold-file-diaries)
  python scripts/yt_scan_outliers.py --handle @AlgumCanal
  python scripts/yt_scan_outliers.py --channels monitor/channels.json --ratio 3
  python scripts/yt_scan_outliers.py --watch                      # roda a lista monitor/channels.json

O que faz:
  - pega os ultimos videos de cada canal (Data API v3)
  - calcula a mediana de views e marca outliers (views >= ratio x mediana)
  - grava em data/dark.db (tabela outliers) e imprime um relatorio

Pre-requisito: python scripts/yt_auth.py  (escopo youtube.readonly)
"""
import argparse
import json
import statistics
import sys
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
TOKEN = Path.home() / ".config" / "opencode" / "secrets" / "yt-token.json"
WATCHLIST = ROOT / "monitor" / "channels.json"


def creds():
    from googleapiclient.discovery import build
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    if not TOKEN.exists():
        print("[!] Rode antes: python scripts/yt_auth.py")
        sys.exit(2)
    c = Credentials.from_authorized_user_file(str(TOKEN), [
        "https://www.googleapis.com/auth/youtube.readonly"])
    if not c.valid and c.expired and c.refresh_token:
        c.refresh(Request())
        TOKEN.write_text(c.to_json(), encoding="utf-8")
    return build("youtube", "v3", credentials=c)


def resolve_uploads(yt, handle=None, channel_id=None, mine=False):
    if mine:
        r = yt.channels().list(part="contentDetails", mine=True).execute()
        return r["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"], "MINE"
    if channel_id:
        r = yt.channels().list(part="contentDetails,snippet", id=channel_id).execute()
    else:
        r = yt.channels().list(part="contentDetails,snippet", forHandle=handle).execute()
    if not r.get("items"):
        return None, None
    it = r["items"][0]
    return it["contentDetails"]["relatedPlaylists"]["uploads"], it["snippet"]["title"]


def recent_views(yt, uploads, n=30):
    r = yt.playlistItems().list(part="contentDetails", playlistId=uploads, maxResults=n).execute()
    vids = [i["contentDetails"]["videoId"] for i in r.get("items", [])]
    if not vids:
        return []
    out = []
    for i in range(0, len(vids), 50):
        chunk = vids[i:i + 50]
        v = yt.videos().list(part="statistics,snippet", id=",".join(chunk)).execute()
        for it in v.get("items", []):
            out.append({
                "video_id": it["id"],
                "title": it["snippet"]["title"],
                "published": it["snippet"]["publishedAt"][:10],
                "views": int(it["statistics"].get("viewCount", 0)),
            })
    return out


def scan(yt, uploads, label, ratio):
    vids = recent_views(yt, uploads)
    if not vids:
        return []
    med = statistics.median([v["views"] for v in vids]) or 1
    hits = []
    for v in vids:
        r = v["views"] / med
        if r >= ratio:
            hits.append({**v, "median": med, "ratio": round(r, 2)})
    hits.sort(key=lambda x: -x["ratio"])
    print(f"\n=== {label} | mediana {med:.0f} views | {len(vids)} videos | {len(hits)} outlier(s) ===")
    for h in hits:
        print(f"  {h['ratio']}x  {h['views']:>7} views  [{h['published']}]  {h['title'][:70]}")
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mine", action="store_true")
    ap.add_argument("--handle")
    ap.add_argument("--channels")
    ap.add_argument("--ratio", type=float, default=3.0)
    ap.add_argument("--watch", action="store_true")
    a = ap.parse_args()

    yt = creds()
    all_hits = []
    if a.watch or a.channels:
        path = Path(a.channels) if a.channels else WATCHLIST
        data = json.loads(path.read_text(encoding="utf-8"))
        for ch in data.get("channels", []):
            up, label = resolve_uploads(yt, handle=ch.get("handle"), channel_id=ch.get("id"))
            if up:
                all_hits += scan(yt, up, label or ch.get("name", "?"), a.ratio)
    else:
        up, label = resolve_uploads(yt, handle=a.handle, mine=a.mine)
        if up:
            all_hits = scan(yt, up, label or "canal", a.ratio)

    # grava no banco (Neon Postgres se DATABASE_URL, senao SQLite)
    if all_hits:
        sys.path.insert(0, str(HERE))
        import yt_db
        ts = datetime.now().isoformat(timespec="seconds")
        for h in all_hits:
            yt_db.save_outlier({
                "detected_ts": ts, "channel": a.handle or "watchlist",
                "video_id": h["video_id"], "title": h["title"], "format": "",
                "views": h["views"], "channel_median": h["median"], "ratio": h["ratio"],
                "pattern": "", "note": "auto",
            })
        print(f"\n[OK] {len(all_hits)} outlier(s) gravados no banco ({yt_db.backend()})")

    print("\n[!] ALERTA: revise os outliers acima — o padrao (hook/tema/formato/thumb) vira sugestao de conteudo.")


if __name__ == "__main__":
    main()
