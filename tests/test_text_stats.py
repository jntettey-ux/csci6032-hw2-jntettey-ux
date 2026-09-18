import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from src.text_stats import get_text_stats


class TextStatsTests(unittest.TestCase):
    def test_counts_lines_words_and_characters(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "example.txt"
            path.write_text("Hello world\nThis is a test\n", encoding="utf-8")

            self.assertEqual(
                get_text_stats(path),
                {"lines": 2, "words": 6, "characters": 27},
            )

    def test_counts_unicode_characters(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "unicode.txt"
            path.write_text("Café 🌍\n", encoding="utf-8")

            self.assertEqual(
                get_text_stats(path),
                {"lines": 1, "words": 2, "characters": 7},
            )

    def test_empty_file_has_zero_counts(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "empty.txt"
            path.write_text("", encoding="utf-8")

            self.assertEqual(
                get_text_stats(path),
                {"lines": 0, "words": 0, "characters": 0},
            )

    def test_command_line_output_is_json(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "cli.txt"
            path.write_text("one two\nthree", encoding="utf-8")

            result = subprocess.run(
                [sys.executable, "src/text_stats.py", str(path)],
                check=True,
                capture_output=True,
                text=True,
            )

            self.assertEqual(
                json.loads(result.stdout),
                {"lines": 2, "words": 3, "characters": 13},
            )


if __name__ == "__main__":
    unittest.main()
