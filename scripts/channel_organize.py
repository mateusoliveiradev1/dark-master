#!/usr/bin/env python3
"""channel_organize.py — organiza a pasta de um canal (dry-run por padrão).

Uso:
  python scripts/channel_organize.py "<pasta do canal>"                 # relatório (nao move nada)
  python scripts/channel_organize.py "<pasta do canal>" --apply         # aplica a organizacao
  python scripts/channel_organize.py "<pasta do canal>" --apply --archive # move backups/caches

Seguranca:
  - por padrao NAO move nada (dry-run);
  - nunca apaga; --archive so move para 99_ARCHIVE/;
  - nao sobrescreve: se o destino existir, renomeia com _dup1, _dup2...

Regras de classificacao por tipo em cada videoNN/:
  video (.mp4/.mov/.mkv/.webm)            -> 04_video_final/
  audio/legenda (.wav/.mp3/.m4a/.aac/.srt/.vtt/.ass) -> 02_audio/
  imagem (.jpg/.jpeg/.png/.webp)          -> 03_imagens/
  roteiro (.txt/.md de roteiro)           -> 01_roteiro/
  pacote (youtube_package/PACOTE_*)       -> raiz do videoNN/
  script (.py)                            -> scripts/
  backup (.bak*)                          -> 99_ARCHIVE/backups/
"""
import argparse
import re
import shutil
from datetime import datetime
from pathlib import Path

VIDEO_RE = re.compile(r"^(video|ep|episode)[ _-]?\d+", re.IGNORECASE)
VIDEO_SUBS = ["01_roteiro", "02_audio", "03_imagens", "04_video_final"]

RULES = [
    (("04_video_final",), {".mp4", ".mov", ".mkv", ".webm", ".avi", ".m4v"}),
    (("02_audio",), {".wav", ".mp3", ".m4a", ".aac", ".flac", ".ogg", ".srt", ".vtt", ".ass"}),
    (("03_imagens",), {".jpg", ".jpeg", ".png", ".webp", ".gif"}),
    (("01_roteiro",), {".txt", ".md"}),
]
PACKAGE_HINTS = ("youtube_package", "pacote_publicacao", "pacote_publicação")
SCRIPT_EXT = {".py", ".js", ".mjs", ".ts"}
ARCHIVE_EXT = {".bak", ".tmp", ".old", ".pyc", ".log"}
CACHE_DIRS = {"__pycache__", "_parts", "_parts_forense", "_outro_tmp", ".cache", ".venv", ".venv-xtts"}


def is_video_dir(p: Path) -> bool:
    return p.is_dir() and bool(VIDEO_RE.match(p.name))


def ensure_subs(vdir: Path, plan, apply):
    for s in VIDEO_SUBS:
        d = vdir / s
        if not d.exists():
            plan.append(("mkdir", d, d))
            if apply:
                d.mkdir(parents=True, exist_ok=True)


def unique_dest(dest: Path) -> Path:
    if not dest.exists():
        return dest
    stem, suf, i = dest.stem, dest.suffix, 1
    while True:
        cand = dest.with_name(f"{stem}_dup{i}{suf}")
        if not cand.exists():
            return cand
        i += 1


def classify(name: str, ext: str, vdir: Path):
    low = name.lower()
    for hints in PACKAGE_HINTS:
        if hints in low:
            return vdir
    if ext in SCRIPT_EXT:
        return "scripts"
    if ext in ARCHIVE_EXT or ".bak_" in low:
        return "99_ARCHIVE/backups"
    for (subs, exts) in RULES:
        if ext in exts:
            return vdir / subs[0]
    return None


def organize(root: Path, apply: bool, archive: bool):
    plan = []
    if not root.exists():
        print(f"[!] pasta nao existe: {root}")
        return

    vids = sorted([p for p in root.iterdir() if is_video_dir(p)], key=lambda x: x.name)
    print(f"# Organizacao — {root}\n")
    print(f"Videos encontrados: {len(vids)}")
    print(f"Modo: {'APLICAR' if apply else 'DRY-RUN (nada sera movido)'}\n")

    def move(src: Path, dest_dir):
        if isinstance(dest_dir, str):
            dest_dir = root / dest_dir
        dest = unique_dest(dest_dir / src.name)
        plan.append(("move", src, dest))
        if apply:
            dest_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dest))

    # por video
    for v in vids:
        ensure_subs(v, plan, apply)
        for f in list(v.iterdir()):
            if f.is_dir():
                continue
            dest = classify(f.name, f.suffix.lower(), v)
            if dest and isinstance(dest, Path) and dest != v:
                move(f, dest)

    # raiz do canal: arquivos soltos
    for f in list(root.iterdir()):
        if f.is_dir():
            if archive and f.name in CACHE_DIRS:
                dest = unique_dest(root / "99_ARCHIVE" / "cache" / f.name)
                plan.append(("archive", f, dest))
                if apply:
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(f), str(dest))
            continue
        ext = f.suffix.lower()
        if ext in SCRIPT_EXT:
            move(f, "scripts")
        elif ext in ARCHIVE_EXT:
            move(f, "99_ARCHIVE/backups")
        elif ext in {".mp4", ".mkv", ".mov"}:
            move(f, "99_ARCHIVE/raiz_videos")
        elif ext in {".jpg", ".png", ".jpeg"} and "thumb" not in f.name.lower():
            move(f, "00_CANAL/assets")

    # aplica mkdirs pendentes
    if plan:
        print(f"Acoes planejadas: {len(plan)}")
        for kind, a, b in plan:
            rel = b.relative_to(root) if isinstance(b, Path) and root in b.parents else b
            print(f"  [{kind}] {a.name if isinstance(a, Path) else a} -> {rel}")
    else:
        print("Tudo organizado. Nada a fazer.")

    # relatorio
    if apply:
        rep = root / "ORGANIZACAO.md"
        with rep.open("a", encoding="utf-8") as fh:
            fh.write(f"\n## {datetime.now().isoformat(timespec='seconds')}\n")
            for kind, a, b in plan:
                fh.write(f"- {kind}: `{a}` -> `{b}`\n")
        print(f"\n[OK] relatorio atualizado: {rep}")
    else:
        print("\n[dry-run] rode com --apply para aplicar.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--archive", action="store_true")
    a = ap.parse_args()
    organize(Path(a.path).expanduser(), a.apply, a.archive)


if __name__ == "__main__":
    main()
