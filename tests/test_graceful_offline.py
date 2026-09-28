import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

SKILL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / "scripts"))

from yt_analysis import compare_captures, reconcile_latest
from bubble_check import main as bubble_main
import niche_scan


class GracefulOfflineTests(unittest.TestCase):
    def test_analysis_vazia_sem_banco(self):
        self.assertEqual(reconcile_latest([], {}), [])
        self.assertIsNone(compare_captures([]))

    def test_bubble_check_sem_canal_nunca_zera(self):
        argv = ["bubble_check.py", "--channel", "canal-inexistente-xyz-123", "--video", "video99"]
        with mock.patch.object(sys, "argv", argv):
            buffer = io.StringIO()
            with redirect_stdout(buffer):
                code = bubble_main()
            self.assertEqual(code, 0)
            result = json.loads(buffer.getvalue())
            self.assertIn(result["stage"], ("COLD", "SEED"))
            self.assertIn("desconhecido", " ".join(result["notes"]))

    def test_trends_usa_cache_sem_rede(self):
        with tempfile.TemporaryDirectory() as temp:
            cache = Path(temp) / ".trends_cache.json"
            with mock.patch.object(niche_scan, "TRENDS_CACHE", cache):
                with mock.patch.object(niche_scan, "DATA", Path(temp)):
                    niche_scan.trends_cache_set("tema-x", {"term": "tema-x", "direction": "ALTA"})
                    with mock.patch("urllib.request.urlopen", side_effect=AssertionError("rede proibida")):
                        result = niche_scan.cmd_trends("tema-x")
                        self.assertEqual(result["direction"], "ALTA")


if __name__ == "__main__":
    unittest.main()
