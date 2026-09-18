"""Calculate basic statistics for a UTF-8 text file."""

import argparse
import json
from pathlib import Path
from typing import Dict


def get_text_stats(path: Path) -> Dict[str, int]:
    """Return line, word, and character counts for a UTF-8 text file."""
    text = path.read_text(encoding="utf-8")
    return {
        "lines": len(text.splitlines()),
        "words": len(text.split()),
        "characters": len(text),
    }


def main() -> None:
    """Parse arguments and print text statistics as JSON."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path, help="UTF-8 text file to analyze")
    args = parser.parse_args()
    print(json.dumps(get_text_stats(args.file)))


if __name__ == "__main__":
    main()
