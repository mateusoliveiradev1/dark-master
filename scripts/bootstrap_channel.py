#!/usr/bin/env python3
import argparse
import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILL_ROOT = HERE.parent
TEMPLATES = SKILL_ROOT / "assets" / "channel-template"


def write_profile(path: Path, channel: str, name: str, language: str) -> None:
    path.write_text(
        "\n".join(
            [
                f"# {name}",
                "",
                f"**Canal:** `{channel}`",
                f"**Idioma:** `{language}`",
                "**Status:** novo",
                "",
                "## Público",
                "",
                "Preencher com público, problema, promessa, tom e limites.",
                "",
                "## Identidade",
                "",
                "Preencher paleta, fonte, logo, banner, watermark e séries.",
                "",
                "## Operação",
                "",
                "Preencher lane, calendário, frequência, voice, motion e regras de publicação.",
            ],
        )
        + "\n",
        encoding="utf-8",
    )


def load_brief(path):
    """Brief JSON do niche_scan --brief. Retorna {} se ausente/ilegivel."""
    try:
        data = json.loads(Path(path).expanduser().read_text(encoding="utf-8-sig"))
    except (OSError, ValueError):
        return {}
    return data if isinstance(data, dict) else {}


def pick_model(brief, model=None):
    """Modelo sugerido: --model vence; senao casa theme do brief com models/<slug>."""
    if model:
        return model
    theme = str((brief.get("cluster") or {}).get("theme") or brief.get("theme") or "")
    slug = "".join(c if c.isalnum() else "-" for c in theme.lower()).strip("-")[:60]
    candidate = SKILL_ROOT / "models" / slug
    if slug and candidate.is_dir():
        return slug
    return "generic"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--channel", required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--root", required=True)
    parser.add_argument("--playbook-root")
    parser.add_argument("--language", default="pt")
    parser.add_argument("--engine", choices=["remotion", "legacy"], default="remotion")
    parser.add_argument("--from-brief", default="",
                        help="brief JSON do niche_scan: preenche profile, vigias e piloto")
    parser.add_argument("--model", default="", help="models/<slug> (default: casa com o theme do brief)")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    root = Path(args.root).expanduser().resolve()
    playbook_root = Path(args.playbook_root).expanduser().resolve() if args.playbook_root else SKILL_ROOT / "playbooks"
    playbook = playbook_root / args.channel
    if playbook.exists() and not args.force:
        print(json.dumps({"status": "FAIL", "error": "playbook_exists", "path": str(playbook)}))
        return 1
    brief = load_brief(args.from_brief) if args.from_brief else {}
    if args.from_brief and not brief:
        print(json.dumps({"status": "FAIL", "error": "brief_ilegivel", "path": args.from_brief}))
        return 1
    model = pick_model(brief, args.model or None)
    root.mkdir(parents=True, exist_ok=True)
    for relative in (
        "00_CANAL/assets",
        "00_CANAL/branding",
        "video01/01_roteiro",
        "video01/02_audio",
        "video01/03_imagens",
        "video01/04_video_final",
    ):
        (root / relative).mkdir(parents=True, exist_ok=True)
    playbook.mkdir(parents=True, exist_ok=True)
    write_profile(playbook / "profile.md", args.channel, args.name, args.language)
    for name in ("style.json", "motion.json", "voice.json", "roteiro.json", "visual.json"):
        source = TEMPLATES / name
        target = playbook / name
        if target.exists() and args.force:
            target.unlink()
        shutil.copy2(source, target)
    motion_path = playbook / "motion.json"
    motion = json.loads(motion_path.read_text(encoding="utf-8"))
    motion["engine"] = args.engine
    motion_path.write_text(json.dumps(motion, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if brief:
        cluster = brief.get("cluster", {}) if isinstance(brief.get("cluster"), dict) else {}
        evidence = [c.get("channel", "") for c in cluster.get("channels", [])[:3] if c.get("channel")]
        checks = [f"- {c.get('status')}: {c.get('name')}" for c in brief.get("checks", [])]
        suggest = brief.get("suggest", {}) if isinstance(brief.get("suggest"), dict) else {}
        ideas = [str(s) for s in suggest.get("suggestions", [])[:20]]
        profile_extra = [
            "",
            "## Origem (brief de nicho)",
            "",
            f"- Theme: `{brief.get('theme', '')}` | veredito: `{brief.get('verdict', '')}` | modelo: `{model}`",
            f"- Canais-evidencia: {', '.join(evidence) or '-'}",
            "- Checklist do brief:",
            *(f"  {c}" for c in checks),
            "- 20 ideias-semente (autocomplete):",
            *(f"  - {idea}" for idea in ideas),
        ]
        with (playbook / "profile.md").open("a", encoding="utf-8") as handle:
            handle.write("\n".join(profile_extra) + "\n")
        watch_path = SKILL_ROOT / "monitor" / "channels.json"
        try:
            watch = json.loads(watch_path.read_text(encoding="utf-8"))
            seen = {c.get("handle") for c in watch.get("channels", [])}
            for channel in evidence:
                handle = channel if channel.startswith("@") else ""
                if handle and handle not in seen:
                    watch.setdefault("channels", []).append(
                        {"name": channel, "handle": handle, "niche": model, "nota": f"evidencia do brief {brief.get('theme', '')}"})
                    seen.add(handle)
            watch_path.write_text(json.dumps(watch, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        except (OSError, ValueError) as exc:
            print(json.dumps({"status": "WARN", "warning": f"watchlist_nao_atualizada:{exc}"}))
    (root / "00_CANAL" / "CALENDARIO_30.txt").write_text("DIA | DATA | video | tema | serie | status\n", encoding="utf-8")
    (root / "00_CANAL" / "PIPELINE.txt").write_text(
        "\n".join(
            [
                "PIPELINE REMOTION",
                "",
                "1. Preencher profile.md, visual.json e contracts.",
                "2. Rodar contract_audit.py.",
                "3. Produzir pesquisa, claims, narration e Short separado.",
                "4. Gerar todas as imagens e passar image_audit.py.",
                "5. Gerar voz, captions e timing PASS.",
                "6. Gerar RENDER_PLAN e stills.",
                "7. Revisar com dark-artdirector e dark-visual-reviewer.",
                "8. Renderizar somente após aprovação visual.",
                "9. Rodar audit_all.py e manter o upload manual.",
            ],
        )
        + "\n",
        encoding="utf-8",
    )
    result = {"status": "PASS", "project": str(root), "playbook": str(playbook), "engine": args.engine,
              "model": model, "brief": args.from_brief or None}
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
