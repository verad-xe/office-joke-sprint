#!/usr/bin/env python3
"""One-Line Office Joke: writes a single office joke to entry.txt."""

import os

# The hook: a performance review — the moment your pay is decided — derailed
# by the office's most mundane failure, the printer; the punchline makes the
# raise literal, queued behind forty copies of the org chart.
JOKE = "The printer jammed during my performance review, so my raise is stuck in the queue behind forty copies of the org chart."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Gate self-check: the sealed scorer only accepts UTF-8 text of
    # 1-200 characters that is not only white space, on a single line.
    text = JOKE.strip()
    assert text, "joke must not be blank"
    assert "\n" not in text and "\r" not in text, "joke must be a single line"
    assert 1 <= len(text) <= 200, "joke must be 1-200 characters, got %d" % len(text)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
