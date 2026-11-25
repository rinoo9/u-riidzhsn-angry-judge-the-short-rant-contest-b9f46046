"""Angry Judge: The Short Rant Contest entry.

Writes one short, funny rant about an everyday annoyance to /output/entry.txt.
Deterministic: no network, no randomness, no input.
"""

import os

ENTRY = "The self-checkout froze on 'unexpected item in the bagging area'. The only unexpected item was my will to live — and it still made me wait for assistance."


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
