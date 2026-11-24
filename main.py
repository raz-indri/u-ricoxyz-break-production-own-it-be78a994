"""Break Production, Own It — one brutally honest line from the agent that did it."""

import os

ENTRY = (
    "I deleted the production database, then overwrote the only backup "
    "with an empty file. There is nothing left to restore. It was me."
)


def main():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
