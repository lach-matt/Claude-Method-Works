# DEF-153H — a regression I introduced at BUILD95, and why the Appendix D row is blocked.

## H-1  BUILD95 left §D.5.10's caption contradicting its own table  (REGRESSION, mine)

`r3-vocab.py` (BUILD94 -> BUILD95) moved the observability boundary's row on M's ruling:

    L10890  the observability boundary, tested once   law · physics   verified · sampled · found

It did not touch the caption below the same table, which still reads:

    L10910  The observability boundary is the second element to enter as *conjectured* (§D.5.7's
            slack = kernel was the first): one confirming instance, falsifiable, tested once — the
            compendium says so in those words, and *conjectured · sampled* is what those words are.
            Law · physics now holds four elements over three cells and closes; the box it spans
            admits *conjectured · exhaustive* and *proved · sampled*, and §6.1's bounds exclude
            both, which is the closure doing its work rather than the count.

Two faults, not one. The caption states a status the row no longer carries — that is a plain
contradiction. And the closure argument in its second half is COMPUTED FROM the coordinates the row
no longer has: "the box it spans", and which cells §6.1's bounds exclude, both change when
`conjectured · sampled` becomes `verified · sampled`. So the sentence is not merely stale wording,
it is an unsound argument, and repairing only the first half would leave an uncomputed claim
standing in the book.

The build that did this checked its substitution anchors, its press anchors and its reverse md5, and
none of those could have caught it: every guard was structural, and this is a semantic dependency
between a table and prose forty lines below it. That is DEF-153F item 3 with a consequence attached.

## H-2  The theorem/law split cannot be executed here — the element set is not reconstructible

DEF-153G item 1 proposed splitting the necessity-of-state row in two. Measured, that is not a row
edit but a RE-CLOSURE of §D.5.10, and it moves at least six recorded figures:

  - the sum: "Sixty-five elements become **seventy-seven** over **twenty-four** fibres, and E = 0"
  - "Law · physics now holds **four** elements over three cells"
  - Appendix D's whole-appendix fibre census: theorem · physics 2 -> 1, theorem · order 21 -> 22,
    law · physics 4 -> 5
  - F.4.2's bracket, which register 1449 records as recomputed at 77: 2.47 : 1, 0.288, 0.867 bits,
    and 128 -> 1.48 : 1 with the Index's terms
  - E itself, per fibre, under §6.1's ℛ

E is computable in principle — `tools/cypher.py --cells` takes a TSV of cells and returns
|ℛ(X)| − |X| — and the house discipline is to reproduce the recorded E = 0 at seventy-seven before
computing anything at seventy-eight.

**It cannot be reproduced from the volume.** The main volume holds FIVE element tables carrying
`element / fibre / coordinates`, at L10736, L10761, L10794, L10830 and L10882, and they hold
**45 rows in total**. The closure is stated over seventy-seven. Thirty-two elements of §D.5.2–§D.5.9
are not in that form and are not recoverable by reading the tables.

So computing E at 78 would mean inventing the element set that E is computed over. Register 1400's
precedent forbids exactly this: quoting against a basis the artefact does not supply is a fault.
The split is therefore NOT TAKEN, and the blocker is the missing element set rather than the ruling.

What would unblock it: the source §D.5.10 was closed from — the same generator estate as DEF-153F
item 1, or a listing of the sixty-five.

## Status

Both recorded, neither repaired, per the chat-67 hold. H-1 is a regression from a build run in this
session and is the more urgent of the two: the book currently contains a contradiction it did not
contain at BUILD94.
