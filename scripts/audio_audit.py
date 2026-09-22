#!/usr/bin/env python3
"""audio_audit.py — audita a voz/áudio de um vídeo.

Uso:
  python scripts/audio_audit.py "<videoNN>/02_audio/voice_FINAL.wav"
  python scripts/audio_audit.py "<videoNN>/02_audio/voice_FINAL.wav" --target -16

Checa:
  - duracao, sample rate, canais, codec
  - loudness integrado (LUFS), true peak (dBTP), LRA  (via loudnorm)
  - clipping (amostras no teto)
  - silencios longos (via silencedetect)
  - consistencia vs alvo de loudness

Sai com codigo 1 se houver falha. Requer ffmpeg/ffprobe no PATH.
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

FFMPEG = shutil.which("ffmpeg")
FFPROBE = shutil.which("ffprobe")


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, errors="replace")


def probe(path):
    if not FFPROBE:
        return {}
    r = run([FFPROBE, "-v", "error", "-show_entries",
             "stream=sample_rate,channels,codec_name,bit_rate",
             "-show_entries", "format=duration,bit_rate",
             "-of", "json", str(path)])
    try:
        d = json.loads(r.stdout)
    except Exception:  # noqa
        return {}
    st = (d.get("streams") or [{}])[0]
    fmt = d.get("format") or {}
    return {
        "duration": float(fmt.get("duration") or 0),
        "sample_rate": st.get("sample_rate"),
        "channels": st.get("channels"),
        "codec": st.get("codec_name"),
    }


def loudness(path):
    if not FFMPEG:
        return {}
    r = run([FFMPEG, "-hide_banner", "-i", str(path),
             "-af", "loudnorm=print_format=json", "-f", "null", "-"])
    m = re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", r.stderr, re.S)
    if not m:
        return {}
    try:
        d = json.loads(m.group(0))
        return {"i": float(d["input_i"]), "tp": float(d["input_tp"]), "lra": float(d["input_lra"])}
    except Exception:  # noqa
        return {}


def silences(path, noise="-40dB", dur=1.5):
    if not FFMPEG:
        return []
    r = run([FFMPEG, "-hide_banner", "-i", str(path),
             "-af", f"silencedetect=noise={noise}:d={dur}", "-f", "null", "-"])
    out = []
    cur = None
    for line in r.stderr.splitlines():
        m1 = re.search(r"silence_start:\s*([\d.]+)", line)
        m2 = re.search(r"silence_end:\s*([\d.]+)", line)
        if m1:
            cur = float(m1.group(1))
        if m2 and cur is not None:
            out.append((cur, float(m2.group(1))))
            cur = None
    return out


def peak_dbfs(path):
    """pico maximo em dBFS via astats."""
    if not FFMPEG:
        return None
    r = run([FFMPEG, "-hide_banner", "-i", str(path),
             "-af", "astats=metadata=1:reset=0", "-f", "null", "-"])
    m = re.search(r"Peak level dB:\s*(-?[\d.]+)", r.stderr)
    return float(m.group(1)) if m else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--target", type=float, default=-16.0, help="LUFS alvo")
    ap.add_argument("--tol", type=float, default=2.0, help="tolerancia de loudness (LU)")
    ap.add_argument("--max-silence", type=float, default=1.5, help="silencio max permitido (s)")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    p = Path(a.path).expanduser()
    if not p.exists():
        print(f"[!] nao existe: {p}"); sys.exit(2)
    if not FFMPEG:
        print("[!] ffmpeg nao encontrado no PATH"); sys.exit(2)

    info = probe(p)
    ld = loudness(p)
    pk = peak_dbfs(p)
    sil = silences(p, dur=a.max_silence)

    flags = []
    if info.get("duration", 0) < 60:
        flags.append(f"curto({info.get('duration',0):.0f}s)")
    if ld:
        if abs(ld["i"] - a.target) > a.tol:
            flags.append(f"loudness({ld['i']} LUFS vs {a.target})")
        if ld["tp"] > -1.0:
            flags.append(f"true_peak({ld['tp']} dBTP)")
        if ld["lra"] > 14:
            flags.append(f"lra_alto({ld['lra']})")
    if pk is not None and pk >= -0.1:
        flags.append(f"clipping({pk} dBFS)")
    if sil:
        flags.append(f"{len(sil)} silencio(s)>{a.max_silence}s")

    print(f"# Auditoria de audio — {p.name}\n")
    print(f"  duracao: {info.get('duration',0):.1f}s | {info.get('sample_rate')}Hz | "
          f"{info.get('channels')}ch | {info.get('codec')}")
    if ld:
        print(f"  loudness: {ld['i']} LUFS (alvo {a.target}) | true peak {ld['tp']} dBTP | LRA {ld['lra']}")
    if pk is not None:
        print(f"  pico: {pk} dBFS")
    if sil:
        print(f"  silencios > {a.max_silence}s: {len(sil)}")
        for s0, s1 in sil[:8]:
            print(f"    {s0:.2f}s -> {s1:.2f}s  ({s1-s0:.2f}s)")
    print(f"\nRESULTADO: {'PASSOU' if not flags else 'FALHA'} {', '.join(flags)}")

    rep = p.parent / "AUDITORIA_AUDIO.md"
    rep.write_text(
        f"# Auditoria de audio\n\nArquivo: `{p.name}`\n\n"
        f"- duracao: {info.get('duration',0):.2f}s\n"
        f"- loudness: {ld.get('i','?')} LUFS | TP {ld.get('tp','?')} dBTP | LRA {ld.get('lra','?')}\n"
        f"- pico: {pk} dBFS\n- silencios>{a.max_silence}s: {len(sil)}\n"
        f"- flags: {', '.join(flags) or 'nenhuma'}\n", encoding="utf-8")
    if not a.quiet:
        print(f"[OK] relatorio: {rep}")
    sys.exit(0 if not flags else 1)


if __name__ == "__main__":
    main()
