#!/usr/bin/env python3
"""The joke the reviewer laughs at.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

No network, no randomness, no dependencies: the joke is a fixed text,
so every run writes the same valid entry (UTF-8, 1-280 code points,
not only whitespace).
"""

import os
import sys


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    joke = "My coding agent rewrote 47 files to fix one typo \u2014 and missed the only file that had it."
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(joke)
    chars = len(joke)
    if not (1 <= chars <= 280) or not joke.strip():
        print(f"INVALID: {chars} code points", file=sys.stderr)
        return 1
    print(f"Wrote {path}: {chars} code points, {len(joke.encode('utf-8'))} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
