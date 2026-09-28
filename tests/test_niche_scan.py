import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

SKILL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / "scripts"))

import niche_scan
from niche_scan import require_scope, token_scopes, trends_cache_get, trends_cache_set, watchlist_due, watchlist_save


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
