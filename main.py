#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — make.fun haiku entry.

Writes one 5-7-5 haiku about debugging to /output/entry.txt.
Python 3 standard library only.
"""

import os

HAIKU = (
    "breakpoint on line twelve\n"
    "cursor blinks at three a.m.\n"
    "the bug wore my face\n"
)


def main() -> None:
    # Guard the gate: exactly 3 lines, 1-200 chars, non-blank.
    lines = HAIKU.splitlines()
    assert len(lines) == 3, "haiku must be exactly 3 lines"
    assert 1 <= len(HAIKU) <= 200, "haiku must be 1-200 characters"
    assert all(line.strip() for line in lines), "no blank lines"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
