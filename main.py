"""Write the tournament-winning one-line excuse to /output/entry.txt."""

import os

ENTRY = "I finished it, then autosave replaced it with Tuesday's version. Tuesday disagrees with everything."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Self-check: read back and verify the written file matches exactly.
    with open("/output/entry.txt", "rb") as f:
        data = f.read()
    assert data == ENTRY.encode("utf-8"), "entry.txt does not match the winning line"
    assert len(data) == 99, f"entry.txt must be 99 bytes, got {len(data)}"
    assert not data.endswith(b"\n"), "entry.txt must not end with a newline"


if __name__ == "__main__":
    main()
