#!/usr/bin/env python3
"""thumb_build.py — gera os pixels da thumb a partir do THUMB_BRIEF.json.

Para cada conceito (2-3): fundo (imagem --bg <id=path> ou gradiente do canal)
+ overlay de texto (<=4 palavras, idioma do canal) em 1280x720, com safe areas
(canto inferior-direito livre para o selo de duracao, margem 48px), JPEG <=2MB.
Gera preview 120px + contact sheet, roda thumb_audit por conceito e grava
THUMB_BUILD.json; o vencedor (primeiro PASS, senao primeiro REVIEW) vira o
campo `image` do brief para o gate do audit_all ser honesto.

Uso:
  python scripts/thumb_build.py --brief <video>/01_roteiro/THUMB_BRIEF.json \
      --channel <canal> --titles "Titulo PT | Title EN" [--bg A=bg_a.jpg] [--render-bg]
"""
import argparse
import json
import re
import sys
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from thumb_audit import audit as thumb_audit_fn, audit_image as thumb_audit_image_fn

WIDTH, HEIGHT = 1280, 720
MARGIN = 48
DURATION_BADGE = (320, 180)
MAX_BYTES = 2 * 1024 * 1024


def load_font(path, size):
    from PIL import ImageFont
    candidates = [path] if path else []
    candidates += ["C:/Windows/Fonts/arialbd.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]
    for candidate in candidates:
        try:
            if candidate and Path(candidate).exists():
                return ImageFont.truetype(str(candidate), size)
        except (OSError, ValueError):
            continue
    return ImageFont.load_default()


def channel_style(channel):
    if not channel:
        return {}
    base = Path(__file__).resolve().parent.parent / "playbooks"
    candidate = Path(channel).expanduser()
    root = candidate if candidate.is_dir() else base / channel
    style_file = root / "style.json"
    if not style_file.exists():
        print(f"[AVISO] style.json ausente para '{channel}' - usando defaults neutros.")
        return {}
    try:
        return json.loads(style_file.read_text(encoding="utf-8"))
    except ValueError as exc:
        print(f"[AVISO] style.json invalido ({exc}) - usando defaults neutros.")
        return {}


def overlay_text(concept, language):
    return str(concept.get("text_en" if language == "en" else "text_pt", "") or "")


def fetch_background(prompt, out_path, timeout=120):
    url = ("https://image.pollinations.ai/prompt/" + urllib.parse.quote(prompt)
           + "?width=1280&height=720&nologo=true&model=flux")
    try:
        data = urllib.request.urlopen(url, timeout=timeout).read()
        if len(data) > 10000:
            Path(out_path).write_bytes(data)
            return True
    except Exception as exc:
        print(f"[!] fundo IA indisponivel ({exc}) - usando gradiente do canal.")
    return False


def gradient_background(colors):
    from PIL import Image, ImageDraw
    top = tuple(colors.get("top", [16, 18, 24]))
    bottom = tuple(colors.get("bottom", [5, 5, 8]))
    image = Image.new("RGB", (WIDTH, HEIGHT), top)
    draw = ImageDraw.Draw(image)
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        draw.line([(0, y), (WIDTH, y)],
                  fill=tuple(int(top[i] + (bottom[i] - top[i]) * ratio) for i in range(3)))
    return image


def fit_background(image):
    from PIL import Image
    image = image.convert("RGB")
    scale = max(WIDTH / image.width, HEIGHT / image.height)
    resized = image.resize((int(image.width * scale) + 1, int(image.height * scale) + 1), Image.LANCZOS)
    left = (resized.width - WIDTH) // 2
    top = (resized.height - HEIGHT) // 2
    return resized.crop((left, top, left + WIDTH, top + HEIGHT))


def wrap_overlay(text, font_getter, max_width):
    from PIL import ImageDraw, Image
    words = text.split()
    lines, current = [], ""
    probe = ImageDraw.Draw(Image.new("RGB", (8, 8)))
    for word in words:
        trial = f"{current} {word}".strip()
        if probe.textlength(trial, font=font_getter()) <= max_width or not current:
            current = trial
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines[:3]


def render_concept(concept, style, language, out_path, bg_path=None, render_bg=False, image_suffix=""):
    from PIL import Image, ImageDraw
    thumb = style.get("thumb", {}) if isinstance(style, dict) else {}
    colors = thumb.get("colors", {}) if isinstance(thumb.get("colors"), dict) else {}
    white = tuple(colors.get("white", [245, 245, 244]))
    black = tuple(colors.get("black", [0, 0, 0]))
    accent = tuple(colors.get("accent", colors.get("red", [220, 38, 38])))
    if bg_path and Path(bg_path).exists():
        with Image.open(bg_path) as background:
            canvas = fit_background(background)
    elif render_bg:
        tmp = Path(out_path).parent / f".bg_{concept.get('id', 'x')}.jpg"
        prompt = f"{concept.get('focal', '')}, {concept.get('background', '')}, {image_suffix}, no text, no watermark, 16:9"
        if fetch_background(prompt, tmp):
            with Image.open(tmp) as background:
                canvas = fit_background(background)
        else:
            canvas = gradient_background({"top": list(black), "bottom": [5, 5, 8]})
    else:
        canvas = gradient_background({"top": list(black), "bottom": [5, 5, 8]})
    # Faixa de leitura: terco esquerdo, fora do selo de duracao e das margens.
    text = overlay_text(concept, language)
    max_width = WIDTH - DURATION_BADGE[0] - MARGIN * 3
    size = 200
    while size > 64:
        font = load_font(thumb.get("font"), size)
        if not wrap_overlay(text, lambda: font, max_width):
            break
        lines = wrap_overlay(text, lambda: font, max_width)
        probe = ImageDraw.Draw(canvas)
        heights = [probe.textbbox((0, 0), line, font=font, stroke_width=max(2, size // 24)) for line in lines]
        total = sum(bottom - top for _, top, _, bottom in heights) + (len(lines) - 1) * size // 6
        if total <= HEIGHT - MARGIN * 2 - 120:
            break
        size -= 12
    draw = ImageDraw.Draw(canvas)
    y = MARGIN + 40
    stroke = max(3, size // 22)
    for index, line in enumerate(lines):
        words = line.split()
        x = MARGIN + 20
        for position, word in enumerate(words):
            # Ultima palavra do bloco em destaque (padrao forte de CTR).
            fill = accent if (index == len(lines) - 1 and position == len(words) - 1 and len(words) > 1) else white
            draw.text((x, y), word, font=font, fill=fill, stroke_width=stroke, stroke_fill=black)
            x += draw.textlength(word + " ", font=font)
        box = draw.textbbox((0, 0), line, font=font, stroke_width=stroke)
        y += (box[3] - box[1]) + size // 6
    quality = 90
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    while quality >= 60:
        canvas.save(out_path, "JPEG", quality=quality)
        if Path(out_path).stat().st_size <= MAX_BYTES:
            break
        quality -= 8
    return {"path": str(out_path), "bytes": Path(out_path).stat().st_size, "quality": quality}


def preview_120(image_path, out_path):
    from PIL import Image
    with Image.open(image_path) as image:
        small = image.convert("RGB").resize((120, 68), Image.LANCZOS)
        Path(out_path).parent.mkdir(parents=True, exist_ok=True)
        small.save(out_path, "JPEG", quality=85)
    return str(out_path)


def contact_sheet(images, out_path):
    from PIL import Image
    cells = []
    for path in images:
        with Image.open(path) as image:
            thumb = image.convert("RGB")
            thumb.thumbnail((400, 225), Image.LANCZOS)
            cells.append(thumb.copy())
    sheet = Image.new("RGB", (400 * len(cells), 225), (10, 10, 12))
    for index, cell in enumerate(cells):
        sheet.paste(cell, (index * 400, 0))
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out_path, "JPEG", quality=88)
    return str(out_path)


def build(brief_path, channel=None, titles="", outdir=None, bg_map=None, render_bg=False):
    brief_path = Path(brief_path)
    brief = json.loads(brief_path.read_text(encoding="utf-8"))
    style = channel_style(channel)
    language = style.get("language", "pt") if isinstance(style, dict) else "pt"
    language = "en" if str(language).lower().startswith("en") else "pt"
    title_list = [part.strip() for part in re.split(r"\|", titles) if part.strip()]
    episode_root = brief_path.parent.parent
    final_dir = Path(outdir) if outdir else episode_root / "04_video_final"
    final_dir.mkdir(parents=True, exist_ok=True)
    image_suffix = style.get("image_suffix", "") if isinstance(style, dict) else ""
    structural = thumb_audit_fn(brief, title_list, brief_path.parent)
    results = []
    for concept in brief.get("concepts", []):
        cid = str(concept.get("id", "x"))
        image_path = final_dir / f"thumb_{cid}.jpg"
        bg_path = (bg_map or {}).get(cid)
        meta = render_concept(concept, style, language, image_path, bg_path, render_bg, image_suffix)
        preview = preview_120(image_path, final_dir / f"thumb_{cid}_120.jpg")
        image_result, image_errors, image_warnings = thumb_audit_image_fn(image_path.name, final_dir)
        concept_errors = [e for e in structural["errors"]
                          if e.startswith(f"{cid}:") or e.startswith("conceitos_") or e.startswith("imagem_")]
        concept_warnings = [w for w in structural["warnings"] if w.startswith(f"{cid}:")]
        errors = concept_errors + image_errors
        warnings = concept_warnings + image_warnings
        status = "FAIL" if errors or image_result.get("status") == "FAIL" else ("REVIEW" if warnings else "PASS")
        results.append({"id": cid, "image": image_path.name, "preview": Path(preview).name,
                        "bytes": meta["bytes"], "audit": status,
                        "errors": errors, "warnings": warnings})
    sheet = contact_sheet([final_dir / item["image"] for item in results], final_dir / "thumb_contact_sheet.jpg") if results else ""
    order = {"PASS": 0, "REVIEW": 1, "FAIL": 2}
    winner = min(results, key=lambda item: (order.get(item["audit"], 3), item["id"])) if results else None
    build_report = {"status": winner["audit"] if winner else "FAIL", "winner": winner["id"] if winner else None,
                    "concepts": results, "contact_sheet": Path(sheet).name if sheet else ""}
    (final_dir / "THUMB_BUILD.json").write_text(json.dumps(build_report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if winner:
        brief["image"] = f"../04_video_final/{winner['image']}"
        brief_path.write_text(json.dumps(brief, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return build_report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--brief", required=True)
    parser.add_argument("--channel", default=None)
    parser.add_argument("--titles", default="")
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--bg", action="append", default=[],
                        help="fundo por conceito: --bg A=path.jpg (repetir por variante)")
    parser.add_argument("--render-bg", action="store_true", help="gera fundo via IA (rede; fallback gradiente)")
    args = parser.parse_args()
    bg_map = {}
    for item in args.bg:
        if "=" in item:
            key, value = item.split("=", 1)
            bg_map[key.strip()] = value.strip()
    report = build(args.brief, args.channel, args.titles, args.outdir, bg_map, args.render_bg)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] in {"PASS", "REVIEW"} else 1


if __name__ == "__main__":
    sys.exit(main())
