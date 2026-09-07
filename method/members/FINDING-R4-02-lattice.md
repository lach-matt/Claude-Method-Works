# FINDING R4-02 — "not a lattice" is used for what Appendix A correctly calls "meet-broken". The triangle region IS a lattice. Scope stated carefully. NOT REPAIRED.

Opened 6 September 2026 on M's question *"what is the lattice-hood question?"*, and bounded by his caution that the
three-body paper here is **for unknown masses** and that Chapter 14 may be about a different three-body problem.

## The three sites, and they do not say the same thing

**Appendix A.18, heading (main L10107): "The triangle region is join-closed and meet-broken."** Appendix A.15's
heading likewise: "Two bands, and only one of them is a **sublattice**." This is exact. *Meet-broken* and *not a
sublattice* are statements about closure under the componentwise operations, and that is what the book measures.

**Main §12.11.2 (L3380):** *"The exact coupling region is **not a lattice in any presentation tried**: as 2S′
(50,592 failures), as parity alone (52,080), as the min-cap (17,856), as pair count (7,254), as (2S,2L,2J) (2,443
meets)."* Hedged by *in any presentation tried*, but the word is *lattice*.

**The three-body paper, Law 3's table row (L157):** *"K₃ needs strong 3-consistency; ℛ gives 2; **the exact region is
not a lattice**"*, citing §12.11.2 and §21.5.1. **Unhedged.** The paper imports §12.11.2's clause by citation.

**Chapter 14 carries no lattice claim at all.** The item that opened this (DEF-153P, PO-0158) names "main §14"; §14 is
Closure, and its only three-body mention is a count of register objects. The claim is §12.11.2's. Recorded so the
next reader does not go to §14.

## Why the two phrases are different propositions

A set can be a lattice without being a sublattice. *Meet-broken* says the componentwise minimum of two members falls
outside the set. *Not a lattice* says the induced order has a pair with no greatest lower bound **inside** the set —
a strictly stronger claim, and it does not follow from the first. The book's own counts are counts of the first.

## Measured

The regions Appendix A defines, built exactly as the seated instrument `r2-ch19a3.py` builds them —
`C = {(a,b,c) ∈ [0,cap]³ : |a−b| ≤ c}` and the two-sided `T = {(a,b,j) : |a−b| ≤ j ≤ a+b}` — tested for a greatest
lower bound **within the region** at every pair whose componentwise minimum falls outside it:

| region | cap | members | componentwise meet fails | join fails | pairs with **no** glb in the region | a lattice? |
|---|---|---|---|---|---|---|
| T two-sided | 4 | 65 | 411 | 0 | **0** | **yes** |
| T two-sided | 6 | 175 | 2,862 | 0 | **0** | **yes** |
| T two-sided | 8 | 369 | 12,489 | 0 | **0** | **yes** |
| C one-sided | 4 | 85 | 390 | 0 | **0** | **yes** |
| C one-sided | 6 | 231 | 2,842 | 0 | **0** | **yes** |
| C one-sided | 8 | 489 | **12,654** | 0 | **0** | **yes** |

**The construction is corroborated by the book's own figure:** §A.15's printed meet-failure counts are *"12,654 at
cap 8, 113,568 at cap 12, 565,284 at cap 16"*, and C at cap 8 reproduces **12,654** exactly. So this is the book's
object, built as the book builds it.

**Result.** Every one of those thousands of broken meets has a greatest lower bound inside the region; it is simply
not the componentwise minimum. **The triangle region is a lattice, and Appendix A's "join-closed and meet-broken" is
the correct description of it.** "Not a lattice" is the wrong phrase for this object.

## The scope, stated so it is not overclaimed

**What is settled:** Appendix A's triangle regions are lattices. Appendix A does not call them anything else, so
Appendix A is right and nothing there needs repair.

**What is NOT settled:** §12.11.2's *"exact coupling region"* is a different object — the physical coupling region in
five presentations, whose failure counts (50,592 · 52,080 · 17,856 · 7,254 · 2,443) are an order of magnitude larger
than the abstract region's and cannot be the same set. **I have not built it and have not tested it.** Its cells would
have to come from the term structure of ℓᵏ, and I have not established that the repository holds them in a form the
test can use. Until it is built, whether §12.11.2's claim is false or merely overstated is open, and finding R4-01's
lesson says not to guess.

**What M's caution changes.** The three-body paper is *The Three Body Problem for Unknown Masses*; its Law 3 uses
three bodies forming K₃ as a **constraint-graph** structure, and imports the lattice clause from §12.11.2 rather than
establishing it about its own subject. So the paper's exposure is inherited: if §12.11.2's phrase is an overstatement,
the paper repeats it unhedged, having dropped *"in any presentation tried"*.

## What is owed

Build §12.11.2's exact coupling region from the term structure, reproduce at least one of its five printed failure
counts as proof the right object has been built, then run the same glb test on it. If its cells cannot be recovered
from the repository, that is the question to put to M.

`method/proofs/lattice.py` and `lattice.out` hold the test and its output.

---

## Provenance, searched rather than reconstructed (6 September, on M's instruction)

