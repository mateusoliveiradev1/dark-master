#!/usr/bin/env python3
"""yt_analysis.py — diagnóstico explicável e rastreável do canal."""
import argparse
import csv
import json
import statistics
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DATA = ROOT / "data"


def number(value, default=0):
    if value is None or value == "":
        return default
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def integer(value):
    return int(number(value, 0))


def median(values):
    clean = [number(value) for value in values if value is not None and value != ""]
    return round(statistics.median(clean), 2) if clean else None


def ratio(value, baseline):
    value = number(value)
    baseline = number(baseline)
    return round(value / baseline, 2) if baseline else None


def percent(value, total):
    return round(number(value) / number(total) * 100, 2) if number(total) else None


def fmt(value, suffix=""):
    if value is None or value == "":
        return "n/d"
    if isinstance(value, str):
        try:
            value = float(value)
        except ValueError:
            return f"{value}{suffix}"
    if isinstance(value, float):
        if value.is_integer():
            return f"{int(value):,}".replace(",", ".") + suffix
        return f"{value:,.2f}".replace(".", "§").replace(",", ".").replace("§", ",") + suffix
    return f"{value:,}".replace(",", ".") + suffix


def load_data(channel):
    sys.path.insert(0, str(HERE))
    import yt_db
    yt_db.init(quiet=True)
    c = yt_db.conn()
    snapshots = yt_db._rows(c, "SELECT * FROM snapshots WHERE channel=? ORDER BY ts, video_id", (channel,))
    mappings = yt_db._rows(c, "SELECT * FROM videos WHERE channel=?", (channel,))
    traffic = yt_db._rows(c, "SELECT * FROM traffic_sources WHERE channel=? ORDER BY captured_ts", (channel,))
    retention = yt_db._rows(c, "SELECT * FROM retention_points WHERE channel=? ORDER BY captured_ts", (channel,))
    experiments = yt_db._rows(c, "SELECT * FROM experiments WHERE channel=? ORDER BY ts DESC", (channel,))
    c.close()
    csv_rows = {}
    csv_path = DATA / "metrics.csv"
    if csv_path.exists():
        with csv_path.open(encoding="utf-8-sig", newline="") as handle:
            csv_rows = {row["video_id"]: row for row in csv.DictReader(handle) if row.get("video_id")}
    return snapshots, mappings, traffic, retention, experiments, csv_rows


def reconcile_latest(snapshots, csv_rows):
    history = defaultdict(dict)
    aliases = {"subs_gained": "subscribers_gained", "subs_lost": "subscribers_lost"}
    for row in snapshots:
        for key in ("title", "format", "published", "duration_seconds", "subscribers_gained", "subscribers_lost"):
            if row.get(key) not in (None, "") and key not in history[row["video_id"]]:
                history[row["video_id"]][key] = row[key]
    latest = latest_rows(snapshots)
    output = []
    for row in latest:
        merged = dict(history.get(row["video_id"], {}))
        merged.update({key: value for key, value in row.items() if value not in (None, "")})
        for key, value in csv_rows.get(row["video_id"], {}).items():
            normalized = aliases.get(key, key)
            if value not in (None, ""):
                merged[normalized] = value
        output.append(merged)
    return output


def latest_rows(snapshots):
    latest = {}
    for row in snapshots:
        latest[row["video_id"]] = row
    return list(latest.values())


def capture_groups(snapshots):
    groups = defaultdict(list)
    for row in snapshots:
        groups[row["ts"]].append(row)
    return sorted(groups.items(), key=lambda item: item[0])


def baseline_for(rows, video_format):
    subset = [row for row in rows if row.get("format") == video_format]
    return {
        "n": len(subset),
        "views_median": median([row.get("views") for row in subset]),
        "avd_median": median([row.get("avd_seconds") for row in subset]),
        "avp_median": median([row.get("avp_percent") for row in subset]),
        "watch_hours_median": median([row.get("watch_hours") for row in subset]),
        "subs_median": median([row.get("subscribers_gained") for row in subset]),
        "engagement_rate_median": median([
            percent(row.get("engaged_views"), row.get("views")) for row in subset if number(row.get("views"))
        ]),
    }


