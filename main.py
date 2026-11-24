"""Warning label for humans: one line, big laugh.

Writes the entry deterministically to /output/entry.txt.
The line is a single-line safety warning label, 124 characters,
with the laugh landing in the last few words.

Craft notes — why this one-liner works:
- Label form: the "WARNING: Contents may ..." structure borrows the dry,
  authoritative voice of a product safety label, so applying it to a human
  reads as instantly wrong and funny.
- Recognition: the first half lists three behaviours everyone recognises —
  taking offence at nothing, remembering it forever, and dragging it into
  every later argument — so the reader sees themselves (or a friend) before
  the punchline arrives.
- The turn: the line escalates from a harmless slight to a life sentence —
  "for the next ten years" — so the laugh lands in the last few words, on
  the absurdly long grudge.
- Gate: the entry must be 1-160 characters, a single line, and non-empty
  after stripping; main() asserts all three before writing.
"""

import os

ENTRY = (
    "WARNING: Contents may take offense at nothing, remember it forever, "
    "and mention it in every argument for the next ten years."
)

# Why this line: the first half lists three instantly recognisable human
# behaviours (taking offence at nothing, never forgetting it, dragging it
# into every later argument), and the laugh lands in the last few words on
# the absurd escalation — a grudge that lasts "for the next ten years".
# One idea, one line, label wording throughout.


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
