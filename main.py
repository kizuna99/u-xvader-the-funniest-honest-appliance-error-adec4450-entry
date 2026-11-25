#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Write the entry line for 'The Funniest Honest Appliance Error'.

The program writes one line of at most 200 characters to /output/entry.txt:
the funniest honest error message an appliance could show.
"""

import os

ENTRY = (
    "ERROR: Drain blocked. I am sitting in your grey water. "
    "I have seen what was in your pockets. We will not discuss it."
)


def main() -> None:
    # The grader reads /output/entry.txt; fall back to ./output for local runs.
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = os.path.join("output", "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
