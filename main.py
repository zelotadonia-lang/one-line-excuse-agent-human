"""Write the tournament-winning one-line excuse to /output/entry.txt.

Round 2 entry (89 bytes): the file was compressed to save time until
only the word 'soon' was left.
"""

import os

ENTRY = "I compressed the file to save time. It is now 12 bytes and contains only the word 'soon'."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Self-check: read back and verify the written file matches exactly.
    with open("/output/entry.txt", "rb") as f:
        data = f.read()
    assert data == ENTRY.encode("utf-8"), "entry.txt does not match the winning line"
    assert len(data) == 89, f"entry.txt must be 89 bytes, got {len(data)}"
    assert b"'soon'" in data, "entry.txt must contain the payoff word 'soon'"
    assert not data.endswith(b"\n"), "entry.txt must not end with a newline"


if __name__ == "__main__":
    main()
