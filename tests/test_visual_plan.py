import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import visual_plan


class VisualPlanTests(unittest.TestCase):
    def test_init_creates_gated_artifacts(self):
        with tempfile.TemporaryDirectory() as temp:
            episode = Path(temp) / "video01"
            script_dir = episode / "01_roteiro"
            (episode / "03_imagens").mkdir(parents=True)
            script_dir.mkdir(parents=True)
            (script_dir / "ROTEIRO_MAP.json").write_text(json.dumps({"blocks": [{"id": "B001", "beat": "HOOK", "question": "O que muda?", "state_change": "A prova entra."}]}), encoding="utf-8")
            result = visual_plan.init_artifacts(episode)
            self.assertEqual(result["status"], "NEEDS_ART_DIRECTION")
            self.assertEqual(len(result["prompts"]), 1)
            self.assertTrue((script_dir / "SHOT_SPECS.json").exists())
            self.assertTrue((script_dir / "PROMPT_PLAN.json").exists())
            self.assertTrue((episode / "03_imagens" / "PROMPTS.md").exists())

    def test_compile_becomes_ready_after_specs_are_completed(self):
        with tempfile.TemporaryDirectory() as temp:
            episode = Path(temp) / "video01"
            script_dir = episode / "01_roteiro"
            script_dir.mkdir(parents=True)
            (episode / "03_imagens").mkdir(parents=True)
            (script_dir / "ROTEIRO_MAP.json").write_text(json.dumps({"blocks": [{"id": "B001", "beat": "HOOK", "question": "O que muda?", "state_change": "A prova entra."}]}), encoding="utf-8")
            visual_plan.init_artifacts(episode)
            specs_path = script_dir / "SHOT_SPECS.json"
            data = json.loads(specs_path.read_text(encoding="utf-8"))
            data["shots"][0]["status"] = "ready"
            data["shots"][0]["visual"]["subject"] = "a forensic workspace"
            data["shots"][0]["visual"]["action"] = "a controlled evidence reveal"
            data["shots"][0]["visual"]["location"] = "an empty laboratory at night"
            data["shots"][0]["visual"]["timeOfDay"] = "night"
            data["shots"][0]["visual"]["camera"] = "a purposeful documentary close-up"
            specs_path.write_text(json.dumps(data), encoding="utf-8")
            result = visual_plan.compile_prompt_plan(episode, specs_path=specs_path)
            self.assertEqual(result["status"], "PROMPTS_READY")
            self.assertIn("forensic workspace", result["prompts"][0]["prompt"])


if __name__ == "__main__":
    unittest.main()
