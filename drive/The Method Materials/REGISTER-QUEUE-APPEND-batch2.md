# REGISTER QUEUE APPEND — B-list Batch 2 (chat 56, BUILD56 → BUILD57)
# Append to OWED-REGISTER-EXPANSIONS.md. Numbers await Register 1.1 (append-only; Ruling 27).

## SUBJECT-REGISTER CORRECTION SLIPS (queue after slips B1-C1..C3)

SLIP B2-C1 — THE ω-BOUND'S PRIOR-ART GLOSS MISSTATED WHAT ω COUNTS; CORRECTED FROM
"NON-MINIMAL COORDINATES" TO "POSITIVE-EXPONENT COORDINATES." The `L.omega` object's
prior-art line read "the number of coordinates in which x is non-minimal." This is false
in the divisor embedding: ω(N(x)) is the number of distinct primes dividing N(x), which is
|{ i : xᵢ > 0 }|, NOT |{ i : xᵢ > minᵢ }|. The floors n, k, e ≥ 1 (`L.def`) put those three
exponents positive on every cell, so three primes divide N(x) universally and ω ≥ 3 everywhere;
the "non-minimal" reading undercounts by treating a floored coordinate at its minimum (value 1)
as contributing no prime, when it contributes one. Measured: over Λ₈, max ω = 8 attained at
100 cells (the "non-minimal" reading gives 96 — the discrepancy is exactly the cells where a
floored coordinate sits at its minimum yet still carries its prime). Tight cell (2,1,3,3,2,1,3,3),
ω = 8 by direct factorisation. The bold statement of `L.omega` was already correct (B1-C2:
"coordinate count," not dim); this slip corrects only the prior-art gloss beneath it. The prior
wording stands as history; the object now carries the positive-exponent reading. Cites B1-C2 and
the `L.omega` object. Both states preserved.

## WORKING-REGISTER ENTRY (editorial; never enters the books)

W-B2 — B-LIST BATCH 2 PARTIAL: MC-07, MC-08, MC-09 AUTHORED AND VERIFIED; MC-10, MC-11 OPEN.
chat 56, BUILD56 → BUILD57. Every claim computationally verified on the rebuilt Λ₈ (976 cells,
recipe from HANDOFF-7) BEFORE writing (HANDOFF-6 rule).

 MC-07 §7.1 ω-bound + rank=Ω(N) [Ruling A: full expansion] — VERIFIED: ω(N(x)) = |{i:xᵢ>0}|
   = #distinct primes | N(x) (real factorisation); max ω = 8 = coordinate count, 100 cells attain
   it; tight at (2,1,3,3,2,1,3,3); ω ≥ 3 everywhere (floors); ω = 8 > dim = 7 at tight cell;
   rank(x) = Ω(N(x)) = Σxᵢ on all 976 cells. AUTHORED: `L.omega` bold statement upgraded to a
   worked proof of bound + tightness (grade PROVED, now earned in place); mechanism note corrected
   (ω is |{xᵢ>0}|, not "non-minimal"); prior-art gloss corrected (→ slip B2-C1). `L.arith`
   mechanism note expanded with the identity rank = Ω(N) = Σxᵢ and the ω/Ω contrast.

 MC-08 §7.2 occupancy measure d(x,y): five forms + metric props [full expansion] — VERIFIED:
   the book's five §9.2 forms all = ∏(|Δᵢ|+1), 2,000 pairs 0 mismatch (p-adic form checked by
   independent numerator/denominator factorisation); d(x,x)=1, symmetric, d≥1 with equality iff
   x=y; multiplicative triangle via per-coordinate (|a−c|+1)≤(|a−b|+1)(|b−c|+1), 200k integer
   triples 0 fail, global equality iff y∈[x∧z,x∨z]; log d = Σlog(|Δᵢ|+1) ℓ¹; hyperbolic balls,
   d=D level set = lattice hyperbola (1+|Δ₁|)(1+|Δ₂|)=D; log-distortion first step log2, tenth
   log(11/10). AUTHORED: `L.occ` five equivalent forms + equivalence proof (one-prime-per-coord),
   grade COMPUTED→PROVED; `L.metric` multiplicative-triangle + ℓ¹ proofs via per-coordinate
   reduction + hyperbolic balls + log-distortion, grade COMPUTED→PROVED. FIDELITY: the five forms
   authored are the main §9.2 list verbatim, not a reconstruction.

 MC-09 §7.3 Möbius closed form + transfer condition (60/56) [full expansion] — VERIFIED:
   closed form μ=(−1)^|y∖x| on antichains else 0, values {−1,0,+1}; TRANSFER BICONDITIONAL
   μ_Λ = μ_arith ⟺ void-free unit hypercube — restricted to the CORRECT population (unit-hypercube
   pairs, where μ_arith≠0): 1,500 sampled, 741 void-free ALL agree, 759 void-bearing ALL disagree,
   0 mixed case; mechanism: void-free unit hypercube = full Boolean cube (Möbius=product), a void
   prunes it. "Seven comparisons" GROUNDED from the build: max local up-degree = 7 (attained at 6
   cells; couplings pin ≥1 coordinate from every cell), so a unit box spans ≤7 coordinates.
   RECONSTRUCTION NOTE: first test flagged 4,000 "violations" — finding was about the test (it
   counted trivial 0=0 agreement on non-unit pairs as violations); corrected to the unit-pair
   population before authoring; nothing wrong entered the file. AUTHORED: `L.mobius` closed-form
   justification + transfer biconditional + verified split + up-degree grounding, grade
   COMPUTED→PROVED, +dependency on `L.arith`.

Volume identity: BUILD57 main 18,446 lines md5 5292fce89637c6b495363f76f99a4885 (UNTOUCHED,
 byte-identical to BUILD56 — Batch 2 is compendia-only); compendia 32,451 lines md5
 e2c0f5a8ead1996b3a69850f11ec0ccc.
Guard substitute (measured, not inferred): diff(BUILD56.compendia, BUILD57.compendia) = exactly
 6 hunks, all within the L.* object cluster (lines 14493–14731): 14497 L.arith · 14685 L.metric ·
 14695 L.mobius · 14715 L.occ · 14725 L.omega statement · 14731 L.omega prior-art. Line count
 32,451 unchanged (delta 0). No other line touched. All §0 compendia discriminators still = 1.
OWED-EXPANSIONS-2 rows 7, 8, 9: mark DONE. Rows 10, 11 remain OPEN. Token resolution remains LAST.
Next: Batch 2 completion — MC-10 (§10.2 correlation 1.49×, NEW M-flagged derivation), MC-11
 (§10.4 closed-form void count + treeness⟺sieve-free). Then B3..B10 in HANDOFF-6's order.
