"""Calculate basic statistics for a UTF-8 text file."""

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Dict, Optional


def get_text_stats(path: Path, top: Optional[int] = None) -> Dict[str, object]:
    """Return line, word, and character counts for a UTF-8 text file."""
    text = path.read_text(encoding="utf-8")
    stats: Dict[str, object] = {
        "lines": len(text.splitlines()),
        "words": len(text.split()),
        "characters": len(text),
    }
    if top is not None:
        frequencies = Counter(word.casefold() for word in text.split())
        stats["top"] = [
            {"word": word, "count": count}
            for word, count in sorted(
                frequencies.items(), key=lambda item: (-item[1], item[0])
            )[:top]
        ]
    return stats


def non_negative_int(value: str) -> int:
    """Parse a non-negative integer for an argparse option."""
    number = int(value)
    if number < 0:
        raise argparse.ArgumentTypeError("must be non-negative")
    return number


def main() -> None:
    """Parse arguments and print text statistics as JSON."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path, help="UTF-8 text file to analyze")
    parser.add_argument(
        "--top",
        type=non_negative_int,
        metavar="N",
        help="include the N most frequent words",
    )
    args = parser.parse_args()
    print(json.dumps(get_text_stats(args.file, args.top)))


if __name__ == "__main__":
    main()
