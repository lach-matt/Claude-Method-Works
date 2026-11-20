# R-I1b: confirming reading of the I-1 integration hunks, chapters 30–84 (my share)

Scope: the I-1 hunks in chapters 30, 31, 32, 34, 35, 36, 37, 38, 39, 43, 46, 60, 70, 80, 81 and 84 of
scratch/i1/i1.diff (base 9f47d2bc). For each of these chapters the I-1 hunk is byte-identical to
`git diff 9f47d2bc HEAD` (HEAD f877acb1), and the working tree is clean, so the files read are exactly base + I-1.
Work files: scratch/r_i1b/ (old/ and new/ copies, word-level and line-level diffs).

## What was checked, and the result

**Nothing else in the diff (check 4).** For every chapter I compared the old and new word sequences after applying
only the intended renames. Everything left over is an intended item:

- 30, 37, 60, 70, 80, 81, 84: no word changes beyond 𝒦_m → 𝒴_m and β_0 → β_Γ (30, 37, 81, 84 are pure rewraps).
- 35, 39: no change beyond 𝓘 → ℐ (35 also ℂ^N → ℂ^(N_E)). The line structure is unchanged.
- 31: the chain insertion, five β₀ → β_Γ sites (206 ×2, 489, 873, 914, 1140) and the reworded remark. Nothing else.
- 32: chain, four β_0 → β_Γ sites, the (E3) clause at 1863. 34: chain, β_Γ at 259, the citation at 453, N_E.
- 36: "(E1)–(E2)" → "(E1)–(E3)" at 1307 and the (E3) clause at 1622. 46: the citation at 1619.
- 38: chain, β_Γ at 703 and 929–935, 𝓘 → ℐ. 43: 𝓘 → ℐ, β_Γ at 256, ρ → ψ (all row objects), "finitely many
  windows" at 355, the (E3) clause at 642, ψ → ϖ at 657–658, the notation sentence at 70–71.

No label `{#…}` changed. The only reference changes are the five citations the items name.

**Renames (check 1).**

- 𝒦_m → 𝒴_m (60, 80, 84): 2, 9 and 5 sites. 𝒴 had 0 occurrences in these chapters before. The 𝒦 that remain are
  all the Kretschmann scalar (80:174, 196, 203, 206, 384, 423; 84:1010–1011). The cited source, chapter 4
  (eq:stage-m, eq:stage-system, lem:first-entry), writes 𝒴_m. No 𝒦_m or 𝒦_1 is left in any chapter. (The 𝒦_0 of
  39 is a compact set and the 𝒦_I of 82 is a local commutator sum. Neither is this object.)
- 𝓘 → ℐ (35, 38, 39, 43): 55, 98, 50 and 15 sites, one for one. ℐ had 0 occurrences there before. No 𝓘 is left in
  any chapter. Every ℐ means null infinity: ℐ⁺, the index sets ℰ_(ι⁺,ℐ), and at 43:723 the ℐ-face of the space
  on M in [[prop:iii-a-4-2]] (chapter 30 writes the same face ℐ).
- ℂ^N → ℂ^(N_E) (34:500–575, 35:1119): complete. No bundle-rank ℂ^N is left in chapters 20–90 (the only ℂ^N left
  is in the literature statements of chapter 95). 34:88 already reads N_E = 15. The N = 4 at 34:406 is the space
  dimension, not a rank.
- β_0/β₀ → β_Γ: every renamed site is the trapped-set constant ½ min_Γ |q_(z₀)| of (Γ.4), or its value 2, or its
  continuity in b. Every horizon β₀ stayed: 31:263–281, 455, 634–678, 1082–1092 ((H3)), 32:417–419 and 34:794 (the
  red-shift rate in the threshold), 35:237–816 (the radial-source rate at ∂ℛ_±). The β₀ in 36:355–1846 are covector
  components, and 43:367 has levels β_0 < ⋯ < β_K; neither is this object. No trapped-set β_0 is left in my share.
  The one left anywhere is 71:642, deferred by the coordinator. 31:494–496 now matches 21:143 (β_Γ in (Γ.4)) and
  20:92 (β₀ in (H3)). q^Γ ≥ 2β_Γ (38:929) and q^Γ = 2β_Γ = 4 (70:913) are consistent with 31:489.
- Row index ρ → ψ in 43: complete within 43. No ρ subscript is left there; every ρ in 43 is now ρ_+, ρ_K or ρ^a.
  The new sentence at 70–71, "as in [[ch:s22]] and [[ch:s23]]", is true: 41 and 42 write Y_ψ, d_ψ, w_ψ, T_(ψ,b),
  𝒴_ψ and ℰ^α_ψ. The local ψ := φ/R became ϖ. ϖ appears nowhere else in 43, and OUTLINE reserves only ϖ_K, which 43
  does not use. **Not complete in a citing chapter**: see finding 1.

**Added proof steps (check 2).**

- 31:55. By def:s12-radii, r₀ = r_♭ ≤ ½R₁ and δ₀ = min(R₁/16, r_♭/4) ≤ R₁/16. So r₀ + δ₀ ≤ 9R₁/16 < 14R₁/16 = r₂.
  Both facts are in the stated reason "δ₀ ≤ r_♭/4, r_♭ ≤ ½R₁ < 7R₁/8 and δ₀ ≤ R₁/16". I rechecked the other
  links: ½r_♭ ≤ r₀ − 2δ₀ follows from δ₀ ≤ r_♭/4, and r_h + δ₀ ≤ 17R₁/16 = r_e. The link is true.