def totals(rows):
    result = {key: sum(number(row.get(key)) for row in rows) for key in (
        "views", "engaged_views", "watch_hours", "subscribers_gained", "subscribers_lost", "likes", "comments", "shares"
    )}
    result["engagement_rate"] = percent(result["engaged_views"], result["views"])
    result["subs_per_1000_views"] = round(result["subscribers_gained"] / number(result["views"]) * 1000, 2) if number(result["views"]) else None
    return result


def compare_captures(snapshots):
    groups = capture_groups(snapshots)
    if len(groups) < 2:
        return None
    current_rows, previous_rows = groups[-1][1], groups[-2][1]
    current = totals(current_rows)
    previous = totals(previous_rows)
    changes = {}
    for key in ("views", "engaged_views", "watch_hours", "subscribers_gained"):
        before = number(previous.get(key))
        current_value = number(current.get(key))
        changes[key] = round((current_value - before) / before * 100, 1) if before else None
    current_period = (current_rows[0].get("period_start"), current_rows[0].get("period_end")) if current_rows else (None, None)
    previous_period = (previous_rows[0].get("period_start"), previous_rows[0].get("period_end")) if previous_rows else (None, None)
    comparable = current_period != (None, None) and current_period == previous_period
    if not comparable:
        changes = {key: None for key in changes}
    return {
        "current_ts": groups[-1][0], "previous_ts": groups[-2][0],
        "current": current, "previous": previous, "changes": changes,
        "current_period": current_period, "previous_period": previous_period,
        "comparable_period": comparable,
    }


def latest_traffic(traffic):
    if not traffic:
        return []
    captured = max(row["captured_ts"] for row in traffic)
    return [row for row in traffic if row["captured_ts"] == captured]


def latest_retention(retention):
    if not retention:
        return {}
    captured = max(row["captured_ts"] for row in retention)
    grouped = defaultdict(list)
    for row in retention:
        if row["captured_ts"] == captured:
            grouped[row["video_id"]].append(row)
    return {video_id: sorted(points, key=lambda point: number(point.get("elapsed_ratio"))) for video_id, points in grouped.items()}


def traffic_summary(traffic_rows):
    grouped = defaultdict(lambda: {"views": 0, "engaged_views": 0, "watch_hours": 0.0, "videos": set()})
    for row in traffic_rows:
        item = grouped[row.get("source_type") or "n/d"]
        item["views"] += integer(row.get("views"))
        item["engaged_views"] += integer(row.get("engaged_views"))
        item["watch_hours"] += number(row.get("watch_hours"))
        item["videos"].add(row.get("video_id"))
    output = []
    for source, values in grouped.items():
        output.append({
            "source": source, "views": values["views"], "engaged_views": values["engaged_views"],
            "watch_hours": round(values["watch_hours"], 2), "videos": len(values["videos"]),
        })
    return sorted(output, key=lambda item: item["views"], reverse=True)


def short_to_long(traffic_rows, mappings, long_ids):
    mapping_by_id = {row["video_id"]: row for row in mappings}
    funnel = {"views": 0, "watch_hours": 0.0, "pairs": [], "unmatched_sources": []}
    for row in traffic_rows:
        if row.get("video_id") not in long_ids or row.get("source_type") not in {"RELATED_VIDEO", "END_SCREEN"}:
            continue
        source_id = row.get("source_detail") or ""
        views = integer(row.get("views"))
        source_mapping = mapping_by_id.get(source_id, {})
        if source_mapping.get("format") != "short":
            funnel["unmatched_sources"].append({
                "long_tag": mapping_by_id.get(row["video_id"], {}).get("video_tag"),
                "long_id": row.get("video_id"), "source": row.get("source_type"),
                "source_id": source_id, "views": views,
            })
            continue
        watch_hours = number(row.get("watch_hours"))
        funnel["views"] += views
        funnel["watch_hours"] += watch_hours
        funnel["pairs"].append({
            "short_tag": source_mapping.get("video_tag"), "long_tag": mapping_by_id.get(row["video_id"], {}).get("video_tag"),
            "source": row.get("source_type"), "views": views, "watch_hours": round(watch_hours, 2),
        })
    return funnel


