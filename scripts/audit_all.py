#!/usr/bin/env python3
"""audit_all.py — roda TODAS as auditorias de um video (ou canal) e da um veredito.

Uso:
  python scripts/audit_all.py "<videoNN>"
  python scripts/audit_all.py "C:/.../canal dark1"          # varre todos os videoNN
  python scripts/audit_all.py "<videoNN>" --json

Gates: imagens (image_audit) + audio (audio_audit) + legendas (captions_audit) + timing + pronúncia + consistência + Short QA + originalidade + compliance + scorecard + research + pacote/final.
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


def audio_target(vdir):
    try:
        contract = json.loads((vdir / "02_audio" / "voice_contract.json").read_text(encoding="utf-8"))
        return float(contract.get("loudnorm", -16.0))
    except (OSError, ValueError, TypeError, AttributeError):
        return -16.0


def timing_gate(vdir, audio):
    script_dir = vdir / "01_roteiro"
    map_data = {}
    try:
        map_data = json.loads((script_dir / "ROTEIRO_MAP.json").read_text(encoding="utf-8"))
    except (OSError, ValueError, AttributeError):
        pass
    target = map_data.get("target_minutes") if isinstance(map_data, dict) else ""
    narration = script_dir / "narration_v3.txt"
    captions_times = vdir / "02_audio" / "captions_times.json"
    output = script_dir / "TIMING_AUDIT.json"
    if not target or not narration.exists() or not captions_times.exists() or not audio:
        return False
    result = subprocess.run(
        [sys.executable, str(HERE / "timing_audit.py"), "--narration", str(narration),
         "--captions-times", str(captions_times), "--target-minutes", str(target),
         "--map", str(script_dir / "ROTEIRO_MAP.json"), "--voice", str(audio), "--out", str(output)],
        capture_output=True,
        text=True,
    )
    try:
        return result.returncode == 0 and json.loads(output.read_text(encoding="utf-8")).get("status") == "PASS"
    except (OSError, ValueError, AttributeError):
        return False


def optional_artifact_status(path):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError, TypeError):
        return "FALHA"
    return str(data.get("status", "FALHA")).upper() if isinstance(data, dict) else "FALHA"


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
        target = audio_target(v)
        code, out = run("audio_audit.py", [str(audio), "--target", str(target)])
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

    if timing_gate(v, audio):
        res["gates"]["timing"] = "ok"
    else:
        res["gates"]["timing"] = "FALHA"
        res["flags"].append("timing")

    render_plans = list((v / "01_roteiro").glob("RENDER_PLAN_*.json")) if (v / "01_roteiro").exists() else []
    if render_plans:
        remotion_results = []
        for plan in render_plans:
            format_name = plan.stem.removeprefix("RENDER_PLAN_").lower()
            code, output = run("remotion.py", ["audit", v.name, "--root", str(v.parent), "--format", format_name])
            remotion_results.append(code)
        res["gates"]["remotion"] = "ok" if all(code == 0 for code in remotion_results) else "FALHA"
        if any(code != 0 for code in remotion_results):
            res["flags"].append("remotion")
    else:
        res["gates"]["remotion"] = "nao_ativo"

    pronunciation = v / "01_roteiro" / "PRONUNCIA_TTS.json"
    try:
        pronunciation_data = json.loads(pronunciation.read_text(encoding="utf-8"))
    except (OSError, ValueError, AttributeError):
        pronunciation_data = {}
    if pronunciation_data.get("status") == "PASS":
        res["gates"]["pronuncia"] = "ok"
    else:
        res["gates"]["pronuncia"] = "FALHA"
        res["flags"].append("pronuncia")

    consistency = v / "01_roteiro" / "CONSISTENCIA_TTS.json"
    try:
        consistency_data = json.loads(consistency.read_text(encoding="utf-8"))
    except (OSError, ValueError, AttributeError):
        consistency_data = {}
    if consistency_data.get("status") == "PASS":
        res["gates"]["consistencia"] = "ok"
    else:
        res["gates"]["consistencia"] = "FALHA"
        res["flags"].append("consistencia")

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

    optional_artifacts = (
        ("titulo", v / "01_roteiro" / "TITLE_RESEARCH.json"),
        ("rotacao", v / "01_roteiro" / "ROTATION_AUDIT.json"),
        ("assets", v / "01_roteiro" / "PROMPT_STATUS.json"),
    )
    for key, path in optional_artifacts:
        if not path.exists():
            res["gates"][key] = "nao_ativo"
            continue
        artifact_status = optional_artifact_status(path)
        res["gates"][key] = "ok" if artifact_status in {"PASS", "REVIEW"} else artifact_status
        if artifact_status == "FAIL":
            res["flags"].append(key)

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
    if not pkg:
        res["flags"].append("pacote")
    final = any(v.glob("04_video_final/*.mp4")) if (v / "04_video_final").exists() else False
    res["gates"]["final"] = "ok" if final else "ausente"
    if not final:
        res["flags"].append("final")

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
        print(f"{'video':<20} {'imgs':<8} {'audio':<8} {'caps':<8} {'timing':<8} {'remotion':<8} {'titulo':<8} {'rotacao':<8} {'assets':<8} {'pron':<8} {'cons':<8} {'short':<8} {'orig':<8} {'comp':<8} {'score':<8} {'research':<8} {'pacote':<8} {'final':<8} veredito")
        for r in results:
            g = r["gates"]
            print(f"{r['video']:<20} {g['imagens']:<8} {g['audio']:<8} {g['caps']:<8} "
                  f"{g['timing']:<8} {g['remotion']:<8} {g['titulo']:<8} {g['rotacao']:<8} {g['assets']:<8} {g['pronuncia']:<8} {g['consistencia']:<8} {g['short_qa']:<8} {g['originalidade']:<8} {g['compliance']:<8} {g['scorecard']:<8} {g['research']:<8} {g['pacote']:<8} {g['final']:<8} {r['veredito']}")
        print(f"\nTotal: {len(results)} | Falhas: {len(fails)}")
        print("Falhas:", ", ".join(r["video"] for r in fails) or "nenhuma")

    sys.exit(0 if not fails else 1)


if __name__ == "__main__":
    main()
