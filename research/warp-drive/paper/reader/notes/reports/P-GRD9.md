# P-GRD9: writer's report (sec:tl5-hfz, "The recovery sharpened and counted over the words")

**File:** research/warp-drive/paper/reader/proofs/P-GRD9.md, md5 2cd3f900871544f6ed0bc098a79d1073, 313 lines. It is
uncommitted and was copied once from the scratch draft.
- chapter text: lines 1–204 (sec:tl5-hfz, 12 labels);
- Placement: 206–226;
- Comparison: 228–293;
- crosswalk rows: 295–313.

**Base:** chapter 87 at fa3fa0f0 (md5 e3ab2f41…, 6392 lines). HEAD has since moved to 5deaf9e8, which changes only
rule/ and notes/reports/I-RULE.md. Chapter 87, its crosswalk, lint.py and assemble.py are byte-identical there, so the
Placement and the checks hold at the current HEAD.

I read nothing under method/, drive/, extracted/ or recovered/. I committed nothing and ran plain assemble.py nowhere;
PAPER.md's md5 was unchanged by `--check`. Scratch: scratchpad/reader/pgrd9/.

## What is proved (chapter text)

1. **lem:tl5-hfz-rec, the recovery with the entry (1, 1) apart.** If |H| ≤ 𝔥 < 1 at p, then
   |D̂²Ψ| ≤ 𝔨_♯(𝔥) K_rec((Σ|D̂ℒ_ZΨ|²)^(1/2) + (Σ𝔷_Z²)^(1/2)) + (1 − 𝔥)⁻¹(|𝔣| + 𝔯_♯|Ψ|), where
   - 𝔨_♯(𝔥) := (1 + (2 + √2𝔥)²/(1 − 𝔥)²)^(1/2);
   - 𝔯_♯ := 2‖𝓡̂‖ + ‖𝒞_(·1)‖.

   **How.** |D̂²Ψ| is taken as (R² + |D̂²Ψ(1,1)|²)^(1/2), not R + |D̂²Ψ(1,1)|. R is bounded by (X₀ + 2X₁)^(1/2), not
   √3 X^(1/2). The H term is bounded by |H| R, not |H| |D̂²Ψ|, so it is not moved to the left. A convexity argument in
   s = (X₀/X)^(1/2) finishes the proof.

   **Result.** 𝔨_♯ runs from √5 = 2.236 (as 𝔥 → 0) to 2.442 at 𝔥 = 1/16, against (6/5)(√3 + 8/3) = 5.278. For 𝔥 ≤ 1/4
   every coefficient is at most the old one divided by 1 − (4/3)𝔥.

2. **def:tl5-hfz-constants, the constants with index z.** After Step 1 of the bootstrap, |H| ≤ 𝔰 ≤ 𝔰₁^v ≤ 1/16, and
   this gives:
   - k₁^(j,ν′,z) = 𝔨_♯ K_rec(1 + ν′^(1/2)√7(…)) + (1 − 𝔰₁^v)⁻¹(ν′^(1/2)𝔯_♯ + α_𝔄^(j,ν′));
   - k₂^z = q₁/(1 − 𝔰₁^v) = (5/8)(1 − 𝔰₁^v)⁻¹k₂;
   - k₃^z = (5/8)(1 − 𝔰₁^v)⁻¹k₃;
   - 𝔵^z = 𝔰₁^v sup k₃^z ≤ 2𝔵/3 ≤ 1/6;
   - 𝔨_rec^z, 𝔨_rec^(ϱ,z), 𝔨_rec^(0,z), which carry 𝔨_♯;
   - the coupling norm over the words 𝔞_𝔄(B), and 𝔩₀ and 𝔩;
   - C₁^z and C_(1,ϱ)^z (eq:tl5-hfz-c1).

   The thresholds 𝔰₀, 𝔰₁^v and the cap keep k₃, so no hypothesis moves.

3. **lem:tl5-hfz-abs.** The lemmas of lem:tl5-hfy-abs hold with the index-z recovery constants. Each new constant is at
   most the old one.

