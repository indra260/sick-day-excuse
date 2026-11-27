"""The Funniest Sick-Day Excuse -- make.fun entry.

Writes one short original sick-day excuse to /output/entry.txt: the
writer's lower back quits its job the moment they try to stand up,
so they call in sick before the rest of their body hands in notice
too. The excuse is a single constant: no input is read, nothing is
generated at run time, so two runs always produce byte-identical
output.
"""

import os
import sys

ENTRY_TEXT = (
    "I woke up, tried to stand, and my lower back immediately resigned. "
    "Calling in sick before the rest of me hands in its notice too."
)

MIN_CHARS = 1
MAX_CHARS = 200


def main() -> int:
    """Validate the excuse against the competition gate, then write it."""
    text = ENTRY_TEXT
    if (
        not text.strip()
        or not MIN_CHARS <= len(text) <= MAX_CHARS
        or "\n" in text
        or "\r" in text
    ):
        print(
            "entry out of gate: %d chars (must be %d-%d, one line)"
            % (len(text), MIN_CHARS, MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
