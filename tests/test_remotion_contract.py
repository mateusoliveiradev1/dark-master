import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import remotion
import visual_plan
import visual_review
from test_visual_plan import VisualPlanTests


class RemotionContractTests(unittest.TestCase):
    def test_srt_seconds_parses_milliseconds(self):
        self.assertEqual(remotion.srt_seconds("00:01:02,250"), 62.25)

    def test_block_type_maps_editorial_beats(self):
        self.assertEqual(remotion.block_type({"beat": "EVIDÊNCIAS"}), "evidence-reveal")
        self.assertEqual(remotion.block_type({"beat": "LINHA DO TEMPO"}), "timeline")

    def test_theme_keeps_channel_values(self):
        theme = remotion.theme_from_style({"background": "#112233", "accent": "#445566"})
        self.assertEqual(theme["background"], "#112233")
        self.assertEqual(theme["accent"], "#445566")
        self.assertEqual(theme["safeArea"], {"x": 72, "y": 54})

    def test_scene_blocks_bind_motion_contract_to_case_identity(self):
        with tempfile.TemporaryDirectory() as temp:
            episode = Path(temp) / "video01"
            script = episode / "01_roteiro"
            script.mkdir(parents=True)
            (script / "ROTEIRO_MAP.json").write_text(json.dumps({
                "blocks": [{
                    "id": "B001",
                    "beat": "PERICIA",
                    "question": "O que o laudo limita?",
                    "state_change": "A conclusão deixa de ser definitiva.",
                    "target_seconds": 8,
                }]
            }, ensure_ascii=False), encoding="utf-8")
            spec = {
                "shotId": "SHOT-B001",
                "promptId": "PROMPT-B001",
                "sourceBlockIds": ["B001"],
                "claimIds": ["C001"],
                "sourceIds": ["S001"],
                "purpose": "limitar a conclusão",
                "question": "O que o laudo limita?",
                "stateChange": "A conclusão deixa de ser definitiva.",
                "classification": "FATO",
                "subject": "lacre de tubo sem rótulo",
                "setting": "laboratório de 1978",
                "composition": "close documental no lacre",
                "layers": ["environment", "subject", "state-change"],
                "cropPolicy": {"masterAspect": "16:9", "long": {"focalPoint": [0.5, 0.45]}, "short": {"focalPoint": [0.5, 0.42], "dedicatedReframeRequired": True}},
                "safeAreas": {"long": {"action": [0, 0, 1, 1]}, "short": {"action": [0, 0, 1, 1]}},
                "negativeGuards": ["no baked-in text"],
                "continuity": {"evidenceTreatment": "documented reconstruction only"},
                "imagePrompt": {"full": "IMAGE_PROMPT"},
                "motionPrompt": {
                    "cameraPath": {"description": "move to the sealed tube"},
                    "transitions": {"in": "cut", "out": "dissolve"},
                },
                "states": [{"id": "focus", "timeRange": [0, 1], "motion": "detail-reveal"}],
            }
            scene = remotion.scene_blocks(episode, 8, "long", [spec])[0]
            self.assertEqual(scene["id"], "SHOT-B001")
            self.assertEqual(scene["shotId"], "SHOT-B001")
            self.assertEqual(scene["promptId"], "PROMPT-B001")
            self.assertEqual(scene["motionVariant"], "detail-reveal")
            self.assertEqual(scene["transitionIn"], "cut")
            self.assertEqual(scene["transitionOut"], "dissolve")
            self.assertEqual(scene["sourceIds"], ["S001"])
            self.assertEqual(scene["motionPrompt"], spec["motionPrompt"])

    def test_build_plan_resolves_assets_by_identity(self):
        with tempfile.TemporaryDirectory() as temp:
            episode, visual_path = VisualPlanTests().make_episode(temp)
            prompt_plan = visual_plan.init_artifacts(episode, visual_path)
            binding = prompt_plan["prompts"][0]["assetBindings"][0]
            image_path = episode / "03_imagens" / "case-evidence.jpg"
            image_path.write_bytes(b"case-evidence")
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
                    "blocked": False,
                    "role": "primary",
                }],
            }
            (episode / "03_imagens" / "ASSET_MANIFEST.json").write_text(json.dumps(manifest), encoding="utf-8")
            contracts = {
                "style": json.loads(visual_path.read_text(encoding="utf-8")),
                "motion": {"engine": "remotion", "size": [1920, 1080], "fps": 30},
            }
            with self.assertRaises(ValueError):
                remotion.build_plan(episode, "Caso-Teste", "long", contracts)
            plan = remotion.build_plan(episode, "Caso-Teste", "long", contracts, allow_incomplete=True)
            self.assertTrue(plan["diagnostic"])
            scene = plan["scenes"][0]
            self.assertEqual(scene["assets"][0]["assetId"], binding["assetId"])
            self.assertEqual(scene["assets"][0]["promptId"], binding["promptId"])
            self.assertEqual(scene["assets"][0]["shotId"], binding["shotId"])
            self.assertEqual(scene["assets"][0]["hash"], image_hash)
            self.assertEqual(scene["assets"][0]["sourceBlockIds"], ["B001"])
            self.assertEqual(scene["asset"], f"images/{binding['assetId']}.jpg")
            self.assertEqual(scene["motionPrompt"]["intensity"], 2)

    def test_visual_review_rejects_camera_only_state_sequence(self):
        audit = visual_review.audit_scene_motion({
            "states": [
                {"id": "entry", "assetIds": ["A"], "visibleLayers": ["evidence"], "motion": "slow-push"},
                {"id": "focus", "assetIds": ["A"], "visibleLayers": ["evidence"], "motion": "controlled-crop"},
            ],
            "motionPrompt": {"staticException": {"allowed": False}},
        })
        self.assertEqual(audit["status"], "FAIL")
        self.assertEqual(audit["reason"], "static_frame_guard")

    def test_stage_assets_uses_explicit_asset_identity(self):
        with tempfile.TemporaryDirectory() as temp:
            episode = Path(temp) / "video01"
            images = episode / "03_imagens"
            public = episode / "04_video_final" / "_remotion" / "public"
            images.mkdir(parents=True)
            (images / "wrong-order.jpg").write_bytes(b"first")
            (images / "right-order.jpg").write_bytes(b"second")
            records = [
                {"assetId": "A-B002", "promptId": "PROMPT-B002", "shotId": "SHOT-B002", "path": "right-order.jpg", "blocked": False},
                {"assetId": "A-B001", "promptId": "PROMPT-B001", "shotId": "SHOT-B001", "path": "wrong-order.jpg", "blocked": False},
            ]
            _, staged, _ = remotion.stage_assets(episode, public, None, {}, records)
            self.assertEqual(set(staged), {"A-B001", "A-B002"})
            self.assertEqual(staged["A-B001"].name, "A-B001.jpg")
            self.assertEqual(staged["A-B002"].name, "A-B002.jpg")


if __name__ == "__main__":
    unittest.main()
