# P-UB2: the upper bound of chapter 71 as a function of the admissible choice

Proof file for the coordinator. Nothing in chapters/, crosswalk/ or elsewhere in the repository was edited; this is the
only file written there. Every old text below is copied from the chapter files at HEAD ac31449d (equal to the
working tree for these files): 71-explicit-constants.md md5 427412e02c74261f1f87da24b60ddbca,
00-front.md fcb33a08a5d5df2ae599389726a59dba, 01-introduction.md 9cfc5f6bcd496e6d6100c3bf7ed88ffa,
03-theorems.md 4c4bc00c635267eef3f73f747efee2d0, 63-own-data.md 2bd560af0194b8699f05a6fc017404a6,
90-scope.md 8c96f1f3d84ffcc63831372a70b0a09a. Each old text occurs exactly once in its file as whole lines;
line numbers are of those files. Both sets of texts were merged with P-UB1's texts T1–T14 on a scratch copy made from
a git archive of HEAD and checked there, through the assembled paper (section 7).

The numbers in the drafted texts are evaluated at **the proved inputs of P-UB1** (proofs/P-UB1.md, md5
a4e10a41efcf0b396490ffad095af7dd):
ε_K = 1.6747·10⁻¹⁷, ε_+ = 1.67478·10⁻¹⁷, N̄_Λ = 909,507,124,095,312, k̄_0 = 3, J_* = 15,000,015, l_* = 50.
Every number that depends on them is recomputed by the one evaluation step of section 3. Section 8 lists what changed
since the provisional version (md5 eb5f55fcc614dcad6625c8778ac03c70).

## 1. Summary

### 1.1 Which inputs the error changes

The chain from [[def:uc-choice]] to [[thm:uc-integer]], [[prop:uc-d-small]] and [[prop:uc-data-order]] (d) reads the
choice only through the following inputs ([[prop:uc-dependence]], new, proves that it reads nothing else).

| input | old value | changes? | where it enters |
|---|---|---|---|
| ε_K | 1.6416·10⁻¹⁴ | yes: every admissible ε_K < 1.67488·10⁻¹⁷ | Δβ_0 = 0.999²ε_K: L_<, L_>, R_b, D_e, everything |
| ε_+ | 1.64160217·10⁻¹⁴ | yes | only ε_+ < 10⁻¹³ (T_2, I_lev) and the factor 1 + ε_+ in T_2 |
| N̄_Λ ≥ N_Λ | 16,747,199,999,999 | yes: N_Λ ≈ 9.1·10¹⁴ | N_ι (quadratically), k̄_max, d̄_Φ, C_lev, C_* |
| k̄_0, J_*, l_* (J′) | 3, 15,000,015, 50 (765,000,816) | no (R-V-I11); P-UB1 to confirm | N_ι, k̄_max (linearly) |
| ε_Υ = ε_g, Δτ_0 = 0.999ε_Υ | 1.4619·10⁻¹⁰ | no | D_e (∝ 1/Δτ_0), I_lev |
| 𝔡₁ = η_0 = ε^ι_ind | lem:is-offsets (b) | no | W ≤ 1,470,302, T_2, I_lev |
| ℓ⁺_tf, d_BG, r_ι | 1, 11, 16 | no | the per-step charges |
| per-step charges | 497, 469, 466, 20,183, 1,914, 407, 30, 11 | no | C_lev, C_*, I_base |
| I_lev | 34,268,829,852 | no (needs only ε_+ < 10⁻¹³) | T_11, T_12, D′_* |

N_ι, C_lev, C_lev's coefficient 2, C_*'s coefficient 6, M_c, K̄ and D_e are not inputs; they are outputs.

### 1.2 How each output depends on the inputs (all proved in the texts of section 5)

With u := 1/Δβ_0 = 1/(0.998001ε_K) and N̄ := N̄_Λ:

| output | formula | order |
|---|---|---|
| L_<, L_>, R_b | ⌊u⌋, ⌊(1 + ε_K)u⌋ + 1, L_< + 2 | u |
| D_e (first line) | F_1 of [[prop:uc-dependence]] | 3u/Δτ_0 |
| N_ι | (k̄_0 + 1)N̄ + J′N̄(N̄ + 1)/2 | J′N̄²/2 |
| k̄_max, d̄_Φ | k̄_0 + J′N̄, 62N̄ + 2 | N̄ |
| C_lev | 2N_ι + N̄ + 529 | J′N̄² |
| I_base, R_base | 935R_b + 466 + 23,524,832(R_b + 3), 22,097 + I_base | 2.35·10⁷u |
| T_12, D_* | C_lev + I_lev + 4k̄_max + 24, T_12 + 14 | J′N̄² |
| C_* | 6N_ι + 3N̄ + 3I_lev + 8k̄_max + I_base + d̄_Φ + (N̄ + 2)(d̄_Φ + 30) + 45,862 | 3J′N̄² |
| D_acc = D_♭ | D_e + 497L_< + L_>C_lev + 469R_b + 466(R_b + 1) + C_* | J′N̄²u |
| D′_* | T_12 + 18 + 20,565,308,337L_< + (C_lev + I_lev − 9)L_> + 2R_base | J′N̄²u |
| D_b (seminorms of (d)) | D_acc + D_* + d̄_Φ | J′N̄²u |
| D_NM (both readings) | D_acc + D′_* + d̄_Φ | 2J′N̄²u |
| N_NM, K, d_1, N | 21D_NM + 6, 22D_NM + 345, 22D_NM + 331, 22D_NM + 348 | |
| K* (class ℰ_0^½) | < 4k̄² + 48k̄ + 109, k̄ := 22D_NM + 340 | 1936D_NM² |

Each is non-decreasing in N̄_Λ, k̄_0, J′ and non-increasing in ε_K ([[prop:uc-dependence]]). R-V-I11's scaling
(rounds like 1/ε_K, Fourier counts like N_Λ²) is right: the old level-by-level bound times
(1.6416·10⁻¹⁴/ε_K)·(N̄_Λ/16,747,199,999,999)² reproduces the new one to twelve digits.

### 1.3 What the check of every step found

1. **Two proofs used that Λ ∩ {Re ≤ 3 + ε_+} is real.** lem:uc-lambda (c) listed it "in increasing order", and the
   proof of lem:cs-fourier (b) used reality to decide which zf-terms lie below 1 + ε_K. With the generators 1 + 𝒵 of the
   repaired Λ that set has non-real elements (R-V-I11 §2). Both are repaired (blocks M9, M15a, M15b): the list is taken
   in an order of non-decreasing real part, so n(λ_i) ≤ i − 1 and k̄(λ_i) ≤ k̄_0 + J′i, which is all lem:uc-n-iota and
   lem:cs-fourier use; and lem:cs-fourier needs only that the elements of real part at most 2 are real (lem:iii-i10-1-2
   (a), and prop:is-iota: every ι ∈ Z has real part above 2) with (G). The counts N_ι and n_K ≤ N_Λ + N_ι keep their
   form.
2. **Nothing else in the chain uses a numerical value of an input except through the formulas of 1.2.** In particular
   I_lev, W, the level-2 and level-3 counts, R_b's role, the per-step charges, d_BG, ℓ⁺_tf and the rules of sec:cs
   do not involve ε_K or N_Λ; R_b becomes ⌊1/Δβ_0⌋ + 2 (exact) instead of a rounded constant.
3. **Slack, proved (new): the levels split.** lem:cs-sharp charged every one of the K ≤ K̄ levels C_lev, but at most
   L_< ≈ 1/Δβ_0 levels lie in (2, 3), where lem:cs-levels (a) gives 497; only the at most L_> levels in (3, α] cost
   C_lev (lem:ec-counts (a)). The same split applies to the recursion ρ_k ≤ ρ_(k+1) + 2 + (charge of step k) of
   rem:uc-small-reading, a step below 3 costing at most 20,565,308,335 with its iterations (the count in the proof of
   lem:uc-small-orders (d)). This halves D_♭ and D′_*. The crude form D_e + M_c C_* of the old thm:uc-integer is
   dropped: thm:uc-integer now states the sharp D_acc := D_♭ and D_NM := D_♭ + D′_* + d̄_Φ, which covers both readings of
   the fixed seminorms, and prop:uc-data-order (d) uses D_NM.
4. No other proved improvement was found that changes the order: C_lev ≈ 2N_ι comes from two counts (n_ι ≤ N_ι in Step 0
   and n_K ≤ N_ι + N_Λ in Step 7) taken at the bound k̄(λ) for every logarithmic order, which this paper proves no
   better; the first line D_e is within the factor 1.0072 of the lower bound 3R.
5. Unchanged and not drafted: thm:loss-d's "(G) asks ε_K < μ_G" (still true, Λ ⊃ Λ_ℬ); cor:uc-two-offsets and
   rem:uc-offset-d0 (upper bounds on admissible ε_K, still true); the lower bounds. A remark for the coordinator:
   [[prop:ec-rounds]] with ε_K < 1.67488·10⁻¹⁷ would raise the lower bound for the index sets as constructed from
   3R > 1.2497·10²⁴ to 3R > 1.2250·10²⁷ ((1 − 1.98·10⁻⁸)·3/(1.67488·10⁻¹⁷ · 1.46214·10⁻¹⁰) = 1.22502…·10²⁷); not
   drafted here. P-UB1 proves it as the optional cor:is-lower (3R > 1.2250·10²⁷, N_NM > 2.5725·10²⁸); these texts
   keep 1.2497·10²⁴ through cor:uc-two-offsets, and section 8 (Option L) gives the exact substitutions if cor:is-lower
   is kept.

### 1.4 What these texts take from P-UB1 (all met by proofs/P-UB1.md)

- R1. def:uc-choice and lem:uc-admissible keep eq:uc-deltas (Δβ_0 = 0.999²ε_K = 1.6713522747·10⁻¹⁷, Δτ_0 = 0.999ε_Υ),
  ε ≤ 10⁻³ε_g, ε_Υ = 1.4619·10⁻¹⁰, a♭_K − 2 ≥ Δβ_0, ε_K = 1.6747·10⁻¹⁷ < ε_+ = 1.67478·10⁻¹⁷ < 10⁻¹³, and give (G),
  (G⁺) and the hypotheses of prop:ec-upper.
- R2. prop:is-count (a) gives N_Λ ≤ 909,507,124,095,312 (lem:uc-lambda (a)); (b), (c) give k̄_0 = 3, η_0 = 𝔡₁,
  J_* = 15,000,015, and l_* = 50 stands (cor:sp-lstar): so lem:uc-lambda (b), block M6 and block M8 keep their values.
- R3. prop:is-lambda: every element of Λ of real part at most 2.514 is real (block M15a cites exactly this).
- R4. thm:is-gap (label kept): (G) holds if and only if ε_K < μ_Z, 1.6747856·10⁻¹⁷ < μ_Z < 1.6747859·10⁻¹⁷
  (eq:is-mu-z). Blocks M5–M8 and F1, F5, F6, FO3, FO5 cite it, with the sharpened 1.6747859·10⁻¹⁷.
- R5. The repaired def:iii-i10-1-1 of chapter 41 names the generators 1 + 𝒵 (blocks M6, M7, M13), as P-UB1's T1, T2,
  T7, T13 do; if that chapter's text names the set otherwise, all these take its name.
- P-UB1's texts and these do not overlap; thm:uc-reduction (iii) is block M8 only. V-I11 §5.1–5.5 are not applied.

## 2. The chain, step by step (where each statement is proved)

| step | statement (block) | depends on | proof |
|---|---|---|---|
| 1 | L_<, L_>, R_b, K ≤ L_< + L_>, N_b < R_b, D_e (prop:uc-explicit, M11) | ε_K, ε_+, ε_Υ, 𝔡₁ | lem:ec-counts |
| 2 | N̄_Λ, J′, k̄(λ_i) ≤ k̄_0 + J′i, k̄_max, d̄_Φ (lem:uc-lambda, M9) | N̄_Λ, k̄_0, J_*, l_* | def:iii-i10-1-1 |
| 3 | n(E, w) ≤ N_ι (lem:uc-n-iota, M10) | step 2 | sum over i of k̄_0 + 1 + J′i |
| 4 | n_K ≤ N_Λ + N_ι (lem:cs-fourier (b), M15a/b) | step 2, (G), R3 | zf-terms below 1 + ε_K |
| 5 | c(β) ≤ 497 below 3, ≤ C_lev above 3 (lem:cs-levels, M16) | steps 3, 4 | charges added (unchanged proof) |
| 6 | I_lev, I_base (lem:cs-iterations, M17) | R_b | unchanged proof |
| 7 | c_0 bound, C_* (lem:cs-rest, prop:cs-cstar, M18–M20) | steps 2, 5, 6 | eq:cs-c0 written out |
| 8 | d_acc, d_R ≤ D_♭ (lem:cs-sharp, M22) | steps 1, 5, 7 | split of the levels (new) |
| 9 | k_0, D_* (lem:uc-small-orders, M23) | steps 5–7 | unchanged proof, checks 2R_base + 16 < T_12, X_12 > R_base |
| 10 | D′_* (rem:uc-small-reading, M24) | steps 1, 5, 6, 9 | recursion, split of the levels (new) |
| 11 | d_NM ≤ D_b, D_NM; N_NM (prop:uc-d-small, M25) | steps 8–10 | eq:uc-d-small |
| 12 | D_acc, D_NM, 3R, D_e < 1.0072·3R (thm:uc-integer, M12) | steps 8–11 | prop:ec-rounds |
| 13 | monotonicity and the formulas (prop:uc-dependence, M12) | all | the proofs above use only the inputs of 1.1 |
| 14 | K, d_1, N, k1, K* (prop:uc-data-order (d), M26) | step 11 | eq:uc-data-order, eq:uc-kstar-own |
| 15 | h-threshold of rem:ec-lb-unbounded (M4) | step 12 | 0.3168h⁻² > D_NM |

## 3. The evaluation (the step to redo with P-UB1's inputs)

Given ε_K, ε_+, N̄_Λ (and k̄_0, J_*, l_*), in exact rational arithmetic: Δβ_0 = 0.998001ε_K; L_< = ⌊1/Δβ_0⌋,
L_> = ⌊(1 + ε_K)/Δβ_0⌋ + 1, R_b = L_< + 2; D_e a 6-digit decimal above F_1 (rounded through the decimals printed in
the proof of prop:uc-explicit); then the formulas of 1.2 in the order of section 2; then 3R and the h-threshold. Every
drafted text of sections 5 and 6 is produced from these values and rechecked (line widths, wrap rule, labels, lint) in
one pass. At the inputs of this file:

| quantity | value |
|---|---|
| Δβ_0 | 1.6713522747·10⁻¹⁷ |
| L_<, L_>, R_b | 59,831,791,007,643,518, 59,831,791,007,643,520, 59,831,791,007,643,520 |
| D_e (first line) | 1.23382·10²⁷ (windows 4.22261·10²⁴) |
| N_ι | 316,405,564,857,307,442,898,487,679,625,881,224,896 |
| k̄_max, d̄_Φ | 695,773,692,090,726,941,774,595, 56,389,441,693,909,346 |
| C_lev | 632,811,129,714,614,885,796,976,268,758,886,545,633 |
| I_base, R_base | 1,407,588,774,438,516,741,154,802, 1,407,588,774,438,516,741,176,899 |
| T_12 | 632,811,129,714,617,668,891,744,631,700,922,473,889 |
| C_* | 1,898,433,440,430,450,575,537,204,488,161,337,695,702 |
| D_acc = D_♭ | 37,862,223,260,395,633,917,123,246,147,912,828,863,693,156,076,559,963,974 < 3.78623·10⁵⁵ |
| D′_* | 37,862,223,260,395,632,651,500,935,434,129,742,005,773,058,097,412,552,791 |
| D_b | 37,862,223,260,395,634,549,934,375,862,530,497,755,494,177,219,176,347,223 < 3.78623·10⁵⁵ |
| D_NM | 75,724,446,520,791,266,568,624,181,582,042,570,869,522,603,615,666,426,111 < 7.57245·10⁵⁵ |
| 21D_NM + 6 | < 1.59022·10⁵⁷ |
| K ≤ 22D_NM + 345 | < 1.66594·10⁵⁷ (seminorms of (d): < 8.3297·10⁵⁶) |
| K* (class ℰ_0^½) | < 1.11014·10¹¹⁵ |
| 3R at the choice | > 1.2251·10²⁷, D_e < 1.0072·3R |
| rem:ec-lb-unbounded | d_NM > D_NM where h ≤ 6.46·10⁻²⁹ |

The three forms of the bound at these inputs, for comparison (only the last is drafted):

| form | d_acc, d_R | d_NM (both readings) | K |
|---|---|---|---|
| old thm:uc-integer, D_e + M_c C_* | 4.54347·10⁵⁶ | 4.54347·10⁵⁶ | 9.99563·10⁵⁷ |
| old lem:cs-sharp and rem:uc-small-reading (K̄ C_lev) | 7.57245·10⁵⁵ | 1.51449·10⁵⁶ | 3.33188·10⁵⁷ |
| split levels (drafted) | 3.78623·10⁵⁵ | 7.57245·10⁵⁵ | 1.66594·10⁵⁷ |

