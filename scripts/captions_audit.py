#!/usr/bin/env python3
"""captions_audit.py — audita legendas SRT/VTT.

Uso:
  python scripts/captions_audit.py "<videoNN>/02_audio/captions.srt"
  python scripts/captions_audit.py captions.srt --audio voice_FINAL.wav

Checa:
  - nº de cues, 1ª cue perto de 0:00
  - duracao por cue (min/max), sobreposicoes, gaps grandes
  - linhas por cue (<=2), chars por linha (<=42)
  - velocidade de leitura (CPS)
  - cues vazias e ultima cue vs duracao do audio

Sai com codigo 1 se houver falha.
"""
import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

TS = re.compile(r"(\d+):(\d{2}):(\d{2})[,.](\d{3})")


def to_sec(h, m, s, ms):
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000.0


def parse(path):
    txt = Path(path).read_text(encoding="utf-8", errors="replace")
    cues = []
    for block in re.split(r"\n\s*\n", txt):
        lines = [l for l in block.splitlines() if l.strip() != ""]
        if not lines:
            continue
        ti = None
        for i, l in enumerate(lines):
            if "-->" in l:
                ti = i
                break
        if ti is None:
            continue
        m = TS.findall(lines[ti])
        if len(m) < 2:
            continue
        start = to_sec(*m[0]); end = to_sec(*m[1])
        text = "\n".join(l for l in lines[ti + 1:]).strip()
        text = re.sub(r"<[^>]+>", "", text)
        cues.append({"start": start, "end": end, "text": text})
    return cues


def audio_duration(path):
    fp = shutil.which("ffprobe")
    if not fp or not path:
        return None
    r = subprocess.run([fp, "-v", "error", "-show_entries", "format=duration",
                        "-of", "default=nk=1:nw=1", str(path)], capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except Exception:  # noqa
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--audio", help="arquivo de audio para comparar a ultima cue")
    ap.add_argument("--max-lines", type=int, default=2)
    ap.add_argument("--max-chars", type=int, default=42)
    ap.add_argument("--max-cps", type=float, default=21.0)
    ap.add_argument("--min-dur", type=float, default=0.5)
    ap.add_argument("--max-dur", type=float, default=7.0)
    a = ap.parse_args()

    p = Path(a.path).expanduser()
    if not p.exists():
        print(f"[!] nao existe: {p}"); sys.exit(2)
    cues = parse(p)
    if not cues:
        print("[!] nenhuma cue encontrada"); sys.exit(2)

    flags = []
    warns = []
    if cues[0]["start"] > 1.5:
        flags.append(f"1a_cue_tarde({cues[0]['start']:.1f}s)")
    overlaps = gaps = empty = 0
    long_cue = short_cue = bad_lines = bad_chars = fast = 0
    for i, c in enumerate(cues):
        dur = c["end"] - c["start"]
        if not c["text"]:
            empty += 1
        lines = [l for l in c["text"].split("\n")] if "\n" in c["text"] else [c["text"]]
        if len(lines) > a.max_lines:
            bad_lines += 1
        if any(len(l) > a.max_chars for l in lines):
            bad_chars += 1
        if dur > a.max_dur:
            long_cue += 1
        if dur < a.min_dur:
            short_cue += 1
        if dur > 0 and dur >= 0.6 and (len(c["text"]) / dur) > a.max_cps:
            fast += 1
        if i > 0:
            if c["start"] < cues[i - 1]["end"] - 0.05:
                overlaps += 1
            elif c["start"] - cues[i - 1]["end"] > 3.0:
                gaps += 1

    if empty:
        flags.append(f"cues_vazias({empty})")
    if overlaps:
        flags.append(f"sobreposicoes({overlaps})")
    if gaps:
        flags.append(f"gaps>3s({gaps})")
    if long_cue:
        flags.append(f"cues_longas({long_cue})")
    if short_cue:
        warns.append(f"cues_curtas({short_cue})")
    if bad_lines:
        flags.append(f">linhas({bad_lines})")
    if bad_chars:
        flags.append(f">chars({bad_chars})")
    if fast:
        warns.append(f"leitura_rapida({fast})")

    dur_audio = audio_duration(a.audio) if a.audio else None
    last = cues[-1]["end"]
    coverage = (last / dur_audio * 100) if dur_audio else None
    if dur_audio and coverage and coverage < 90:
        flags.append(f"cobertura({coverage:.0f}%)")

    print(f"# Auditoria de legendas — {p.name}\n")
    print(f"  cues: {len(cues)}")
    print(f"  1a cue: {cues[0]['start']:.2f}s | ultima: {last:.2f}s")
    if coverage:
        print(f"  cobertura vs audio ({dur_audio:.1f}s): {coverage:.0f}%")
    print(f"  problemas: vazias {empty} | sobrepostas {overlaps} | gaps {gaps} | "
          f"longas {long_cue} | curtas {short_cue} | >linhas {bad_lines} | >chars {bad_chars} | rapida {fast}")
    if warns:
        print(f"  avisos (nao bloqueiam): {', '.join(warns)}")
    print(f"\nRESULTADO: {'PASSOU' if not flags else 'FALHA'} {', '.join(flags)}")

    rep = p.parent / "AUDITORIA_CAPTIONS.md"
    rep.write_text(
        f"# Auditoria de legendas\n\nArquivo: `{p.name}`\n\n"
        f"- cues: {len(cues)}\n- 1a: {cues[0]['start']:.2f}s | ultima: {last:.2f}s\n"
        f"- cobertura: {f'{coverage:.0f}%' if coverage else 'n/d'}\n"
        f"- falhas: {', '.join(flags) or 'nenhuma'}\n- avisos: {', '.join(warns) or 'nenhum'}\n", encoding="utf-8")
    print(f"[OK] relatorio: {rep}")
    sys.exit(0 if not flags else 1)


if __name__ == "__main__":
    main()
