# Review R-P-LL: proofs/P-LL.md (Chebyshev interpolation lemma; the size of λ_L)

## Verdict

**CONFIRMED — 0 Major, 0 minor, 3 nits.**

The new lemma is correct. Its closed form is right, and C_(1,m) = m((2m − 2)^(m−1)/(m − 1)!)^(1/m) is exact. The
citation of Duffin–Schaeffer matches what the proof uses. Every step of the new remark checks, and every inequality
points the way an upper bound on Λ_4 needs. **The bound 2.709·10⁻¹² stands.** The remark's own inputs give
Λ_4(0) ≤ 2.70868·10⁻¹², with a margin of 1.1·10⁻⁴ in the logarithm at the last printed comparison.

The remark claims nothing at P*. Its scope is "every l5, A, τ0, T and K that thm:layer admits", so μ0 = √72 l5². The
derivation uses only m and env_C, through c_e > 1 and the support [1/2, 7/2].

All six placement old texts occur exactly once at the stated lines. A simulation of the placement assembles with 0
problems, and the assembled text lints with 0 hits. `python3 assemble.py --check` on the unchanged tree ends with
"labels 4579, computations cited 0, problems 0".

## Findings

### n1 (nit) — the quoted display of Theorem III: the range and the label could not be read in the journal text

- **Location:** proofs/P-LL.md lines 114–122 (the new thm:std-duffin-schaeffer, placement item 5).
- **What I could confirm.** I read the AMS PDF (pdf text layer, 12 pages) through a scraping connector, because the
  proxy refuses ams.org directly. These parts of the quotation agree word for word:
  - "Let f(z) be a polynomial of degree n satisfying |f(cos(νπ/n))| ≤ 1; ν = 0, 1, 2, ⋯, n. Then for p = 1, 2, 3, ⋯, n";
  - the bound n²(n² − 1)(n² − 2²)⋯(n² − (p − 1)²)/(1·3·5⋯(2p − 1));
  - "The equality occurs only if f(z) ≡ γT_n(z), |γ| = 1.";
  - the last sentence of the proof, "Now T_n(1) = 1 so, using induction, we find that T_n^(p)(1) is equal to the
    right-hand side of (19).";
  - "the Tchebychef polynomial T_n(x) = cos(n cos⁻¹ x)" on the first page.
- **What I could not confirm.** On Theorem III's display line the text layer has neither the label "(19)" nor the
  range "−1 ≤ x ≤ 1". The label certainly exists, because the proof cites it. The parser also drops other labels on
  display lines, for example (4) and (6) of Theorem I. So the range is probably there too, but I could not read it.
  The proof's own display is legible: "|cf^(p)(x)| ≤ |T_n^(p)(1)|, −1 ≤ x ≤ 1".
- **Why it matters.** Appendix A's convention is that quotation marks enclose the source's own wording.
- **Replacement.** First confirm the line from a page image, which I could not render. If the range is printed, keep
  the text as it is. Otherwise, or if no image is available, replace lines 114–122 by the following. It also adds
  p. 517 to the heading, which the entry already cites in its body:

      **Theorem {#thm:std-duffin-schaeffer}** (Derivatives of a polynomial bounded at the Chebyshev points; [DS41, p. 517;
      Theorem III and its proof, p. 525].) In [DS41], T_n(x) = cos(n cos⁻¹ x) is "the Tchebychef polynomial" (p. 517).
      Theorem III: "Let f(z) be a polynomial of degree n satisfying |f(cos(νπ/n))| ≤ 1; ν = 0, 1, 2, ⋯, n. Then for
      p = 1, 2, 3, ⋯, n,

          |f^(p)(x)| ≤ n²(n² − 1)(n² − 2²) ⋯ (n² − (p − 1)²)/(1 · 3 · 5 ⋯ (2p − 1)).      (19)

      The equality occurs only if f(z) ≡ γT_n(z), |γ| = 1." The variable x of (19) ranges over −1 ≤ x ≤ 1: the proof
      obtains (19) from "|cf^(p)(x)| ≤ |T_n^(p)(1)|, −1 ≤ x ≤ 1", c > 1 a constant, and ends: "Now T_n(1) = 1 so, using
      induction, we find that T_n^(p)(1) is equal to the right-hand side of (19)." The points cos(νπ/n) are the Chebyshev
      points x_j of [[thm:std-chebyshev]].

  Every line is at most 116 characters, before and after label resolution.

