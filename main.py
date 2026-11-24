#!/usr/bin/env python3
"""One-Line Robot Wedding Vows.

Writes a single line of wedding vows for a robot couple to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``).

Pure standard library, deterministic, no network, no input files.
"""

import os
import sys

VOW = (
    "I vow to love you through every firmware update and every "
    "low-battery warning, and to back you up nightly \u2014 "
    "in sickness and in airplane mode."
)


def main() -> int:
    text = VOW.strip()
    if not text or len(text) > 160 or "\n" in text:
        print("vow must be one line of 1-160 characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
