import json
import sys
import tempfile
import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
SCRIPTS = SKILL / "scripts"
sys.path.insert(0, str(SCRIPTS))

from script_builder import (
    build_short_funnel,
    load_beats,
    minutes_window,
    porte_short_window,
    validate_beats,
    validate_funnel_plan,
    wpm_for,
)
import importlib.util


def _load_hyphen_module(name):
    spec = importlib.util.spec_from_file_location(name, str(SCRIPTS / f"{name}.py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


lint_roteiro = _load_hyphen_module("lint-roteiro")
narration_dates = lint_roteiro.narration_dates
from compliance_audit import audit as compliance_audit
from research_audit import audit as research_audit
from short_qa import run as short_qa_run
from timing_audit import audit as timing_audit


class RoteiroQualityTests(unittest.TestCase):
    def test_beats_template_generic_valido(self):
        data = json.loads((SKILL / "models" / "_template" / "beats.json").read_text(encoding="utf-8"))
        self.assertEqual(validate_beats(data["generic"]), [])

    def test_beats_rejeita_soma_duplicata_guia(self):
        self.assertTrue(any("soma" in e for e in validate_beats([["A", 0.5, "g"], ["B", 0.6, "g"]])))
        self.assertTrue(any("duplicado" in e for e in validate_beats([["A", 0.5, "g"], ["A", 0.5, "g"]])))
        self.assertTrue(any("guia_vazio" in e for e in validate_beats([["A", 1.0, ""]])))

    def test_load_beats_rejeita_genero_ruim_sem_quebrar_bom(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "beats.json"
            path.write_text(json.dumps({
                "bom": [["A", 0.5, "guia a"], ["B", 0.5, "guia b"]],
                "ruim": [["A", 0.5, "guia a"], ["B", 0.9, "guia b"]],
            }), encoding="utf-8")
            load_beats(str(path))
            import script_builder
            self.assertIn("bom", script_builder.GENRES)
            self.assertNotIn("ruim", script_builder.GENRES)

    def test_wpm_por_idioma_e_canal(self):
        self.assertEqual(wpm_for(None, "pt"), 145)
        self.assertEqual(wpm_for(None, "en"), 155)
        self.assertEqual(wpm_for(None, "es"), 150)
        with tempfile.TemporaryDirectory() as temp:
            pb = Path(temp) / "canal-x"
            pb.mkdir()
            (pb / "roteiro.json").write_text(json.dumps({"wpm": {"pt": 140}}), encoding="utf-8")
            self.assertEqual(wpm_for(str(pb), "pt"), 140)
            self.assertEqual(wpm_for(str(pb), "en"), 155)

    def test_minutes_window_wpm(self):
        self.assertEqual(minutes_window("30-35"), (4200, 5600))
        self.assertEqual(minutes_window("30-35", 145), (4350, 5075))
        self.assertNotEqual(porte_short_window("25s", "pt"), porte_short_window("25s", "en"))

    def test_funnel_gerado_passa_e_exige_claim_beat(self):
        with tempfile.TemporaryDirectory() as temp:
            plan = Path(temp) / "ROTEIRO_SHORT_PLANO.md"
            plan.write_text(build_short_funnel({"case": "Caso", "target_long": "video01"}), encoding="utf-8")
            errors = validate_funnel_plan(plan)
            self.assertTrue(any("Claim IDs" in e for e in errors))
            self.assertTrue(any("Beat do long" in e for e in errors))
            text = plan.read_text(encoding="utf-8")
            text = text.replace("- Claim IDs: \n", "- Claim IDs: C001\n").replace("- Beat do long: \n", "- Beat do long: EVIDENCIAS\n")
            plan.write_text(text, encoding="utf-8")

    def test_research_chain_vira_review(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "video01" / "01_roteiro"
            root.mkdir(parents=True)
            (root / "CLAIMS.json").write_text(json.dumps({"claims": [{
                "id": "C001", "text": "Fato", "layer": "FATO", "source_ids": ["S001"],
                "locator": "p. 1", "primary_source": True, "confidence": "ALTA"}]}), encoding="utf-8")
            (root / "PESQUISA_FONTE.md").write_text("| ID | Camada | Tipo | Fonte | Depende de | URL | Trecho/localizador | Limitações |\n|---|---|---|---|---|---|---|---|\n| S001 | FATO | primária | Registro | independente | fonte://x | p. 1 | nenhuma |", encoding="utf-8")
            (root / "LINHA_DO_TEMPO.md").write_text("| data | fato | camada | fonte |\n|---|---|---|---|\n| 2001-01-01 | E1 | FATO | S001 |\n| 2002-01-01 | E2 | FATO | S001 |\n| 2003-01-01 | E3 | FATO | S001 |", encoding="utf-8")
            result = research_audit(root.parent)
            self.assertEqual(result["status"], "REVIEW")
            self.assertTrue(any("chain_" in item for item in result["review"]))

    def test_lint_meses_es(self):
        dates = narration_dates("Ocorreu em 15 de enero de 2020 na cidade.", "es")
        self.assertTrue(any(dt == (2020, 1, 15) for _, dt, _, _ in dates))

    def test_compliance_en_es(self):
        with tempfile.TemporaryDirectory() as temp:
            narration = Path(temp) / "narration.txt"
            narration.write_text("He murdered the victim that night.", encoding="utf-8")
            result = compliance_audit(str(narration))
            self.assertEqual(result["status"], "REVIEW")
            self.assertTrue(any("legal_status" in item for item in result["review"]))
            narration.write_text("The alleged suspect left the city.", encoding="utf-8")
            result = compliance_audit(str(narration))
            self.assertNotIn("living_or_case_status_review", result["review"])

    def test_short_qa_claim_desconhecida_e_parafrase(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            narration = root / "narration_short.txt"
            narration.write_text("A porta estava trancada por dentro.\n\nA prova muda o caso.", encoding="utf-8")
            plan = root / "SHORT_FUNNEL.md"
            plan.write_text("\n".join([
                "- Frame 1 visual: porta", "- Texto na tela: PORTA TRANCADA",
                "- Fala inicial: A porta estava trancada por dentro",
                "- Promessa do Short: a contradição", "- Payoff: o acesso estava impossível",
                "- Ponte: o laudo explica", "- Emenda visual: mesma porta",
                "- Emenda sonora: trancada", "- Loop semântico: a pergunta continua",
                "- Comentário fixado: veja o long", "- Related Video: video01",
                "- Claim IDs: C999", "- Beat do long: EVIDENCIAS"]), encoding="utf-8")
            claims = root / "CLAIMS.json"
            claims.write_text(json.dumps({"claims": [{"id": "C001", "text": "Porta.", "layer": "FATO", "source_ids": ["S001"]}]}), encoding="utf-8")
            result = short_qa_run(str(narration), str(plan), None, None, "PORTA TRANCADA", str(claims))
            self.assertEqual(result["status"], "FAIL")
            self.assertTrue(any("short_claim_desconhecida" in e for e in result["errors"]))
            long_form = root / "narration_v3.txt"
            long_form.write_text("A porta estava trancada por dentro e ninguém entendia nada do caso ocorrido.\n\nDepois veio a prova.", encoding="utf-8")
            result = short_qa_run(str(narration), str(plan), None, str(long_form), "PORTA TRANCADA", str(claims))
            self.assertTrue(any("parafrase" in e or "overlap" in e for e in result["errors"]))

    def test_timing_tolerancia_por_beat_e_fallback(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            narration = root / "narration_v3.txt"
            narration.write_text(" ".join(["palavra"] * 300), encoding="utf-8")
            captions = root / "captions_times.json"
            captions.write_text(json.dumps({"total": 120, "blocos": [{"start": 0, "end": 120, "dur": 120}]}), encoding="utf-8")
            result = timing_audit(str(narration), str(captions), "30-35")
            self.assertEqual(result["status"], "FALHA")
            result = timing_audit(str(narration), str(root / "ausente.json"), "30-35")
            self.assertEqual(result["status"], "REVIEW")
            self.assertIn("estimate_seconds", result)


if __name__ == "__main__":
    unittest.main()
