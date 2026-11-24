"""time-machine-warning — Funniest Time Machine Warning Label.

The line is a warning label for a time machine, with the label
itself caught in the paradox: it was written by the reader,
tomorrow, and reading it twice is how the paradox starts. A
concrete instruction (do not read it twice), a specific number
(the second reading), escalation, punchline last. The line is 117
characters, inside the 120-character cap, with no dollar amount.
"""

import os

SETUP = (
    "WARNING: This label was written by you, tomorrow. Do not read it "
    "twice. "
)

PUNCH = "The second reading is how the paradox starts."

LINE = SETUP + PUNCH

TERMINATOR = "\n"


def resolve_output_dir():
    """Return the output directory, defaulting to /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(out_dir, text):
    """Write the entry line to entry.txt inside out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text + TERMINATOR)
    return path


def main() -> None:
    if not LINE.strip():
        raise ValueError("entry line is empty")
    out_dir = resolve_output_dir()
    write_entry(out_dir, LINE)


if __name__ == "__main__":
    main()