(R-V-I11's estimates 4.5·10⁵⁶, 7.6·10⁵⁵ and K ≈ 10⁵⁸ are the first two rows.) At the old inputs the split form would give
d_acc ≤ 1.30963·10⁴⁹ and d_NM ≤ 2.61926·10⁴⁹ against the printed 1.57157·10⁵⁰; the formulas reproduce every printed
integer of the old chain exactly (section 7).

## 4. Every site that quotes the upper bound or a changed number

Drafted here (main set, section 5; fallback, section 6):

| site | block (main / fallback) |
|---|---|
| chapters/00-front.md:37 (35–37) | O1 / FO1 |
| chapters/01-introduction.md:156 (155–156) | O2 / FO2 |
| chapters/03-theorems.md:318–319 (316–319) | O3 / FO3 |
| chapters/03-theorems.md:363–366 (qualitative; true in the main set) | — / FO4 |
| chapters/63-own-data.md:70–71, 298–299 ("bounded above only at the computational point") | — / FO6, FO7 |
| chapters/90-scope.md:77–79 (75–79) | O4 / FO5 |
| 71:24–28 and 33 (chapter summary) | M1, M2 / F1, F2 |
| 71:425 (rem:ec-other-losses, last sentence; true in the main set) | — / F9 |
| 71:1497–1499 (thm:loss-d, last sentence of the statement) | M3 / F3 |
| 71:1810 (rem:ec-lb-unbounded; h ≤ 4.48·10⁻²⁶ becomes h ≤ 6.46·10⁻²⁹) | M4 / F4 (1809–1810) |
| 71:2206–2215 rem:ec-upper-point | M5 / F5 |
| 71:2217–2242 rem:ec-upper-open | M6 / rule |
| 71:2246–2263 sec:uc-close, opening paragraph | M7 / rule |
| 71:2559–2564 thm:uc-reduction (iii) | M8 / rule |
| 71:2662–2680 lem:uc-lambda; 2682–2700 lem:uc-n-iota; 2702–2738 prop:uc-explicit | M9, M10, M11 / rule |
| 71:2759–2796 thm:uc-integer, and the new prop:uc-dependence after it | M12 / F6 |
| 71:2798–2823 rem:uc-missing | M13 / rule |
| 71:4094–4112 sec:cs, opening | M14 / rule |
| 71:4396–4398 and 4402–4406 lem:cs-fourier (b), proof (reality of Λ) | M15a, M15b / same |
| 71:4417 lem:cs-levels (b), C_lev | M16 / rule |
| 71:4488–4492 lem:cs-iterations; 4524 and 4573 lem:cs-rest | M17, M18, M19 / rule |
| 71:4592–4622 prop:cs-cstar, rem:cs-sharpness | M20 / rule |
| 71:4635–4640 sec:cs-small notation (K̄ removed) | M21 / rule |
| 71:4652–4683 lem:cs-sharp | M22 / rule |
| 71:4698–4700, 4715, 4830–4842 lem:uc-small-orders (b), (e) | M23a–c / rule |
| 71:4844–4862 rem:uc-small-reading | M24 / rule |
| 71:4876–4884, 4906–4920, 4922–4924 prop:uc-d-small and after | M25a–c / rule |
| 71:5122–5130 and 5209–5230 prop:uc-data-order (d) | M26a, M26b / F7, F8 |

P-UB1's (not drafted here; they quote changed numbers): rem:gap-sums last sentence (71:169–170), the opening of sec:is
(71:2827–2858: (G) "exactly for ε_K < μ_G", N_Λ bounds), prop:is-lambda (3216–3232), thm:is-gap (3250–3325),
prop:is-count (3327–3359), rem:is-summary (3469–3487), def:uc-choice (2583–2597), lem:uc-admissible (2599–2644); and
lem:uc-gaps (2646–2660) if η_0 changes.

Outside chapters/ (not part of the edition's text): PAPER.md (assembled; regenerate), STATUS.md and INTEGRATION.md
(records of the old bound), proofs/P-TR.md (thm:tr-transfer (ii) quotes C_* = 6.4368·10³⁵, D_acc < 1.57157·10⁵⁰ and
N_NM < 3.30029·10⁵¹ at lines 61–62; prop:tr-fail and lines 3–23, 471–490, 535–551, 636–686 use D_acc; its claim that
N_Λ, k̄_0, J_*, η_0 do not move with h (line 478) fails for the repaired Λ, whose generators 1 + 𝒵 move with h).

## 5. The main set of texts

The rule of the numbers: every number below that depends on ε_K, ε_+ or N̄_Λ was produced by the evaluation step of
section 3 at the inputs stated at the top of this file.

### M1. chapter summary, 71-explicit-constants.md lines 24–28

Old (5 lines):

```old
for the index sets as the proofs construct them ([[cor:uc-two-offsets]]). At that point, at one admissible choice of
the weights and of the free orders and inner products ([[def:uc-choice]], [[def:cs-choices]]), d_acc and d_NM, the
latter the d of [[thm:iii-k-3-2]], at least the orders at which its lemmas ask U small ([[prop:uc-d-small]]), are at
most an integer below 1.57157 × 10⁵⁰, and N_NM at most one below 3.30029 × 10⁵¹ ([[thm:uc-integer]]). That parameter
point is not shown to lie in the set on which [[thm:settling]] is proved ([[rem:ec-point-outside]]), and the bounds at
```

New (6 lines):

```new
for the index sets as the proofs construct them ([[cor:uc-two-offsets]]). At that point, at one admissible choice of the
weights and of the free orders and inner products ([[def:uc-choice]], [[def:cs-choices]]), d_acc is at most an integer
below 3.78623 × 10⁵⁵, and d_NM, the d of [[thm:iii-k-3-2]], at least d_acc and the orders at which its lemmas ask U small
([[prop:uc-d-small]]), is at most an integer below 7.57245 × 10⁵⁵, and N_NM at most one below 1.59022 × 10⁵⁷
([[thm:uc-integer]]). That parameter point is not shown to lie in the set on which [[thm:settling]] is proved
([[rem:ec-point-outside]]), and the bounds at
```

### M2. chapter summary, 71-explicit-constants.md lines 33–33

Old (1 lines):

```old
being an explicit number of derivatives; at the computational point K is at most an integer below 3.45745 × 10⁵¹
```

New (1 lines):

```new
being an explicit number of derivatives; at the computational point K is at most an integer below 1.66594 × 10⁵⁷
```

### M3. thm:loss-d, last sentence of the statement, 71-explicit-constants.md lines 1497–1499

Old (3 lines):

```old
the index sets. At the computational point [[thm:uc-integer]] evaluates every number of steps and every such count, and
[[lem:uc-small-orders]] and [[prop:uc-d-small]] the orders at which the proof of [[thm:iii-k-3-2]] asks U small: d_acc
and d_NM are at most an integer below 1.57157 × 10⁵⁰, and N_NM at most one below 3.30029 × 10⁵¹.
```

New (4 lines):

```new
the index sets. At the computational point [[thm:uc-integer]] evaluates every number of steps and every such count, and
[[lem:uc-small-orders]] and [[prop:uc-d-small]] the orders at which the proof of [[thm:iii-k-3-2]] asks U small: d_acc is
at most an integer below 3.78623 × 10⁵⁵, d_NM at most one below 7.57245 × 10⁵⁵, and N_NM at most one below 1.59022 ×
10⁵⁷.
```

### M4. rem:ec-lb-unbounded, 71-explicit-constants.md lines 1810–1810

Old (1 lines):

```old
exceeds 1.57157·10⁵⁰, the bound of [[thm:uc-integer]], at every point of the proved set with h ≤ 4.48·10⁻²⁶. Likewise, at
```

New (1 lines):

```new
exceeds 7.57245·10⁵⁵, the bound of [[thm:uc-integer]], at every point of the proved set with h ≤ 6.46·10⁻²⁹. Likewise, at
```

### M5. rem:ec-upper-point, 71-explicit-constants.md lines 2206–2215

Old (10 lines):

```old
**Remark {#rem:ec-upper-point}** (The upper bound at the computational point.) At the computational point ε_g ≤ ε_Υ <
1.46214·10⁻¹⁰ ([[lem:ec-gauge-gap]], [[rem:ec-gauge-gap]]), and for the index sets as the proofs construct them 𝔡₀ and 𝔡₁
are increments of Λ ([[cor:uc-two-offsets]], [[rem:uc-offset-d0]]) and (G) holds exactly for ε_K < μ_G, where μ_G <
1.64160217198·10⁻¹⁴ ([[thm:is-gap]]). The levels are then less than μ_G apart, and the first line of [[eq:ec-upper]] is
of the order 3/(ε_Kε_g), the order of the lower bound 3R of [[prop:ec-rounds]]. [[prop:uc-explicit]] evaluates it at the
admissible choice of [[def:uc-choice]], with ε_K = 1.6416·10⁻¹⁴ and ε_g = ε_Υ = 1.4619·10⁻¹⁰: it is less than
1.2587·10²⁴, of which less than 4.30775·10²¹ comes from the window loops at ι⁺ (bounded there through ε^ι_ind = 𝔡₁,
[[lem:uc-gaps]]), and less than 1.0072 times the lower bound 3R > 1.2498·10²⁴ at the same choice ([[thm:uc-integer]]).
The losses c(β_k), c_b and c′_b of single steps enter the second line with the multiplicities K < 1.22077·10¹⁴ and N_b,
N_b + 1 < 6.10383·10¹³, and c_0 once; [[prop:cs-cstar]] bounds their largest value c_* by 6.4368·10³⁵.
```

New (11 lines):

```new
**Remark {#rem:ec-upper-point}** (The upper bound at the computational point.) At the computational point ε_g ≤ ε_Υ <
1.46214·10⁻¹⁰ ([[lem:ec-gauge-gap]], [[rem:ec-gauge-gap]]), and for the index sets as the proofs construct them every ε_K
with which (G) holds lies below 1.6747859·10⁻¹⁷ ([[thm:is-gap]]). The levels are then less than 1.6747859·10⁻¹⁷ apart,
and the first line of [[eq:ec-upper]] is of the order 3/(ε_Kε_g), the order of the lower bound 3R of [[prop:ec-rounds]].
[[prop:uc-explicit]] evaluates it at the admissible choice of [[def:uc-choice]], with ε_K = 1.6747·10⁻¹⁷ and ε_g = ε_Υ =
1.4619·10⁻¹⁰: it is less than 1.23382·10²⁷, of which less than 4.22261·10²⁴ comes from the window loops at ι⁺ (bounded
there through ε^ι_ind = 𝔡₁, [[lem:uc-gaps]]), and less than 1.0072 times the lower bound 3R > 1.2251·10²⁷ at the same
choice ([[thm:uc-integer]]). The losses c(β_k), c_b and c′_b of single steps enter the second line with the
multiplicities K, N_b and N_b + 1, and c_0 once: at most 59,831,791,007,643,518 levels lie in (2, 3), where c(β_k) ≤ 497,
at most 59,831,791,007,643,520 in (3, α], where c(β_k) ≤ C_lev < 6.32812·10³⁸ ([[lem:cs-levels]]), and N_b <
59,831,791,007,643,520 ([[prop:uc-explicit]]); [[prop:cs-cstar]] bounds c_0 by C_* < 1.89844·10³⁹.
```

### M6. rem:ec-upper-open, 71-explicit-constants.md lines 2217–2242

Old (26 lines):

```old
**Remark {#rem:ec-upper-open}** (The inputs of the upper bound.) Four inputs separate [[prop:ec-upper]] from an integer;
at the computational point all four are bounded: (1), (2) and (4) are evaluated, and (3) through one number, c_*, which
[[prop:cs-cstar]] bounds. (1) ε_K, N_Λ, k̄_0 and l_*: (G) asks that no element of the set Λ of [[def:iii-i10-1-1]] have
real part in (2, 2 + ε_K] or in (3, 3 + ε_K], and that no λ + d_c0 or λ + d_c1, λ ∈ Λ, have real part in (2, 2 + ε_K].
[[prop:gap-sums]] and [[rem:gap-sums]] settle the three windows for ε_K < 5.019·10⁻⁸ on the part of Λ built from 2, 3,
λ_♯ and the offsets 𝔡₁, 1 + 𝔡₀, 1 + δ₂, 1 + δ′₁. With ℰ_ind as the proofs construct it, 𝔡₀ and 𝔡₁ are themselves
increments, and (G) holds exactly for ε_K < μ_G, 1.64160217197·10⁻¹⁴ < μ_G < 1.64160217198·10⁻¹⁴ ([[thm:is-gap]],
[[cor:uc-two-offsets]]); [[prop:is-count]] and [[cor:sp-lstar]] give 1.62066·10¹³ < N_Λ < 1.67472·10¹³, k̄_0 = 3, J_* =
15,000,015 and the admissible l_* = 50, and [[prop:uc-explicit]] the numbers of levels, rounds, applications and windows
at an admissible choice. (2) ℓ⁺_tf = 1 at the choices of [[lem:ec-tf-loss]] with s = 1 ([[prop:uc-ltf]]). (3) The
single-step losses c(β), c_b, c′_b and c_0: each is a finite composition of the elementary losses of
[[lem:ec-closed-forms]] and [[rem:ec-other-losses]] and of the forward loss, at most 20,180 ([[thm:fwd-loss]],
[[cor:fwd-near-b0]]) and 20,183 at the backgrounds h + h_rem(q) + h_tot(p⃗) ([[lem:cs-elem]] (e)), charged at each
forward solution they apply; they contain the counts n(E, β) of the index sets entering [[eq:ec-fourier-loss]], which
[[lem:uc-n-iota]] bounds through N_Λ, k̄_0, l_* and J_*; c_0 contains, besides, the iterations of Steps 4′ and 4 at the
top level, each bounded as in [[lem:ec-counts]], and the loss of
[[thm:iii-j-2-4]], which its proof takes as the sum of the losses of its steps over the exponents of Λ ∩ {Re < 3 + ε_+}
([[lem:uc-phi-loss]]). Their largest value c_* enters [[thm:uc-integer]] with the coefficient 2.44153·10¹⁴;
[[prop:cs-cstar]] bounds it by 6.4368·10³⁵. (4) d_BG = 11 serves ([[prop:uc-dbg]]); it enters c(β), c_b, c′_b and c_0
through the charge max(2, d_BG). For d_NM, and so for N_NM, the losses of [[lem:iii-k-2-2]] and [[prop:iii-j2-4-3]] are
at most 62N_Λ + 10 < 1.04·10¹⁵ ([[lem:uc-phi-loss]], [[lem:uc-lambda]]), that of [[lem:iii-k-2-3]] satisfies
[[eq:ec-upper]] in the form of [[lem:uc-dr]], and [[lem:uc-small-orders]] and [[prop:uc-d-small]] bound the orders at
which these results ask U small, and with them d_NM ([[thm:uc-integer]]). Given ε_K, the explicit part
of [[eq:ec-upper]] is of the order 1/(ε_Kε_g), the order of the lower bound of [[prop:ec-rounds]]; ℓ⁺_tf multiplies terms
of that order, c(β) enters at most N_< + N_> times, about 2/ε_K, and c_b and c′_b at most about 1/ε_K times each. All
these numbers depend on the point through z, which fixes ε_Υ ([[rem:ec-gauge-gap]]), and through the index sets.
```

New (28 lines):

```new
**Remark {#rem:ec-upper-open}** (The inputs of the upper bound.) Four inputs separate [[prop:ec-upper]] from an integer;
at the computational point all four are bounded: (1), (2) and (4) are evaluated, and (3) through the numbers C_lev and
C_*, which [[lem:cs-levels]] and [[prop:cs-cstar]] bound. (1) ε_K, N_Λ, k̄_0 and l_*: (G) asks that no element of the set
Λ of [[def:iii-i10-1-1]] have real part in (2, 2 + ε_K] or in (3, 3 + ε_K], and that no λ + d_c0 or λ + d_c1, λ ∈ Λ, have
real part in (2, 2 + ε_K]. [[prop:gap-sums]] and [[rem:gap-sums]] settle the three windows for ε_K < 5.019·10⁻⁸ on the
part of Λ built from 2, 3, λ_♯ and the offsets 𝔡₁, 1 + 𝔡₀, 1 + δ₂, 1 + δ′₁. With ℰ_ind as the proofs construct it, 𝔡₀ and
𝔡₁ are themselves increments, which asks ε_K < 1.6417·10⁻¹⁴ ([[cor:uc-two-offsets]]), and with the generators 1 + 𝒵 of Λ
(G) holds exactly for ε_K < μ_Z, where μ_Z < 1.6747859·10⁻¹⁷ ([[thm:is-gap]], [[eq:is-mu-z]]); [[prop:is-count]] and
[[cor:sp-lstar]] give N_Λ ≤ 909,507,124,095,312, k̄_0 = 3, J_* = 15,000,015 and the admissible l_* = 50, and
[[prop:uc-explicit]] the numbers of levels, rounds, applications and windows at an admissible choice. (2) ℓ⁺_tf = 1 at
the choices of [[lem:ec-tf-loss]] with s = 1 ([[prop:uc-ltf]]). (3) The single-step losses c(β), c_b, c′_b and c_0: each
is a finite composition of the elementary losses of [[lem:ec-closed-forms]] and [[rem:ec-other-losses]] and of the
forward loss, at most 20,180 ([[thm:fwd-loss]], [[cor:fwd-near-b0]]) and 20,183 at the backgrounds h + h_rem(q) +
h_tot(p⃗) ([[lem:cs-elem]] (e)), charged at each forward solution they apply; they contain the counts n(E, β) of the
index sets entering [[eq:ec-fourier-loss]], which [[lem:uc-n-iota]] bounds through N_Λ, k̄_0, l_* and J_*; c_0 contains,
besides, the iterations of Steps 4′ and 4 at the top level, each bounded as in [[lem:ec-counts]], and the loss of
[[thm:iii-j-2-4]], which its proof takes as the sum of the losses of its steps over the exponents of Λ ∩ {Re < 3 + ε_+}
([[lem:uc-phi-loss]]). The c(β) of the levels above 3 are at most C_lev < 6.32812·10³⁸ ([[lem:cs-levels]]), and these
levels, at most 59,831,791,007,643,520 of them, carry the bound of [[thm:uc-integer]]; c_0 enters once, and
[[prop:cs-cstar]] bounds it by C_* < 1.89844·10³⁹. (4) d_BG = 11 serves ([[prop:uc-dbg]]); it enters c(β), c_b, c′_b
and c_0 through the charge max(2, d_BG). For d_NM, and so for N_NM, the losses of [[lem:iii-k-2-2]] and
[[prop:iii-j2-4-3]] are at most 62N_Λ + 10 ≤ 56,389,441,693,909,354 ([[lem:uc-phi-loss]], [[lem:uc-lambda]]), that of
[[lem:iii-k-2-3]] satisfies [[eq:ec-upper]] in the form of [[lem:uc-dr]], and [[lem:uc-small-orders]] and
[[prop:uc-d-small]] bound the orders at which these results ask U small, and with them d_NM ([[thm:uc-integer]]). Given
ε_K, the explicit part of [[eq:ec-upper]] is of the order 1/(ε_Kε_g), the order of the lower bound of [[prop:ec-rounds]];
ℓ⁺_tf multiplies terms of that order, c(β) enters at most N_< + N_> times, about 2/ε_K, and c_b and c′_b at most about
1/ε_K times each. All these numbers depend on the point through z, which fixes ε_Υ ([[rem:ec-gauge-gap]]), and through
the index sets.
```

### M7. sec:uc-close, opening paragraph, 71-explicit-constants.md lines 2246–2263

Old (18 lines):

```old
This section takes the inputs that [[prop:ec-upper]] leaves free, evaluates them at the computational point, and
assembles the bound. Two are fixed by general statements of this paper. The loss of the inverse of the transition face
model is 1 at the weights at which the construction may use it, so ℓ_tf = 1 ([[prop:uc-ltf]]); and the order of the
background terms may be taken to be d_BG = 11 ([[prop:uc-dbg]]). The others are fixed by the index sets that define the
set Λ of [[def:iii-i10-1-1]] and by the orders of the poles of N_ι⁺(L̄, ·)⁻¹: the admissible ε_K of the gap condition
(G), the counts n(E, β) of the index sets entering the Fourier steps of the levels ([[lem:uc-fourier-count]]), and the
loss of the map Φ of [[thm:iii-j-2-4]], which governs the other two losses ([[lem:uc-phi-loss]]). Memberships
and least real parts of the index sets alone fix no admissible ε_K ([[prop:uc-no-eps]]); and if both offsets of the class
roots are increments of Λ, as they are for the index sets that the proofs construct, every admissible ε_K lies below
1.6417·10⁻¹⁴ ([[cor:uc-two-offsets]]). [[sec:is]] lists the exponents of the index sets as constructed, and [[sec:sp]]
the poles of N_ι⁺(L̄, ·)⁻¹ at real part at most 5, all simple. With them (G) holds exactly for ε_K < μ_G
([[thm:is-gap]]), and N_Λ, k̄_0, l_* and J_* are explicit ([[prop:is-count]], [[cor:sp-lstar]]). [[sec:uc-eval]] fixes an
admissible choice of the weights, evaluates every count of [[eq:ec-upper]] at it, and proves [[thm:uc-integer]]: d_acc
and d_NM are at most an integer D_acc < 1.57157·10⁵⁰, the largest single-step loss being below 6.4368·10³⁵
([[prop:cs-cstar]]) and the orders of smallness being bounded in [[sec:cs-small]], against the lower bound
1.2497·10²⁴; [[rem:uc-missing]] states what the bound rests on. Throughout
we work at the computational point of [[def:ec-point]], so z = 4·10⁻⁶ = 1/250000 and λ_♯ = 15099/10000, and 𝔡₀ = d_c0,
𝔡₁ = d_c1 are the offsets of [[sec:ec-gap-sums]].
```

New (20 lines):

```new
This section takes the inputs that [[prop:ec-upper]] leaves free, evaluates them at the computational point, and
assembles the bound. Two are fixed by general statements of this paper. The loss of the inverse of the transition face
model is 1 at the weights at which the construction may use it, so ℓ_tf = 1 ([[prop:uc-ltf]]); and the order of the
background terms may be taken to be d_BG = 11 ([[prop:uc-dbg]]). The others are fixed by the index sets that define
the set Λ of [[def:iii-i10-1-1]] and by the orders of the poles of N_ι⁺(L̄, ·)⁻¹: the admissible ε_K of the gap condition
(G), the counts n(E, β) of the index sets entering the Fourier steps of the levels ([[lem:uc-fourier-count]]), and the
loss of the map Φ of [[thm:iii-j-2-4]], which governs the other two losses ([[lem:uc-phi-loss]]). Memberships and least
real parts of the index sets alone fix no admissible ε_K ([[prop:uc-no-eps]]); if both offsets of the class roots are
increments of Λ, as they are for the index sets that the proofs construct, every admissible ε_K lies below 1.6417·10⁻¹⁴
([[cor:uc-two-offsets]]), and the generators 1 + 𝒵 of Λ put it below 1.6747859·10⁻¹⁷ ([[thm:is-gap]]). [[sec:is]] lists
the exponents of the index sets as constructed, and [[sec:sp]] the poles of N_ι⁺(L̄, ·)⁻¹ at real part at most 5, all
simple. With them (G) holds exactly for ε_K < μ_Z ([[thm:is-gap]]), and N_Λ, k̄_0, l_* and J_* are explicit
([[prop:is-count]], [[cor:sp-lstar]]). [[sec:uc-eval]] fixes an admissible choice of the weights, evaluates every
count of [[eq:ec-upper]] at it, and proves [[thm:uc-integer]]: d_acc and d_R are at most an integer D_acc < 3.78623·10⁵⁵,
and d_NM at most an integer D_NM < 7.57245·10⁵⁵, the single-step losses being at most C_lev < 6.32812·10³⁸ at the levels
above 3 ([[lem:cs-levels]]) and at most C_* < 1.89844·10³⁹ in all ([[prop:cs-cstar]]), and the orders of smallness being
bounded in [[sec:cs-small]], against the lower bound 1.2497·10²⁴; [[prop:uc-dependence]] gives D_acc and D_NM as
functions of the inputs of the choice, and [[rem:uc-missing]] states what the bound rests on. Throughout we work at the
computational point of [[def:ec-point]], so z = 4·10⁻⁶ = 1/250000 and λ_♯ = 15099/10000, and 𝔡₀ = d_c0, 𝔡₁ = d_c1 are the
offsets of [[sec:ec-gap-sums]].
```

### M8. thm:uc-reduction (iii), 71-explicit-constants.md lines 2559–2564

Old (6 lines):

```old
(iii) N_Λ, k̄_0, l_*, J_* and the admissible ε_K (through (G)) are fixed by the exponents and logarithmic orders of the
index sets of [[sec:uc-index-sets]] and by the orders of the poles of N_ι⁺(L̄, ·)⁻¹ at real part at most 5. For the
index sets as constructed and the least ℰ^C_I, (G) holds exactly for ε_K < μ_G, where
1.64160217197·10⁻¹⁴ < μ_G < 1.64160217198·10⁻¹⁴ ([[thm:is-gap]]); 1.62066·10¹³ < N_Λ < 1.67472·10¹³, k̄_0 = 3 is the
least admissible bound and J_* = 15,000,015 ([[prop:is-count]]); and l_* = 50 is admissible ([[cor:sp-lstar]]).
Memberships and least real parts alone fix no admissible ε_K ([[prop:uc-no-eps]]).
```

New (6 lines):

```new
(iii) N_Λ, k̄_0, l_*, J_* and the admissible ε_K (through (G)) are fixed by the exponents and logarithmic orders of the
index sets of [[sec:uc-index-sets]] and by the orders of the poles of N_ι⁺(L̄, ·)⁻¹ at real part at most 5. For the index
sets as constructed and the least ℰ^C_I, (G) holds exactly for ε_K < μ_Z, where 1.6747856·10⁻¹⁷ < μ_Z < 1.6747859·10⁻¹⁷
([[thm:is-gap]], [[eq:is-mu-z]]); N_Λ ≤ 909,507,124,095,312, k̄_0 = 3 is the least admissible bound and J_* = 15,000,015
([[prop:is-count]]); and l_* = 50 is admissible ([[cor:sp-lstar]]). Memberships and least real parts alone fix no
admissible ε_K ([[prop:uc-no-eps]]).
```

### M9. lem:uc-lambda, 71-explicit-constants.md lines 2662–2680

Old (19 lines):

```old
**Lemma {#lem:uc-lambda}** (The numbers of [[def:iii-i10-1-1]].) At the choice of [[def:uc-choice]]:

(a) N_Λ = #(Λ ∩ {Re < 3 + ε_+}) is an integer with 16,206,600,000,000 < N_Λ ≤ 16,747,199,999,999;

(b) k̄_0 = 3, l_* = 50, η_0 = 𝔡₁ and J_* = 15,000,015, so that J′ := (J_* + 1)(l_* + 1) = 765,000,816;

(c) the elements of Λ ∩ {Re < 3 + ε_+} are real; listed in increasing order as λ_1 < ⋯ < λ_(N_Λ), they have
n(λ_i) = i − 1 and k̄(λ_i) = 3 + 765,000,816·i ≤ 12,811,621,665,714,434,999,187 < 1.28117·10²²;

(d) d_Φ = 62N_Λ + 2 ≤ 1,038,326,399,999,940, and d_FM, d_Ψ ≤ 62N_Λ + 10 ≤ 1,038,326,399,999,948.

*Proof.* (a) is [[prop:is-count]] (a): 1.62066·10¹³ = 16,206,600,000,000, and an integer below 1.67472·10¹³ is at most
16,747,199,999,999. (b) [[prop:is-count]] (b), (c) give k̄_0 = 3 as the least admissible bound, η_0 = 𝔡₁ and
J_* = 15,000,015; l_* = 50 is admissible by [[cor:sp-lstar]] (a); and 15,000,016 · 51 = 765,000,816. (c) By
[[prop:is-lambda]] the elements of Λ of real part at most 3 + ε_+ are real. The λ′ ∈ Λ with Re λ′ < λ_i lie in
Λ ∩ {Re < 3 + ε_+}, so they are λ_1, …, λ_(i−1), and n(λ_i) = i − 1; then [[def:iii-i10-1-1]] gives
k̄(λ_i) = k̄_0 + J′(n(λ_i) + 1) = 3 + 765,000,816·i, and for i ≤ 16,747,199,999,999 this is at most
3 + 765,000,816 · 16,747,199,999,999 = 12,811,621,665,714,434,999,187. (d) is [[lem:uc-phi-loss]] with (a), as
62 · 16,747,199,999,999 = 1,038,326,399,999,938. ∎
```

New (16 lines):

```new
**Lemma {#lem:uc-lambda}** (The numbers of [[def:iii-i10-1-1]].) At the choice of [[def:uc-choice]]:

(a) N_Λ = #(Λ ∩ {Re < 3 + ε_+}) is an integer with N_Λ ≤ N̄_Λ := 909,507,124,095,312;

(b) k̄_0 = 3, l_* = 50, η_0 = 𝔡₁ and J_* = 15,000,015, so that J′ := (J_* + 1)(l_* + 1) = 765,000,816;

(c) listed in an order of non-decreasing real part as λ_1, …, λ_(N_Λ), the elements of Λ ∩ {Re < 3 + ε_+} have n(λ_i) ≤
i − 1 and k̄(λ_i) ≤ k̄_0 + J′i ≤ k̄_max := k̄_0 + J′N̄_Λ = 695,773,692,090,726,941,774,595;

(d) d_Φ = 62N_Λ + 2 ≤ d̄_Φ := 62N̄_Λ + 2 = 56,389,441,693,909,346, and d_FM, d_Ψ ≤ 62N̄_Λ + 10 = 56,389,441,693,909,354.

*Proof.* (a) is [[prop:is-count]] (a). (b) [[prop:is-count]] (b), (c) give k̄_0 = 3 as the least admissible bound,
η_0 = 𝔡₁ and J_* = 15,000,015; l_* = 50 is admissible by [[cor:sp-lstar]] (a); and 15,000,016 · 51 = 765,000,816. (c)
The λ′ ∈ Λ with Re λ′ < Re λ_i lie in Λ ∩ {Re < 3 + ε_+} and come before λ_i in the list, so n(λ_i) ≤ i − 1; then
[[def:iii-i10-1-1]] gives k̄(λ_i) = k̄_0 + J′(n(λ_i) + 1) ≤ k̄_0 + J′i, and i ≤ N_Λ ≤ N̄_Λ. (d) is [[lem:uc-phi-loss]]
with (a), as 62 · 909,507,124,095,312 = 56,389,441,693,909,344. ∎
```

### M10. lem:uc-n-iota, 71-explicit-constants.md lines 2682–2700

Old (19 lines):

```old
**Lemma {#lem:uc-n-iota}** (The counts of the Fourier steps.) At the choice of [[def:uc-choice]], let E be an index set
with π_1(E ∩ {Re < 3 + ε_+}) ⊂ Λ whose logarithmic order at each λ ∈ Λ with Re λ < 3 + ε_+ is at most k̄(λ); by
[[prop:iii-i10-3-1]] (c), ℰ^♭ is one. Then for every w < 3 + ε_+,

    n(E, w) ≤ 4N_Λ + 765,000,816·N_Λ(N_Λ + 1)/2 ≤ N_ι,
    N_ι := 107,279,395,180,026,392,909,234,131,199,999,996,                                               {#eq:uc-n-iota}

and N_ι < 1.07280·10³⁵. In particular the count n_ι of [[lem:uc-fourier-count]] is at most N_ι, and the Fourier step of
Step 0 of the proof of [[prop:iii-i11-3-1]] at a level β ∈ (3, α] loses at most 9 + N_ι.

*Proof.* A pair (z, m) ∈ E with Re z ≤ w has z ∈ Λ ∩ {Re < 3 + ε_+}, so z = λ_i for some i ≤ N_Λ, and m ≤ k̄(λ_i)
([[lem:uc-lambda]] (c)); at z = λ_i there are at most k̄(λ_i) + 1 = 4 + 765,000,816·i such pairs. Summing over i,
n(E, w) ≤ 4N_Λ + 765,000,816·N_Λ(N_Λ + 1)/2, which increases with N_Λ; at N_Λ = 16,747,199,999,999, where
(N_Λ + 1)/2 = 8,373,600,000,000, it equals

    4 · 16,747,199,999,999 + 765,000,816 · 16,747,199,999,999 · 8,373,600,000,000 = N_ι.

By [[lem:uc-fourier-count]], n_ι counts the pairs (λ, k) ∈ ℰ^♭ with Re λ ≤ 3 + ε_+ − ε, so n_ι = n(ℰ^♭, 3 + ε_+ − ε)
≤ N_ι, and the loss [[eq:uc-fourier-count]] is 1 + n_ι + 2⌊β − ε⌋ ≤ 1 + N_ι + 8, as β − ε < α ≤ 4 + ε_K < 5. ∎
```

New (19 lines):

```new
**Lemma {#lem:uc-n-iota}** (The counts of the Fourier steps.) At the choice of [[def:uc-choice]], let E be an index set
with π_1(E ∩ {Re < 3 + ε_+}) ⊂ Λ whose logarithmic order at each λ ∈ Λ with Re λ < 3 + ε_+ is at most k̄(λ); by
[[prop:iii-i10-3-1]] (c), ℰ^♭ is one. Then for every w < 3 + ε_+,

    n(E, w) ≤ (k̄_0 + 1)N_Λ + J′N_Λ(N_Λ + 1)/2 ≤ N_ι := (k̄_0 + 1)N̄_Λ + J′N̄_Λ(N̄_Λ + 1)/2,    {#eq:uc-n-iota}

and N_ι = 316,405,564,857,307,442,898,487,679,625,881,224,896 < 3.16406·10³⁸. In particular the count n_ι of
[[lem:uc-fourier-count]] is at most N_ι, and the Fourier step of Step 0 of the proof of [[prop:iii-i11-3-1]] at a level β
∈ (3, α] loses at most 9 + N_ι.

*Proof.* A pair (z, m) ∈ E with Re z ≤ w has z ∈ Λ ∩ {Re < 3 + ε_+}, so z = λ_i for some i ≤ N_Λ, and m ≤ k̄(λ_i) ≤
k̄_0 + J′i ([[lem:uc-lambda]] (c)); at z = λ_i there are at most k̄_0 + 1 + J′i such pairs. Summing over i, n(E, w) ≤
(k̄_0 + 1)N_Λ + J′N_Λ(N_Λ + 1)/2, which increases with N_Λ; at N_Λ = N̄_Λ = 909,507,124,095,312, where (N̄_Λ + 1)/2 =
454,753,562,047,656, it equals

    4 · 909,507,124,095,312 + 765,000,816 · 909,507,124,095,312 · 454,753,562,047,656 = N_ι.

By [[lem:uc-fourier-count]], n_ι counts the pairs (λ, k) ∈ ℰ^♭ with Re λ ≤ 3 + ε_+ − ε, so n_ι = n(ℰ^♭, 3 + ε_+ − ε) ≤
N_ι, and the loss [[eq:uc-fourier-count]] is 1 + n_ι + 2⌊β − ε⌋ ≤ 1 + N_ι + 8, as β − ε < α ≤ 4 + ε_K < 5. ∎
```

### M11. prop:uc-explicit, 71-explicit-constants.md lines 2702–2738

Old (37 lines):

```old
**Proposition {#prop:uc-explicit}** (The counts of the long iterations.) At the choice of [[def:uc-choice]], in
[[lem:ec-counts]], [[eq:ec-upper-counts]] and [[eq:uc-t2-w]],

    N_<, N_>, N_b < 6.10382·10¹³,     T_<, T_> < 2.089723·10²³,     T_2 < 1.83115·10²⁰,     W < 1,470,302.27,
                                                                                                     {#eq:uc-counts}

and every window loop has at most 1,470,302 windows. The first line of [[eq:ec-upper]], with ℓ⁺_tf = 1, r_ι ≤ 16 and
the T_2 and W of [[eq:uc-t2-w]], is less than D_e := 1.2587·10²⁴; of it, the window loops at ι⁺ contribute less than
4.30775·10²¹. The number K of the levels β_1, …, β_K and the number N_b of [[lem:ec-counts]] (f) satisfy
K + 2N_b + 2 < M_c := 2.44153·10¹⁴.

*Proof.* By [[eq:uc-deltas]] and the lower bound for 𝔡₁ of [[lem:is-offsets]] (b),

    1/Δβ_0 < 6.1038195·10¹³,     1/Δτ_0 < 6.847261·10⁹,     1/(2Δβ_0Δτ_0) < 2.0897221·10²³,
    1/𝔡₁ < 3.0000026·10⁶,     0.4901/𝔡₁ < 1,470,301.27,

each by multiplying out (for instance 1.6383184416 · 6.1038195 > 10, and
3.333330462964850822194855 · 1.47030127 > 4.901). By [[eq:ec-upper-counts]], N_< ≤ 1/Δβ_0, and N_>, N_b ≤
(1 + ε_K)/Δβ_0 + 1 < 1/Δβ_0 + 3, as ε_K/Δβ_0 = 1/0.998001 < 2; so all three are less than
6.1038195·10¹³ + 3 < 6.10382·10¹³. As (1 + Δβ_0/2)² < 1 + 2·10⁻¹⁴, (1 + ε_K + Δβ_0/2)² < 1 + 6·10⁻¹⁴ and
2(1 + ε_K)/Δβ_0 + 2 < 1.3·10¹⁴,

    T_< < 2.0897221·10²³ · (1 + 2·10⁻¹⁴) + 6.2·10¹³ < 2.089723·10²³,
    T_> < 2.0897221·10²³ · (1 + 6·10⁻¹⁴) + 1.3·10¹⁴ < 2.089723·10²³.

As η_2 − η_1 < ε_+ < 10⁻¹³, (1 + η_2 − η_1)/𝔡₁ + 2 < (1 + 10⁻¹³) · 3.0000026·10⁶ + 2 < 3.000005·10⁶, and so
T_2 < 6.10382·10¹³ · 3.000005·10⁶ < 1.83115·10²⁰. W = 0.4901/𝔡₁ + 1 < 1,470,302.27, and the number of windows of a
loop, an integer at most W ([[lem:uc-gaps]]), is at most 1,470,302. In the first line of [[eq:ec-upper]],
1/Δτ ≤ 1/Δτ_0, so 4(1/Δτ + 2) < 4(6.847261·10⁹ + 2) < 2.74·10¹⁰; N_< + N_> + N_b + 3 < 3 · 6.10382·10¹³ + 3 <
1.831147·10¹⁴, so r_ιW(N_< + N_> + N_b + 3) < 16 · 1,470,302.27 · 1.831147·10¹⁴ < 4.30775·10²¹, and so is the
contribution of the window loops, each of at most 1,470,302 windows. Hence the first line is less than

    3 · (2 · 2.089723·10²³ + 1.83115·10²⁰) + 2.74·10¹⁰ + 4.30775·10²¹
        < 1.2543832·10²⁴ + 4.30775·10²¹ + 2.74·10¹⁰ < 1.2587·10²⁴.

Finally, at most N_< levels lie in (2, 3) and at most N_> in (3, α] ([[lem:ec-counts]] (a)), and no level equals 3; so
K ≤ N_< + N_>, and K + 2N_b + 2 < 4 · 6.10382·10¹³ + 2 < 2.44153·10¹⁴. ∎
```

New (48 lines):

```new
**Proposition {#prop:uc-explicit}** (The counts of the long iterations.) At the choice of [[def:uc-choice]] put

    L_< := ⌊1/Δβ_0⌋,     L_> := ⌊(1 + ε_K)/Δβ_0⌋ + 1,     R_b := L_< + 2.                 {#eq:uc-levels}

Then at most L_< of the levels β_1, …, β_K lie in (2, 3) and at most L_> in (3, α], so that K ≤ L_< + L_>; the number N_b
of [[lem:ec-counts]] (f) satisfies N_b < R_b; and L_< = 59,831,791,007,643,518, L_> = 59,831,791,007,643,520 and R_b =
59,831,791,007,643,520. In [[lem:ec-counts]], [[eq:ec-upper-counts]] and [[eq:uc-t2-w]],

    N_<, N_>, N_b < 5.98318·10¹⁶,   T_<, T_> < 2.04842·10²⁶,   T_2 < 1.79496·10²³,   W < 1,470,302.27,    {#eq:uc-counts}

and every window loop has at most 1,470,302 windows. The first line of [[eq:ec-upper]], with ℓ⁺_tf = 1, r_ι ≤ 16 and the
T_2 and W of [[eq:uc-t2-w]], is less than D_e := 1.23382·10²⁷; of it, the window loops at ι⁺ contribute less than
4.22261·10²⁴.

*Proof.* *The levels.* By [[eq:uc-deltas]], Δβ_0 = 0.999²ε_K = 1.6713522747·10⁻¹⁷ = 16,713,522,747·10⁻²⁷, and

    16,713,522,747 · 59,831,791,007,643,518 = 999,999,999,999,999,988,960,103,946,
    16,713,522,747 · 59,831,791,007,643,519 = 1,000,000,000,000,000,005,673,626,693,
    16,713,522,747 · 59,831,791,007,643,520 = 1,000,000,000,000,000,022,387,149,440,

while 10²⁷(1 + ε_K) = 1,000,000,000,000,000,016,747,000,000; so ⌊1/Δβ_0⌋ = 59,831,791,007,643,518 and ⌊(1 + ε_K)/Δβ_0⌋ =
59,831,791,007,643,519. By [[lem:ec-counts]] (a), at most N_< = (3 − α_1)/Δβ ≤ 1/Δβ_0 of the levels lie in (2, 3), as
α_1 > 2 and Δβ ≥ Δβ_0 ([[lem:uc-admissible]]), and at most N_> = (α − 3)/Δβ + 1 ≤ (1 + ε_K)/Δβ_0 + 1 in (3, α], as α ≤
4 + ε_K; these numbers of levels are integers, so they are at most L_< and L_>. Every level exceeds α_1 > 2 and none
equals 3, so K ≤ L_< + L_>. By [[eq:ec-upper-counts]], N_b ≤ 1/Δβ_0 + 1 < L_< + 2 = R_b.

*The counts.* By [[eq:uc-deltas]] and the lower bound for 𝔡₁ of [[lem:is-offsets]] (b),

    1/Δβ_0 < 5.9831792·10¹⁶,     1/Δτ_0 < 6.847261·10⁹,     1/(2Δβ_0Δτ_0) < 2.0484193·10²⁶,
    1/𝔡₁ < 3.0000026·10⁶,     0.4901/𝔡₁ < 1,470,301.27,

each by multiplying out (for instance 1.6713522747 · 5.9831792 > 10, and 3.333330462964850822194855 · 1.47030127 >
4.901). By [[eq:ec-upper-counts]], N_< ≤ 1/Δβ_0, and N_>, N_b ≤ (1 + ε_K)/Δβ_0 + 1 < 1/Δβ_0 + 3, as ε_K/Δβ_0 = 1/0.998001
< 2; so all three are less than 5.98318·10¹⁶. As (1 + Δβ_0/2)² < 1 + 2·10⁻¹⁷, (1 + ε_K + Δβ_0/2)² < 1 + 6·10⁻¹⁷, 1/Δβ_0 <
6·10¹⁶ and 2(1 + ε_K)/Δβ_0 + 2 < 1.3·10¹⁷,

    T_< < 2.0484193·10²⁶ · (1 + 2·10⁻¹⁷) + 6·10¹⁶ < 2.04842·10²⁶,
    T_> < 2.0484193·10²⁶ · (1 + 6·10⁻¹⁷) + 1.3·10¹⁷ < 2.04842·10²⁶.

As η_2 − η_1 < ε_+ < 10⁻¹³, (1 + η_2 − η_1)/𝔡₁ + 2 < (1 + 10⁻¹³) · 3.0000026·10⁶ + 2 < 3.000005·10⁶, and so T_2 <
5.98318·10¹⁶ · 3.000005·10⁶ < 1.79496·10²³. W = 0.4901/𝔡₁ + 1 < 1,470,302.27, and the number of windows of a loop, an
integer at most W ([[lem:uc-gaps]]), is at most 1,470,302. In the first line of [[eq:ec-upper]], 1/Δτ ≤ 1/Δτ_0, so
4(1/Δτ + 2) < 4(6.847261·10⁹ + 2) < 2.74·10¹⁰; N_< + N_> + N_b + 3 < 3 · 5.98318·10¹⁶ + 3 < 1.794955·10¹⁷, so r_ιW(N_< +
N_> + N_b + 3) < 16 · 1,470,302.27 · 1.794955·10¹⁷ < 4.22261·10²⁴, and so is the contribution of the window loops, each
of at most 1,470,302 windows. Hence the first line is less than

    3 · (2 · 2.04842·10²⁶ + 1.79496·10²³) + 2.74·10¹⁰ + 4.22261·10²⁴
        < 1.2295905·10²⁷ + 4.22261·10²⁴ + 2.74·10¹⁰ < 1.23382·10²⁷. ∎
```

### M12. thm:uc-integer, and a new proposition after it, 71-explicit-constants.md lines 2759–2796

Old (38 lines):

```old
**Theorem {#thm:uc-integer}** (The loss d at the computational point.) At the computational point, with the index sets as
constructed, the admissible choice of the weights of [[def:uc-choice]] and the free orders and inner products of
[[def:cs-choices]], let c_* be the largest of the numbers c(β_k) (1 ≤ k ≤ K), c_b, c′_b and c_0 defined before
[[prop:ec-upper]] and c^Ψ(β_k), c^Ψ_b, c′^Ψ_b and c^Ψ_0 of [[lem:uc-dr]]: the largest loss that [[def:ec-accounted-loss]]
assigns to a single step outside the long iterations. Then
c_* < C_* := 643,680,000,000,000,000,000,000,000,000,000,000 = 6.4368·10³⁵ ([[prop:cs-cstar]]), and

    d_acc ≤ d_R ≤ D_acc,     d_NM ≤ D_NM := D_acc,     N_NM = 21d_NM + 6 ≤ 21D_NM + 6,                 {#eq:uc-integer}

where, with D_e = 1.2587·10²⁴ = 1,258,700,000,000,000,000,000,000 and M_c = 2.44153·10¹⁴ = 244,153,000,000,000,

    D_acc := D_e + M_c C_* = 157,156,403,040,000,000,000,000,001,258,700,000,000,000,000,000,000 < 1.57157·10⁵⁰,
    21D_NM + 6 = 3,300,284,463,840,000,000,000,000,026,432,700,000,000,000,000,000,006 < 3.30029·10⁵¹.

The losses of [[lem:iii-k-2-2]] and [[prop:iii-j2-4-3]] satisfy d_Ψ, d_FM ≤ 1,038,326,399,999,948, and the finer bounds
d_acc, d_R < 2.6193·10⁴⁹ and d_NM < 5.2386·10⁴⁹ hold ([[lem:cs-sharp]], [[prop:uc-d-small]]). At a level β ∈ (3, α],
1 + n_ι ≤ c(β) ≤ 2N_ι + N̄_Λ + 529 = C_lev, with N_ι of [[eq:uc-n-iota]], N̄_Λ = 16,747,199,999,999 and C_lev of
[[eq:cs-clev]] ([[lem:cs-levels]]). Against these, for every admissible choice of the weights,

    d_NM ≥ d_acc ≥ 3R > 1.2497·10²⁴,     N_NM > 2.624·10²⁵,                                                {#eq:uc-lower}

and at the choice of [[def:uc-choice]], 3R > 1.2498·10²⁴, so that D_e < 1.0072 · 3R.

*Proof.* By [[prop:cs-cstar]], c_* < C_*. By [[lem:uc-admissible]] the hypotheses of [[prop:ec-upper]] hold, and by
[[lem:uc-gaps]] it holds with the T_2 and W of [[eq:uc-t2-w]]. Its first line is less than D_e by [[prop:uc-explicit]],
and its second line is at most Σ_k c(β_k) + N_b c_b + (N_b + 1)c′_b + c_0 ≤ (K + 2N_b + 2)c_* ≤ M_c C_*, again by
[[prop:uc-explicit]]. So d_acc ≤ D_e + M_c C_* = D_acc. Here M_c C_* = 244,153 · 64,368 · 10⁴⁰, which is
15,715,640,304 · 10⁴⁰ = 157,156,403,040 · 10³⁹; adding D_e = 1,258,700 · 10¹⁸ gives the integer printed, and
21D_acc + 6 is 21 · 157,156,403,040 · 10³⁹ + 21 · 1,258,700 · 10¹⁸ + 6, that is
3,300,284,463,840 · 10³⁹ + 26,432,700 · 10¹⁸ + 6.
[[lem:uc-dr]] gives the same bound for d_R, its first line being the same and its single-step losses being at most
c_* < C_*; and d_R ≥ d_acc ([[thm:loss-d]]). By [[prop:uc-d-small]] (d), d_NM < D_acc, so d_NM ≤ D_NM, and the finer
bounds are [[lem:cs-sharp]] and (b), (c) there; the bounds for d_FM and d_Ψ are [[lem:uc-lambda]] (d).
N_NM = 21d_NM + 6 by [[thm:loss-d]], so N_NM ≤ 21D_NM + 6. The statements at the levels above 3 are
[[lem:uc-fourier-count]] and [[lem:cs-levels]] (b). [[eq:uc-lower]] is [[cor:uc-two-offsets]] (a),
whose hypothesis holds by (b) there. At the choice of [[def:uc-choice]], [[prop:ec-rounds]] gives
R > (1 − 3ε_K − 2δ̂ − δ̄)/(ε_Kδ̂), where 3ε_K + 2δ̂ + δ̄ < 1.98·10⁻⁸ and ε_Kδ̂ = 2.400249024·10⁻²⁴ < 2.40025·10⁻²⁴; so
3R > 3(1 − 1.98·10⁻⁸)/(2.40025·10⁻²⁴) > 1.2498·10²⁴, and 1.0072 · 1.2498 > 1.2587. ∎
```

New (69 lines):

```new
**Theorem {#thm:uc-integer}** (The loss d at the computational point.) At the computational point, with the index sets as
constructed, the admissible choice of the weights of [[def:uc-choice]] and the free orders and inner products of
[[def:cs-choices]], let c_* be the largest of the numbers c(β_k) (1 ≤ k ≤ K), c_b, c′_b and c_0 defined before
[[prop:ec-upper]] and c^Ψ(β_k), c^Ψ_b, c′^Ψ_b and c^Ψ_0 of [[lem:uc-dr]]: the largest loss that [[def:ec-accounted-loss]]
assigns to a single step outside the long iterations. Then c_* ≤ C_* < 1.89844·10³⁹ ([[prop:cs-cstar]]); at a level β ∈
(3, α], 1 + n_ι ≤ c(β) ≤ C_lev = 2N_ι + N̄_Λ + 529 < 6.32812·10³⁸, with N_ι of [[eq:uc-n-iota]] and N̄_Λ of
[[lem:uc-lambda]] ([[lem:cs-levels]]); and

    d_acc ≤ d_R ≤ D_acc,     d_NM ≤ D_NM,     N_NM = 21d_NM + 6 ≤ 21D_NM + 6,            {#eq:uc-integer}

where D_acc := D_♭ of [[eq:cs-sharp]] and D_NM := D_♭ + D′_* + d̄_Φ, with D′_* of [[rem:uc-small-reading]] and d̄_Φ of
[[lem:uc-lambda]] (d):

    D_acc = 37,862,223,260,395,633,917,123,246,147,912,828,863,693,156,076,559,963,974 < 3.78623·10⁵⁵,
    D_NM = 75,724,446,520,791,266,568,624,181,582,042,570,869,522,603,615,666,426,111 < 7.57245·10⁵⁵,
    21D_NM + 6 = 1,590,213,376,936,616,597,941,107,813,222,893,988,259,974,675,928,994,948,337 < 1.59022·10⁵⁷.

For the fixed seminorms of [[lem:uc-small-orders]] (d) also d_NM ≤ D_acc + D_* + d̄_Φ < 3.78623·10⁵⁵ ([[prop:uc-d-small]]
(b)). The losses of [[lem:iii-k-2-2]] and [[prop:iii-j2-4-3]] satisfy d_Ψ, d_FM ≤ 62N̄_Λ + 10 = 56,389,441,693,909,354.
Against these, for every admissible choice of the weights,

    d_NM ≥ d_acc ≥ 3R > 1.2497·10²⁴,     N_NM > 2.624·10²⁵,                                {#eq:uc-lower}

and at the choice of [[def:uc-choice]], 3R > 1.2251·10²⁷, so that D_e < 1.0072 · 3R.

*Proof.* By [[prop:cs-cstar]], c_* ≤ C_*. The bounds at the levels above 3 are [[lem:uc-fourier-count]] and
[[lem:cs-levels]] (b). By [[lem:cs-sharp]], d_acc ≤ D_♭ = D_acc and d_R ≤ D_acc, and d_R ≥ d_acc ([[thm:loss-d]]). By
[[prop:uc-d-small]] (c) and (d), d_NM ≤ D_♭ + D′_* + d̄_Φ = D_NM for the fixed seminorms of [[lem:uc-small-orders]] (d)
and for those of [[rem:uc-small-reading]], and (b) there gives the bound with D_*; the integers are those of
[[eq:cs-sharp]] and [[prop:uc-d-small]] (c). N_NM = 21d_NM + 6 by [[thm:loss-d]], so N_NM ≤ 21D_NM + 6. The bounds for
d_FM and d_Ψ are [[lem:uc-lambda]] (d). [[eq:uc-lower]] is [[cor:uc-two-offsets]] (a), whose hypothesis holds by (b)
there. At the choice of [[def:uc-choice]], [[prop:ec-rounds]] gives R > (1 − 3ε_K − 2δ̂ − δ̄)/(ε_Kδ̂), where 3ε_K + 2δ̂ +
δ̄ < 1.98·10⁻⁸ and ε_Kδ̂ = 2.448645858·10⁻²⁷ < 2.44865·10⁻²⁷; so 3R > 3(1 − 1.98·10⁻⁸)/(2.44865·10⁻²⁷) > 1.2251·10²⁷, and
1.0072 · 1.2251·10²⁷ > 1.23382·10²⁷ = D_e. ∎

**Proposition {#prop:uc-dependence}** (The bound as a function of the choice.) Let a choice be made as in
[[def:uc-choice]], except that ε_K and ε_+ are any numbers with 0 < ε_K < ε_+ < 10⁻¹³ for which it is admissible, and let
N̄_Λ ≥ N_Λ, k̄_0, J_* and l_* be integers for which [[lem:uc-lambda]] (b) and (c) hold, with J′ := (J_* + 1)(l_* + 1).
Put Δβ_0 := 0.999²ε_K and Δτ_0 := 0.999ε_Υ, L_<, L_> and R_b as in [[eq:uc-levels]], N_ι as in [[eq:uc-n-iota]], k̄_max
:= k̄_0 + J′N̄_Λ, d̄_Φ := 62N̄_Λ + 2, C_lev := 2N_ι + N̄_Λ + 529, I_lev := 34,268,829,852, I_base := 935R_b + 466 +
23,524,832(R_b + 3), T_12 := C_lev + I_lev + 4k̄_max + 24, R_base := 22,097 + I_base,

    F_1 := 3((1 + Δβ_0/2)² + (1 + ε_K + Δβ_0/2)²)/(2Δβ_0Δτ_0) + 3(3 + 2ε_K)/Δβ_0 + 6 + 4/Δτ_0 + 8
           + 3((1 + ε_K)/Δβ_0 + 1)((1 + ε_+)/𝔡₁ + 2) + 16(0.4901/𝔡₁ + 1)((3 + ε_K)/Δβ_0 + 5),
    C_* := 6N_ι + 3N̄_Λ + 3I_lev + 8k̄_max + I_base + d̄_Φ + (N̄_Λ + 2)(d̄_Φ + 30) + 45,862,
    D′_* := T_12 + 18 + 20,565,308,337L_< + (C_lev + I_lev − 9)L_> + 2R_base,
    D_acc := D_e + 497L_< + L_>C_lev + 935R_b + 466 + C_*,     D_NM := D_acc + D′_* + d̄_Φ,

with D_e any number at least F_1. Then d_acc ≤ d_R ≤ D_acc, d_NM ≤ D_NM and N_NM ≤ 21D_NM + 6. Each of N_ι, k̄_max, d̄_Φ,
C_lev, I_base, T_12, R_base, C_*, D′_* and D_acc − D_e is a polynomial with non-negative coefficients in N̄_Λ, k̄_0, J′,
L_<, L_> and R_b; L_<, L_> and R_b are non-increasing in ε_K, and F_1 is non-increasing in ε_K and non-decreasing in ε_+.
So, with D_e := F_1, D_acc and D_NM are non-decreasing in N̄_Λ, k̄_0, J′ and ε_+ and non-increasing in ε_K. Moreover
D_acc = L_>C_lev + D_e + 497L_< + 935R_b + 466 + C_*, and L_>C_lev > J′N̄_Λ(N̄_Λ + 1)(1 + ε_K)/Δβ_0: the bound is at
least quadratic in N̄_Λ and of the order 1/ε_K.

*Proof.* The proofs of [[prop:uc-explicit]], [[lem:cs-levels]], [[lem:cs-base]], [[lem:cs-iterations]], [[lem:cs-rest]],
[[prop:cs-cstar]], [[lem:cs-sharp]], [[lem:uc-small-orders]], [[rem:uc-small-reading]] and [[prop:uc-d-small]] use, of
the numbers of [[def:uc-choice]] and [[lem:uc-lambda]], only N_Λ ≤ N̄_Λ, k̄(λ_i) ≤ k̄_0 + J′i, Δβ ≥ Δβ_0, a♭_K − 2 ≥
Δβ_0, Δτ ≥ Δτ_0, ε_K < ε_+ < 10⁻¹³ and the bounds of [[lem:is-offsets]] (b); and they give d_acc, d_R ≤ D_acc and d_NM ≤
D_NM with the expressions above. F_1 is the bound for the first line of [[eq:ec-upper]] that [[eq:ec-upper-counts]],
[[eq:uc-t2-w]], ℓ⁺_tf = 1, r_ι ≤ 16 and η_2 − η_1 < ε_+ give, with N_< ≤ 1/Δβ_0, N_> ≤ (1 + ε_K)/Δβ_0 + 1 and N_b ≤
1/Δβ_0 + 1 ([[eq:ec-upper-counts]]): 3(T_< + T_> + T_2) + 4(1/Δτ + 2) + 16W(N_< + N_> + N_b + 3), 1/Δτ ≤ 1/Δτ_0, written
out; 1/𝔡₁ may be replaced by any upper bound. C_* is the right side of [[eq:cs-c0]] written out (1,587 + 44,227 + 48 =
45,862 and 2X_12 = 8k̄_max + 48), I_base is that of [[eq:cs-iterations]] (469R_b + 466(R_b + 1) = 935R_b + 466 and 16 ·
1,470,302 = 23,524,832), and 22,097 = 20,183 + 1,914. These are sums of products of N̄_Λ, k̄_0, J′, L_<, L_>, R_b and
positive constants, so they do not decrease when one of these integers increases. As ε_K increases, Δβ_0 increases, and
1/Δβ_0 and (1 + ε_K)/Δβ_0 = 1/Δβ_0 + 1/0.998001 decrease, and so do their integer parts; each term of F_1 is
non-increasing in ε_K, as x ↦ (1 + cx)²/x decreases on (0, 1/c) and (1 + ε_K)/Δβ_0 and (3 + ε_K)/Δβ_0 decrease, and ε_+
enters F_1 only through the factor 1 + ε_+. Finally C_lev > 2N_ι ≥ J′N̄_Λ(N̄_Λ + 1) and L_> > (1 + ε_K)/Δβ_0. ∎
```

### M13. rem:uc-missing, 71-explicit-constants.md lines 2798–2823

Old (26 lines):

```old
**Remark {#rem:uc-missing}** (What the integer bound rests on.) The counts of [[prop:ec-upper]] need two statements at
the computational point, and both are established. (IS): the exponents of real part at most 5 of ℰ_ind (with its
enlargements in [[sec:iii-i8-1]] and [[sec:iii-i9-1]]), ℰ^ι_ind and the least ℰ^C_I, and those of the least ℰ_++ below
2λ_♯, as the constructions of [[sec:uc-index-sets]] give them, with bounds for their logarithmic orders, and the
multiplicities of the indicial roots of L̂_b(0) ([[prop:is-ind]], [[prop:is-logs]], [[prop:is-iota]],
[[prop:is-ci-pp]], [[prop:is-mult]]). (SP): the orders of the poles of N_ι⁺(L̄, ·)⁻¹ at real part at most 5, all equal
to 1 ([[thm:sp-spectrum]], [[cor:sp-lstar]]). With them (G), N_Λ, k̄_0, l_*, J_* and every number of steps of the long
iterations are explicit ([[thm:is-gap]], [[prop:is-count]], [[lem:uc-lambda]], [[prop:uc-explicit]]), and so is a bound
for the count n(E, w) of every index set whose exponents below 3 + ε_+ lie in Λ with the logarithmic orders k̄(λ)
([[lem:uc-n-iota]]), which [[lem:iii-i10-1-2]] (c) and [[lem:iii-i13-1-3]] (b) assert of every exponent that the level
steps produce.

The single-step losses are bounded in [[sec:cs]], which lists the factors of each composition: for the level steps
those of [[lem:iii-i8-3-2]] and [[lem:iii-i13-2-2]], with the steps of [[prop:iii-i10-3-1]], [[prop:iii-i11-3-1]] and
[[prop:iii-i13-2-1]] outside the long iterations, and the background terms of Step 2 of the proof of
[[thm:iii-i14-3-1]] ([[lem:cs-levels]]); one round of [[prop:iii-i5-2-1]] and one step of [[prop:iii-i2-5-1]]
([[lem:cs-base]]); and Steps 0, 1, 3, 4′ and 4 of that proof, U ↦ Φ(U) and Steps 1–3 of the proof of
[[thm:iii-j1-2-1]], with their counterparts for ℛ(U) ([[lem:cs-rest]]). The closed forms are evaluated at the free
choices of [[def:cs-choices]]: the regularity order s_c = 3 > ½ + ϑ_ℋ and the inner products in which ϑ_in = 0 and
ϑ_ℋ < 9/4 ([[lem:cs-transforms]]). The count of the K⁺-exponents in the application of [[prop:iii-a-4-2]] (2) in Step 7
of the proof of [[prop:iii-i11-3-1]] is at most N_ι + N_Λ ([[lem:cs-fourier]]). So M_c C_* is of the order of 10⁵⁰, far
above D_e: the bound counts every logarithmic term that k̄(λ) allows, and a bound for c_* of the order of D_e/M_c needs
the logarithmic orders that the level steps produce, which this paper bounds only by k̄(λ) ([[rem:cs-sharpness]]). The
bound for d_NM rests in addition on the orders of the smallness conditions, which [[lem:uc-small-orders]] bounds for
the fixed seminorms of its (d), and [[rem:uc-small-reading]] for the larger ones that [[sec:iii-i8-1]] describes
([[prop:uc-d-small]]).
```

New (27 lines):

```new
**Remark {#rem:uc-missing}** (What the integer bound rests on.) The counts of [[prop:ec-upper]] need two statements at
the computational point, and both are established. (IS): the exponents of real part at most 5 of ℰ_ind (with its
enlargements in [[sec:iii-i8-1]] and [[sec:iii-i9-1]]), ℰ^ι_ind and the least ℰ^C_I, and those of the least ℰ_++ below
2λ_♯, as the constructions of [[sec:uc-index-sets]] give them, with bounds for their logarithmic orders, the
multiplicities of the indicial roots of L̂_b(0), and the indicial roots of L̂_b(0) of real part in (0, 3), which enter Λ
through the generators 1 + 𝒵 ([[prop:is-ind]], [[prop:is-logs]], [[prop:is-iota]], [[prop:is-ci-pp]],
[[prop:is-mult]], [[prop:is-lambda]]). (SP): the orders of the poles of N_ι⁺(L̄, ·)⁻¹ at real part at most 5, all equal
to 1 ([[thm:sp-spectrum]], [[cor:sp-lstar]]). With them (G), N_Λ, k̄_0, l_*, J_* and every number of steps of the long
iterations are explicit ([[thm:is-gap]], [[prop:is-count]], [[lem:uc-lambda]], [[prop:uc-explicit]]), and so is a bound
for the count n(E, w) of every index set whose exponents below 3 + ε_+ lie in Λ with the logarithmic orders k̄(λ)
([[lem:uc-n-iota]]), which [[lem:iii-i10-1-2]] (c) and [[lem:iii-i13-1-3]] (b) assert of every exponent that the level
steps produce.

The single-step losses are bounded in [[sec:cs]], which lists the factors of each composition: for the level steps
those of [[lem:iii-i8-3-2]] and [[lem:iii-i13-2-2]], with the steps of [[prop:iii-i10-3-1]], [[prop:iii-i11-3-1]] and
[[prop:iii-i13-2-1]] outside the long iterations, and the background terms of Step 2 of the proof of [[thm:iii-i14-3-1]]
([[lem:cs-levels]]); one round of [[prop:iii-i5-2-1]] and one step of [[prop:iii-i2-5-1]] ([[lem:cs-base]]); and Steps 0,
1, 3, 4′ and 4 of that proof, U ↦ Φ(U) and Steps 1–3 of the proof of [[thm:iii-j1-2-1]], with their counterparts for ℛ(U)
([[lem:cs-rest]]). The closed forms are evaluated at the free choices of [[def:cs-choices]]: the regularity order s_c =
3 > ½ + ϑ_ℋ and the inner products in which ϑ_in = 0 and ϑ_ℋ < 9/4 ([[lem:cs-transforms]]). The count of the K⁺-exponents
in the application of [[prop:iii-a-4-2]] (2) in Step 7 of the proof of [[prop:iii-i11-3-1]] is at most N_ι + N_Λ
([[lem:cs-fourier]]). So the levels above 3 carry the bound: at most L_> = 59,831,791,007,643,520 of them, each charged
at most C_lev < 6.32812·10³⁸, make all of D_acc but less than 1.9·10³⁹ ([[lem:cs-sharp]]), far above D_e. C_lev counts
every logarithmic term that k̄(λ) allows, and a bound for it of a smaller order needs the logarithmic orders that the
level steps produce, which this paper bounds only by k̄(λ) ([[rem:cs-sharpness]]). The bound for d_NM rests in addition
on the orders of the smallness conditions, which [[lem:uc-small-orders]] bounds for the fixed seminorms of its (d), and
[[rem:uc-small-reading]] for the larger ones that [[sec:iii-i8-1]] describes ([[prop:uc-d-small]]).
```

### M14. sec:cs, opening paragraphs, 71-explicit-constants.md lines 4094–4112

Old (19 lines):

```old
[[thm:uc-integer]] bounds d_acc and d_R by D_e + M_c c_*, where c_* is the largest of the numbers c(β_k), c_b, c′_b and
c_0 defined before [[prop:ec-upper]] and of their counterparts c^Ψ(β_k), c^Ψ_b, c′^Ψ_b and c^Ψ_0 of [[lem:uc-dr]]. Each
of these numbers is assigned by [[def:ec-accounted-loss]] to a finite composition of elementary families. This section
lists, step by step, the families that each of them composes, bounds the charge of every one of them at the choice of
[[def:uc-choice]], and adds the charges. Two counts of index sets dominate the result: the count n_ι of the Fourier
transform in Step 0 of the proof of [[prop:iii-i11-3-1]], at most N_ι by [[lem:uc-n-iota]], and the count n_K of the
K⁺-exponents of the inverse transform in its Step 7, at most N_ι + N_Λ ([[lem:cs-fourier]]). A level step below 3 is
charged at most 497, a round and a step of the base at most 469 and 466, a level step above 3 at most
C_lev = 2N_ι + N̄_Λ + 529, with the bound N̄_Λ ≥ N_Λ below ([[lem:cs-levels]], [[lem:cs-base]]), and c_0, whose bound
counts three runs of the top level, less than 6N_ι + 1.74·10²⁸ ([[lem:cs-rest]]). So c_* < 6.4368·10³⁵
([[prop:cs-cstar]]).

Throughout we write

    N̄_Λ := 16,747,199,999,999,     k̄_max := 3 + 765,000,816 · N̄_Λ = 12,811,621,665,714,434,999,187,

so that N_Λ ≤ N̄_Λ and k̄(λ) ≤ k̄_max for every λ ∈ Λ with Re λ < 3 + ε_+ ([[lem:uc-lambda]] (a), (c)), and N_ι is the
number of [[eq:uc-n-iota]]. Weights, levels and the loss ε are those of [[def:uc-choice]]; in particular
3 + ε_+ < ℓ_I < 3.5, α ≤ 4 + ε_K, and ε ≤ 10⁻³ε_g < 10⁻¹².
```

New (16 lines):

```new
[[thm:uc-integer]] bounds d_acc and d_R through the numbers c(β_k), c_b, c′_b and c_0 defined before [[prop:ec-upper]]
and their counterparts c^Ψ(β_k), c^Ψ_b, c′^Ψ_b and c^Ψ_0 of [[lem:uc-dr]], and through c_*, the largest of them. Each of
these numbers is assigned by [[def:ec-accounted-loss]] to a finite composition of elementary families. This section
lists, step by step, the families that each of them composes, bounds the charge of every one of them at the choice of
[[def:uc-choice]], and adds the charges. Two counts of index sets dominate the result: the count n_ι of the Fourier
transform in Step 0 of the proof of [[prop:iii-i11-3-1]], at most N_ι by [[lem:uc-n-iota]], and the count n_K of the
K⁺-exponents of the inverse transform in its Step 7, at most N_ι + N_Λ ([[lem:cs-fourier]]). A level step below 3 is
charged at most 497, a round and a step of the base at most 469 and 466, a level step above 3 at most C_lev = 2N_ι +
N̄_Λ + 529 ([[lem:cs-levels]], [[lem:cs-base]]), and c_0, whose bound counts three runs of the top level, less than
6N_ι + 5.13·10³¹ ([[lem:cs-rest]]). So c_* ≤ C_* < 1.89844·10³⁹ ([[prop:cs-cstar]]), and the levels above 3 give the
bound of [[lem:cs-sharp]].

Throughout, N̄_Λ, J′, k̄_max and d̄_Φ are the numbers of [[lem:uc-lambda]], so that N_Λ ≤ N̄_Λ and k̄(λ) ≤ k̄_max for
every λ ∈ Λ with Re λ < 3 + ε_+, N_ι is the number of [[eq:uc-n-iota]], and L_<, L_> and R_b are those of
[[eq:uc-levels]]. Weights, levels and the loss ε are those of [[def:uc-choice]]; in particular 3 + ε_+ < ℓ_I < 3.5, α ≤
4 + ε_K, and ε ≤ 10⁻³ε_g < 10⁻¹².
```

### M15a. lem:cs-fourier (b), proof, first place, 71-explicit-constants.md lines 4396–4398

Old (3 lines):

```old
[[lem:iii-i13-1-3]] (b)). As Λ ∩ {Re ≤ 3 + ε_+} is real ([[prop:is-lambda]]) and meets (2, 2 + ε_K] in no point ((G)),
and as the roots of the table are real, and those with −1 < μ < 0 have −μ ≥ ε_ind > ε_K by [[eq:iii-f1-2-2]]
([[sec:iii-g4-1]], [[eq:iii-i9-1-1]]), a term of real part below
```

New (3 lines):

```new
[[lem:iii-i13-1-3]] (b)). As the elements of Λ of real part at most 2.514 are real ([[prop:is-lambda]]), as Λ meets {2 <
Re ≤ 2 + ε_K} in no point ((G)), and as the roots of the table are real, and those with −1 < μ < 0 have −μ ≥ ε_ind > ε_K
by [[eq:iii-f1-2-2]] ([[sec:iii-g4-1]], [[eq:iii-i9-1-1]]), a term of real part below
```

### M15b. lem:cs-fourier (b), proof, second place, 71-explicit-constants.md lines 4402–4406

Old (5 lines):

```old
of E_K − 1 of real part below 1 + ε_K is (λ − 2, m) with λ ∈ Λ, 2 ≤ λ < 3 + ε_+, and m ≤ k̄(λ) + 1, where at degree 1
we use k̄(2) ≤ k̄(3) and 2, 3 ∈ Λ. The ℕ₀-shifts add nothing below 1 + ε_K except at the degree 0 + 1 = 1, as every other
degree has real part above ε_K. Hence, with λ_1 < ⋯ < λ_(N_Λ) as in [[lem:uc-lambda]] (c),

    n_K ≤ Σ_(i≤N_Λ) (k̄(λ_i) + 2) = N_Λ + 4N_Λ + 765,000,816 · N_Λ(N_Λ + 1)/2 ≤ N_Λ + N_ι
```

New (5 lines):

```new
of E_K − 1 of real part below 1 + ε_K is (λ − 2, m) with λ ∈ Λ, 2 ≤ Re λ < 3 + ε_+, and m ≤ k̄(λ) + 1, where at degree 1
we use k̄(2) ≤ k̄(3) and 2, 3 ∈ Λ. The ℕ₀-shifts add nothing below 1 + ε_K except at the degree 0 + 1 = 1, as every other
degree has real part above ε_K. Hence, with λ_1, …, λ_(N_Λ) as in [[lem:uc-lambda]] (c),

    n_K ≤ Σ_(i≤N_Λ) (k̄(λ_i) + 2) ≤ N_Λ + (k̄_0 + 1)N_Λ + J′N_Λ(N_Λ + 1)/2 ≤ N_Λ + N_ι
```

### M16. lem:cs-levels (b), the display, 71-explicit-constants.md lines 4417–4417

Old (1 lines):

```old
    c(β_k) ≤ C_lev := 2N_ι + N̄_Λ + 529 = 214,558,790,360,052,785,818,485,009,600,000,520.            {#eq:cs-clev}
```

New (1 lines):

```new
    c(β_k) ≤ C_lev := 2N_ι + N̄_Λ + 529 = 632,811,129,714,614,885,796,976,268,758,886,545,633.    {#eq:cs-clev}
```

### M17. lem:cs-iterations, statement, 71-explicit-constants.md lines 4488–4492

Old (5 lines):

```old
**Lemma {#lem:cs-iterations}** (Iterations charged in full.) Put R_b := 61,038,200,000,000 and

    I_lev := 16 · 1,470,302 + 3 + 3 · 3,000,004 + 5 · 6,847,261,001 = 34,268,829,852,
    I_base := 469 R_b + 466 (R_b + 1) + 16 · 1,470,302 · (R_b + 3)
            = 1,435,970,471,299,470,574,962.                                                          {#eq:cs-iterations}
```

New (5 lines):

```new
**Lemma {#lem:cs-iterations}** (Iterations charged in full.) With R_b of [[eq:uc-levels]] put

    I_lev := 16 · 1,470,302 + 3 + 3 · 3,000,004 + 5 · 6,847,261,001 = 34,268,829,852,
    I_base := 469 R_b + 466 (R_b + 1) + 16 · 1,470,302 · (R_b + 3)
            = 1,407,588,774,438,516,741,154,802.                                      {#eq:cs-iterations}
```

### M18. lem:cs-rest, statement, 71-explicit-constants.md lines 4524–4524

Old (1 lines):

```old
with d_Φ = 62N_Λ + 2 ≤ 1,038,326,399,999,940, and the same bound holds for c^Ψ_0 and at a rotating black hole parameter.
```

New (2 lines):

```new
with d_Φ = 62N_Λ + 2 ≤ d̄_Φ ([[lem:uc-lambda]] (d)), and the same bound holds for c^Ψ_0 and at a rotating black hole
parameter.
```

### M19. lem:cs-rest, proof, 71-explicit-constants.md lines 4573–4573

Old (1 lines):

```old
*The map U ↦ Φ(U)* has the loss d_Φ of [[lem:uc-phi-loss]], at most 1,038,326,399,999,940 ([[lem:uc-lambda]] (d)).
```

New (2 lines):

```new
*The map U ↦ Φ(U)* has the loss d_Φ of [[lem:uc-phi-loss]], at most d̄_Φ = 56,389,441,693,909,346 ([[lem:uc-lambda]]
(d)).
```

### M20. prop:cs-cstar and rem:cs-sharpness, 71-explicit-constants.md lines 4592–4622

Old (31 lines):

```old
**Proposition {#prop:cs-cstar}** (The largest single-step loss.) At the computational point, with the index sets as
constructed and the choices of [[def:uc-choice]] and [[def:cs-choices]],

    c_* ≤ 6N_ι + 3N̄_Λ + 17,389,163,815,025,371,354,557,103,786
        = 643,676,388,469,322,172,480,826,383,357,103,759
        < C_* := 643,680,000,000,000,000,000,000,000,000,000,000 = 6.4368·10³⁵.                        {#eq:cs-cstar}

*Proof.* By [[lem:cs-levels]] and [[lem:cs-base]], c(β_k), c^Ψ(β_k) ≤ max(497, C_lev) = C_lev and c_b, c^Ψ_b ≤ 469,
c′_b, c′^Ψ_b ≤ 466. By [[lem:cs-rest]], c_0 and c^Ψ_0 are at most the right side of [[eq:cs-c0]]. With
C_lev = 2N_ι + N̄_Λ + 529, this is

    2 · 20,183 + 2 · 1,914 + 33 + 3C_lev + 3I_lev + 2X_12 + I_base + d_Φ + (N̄_Λ + 2)(d_Φ + 30)
        = 6N_ι + 3N̄_Λ + 1,587 + 44,227 + 102,806,489,556 + 102,492,973,325,715,479,993,544
          + 1,435,970,471,299,470,574,962 + 1,038,326,399,999,940 + 17,389,059,886,080,535,910,399,999,970,

with 3I_lev = 102,806,489,556, 2X_12 = 8k̄_max + 48 = 102,492,973,325,715,479,993,544 and
(N̄_Λ + 2)(d_Φ + 30) ≤ 16,747,200,000,001 · 1,038,326,399,999,970 = 17,389,059,886,080,535,910,399,999,970. The seven
numbers after 6N_ι + 3N̄_Λ add up to 17,389,163,815,025,371,354,557,103,786, and with
6N_ι = 643,676,371,080,158,357,455,404,787,199,999,976 and 3N̄_Λ = 50,241,599,999,997 the sum is the integer of
[[eq:cs-cstar]], which is less than C_*. This bound exceeds C_lev, 469 and 466, so it bounds c_*. ∎

**Remark {#rem:cs-sharpness}** (What the bound counts.) Of the bound of [[eq:cs-cstar]], all but less than 1.74·10²⁸
is 6N_ι (C_* itself exceeds 6N_ι by less than 3.63·10³⁰): two counts of the logarithmic terms of Λ below 3 + ε_+ in
each of the three runs of the top level counted in the bound for c_0, each count being taken at the bound k̄(λ) of
[[def:iii-i10-1-1]] for the logarithmic orders. The next term,
(N̄_Λ + 2)(d_Φ + 30) < 1.739·10²⁸, comes from Step 2 of the proof of [[thm:iii-j1-2-1]], whose chain passes through
every exponent of Λ_* and composes the map Φ at each. A level step above 3 is charged at most C_lev ≈ C_*/3, and c_0
enters the second line of [[eq:ec-upper]] once; bounding that line by K·C_lev + 469N_b + 466(N_b + 1) + C_*, with
K < 1.22077·10¹⁴ ([[rem:ec-upper-point]]), instead of by M_c C_*, gives d_acc, d_R < 2.62·10⁴⁹ ([[lem:cs-sharp]]). The
bound is crude in another way as well: n_ι and n_K count every pair (λ, k) with k ≤ k̄(λ), while the logarithmic
orders that the constructions produce are bounded in this paper only by k̄(λ).
```

New (30 lines):

```new
**Proposition {#prop:cs-cstar}** (The largest single-step loss.) At the computational point, with the index sets as
constructed and the choices of [[def:uc-choice]] and [[def:cs-choices]],

    c_* ≤ C_* := 6N_ι + 3N̄_Λ + 51,286,605,918,146,275,681,884,678,060,390
             = 1,898,433,440,430,450,575,537,204,488,161,337,695,702 < 1.89844·10³⁹.       {#eq:cs-cstar}

*Proof.* By [[lem:cs-levels]] and [[lem:cs-base]], c(β_k), c^Ψ(β_k) ≤ max(497, C_lev) = C_lev and c_b, c^Ψ_b ≤ 469, c′_b,
c′^Ψ_b ≤ 466. By [[lem:cs-rest]], c_0 and c^Ψ_0 are at most the right side of [[eq:cs-c0]]. With C_lev = 2N_ι + N̄_Λ +
529, this is

    2 · 20,183 + 2 · 1,914 + 33 + 3C_lev + 3I_lev + 2X_12 + I_base + d_Φ + (N̄_Λ + 2)(d_Φ + 30)
        ≤ 6N_ι + 3N̄_Λ + 1,587 + 44,227 + 102,806,489,556 + 5,566,189,536,725,815,534,196,808
          + 1,407,588,774,438,516,741,154,802 + 56,389,441,693,909,346 + 51,286,598,944,367,908,128,007,902,264,064,

with 3I_lev = 102,806,489,556, 2X_12 = 8k̄_max + 48 = 5,566,189,536,725,815,534,196,808, d_Φ ≤ d̄_Φ and (N̄_Λ + 2)(d_Φ +
30) ≤ 909,507,124,095,314 · 56,389,441,693,909,376 = 51,286,598,944,367,908,128,007,902,264,064. The seven numbers after
6N_ι + 3N̄_Λ add up to 51,286,605,918,146,275,681,884,678,060,390, and with 6N_ι =
1,898,433,389,143,844,657,390,926,077,755,287,349,376 and 3N̄_Λ = 2,728,521,372,285,936 the sum is the integer of
[[eq:cs-cstar]]. This bound exceeds C_lev, 469 and 466, so it bounds c_*. ∎

**Remark {#rem:cs-sharpness}** (What the bound counts.) Of the bound of [[eq:cs-cstar]], all but less than 5.13·10³¹ is
6N_ι: two counts of the logarithmic terms of Λ below 3 + ε_+ in each of the three runs of the top level counted in the
bound for c_0, each count being taken at the bound k̄(λ) of [[def:iii-i10-1-1]] for the logarithmic orders. The next
term, (N̄_Λ + 2)(d̄_Φ + 30) < 5.129·10³¹, comes from Step 2 of the proof of [[thm:iii-j1-2-1]], whose chain passes
through every exponent of Λ_* and composes the map Φ at each. A level step above 3 is charged at most C_lev, about C_*/3,
and c_0 enters the second line of [[eq:ec-upper]] once; the at most L_> levels above 3 carry the bound, L_>C_lev being
all of D_acc but less than 1.9·10³⁹ ([[lem:cs-sharp]]). The bound is crude in another way as well: n_ι and n_K count
every pair (λ, k) with k ≤ k̄(λ), while the logarithmic orders that the constructions produce are bounded in this paper
only by k̄(λ). Through N_ι, C_lev is quadratic in N̄_Λ and linear in J′ ([[eq:uc-n-iota]]), and L_> is about
1/(0.998001ε_K) ([[eq:uc-levels]]); [[prop:uc-dependence]] states the dependence.
```

### M21. sec:cs-small, the notation, 71-explicit-constants.md lines 4635–4640

Old (6 lines):

```old
Throughout, the point, the index sets and the choices are those of [[thm:uc-integer]]; N_ι, N̄_Λ, k̄_max, C_lev, R_b,
I_lev, I_base, X_12, T_11 and T_12 are the numbers of [[sec:cs]]; d_T = 20,180 is the loss of [[thm:iii-i-5-3]] at
every b ∈ ℬ̄_* ([[thm:fwd-loss]], [[cor:fwd-near-b0]]); ‖β‖_j = ‖h‖_(𝒳^j) + |p⃗| + ‖q‖_(𝒬^j) is the background norm of
[[sec:iii-j2-1]]; and

    K̄ := 122,076,389,376,829,     R_base := 20,183 + 1,914 + I_base = 1,435,970,471,299,470,597,059.
```

New (6 lines):

```new
Throughout, the point, the index sets and the choices are those of [[thm:uc-integer]]; N_ι, N̄_Λ, k̄_max, C_lev, L_<,
L_>, R_b, I_lev, I_base, X_12, T_11 and T_12 are the numbers of [[sec:cs]]; d_T = 20,180 is the loss of
[[thm:iii-i-5-3]] at every b ∈ ℬ̄_* ([[thm:fwd-loss]], [[cor:fwd-near-b0]]); ‖β‖_j = ‖h‖_(𝒳^j) + |p⃗| + ‖q‖_(𝒬^j) is the
background norm of [[sec:iii-j2-1]]; and

    R_base := 20,183 + 1,914 + I_base = 1,407,588,774,438,516,741,176,899.
```

### M22. lem:cs-sharp, 71-explicit-constants.md lines 4652–4683

Old (32 lines):

```old
**Lemma {#lem:cs-sharp}** (The single-step losses summed level by level.) The number K of the levels β_1, …, β_K of
[[thm:iii-i14-3-1]] satisfies K ≤ K̄, and

    d_acc ≤ D_♭,     d_R ≤ D_♭,     D_♭ := D_e + K̄ C_lev + 469R_b + 466(R_b + 1) + C_*,
    D_♭ = 26,192,562,436,215,872,034,699,391,908,492,342,632,997,875,951,546 < 2.6193·10⁴⁹,          {#eq:cs-sharp}

with D_e and C_* of [[thm:uc-integer]].

*Proof.* *The levels.* At the choice of [[def:uc-choice]], α_1 = β_0 < β_1 < ⋯ < β_K = α, and every spacing
β_(k+1) − β_k is at least Δβ_0 ([[lem:uc-admissible]]); so KΔβ_0 ≤ α − α_1 < 2 + ε_K, as α ≤ 4 + ε_K and α_1 > 2.
With ε_K = 16,416·10⁻¹⁸ and Δβ_0 = 16,383,184,416·10⁻²⁴ ([[eq:uc-deltas]]), (2 + ε_K)/Δβ_0 is
2,000,000,000,000,016,416,000,000/16,383,184,416, and

    16,383,184,416 · 122,076,389,376,829 = 2,000,000,000,000,012,824,296,864,
    16,383,184,416 · 122,076,389,376,830 = 2,000,000,000,000,029,207,481,280;

so K < 122,076,389,376,830, that is, K ≤ K̄.

*The bound.* By [[lem:uc-admissible]] and [[lem:uc-gaps]], [[prop:ec-upper]] holds with the T_2 and W of
[[eq:uc-t2-w]], and its first line is less than D_e ([[prop:uc-explicit]]). Its second line is
Σ_k c(β_k) + N_b c_b + (N_b + 1)c′_b + c_0. There every c(β_k) is at most max(497, C_lev) = C_lev ([[lem:cs-levels]]),
c_b ≤ 469 and c′_b ≤ 466 ([[lem:cs-base]]), and c_0 is at most the integer of [[eq:cs-cstar]], which is less than C_*
([[lem:cs-rest]], [[prop:cs-cstar]]). The number N_b of [[lem:ec-counts]] (f) is at most 1/Δβ_0 + 1
([[eq:ec-upper-counts]]), and 16,383,184,416 · 61,038,194,688,415 > 10²⁴, so N_b < 61,038,194,688,416 < R_b. Hence
the second line is at most K̄C_lev + 469R_b + 466(R_b + 1) + C_*, and d_acc ≤ D_♭. By [[lem:uc-dr]], d_R satisfies
[[eq:ec-upper]] with the same first line and with c^Ψ(β_k), c^Ψ_b, c′^Ψ_b and c^Ψ_0 in place of c(β_k), c_b, c′_b and
c_0; these satisfy the same bounds ([[lem:cs-levels]], [[lem:cs-base]], [[lem:cs-rest]]), so d_R ≤ D_♭.

*The integer.* K̄C_lev = 26,192,562,436,215,228,354,699,390,649,792,285,562,280,875,951,080, and
469R_b + 466(R_b + 1) = 28,626,915,800,000,000 + 28,443,801,200,000,466 = 57,070,717,000,000,466. Adding these,
D_e = 1,258,700,000,000,000,000,000,000 and C_* = 643,680,000,000,000,000,000,000,000,000,000,000 gives the integer of
[[eq:cs-sharp]], whose leading digits are 2.619256. ∎
```

New (21 lines):

```new
**Lemma {#lem:cs-sharp}** (The single-step losses summed level by level.) With D_e, L_<, L_> and R_b of
[[prop:uc-explicit]] and C_* of [[prop:cs-cstar]],

    d_acc ≤ D_♭,     d_R ≤ D_♭,     D_♭ := D_e + 497L_< + L_>C_lev + 469R_b + 466(R_b + 1) + C_*,
    D_♭ = 37,862,223,260,395,633,917,123,246,147,912,828,863,693,156,076,559,963,974 < 3.78623·10⁵⁵.    {#eq:cs-sharp}

*Proof.* *The bound.* By [[lem:uc-admissible]] and [[lem:uc-gaps]], [[prop:ec-upper]] holds with the T_2 and W of
[[eq:uc-t2-w]], and its first line is less than D_e ([[prop:uc-explicit]]). Its second line is Σ_k c(β_k) + N_b c_b +
(N_b + 1)c′_b + c_0. Of the levels β_1, …, β_K, at most L_< lie in (2, 3), where c(β_k) ≤ 497, and at most L_> in (3, α],
where c(β_k) ≤ C_lev ([[prop:uc-explicit]], [[lem:cs-levels]]); every level lies in one of the two intervals, as all
exceed α_1 > 2 and none equals 3. So Σ_k c(β_k) ≤ 497L_< + L_>C_lev. Further c_b ≤ 469 and c′_b ≤ 466 ([[lem:cs-base]]),
N_b < R_b ([[prop:uc-explicit]]), and c_0 ≤ C_* ([[lem:cs-rest]], [[prop:cs-cstar]]). Hence the second line is at most
497L_< + L_>C_lev + 469R_b + 466(R_b + 1) + C_*, and d_acc ≤ D_♭. By [[lem:uc-dr]], d_R satisfies [[eq:ec-upper]] with
the same first line and with c^Ψ(β_k), c^Ψ_b, c′^Ψ_b and c^Ψ_0 in place of c(β_k), c_b, c′_b and c_0; these satisfy the
same bounds ([[lem:cs-levels]], [[lem:cs-base]], [[lem:cs-rest]]), so d_R ≤ D_♭.

*The integer.* L_>C_lev = 37,862,223,260,395,632,018,689,805,716,228,433,240,809,543,192,276,748,160, 497L_< =
29,736,400,130,798,828,446, and 469R_b + 466(R_b + 1) = 28,061,109,982,584,810,880 + 27,881,614,609,561,880,786 =
55,942,724,592,146,691,666. Adding these, D_e = 1,233,820,000,000,000,000,000,000,000 and C_* =
1,898,433,440,430,450,575,537,204,488,161,337,695,702 gives the integer of [[eq:cs-sharp]], whose leading digits are
3.786222. ∎
```

### M23a. lem:uc-small-orders (b), 71-explicit-constants.md lines 4698–4700

Old (3 lines):

```old
(b) in [[eq:s20-d]] one may take k_1 = 10 and k_0 = k̄_0 := 20,602 + 466R_b = 28,443,801,200,020,602, and so the d of
[[eq:s20-d]] equal to k̄_0 + 2; the conditions of [[ch:s20]] then have order k̄_0 + 2, and k̄_0 + 5 at the backgrounds
h + h_rem(q) + h_tot(p⃗);
```

New (3 lines):

```new
(b) in [[eq:s20-d]] one may take k_1 = 10 and k_0 = k̄_0 := 20,602 + 466R_b = 27,881,614,609,561,900,922, and so the d of
[[eq:s20-d]] equal to k̄_0 + 2; the conditions of [[ch:s20]] then have order k̄_0 + 2, and k̄_0 + 5 at the backgrounds
h + h_rem(q) + h_tot(p⃗);
```

### M23b. lem:uc-small-orders (e), the display, 71-explicit-constants.md lines 4715–4715

Old (1 lines):

```old
    D_* := T_12 + 14 = 214,558,790,360,104,032,305,147,901,608,827,158 < 2.14559·10³⁵,               {#eq:uc-small}
```

New (1 lines):

```new
    D_* := T_12 + 14 = 632,811,129,714,617,668,891,744,631,700,922,473,903 < 6.32812·10³⁸,    {#eq:uc-small}
```

### M23c. lem:uc-small-orders, proof of (e), 71-explicit-constants.md lines 4830–4842

Old (13 lines):

```old
*(e)* The orders of (a)–(c) are at most 2R_base + 16 = 2,871,940,942,598,941,194,134, which is less than T_12. Those of
(d) are at most ρ + 14 < T_12 + 14, or ρ + R_base + 16. Of the conditions of (d), one read at a reference point
(0, p⃗_b) with b ≠ b₀ occurs only at a level, where ρ ≤ C_lev − 11 + I_lev: Step 4′ is a step of [[thm:iii-i14-3-1]],
at b₀, and at a rotating b [[prop:iii-i15-2-5]] has no Step 4′ ([[sec:s23-base-points]]), its rotation coordinates
being the A_b read at the levels. So ρ + R_base + 16 ≤ C_lev + I_lev + R_base + 5 < T_12 + 14, as
X_12 = 51,246,486,662,857,739,996,772 exceeds R_base. The convention "h small" of [[sec:iii-i7-1]], kept in
[[sec:iii-i8-1]], in [[sec:iii-i9-1]] and so at the base points of [[ch:s22]], and the convention "q small" of
[[sec:iii-i14-1]] each fix one order for all their uses: the largest of the orders that those uses ask. The uses lie
in the bases, at the levels and in Steps 4′ and 4, and each asks an order that (a)–(d) bound, by (F1) at the
regularity of its seminorm. So every order is at most D_*, and so is their largest, d_*. The order m of the proof of
[[lem:iii-k-2-3]] is the largest regularity ρ of the seminorms in which the proof of [[lem:iii-j2-2-3]] asks R_j → 0,
and the condition asked in that seminorm has an order at least m + 14 by (c) and (d); so m + 14 ≤ d_*. The integer:
T_12 = C_lev + I_lev + X_12 = 214,558,790,360,104,032,305,147,901,608,827,144, and D_* = T_12 + 14. ∎
```

New (13 lines):

```new
*(e)* The orders of (a)–(c) are at most 2R_base + 16 = 2,815,177,548,877,033,482,353,814, which is less than T_12. Those
of (d) are at most ρ + 14 < T_12 + 14, or ρ + R_base + 16. Of the conditions of (d), one read at a reference point (0,
p⃗_b) with b ≠ b₀ occurs only at a level, where ρ ≤ C_lev − 11 + I_lev: Step 4′ is a step of [[thm:iii-i14-3-1]], at b₀,
and at a rotating b [[prop:iii-i15-2-5]] has no Step 4′ ([[sec:s23-base-points]]), its rotation coordinates being the A_b
read at the levels. So ρ + R_base + 16 ≤ C_lev + I_lev + R_base + 5 < T_12 + 14, as X_12 =
2,783,094,768,362,907,767,098,404 exceeds R_base. The convention "h small" of [[sec:iii-i7-1]], kept in [[sec:iii-i8-1]],
in [[sec:iii-i9-1]] and so at the base points of [[ch:s22]], and the convention "q small" of [[sec:iii-i14-1]] each fix
one order for all their uses: the largest of the orders that those uses ask. The uses lie in the bases, at the levels and
in Steps 4′ and 4, and each asks an order that (a)–(d) bound, by (F1) at the regularity of its seminorm. So every order
is at most D_*, and so is their largest, d_*. The order m of the proof of [[lem:iii-k-2-3]] is the largest regularity ρ
of the seminorms in which the proof of [[lem:iii-j2-2-3]] asks R_j → 0, and the condition asked in that seminorm has an
order at least m + 14 by (c) and (d); so m + 14 ≤ d_*. The integer: T_12 = C_lev + I_lev + X_12 =
632,811,129,714,617,668,891,744,631,700,922,473,889, and D_* = T_12 + 14. ∎
```

### M24. rem:uc-small-reading, 71-explicit-constants.md lines 4844–4862

Old (19 lines):

```old
**Remark {#rem:uc-small-reading}** (Fixed seminorms that also bound the remainders.) [[sec:iii-i8-1]] takes the
regularity of its fixed seminorm so large that the maps from the forcing to the coefficients and to the remainder are
bounded in it, and [[lem:iii-i11-3-2]] chooses its seminorms in the same way. If this is required at every level, the
regularities grow downwards through the levels, and d_* is still bounded. Let ρ_k be the regularity of the fixed
seminorm of the forcing class of the step from β_(k−1) to β_k. The step maps the forcing to the remainder ũ ∈ 𝒵_(β_k),
which is measured in the seminorm of the hypothesis of the next step, and that seminorm must bound (L − L_b)u and R_qu
in the seminorm of the next forcing class, two orders lower. The remainder map is part of the step, so by
[[lem:cs-iterations]] (a), and the count in the proof of [[lem:uc-small-orders]] (d) for the levels below 3,
ρ_k ≤ ρ_(k+1) + 2 + C_lev − 11 + I_lev, and ρ_K ≤ T_12 + 2 + C_lev − 11 + I_lev,
Step 4′ reading the solution at α at an order below T_12 + 2. So ρ_k ≤ T_12 + K̄(C_lev + I_lev − 9) for every k, by
[[lem:cs-sharp]]. The norms of the base must bound its maps into the seminorm of the hypothesis of the first step, so
they are needed at regularities at most ρ_1 + 2 + R_base, and at most ρ_1 + 2R_base + 4 with the terms at a reference
point (0, p⃗_b). By (F1)–(F3) and the proofs of (c)–(e), every order is then at most

    D′_* := T_12 + 18 + K̄(C_lev + I_lev − 9) + 2R_base
         = 26,192,562,436,215,442,913,489,754,940,111,547,055,147,233,880,207 < 2.6193·10⁴⁹,

and d_* ≤ D′_*. Here K̄(C_lev + I_lev − 9) = 26,192,562,436,215,228,354,699,394,833,207,300,964,646,683,858,927, to which
T_12 + 18 and 2R_base = 2,871,940,942,598,941,194,118 are added.
```

New (21 lines):

```new
**Remark {#rem:uc-small-reading}** (Fixed seminorms that also bound the remainders.) [[sec:iii-i8-1]] takes the
regularity of its fixed seminorm so large that the maps from the forcing to the coefficients and to the remainder are
bounded in it, and [[lem:iii-i11-3-2]] chooses its seminorms in the same way. If this is required at every level, the
regularities grow downwards through the levels, and d_* is still bounded. Let ρ_k be the regularity of the fixed seminorm
of the forcing class of the step from β_(k−1) to β_k. The step maps the forcing to the remainder ũ ∈ 𝒵_(β_k), which is
measured in the seminorm of the hypothesis of the next step, and that seminorm must bound (L − L_b)u and R_qu in the
seminorm of the next forcing class, two orders lower. The remainder map is part of the step, so ρ_k ≤ ρ_(k+1) + 2 +
C_lev − 11 + I_lev when β_k > 3, by [[lem:cs-iterations]] (a), and ρ_k ≤ ρ_(k+1) + 2 + 497 + 23,524,832 +
20,541,783,006 = ρ_(k+1) + 20,565,308,337 when β_k < 3, by the count in the proof of [[lem:uc-small-orders]] (d); and ρ_K
≤ T_12 + 2 + C_lev − 11 + I_lev, Step 4′ reading the solution at α at an order below T_12 + 2. At most L_< of the levels
lie below 3 and at most L_> above ([[prop:uc-explicit]]), so ρ_k ≤ T_12 + 20,565,308,337L_< + (C_lev + I_lev − 9)L_> for
every k. The norms of the base must bound its maps into the seminorm of the hypothesis of the first step, so they are
needed at regularities at most ρ_1 + 2 + R_base, and at most ρ_1 + 2R_base + 4 with the terms at a reference point (0,
p⃗_b). By (F1)–(F3) and the proofs of (c)–(e), every order is then at most

    D′_* := T_12 + 18 + 20,565,308,337L_< + (C_lev + I_lev − 9)L_> + 2R_base
         = 37,862,223,260,395,632,651,500,935,434,129,742,005,773,058,097,412,552,791 < 3.78623·10⁵⁵,

and d_* ≤ D′_*. Here 20,565,308,337L_< = 1,230,459,230,427,132,871,449,409,566 and (C_lev + I_lev − 9)L_> =
37,862,223,260,395,632,018,689,805,718,278,798,706,052,416,491,558,315,520, to which T_12 + 18 =
632,811,129,714,617,668,891,744,631,700,922,473,907 and 2R_base = 2,815,177,548,877,033,482,353,798 are added.
```

### M25a. prop:uc-d-small (b)-(d), 71-explicit-constants.md lines 4876–4884

Old (9 lines):

```old
(b) for the fixed seminorms of [[lem:uc-small-orders]] (d), d_NM ≤ D_♭ + D_* + 1,038,326,399,999,940 =
26,192,562,436,216,086,593,489,752,012,524,648,819,225,884,778,644, so d_NM < 2.6193·10⁴⁹, and N_NM = 21d_NM + 6 ≤
550,043,811,160,537,818,463,284,792,263,017,625,203,743,580,351,530 < 5.5005·10⁵⁰;

(c) for those of [[rem:uc-small-reading]], d_NM ≤ D_♭ + D′_* + 1,038,326,399,999,940 =
52,385,124,872,431,314,948,189,146,848,603,890,726,471,509,831,693 < 5.2386·10⁴⁹, and N_NM < 1.10009·10⁵¹;

(d) in either case d_NM < D_acc and N_NM < 21D_acc + 6, with D_acc of [[thm:uc-integer]]; and every lower bound for
d_acc and N_NM in this chapter holds for d_NM and N_NM.
```

New (10 lines):

```new
(b) for the fixed seminorms of [[lem:uc-small-orders]] (d), d_NM ≤ D_♭ + D_* + d̄_Φ =
37,862,223,260,395,634,549,934,375,862,530,497,755,494,177,219,176,347,223, so d_NM < 3.78623·10⁵⁵, and N_NM = 21d_NM + 6
≤ 795,106,688,468,308,325,548,621,893,113,140,452,865,377,721,602,703,291,689 < 7.9511·10⁵⁶;

(c) for those of [[rem:uc-small-reading]], d_NM ≤ D_♭ + D′_* + d̄_Φ =
75,724,446,520,791,266,568,624,181,582,042,570,869,522,603,615,666,426,111 < 7.57245·10⁵⁵, and N_NM ≤
1,590,213,376,936,616,597,941,107,813,222,893,988,259,974,675,928,994,948,337 < 1.59022·10⁵⁷;

(d) in either case d_NM ≤ D_NM and N_NM ≤ 21D_NM + 6, with D_NM := D_♭ + D′_* + d̄_Φ of [[thm:uc-integer]]; and every
lower bound for d_acc and N_NM in this chapter holds for d_NM and N_NM.
```

### M25b. prop:uc-d-small, proof of (b)-(d), 71-explicit-constants.md lines 4906–4920

Old (15 lines):

```old
(b) By [[lem:cs-sharp]], d_F ≤ d_R ≤ D_♭; by [[lem:uc-small-orders]] (e), d_* ≤ D_*; and d_Φ ≤ 1,038,326,399,999,940
([[lem:uc-lambda]] (d)). So both terms of [[eq:uc-d-small]] are at most D_♭ + D_* + 1,038,326,399,999,940, the
integer printed: D_♭ + D_* = 26,192,562,436,216,086,593,489,752,012,524,647,780,899,484,778,704, and adding
1,038,326,399,999,940 gives it. Its leading digits are 2.619256, and 21 times it plus 6 is the integer printed, with
leading digits 5.500438.

(c) is (b) with D′_*: D_♭ + D′_* = 52,385,124,872,431,314,948,189,146,848,603,889,688,145,109,831,753, and adding
1,038,326,399,999,940 gives the integer printed, with leading digits 5.238512; 21 times it plus 6 has the leading
digits 1.100087.

(d) D_acc = 157,156,403,040,000,000,000,000,001,258,700,000,000,000,000,000,000 exceeds the integer of (c) by
104,771,278,167,568,685,051,810,854,410,096,109,273,528,490,168,307, so d_NM < D_acc in either case, and
N_NM = 21d_NM + 6 < 21D_acc + 6. The lower bounds of [[thm:loss-d]] (ii), [[cor:uc-two-offsets]] and
[[thm:uc-integer]] are bounds for d_acc, carried to d_NM and N_NM by d_NM ≥ d_acc and N_NM = 21d_NM + 6; by (a) they
hold for the d_NM of [[eq:uc-d-small]]. ∎
```

New (13 lines):

```new
(b) By [[lem:cs-sharp]], d_F ≤ d_R ≤ D_♭; by [[lem:uc-small-orders]] (e), d_* ≤ D_*; and d_Φ ≤ d̄_Φ =
56,389,441,693,909,346 ([[lem:uc-lambda]] (d)). So both terms of [[eq:uc-d-small]] are at most D_♭ + D_* + d̄_Φ, the
integer printed: D_♭ + D_* = 37,862,223,260,395,634,549,934,375,862,530,497,755,437,787,777,482,437,877, and adding d̄_Φ
gives it. Its leading digits are 3.786222, and 21 times it plus 6 is the integer printed, with leading digits 7.951066.

(c) is (b) with D′_*: D_♭ + D′_* = 75,724,446,520,791,266,568,624,181,582,042,570,869,466,214,173,972,516,765, and adding
d̄_Φ gives the integer printed, with leading digits 7.572444; 21 times it plus 6 is the integer printed, with leading
digits 1.590213.

(d) D′_* ≥ D_*, as T_12 + 18 > T_12 + 14, so the integer of (c) is at least that of (b), and d_NM ≤ D_NM in either case;
then N_NM = 21d_NM + 6 ≤ 21D_NM + 6. The lower bounds of [[thm:loss-d]] (ii), [[cor:uc-two-offsets]] and
[[thm:uc-integer]] are bounds for d_acc, carried to d_NM and N_NM by d_NM ≥ d_acc and N_NM = 21d_NM + 6; by (a) they hold
for the d_NM of [[eq:uc-d-small]]. ∎
```

### M25c. after prop:uc-d-small, 71-explicit-constants.md lines 4922–4924

Old (3 lines):

```old
The bound (b) rests on [[lem:uc-small-orders]] (d), in which the fixed seminorms are those of the reads; (c) holds
under the larger reading of [[rem:uc-small-reading]]. The integer bound of [[thm:uc-integer]] for d_NM and N_NM holds
under both.
```

New (2 lines):

```new
The bound (b) rests on [[lem:uc-small-orders]] (d), in which the fixed seminorms are those of the reads; (c) holds under
the larger reading of [[rem:uc-small-reading]]. The bound D_NM of [[thm:uc-integer]] for d_NM and N_NM holds under both.
```

### M26a. prop:uc-data-order (d), 71-explicit-constants.md lines 5122–5130

Old (9 lines):

```old
(d) At the computational point, with the index sets as constructed and the choices of [[def:uc-choice]] and
[[def:cs-choices]], J ≤ 8; so L_P ≤ 39 in the class of [[eq:vii-0-1]] and L_P ≤ 44 in the class ℰ_0^½. With D_acc of
[[thm:uc-integer]],

    K ≤ 22D_acc + 345 = 3,457,440,866,880,000,000,000,000,027,691,400,000,000,000,000,000,345 < 3.45745·10⁵¹,

d_1 ≤ 22D_acc + 331 and N ≤ 22D_acc + 348. For the fixed seminorms of [[lem:uc-small-orders]] (d), K < 5.7624·10⁵⁰,
and for those of [[rem:uc-small-reading]], K < 1.15248·10⁵¹; and K > 22d > 2.7493·10²⁵. In the class ℰ_0^½,
k1 ≤ 22D_acc + 340 and 1.0078·10⁵¹ < K*(a, M, k1) < 4.78156·10¹⁰³ for every a ∈ (ℓ0 − 1, 3).
```

New (10 lines):

```new
(d) At the computational point, with the index sets as constructed and the choices of [[def:uc-choice]] and
[[def:cs-choices]], J ≤ 8; so L_P ≤ 39 in the class of [[eq:vii-0-1]] and L_P ≤ 44 in the class ℰ_0^½. With D_NM of
[[thm:uc-integer]],

    K ≤ 22D_NM + 345
      = 1,665,937,823,457,407,864,509,731,994,804,936,559,129,497,279,544,661,374,787 < 1.66594·10⁵⁷,

d_1 ≤ 22D_NM + 331 and N ≤ 22D_NM + 348. For the fixed seminorms of [[lem:uc-small-orders]] (d), K < 8.3297·10⁵⁶; and K >
22d > 2.7493·10²⁵. In the class ℰ_0^½, k1 ≤ 22D_NM + 340 and 1.0078·10⁵¹ < K*(a, M, k1) < 1.11014·10¹¹⁵ for every a ∈
(ℓ0 − 1, 3).
```

### M26b. prop:uc-data-order, proof of (d), 71-explicit-constants.md lines 5209–5230

Old (22 lines):

```old
(d) At the choice of [[def:uc-choice]], ℓ_I < 3.5 and γ_Υ = e_Υ = 1/100 ([[def:ec-point]]), so
ℓ^♭_I = 3/2 + ¼ · (99/100) · (1/100) = 60,099/40,000 and 4(ℓ_I − ℓ^♭_I) + 1 < 4(7/2 − 60,099/40,000) + 1 = 89,901/10,000
< 9; so J ≤ 8, the weights being the same for the two classes ([[thm:own-half-settling]]). With L_0 ≤ 23, resp. 28,
L_P ≤ 39, resp. 44, and K = 22d + 306 + L_P ≤ 22d + 345. Here d is the d_NM of [[prop:uc-d-small]], and d_NM ≤ D_acc
([[thm:uc-integer]]). D_acc = 157,156,403,040 · 10³⁹ + 1,258,700 · 10¹⁸, and 22 · 157,156,403,040 = 3,457,440,866,880 and
22 · 1,258,700 = 27,691,400; so 22D_acc = 3,457,440,866,880 · 10³⁹ + 27,691,400 · 10¹⁸, which with 345 added is the
integer printed, with leading digits 3.4574408. d_1 = K − 14 and N = K + 3 give the next two bounds. By
[[prop:uc-d-small]] (b) and (c), d_NM is at most D_b, resp. D_c, where

    D_b := 26,192,562,436,216,086,593,489,752,012,524,648,819,225,884,778,644,
    D_c := 52,385,124,872,431,314,948,189,146,848,603,890,726,471,509,831,693,

and

    22D_b + 345 = 576,236,373,596,753,905,056,774,544,275,542,274,022,969,465,130,513 < 5.7624·10⁵⁰,
    22D_c + 345 = 1,152,472,747,193,488,928,860,161,230,669,285,595,982,373,216,297,591 < 1.15248·10⁵¹.

By [[eq:uc-lower]], d ≥ d_acc > 1.2497·10²⁴, so K > 22d > 2.74934·10²⁵. In the class ℰ_0^½, d_1 ≤ 22d + 336 and
k1 = d_1 + 4 ≤ 22D_acc + 340 =: k̄, and by (c) K*(a, M, k1) < k̄ + 4 + (4k̄ + 35)(k̄ + 3) = 4k̄² + 48k̄ + 109. As
k̄ > 10⁵¹, 48k̄ + 109 < 10⁻⁴⁹k̄², and as k̄ < 3.4574408669·10⁵¹, k̄² < 11.95389735·10¹⁰²; so
K*(a, M, k1) < (4 + 10⁻⁴⁹) · 11.95389735·10¹⁰² < 4.78156·10¹⁰³. And K*(a, M, k1) > (4/3)k1², with
k1 > 22d > 2.74934·10²⁵, so K*(a, M, k1) > (4/3) · 7.5588·10⁵⁰ > 1.0078·10⁵¹. ∎
```

New (13 lines):

```new
(d) At the choice of [[def:uc-choice]], ℓ_I < 3.5 and γ_Υ = e_Υ = 1/100 ([[def:ec-point]]), so ℓ^♭_I = 3/2 + ¼ · (99/100)
· (1/100) = 60,099/40,000 and 4(ℓ_I − ℓ^♭_I) + 1 < 4(7/2 − 60,099/40,000) + 1 = 89,901/10,000 < 9; so J ≤ 8, the weights
being the same for the two classes ([[thm:own-half-settling]]). With L_0 ≤ 23, resp. 28, L_P ≤ 39, resp. 44, and K =
22d + 306 + L_P ≤ 22d + 345. Here d is the d_NM of [[prop:uc-d-small]], and d_NM ≤ D_NM ([[thm:uc-integer]]); 22D_NM =
1,665,937,823,457,407,864,509,731,994,804,936,559,129,497,279,544,661,374,442, which with 345 added is the integer
printed, with leading digits 1.6659378. d_1 = K − 14 and N = K + 3 give the next two bounds. By [[prop:uc-d-small]] (b),
for the fixed seminorms of [[lem:uc-small-orders]] (d), d_NM is at most D_b :=
37,862,223,260,395,634,549,934,375,862,530,497,755,494,177,219,176,347,223, and 22D_b + 345 =
832,968,911,728,703,960,098,556,268,975,670,950,620,871,898,821,879,639,251 < 8.3297·10⁵⁶. By [[eq:uc-lower]], d ≥
d_acc > 1.2497·10²⁴, so K > 22d > 2.74934·10²⁵. In the class ℰ_0^½, d_1 ≤ 22d + 336 and k1 = d_1 + 4 ≤ 22D_NM + 340 =:
k̄, and by (c) K*(a, M, k1) < k̄ + 4 + (4k̄ + 35)(k̄ + 3) = 4k̄² + 48k̄ + 109. As k̄ > 10⁵⁷, 48k̄ + 109 < 10⁻⁵⁵k̄², and
as k̄ < 1.6659378235·10⁵⁷, k̄² < 2.775348832·10¹¹⁴; so K*(a, M, k1) < (4 + 10⁻⁵⁵) · 2.775348832·10¹¹⁴ < 1.11014·10¹¹⁵.
And K*(a, M, k1) > (4/3)k1², with k1 > 22d > 2.74934·10²⁵, so K*(a, M, k1) > (4/3) · 7.5588·10⁵⁰ > 1.0078·10⁵¹. ∎
```

### O1. front matter, 00-front.md lines 37–37

Old (1 lines):

```old
1.2497 × 10²⁴ < d < 1.57157 × 10⁵⁰; at equality, μ0 = √72 l5², timelike
```

New (1 lines):

```new
1.2497 × 10²⁴ < d < 7.57245 × 10⁵⁵; at equality, μ0 = √72 l5², timelike
```

### O2. introduction, 01-introduction.md lines 156–156

Old (1 lines):

```old
and d < 1.57157 × 10⁵⁰ at one admissible choice of the weights, orders and inner products ([[thm:uc-integer]]). A
```

New (1 lines):

```new
and d < 7.57245 × 10⁵⁵ at one admissible choice of the weights, orders and inner products ([[thm:uc-integer]]). A
```

### O3. theorems chapter, 03-theorems.md lines 318–319

Old (2 lines):

```old
weights, orders and inner products, d is at most an integer below 1.57157 × 10⁵⁰ ([[thm:uc-integer]]), and K at most
one below 3.45745 × 10⁵¹.
```

New (2 lines):

```new
weights, orders and inner products, d is at most an integer below 7.57245 × 10⁵⁵ ([[thm:uc-integer]]), and K at most one
below 1.66594 × 10⁵⁷.
```

### O4. scope chapter, 90-scope.md lines 77–79

Old (3 lines):

```old
d is at most an integer below 1.57157 × 10⁵⁰ and N_NM at most one below 3.30029 × 10⁵¹ ([[thm:uc-integer]]). The order
of the approximant of [[thm:settling]] is K = d_1 + 14 = 22d + 306 + L_P, with L_P ≤ 43 an explicit number of
derivatives, so that at that point K is at most an integer below 3.45745 × 10⁵¹ ([[prop:uc-data-order]]). The
```

New (3 lines):

```new
d is at most an integer below 7.57245 × 10⁵⁵ and N_NM at most one below 1.59022 × 10⁵⁷ ([[thm:uc-integer]]). The order of
the approximant of [[thm:settling]] is K = d_1 + 14 = 22d + 306 + L_P, with L_P ≤ 43 an explicit number of derivatives,
so that at that point K is at most an integer below 1.66594 × 10⁵⁷ ([[prop:uc-data-order]]). The
```


## 6. The fallback set: the upper bound withdrawn

If no admissible choice is proved, these texts state only what is proved: the lower bounds, and that the upper bound is
an explicit function (prop:uc-dependence) of inputs that are not evaluated. They replace the main blocks M1–M5, M12,
M26a, M26b, O1–O4. **Rule for the other main blocks (M6–M11, M13–M25):** apply them with every evaluated number
deleted together with the words that state it (for instance "N_Λ ≤ N̄_Λ := 910,000,000,000,000" becomes "N_Λ ≤ N̄_Λ",
"C_lev := 2N_ι + N̄_Λ + 529 = …" becomes "C_lev := 2N_ι + N̄_Λ + 529", "L_< = …, L_> = … and R_b = …" and the *The
integer.* paragraphs of lem:cs-sharp and prop:uc-d-small are deleted, the evaluated displays of prop:uc-explicit and its
*The counts.* paragraph are deleted), and with "at the choice of [[def:uc-choice]]" read as "at a choice as in
[[def:uc-choice]] at which the weights are admissible"; M15a and M15b are applied unchanged. Their formulas and proofs
are the proofs of prop:uc-dependence, so they stay true. def:uc-choice and lem:uc-admissible are P-UB1's. Since
P-UB1 proved an admissible choice, this set is not needed; it is kept as asked. Checked merged with P-UB1's texts and
the main blocks other than those replaced (section 7).

### F1. chapter summary, 71-explicit-constants.md lines 24–28

Old (5 lines):

```old
for the index sets as the proofs construct them ([[cor:uc-two-offsets]]). At that point, at one admissible choice of
the weights and of the free orders and inner products ([[def:uc-choice]], [[def:cs-choices]]), d_acc and d_NM, the
latter the d of [[thm:iii-k-3-2]], at least the orders at which its lemmas ask U small ([[prop:uc-d-small]]), are at
most an integer below 1.57157 × 10⁵⁰, and N_NM at most one below 3.30029 × 10⁵¹ ([[thm:uc-integer]]). That parameter
point is not shown to lie in the set on which [[thm:settling]] is proved ([[rem:ec-point-outside]]), and the bounds at
```

New (6 lines):

```new
for the index sets as the proofs construct them ([[cor:uc-two-offsets]]). At that point d_acc, d_R and d_NM are bounded
above by explicit functions of the admissible ε_K of the gap condition and of the counts of the index sets
([[prop:ec-upper]], [[prop:uc-dependence]]); every admissible ε_K there is below 1.6747859·10⁻¹⁷ ([[thm:is-gap]]), and
the admissible ε_K and the number of points of Λ below 3 + ε_+ are not evaluated here, so these bounds are not evaluated.
That parameter point is not shown to lie in the set on which [[thm:settling]] is proved ([[rem:ec-point-outside]]), and
the bounds at
```

### F2. chapter summary, 71-explicit-constants.md lines 33–33

Old (1 lines):

```old
being an explicit number of derivatives; at the computational point K is at most an integer below 3.45745 × 10⁵¹
```

New (1 lines):

```new
being an explicit number of derivatives; at the computational point K exceeds 2.7493 × 10²⁵
```

### F3. thm:loss-d, last sentence, 71-explicit-constants.md lines 1497–1499

Old (3 lines):

```old
the index sets. At the computational point [[thm:uc-integer]] evaluates every number of steps and every such count, and
[[lem:uc-small-orders]] and [[prop:uc-d-small]] the orders at which the proof of [[thm:iii-k-3-2]] asks U small: d_acc
and d_NM are at most an integer below 1.57157 × 10⁵⁰, and N_NM at most one below 3.30029 × 10⁵¹.
```

New (2 lines):

```new
the index sets. At the computational point [[prop:uc-dependence]] gives d_acc, d_R and d_NM upper bounds that are
explicit functions of the admissible ε_K and of the counts of the index sets, which are not evaluated.
```

### F4. rem:ec-lb-unbounded, 71-explicit-constants.md lines 1809–1810

Old (2 lines):

```old
proved set, and an explicit upper bound for it can hold at points of that set but not on all of it; in particular d_NM
exceeds 1.57157·10⁵⁰, the bound of [[thm:uc-integer]], at every point of the proved set with h ≤ 4.48·10⁻²⁶. Likewise, at
```

New (1 lines):

```new
proved set, and an explicit upper bound for it can hold at points of that set but not on all of it. Likewise, at
```

### F5. rem:ec-upper-point, 71-explicit-constants.md lines 2206–2215

Old (10 lines):

```old
**Remark {#rem:ec-upper-point}** (The upper bound at the computational point.) At the computational point ε_g ≤ ε_Υ <
1.46214·10⁻¹⁰ ([[lem:ec-gauge-gap]], [[rem:ec-gauge-gap]]), and for the index sets as the proofs construct them 𝔡₀ and 𝔡₁
are increments of Λ ([[cor:uc-two-offsets]], [[rem:uc-offset-d0]]) and (G) holds exactly for ε_K < μ_G, where μ_G <
1.64160217198·10⁻¹⁴ ([[thm:is-gap]]). The levels are then less than μ_G apart, and the first line of [[eq:ec-upper]] is
of the order 3/(ε_Kε_g), the order of the lower bound 3R of [[prop:ec-rounds]]. [[prop:uc-explicit]] evaluates it at the
admissible choice of [[def:uc-choice]], with ε_K = 1.6416·10⁻¹⁴ and ε_g = ε_Υ = 1.4619·10⁻¹⁰: it is less than
1.2587·10²⁴, of which less than 4.30775·10²¹ comes from the window loops at ι⁺ (bounded there through ε^ι_ind = 𝔡₁,
[[lem:uc-gaps]]), and less than 1.0072 times the lower bound 3R > 1.2498·10²⁴ at the same choice ([[thm:uc-integer]]).
The losses c(β_k), c_b and c′_b of single steps enter the second line with the multiplicities K < 1.22077·10¹⁴ and N_b,
N_b + 1 < 6.10383·10¹³, and c_0 once; [[prop:cs-cstar]] bounds their largest value c_* by 6.4368·10³⁵.
```

New (7 lines):

```new
**Remark {#rem:ec-upper-point}** (The upper bound at the computational point.) At the computational point ε_g ≤ ε_Υ <
1.46214·10⁻¹⁰ ([[lem:ec-gauge-gap]], [[rem:ec-gauge-gap]]), and for the index sets as the proofs construct them every ε_K
with which (G) holds lies below 1.6747859·10⁻¹⁷ ([[thm:is-gap]]). The levels are then less than 1.6747859·10⁻¹⁷ apart,
and the first line of [[eq:ec-upper]] is of the order 3/(ε_Kε_g), the order of the lower bound 3R of [[prop:ec-rounds]].
In the second line the levels above 3, about 1/ε_K of them, are each charged at most C_lev = 2N_ι + N̄_Λ + 529, which is
quadratic in a bound N̄_Λ for the number N_Λ of points of Λ below 3 + ε_+ ([[lem:cs-levels]], [[prop:uc-dependence]]).
The admissible ε_K and N_Λ are not evaluated in this paper, and so neither is the bound.
```

### F6. thm:uc-integer, then prop:uc-dependence as in M12, 71-explicit-constants.md lines 2759–2796

Old (38 lines):

```old
**Theorem {#thm:uc-integer}** (The loss d at the computational point.) At the computational point, with the index sets as
constructed, the admissible choice of the weights of [[def:uc-choice]] and the free orders and inner products of
[[def:cs-choices]], let c_* be the largest of the numbers c(β_k) (1 ≤ k ≤ K), c_b, c′_b and c_0 defined before
[[prop:ec-upper]] and c^Ψ(β_k), c^Ψ_b, c′^Ψ_b and c^Ψ_0 of [[lem:uc-dr]]: the largest loss that [[def:ec-accounted-loss]]
assigns to a single step outside the long iterations. Then
c_* < C_* := 643,680,000,000,000,000,000,000,000,000,000,000 = 6.4368·10³⁵ ([[prop:cs-cstar]]), and

    d_acc ≤ d_R ≤ D_acc,     d_NM ≤ D_NM := D_acc,     N_NM = 21d_NM + 6 ≤ 21D_NM + 6,                 {#eq:uc-integer}

where, with D_e = 1.2587·10²⁴ = 1,258,700,000,000,000,000,000,000 and M_c = 2.44153·10¹⁴ = 244,153,000,000,000,

    D_acc := D_e + M_c C_* = 157,156,403,040,000,000,000,000,001,258,700,000,000,000,000,000,000 < 1.57157·10⁵⁰,
    21D_NM + 6 = 3,300,284,463,840,000,000,000,000,026,432,700,000,000,000,000,000,006 < 3.30029·10⁵¹.

The losses of [[lem:iii-k-2-2]] and [[prop:iii-j2-4-3]] satisfy d_Ψ, d_FM ≤ 1,038,326,399,999,948, and the finer bounds
d_acc, d_R < 2.6193·10⁴⁹ and d_NM < 5.2386·10⁴⁹ hold ([[lem:cs-sharp]], [[prop:uc-d-small]]). At a level β ∈ (3, α],
1 + n_ι ≤ c(β) ≤ 2N_ι + N̄_Λ + 529 = C_lev, with N_ι of [[eq:uc-n-iota]], N̄_Λ = 16,747,199,999,999 and C_lev of
[[eq:cs-clev]] ([[lem:cs-levels]]). Against these, for every admissible choice of the weights,

    d_NM ≥ d_acc ≥ 3R > 1.2497·10²⁴,     N_NM > 2.624·10²⁵,                                                {#eq:uc-lower}

and at the choice of [[def:uc-choice]], 3R > 1.2498·10²⁴, so that D_e < 1.0072 · 3R.

*Proof.* By [[prop:cs-cstar]], c_* < C_*. By [[lem:uc-admissible]] the hypotheses of [[prop:ec-upper]] hold, and by
[[lem:uc-gaps]] it holds with the T_2 and W of [[eq:uc-t2-w]]. Its first line is less than D_e by [[prop:uc-explicit]],
and its second line is at most Σ_k c(β_k) + N_b c_b + (N_b + 1)c′_b + c_0 ≤ (K + 2N_b + 2)c_* ≤ M_c C_*, again by
[[prop:uc-explicit]]. So d_acc ≤ D_e + M_c C_* = D_acc. Here M_c C_* = 244,153 · 64,368 · 10⁴⁰, which is
15,715,640,304 · 10⁴⁰ = 157,156,403,040 · 10³⁹; adding D_e = 1,258,700 · 10¹⁸ gives the integer printed, and
21D_acc + 6 is 21 · 157,156,403,040 · 10³⁹ + 21 · 1,258,700 · 10¹⁸ + 6, that is
3,300,284,463,840 · 10³⁹ + 26,432,700 · 10¹⁸ + 6.
[[lem:uc-dr]] gives the same bound for d_R, its first line being the same and its single-step losses being at most
c_* < C_*; and d_R ≥ d_acc ([[thm:loss-d]]). By [[prop:uc-d-small]] (d), d_NM < D_acc, so d_NM ≤ D_NM, and the finer
bounds are [[lem:cs-sharp]] and (b), (c) there; the bounds for d_FM and d_Ψ are [[lem:uc-lambda]] (d).
N_NM = 21d_NM + 6 by [[thm:loss-d]], so N_NM ≤ 21D_NM + 6. The statements at the levels above 3 are
[[lem:uc-fourier-count]] and [[lem:cs-levels]] (b). [[eq:uc-lower]] is [[cor:uc-two-offsets]] (a),
whose hypothesis holds by (b) there. At the choice of [[def:uc-choice]], [[prop:ec-rounds]] gives
R > (1 − 3ε_K − 2δ̂ − δ̄)/(ε_Kδ̂), where 3ε_K + 2δ̂ + δ̄ < 1.98·10⁻⁸ and ε_Kδ̂ = 2.400249024·10⁻²⁴ < 2.40025·10⁻²⁴; so
3R > 3(1 − 1.98·10⁻⁸)/(2.40025·10⁻²⁴) > 1.2498·10²⁴, and 1.0072 · 1.2498 > 1.2587. ∎
```

New (53 lines):

```new
**Theorem {#thm:uc-integer}** (The loss d at the computational point.) At the computational point, with the index sets as
constructed, let the weights be chosen as in [[def:uc-choice]], with ε_K and ε_+ for which the choice is admissible, and
the free orders and inner products as in [[def:cs-choices]], and let c_* be the largest of the numbers c(β_k) (1 ≤ k ≤
K), c_b, c′_b and c_0 defined before [[prop:ec-upper]] and c^Ψ(β_k), c^Ψ_b, c′^Ψ_b and c^Ψ_0 of [[lem:uc-dr]]: the
largest loss that [[def:ec-accounted-loss]] assigns to a single step outside the long iterations. Then c_* ≤ C_*, at a
level β ∈ (3, α] 1 + n_ι ≤ c(β) ≤ C_lev, and

    d_acc ≤ d_R ≤ D_acc,     d_NM ≤ D_NM,     N_NM = 21d_NM + 6 ≤ 21D_NM + 6,            {#eq:uc-integer}

with C_*, C_lev, D_acc and D_NM the explicit functions of ε_K, ε_+, N̄_Λ, k̄_0, J_* and l_* of [[prop:uc-dependence]].
Every admissible ε_K is below 1.6747859·10⁻¹⁷ ([[thm:is-gap]]); this paper evaluates neither the admissible ε_K nor N_Λ,
and so gives no number for D_acc or D_NM. Against these, for every admissible choice of the weights,

    d_NM ≥ d_acc ≥ 3R > 1.2497·10²⁴,     N_NM > 2.624·10²⁵.                                {#eq:uc-lower}

*Proof.* The bounds for c_* and at the levels above 3 are [[prop:cs-cstar]], [[lem:uc-fourier-count]] and
[[lem:cs-levels]] (b), and the others are [[prop:uc-dependence]]; N_NM = 21d_NM + 6 by [[thm:loss-d]]. [[eq:uc-lower]] is
[[cor:uc-two-offsets]] (a), whose hypothesis holds by (b) there. ∎

**Proposition {#prop:uc-dependence}** (The bound as a function of the choice.) Let a choice be made as in
[[def:uc-choice]], except that ε_K and ε_+ are any numbers with 0 < ε_K < ε_+ < 10⁻¹³ for which it is admissible, and let
N̄_Λ ≥ N_Λ, k̄_0, J_* and l_* be integers for which [[lem:uc-lambda]] (b) and (c) hold, with J′ := (J_* + 1)(l_* + 1).
Put Δβ_0 := 0.999²ε_K and Δτ_0 := 0.999ε_Υ, L_<, L_> and R_b as in [[eq:uc-levels]], N_ι as in [[eq:uc-n-iota]], k̄_max
:= k̄_0 + J′N̄_Λ, d̄_Φ := 62N̄_Λ + 2, C_lev := 2N_ι + N̄_Λ + 529, I_lev := 34,268,829,852, I_base := 935R_b + 466 +
23,524,832(R_b + 3), T_12 := C_lev + I_lev + 4k̄_max + 24, R_base := 22,097 + I_base,

    F_1 := 3((1 + Δβ_0/2)² + (1 + ε_K + Δβ_0/2)²)/(2Δβ_0Δτ_0) + 3(3 + 2ε_K)/Δβ_0 + 6 + 4/Δτ_0 + 8
           + 3((1 + ε_K)/Δβ_0 + 1)((1 + ε_+)/𝔡₁ + 2) + 16(0.4901/𝔡₁ + 1)((3 + ε_K)/Δβ_0 + 5),
    C_* := 6N_ι + 3N̄_Λ + 3I_lev + 8k̄_max + I_base + d̄_Φ + (N̄_Λ + 2)(d̄_Φ + 30) + 45,862,
    D′_* := T_12 + 18 + 20,565,308,337L_< + (C_lev + I_lev − 9)L_> + 2R_base,
    D_acc := D_e + 497L_< + L_>C_lev + 935R_b + 466 + C_*,     D_NM := D_acc + D′_* + d̄_Φ,

with D_e any number at least F_1. Then d_acc ≤ d_R ≤ D_acc, d_NM ≤ D_NM and N_NM ≤ 21D_NM + 6. Each of N_ι, k̄_max, d̄_Φ,
C_lev, I_base, T_12, R_base, C_*, D′_* and D_acc − D_e is a polynomial with non-negative coefficients in N̄_Λ, k̄_0, J′,
L_<, L_> and R_b; L_<, L_> and R_b are non-increasing in ε_K, and F_1 is non-increasing in ε_K and non-decreasing in ε_+.
So, with D_e := F_1, D_acc and D_NM are non-decreasing in N̄_Λ, k̄_0, J′ and ε_+ and non-increasing in ε_K. Moreover
D_acc = L_>C_lev + D_e + 497L_< + 935R_b + 466 + C_*, and L_>C_lev > J′N̄_Λ(N̄_Λ + 1)(1 + ε_K)/Δβ_0: the bound is at
least quadratic in N̄_Λ and of the order 1/ε_K.

*Proof.* The proofs of [[prop:uc-explicit]], [[lem:cs-levels]], [[lem:cs-base]], [[lem:cs-iterations]], [[lem:cs-rest]],
[[prop:cs-cstar]], [[lem:cs-sharp]], [[lem:uc-small-orders]], [[rem:uc-small-reading]] and [[prop:uc-d-small]] use, of
the numbers of [[def:uc-choice]] and [[lem:uc-lambda]], only N_Λ ≤ N̄_Λ, k̄(λ_i) ≤ k̄_0 + J′i, Δβ ≥ Δβ_0, a♭_K − 2 ≥
Δβ_0, Δτ ≥ Δτ_0, ε_K < ε_+ < 10⁻¹³ and the bounds of [[lem:is-offsets]] (b); and they give d_acc, d_R ≤ D_acc and d_NM ≤
D_NM with the expressions above. F_1 is the bound for the first line of [[eq:ec-upper]] that [[eq:ec-upper-counts]],
[[eq:uc-t2-w]], ℓ⁺_tf = 1, r_ι ≤ 16 and η_2 − η_1 < ε_+ give, with N_< ≤ 1/Δβ_0, N_> ≤ (1 + ε_K)/Δβ_0 + 1 and N_b ≤
1/Δβ_0 + 1 ([[eq:ec-upper-counts]]): 3(T_< + T_> + T_2) + 4(1/Δτ + 2) + 16W(N_< + N_> + N_b + 3), 1/Δτ ≤ 1/Δτ_0, written
out; 1/𝔡₁ may be replaced by any upper bound. C_* is the right side of [[eq:cs-c0]] written out (1,587 + 44,227 + 48 =
45,862 and 2X_12 = 8k̄_max + 48), I_base is that of [[eq:cs-iterations]] (469R_b + 466(R_b + 1) = 935R_b + 466 and 16 ·
1,470,302 = 23,524,832), and 22,097 = 20,183 + 1,914. These are sums of products of N̄_Λ, k̄_0, J′, L_<, L_>, R_b and
positive constants, so they do not decrease when one of these integers increases. As ε_K increases, Δβ_0 increases, and
1/Δβ_0 and (1 + ε_K)/Δβ_0 = 1/Δβ_0 + 1/0.998001 decrease, and so do their integer parts; each term of F_1 is
non-increasing in ε_K, as x ↦ (1 + cx)²/x decreases on (0, 1/c) and (1 + ε_K)/Δβ_0 and (3 + ε_K)/Δβ_0 decrease, and ε_+
enters F_1 only through the factor 1 + ε_+. Finally C_lev > 2N_ι ≥ J′N̄_Λ(N̄_Λ + 1) and L_> > (1 + ε_K)/Δβ_0. ∎
```

### F7. prop:uc-data-order (d), 71-explicit-constants.md lines 5122–5130

Old (9 lines):

```old
(d) At the computational point, with the index sets as constructed and the choices of [[def:uc-choice]] and
[[def:cs-choices]], J ≤ 8; so L_P ≤ 39 in the class of [[eq:vii-0-1]] and L_P ≤ 44 in the class ℰ_0^½. With D_acc of
[[thm:uc-integer]],

    K ≤ 22D_acc + 345 = 3,457,440,866,880,000,000,000,000,027,691,400,000,000,000,000,000,345 < 3.45745·10⁵¹,

d_1 ≤ 22D_acc + 331 and N ≤ 22D_acc + 348. For the fixed seminorms of [[lem:uc-small-orders]] (d), K < 5.7624·10⁵⁰,
and for those of [[rem:uc-small-reading]], K < 1.15248·10⁵¹; and K > 22d > 2.7493·10²⁵. In the class ℰ_0^½,
k1 ≤ 22D_acc + 340 and 1.0078·10⁵¹ < K*(a, M, k1) < 4.78156·10¹⁰³ for every a ∈ (ℓ0 − 1, 3).
```

New (4 lines):

```new
(d) At the computational point, with the index sets as constructed and the weights, orders and inner products chosen as
in [[def:uc-choice]] and [[def:cs-choices]] with an admissible ε_K, J ≤ 8; so L_P ≤ 39 in the class of [[eq:vii-0-1]] and
L_P ≤ 44 in the class ℰ_0^½, K ≤ 22d + 345, and K > 22d > 2.7493·10²⁵. In the class ℰ_0^½, k1 > 22d > 2.7493·10²⁵ and
K*(a, M, k1) > 1.0078·10⁵¹ for every a ∈ (ℓ0 − 1, 3).
```

### F8. prop:uc-data-order, proof of (d), 71-explicit-constants.md lines 5209–5230

Old (22 lines):

```old
(d) At the choice of [[def:uc-choice]], ℓ_I < 3.5 and γ_Υ = e_Υ = 1/100 ([[def:ec-point]]), so
ℓ^♭_I = 3/2 + ¼ · (99/100) · (1/100) = 60,099/40,000 and 4(ℓ_I − ℓ^♭_I) + 1 < 4(7/2 − 60,099/40,000) + 1 = 89,901/10,000
< 9; so J ≤ 8, the weights being the same for the two classes ([[thm:own-half-settling]]). With L_0 ≤ 23, resp. 28,
L_P ≤ 39, resp. 44, and K = 22d + 306 + L_P ≤ 22d + 345. Here d is the d_NM of [[prop:uc-d-small]], and d_NM ≤ D_acc
([[thm:uc-integer]]). D_acc = 157,156,403,040 · 10³⁹ + 1,258,700 · 10¹⁸, and 22 · 157,156,403,040 = 3,457,440,866,880 and
22 · 1,258,700 = 27,691,400; so 22D_acc = 3,457,440,866,880 · 10³⁹ + 27,691,400 · 10¹⁸, which with 345 added is the
integer printed, with leading digits 3.4574408. d_1 = K − 14 and N = K + 3 give the next two bounds. By
[[prop:uc-d-small]] (b) and (c), d_NM is at most D_b, resp. D_c, where

    D_b := 26,192,562,436,216,086,593,489,752,012,524,648,819,225,884,778,644,
    D_c := 52,385,124,872,431,314,948,189,146,848,603,890,726,471,509,831,693,

and

    22D_b + 345 = 576,236,373,596,753,905,056,774,544,275,542,274,022,969,465,130,513 < 5.7624·10⁵⁰,
    22D_c + 345 = 1,152,472,747,193,488,928,860,161,230,669,285,595,982,373,216,297,591 < 1.15248·10⁵¹.

By [[eq:uc-lower]], d ≥ d_acc > 1.2497·10²⁴, so K > 22d > 2.74934·10²⁵. In the class ℰ_0^½, d_1 ≤ 22d + 336 and
k1 = d_1 + 4 ≤ 22D_acc + 340 =: k̄, and by (c) K*(a, M, k1) < k̄ + 4 + (4k̄ + 35)(k̄ + 3) = 4k̄² + 48k̄ + 109. As
k̄ > 10⁵¹, 48k̄ + 109 < 10⁻⁴⁹k̄², and as k̄ < 3.4574408669·10⁵¹, k̄² < 11.95389735·10¹⁰²; so
K*(a, M, k1) < (4 + 10⁻⁴⁹) · 11.95389735·10¹⁰² < 4.78156·10¹⁰³. And K*(a, M, k1) > (4/3)k1², with
k1 > 22d > 2.74934·10²⁵, so K*(a, M, k1) > (4/3) · 7.5588·10⁵⁰ > 1.0078·10⁵¹. ∎
```

New (6 lines):

```new
(d) At such a choice, ℓ_I < 3.5 and γ_Υ = e_Υ = 1/100 ([[def:ec-point]]), so ℓ^♭_I = 3/2 + ¼ · (99/100) · (1/100) =
60,099/40,000 and 4(ℓ_I − ℓ^♭_I) + 1 < 4(7/2 − 60,099/40,000) + 1 = 89,901/10,000 < 9; so J ≤ 8, the weights being the
same for the two classes ([[thm:own-half-settling]]). With L_0 ≤ 23, resp. 28, L_P ≤ 39, resp. 44, and K = 22d + 306 +
L_P ≤ 22d + 345. By [[eq:uc-lower]], d ≥ d_acc > 1.2497·10²⁴, so K > 22d > 2.74934·10²⁵. In the class ℰ_0^½, k1 = d_1 +
4 > 22d > 2.74934·10²⁵, and by (c) K*(a, M, k1) > k1 + 4 + (4k1 + 35)(k1 + 2)/3 > (4/3)k1² > (4/3) · 7.5588·10⁵⁰ >
1.0078·10⁵¹. ∎
```

### FO1. front matter, 00-front.md lines 35–37

Old (3 lines):

```old
damping parameter, so that d is unbounded on that set, and, at a parameter point not shown to lie in it, for one
admissible choice of the weights, orders and inner products and the index sets as the proofs construct them,
1.2497 × 10²⁴ < d < 1.57157 × 10⁵⁰; at equality, μ0 = √72 l5², timelike
```

New (3 lines):

```new
damping parameter, so that d is unbounded on that set, and, at a parameter point not shown to lie in it, for every
admissible choice of the weights and the index sets as the proofs construct them, d > 1.2497 × 10²⁴; at equality, μ0 =
√72 l5², timelike
```

### FO2. introduction, 01-introduction.md lines 155–156

Old (2 lines):

```old
lie in it, d > 1.2497 × 10²⁴ at every admissible choice of the weights, for the index sets as the proofs construct them,
and d < 1.57157 × 10⁵⁰ at one admissible choice of the weights, orders and inner products ([[thm:uc-integer]]). A
```

New (2 lines):

```new
lie in it, d > 1.2497 × 10²⁴ at every admissible choice of the weights, for the index sets as the proofs construct them.
A
```

### FO3. theorems chapter, 03-theorems.md lines 316–319

Old (4 lines):

```old
computational point of [[def:ec-point]], which is not shown to lie in that set ([[rem:ec-point-outside]]), and at one
admissible choice of the
weights, orders and inner products, d is at most an integer below 1.57157 × 10⁵⁰ ([[thm:uc-integer]]), and K at most
one below 3.45745 × 10⁵¹.
```

New (3 lines):

```new
computational point of [[def:ec-point]], which is not shown to lie in that set ([[rem:ec-point-outside]]), d > 1.2497 ×
10²⁴ at every admissible choice of the weights ([[cor:uc-two-offsets]]); an upper bound there is an explicit function of
the admissible ε_K of the set Λ, which lies below 1.6747859·10⁻¹⁷ ([[thm:is-gap]]) and is not evaluated here.
```

### FO4. theorems chapter, list item, 03-theorems.md lines 363–366

Old (4 lines):

```old
  explicit lower bounds ([[thm:loss-d]]) and explicit upper bounds for d and N_NM at one admissible choice of the
  weights, orders and inner products ([[thm:uc-integer]]); through the lower bounds, upper bounds for δ and for the
  modulus of the initial family at 2δ (and λ1 < δ); explicit resolvent bounds on five-dimensional Tangherlini
  ([[ch:resolvent-bounds]]); and where explicit evaluation of λ1 and δ stops ([[ch:explicit-constants]]).
```

New (3 lines):

```new
  explicit lower bounds ([[thm:loss-d]], [[cor:uc-two-offsets]]); through the lower bounds, upper bounds for δ and for
  the modulus of the initial family at 2δ (and λ1 < δ); explicit resolvent bounds on five-dimensional Tangherlini
  ([[ch:resolvent-bounds]]); and where explicit evaluation of λ1 and δ stops ([[ch:explicit-constants]]).
```

### FO5. scope chapter, 90-scope.md lines 75–79

Old (5 lines):

```old
loss that this proof's choices produce, not for the least loss with which the tame estimates hold ([[thm:loss-d]]). At
that point, for those index sets and at one admissible choice of the weights and of the free orders and inner products,
d is at most an integer below 1.57157 × 10⁵⁰ and N_NM at most one below 3.30029 × 10⁵¹ ([[thm:uc-integer]]). The order
of the approximant of [[thm:settling]] is K = d_1 + 14 = 22d + 306 + L_P, with L_P ≤ 43 an explicit number of
derivatives, so that at that point K is at most an integer below 3.45745 × 10⁵¹ ([[prop:uc-data-order]]). The
```

New (5 lines):

```new
loss that this proof's choices produce, not for the least loss with which the tame estimates hold ([[thm:loss-d]]). An
upper bound at that point is an explicit function of the admissible ε_K of the set Λ, below 1.6747859·10⁻¹⁷
([[thm:is-gap]]), and of the counts of the index sets, which are not evaluated here ([[thm:uc-integer]]). The order of
the approximant of [[thm:settling]] is K = d_1 + 14 = 22d + 306 + L_P, with L_P ≤ 43 an explicit number of derivatives
([[prop:uc-data-order]]). The
```

### FO6. own-data chapter, 63-own-data.md lines 70–71

Old (2 lines):

```old
quadratic in d_1 ([[prop:uc-data-order]]); d is bounded above only at the computational point of [[def:ec-point]], which
is not shown to lie in the set where the theorem is proved. The order k_P is what the subtracted
```

New (2 lines):

```new
quadratic in d_1 ([[prop:uc-data-order]]); d is bounded below, and no upper bound for it is evaluated in this paper. The
order k_P is what the subtracted
```

### FO7. own-data chapter, 63-own-data.md lines 298–299

Old (2 lines):

```old
([[prop:uc-data-order]]). None of ε, λ1, δ is evaluated, in either class, and d is bounded above only at the
computational point. (c) The weights α_1, α′ avoid finitely many more points in each bounded interval.
```

New (2 lines):

```new
([[prop:uc-data-order]]). None of ε, λ1, δ is evaluated, in either class, and no upper bound for d is evaluated. (c) The
weights α_1, α′ avoid finitely many more points in each bounded interval.
```

### F9. rem:ec-other-losses, last sentence, 71-explicit-constants.md lines 425–425

Old (1 lines):

```old
[[thm:loss-d]] (ii)), and at the computational point [[thm:uc-integer]] bounds d_acc, d_NM and N_NM from above.
```

New (2 lines):

```new
[[thm:loss-d]] (ii)), and at the computational point [[thm:uc-integer]] bounds d_acc, d_NM and N_NM from above by
explicit functions of the admissible ε_K and of the counts of the index sets, which are not evaluated.
```


## 7. Checks (on scratch copies; nothing run in the repository)

- **The formulas reproduce the old chain.** Evaluated at the old inputs (ε_K = 1.6416·10⁻¹⁴, ε_+ = 1.64160217·10⁻¹⁴,
  N̄_Λ = 16,747,199,999,999, R_b = 61,038,200,000,000 as printed), they give exactly the printed N_ι, k̄_max, d_Φ, C_lev,
  I_lev, I_base, X_12, T_12, the c_0 bound of eq:cs-cstar, R_base, 2R_base + 16, K̄, D_♭, D′_*, the integers of
  prop:uc-d-small (b) and (c), D_acc = D_e + M_c C_*, and the first line below 1.2587·10²⁴ with windows below
  4.30775·10²¹. So no formula of section 1.2 is misread from the chapter.
- **Exact arithmetic.** Every value of section 3 and every number in the texts was computed with exact rationals; each
  decimal is checked to bound its quantity in the stated direction (upper bounds strictly above, lower strictly below),
  the floors L_<, ⌊(1 + ε_K)/Δβ_0⌋ by the printed integer products, the inequalities 2R_base + 16 < T_12,
  X_12 > R_base, k_0 + 5 < R_base, k̄ > 10⁵⁷ with 48k̄ + 109 < 10⁻⁵⁵k̄², 1.0072·3R > D_e and 0.3168h⁻² > D_NM at the
  printed h, and the identities C_* = 6N_ι + 3N̄_Λ + (seven numbers) and c_0-bound = 20,183 + 1,914 + T_11 + 2T_12 + 11
  + d_Φ + (N̄_Λ + 2)(d_Φ + 30).
- **Form.** Every new block: lines at most 121 characters, no wrapped line starting with "+ ", "- ", "* ", "> ", "#", "="
  or "|", labels lowercase, no unfilled placeholder. Applied to a scratch copy of chapters/ (main set; and fallback set
  with the main blocks it does not replace), the edition's own lint in its --chapters mode reports 0 hits, with 4,667
  labels defined (two new: prop:uc-dependence, eq:uc-levels) and every reference resolved. The old texts each occur
  exactly once.
- **Scratch merge from a git archive of HEAD ac31449d** (nothing run in the repository): P-UB1's 14 texts T1–T14
  (located by their old texts) and the 36 main blocks applied together, disjoint. Results:
  lint --chapters: "chapters: 62 file(s), 4794 label(s) defined, 0 hit(s)";
  assemble --check: "labels 4794, computations cited 0, problems 0";
  assemble: "labels 4794, computations cited 0, problems 0";
  lint --paper on the scratch PAPER.md: "PAPER.md: 0 hit(s)".
  The same with the fallback set and the main blocks it does not replace:
  "chapters: 62 file(s), 4794 label(s) defined, 0 hit(s)";
  "labels 4794, computations cited 0, problems 0"; "PAPER.md: 0 hit(s)".
  The line widths of the new texts are measured with every label resolved to its number in that merged assembly, plus
  one character per label, so a shift of the numbering by a digit stays within 121 characters.
- **Not checked here:** P-UB1's texts (sec:is, def:uc-choice, lem:uc-admissible) and their numbers; the crosswalk rows
  (crosswalk/71-explicit-constants.tsv needs rows for prop:uc-dependence and eq:uc-levels and notes for the blocks);
  the real PAPER.md (regenerate after the merge).

## 8. What changed since md5 eb5f55fcc614dcad6625c8778ac03c70

For the reader checking the delta. The structure (formulas, repairs, split levels, prop:uc-dependence, eq:uc-levels,
fallback rule) is unchanged.

1. **Inputs.** Final, from P-UB1: ε_+ 1.67475·10⁻¹⁷ → 1.67478·10⁻¹⁷; N̄_Λ 910,000,000,000,000 → 909,507,124,095,312;
   ε_K = 1.6747·10⁻¹⁷, k̄_0, J_*, l_*, ε_Υ and the 0.999 factors unchanged. Every generated number is recomputed (the
   table of section 3); L_<, L_>, R_b, D_e, the decimals of prop:uc-explicit's proof and 3R depend on ε_K only and are
   unchanged, as are I_lev, W and the per-step constants.
2. **The gap bound sharpened** from 1.67488·10⁻¹⁷ (V-I11) to 1.6747859·10⁻¹⁷ (P-UB1's eq:is-mu-z) in M5 (twice), M7
   and in F1, F5 (twice), F6, FO3, FO5.
3. **M6** (rem:ec-upper-open (1)): "and the generators 1 + 𝒵 of Λ ask ε_K < 1.67488·10⁻¹⁷; [[thm:is-gap]] gives the
   admissible ε_K," → "and with the generators 1 + 𝒵 of Λ (G) holds exactly for ε_K < μ_Z, where μ_Z < 1.6747859·10⁻¹⁷
   ([[thm:is-gap]], [[eq:is-mu-z]]);".
4. **M7** (sec:uc-close): "With them [[thm:is-gap]] gives the admissible ε_K," → "With them (G) holds exactly for
   ε_K < μ_Z ([[thm:is-gap]]),".
5. **M8** (thm:uc-reduction (iii)): "every ε_K with which (G) holds is below 1.67488·10⁻¹⁷, and [[thm:is-gap]] gives the
   admissible ε_K;" → "(G) holds exactly for ε_K < μ_Z, where 1.6747856·10⁻¹⁷ < μ_Z < 1.6747859·10⁻¹⁷ ([[thm:is-gap]],
   [[eq:is-mu-z]]);" — the form of the old (iii) with μ_Z for μ_G.
6. **M15a** (lem:cs-fourier (b)): "As the elements of Λ of real part at most 2 are real ([[lem:iii-i10-1-2]] (a),
   [[prop:is-lambda]]: those of Λ ∩ {Re ≤ 3 + ε_+} that are not real have real part above 2)," → "As the elements of
   Λ of real part at most 2.514 are real ([[prop:is-lambda]])," — P-UB1's statement, which contains what the proof
   uses (real part at most 2).
7. **Rewrapping.** Lines are now measured with the labels resolved (section 7). This rewraps, among others, the four
   lines P-UB1 found over 121 characters in the assembled paper (M6, M7, M13 twice); the words are unchanged.
8. **This file:** header (final inputs, HEAD ac31449d, md5s of 01, 03, 90, which changed at HEAD elsewhere, the quoted
   lines being unchanged and found once), §1.3 item 5 (cor:is-lower), §1.4 (requirements met), §6 (fallback not needed),
   §7 (the merge), §8.

**Option L (if cor:is-lower is kept).** Exact substitutions in these texts, all lower bounds that cor:is-lower implies:
in M12, the display "d_NM ≥ d_acc ≥ 3R > 1.2497·10²⁴,     N_NM > 2.624·10²⁵," becomes
"d_NM ≥ d_acc ≥ 3R > 1.2250·10²⁷,     N_NM > 2.5725·10²⁸," and "[[eq:uc-lower]] is [[cor:uc-two-offsets]] (a), whose
hypothesis holds by (b) there." becomes "[[eq:uc-lower]] is [[cor:is-lower]]."; in M7, "against the lower bound
1.2497·10²⁴" becomes "against the lower bound 1.2250·10²⁷"; in M26a and M26b, "K > 22d > 2.7493·10²⁵" becomes
"K > 22d > 2.695·10²⁸" (22 · 1.2250·10²⁷ = 2.695·10²⁸), "k1 > 22d > 2.74934·10²⁵" stays true, and
"1.0078·10⁵¹ < K*(a, M, k1)" may become "9.684·10⁵⁶ < K*(a, M, k1)" ((4/3)(2.695·10²⁸)² = 9.6840…·10⁵⁶), with the
proof's "(4/3) · 7.5588·10⁵⁰ > 1.0078·10⁵¹" → "(4/3) · 7.263025·10⁵⁶ > 9.684·10⁵⁶". The chapter summary (71:23),
00-front, 01, 03 and 90 quote 1.2497·10²⁴ in lines no block here touches; with Option L they may stay (true) or take
1.2250·10²⁷ — the coordinator's choice. Default: not applied.