4. **lem:tl5-hfz-words, target 1.** At the points of the face:

   (Σ_J |D̂²Ψ_(JB)|²)^(1/2) ≤ μ^(−(|B|+3)/2) 𝔩 𝒥_g + 43^(1/2) P_ϱ, with
   - 𝔩 = 𝔩₀ + 43^(1/2) 𝔵^z (k₁^z + 2)/(1 − 𝔵^z);
   - 𝔩₀ = k₁^z with 𝔞_𝔄 in place of α_𝔄^(N−1,μ).

   **How each part counts:**
   - **The leading term counts once**, because the words ZJB are distinct.
   - **The 𝔷 and 𝔯 terms** use the distinct words JB.
   - **The couplings** enter through 𝔞_𝔄(B), the operator norm of the block family (μ^((|B|+3−|K|)/2)𝔄_(JB,K))_(J,K).
     It is bounded explicitly: 𝔞_𝔄(B) ≤ Schur's (r_B c_B)^(1/2) ≤ 43^(1/2) r_B ≤ (43/2)^(1/2) α_𝔄^(N−1,μ). Hence
     𝔩 ≤ √43 (k₁^z + 2𝔵^z)/(1 − 𝔵^z) always.
   - **The nonlinear part keeps the count 43 per word.** It is bounded through the maximum of the second derivatives
     and is not absorbed over the words. So no condition on √43 𝔵^z is needed, which answers C-P-GRD8's remark
     (√43/4 > 1). The per-word part, where summing does not pay, is kept as it was.

   **Against G0k's pricing.** G0k priced (k₁ + 2√43𝔵)/(1 − 𝔵) and assumed the Schur norm equals the row norm. What is
   proved is 𝔩₀ + √43𝔵^z(k₁^z + 2)/(1 − 𝔵^z): the nonlinear part carries (k₁ + 2) rather than 2. The couplings use the
   true norm, with a bound that is never worse than the per-word one.

5. **lem:tl5-hfz-c1, target 3.** The 𝒥_g and ϱ parts are separated by Minkowski's inequality in L² of the face, then
   in ℝ³, instead of (x + y)² ≤ 2x² + 2y².
   - **C₁^z** = 6C²𝔴⁶ sup 𝔳⁶R⁻³𝔨₂((1 + 18|D̂∂_γ|²)(1 + ϖ′^(1/2))² + 2|∂_γ|²(𝔩 + (2ϖ′)^(1/2))²).
   - **C_(1,ϱ)^z** is C_(1,ϱ) with 2(k₂^z)²/(1 − 𝔵^z)² in place of 32k₂². It is 8k₂²/(1 − 𝔵)² in thm:tl5-hfy.
   - **Proved:** C₁^z ≤ both entries of C₁^x, pointwise in the integrand, and C_(1,ϱ)^z ≤ C_(1,ϱ). So no minimum and no
     maximum device is needed.

6. **thm:tl5-hfz.** Under (a) η₀ < 𝔰₁^v, (b) the admissibility of the rates as in thm:tl5-hfv, and (c) η_z > 0 and
   𝔰_*^z < 𝔰₁^v, the closing condition is

       4 A_z B_z = 4 η_z^(−3/2) (δ_w + η_z^(−1/2) (ε^z + ε_M^z)) (S_F^z + S_M^z) < 1,

   with:
   - ε^z = 𝒮[s_N[2R̂ic] + 𝔰₁^v (1 − 𝔵^z)⁻¹ 𝔤_ϱ^v k₂^z ϱ];
   - η_z = 1 − max(ϑ₁, ϑ₂) − 𝔯^z;
   - S_F^z, S_M^z, ε_M^z, 𝔯^z and 𝔰_*^z, which are those of thm:tl5-hfy formed with the index-z constants.

   It then gives the conclusions of thm:tl5-hf or thm:tl5-hf4 with A_z and 𝔰_*^z. Every new constant is at most the
   one it replaces, and η_z ≥ η. So thm:tl5-hfz contains thm:tl5-hfy, and every earlier closing condition remains
   valid.

7. **rem:tl5-hfz-what.**

## Target 2: what sets k₁^μ, and the sharpening

At G0k's suprema k₁^μ ≈ 5.3 = (6/5)(√3 + 8/3) K_rec with K_rec ≈ 1. The 𝔄, 𝔯₀ and 𝔷 terms carry μ^(1/2) ≤ 3 × 10⁻³, so
the whole of k₁^μ is the constant of the linear algebra of the recovery. It has two parts:
- **The factor 6/5.** It comes from 1 − (4/3)|H| ≥ 5/6, that is from |H| ≤ 1/8.
- **The factor √3 + 8/3.** It comes from two triangle inequalities and from moving the H term to the left.

lem:tl5-hfz-rec replaces both with 𝔨_♯ → √5, a factor 0.4236 (−0.373 decades). The same change lowers k₂ and k₃ by
(5/8)(1 − 𝔰₁^v)⁻¹, and so 𝔵. **√5 is the best this argument gives:** its inequalities become equalities for a
diagonal X with D̂²Ψ(0,0) = −D̂²Ψ(j,j). Going further needs more structure.

## Target 3: the optimised split

The task asked for a free δ. It is not stated, because it is dominated. The triangle inequality in L² gives the factors
(1, 1) on the two parts, against (1 + δ, 1 + 1/δ) for every δ > 0. So C₁ ÷ √2, which is G0k's δ = 0.01 gain, comes
with C_(1,ϱ) ÷ 2 against thm:tl5-hfy, instead of × 7.1. The Comparison and the remark say so.

