#!/usr/bin/env python3
"""niche_scan.py — pesquisa de nicho real (Data API + autocomplete + Trends + comentarios).

Modos:
  --query "..."         varre canais do termo: GATES (idade<=45d, 5 primeiros>=10k, >=1k/dia) + outliers
  --channel @handle     analisa um canal (gates + outliers vs mediana do proprio canal)
  --cluster "tema"      outliers cross-canal: >=2 canais diferentes com outlier = fome do algoritmo
  --comments VIDEOID    minera demanda nos comentarios (perguntas/pedidos recorrentes)
  --suggest "seed"      autocomplete do YouTube (profundidade de perguntas; sem API key)
  --trends "termo"      Google Trends (YouTube, 12m) via pytrends — fallback: autocomplete
  --brief "tema"        roda query + suggest + trends e salva BRIEF DE NICHO (.md + .json) em data/briefs/

Flags:
  --ratio 3             outlier = video >= ratio x a mediana do canal (default 3)
  --small 200000        max subs para considerar "canal pequeno"
  --max 8               nº de canais (query) / canais analisados (cluster)
  --lang en|pt|es       idioma de autocomplete/comentarios (default en)
  --out CAMINHO         caminho do .md (brief) ou .json (outros modos)
  --json                imprime o resultado cru em JSON

Requer OAuth (python scripts/yt_auth.py). Consome quota da Data API (~100 un por search) — use com moderacao.
"""
import argparse
import json
import re
import statistics
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

TOKEN = Path.home() / ".config" / "opencode" / "secrets" / "yt-token.json"
SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]
DATA = Path(__file__).resolve().parent.parent / "data" / "briefs"

DEMAND_PATTERNS = [
    r"\?", r"\b(why|how|what|who|when|where)\b", r"\b(please|pls)\b",
    r"\b(do|make) (a |another )?video\b", r"\b(can you|could you|you should)\b",
    r"\b(what happened to|where is|where are)\b",
    r"\b(por que|pq|como|quando|onde|quem)\b", r"\b(faz|fa[cç]a) um v[ií]deo\b",
    r"\b(voc[eê] pode|podia|deveria)\b", r"\b(o que aconteceu|cad[eê])\b",
]


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


def yt_client():
    from googleapiclient.discovery import build
    return build("youtube", "v3", credentials=creds())


def api(fn, **kw):
    """Chamada tolerante a quota: devolve {} e avisa se estourar."""
    from googleapiclient.errors import HttpError
    try:
        return fn(**kw).execute()
    except HttpError as e:
        reason = ""
        try:
            reason = json.loads(e.content.decode("utf-8"))["error"]["errors"][0]["reason"]
        except Exception:
            reason = str(e)
        if reason in ("quotaExceeded", "dailyLimitExceeded"):
            print(f"[!] QUOTA DA DATA API ESGOTADA ({reason}). Tente amanha ou use outro projeto.")
        else:
            print(f"[!] Erro na API: {reason}")
        return {}


def age_days(published):
    d = datetime.fromisoformat(published.replace("Z", "+00:00"))
    return (datetime.now(timezone.utc) - d).days


def slugify(s):
    s = re.sub(r"[^\w\s-]", "", s.lower(), flags=re.UNICODE).strip()
    return re.sub(r"[\s_]+", "-", s)[:60]


def channel_info(yt, cid):
    r = api(yt.channels().list, part="snippet,statistics,contentDetails", id=cid)
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


def channel_videos(yt, uploads, recent=15):
    r = api(yt.playlistItems().list, part="contentDetails", playlistId=uploads, maxResults=recent)
    ids = [i["contentDetails"]["videoId"] for i in r.get("items", [])]
    if not ids:
        return []
    v = api(yt.videos().list, part="statistics,snippet", id=",".join(ids))
    return [{
        "id": it["id"], "title": it["snippet"]["title"],
        "channel": it["snippet"]["channelTitle"], "channelId": it["snippet"]["channelId"],
        "published": it["snippet"]["publishedAt"][:10],
        "views": int(it["statistics"].get("viewCount", 0) or 0),
    } for it in v.get("items", [])]


