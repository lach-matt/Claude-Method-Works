# READ-reg8.md — the Register, unit 8: the withdrawn entries (out of source order, at M's direction)

M directed an exhaustive search for entry 1725 after reg1-05 recorded that the front matter cites
four entries which have no heading in the seated Register. Instrument `r2-reg8a.py`, golden
`r2-reg8a.out`. All instrument checks OK. **Three findings, and they reframe three earlier ones.**

The search was not made in Graphify. Graphify holds code symbols (DEF-145 item 8, re-confirmed at
W-187) and `graphify-out/` predates the CORPUS files, so a miss there is not evidence of absence.
The witness that answers the question is the one Ruling 56 already names: **the archive**. The
mirrored `BUILD9` and `BUILD10` main bundles are earlier states of this same volume.

## The answer is not "never written"

**All four were written, seated, and later removed with their content.**

| entry | what it recorded | archive | live |
|---|---|---|---|
| **1725** | the settled form — the ruling-C normalisation | present | **gone** |
| **1732** | the citation counts recomputed, the load-bearing table regenerated | present | **gone** |
| **1744** | the asterisk residues — *"the Register's tangles were split delimiters"* | present | **gone** |
| **1756** | the carried residue computed out | present | **gone** |
| 1710, 1743 | hygiene faults; the press pass 1744 rests on | present | **gone** |

**It is a removal, not a renumbering.** Entry 1725's headline — *"THE RECORD NORMALISED TO ITS OWN
SETTLED FORM — 1,517 ENTRIES, ONE HEADLINE AND ONE BODY EACH"* — appears in **none of the six live
volumes, under any number**. Measured, not inferred.

## A — findings

**reg8-01 — 110 entries present in the archive are absent from the live Register.** Entry **1782**
discloses the practice in aggregate — *"132 are absent — the thirteen never assigned, together with
those withdrawn with their content"* — and **names none of them**. The front matter's own discipline
reads *"A correction never replaces what it corrects. Both states are kept … a register that tidied
itself would be evidence of nothing"*, and the standing rule makes entries append-only and never
removed. For these 110 the prior state survives only in the archive, which is not a reader-facing
volume.

**reg8-02 — the front matter cites four entries the register withdrew, and all four are the record
of the volume's own machinery.** 1725, 1732, 1744, 1756. Measured: **no other part of the live
register cites a withdrawn entry** — the front matter is the only place in the volume that does.
(571 also appears there, but as the load-bearing *count*, not a pointer, and is excluded.)

**reg8-03 — the register diagnosed the split-delimiter class itself, and the diagnosis was withdrawn
while the defect was not repaired.** Archive entry 1744: *"THE ASTERISK RESIDUES WERE NOT THE
FLANKING RULE … **THE REGISTER'S TANGLES WERE SPLIT DELIMITERS** … Register 1743 counted 738 stray
asterisks in the main volume's render and 106 in the Register's."* Both 1743 and 1744 are withdrawn.
**275 entries still carry the class**, which reg7-01 rediscovered independently at 429 sites without
knowing the record had found it first.

## B — why the withdrawal itself is not scored

**Ruling 45 forbids build and editorial-process remarks in any reader-facing volume**, and every
entry examined here is exactly that: 1743 names `build.py` and the press pipeline, 1732 the citation
parser, 1725 the generator's retirement. Removing them from a reader-facing volume is **consistent
with a ruling in force**, so the removal is not a finding and is not scored.

What is a finding is that the cleanup **left both loose ends**: the citations to the withdrawn
entries were not removed with them, and the front matter that cites them still carries the four
script names and two build handles Ruling 46 forbids (reg1-06). The pass took the entries and left
the things they were removed for.

## C — what this changes in the earlier units

- **reg1-05** is superseded in its explanation. The four pointers do not dangle because the entries
  were never written; they dangle because the entries were withdrawn. The defect stands, its cause
  is now measured, and the repair is different: R3 either restores the citations' targets or removes
  the citations, and cannot do the first without re-admitting Ruling-45 material.
- **reg7-01 / reg7-02** are no longer first findings. The record found the class, counted it at 106
  stray asterisks in the Register's render, and lost the entry that said so. `R3-CLASS-EM.md` should
  cite archive 1743/1744 as the prior diagnosis.
- **reg1-01 / reg1-02** gain their cause. Entry 1732 is the recomputation of exactly the citation
  counts and load-bearing table that are now stale — 571 against 593, 387/701/970 against
  392/862/1056. The entry that recomputed them was withdrawn, and the figures were not maintained
  after it.

## Census

No census row engages this unit's sites. `CENSUS-CLOSURES-reg8.tsv` is header-only.
