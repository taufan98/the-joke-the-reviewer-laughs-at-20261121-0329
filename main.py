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

# The joke lives in the data, not buried in main(): the em-dash is the
# hinge -- everything before it is the heroic setup (47 files for one
# typo), everything after it is the punchline (the one file that had
# the typo is the one it missed). One line, no trailing newline: the
# gate counts code points, and a stray newline would be a second line.
JOKE = "My coding agent rewrote 47 files to fix one typo \u2014 and missed the only file that had it."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    joke = JOKE
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
