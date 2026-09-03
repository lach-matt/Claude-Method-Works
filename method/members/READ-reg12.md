# READ-reg12.md — the Register, the remainder: entries 395–1792 (L1467–L6611)

Instrument `r2-reg12.py`, golden `r2-reg12.out` (4,606 B · `9d844002`). All instrument checks OK.

## The cadence changes here, and why

Units 1–11 ran at the chat-81 mean of ~120 lines because the early record needed its conventions
established one at a time. Three things license larger blocks, stated before the blocks are cut:

1. `r2-regsweep` has already resolved **every** pointer in the volume, so a unit no longer rebuilds
   six resolvers to find nothing.
2. The mature record is a flat run of one-line entries, not the main volume's nested prose — there is
   no subsection structure for a unit boundary to respect.
3. Units 5, 6, 9, 10 and 11 returned **no deviation at all**, and the defect classes that remain are
   volume-wide and already measured volume-wide.

**The read is not thinned.** Every entry is resolved, every anchor figure extracted, every census row
in range engaged. What changes is that one instrument carries it with one golden instead of thirty-two.

## A — findings

**reg12-01 — reg8-02 is FALSE, and this read's own net is why.** reg8-02 concluded that *"no other
part of the live register cites a withdrawn entry"* — the front matter alone. Measured on the right
nets, the **body cites withdrawn entries at four sites**:

| form | sites | on the `register N` net |
|---|---:|---:|
| `entry 1000` | 1 | **0** |
| `R 1002` | 3 | **0** |

Both entries are in the BUILD10 archive and absent from the live register (reg8-01). reg8-02 used
`registers?\s+N`, which returns nothing for either form. **Census rows 8, 15, 16 and 17 carried them
the whole time.**

This is the third time the read has met the lesson reg1-05 first stated — *what a sweep sees is
decided by the net it uses* — and **the first time it has caught the read itself.** The correction
belongs to reg8-02 and is recorded against it.

**reg12-02 — the unprinted-theorem class is three theorems, not one.** 26b-09 (W-190) records
**Thm 11.1**, cited by the register and printed in no volume. Measured over all six volumes on
`(Theorem|Thm)`:

- **Thm 11.2** — 2 sites, printed **nowhere**
- **Thm 12.1** — 2 sites, printed **nowhere**
- Thm 11.1 — 1 site, printed nowhere (26b-09)
- Thm 10.1 — **is** in the Mathematical Compendium at 2 sites, so **not** in this class

Four further sites in the class 26b-09 opened. Docket 2 / 9(c).

**reg12-03 — the object-handle leak is ten sites, not the one recorded.** 26b-10 records the
`BUILD-10` handle and four internal file names at reg L6507. The census carries **ten more** in the
same reader-facing volume — `3B.tri`, `3B.five`, `3B.pot` ×2, `3B.shape` ×5, `3B.metric` — at
L6403–L6467. Ruling 46 forbids object handles and internal references to readers. Docket 6 / 28.

## B — verified across the remainder

- **Every section pointer resolves**, in every block, with nothing unaccounted for.
- **Every `register N` pointer resolves** — the sweep's absent-and-cited pair (344, 571) is cited
  from the *main* volume, not from the register, so the remainder correctly shows none.
- **Seven seated tower figures are restated by 48 entries** across the remainder — Λ₈ 976 by 31
  entries, the ambient box 6,912 by 6, Λ₉ 1,654 by 5, and Λ₁₀–Λ₁₃ by one or two each. Each is a
  figure this read has already reproduced; an entry restating one is corroboration, not a new claim.
- **The emphasis class does not stop at entry 394**: 247 of the 1,287 entries in the remainder carry
  it, at 372 sites — already scored volume-wide at reg7-01 and specified in `R3-CLASS-EM.md`.

## Census

**249 rows engaged. 26 closed, 223 left open, and the 223 are open on principle.**

The 26 non-C9 rows are closed individually in `CENSUS-CLOSURES-reg12.tsv`, each on a measurement:
6 theorem pointers, 5 section pointers, 4 register pointers, 11 handle leaks.

The **223 C9-OVERGENERALISATION-WORD rows are engaged and NOT closed.** Twenty C9 rows have been
closed across this read and every one was *not a defect*, so the class is very likely uniform — but
**a row is not closed on a reading that did not take it**, and this block read the entries for
pointers and figures, not word by word for each flagged token. W-192 left an engaged block open on
exactly this principle and it is followed here. They are recorded as engaged-and-open, for a reading
that takes them.
