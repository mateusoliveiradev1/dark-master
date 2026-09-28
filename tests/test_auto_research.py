import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

SKILL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / "scripts"))

from auto_research import build_alerts
from learn_loop import build_dashboard


class AutoResearchTests(unittest.TestCase):
    def test_demand_depth_alerta_perguntas_novas(self):
        current = {"seeds": [{"seed": "fraud documentary", "depth": 20,
                              "suggestions": [f"pergunta nova {i}" for i in range(6)], "rising": []}]}
        alerts = build_alerts(current, {"seeds": []})
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

    def test_dashboard_agrega_multicanal(self):
        import learn_loop
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "monitor").mkdir()
            (root / "monitor" / "channels.json").write_text(
                '{"channels": [{"handle": "@A", "name": "A", "mine": true}, {"handle": "@B", "name": "B"}]}',
                encoding="utf-8")
            (root / "data" / "research").mkdir(parents=True)
            (root / "data" / "research" / "latest.json").write_text(
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
