# FINDING R4-04 — Part I says its rules are "indexed and closed at E = 0". The protocol index has E = 105, and there is no principles index. NOT REPAIRED.

Found 6 September 2026, from the Chapter 2 subject-matter read (`RULINGS-R4c.md`). Measured by
`method/proofs/part1index.py`, whose selftest asserts the book's own printed numbers.

## The record had this site open, and nobody had measured it

The R2 read reached it and stopped where the evidence stopped. Its entry, verbatim:

> **1-27 · L558–559.** PRINTED: *"Part I indexes the principles and the protocols. §28.8 indexes the
> process. Each … closes with E = 0."* SOURCE: … no E = 0 statement for the Part I index found in
> L568–1510. MEASURED (grep). **READING: unverified — INFERRED open.**

**That is what this finding closes.** The site was open because the read was a read: it established
that the book never states the E it claims, which is not the same as establishing what the E is. The
measurement below supplies it.

## What is claimed, in two places

**Part I's header (main L236):** *"…and twenty-four protocols the law is made of, **indexed and
closed at E = 0**."*

**The close of Chapter 1 (main L559):** *"Part I indexes the principles and the protocols. §28.8
indexes the process. Each turns a rule set into content, and **each closes with E = 0**."*

Three objects are named. One of them closes.

## What is measured

| the object | cells | box | \|ℛ(X)\| | **E** | closes at 0? |
|---|---|---|---|---|---|
| the protocol index, 24 protocols | 19 | 192 | 124 | **105** | **no** |
| §28.8's process index, 36 cells | 36 | — | — | **0** | yes, as printed |
| a principles index | — | — | — | — | **there is none** |

**The protocol figure is not mine.** `protindex.py` — the instrument that assigns each protocol its
cell — is in the recovered estate at `extracted/archives/restore-point-2-13/`. It is imported by path
and not reimplemented, because which cell a protocol occupies is the book's judgement and not a
program's. It returns 24 protocols in 19 cells, E = 105.

**And the book already prints that number.** The Index of Indices' table of the book's own indexes
carries the row *"the protocols · trigger · object · failure · earned · **19** · **105** ·
twenty-four protocols"*, and the Mathematical Compendium's entry *The protocol index* carries
*"the 24 protocols occupy 19 cells in four coordinates"*. So the volumes state E = 105 and E = 0
about the same object.

**The instrument said so before it ran.** `protindex.py`'s header records its commitment under
§2.13 — *commit before you look* — and the first line of it is:

> *(a) the protocol index is OPEN — a book that adds protocols when it fails will not have covered
> the space evenly*

That prediction was written down before the computation and the computation confirmed it.

**There is no principles index at all.** Searched both bundles: no E is computed over the
principles anywhere. Chapter 1 sorts the twenty-three into MECHANISM, OPERATION and RELATION, and
that sort is not an index in this book's sense — it has one coordinate and no closure operator is
applied to it. So for the principles the claim has no object rather than a wrong one.

## Why this is subject matter and not a phrase

The test is M's: *a false claim is an object that is false when the prose is stripped away.* Strip
the prose here and the object is **E = 0 over the protocol index**, which is a computed quantity of
the kind §2.18 calls computable — recoverable by ℛ from what the book prints. It is computed, it is
printed, and it is 105.

This is the difference from R4-02, where *not a lattice* was a loose word over a sound argument.
Here nothing is loose. Two sections of one book compute the same quantity and disagree by 105.

**And the argument Chapter 1 is making does not need E = 0.** The passage is arguing P22 — that a
complete index converts deception into disagreement, because every rule is content rather than
inference. What that needs is for the rules to be **stated**. Completeness of the index over them is
a separate property and the argument never uses it. So the false clause is carrying no weight.

## What the claim costs, which is the reason to repair it rather than delete it

**E = 105 is a result, not a defect.** One hundred and five cells the structure admits and the book
does not occupy is a measurement of how much of the protocol space is unexplored — which is exactly
what §18.4.1 and register 275 say an E is for, and exactly what §2.18.1 did with the ten decisions
when E located a decision nobody had made. Asserting E = 0 does not overstate a good result. **It
replaces a real finding with a false one**, and the real one is more interesting.

## What is owed, and it is M's

Two decisions, and they are separate.

1. **The protocols.** The measured statement is *twenty-four protocols in nineteen cells, E = 105,
   an open index by its own committed prediction.* Does that replace *"indexed and closed at E = 0"*
   in the Part I header and in Chapter 1's close, or is the clause simply struck?
2. **The principles.** There is no index over them. Either one is built — the coordinates would have
   to be M's, since assigning them is a decision in §2.18's sense and not a computation — or Chapter
   1's sentence names only the two objects that exist, §28.8's process index and the protocols.

**Nothing is repaired here.** Under `RULINGS-R4c.md` the prose is not touched until the subject
matter is settled, and the settlement is a ruling rather than a measurement.

`method/proofs/part1index.py` holds the test; `part1index.out` its banked output.
`python3 method/proofs/part1index.py --selftest` asserts twelve of the corpus's own recorded numbers.
