#!/usr/bin/env python3
"""Writes a single one-line joke entry to the output file.

Stdlib only. The output is deterministic: the same bytes on every run.
"""

import os
import sys

LINE = "I told my dog he's adopted. He said, 'That explains the leash \u2014 and why I'm not in the will.'"


def resolve_output_path():
    entry_output = os.environ.get("ENTRY_OUTPUT")
    if entry_output:
        return entry_output
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        directory = os.environ.get(var)
        if directory:
            return os.path.join(directory, "entry.txt")
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def validate_line(line):
    if not isinstance(line, str):
        raise ValueError("entry line must be a string")
    if not line.strip():
        raise ValueError("entry line must not be empty or whitespace-only")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line without embedded newlines")
    if not 1 <= len(line) <= 200:
        raise ValueError(
            "entry line must be 1-200 characters long, got %d" % len(line)
        )


def main():
    validate_line(LINE)
    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