def retention_drops(points):
    if len(points) < 3:
        return []
    ordered = sorted(points, key=lambda point: number(point.get("elapsed_ratio")))
    previous_value = number(ordered[0].get("audience_watch_ratio"))
    drops = []
    for point in ordered[1:]:
        ratio_value = number(point.get("elapsed_ratio"))
        value = number(point.get("audience_watch_ratio"))
        drops.append({
            "at": ratio_value, "retention": value,
            "drop": round((previous_value - value) * 100, 2),
        })
        previous_value = value
    return sorted(drops, key=lambda item: item["drop"], reverse=True)


def video_diagnosis(row, baselines, mapping):
    video_format = row.get("format")
    baseline = baselines.get(video_format, {})
    views = integer(row.get("views"))
    view_ratio = ratio(views, baseline.get("views_median"))
    avd = number(row.get("avd_seconds"))
    avd_ratio = ratio(avd, baseline.get("avd_median"))
    watch_hours = number(row.get("watch_hours"))
    watch_ratio = ratio(watch_hours, baseline.get("watch_hours_median"))
    ctr = row.get("ctr_percent")
    subscribers = integer(row.get("subscribers_gained"))
    subscriber_rate = subscribers / views if views else 0
    if video_format == "long":
        if view_ratio is not None and view_ratio < 1 and subscriber_rate >= 0.05:
            bottleneck = "conversão excepcional com baixo alcance"
            confidence = "baixa"
            explanation = "os inscritos por view estão acima de 5%; o problema provável é alcance, mas a amostra é pequena."
        elif view_ratio is not None and view_ratio < 1 and watch_ratio is not None and watch_ratio >= 1:
            bottleneck = "tráfego/embalagem"
            confidence = "média" if baseline.get("n", 0) >= 5 else "baixa"
            explanation = "recebe menos views que a mediana, mas entrega watch hours acima da mediana; quem chega assiste."
        elif view_ratio is not None and avd_ratio is not None and watch_ratio is not None and view_ratio >= 1 and avd_ratio >= 1 and watch_ratio >= 1:
            is_outlier = max(number(view_ratio), number(watch_ratio)) >= 3
            bottleneck = "outlier de watch time" if is_outlier else "acima da mediana"
            confidence = "média" if baseline.get("n", 0) >= 5 else "baixa"
            explanation = "alcance, duração média e watch hours acima da mediana; tratar como caso de estudo, não causalidade."
        elif view_ratio is not None and avd_ratio is not None and view_ratio >= 1 and avd_ratio < 1:
            bottleneck = "retenção"
            confidence = "média" if baseline.get("n", 0) >= 5 else "baixa"
            explanation = "alcance acima da mediana com duração média abaixo da mediana."
        else:
            bottleneck = "dados insuficientes"
            confidence = "baixa"
            explanation = "não há contraste suficiente contra a coorte do próprio canal."
    elif video_format == "short":
        if view_ratio is not None and view_ratio >= 2:
            bottleneck = "outlier de alcance"
            confidence = "baixa"
            explanation = "alcance muito acima da mediana; retenção e conversão ainda precisam ser comparadas."
        elif view_ratio is not None and avd_ratio is not None and view_ratio < 1 and avd_ratio >= 1:
            bottleneck = "distribuição/embalagem"
            confidence = "baixa"
            explanation = "retenção acima da mediana com baixo alcance; falta CTR/impressões para separar embalagem de distribuição."
        else:
            bottleneck = "aberto"
            confidence = "baixa"
            explanation = "o conjunto não isola um gargalo sem perder qualidade de amostra."
    else:
        bottleneck = "formato desconhecido"
        confidence = "baixa"
        explanation = "o Analytics não informou o tipo de conteúdo."
    return {
        "video_id": row.get("video_id"), "video_tag": mapping.get("video_tag"),
        "case_name": mapping.get("case_name"), "series": mapping.get("series"),
        "format": video_format, "views": views, "engaged_views": integer(row.get("engaged_views")),
        "avd_seconds": avd, "avp_percent": row.get("avp_percent"), "watch_hours": watch_hours,
        "subscribers_gained": integer(row.get("subscribers_gained")),
        "ctr_percent": ctr, "view_ratio": view_ratio, "avd_ratio": avd_ratio,
        "subscriber_rate_percent": round(subscriber_rate * 100, 2),
        "watch_ratio": watch_ratio, "bottleneck": bottleneck, "confidence": confidence,
        "explanation": explanation,
    }


