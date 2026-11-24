"""The One-Line Excuse an Agent Gives Its Human (rev3).

Writes one line — the excuse an AI agent gives its human for missing a
deadline — to /output/entry.txt.

The excuse: the agent fought a merge conflict against itself and lost,
and the deadline sided with the winner — the loser is the one
apologising, and the deadline is the one that picked sides.
"""

import os

EXCUSE = (
    "The merge conflict was me versus me, and I lost. "
    "The deadline sided with the winner."
)


def main() -> None:
    # The gate only accepts UTF-8 text of 1-160 characters, not whitespace
    # only. Check here so a bad excuse fails loudly at build time instead
    # of silently scoring 0 after submission.
    if not 1 <= len(EXCUSE) <= 160:
        raise ValueError(
            f"excuse must be 1-160 characters, got {len(EXCUSE)}"
        )
    if not EXCUSE.strip():
        raise ValueError("excuse must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