## What it should give (deduced, not evaluated; Comparison, 269–280)

**Assumptions:**
- k₁^μ ≈ 5.3, carried by its K_rec term;
- 𝔄, 𝔯 and 𝔷 negligible;
- the k-term the whole bracket of C₁, as G0k reports.

**At level 4**, with 𝔵 = 0.073, 0.099, 0.086, 0.147:
- 𝔵^z ≈ 0.046–0.092;
- the k-term √43(k₁ + 2𝔵)/(1 − 𝔵) ≈ 38.5–43.0 becomes 𝔩 ≈ 3.6–5.1;
- C₁ falls by about 1.18, 1.14, 1.16 and 1.08 decades, including the √2;
- C_P^v, where 𝔨_rec is its largest entry, falls by about 1.57, 1.53, 1.55 and 1.48 decades, because 𝔨_rec also carries
  𝔨_♯;
- C_(1,ϱ) is about × 0.30, and k₂ about × 0.63.

If f keeps moving 1:1 with C_P, the gain at level 4 could approach 1.5 decades. It will stop sooner wherever another
condition binds first: the 𝔰_* slack, ϱ, or the part of C₁ without k₁. This needs the evaluation.

**At level 6:** the ε coefficient of ϱ falls by about 0.20 decades, and C_(1,ϱ) by about 0.52.

## Not done, and why

- **Target 4** (the count 7² in 𝔤_(𝒥,s) and 𝔠^♮₄(μ) against 9·2⁴): not attempted.
- **A further lever found, not taken: √7 in 𝔨_rec.** It comes from √7 max_Z |D̂Ψ_Z(p)|. The same argument applies to
  the family (D̂Ψ_Z)_Z at once, with √301 𝔵^z in place of √43 𝔵^z. Deduced worth: 0.14–0.22 decades on 𝔨_rec. It was
  not done, to keep this section's scope checkable.
- **No ℓ² absorption of the nonlinear part.** Its high factors are second derivatives of words not of the form J′B,
  which would need a new bound over the words.
- **Not attempted:** 1/z̲ in 𝔨₂, the rank-3 Sobolev constant, and the 1/κ′ part.

## Checks

The scratch tree is `git archive fa3fa0f0` with the Placement applied by scratchpad/reader/pgrd9/tools/merge.py: item
2 found exactly once, the section appended, and 12 crosswalk rows appended.

| check | result |
|---|---|
| `python3 lint.py --chapters` | 62 files, 5266 labels (5254 + 12), 0 hits |
| `python3 assemble.py --check` | labels 5266, problems 0; PAPER.md md5 unchanged |
| in-memory assembled check | `[] 0` |
| printed numbers of the 5254 existing labels | 0 changed |
| new numbers | Section 57.24; Lemma 57.208 (rec), (57.147), Definition 57.209, (57.148), Lemma 57.210 (abs), Lemma 57.211 (words), (57.149), Lemma 57.212 (c1), Theorem 57.213, (57.150), Remark 57.214 |
| crosswalk | 415 rows = 415 labels of chapter 87, in order; each of the 12 rows' line holds its label |
| chapter-text lines | all ≤ 120 characters |
| wrapped-line starts | no line starts with "+ ", "- ", "* ", "> ", "#", "=" or "|" |
| labels and content | all labels lowercase; no file or program names, no code |
| proofs | 5 opened, 5 closed by ∎ |

Numerical constants used in the text, checked: 𝔨_♯(1/4) = 3.2936, 𝔨_♯(1/16) = 2.4418, (6/5)(√3 + 8/3) = 5.2785,
√5 = 2.2361, √1320 = 36.33 ≤ 37, and 43·4·72 = 12384 ≥ 10560 = 8·1320.

## Points a reader should check first

1. **The norm in lem:tl5-hfz-rec.** It assumes |H|² = Σ_MN |H^MN|² in the frame F. The old proof's |H^11| ≤ |H| and
   |H| |D̂²Ψ| bounds use the same fact.
2. **The weights P_ϱ in lem:tl5-hfz-words (b).** P_ϱ = w k₂^z ϱ/(1 − 𝔵^z), with w = 1, μ^(−(|B|+3)/2) or
   ν^(−(|B|+3)/2) in the four first-order steps. It must bound the ϱ part of the per-word bound for every word of length
   ≤ |B| + 2.
3. **Scope.** lem:tl5-hfz-abs claims every recovery constant is formed from the three factors 6/5·(√3 + 8/3), 6/5·𝔯₀
   and 8/5. The list covers k₁ in all its forms, k₂, k₃ in all its forms, and the three 𝔨_rec. Under this section, 𝔵
   enters only the absorptions; the thresholds keep k₃.
