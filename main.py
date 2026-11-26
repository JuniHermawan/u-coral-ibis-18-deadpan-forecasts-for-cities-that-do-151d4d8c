#!/usr/bin/env python3
"""Deadpan weather forecast for a city that does not exist.

Writes one line (<=160 chars) to /output/entry.txt: an overnight forecast
for Quibbleford, where the fog thickens into custard. The joke is a single
deadpan twist delivered as a straight broadcast line, with three concrete
details (2 a.m., three feet of visibility, a low of 4 degrees) so the
invented place feels real.

The output is fully deterministic: the same line every run.
"""

import os

FORECAST = (
    "Overnight in Quibbleford, fog thickens into custard by 2 a.m., "
    "visibility three feet, low of 4 degrees. "
    "Drivers should allow extra time \u2014 and bring a spoon."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORECAST)


if __name__ == "__main__":
    main()
