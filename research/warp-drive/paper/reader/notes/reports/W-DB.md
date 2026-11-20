# W-DB report: the explicit upper bound for the loss d

**Outcome.** Every count and number of steps is evaluated; one finite integer remains, c_*, the largest single-step loss outside the long iterations ([[pending:issue-db-1]]). The bound is explicit and affine in c_*.

## Choice (def:uc-choice, close l. 339; admissibility lem:uc-admissible, l. 353)
- ε_Υ = 1.4619·10⁻¹⁰, so ε_g = ε_Υ (ε_ind = δ_50).
- ε_K = 1.6416·10⁻¹⁴. This is below μ_G > 1.64160217197·10⁻¹⁴, so (G) holds (thm:is-gap), and ε_K < ε_Υ.
- ε_+ = 1.9·10⁻⁸, l_* = 50, k̄_0 = 3.
- ℓ_I ∈ (3 + ε_+, 3.5), λ₋ ∈ (ℓ_I − 2, 3/2), δ_ι < 3.5 − ℓ_I.
- η_1 < η_2 in (ε_K, ε_+), off Re Λ − {2, 3}.
- ε ≤ 10⁻³ε_g.
- 0.999ε_K ≤ α − 4 ≤ ε_K, level spacings in [0.999(α − 4), α − 4), 0.999(α − 4) ≤ a♭_K − 2 < α − 4.
- This gives Δβ_0 = 1.6383184416·10⁻¹⁴ and Δτ_0 = 1.4604381·10⁻¹⁰.

## Evaluated quantities
- **lem:uc-gaps (l. 387).** min Re ℰ_ind = min Re ℰ^ι_ind = η_0 = 𝔡₁. Therefore lem:ec-counts (d), (e) and prop:ec-upper hold with 𝔡₁ in place of ε_Υ: T_2 = N_>((1 + η_2 − η_1)/𝔡₁ + 2) and W = 0.4901/𝔡₁ + 1.
- **lem:uc-lambda (l. 403).**
  - N_Λ lies in (16,206,600,000,000, 16,747,199,999,999].
  - J_* = 15,000,015, l_* = 50, k̄_0 = 3, J′ = 765,000,816.
  - n(λ_i) = i − 1 and k̄(λ_i) = 3 + 765,000,816·i < 1.28117·10²².
  - d_Φ ≤ 1,038,326,399,999,940 and d_FM, d_Ψ ≤ 1,038,326,399,999,948.
- **lem:uc-n-iota (l. 423).**
  - Any n(E, w) whose logarithmic orders are bounded by k̄ is at most 4N_Λ + J′N_Λ(N_Λ + 1)/2 ≤ N_ι = 107,279,395,180,026,392,909,234,131,199,999,996 < 1.07280·10³⁵.
  - Hence n_ι ≤ N_ι, and the Step 0 Fourier loss is ≤ 9 + N_ι.
- **prop:uc-explicit (l. 443).**
  - N_<, N_>, N_b < 6.10382·10¹³.
  - T_<, T_> < 2.089723·10²³ and T_2 < 1.83115·10²⁰.
  - W ≤ 1,470,302 windows; the window loops contribute < 4.30775·10²¹.
  - First line of eq:ec-upper < **D_e = 1.2587·10²⁴**.
  - K + 2N_b + 2 < **M_c = 2.44153·10¹⁴**.
- **lem:uc-dr (l. 481).** d_R satisfies eq:ec-upper with the same first line and its own single-step losses. d_NM = d_R once d_R > 62N_Λ + 10.

## Result: thm:uc-integer (l. 500)
- d_acc ≤ 1,258,700,000,000,000,000,000,000 + 244,153,000,000,000·c_*
- d_NM = d_R ≤ the same bound.
- N_NM ≤ 26,432,700,000,000,000,000,000,006 + 5,127,213,000,000,000·c_*

Lower bounds:
- For every admissible choice: d_NM ≥ d_acc ≥ 3R > 1.2497·10²⁴ and N_NM > 2.624·10²⁵.
- At this choice: 3R > 1.2498·10²⁴, so D_e < 1.0072·3R. The explicit part is within 0.72 % of the lower bound.

