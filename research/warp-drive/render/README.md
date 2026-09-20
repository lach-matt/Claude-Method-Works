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

## The index plates

One plate per seated index, all on the shared scaffold in `plate.py`, so the stylesheet, the
measured axis choice, the swept camera and the inlined runtime are one implementation rather than
one per plate.

    python3 build_index_plates.py              the periodic-element indexes
    python3 build_particle_plates.py           DOCKET 27's three particle indexes,
                                               and DOCKET 30/31/32/34/35's
    python3 build_particle_plates.py nucbands  the one plate with NO 3-D view:
                                               its index is arity 2, and every
                                               third axis is a DIFFERENT chart at K0
    python3 build_particle_plates.py mesons    just one

**Every figure on a plate is read from its instrument at build time.** Nothing is retyped, and each
plate's footer prints the commands that re-verify it.

`build_particle_plates.py` writes `fundamental-plate.html`, `mesons-plate.html` and
`baryons-plate.html`. None of the three indexes has arity 3, so **every view on them is a
projection** and `plate.exactness()` states in the caption how many cells it keeps and how many it
collapses — 25 of 26 for the fundamental particles, 39 of 66 for the mesons, and 54 of 184 for the
baryons, whose seven coordinates make it the heaviest projection here bar `gravity`'s.

The hue is chosen by measurement, not taste: `plate.axis_choice()` refuses a projection where two
cells would land in one place carrying different colours. **A parity-coloured baryon view is impure
at every projection** — 86 points would carry two colours — which is the same fact section 05 of
that plate states as a finding, showing up in the rendering.

Each particle plate also carries a provenance block read from `registry.sources()`: the declared
`SOURCE` beside the code that reads the data, the file it names, its size and its md5. A provenance
held only in prose has to be recovered later.

## The two legacy builders, and the inputs that were missing

`build_plates.py` and `build_plates8.py` predate `plate.py` and are **not** on the shared scaffold:
each inlines its own frozen copy of the pre-`scatter3d.js` widget. Both **raised
`FileNotFoundError` at import** — they read `style.css`, `w3d.js` and a points file at module level
and none of the four had ever been committed. Nothing in the tree said so.

    python3 build_plates.py              ion.html, axs.html, rid.html
    python3 build_plates8.py             spx.html, ent.html, oct.html
    python3 build_plates.py  --selftest  14 fixtures
    python3 build_plates8.py --selftest  17 fixtures

**The inputs were RECOVERABLE, and are restored by extraction from the plates themselves** — a
plate inlines its stylesheet, its widget and its points, so it is a complete record of what built
it. Git history has never held any of the four (`--diff-filter=D` and `--diff-filter=A` both
empty); the two other `style.css` the search turns up were each checked and neither is this one —
`recovered/style.css`, on disk, is 700 bytes of unrelated DejaVu print CSS, and `public/style.css`,
in history only, is the website's own sheet, whose 16 committed versions were hashed and none
matches.

| file | bytes | md5 | recovered from |
|---|---|---|---|
| `style.css` | 7,280 | `bfec0696c0e551145759a290ad5d500a` | identical in all seven plates here |
| `w3d-r1.js` | 5,753 | `f9348be9b963d26e2c63240fc974e060` | `ions`, `axes`, `rindex` plates |
| `w3d-r2.js` | 6,542 | `4154dde8161ec3e0dc154fadab88e7dd` | `spectra`, `entropy`, `octad`, `hexad` |
| `new_pts.json` | 4,715 | `7b827facb5d6d2dc9a0c63293034c159` | the three `scatter3d(...)` calls |
| `oct_pts.json` | 8,544 | `604eb92e920b965623cc531e11fdbb08` | the three calls, plus the octad's 28 edges |

**`w3d.js` is re-pinned to two files because one name held two contents.** `plate.py` records the
count from the other side — "three generations have since diverged" — and these are those three:
r1, r2 (r1 plus the `opts.edges` pass and the hollow-point branch, which is why only the octad can
draw its threads) and `scatter3d.js` at 7,975 bytes. The ambiguous name is retired rather than
given one of its two meanings, and `scatter3d.js` is **not** a substitute: a plate built against it
is a different plate.

**All six rebuilt pages are byte-identical to the plates in the tree** — `ion.html` ==
`ions-plate.html` and so on, the `-plate` names being a rename that happened outside these
programs. Each selftest rebuilds its three in memory and compares md5s, so the pairing cannot
quietly stop holding. Inputs now resolve against the file's own directory; outputs still land in
the working directory, unchanged.