def scan_channel(yt, info, ratio, small_max):
    vids = channel_videos(yt, info["uploads"])
    if not vids:
        return None
    age = age_days(info["published"])
    firsts = vids[-5:] if len(vids) >= 5 else vids
    first5 = sum(x["views"] for x in firsts)
    vpd = info["views"] / age if age else info["views"]
    med = statistics.median([x["views"] for x in vids]) or 1
    outs = [v for v in vids if v["views"] / med >= ratio]
    gates = {"age<=45": age <= 45, "first5>=10k": first5 >= 10000, "vpd>=1k": vpd >= 1000}
    return {"info": info, "age": age, "first5": first5, "vpd": round(vpd),
            "median": med, "outliers": outs, "gates": gates, "small": info["subs"] <= small_max}


def cmd_scan(yt, a):
    channels = []
    if a.channel:
        h = a.channel.lstrip("@")
        r = api(yt.channels().list, part="id", forHandle=h)
        if r.get("items"):
            channels = [r["items"][0]["id"]]
        else:
            print("[!] handle nao encontrado")
            return {}
    elif a.query:
        r = api(yt.search().list, part="snippet", q=a.query, type="channel", maxResults=a.max)
        channels = [i["snippet"]["channelId"] for i in r.get("items", [])]
    else:
        print("Use --query ou --channel")
        return {}

    print(f"# Niche scan — {a.query or a.channel}\n")
    passed, rows = [], []
    for cid in channels:
        info = channel_info(yt, cid)
        if not info:
            continue
        res = scan_channel(yt, info, a.ratio, a.small)
        if not res:
            continue
        g = res["gates"]
        ok = all(g.values())
        star = " *" if res["small"] else ""
        print(f"\n{info['title']}{star} — {info['subs']:,} subs | idade {res['age']}d | "
              f"5primeiros {res['first5']:,} | {res['vpd']:,}/dia | mediana {res['median']:.0f}")
        print(f"  gates: idade<=45 {'ok' if g['age<=45'] else 'X'} | "
              f"5primeiros>=10k {'ok' if g['first5>=10k'] else 'X'} | "
              f"views/dia>=1k {'ok' if g['vpd>=1k'] else 'X'}  -> {'PASSA' if ok else 'falha'}")
        for o in res["outliers"][:5]:
            print(f"    outlier {o['views']/res['median']:.1f}x  {o['views']:>8}  [{o['published']}] {o['title'][:60]}")
        rows.append({"channel": info["title"], "id": info["id"], "subs": info["subs"],
                     "age_days": res["age"], "first5": res["first5"], "vpd": res["vpd"],
                     "median": res["median"], "gates": g, "small": res["small"],
                     "outliers": [{"title": o["title"], "views": o["views"],
                                   "ratio": round(o["views"] / res["median"], 1),
                                   "published": o["published"], "id": o["id"]} for o in res["outliers"][:5]]})
        if ok and res["small"]:
            passed.append(info["title"])
    print(f"\n=== Canais pequenos que passam os 3 gates: {len(passed)} ===")
    print(passed or "nenhum — estreite o cruzamento formato×topico")
    print("\nRegra: nicho aprovado exige >=3 canais pequenos passando os gates.")
    return {"query": a.query or a.channel, "channels": rows, "passed": passed,
            "verdict": "PASSA" if len(passed) >= 3 else "REPROVA"}


