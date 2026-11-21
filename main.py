#!/usr/bin/env python3
"""Write a short poem about permission to /output/entry.txt.

A sea poem: a fisherman asks the tide for a catch, and an old man
teaches his grandson how to ask properly - not demand, not beg -
and to accept whatever the sea gives back.
"""
import os

POEM = (
    "Grandad taught me to ask the sea -\n"
    "knuckle, not fist. The rope burns,\n"
    "salt stings the cracks in my hands.\n"
    "\n"
    "Some mornings the net comes heavy.\n"
    "Some mornings it comes up light,\n"
    "and he shakes the water out,\n"
    "wades back in to his knees,\n"
    "and lets the cold come to him.\n"
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)
    print(POEM, end="")


if __name__ == "__main__":
    main()
