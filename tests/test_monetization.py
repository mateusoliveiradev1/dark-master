import json
import sys
import tempfile
import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / "scripts"))

from ypp_check import check as ypp_check
from inauthentic_audit import audit as inauthentic_audit


def make_video(root, text, hook_extra=""):
    video = Path(root) / "video01"
    script_dir = video / "01_roteiro"
    script_dir.mkdir(parents=True)
    (script_dir / "narration_v3.txt").write_text(text, encoding="utf-8")
    return video


class YppCheckTests(unittest.TestCase):
    def test_elegivel_2026_nao_2027(self):
        result = ypp_check(1500, 5000, 0, 6, 0, 300)
        self.assertTrue(result["regimes"]["2026"]["eligible_long"])
        self.assertFalse(result["regimes"]["2027"]["eligible_long"])
        self.assertEqual(result["regimes"]["2027"]["hours_gap"], 3000)

    def test_ritmo_diario(self):
        result = ypp_check(1000, 3500, 0, 6, 0, 100)
        self.assertEqual(result["regimes"]["2026"]["daily_watch_hours_needed"], 5.0)

    def test_shorts_nao_contam_para_horas(self):
        result = ypp_check(1000, 100, 15_000_000, 0, 20, 300)
        self.assertFalse(result["regimes"]["2026"]["eligible_long"])
        self.assertTrue(result["regimes"]["2026"]["eligible_shorts"])

    def test_manutencao_minima(self):
        result = ypp_check(2000, 500, 0, 0, 0, 300)
        self.assertFalse(result["maintenance"]["safe"])
        result = ypp_check(2000, 500, 0, 3, 0, 300)
        self.assertTrue(result["maintenance"]["safe"])
        result = ypp_check(2000, 5000, 0, 0, 0, 300)
        self.assertTrue(result["maintenance"]["safe"])


class InauthenticAuditTests(unittest.TestCase):
    TEXT_A = "O relatorio apontou a falha na comporta leste. O engenheiro assinou o laudo em marco."
    TEXT_B = "O relatorio apontou a falha na comporta leste. O engenheiro assinou o laudo em marco."

    def test_swap_test_reprova_template(self):
        with tempfile.TemporaryDirectory() as temp:
            previous = Path(temp) / "canal"
            old = previous / "video00"
            old.mkdir(parents=True)
            (old / "01_roteiro").mkdir()
            (old / "01_roteiro" / "narration_v3.txt").write_text(self.TEXT_A, encoding="utf-8")
            video = make_video(temp, self.TEXT_B)
            result = inauthentic_audit(str(video), str(previous))
            self.assertEqual(result["status"], "FAIL")
            self.assertTrue(any("swap_test" in e for e in result["errors"]))

    def test_primeiro_video_nao_bloqueia(self):
        with tempfile.TemporaryDirectory() as temp:
            video = make_video(temp, "Texto totalmente original sobre o caso do farol apagado.")
            result = inauthentic_audit(str(video), None)
            self.assertIn(result["status"], ("PASS", "REVIEW"))

    def test_sem_pesquisa_primaria_vira_review(self):
        with tempfile.TemporaryDirectory() as temp:
            video = make_video(temp, "Um caso unico com detalhes que ninguem contou ainda hoje.")
            (video / "01_roteiro" / "CLAIMS.json").write_text(
                json.dumps({"claims": [{"id": "C001", "text": "X", "layer": "FATO", "source_ids": ["S001"]}]}),
                encoding="utf-8")
            result = inauthentic_audit(str(video), None)
            self.assertIn("sem_pesquisa_primaria", result["review"])

    def test_persona_ia_em_financas_exige_disclosure(self):
        with tempfile.TemporaryDirectory() as temp:
            video = make_video(temp, "O investimento rendeu juros altos e a carteira de acoes dobrou no trimestre.")
            audio = video / "02_audio"
            audio.mkdir()
            (audio / "voice_contract.json").write_text(json.dumps({"engine": "edge"}), encoding="utf-8")
            result = inauthentic_audit(str(video), None)
            self.assertTrue(any("persona_ia_tema_sensivel" in item for item in result["review"]))


if __name__ == "__main__":
    unittest.main()
