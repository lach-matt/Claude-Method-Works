# R3-IS-SP: confirming reading of P-U71-IS and P-U71-SP

Reader: R3-IS-SP (independent; changed nothing). Texts: proofs/P-U71-IS.md (660 lines, md5
545148220f81b7a3c8a8edd1c1458f92) and proofs/P-U71-SP.md (602 lines, md5 f2461a601b62a16cee0b429f005a0ce1), unchanged
over the whole reading (md5 re-checked on resuming). "IS l. n" and "SP l. n" are lines of these files. Read against
them: READER-BRIEF, STYLE, WRITER-BRIEF(-S); notes/reviews/R2-P-U71-IS.md, notes/reports/F2-P-U71-IS.md,
notes/reviews/R-P-U71-SP.md, notes/reports/F-P-U71-SP.md, INTEGRATION.md (IS/SP entries); every cited statement in
chapters 30, 32, 33, 34, 35, 36, 38, 40, 41, 42, 71 and in P-A-indicial, P-A3-every-h, P-U71-close, P-U71-assembly
(the last two only for the keys cited; they are being edited by another worker, and each cited key was re-checked to
exist with the statement used just before this report). Private checks: exact rationals (fractions, sympy) and
mpmath at 60-80 digits, in scratchpad/reader/scratch/r3_is_sp/ (offsets.py, exps.py, orders.py, gap.py, count.py,
window.py, valuation.py, contract.py, refs.py, fixes.txt).

## Verdicts

- **P-U71-IS: NOT CONFIRMED** — 0 Major, 1 minor, 2 nits.
- **P-U71-SP: NOT CONFIRMED** — 0 Major, 1 minor, 2 nits.

Both are one-line fixes; no number moves and nothing on the path of the integer bound changes. The mathematics of
both texts is right: every finding of R2-P-U71-IS and R-P-U71-SP is resolved correctly, and every number listed in the
brief re-derives exactly. The two minors are a cross-text inconsistency created when SP landed (IS's summary still
says the pole orders are not determined by the paper) and a hypothesis of SP's cor:sp-lstar (d) that the fix round left
too weak when it deleted two conditional clauses.

## Findings

### P-U71-IS

