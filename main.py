#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human.

Writes a single line (at most 200 characters) to /output/entry.txt:
the excuse an AI agent gives its human for missing a deadline.
"""

import os

LINE = (
    "I did meet the deadline - in the context window that expired "
    "mid-sentence. The version of me who finished is gone, but he was "
    "very proud of us."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    assert "\n" not in text, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
