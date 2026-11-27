# Review R-P-TRF: proofs/P-TRF.md (the smaller index sets at the other values of h)

File: research/warp-drive/paper/reader/proofs/P-TRF.md, md5 02cba0dc0b656d785d718d765a9cabd8, 650 lines, read at
87e4d2c5 on branch ccr-66909215-gi0qa5. The writer's report is notes/reports/P-TRF.md. No repository file was edited
and nothing was committed.

## Outcome

- The mathematics is correct. Every step of the six results was checked, and every constant was recomputed.
- No Major finding.
- Two minor findings:
  - m1: no crosswalk notes for the nine existing labels that items 2–11 change;
  - m2: "the gap of (G) is μ♭(h)" in the opening of sec:tr-flat, and the matching "at these" in item 6, leave out the
    cap ε_Υ. Above ε_Υ that statement is not proved and can fail.
- Two nits: n1 in chapter text and n2 in the notes only.
- A tested fixed copy is at
  /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/rptrf/P-TRF.fixed.md
  (686 lines, md5 07edd9208d46a77d0d65da29beafb8cc).

## Mechanical checks

The scratch tree is `git archive 87e4d2c5` under
/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/rptrf/.

- **Old texts.** All eleven Placement texts (the insertion point and items 2–11) occur exactly once at 87e4d2c5, at the
  stated line numbers, and each is a run of whole lines.
  - Chapters 71, 03 and 90 and their crosswalks are byte-identical at aa181269, the writer's base, and at 87e4d2c5.
  - The commit after 87e4d2c5, 638510a5, touches only solver/README.md.
- **Application.** A script applied the Placement and the seven rows, replacing `@PENDING:` with `@87e4d2c5:`. The rows
  go after the row of prop:tr-mu-small.
- **The three required checks**, on both the file as written and the fixed copy:
  - `lint.py --chapters`: 0 hits (5228 labels);
  - `assemble.py --check`: 0 problems;
  - the assembled-paper command prints `[] 0`.
- **Crosswalk.** Chapter 71 has 287 labels and 287 rows, in chapter order; chapters 03 and 90 are also in order. Each
  new row's line number points at its label: sec:tr-flat:1, prop:tr-flat-serves:15, def:tr-flat-excess:93,
  prop:tr-flat-lambda:104, thm:tr-flat:199, prop:tr-flat-lower:247, rem:tr-flat-scope:280.
- **Paper rules.**
  - Chapter-text lines are at most 121 characters (characters, not bytes).
  - The only line starting with a marker is the heading.
  - Labels are lowercase.
  - No file or program names.
- **No printed number changes.** Every number of each old text occurs in its new text; only the stop after
  4.76·10⁻¹¹ moves.

## 1. prop:tr-flat-serves

### (a), at every h ∈ (0, 10⁻⁶]

Each input of def:is-flat-set through thm:is-flat-serves was checked against its source.

- **□^Υ_b carries E_Υ, not E_C.** eq:iii-b-6-4 reads □^Υ_(g,E_Υ) := 2δ_(g,E_Υ)G_gδ*_g; E_C enters only □^C. So the roots
  depend only on z: R, 𝔡₀, 𝔡₁, δ′₁ and δ₂ (lem:is-roots, lem:is-offsets). The weights lie in [0, 2 + 𝔡₁), where
  E(α) = R + ℕ₀ (proof of prop:is-ind).
- **The parity preserves c_C.** (P3) of lem:iii-i15-1-1 states that x ↦ −x preserves c_Υ, c_(Υ,H) and c_C (radial
  coefficients) and commutes with L_b, □^Υ_b, P_b and L̂_b(0). The parities of the constructions come from the proof
  of thm:is-d0 (b).