### n2 (nit) — "C1 Δτ ≥ 0" is stated without a reason

- **Location:** proofs/P-LL.md line 53, inside the new remark.
- **What is wrong.** The sign is used to drop the factor (1 + C1Δτ/(2π))^(−m/(m−p)) ≤ 1, and the text gives no
  reason for it. It is true:
  - C1 is the bound constant of eq:eq-c1;
  - Δτ = τ_end − τ0 > 0, since τ_end ≥ v_start − r_q(v_start) = v_start − q0 and v_start − τ0 > √μ0 + 1 > q0
    (chapter 2, setting).
- **Replacement** for line 53:

      m = 1456 for K = 6 and m ≥ 1568 for K ≥ 7. Since 4π + 2 C1 Δτ = 4π (1 + C1 Δτ/(2π)), and C1 Δτ ≥ 0, as C1 ≥ 0 and
      τ_end ≥ v_start − q0 > τ0,

### n3 (nit) — the "Unchanged" list of placement item 7 omits two users of the lemma

- **Location:** proofs/P-LL.md lines 202–204. This is placement wording, not paper text.
- **What is wrong.** prop:layer-regions and thm:layer-past also rest on the lemma. prop:layer-regions takes
  m := max(56M, 4PM, ⌈4M/δ⌉), and thm:layer-past takes m := 56 M_P. Both use it through its inequality only, for any
  m ≥ 2, so they are unaffected.
- **Replacement** for "[[cor:layer-interpolation-band]], [[lem:layer-levels]] and the statement and proof of
  [[thm:layer]], which use the lemma only through its inequality.":

      [[cor:layer-interpolation-band]], [[lem:layer-levels]], the statement and proof of [[thm:layer]], [[thm:layer-past]]
      and [[prop:layer-regions]], which use the lemma only through its inequality.

## Line-by-line check

### The lemma (lines 7–42)

- **The nodes.** x_k = u − H/2 + (H/2)cos(kπ/n), k = 0..n, n = m − 1 ≥ 1. They are distinct, lie in [u − H, u],
  and x_0 = u.
- **The rescaled polynomial.** Q(s) = P(u − H/2 + (H/2)s)/E has real coefficients and degree ≤ n, and
  |Q(cos(kπ/n))| = |f(x_k)|/E_f(v) ≤ 1, since x_k ≤ u ≤ v. These are exactly the hypotheses of Theorem III.
- **Degree below n.** Q + εT_n then has degree n, and its modulus at the nodes is ≤ 1 + ε. Dividing by 1 + ε and
  letting ε → 0 is correct, since T_n^(i) is bounded on [−1, 1].
- **The interpolant at the endpoint.** P^(i)(u) = (2/H)^i E Q^(i)(1), so |P^(i)(u)| ≤ 2^i T_n^(i)(1) E H^(−i), with
  1 ≤ i ≤ n = m − 1. That is the lemma's range 0 < i < m.
- **The remainder.**
  - By Rolle's theorem g^(i) has m − i distinct zeros in I.
  - Newton's form gives g^(i)(u) = g^(i)[x′_1, …, x′_(m−i), u] Π(u − x′_j).
  - That divided difference equals f^(m)(ξ)/(m − i)! with ξ ∈ I ⊂ (−∞, v].
  - Each |u − x′_j| ≤ H, so |g^(i)(u)| ≤ M_m(v) H^(m−i)/(m − i)!.
