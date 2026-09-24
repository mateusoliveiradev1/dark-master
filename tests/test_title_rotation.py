import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / "scripts"))

from asset_manifest import audit as asset_audit
from rotation_audit import audit as rotation_audit
from title_research import audit as title_audit, extract_titles, load_history


class TitleRotationTests(unittest.TestCase):
    def test_title_research_flags_near_duplicate(self):
        history = ["A porta trancada muda o caso inteiro"]
        result = title_audit(["Uma porta trancada muda o caso inteiro"], history)
        self.assertEqual(result["status"], "FAIL")
        self.assertEqual(result["candidates"][0]["history_similarity"], 1.0)

    def test_title_research_does_not_infer_demand(self):
        result = title_audit(["Um título novo sobre o caso"], [])
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["demand_evidence"], "not_inferred")

    def test_title_research_reads_package_history(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "youtube_package.txt"
            path.write_text("TITLE: A porta trancada\nALT 2: Outro título\n", encoding="utf-8")
            self.assertEqual(extract_titles(path), ["A porta trancada", "Outro título"])

    def test_title_research_keeps_numeric_history_order(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for number, title in ((1, "Antigo"), (2, "Intermediário"), (10, "Recente")):
                episode = root / f"video{number:02d}"
                episode.mkdir()
                (episode / "youtube_package.txt").write_text(f"TITLE: {title}\n", encoding="utf-8")
            self.assertEqual(load_history(root, 2), ["Intermediário", "Recente"])

    def test_rotation_audit_uses_last_three_and_blocks_near_duplicate(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            previous = root / "previous"
            current = root / "current" / "video04"
            for number in (1, 2, 3):
                episode = previous / f"video{number:02d}"
                script = episode / "01_roteiro"
                script.mkdir(parents=True)
                (episode / "youtube_package.txt").write_text("TITLE: O mesmo caso e a mesma promessa\n", encoding="utf-8")
                (script / "narration_v3.txt").write_text("A porta estava trancada. A prova muda o caso e ninguém encontra uma resposta.\n\nA pergunta continua aberta.\n", encoding="utf-8")
                (script / "ROTEIRO_MAP.json").write_text(json.dumps({"blocks": [
                    {"id": "B001", "beat": "HOOK"},
                    {"id": "B002", "beat": "CONTEXTO"},
                    {"id": "B003", "beat": "PAYOFF"},
                ]}), encoding="utf-8")
            current_script = current / "01_roteiro"
            current_script.mkdir(parents=True)
            (current / "youtube_package.txt").write_text("TITLE: O mesmo caso e a mesma promessa\n", encoding="utf-8")
            (current_script / "narration_v3.txt").write_text("A porta estava trancada. A prova muda o caso e ninguém encontra uma resposta.\n\nA pergunta continua aberta.\n", encoding="utf-8")
            (current_script / "ROTEIRO_MAP.json").write_text(json.dumps({"blocks": [
                {"id": "B001", "beat": "HOOK"},
                {"id": "B002", "beat": "CONTEXTO"},
                {"id": "B003", "beat": "PAYOFF"},
            ]}), encoding="utf-8")
            result = rotation_audit(current, previous)
            self.assertEqual(result["status"], "FAIL")
            self.assertEqual(result["scope"], "last_three_episodes")
            self.assertTrue(result["issues"])

    def test_asset_manifest_rejects_numeric_index_fallback(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            images = root / "video01" / "03_imagens"
            script = root / "video01" / "01_roteiro"
            images.mkdir(parents=True)
            script.mkdir(parents=True)
            (images / "01.jpg").write_bytes(b"asset")
            plan = {
                "status": "PROMPTS_READY",
                "prompts": [
                    {"promptId": "PROMPT-B001", "shotId": "SHOT-B001", "sourceBlockIds": ["B001"]},
                    {"promptId": "PROMPT-B002", "shotId": "SHOT-B002", "sourceBlockIds": ["B002"]},
                ],
            }
            (script / "PROMPT_PLAN.json").write_text(json.dumps(plan), encoding="utf-8")
            result = asset_audit(images)
            self.assertEqual(result["status"], "FAIL")
            self.assertEqual(result["reason"], "identity_resolution_failed")
            self.assertIn("identity_manifest_required", result["errors"])

    def test_asset_manifest_preserves_identity_hash_rights_and_blocked_state(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            images = root / "video01" / "03_imagens"
            script = root / "video01" / "01_roteiro"
            images.mkdir(parents=True)
            script.mkdir(parents=True)
            blocked_path = images / "blocked.jpg"
            blocked_path.write_bytes(b"blocked")
            available_path = images / "01.jpg"
            available_path.write_bytes(b"available")
            available_hash = hashlib.sha256(available_path.read_bytes()).hexdigest()
            plan = {
                "status": "PROMPTS_READY",
                "prompts": [
                    {"promptId": "PROMPT-B001", "shotId": "SHOT-B001", "sourceBlockIds": ["B001"]},
                    {"promptId": "PROMPT-B002", "shotId": "SHOT-B002", "sourceBlockIds": ["B002"]},
                ],
            }
            (script / "PROMPT_PLAN.json").write_text(json.dumps(plan), encoding="utf-8")
            manifest = {
                "version": 1,
                "assets": [
                    {
                        "assetId": "A-B001",
                        "promptId": "PROMPT-B001",
                        "shotId": "SHOT-B001",
                        "sourceBlockIds": ["B001"],
                        "path": "blocked.jpg",
                        "hash": hashlib.sha256(b"blocked").hexdigest(),
                        "rightsStatus": "licensed",
                        "blocked": True,
                    },
                    {
                        "assetId": "A-B002",
                        "promptId": "PROMPT-B002",
                        "shotId": "SHOT-B002",
                        "sourceBlockIds": ["B002"],
                        "path": "01.jpg",
                        "hash": available_hash,
                        "rightsStatus": "licensed",
                        "blocked": False,
                    },
                ],
            }
            (images / "ASSET_MANIFEST.json").write_text(json.dumps(manifest), encoding="utf-8")
            result = asset_audit(images)
            self.assertEqual(result["status"], "FAIL")
            self.assertEqual(result["missing"], ["PROMPT-B001"])
            self.assertEqual(result["blocked"], ["A-B001"])
            blocked = next(asset for asset in result["assets"] if asset["assetId"] == "A-B001")
            available = next(asset for asset in result["assets"] if asset["assetId"] == "A-B002")
            self.assertEqual(blocked["hash"], manifest["assets"][0]["hash"])
            self.assertEqual(blocked["rightsStatus"], "licensed")
            self.assertTrue(blocked["blocked"])
            self.assertEqual(blocked["sourceBlockIds"], ["B001"])
            self.assertEqual(available["hash"], available_hash)
            self.assertEqual(available["status"], "PRESENT")


if __name__ == "__main__":
    unittest.main()