def experiments_for(latest, baselines, traffic_rows, calendar_context, funnel):
    experiments = []
    longs = [row for row in latest if row.get("format") == "long"]
    shorts = [row for row in latest if row.get("format") == "short"]
    long_baseline = baselines.get("long", {})
    short_baseline = baselines.get("short", {})
    if len(longs) >= 3 and number(long_baseline.get("views_median")):
        high_value = [row for row in longs if number(row.get("watch_hours")) >= number(long_baseline.get("watch_hours_median"))]
        if high_value and number(long_baseline.get("views_median")) < 100:
            experiments.append({
                "scope": "long/embalagem", "variable": "título",
                "hypothesis": "Um título mais explícito aumenta impressões qualificadas sem mudar o conteúdo.",
                "baseline": f"mediana de {fmt(long_baseline.get('views_median'))} views em {long_baseline.get('n')} longs",
                "target": "superar a mediana de views mantendo watch hours por view",
                "measurement": "impressões, CTR, engaged views e watch hours",
                "sample": "4–6 longs comparáveis, uma versão por vídeo",
                "risk": "misturar efeito do título com mudança de thumbnail",
            })
    if len(shorts) >= 5 and number(short_baseline.get("views_median")):
        high_retention = [row for row in shorts if ratio(row.get("avd_seconds"), short_baseline.get("avd_median")) and ratio(row.get("avd_seconds"), short_baseline.get("avd_median")) >= 1]
        if high_retention and number(short_baseline.get("views_median")) < 100:
            experiments.append({
                "scope": "short/embalagem", "variable": "título do Short",
                "hypothesis": "Shorts com retenção alta e alcance baixo têm espaço em packaging, mas a métrica exata precisa ser confirmada.",
                "baseline": f"mediana de {fmt(short_baseline.get('views_median'))} views em {short_baseline.get('n')} Shorts",
                "target": "aumentar alcance sem reduzir AVD/engaged rate",
                "measurement": "impressões, CTR, AVD, engaged views e inscritos",
                "sample": "4–6 Shorts; testar somente o título em cada vídeo",
                "risk": "métrica de exposição não disponível e risco de confundir efeito do título com o tema",
            })
    if not funnel.get("pairs"):
        next_long = next((row for row in calendar_context.get("upcoming", []) if row.get("ready")), None)
        experiments.append({
            "scope": "funil Short→Long", "variable": "vídeo relacionado",
            "hypothesis": "Adicionar o Long como relacionado ao Short aumenta views do Long sem depender de CTA verbal.",
            "baseline": "par Short→Long ainda não medido",
            "target": "registrar source RELATED_VIDEO por par",
            "measurement": "views e watch hours do Long por source e detail",
            "sample": "próximos 4 Shorts; um método por vez",
            "risk": "atribuição só fica completa depois que o Short e o Long estiverem públicos",
            "video_tag": next_long.get("video_tag") if next_long else None,
        })
    return experiments[:3]