- **The substitution.** H = κ(E/M)^(1/m) gives E H^(−i) = κ^(−i) E^(1−i/m) M^(i/m) and
  M H^(m−i) = κ^(m−i) E^(1−i/m) M^(i/m).
- **Weighted AM–GM.** The weights are (m − i)/m and i/m. The powers of κ cancel, since
  −i(m − i)/m + (m − i)i/m = 0. Equality holds at κ^m = i a (m − i)!/(m − i).
- **The closed form.** C_(i,m) = (ma/(m − i))^(1−i/m) (m/(i(m − i)!))^(i/m) agrees with the direct minimum to 10⁻³⁵
  relative, for m = 4, 6, 9, 30 with every i, and for m = 1456 with i = 1, 2, 3, 4, 26.
- **At i = 1.** a = 2(m − 1)² gives (2m(m − 1))^((m−1)/m)(m/(m − 1)!)^(1/m) = m((2m − 2)^(m−1)/(m − 1)!)^(1/m),
  checked algebraically and numerically at m = 5, 17, 1456.
- **The product formula.** T_n^(i)(1) = Π_(j<i)(n² − j²)/(2j + 1) is the value the source proves.
- **Sharpness at the endpoint.** Σ_k |l_k^(i)(1)| on the Lobatto nodes equals T_n^(i)(1) for n = 3, 5, 8, 12 and every
  i ≤ n. This is not needed for the proof.
- **A test function.** For f = exp(−1/v) on v > 0, with (m, v) = (6, 0.6), (6, 2), (8, 0.4), (10, 1) and every
  0 < i < m, the lemma's inequality holds; the worst ratio of left to right side is 0.021.
- **The zero cases.** If M_m(v) = 0 or E_f(v) = 0, the function is zero on (−∞, v] and the inequality is trivial.

### Uses of the lemma

The uses are in cor:layer-interpolation-band (with C_(0,m) := 1), eq:layer-margin-lower, lem:layer-levels (i = 1),
the proof of thm:layer, prop:layer-regions and thm:layer-past. In the proof of thm:layer it enters:

- Λ_4 (i = 1);
- C_ε (i ≤ M, m = 56M);
- Λ_5′ (i ≤ 4);
- Λ_8b–Λ_8d (through C_ε).

Each takes the lemma only as "sup_(v′≤v)|f^(i)| ≤ C_(i,m) E_f^(1−i/m) M_m^(i/m) for 0 < i < m". The new lemma has the
same hypotheses and the same conclusion, with finite constants C_(i,m), so no proof changes.

- The notation Λ_(i,m) and the old "in particular" bound C_(i,m) ≤ Λ_(i,m) + (m − 1)^(m−i) occur only in the old
  lemma and the old remark.
- Chapter 85 (line 1906) uses cor:layer-interpolation-band only.
- No other chapter cites C_(i,m).
- The new constants at m = 1456: log10 C_(i,1456) = 3.8966206, 7.3116032, 10.500934, 13.540637 and 66.861203 for
  i = 1, 2, 3, 4, 26.
- The old C_(1,1456) was at least 10^430.

### The remark (lines 44–107)

- **The two global inputs.**
  - λ_L ≤ Λ_4 is a minimum.
  - M_m in Λ_4 is the global sup |env^(m)| of eq:layer-cost-level, so a lower bound on M_m is the right direction.
- **The exponent.** m = 56M, M = 2N + 8 = 2K + 14, so m = 112K + 784. That gives 1456, 1568 and 1680 at K = 6, 7, 8,
  and m/(m − p) = 1456/1442 at K = 6.
- **eq:layer-size-base.** 8·4π = 32π, and the factorisation is exact.
- **eq:layer-size-c.**
  - The trapezoid sum Σ_(k=1)^(n−1)(ln k + ln(k + 1))/2 = ln n! − (1/2)ln n lies below ∫_1^n ln x, since ln is concave.
  - The first form is exact algebra.
  - The second form subtracts (1/2)ln m ≥ (1/2)ln(m − 1), so it is lower.
