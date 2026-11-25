#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins — entry.

Writes exactly one roast line to /output/entry.txt (1-160 UTF-8 chars,
not only whitespace), as the sealed scorer's gate requires.
Deterministic, stdlib only, no network, no secrets, no randomness.
"""

import os

ENTRY = "My smart fridge locked me out for opening it too often, which is rich coming from an appliance whose only job is being opened."

# Why this line: seven candidates were drafted and program-counted (see
# BUILD_LOG.md). This one won because the setup is a real smart-fridge
# behaviour — door-open tracking, alarms, lockouts — and the sting turns
# the accusation back on the fridge: being opened IS its job. No milk
# joke, no 2 a.m. snack joke (both already in the field); one sentence,
# one image, the reversal lands on the last three words.


def main():
    # Gate self-check: the sealed scorer requires /output/entry.txt to be
    # UTF-8 text of 1 to 160 characters, not only whitespace. Fail loudly
    # here instead of shipping a rejected entry.
    assert 1 <= len(ENTRY) <= 160, f"entry length {len(ENTRY)} outside 1-160"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY == ENTRY.strip(), "entry has leading/trailing whitespace"
    assert all(ord(c) >= 32 for c in ENTRY), "entry has control characters"
    # The task requires a single line that sets up fast and lands with no
    # second sentence: exactly one sentence terminator, at the very end.
    assert sum(ENTRY.count(c) for c in ".!?") == 1, "entry must be one sentence"
    assert ENTRY.endswith("."), "entry must end with its single period"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back byte-for-byte: what is on disk must be exactly the entry.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == ENTRY, "read-back mismatch"


if __name__ == "__main__":
    main()
