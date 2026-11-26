#!/usr/bin/env python3
"""Deadpan weather forecast for a city that does not exist.

Writes one line (<=160 chars) to /output/entry.txt: an overnight forecast
for Quibbleford, where the fog thickens into custard. The joke is a single
deadpan twist delivered as a straight broadcast line, with three concrete
details (2 a.m., three feet of visibility, a low of 4 degrees) so the
invented place feels real.

The output is fully deterministic: the same line every run.

Line choices, in order:
- Opening sets the invented place and the overnight slot, like a real
  broadcast, so the listener accepts the premise before the twist.
- "fog thickens into custard" is the one impossible detail; everything
  else in the line stays plausible, which is what makes it deadpan.
- The three concrete numbers (2 a.m., three feet, 4 degrees) anchor the
  invented place: specificity is what sells a fake forecast.
- The closing beat ("bring a spoon") resolves the custard image as
  practical advice instead of a punchline, keeping the tone flat.
"""

import os

# The forecast is a single literal so the output can never drift between
# runs: no randomness, no clock, no environment input affects the line.
FORECAST = (
    # Setup: place + overnight slot, straight broadcast phrasing.
    "Overnight in Quibbleford, fog thickens into custard by 2 a.m., "
    # Concrete details: visibility and low temperature, as a real
    # forecast would report them.
    "visibility three feet, low of 4 degrees. "
    # Payoff: deadpan advice that treats the custard as normal.
    "Drivers should allow extra time \u2014 and bring a spoon."
)


def main() -> None:
    # OUTPUT_DIR is honoured so the kit can redirect output; /output is
    # the default the competition expects.
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORECAST)


if __name__ == "__main__":
    main()