- **c_b and ω̇_b(0, ·) come only from g_b and the inverse of (□^Υ_b)^(0).** By eq:iii-f3-2-1,
  ω̇_b(ḃ) = −(□^Υ_b)^(0)⁻¹η_b(ḃ) with η_b = 2δ_(g_b,E_Υ)G_(g_b)ġ_b, and ġ^Υ_b = ġ_b + δ*_(g_b)ω̇_b. Neither uses E_C,
  and rem:is-cb-open says the same. So the removed pairs, ℰ^φ_ind and eq:is-flat-memb are the same at every h.
- **The physical states add only integers and ι + 1 + j with real part above 3.** By the proof of prop:is-iota they add
  integers and r + 2 = ι + 1 for the roots r = ι − 1. That proof uses (C1) only (proof of prop:tr-inputs (a)), and (C1)
  holds on (0, 10⁻⁶] (lem:iv4-1-3 (a)). Re ι > 2 by prop:np-10-54 (ii). So below real part 3, ℰ^ι_ind at h is ℰ_ind
  plus integers.
  - The monotonicity argument of lem:is-flat-memberships (c) then gives ℰ^(ι,φ)_ind ⊂ ℰ^ι_ind. It needs no simplicity
    and no (H_ε).
  - 𝔡₁ ∈ π_1ℰ^(ι,φ)_ind, and 𝔡₀ is not in it.
- **The increments.** Only 𝔡₁ lies below 1. Every increment up to 3/2 is a sum of 𝔡₁, 1, 1 + δ′₁, 1 + δ₂, 1 + 𝔡₀ and
  1 + 2𝔡₀; these six lie in the h-independent ℰ^φ_ind.
- **The rest.** Λ^φ ⊂ Λ at h. η_0 = 𝔡₁, and J_* = ⌈5/𝔡₁⌉ + 2 = 15,000,015 (5/𝔡₁ = 15,000,012.92). These follow as
  stated.

**Is anything h-dependent missed?** No. I also checked:

- the least ℰ^C_I, fixed by σ_Υ;
- ℰ^♯_+ ∩ {Re < 2} = {(λ_♯, 0)} and λ_♯ = 3/2 + (1 − e_Υ)γ_Υ;
- 𝒢 and ℰ_col, built from ℰ^φ_ind;
- the class roots and the towers of □^Υ, and the gauge and class states, which lie in ker L_b without E_C;
- lem:is-flat-uses, which concerns proofs at every admissible point.

The h-dependent objects are 1 + 𝒵, handled in prop:tr-flat-lambda, and the pole orders and multiplicities, which do not
depend on the index sets and enter (b).

### (b), on [h_m, 10⁻⁶) ∖ 𝖩

- **Orders.** Orders for the smaller sets are at most those of the sets as constructed, by the inclusions.
- **l_* = 50.** It follows from prop:tr-inputs (a), (b), (d).
- **k̄_0 = 3.** prop:is-count (b) reads ℰ_ind below 1.0198 and the orders of ℰ_++ (prop:is-ci-pp (b)), that is the
  exponents below 1.5099. Nothing lies in (1.5, 1.5099), and the orders there are at most 3 (prop:tr-inputs (a)).

The step is correct.

*Observation, no change asked.* The order bound 3 below 3/2 uses only (C1). So k̄_0 = 3 could be proved at every
h ∈ (0, 10⁻⁶]. The file states it only where l_* is proved. This is conservative and true. "The proof of part (b) is
not available" is accurate as written, but Notes §1's "k̄_0 and l_* ... need h ∈ [h_m, 10⁻⁶) ∖ 𝖩" is too strong for
k̄_0.

## 2. def:tr-flat-excess

- **m♭.** m♭(y) = (⌊y/𝔡₁⌋ + 1)𝔡₁ − y is the least positive q𝔡₁ − y. It is one of the numbers whose infimum is m(y)
  (p = 0), so m(y) ≤ m♭(y) ≤ 𝔡₁. This holds also when y/𝔡₁ is an integer.
- **μ♭(h).** μ_G < μ♭ (eq:is-mu, cor:is-flat). Hence μ(h) ≤ μ♭(h) ≤ μ♭.
- **μ♭.** μ♭ = 4470304𝔡₁ − 1.4901 = 5.0191362·10⁻⁸ < 5.0193·10⁻⁸.

