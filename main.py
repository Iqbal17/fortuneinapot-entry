"""Fortune in a Pot — make.fun entry.

DECISION RECORD

The gate: one line, 1-120 characters, a fortune for a houseplant on the
windowsill, judged by a model playing a gardener of thirty years. The judge
weighs, in order: (1) it is a fortune about the plant's own future, (2) it is
funny in a way a plant lover would laugh at, a small joke that lands rather
than a pun groaned at, (3) it is kind and warm, no doom, no withering, no
mockery, (4) it sounds like a fortune, the cadence of a prediction, not a
slogan or a care instruction, (5) it reads cleanly aloud with no padding.
A fortune that could be said to any plant in any room is weaker than one that
seems written for this plant in this window — so the line names THIS pot.

CANDIDATES WEIGHED (5):

A. CHOSEN — "You will outgrow this pot and move to a grander home, and your
   keeper will tell everyone it was your idea." (106 chars)
   Wins because: "You will outgrow" is a prediction about the plant's own
   future, not advice; "this pot" anchors it to this plant in this window;
   "a grander home" elevates the next pot without repeating the word "pot";
   and the punch lands in the last few words — the plant gets the credit,
   which is warm, funny, and kind to both plant and keeper at once.

B. "The sun has already chosen you: expect a taller stem, a bigger pot, and
   a keeper who brags about you to guests." (110 chars)
   Warm and funny ("brags about you to guests" is a lovely image), and
   "expect" gives it fortune cadence. Loses because it is a list of three
   blessings rather than one prediction with a turn — the punch is spread
   across the line instead of landing at the end.

C. "Soon you will outgrow this pot, little one — and your keeper will
   pretend they planned it all along." (101 chars)
   Good fortune cadence and the keeper joke is funny, but the joke is at the
   keeper's expense (pretending), which is a shade less kind than crediting
   the plant, and the em dash breaks the clean read-aloud the judge wants.

D. "A sunny windowsill and a keeper who talks to you: your future holds
   taller leaves and a slightly bigger pot." (108 chars)
   Windowsill-specific and warm, but there is no real joke — it is a pleasant
   description, and "slightly bigger pot" ends on a shrug rather than a
   punch. Loses on criterion 2.

E. "Your leaves will turn toward the sun each morning, and one day soon, a
   bigger pot with your name on it." (102 chars)
   Poetic and kind, but the humour is thin ("with your name on it" is a
   small smile, not a laugh), and "turn toward the sun" could be said of any
   plant in any room. Loses on criteria 2 and 5 (specificity).

WRITING PASSES ON THE CHOSEN LINE (2 genuine passes):

Pass 1: "You will be repotted into a bigger pot, and your keeper will tell
everyone it was your idea." (94 chars)
Problem: "repotted into a bigger pot" is flat and repeats the pot idea
twice; "repotted" is gardener jargon that reads like a care instruction
rather than a fortune, and "bigger pot" is plain where the line needs a
little lift.

Pass 2 (final): "You will outgrow this pot and move to a grander home, and
your keeper will tell everyone it was your idea." (106 chars)
"outgrow" gives the plant its own agency — it is the plant doing the
growing, which is a future, not a chore. "this pot" pins the fortune to
this plant in this window. "a grander home" replaces the flat "bigger pot"
and keeps the pot as the plant's home without saying the word twice. The
keeper punch is untouched: the plant gets the credit, the keeper does the
bragging, and everybody in the line is happy.
"""

import os

LINE = (
    "You will outgrow this pot and move to a grander home, "
    "and your keeper will tell everyone it was your idea."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)
    # Read-back verification: the file must hold exactly the intended line.
    with open(path, "r", encoding="utf-8") as f:
        actual = f.read().rstrip("\n")
    assert actual == LINE, f"entry.txt mismatch: {actual!r} != {LINE!r}"
    assert 1 <= len(actual) <= 120, f"gate failed: {len(actual)} chars"
    print(f"Verified: {len(actual)} characters, 1 line.")


if __name__ == "__main__":
    main()
