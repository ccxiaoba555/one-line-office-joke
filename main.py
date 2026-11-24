#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint.

Writes a single original one-line joke about office life
(<=200 characters) to /output/entry.txt.

The joke: HR calls the company a family, so the only inheritance
this job ever leaves you is your predecessor's login and his
unfinished spreadsheets. Deterministic: the same single line on
every run, no network, no input.
"""

import os

JOKE = (
    "HR said we're a family, which explains why the only inheritance "
    "I got from this job is my predecessor's login and his unfinished "
    "spreadsheets."
)


def main() -> None:
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars"
    assert JOKE.strip() == JOKE and "\n" not in JOKE
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
