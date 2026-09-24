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

    def test_asset_manifest_reports_missing_assets(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            images = root / "03_imagens"
            images.mkdir()
            (images / "PROMPTS.md").write_text("01.jpg — cena\n02.jpg — cena\n03.jpg — cena\n", encoding="utf-8")
            (images / "01.jpg").write_bytes(b"asset")
            result = asset_audit(images)
            self.assertEqual(result["status"], "FAIL")
            self.assertEqual(result["missing"], [2, 3])


if __name__ == "__main__":
    unittest.main()
