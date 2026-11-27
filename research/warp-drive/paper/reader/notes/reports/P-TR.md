# Report P-TR: conditional transfer in h of the upper bound on d

Output: `research/warp-drive/paper/reader/proofs/P-TR.md` (701 lines). It holds the new section sec:tr (23 labels, all
with the prefix `tr-`), a Placement section (8 items) and 23 crosswalk rows. No chapter or crosswalk file was edited.
Scratch work is in `/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/ptr/`.

## Headline

The planned theorem ("if (1/100, 1/100) is admissible, the bounds of thm:uc-integer hold at every
h ∈ 𝖧 ∩ [h₁, 10⁻⁶)") is **false as planned**. It holds only off an exceptional set 𝖩, and 𝖩 cannot be dropped:

- As h moves, the roots of the □^C polynomials of real part ≥ 5/2 cross the integers 3–51. This happens for ι_B ≈ 2 + x
  and for Re ι_P ≈ a(x) at x = hκ ≈ n − 2 and x ≈ (4n − 10)/3, and for the vector root ι_v exactly at
  h = (n − 3)/((l+1)² − (n−1)²).
- Each family crosses at finitely many h per degree, but there are of the order of 10⁸ crossings in [h₁, 10⁻⁶].
- Near each crossing, ε_ind(h) → 0. Then lem:ec-lb-rounds with Θ_g := ε_ind(h) gives d_acc ≥ 3R > 3(1 − 2.1·10⁻⁸)/ε_ind(h)².
  This exceeds D_acc once ε_ind(h) < 1.38·10⁻²⁵, for **every** admissible choice of the weights. So the upper bound
  itself fails there, not just the proof (prop:tr-fail).
- Explicit example: h_c = 1/1001992 ≈ 9.98·10⁻⁷, where ι_v(1000, h_c) = 4. For 0 < |h − h_c| < 1.377·10⁻³¹,
  ε_ind(h) < 1.38·10⁻²⁵.

**What is proved (thm:tr-transfer).** Let h₁ := 4.76·10⁻¹¹, and take h ∈ 𝖧 with h₁ ≤ h < 10⁻⁶ and h ∉ 𝖩. Assume
(γ_Υ, e_Υ) = (1/100, 1/100) meets the gauge conditions of thm:vi-c-2-1 at that h, for some γ_(Υ,H). Then every
statement of thm:uc-integer holds at (h, 1/100, 1/100) with the same numbers:

- D_acc < 1.57157·10⁵⁰;
- 21D_acc + 6 < 3.30029·10⁵¹;
- C_* = 6.4368·10³⁵;
- d_Ψ, d_FM ≤ 1,038,326,399,999,948;
- the finer bounds d_acc, d_R < 2.6193·10⁴⁹ and d_NM < 5.2386·10⁴⁹;
- the lower bounds 1.2497·10²⁴ and 2.624·10²⁵.

**The exceptional set.** 𝖩 is a finite union of intervals of total length < 1.698·10⁻¹¹, which is less than 1.7·10⁻⁵ of
[h₁, 10⁻⁶] (prop:tr-measure).

**Caveat, stated in rem:tr-scope.** The hypothesis may be empty:

- if h_* ≤ h₁, no h qualifies, and h_* = min(10⁻⁶, h_0, h_tf) is not determined;
- the admissibility of the gauge values 1/100 at h is not decided.

## h₁

- **The constraint.** h₁ is fixed by the root ι₂(h) of P_2 near 2. lem:ec-lb-ind, which is now merged into ch. 71,
  gives (40/13)h(1 − 5·10⁴h) < ι₂(h) − 2 < 40h/13.
- **Below the threshold.** For h ≤ 13ε_Υ/40 = 4.7512·10⁻¹¹, ι₂ violates the condition, so ε_ind(h) < ε_Υ = 1.4619·10⁻¹⁰
  and ε_g ≠ ε_Υ. The chain then changes: Δτ_0, T_<, T_>, I_lev and everything downstream.
- **The choice.** h₁ = 4.76·10⁻¹¹ is within 0.19 % of that threshold. At h₁,
  (40/13)h₁(1 − 5·10⁴h₁) = 1.4646·10⁻¹⁰ > ε_Υ.
- **Far below.** The verbatim chain is not re-run below h₁. For h ≤ 4.48·10⁻²⁶, thm:ec-lb-proved already puts d above
  D_acc.

## The four inputs, uniformly in h

**Method.** P_l is split as P_l = U + eF, with U = (2 + x − ι)𝒬. This is exactly lem:s14-sextic-split with ε₀ := e/h,
and F_k = ϖR_k, where ϖ := h/e ∈ (0, 0.1024]. Two parameters are used: x = hκ and y = eκ (y fixes the degree). There is
also an exact formula for ∂_hP_l at fixed l (eq:tr-dh); in it the 1/ϖ terms cancel.

**(a) ε_ind(h)** (prop:tr-eps).

- Off 𝖩, every h-dependent root with |ι − 1| ≤ 50 is at distance ≥ ε_Υ from ℤ (condition (H_ε)). Hence
  ε_Υ ≤ ε_ind(h) ≤ min(δ_50, ι₂(h) − 2) < min(δ_50, 40h/13).
- Root enclosures valid for every h ∈ (0, 10⁻⁶]:
  - **C:** 2 + 7·10⁻⁵ < ι₁ < 5/2.
  - **Vector type:** ι_v(2, h) − 3 ≥ 5h/(1 + 6h), with closed-form crossings and slope.
  - **l ≤ 122 (y ≤ 3/20):** three real roots, in (2 + 3.1h or ι₂, 2 + y), (2 + y, a) and (a, 3 − y/2).
  - **123 ≤ l ≤ 142:** ι_B ∈ (2 + x/2, 2.031), plus two roots with Re in (2.1, 2.92).
  - **l ≥ 143, x ≤ 70:** ι_B is within 1/100 of 2 + x, and ι_P is within ϱ = 1/20 (for x ≤ 20) or 1/5 of
    ζ = a + ib (b/10 when b ≥ 56).
  - **x ≥ 70:** no root with |ι − 1| ≤ 50.

**(b) □^C exponents of ℰ^ι_ind** (prop:tr-inputs (a)).

- They are ι + 1 + j with Re ι > 2, so they have real part > 3, and none is an integer under (H_ε).
- The logarithmic orders are ≤ 3 at Re ≤ 3/2 and ≤ 50 at Re ≤ 5. The general real-exponent bound of prop:is-logs (c)
  is used here. Its refinement "order ≤ 1 at ι + 1 + j" needs a distance > 1.34·10⁻⁶ from ℤ, is not available at
  general h, and is not needed.

**(c) Simplicity on [−101, 5]** (prop:tr-inputs (b)).

- From h ∉ 𝖹₁ (lem:iv4-1-3 (b)), plus (H_ε) for "no integer root".
- No coincidence with □^Υ entries of the same type: those lie in (1, 5] only at scalar l ≤ 2, where the □^C entries lie
  in (1, 2).

**(d) Poles at ι⁺** (prop:tr-inputs (c), (d)).

- The 𝒮_τ lists are recomputed at h, with "no integer differences" except {2, 4} and {3, 4}.
- So every pole of N_sf⁻¹ and N_ι⁺⁻¹ at Re ≤ 5 is simple, l_* = 50 and K_ι ≤ 2.
- The visibility equality spec_ι⁺ = 𝒫 (lem:sp-exceptional) is not shown on a countable set 𝖹_Q. No bound uses it, because
  N_ι⁺⁻¹ has pole order ≤ that of N_sf⁻¹ at every point.

## The chain

Every other input of thm:uc-integer is either gauge-only or holds for every γ_C:

- **Gauge-only:** gap sums, ε_Υ, Λ below 3 + ε_+, μ_G, N_Λ, k̄_0, J_*, η_0 = 𝔡₁.
- **Every γ_C:** the forward loss (lem:fwd-orders), ϑ_ℋ < 9/4, lem:ec-theta-in-zero, ℓ_tf = 1 and d_BG = 11.

With ε_ind(h) ≥ ε_Υ we have ε_g = ε_Υ, so Δτ_0, I_lev, C_lev, C_* and D′_* are unchanged and thm:uc-integer holds
verbatim.

## Numbers (all with outward rounding; scratch scripts reproduce them)

**Regime S (l ≤ 122).**

- F₁(2 + y)/y ≤ −15 + 1.652, and the h-part is ≤ 15.8·10⁻⁶.
- U(a) ≥ 0.0248 and |F(a)| ≤ 4.833.
- U(3 − y/2) ≤ −1.4466y and |F₁(3 − y/2)| ≤ 8ϖ + 13.89y.
- |F(2)| ≤ 9.326x and |∂_ιF| ≤ 15.64 near 2.

**Rouché for ι_B** (6 x-pieces, radius 1/100). The tightest piece is [55, 70]: 11.82 < 14.45. The x/2 circle gives
0.0025x < 0.194x.

**T-disc.** e|F| ≤ 8.87·10⁻⁵ < 5.81·10⁻³.

**Rouché for ι_P.**

- 23 boxes for b ≤ 56. The tightest box is [5, 20] × [16, 32]: 14.67 < 50.96.
- For b ≥ 56: e|F| ≤ 6.8·10⁻⁴b³ < 0.342b³.

**Far region.** e|F| < 0.0377x² < 0.001959x³.

**Slopes.**

- ∂_hι_B ≥ 0.98κ (worst ratio 0.9846).
- ∂_h Re ι_P ≥ (3/4 − 0.2923)κ > (2/5)κ.
- ∂_hι_v ≥ 0.99κ.

**Measure of 𝖩.** 0.02659ε_Υ (ι_B) + 0.06346ε_Υ (ι_P) + 0.02601ε_Υ (ι_v), by integral bounds on Σ_n 1/L_n, giving
< 0.1161ε_Υ = 1.697·10⁻¹¹.

**Independent numerical spot checks.** These used 40–50 digit roots over 6 values of h and about 34 degrees each:

- every location claim holds;
- the slopes at crossings are dι_B/dh ≈ κ and dRe ι_P/dh ≈ 0.75κ.

## Consistency with P-LB (merged into ch. 71 during this task)

- The chapters changed mid-task: lem:ec-lb-ind, lem:ec-lb-rounds, thm:ec-lb-proved, rem:ec-lb-unbounded and
  rem:s14-eps-ind-scope were added or updated. P-TR uses them:
  - ι₂ and its sign points come from lem:ec-lb-ind;
  - the failure bound comes from lem:ec-lb-rounds;
  - the small-h failure comes from thm:ec-lb-proved.
- All Placement Old texts were re-taken from the current chapters, and each was matched verbatim and uniquely.
- Placement item 6 (ch. 90) touches only line 78, so it does not collide with P-K's item on lines 72–73 (now 76–77).
- Item 7 (rem:s14-eps-ind-scope in ch. 33) is offered but flagged, because ch. 33 is being edited.
- Commits made by others during the task (snapshots c4214cb8 and 688cf319, and 2a4c9cd3) picked up P-TR.md. The working
  copy now equals HEAD. I made no commit.

## Not closed

1. **Whether the hypothesis is non-empty.** This needs h_* > h₁ and the gauge thresholds above 1/100; both are open
   (T2, T3, T5–T8 of S-INSIDE).
2. **The bound for h ∈ [h₁, 10⁻⁶) ∩ 𝖩 with ε_ind(h) ≥ ε_+.** It plausibly holds with modified integers, but this needs a
   re-run of the ε_g-dependent counts of sec:cs (I_lev, T_11, T_12, D′_*). Not done. The same applies to
   h ∈ [5.6·10⁻¹⁵, h₁), where ε_+ = 1.6416·10⁻¹⁴ is still allowed.
3. **𝖩 is described implicitly.** It is given by the root conditions with a measure bound; the individual crossing
   intervals are not listed, and they number about 10⁸. The largest 𝖩-free interval [h, 10⁻⁶) is not determined. Crossings
   occur within about 0.2 % below 10⁻⁶ (for example the vector crossing at 9.980·10⁻⁷).
4. **Visibility at h ∈ 𝖹_Q** (lem:sp-exceptional) is not decided. It is not needed for any bound.
5. **Style.** lint.py flags only the crosswalk rows (file locations, same convention as P-K) and the cross-file label
   references; my own check confirmed that all 60+ referenced labels exist. Line lengths are ≤ 121 after a conservative
   label resolution.
