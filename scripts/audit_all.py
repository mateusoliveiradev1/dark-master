#!/usr/bin/env python3
"""audit_all.py — roda TODAS as auditorias de um video (ou canal) e da um veredito.

Uso:
  python scripts/audit_all.py "<videoNN>"
  python scripts/audit_all.py "C:/.../canal dark1"          # varre todos os videoNN
  python scripts/audit_all.py "<videoNN>" --json

Gates: imagens (image_audit) + audio (audio_audit) + legendas (captions_audit) + timing + Short QA + originalidade + compliance + scorecard + research + pacote/final.
Sai com codigo 1 se qualquer gate falhar.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
VIDEO_RE = __import__("re").compile(r"^(video|ep|episode)[ _-]?\d+", __import__("re").IGNORECASE)


def run(script, args):
    r = subprocess.run([sys.executable, str(HERE / script), *args],
                       capture_output=True, text=True, errors="replace")
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def find(d, names):
    for n in names:
        p = d / n
        if p.exists():
            return p
    return None


def audit_video(v):
    res = {"video": v.name, "gates": {}, "flags": []}

    img = v / "03_imagens"
    if img.exists() and any(img.glob("*.jpg")):
        code, out = run("image_audit.py", [str(img), "--sheet"])
        res["gates"]["imagens"] = "ok" if code == 0 else "FALHA"
        if code != 0:
            res["flags"].append("imagens")
    else:
        res["gates"]["imagens"] = "ausente"

    audio = find(v / "02_audio", ["voice_FINAL.wav", "voice_V3_FINAL.wav"]) if (v / "02_audio").exists() else None
    if audio:
        code, out = run("audio_audit.py", [str(audio)])
        res["gates"]["audio"] = "ok" if code == 0 else "FALHA"
        if code != 0:
            res["flags"].append("audio")
    else:
        res["gates"]["audio"] = "ausente"

    cap = find(v / "02_audio", ["captions.srt", "captions.vtt"]) if (v / "02_audio").exists() else None
    if cap:
        args = [str(cap)] + (["--audio", str(audio)] if audio else [])
        code, out = run("captions_audit.py", args)
        res["gates"]["captions"] = "ok" if code == 0 else "FALHA"
        if code != 0:
            res["flags"].append("captions")
    else:
        res["gates"]["captions"] = "ausente"

    timing = v / "01_roteiro" / "TIMING_AUDIT.json"
    try:
        timing_data = json.loads(timing.read_text(encoding="utf-8"))
    except (OSError, ValueError, AttributeError):
        timing_data = {}
    if timing_data.get("status") == "PASS":
        res["gates"]["timing"] = "ok"
    else:
        res["gates"]["timing"] = "FALHA"
        res["flags"].append("timing")

    short_qa = v / "01_roteiro" / "SHORT_QA.json"
    try:
        short_qa_data = json.loads(short_qa.read_text(encoding="utf-8"))
    except (OSError, ValueError, AttributeError):
        short_qa_data = {}
    if short_qa_data.get("status") == "PASS":
        res["gates"]["short_qa"] = "ok"
    else:
        res["gates"]["short_qa"] = "FALHA"
        res["flags"].append("short_qa")

    originality = v / "01_roteiro" / "ORIGINALITY_AUDIT.json"
    try:
        originality_data = json.loads(originality.read_text(encoding="utf-8"))
    except (OSError, ValueError, AttributeError):
        originality_data = {}
    if originality_data.get("status") in {"PASS", "REVIEW"}:
        res["gates"]["originalidade"] = "ok"
    else:
        res["gates"]["originalidade"] = "FALHA"
        res["flags"].append("originalidade")

    compliance = v / "01_roteiro" / "COMPLIANCE_AUDIT.json"
    try:
        compliance_data = json.loads(compliance.read_text(encoding="utf-8"))
    except (OSError, ValueError, AttributeError):
        compliance_data = {}
    if compliance_data.get("status") == "PASS":
        res["gates"]["compliance"] = "ok"
    else:
        res["gates"]["compliance"] = "FALHA"
        res["flags"].append("compliance")

    scorecard = v / "01_roteiro" / "SCRIPT_SCORECARD.json"
    try:
        scorecard_data = json.loads(scorecard.read_text(encoding="utf-8"))
    except (OSError, ValueError, AttributeError):
        scorecard_data = {}
    if scorecard_data.get("status") == "PASS":
        res["gates"]["scorecard"] = "ok"
    else:
        res["gates"]["scorecard"] = "FALHA"
        res["flags"].append("scorecard")

    research_audit = v / "01_roteiro" / "RESEARCH_AUDIT.json"
    try:
        research_data = json.loads(research_audit.read_text(encoding="utf-8"))
    except (OSError, ValueError, AttributeError):
        research_data = {}
    if research_data.get("status") == "PASS":
        res["gates"]["research"] = "ok"
    else:
        res["gates"]["research"] = "FALHA"
        res["flags"].append("research")

    pkg = find(v, ["youtube_package.txt", "PACOTE_PUBLICACAO.txt"])
    res["gates"]["pacote"] = "ok" if pkg else "ausente"
    final = any(v.glob("04_video_final/*.mp4")) if (v / "04_video_final").exists() else False
    res["gates"]["final"] = "ok" if final else "ausente"

    res["veredito"] = "PASSOU" if not res["flags"] else "FALHA"
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    root = Path(a.path).expanduser()
    if not root.exists():
        print(f"[!] nao existe: {root}"); sys.exit(2)

    targets = [root] if VIDEO_RE.match(root.name) else \
        sorted([p for p in root.iterdir() if p.is_dir() and VIDEO_RE.match(p.name)], key=lambda x: x.name)
    if not targets:
        print("Nenhum videoNN encontrado."); sys.exit(2)

    results = [audit_video(v) for v in targets]
    fails = [r for r in results if r["veredito"] == "FALHA"]

    if a.json:
        print(json.dumps(results, ensure_ascii=False, indent=1))
    else:
        print("# Auditoria geral\n")
        print(f"{'video':<20} {'imgs':<8} {'audio':<8} {'caps':<8} {'timing':<8} {'short':<8} {'orig':<8} {'comp':<8} {'score':<8} {'research':<8} {'pacote':<8} {'final':<8} veredito")
        for r in results:
            g = r["gates"]
            print(f"{r['video']:<20} {g['imagens']:<8} {g['audio']:<8} {g['captions']:<8} "
                  f"{g['timing']:<8} {g['short_qa']:<8} {g['originalidade']:<8} {g['compliance']:<8} {g['scorecard']:<8} {g['research']:<8} {g['pacote']:<8} {g['final']:<8} {r['veredito']}")
        print(f"\nTotal: {len(results)} | Falhas: {len(fails)}")
        print("Falhas:", ", ".join(r["video"] for r in fails) or "nenhuma")

    sys.exit(0 if not fails else 1)


if __name__ == "__main__":
    main()
