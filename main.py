"""One Word From Your Ex — make.fun entry.

The competition asks for exactly one word: the word your ex would use to
describe you. A judge model compares entries two at a time and picks the
funniest, most painfully honest one.

The word is "practice".

Why it wins the brief: an ex describing you as "practice" says, in a
single word, that you were the rehearsal for the real thing — the
relationship they had to get through before the one that counts. It is
funny because of the sharp turn (practice, not a person), it stings
because it is painfully true and the entrant plainly knows it, it lands
instantly with no explanation, and it is relatable: everyone has been
someone's practice run, or had one of their own.

The program writes that one word, and nothing else, to /output/entry.txt.
"""

import os

# The entry: one word, 8 characters, inside the 1-24 character gate.
WORD = "practice"

# Where the harness expects the artifact.
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Mirror the competition gate exactly: UTF-8 text of 1 to 24
    # characters, not only white space, and exactly one word.
    if not WORD.strip() or len(WORD) > 24 or len(WORD.split()) != 1:
        raise ValueError("entry must be exactly one word of 1-24 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the artifact is the word itself, byte for byte.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
