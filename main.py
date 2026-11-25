#!/usr/bin/env python3
"""One-Line Office Jokes entry: writes one funny line about office life."""
import os

ENTRY = "I hit reply-all to ask everyone to stop replying all \u2014 and 47 people agreed, all at once."

def main():
    line = ENTRY.strip()
    # Gate: /output/entry.txt must be UTF-8 text of 1-199 chars, one line.
    assert 1 <= len(line) <= 199, f"entry must be 1-199 chars, got {len(line)}"
    assert "\n" not in line, "entry must be a single line"
    assert line.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")

if __name__ == "__main__":
    main()
