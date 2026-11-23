"""Warning label for humans: one line, big laugh.

Writes the entry deterministically to /output/entry.txt.
The line is a single-line safety warning label, 154 characters,
with the laugh landing in the last few words.

Craft notes — why this one-liner works:
- Label form: the "WARNING: Contents may ..." plus "Keep away from ..."
  structure borrows the dry, authoritative voice of a product safety
  label, so applying it to a human reads as instantly wrong and funny.
- Recognition: the first half lists three behaviours everyone catches
  themselves doing — overthinking, oversharing, and replying "haha" to
  nothing funny — so the reader sees themselves (or a friend) before the
  punchline arrives.
- The turn: the "keep away from" list starts mundane (Wi-Fi outages,
  Mondays) and escalates to a social dread — "anyone saying 'we need to
  talk'" — so the laugh lands in the last few words, on the most dreaded
  sentence in English.
- Gate: the entry must be 1-160 characters, a single line, and non-empty
  after stripping; main() asserts all three before writing.
"""

import os

ENTRY = (
    "WARNING: Contents may overthink, overshare, and reply 'haha' to nothing "
    "funny. Keep away from Wi-Fi outages, Mondays, and anyone saying "
    "'we need to talk'."
)

# Why this line: the first half lists three instantly recognisable human
# behaviours (overthinking, oversharing, fake-laughing at nothing), the
# second half escalates a standard "keep away from" label list, and the
# laugh lands in the last few words on the most dreaded sentence in
# English — "we need to talk". One idea, one line, label wording throughout.


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
