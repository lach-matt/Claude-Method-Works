# Report P-LL: λ_L with Chebyshev/Duffin–Schaeffer interpolation, and the source's 2.71·10⁻¹²

Proof text: `research/warp-drive/paper/reader/proofs/P-LL.md` (208 lines; lint clean apart from cross-file label
references and the intended duplicate keys of the replacement texts; every line ≤ 121 also after label resolution).

## 1. Verdict

**Proved in corrected form.** The claim

    Λ_4(C1) ≤ 2.71·10⁻¹² (1 + 0.945 C1)^(−1.0097)   at P*

is **true**, but the source's argument does not prove it as written. It has two direction slips, and the claim
survives only because the source rounded 2.704 up to 2.71:

- the interpolation constant enters at log10 C^Ch_(1,1456) = 3.89723, a grid-point value that is an **upper** bound of
  the minimum, where a lower bound is needed. The exact value is **3.8966206**;
- the coefficient 0.945 is Δτ/(2π) worked out from a certified **upper** bound of Δτ (5.937209) and then rounded up. An
  upper bound on Λ_4 needs a lower bound of Δτ. The true value is Δτ/(2π) ∈ (0.9449359, 0.9449361) < 0.945.

The best proved bound at C1 = 0 (exact C_(1,m), the source's own Taylor point, c_e > 1.3240867) is
**Λ_4(0) ≤ 2.70796·10⁻¹² = 10^(−11.56736)**. The source printed "Λ_4 ≤ 10^(−11.568)" (= 2.704·10⁻¹²), and that
figure is **not proved**: with its own inputs corrected it reads 10^(−11.5674). It is not refuted either, because the
true M_1456 is unknown. The source's 2.71·10⁻¹² holds with margin about 0.08 %.

The edition's version, written out in the proof text, uses only c_e > 1 and elementary factorial bounds. It gives
Λ_4(0) < 2.70869·10⁻¹² < 2.709·10⁻¹². Combined with the C1 factor:

    Λ_4(0)(1 + aC1)^(−1456/1442) ≤ Λ_4(0) (0.945/a)^1.0097 (1 + 0.945 C1)^(−1.0097),   a = Δτ/(2π) > 0.9449359,

The first step uses 1 + aC1 ≥ 1 and 1456/1442 > 1.0097. The second uses (1 + 0.945C)/(1 + aC) ≤ 0.945/a. Here
(0.945/a)^1.0097 < 1.0000685, so the right side is ≤ 2.70887·10⁻¹² (1 + 0.945 C1)^(−1.0097) < 2.71·10⁻¹²(…) for every
C1 ≥ 0. **The claim at P* is proved.**

**Caveat on P*.** P* is the numerical point of the source's constants document: l5 = 1/10, μ0 = A = T = 1, τ0 = −2.
In the edition this is def:lambda0-point, and it is **not a point of equality** (μ0 = 1 > √72/100). thm:layer does
not apply there, as the edition says at 86:26. "λ_L at P*" is therefore the formula of eq:layer-threshold evaluated
at a point where the theorem is silent.

The source's layer constants use the equality r_q: C_Φ through r_q′ = μ0^(1/4) μ^(−3/4) μ′/4, and C_m0. Its Δτ,
however, comes from the l5 = 1/10 point (q_end = 0.56279).

At the equality point with the same μ0, A, τ0, T and env_C (l5 = 72^(−1/4), r_q(V) = (227/192)^(1/4)), the values are
Δτ = 13/2 − (227/192)^(1/4) ∈ (5.457247, 5.457248) and Δτ/(2π) = 0.868548. There the proved form is
2.709·10⁻¹² (1 + 0.86855 C1)^(−1456/1442). The coefficient 0.945 is not implied once C1 exceeds about 0.012, and it is
not refuted either: the upper bound B(1456) gives only Λ_4(0) ≥ 1.25·10⁻¹².

**The C1-free statement holds at every admissible point, equality or not.** That statement is "the threshold this proof
delivers is below 2.71·10⁻¹², whatever Theorem 1's constants are". It is the one the edition carries.

## 2. The source's argument, reconstructed

- **Chebyshev–Lobatto constants** (A15, EQUALITY5-LAYER.md 969–975; R4.5, 1568–1574). Take the interpolant P on the
  nodes u − H/2 + (H/2)cos(kπ/n), n = m − 1.
  - Its i-th derivative at the endpoint is bounded by (2/H)^i T_n^(i)(1) E. This is the endpoint row sum of the
    differentiation matrix, equal to n² at i = 1.
  - The remainder f − P has m − i zeros of its i-th derivative in [u − H, u]. So |(f − P)^(i)(u)| ≤ M_m H^(m−i)/(m − i)!.
  - This gives C^DS_(i,m) = min_κ [T_(m−1)^(i)(1)(2/κ)^i + κ^(m−i)/(m − i)!], which is the edition's new
    eq:layer-interpolation.
  - The source checked the row-sum identity in floating point at n = 1455 and said "the general n is the
    Duffin–Schaeffer inequality, not re-derived" (lamL5b M3; EQUALITY5-LAYER.md 1717).
  - Values printed: log10 C^DS_(i,1456) = 3.897, 7.312, 10.501, 13.541.
- **Duffin–Schaeffer, as used.** If p has degree n and |p(cos(kπ/n))| ≤ 1 for k = 0..n, then |p^(i)| ≤ T_n^(i)(1) on
  [−1, 1]. Applied to P/E after the affine map, this gives the endpoint bound.
  - Sharpness at the endpoint comes from T_n itself. So the row sum equals T_n^(i)(1) exactly. I checked this exactly
    at n = 5 and n = 8 for i ≤ 3.
- **Lemma L.4′** (1474ff.). Lemma L.4's remainder bound |w| ≤ C λ^(N−5) ε_(M*)(v1) holds under ε_4(v1) ≤ λ instead of
  ε_(M*)(v1) ≤ λ³. This replaces Λ_5 by Λ_5′, which needs C_(i,m) only for i ≤ 4. In the edition this is
  lem:layer-remainder-weak with Λ_5′, already carried. It does not touch Λ_4.
- **P*** (lamL5.py header; CONSTANTS5): μ0 = A = 1, τ0 = −2, v_s = 1/2, K = 6 (N = 9, M = 26, m = 1456), p = 14,
  env_C, and τ_end − τ0 ≤ 5.937209.
- **C1 and Δτ.** These enter only through L = (4π + 2C1Δτ)λ. Hence
  Λ_4(C1) = Λ_4(0)(1 + C1Δτ/(2π))^(−m/(m−p)), with m/(m − p) = 1456/1442 = 1.0097087.
- **M_1456 and B(1456).**
  - R3.3 evaluated Λ_4 with the Cauchy-estimate upper bound M_1456 ≤ B(1456) = 10^8573.894, giving
    "Λ_4 at C1 = 0 (an upper bound of Λ_4) = 1.25·10⁻¹²". **Wrong direction**: Λ_4 decreases in M_m, so a bound
    computed with B is a lower bound of Λ_4.
  - The source's own V-M2 (R4.5/R4.6) flagged this. It replaced B by the Taylor lower bound
    M_1456 ≥ m! env(v_s + x)/x^m at x = 5.1·10⁻⁴ (log10 M_1456 ≥ 8091.60), which gives the 2.71·10⁻¹².
  - B(1456) still appears, correctly, as the input to the lower bounds of the thresholds (R4.6 "a valid upper bound").

## 3. Direction check (an upper bound on Λ_4 needs lower bounds on C_(1,m), M_m^(1/m) and 4π + 2C1Δτ)

| input | source used | needed | verdict |
|---|---|---|---|
| M_1456, R3.3 | B(1456) = 10^8573.894 (upper) | lower | wrong; 1.25·10⁻¹² is a lower bound of Λ_4(0) |
| M_1456, R4.5 M5 | Taylor at x = 5.1·10⁻⁴, c ≥ 1.32407110621, interval lower end: 10^8091.604 | lower | right (re-derived: 8091.6042 at x = 3/5776) |
| C_(1,1456), R4.5 M5 | hard-coded 3.89723 (lamL5b.py:303) = value at the grid point of lamL5 cstar, a log-κ grid of step 0.005 (lamL5.py:206), times 1 + 10⁻³⁰ | lower | **wrong** by +0.00061 in log10; exact closed form m((2n)^n/n!)^(1/m) gives 3.8966206 |
| C^DS_(i,1456) in M4/M5 (cds, κ step 1/4) | grid values | lower in M5 | wrong in principle, negligible (< 2·10⁻⁵ in log10) |
| Δτ in the C1 factor | 5.937209, a certified **upper** bound; 5.937209/(2π) = 0.9449362, rounded up to 0.945 | lower | **wrong**; true Δτ/(2π) > 0.9449359; costs a factor ≤ 1.0000685 |
| exponent 1.0097 | ≤ 1456/1442 | ≤ true value (base ≥ 1) | right |
| 4π + 2C1Δτ ≥ 4π at C1 = 0 | yes | lower | right |

Each slip is absorbed by the rounding of 2.704 up to 2.71. The claim therefore stands, but not by the source's argument.

## 4. Every number recomputed

Exact rationals plus outward-rounded 200-bit interval arithmetic, scratch scripts only. Every inequality printed in the
proof text was re-checked in the direction stated.

- C_(i,m) closed form: C_(i,m) = (m a/(m − i))^(1−i/m) (m/(i (m − i)!))^(i/m), a = 2^i T_(m−1)^(i)(1), from weighted
  AM–GM; it agrees with the direct minimum.
  - log10 C_(i,1456), i = 1, 2, 3, 4, 26: 3.8966206, 7.3116032, 10.500934, 13.540637, 66.861203.
  - The source's 3.897, 7.312, 10.501, 13.541 are upper roundings.
  - Elementary lower bound used in the paper (n! ≤ e√n(n/e)^n): ln C_(1,1456) > 8.972244, i.e. log10 > 3.896596.
- log10 M_1456 lower bounds at x = 3/5776, the optimum of exp(−3/(4x)) x^(12−m):

  | ln m! | c_e lower bound | log10 M_1456 ≥ |
  |---|---|---|
  | exact | 1.3240867 | 8091.6042 |
  | exact | 1 | 8091.4823 |
  | midpoint rule (as printed) | 1 | 8091.4705 |

  So log10 M^(1/1456) ≥ 5.557329.
- Upper bounds on Λ_4(0) at m = 1456:

  | inputs | Λ_4(0) ≤ |
  |---|---|
  | exact C, exact m!, c_e > 1.3240867 | 2.70795·10⁻¹² |
  | elementary bounds, c_e > 1.3240867 | 2.70816·10⁻¹² |
  | elementary bounds, c_e > 1 (the paper's) | 2.70868·10⁻¹² |
  | source inputs (3.89723, 8091.604) | 2.70412·10⁻¹², the source's "10^(−11.568)" |

- Δτ at P*: 13/2 − q_end with q_end ∈ (0.5627915, 0.5627922) (86 lem:lambda0-point (c), (e)), so Δτ ∈ (5.9372078,
  5.9372085). At the equality point, Δτ = 13/2 − (227/192)^(1/4) ∈ (5.4572477, 5.4572478).
- K ≥ 7 (paper): β(m) = ln(256π/(3e)) + 3 ln m − (14 ln 2 + 3/2 + (25/2) ln m)/m. β(1568) = 26.598164 and
  β(1680) = 26.809016. So Λ_4 < 2.22·10⁻¹² at K = 7 and < 2.28·10⁻¹² for K ≥ 8.
- Other thresholds, for information only; the edition evaluates none of them. Λ_5′ ∈ [10^(−2.9233), 10^(−2.8211)],
  binding i = 4; the lower end uses the source's B(1456), which I did not re-derive. log10 C_ε ∈ [211.45, 220.06].
  Both agree with R4.5/R5.6.
- Sanity checks: the Chebyshev lemma held on exp(−1/x) at (i, m) = (1,6), (2,6), (3,6), (5,6), (1,8), (4,8), with worst
  ratio 0.25.

## 5. Duffin–Schaeffer: the citation, checked against the journal

- Journal record (pubs.ams.org): **R. J. Duffin** and A. C. Schaeffer, *A refinement of an inequality of the brothers
  Markoff*, Trans. Amer. Math. Soc. 50 (1941), 517–528, doi:10.1090/S0002-9947-1941-0005942-4, MR0005942.
  - **The prompt's "A. J. Duffin" is wrong.** The author is Richard J. Duffin.
- Text read from the AMS PDF:
  - **Theorem III**: "Let f(z) be a polynomial of degree n satisfying |f(cos(νπ/n))| ≤ 1; ν = 0, 1, …, n. Then for
    p = 1, …, n, |f^(p)(x)| ≤ n²(n² − 1)⋯(n² − (p − 1)²)/(1·3·5⋯(2p − 1)), −1 ≤ x ≤ 1 (19)", plus the equality clause.
  - The proof ends with "T_n^(p)(1) is equal to the right-hand side of (19)".
  - T_n is defined on the first page.
- **Page: p. 525, inferred, not read.**
  - The proxy refuses ams.org, so I read the PDF through a scraping connector, truncating to the first k pages.
  - Four pages end mid-sentence inside Theorem I's proof; eight pages end exactly at Theorem II's statement; nine pages
    contain Theorem III and the end of its proof.
  - With 12 PDF pages for pp. 517–528 and the title on PDF page 1, Theorem III and the quoted sentence are on p. 525.
    The printed running head was not legible to the tools; one rendered-page attempt timed out.
  - **The coordinator may wish to confirm "p. 525" from a printed copy.**
- The edition needs only real coefficients and real x. The lemma's proof handles degree < n by perturbing with εT_n.

## 6. Should the edition carry the Chebyshev version? Yes.

- It is the source's latest form. R4.5–R5.6 state λ_L with the Duffin–Schaeffer constants, and the crosswalk note
  "Chebyshev-Lobatto variant not carried" marks this as the one point where the edition kept an older constant.
- The proof is as short as the old one, given one classical theorem in Appendix A.
- Every downstream form is unchanged: eq:layer-threshold, cor:layer-interpolation-band, lem:layer-levels and the proof
  of thm:layer use only the lemma's inequality. thm:layer stays true as an existence statement, now with a larger
  delivered threshold.
- Size: Λ_4 goes from ≤ 10^(−430) to < 2.709·10⁻¹² at K = 6.
- No form of eq:layer-threshold changes.

## 7. What changes in the edition (exact texts in the Placement section of P-LL.md)

1. **84, lem:layer-interpolation (844–862):** whole lemma replaced.
   - Nodes: Chebyshev points on [u − H, u].
   - Constant: C_(i,m) := min_κ [2^i T_(m−1)^(i)(1) κ^(−i) + κ^(m−i)/(m − i)!].
   - Added: the closed form, and C_(1,m) = m((2m − 2)^(m−1)/(m − 1)!)^(1/m).
   - Dropped: the κ = 1 "in particular" bound, which nothing else uses (grep: Λ_(i,m) and (m − 1)^(m−i) occur only in
     the lemma and the remark).
2. **84, rem:layer-threshold-size (1354–1365):** replaced. λ_L ≤ Λ_4 < 2.709·10⁻¹² (1 + C1Δτ/(2π))^(−1456/1442) for
   K = 6, < 2.3·10⁻¹² for K ≥ 7, hence below 2.71·10⁻¹² for every l5, A, τ0, T, K. Stated for env_C, and as the
   threshold the proof delivers. Four new private equation keys: eq:layer-size-base, -c, -taylor, -edge.
3. **90-scope 97–98:** "at most 10^(−430)" becomes "below 2.71·10⁻¹²".
4. **95, opening paragraph 8–12:** [DS41] added to the journal-page list (rewrapped).
5. **95, sec:std-chebyshev:** new thm:std-duffin-schaeffer after thm:std-chebyshev.
6. **98:** [DS41] entry between [DS23] and [Dya16]. The key [DS23] is Disconzi–Shao, so the new key is DS41.
7. **Unchanged:** chapters 01 and 03, which state no size of λ_L; 85:2058, which states no size; 86:11 ("c_e > 1 is
   also what the remark uses"), still true because the new remark uses only c_e > 1.

## 8. For the coordinator (not edited by me)

- Crosswalk rows to update:
  - 84-equality-layer.tsv lem:layer-interpolation, eq:layer-interpolation: source EQUALITY5-LAYER.md 969–975 and
    1568–1574 (A15 with R4.5's C^DS).
  - rem:layer-threshold-size: the hand bound replaces the "reported, not carried" note; the source's 2.71·10⁻¹² is now
    proved, after correcting C_(1,m) and Δτ.
  - 95's crosswalk: a new row for thm:std-duffin-schaeffer.
  - OUTLINE.md: register the bibliography key DS41 and the exported key thm:std-duffin-schaeffer.
- The source itself should note the two direction slips (lamL5b.py:303's 3.89723; lamL5.py:67's DTAU used as the C1
  coefficient) and the non-equality P*. I made no edit there.
