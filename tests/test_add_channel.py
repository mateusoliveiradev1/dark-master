import json
import sys
import unittest
from pathlib import Path
from unittest import mock

SKILL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / "scripts"))

import add_channel
from add_channel import add, suggest_watchers


class AddChannelTests(unittest.TestCase):
    def test_rejeita_duplicado(self):
        with mock.patch.object(add_channel, "CHANNELS", Path("/inexistente.json")):
            import builtins
            real_open = open
            channels = {"channels": [{"handle": "@A", "niche": "x"}]}
            with mock.patch("pathlib.Path.read_text", return_value=json.dumps(channels)):
                with mock.patch("pathlib.Path.write_text"):
                    with mock.patch("learn_loop.build_dashboard", return_value={}):
                        result = add("@a", "", False, "x", "BR", "pt", {"title": "A"}, dry_run=False)
                        self.assertEqual(result["status"], "FAIL")

    def test_dry_run_nao_escreve(self):
        with mock.patch("pathlib.Path.read_text", return_value='{"channels": []}'):
            written = []
            with mock.patch("pathlib.Path.write_text", lambda self, *a, **k: written.append(str(self))):
                result = add("@Novo", "Novo", True, "true-crime", "BR", "pt",
                             {"title": "Novo", "subs": 10, "videos_total": 3, "country": "BR",
                              "recent": []}, dry_run=True)
                self.assertEqual(result["status"], "DRY_RUN")
                self.assertEqual(written, [])
                self.assertEqual(result["channel"]["handle"], "@Novo")
                self.assertTrue(result["channel"]["mine"])

    def test_sugere_vigias_do_mesmo_nicho(self):
        channels = {"channels": [
            {"handle": "@A", "niche": "true-crime"},
            {"handle": "@B", "niche": "financas"},
            {"handle": "@C", "niche": "true-crime"},
        ]}
        with mock.patch("pathlib.Path.read_text", return_value=json.dumps(channels)):
            self.assertEqual(suggest_watchers("true-crime", "@Novo"), ["@A", "@C"])
            self.assertEqual(suggest_watchers("financas", "@Novo"), ["@B"])

    def test_validate_aborta_pais_diferente(self):
        fake_yt = mock.MagicMock()
        fake_yt.channels.return_value.list.return_value.execute.return_value = {
            "items": [{"id": "x", "snippet": {"title": "T", "country": "US"},
                       "statistics": {"subscriberCount": "5", "videoCount": "2"},
                       "contentDetails": {"relatedPlaylists": {}}}]}
        with mock.patch("niche_scan.yt_client", return_value=fake_yt):
            with mock.patch("niche_scan.creds"):
                result = add_channel.validate("@T", "BR", "pt")
                self.assertFalse(result["ok"])
                self.assertIn("US", result["error"])


if __name__ == "__main__":
    unittest.main()