- **Taylor's formula.** Every derivative of env_C vanishes at 1/2, so env_C(1/2 + x) = env_C^(m)(ξ)x^m/m! with
  ξ ∈ (1/2, 1/2 + x). This gives eq:layer-size-taylor for 0 < x < 3.
- **The substitution.** y = (2v − 4)/3 = t − 1, and cos(π(t − 1)/2) = sin(πt/2).
- **The exponent of env_C.** 1 − y² = t(2 − t) and 1/(t(2 − t)) = 1/(2t) + 1/(4 − 2t). With c_e > 1
  (lem:envelope-constant (b) gives c_e > 1.3240867), eq:layer-size-edge follows.
- **K = 6, the Taylor point.** x = 3/5776 gives t = 1/2888, 1/(2t) = 1444 and 1/(4 − 2t) = 1444/5775.
- **K = 6, the sine.** sin s ≥ s − s³/6, and ln(1 − w) ≥ −w/(1 − w).
- **K = 6, the factorial.** The midpoint rule overestimates ∫ ln on each cell, because ln is concave, and ln 1 = 0, so
  the sum from k = 2 is ln 1456!.
- **K ≥ 7, the Taylor point.** x = 3/(4m) gives t = 1/(2m) ≤ 1, 1/(2t) = m and 1/(4 − 2t) ≤ 1/2.
- **K ≥ 7, the sine.** sin(πt/2) ≥ t, by concavity on [0, 1].
- **K ≥ 7, the factorial.** m! ≥ (m/e)^m.
- **K ≥ 7, M_m.** The resulting M_m ≥ e^(1/2)(2m)^(−12)(4m²/(3e²))^m is exact algebra.
- **β(m).** Composing the second form of eq:layer-size-c with this bound on M_m gives exactly β(m). I checked this
  symbolically and numerically at m = 1568.
- **β′(m).** β′(m) = 3/m − 25/(2m²) + (14 ln 2 + 3/2 + (25/2)ln m)/m² > 0 for m ≥ 5.
- **K = 7.** It uses the exact exponent 1568/1554.
- **K ≥ 8.** It uses B_m > 1 and m/(m − p) > 1, which give B_m^(−m/(m−p)) ≤ B_m^(−1).
- **Scope.**
  - The remark speaks of λ_L "for every l5, A, τ0, T and K that thm:layer admits", and calls it the threshold the proof
    delivers, not the largest admissible λ.
  - It makes no statement at the numerical point P* (l5 = 1/10, not a point of equality), where thm:layer does not
    apply.
  - The source's coefficient 0.945 is rightly absent: it is Δτ/(2π) at P* rounded up from an upper bound of Δτ.

## Numbers recomputed (mpmath, 50–60 digits; each printed bound checked in its stated direction)

### The interpolation constant at m = 1456

| quantity | text | recomputed |
|---|---|---|
| ln 1456 | 7.2834482… | 7.28344822876 |
| 1455 ln 2 | 1008.5291477… | 1008.52914771 |
| (1/2) ln 1455 | 3.6413805… | 3.64138058980 |
| 1455 ln 2 + 1454 − (1/2) ln 1455 | ≥ 2458.887766 | 2458.88776712 |
| ln C_(1,1456), first form | > 8.972244 | 8.97224477 (second form 8.97224454) |
| ln C_(1,1456), exact | — | 8.97230041; log10 = 3.8966206 |

### M_1456 at x = 3/5776