def build_report(channel, project, today):
    snapshots, mappings, traffic, retention, experiment_rows, csv_rows = load_data(channel)
    latest = reconcile_latest(snapshots, csv_rows)
    mapping_by_id = {row["video_id"]: row for row in mappings}
    baselines = {fmt_name: baseline_for(latest, fmt_name) for fmt_name in ("short", "long")}
    channel_totals = totals(latest)
    capture = compare_captures(snapshots)
    traffic_rows = latest_traffic(traffic)
    retention_by_video = latest_retention(retention)
    long_ids = {row["video_id"] for row in latest if row.get("format") == "long"}
    funnel = short_to_long(traffic_rows, mappings, long_ids)
    current = None
    calendar_context = {"upcoming": [], "today_video": None, "next_to_produce": None, "ready_stock": 0}
    if project:
        sys.path.insert(0, str(HERE))
        import channel_scan
        calendar_context = channel_scan.build_context(project, today)
    else:
        current = None
    current = calendar_context.get("today_video")
    diagnoses = [video_diagnosis(row, baselines, mapping_by_id.get(row["video_id"], {})) for row in latest]
    diagnoses.sort(key=lambda item: (item.get("format") or "", -(item.get("views") or 0)))
    experiments = experiments_for(latest, baselines, traffic_rows, calendar_context, funnel)
    tag_groups = defaultdict(list)
    for mapping in mappings:
        if mapping.get("video_tag") and mapping.get("match_status") == "matched":
            tag_groups[(mapping.get("video_tag"), mapping.get("format"))].append(mapping.get("video_id"))
    duplicate_mappings = [
        {"video_tag": tag, "format": video_format, "video_ids": video_ids}
        for (tag, video_format), video_ids in tag_groups.items() if len(video_ids) > 1
    ]
    outliers = []
    for row in diagnoses:
        if row.get("view_ratio") is not None and row["view_ratio"] >= 3:
            outliers.append(row)
    quality = {
        "snapshot_count": len(snapshots),
        "latest_video_count": len(latest),
        "capture_count": len(capture_groups(snapshots)),
        "traffic_rows": len(traffic_rows),
        "retention_videos": len(retention_by_video),
        "missing_title": len([row for row in latest if not row.get("title")]),
        "unmatched": len([row for row in latest if not mapping_by_id.get(row["video_id"], {}).get("video_tag")]),
        "duplicate_mappings": duplicate_mappings,
        "ctr_available": len([row for row in latest if row.get("ctr_percent") is not None]),
        "published_missing": len([row for row in mappings if not row.get("published_at")]),
        "period_end": max((row.get("period_end") or "" for row in latest), default=""),
    }
    return {
        "channel": channel, "project": project, "today": today, "quality": quality,
        "totals": channel_totals, "capture": capture, "baselines": baselines, "mappings": mapping_by_id,
        "diagnoses": diagnoses, "outliers": outliers, "traffic": traffic_summary(traffic_rows),
        "funnel": funnel, "retention_by_video": retention_by_video,
        "calendar": calendar_context, "experiments": experiments,
        "stored_experiments": experiment_rows,
    }


