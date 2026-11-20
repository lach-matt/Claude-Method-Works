# R2-DB-b: second reading of P-U71-cstar.md and P-U71-forward.md after F-DB-b

Reader R2-DB-b. Scope: the fixes of F-DB-b for the 15 findings of R-DB-1. The baseline is d7580340 and the files are
read at HEAD f4eabee8. I read `proofs/P-U71-cstar.md` (527 lines) in full. In `proofs/P-U71-forward.md` I read the new
`cor:fwd-near-b0` and its proof in full, as new mathematics, together with the counted calculus it reuses
(lem:fwd-orders, lem:fwd-tame, prop:fwd-calculus, lem:fwd-derived, lem:fwd-box, lem:fwd-increments, the proof of
thm:fwd-loss). Against these I read the chapter results they rest on:

- sec:iii-h2-0 ((B1)–(B5) and the order of the choices), thm:iii-h2-2-1, thm:iii-h2-3-1, thm:iii-h2-4-1,
  cor:iii-h2-5-1, thm:iii-i-5-3, cor:iii-i-5-2 and lem:iii-i-3-6 (ch. 38);
- prop:ii-c-5-1 with its construction sec:ii-c-5-2, and def:ii-c-2-4 (ch. 24);
- lem:ii-f1-2-3, sec:ii-f1-3-1 and rem:ii-f1-7-1 (ch. 28), and thm:ii-e-6-1 (ch. 26);
- sec:iii-i8-1, lem:iii-i8-3-2 and prop:iii-i8-4-1 (ch. 40), and thm:iii-i11-4-1 and thm:iii-i12-3-1 Step 6 (ch. 41);
- Steps 3–4 of thm:iii-i14-3-1 (ch. 42), prop:iii-i15-2-5 and lem:s25-p6 (ch. 44), lem:iii-a-1-4 (ch. 30),
  lem:iii-i11-2-1 (ch. 41) and prop:iii-g4-4-4 Step 1.1 (ch. 36).

Nothing in the repository was changed. Every integer was redone in exact Python integers and fractions, under
`.../scratchpad/reader/scratch/r2_db_b/`.

**Verdicts.**