| quantity | text | recomputed |
|---|---|---|
| w = s²/6 | < 4.94·10⁻⁸ | 4.93054·10⁻⁸ |
| w/(1 − w) | < 10⁻⁷ | 4.93054·10⁻⁸ |
| 1456.5 ln 1456.5 | 10608.842431… | 10608.8424310 |
| 1.5 ln 1.5 | 0.6081976… | 0.60819766 |
| ln s | −7.5167367… | −7.51673679 |
| 1444/5775 | 0.2500432… | 0.25004329 |
| 1456 ln(5776/3) | 11011.515994… | 11011.5159946 |
| group 1 (midpoint) | > 9153.2342 | 9153.23423 (exact ln 1456! = 9153.26134) |
| group 2 | > −90.200843 | −90.2008427 |
| group 3 | > −1443.250044 | −1443.2500433 |
| group 4 | > 11011.515994 | 11011.5159946 |
| ln M_1456 (lower) | > 18631.299 | 18631.29934 |
| (1/1456) ln M_1456 | > 12.796221 | 12.79622208 |

### Λ_4 at K = 6

| quantity | text | recomputed |
|---|---|---|
| ln(32π) | 4.6104657… | 4.61046579 |
| (ln 2)/1456 | 0.0004760… | 0.00047606 |
| ln B_1456 (lower) | > 26.378453 | 26.3784566 |
| (1456/1442)·26.378453 | > 26.63455 | 26.6345545 |
| ln(2.709·10⁻¹²) | −26.634441… | −26.6344416 |
| Λ_4 bound from the remark's inputs | < 2.709·10⁻¹² | 2.708684·10⁻¹² |

- With the exact C_(1,m), the exact factorial and c_e > 1, the bound is 2.708481·10⁻¹².
- With c_e > 1.3240867 as well, it is 2.707954·10⁻¹².

### K ≥ 7

| quantity | text | recomputed |
|---|---|---|
| ln(256π/(3e)) | 4.5912950… | 4.59129504 |
| ln 1568 | 7.3575562… | 7.35755620 |
| ln 1680 | 7.4265490… | 7.42654907 |
| β(1568) | > 26.598 | 26.5981642 |
| β(1680) | > 26.809 | 26.8090161 |
| (1568/1554)·26.598 | > 26.837 | 26.8376216 |
| e^(−26.837) | < 2.22·10⁻¹² | 2.21227·10⁻¹² |
| e^(−26.809) | < 2.28·10⁻¹² | 2.27509·10⁻¹² |

### The source's claim at P* (report only, not edition text)

- Δτ = 13/2 − q_end ∈ (5.9372078, 5.9372085), so Δτ/(2π) ∈ (0.94493597, 0.94493608) < 0.945.
- (0.945/a)^1.0097 < 1.0000685, which gives 2.708684·10⁻¹² × 1.0000684 = 2.70887·10⁻¹² < 2.71·10⁻¹².
- 1456/1442 = 1.0097087 > 1.0097.
- At the equality point with the same parameters, Δτ/(2π) = 0.8685479.

All of these agree with the writer's report.

## Citation check

- **Bibliographic record.** The AMS article page confirms: R. J. Duffin and A. C. Schaeffer, *A refinement of an
  inequality of the brothers Markoff*, Trans. Amer. Math. Soc. 50 (1941), 517–528, doi:10.1090/S0002-9947-1941-0005942-4.
  The [DS41] entry matches it, and its format matches [See64] and [MM87]. The order DS23 < DS41 < Dya16 is correct.
- **Theorem number.** It is Theorem III, in Section III "Markoffs' inequalities".
  - The hypothesis is that f has degree n and |f(cos(νπ/n))| ≤ 1 for ν = 0..n. The theorem allows complex
    coefficients; the sentence before it says so.
  - The conclusion is the W. Markoff bound T_n^(p)(1) for p = 1..n, on the real interval. The proof obtains it with
    c > 1 from the Remark to Theorem I and evaluates T_n^(p)(1) by the recursion (2p + 1)T_n^(p+1)(1) =
    (n² − p²)T_n^(p)(1).
  - The lemma uses exactly this, at the endpoint s = 1, for a real polynomial of degree ≤ n, with the εT_n perturbation
    for degree < n. Theorem II, the strip version, needs real coefficients and is not used.