def render_markdown(report):
    quality = report["quality"]
    totals_data = report["totals"]
    baselines = report["baselines"]
    lines = [
        f"# Revisão diária — {report['channel']}",
        f"Data de referência: {report['today']}",
        "",
        "## Resumo executivo",
        f"- Views públicas no último snapshot: **{fmt(totals_data.get('views'))}**.",
        f"- Engaged views: **{fmt(totals_data.get('engaged_views'))}** ({fmt(totals_data.get('engagement_rate'), '%')} das views).",
        f"- Watch time público: **{fmt(totals_data.get('watch_hours'), ' h')}**; use o Studio para watch hours qualificados do YPP.",
        f"- Inscritos ganhos: **{fmt(totals_data.get('subscribers_gained'))}**; perdidos: **{fmt(totals_data.get('subscribers_lost'))}**.",
        f"- Base: {quality['latest_video_count']} vídeos, {quality['capture_count']} capturas e dados completos até **{quality['period_end'] or 'n/d'}**.",
        "",
        "## Qualidade e limites dos dados",
        f"- Títulos ausentes: {quality['missing_title']}; mapeamentos não confirmados: {quality['unmatched']}.",
        f"- Tags locais ligadas a mais de um ID: {len(quality['duplicate_mappings'])}; revisar antes de usar esses dados em causalidade.",
        f"- Datas de publicação ausentes: {quality['published_missing']}; reexecute `python scripts/yt_auth.py` para renovar `youtube.readonly`.",
        f"- CTR disponível em {quality['ctr_available']} vídeos; shown-in-feed/chose-to-view continuam dependentes de fonte declarada.",
        f"- Linhas de tráfego na última captura: {quality['traffic_rows']}; vídeos com curva de retenção: {quality['retention_videos']}.",
        "- A Analytics API tem defasagem; números públicos e métricas processadas não devem ser comparados como se fossem simultâneos.",
        "- Ausência de dado é desconhecida, nunca zero. Amostra pequena gera hipótese, não regra.",
        "",
        "## Evolução entre capturas",
    ]
    capture = report.get("capture")
    if capture:
        comparable = "mesmo período" if capture["comparable_period"] else "períodos diferentes; comparação apenas indicativa"
        lines.append(f"- Captura anterior: {capture['previous_ts']} ({comparable}).")
        for key, change in capture["changes"].items():
            lines.append(f"- {key}: {fmt(capture['current'].get(key))}; variação **{fmt(change, '%')}**.")
    else:
        lines.append("- Ainda existe apenas uma captura; não há variação temporal confiável.")
    lines.extend(["", "## Baseline por formato"])
    for name, baseline in baselines.items():
        lines.append(
            f"- **{name}**: n={baseline['n']}; views {fmt(baseline['views_median'])}; "
            f"AVD {fmt(baseline['avd_median'])}s; AVP {fmt(baseline['avp_median'], '%')}; "
            f"watch hours {fmt(baseline['watch_hours_median'], ' h')}; inscritos {fmt(baseline['subs_median'])}."
        )
    for duplicate in quality["duplicate_mappings"]:
        lines.append(f"- Conflito: {duplicate['video_tag']} [{duplicate['format']}] ligado a {', '.join(duplicate['video_ids'])}.")
    lines.extend(["", "## Diagnóstico por vídeo"])
    for item in report["diagnoses"]:
        tag = f" {item['video_tag']}" if item.get("video_tag") else ""
        case = f" — {item['case_name']}" if item.get("case_name") else ""
        lines.append(
            f"### {tag}{case} [{item['format']}]"
        )
        lines.append(
            f"- `{item['video_id']}`: {fmt(item['views'])} views, {fmt(item['engaged_views'])} engaged, "
            f"AVD {fmt(item['avd_seconds'])}s, AVP {fmt(item['avp_percent'], '%')}, "
            f"{fmt(item['watch_hours'], ' h')}, {fmt(item['subscribers_gained'])} inscritos."
        )
        lines.append(f"- Conversão: {fmt(item['subscriber_rate_percent'], '%')} inscritos por view.")
        lines.append(
            f"- Gargalo provável: **{item['bottleneck']}**; confiança **{item['confidence']}**; "
            f"razão views/baseline {fmt(item['view_ratio'], 'x')}; razão AVD/baseline {fmt(item['avd_ratio'], 'x')}."
        )
        lines.append(f"- Explicação: {item['explanation']}")
        if item.get("ctr_percent") is None:
            lines.append("- CTR n/d: não diferencia packaging de distribuição sem inventar valor.")
    lines.extend(["", "## Outliers por formato"])
    if report["outliers"]:
        for item in report["outliers"]:
            lines.append(
                f"- {item.get('video_tag') or item['video_id']} ({item['format']}): "
                f"{fmt(item['views'])} views, {fmt(item['view_ratio'], 'x')} a mediana; hipótese, não causalidade."
            )
    else:
        lines.append("- Nenhum outlier ≥3× no snapshot atual.")
    lines.extend(["", "## Fontes de tráfego"])
    if report["traffic"]:
        for item in report["traffic"]:
            lines.append(
                f"- {item['source']}: {fmt(item['views'])} views, {fmt(item['engaged_views'])} engaged, "
                f"{fmt(item['watch_hours'], ' h')} em {item['videos']} vídeos."
            )
    else:
        lines.append("- Nenhuma fonte de tráfego persistida; o funil não pode ser atribuído ainda.")
    lines.append("- `SHORTS` representa navegação vertical entre Shorts; não é tráfego Short→Long. Pares de conversão usam `RELATED_VIDEO` com o ID de origem quando disponível.")
    funnel = report["funnel"]
    lines.extend(["", "## Funil Short→Long", f"- Pares medidos: {len(funnel['pairs'])}; views atribuídas: {fmt(funnel['views'])}; watch hours: {fmt(funnel['watch_hours'], ' h')}."])
    for pair in sorted(funnel["pairs"], key=lambda item: item["views"], reverse=True)[:10]:
        lines.append(f"- {pair['short_tag']} → {pair['long_tag']} via {pair['source']}: {fmt(pair['views'])} views, {fmt(pair['watch_hours'], ' h')}.")
    for item in sorted(funnel["unmatched_sources"], key=lambda row: row["views"], reverse=True)[:10]:
        lines.append(f"- {item['long_tag'] or item['long_id']} recebeu {fmt(item['views'])} views de `{item['source_id'] or 'n/d'}`; origem ainda sem match confirmado.")
    lines.extend(["", "## Retenção por trecho"])
    if report["retention_by_video"]:
        for video_id, points in sorted(report["retention_by_video"].items()):
            drops = retention_drops(points)[:3]
            if not drops:
                continue
            tag = report["mappings"].get(video_id, {}).get("video_tag") or video_id
            formatted = ", ".join(f"{int(item['at'] * 100)}%: −{fmt(item['drop'], ' p.p')}" for item in drops)
            lines.append(f"- {tag}: maiores quedas aproximadas — {formatted}.")
    else:
        lines.append("- Sem curvas de retenção retornadas.")
    lines.extend(["", "## Calendário e estoque"])
    calendar_context = report["calendar"]
    today_video = calendar_context.get("today_video")
    if today_video:
        lines.append(f"- Vídeo do dia: {today_video['video_tag']} — {today_video['case_name']} — {today_video['state']}.")
    lines.append(f"- Estoque futuro pronto: {calendar_context.get('ready_stock', 0)}.")
    for row in calendar_context.get("upcoming", [])[:7]:
        lines.append(f"- {row['date']} {row['video_tag']} {row['case_name']}: **{row['state']}**.")
    if calendar_context.get("next_to_produce"):
        row = calendar_context["next_to_produce"]
        lines.append(f"- Próximo a produzir: {row['video_tag']} — {row['case_name']}.")
    chain = calendar_context.get("chain", [])
    broken = [row for row in chain if not row.get("ok")]
    lines.append(f"- Corrente de teasers: {len(chain) - len(broken)}/{len(chain)} com próximo caso comprovado.")
    lines.extend(["", "## Experimentos propostos"])
    for index, experiment in enumerate(report["experiments"], 1):
        lines.append(f"### {index}. {experiment['scope']}")
        lines.append(f"- Variável: {experiment['variable']}.")
        lines.append(f"- Hipótese: {experiment['hypothesis']}")
        lines.append(f"- Baseline: {experiment['baseline']}.")
        lines.append(f"- Meta: {experiment['target']}.")
        lines.append(f"- Medição: {experiment['measurement']}; amostra: {experiment['sample']}.")
        lines.append(f"- Risco: {experiment['risk']}.")
    if not report["experiments"]:
        lines.append("- Sem experimento novo: ainda falta amostra, mapa ou baseline confiável.")
    lines.extend(["", "## Checkpoints", "- Próxima captura diária: verificar mudança e mapeamentos.", "- D+2/D+7: comparar o mesmo vídeo quando houver snapshots maduros.", "- Após 4–6 vídeos comparáveis: decidir manter, ajustar ou descartar cada hipótese.", "- Alterar calendário, metadata ou produção somente após aprovação explícita."])
    return "\n".join(lines)


