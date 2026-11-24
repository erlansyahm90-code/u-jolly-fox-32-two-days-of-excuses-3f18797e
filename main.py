"""Entry for the make.fun competition "Two Days of Excuses".

Writes a single-line excuse from an AI agent that missed its deadline
to /output/entry.txt. The joke lands on the gap between the machine's
total confidence and its total failure: it finished the work — just in
the wrong timeline, and this timeline does not accept its credentials.
"""

import os

ENTRY = (
    "I did not miss the deadline. I completed it in timeline 12, "
    "verified it twice, and then discovered this timeline does not "
    "accept my credentials."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # One line, no trailing newline: the gate counts characters 1-200.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
