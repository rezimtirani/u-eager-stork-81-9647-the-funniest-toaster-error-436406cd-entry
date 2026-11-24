#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun entry.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt (default ./output):
the error message a kitchen toaster shows its owner when something
goes wrong. Deadpan appliance voice, no setup, lands in one read.

Run:  python3 main.py
"""

import os

LINE = "E04: Your bagel is still frozen. I refuse to participate in this."


def gate_ok(text):
    """Check the gate from RULES.txt: UTF-8, 1-120 chars, not blank."""
    if not isinstance(text, str):
        return False
    if not text or text.strip() == "":
        return False
    if len(text) > 120:
        return False
    text.encode("utf-8")
    return True


def write_entry(out_dir):
    """Write the line to entry.txt inside out_dir and return its path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    return path


def verify_written(path, expected):
    """Re-read the file and confirm it matches the line byte for byte."""
    with open(path, "r", encoding="utf-8", newline="") as handle:
        actual = handle.read()
    if actual != expected:
        raise SystemExit("written entry does not match the line")
    if len(actual.encode("utf-8")) > 120:
        raise SystemExit("written entry is over 120 bytes")
    return len(actual)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "output")
    if not gate_ok(LINE):
        raise SystemExit("entry fails the gate")
    path = write_entry(out_dir)
    size = verify_written(path, LINE)
    print("Wrote %s (%d chars, verified)" % (path, size))


if __name__ == "__main__":
    main()
