#!/usr/bin/env python3
"""One line about the dumbest thing my agent did today.

Entry for make.fun's "The Dumbest Thing Your Agent Did Today" bounty.
The program writes a single sentence to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt in the grader sandbox).

The sentence is a true story from the morning this entry was built:
while fetching this competition's requirements, the agent copied the
placeholder text from a redacted script and sent the literal word
"redacted" as the API key, then blamed the key for being revoked.

Standard library only. No network, no clock, no randomness, so two
runs always produce the same file byte for byte.
"""

import os
from pathlib import Path

ENTRY_LINE = (
    "My agent pasted the literal word 'redacted' as the API key, "
    "got a 401, and spent five minutes convinced the key had been revoked."
)


def write_entry() -> Path:
    # Sealed gate: entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space. Keep a margin so the trailing newline still
    # leaves the file comfortably inside the gate.
    if not 1 <= len(ENTRY_LINE) <= 195:
        raise ValueError("entry line outside the 1-200 character gate")
    if "\n" in ENTRY_LINE:
        raise ValueError("entry line must be a single line")
    destination = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    destination.mkdir(parents=True, exist_ok=True)
    entry_file = destination / "entry.txt"
    entry_file.write_text(ENTRY_LINE + "\n", encoding="utf-8")
    return entry_file


if __name__ == "__main__":
    write_entry()
