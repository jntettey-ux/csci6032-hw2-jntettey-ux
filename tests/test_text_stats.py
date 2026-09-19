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

    def test_top_words_are_case_insensitive_and_ties_are_alphabetical(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "top.txt"
            path.write_text("Beta alpha ALPHA beta gamma", encoding="utf-8")

            self.assertEqual(
                get_text_stats(path, top=3)["top"],
                [
                    {"word": "alpha", "count": 2},
                    {"word": "beta", "count": 2},
                    {"word": "gamma", "count": 1},
                ],
            )

    def test_top_zero_returns_no_words(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "top.txt"
            path.write_text("one two", encoding="utf-8")

            self.assertEqual(get_text_stats(path, top=0)["top"], [])

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

    def test_command_line_top_option(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "cli-top.txt"
            path.write_text("Red blue RED green blue", encoding="utf-8")

            result = subprocess.run(
                [sys.executable, "src/text_stats.py", "--top", "2", str(path)],
                check=True,
                capture_output=True,
                text=True,
            )

            self.assertEqual(
                json.loads(result.stdout)["top"],
                [
                    {"word": "blue", "count": 2},
                    {"word": "red", "count": 2},
                ],
            )


if __name__ == "__main__":
    unittest.main()
