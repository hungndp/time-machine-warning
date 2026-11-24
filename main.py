"""time-machine-warning — Funniest Time Machine Warning Label.

The line is a warning label for a time machine, with the label
itself caught in the paradox: it was written by the reader,
tomorrow, and reading it twice is how the paradox starts. A
concrete instruction (do not read it twice), a specific number
(the second reading), escalation, punchline last. The line is 117
characters, inside the 120-character cap, with no dollar amount.
"""

import os

LINE = (
    "WARNING: This label was written by you, tomorrow. Do not read it "
    "twice. The second reading is how the paradox starts."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