- 32:41 and 34:46 cite [[sec:i-a-1-1]], which fixes 0 < r₀ − 2δ₀ < r₀ < r₀ + δ₀ < r₂ < r_h (20:29) and shows the
  condition costs nothing (20:43–48). 38:45 cites [[def:s12-radii]] (true by the computation above). No chain
  without r₀ + δ₀ is left in chapters 20–48.
- (E3) at 32:1863. (E3) is stated with a projection Π that is bounded on L², maps H^s into itself and commutes with
  N(A, ι). The projection onto the types of f_(m_*) qualifies, since N(A, ι) preserves the types (same sentence).
  Then (E3) gives that N(A, m_*) is bijective on ΠC^∞ exactly when m_* is not a root of those types. This is the
  lemma's hypothesis, and it is what defines w. Correct.
- (E3) at 36:1307. The proof uses that the poles of N₀(λ)⁻¹ in the strip are the roots, and that N₀(z_j) is
  invertible. That is (E3) with Π = Id. Correct.
- (E3) at 36:1622. The line Re λ = α − 2 − j holds no indicial root, so (E3) (Π = Id) gives invertibility on it.
  Correct (see nit 2).
- (E3) at 43:642. The strip avoids spec_b(A_0) = {−μ}, so N(A_0, ζ) is invertible there by (E3). Correct.
- lem:s14-delta50 at 34:453 and 46:1619. 33:2848 states 1.941370568463·10⁻⁸ < δ_50 < 1.941370568464·10⁻⁸, which
  agrees with the 1.94137… × 10⁻⁸ of 46:1618, and rem:s14-delta50 (33:2822) says the value is given there.
  cor:s14-eps-ind-point proves ε_ind(10⁻⁶) = δ_50, so the new key is the right one for "its value".
- 43:355 "finitely many windows": N_* is defined nowhere in chapters 20–48 (its only definition is a local one in 85). The inventory's preamble (43:324–325) fixes
  every loop length by the weights and orders, never by k, which is all that thm:iii-j2-4-1 uses. Not a weakening.

**Rewraps (check 3).** 30:1893–1898, 32:1636–1638, 32:1863–1869, 36:1622–1624, 37:1131, 38:45–52, 43:642–644,
46:1618–1621, 81:983–987 and 84:1297–1298. The word sequences are identical except for the inserted citations.
Every added line has at most 121 characters (the maximum is 121; counted in code points). No added line starts with
"+ ", "- ", "* ", "> ", "#", "=", "|", or a numeral followed by "." or ")". The old offenders are gone: "1) at tf"
(30), "0) and" (32), "0. So" (81), "1) i^(j−2)" (84), and the stray "([[lem:iii-h1-4-1]])" line (37). Across all 16
chapters, the only numeral line starts left are the intended list 80:75–95.

**Tools.** `python3 lint.py --chapters`: 1 hit (90:66, the pending marker), as expected.
`python3 assemble.py --check`: 4405 labels, 0 problems. I ran both with PYTHONDONTWRITEBYTECODE=1, and
`git status` was clean afterwards.

## Findings

**1. minor — 46:1728 and 46:1769: the row index of the towers is still ρ in chapter 46.**
Evidence: 41:1065–1066 and 42:151, 696 write the coefficient space 𝒴_ψ and the towers T_(ψ,b). Chapter 43 now
writes ψ, and chapter 46 itself writes Y_(ψ,rem), ψ ∈ ℛ′_0 at 1386–1408. But 46:1728 reads "coefficient spaces 𝒲_τ,
𝒴_ρ", and 46:1769 reads "the towers and states at b used in h_(b,rem)(q), namely T_(ρ,b)". The index ρ is defined
nowhere in 46, where ρ is a boundary defining function (46:1720–1721). The I-1 item scoped the rename to chapter 43,
so it is incomplete in a chapter that cites the renamed object. The text was already there at 9f47d2bc.
Fix (character counts unchanged):
- 46:1728 "coefficient spaces 𝒲_τ, 𝒴_ρ (spaces of harmonics" → "coefficient spaces 𝒲_τ, 𝒴_ψ (spaces of harmonics".
- 46:1769 "used in h_(b,rem)(q), namely T_(ρ,b), h^(≤1)_(b,s1)" → "used in h_(b,rem)(q), namely T_(ψ,b), h^(≤1)_(b,s1)".
No other subscript-ρ row object is left in chapters 38a and 40–48 or in the 60s.

**2. nit — 36:1622–1623: the bound on the compact part of the line, and a repeated reference.**
The sentence reads "its Mellin family is invertible on that line ((E3) of [[sec:iii-a-1-1]]), with the bounds (E1) of
[[sec:iii-a-1-1]]". (E1) bounds the inverse only for |Im λ| ≥ R. On the rest of the line the bound comes from (E2)
(uniform on compact sets of non-poles), as 43:641–642 says explicitly. The text was already there; the hunk added
only (E3). Fix: replace "((E3) of [[sec:iii-a-1-1]]), with the bounds (E1) of [[sec:iii-a-1-1]], and" with
"((E3) of [[sec:iii-a-1-1]]), with the bounds (E1) there for |Im λ| large and (E2) on the rest of the line, and",
and rewrap the paragraph to ≤ 121 characters.

## Verdict

**NOT CONFIRMED**: 0 Major, 1 minor (finding 1), 1 nit (finding 2). Every applied item in my share is correct,
complete within its chapter, and changes nothing else. The one gap is the row-index rename, which also needs 46:1728
and 46:1769.
