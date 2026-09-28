import csv
import json
import sys
import tempfile
import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / "scripts"))

from bubble_check import classify, load_csv_captures, parse_date


def captures(rows):
    return [{"date": parse_date(date), "views": views, "engaged": None, "likes": None}
            for date, views in rows]


class BubbleCheckTests(unittest.TestCase):
    def test_cold_sem_capturas(self):
        result = classify([], parse_date("2026-09-20"))
        self.assertEqual(result["stage"], "COLD")

    def test_seed_primeira_captura(self):
        result = classify(captures([("2026-09-28", 400)]), parse_date("2026-09-28"))
        self.assertEqual(result["stage"], "SEED")

    def test_stalled_flat_tres_capturas(self):
        result = classify(captures([("2026-09-20", 900), ("2026-09-24", 910), ("2026-09-28", 905)]),
                          parse_date("2026-09-20"))
        self.assertEqual(result["stage"], "STALLED")

    def test_expanding_acelera(self):
        result = classify(captures([("2026-09-20", 500), ("2026-09-24", 900), ("2026-09-28", 2500)]),
                          parse_date("2026-09-20"))
        self.assertEqual(result["stage"], "EXPANDING")

    def test_late_spike_apos_flat(self):
        result = classify(captures([("2026-09-01", 800), ("2026-09-10", 805), ("2026-09-20", 810), ("2026-09-28", 1500)]),
                          parse_date("2026-09-01"))
        self.assertEqual(result["stage"], "LATE_SPIKE")

    def test_amostra_pequena_sem_tendencia(self):
        result = classify(captures([("2026-09-20", 40), ("2026-09-28", 45)]), parse_date("2026-09-20"))
        self.assertEqual(result["stage"], "SEED")

    def test_csv_studio(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "exp.csv"
            with path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.writer(handle)
                writer.writerow(["snapshot_date", "views"])
                writer.writerow(["2026-09-20", "900"])
                writer.writerow(["2026-09-28", "905"])
            rows, error = load_csv_captures(str(path))
            self.assertEqual(error, "")
            result = classify(rows, parse_date("2026-09-20"))
            self.assertEqual(result["stage"], "STALLED")


if __name__ == "__main__":
    unittest.main()
