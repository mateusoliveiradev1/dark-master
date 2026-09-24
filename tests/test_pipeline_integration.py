import hashlib
import json
import sys
import tempfile
import unittest
import wave
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

SKILL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / "scripts"))
sys.path.insert(0, str(SKILL / "tests"))

import orchestrate
import remotion
import visual_review
import visual_plan
from test_visual_plan import VisualPlanTests


class PipelineIntegrationTests(unittest.TestCase):
    def make_episode(self, root, blocked=False):
        episode, visual_path = VisualPlanTests().make_episode(root)
        (episode / "02_audio").mkdir(exist_ok=True)
        (episode / "01_roteiro" / "VISUAL_BIBLE.json").write_text(visual_path.read_text(encoding="utf-8"), encoding="utf-8")
        prompt_plan = visual_plan.init_artifacts(episode, visual_path)
        binding = prompt_plan["prompts"][0]["assetBindings"][0]
        image_path = episode / "03_imagens" / "case-evidence.jpg"
        image_path.write_bytes(b"blocked-evidence" if blocked else b"case-evidence")
        image_hash = hashlib.sha256(image_path.read_bytes()).hexdigest()
        manifest = {
            "version": 1,
            "assets": [{
                "assetId": binding["assetId"],
                "promptId": binding["promptId"],
                "shotId": binding["shotId"],
                "sourceBlockIds": binding["sourceBlockIds"],
                "path": image_path.name,
                "hash": image_hash,
                "rightsStatus": "licensed",
                "blocked": blocked,
                "role": "primary",
            }],
        }
        (episode / "03_imagens" / "ASSET_MANIFEST.json").write_text(json.dumps(manifest), encoding="utf-8")
        (episode / "03_imagens" / "IMAGE_AUDIT.json").write_text(json.dumps({"status": "PASS"}), encoding="utf-8")
        (episode / "01_roteiro" / "TIMING_AUDIT.json").write_text(json.dumps({"status": "PASS"}), encoding="utf-8")
        (episode / "02_audio" / "captions.srt").write_text("1\n00:00:00,000 --> 00:00:04,000\nUma frase.\n", encoding="utf-8")
        with wave.open(str(episode / "02_audio" / "voice_FINAL.wav"), "wb") as handle:
            handle.setnchannels(1)
            handle.setsampwidth(2)
            handle.setframerate(8000)
            handle.writeframes(b"\0" * (8000 * 4 * 2))
        contracts = {
            "style": json.loads(visual_path.read_text(encoding="utf-8")),
            "motion": {"engine": "remotion", "size": [1920, 1080], "fps": 30},
            "voice": {"engine": "edge"},
            "roteiro": {},
        }
        return episode, contracts, binding

    def test_existing_channel_bypasses_niche_and_outliers(self):
        with tempfile.TemporaryDirectory() as temp:
            plan = orchestrate.build_orchestration_plan(temp, "video01", channel_state="existing")
            self.assertNotIn("niche", plan["steps"])
            self.assertNotIn("outliers", plan["steps"])
            new_plan = orchestrate.build_orchestration_plan(temp, "video01", channel_state="new")
            self.assertEqual(new_plan["steps"][:2], ["niche", "outliers"])

    def test_missing_gate_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            episode, contracts, _ = self.make_episode(temp)
            prompt_path = episode / "01_roteiro" / "PROMPT_PLAN.json"
            prompt = json.loads(prompt_path.read_text(encoding="utf-8"))
            prompt["status"] = "NEEDS_ART_DIRECTION"
            prompt_path.write_text(json.dumps(prompt), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "production_gates_failed"):
                remotion.build_plan(episode, "existing", "long", contracts)
            diagnostic = remotion.build_plan(episode, "existing", "long", contracts, allow_incomplete=True)
            self.assertTrue(diagnostic["diagnostic"])
            self.assertFalse(diagnostic["releaseEligible"])

    def test_stale_staging_is_not_reused(self):
        with tempfile.TemporaryDirectory() as temp:
            episode, contracts, _ = self.make_episode(temp)
            first = remotion.build_plan(episode, "existing", "long", contracts)
            first_public = episode / first["staging"]["publicDir"]
            stale = first_public / "images" / "stale.jpg"
            stale.write_bytes(b"stale")
            second = remotion.build_plan(episode, "existing", "long", contracts)
            second_public = episode / second["staging"]["publicDir"]
            self.assertNotEqual(first_public, second_public)
            self.assertFalse((second_public / "images" / "stale.jpg").exists())
            self.assertEqual(remotion.staging_integrity(second, episode)["status"], "PASS")

    def test_visual_review_emits_three_stills_and_contact_sheets(self):
        with tempfile.TemporaryDirectory() as temp:
            episode, contracts, _ = self.make_episode(temp)
            plan = remotion.build_plan(episode, "existing", "long", contracts)
            from PIL import Image

            def fake_still(plan_path, public_dir, composition_id, frame, output):
                output.parent.mkdir(parents=True, exist_ok=True)
                Image.new("RGB", (32, 18), "black").save(output)
                return output

            with mock.patch.object(visual_review, "run_still", side_effect=fake_still):
                manifest = visual_review.run(episode / "01_roteiro" / "RENDER_PLAN_LONG.json", "long", False)
            self.assertEqual(manifest["status"], "REVIEW_REQUIRED")
            self.assertEqual([item["sample"] for item in manifest["samples"]], ["F0", "F50", "F100"])
            self.assertEqual(len(manifest["contactSheets"]), 2)
            self.assertTrue(manifest["samples"][0]["hash"])
            self.assertEqual(remotion.review_gate(episode, "long")["status"], "FAIL")

    def test_run_hash_and_independent_receipt(self):
        with tempfile.TemporaryDirectory() as temp:
            episode, contracts, _ = self.make_episode(temp)
            plan = remotion.build_plan(episode, "existing", "long", contracts)
            plan_file = episode / "01_roteiro" / "RENDER_PLAN_LONG.json"
            run_dir = remotion.run_dir_from_plan(plan, episode)
            run = remotion.run_ledger.load_run(run_dir)
            self.assertEqual(run["planHash"], remotion.sha256(plan_file))
            self.assertEqual(run["profileHash"], plan["profileHash"])
            self.assertEqual(run["profileHash"], remotion.sha256(episode / "01_roteiro" / "VISUAL_BIBLE.json"))
            self.assertTrue(run["versions"]["node"])
            sample = run_dir / "review" / "sample.png"
            sample.parent.mkdir(parents=True, exist_ok=True)
            sample.write_bytes(b"sample")
            manifest = {
                "status": "REVIEW_REQUIRED",
                "plan": str(plan_file),
                "planHash": remotion.sha256(plan_file),
                "runId": plan["runId"],
                "format": "long",
                 "receipt": str(episode / "01_roteiro" / "VISUAL_REVIEW_RECEIPT_LONG.json"),
                 "staticGuard": "SEMANTIC_MOTION_BOUND",
                 "motionAudit": {"status": "PASS", "sceneCount": 1, "meaningfulChangeCount": 4},
                 "samples": [

                    {"sceneId": "SHOT-B001", "sample": label, "path": str(sample)}
                    for label in ("F0", "F50", "F100")
                ],
                "contactSheets": [
                    {"sceneId": "SHOT-B001", "path": str(sample)},
                    {"sequence": True, "path": str(sample)},
                ],
            }
            manifest_file = episode / "01_roteiro" / "VISUAL_REVIEW_LONG.json"
            manifest_file.write_text(json.dumps(manifest), encoding="utf-8")
            receipt = visual_review.register_receipt(manifest_file, reviewer="independent-reviewer", score=95, findings=["minor polish"])
            self.assertEqual(receipt["planHash"], remotion.sha256(plan_file))
            self.assertEqual(remotion.review_gate(episode, "long", plan_file)["status"], "PASS")
            plan_file.write_text(plan_file.read_text(encoding="utf-8") + "\n", encoding="utf-8")
            self.assertEqual(remotion.review_gate(episode, "long", plan_file)["status"], "FAIL")

    def test_blocked_asset_is_rejected_and_not_staged(self):
        with tempfile.TemporaryDirectory() as temp:
            episode, contracts, _ = self.make_episode(temp, blocked=True)
            with self.assertRaisesRegex(ValueError, "production_gates_failed"):
                remotion.build_plan(episode, "existing", "long", contracts)
            images = episode / "03_imagens"
            public = episode / "04_video_final" / "blocked-staging" / "public"
            records, _ = remotion.asset_tools.load_asset_records(images, episode / "01_roteiro" / "PROMPT_PLAN.json")
            remotion.stage_assets(episode, public, None, {}, records)
            ledger = json.loads((public / "asset_ledger.json").read_text(encoding="utf-8"))
            self.assertEqual(ledger["assets"], [])

    def test_final_audit_rejects_output_from_another_run(self):
        with tempfile.TemporaryDirectory() as temp:
            episode, contracts, _ = self.make_episode(temp)
            plan = remotion.build_plan(episode, "existing", "long", contracts)
            plan_file = episode / "01_roteiro" / "RENDER_PLAN_LONG.json"
            output = remotion.expected_output_path(episode, "long")
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes(b"output")
            report = {
                "status": "PASS",
                "engine": "remotion",
                "runId": "another-run",
                "output": str(output),
                "outputs": {str(output): remotion.sha256(output)},
                "plan": str(plan_file),
                "planHash": remotion.sha256(plan_file),
                "profileHash": plan["profileHash"],
                "inputHash": plan["inputHash"],
                "outputHash": remotion.sha256(output),
            }
            (episode / "01_roteiro" / "RENDER_REPORT_LONG.json").write_text(json.dumps(report), encoding="utf-8")
            with mock.patch.object(remotion, "ffprobe_duration", return_value=1.0):
                result = remotion.audit_render_outputs(episode)
            self.assertEqual(result["status"], "FAIL")
            self.assertTrue(any("render_run_id_mismatch" in error for error in result["errors"]))

    def test_render_rejects_existing_output_conflict(self):
        with tempfile.TemporaryDirectory() as temp:
            episode, _, _ = self.make_episode(temp)
            output = remotion.expected_output_path(episode, "long")
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes(b"existing")
            args = SimpleNamespace(root=temp, episode=episode.name, channel=None, format="long", overwrite=False)
            self.assertEqual(remotion.render_command(args), 1)
            self.assertEqual(output.read_bytes(), b"existing")


if __name__ == "__main__":
    unittest.main()
