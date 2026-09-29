import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

SKILL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / "scripts"))

from auto_research import build_alerts, outlier_flares


class AutoResearchTests(unittest.TestCase):
    def test_demand_depth_alerta_perguntas_novas(self):
        current = {"seeds": [{"seed": "fraud documentary", "depth": 20,
                              "suggestions": [f"pergunta nova {i}" for i in range(6)], "rising": []}]}
        previous = {"seeds": [{"seed": "other", "depth": 3, "suggestions": [], "rising": []}]}
        alerts = build_alerts(current, previous)
        demand = [a for a in alerts if a["type"] == "DEMAND_DEPTH"]
        self.assertEqual(len(demand), 1)
        self.assertIn("6 perguntas novas", demand[0]["detail"])

    def test_trend_up_queries_novas_e_virada(self):
        current = {"seeds": [{"seed": "x", "depth": 5, "suggestions": [],
                              "rising": ["q nova"], "trends_direction": "ALTA"}]}
        previous = {"seeds": [{"seed": "x", "depth": 5, "suggestions": [],
                               "rising": ["q antiga"], "trends_direction": "ESTAVEL"}]}
        alerts = build_alerts(current, previous)
        types = [a["type"] for a in alerts]
        self.assertIn("TREND_UP", types)
        self.assertEqual(sum(1 for a in alerts if a["type"] == "TREND_UP"), 2)

    def test_sem_duplicar_quando_nada_mudou(self):
        round_data = {"seeds": [{"seed": "x", "depth": 20, "suggestions": ["a", "b"],
                                 "rising": ["q"], "trends_direction": "ALTA"}]}
        self.assertEqual(build_alerts(round_data, round_data), [])

    def test_baseline_sem_rodada_anterior(self):
        current = {"seeds": [{"seed": "x", "depth": 100, "suggestions": ["a"], "rising": []}]}
        alerts = build_alerts(current, {})
        self.assertEqual(len(alerts), 1)
        self.assertEqual(alerts[0]["type"], "BASELINE")

    def test_flare_imediato_acima_de_10x(self):
        rows = [{"video_id": "v1", "title": "T", "channel": "@A", "pattern": "true-crime",
                 "views": 5000, "ratio": 12.5, "detected_ts": "2026-09-28T06:00:00"}]
        alerts, newly = outlier_flares(rows, set(), "2026-09-28")
        self.assertEqual(len(alerts), 1)
        self.assertEqual(alerts[0]["type"], "OUTLIER_FLARE")
        self.assertIn("1/1 (flare)", alerts[0]["detail"])
        self.assertEqual(alerts[0]["niche"], "true-crime")
        self.assertEqual(newly, ["v1"])

    def test_confirma_dois_dias_antes_de_alertar(self):
        one = [{"video_id": "v2", "title": "T", "channel": "@A", "pattern": "true-crime",
                "views": 900, "ratio": 4.2, "detected_ts": "2026-09-28T06:00:00"}]
        alerts, _ = outlier_flares(one, set(), "2026-09-28")
        self.assertEqual(alerts, [])
        two = one + [{"video_id": "v2", "title": "T", "channel": "@A", "pattern": "true-crime",
                      "views": 950, "ratio": 4.0, "detected_ts": "2026-09-29T06:00:00"}]
        alerts, newly = outlier_flares(two, set(), "2026-09-29")
        self.assertEqual(len(alerts), 1)
        self.assertIn("confirmado 2/2", alerts[0]["detail"])
        self.assertIn("detectado ha 1d", alerts[0]["detail"])
        self.assertIn("youtube.com/watch?v=v2", alerts[0]["examples"][0])

    def test_nao_duplica_video_ja_alertado(self):
        rows = [{"video_id": "v3", "title": "T", "channel": "@A", "pattern": "",
                 "views": 9000, "ratio": 15.0, "detected_ts": "2026-09-28T06:00:00"}]
        alerts, newly = outlier_flares(rows, {"v3"}, "2026-09-28")
        self.assertEqual((alerts, newly), ([], []))

    def test_details_neon_ou_unknown(self):
        import learn_loop
        fake_db = mock.MagicMock()
        fake_db._rows.return_value = [
            {"video_id": "a", "title": "V A", "format": "short", "views": 1000,
             "engaged_views": 400, "snapshot_date": "2026-09-28", "ts": "2026-09-28T06:00:00"},
            {"video_id": "b", "title": "V B", "format": "long", "views": 500,
             "engaged_views": 100, "snapshot_date": "2026-09-28", "ts": "2026-09-28T06:00:00"},
        ]
        with mock.patch.dict(sys.modules, {"yt_db": fake_db}):
            detail = learn_loop.channel_details("@A", "A")
            self.assertEqual(detail["status"], "ok")
            self.assertEqual(detail["views_30d"], 1500)
            self.assertEqual(detail["top"][0]["title"], "V A")
        bad = mock.MagicMock()
        bad.init.side_effect = RuntimeError("sem banco")
        with mock.patch.dict(sys.modules, {"yt_db": bad}):
            self.assertEqual(learn_loop.channel_details("@A", "A")["status"], "unknown")

    def test_oportunidades_persistentes_e_diagnostico(self):
        import learn_loop
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "monitor").mkdir()
            (root / "monitor" / "channels.json").write_text('{"channels": []}', encoding="utf-8")
            (root / "data" / "research").mkdir(parents=True)
            (root / "data" / "research" / "latest-en.json").write_text(json.dumps({
                "alerts": [], "lang": "en", "seeds": [
                    {"seed": "x quente", "date": "2026-09-29", "depth": 100,
                     "suggestions": ["q1"], "trends_direction": "ALTA", "rising": []},
                    {"seed": "x frio", "date": "2026-09-29", "depth": 3,
                     "suggestions": [], "trends_direction": "BAIXA", "rising": []}]}), encoding="utf-8")
            with mock.patch.object(learn_loop, "ROOT", root):
                dashboard = learn_loop.build_dashboard()
            kinds = [(a["type"], a["seed"]) for a in dashboard["alerts"]]
            self.assertIn(("OPPORTUNITY", "x quente"), kinds)
            self.assertNotIn(("OPPORTUNITY", "x frio"), [kinds[0][1] if kinds else ""])
            self.assertIn("db_backend", dashboard["diagnostics"])
            self.assertIn("research_rounds", dashboard["diagnostics"])

    def test_dashboard_agrega_multicanal(self):
        import learn_loop
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "monitor").mkdir()
            (root / "monitor" / "channels.json").write_text(
                '{"channels": [{"handle": "@A", "name": "A", "mine": true}, {"handle": "@B", "name": "B"}]}',
                encoding="utf-8")
            (root / "data" / "research").mkdir(parents=True)
            (root / "data" / "research" / "latest-en.json").write_text(
                '{"alerts": [{"type": "TREND_UP", "seed": "x", "detail": "d", "examples": []}]}', encoding="utf-8")
            (root / "data" / "ypp_input.json").write_text(
                '{"@A": {"subs": 2000, "hours": 5000, "short_views": 0, "longs_90d": 3, "shorts_90d": 0}}',
                encoding="utf-8")
            with mock.patch.object(learn_loop, "ROOT", root):
                dashboard = learn_loop.build_dashboard()
            self.assertEqual(len(dashboard["channels"]), 2)
            self.assertEqual(len(dashboard["alerts"]), 1)
            self.assertTrue(dashboard["ypp"]["@A"]["eligible_2026"])
            self.assertTrue((root / "data" / "dashboard.json").exists())


if __name__ == "__main__":
    unittest.main()
