import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

SKILL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / "scripts"))

import niche_scan
from niche_scan import brief_checks, brief_verdict, iso8601_seconds, require_scope, token_scopes, trends_cache_get, trends_cache_set, watchlist_due, watchlist_save


class NicheScanTests(unittest.TestCase):
    def test_token_scopes_le_do_arquivo(self):
        with tempfile.TemporaryDirectory() as temp:
            token = Path(temp) / "yt-token.json"
            token.write_text(json.dumps({"scopes": ["https://www.googleapis.com/auth/youtube.readonly"]}), encoding="utf-8")
            self.assertIn("https://www.googleapis.com/auth/youtube.readonly", token_scopes(str(token)))
            self.assertEqual(token_scopes(str(token / "ausente.json")), [])

    def test_require_scope_falha_cedo_com_acao(self):
        with tempfile.TemporaryDirectory() as temp:
            token = Path(temp) / "yt-token.json"
            token.write_text(json.dumps({"scopes": ["https://www.googleapis.com/auth/youtube.readonly"]}), encoding="utf-8")
            with mock.patch.object(niche_scan, "TOKEN", token):
                ok, message = require_scope(niche_scan.FORCE_SSL)
                self.assertFalse(ok)
                self.assertIn("yt_auth.py", message)

    def test_trends_cache_ttl(self):
        with tempfile.TemporaryDirectory() as temp:
            cache = Path(temp) / ".trends_cache.json"
            with mock.patch.object(niche_scan, "TRENDS_CACHE", cache):
                with mock.patch.object(niche_scan, "DATA", Path(temp)):
                    self.assertIsNone(trends_cache_get("tema"))
                    trends_cache_set("tema", {"term": "tema", "direction": "ALTA"})
                    self.assertEqual(trends_cache_get("tema")["direction"], "ALTA")

    def test_watchlist_due_apos_14d(self):
        items = [{"theme": "a", "date": "2026-09-01"}, {"theme": "b", "date": "2026-09-27"}]
        due = watchlist_due(items, today="2026-09-28")
        self.assertEqual([item["theme"] for item in due], ["a"])
        self.assertEqual(due[0]["age_days"], 27)

    def test_iso8601_seconds_da_data_api(self):
        self.assertEqual(iso8601_seconds("PT15M33S"), 933)
        self.assertEqual(iso8601_seconds("PT1H2M3S"), 3723)
        self.assertEqual(iso8601_seconds("PT59S"), 59)
        self.assertEqual(iso8601_seconds(""), 0)
        self.assertEqual(iso8601_seconds(None), 0)

    def test_brief_passa_com_gates_fome_e_demanda(self):
        from datetime import datetime, timezone
        recent = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        cluster = {"passed": ["a", "b", "c"], "hungry": ["a", "b"], "signal": True, "emerging": [],
                   "channels": [{"age_days": 20, "short_share": 0.9,
                                 "outliers": [{"published": recent, "title": "t", "views": 100}]}]}
        suggest = {"depth": 25}
        trends = {"direction": "ALTA"}
        checks = brief_checks(cluster, suggest, trends, "BR")
        self.assertTrue(all(c["status"] == "PASS" for c in checks if c["status"] != "MANUAL"))
        self.assertEqual(brief_verdict(cluster, checks), "PASSA")

    def test_brief_parcial_com_fome_sem_gates(self):
        cluster = {"passed": [], "hungry": ["a", "b"], "signal": True, "emerging": ["c"],
                   "channels": [{"age_days": 200, "short_share": 0.5, "outliers": []}]}
        checks = brief_checks(cluster, {"depth": 30}, {"direction": "ESTAVEL"}, "US")
        self.assertEqual(brief_verdict(cluster, checks), "PARCIAL")

    def test_brief_reprova_sem_fome(self):
        cluster = {"passed": [], "hungry": [], "signal": False, "emerging": [],
                   "channels": [{"age_days": 400, "short_share": 0.1, "outliers": []}]}
        checks = brief_checks(cluster, {"depth": 3}, {"error": "sem dados"}, "")
        self.assertEqual(brief_verdict(cluster, checks), "REPROVA")

    def test_watchlist_save_dedup_por_tema(self):
        with tempfile.TemporaryDirectory() as temp:
            watchlist = Path(temp) / "watchlist.json"
            with mock.patch.object(niche_scan, "WATCHLIST", watchlist):
                with mock.patch.object(niche_scan, "DATA", Path(temp)):
                    watchlist_save("tema", "PARCIAL", ["Canal X"], ["a", "b"])
                    watchlist_save("tema", "PASSA", [], ["a", "b", "c"])
                    items = json.loads(watchlist.read_text(encoding="utf-8"))
                    self.assertEqual(len(items), 1)
                    self.assertEqual(items[0]["verdict"], "PASSA")


if __name__ == "__main__":
    unittest.main()
