#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human — make.fun bounty entry.

Writes one funny single-line one-star review from a house cat about its
human (under 200 characters) to /output/entry.txt, creating /output if
needed.
"""

import os
import sys

ENTRY = (
    "One star. The food was late by four minutes. "
    "I have filed a formal complaint by vomiting "
    "on the only rug he likes."
)

# The entry must stay a single line of 1-200 characters (gate rule).
assert 1 <= len(ENTRY) <= 200 and "\n" not in ENTRY


def main() -> None:
    # Grader-style invocation: honour MAKEFUN_OUTPUT_DIR first, then an
    # optional argv path, then the current directory (the grader runs with
    # no arguments in a read-only directory, so never default to /output).
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or (
        sys.argv[1] if len(sys.argv) > 1 else "."
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
