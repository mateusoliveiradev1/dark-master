#!/usr/bin/env python3
"""add_channel.py — coloca um canal novo no painel com verificacao real.

Valida na Data API (existe? pais? uploads recentes? idioma dos uploads) e
aborta explicando se nao. Sugere vigias iniciais (canais do mesmo nicho ja
monitorados) e reconstrui data/dashboard.json. Sem rede/API: --dry-run mostra
o que faria.

Uso:
  python scripts/add_channel.py --handle @Novo --name "Nome" --mine \
      --niche true-crime --country BR --lang pt
  python scripts/add_channel.py --handle @Ref --niche true-crime   # vigia
"""
import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

CHANNELS = ROOT / "monitor" / "channels.json"
YPP_INPUT = ROOT / "data" / "ypp_input.json"


def validate(handle, country, lang):
    """Consulta real: snippet (pais, idioma) + uploads recentes. Retorna dict."""
    from niche_scan import api, creds, yt_client
    yt = yt_client()
    creds()
    handle = handle.lstrip("@")
    r = api(yt.channels().list, part="snippet,statistics,contentDetails", forHandle=handle)
    items = r.get("items", [])
    if not items:
        return {"ok": False, "error": f"handle @{handle} nao encontrado"}
    info = items[0]
    snippet = info.get("snippet", {})
    stats = info.get("statistics", {})
    uploads = info.get("contentDetails", {}).get("relatedPlaylists", {}).get("uploads", "")
    videos = []
    if uploads:
        page = api(yt.playlistItems().list, part="snippet,contentDetails", playlistId=uploads, maxResults=10)
        for item in page.get("items", []):
            snippet_item = item.get("snippet", {})
            videos.append({"title": snippet_item.get("title", ""),
                           "published": (snippet_item.get("publishedAt") or "")[:10]})
    detected_country = snippet.get("country", "")
    if country and detected_country and detected_country.upper() != country.upper():
        return {"ok": False, "error": f"pais do canal ({detected_country}) difere de --country {country}"}
    return {"ok": True, "id": info.get("id", ""), "title": snippet.get("title", ""),
            "country": detected_country or country.upper(),
            "subs": int(stats.get("subscriberCount", 0) or 0),
            "videos_total": int(stats.get("videoCount", 0) or 0),
            "recent": videos}


def suggest_watchers(niche, handle, limit=4):
    """Vigias sugeridos: canais ja monitorados do mesmo nicho."""
    try:
        data = json.loads(CHANNELS.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return []
    mine_handle = handle.lower()
    return [c.get("handle", "") for c in data.get("channels", [])
            if c.get("niche") == niche and c.get("handle", "").lower() != mine_handle][:limit]


def add(handle, name, mine, niche, country, lang, info, dry_run=False, args_account=None):
    handle = "@" + handle.lstrip("@")
    try:
        data = json.loads(CHANNELS.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        data = {"channels": []}
    if any(c.get("handle", "").lower() == handle.lower() for c in data.get("channels", [])):
        return {"status": "FAIL", "error": f"{handle} ja monitorado"}
    entry = {"name": name or info.get("title", handle), "handle": handle,
             "niche": niche or "unknown", "country": country.upper(), "lang": lang,
             "nota": info.get("title", "")}
    if mine:
        entry["mine"] = True
    if args_account:
        entry["account"] = args_account
    watchers = suggest_watchers(niche, handle) if niche else []
    result = {"status": "OK", "channel": entry, "suggested_watchers": watchers,
              "info": {k: info.get(k) for k in ("subs", "videos_total", "country", "recent")}}
    if dry_run:
        result["status"] = "DRY_RUN"
        return result
    data.setdefault("channels", []).append(entry)
    CHANNELS.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if mine:
        try:
            ypp = json.loads(YPP_INPUT.read_text(encoding="utf-8")) if YPP_INPUT.exists() else {}
        except ValueError:
            ypp = {}
        ypp.setdefault(handle, {"subs": info.get("subs", 0), "hours": 0, "short_views": 0,
                                "longs_90d": 0, "shorts_90d": 0})
        YPP_INPUT.parent.mkdir(parents=True, exist_ok=True)
        YPP_INPUT.write_text(json.dumps(ypp, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    from learn_loop import build_dashboard
    build_dashboard()
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--handle", required=True)
    parser.add_argument("--name", default="")
    parser.add_argument("--mine", action="store_true")
    parser.add_argument("--niche", default="")
    parser.add_argument("--country", default="")
    parser.add_argument("--lang", default="pt", choices=["pt", "en", "es"])
    parser.add_argument("--account", default="",
                        help="alias da conta Google dona do canal (yt-token-<alias>.json)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        info = validate(args.handle, args.country, args.lang)
    except SystemExit as exc:
        print(json.dumps({"status": "FAIL", "error": f"sem_auth:{exc}"}))
        return 2
    except Exception as exc:
        print(json.dumps({"status": "FAIL", "error": f"api:{exc}"[:200]}))
        return 1
    if not info.get("ok"):
        print(json.dumps({"status": "FAIL", **info}, ensure_ascii=False))
        return 1
    result = add(args.handle, args.name, args.mine, args.niche, args.country, args.lang, info, args.dry_run, args.account or None)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] in {"OK", "DRY_RUN"} else 1


if __name__ == "__main__":
    sys.exit(main())
