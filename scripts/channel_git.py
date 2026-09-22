#!/usr/bin/env python3
"""channel_git.py — versiona o projeto do canal SEM a mídia pesada (vídeo/áudio/imagem).

O canal real costuma ter dezenas de GB de mídia; o git guarda só o que importa:
roteiro, pesquisa, PROMPTS, pacotes, scripts, configs, branding e regras.

Uso:
  python scripts/channel_git.py "<pasta do canal>"                     # auditoria (dry-run)
  python scripts/channel_git.py "<pasta>" --init                       # .gitignore + git init
  python scripts/channel_git.py "<pasta>" --init --commit              # + commit inicial
  python scripts/channel_git.py "<pasta>" --status                     # status/log resumidos

Guardas:
  - `.gitignore` existente NUNCA é sobrescrito (avisa e segue).
  - `--commit` mede o staged; acima de --max-mb (default 50) aborta e desfaz o stage.
"""
import argparse
import fnmatch
import os
import subprocess
import sys
from pathlib import Path

TEMPLATE = Path(__file__).resolve().parent.parent / "assets" / "gitignore-canal"
SKIP_DIRS = {".git", "__pycache__", "node_modules", "99_ARCHIVE"}


def is_ignored(rel, patterns):
    rel = rel.replace("\\", "/")
    for p in patterns:
        p = p.strip()
        if not p or p.startswith("#"):
            continue
        if p.endswith("/"):
            if rel == p[:-1] or rel.startswith(p):
                return True
            continue
        if fnmatch.fnmatch(rel, p) or fnmatch.fnmatch(os.path.basename(rel), p):
            return True
        if "/" in rel and fnmatch.fnmatch(rel, "*/" + p):
            return True
    return False


def load_patterns(root):
    gi = root / ".gitignore"
    text = gi.read_text(encoding="utf-8") if gi.exists() else TEMPLATE.read_text(encoding="utf-8")
    return text, [l for l in text.splitlines() if l.strip() and not l.strip().startswith("#")]


def run(root, *args, check=False):
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, check=check)


def audit(root):
    text, pats = load_patterns(root)
    tracked, ignored = [], []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            p = Path(dirpath) / fn
            rel = str(p.relative_to(root))
            (ignored if is_ignored(rel, pats) else tracked).append((rel, p.stat().st_size))
    tracked.sort(key=lambda x: -x[1])
    total = sum(s for _, s in tracked)
    print(f"# Auditoria — {root}\n")
    print(f"seriam versionados: {len(tracked)} arquivos | {total/1e6:.2f} MB")
    print(f"ficariam de fora (mídia/cache): {len(ignored)} arquivos | {sum(s for _, s in ignored)/1e6:.1f} MB\n")
    print("maiores arquivos versionados:")
    for rel, s in tracked[:8]:
        print(f"  {s/1e3:9.1f} KB  {rel}")
    if not (root / ".gitignore").exists():
        print("\n[!] sem .gitignore — rode com --init para criar (a partir do template do canal).")
    return tracked


def init(root):
    gi = root / ".gitignore"
    if gi.exists():
        print("[i] .gitignore ja existe — nao sobrescrevi.")
    else:
        gi.write_text(TEMPLATE.read_text(encoding="utf-8"), encoding="utf-8")
        print(f"[OK] .gitignore criado: {gi}")
    if not (root / ".git").exists():
        r = run(root, "init", "-b", "main")
        if r.returncode != 0:
            r = run(root, "init")
        print("[OK] git init" + ("" if r.returncode == 0 else f" FALHOU: {r.stderr.strip()}"))
    else:
        print("[i] ja e um repositorio git.")
    audit(root)
    print("\nProximo: python scripts/channel_git.py \"%s\" --commit" % root)


def commit(root, message, max_mb):
    if not (root / ".git").exists():
        print("[!] nao e repositorio — rode --init primeiro."); return 1
    r = run(root, "add", "-A")
    if r.returncode != 0:
        print("[!] git add falhou:", r.stderr.strip()); return 1
    ls = run(root, "ls-files", "-z")
    files = [f for f in ls.stdout.split("\0") if f]
    total = sum((root / f).stat().st_size for f in files if (root / f).exists())
    print(f"staged: {len(files)} arquivos | {total/1e6:.2f} MB")
    if total / 1e6 > max_mb:
        run(root, "reset")
        print(f"[!] ABORTADO: staged acima de {max_mb} MB — mídia vazou pro .gitignore? stage desfeito.")
        biggest = sorted(((f, (root / f).stat().st_size) for f in files if (root / f).exists()),
                         key=lambda x: -x[1])[:8]
        for f, s in biggest:
            print(f"   {s/1e6:8.2f} MB  {f}")
        return 1
    r = run(root, "commit", "-m", message)
    print(r.stdout.strip() or r.stderr.strip())
    return 0 if r.returncode == 0 else 1


def status(root):
    for args in (("status", "-sb"), ("log", "--oneline", "-5")):
        r = run(root, *args)
        print(r.stdout.strip() or r.stderr.strip())
    return 0


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("channel")
    ap.add_argument("--init", action="store_true", help="cria .gitignore (template do canal) + git init")
    ap.add_argument("--commit", action="store_true", help="add + commit (com guarda de tamanho)")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--message", "-m", default="checkpoint: canal versionado (texto; midia fora)")
    ap.add_argument("--max-mb", type=float, default=50.0)
    a = ap.parse_args()

    root = Path(a.channel).expanduser().resolve()
    if not root.is_dir():
        print(f"[!] pasta nao encontrada: {root}"); return 1
    if a.status:
        return status(root)
    if a.init:
        init(root)
        return 0
    if a.commit:
        return commit(root, a.message, a.max_mb)
    audit(root)
    return 0


if __name__ == "__main__":
    sys.exit(main())
