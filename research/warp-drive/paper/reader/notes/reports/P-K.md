# P-K: an explicit bound for the data order K (G-SWEEP §4, V1)

**Output.** `research/warp-drive/paper/reader/proofs/P-K.md`. It has 452 lines, md5 6c7eb17393ce45f0f67b0d52cbd36773.
It contains:
- the new section `sec:uc-data-order`, for chapter 71, with `lem:uc-data-losses` (full proof), `prop:uc-data-order`
  (full proof), the displays `eq:uc-data-order` and `eq:uc-kstar-own`, and `rem:uc-data-order-limits`;
- a Placement section with ten items: the insertion point and nine exact old/new texts, covering chapters 71, 03, 46,
  63 and 90;
- crosswalk rows.

No chapter, crosswalk, appendix or bibliography file was edited.

## Result in one line

K = d_1 + 14 = **22d + 305 + L_P**, where:
- d is the Nash–Moser loss of thm:iii-k-3-2 (ch. 71's d_NM);
- L_P = L_0 + 2J ≤ 43 is an explicit number of derivatives (L_0 ≤ 23 from Step 1 and J ≤ 10 from Step 2 of
  thm:iii-c1-3-1).

So K ≤ 22d + 348. At the computational point J ≤ 8, so K ≤ 22d + 344 ≤ 22·D_acc + 344
= 3,457,440,866,880,000,000,000,000,027,691,400,000,000,000,000,000,344 **< 3.45745·10⁵¹**. This lies outside the proved
set, just as d does (rem:ec-point-outside).

## 1. Every order traced

**d_1 := max(d_0, N_NM + k″) and k″ := d + 3 + k′_(N_NM+d+3)** (46:1603, 46 Smallness).
- N_NM = 21d + 6, with d the d of thm:iii-k-3-2, that is ch. 71's d_NM.
- The "+3" is the order shift of Θ_j in eq:s27-theta: lem:ii-g-4-1 (2)–(3) with d = 3 reads one factor at order k + 3,
  and (3) bounds at order k + 2 ⇒ H^(j+5).
- So N_NM + k″ = 22d + 9 + k′_(22d+9).

**d_0** (prop:iii-k-1-2: the largest regularity asked by thm:iii-c2-3-1 with thm:iii-c1-3-1, by thm:iv3-2-2 and by
(N)) = **309**.
- thm:iii-c2-3-1 asks k₂ = 2·153 + 2 = 308 on the gauged data (45:1735). prop:iii-c2-4-1 costs 1, giving 309.
- thm:iv3-2-2 asks N_ex = 153 on the pulled-back data. The pull-back costs 2 and the forward/exterior solution costs
  132, giving 287 on h̊ and 288 on (γ̃, k̃).
- (N) asks r_0 = 4, that is H^5 × H^4.
- d_0 is irrelevant to K, since 22d + 9 + k′ > 309.

**k′_k** (prop:iii-k-1-2 (3); its proof says only "k′_k collects the losses up to the order k + 2").

The count gives **a constant: k′_k = 282 + L_P for every k**, so the data order is k + 282 + L_P. The losses are below.
"Order n controls order m" means a modulus: small at n ⇒ small at m, uniformly in |S| + |S⁰| ≤ σ_0.

| step | loss | where |
|---|---|---|
| (γ̃,k̃) → gauged data (h̊_0, h̊_1) in ℬ_Σ | 1 | proof of prop:iii-c2-4-1: h̊_1 is algebraic in k̃ and ∂γ̃ |
| forward solution on 𝒟⁺ / exterior, class 𝒜 = H^(·,ℓ^♭_0,(−,ℓ^♭_I)) | a = 132 (data 153 + k → solution 21 + k) | last clauses of thm:iv3-2-2, thm:iv2-3-1 |
| backward solution on 𝔒⁻ | 0 (H^(r+1)×H^r → H^(r+1)) | (N) of sec:s27-local |
| Step 1, expansion at I₀ (≤ 3 steps; per step p + 6, with p the number of factors of R) | L_0 ≤ 7+8+8 = 23 (½ class 8+10+10 = 28) | proof of thm:iii-c1-3-1 Step 1, cor:iv3-2-3 |
| Step 2, expansion at ℐ⁺ (J repetitions, 2 each) | 2J, J ≤ 4(ℓ_I − ℓ^♭_I) + 1 | Step 2; lem:iii-a-1-2 and lem:iii-a-3-2 lose 0 |
| pull-back data of (S,S⁰), l parameter derivatives | 2 + l in 𝒜; 4 + l in ℬ (Taylor re-expansion at I₀ costs 2) | proof of thm:iii-c2-3-1, lem:s27-translated-exterior |
| ∂h (linearised equation, thm:iv3-2-1, tame eq:iv2-2-3) | needs h at n + 7, F₁ at n + 4 (h at n + 6), data at n + 4 | proof of prop:iii-k-1-2 (3) |
| ∂²h | needs ∂h at n + 6 and h at n + 7 | same |

The per-step loss p + 6 in Step 1 breaks down as:
- loss 4 of the linear estimate (eq:iii-c1-2-2 / eq:iv2-2-3 at h = 0);
- p for R;
- 2 for the quadratic term Lh = −∫(L_s − L)h, from the coefficients in h and its two derivatives (prop:iii-c-4-4,
  lem:iii-c-2-1).

The data of Rh need the jet of order p + 1 on Σ^IVP, that is data at order j + p + 5.

The binding chain is the tame term of thm:iv3-2-1:
- the triple at 𝒜-order n needs h_(S,S⁰) at n + 13;
- that needs the pulled-back data at n + 13 + 132;
- that needs h_0 at n + 15 + 132;
- that needs h̊ at n + 15 + 264;
- that needs (γ̃, k̃) at **n + 280**.

Steps 1–2 need the triple in 𝒜 at n = m + L_P. The data route through ℬ needs only n + 6 + L_0 + 133 ≤ n + 167. At
m = k + 2 this gives k′_k = 282 + L_P.

Hence **d_1 = 22d + 291 + L_P**.

**The "+14"** (sec:vii-4, explicit, nothing to evaluate) is 5 + 5 + 4:
- k := d_1 + 5: cor:vii-2-3 reads the C^(d_1+3) norm through lem:vii-0-1, and eq:vii-2-2 gives C^(k−2) for K̂.
- J := k + 5: eq:vii-2-1 needs k + 4 derivatives of the data, and the data are first derivatives of g_λ.
- K := J + 4: lem:vii-1-1, C_Kλ^(K−j−3) ≤ C_Kλ.

The approximant then has N = K + 3 stages.

**thm:own-data** (½ class):
- d is the same as in the integer class. The Ω_* constructions see ℰ_0 only through ℰ^C_I and Λ, which are the same
  by prop:own-same-index-sets, and they see the data only through constants.
- L_0 ≤ 28, so L_P ≤ 48 and d_1^½ = 22d + 291 + L_P.
- k1 = d_1 + 4 and M = 2k1 + 17.
- s_R = (4k1 + 35)/(7 − 2a), and the first entry of eq:own-kstar dominates for k1 ≥ 8. All four comparison
  inequalities were checked by hand and are printed. So **K*(a,M,k1) = k1 + 4 + (4k1 + 35)(k1 + a)/(7 − 2a)**.
- K* exceeds d_1 + 14, and lies between k1 + 4 + (4k1+35)(k1+2)/3 and k1 + 4 + (4k1+35)(k1+3) for a ∈ (2, 3).
- The admissible K are the integers above K*, so **K grows quadratically in d_1**.

## 2. The bound (as stated in prop:uc-data-order)

In general:
- d_1 = 22d + 291 + L_P and K = 22d + 305 + L_P, with L_P ≤ 43, so K ≤ 22d + 348.
- ½ class: L_P ≤ 48.

At the computational point (def:ec-point, def:uc-choice, def:cs-choices), J ≤ 8, and:
- K ≤ 22D_acc + 344 < 3.45745·10⁵¹;
- d_1 ≤ 22D_acc + 330;
- N ≤ 22D_acc + 347;
- K < 5.7624·10⁵⁰ under prop:uc-d-small (b), and K < 1.15248·10⁵¹ under (c);
- K > 22d > 2.7493·10²⁵, by eq:uc-lower.

½ class at the computational point:
- k1 ≤ 22D_acc + 339;
- 1.0078·10⁵¹ < K* < 4.78156·10¹⁰³.

## 3. Numbers recomputed (exact Python integers and fractions, scratch only)

- ch. 71's own values were reproduced:
  - D_acc = 157,156,403,040,000,000,000,000,001,258,700,000,000,000,000,000,000;
  - 21D_acc + 6 = 3,300,284,463,840,000,000,000,000,026,432,700,000,000,000,000,000,006.
- 22D_acc = 3,457,440,866,880·10³⁹ + 27,691,400·10¹⁸, and adding 344 gives the integer above.
- 22D_b + 344 = 576,236,373,596,753,905,056,774,544,275,542,274,022,969,465,130,512, and 22D_c + 344 =
  1,152,472,747,193,488,928,860,161,230,669,285,595,982,373,216,297,590 (D_b and D_c as in prop:uc-d-small (b), (c)).
- ℓ^♭_0 = 30,099/20,000 and ℓ^♭_I = 60,099/40,000 at γ_Υ = e_Υ = 1/100.
- 4(7/2 − ℓ^♭_I) + 1 = 89,901/10,000 < 9, so J ≤ 8. In general the bound is < 11, so J ≤ 10.
- k̄ = 22D_acc + 339 = 3,457,440,866,880,000,000,000,000,027,691,400,000,000,000,000,000,339.
  - k̄ + 4 + (4k̄+35)(k̄+3) = 4k̄² + 48k̄ + 109 = 4.7815589391887…·10¹⁰³.
  - This is below 4.78156·10¹⁰³, checked with k̄ < 3.4574408669·10⁵¹ and k̄² < 11.95389735·10¹⁰².
- Lower bound for K*: (4/3)(22·1.2497·10²⁴)² = 1.00784939…·10⁵¹ > 1.0078·10⁵¹.
- The K* dominance inequalities 4k1² + 7k1 ≥ 146, 16k1² + 114k1 ≥ 79, and the others hold for k1 ≥ 8.
- The loss sums were checked: 7 + 8 + 8 = 23, 8 + 10 + 10 = 28, 2·132 + 16 = 280.

## 4. What is not closed

1. **d itself on the proved set.** K is now explicit *in d*. But d is evaluated only at the computational point,
   which is outside the set where thm:settling is proved (rem:ec-point-outside; S-INSIDE says d is unbounded there). So
   K on the proved set is "22d + 305 + L_P with d unevaluated", exactly as for d.
2. **L_0 and J are bounded, not fixed.** They depend on ℓ_0, ℓ_I and on the weights chosen in thm:iii-c1-3-1:
   - the lowerings of α₀, which P-K takes below 1/6 (a choice the proof's "slightly" allows, stated as a hypothesis of
     lem:uc-data-losses);
   - ν in Step 2.
3. **The count rests on the paper's existence statements, which it makes quantitative.** P-K adds counting arguments
   that the paper does not write out, and these should get a careful independent reading:
   - (a) the jet argument giving the data loss p + 1 in Step 1;
   - (b) the Taylor argument that pull-back costs 2 derivatives in the partially polyhomogeneous class (the paper only
     says pull-back "preserves" it);
   - (c) the loss 1 of prop:iii-c2-4-1 (the paper says only "continuous");
   - (d) the (S, S⁰)-derivative losses replacing "[Hin26, footnote 59]";
   - (e) the claim that d is the same in the ½ class.

   The memberships themselves (that ∂h lies in the class, and that F₁ lies in the forcing class) are the paper's own
   claims, used as stated (thm:iii-c2-3-1 (2), cor:iv3-2-3). P-K counts orders and does not reprove them.
4. **The count is an upper count.** Smaller orders may serve, for example by avoiding the tame term's +7.
5. **thm:own-data's stage count** K + 4 + ⌈4β0(k_P)⌉ involves β0(k_P) = max(2, 4C(k_P) + 1). The constants C(q) of
   eq:near-lines are not evaluated.
6. **Thresholds.** λ1, δ and λ_2 remain unevaluated (rem:ec-not-evaluated). Nothing here touches them, and
   prop:ec-delta-cap stands.

## 5. Checks

- My own checker (scratch) used the assembler's numbering read-only, with new labels resolved as "Proposition 49.999"
  etc.:
  - every line is ≤ 121 characters before and after resolution;
  - no wrapped line starts with "+ ", "- ", "* ", "> ", "#", "=" or "|";
  - no backslash, and label keys are lowercase.
- lint patterns: the only hits are the six crosswalk rows. They carry the source path `paper/reader/proofs/P-K.md:N`,
  as crosswalk sources must. There are no hits in the proof text.
- All nine old texts of the Placement section were verified to occur verbatim, exactly once, in the current chapters.
  The chapters are being edited concurrently (63 changed during this work), so the coordinator should re-verify before
  merging.
- `python3 assemble.py --check`: labels 4591, problems 0. I made no chapter edits. git shows chapters 21, 22, 23, 33,
  95 and 98 modified by concurrent work, not by me.
- A coordinator snapshot (d08d1369) committed an in-progress copy of `proofs/P-K.md`. The working copy is the final one.
  Nothing was committed by me.