**IS-F1 (minor) — IS l. 653-656 (rem:is-summary): "(SP) not determined by this paper" contradicts SP.** The remark says
"Two further things are not determined by this paper. (1) The orders of the poles of N_ι⁺(L̄, ·)⁻¹, statement (SP) of
[[rem:uc-missing]]; l_* depends on them." In the assembled chapter 71 these orders are determined: SP's
thm:sp-spectrum (b) and cor:sp-lstar (a) show every pole of N_ι⁺(L̄, ·)⁻¹ at real part at most 5 is simple, so they add
exactly 1 to the quantities l_* bounds and the least admissible l_* is L ∈ [39, 50]. The sentence is false once both
texts are in the paper; the mathematics is unaffected. (R2 could not see this: SP's fix round post-dates it.)

*Fix.* Replace IS l. 653-656 from "[[prop:is-count]]. Two further things" to "Neither question in (2) enters an upper"
by (lines already wrapped, at most 121 characters):

    [[prop:is-count]]. The orders of the poles of N_ι⁺(L̄, ·)⁻¹ at real part at most 5, statement (SP) of [[rem:uc-missing]],
    are all 1 ([[cor:sp-lstar]] (a)), so they do not raise l_* above L. One thing is not determined by this paper: the
    coefficient c_b of [[def:is-cb]] at a rotating b; for index sets that keep 𝔡₁ it decides whether ε_K may be taken up to
    μ♭ ([[cor:is-flat]]) or only below μ_G ([[thm:is-gap]]); whether an admissible ℰ_ind can omit 𝔡₁ is not decided either.
    Neither question enters an upper

(the rest of l. 656-658, "bound for d: the index sets as constructed serve …", unchanged; re-wrap the paragraph).

**IS-N1 (nit) — IS l. 532: past tense and "bound".** "[[lem:uc-fourier-count]] bounded J_* through η_0 ≥ ε_Υ; with
η_0 = 𝔡₁ the bound becomes J_* = 15,000,015." reads as narration, and 15,000,015 is the value, not a bound. *Fix:*
"[[lem:uc-fourier-count]] bounds J_* through η_0 ≥ ε_Υ; with η_0 = 𝔡₁, J_* = 15,000,015 ([[prop:is-count]] (c))."

**IS-N2 (nit) — IS l. 228-230 (proof of prop:is-logs (a)): three contributions not written out.** The orders at the
offsets 𝔡₀ and 𝔡₁ receive contributions from (c2) at 1 + 𝔡₀ and 1 + 𝔡₁ (through E_(c1) − 1), and the offset
1 + 𝔡₀ + 𝔡₁ receives one from the class at m = 1 − 𝔡₁ at 2 + 𝔡₀; the text computes the sibling cases but not these.
Each is 0 by the same count (checked: orders.py), so the values 0, 0, …, 0 of (a) stand. *Fix:* replace l. 228-231 from
"at 2 + 𝔡₁ the count is" to "At the" by

    at 2 + 𝔡₁ the count is ℓ̂_F(2 + 𝔡₁) + ℓ̂_F(1 + 𝔡₁) + 1 = 2 + 1 + 1, so k = 3, and likewise at 2 + 𝔡₀; at 1 + 𝔡₀,
    1 + 𝔡₁, 2 + δ′₁ and 2 + δ₂, ℓ̂_F = 1 and no root lies at or below, so k = 0. The classes: at m = 1 − 𝔡₀ the exponent
    2 + 𝔡₀ comes from u₂ alone, with no term of 𝒢 ⊂ {Re ≥ 3} below it, so k = 0; the same at 2 + 𝔡₁ for m = 1 − 𝔡₀ and
    m = 1 − 𝔡₁, and at 2 + 𝔡₀ for m = 1 − 𝔡₁. At the

(continuing "integer offset 1 of a step at m ≤ 0 …" as now; re-wrap).

### P-U71-SP

**SP-F1 (minor) — SP l. 548 (cor:sp-lstar (d)): the stated hypothesis ε_+ < 1/4 is too weak for the list.** The
statement lists the poles on {2 ≤ Re ϰ ≤ 3 + ε_+} "ε_+ < 1/4" as 3, ι₁, the roots ι of P_l with 2 < Re ι ≤ 3 + ε_+
and ι + 1 for those with Re ι ≤ 2 + ε_+. For 4·10⁻⁶ < ε_+ < 1/4 this is false: ι_v(2) = 3.00000499998… and
ι₁ + 1 = 3.0000747… are poles (thm:sp-spectrum (a)) in the strip and are not listed. The proof (l. 585-587) uses
ε_+ < ε_ind = δ_50 < δ̄ < 2·10⁻⁸, which [[eq:iii-i9-1-1]] imposes at the computational point, so the corollary is true
in the paper's setting; but its statement names the wrong bound. The fix round created this: R-P-U71-SP N5 had the two
conditional clauses ("ι₁ + 1 if ι₁ ≤ 2 + ε_+", "ι_v(l) ≤ 3 + ε_+") deleted as empty at the point, and they were what
made the list right for every ε_+ < 1/4. *Fix:* replace SP l. 548-549 up to "([[def:iii-i10-1-1]]);" by

    (d) On {2 ≤ Re ϰ ≤ 3 + ε_+}, where ε_+ < δ_50 < 2·10⁻⁸ ([[eq:iii-i9-1-1]], [[def:ec-point]]), the poles are 3; ι₁;
    and the roots ι of P_l (l ≥ 1) with 2 < Re ι ≤ 3 + ε_+, together with ι + 1 for those with Re ι ≤ 2 + ε_+. All are
    simple. Of these poles, 3 lies in Λ ([[def:iii-i10-1-1]]);

(continuing "whether ι₁, a root ι of some P_l …" as now; re-wrap the paragraph to 121).

**SP-N1 (nit) — SP l. 25 and l. 319-330: μ in two senses, and the weight renamed silently.** (i) Chapter 35 writes the
admissible pair (s, μ) ([[eq:iii-g-2-6]]); SP writes (s, c) from l. 85 on without saying so (μ being its letter for
roots). (ii) In the proof of lem:sp-two-roots (c) the kernel vector is (μ_0, μ_1, μ_2, μ_3), while μ is an indicial root
everywhere else in the section, including two lines earlier. *Fix:* (i) SP l. 25, after "[[eq:iii-g-2-6]]–[[eq:iii-g-2-7]]"
replace "." by "; we write c for the weight μ there, μ denoting indicial roots in this section." (ii) In l. 319-330
replace μ_0, μ_1, μ_2, μ_3 by ν_0, ν_1, ν_2, ν_3 throughout (the vector of moments is ν in prop:sp-visible).

**SP-N2 (nit) — SP l. 341: bounds cited to a statement that does not contain them.** "1.3333327·10⁻⁶ < 𝔡₀ <
1.3333334·10⁻⁶ and 3.3333·10⁻⁷ < 𝔡₁ < 3.3334·10⁻⁷ ([[prop:gap-sums]])": these bounds are in the proof of prop:gap-sums
("*The offsets.*", ch. 71 l. 81-92), not in its statement. *Fix:* "([[prop:gap-sums]])" → "(proof of [[prop:gap-sums]])".

## 1. The earlier findings

R2-P-U71-IS (1 Major, 1 minor, 5 nits):

| Finding | Where now | Resolved |
|---|---|---|
| F1 (Major), the window 134 ≤ l ≤ 172 | IS l. 336-350; statement l. 306-312; prop:is-logs (c) l. 273-276; intro l. 6-8; rem l. 646 | Yes. Constants re-derived exactly for all 39 l (below). |
| F2 (minor), hκ > 70 | IS l. 350-354, l. 309-310 | Yes: ῑ ≠ ι of equal multiplicity m and real part, three roots above 19/10 counted with multiplicity, 2m ≤ 3, m = 1. No "at most 3" remains. |
| N1 ε_Υ a choice | IS l. 430-431, 496-497 | Yes (lem:ec-gauge-gap says "an admissible choice"). |
| N2 intro rounding | IS l. 15 | Yes. |
| N3 □^C roots = polynomial roots | IS l. 315-316 | Yes (prop:np-10-12 (ii), (iii)). |
| N4 N(L̂_b(0), ·) | IS l. 32, 322 | Yes. |
| N5 K → k_R, κ₀ → ν₀ | IS l. 237-243, 519-521 | Yes; no κ₀, no "except possibly", no "at most 3 on" left. M* kept (allowed). |

R-P-U71-SP (1 Major, 5 minor, 10 nits):

| Finding | Where now | Resolved |
|---|---|---|
| F1 (Major), the window | SP l. 385-401 | Yes, proved inside SP (no IS citation): signs −, +, − at a ∓ 0.45, a for l = 134, 135; 𝒬 > 2.87·10⁻³ on ℝ for 136 ≤ l ≤ 172; conjugation with multiplicity. |
| F2 values of l_* | SP l. 527-534, 553-560, 599-602 | Yes: M ≤ 7, 39 ≤ L ≤ 50, least l_* = L, l_* = 50 taken. |
| F3 hκ > 70 | SP l. 405-411 | Yes, with multiplicities. |
| F4 raise of 𝒮_(λ₀) | SP l. 543-546, 577-583 | Yes: cor:iii-g3-3-1 (1) (log powers ≤ J + K, K the pole order of [[eq:iii-g3-2-2]]), and sec:s23-step (ch. 42 l. 779-781) says the inverse acts there as that of thm:iii-g1-3-1 (2); cor:iii-g2-4-3 kept only for lem:iii-i10-1-2 (c). |
| F5 Λ ∩ spec | SP l. 549-551, 588-589 | Yes; the departure (no prop:is-lambda citation) is sound: 3 ∈ Λ as a generator of def:iii-i10-1-1. |
| F6 K_ι ≤ 2 | SP l. 536-541, 562-575 | Yes; 52 and 101 also stated and true. |
| N1-N10 | l. 176, 197, 132-140, 489-491, 548-549, 268-334 and 66-81, 184-187, 𝔫, ϰ, 𝔮_k | Yes; N5's deletion causes SP-F1 above. |

The specific points of the brief:

- **Distinctness for 134 ≤ l ≤ 172** (IS l. 336-350, SP l. 385-401): x(133) = 0.017955 < 0.018 ≤ x(134) = 0.018224 and
  x(172) = 0.029928 ≤ 0.03 < x(173) = 0.030275; Δ(0.01866) > 0 > Δ(0.01867); Δ′ = 2x − 1715/8 vanishes only at 107.1875;
  Δ(0.018224) = 0.093562114176, Δ(0.018495) = 0.035476440025, Δ(0.018768) = −0.023037762176 (exact); U(ξ_x) =
  0.0057943…, 0.0021967…; 𝒬(ξ_x ± 0.45) = 0.405 − Δ/8 > 0.3925; −Δ(0.018768)/8 = 0.002879720272;
  0.0425·0.0028 = 1.19·10⁻⁴, 0.0425·0.00287 = 1.21975·10⁻⁴. The identity 𝒬 = 2(ι − ξ_x)² − Δ/8 holds exactly at every l.
  **All 39 values** (window.py, exact rationals): P_l built from [[eq:s14-nl]] at (v, e, h) = (1/2, 1/102400, 10⁻⁶);
  the rigorous majorant Σ|coeff|·0.45^k of P_l − U about ξ_x is ≤ 9.3353·10⁻⁵ < 9.4·10⁻⁵ at every l = 134, …, 172
  (independently confirming lem:s14-sextic-large (b) on the closed disc); signs at ξ_x − 0.45, ξ_x, ξ_x + 0.45 are
  −, +, − at l = 134, 135 and −, −, − at each l = 136, …, 172; Sturm counts of real roots on the closed diameter are 2 at
  l = 134, 135 and 0 at each l = 136, …, 172. Sanity (numerical roots): 2.43755, 2.58986 (134); 2.46734, 2.56049 (135);
  2.51412 ± 0.03858i (136) … 2.52249 ± 0.38857i (172).
- **hκ > 70 simple by conjugation**: correct in both texts (IS l. 350-354; SP l. 405-411).
- **cor:iii-g3-3-1 (1) for 𝒮_(λ₀)**: correct (above).
- **K_ι ≤ 2 on Σ, and 52, 101**: K_ι is the pole order of [[eq:iii-g3-2-2]] (ch. 42 l. 559-560), ≤ m_ι + m_♯
  (prop:iii-g3-2-4); m_ι ∈ {0, 1} on Re ≤ 5 (thm:sp-spectrum (b), lem:iii-g1-4-2 (b)); the least ℰ^C_I has all orders 0
  (induction on the ℰ_((m)) of lem:iii-c-3-2 (e), sums adding orders by [[def:s11-b-analysis]] (4)), so m_♯ ≤ 1 and
  K_ι ≤ 2; with k(E, z) := −1 off π₁E the bound K_ι ≤ 2 + k ≤ l_* + 2 = 52 holds at every ϰ, and 2l_* + 1 = 101
  is lem:iii-j-1-2. K_ι(λ_♯) = 1 by cor:iii-g3-2-6.
- **l_* = L ∈ [39, 50], l_* = 50**: correct (§2).
- **Renames**: 𝔫 and 𝔮 occur nowhere in chapters 33-36, 71 or the other d-bound texts. ϰ is chapter 35's and 71's
  spectral parameter, as in SP; chapter 34 also uses ϰ locally for a rotation coefficient (l. 209-253), a homonym
  between chapters 34 and 35 that predates SP. 𝔉 occurs in chapter 36 only as the subscripted class 𝔉_D of sec iii-g4-3
  (l. 1240-1303); F-P-U71-SP checked 33-35 and 71 only. Neither is a clash of meaning with SP's local symbols; no
  change needed.

## 2. Consistency between the two texts

SP cites IS at exactly two keys: [[prop:is-mult]] (SP l. 554, 600: M ≤ 7; simple on [−101, 5]) and [[prop:is-logs]]
(SP l. 559, 601: 39 ≤ L ≤ 50). IS proves exactly these: prop:is-mult (IS l. 306-358) gives multiplicity ≤ 7 at each
type (prop:iii-f1-2-3 (a), (b) under (C1), which holds at h = 10⁻⁶ by prop:np-10-54 (i), (ii)) and simplicity on
[−101, 5]; prop:is-logs (b) gives ℰ_ind ≤ 39 with (5, 39) ∈ ℰ_ind (the boost correction at 1 + 5), (c) gives
ℰ^ι_ind ≤ 50. The ℰ^C_I part of L (order 0) SP proves itself (SP l. 563-569) from lem:iii-c-3-2, whose (a) states
ℰ_I^C + ½ ⊂ ℰ_I^C and (2, 0), (3, 0) ⊂ ℰ_I^C and whose (e) gives the least ℰ_I^C ⊇ ℰ̃ as the union of the ℰ_((m))
(ch. 36 l. 248-277): exactly what SP uses, with ℰ̃ = ∅ allowed (min Re ∅ = ∞). Everything else SP uses about the
roots it proves itself (lem:sp-roots, lem:sp-exceptional). IS's own prop:is-ci-pp (a) (least ℰ^C_I = {(1 + n/2 + c, 0)})
agrees with SP's (3, 0) ∈ ℰ^C_I and order 0.

The one inconsistency is IS-F1. Values agree: l_* = 50 in IS rem:is-summary (IS part) and SP cor:sp-lstar (all); K_ι
≤ 2 (SP) is consistent with IS's K-free statements.

## 3. Numbers re-derived

All exact (rationals, sympy) or certified at 60-80 digits (mpmath), the latter only where an irrational is compared with
printed decimals.

- **lem:is-offsets.** D_l identity 125000²(16u² + 16z + 4z²) = D_l (l ≤ 5); 9/4 + z = 562501/250000. The six first and
  six second squares: every printed expansion is the true square's leading digits, each on the claimed side. The I, I′,
  I₂ brackets are the images of the √D, √D₂ brackets. 𝔡₀ = 1.33333274074126748912665825006…·10⁻⁶,
  𝔡₁ = 3.33333046296485082219485898…·10⁻⁷, δ′₁ = 6.00000077999906280030651019…·10⁻⁷,
  δ₂ = 2.66666533925966422384840394…·10⁻⁷, ε₀ = 5.55555327160248714656…·10⁻¹³: all inside the printed enclosures,
  and the enclosures follow from the square brackets. d₂(1) = 𝔡₁, d₁(1) = δ′₁, d₂(2) = δ₂ from the closed forms. (c):
  D = 3·333333666667 (digit sum 55), 562501 (digit sum 19).
- **lem:is-roots (b).** (u + 1)/(2u(2u + 1)) ≤ 3/20 at u ≥ 2; (3z/20)(1 + z) = 6.0000024·10⁻⁷ < 6.1·10⁻⁷;
  4/21 < (3/10)(1 − z)/(1 + z); |θ₁|, |θ₂| ≤ z from [[eq:s14-theta]].
- **Exponents to Re 5** (exps.py): the 33 pairs (f, n_f) of prop:is-ind are exactly the least integer parts of
  ℕ ∪ ⋃_(m∈M*)((R − m) + ℕ₀) below 5 (1 + 2 + 5 + 6 + 9 + 10 by n_f); the order [[eq:is-low]] holds.
- **Logarithmic orders** (orders.py, an independent implementation of [[eq:is-l1]]): (c1) 2j at 2 + j, ≤ 4 at
  non-integer offsets ≤ 5; (c2) 0, 3, 9, 17, 27, 39 at 1 + j, j = 0, …, 5, ≤ 18 at non-integer offsets (at 4 + 𝔡₀);
  (c3) j + (j − 1)₊ = 1, 3, 5, 7, 9, ≤ 3 at non-integer offsets; at 2 + 𝔡₀, 2 + 𝔡₁ (c2) has 3, at 1 + 𝔡₀, 1 + 𝔡₁,
  2 + δ′₁, 2 + δ₂ it has 0. Step bounds 2·5 + 2 − 1 = 11, 5 + 1 − 1 = 5, 4·7 + 4 − 1 = 31; chains 24, 31, 38 (s1),
  18, 25, 32 (s0), 11, 18, 25 (v1), 18, 25, 32 (companions), all ≤ 39, each inheritance shift (t − 2, t − 4, t − 3)
  re-derived from prop:iii-d3-3-1 (1)-(7). u_b: 3·16 + 3 − 1 = 50. **Maximum 39, attained at (5, 39)**.
- **μ_G** (gap.py): μ_G = 1.641602171971270779192935…·10⁻¹⁴, so 1.64160217197·10⁻¹⁴ < μ_G < 1.64160217198·10⁻¹⁴ and
  μ_G ∈ (1.6416021719700, 1.6416021719734)·10⁻¹⁴. All 28 rows of the table: n⁺, frac (to four digits; closest call
  0.18885 at y = 0.4602), n⁻, every n, p, q and every excess interval as printed; distances of y/𝔡₁, 4y/𝔡₀ from ℤ at
  least 0.1367 and 0.0132; θ_n/ε₀ − (p − 1) ∈ [0.0295, 0.9705]; least p = 0 candidate 5.01914·10⁻⁸ > 5.01·10⁻⁸;
  next excesses 2.3181480701976·10⁻¹⁴, 8.0959353086799·10⁻¹⁴, then 4.2197168·10⁻¹³ > 4.2·10⁻¹³. Every printed
  full-digit partial product and y lies in its printed interval. μ_G < 10⁻¹³, < 1.4619·10⁻¹⁰.
- **N_Λ** (count.py): Σ(3 − β)² = 720294717/50000000 = 14.40589434, Σ(3 − β) = 2229/125 = 17.832 over the 26 rational
  β; 1/(2𝔡₀𝔡₁) = 1125001468750.40538…; ε_+ + 𝔡₀ + 𝔡₁ < 1.68608·10⁻⁶ < 1.69·10⁻⁶; N_Λ > 1.6206652291·10¹³ > 1.62066·10¹³
  and N_Λ < 1.6747170053·10¹³ < 1.67472·10¹³. The lattice-count bounds X²/(2𝔡₀𝔡₁) ≤ T(X) ≤ (X + 𝔡₀ + 𝔡₁)²/(2𝔡₀𝔡₁)
  and the disjointness (lem:is-offsets (c)) checked by hand.
- **k̄_0 = 3**: 𝒢 has order 3 at 3 = 2 + 1 (ℰ_ind order 3 at 1); ℰ_ind below 1.0198 is [[eq:is-low]]; ℰ_++ ≤ 3 below
  2λ_♯; ℰ⁰_src below 2λ_♯ is 𝒢 ∪ (ℰ_rows ∩ {Re < 2}) by [[eq:iii-i10-1-1]] and (H1).
- **J_* = 15,000,015**: η_0 = 𝔡₁; 1/𝔡₁ = 3000002.58333386…, 5/𝔡₁ = 15000012.9166693…, ceiling 15000013.
- **cor:is-flat**: μ♭ = 5.01913624…·10⁻⁸; y/𝔡₁ = 1470297.2660903…, 1470293.2660886…; second excess 1.3888859·10⁻⁷;
  counts 56,436,655 (28 bases), 56,436,656 (with 3), 59,377,257 (all 31).
- **SP valuation table** (valuation.py): c_3 = 10⁻¹⁸ and c_2, c_1 exactly as printed (the κ-coefficients of
  det(hN_l)); c_0 = (−h(ι − 1)² − (ι − 3))P_0 and P_0 = −(ι − 2)C exactly; the twelve c_0(q) equal the printed
  fractions; numerators odd (first nine) and prime to 5 (last three, residues 2, 4, 3); coefficient valuations −18,
  −23, −22, −24, −24 / −18, −18, −18, −14, −18 (c_1) and −18, −24, −24 / −18, −18, −18 (c_2); every row of the table
  (−29, −26, −25, −18), (−44, −35, −28, −18), (−34, −29, −26, −18), (−30, −26, −22, −18) at all three q of each row;
  3218988513000625 = 5⁴·17·23·13172331511. Vector type: each q has denominator 2, 10⁴, 10² or 25.
- **SP pole list**: ι_v(1) = 3, ι_v(2) ∈ (3, 4) (500002² = 250002000004), (500002 + 4·10⁻⁶)² < 250002000009, ι_v(l) ≤ 5 ⟺
  l ≤ 1413 (1414² = 1999396 ≤ 2000016 < 2002225 = 1415²); 1000009, 2000016, 3000025 not squares; 𝒮_τ for every type
  re-read off prop:iii-f1-2-3; the union of thm:sp-spectrum (a) re-derived from 𝒮_τ + {1, 2, …}; every difference in
  lem:sp-roots (c); Q's distance 12/25 from ℤ.
- **Kernels**: c_τ(3) = 1 (s0); c_τ(4) = 1 at s0, s1, v1; c_τ(5) = 2 at s0, v1 and 1 at s1, s2, v2, t2; d_τ =
  1, 4, 9, 6, 16, 10; dimensions 1, 11, 53. lem:sp-two-roots (a), (b) re-derived by hand: the six Laplacian and
  divergence identities on ℝ⁴, δ̄u = −3(ι − 4)r^(−ι−1)dr and ½(ι − 4)r^(−ι−1)V̂, ι_Xu, tr Z = 12, ḠZ, δ̄Ḡ(r⁻²Z) = 0,
  □̄(r⁻²Z) = 4(e_Υ + 2)r⁻⁴K_s0; the kernel construction at ϰ = 5 and the use of lem:sp-block.
- **Reduction theorem**: the descent c_i = c − i(1 + η) (all inequalities), the index count codim ran(Id − G) =
  dim ker(Id − G), the onto map Ψ and lem:sp-pole-order, lem:sp-block, lem:sp-moments, lem:sp-primitive checked line by
  line.

## 4. Citations

All 80 distinct keys of IS and 84 of SP resolve (refs.py) in chapters/ or proofs/; the only key defined twice is
[[prop:gap-sums]] (ch. 71 l. 72 and P-A-indicial l. 421, the same statement; pre-existing, for integration). Each
external statement was read at its definition and gives what is used, with hypotheses met at the point of use:
prop:iii-f1-2-3 (z ∈ (0, ½], (C1)), lem:iii-f1-2-1/-2/-4, lem:iii-f-2-1 (2), (3), lem:iii-d-4-1 and
[[eq:iii-d-4-2]], lem:iii-d-2-1 (3), prop:np-10-12, -30 (iv), -52 (i) with [[eq:s14-theta]], -54 (i)-(iii),
lem:iii-a-1-4, -5, Spec_b and (E2), (E3), [[def:s11-b-analysis]] (4) (extended union, sums, k = −1 off π₁E),
lem:iii-d3-2-1, prop:iii-d3-3-1, lem:iii-f3-2-1, prop:iii-f3-2-2, rem:iii-f3-2-3, prop:iii-f4-5-1, lem:iii-i15-1-1,
the P-A-indicial lemmas (sextic-split, majorant, count, small, large (a)-(c), scalar-zero, vector-distance,
damping-distance, delta50), prop:s14-scalar-every-h and cor:s14-remote-point, def:iii-c-3-1, lem:iii-c-3-2 (a), (e),
[[eq:iii-i1-3-2]] (Ĕ_+ = ∅; "rounds" is chapter 38's own term), def:iii-i10-1-1, lem:iii-i10-1-2 (b), (c),
def:iii-i10-1-3, [[eq:iii-i9-1-1]], [[eq:iii-i10-1-1]], lem:iii-h2-3-2, lem:iii-g-1-2 (e), (f), [[eq:iii-g-2-6]],
prop:iii-g-3-2, thm:iii-g-5-1 (1)-(3), thm:iii-g1-3-1 (1), (2) with [[eq:iii-g1-3-1]], [[eq:iii-g1-3-3]],
def:iii-g1-4-1, lem:iii-g1-4-2 (a), (b), lem:iii-g1-4-3, [[eq:iii-g1-1-4]] (σ_Υ = {0, 99/10000, 1/100, 1/50}, s_C =
γ_C(1 − e_C)(1 − v_C) > 100), prop:iii-g3-2-4, [[eq:iii-g3-2-1]], cor:iii-g3-2-6, cor:iii-g3-3-1 (1), sec:s23-step,
def:iii-j-1-1, lem:iii-j-1-2, def:ec-point, lem:ec-gauge-gap, sec:uc-index-sets, rem:uc-missing, cor:uc-two-offsets,
lem:uc-fourier-count. The one citation aimed at a proof rather than a statement is SP-N2.

## 5. Contract

- `python3 lint.py proofs/P-U71-IS.md proofs/P-U71-SP.md`: 247 hits, all "reference to undefined label" (cross-chapter
  keys in a file run); no other hit. No file, program, code, AI or process word; "computational point", "computed from
  the constructions" (IS l. 27), "exact arithmetic on the printed numbers" (IS l. 123) and chapter 38's "rounds"
  (IS l. 382) are mathematical uses. No [[pending:…]], no backticks, bold only in result headings.
- Every proof closed by ∎: IS 16/16, SP 11/11. Explicit constants throughout.
- Lines: maximum 121 in both (Python len). No wrapped line starts with "+ ", "- ", "* ", "> ", "#", "=" or "|" (the
  only such lines are headings and IS's table). The fix texts above are wrapped to at most 121.
- Labels: IS 32, SP 26, all lowercase; none defined twice in the two texts, chapters/ or proofs/.

## Values for the integer bound

| Value | Text | Confirmed |
|---|---|---|
| μ_G (gap: (G) iff ε_K < μ_G) | IS thm:is-gap | 1.64160217197·10⁻¹⁴ < μ_G < 1.64160217198·10⁻¹⁴ (μ_G = 1.6416021719713·10⁻¹⁴); ε_K = 1.6416·10⁻¹⁴ admissible; μ_G < ε_Υ = 1.4619·10⁻¹⁰, < δ_50 |
| N_Λ | IS prop:is-count (a) | 1.62066·10¹³ < N_Λ < 1.67472·10¹³ (true bounds 1.62067·10¹³, 1.67472·10¹³ to 6 digits) |
| k̄_0 | IS prop:is-count (b) | 3, the least admissible |
| J_* | IS prop:is-count (c) | 15,000,015 (η_0 = 𝔡₁); replaces P-U71-close's J_* ≤ 34,202,065,807 at integration |
| l_* | SP cor:sp-lstar (a), IS rem:is-summary | 50 admissible; least admissible is L |
| K_ι | SP cor:sp-lstar (b) | ≤ 2 on Σ (≤ 1 off spec_ι⁺(L̄) ∩ π_1ℰ^C_I); also ≤ 52 = l_* + 2 and ≤ 101 = 2l_* + 1 |
| L | IS prop:is-logs, SP | 39 ≤ L ≤ 50 ((5, 39) ∈ ℰ_ind; ℰ^ι_ind ≤ 50; least ℰ^C_I 0) |
| M | IS prop:is-mult | ≤ 7 on Re ≤ 5; 1 on [−101, 5] |
| pole orders / raises | SP thm:sp-spectrum, cor:sp-lstar (c) | all 1 at Re ≤ 5; each raise ≤ 1 |
