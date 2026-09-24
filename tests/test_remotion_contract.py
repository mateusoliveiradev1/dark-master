import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import remotion


class RemotionContractTests(unittest.TestCase):
    def test_srt_seconds_parses_milliseconds(self):
        self.assertEqual(remotion.srt_seconds("00:01:02,250"), 62.25)

    def test_block_type_maps_editorial_beats(self):
        self.assertEqual(remotion.block_type({"beat": "EVIDÊNCIAS"}), "evidence-reveal")
        self.assertEqual(remotion.block_type({"beat": "LINHA DO TEMPO"}), "timeline")

    def test_theme_keeps_channel_values(self):
        theme = remotion.theme_from_style({"background": "#112233", "accent": "#445566"})
        self.assertEqual(theme["background"], "#112233")
        self.assertEqual(theme["accent"], "#445566")
        self.assertEqual(theme["safeArea"], {"x": 72, "y": 54})


if __name__ == "__main__":
    unittest.main()
