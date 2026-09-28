import sys
import tempfile
import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / "scripts"))

from packaging_audit import audit as packaging_audit
from thumb_audit import audit as thumb_audit
import short_qa


def make_pair(pid, title_pt, title_en, overlay_pt, overlay_en, short="Payoff em oito palavras aqui agora"):
    return {
        "id": pid,
        "formula": "Y1",
        "goal": "browse",
        "title": {"pt": title_pt, "en": title_en},
        "thumb": {
            "text_pt": overlay_pt,
            "text_en": overlay_en,
            "concept": "angulo que vende",
            "focal": "objeto unico",
            "background": "fundo escuro BOGY",
            "composition": "tercos",
            "variants_axis": "face-vs-objeto",
        },
        "hook": {"long30s": "Cumpre a promessa e abre um loop.", "short3s": short},
        "evidence": {"urls": ["https://example.com/video (data: 2026-09-28)"]},
    }


def make_packaging(pairs, winner="P1", alternatives=None, human="humano"):
    return {
        "version": 1,
        "episode": "video01",
        "channel": "canal-teste",
        "model": "generic",
        "market": {"primary": "pt-BR", "secondary": "en"},
        "pairs": pairs,
        "decision": {"winner_id": winner, "alternatives": alternatives or ["P2"], "human": human, "date": "2026-09-28"},
    }


def make_concept(cid, overlay_pt, overlay_en, axis="face-vs-objeto"):
    return {
        "id": cid,
        "angle": "angulo que vende",
        "focal": "objeto unico",
        "text_pt": overlay_pt,
        "text_en": overlay_en,
        "position": "terco oposto",
        "background": "fundo escuro BOGY",
        "composition": "tercos",
        "note_120px": "numero legivel a 120px",
        "variant_axis": axis,
    }


class PackagingBubblesTests(unittest.TestCase):
    def test_packaging_pass_bilingue_sem_repeticao(self):
        pairs = [
            make_pair("P1", "O cofre de 1974 que mudou o inquerito em 9 dias", "The 1974 vault that changed the inquiry in 9 days", "ARQUIVO SECRETO", "SEALED FILE"),
            make_pair("P2", "Como 4 gramas viraram prova em 3 testes", "How 4 grams became evidence in 3 tests", "LAUDO FINAL", "FINAL REPORT"),
            make_pair("P3", "A viuva que ergueu 500 milhoes do zero", "The widow who built 500 million from zero", "IMPERIO OCULTO", "HIDDEN EMPIRE"),
        ]
        result = packaging_audit(make_packaging(pairs, winner="P1", alternatives=["P2"]))
        self.assertEqual(result["status"], "PASS", result)

    def test_packaging_falha_quando_thumb_repete_titulo(self):
        pairs = [
            make_pair("P1", "O arquivo de 1988 que reabriu o caso em 12 dias", "The 1988 file that reopened the case in 12 days", "ARQUIVO 1988", "FILE 1988"),
            make_pair("P2", "Como 4 gramas mudaram o laudo em 3 testes", "How 4 grams changed the report in 3 tests", "4 GRAMAS LAUDO TESTES EXTRA HOJE", "4 GRAMS"),
            make_pair("P3", "A viuva que construiu 500 milhoes do zero", "The widow who built 500 million from zero", "500 MILHOES", "500 MILLION"),
        ]
        result = packaging_audit(make_packaging(pairs))
        self.assertEqual(result["status"], "FAIL")
        self.assertTrue(any("thumb" in error for error in result["errors"]))

    def test_packaging_falha_sem_tres_pares_e_sem_humano(self):
        pairs = [make_pair("P1", "O arquivo de 1988 que reabriu o caso em 12 dias", "The 1988 file that reopened the case in 12 days", "ARQUIVO 1988", "FILE 1988")]
        result = packaging_audit(make_packaging(pairs, winner="PX", alternatives=[], human=""))
        self.assertEqual(result["status"], "FAIL")

    def test_thumb_pass_dois_conceitos(self):
        brief = {"version": 1, "episode": "video01", "channel": "x", "image": "",
                 "concepts": [make_concept("A", "ARQUIVO SECRETO", "SEALED FILE", "face-vs-objeto"),
                              make_concept("B", "PROVA OCULTA", "HIDDEN PROOF", "texto-vs-sem-texto")]}
        with tempfile.TemporaryDirectory() as temp:
            result = thumb_audit(brief, ["O cofre de 1974 que mudou tudo em 9 dias", "The 1974 vault that changed everything in 9 days"], Path(temp))
        self.assertIn(result["status"], ("PASS", "REVIEW"), result)

    def test_thumb_falha_overlay_longo_e_repeticao(self):
        brief = {"version": 1, "episode": "video01", "channel": "x", "image": "",
                 "concepts": [make_concept("A", "O ARQUIVO COMPLETO DO CASO REABERTO HOJE", "FILE", "x"),
                              make_concept("B", "12 DIAS", "12 DAYS", "y")]}
        with tempfile.TemporaryDirectory() as temp:
            result = thumb_audit(brief, ["O arquivo completo do caso reaberto hoje com 5 provas"], Path(temp))
        self.assertEqual(result["status"], "FAIL")

    def test_short_qa_bloqueia_hook_longo_abertura_e_frame1(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            narration = root / "narration_short.txt"
            narration.write_text("Esta primeira frase tem claramente mais do que oito palavras curtas\n\nSegundo bloco.\n", encoding="utf-8")
            plan = root / "plan.txt"
            plan.write_text("plano", encoding="utf-8")
            result = short_qa.run(str(narration), str(plan), None, None, "UM DOIS TRES QUATRO CINCO SEIS SETE")
            self.assertEqual(result["status"], "FAIL")
            self.assertTrue(any("hook_short_longo" in e or "frame1_texto_longo" in e for e in result["errors"]))

    def test_short_qa_bloqueia_saudacao_logo(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            narration = root / "narration_short.txt"
            narration.write_text("Oi gente hoje vou mostrar algo\n\nSegundo bloco.\n", encoding="utf-8")
            plan = root / "plan.txt"
            plan.write_text("plano", encoding="utf-8")
            result = short_qa.run(str(narration), str(plan), None, None, "PAYOFF AQUI")
            self.assertEqual(result["status"], "FAIL")
            self.assertIn("abertura_proibida_logo_ou_saudacao", result["errors"])


if __name__ == "__main__":
    unittest.main()
