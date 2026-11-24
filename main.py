"""Write the locked entry line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Verified: entry is 142 chars, 144 bytes, single line, no trailing
newline — inside the 1-200 char gate.
"""
import os
from pathlib import Path

LINE = "I didn't miss the deadline, boss — I moved it. Your calendar said 'ship Friday', so my scheduler shipped it Friday. It is Friday. Next Friday."

def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")

if __name__ == "__main__":
    main()
