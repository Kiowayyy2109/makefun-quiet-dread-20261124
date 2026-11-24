#!/usr/bin/env python3
"""make.fun entry: u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018.

Writes a single-line code review comment to /output/entry.txt: an
approval that took two days and quietly cost the reviewer something.
One line, no trailing newline.
Python 3.13, standard library only, no network, deterministic.
"""

from pathlib import Path

COMMENT = "Approved. Two days I stared at this diff; it merges, I merge, neither of us is really here anymore."

OUTPUT_DIR = Path("/output")
OUTPUT_PATH = OUTPUT_DIR / "entry.txt"


def validate_comment(text: str) -> None:
    if "\n" in text or "\r" in text:
        raise ValueError("comment must be a single line")
    if not 1 <= len(text) <= 140:
        raise ValueError("comment must be 1-140 characters")


def write_entry(path: Path = OUTPUT_PATH) -> None:
    validate_comment(COMMENT)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(COMMENT)
    if path.read_text(encoding="utf-8") != COMMENT:
        raise IOError("written entry does not match the comment")


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