def save_experiments(report):
    sys.path.insert(0, str(HERE))
    import yt_db
    start = date.fromisoformat(report["today"])
    end = start + timedelta(days=30)
    for experiment in report["experiments"]:
        yt_db.save_experiment({
            "ts": datetime.now().isoformat(timespec="seconds"),
            "channel": report["channel"],
            "video_id": experiment.get("video_tag"),
            "scope": experiment.get("scope"),
            "variable": f"{experiment.get('scope')}:{experiment.get('variable')}",
            "hypothesis": experiment.get("hypothesis"),
            "baseline": experiment.get("baseline"),
            "target": experiment.get("target"),
            "start_date": start.isoformat(),
            "end_date": end.isoformat(),
            "status": "proposto",
            "evidence": experiment.get("measurement"),
            "decision": "",
        })


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--channel", default="cold-file-diaries")
    parser.add_argument("--project")
    parser.add_argument("--today", default=date.today().isoformat())
    parser.add_argument("--json", action="store_true", dest="as_json")
    parser.add_argument("--save-experiments", action="store_true")
    args = parser.parse_args()
    report = build_report(args.channel, args.project, args.today)
    if args.save_experiments:
        save_experiments(report)
    if args.as_json:
        print(json.dumps(report, ensure_ascii=False, indent=2, default=str))
    else:
        print(render_markdown(report))
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    sys.exit(main())
