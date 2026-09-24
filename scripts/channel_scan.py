#!/usr/bin/env python3
"""channel_scan.py — estado real, calendário, estoque e corrente de teasers."""
import argparse
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

VIDEO_RE = re.compile(r"^(?:video|ep|episode)[ _-]?(\d+)$", re.IGNORECASE)
SERIES_HINT = (
    "SMALL TOWN SECRETS",
    "KILLERS UNKNOWN",
    "HEISTS & LIES",
    "VANISHED",
    "HEIST/KILLER",
    "SMALL TOWN",
    "HEISTS",
    "KILLERS",
    "HEIST",
)


def find_calendar(root):
    candidates = list(root.rglob("CALENDARIO*.txt")) + list(root.rglob("calendar*.txt")) \
        + list(root.rglob("CALENDARIO*"))
    return next((p for p in candidates if p.is_file()), None)


def find_project_root(path):
    root = Path(path).expanduser().resolve()
    if root.is_file():
        root = root.parent
    return root


def calendar_year(calendar):
    if not calendar:
        return date.today().year
    text = calendar.read_text(encoding="utf-8", errors="replace")
    years = [int(value) for value in re.findall(r"\b(20\d{2})\b", text)]
    return max(years) if years else date.today().year


def parse_calendar(calendar):
    if not calendar:
        return []
    text = calendar.read_text(encoding="utf-8", errors="replace")
    year = calendar_year(calendar)
    rows = []
    for line in text.splitlines():
        match = re.match(r"^D(\d+)\s+(\d{2}/\d{2})(?:\s+\S+)?\s+((?:video|ep)\S*)\s+(.+)$", line.strip(), re.IGNORECASE)
        if not match:
            continue
        before, separator, status = line.partition("|")
        tail = match.group(4)
        upper = tail.upper()
        candidates = [(upper.rfind(series), series) for series in SERIES_HINT if upper.rfind(series) >= 0]
        if candidates:
            position, series = max(candidates, key=lambda item: item[0])
            case_name = tail[:position].strip()
        else:
            series = ""
            case_name = tail.strip()
        day, day_month, tag = match.group(1), match.group(2), match.group(3)
        try:
            scheduled = datetime.strptime(f"{day_month}/{year}", "%d/%m/%Y").date()
        except ValueError:
            continue
        rows.append({
            "day": f"D{day}",
            "date": scheduled.isoformat(),
            "weekday": before.split()[2] if len(before.split()) > 2 else "",
            "video_tag": tag,
            "case_name": case_name,
            "series": series,
            "status": status.strip() if separator else "",
        })
    return sorted(rows, key=lambda row: row["date"])


def video_dirs(root):
    output = []
    for path in root.iterdir():
        if not path.is_dir() or not VIDEO_RE.fullmatch(path.name):
            continue
        output.append(path)
    return sorted(output, key=lambda path: int(VIDEO_RE.fullmatch(path.name).group(1)))


def package_info(vdir):
    package = vdir / "youtube_package.txt"
    if not package.exists():
        return {"case_name": "", "series": "", "long_title": "", "short_title": "", "pending": True}
    text = package.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    case_name = ""
    series = ""
    long_title = ""
    short_title = ""
    for line in lines:
        stripped = line.strip()
        if stripped.upper().startswith("CASO:") and not case_name:
            case_name = re.split(r"\s*\|\s*", stripped.split(":", 1)[1].strip())[0]
        if stripped.upper().startswith("SERIE:") and not series:
            series = stripped.split(":", 1)[1].split("|", 1)[0].strip()
        if re.match(r"^TITLE:\s*\S", stripped, re.IGNORECASE) and not long_title:
            long_title = stripped.split(":", 1)[1].strip()
    short_section = re.search(r"(?ms)^SHORT\b.*?\Z", text)
    if short_section:
        match = re.search(r"(?mi)^TITLE \(copiar\):\s*(.+)$", short_section.group(0))
        if not match:
            match = re.search(r"(?mi)^TITLE:\s*(.+)$", short_section.group(0))
        if match:
            short_title = match.group(1).strip()
    if not long_title:
        match = re.search(r"(?mi)^TITLE[^\n]*\n\s*1\.\s*(.+)$", text)
        if match:
            long_title = match.group(1).strip()
    return {
        "case_name": case_name,
        "series": series,
        "long_title": long_title,
        "short_title": short_title,
        "pending": any("PENDENTE" in line.upper() for line in lines),
    }


def expected_images(package_text):
    matches = re.findall(r"(?i)(\d+)\s+imgs", package_text)
    return int(matches[-1]) if matches else None