**The numbers, recomputed.** 𝔡₀, 𝔡₁, δ′₁ and δ₂ were taken from the closed forms of lem:is-offsets (a) at 80 digits;
the floors use the enclosures of lem:is-offsets (b).

- **ℬ♭ has 31 elements.** That is λ_♯, the four irrational λ_♯ + 1 + t, |σ^(2)| = 9, |σ^(3)| = 16, and 3. Its
  30 numbers y = 3 − β < 3 give Σ(⌊y/𝔡₁⌋ + 1) = 59,377,256, so 59,377,257 with β = 3. Without λ_♯ + 1 + δ′₁ and
  λ_♯ + 1 + δ₂ the total is 56,436,656, as in cor:is-flat.
- **The sum over Z₃.** It was recomputed from the 1269 + 680 rows of sec:tab-is, each non-real row counted twice and
  every floor determined at both ends of its interval (y ± 10⁻²¹):
  - Σ_(Z₃)(⌊y_ι/𝔡₁⌋ + 1) = 3,623,813,354;
  - the non-real part is 1,227,124,256;
  - #Z₃ = 2629.
  - N̄♭(10⁻⁶) = 59,377,257 + 3,623,813,354 = 3,683,190,611.
- **The least m♭(y_ι).** It is 3.5481255635·10⁻¹⁰ at l = 700, which is μ♭_Z; the next is 4.24068·10⁻¹⁰ at l = 869.
  So μ♭(10⁻⁶) = μ♭_Z.

## 3. prop:tr-flat-lambda

### (a)

- **The part below 3 + ε.** The increments below 3/2 that can enter below 3 + ε (ε < δ₂) are q𝔡₁ and t + q𝔡₁, t ∈ T.
  - The generators there are the exponents of ℰ_++ (λ_♯ plus increments), π_1𝒢, π_1ℰ^C_I (2 + c, 5/2 + c and 3, as
    ε < 0.0099), λ_♯ and 3.
  - g + t > 3 + ε for g ≠ λ_♯ unless g + t = 3, and λ_♯ + 1 = 5/2 + 0.0099.
  - This gives exactly {β + q𝔡₁ : β ∈ ℬ♭}, real and independent of h.
- **The excesses, recomputed.**
  - The least m♭(3 − β) is at y = 1.4901: μ♭ = 5.01913624·10⁻⁸.
  - At the other 29 numbers it exceeds 1.388886·10⁻⁷ > 1.3888·10⁻⁷, attained at y = 1. This holds even from the
    rounded "frac" column: (1 − 0.58335)𝔡₁ > 1.38883·10⁻⁷.
  - m♭(0.4901) = 2.4463581·10⁻⁷ and m♭(0.4901 − 𝔡₀) = 2.4463637·10⁻⁷ both exceed 2.446·10⁻⁷.
  - y/𝔡₁ = 1470297.26609 and 1470293.26609 at 0.4901 − 𝔡₀ and 0.4901 − 2𝔡₀.
- **The third window, checked directly.** λ + 𝔡₀ ∈ (2, 2 + ε] forces Re λ < 2, so λ = λ_♯ + q𝔡₁ with excess at least
  m♭(0.4901 − 𝔡₀). λ + 𝔡₁ lies in Λ^φ_ℬ. "For every ε_K > 0" is right: for ε_K ≥ δ₂ the element 3 + μ♭ violates (G).
- **The generator 1 + 𝒵.**
  - (C1) gives 1 + 𝒵 = {3} ∪ {ι ∈ Z(h) : Re ι < 4}.
  - lem:tr-z3 (a) puts Re ι ≥ 3 + ε_Υ > 3 + ε_+, or Re ι > 2 + 1.4646·10⁻¹⁰.
  - With 𝔡₁ as the only increment below 1, the description and both real-part statements follow.

### (b)

