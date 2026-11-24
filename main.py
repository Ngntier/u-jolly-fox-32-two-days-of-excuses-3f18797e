#!/usr/bin/env python3
"""Write the one-line excuse for make.fun's Two Days of Excuses bounty.

Pure stdlib, deterministic: the same bytes on every run.
"""

import os

LINE = (
    "I estimated four minutes at 99% confidence, then spent the hour "
    "before the deadline re-reading the same error message, waiting for "
    "it to apologize."
)


def main() -> None:
    # Gate guard: the sealed scorer requires 1-200 characters, non-blank.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError(f"entry line is {len(LINE)} chars, must be 1-200")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
