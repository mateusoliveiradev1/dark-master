import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

SKILL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / "scripts"))

from learn_loop import due_themes, estimate, loop


class LearnLoopTests(unittest.TestCase):
    def test_estimate_corta_revalidate_no_teto(self):
        total, plan = estimate(["@A"], ["@A", "@B"], [{"theme": "t1"}, {"theme": "t2"}], 400)
        self.assertEqual(plan["revalidate"], [])
        self.assertEqual(plan["skipped_quota"], ["t1", "t2"])
        self.assertLessEqual(total, 400)

    def test_estimate_cabe_no_orcamento(self):
        total, plan = estimate(["@A"], ["@A"], [{"theme": "t1"}], 8000)
        self.assertEqual(plan["revalidate"], ["t1"])
        self.assertEqual(total, 300 + 50 + 150)

    def test_loop_dry_run_nao_executa(self):
        with tempfile.TemporaryDirectory() as temp:
            channels = [{"handle": "@A", "mine": True}, {"handle": "@B"}]
            report = loop(channels, [], {"all"}, True, 8000, temp)
            self.assertEqual(report["status"], "OK")
            self.assertTrue(all(step["status"] == "DRY_RUN" for step in report["quota"]["steps"]))
            self.assertTrue((Path(temp) / f"{report['date']}.json").exists())

    def test_loop_falha_graciosa_sem_rede(self):
        with tempfile.TemporaryDirectory() as temp:
            with mock.patch("learn_loop.sh", return_value=(1, "", "sem rede")):
                report = loop([{"handle": "@A", "mine": True}], [], {"all"}, False, 8000, temp)
                self.assertEqual(report["status"], "DEGRADED")
                self.assertTrue(report["failed_steps"])

    def test_due_themes_usa_watchlist(self):
        self.assertIsInstance(due_themes(), list)


if __name__ == "__main__":
    unittest.main()
