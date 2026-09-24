import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import visual_plan


class VisualPlanTests(unittest.TestCase):
    def make_episode(self, root, complete_research=True):
        episode = Path(root) / "video01"
        script_dir = episode / "01_roteiro"
        script_dir.mkdir(parents=True)
        (episode / "03_imagens").mkdir()
        if not complete_research:
            (script_dir / "ROTEIRO_MAP.json").write_text(json.dumps({
                "blocks": [{
                    "id": "B001",
                    "beat": "HOOK",
                    "text": "Uma porta aparece.",
                    "claim_ids": [],
                    "question": "O que aparece?",
                    "state_change": "A porta entra no caso.",
                    "target_seconds": 4,
                }]
            }, ensure_ascii=False), encoding="utf-8")
            return episode, None
        (script_dir / "PESQUISA_BRIEF.md").write_text(
            "# BRIEF DE PESQUISA — Caso do Medidor\n\n"
            "## Caso\n- Pergunta central: Por que o medidor lacustre diverge do registro de 1978?\n"
            "- Ângulo editorial: contrasting equipment readings.\n\n"
            "## Plano narrativo\n- A divergência do medidor organiza a reconstrução.\n",
            encoding="utf-8",
        )
        (script_dir / "PESQUISA_FONTE.md").write_text(
            "| ID | Camada | Fonte | URL | Localizador | Limitações |\n"
            "|---|---|---|---|---|---|\n"
            "| S001 | FATO | Laudo do medidor 1978 | fonte://medidor/1978 | p. 12 | nenhuma |\n",
            encoding="utf-8",
        )
        (script_dir / "CLAIMS.json").write_text(json.dumps({
            "case_id": "MEDIDOR-1978",
            "claims": [{
                "id": "C001",
                "text": "O medidor lacustre registrou dezoito graus enquanto o arquivo anotava vinte e dois.",
                "layer": "FATO",
                "source_ids": ["S001"],
                "locator": "p. 12",
                "primary_source": True,
                "confidence": "ALTA",
            }],
        }, ensure_ascii=False), encoding="utf-8")
        (script_dir / "LINHA_DO_TEMPO.md").write_text(
            "| data | fato | camada | fonte |\n|---|---|---|---|\n"
            "| 1978-04-11 | O medidor lacustre foi retirado da escala | FATO | S001 |\n",
            encoding="utf-8",
        )
        (script_dir / "ROTEIRO_MAP.json").write_text(json.dumps({
            "case_id": "Caso do Medidor",
            "blocks": [{
                "id": "B001",
                "beat": "HOOK",
                "text": "Duas leituras do mesmo medidor não podem coexistir sem explicação.",
                "claim_ids": ["C001"],
                "question": "Por que o medidor lacustre diverge do arquivo de 1978?",
                "state_change": "A divergência entre dezoito e vinte e dois graus torna a escala do lago-fi.",
                "target_seconds": 4,
            }],
        }, ensure_ascii=False), encoding="utf-8")
        visual = Path(root) / "visual.json"
        visual.write_text(json.dumps({
            "channel": "Caso-Teste",
            "version": 2,
            "palette": {"background": "#08090B", "surface": "#17191D", "text": "#F4F1EA", "muted": "#9A9CA3", "accent": "#B33A2E", "evidence": "#D6A43B"},
            "typography": {"heading": "Arial", "body": "Arial"},
            "safeAreas": visual_plan.DEFAULT_VISUAL["safeAreas"],
            "image": {"negativeGuards": visual_plan.DEFAULT_VISUAL["image"]["negativeGuards"]},
            "motion": visual_plan.DEFAULT_VISUAL["motion"],
            "qa": visual_plan.DEFAULT_VISUAL["qa"],
        }, ensure_ascii=False), encoding="utf-8")
        return episode, visual

    def test_init_creates_gated_artifacts_without_research_fallback(self):
        with tempfile.TemporaryDirectory() as temp:
            episode, _ = self.make_episode(temp, complete_research=False)
            result = visual_plan.init_artifacts(episode)
            self.assertEqual(result["status"], "NEEDS_ART_DIRECTION")
            self.assertEqual(len(result["prompts"]), 1)
            self.assertIn("research_missing:PESQUISA_BRIEF", result["errors"])
            self.assertIn("research_missing:PESQUISA_FONTE", result["errors"])
            self.assertIn("research_missing:CLAIMS", result["errors"])
            self.assertIn("research_missing:LINHA_DO_TEMPO", result["errors"])
            self.assertIn("visual_contract_missing", result["errors"])
            self.assertTrue((episode / "01_roteiro" / "SHOT_SPECS.json").exists())
            self.assertTrue((episode / "01_roteiro" / "PROMPT_PLAN.json").exists())
            self.assertTrue((episode / "03_imagens" / "PROMPTS.md").exists())

    def test_case_bound_image_and_motion_contracts_are_ready_and_deterministic(self):
        with tempfile.TemporaryDirectory() as temp:
            episode, visual = self.make_episode(temp)
            result = visual_plan.init_artifacts(episode, visual)
            self.assertEqual(result["status"], "PROMPTS_READY", result["errors"])
            shot = result["shots"][0]
            for field in visual_plan.REQUIRED_SCENE_FIELDS:
                self.assertIn(field, shot)
            self.assertEqual(shot["claimIds"], ["C001"])
            self.assertEqual(shot["sourceIds"], ["S001"])
            self.assertEqual(shot["classification"], "FATO")
            self.assertIn("dezoito graus", shot["imagePrompt"]["full"])
            self.assertIn("Laudo do medidor 1978", shot["imagePrompt"]["full"])
            self.assertIn("Por que o medidor lacustre", shot["imagePrompt"]["full"])
            self.assertIn("no baked-in text", shot["imagePrompt"]["full"])
            self.assertIn("documented reconstruction only", " ".join(shot["negativeGuards"]))
            motion = shot["motionPrompt"]
            self.assertIsInstance(motion["intensity"], int)
            self.assertTrue(0 <= motion["intensity"] <= 4)
            self.assertEqual(motion["states"][0]["timeRange"][0], 0)
            self.assertEqual(motion["states"][-1]["timeRange"][1], 100)
            self.assertIn(shot["subject"], motion["cameraPath"]["description"])
            self.assertIn(shot["stateChange"], motion["cameraPath"]["description"])
            self.assertTrue(motion["audioCues"])
            self.assertIn("allowed", motion["staticException"])
            self.assertIn("no generic zoom used as the only motion", motion["negativeMotion"])
            self.assertNotEqual(motion["full"], shot["imagePrompt"]["full"])
            self.assertEqual(len(shot["states"]), 5)
            self.assertTrue(all(state["assetIds"] for state in shot["states"]))
            self.assertTrue(any(state["motion"] not in {"slow-push", "lateral-drift", "controlled-crop", "static-hold"} for state in shot["states"]))
            serialized = json.dumps({"image": shot["imagePrompt"], "motion": motion}, ensure_ascii=False).lower()
            for token in ("[preencher", "placeholder", "tbd", "a concrete documentary subject", "the correct time of day"):
                self.assertNotIn(token, serialized)
            first = (episode / "01_roteiro" / "PROMPT_PLAN.json").read_text(encoding="utf-8")
            visual_plan.compile_prompt_plan(episode, visual)
            second = (episode / "01_roteiro" / "PROMPT_PLAN.json").read_text(encoding="utf-8")
            self.assertEqual(first, second)

    def test_state_asset_binding_preserves_layer_and_supporting_asset(self):
        shot = visual_plan.default_shot({
            "id": "B-LAYER",
            "beat": "EVIDÊNCIAS",
            "question": "O que aparece?",
            "state_change": "A prova entra em foco.",
            "classification": "FATO",
            "subject": "selo de arquivo",
            "setting": "sala de arquivo",
            "layers": ["environment", "evidence", "continuity"],
            "assets": {
                "primary": [{"assetId": "A-ENV", "layer": "environment", "role": "primary"}],
                "supporting": [{"assetId": "A-EVIDENCE", "layer": "evidence", "role": "supporting"}],
            },
        }, 1, [], {}, None)
        self.assertEqual(shot["assets"][0]["layer"], "environment")
        self.assertEqual(shot["assets"][1]["layer"], "evidence")
        self.assertIn("A-ENV", shot["states"][0]["assetIds"])
        self.assertIn("A-EVIDENCE", shot["states"][0]["assetIds"])
        self.assertIn("A-EVIDENCE", shot["states"][-1]["assetIds"])

    def test_generic_camera_path_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            episode, visual = self.make_episode(temp)
            visual_plan.init_artifacts(episode, visual)
            specs_path = episode / "01_roteiro" / "SHOT_SPECS.json"
            specs = json.loads(specs_path.read_text(encoding="utf-8"))
            specs["shots"][0]["motionPrompt"]["cameraPath"] = {
                "kind": "push-in",
                "description": "zoom and fade",
                "keyframes": [],
            }
            specs_path.write_text(json.dumps(specs, ensure_ascii=False), encoding="utf-8")
            result = visual_plan.compile_prompt_plan(episode, visual, specs_path)
            self.assertEqual(result["status"], "NEEDS_ART_DIRECTION")
            self.assertTrue(any("generic_camera_path" in error for error in result["errors"]))


if __name__ == "__main__":
    unittest.main()
