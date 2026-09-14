# `render/` — the master-lattice artifact, and the programs that produce it

`master-lattice.html` is the rotatable drawing of the master index. It is published as an
Artifact; this directory is the source of record for it.

    python3 gendata2.py > DATA2.json    # refusal index, warp readings, obstruction, Petrov fix
    python3 gendata.py  > DATA.json     # the lattice itself; reads DATA2.json
    python3 splice.py                   # rewrite the page's `const DATA = { … }` block

**Every number in `DATA.json` and `DATA2.json` is measured on the spot from the instruments.**
Nothing is carried forward from a previous render, and nothing is transcribed. The page's prose is
the only hand-written part, and it is the only part that can go stale.

## Why `gendata2.py` exists at all

`DATA2.json` was written once by hand and **no program survived to reproduce it.** When the tenth
index was seated, every figure in it had to be re-derived from definitions that had to be guessed —
and one of them, a census of K7 cells over the bounds box, could not be reconstructed exactly. It is
now recomputed under a definition the file states outright, and reads 67 where the unreproducible
original read 48.

So: **a render is a deliverable, and a deliverable with no generator is a transcription.** Both
generators are seated here for that reason.

## What the page must not be allowed to claim

The instruments are the authority. Where the page states a figure the generators do not supply, it
is hand-written prose and carries the same risk any prose does — the tenth seating found several
sentences describing an earlier state of the lattice, including one (`0 of 36 comparable`) that had
been stale since Janet was recoded, two dockets earlier. Legend counts and the population panel are
now **derived from `DATA` at run time** rather than typed, because those were the figures that went
wrong first.