def cmd_cluster(yt, a):
    """Outliers cross-canal: canais PEQUENOS com outlier no mesmo tema = fome do algoritmo."""
    since = (datetime.now(timezone.utc) - timedelta(days=a.window)).strftime("%Y-%m-%dT%H:%M:%SZ")
    r = api(yt.search().list, part="snippet", q=a.cluster, type="video", order="viewCount",
            maxResults=50, publishedAfter=since)
    items = r.get("items", [])
    if not items:
        print("[!] nenhum video encontrado para o tema")
        return {}
    found = {}
    for it in items:
        cid = it["snippet"]["channelId"]
        found.setdefault(cid, {"channel": it["snippet"]["channelTitle"], "videos": []})
        found[cid]["videos"].append({
            "id": it["id"]["videoId"], "title": it["snippet"]["title"],
            "published": it["snippet"]["publishedAt"][:10]})
    # metadados de todos os canais numa tacada (1 un por 50 ids) e filtra pequenos/jovens
    cids = list(found.keys())
    meta = {}
    for i in range(0, len(cids), 50):
        chunk = cids[i:i + 50]
        cr = api(yt.channels().list, part="snippet,statistics", id=",".join(chunk))
        for it in cr.get("items", []):
            meta[it["id"]] = {
                "title": it["snippet"]["title"], "published": it["snippet"]["publishedAt"],
                "subs": int(it["statistics"].get("subscriberCount", 0) or 0),
            }
    small_young = [cid for cid in cids if cid in meta
                   and meta[cid]["subs"] <= a.small and age_days(meta[cid]["published"]) <= a.age]
    print(f"# Cluster — {a.cluster}\n")
    print(f"canais encontrados: {len(found)} | pequenos (<= {a.small:,} subs) e <= {a.age}d: {len(small_young)}"
          f" | analisando {min(a.max, len(small_young))} (quota)\n")
    hungry, rows, passed, emerging = [], [], [], []
    for cid in small_young[:a.max]:
        info = channel_info(yt, cid)
        if not info:
            continue
        vids = channel_videos(yt, info["uploads"])
        med = statistics.median([v["views"] for v in vids]) or 1
        outs = []
        for fv in found[cid]["videos"]:
            match = next((v for v in vids if v["id"] == fv["id"]), None)
            if match and match["views"] / med >= a.ratio:
                outs.append({"title": match["title"], "views": match["views"],
                             "ratio": round(match["views"] / med, 1), "published": match["published"]})
        if outs:
            hungry.append(info["title"])
        age = age_days(info["published"])
        firsts = vids[-5:] if len(vids) >= 5 else vids
        first5 = sum(x["views"] for x in firsts)
        vpd = info["views"] / age if age else info["views"]
        gates = {"age<=45": age <= 45, "first5>=10k": first5 >= 10000, "vpd>=1k": vpd >= 1000}
        if all(gates.values()) and info["subs"] <= a.small:
            passed.append(info["title"])
        elif age <= 90 and sum(gates.values()) >= 2 and info["subs"] <= a.small:
            emerging.append(info["title"])
        print(f"{info['title']} — {info['subs']:,} subs | {age}d | 5primeiros {first5:,} | "
              f"{vpd:,.0f}/dia | mediana {med:.0f} | outliers {len(outs)}")
        for o in outs[:5]:
            print(f"    outlier {o['ratio']}x  {o['views']:>8}  [{o['published']}] {o['title'][:60]}")
        rows.append({"channel": info["title"], "id": cid, "subs": info["subs"], "age_days": age,
                     "first5": first5, "vpd": round(vpd), "gates": gates,
                     "median": med, "outliers": outs})
    print(f"\n=== GATES: {len(passed)} canal(is) pequeno(s) passando os 3 gates (meta >=3) ===")
    print(passed or "nenhum — estreite o cruzamento formato x topico")
    if emerging:
        print(f"\n=== EMERGENTES (watchlist: <=90d + 2/3 gates, NAO aprovam sozinhos) ===")
        print(emerging)
    print(f"\n=== FOME DO ALGORITMO: {len(hungry)} canal(is) com outlier >= {a.ratio}x ===")
    print(hungry or "nenhum — tema frio ou sem outlier na janela")
    if len(hungry) >= 2:
        print("SINAL: >=2 canais diferentes com outlier no mesmo tema -> janela de 2-6 semanas aberta.")
    return {"theme": a.cluster, "window_days": a.window, "channels": rows,
            "passed": passed, "emerging": emerging, "hungry": hungry, "signal": len(hungry) >= 2,
            "verdict": "PASSA" if len(passed) >= 3 else "REPROVA"}


def cmd_comments(yt, a):
    r = api(yt.commentThreads().list, part="snippet", videoId=a.comments, order="relevance",
            maxResults=100, textFormat="plainText")
    threads = r.get("items", [])
    if not threads:
        print("[!] sem comentarios (ou desativados). Se o erro foi insufficientPermissions,")
        print("    rode de novo: python scripts/yt_auth.py (o escopo force-ssl e necessario).")
        return {}
    comments = []
    for t in threads:
        s = t["snippet"]["topLevelComment"]["snippet"]
        comments.append({"text": s.get("textDisplay", ""), "likes": int(s.get("likeCount", 0)),
                         "replies": int(t["snippet"].get("totalReplyCount", 0))})
    comments.sort(key=lambda c: c["likes"], reverse=True)
    demand = [c for c in comments if any(re.search(p, c["text"], re.IGNORECASE) for p in DEMAND_PATTERNS)]
    print(f"# Comentarios — video {a.comments}\n")
    print(f"comentarios: {len(comments)} | com demanda explicita: {len(demand)}\n")
    print("## Top comentarios (por like)")
    for c in comments[:10]:
        print(f"  [{c['likes']:>4} likes] {c['text'][:110].replace(chr(10), ' ')}")
    print("\n## Demanda (perguntas/pedidos)")
    for c in demand[:15]:
        print(f"  [{c['likes']:>4}] {c['text'][:110].replace(chr(10), ' ')}")
    return {"videoId": a.comments, "total": len(comments),
            "top": comments[:20], "demand": demand[:30]}


