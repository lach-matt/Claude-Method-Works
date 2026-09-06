# FINDING R4-25 — §12.11.2's lattice paragraph, re-derived: **six of six printed claims reproduce exactly**, including the sentence about what the meet manufactures. The **five presentation counts still do not**, and one arithmetic lead is recorded rather than chased. A6 stays blocked, and the boundary is now sharp. NOT REPAIRED.

Measured 6 September 2026 under M's *"complete R3 please"*, as the blocking step `FINDING-R4-02` named:
*"Build §12.11.2's exact coupling region … reproduce at least one of its five printed failure counts as
proof the right object has been built."* `method/proofs/coupling.py`, banked `coupling.out`.
**Selftest 13 of 13.**

## 1. What reproduces, and it is the whole second half of the paragraph

§12.11.2 prints, of the region {|2L−2S| ≤ 2J ≤ 2L+2S}:

> *"JOIN-closed — zero failures at caps 6, 8, 10 and 12 — and meet-broken at every one, by **2,862,
> 12,489, 40,887 and 110,229** failing meets … impose the parity congruence as well and the join closure
> dies too — **1,848 failures at cap 6**"*

| cap | cells | meet failures | printed | join failures |
|---|---|---|---|---|
| 6 | 175 | **2,862** | 2,862 | **0** |
| 8 | 369 | **12,489** | 12,489 | **0** |
| 10 | 671 | **40,887** | 40,887 | **0** |
| 12 | 1,105 | **110,229** | 110,229 | **0** |
| 6, with the parity congruence | 106 | 2,292 | — | **1,848**, printed 1,848 |

**And the sixth claim is the sentence, not a number.** §12.11.2 says *"the triangle's first meet failure
manufactures J = ½ from S = L = 0."* The instrument returns it: **(0,1,1) ∧ (1,0,1) = (0,0,1)** — 2S = 2L = 0
and 2J = 1, which is J = ½ with S = L = 0. **Six of six.**

**The convention was fixed by the reproduction, not assumed.** Pairs are **unordered and distinct**;
counting ordered pairs doubles every figure and matches none of them. That is recorded because the same
choice decides every other meet-closure count in the corpus.

This upgrades `FINDING-R4-02`, which reproduced two of the four cap figures against a differently built
region; all four now reproduce from the region's own definition, together with the join closure and the
parity variant.

## 2. What does not reproduce, and it is the half the repair needed

> *"The exact coupling region is not a lattice in any presentation tried: as 2S′ (**50,592** failures), as
> parity alone (**52,080**), as the min-cap (**17,856**), as pair count (**7,254**), as (2S,2L,2J)
> (**2,443** meets)"*

**None of the five is reproduced here.** `FINDING-R4-02` had already established that no instrument
anywhere in the repository prints any of them and that the five presentations are named in the prose and
defined nowhere. This pass searched further and did not close it: the tower's own stages are meet- and
join-closed at every level (E = 0, measured on `tower-2.py` — Λ₈ 976 cells, Λ₉ 1,654, Λ₁₀ 2,535, **zero
meet failures and zero join failures at each**), so the exact coupling region is not a tower stage; and
the exact term structure of ℓᵏ from `method_tower.terms`, presented as (2S,2L,2J) over every cap tried,
gives 23, 126, 365, 589, 374, 1,634, 5,450 and 7,314 failing meets — **7,314 lands 60 short of 7,254 and
that is the closest any construction came.**

**One arithmetic lead, recorded and not chased.** **31 divides four of the five**: 50,592 = 31 × 1,632 ·
52,080 = 31 × 1,680 · 17,856 = 31 × 576 · 7,254 = 31 × 234. The fifth, 2,443 = 7 × 349, does not. Four
independent numbers sharing a factor of 31 is not what coincidence usually looks like, and it is the
sharpest thing anyone has to go on. **It is a lead. It is not a finding, and nothing is built on it.**

## 3. What this settles about A6, and it is a boundary rather than a repair

`docs/R3-REPAIR-PLAN.md`'s **A6** proposes narrowing *"is not a lattice"* to *"is not a sublattice of the
product"* at main L3380 and at the three-body paper's Law 3 table. **It still cannot be done**, and the
reason is now exact rather than general:

- **Appendix A is right and needs nothing.** Its triangle regions **are** lattices — every one of
  thousands of broken componentwise meets has a greatest lower bound inside the region — and
  *"join-closed and meet-broken"* is the correct description (`FINDING-R4-02`).
- **§12.11.2's second paragraph is right and now fully verified.** Six of six.
- **§12.11.2's first paragraph — the five presentations — is the sentence A6 would edit, and it is the
  one thing still unreproduced.** Narrowing *"not a lattice"* to *"not a sublattice"* there would assert
  a property of an object nobody in this repository has built.

**So A6 is not blocked on judgement; it is blocked on one construction, and the construction is the five
presentations' definitions.** Those are M's to supply or to withdraw, because they exist only in the
prose that states them.

## 4. What is owed

1. **The five presentations' definitions.** Without them the sentence cannot be verified, corrected or
   narrowed. This is the whole of what stands between A6 and a repair.
2. **The factor 31** is unexplained. Whoever supplies the definitions should check it first: if the region
   is a union of 31 congruence classes, or 31 shells, or 31 anything, the four counts fall out and the
   fifth's being different becomes the informative fact.

Nothing is repaired in any volume. Every figure is MEASURED by `coupling.py` or RECORD-CARRIED with its
quote.
