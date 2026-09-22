#!/usr/bin/env python3
"""niche_scan.py — pesquisa de nicho real via YouTube Data API v3.

Uso:
  python scripts/niche_scan.py --query "dark history documentary"
  python scripts/niche_scan.py --channel @FascinatingHorror --ratio 3
  python scripts/niche_scan.py --query "true crime shorts" --ratio 5 --small 200000

O que faz:
  - busca canais/videos recentes do termo (search.list)
  - para cada canal pequeno, calcula os GATES (idade<=45d? soma 5 primeiros? views/dia?)
  - calcula a mediana e marca OUTLIERS (video >= ratio x a mediana do canal)
  - imprime um brief com a evidencia

Requer OAuth (python scripts/yt_auth.py). Consome quota da Data API — use com moderacao.
"""
import argparse
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path

TOKEN = Path.home() / ".config" / "opencode" / "secrets" / "yt-token.json"
SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]


def creds():
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    if not TOKEN.exists():
        print("[!] Rodar: python scripts/yt_auth.py")
        sys.exit(2)
    c = Credentials.from_authorized_user_file(str(TOKEN), SCOPES)
    if not c.valid and c.expired and c.refresh_token:
        c.refresh(Request())
        TOKEN.write_text(c.to_json(), encoding="utf-8")
    return c


def age_days(published):
    d = datetime.fromisoformat(published.replace("Z", "+00:00"))
    return (datetime.now(timezone.utc) - d).days


def channel_info(yt, cid):
    r = yt.channels().list(part="snippet,statistics,contentDetails", id=cid).execute()
    if not r.get("items"):
        return None
    it = r["items"][0]
    return {
        "id": cid,
        "title": it["snippet"]["title"],
        "published": it["snippet"]["publishedAt"],
        "subs": int(it["statistics"].get("subscriberCount", 0) or 0),
        "views": int(it["statistics"].get("viewCount", 0) or 0),
        "videos": int(it["statistics"].get("videoCount", 0) or 0),
        "uploads": it["contentDetails"]["relatedPlaylists"]["uploads"],
    }


def first_n_and_recent(yt, uploads, n=5, recent=15):
    r = yt.playlistItems().list(part="contentDetails", playlistId=uploads, maxResults=recent).execute()
    ids = [i["contentDetails"]["videoId"] for i in r.get("items", [])]
    if not ids:
        return [], []
    v = yt.videos().list(part="statistics,snippet", id=",".join(ids)).execute()
    vids = [{
        "id": it["id"], "title": it["snippet"]["title"],
        "published": it["snippet"]["publishedAt"][:10],
        "views": int(it["statistics"].get("viewCount", 0) or 0),
    } for it in v.get("items", [])]
    # uploads playlist e mais recente -> ultimos = vids[:recent]; primeiros = os mais antigos entre os n
    firsts = vids[-n:] if len(vids) >= n else vids
    return firsts, vids


def scan_channel(yt, info, ratio, small_max):
    firsts, vids = first_n_and_recent(yt, info["uploads"])
    if not vids:
        return None
    age = age_days(info["published"])
    first5 = sum(x["views"] for x in firsts)
    vpd = info["views"] / age if age else info["views"]
    med = statistics.median([x["views"] for x in vids]) or 1
    outs = [v for v in vids if v["views"] / med >= ratio]
    gates = {
        "age<=45": age <= 45,
        "first5>=10k": first5 >= 10000,
        "vpd>=1k": vpd >= 1000,
    }
    return {"info": info, "age": age, "first5": first5, "vpd": round(vpd),
            "median": med, "outliers": outs, "gates": gates, "small": info["subs"] <= small_max}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--query")
    ap.add_argument("--channel")
    ap.add_argument("--ratio", type=float, default=3.0)
    ap.add_argument("--small", type=int, default=200000, help="max subs para considerar 'pequeno'")
    ap.add_argument("--max", type=int, default=8, help="nº de canais a analisar")
    a = ap.parse_args()

    from googleapiclient.discovery import build
    yt = build("youtube", "v3", credentials=creds())

    channels = []
    if a.channel:
        h = a.channel.lstrip("@")
        r = yt.channels().list(part="id", forHandle=h).execute()
        if r.get("items"):
            channels = [r["items"][0]["id"]]
        else:
            print("[!] handle nao encontrado")
    elif a.query:
        r = yt.search().list(part="snippet", q=a.query, type="channel", maxResults=a.max).execute()
        channels = [i["snippet"]["channelId"] for i in r.get("items", [])]
    else:
        print("Use --query ou --channel"); return

    print(f"# Niche scan — {a.query or a.channel}\n")
    passed = []
    for cid in channels:
        info = channel_info(yt, cid)
        if not info:
            continue
        res = scan_channel(yt, info, a.ratio, a.small)
        if not res:
            continue
        g = res["gates"]
        ok = all(g.values())
        tag = "PASSA" if ok else "falha"
        star = " ★" if res["small"] else ""
        print(f"\n{info['title']}{star} — {info['subs']:,} subs | idade {res['age']}d | "
              f"5primeiros {res['first5']:,} | {res['vpd']:,}/dia | mediana {res['median']:.0f}")
        print(f"  gates: idade<=45 {'ok' if g['age<=45'] else 'X'} | "
              f"5primeiros>=10k {'ok' if g['first5>=10k'] else 'X'} | "
              f"views/dia>=1k {'ok' if g['vpd>=1k'] else 'X'}  -> {tag}")
        for o in res["outliers"][:5]:
            print(f"    outlier {o['views']/res['median']:.1f}x  {o['views']:>8}  [{o['published']}] {o['title'][:60]}")
        if ok and res["small"]:
            passed.append(info["title"])
    print(f"\n=== Canais pequenos que passam os 3 gates: {len(passed)} ===")
    print(passed or "nenhum — estreite o cruzamento formato×topico")
    print("\nRegra: nicho aprovado exige >=3 canais pequenos passando os gates.")


if __name__ == "__main__":
    main()
