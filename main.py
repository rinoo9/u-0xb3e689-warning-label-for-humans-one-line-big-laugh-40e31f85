"""Warning label for humans: one line, big laugh.

Writes the entry deterministically to /output/entry.txt.
The line is a single-line safety warning label, 113 characters,
with the laugh landing in the last few words.

Craft notes — why this one-liner works:
- Label form: the "WARNING: Do not feed after midnight" structure borrows
  the dry, authoritative voice of a product safety label — and the old
  Gremlins rule — so applying it to a human reads as instantly wrong
  and funny.
- Recognition: everyone has met the late-night human who turns into an
  amateur philosopher, so the reader sees a friend before the punchline.
- The turn: the line escalates through three late-night personas —
  philosopher, DJ, conspiracy theorist — and "in that order" makes it a
  schedule, as if the transformation were documented and repeatable.
- Gate: the entry must be 1-160 characters, a single line, and non-empty
  after stripping; main() asserts all three before writing.
"""

import os

ENTRY = (
    "WARNING: Do not feed after midnight. Human becomes a philosopher, "
    "a DJ, and a conspiracy theorist, in that order."
)

# Why this line: the label form borrows the dry voice of a product safety
# warning (and the old Gremlins rule), and the laugh lands in the last few
# words on the escalation — three late-night personas, "in that order", as
# if the transformation were a documented schedule. One idea, one line,
# label wording throughout.


def main() -> None:
    # Gate: 1-160 chars, not only whitespace, single line.
    assert 1 <= len(ENTRY) <= 160, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.strip() == ENTRY
    assert "\n" not in ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote /output/entry.txt ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
