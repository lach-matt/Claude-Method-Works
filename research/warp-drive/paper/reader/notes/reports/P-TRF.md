# Report P-TRF: the smaller index sets at the other values of h

File: research/warp-drive/paper/reader/proofs/P-TRF.md, 650 lines, md5 02cba0dc0b656d785d718d765a9cabd8. I did not
commit it. The coordinator's snapshot commit d0b280ab holds an earlier draft that differs in two lines of the notes. No
other repository file was edited.

## What is proved

### 1. thm:is-flat-serves at h (prop:tr-flat-serves)

- **(a) Holds at every h ∈ (0, 10⁻⁶].** This covers:
  - ℰ^φ_ind is the same at every h;
  - ℰ^φ_ind and ℰ^(ι,φ)_ind may be taken for ℰ_ind and ℰ^ι_ind, with the forms eq:is-flat-memb;
  - Λ^φ ⊂ Λ (both built at h);
  - 𝔡₁ is the only increment below 1, and every increment ≤ 3/2 is a sum of 𝔡₁, 1, 1+δ′₁, 1+δ₂, 1+𝔡₀ and 1+2𝔡₀;
  - η_0 = 𝔡₁ and J_* = 15,000,015.
- **(b) Holds at every h ∈ [h_m, 10⁻⁶) ∖ 𝖩:** k̄_0 = 3 and l_* = 50.
- **Where it stops.** Nothing fails on [h_m, 10⁻⁶) ∖ 𝖩.
  - On 𝖩 and below h_m, the proof of (b) is not available. It goes through prop:tr-inputs, that is through (H_ε) and
    the simplicity of the roots.
  - This is the same restriction as for the index sets as constructed. The smaller index sets add none.
- **The h-record of each input** is in the proof and in Notes §1:
  - □^Υ_b = 2δ_(E_Υ)Gδ* carries E_Υ, not E_C.
  - The parity preserves c_C.
  - c_b and ω̇_b(0, ·) are built from g_b by inverting (□^Υ_b)^(0).
  - The physical states, through (C1) on (0, 10⁻⁶], add only integers and ι + 1 + j with Re > 3.
- **The earlier review's assessment is confirmed, with two refinements:**
  - what matters is that the h-dependent exponents have real part above 3;
  - l_* = 50 does involve h, through prop:tr-inputs.

### 2. The counterparts of def:tr-excess, prop:tr-lambda and thm:tr-transfer (iii)

**def:tr-flat-excess:**
- m♭(y) := (⌊y/𝔡₁⌋ + 1)𝔡₁ − y;
- μ♭(h) := min({μ♭} ∪ {m♭(y_ι) : ι ∈ Z₃(h)});
- N̄♭(h) := 59,377,257 + Σ_(ι∈Z₃(h))(⌊y_ι/𝔡₁⌋ + 1);
- μ(h) ≤ μ♭(h) ≤ μ♭ < 5.0193·10⁻⁸. This is proved directly: m ≤ m♭ and μ_G < μ♭.

**prop:tr-flat-lambda:**
- (a) Λ^φ_ℬ below 3 + δ₂ is {β + q𝔡₁}, over 31 numbers β (ℬ♭). It does not depend on h, and its least excess over the
  three windows is μ♭. For ε_+ < ε_Υ, Λ^φ below 3 + ε_+ is that part together with the ι + q𝔡₁, ι ∈ Z₃(h).
- (b) For ε_K < ε_Υ, (G) holds for Λ^φ iff ε_K < μ♭(h); (G⁺) holds iff ε_+ < μ♭(h). The third window (λ + 𝔡₀ near
  2), which for Λ^φ is not inside the first, is checked directly.
- (c) N_Λ ≤ 59,377,257 + Σ(⌊(y_ι + ε_+)/𝔡₁⌋ + 1); for ε_+ < μ♭(h) this is N̄♭(h). The explicit bound is
  **N̄♭(h) < 1.33738·10⁹ + 4.0697·10⁶h^(−1/2)**:
  - below 5.408·10⁹ at h = 10⁻⁶;
  - below 5.913·10¹¹ at h = h_m;
  - against N̄(h) ≥ 1.67472·10¹³ for the index sets as constructed.

**thm:tr-flat (the counterpart of (iii)):**
- Hypotheses: h ∈ [h_m, 10⁻⁶) ∖ 𝖩, admissible, (R_h).
- For 0 < ε_K < ε_+ < min(μ♭(h), ε_Υ) and ε_K < 0.998ε_Υ, the choice of def:uc-choice at h is admissible.
- The bounds are D_acc and D_NM of prop:uc-dependence at N̄_Λ = N̄♭(h), k̄_0 = 3, J_* = 15,000,015 and l_* = 50.
- **Check at h = 10⁻⁶:** μ♭ = μ♭_Z, N̄♭ = 3,683,190,611, and the ε_K, ε_+ of eq:uc-choice satisfy the conditions. The
  theorem then gives the bounds of thm:uc-integer: N_Λ ≤ 3,683,190,611, d_NM < 1.42556·10³⁸ and K < 3.13622·10³⁹.