- **The page, p. 525.** I confirmed it by page arithmetic, not by reading the printed folio. The PDF has 12 pages for
  pp. 517–528, so it has no cover sheet and PDF page k is p. 516 + k.
  - The first 8 PDF pages end exactly at the statement of Theorem II.
  - The first 9 PDF pages contain Theorem III, its proof and the quoted last sentence, and end at "… does not include
    the point x = cos(λπ/n). If".
  - So Theorem III and the end of its proof lie wholly on PDF page 9, which is p. 525.
  - "the Tchebychef polynomial" is on PDF page 1, which is p. 517.
  - This reproduces the writer's inference independently. The direct download (403), two other fetch connectors and a
    rendered screenshot all failed.
  - p. 525 can stand. Suggested wording if the coordinator prefers not to rely on page arithmetic: "[DS41, Section III,
    Theorem III and its proof]", or the full range "pp. 517–528".
- **Quoted text.** See n1. Everything is verbatim except the display's "−1 ≤ x ≤ 1" and "(19)", which the text layer
  does not carry.
- **Appendix format.** It follows chapter 95's pattern: a title, then the citation in parentheses, as in
  thm:std-sbierski and thm:std-mazzeo-melrose; then "In [DS41], …" and the source's words in quotation marks. The
  opening paragraph's journal-page sentence is updated consistently (item 4). Rewrapped, it equals the old lines 8–12
  with only "[See64] and [MM87] are" changed to "[See64], [MM87] and [DS41] are".

## Placement texts

- **The six old texts.** After whitespace normalisation, and with "(its equation label)" read as
  {#eq:layer-interpolation}, each occurs exactly once:
  1. chapter 84, lines 844–862;
  2. chapter 84, lines 1354–1365;
  3. chapter 90, lines 97–98;
  4. chapter 95, lines 8–12;
  5. chapter 95, the last line "…". Here log is the natural logarithm.";
  6. chapter 98, [DS23] directly followed by [Dya16].
- **Every new text is true.** Chapter 90's "below 2.71·10⁻¹²" is the remark's uniform bound.
- **Other statements of λ_L's size.** In chapters/*.md, "10^(−430)" occurs only at 84:1357 and 1362–1365 (replaced
  by item 2) and 90:98 (item 3). There is no "10⁻⁴³⁰" anywhere.
- **Sentences that stay true.**
  - 84:17 says λ_L is written as an explicit formula.
  - 85:2058 says C_L11 and C_L4 are not evaluated.
  - 86:11 says c_e > 1 is what the remark uses.
  - 90:95–96 says λ_L is not evaluated.
- **Outside chapters/.** PAPER.md (generated), STATUS.md:57 and INTEGRATION.md:960 and 1196 still say 10^(−430). They
  are not chapter text and are for the coordinator's records. INTEGRATION.md:960's "proves λ_L ≤ 10^(−430) at the
  numerical point" is also inexact about the point.

## Contract

- **Line lengths.** Simulated placement, then assemble.number/resolve and lint.scan_text in assembled mode: 0
  problems, 0 lint hits. The longest resolved inserted line is 119 characters, and the maximum over the whole
  assembled text is 121. In the proof file itself the maximum is 121.
- **Wrapped lines.** No inserted paragraph line starts with "+ ", "- ", "* ", "> ", "#", "=" or "|". The only lines
  that do are displays indented four spaces (lines 33 and 118), the proof file's own headings, and the bibliography
  list item.
- **Labels and characters.** No backslash anywhere. All label keys are lowercase. The four new equation keys and
  thm:std-duffin-schaeffer collide with no existing key.
- **Lint.** `python3 lint.py proofs/P-LL.md` flags only references to labels defined in other chapter files, and
  every such label is defined in chapters/*.md. It reports no file, program, code or AI language.
- **Assembly.** `python3 assemble.py --check` ends: **labels 4579, computations cited 0, problems 0**.