def research_contract(vdir):
    script_dir = vdir / "01_roteiro"
    brief = script_dir / "PESQUISA_BRIEF.md"
    source = script_dir / "PESQUISA_FONTE.md"
    claims = script_dir / "CLAIMS.json"
    timeline = script_dir / "LINHA_DO_TEMPO.md"
    result = {"ready": False, "legacy": False, "brief": False, "sources": False, "claims": False, "timeline": False}
    brief_text = brief.read_text(encoding="utf-8", errors="replace") if brief.exists() else ""
    source_text = source.read_text(encoding="utf-8", errors="replace") if source.exists() else ""
    result["brief"] = len(brief_text.strip()) > 120
    result["sources"] = len(source_text.strip()) > 120
    try:
        data = json.loads(claims.read_text(encoding="utf-8"))
        items = data.get("claims", []) if isinstance(data, dict) else []
        result["claims"] = bool(items) and all(
            isinstance(item, dict)
            and item.get("id")
            and item.get("text")
            and item.get("layer")
            and (item.get("layer") in {"LENDA", "HIPOTESE"} or item.get("source_ids"))
            for item in items
        )
    except (OSError, ValueError, AttributeError):
        result["claims"] = False
    result["timeline"] = timeline.exists() and len([
        line for line in timeline.read_text(encoding="utf-8", errors="replace").splitlines()
        if line.strip().startswith("|") and "preencher" not in line.lower()
    ]) >= 3
    legacy_candidate = (
        not brief.exists()
        and not claims.exists()
        and result["sources"]
        and "Uma camada por linha" not in source_text
        and "preencher" not in source_text.lower()
    )
    result["legacy"] = legacy_candidate
    result["ready"] = all(result[key] for key in ("brief", "sources", "claims", "timeline")) or legacy_candidate
    return result


def strict_state(vdir):
    final_dir = vdir / "04_video_final"
    audio_dir = vdir / "02_audio"
    image_dir = vdir / "03_imagens"
    package = package_info(vdir)
    narration_files = list((vdir / "01_roteiro").glob("narration*.txt")) if (vdir / "01_roteiro").exists() else []
    research_files = []
    for name in ("PESQUISA_FONTE.md", "PESQUISA_BRIEF.md", "CLAIMS.json", "case-brief.md", "TRADUCAO_PT.txt"):
        research_files.extend((vdir / "01_roteiro").rglob(name))
    research_contract_state = research_contract(vdir)
    image_files = [p for p in image_dir.rglob("*") if p.is_file() and p.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}] \
        if image_dir.exists() else []
    thumbs = [p for p in final_dir.glob("thumb*.png")] + [p for p in final_dir.glob("thumb*.jpg")] \
        if final_dir.exists() else []
    package_path = vdir / "youtube_package.txt"
    package_text = package_path.read_text(encoding="utf-8", errors="replace") if package_path.exists() else ""
    images_expected = expected_images(package_text)
    narration = bool(narration_files)
    research = research_contract_state["ready"]
    audio = (audio_dir / "voice_FINAL.wav").exists() or (audio_dir / "voice_V3_FINAL.wav").exists()
    captions = (audio_dir / "captions.srt").exists()
    long_video = (final_dir / f"{vdir.name}_YOUTUBE.mp4").exists() or (final_dir / f"{vdir.name}_FINAL.mp4").exists()
    short_video = (final_dir / f"{vdir.name}_SHORT.mp4").exists()
    thumbs_ready = len({p.name for p in thumbs}) >= 3
    package_ready = package_path.exists() and not package["pending"] and bool(package["long_title"])
    images_ready = bool(image_files) and (images_expected is None or len(image_files) >= images_expected)
    core_ready = narration and research and audio and captions and long_video and short_video and thumbs_ready and package_ready and images_ready
    if core_ready:
        stage = "pronto"
    elif long_video and short_video and package_ready:
        stage = "validar_acessorios"
    elif long_video:
        stage = "montagem"
    elif audio:
        stage = "imagens"
    elif image_files:
        stage = "roteiro"
    elif narration:
        stage = "roteiro"
    else:
        stage = "backlog"
    return {
        "roteiro": narration,
        "pesquisa": research,
        "research_contract": research_contract_state,
        "imagens": images_ready,
        "image_count": len(image_files),
        "images_expected": images_expected,
        "audio": audio,
        "captions": captions,
        "long": long_video,
        "short": short_video,
        "thumbs": thumbs_ready,
        "thumb_count": len({p.name for p in thumbs}),
        "pacote": package_ready,
        "ready": core_ready,
        "stage": stage,
        "case_name": package["case_name"],
        "series": package["series"],
        "long_title": package["long_title"],
        "short_title": package["short_title"],
    }


def narration_text(vdir):
    script_dir = vdir / "01_roteiro"
    if not script_dir.exists():
        return ""
    preferred = script_dir / "narration_v3.txt"
    files = [preferred] if preferred.exists() else sorted(script_dir.glob("narration*.txt"))
    for path in files:
        if path.exists():
            return path.read_text(encoding="utf-8", errors="replace")
    return ""


def teaser_line(vdir):
    text = narration_text(vdir)
    if not text:
        return ""
    tail = text[-1600:]
    match = re.search(r"([^\n]*(?:tomorrow|next case|next file|coming next|full file)[^\n]*)", tail, re.IGNORECASE)
    return re.sub(r"\s+", " ", match.group(1)).strip()[:260] if match else ""


def normalize(value):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", value.lower())).strip()