All arithmetic checked exactly; every printed bound rounded outward.

## Pending: [[pending:issue-db-1]] (close l. 517, 553)
c_* is the largest of c(β_k), c_b, c′_b, c_0 and their counterparts for ℛ(U).

**Why it is not evaluated here.**
- The texts state each of these numbers only as finite (assembly l. 514–525: "Each of these numbers is finite, being assigned … to a composition of finitely many elementary families").
- Several component losses are stated only as "fixed loss" (ch. 43 lem:iii-j2-2-1 (g), l. 234–243: thm:iii-g4-3-1/prop:iii-g4-4-4/prop:iii-g4-5-1 compositions, prop:iii-i1-2-1, prop:iii-i1-3-1).
- Writing c_* out needs four things:
  1. A step-by-step list of the factors of each level step: lem:iii-i8-3-2, lem:iii-i13-2-2 with prop:iii-i10-3-1, prop:iii-i11-3-1 and prop:iii-i13-2-1 (ch. 41 l. 410–851, 1526–1599).
  2. The same for one base round (prop:iii-i5-2-1, ch. 39 l. 986ff), one base step (prop:iii-i2-5-1), and c_0's steps (Steps 0, 1, 3, 4′, 4 of thm:iii-i14-3-1, Φ, thm:iii-j1-2-1 Steps 1–3).
  3. The regularity order s_c > ½ + ϑ_ℋ and the thresholds of L̂_b(σ) used by cor:ii-g1-4-2, prop:ii-g1-4-7 and cor:ii-g1-4-5 (ch. 29 l. 1034–1044, 1103–1114, 1167–1175).
  4. The count of K⁺-exponents in the prop:iii-a-4-2 (2) application at Step 7 of prop:iii-i11-3-1 (ch. 41 l. 839–844).

**Scale.** Through N_ι, M_c·c_* is of order 10⁴⁹, far above D_e; a smaller bound needs the actual logarithmic orders, which the texts bound only by k̄(λ).

**rem:uc-missing (l. 533)** now states (IS), (SP) as established and lists what c_* needs; its claim that (IS) and (SP) alone give an integer was too strong.

## Other text changes
Close: intro, sec:uc-index-sets ("[[sec:is]] lists them"), cor:uc-two-offsets (a), rem:uc-offset-d0 (cites thm:is-d0),
lem:uc-fourier-count (J_* = 15,000,015), thm:uc-reduction. Assembly: the paragraph closing thm:loss-d (l. 152–158),
rem:ec-upper-point (now the admissible evaluation, not the hypothetical 1.46·10⁻¹⁰), rem:ec-upper-open. No statement
that (IS) or (SP) is missing remains.

## Chapter 71 statements that must change
1. rem:ec-weights-observed (l. 552–570) asserts "(G) holds by [[prop:gap-sums]]" at ε_K = 188·10⁻¹⁰; false for the
   index sets as constructed (thm:is-gap). Replace that clause by: "the gap condition (G) holds by [[prop:gap-sums]]
   for the subset 𝒮 of Λ; for the index sets as constructed it fails at this ε_K ([[thm:is-gap]]), so these weights are
   not admissible", and open rem:ec-integer-bound (l. 572–595) with "(at weights that are not admissible,
   [[rem:ec-weights-observed]])".
2. l. 20–22, "No upper bound for d is proved: … is an observation." → "[[thm:uc-integer]] bounds d_acc and d_NM by
   1.2587 × 10²⁴ plus 2.44153 × 10¹⁴ times the largest single-step loss c_*, which this paper does not evaluate."
3. rem:ec-other-losses l. 385–387, "None is proved here; … weights." → "[[lem:uc-lambda]] and [[lem:uc-dr]] give them;
   [[thm:uc-integer]] states the resulting bound."

## Lint and size
- `python3 lint.py proofs/P-U71-close.md proofs/P-U71-assembly.md` reports only the two pending markers, plus the cross-file references that are expected to show as undefined in a file run.
- All references resolve; the 16 new labels are unique; no line over 121 characters or with a forbidden start.
- Final line counts: P-U71-close.md 559, P-U71-assembly.md 635.
