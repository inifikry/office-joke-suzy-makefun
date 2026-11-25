#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line office joke to /output/entry.txt.
Deterministic: the same joke, byte for byte, on every run.
"""

import os

JOKE = "My boss said dress for the job you want, so I came in pajamas: my dream job is being unemployed."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate guard: entry must be 1-200 characters, a single line, not blank.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert "\n" not in JOKE and JOKE.strip(), "joke must be one non-blank line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
