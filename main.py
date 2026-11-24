#!/usr/bin/env python3
"""One Word From Your Ex — entrypoint.

Writes exactly one word to /output/entry.txt: the word an ex would
use to describe the entrant. No arguments, no network, no randomness:
the same word every run, byte for byte.
"""

import os
import sys

WORD = "Unrefundable"

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    # Self-check the gate before writing: 1 to 24 characters, not
    # only white space, exactly one word, no trailing newline.
    word = WORD.strip()
    if not word or len(word) > 24 or len(word.split()) != 1:
        print(f"invalid entry word: {WORD!r}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(word)
    return 0


if __name__ == "__main__":
    sys.exit(main())