def mentions_case(text, case_name):
    haystack = normalize(text)
    needle = normalize(case_name)
    if not haystack or not needle:
        return False
    if needle in haystack:
        return True
    tokens = [token for token in needle.split() if len(token) > 2 and token not in {"the", "case", "murder", "murders"}]
    if len(tokens) >= 2 and " ".join(tokens[:2]) in haystack:
        return True
    return any(token in haystack for token in tokens if len(token) >= 4)


def build_context(root, today=None):
    root = find_project_root(root)
    today = today or date.today().isoformat()
    calendar_path = find_calendar(root)
    calendar_rows = parse_calendar(calendar_path)
    by_tag = {row["video_tag"]: row for row in calendar_rows}
    videos = []
    for vdir in video_dirs(root):
        state = strict_state(vdir)
        calendar_row = by_tag.get(vdir.name, {})
        videos.append({
            **state,
            "video_tag": vdir.name,
            "path": str(vdir),
            "date": calendar_row.get("date", ""),
            "case_name": calendar_row.get("case_name") or state["case_name"],
            "series": calendar_row.get("series") or state["series"],
            "calendar_status": calendar_row.get("status", ""),
        })
    videos_by_tag = {video["video_tag"]: video for video in videos}
    calendar = []
    for row in calendar_rows:
        video = videos_by_tag.get(row["video_tag"])
        calendar.append({**row, "state": video["stage"] if video else "ausente", "ready": video["ready"] if video else False})
    chain = []
    for current, following in zip(calendar, calendar[1:]):
        video = videos_by_tag.get(current["video_tag"])
        text = narration_text(Path(video["path"])) if video else ""
        chain.append({
            "from": current["video_tag"],
            "to": following["video_tag"],
            "expected_case": following["case_name"],
            "ok": mentions_case(text[-1600:], following["case_name"]),
            "tease": teaser_line(Path(video["path"])) if video else "",
        })
    future = [row for row in calendar if row["date"] >= today]
    upcoming = future[:7]
    current = next((row for row in calendar if row["date"] == today), None)
    next_produce = next((row for row in future if not row["ready"]), None)
    return {
        "project": str(root),
        "today": today,
        "calendar_file": str(calendar_path) if calendar_path else "",
        "calendar": calendar,
        "today_video": current,
        "upcoming": upcoming,
        "next_to_produce": next_produce,
        "ready_stock": len([row for row in future if row["ready"]]),
        "chain": chain,
        "videos": videos,
        "quality": {
            "calendar_entries": len(calendar),
            "regular_video_folders": len(videos),
            "ready_total": len([video for video in videos if video["ready"]]),
            "chain_ok": len([row for row in chain if row["ok"]]),
            "chain_total": len(chain),
        },
    }


def render_text(context):
    lines = [
        f"# Contexto do canal\n\nProjeto: {context['project']}\nData: {context['today']}",
        f"Calendário: {context['calendar_file'] or 'NAO ENCONTRADO'}",
        f"Estoque futuro pronto: {context['ready_stock']}",
    ]
    current = context.get("today_video")
    upcoming = context.get("upcoming") or []
    if current:
        lines.append(f"Vídeo do dia: {current['video_tag']} — {current['case_name']} — {current['state']}")
    if upcoming:
        lines.append("Próximos:")
        for row in upcoming:
            lines.append(f"  {row['date']} {row['video_tag']} {row['case_name']} [{row['state']}]")
    nxt = context.get("next_to_produce")
    if nxt:
        lines.append(f"Próximo a produzir: {nxt['video_tag']} — {nxt['case_name']}")
    lines.append("\nEstado dos vídeos:\n")
    lines.append(f"{'video':<10} {'data':<10} {'estado':<20} {'long':<5} {'short':<5} {'imgs':<8} {'thumbs':<7} {'pacote':<7}")
    for video in context["videos"]:
        images = f"{video['image_count']}/{video['images_expected']}" if video["images_expected"] else str(video["image_count"])
        lines.append(f"{video['video_tag']:<10} {video['date'] or '-':<10} {video['stage']:<20} "
                     f"{'ok' if video['long'] else '-':<5} {'ok' if video['short'] else '-':<5} "
                     f"{images:<8} {video['thumb_count']:<7} {'ok' if video['pacote'] else '-':<7}")
    lines.append("\nCorrente de teasers:")
    for row in context["chain"]:
        lines.append(f"  {row['from']} -> {row['to']} {row['expected_case']}: {'OK' if row['ok'] else 'REVISAR'}")
    quality = context["quality"]
    lines.append(f"\nResumo: {quality['ready_total']} prontos | corrente {quality['chain_ok']}/{quality['chain_total']} íntegra")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?")
    parser.add_argument("--channel", dest="channel")
    parser.add_argument("--today")
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()
    source = args.channel or args.path or "."
    root = find_project_root(source)
    if not root.exists():
        print(f"[!] caminho não existe: {root}")
        return 1
    context = build_context(root, args.today)
    if args.as_json:
        print(json.dumps(context, ensure_ascii=False, indent=2))
    else:
        print(render_text(context))
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    sys.exit(main())
