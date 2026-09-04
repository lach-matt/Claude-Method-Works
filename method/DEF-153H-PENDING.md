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

## H-2  The theorem/law split is a RE-CLOSURE — and it is no longer blocked

UPDATED after M landed `extracted/` (782 files) on main. The earlier reading of this item said the
element set was not reconstructible from the volume. **That was wrong, and the error was mine: it
was a format assumption, not a missing set.**

Appendix D's element tables do not share a column order. §D.5.2 writes

    fibre                              element                       status · verification · precedent

and §D.5.6 through §D.5.10 write

    new element                        fibre                         coordinates

An element-first reader silently matches the second family and misses the first — which is how 27
rows disappeared and the count came out at 45 against a closure stated over 77. A reader that takes
each table's own header and slices by its own column offsets recovers **72 of 77** immediately, and
`law · physics` = 4, matching §D.5.10's caption exactly.

This is the same defect class as `qgraph.py` (DEF-153F item 2) and as the wrong-table-header bug
`r3-vocab` hit at §D.2: **Appendix D's tables are not one format, and any instrument that assumes
they are will under-report rather than fail.** The reader must be written against each header.

STILL OUTSTANDING before E can be computed at 78:

  - §D.5.3's five elements ("What makes something an element, and the five that test it") are not
    in either table family and have not been located.
  - four rows whose element text overruns its column, shifting the slice by one character:
    `V = 4ν/3, §23`, `the bracket width, §23`, `the Rydberg term T(ν) = Z²R/ν², §22`, and
    `the limit — Λ_spectra closes at the last species`. Column slicing must be bounded by the
    NEXT column's start, not by a fixed width.
  - the reconciliation of the extracted fibre counts against §D.5's printed census: extraction
    gives theorem · order 16 where the census prints 21, and §D.5.4 records a correction
    "theorem · order 5 -> 10" applied after that census was written. Which of the two is current
    has to be established before either is used as a fixture.

The discipline is unchanged: reproduce the recorded E = 0 at seventy-seven with
`tools/cypher.py --cells` BEFORE computing anything at seventy-eight. The blocker is now three
tractable extraction問 rather than an absent set.

## Status

Both recorded, neither repaired, per the chat-67 hold. H-1 is a regression from a build run in this
session and is the more urgent of the two: the book currently contains a contradiction it did not
contain at BUILD94.
