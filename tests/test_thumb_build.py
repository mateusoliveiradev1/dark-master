import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / "scripts"))

from thumb_build import build


class ThumbBuildTests(unittest.TestCase):
    def make_episode(self, root):
        episode = Path(root) / "video01"
        roteiro = episode / "01_roteiro"
        roteiro.mkdir(parents=True)
        brief = json.loads((SKILL / "templates" / "thumb_brief.json").read_text(encoding="utf-8"))
        brief["episode"] = "video01"
        (roteiro / "THUMB_BRIEF.json").write_text(json.dumps(brief, ensure_ascii=False), encoding="utf-8")
        return episode, roteiro / "THUMB_BRIEF.json"

    def test_build_gera_variantes_auditadas_e_vencedor(self):
        with tempfile.TemporaryDirectory() as temp:
            episode, brief_path = self.make_episode(temp)
            report = build(str(brief_path), None, "TITULO PT vencedor | Winner EN title")
            self.assertIn(report["status"], ("PASS", "REVIEW"), report)
            self.assertEqual(len(report["concepts"]), 2)
            final_dir = episode / "04_video_final"
            for item in report["concepts"]:
                image = final_dir / item["image"]
                self.assertTrue(image.exists())
                self.assertLessEqual(image.stat().st_size, 2 * 1024 * 1024)
                self.assertTrue((final_dir / item["preview"]).exists())
            self.assertTrue((final_dir / "thumb_contact_sheet.jpg").exists())
            self.assertTrue((final_dir / "THUMB_BUILD.json").exists())
            brief = json.loads(brief_path.read_text(encoding="utf-8"))
            self.assertTrue(brief.get("image", "").endswith(report["winner"] and f"thumb_{report['winner']}.jpg"))

    def test_build_mede_contraste_acima_do_piso(self):
        with tempfile.TemporaryDirectory() as temp:
            episode, brief_path = self.make_episode(temp)
            report = build(str(brief_path), None, "TITULO PT vencedor | Winner EN title")
            for item in report["concepts"]:
                self.assertGreaterEqual(item["contrast"]["white"], 3.0)

    def test_build_reprova_overlay_repetido(self):
        with tempfile.TemporaryDirectory() as temp:
            episode, brief_path = self.make_episode(temp)
            brief = json.loads(brief_path.read_text(encoding="utf-8"))
            brief["concepts"][0]["text_pt"] = "TITULO PT vencedor repetido aqui agora"
            brief_path.write_text(json.dumps(brief, ensure_ascii=False), encoding="utf-8")
            report = build(str(brief_path), None, "TITULO PT vencedor | Winner EN title")
            concept = next(item for item in report["concepts"] if item["id"] == brief["concepts"][0]["id"])
            self.assertEqual(concept["audit"], "FAIL")
            self.assertTrue(any("repete_titulo" in e or "palavras" in e for e in concept["errors"]))


if __name__ == "__main__":
    unittest.main()
