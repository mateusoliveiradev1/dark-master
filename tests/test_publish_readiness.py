import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

SKILL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / "scripts"))
sys.path.insert(0, str(SKILL / "templates"))

from publish_readiness import disclosure_status, readiness_from, winner_titles


class PublishReadinessTests(unittest.TestCase):
    def test_ready_quando_tudo_ok(self):
        audit = {"veredito": "PASSOU", "flags": [], "gates": {}}
        result = readiness_from(audit, {"status": "PASS"}, "human_voice")
        self.assertEqual(result["status"], "READY")

    def test_bloqueia_flag_pair_e_disclosure(self):
        audit = {"veredito": "PASSOU", "flags": [], "gates": {}}
        result = readiness_from(audit, {"status": "FAIL"}, "synthetic_undeclared")
        self.assertEqual(result["status"], "BLOCKED")
        self.assertIn("strict_pair", result["blockers"])
        self.assertIn("disclosure", result["blockers"])

    def test_bloqueia_flag_do_audit(self):
        audit = {"veredito": "FALHA", "flags": ["audio"], "gates": {}}
        result = readiness_from(audit, {"status": "PASS"}, "declared")
        self.assertEqual(result["status"], "BLOCKED")
        self.assertIn("audio", result["blockers"])

    def test_winner_titles_do_packaging(self):
        with tempfile.TemporaryDirectory() as temp:
            packaging = Path(temp) / "PACKAGING.json"
            packaging.write_text(json.dumps({
                "pairs": [{"id": "P1", "title": {"pt": "Titulo Um", "en": "Title One"}},
                          {"id": "P2", "title": {"pt": "Titulo Dois", "en": "Title Two"}}],
                "decision": {"winner_id": "P2"}}), encoding="utf-8")
            self.assertEqual(winner_titles(str(packaging)), ["Titulo Dois", "Title Two"])
            self.assertEqual(winner_titles(str(Path(temp) / "ausente.json")), [])

    def test_disclosure_status(self):
        with tempfile.TemporaryDirectory() as temp:
            video = Path(temp) / "video01"
            (video / "01_roteiro").mkdir(parents=True)
            self.assertEqual(disclosure_status(video), "unknown")
            (video / "02_audio").mkdir()
            (video / "02_audio" / "voice_contract.json").write_text(
                json.dumps({"engine": "edge"}), encoding="utf-8")
            self.assertEqual(disclosure_status(video), "synthetic_undeclared")
            (video / "DISCLOSURE_IA.txt").write_text("voz edge-tts, rosto IA: nao", encoding="utf-8")
            self.assertEqual(disclosure_status(video), "declared")


if __name__ == "__main__":
    unittest.main()