def _suggest_once(seed, hl):
    url = "https://suggestqueries.google.com/complete/search?" + urllib.parse.urlencode(
        {"client": "youtube", "ds": "yt", "hl": hl, "q": seed})
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    raw = urllib.request.urlopen(req, timeout=10).read().decode("utf-8", "replace")
    m = re.search(r"\[.*\]", raw, re.DOTALL)
    if not m:
        return []
    try:
        data = json.loads(m.group(0))
    except Exception:
        return []
    out = []
    for item in data[1] if len(data) > 1 else []:
        if isinstance(item, list) and item:
            out.append(str(item[0]))
        elif isinstance(item, str):
            out.append(item)
    return out


def cmd_suggest(seed, hl):
    seen, results = set(), []
    for q in [seed] + [f"{seed} {c}" for c in "abcdefghijklmnopqrstuvwxyz"]:
        try:
            for s in _suggest_once(q, hl):
                if s.lower() not in seen:
                    seen.add(s.lower())
                    results.append(s)
        except Exception:
            continue
    print(f"# Autocomplete — {seed}\n")
    print(f"profundidade: {len(results)} termos unicos (meta >=15)\n")
    for s in results[:60]:
        print(f"  {s}")
    return {"seed": seed, "depth": len(results), "suggestions": results}


def cmd_trends(term):
    try:
        from pytrends.request import TrendReq
    except ImportError:
        print("[!] pytrends nao instalado (pip install pytrends). Fallback: use --suggest.")
        return {"term": term, "error": "pytrends ausente"}
    try:
        p = TrendReq(hl="en-US", tz=0)
        p.build_payload([term], timeframe="today 12-m", gprop="youtube")
        df = p.interest_over_time()
        if df is None or df.empty:
            print("[!] Trends sem dados para o termo")
            return {"term": term, "error": "sem dados"}
        vals = df[term].tolist()
        recent, prior = vals[-4:], vals[-16:-4] or vals[:-4]
        avg_recent = sum(recent) / len(recent)
        avg_prior = (sum(prior) / len(prior)) if prior else 0
        direction = "ALTA" if avg_recent > avg_prior * 1.1 else ("BAIXA" if avg_recent < avg_prior * 0.9 else "ESTAVEL")
        related = p.related_queries() or {}
        rising = []
        rq = related.get(term, {}).get("rising")
        if rq is not None and not rq.empty:
            rising = rq.head(10).to_dict("records")
        print(f"# Trends (YouTube 12m) — {term}\n")
        print(f"interesse: recente {avg_recent:.0f} vs anterior {avg_prior:.0f} -> {direction}")
        print("\n## Queries em alta")
        for r in rising:
            print(f"  {r.get('query')} (+{r.get('value')}%)")
        return {"term": term, "avg_recent": avg_recent, "avg_prior": avg_prior,
                "direction": direction, "rising": rising}
    except Exception as e:
        print(f"[!] Trends falhou ({e}). Fallback: use --suggest.")
        return {"term": term, "error": str(e)}


