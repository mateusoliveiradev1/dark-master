import sys
import unittest
from pathlib import Path
from unittest import mock

SKILL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / "scripts"))

from remotion_check import check, parse_vitest

VITEST_OK = " Test Files  3 passed (3)\n      Tests  45 passed (45)\n"
VITEST_FAIL = " Test Files  1 failed | 2 passed (3)\n      Tests  2 failed | 43 passed (45)\n"


class RemotionCheckTests(unittest.TestCase):
    def test_parse_vitest_ok(self):
        parsed = parse_vitest(VITEST_OK)
        self.assertEqual((parsed["files"], parsed["passed"], parsed["failed"]), (3, 45, 0))

    def test_parse_vitest_fail(self):
        parsed = parse_vitest(VITEST_FAIL)
        self.assertEqual(parsed["failed"], 2)

    def test_check_verde_mockado(self):
        proc = mock.Mock(returncode=0, stdout=VITEST_OK, stderr="")
        with mock.patch("remotion_check.run_npm", return_value=(proc, "")):
            result = check(skip_typecheck=True)
            self.assertEqual(result["status"], "PASS")
            self.assertEqual(result["tests"]["passed"], 45)

    def test_check_vermelho_mockado(self):
        proc = mock.Mock(returncode=1, stdout=VITEST_FAIL, stderr="")
        with mock.patch("remotion_check.run_npm", return_value=(proc, "")):
            result = check(skip_typecheck=True)
            self.assertEqual(result["status"], "FAIL")

    def test_vitest_real_roda(self):
        import remotion_check
        proc, error = remotion_check.run_npm(["test"])
        self.assertEqual(error, "")
        parsed = parse_vitest(proc.stdout + proc.stderr)
        self.assertGreater(parsed["passed"], 0)
        self.assertEqual(parsed["failed"], 0)


if __name__ == "__main__":
    unittest.main()