**The passage is not new to this book.** It appears verbatim in `drive/The Method Materials/The_Method.pdf`, page 34,
headed *"The Method — The Lach Cylinder"* — the same sentence, the same five presentations, the same five counts. Only
the pointers differ: that book says §3, §9.4, §2.4 and Chapter 12 where this one says §8.4, §14.4, §7.4 and Chapter 17.
**M's caution is confirmed in the object: the tools and the older texts carry section numbers this book has outgrown,
so a pointer is never evidence of what a claim is about.** `The Method 1.2-1.pdf` carries it too.

**The three-body paper does not contain this material at all.** Searched for *coupling region*, *meet-broken*, all five
counts, *seniority*, *2S,2L,2J*, *not a lattice* and *strong 3-consistency*: `The_Three_Body_Problem_for_Unknown_Masses_Lach.pdf`
matches **none of them**. Law 3's clause is imported from §12.11.2 by citation. **M's caution holds exactly: the paper
is about unknown masses, and the lattice clause is not its own result.**

**A false lead, recorded so it is not chased again.** `On_the_Matter_of_Time_Travel.pdf` contains the string *52,080*,
which is one of §12.11.2's five counts. It is a different quantity: there it is a section size in the Λ₁₃ factorisation
(*"sections 11,470 · 45,880 · 89,700 · 52,080 reproducing §12.11.5's printed table to the cell"*). Coincidence of value.

**The computation behind the five counts is not in the repository.** Searched `drive/`, `extracted/` and `method/` for
each count with and without its comma: **the numbers occur only in book texts** — this volume, `The_Method.pdf`,
`The Method 1.2-1.pdf`, `BUILD12`, and PDF extractions of the same. No instrument prints them, and the restore point's
348 files contain none of them.

**The machinery to compute them IS in the repository.** `extracted/archives/restore-point-2-13/method_tower.py`
carries `terms(l, k)` — the full LS decomposition of a shell — with `exact_2J`, `max2J` and `phihat`, and
`schemes.py` uses them for the four coupling schemes. So the exact coupling region can be built from the book's own
functions rather than invented. What is not recoverable is **which** construction produced 50,592 · 52,080 · 17,856 ·
7,254 · 2,443, and the five presentations are named in the prose but not defined there.

**Where that leaves the question.** Appendix A's regions are lattices, measured, and Appendix A's wording is right.
§12.11.2's exact coupling region is a different and larger object whose five counts have no surviving instrument. It
can be re-derived from `method_tower.terms`, and the test of whether the construction is the right one is whether it
reproduces one of the five counts. That re-derivation is the next step and it needs M's word, since it is a
reconstruction and the standing rule is that the repository is searched first — which has now been done.

---

## RESOLVED by reading the chapter, 6 September. It is a prose error, not a false claim.

M: *"the context of their presentation tells you if they are questionable results."* Done, and the context reverses
the reading. §12.11.2 does not stand alone: it is the evidence for §12.11.3, **The dichotomy**, which is the chapter's
result.

**What the chapter is arguing.** *"Counting coordinates close exactly. Coupling coordinates close as envelopes. There
is no third kind in this object."* And the reason: *"Vector coupling gives envelopes, provably and permanently,
**because its exact form is made of the three excluded shapes**"* — the reflection, the congruence, the triangle of
§12.11.2. The law that follows: *"every coupling coordinate's exact physical bound requires either two parents or a
congruence, and the tree carries only one."*

**So the property the argument needs is sublattice-hood, and that is exactly what the counts measure.** The
construction can carry a constraint only if it is a monotone single-parent bound — that is, only if the region is cut
out as a **sublattice of a product of chains** (the cylinder paper's §3.1: *"Λ is a sublattice of a product of chains,
and every such sublattice is distributive"*, which is what admits Birkhoff). A region that is not closed under the
componentwise meet cannot be carried exactly, whatever else is true of it. **Being a lattice under its own induced
order would not help the construction at all**, because the construction cannot reach an operation that is not the
componentwise one.

**Therefore the mathematics is sound and the word is loose.** The five presentations are five attempts to present the
exact coupling region so the machinery could carry it; each failed on the meet; the conclusion drawn — that coupling
coordinates close only as envelopes — follows from precisely that. Strip the prose and the object is *"the exact
coupling region is not closed under componentwise meet in any of five presentations"*, which is true and is what the
argument uses. **Under M's test this is a prose error: true before the prose, wrong when the prose is applied.**

**The repair is one word, and it is M's, at the prose pass:** *not a lattice* → *not a sublattice*, in §12.11.2 and in
the three-body paper's Law 3 row, matching Appendix A.15 and A.18, which already say it correctly. No number moves.

**What R4-02's measurement is worth after all.** It establishes that the two words differ **in fact** for this object
and not merely in principle: the triangle region really is a lattice under its induced order, so *not a lattice* is
not a harmless shorthand for *meet-broken* — it is false of the object while the argument's real premise is true.
That is why the word is worth changing rather than leaving.

**What remains unproven, and it is separate.** The five counts — 50,592 · 52,080 · 17,856 · 7,254 · 2,443 — have no
surviving instrument anywhere in the repository, and the five presentations are named in the prose but nowhere
defined. The claim they support is sound; the numbers themselves are not yet reproduced. Under *"true and proven so"*
they are owed a re-derivation from `method_tower.terms`, and that is Phase 1 work on this chapter, not a defect.

**Second time in two findings that context has overturned a reconstruction.** R4-01 was a misread clause; this was a
number judged out of its argument. The rule earned: read the chapter before scoring the figure.