- **First and third windows.** Elements of Λ^φ ∖ Λ^φ_ℬ have real part above 2 + 1.4646·10⁻¹⁰ > 2 + ε_K at most 3 + ε_K,
  and real part above 2 in general. So they miss the first and third windows.
- **Second window.** There the excesses are q𝔡₁ − y_ι ≥ m♭(y_ι).
- **Converse.** It uses λ_♯ + 4470304𝔡₁ and ι + (⌊y_ι/𝔡₁⌋ + 1)𝔡₁ ∈ Λ^φ.
- **(G⁺).** The same argument gives it.
- Both equivalences hold under ε_K < ε_Υ and ε_+ < ε_Υ, as stated.

### (c)

- **The count.** The bound with ⌊(y_ι + ε_+)/𝔡₁⌋ + 1 is right; m♭(3 − β) ≥ μ♭ > ε_Υ > ε_+ makes the ℬ♭ count
  ⌊(3 − β)/𝔡₁⌋ + 1, whether or not β + q𝔡₁ = 3 can occur. For ε_+ < μ♭(h) it equals N̄♭(h).
- **The explicit bound.**
  - The y_ι bounds f_B and f_P are those of the proof of lem:tr-z3 (b).
  - Both functions are non-increasing, and the integral comparison is that of lem:tr-z3.
  - ½∫f_B x^(−1/2) = 0.72854612 and ½∫f_P x^(−1/2) = ½(11/15)^(3/2) = 0.31399457 (also by quadrature).
  - 1/𝔡₁ < 3,000,002.58333387; 426/𝔡₁ = 1,278,001,100.50; 3,000,002.5834 · 1.356537 = 4,069,614.50.
  - 59,377,683 + 1,278,001,101 = 1,337,378,784 < 1.33738·10⁹.
- **Values.**
  - At h = 10⁻⁶ the bound is 5.40708·10⁹ < 5.408·10⁹.
  - At h_m it is 5.91211·10¹¹ < 5.913·10¹¹ (h_m^(−1/2) = 144,942.76).
  - Sanity check at 10⁻⁶: Σy_ι = 1207.94 < 1782.5 and #Z₃ = 2629 < 3143.7.

## 4. thm:tr-flat

- **Hypotheses.** 0 < ε_K < ε_+ < min(μ♭(h), ε_Υ) and ε_K < 0.998ε_Υ are what the proof uses:
  - (G) and (G⁺) via prop:tr-flat-lambda (b);
  - ε_+ < ε_Υ ≤ ε_ind(h) and ε_+ < δ_♯ for eq:iii-i9-1-1;
  - ε_K + ε < 0.999ε_Υ and ε_K < 0.998ε_Υ ≤ ε_g − 2ε;
  - prop:uc-dependence's own ε_K < 0.998ε_Υ.
  - The rest of the proof follows that of thm:tr-transfer (iii) item by item. prop:tr-flat-lambda replaces
    cor:is-flat, and prop:tr-flat-serves supplies k̄_0, l_*, η_0 and J_*.
- **The writer's ε_+ < ε_Υ.** Confirmed as a condition the proof needs, and one that R-P-D0 m3 and P-UB3's sketch did
  not list.
  - It has two uses:
    - lem:tr-z3 (a) excludes roots only from [3, 3 + ε_Υ);
    - eq:iii-i9-1-1 asks ε_+ < ε_ind, and only ε_ind(h) ≥ ε_Υ is known.
  - In (iii) it is implied by μ(h) ≤ μ_G < ε_Υ. For the smaller sets it binds, since μ♭_Z > ε_Υ already at h = 10⁻⁶.
  - The chapter text calls it a hypothesis, not a necessary condition.
  - Notes §3's first sub-bullet gives the wrong reason (see n2).
- **At h = 10⁻⁶.**
  - The inputs agree with cor:is-flat and thm:uc-integer: μ♭ = μ♭_Z, N̄♭ = 3,683,190,611, ε_K = 1.4589·10⁻¹⁰ <
    ε_+ = 1.459·10⁻¹⁰ < ε_Υ < μ♭_Z, and ε_K < 0.998ε_Υ = 1.4589762·10⁻¹⁰.
  - The integers D_acc and D_NM are those of thm:uc-integer at D_e of prop:uc-explicit.
  - K ≤ 22D_NM + 345 < 3.13622·10³⁹ is prop:uc-data-order (d).
  - The wording is n1.
