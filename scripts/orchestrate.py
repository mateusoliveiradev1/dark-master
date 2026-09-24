from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILL_ROOT = HERE.parent

CANONICAL_STEPS = (
    "research",
    "script",
    "art_direction",
    "image_prompts",
    "assets",
    "motion_prompts",
    "remotion",
    "qa",
)


def channel_steps(channel_state: str) -> list[str]:
    state = str(channel_state or "existing").strip().lower()
    if state == "existing":
        return list(CANONICAL_STEPS)
    if state == "new":
        return ["niche", "outliers", *CANONICAL_STEPS]
    raise ValueError(f"invalid_channel_state:{channel_state}")


plan_steps = channel_steps


def visual_scope_path(episode: Path, visual_scope: str | Path | None) -> Path:
    if visual_scope:
        return Path(visual_scope).expanduser().resolve()
    return (Path(episode) / "01_roteiro" / "VISUAL_BIBLE.json").resolve()


def build_orchestration_plan(
    root: str | Path,
    episode: str | Path,
    channel: str | None = None,
    channel_state: str = "existing",
    lane: str = "mixed",
    visual_scope: str | Path | None = None,
    format_name: str = "long",
) -> dict:
    root_path = Path(root).expanduser().resolve()
    episode_path = Path(episode)
    if not episode_path.is_absolute():
        episode_path = root_path / episode_path
    episode_path = episode_path.resolve()
    state = str(channel_state or "existing").strip().lower()
    steps = channel_steps(state)
    scope = visual_scope_path(episode_path, visual_scope)
    gates = {
        "channel": "PASS" if state == "existing" else "REQUIRES_NEW_CHANNEL",
        "niche": "NOT_REQUIRED" if state == "existing" else "REQUIRED",
        "outliers": "NOT_REQUIRED" if state == "existing" else "REQUIRED",
        "visual_scope": "PASS" if scope else "REQUIRED",
    }
    return {
        "version": 1,
        "root": str(root_path),
        "episode": str(episode_path),
        "channel": channel,
        "channelState": state,
        "lane": lane,
        "format": format_name,
        "steps": steps,
        "gates": gates,
        "visualScope": str(scope),
        "visualScopeIsolated": True,
        "identityCopied": False,
    }


orchestration_plan = build_orchestration_plan


def plan_gates(plan: dict) -> list[str]:
    errors = []
    if not plan.get("visualScope"):
        errors.append("visual_scope_required")
    return errors


def load_pipeline_gates(episode: str | Path, format_name: str = "long") -> dict:
    try:
        import remotion
    except ImportError:
        return {"status": "FAIL", "errors": ["remotion_module_unavailable"]}
    return remotion.validate_production_gates(Path(episode), format_name, require_review=False)


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    plan = sub.add_parser("plan")
    plan.add_argument("--root", required=True)
    plan.add_argument("--episode", required=True)
    plan.add_argument("--channel")
    plan.add_argument("--channel-state", choices=["existing", "new"], default="existing")
    plan.add_argument("--lane", default="mixed")
    plan.add_argument("--visual-scope")
    plan.add_argument("--format", choices=["long", "short"], default="long")
    status = sub.add_parser("status")
    status.add_argument("--episode", required=True)
    status.add_argument("--format", choices=["long", "short"], default="long")
    argv = sys.argv[1:]
    if argv and argv[0] not in {"plan", "status", "-h", "--help"}:
        argv = ["plan", *argv]
    args = parser.parse_args(argv)
    if args.command == "plan":
        result = build_orchestration_plan(args.root, args.episode, args.channel, args.channel_state, args.lane, args.visual_scope, args.format)
        result["errors"] = plan_gates(result)
        result["pendingGates"] = [name for name, status in result["gates"].items() if status == "REQUIRED"]
        result["status"] = "FAIL" if result["errors"] else "PASS"
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if not result["errors"] else 1
    result = load_pipeline_gates(args.episode, args.format)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("status") == "PASS" else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False))
        raise SystemExit(1)