- rem:tr-flat-scope: at every ε_K, ε_+ that thm:tr-transfer (iii) admits, this bound is at most that of (iii)
  (D_e := F_1 in both).

### 3. Lower bounds for the smaller index sets (prop:tr-flat-lower), an addition beyond the brief

- (a) At every admissible h ≤ 10⁻⁶: ε_K < μ♭(h), and d_NM > 2.0517·10¹⁰/min(μ♭(h), ε_Υ) ≥ 2.0517·10¹⁰/μ♭(h).
- (b) μ♭(h) → 0 as h decreases to some h♭ ∈ (5·10⁻⁷, 10⁻⁶). The witness is ι_B(390, h) + 2541391𝔡₁; at h = 10⁻⁶,
  2541391𝔡₁ − y_* ∈ (1.35·10⁻⁷, …).
- So prop:tr-mu-small's conclusion does transfer, with 2541391𝔡₁ in place of w_*. Without this result the scope
  sentences would suggest that the smaller index sets escape the unbounded lower bound near some h, which is false.

## The reviewer's formulas

- μ♭(h): correct.
- The linear count: correct, under 0 < ε_+ < ε_Υ. The constant 59,377,257 needs ε_+ < μ♭.
- One condition the sketch does not show: **ε_+ < ε_Υ**.
  - In (iii) it is implied by μ(h) ≤ μ_G < ε_Υ, but μ♭(h) may exceed ε_Υ.
  - It is needed for the description of Λ^φ (1 + Re ι > 3 + 1.4646·10⁻¹⁰) and for ε_+ < ε_ind(h), of which only ε_ind(h) ≥ ε_Υ
    is known.

## What could not be proved

- k̄_0 = 3 and l_* = 50 on 𝖩 and below h_m: not available, for either family of index sets.
- μ♭(h) at h ≠ 10⁻⁶: not evaluated, as for μ(h).
- The order of h♭ against h_μ: not proved, as the monotonicity of ι_B(390, ·) at x ≈ 0.15 is not established.
- Admissibility at any h and (R_h) off h = 10⁻⁶: undecided, as before.

## Placement

- The new subsection "#### The smaller index sets at h {#sec:tr-flat}" goes at the end of sec:tr, after the paragraph
  that follows prop:tr-mu-small. It holds 7 labels: sec:tr-flat, prop:tr-flat-serves, def:tr-flat-excess,
  prop:tr-flat-lambda, thm:tr-flat, prop:tr-flat-lower and rem:tr-flat-scope.
- Ten replacements, each quoted exactly.
- **False once the flat version exists, replaced:**
  - the sec:tr opening ("does not treat them at other h");
  - the last sentence of rem:tr-scope ("proves thm:is-flat-serves at the computational point only").
- **Qualified (read as covering every choice of index sets):** the last sentence of prop:tr-mu-small.
- **Additions:**
  - chapter 71 opening;
  - rem:ec-point-outside;
  - rem:ec-lb-unbounded;
  - sec:tr opening, the paragraph on input (e);
  - sec:tr-proof (iii): def:is-flat-set–cor:is-flat enter only the run with the smaller index sets;
  - chapters/03-theorems.md:366;
  - chapters/90-scope.md:89.
- Sites checked and left unchanged, with reasons, are listed in Notes §5.
- 7 crosswalk rows go directly after the prop:tr-mu-small row.
- No number already printed changes. This was checked mechanically over the ten pairs.

## Checks

- Scratch trees were made by git archive of paper/reader, at HEAD and at aa181269.
  - HEAD moved to d0b280ab while this work was done.
  - Chapters 71, 03 and 90 and crosswalk/71 are byte-identical at aa181269 and d0b280ab.
- Placement and rows were applied by a script that parses the file. Results, on both trees:
  - lint --chapters: 0 hits;
  - assemble --check: 0 problems;
  - the assembled-paper command prints [] 0;
  - crosswalk: 287 labels, 287 rows, in chapter order.
- Every new number was recomputed exactly, from lem:is-offsets (b) and the 1269 + 680 rows of sec:tab-is: the sums
  59,377,256 and 3,623,813,354, μ♭_Z, μ♭, the integrals, and the remaining constants.

Scratch: /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/ptrf_work/
- text.src: the source paragraphs;
- wrap.py, items.py, notes.md, gen.py: generation;
- apply.py, xwcheck.py, check.sh: application and checks;
- nums.py, nums2.py, ints.py: the numbers.