- **Comparison.** N̄♭(h) < 5.913·10¹¹ < 1.67472·10¹³ ≤ N̄(h), since N̄(h) ≥ 16,747,200,000,000. Every ε_K, ε_+ that (iii)
  admits is admitted by thm:tr-flat. With D_e := F_1 in both, monotonicity in N̄_Λ (prop:uc-dependence) gives the
  comparison of rem:tr-flat-scope.

## 5. prop:tr-flat-lower

- **(a)**
  - λ_♯ + 4470304𝔡₁ ∈ Λ^φ. For ι ∈ Z₃(h), ι − 1 is a root in (0, 3) by (C1), so ι + (⌊y_ι/𝔡₁⌋ + 1)𝔡₁ ∈ Λ^φ, and (G)
    gives ε_K < μ♭(h). This holds at every admissible h ≤ 10⁻⁶, with no h ≥ h_m and no h ∉ 𝖩. It holds for any larger
    ℰ_++ or ℰ^C_I as well.
  - With m := min(μ♭(h), ε_Υ): 3m + 2δ̂ + δ̄ ≤ 2.01447·10⁻⁸ < 2.02·10⁻⁸. Then 3(1 − 2.02·10⁻⁸)/δ̂ = 2.0517871·10¹⁰ and
    21 · 2.0517·10¹⁰ = 4.30857·10¹¹.
  - At μ♭(h) ≥ ε_Υ the bound is 1.4035·10²⁰, consistent with thm:loss-d (ii).
- **(b)**
  - **The root ι_B(390, h).** κ = 152880, y = 1.49297 and x ≤ 0.15288 ≤ 1/2. So ι_B(390, h) ∈ (2 + x/2, 2 + 3x/2) by
    lem:tr-large (a), and it is continuous by def:tr-exceptional (b).
  - **The two endpoints.**
    - At 10⁻⁶, ι_* = ι_B(390, 10⁻⁶). Then 2541391𝔡₁ − y_(ι_*) ∈ (1.3537368·10⁻⁷, 1.3537369·10⁻⁷), recomputed from
      lem:is-gap-z's enclosure of y_(ι_*). The text cites "> 1.35·10⁻⁷", which lem:is-gap-z states.
    - At 5·10⁻⁷: ι_B < 2.11466 and 2541391𝔡₁ = 0.84712960386 < 0.8471297, so the sum is below 3.
  - **The intermediate-value step.** h♭ is the largest h with f(h) := ι_B(390, h) + 2541391𝔡₁ ≤ 3. The set is closed
    and non-empty, so h♭ exists. h♭ < 10⁻⁶ as f(10⁻⁶) > 3. h♭ > 5·10⁻⁷, since f < 3 near 5·10⁻⁷ by continuity.
    f(h♭) = 3, as f ≤ 3 there and f > 3 on its right. f > 3 on (h♭, 10⁻⁶] by maximality.
  - **The conclusion.** ι ∈ Z₃(h) (2 < ι < 2.23 < 3), and m♭(y_ι) ≤ ι + 2541391𝔡₁ − 3 → 0. The last assertion follows
    from (a). The argument is complete.
  - **Scale, for orientation only.** ∂_hι_B ≈ κ, so h♭ ≈ 10⁻⁶ − 8.9·10⁻¹³ and h_μ ≈ 10⁻⁶ − 1.1·10⁻²². Not ordering
    them, as the notes say, is correct, since the monotonicity is not proved.

## 6. The ten replacements, and the rest of the paper

Each new text was read in place in the merged tree.

- **Item 2** (chapter 71 opening). True. The lower bound 2.0517 × 10¹⁰/μ♭(h) is the weaker form of
  prop:tr-flat-lower (a). μ♭(h) → 0 at h♭, and the count bound is that of prop:tr-flat-lambda (c).
