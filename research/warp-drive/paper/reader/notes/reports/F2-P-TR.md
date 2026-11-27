# F2-P-TR: P-TR rewritten for the repaired Λ

- **File:** proofs/P-TR.md, now md5 **48074b35225dbe6f5b7652efb534d15a**, 924 lines. It was e8d94b368ba272fae34afde252394de1.
- **Built against:** HEAD 8d583306 with P-UB1 (58b580fa…) and P-UB2 (4b283156…) applied. Both files changed during this round; I read and applied their current versions.
- **Repository:** no chapter edited, nothing committed.

## What still holds without new hypotheses

All of the following hold on [h_m, 10⁻⁶] ∖ 𝖩, with h_m = 4.76·10⁻¹¹:

- **Root locations.** The root enclosures, uniform in h ∈ (0, 10⁻⁶]: lem:tr-split, tr-c-v, tr-small, tr-large and tr-slopes.
- **The exceptional set.** 𝖩, the condition (H_ε) and prop:tr-measure: total length below 1.698·10⁻¹¹.
- **Inputs (a)–(d).** prop:tr-eps (ε_ind(h) ≥ ε_Υ) and prop:tr-inputs (simple roots, the exponents of ℰ^ι_ind, the pole orders). These are thm:tr-transfer (i). They do not involve Λ.
- **The failure near h_c (prop:tr-fail), with new numbers.**
  - d_acc > 3(1 − 2.1·10⁻⁸)/ε_ind(h)².
  - This exceeds 7.5755·10⁵⁵, and so both of P-UB2's bounds, once ε_ind(h) < 1.99·10⁻²⁸.
  - That happens for 0 < |h − h_c| < 1.986·10⁻³⁴.

## What is new and proved

- **The lower bound depends on h (thm:tr-transfer (ii)).**
  - Every ε_K for which (G) holds satisfies ε_K ≤ μ(h) ≤ μ_G.
  - Hence d_NM ≥ d_acc > 2.0517·10¹⁰/μ(h) and N_NM > 4.3085·10¹¹/μ(h).
  - Here μ(h) is the least excess above 3 of the families ι + p𝔡₀ + q𝔡₁, with ι running over the roots of real part below 3.
  - This holds at every admissible h ∈ (0, 10⁻⁶], whether or not h is in 𝖩 or below h_m.
  - It is always above 1.2498·10²⁴. At h = 10⁻⁶ it is cor:is-lower.
- **No positive lower bound for μ(h) (prop:tr-mu-small).**
  - There is h_μ ∈ (5·10⁻⁷, 10⁻⁶) with ι_B(390, h_μ) + 356327𝔡₀ + 1116082𝔡₁ = 3.
  - As h decreases to h_μ, μ(h) → 0, so d_NM is unbounded at the admissible h near h_μ. The proof uses only continuity.
- **The structure of Λ at h (lem:tr-z3, prop:tr-lambda).**
  - Under (R_h), off 𝖩: Z₃(h) is finite and Λ ∩ {Re ≤ 3 + ε_+} is Λ_ℬ together with the families from Z₃(h).
  - (G) holds if and only if ε_K < μ(h); (G⁺) if and only if ε_+ < μ(h).
  - The count is explicit: N_Λ ≤ N̄(h) < 4.961·10¹⁴ + 1.0155·10¹²·h^(−1/2). The bound is below 1.512·10¹⁵ at 10⁻⁶ and below 1.477·10¹⁷ at h_m.
  - Elements of Λ of real part at most 2.1 are real; the chain needs this only at real parts up to 2 + ε_K.
- **Two new estimates, needed for these results.**
  - lem:tr-large (c), for b ≥ 56 and h ≥ h_m: ι_P lies within ϱ of ζ. The proof is a convex-majorant Rouché bound with two endpoint checks.
  - lem:tr-slopes (b), for b ≥ 56 near real part 3: ∂_h Re ι_P ≥ 2κ/5.
- **𝖩 gains one clause.** It now includes the h at which Re ι_P is within ε_Υ of 3, for any b. The length bound is unchanged.

## What no longer holds, and what replaces it

- **Withdrawn:** "every number of thm:uc-integer holds at h with the same numbers".
  - With the generator 1 + 𝒵 added to Λ, a fifth input appears: the roots of real part below 3.
  - The gap and the count then move with h, so the bound cannot carry over unchanged.
- **Replacement, thm:tr-transfer (iii).**
  - Hypotheses: h ∈ [h_m, 10⁻⁶) ∖ 𝖩, the parameter point is admissible, and (R_h) holds. (R_h) says that no root of P_l with hκ > 70 has real part in [2, 3 + ε_Υ).
  - Conclusion: for any 0 < ε_K < ε_+ < min(μ(h), 10⁻¹³), the bounds of prop:uc-dependence hold with:
    - N̄_Λ = max(N̄(h), N₁), where N₁ secures P-UB2's inequality 4k̄_max + 24 > I_base + 22,119;
    - k̄_0 = 3, J_* = 15,000,015, l_* = 50.
- **The three conditions this rests on are explicit, and none is decided away from h = 10⁻⁶.**
  - Admissibility: not decided at any h.
  - (R_h): proved only at h = 10⁻⁶, by cor:t49-right.
  - μ(h): evaluated only at h = 10⁻⁶ (μ_Z). Elsewhere only 0 < μ(h) ≤ μ_G is proved.
- **What would be needed** to get a uniform upper bound on a range of h:
  - (R_h) on that range;
  - a lower bound for μ(h) there. prop:tr-mu-small rules this out on any interval reaching down to h_μ.

## The first reading (R-P-TR)

Every finding is resolved in the current file:

- M1 (the b ≥ 56 step) is kept, and now strengthened by the ϱ-disc result.
- m1–m10 and nits 1–15 were applied in the last round and still hold.
- m9 needed one more change: placement texts 3 and 4 had used symbols not defined where they land, and now define them inline.
- The old sentence on what the lower bounds use (nit 12) is replaced by the new proof of (ii).

## Placement

- **Against chapter 71 after P-UB1/P-UB2:** items 1 (insertion before sec:ec-linear), 2 (the opening, after M1) and 4 (rem:ec-lb-unbounded, after L3). The file says so.
- **Against HEAD 8d583306:** items 3 and 8 (P-UB1/P-UB2 leave those lines as they are), 5 (chapter 3), 6 (chapter 90) and 7 (chapter 33).
- Every old text occurs exactly once in the form stated.
- Crosswalk: 28 rows, pinned "paper/reader/proofs/P-TR.md@PENDING:N". The new labels are sec:tr-lambda, def:tr-excess, lem:tr-z3, prop:tr-lambda and prop:tr-mu-small.

## Checks

- **Scratch merge** of HEAD + P-UB1 + P-UB2 + P-TR:
  - `lint.py --chapters`: 0 hits;
  - `assemble.py --check`: 0 problems;
  - longest new line after label resolution: 121 characters.
- **The file:** lines are at most 121 characters, also after worst-case label expansion. No bad wrap starts, no backslash, lowercase labels, and no file or program names in the paper text.
- **New numbers:** every one was recomputed in /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/ptr/:
  - the convex-majorant endpoint values, by exact rationals;
  - the slope deviations and the integrals, by interval arithmetic.
