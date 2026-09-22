#!/usr/bin/env python3
"""image_audit.py — audita as imagens geradas de um vídeo/canal.

Uso:
  python scripts/image_audit.py "<pasta de imagens>" [opcoes]
  python scripts/image_audit.py "<canal>/video22/03_imagens" --sheet --hash

O que checa (por imagem):
  - resolucao (largura minima)
  - aspecto (16:9 por padrao, tolerancia)
  - tamanho de arquivo (KB minimo)
  - brilho medio e desvio (detecta imagem quase solida / geracao falhada)
  - saturacao media
  - duplicatas proximas (average hash)

Gera: relatorio no terminal, `AUDITORIA_IMAGENS.md` e (com --sheet) `_contact_sheet.jpg`.
Exit code 1 se houver falhas.
"""
import argparse
import sys
from pathlib import Path

try:
    import numpy as np
    from PIL import Image, ImageDraw
except ImportError:
    print("Instale: python -m pip install pillow numpy")
    sys.exit(2)

EXTS = {".jpg", ".jpeg", ".png", ".webp"}


def ahash(img, size=8):
    g = img.convert("L").resize((size, size), Image.LANCZOS)
    a = np.asarray(g, dtype=np.float32)
    return (a > a.mean()).flatten()


def hamming(a, b):
    return int(np.count_nonzero(a != b))


def analyze(path, min_width, aspect, min_kb, tol):
    flags = []
    try:
        img = Image.open(path)
        img.load()
    except Exception as e:  # noqa
        return {"path": path, "error": str(e), "flags": ["ilegivel"]}, None
    w, h = img.size
    kb = path.stat().st_size / 1024.0
    ar = (w / h) if h else 0
    small = img.convert("RGB").resize((160, 90), Image.LANCZOS)
    arr = np.asarray(small, dtype=np.float32)
    bright = float(arr.mean())
    std = float(arr.std())
    # saturacao (max-min por pixel)
    sat = float((arr.max(axis=2) - arr.min(axis=2)).mean())

    if w < min_width:
        flags.append(f"baixa_res({w}px)")
    if abs(ar - aspect) > tol:
        flags.append(f"aspecto({ar:.2f})")
    if kb < min_kb:
        flags.append(f"pequena({kb:.0f}kb)")
    if std < 12:
        flags.append("quase_solida")
    if bright < 18:
        flags.append("muito_escura")
    elif bright > 240:
        flags.append("muito_clara")

    return ({"path": path, "w": w, "h": h, "kb": round(kb), "ar": round(ar, 3),
             "bright": round(bright), "std": round(std), "sat": round(sat),
             "flags": flags}, ahash(img))


def contact_sheet(images, out, cols=6, cell=320):
    if not images:
        return
    rows = (len(images) + cols - 1) // cols
    W, H = cols * cell, rows * cell
    sheet = Image.new("RGB", (W, H), (10, 10, 12))
    d = ImageDraw.Draw(sheet)
    for i, p in enumerate(images):
        try:
            im = Image.open(p).convert("RGB")
        except Exception:  # noqa
            continue
        im.thumbnail((cell - 8, cell - 28), Image.LANCZOS)
        x = (i % cols) * cell + (cell - im.width) // 2
        y = (i // cols) * cell + 4
        sheet.paste(im, (x, y))
        d.text(((i % cols) * cell + 6, (i // cols) * cell + cell - 20),
               p.name, fill=(200, 200, 200))
    sheet.save(out, quality=82)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--min-width", type=int, default=1280)
    ap.add_argument("--aspect", type=float, default=16 / 9)
    ap.add_argument("--tol", type=float, default=0.06)
    ap.add_argument("--min-kb", type=int, default=50)
    ap.add_argument("--sheet", action="store_true", help="gera _contact_sheet.jpg")
    ap.add_argument("--hash", action="store_true", help="detecta duplicatas proximas")
    a = ap.parse_args()

    root = Path(a.path).expanduser()
    if not root.exists():
        print(f"[!] pasta nao existe: {root}")
        sys.exit(2)
    files = sorted([p for p in root.rglob("*") if p.suffix.lower() in EXTS and not p.name.startswith("_")])
    if not files:
        print("Nenhuma imagem encontrada.")
        sys.exit(2)

    print(f"# Auditoria de imagens — {root}\n({len(files)} imagens)\n")
    results, hashes, fails = [], [], 0
    for p in files:
        r, hh = analyze(p, a.min_width, a.aspect, a.min_kb, a.tol)
        results.append(r)
        if hh is not None:
            hashes.append((p, hh))
        if r["flags"]:
            fails += 1
        status = "ok" if not r["flags"] else "FALHA"
        extra = "" if "error" in r else f"{r['w']}x{r['h']} {r['kb']}kb brilho{r['bright']} std{r['std']}"
        print(f"  [{status}] {p.name:<34} {extra} {', '.join(r['flags'])}")

    # duplicatas
    dups = []
    if a.hash and len(hashes) > 1:
        for i in range(len(hashes)):
            for j in range(i + 1, len(hashes)):
                if hamming(hashes[i][1], hashes[j][1]) <= 2:
                    dups.append((hashes[i][0].name, hashes[j][0].name))
        print(f"\nDuplicatas proximas: {len(dups)}")
        for x, y in dups[:10]:
            print(f"  ~ {x} == {y}")

    if a.sheet:
        out = root / "_contact_sheet.jpg"
        contact_sheet(files, out)
        print(f"\n[OK] contact sheet: {out}")

    rep = root / "AUDITORIA_IMAGENS.md"
    with rep.open("w", encoding="utf-8") as fh:
        fh.write(f"# Auditoria de imagens\n\nPasta: `{root}`\n\n")
        fh.write(f"- Imagens: {len(files)}\n- Com falha: {fails}\n- Duplicatas: {len(dups)}\n\n")
        for r in results:
            mark = "ok" if not r["flags"] else "FALHA"
            fh.write(f"- [{mark}] `{r['path'].name}` {', '.join(r['flags'])}\n")
    print(f"[OK] relatorio: {rep}")

    print(f"\nRESULTADO: {'PASSOU' if fails == 0 else f'{fails} FALHA(S)'}")
    sys.exit(0 if fails == 0 else 1)


if __name__ == "__main__":
    main()