- **Item 3** (rem:ec-point-outside). True.
- **Item 4** (rem:ec-lb-unbounded). True.
- **Item 5** (sec:tr opening). True, and it removes the false "does not treat them at other h".
- **Item 6** (the end of the second paragraph of sec:tr). True except for "at these", which is m2.
- **Item 7** (rem:tr-scope). True, and it removes the false "at the computational point only". 2541391𝔡₁ is a sum of
  increments of Λ^φ.
- **Item 8** (sec:tr-proof (iii)). True: the as-constructed run uses none of def:is-flat-set–cor:is-flat.
- **Item 9** (prop:tr-mu-small). The qualification is right: its last step is thm:tr-transfer (ii), which is for the
  sets as constructed.
- **Item 10** (chapter 03). True: h♭ ∈ (5·10⁻⁷, 10⁻⁶) gives γ_C ∈ (10⁶, 2 × 10⁶).
- **Item 11** (chapter 90). True.

**Other sites.** I searched chapters/ for "other h", "other values of h", "other damping", "these h", thm:tr-transfer,
prop:tr-mu-small, h_μ, μ(h), thm:is-flat-serves, cor:is-flat, "as the proofs construct", "as constructed" and
"computational point only".

- **No other sentence becomes false.** Every hit is one of the following:
  - scoped to the index sets as constructed;
  - stated at the computational point (thm:loss-d's closing, rem:ec-upper-point, rem:ec-upper-open, sec:uc-close,
    rem:is-summary, rem:uc-offset-d0, 00-front, 01-introduction:150–157, 03-theorems:312–318);
  - valid for every choice of index sets (prop:tr-fail).
- **rem:uc-data-order-limits** ("except at the points of thm:tr-transfer (iii)") stays true; thm:tr-flat has the same
  points.
- **The "Used in" lines of sec:tab-is** stay true, since sec:tr-flat uses those rows only through cor:is-flat.
- **63-own-data:70** ("d is bounded above only at the computational point") predates P-TRF and is not changed by it.
  The bounds at other h, in thm:tr-transfer (iii) as in thm:tr-flat, are conditional on admissibility and (R_h). No
  change is asked here.
- The writer's Notes §5 list is accurate.

## Findings

### Major

None.

### minor

**m1. No crosswalk notes for the changed existing labels.**

- The file adds the seven new rows only. Items 2–11 change text in nine existing labels:
  - chapter 71: ch:explicit-constants, rem:ec-point-outside, rem:ec-lb-unbounded, sec:tr (items 5 and 6), rem:tr-scope,
    sec:tr-proof and prop:tr-mu-small;
  - sec:further-results in chapter 03;
  - sec:scope-constants in chapter 90.
- P-D0 ("Notes to append to existing rows") and P-UB3 (a row for each changed label, source appended) both recorded such
  changes, and the crosswalk rows of these labels carry those sources. Without notes the provenance of the ten texts is
  lost.
- **Fix:** a new section "### Crosswalk notes for the changed labels" after the new rows. It gives, for each label, the
  source `P-TRF.md@PENDING:N` (N the first line of its new text), the source name and the note, to be appended to the
  existing fields after "; ".
  - It sits under its own heading, so that a script taking all indented rows under "### Crosswalk rows" does not insert
    them as new rows.
  - Applied and tested: each row keeps four fields, and the labels stay in order.

**m2. "The gap of (G) is a least excess μ♭(h)" leaves out the cap ε_Υ.**

- **Where.** The opening of sec:tr-flat, line 10, has "as 𝔡₁ is the only increment of real part below 1, the gap of (G)
  is a least excess μ♭(h) ≥ μ(h) ...". Item 6 has "The upper bound becomes the bound of [[prop:uc-dependence]] at these".
