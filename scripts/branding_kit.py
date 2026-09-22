#!/usr/bin/env python3
"""branding_kit.py — gera o KIT DE BRANDING de um canal do zero (arquivos reais, não só brief).

Gera em <out>/ (default: <canal>/00_CANAL/assets/branding):
  logo.png        512x512   icone (monograma + paleta)
  profile.png     800x800   foto de perfil (conteudo no circulo seguro)
  banner.png      2560x1440 banner limpo (texto na safe area 1235x338)
  banner_guia.png 2560x1440 banner com guias da safe area (referencia, nao subir)
  watermark.png   150x150   marca d'agua (RGBA)
  palette.json              cores/fontes/arquivos (contrato do branding)
  BRANDING.md               spec de uso (paleta, fontes, tamanhos, do/don't)

Uso:
  python scripts/branding_kit.py --name "Cold File Diaries" --handle ColdFileDiaries \
      --tagline "Unsolved cold cases, retold calmly." --sub "True Crime Files" \
      --palette "#0A0A0C,#B91C1C,#F5F5F4,#8A8A93" \
      --out "<canal>/00_CANAL/assets/branding"

Fonte: --font <arquivo.ttf> (ex.: BebasNeue.ttf). Sem --font, tenta Bebas Neue local,
Arial Bold (Windows) e DejaVuSans; ultimo recurso: fonte default do PIL.
"""
import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

SAFE_W, SAFE_H = 1235, 338  # safe area oficial do banner (desktop/TV) em 2560x1440