- **P-U71-cstar.md: NOT CONFIRMED: 0 Major, 1 minor, 1 nit.** The one minor is finding 1 below. It is a false "="
  that the fix of R-DB-1 finding 7 introduced (copied from R-DB-1's own proposed text). The bound it states holds.
- **P-U71-forward.md: CONFIRMED (0 Major, 0 minor; 2 nits).**

**The integer bound on d stands:** d_acc, d_NM ≤ D_acc < 1.57157·10⁵⁰ and N_NM ≤ 21D_acc + 6 < 3.30029·10⁵¹. Both
Majors of R-DB-1 are closed, and no printed integer moves.

---

## Findings

### 1. minor: a false equality in the bound for thm:iii-i12-3-1 (cstar l. 475)

*Evidence.*

- Line 475 reads "so [[thm:iii-i12-3-1]] is charged at most C_lev − 11 + I_lev + X_12 = T_12".
- Line 422 defines T_12 := C_lev + I_lev + X_12, so the left side is T_12 − 11, not T_12. This was checked exactly:
  T_12 − (C_lev − 11 + I_lev + X_12) = 11.
- The original text had "≤ T_12". The "=" comes from R-DB-1's proposed replacement for finding 7, which the writer
  copied verbatim. (The 11 of slack mirrors T_11, whose C_lev also stands for C_lev − 11 plus the 11 of the sources.)

The bound "charged at most T_12" is true, and nothing downstream changes.

*Fix.* Replace "C_lev − 11 + I_lev + X_12 = T_12." by "C_lev − 11 + I_lev + X_12 < T_12." (same line length, 118).

### 2. nit: the order of (B4) is a free choice that def:cs-choices does not list (cstar l. 51–74, 151–154)

thm:uc-integer is stated "with the choices of def:uc-choice and def:cs-choices". The value d = 20,180 at every b rests
on one more choice: the forward problem's order 𝗌, with s_in = 11 and s_out = −10. lem:cs-elem (e) fixes it only in
passing ("the order of (B4) of [[sec:iii-h2-0]] being that of [[lem:fwd-orders]]"), and cor:fwd-near-b0 takes it as a
hypothesis. thm:fwd-loss makes the same choice implicitly at b₀.

*Fix (optional).* Add to def:cs-choices:

> (h) as the order 𝗌 of the proof of [[thm:iii-i-5-3]] and of (B4) of [[sec:iii-h2-0]], the order of
> [[lem:fwd-orders]] (s_in = 11, s_out = −10).

and to the justification:

> (h): [[lem:fwd-orders]] carries out the construction of [[sec:ii-c-5-2]] with these values, and B_1 is chosen after
> the order ([[sec:iii-h2-0]]), so (B4) holds for it on B̄_1.

Then lem:cs-elem (e) may cite "[[def:cs-choices]] (h)".

### 3. nit: "are no sites" (forward l. 847)

*Fix:* "are not sites".

### 4. nit: the last sentence of cor:fwd-near-b0 is loose for the backgrounds other than h (forward l. 806–808)

"the forward solution operators of [[lem:iii-j2-2-1]] (a) satisfy [[eq:iii-i-5-2]] with d = 20,180". For
h̃ = h + h^(−1)(S), h + h_tot(p⃗) and h + h_rem(q) + h_tot(p⃗), lem:iii-j2-2-1 (a) gives eq:iii-i-5-2 with ‖β‖ (or ‖h̃‖)
in place of ‖h‖, and with the d of the proof of thm:iii-i-5-3 or cor:iii-h2-5-1. That d is 20,180, so the claim is
right, and lem:cs-elem (e) states it precisely.

*Fix (optional):* "satisfy [[eq:iii-i-5-2]], in the form of [[lem:iii-j2-2-1]] (a), with d = 20,180."

---

## The checks of the brief

### 1. Major 1 (def:cs-choices (f)): resolved

- **Admissible for thm:iii-i11-4-1.** Its proof (ch. 41 l. 966) says "Fix an admissible α′ ∈ (2, 3)". Its background
  has a_K ≥ 4 + ε_K "by (H2)", so the admissible levels of sec:iii-i8-1, defined in (2, min(a_K, 3)) = (2, 3), are
  (2, 3) minus a finite set. (2, 2 + ε_g − 2ε) is non-empty, as ε ≤ 10⁻³ε_g, so it contains admissible levels.
- **The level step of the base.** prop:iii-i8-4-1 at α′ asks α_0 ∈ (2, min(a_K, 2 + ε_g, 5/2)) and steps below
  a_K − 2. Both hold for α_0 ∈ (2, α′): α′ < 2 + ε_g and α′ − α_0 < ε_g < 1 < a_K − 2. The one step has ℳ′ = ∅, since
  ℳ_(α′) = ∅ (Re λ − 1 ≥ λ_♯ − 1 > ½ > α′ − 2). So item (6) is charged at most 11 + 0 + 497 = 508, as in Step 1.
- **Uses of α′.** α′ enters thm:iii-i11-4-1 only:
  - as an admissible level (𝒫_(α′), 𝒩′, ℳ_(α′); "none has rate α′ − 2, by admissibility");
  - through w_0 = min(α′ − 2, λ_♯ − 1) > 0 with w_0 + a_K > α;
  - through the bound of ‖·‖_(w_0) by ‖·‖_(α′).

  thm:iii-i12-3-1 uses it only through w_(α′) = min(α′ − 2, λ_♯ − 1) > 0 in Step 6, the level "fixed in the proof of
  thm:iii-i11-4-1". prop:iii-i13-2-4 uses "prop:iii-i8-4-1 at a level α′ ∈ (2, 3)" with the class 𝒴^♮(α′) ⊂ 𝒴(α′),
  for every α′. The other α′ of ch. 41 (lem:iii-i11-3-3, lem:iii-i13-2-3) are separate levels in continuity proofs,
  which are not charged. lem:ec-counts (b)–(c) count rounds by the level β, not by the weight w_0, and
  lem:iii-i11-3-2's Step 0 needs only w_0 + a_K > α. So the restriction costs nothing.
- **Rotating b.** ch. 41 (after the proof of thm:iii-i11-4-1) says "At a base point with black hole parameter
  b ∈ ℬ̄_*, the elimination is [[prop:iii-i15-2-5]] with q = 0". Its Steps 0–1 are those of thm:iii-i14-3-1 at b, with
  base prop:iii-i8-4-1 at α_1 (ch. 44, "*The motion coordinates*"). This is correct.
- **No transition-face round.** In lem:iii-i8-3-2 at the target level α′, Step 3.4′ has i_0 = 0 exactly when
  τ_0 = 2 + ε_g − 2ε > α′ − ε′ (ch. 40, "i_0 = 0 if τ_0 > α − ε′"). This holds, as α′ < τ_0. The same step's
  lem:iii-i2-4-2 condition β_tf − β_zf = ε_g − 2ε − (α′ − 2) + ε′ ∈ (0, 1) holds too. lem:cs-iterations (b) charges no
  transition-face round, and none occurs. The Step 4′ text of lem:cs-rest says this correctly.

### 2. Major 2 (cor:fwd-near-b0): resolved; the corollary and its proof are correct

- **Statement.** With the order 𝗌 of (B4) taken as that of lem:fwd-orders:
  - thm:iii-h2-4-1 (margin 1) has d = 20,104 + 49 + 10 + 11 + 1 = 20,175 on B̄_1;
  - cor:iii-h2-5-1 has d = 20,175 + 5 = 20,180 on B̄_* ⊃ ℬ̄_*.

  Both sums were checked. Stating cor:iii-h2-5-1 on B̄_* rather than B_* is justified in the proof, as (B5) is a
  condition on B̄_* ⊂ B_1. A larger d serves trivially: the norms are monotone in d, and the hypotheses only strengthen.
  So fixing d = 20,175 before B_* is chosen by (B5) is consistent with the order of the choices in sec:iii-h2-0.
- **The formula.** By eq:ii-f1-3-3, rem:ii-f1-7-1 and the proof of thm:iii-h2-4-1, the d at b is
  D_0 + D_1 + d′ + d″ + d̄_ℵ for P_0 = 2L_b.
  - D_0 and D_1 come from input (i) and lem:ii-f1-2-8.
  - d′ and d″ come from input (iii), the orders fixed by (B4).
  - d̄_ℵ = 1 comes from input (v), via thm:iii-h2-2-1 (margin 1).
  - Inputs (ii) and (iv) affect ε_0 and the constants only. thm:ii-f-8-1 for the smooth 2L_b is not a site.
- **(1) The orders.**
  - (B4) reuses the order built for 2L_(b₀), "admissible for 2L_b with the same weights and margin". This is
    prop:ii-c-5-1 (4): the thresholds move by less than 1, and the "+1" margins of the choice of s_in, s_out absorb
    that. Lem:fwd-orders has slack 1/4 and 27/8 over those margins.
  - So inf 𝗌 = −10, sup 𝗌 = 11, d′ = 10 and d″ = 11 (eq:fwd-dprime), with 𝗌_0 = 𝗌 − 3, s_u = −12 and N′ = 13.
  - The constant values at the ∂K⁺ and ℐ⁺ radial sets are those at b₀. The sets are given in the model fibre
    coordinates of sec:ii-c-5-2 ("Values") and def:ii-b-7-1, and 𝗌 is one function.
  - At the horizon and at Γ_b, def:ii-c-2-4 (3) for 2L_b makes 𝗌 constant on {r ≤ r_Γ}, with r_Γ > r_h(b) and
    Γ_b ⊂ T*{r < r_Γ}. The value is s_in = 11, as that set meets Ω_♮ of lem:ii-f1-2-3 (r_0 − 2δ_0 < r_Γ).
  - So the constant orders (12, 8), (11, 8) and (−10, −13) of lem:fwd-tame (iii) and lem:fwd-box are those at b₀.
- **(2) The cited results.**
  - D_1 = 49: every d in lem:fwd-tame is a closed form eq:fwd-dtilde of the orders, N and 𝔩. P_0 does not enter.
  - D_0 ≤ 𝔐(100) + 4 = 20,104:
    - prop:fwd-calculus and lem:fwd-derived involve no operator;
    - thm:ii-e-6-1 states that its "d_0 depends only on 𝗌_0 and 𝗌", uniformly over the stationary models of nearby
      parameters;
    - the sites of lem:fwd-box run at b in the same pattern and at the same parameters: (R) at the radial sets of
      2L_b, (Γ) at Γ_b, which is normally hyperbolic by (B1) and strongly trapping admissible by prop:iii-h2-1-1, and
      the others at the orders of (1) with N′ = 13 and m = 2. So their symbol and Sobolev orders, N and the number of
      quantizations are those at b₀, and the box conditions hold;
    - the increments of lem:fwd-increments are structural: the C^(d_0−j) symbol classes, ϕ^u and ϕ^s of
      prop:ii-c1-3-4, h̃_F of lem:ii-e-3-1, the flow box and d_0 ≥ d_1 + 2;
    - thm:iii-h2-3-1 (with sec:ii-f-6 run at 2L_(b₀)) and thm:iii-h2-2-1 use 2L_b as a smooth operator only, as
      lem:fwd-box says at b₀ for sec:ii-f-6–sec:ii-f-8.
- **(3) The +1 and the +5.**
  - d̄_ℵ = 1 is thm:iii-h2-2-1.
  - The +5 is cor:iii-i-5-2 at P_0 = 2L_b (class ((0;k−5),·)): two b-derivatives plus three of Sobolev embedding, as
    in the tame form of the proof of thm:iii-i-5-3.
  - With reference metric g_b, δ_0 = g_(b₀,b,−S) − g_b has every seminorm O(|b − b₀| + |S|) (lem:iii-i-3-6). So the
    extra term C_k(|b − b₀| + |S|)‖f‖_(H^d) is at most C_k‖f‖_(H^(k+d)), and eq:iii-i-5-2 holds with d = 20,180 at b.
- lem:cs-elem (e) now cites the corollary correctly, and keeps the +3 of ‖q‖_(𝒬^(m+3)), so 20,183.
- Steps 0 and 1 of c_0, and the base inside T_11, are now bounded at every b ∈ ℬ̄_* and for ℛ(U). The base point
  Ψ(U) has the b of Φ(U).

### 3. Minors 3–9, nits 11–15 and the cstar part of finding 10: all applied as proposed

| R-DB-1 | Where (cstar, new lines) | Check |
|---|---|---|
| 3 | l. 29–50 | max(A_M, A_ℓ, A_M + 11) = max(A_ℓ, A_M + 11). In the particular case the applications giving ℓ_i are among M's, so A_ℓ ≤ A_M and the bound is A_M + 11. The paragraph after it now names the identity (linearity and uniqueness of forward solutions) and the coefficient functionals. Correct. |
| 4 | l. 62, 82–84, 209–211, 225–228 | N = 21/4 ∉ ℕ, as prop:ii-g1-3-5 asks (ch. 29 l. 885). β′ = max(N, N − (3/2 − 2ε)) = 21/4; ⌈19/4⌉ = 5; ℓ_3 = 1 + 5 = 6; ⌈19/4 + ε⌉ = 5; ℓ = 12 + 4 + 3 = 19, giving 20 and 30. The charges 5, 5, 6, 20, 30 are unchanged. Targets 3 + η_2 and α − ε < 5 are below 21/4. lem:cs-transforms (b)'s "at most 5 when β_K ≤ 5" does not cover β_K = 21/4, but (e) computes the ceiling directly. Correct. |
| 5 | l. 146–149 | E^ν(W) is as printed in lem:s25-p6 and eq:s21-rows-at-b: L_(h,p⃗) and δ*_(g_0,E_C) applied to fixed sections, linear in W. Charged 11 by the proof of prop:uc-dbg. Correct. |
| 6 | l. 73–74, 92–93, 170–175 | lem:iii-a-1-4's proof: γ := min(β, α + 1), decreased only to avoid Re(spec_b(A) ∪ π₁F) (finite in strips), then α := γ − δ′. A non-final step raises the weight by 1 − dec − δ′ ≥ ¾. From q − 2 > 0, the fourth step starts above 9/4 and reaches q′ − 2 ≤ 3. At most 4 steps, so 8 + 1 = 9. Choice (g) is justified. |
| 7 | l. 473–476 | The largest-part rule gives 4k̄_max + 9 < X_12. **But "= T_12" is false: finding 1.** |
| 8 | l. 11–12, 452–457, 519–521 | G̃_0 := G̃ − Σ_(𝒩_rot) f^ν(W′_ν) with G̃ = F − Δ_q(p⃗′) − R_q u (ch. 42, Step 4′, and the definition repeated in prop:iii-i15-2-5). It is affine in W⃗′^rot on 𝒫_K, and thm:iii-i11-4-1 and thm:iii-i12-3-1 are linear in F. "Whose bound counts three runs" is applied in both places. Correct. |
| 9 | l. 518–519 | Bound − 6N_ι = 17,389,163,815,025,421,596,157,103,783 < 1.74·10²⁸. C_* − 6N_ι = 3,628,919,841,642,544,595,212,800,000,024 < 3.63·10³⁰. Correct. |
| 10 (cstar) | l. 10–11 | C_lev = 2N_ι + N̄_Λ + 529, matching lem:cs-levels (b) and close. Correct. |
| 11 | l. 286–289 | See the judgement below. |
| 12 | l. 301 | "have −μ ≥ ε_ind > ε_K by [[eq:iii-f1-2-2]]". Correct. |
| 13 | l. 103, 129–130 | lem:iii-a-3-3 removed from (a) and from its proof. It is cited nowhere else in the file. Correct. |
| 14 | l. 225–226 | Correct. |
| 15 | l. 342–343 | eq:iii-i6-2-8 and the row term of Step 3.5 (charge 0) added. Correct. |

**The writer's departure in nit 11: right, accept.** Step 1.1 of the proof of prop:iii-g4-4-4 (ch. 36) says
|σ|^(α−2)l_(2−α)(|σ|)G^exc_(s1) "has the tf-exponents 2 and α" (with their ℰ_ind-shifts). So after the factor σ^j,
both 2 + j and α_0 + j occur, and R-DB-1's proposed text omitted the second. All have real part at least 1:

- Re(2 + j) ≥ 3;
- Re(α_0 + j) ≥ Re α_0 + 1 > 2;
- Re(α_0 − 2 + j) ≥ 1, at level 1 with j = 1 and Re α_0 ≥ 2, and at level 2 with j = 2 and Re α_0 ≥ 1 + η_1.

So n_ι = 0 stands. (α_0 + j also lies in α_0 − 2 + j + ℰ_ind, as (2, 0) ∈ ℰ_ind by Step 1.2. Listing it is accurate and
harmless.)

### 4. Integers (exact)

- k̄_max = 12,811,621,665,714,434,999,187.
- N_ι = 107,279,395,180,026,392,909,234,131,199,999,996.
- C_lev = 214,558,790,360,052,785,818,485,009,600,000,520 (eq:cs-clev).
- The step sums 497, 529, 466, 469, 43, 48, 508 and 1,914.
- I_lev = 34,268,829,852 and I_base = 1,435,970,471,299,470,574,962.
- d_Φ ≤ 1,038,326,399,999,940.
- (N̄_Λ + 2)(d_Φ + 30) = 17,389,059,886,080,535,910,399,999,970 < 1.739·10²⁸.
- The seven-number sum is 17,389,163,815,025,371,354,557,103,786, with 3·529 = 1,587 and 2·20,183 + 2·1,914 + 33 =
  44,227.
- The bound for c_* is 643,676,388,469,322,172,480,826,383,357,103,759. It equals the right side of eq:cs-c0 computed
  directly from T_11 and T_12, and C_* − bound = 3,611,530,677,827,519,173,616,642,896,241 ≈ 3.61·10³⁰.
- 6N_ι = 643,676,371,080,158,357,455,404,787,199,999,976 and 3N̄_Λ = 50,241,599,999,997.
- rem:cs-sharpness: D_e + K·C_lev + 469N_b + 466(N_b + 1) + C_* = 2.61927·10⁴⁹ < 2.62·10⁴⁹.
- D_acc = 157,156,403,040,000,000,000,000,001,258,700,000,000,000,000,000,000 < 1.57157·10⁵⁰, with
  M_c C_* = 244,153 · 64,368 · 10⁴⁰.
- 21D_acc + 6 = 3,300,284,463,840,000,000,000,000,026,432,700,000,000,000,000,000,006 < 3.30029·10⁵¹.

All match the printed values of cstar and of thm:uc-integer.

**Close's citations of cstar keys match what cstar now states:**

- prop:cs-cstar: l. 17, 519, 536;
- def:cs-choices: l. 516, 570;
- eq:cs-clev and lem:cs-levels (b), with "c(β) ≤ 2N_ι + N̄_Λ + 529 = C_lev": l. 530, 547;
- lem:cs-base and lem:cs-rest: l. 568–569;
- lem:cs-transforms, with s_c = 3, ϑ_in = 0 and ϑ_ℋ < 9/4: l. 571;
- lem:cs-fourier, with n_K ≤ N_ι + N_Λ: l. 572;
- rem:cs-sharpness: l. 574.

rem:uc-missing names, among the choices of def:cs-choices, only those at which closed forms are evaluated. That stays
accurate with (f) and (g) added. The assembly's three citations of prop:cs-cstar (l. 610, 614, 629) also match.

### 5. The five assembly sentences (P-U71-assembly.md; current line numbers in brackets)

Each is right. Texts 1, 3, 4 and 5 are needed: the loss they describe is used at every base point, and at b ≠ b₀ the
forward operators are those of cor:iii-h2-5-1. Text 2 is right but not needed. lem:iii-j2-2-1 (a) already takes the
forward operators from cor:iii-h2-5-1, whose d does not depend on b, and Ψ(U) has the b of Φ(U). It is harmless; accept
it at the coordinator's discretion. The texts I accept, with wraps that keep every line within 121 characters:

1. **[l. 138–139] thm:loss-d (i).** Old: "operators, which is at most 20,180 ([[thm:fwd-loss]]);". New (113 characters):

   > operators, which is at most 20,180 at every base point ([[thm:fwd-loss]] at b₀, [[cor:fwd-near-b0]] at b ∈ ℬ̄_*);

2. **[l. 169] (optional).** Old: "on the base point ([[lem:iii-j2-2-1]]: only its constants do). By [[def:ec-accounted-loss]], a
   further summand does". New:

   > on the base point ([[lem:iii-j2-2-1]]: only its constants do; for the forward solution operators this is
   > [[cor:fwd-near-b0]]). By [[def:ec-accounted-loss]], a further summand does not lower the largest of the losses of a

   Rewrap the following lines of the paragraph.

3. **[l. 172–173].** Old: "[[def:ec-accounted-loss]] with [[lem:ec-closed-forms]], [[rem:ec-other-losses]],
   [[lem:ec-round-loss]] and [[thm:fwd-loss]]." New:

   > [[def:ec-accounted-loss]] with [[lem:ec-closed-forms]], [[rem:ec-other-losses]], [[lem:ec-round-loss]],
   > [[thm:fwd-loss]] and [[cor:fwd-near-b0]].

4. **[l. 259–260], the split-loss paragraph.** Old: "d_F the loss d of [[thm:iii-i-5-3]] ([[eq:iii-i-5-2]]), at most
   20,180 ([[thm:fwd-loss]])". New:

   > d_F the loss d of [[thm:iii-i-5-3]] and of [[cor:iii-h2-5-1]] ([[eq:iii-i-5-2]]), at most 20,180 ([[thm:fwd-loss]],
   > [[cor:fwd-near-b0]])

   Rewrap the paragraph from l. 259.

5. **[l. 624] rem:ec-upper-open (3).** Old: "forward loss, at most 20,180 ([[thm:fwd-loss]]), charged at each forward
   solution they apply;". New (114 characters), with the rest of the paragraph rewrapped:

   > forward loss, at most 20,180 ([[thm:fwd-loss]], [[cor:fwd-near-b0]]), charged at each forward solution they apply;

No other sentence of the assembly, close or the chapters cites thm:fwd-loss. ch. 71 still carries its older text
("raises by 6", "No upper bound for d is proved"), which R-DB-1 reported to the coordinator.

*A side observation on the paragraph of text 4 (outside this scope; not counted).* With ‖β‖_k := ‖h‖_(𝒳^k) + |p⃗| +
‖q‖_(𝒬^k) (ch. 43 l. 79), the forward operators with h̃ = h + h_rem(q) + h_tot(p⃗) have split loss (d_F; d_F + 3, d_F),
by the bound used in lem:cs-elem (e). So "every family other than the background terms has c, b ≤ a" (assembly
l. 266) is not exact for them. lem:ec-split-loss (d) with X = (d_BG − 2)_+ = 9 ≥ 3 still gives the conclusion, and
cstar charges 20,183 in full, so nothing changes.

### 6. Contract

- `python3 lint.py proofs/P-U71-cstar.md proofs/P-U71-forward.md`: 594 hits. All are "reference to undefined label"
  across files, and every one of the 282 references of the two files resolves in chapters/ or proofs/.
- Lines: the maximum is 121 characters in both files (code points, as lint counts them).
- No wrapped line starts with "+ ", "- ", "* ", "> ", "#", "=" or "|".
- The 23 + 36 labels are lowercase and unique across chapters/ and proofs/, cor:fwd-near-b0 included.
- No `[[pending:` marker, and no process or program words in the added text. "computed" in "quantizations computed from
  them" is mathematical, and lint does not flag it.

**Verdicts.**

- P-U71-cstar.md: **NOT CONFIRMED: 0 Major, 1 minor (finding 1), 1 nit (2).**
- P-U71-forward.md: **CONFIRMED (0 Major, 0 minor; nits 3, 4).**

The integer bound d_acc, d_NM ≤ D_acc < 1.57157·10⁵⁰, N_NM < 3.30029·10⁵¹ stands.
