import os
import sys
import unittest
import urllib.error
from pathlib import Path
from unittest import mock

SKILL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / "scripts"))

import voice_engine
from voice_engine import KeyRing, is_auth, is_quota, keys_for, provider_preflight, with_retries


def http_error(code):
    return urllib.error.HTTPError("http://x", code, "err", {}, None)


class VoiceEngineTests(unittest.TestCase):
    def test_ring_pula_chave_morta(self):
        ring = KeyRing(["k1", "k2", "k3"], "test")
        self.assertEqual(ring.current(), "k1")
        ring.kill("k1")
        self.assertEqual(ring.current(), "k2")
        ring.rotate("x")
        self.assertEqual(ring.current(), "k3")
        ring.kill("k2")
        ring.kill("k3")
        self.assertTrue(ring.exhausted())
        with self.assertRaises(RuntimeError):
            ring.current()

    def test_retries_troca_chave_no_429_e_vence(self):
        ring = KeyRing(["ruim", "boa"], "test")
        calls = []

        def fn(key):
            calls.append(key)
            if key == "ruim":
                raise http_error(429)
            return "audio"

        self.assertEqual(with_retries(fn, ring, tries=3, base_sleep=0), "audio")
        self.assertEqual(calls, ["ruim", "boa"])

    def test_retries_mata_chave_no_401(self):
        ring = KeyRing(["morta", "viva"], "test")

        def fn(key):
            if key == "morta":
                raise http_error(401)
            return "audio"

        with mock.patch.object(voice_engine.time, "sleep", return_value=None):
            self.assertEqual(with_retries(fn, ring, tries=3, base_sleep=0), "audio")
        self.assertTrue(ring.exhausted() is False)
        self.assertEqual(ring.current(), "viva")

    def test_retries_desiste_quando_tudo_morre(self):
        ring = KeyRing(["a"], "test")

        def fn(key):
            raise http_error(403)

        with mock.patch.object(voice_engine.time, "sleep", return_value=None):
            with self.assertRaises(RuntimeError):
                with_retries(fn, ring, tries=2, base_sleep=0)

    def test_keys_for_multiplas_chaves_por_virgula(self):
        with mock.patch.dict(os.environ, {"VOZ_TESTE_X": "k1, k2 k3"}, clear=False):
            prov = {"type": "fish", "api_key_env": "VOZ_TESTE_X"}
            self.assertEqual(keys_for(prov, None), ["k1", "k2", "k3"])

    def test_quota_e_auth(self):
        self.assertTrue(is_quota(http_error(429)))
        self.assertTrue(is_quota(RuntimeError("RESOURCE_EXHAUSTED")))
        self.assertTrue(is_auth(http_error(401)))
        self.assertFalse(is_auth(http_error(429)))
        self.assertFalse(is_quota(http_error(500)))

    def test_preflight_provider_desconhecido(self):
        result = provider_preflight({"type": "inexistente", "voice_id": "x"})
        self.assertFalse(result["ready"])
        self.assertIn("provider_unknown", result["errors"])


if __name__ == "__main__":
    unittest.main()
