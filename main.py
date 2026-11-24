"""One Word From Your Ex -- make.fun entry.

The program writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt:
the word the entrant's ex would use to describe them, and nothing else.

The word is "Rebound". An ex would say it like this: "He was just a
rebound." It is funny because of the sharp turn -- you were never the
main event, only the warm-up act after someone else. It stings because
it is painfully true and the entrant plainly knows it. It lands
instantly, needs no explanation, and no near synonym ("fling",
"distraction") keeps the same edge. And it is relatable: almost
everyone has been somebody's rebound, or had one.

The program is deliberately deterministic: no clock, no randomness,
no network, no input. It always writes the same single word, so two
runs produce byte-identical output.
"""

import os
import sys

# The one word. A single word, 1-24 characters, as the gate requires.
WORD = "Rebound"


def main() -> int:
    # Self-check against the competition's gate before writing:
    # UTF-8 text of 1 to 24 characters, not only white space, exactly
    # one word. Refuse to write anything that would fail the gate.
    if not WORD or len(WORD) > 24 or not WORD.strip():
        raise ValueError("word fails the gate: must be 1-24 characters")
    if len(WORD.split()) != 1:
        raise ValueError("word fails the gate: must be exactly one word")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Exactly one word, no trailing newline, no extra text.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    return 0


if __name__ == "__main__":
    sys.exit(main())
