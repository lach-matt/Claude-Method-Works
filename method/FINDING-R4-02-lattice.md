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