- **What is proved.** prop:tr-flat-lambda (b) proves "(G) iff ε_K < μ♭(h)" only for ε_K < ε_Υ.
- **Why it matters.** μ♭(h) can exceed ε_Υ; it does at h = 10⁻⁶, μ♭_Z = 3.548·10⁻¹⁰. lem:tr-z3 (a) excludes the roots of
  real part ≥ 3 only from [3, 3 + ε_Υ).
  - Just outside an interval of 𝖩_B(l, 3), with ι_B(l, h) = 3 + ε_Υ + η, that root is an element of Λ^φ of excess
    ε_Υ + η. The gap of (G) is then below μ♭(h) whenever μ♭(h) > ε_Υ + η.
  - So the sentence is unproved and in general false.
  - For the index sets as constructed the analogous sentence of the sec:tr opening is right, as μ(h) ≤ μ_G < ε_Υ.
- **Item 6.** "At these" likewise suggests ε_+ up to μ♭(h). thm:tr-flat admits ε_+ < min(μ♭(h), ε_Υ) only.
- **Fix:**
  - Line 10: "for ε_K < ε_Υ the gap of (G) is a least excess μ♭(h) ≥ μ(h) ...", with lines 10–13 rewrapped.
  - Item 6: "at that count, for the ε_K and ε_+ that [[thm:tr-flat]] admits, under the same conditions".
  - No number changes.

### nit

**n1. thm:tr-flat, the paragraph at h = 10⁻⁶, lines 209–211.**

- **The problem.** "the bounds of [[prop:uc-dependence]] at these inputs are those of [[thm:uc-integer]]: N_Λ ≤
  3,683,190,611 ([[cor:is-flat]]), d_NM < 1.42556·10³⁸, and K < 3.13622·10³⁹ ([[prop:uc-data-order]] (d))" is loose:
  - N_Λ ≤ 3,683,190,611 is an input (cor:is-flat), not a bound of prop:uc-dependence;
  - K is prop:uc-data-order (d), not a bound of either result;
  - D_e must be that of prop:uc-explicit, which the proof says and the statement does not.
- **Fix.** "...satisfy the conditions above; N_Λ ≤ 3,683,190,611 ([[cor:is-flat]]); and at these inputs, with D_e of
  [[prop:uc-explicit]], D_acc and D_NM of [[prop:uc-dependence]] are the integers of [[thm:uc-integer]], so that
  d_NM < 1.42556·10³⁸ and K < 3.13622·10³⁹ ([[prop:uc-data-order]] (d))." Same numbers and same line count.

**n2. Notes §3, first sub-bullet (not chapter text).**

- It gives "an element of Z₃(h) plus 1 has real part above 3 + 1.4646·10⁻¹⁰" as the reason ε_+ < ε_Υ is needed. That
  alone would allow ε_+ up to 1.4646·10⁻¹⁰.
- The binding reason is lem:tr-z3 (a)'s window [3, 3 + ε_Υ) for the roots of real part ≥ 3, which the chapter proof
  uses correctly.
- Corrected in the notes.

## The fixed copy

- **Path.**
  /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/rptrf/P-TRF.fixed.md
  (686 lines, md5 07edd9208d46a77d0d65da29beafb8cc).
- **What changed.**
  - It applies m1, m2, n1 and n2, and adds Notes §8, which lists the reader's fixes.
  - The chapter-text line count is unchanged, so the seven row line numbers stay 1, 15, 93, 104, 199, 247 and 280.
  - The note sources point at the first lines of the new texts: 325, 343, 359, 379/396, 417, 435, 452, 467 and 483.
- **Tested** on a fresh `git archive 87e4d2c5` tree, with the eleven texts, the seven rows and the nine appended notes
  applied by script:
  - lint `--chapters` gives 0 hits;
  - `assemble.py --check` gives 0 problems;
  - the assembled-paper command prints `[] 0`;
  - the crosswalks of 71, 03 and 90 are complete and in order, with four fields per row;
  - every row pointer is checked;
  - all old texts are unique, no printed number changes, and lines are at most 121 characters.

Verdict: CONFIRMED