def cmd_brief(yt, a):
    """BRIEF DE NICHO: cluster (gates + outliers cross-canal) + autocomplete + Trends."""
    theme = a.brief
    slug = slugify(theme)
    DATA.mkdir(parents=True, exist_ok=True)
    print(f"# BRIEF DE NICHO — {theme}\n")
    cluster = cmd_cluster(yt, argparse.Namespace(cluster=theme, ratio=a.ratio, small=a.small,
                                                 max=a.max, window=a.window, age=a.age))
    print("\n" + "=" * 60 + "\n")
    suggest = cmd_suggest(theme, a.lang)
    print("\n" + "=" * 60 + "\n")
    trends = cmd_trends(theme)
    verdict = cluster.get("verdict", "REPROVA")
    lines = [
        f"# BRIEF DE NICHO — {theme}",
        f"> Gerado em {datetime.now().strftime('%Y-%m-%d %H:%M')} por `scripts/niche_scan.py --brief`.",
        "",
        f"## Veredito: **{verdict}**",
        f"- canais pequenos analisados: {len(cluster.get('channels', []))} | "
        f"passam os 3 gates: {len(cluster.get('passed', []))} (meta >=3)",
        f"- emergentes (watchlist <=90d + 2/3 gates, nao aprovam sozinhos): "
        f"{len(cluster.get('emerging', []))}",
        f"- fome do algoritmo (outlier >= {a.ratio}x): {len(cluster.get('hungry', []))} canal(is) "
        f"-> sinal {'SIM' if cluster.get('signal') else 'nao'}",
        f"- profundidade de autocomplete: {suggest.get('depth', 0)} termos (meta >=15)",
        f"- Trends: {trends.get('direction', trends.get('error', 'n/d'))}",
        "",
        "## Canais-evidencia (pequenos)",
    ]
    for c in cluster.get("channels", []):
        g = c["gates"]
        gates = "".join("1" if g[k] else "0" for k in ("age<=45", "first5>=10k", "vpd>=1k"))
        lines.append(f"- **{c['channel']}** — {c['subs']:,} subs | {c['age_days']}d | "
                     f"5primeiros {c['first5']:,} | {c['vpd']:,}/dia | gates {gates}")
        for o in c["outliers"][:3]:
            lines.append(f"    - outlier {o['ratio']}x — {o['views']:,} — {o['title'][:70]}")
    lines += ["", "## Autocomplete (demanda)", ""]
    for s in suggest.get("suggestions", [])[:25]:
        lines.append(f"- {s}")
    lines += ["", "## Trends (YouTube 12m)", ""]
    if trends.get("rising"):
        for r in trends["rising"][:10]:
            lines.append(f"- {r.get('query')} (+{r.get('value')}%)")
    else:
        lines.append(f"- {trends.get('direction', trends.get('error', 'n/d'))}")
    lines += ["", "## Proximo passo", "",
              "- Se PASSA: escolher lane (`23`), gerar beats do modelo e piloto em 2 semanas.",
              "- Se REPROVA: estreitar o cruzamento formato x topico (nao insistir)."]
    md = "\n".join(lines) + "\n"
    md_path = Path(a.out) if a.out else DATA / f"{slug}.md"
    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(md, encoding="utf-8")
    json_path = md_path.with_suffix(".json")
    json_path.write_text(json.dumps({"theme": theme, "cluster": cluster, "suggest": suggest,
                                     "trends": trends}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n[OK] brief: {md_path}")
    print(f"[OK] dados: {json_path}")
    return {"brief": str(md_path), "json": str(json_path), "verdict": verdict}


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--query")
    ap.add_argument("--channel")
    ap.add_argument("--cluster")
    ap.add_argument("--comments")
    ap.add_argument("--suggest")
    ap.add_argument("--trends")
    ap.add_argument("--brief")
    ap.add_argument("--ratio", type=float, default=3.0)
    ap.add_argument("--small", type=int, default=200000, help="max subs para 'pequeno'")
    ap.add_argument("--max", type=int, default=8, help="nº de canais a analisar")
    ap.add_argument("--window", type=int, default=90, help="janela em dias (cluster/busca de videos)")
    ap.add_argument("--age", type=int, default=365, help="idade maxima do canal em dias (cluster)")
    ap.add_argument("--lang", default="en", choices=["en", "pt", "es"])
    ap.add_argument("--out")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    hl = {"en": "en", "pt": "pt-BR", "es": "es"}[a.lang]

    if a.suggest:
        res = cmd_suggest(a.suggest, hl)
        if a.out:
            Path(a.out).write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
        return
    if a.trends:
        res = cmd_trends(a.trends)
        if a.out:
            Path(a.out).write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
        return

    yt = yt_client()
    if a.comments:
        res = cmd_comments(yt, a)
    elif a.cluster:
        res = cmd_cluster(yt, a)
    elif a.brief:
        res = cmd_brief(yt, a)
    elif a.query or a.channel:
        res = cmd_scan(yt, a)
    else:
        print("Use --query | --channel | --cluster | --comments | --suggest | --trends | --brief")
        return
    if a.out and a.json:
        Path(a.out).write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[OK] json: {a.out}")


if __name__ == "__main__":
    main()
