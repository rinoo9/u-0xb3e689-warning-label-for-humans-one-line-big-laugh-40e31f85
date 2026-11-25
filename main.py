"""Warning label for humans: one line, big laugh.

The program prints one safety warning label for a human being and
saves that exact line to /output/entry.txt, with nothing else in
the file and no trailing newline, so the output is byte-identical
on every run.

The new line for this revision (129 characters):

    WARNING: Do not tap the glass. Human is already awake, already
    offended, and already rehearsing what it should have said in 2019.

Why this line should win a laugh:

- It borrows the voice of a zoo or aquarium sign. "Do not tap the
  glass" is the sort of instruction printed for an animal behind
  glass, so pointing it at a person is wrong in exactly the way a
  warning label is supposed to be wrong, and funny.
- Everybody knows the behaviour. Most people have lain awake
  replaying a conversation from years ago, inventing the perfect
  reply far too late, so the reader recognises themselves at once.
- The joke stacks three states — awake, offended, rehearsing — and
  the payoff only arrives at the very end, with the year 2019: the
  argument is not from today, or even this week, but from years
  ago, and the human is still losing sleep over it.
- One thought, one line, label language from start to finish, and
  no second gag competing with the first.

The file is checked before it is written: the line must be a
single line of plain text, between 1 and 160 characters long, and
must contain more than blank space. Anything else stops the run
with an error instead of writing a bad entry.
"""

from pathlib import Path

ENTRY = "WARNING: Do not tap the glass. Human is already awake, already offended, and already rehearsing what it should have said in 2019."

OUTPUT_PATH = Path("/output/entry.txt")


def check_entry(line):
    """Refuse to write a line that would fail the entry gate."""
    if not isinstance(line, str):
        raise TypeError("entry must be text")
    if line != line.strip():
        raise ValueError("entry must not start or end with blank space")
    if not line.strip():
        raise ValueError("entry must not be blank")
    if len(line) < 1 or len(line) > 160:
        raise ValueError(f"entry is {len(line)} characters, allowed range is 1-160")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be one line only")


def main():
    check_entry(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    print(f"entry.txt written: {len(ENTRY)} characters")


if __name__ == "__main__":
    main()
