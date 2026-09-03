# READ-reg9.md — the Register, unit 9: entries 290–326 (L1091–L1210)

Source order resumed after units 7 and 8, which M directed out of order. 120 lines, thirty-seven
headings, cut on an entry boundary at 326. Instrument `r2-reg9a.py`, golden `r2-reg9a.out` (2,922 B ·
`76c658a1`). All instrument checks OK. **No deviation.**

## The fault, and it is the third of its kind in this read

Entry 301 prints *"THE CAPS PRINTED IN §8.3 DO NOT REPRODUCE Λ, and the construction is short an
eighth condition — (3,3,2,3) gives 1,548, and only (3,3,1,3) with k ≥ 1 gives 976."*

Rebuilding L8 from `tower-2.py`'s own loops, **(3,3,1,3) reproduced 976 exactly** — and **(3,3,2,3)
returned 1,284**. That stood as a deviation for exactly as long as it took to search the cap space
for 1,548.

**It is there, and the book is right.** Entry 301's tuple is (n, e, ℓ, k) and does **not** carry f.
In `tower-2.py` the ℓ and f caps are *parallel* — `min(1, n-1)` for ℓ and `min(1, e-1)` for f, both
hard-set to 1. Raising ℓ to 2 raises f to 2 with it. Holding f at 1 while lifting ℓ is an asymmetric
change the book never made. **Under the symmetric lift, (3,3,2,3) gives 1,548 to the unit.** Book
right, instrument wrong — recorded here rather than in a finding.

## B — verified

- **Both halves of entry 301 reproduce.** (3,3,1,3) with k ≥ 1 gives **976**; the same caps with
  k ≥ 0 give **1,001**, so *only* k ≥ 1 gives 976 — which is the eighth condition the entry says the
  §8.3 construction is short of. And (3,3,2,3) under the symmetric lift gives **1,548**.
- **Ten section pointers, ten resolutions**, each to its claim: §2.19.1 *The register, examined
  before repairing it*, §3.8, §4 *The failures of the assistant…*, §6.2, §8.3 *Seventeen
  generators*, §12.5, §12.6 *The cylinder is a fibration…*, §18.4.1 *The law of realised closure*,
  §23.1 *The ratio*, §28.7.4 *Forty more…*.
- **976 / 6,912 = 14.12 %**, the fill figure entry 315 states and the third entry to state it (with
  248, 255 and genesis 8) — reproducing to the digit.
- Both register pointers in the unit, 275 and 293, resolve.

## Census

Two rows engaged, both closed **not a defect** in `CENSUS-CLOSURES-reg9.tsv`. **1239**'s *never* is
"the five sections were never rendered" — a bounded fact about five named sections and the reason
register 293's defect escaped nineteen audits. **1240**'s *never* states the author's bracket rule
itself, which the entry then measures against the tower. Both are the C9 regex artefact.

## C — incidental

- Entry 315's *"fill falling monotonically 14.12 % to …"* needs the **ambient** box at each stage;
  `tower-2` prints the lattice sizes and no ambient. Budget with its witness, as at reg6 and unit 5.
  Docket 10.
- The gaps in 290–326 are all carried by grouped headings or absent-and-uncited, on the convention
  fixed at unit 5.
