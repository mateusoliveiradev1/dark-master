#!/usr/bin/env python3
"""remotion_check.py — trava o pipeline Remotion real no loop de verificacao.

Roda `npm run typecheck` (tsc) + `npm test` (vitest) em remotion/ e emite
REMOTION_CHECK.json. Sem isso, o motion e "verde" so no Python.
Uso: python scripts/remotion_check.py [--out 04_video_final/REMOTION_CHECK.json] [--skip-typecheck]
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "remotion"


def npm_command():
    import shutil
    found = shutil.which("npm.cmd") or shutil.which("npm")
    if found:
        return found
    for candidate in (r"C:\Program Files\nodejs\npm.cmd",
                      str(Path.home() / "AppData" / "Roaming" / "npm" / "npm.cmd")):
        if Path(candidate).exists():
            return candidate
    return "npm"


def run_npm(args, timeout=600):
    try:
        result = subprocess.run([npm_command(), *args], cwd=str(ROOT), capture_output=True,
                                text=True, timeout=timeout, errors="replace")
    except FileNotFoundError:
        return None, "npm_nao_encontrado"
    except subprocess.TimeoutExpired:
        return None, "timeout"
    return result, ""


def parse_vitest(output):
    output = output or ""
    files_match = re.search(r"Test Files\s+\d+\s+passed\s+\((\d+)\)", output)
    passed_match = re.search(r"Tests\s+\d+\s+passed\s+\((\d+)\)", output)
    fail_match = re.search(r"Tests\s+[^\n]*?\b(\d+)\s+failed", output)
    files = int(files_match.group(1)) if files_match else 0
    passed = int(passed_match.group(1)) if passed_match else 0
    failed = int(fail_match.group(1)) if fail_match else 0
    return {"files": files, "passed": passed, "failed": failed}


def check(skip_typecheck=False):
    typecheck = {"status": "SKIPPED"}
    if not skip_typecheck:
        result, error = run_npm(["run", "typecheck"])
        if result is None:
            typecheck = {"status": "FAIL", "error": error}
        else:
            typecheck = {"status": "PASS" if result.returncode == 0 else "FAIL",
                         "output": (result.stdout + result.stderr)[-2000:]}
    result, error = run_npm(["test"])
    if result is None:
        tests = {"status": "FAIL", "error": error, "files": 0, "passed": 0, "failed": 1}
    else:
        parsed = parse_vitest(result.stdout + result.stderr)
        tests = {"status": "PASS" if result.returncode == 0 and parsed["failed"] == 0 and parsed["passed"] > 0 else "FAIL",
                 **parsed}
    status = "PASS" if typecheck["status"] in {"PASS", "SKIPPED"} and tests["status"] == "PASS" else "FAIL"
    return {"status": status, "typecheck": typecheck, "tests": tests}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="")
    parser.add_argument("--skip-typecheck", action="store_true")
    args = parser.parse_args()
    result = check(args.skip_typecheck)
    if args.out:
        output = Path(args.out)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
