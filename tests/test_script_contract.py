import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
SCRIPTS = SKILL / "scripts"
sys.path.insert(0, str(SCRIPTS))

from script_builder import minutes_window, validate_claims, validate_funnel_plan


class ScriptContractTests(unittest.TestCase):
    def test_duration_windows(self):
        self.assertEqual(minutes_window("30-35"), (4200, 5600))
        self.assertEqual(minutes_window("45-60"), (6300, 9600))
        self.assertEqual(minutes_window("60-70"), (8400, 11200))

    def test_claims_require_sources(self):
        errors = validate_claims([{"id": "C001", "text": "Uma data.", "layer": "FATO"}])
        self.assertTrue(any("missing_sources" in error for error in errors))

    def test_claims_accept_sourced_fact(self):
        errors = validate_claims([{"id": "C001", "text": "Uma data.", "layer": "FATO", "source_ids": ["S001"]}])
        self.assertEqual(errors, [])

    def test_funnel_plan_checks_hook_limits(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "SHORT_FUNNEL.md"
            path.write_text(
                "\n".join([
                    "- Frame 1 visual: porta trancada por dentro",
                    "- Texto na tela: PORTA TRANCADA",
                    "- Fala inicial: A porta estava trancada por dentro",
                    "- Promessa do Short: a contradição",
                    "- Payoff: o acesso estava impossível",
                    "- Ponte: o laudo explica a divergência",
                    "- Emenda visual: mesma porta",
                    "- Emenda sonora: trancada",
                    "- Loop semântico: a pergunta continua",
                    "- Comentário fixado: veja o laudo completo",
                    "- Related Video: video01",
                ]),
                encoding="utf-8",
            )
            self.assertEqual(validate_funnel_plan(path), [])

    def test_scaffold_creates_research_and_short_contract(self):
        with tempfile.TemporaryDirectory() as temp:
            result = subprocess.run(
                [sys.executable, str(SCRIPTS / "new_video.py"), "01", "Caso teste", "FORENSE",
                 "--root", temp, "--channel", "cold-file-diaries"],
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            root = Path(temp) / "video01" / "01_roteiro"
            for name in ("PESQUISA_BRIEF.md", "PESQUISA_FONTE.md", "CLAIMS.json",
                         "LINHA_DO_TEMPO.md", "SHORT_FUNNEL.md", "narration_short.txt"):
                self.assertTrue((root / name).exists(), name)
            claims = json.loads((root / "CLAIMS.json").read_text(encoding="utf-8"))
            self.assertEqual(claims["claims"], [])

    def test_short_validation_rejects_nine_word_hook(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "PESQUISA_BRIEF.md").write_text("Brief com pergunta central, resumo do caso, fontes, lacunas, contradições e plano de reconstrução documentados para o teste.", encoding="utf-8")
            (root / "PESQUISA_FONTE.md").write_text("| ID | Camada | Fonte | URL | Localizador | Limitações |\n|---|---|---|---|---|---|\n| S001 | FATO | Registro | arquivo.pdf | p. 1 | nenhuma |", encoding="utf-8")
            claims = root / "CLAIMS.json"
            claims.write_text(json.dumps({"claims": [{"id": "C001", "text": "Porta trancada.", "layer": "FATO", "source_ids": ["S001"]}]}), encoding="utf-8")
            plan = root / "SHORT_FUNNEL.md"
            plan.write_text(
                "\n".join([
                    "- Frame 1 visual: porta",
                    "- Texto na tela: PORTA TRANCADA",
                    "- Fala inicial: a porta estava trancada por dentro do apartamento vazio",
                    "- Promessa do Short: a contradição",
                    "- Payoff: o acesso estava impossível",
                    "- Ponte: o laudo explica a divergência",
                    "- Emenda visual: mesma porta",
                    "- Emenda sonora: trancada",
                    "- Loop semântico: a pergunta continua",
                    "- Comentário fixado: veja o laudo completo",
                    "- Related Video: video01",
                ]),
                encoding="utf-8",
            )
            narration = root / "narration_short.txt"
            narration.write_text(
                "A porta estava trancada por dentro do apartamento vazio.\n\n"
                "O registro não explica.\n\n"
                "A contradição permaneceu.\n\n"
                "A porta continua no centro do caso.",
                encoding="utf-8",
            )
            result = subprocess.run(
                [sys.executable, str(SCRIPTS / "script_builder.py"),
                 "--validate", str(narration), "--genre", "short", "--short", "--porte", "13s",
                 "--strict", "--claims", str(claims), "--funnel-plan", str(plan)],
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("hook_short_longo", result.stdout)
    def test_short_validation_accepts_complete_contract(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "PESQUISA_BRIEF.md").write_text("Brief com pergunta central, resumo do caso, fontes, lacunas, contradições e plano de reconstrução documentados para o teste.", encoding="utf-8")
            (root / "PESQUISA_FONTE.md").write_text("| ID | Camada | Fonte | URL | Localizador | Limitações |\n|---|---|---|---|---|---|\n| S001 | FATO | Registro | arquivo.pdf | p. 1 | nenhuma |", encoding="utf-8")
            claims = root / "CLAIMS.json"
            claims.write_text(json.dumps({"claims": [{"id": "C001", "text": "Porta trancada.", "layer": "FATO", "source_ids": ["S001"]}]}), encoding="utf-8")
            plan = root / "SHORT_FUNNEL.md"
            plan.write_text(
                "\n".join([
                    "- Frame 1 visual: porta trancada por dentro",
                    "- Texto na tela: PORTA TRANCADA",
                    "- Fala inicial: A porta estava trancada por dentro",
                    "- Promessa do Short: a contradição",
                    "- Payoff: o acesso estava impossível",
                    "- Ponte: o laudo explica a divergência",
                    "- Emenda visual: mesma porta",
                    "- Emenda sonora: trancada",
                    "- Loop semântico: a pergunta continua",
                    "- Comentário fixado: veja o laudo completo",
                    "- Related Video: video01",
                ]),
                encoding="utf-8",
            )
            narration = root / "narration_short.txt"
            narration.write_text(
                "A porta estava trancada por dentro.\n\n"
                "O registro não explica como isso aconteceu.\n\n"
                "A contradição permaneceu sem uma resposta.\n\n"
                "A porta continua no centro do caso e a próxima prova pode mudar tudo.",
                encoding="utf-8",
            )
            result = subprocess.run(
                [sys.executable, str(SCRIPTS / "script_builder.py"),
                 "--validate", str(narration), "--genre", "short", "--short", "--porte", "13s",
                 "--strict", "--claims", str(claims), "--funnel-plan", str(plan)],
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("RESULTADO: PASSOU", result.stdout)