def hex2rgb(h):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def load_font(path, size):
    cands = []
    if path:
        cands.append(path)
    cands += [
        str(Path(__file__).resolve().parent.parent / "assets" / "fonts" / "BebasNeue.ttf"),
        "C:/Windows/Fonts/arialbd.ttf",
        "C:/Windows/Fonts/arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    ]
    for c in cands:
        try:
            return ImageFont.truetype(c, size)
        except (OSError, TypeError):
            continue
    return ImageFont.load_default()


def initials_of(name):
    words = [w for w in name.replace("-", " ").split() if w.lower() not in ("the", "a", "o", "de", "da")]
    if not words:
        words = name.split() or ["C"]
    return "".join(w[0].upper() for w in words[:3])[:3]


def text_w(draw, txt, font):
    try:
        return draw.textlength(txt, font=font)
    except Exception:
        return len(txt) * font.size * 0.55


def fit(draw, txt, font_path, size, min_size, max_w):
    while size > min_size:
        f = load_font(font_path, size)
        if text_w(draw, txt, f) <= max_w:
            return f, size
        size -= 4
    return load_font(font_path, min_size), min_size


def center(draw, box, txt, font, fill, stroke=0, stroke_fill=(0, 0, 0)):
    x0, y0, x1, y1 = box
    w = text_w(draw, txt, font)
    try:
        asc, desc = font.getmetrics()
        h = asc + desc
    except Exception:
        h = getattr(font, "size", 40)
    draw.text((x0 + (x1 - x0 - w) / 2, y0 + (y1 - y0 - h) / 2), txt, font=font, fill=fill,
              stroke_width=stroke, stroke_fill=stroke_fill)


def bg_plate(w, h, bg, accent, vignette=True):
    img = Image.new("RGB", (w, h), bg)
    d = ImageDraw.Draw(img)
    d.rectangle([0, h - 10, w, h], fill=accent)
    if vignette:
        small = Image.new("L", (64, 36), 0)
        px = small.load()
        cx, cy = 32, 18
        maxd = (cx ** 2 + cy ** 2) ** 0.5
        for yy in range(36):
            for xx in range(64):
                dd = ((xx - cx) ** 2 + (yy - cy) ** 2) ** 0.5 / maxd
                px[xx, yy] = int(max(0, dd - 0.5) * 200)
        img = Image.composite(Image.new("RGB", (w, h), (0, 0, 0)), img, small.resize((w, h)))
    return img


def gen_logo(out, name, accent, text, bg, font_path):
    S = 512
    img = bg_plate(S, S, bg, accent, vignette=False)
    d = ImageDraw.Draw(img)
    d.rectangle([18, 18, S - 18, S - 18], outline=accent, width=6)
    ini = initials_of(name)
    f, _ = fit(d, ini, font_path, 260, 120, S - 140)
    center(d, (0, 40, S, S - 70), ini, f, text)
    fh = load_font(font_path, 34)
    center(d, (0, S - 120, S, S - 60), name.upper()[:22], fh, accent)
    p = out / "logo.png"
    img.save(p, quality=95)
    return p


def gen_profile(logo_path, out):
    S = 800
    img = Image.new("RGB", (S, S), (10, 10, 12))
    lg = Image.open(logo_path).convert("RGB")
    lg = lg.resize((int(S * 0.78), int(S * 0.78)), Image.LANCZOS)
    img.paste(lg, ((S - lg.width) // 2, (S - lg.height) // 2))
    p = out / "profile.png"
    img.save(p, quality=95)
    return p


def gen_banner(out, name, handle, tagline, sub, accent, text, muted, bg, font_path, guides=False):
    W, H = 2560, 1440
    img = bg_plate(W, H, bg, accent)
    d = ImageDraw.Draw(img)
    # faixa de acento atras da safe area
    y0 = (H - SAFE_H) // 2
    d.rectangle([0, y0 - 20, W, y0 - 12], fill=accent)
    box = ((W - SAFE_W) // 2, y0, (W + SAFE_W) // 2, y0 + SAFE_H)
    f_name, _ = fit(d, name, font_path, 190, 90, SAFE_W - 60)
    center(d, (box[0], box[1] + 20, box[2], box[1] + 210), name, f_name, text)
    f_sub = load_font(font_path, 62)
    center(d, (box[0], box[1] + 200, box[2], box[1] + 270), (sub or "").upper(), f_sub, accent)
    f_tag = load_font(font_path, 46)
    center(d, (box[0], box[1] + 275, box[2], box[3] - 8), tagline or "", f_tag, muted)
    f_h = load_font(font_path, 40)
    d.text((box[0], box[3] + 26), f"youtube.com/@{handle}", font=f_h, fill=muted)
    if guides:
        d.rectangle(box, outline=(255, 255, 0), width=4)
        d.rectangle([0, 0, W - 1, H - 1], outline=(255, 0, 0), width=4)
    p = out / ("banner_guia.png" if guides else "banner.png")
    img.save(p, quality=95)
    return p


def gen_watermark(out, name, accent, text):
    S = 150
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.ellipse([4, 4, S - 4, S - 4], fill=(0, 0, 0, 190), outline=accent + (255,), width=5)
    ini = initials_of(name)
    f, _ = fit(d, ini, None, 64, 28, S - 40)
    center(d, (0, 0, S, S), ini, f, text + (255,))
    p = out / "watermark.png"
    img.save(p)
    return p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    ap.add_argument("--handle", default="")
    ap.add_argument("--tagline", default="")
    ap.add_argument("--sub", default="")
    ap.add_argument("--palette", default="#0A0A0C,#B91C1C,#F5F5F4,#8A8A93",
                    help="bg,accent,text,muted (hex separados por virgula)")
    ap.add_argument("--font", default="")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    cols = [hex2rgb(c) for c in a.palette.split(",")]
    while len(cols) < 4:
        cols.append(cols[-1])
    bg, accent, text, muted = cols[:4]

    out = Path(a.out).expanduser()
    out.mkdir(parents=True, exist_ok=True)

    logo = gen_logo(out, a.name, accent, text, bg, a.font)
    gen_profile(logo, out)
    gen_banner(out, a.name, a.handle or a.name, a.tagline, a.sub, accent, text, muted, bg, a.font, guides=False)
    gen_banner(out, a.name, a.handle or a.name, a.tagline, a.sub, accent, text, muted, bg, a.font, guides=True)
    gen_watermark(out, a.name, accent, text)

    (out / "palette.json").write_text(json.dumps({
        "name": a.name, "handle": a.handle, "tagline": a.tagline, "sub": a.sub,
        "colors": {"bg": a.palette.split(",")[0].strip(), "accent": a.palette.split(",")[1].strip(),
                   "text": a.palette.split(",")[2].strip(), "muted": a.palette.split(",")[3].strip()},
        "font": a.font or "(fallback do sistema)",
        "files": ["logo.png", "profile.png", "banner.png", "banner_guia.png", "watermark.png"],
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    md = f"""# BRANDING — {a.name}

> Gerado por `scripts/branding_kit.py`. Contrato de branding do canal (arquivos reais em `00_CANAL/assets/branding/`).

## Identidade
- **Nome:** {a.name}
- **Handle:** @{a.handle or a.name}
- **Tagline:** {a.tagline or "(definir)"}
- **Assinatura/série:** {a.sub or "(definir)"}

## Paleta (travada)
| Papel | Hex |
|---|---|
| Fundo | {a.palette.split(",")[0].strip()} |
| Acento | {a.palette.split(",")[1].strip()} |
| Texto | {a.palette.split(",")[2].strip()} |
| Detalhe/muted | {a.palette.split(",")[3].strip()} |

## Fontes
- Thumbs/títulos: {a.font or "Bebas Neue / Oswald Bold (definir caminho com --font)"}
- Regra: 1 fonte para título + 1 peso; no máximo 3–5 palavras na thumb.

## Arquivos e onde usar
| Arquivo | Tamanho | Uso |
|---|---|---|
| `logo.png` | 512×512 | fonte do logo (não subir direto) |
| `profile.png` | 800×800 | foto do canal (conteúdo no círculo seguro) |
| `banner.png` | 2560×1440 | banner do canal (texto na safe area {SAFE_W}×{SAFE_H}) |
| `banner_guia.png` | 2560×1440 | só referência (guias amarelas = safe area) — NÃO subir |
| `watermark.png` | 150×150 | marca d'água de vídeo |

## Do / Don't
- **Do:** mesma paleta em tudo; texto dentro da safe area; 1 elemento de mistério na thumb.
- **Don't:** rosto real, gore, >5 palavras na thumb, vermelho/branco/preto puros, nada no canto inferior direito (duração do YT).
- Canal novo ≠ clone: este kit é **deste** canal — não copie para outro sem trocar nome/paleta/fonte.
"""
    (out / "BRANDING.md").write_text(md, encoding="utf-8")

    print(f"[OK] branding em: {out}")
    for f in sorted(out.iterdir()):
        print("   ", f.name)


if __name__ == "__main__":
    main()
