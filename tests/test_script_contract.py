import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

SKILL = Path(__file__).resolve().parents[1]
SCRIPTS = SKILL / "scripts"
sys.path.insert(0, str(SCRIPTS))

from script_builder import minutes_window, validate_claims, validate_funnel_plan, validate_roteiro_map
from timing_audit import audit
from short_qa import run as short_qa_run
from originality_audit import audit as originality_audit
from compliance_audit import audit as compliance_audit
from script_feedback import audit as feedback_audit
from research_audit import audit as research_audit
from calibration_audit import audit as calibration_audit
import captions_audit
import voice_engine
from voice_engine import caption_segments, public_step, provider_params, provider_preflight


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

    def test_script_builder_generates_semantic_map(self):
        with tempfile.TemporaryDirectory() as temp:
            result = subprocess.run(
                [sys.executable, str(SCRIPTS / "script_builder.py"),
                 "--genre", "forense", "--target-minutes", "30-35", "--funnel",
                 "--target-long", "video01", "--case", "Caso", "--out", temp],
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            data = json.loads((Path(temp) / "ROTEIRO_MAP.json").read_text(encoding="utf-8"))
            self.assertEqual(data["target_words"], [4200, 5600])
            self.assertEqual(len(data["blocks"]), 9)

    def test_builder_seeds_existing_map_stub(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            scaffold = subprocess.run(
                [sys.executable, str(SCRIPTS / "new_video.py"), "01", "Caso", "FORENSE", "--root", temp],
                capture_output=True,
                text=True,
            )
            self.assertEqual(scaffold.returncode, 0, scaffold.stderr)
            result = subprocess.run(
                [sys.executable, str(SCRIPTS / "script_builder.py"),
                 "--genre", "forense", "--target-minutes", "30-35", "--out", str(root / "video01")],
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            data = json.loads((root / "video01" / "01_roteiro" / "ROTEIRO_MAP.json").read_text(encoding="utf-8"))
            self.assertEqual(len(data["blocks"]), 9)

    def test_roteiro_map_requires_narration_and_claims(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            narration = root / "narration_v3.txt"
            blocks = []
            claims = []
            texts = [
                "O primeiro documento criou uma dúvida.",
                "A segunda prova limita a hipótese.",
                "A testemunha mudou a linha do tempo.",
                "O laudo mostra o que não pode ser concluído.",
                "A cronologia agora reconecta os eventos.",
                "A última pergunta permanece sem resposta.",
            ]
            for index, text in enumerate(texts, 1):
                claims.append({"id": f"C{index:03d}", "text": text, "layer": "FATO", "source_ids": ["S001"]})
                blocks.append({
                    "id": f"B{index:03d}",
                    "beat": ["COLD OPEN", "CONTEXTO", "DESENVOLVIMENTO", "VIRADA", "CONSEQUENCIA", "FECHAMENTO+TEASER"][index - 1],
                    "text": text,
                    "claim_ids": [f"C{index:03d}"],
                    "target_words": 10,
                    "target_seconds": 4,
                    "question": "O que este bloco responde?",
                    "state_change": "O entendimento avança.",
                    "rehook": index in {2, 3, 4},
                    "payoff": index == 6,
                })
            narration.write_text("\n\n".join(texts), encoding="utf-8")
            path = root / "ROTEIRO_MAP.json"
            path.write_text(json.dumps({"blocks": blocks}), encoding="utf-8")
            self.assertEqual(validate_roteiro_map(path, narration, claims, "generic", (1, 1000)), [])

    def test_roteiro_map_rejects_narration_mismatch(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            narration = root / "narration_v3.txt"
            narration.write_text("Texto narrado diferente.", encoding="utf-8")
            path = root / "ROTEIRO_MAP.json"
            path.write_text(json.dumps({"blocks": [{
                "id": "B001", "beat": "COLD OPEN", "text": "Texto do mapa.",
                "claim_ids": ["C001"], "target_words": 10, "target_seconds": 4,
                "question": "Pergunta?", "state_change": "Mudança.", "rehook": False, "payoff": True
            }]}), encoding="utf-8")
            errors = validate_roteiro_map(path, narration, [{"id": "C001"}], "generic", (1, 1000))
            self.assertIn("map_narration_mismatch", errors)

    def test_forensic_end_to_end_targets(self):
        for target, minimum_words in (("30-35", 4200), ("45-60", 6300), ("60-70", 8400)):
            with tempfile.TemporaryDirectory() as temp:
                root = Path(temp) / "video01"
                generated = subprocess.run(
                    [sys.executable, str(SCRIPTS / "script_builder.py"),
                     "--genre", "forense", "--target-minutes", target,
                     "--case", "Caso longo", "--out", str(root)],
                    capture_output=True,
                    text=True,
                )
                self.assertEqual(generated.returncode, 0, generated.stderr)
                script_dir = root / "01_roteiro"
                map_data = json.loads((script_dir / "ROTEIRO_MAP.json").read_text(encoding="utf-8"))
                blocks = map_data["blocks"]
                claims = []
                used = 0
                for index, block in enumerate(blocks):
                    remaining_blocks = len(blocks) - index
                    count = min(150, max(1, (minimum_words - used + remaining_blocks - 1) // remaining_blocks)) if index == 0 else max(1, (minimum_words - used + remaining_blocks - 1) // remaining_blocks)
                    text = " ".join(["evidencia"] * count)
                    if index == len(blocks) - 1:
                        text += " A questão permanece sem resposta."
                    claim_id = f"C{index + 1:03d}"
                    block["text"] = text
                    block["claim_ids"] = [claim_id]
                    block["question"] = "O que este bloco responde?"
                    block["state_change"] = "O grau de certeza muda."
                    block["rehook"] = index in {1, 2, 3, 4, 5, 6}
                    block["payoff"] = index == len(blocks) - 1
                    claims.append({"id": claim_id, "text": text[:80], "layer": "FATO", "source_ids": [f"S{index + 1:03d}"]})
                    used += count
                (script_dir / "ROTEIRO_MAP.json").write_text(json.dumps(map_data, ensure_ascii=False, indent=2), encoding="utf-8")
                (script_dir / "narration_v3.txt").write_text("\n\n".join(block["text"] for block in blocks), encoding="utf-8")
                (script_dir / "CLAIMS.json").write_text(json.dumps({"claims": claims}, ensure_ascii=False), encoding="utf-8")
                (script_dir / "PESQUISA_BRIEF.md").write_text("Brief completo com resumo, pergunta central, fontes, lacunas, contradições, evidências e plano de reconstrução para o caso longo de teste.", encoding="utf-8")
                source = "| ID | Camada | Fonte | URL | Localizador | Limitações |\n|---|---|---|---|---|---|\n"
                source += "\n".join(f"| S{index:03d} | FATO | Registro {index} | fonte-{index} | p. {index} | nenhuma |" for index in range(1, len(blocks) + 1))
                (script_dir / "PESQUISA_FONTE.md").write_text(source, encoding="utf-8")
                timeline = "| data | fato | camada | fonte |\n|---|---|---|---|\n"
                timeline += "\n".join(f"| 200{index:02d}-01-01 | Evento {index} | FATO | S{index:03d} |" for index in range(1, 16))
                (script_dir / "LINHA_DO_TEMPO.md").write_text(timeline, encoding="utf-8")
                result = subprocess.run(
                    [sys.executable, str(SCRIPTS / "script_builder.py"),
                     "--validate", str(script_dir / "narration_v3.txt"), "--genre", "forense",
                     "--target-minutes", target, "--strict", "--claims", str(script_dir / "CLAIMS.json"),
                     "--timeline", str(script_dir / "LINHA_DO_TEMPO.md"), "--map", str(script_dir / "ROTEIRO_MAP.json")],
                    capture_output=True,
                    text=True,
                )
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertIn("RESULTADO: PASSOU", result.stdout)

    def test_caption_segments_respect_publish_limits(self):
        text = " ".join(["palavra"] * 80)
        segments = caption_segments(text, max_chars=30, max_lines=1)
        self.assertTrue(segments)
        self.assertTrue(all(len(line) <= 30 and "\n" not in line for segment in segments for line in segment.splitlines()))
        self.assertEqual(" ".join(segment for segment in segments), text)

    def test_voice_contract_step_omits_runtime_keys(self):
        step = {"type": "edge", "voice_id": "pt-BR-AntonioNeural", "model": None, "api_key_env": "X", "settings": {"a": 1}, "_ring": {"secret": "hidden"}}
        public = public_step(step)
        self.assertNotIn("_ring", public)
        self.assertEqual(public["voice_id"], "pt-BR-AntonioNeural")

    def test_timing_audit_accepts_long_targets(self):
        for target, actual_minutes in (("30-35", 33), ("45-60", 52), ("60-70", 65)):
            with tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                narration = root / "narration_v3.txt"
                narration.write_text("Uma narração de teste com duração medida.", encoding="utf-8")
                captions = root / "captions_times.json"
                captions.write_text(json.dumps({"total": actual_minutes * 60, "blocos": [{"start": 0, "end": actual_minutes * 60, "dur": actual_minutes * 60}]}), encoding="utf-8")
                result = audit(narration, captions, target)
                self.assertEqual(result["status"], "PASS", result)

    def test_timing_audit_checks_map_beats(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            narration = root / "narration_v3.txt"
            narration.write_text("Bloco narrado.", encoding="utf-8")
            captions = root / "captions_times.json"
            captions.write_text(json.dumps({"total": 1980, "blocos": [{"start": 0, "end": 60, "dur": 60}, {"start": 60, "end": 1980, "dur": 1920}]}), encoding="utf-8")
            map_path = root / "ROTEIRO_MAP.json"
            map_path.write_text(json.dumps({"blocks": [
                {"id": "B001", "beat": "HOOK", "target_seconds": 60},
                {"id": "B002", "beat": "PAYOFF", "target_seconds": 1920},
            ]}), encoding="utf-8")
            result = audit(narration, captions, "30-35", map_path=map_path)
            self.assertEqual(result["status"], "PASS", result)
            self.assertEqual(len(result["beat_timing"]), 2)

    def test_timing_audit_rejects_short_target(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            narration = root / "narration_v3.txt"
            narration.write_text("Narração curta.", encoding="utf-8")
            captions = root / "captions_times.json"
            captions.write_text(json.dumps({"total": 1200, "blocos": []}), encoding="utf-8")
            result = audit(narration, captions, "30-35")
            self.assertEqual(result["status"], "FALHA")

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
                         "ROTEIRO_MAP.json", "LINHA_DO_TEMPO.md", "SHORT_FUNNEL.md", "narration_short.txt"):
                self.assertTrue((root / name).exists(), name)
            claims = json.loads((root / "CLAIMS.json").read_text(encoding="utf-8"))
            self.assertEqual(claims["claims"], [])

    def test_research_audit_passes_rich_source_ledger(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "video01" / "01_roteiro"
            root.mkdir(parents=True)
            (root / "CLAIMS.json").write_text(json.dumps({"claims": [{
                "id": "C001", "text": "Fato documentado", "layer": "FATO", "source_ids": ["S001"],
                "locator": "p. 1", "primary_source": True, "confidence": "ALTA"
            }]}), encoding="utf-8")
            (root / "PESQUISA_FONTE.md").write_text("| ID | Camada | Tipo | Fonte | Depende de | URL | Trecho/localizador | Limitações |\n|---|---|---|---|---|---|---|---|\n| S001 | FATO | primária | Registro oficial | independente | fonte://registro | p. 1 | nenhuma |", encoding="utf-8")
            (root / "LINHA_DO_TEMPO.md").write_text("| data | fato | camada | fonte |\n|---|---|---|---|\n| 2001-01-01 | Evento | FATO | S001 |", encoding="utf-8")
            result = research_audit(root.parent)
            self.assertEqual(result["status"], "PASS", result)

    def test_calibration_flags_score_metric_mismatch(self):
        with tempfile.TemporaryDirectory() as temp:
            metrics = Path(temp) / "metrics.csv"
            metrics.write_text("channel,video_tag,format,views,avd_seconds,avp_percent,subscribers_gained\n@Canal,video01,long,100,100,40,2\n@Canal,video01,long,200,200,60,4\n@Canal,video01,long,80,80,30,1\n", encoding="utf-8")
            scorecard = Path(temp) / "score.json"
            scorecard.write_text(json.dumps({"score": 90, "status": "PASS"}), encoding="utf-8")
            result = calibration_audit(metrics, scorecard, "@Canal", "video01")
            self.assertEqual(result["status"], "REVIEW")
            self.assertTrue(result["propose_only"])
            self.assertEqual(result["performance_signals"], 0)

    def test_scorecard_passes_complete_mixed_fixture(self):
        with tempfile.TemporaryDirectory() as temp:
            script_dir = Path(temp) / "video01" / "01_roteiro"
            script_dir.mkdir(parents=True)
            blocks = []
            for index in range(1, 6):
                blocks.append({
                    "id": f"B{index:03d}", "beat": "BEAT", "text": "Texto documentado.",
                    "claim_ids": [f"C{index:03d}"], "target_words": 10, "target_seconds": 4,
                    "question": "Pergunta?", "state_change": "Muda o estado.", "rehook": True,
                    "payoff": index == 5,
                })
            (script_dir / "ROTEIRO_MAP.json").write_text(json.dumps({"blocks": blocks}), encoding="utf-8")
            (script_dir / "CLAIMS.json").write_text(json.dumps({"claims": [
                {"id": f"C{index:03d}", "text": "Fato", "layer": "FATO", "source_ids": ["S001"]}
                for index in range(1, 6)
            ]}), encoding="utf-8")
            (script_dir / "PESQUISA_FONTE.md").write_text("| ID | Camada | Fonte | URL | Localizador | Limitações |\n|---|---|---|---|---|---|\n| S001 | FATO | Registro | fonte | p. 1 | nenhuma |", encoding="utf-8")
            (script_dir / "LINHA_DO_TEMPO.md").write_text("\n".join(f"| 200{index:02d}-01-01 | Evento {index} | FATO | S001 |" for index in range(1, 9)), encoding="utf-8")
            (script_dir / "TIMING_AUDIT.json").write_text(json.dumps({"status": "PASS"}), encoding="utf-8")
            (script_dir / "ORIGINALITY_AUDIT.json").write_text(json.dumps({"status": "PASS"}), encoding="utf-8")
            (script_dir / "COMPLIANCE_AUDIT.json").write_text(json.dumps({"status": "PASS"}), encoding="utf-8")
            (script_dir / "SHORT_QA.json").write_text(json.dumps({"status": "PASS"}), encoding="utf-8")
            (script_dir / "SHORT_FUNNEL.md").write_text("funnel", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(SCRIPTS / "script_scorecard.py"), "--root", str(script_dir.parent), "--lane", "mixed"],
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            data = json.loads(result.stdout)
            self.assertEqual(data["status"], "PASS")
            self.assertGreaterEqual(data["score"], 85)

    def test_feedback_is_propose_only(self):
        with tempfile.TemporaryDirectory() as temp:
            metrics = Path(temp) / "metrics.csv"
            metrics.write_text("channel,video_tag,format,views,avd_seconds,avp_percent,ctr_percent,subscribers_gained\n@Canal,video01,long,100,100,40,5,2\n@Canal,video01,long,200,200,60,6,4\n@Canal,video01,long,80,80,30,4,1\n", encoding="utf-8")
            result = feedback_audit(metrics, "@Canal", "video01")
            self.assertEqual(result["status"], "REVIEW")
            self.assertTrue(result["propose_only"])
            self.assertTrue(result["proposals"])

    def test_compliance_audit_requires_review_for_attribution(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            narration = root / "narration_v3.txt"
            narration.write_text("O suspeito confessou o crime segundo o relatório.", encoding="utf-8")
            claims = root / "CLAIMS.json"
            claims.write_text(json.dumps({"claims": [{"id": "C001", "text": "Relatório", "layer": "FATO", "source_ids": ["S001"]}]}), encoding="utf-8")
            result = compliance_audit(narration, claims)
            self.assertEqual(result["status"], "REVIEW")
            self.assertTrue(result["human_review_required"])
            self.assertTrue(any(item.startswith("legal_status_or_attribution") for item in result["review"]))

    def test_originality_audit_flags_near_duplicate(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            current = root / "current" / "narration_v3.txt"
            previous = root / "previous" / "narration_v3.txt"
            current.parent.mkdir()
            previous.parent.mkdir()
            current.write_text("A porta estava trancada por dentro. A prova muda o caso e ninguém encontra uma resposta clara para a morte.", encoding="utf-8")
            previous.write_text(current.read_text(encoding="utf-8"), encoding="utf-8")
            result = originality_audit(current, root)
            self.assertEqual(result["status"], "FAIL")
            self.assertEqual(result["max_similarity"], 1.0)

    def test_short_qa_requires_rendered_video_for_full_pass(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            narration = root / "narration_short.txt"
            narration.write_text("A porta estava trancada por dentro.\n\nA prova muda o caso.", encoding="utf-8")
            plan = root / "SHORT_FUNNEL.md"
            plan.write_text(
                "\n".join([
                    "- Frame 1 visual: porta trancada",
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
            result = short_qa_run(narration, plan)
            self.assertEqual(result["status"], "REVIEW")
            self.assertIn("video_missing_for_full_qa", result["errors"])

    def test_short_qa_rejects_long_overlap(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            narration = root / "narration_short.txt"
            narration.write_text("A porta estava trancada por dentro do apartamento.\n\nA prova muda o caso.", encoding="utf-8")
            long_form = root / "narration_v3.txt"
            long_form.write_text("A porta estava trancada por dentro do apartamento e ninguém entendia o caso.\n\nDepois veio a prova.", encoding="utf-8")
            plan = root / "SHORT_FUNNEL.md"
            plan.write_text(
                "\n".join([
                    "- Frame 1 visual: porta trancada",
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
            result = short_qa_run(narration, plan, long_form=long_form)
            self.assertEqual(result["status"], "FAIL")
            self.assertTrue(any("short_long_overlap" in error for error in result["errors"]))

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

    def test_captions_audit_rejects_malformed_srt(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "captions.srt"
            path.write_text("1\n00:00:01,000 --> 00:00:02,000\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                captions_audit.parse(path)

    def test_captions_audit_parses_structured_srt(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "captions.srt"
            path.write_text(
                "1\n00:00:00,000 --> 00:00:01,000\nPrimeira frase\n\n"
                "2\n00:00:01,000 --> 00:00:02,000\nSegunda frase\n",
                encoding="utf-8",
            )
            cues = captions_audit.parse(path)
            self.assertEqual(len(cues), 2)
            self.assertEqual(cues[1]["text"], "Segunda frase")

    def test_voice_preflight_blocks_paid_provider_without_key(self):
        step = {"type": "elevenlabs", "voice_id": "voice", "api_key_env": "DARK_TEST_MISSING_KEY", "settings": {}}
        with mock.patch.dict(voice_engine.os.environ, {}, clear=True):
            result = provider_preflight(step, None)
        self.assertFalse(result["ready"])
        self.assertIn("api_key_missing", result["errors"])

    def test_piper_rate_is_converted_to_speed(self):
        step = {"type": "piper", "voice_id": "model.onnx", "settings": {}}
        cfg = {"rules": {"hook": {"rate": "+20%", "pitch": "0Hz"},
                          "outro": {"rate": "0%", "pitch": "0Hz"},
                          "beat": {"rate": "0%", "pitch": "0Hz"}}}
        converted, _ = provider_params(step, "Teste", 0, 1, cfg)
        self.assertEqual(converted["speed"], 1.2)
