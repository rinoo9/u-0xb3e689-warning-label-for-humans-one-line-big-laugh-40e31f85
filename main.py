"""Warning label for humans: one line, big laugh.

Writes the entry deterministically to /output/entry.txt.
The line is a single-line safety warning label, 154 characters,
with the laugh landing in the last few words.
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
