# Review of P-U71-SP (the poles of the inverse of the ι⁺-normal operator)

Reader: R-P-U71-SP. Read: proofs/P-U71-SP.md (518 lines of text), its report reports/P-U71-SP.md, proofs/P-U71-IS.md as
it stands, reviews/R-P-U71-IS.md, reviews/R-P-U71-close.md, and every cited statement in chapters 20, 22, 33, 34, 35,
36, 38, 41, 42, 71 and in P-A-indicial, P-A3-every-h; for the values, P-U71-assembly and P-U71-close. "l. n" is line n
of proofs/P-U71-SP.md. Private checks are in scratchpad/reader/r_sp/ (pl.py, tensor.py, moment.py, moment2.py,
roots.py, misc.py, contract.py, with their .out files).

## Verdict

**NOT CONFIRMED** — 1 Major, 5 minor, 10 nit.

The analysis is right almost everywhere, and every number I re-derived stands: the moment identity, the reduction
theorem, the moment matrices, the two exact identities at ϰ = 5 (for all parameter values), the valuation certificate
(all twelve values of c_0 and every entry of the table), the list of poles up to real part 5, the kernel dimensions
1, 11, 53, and the vector-type arithmetic. The one Major finding is a gap in the proof of simplicity: for
134 ≤ l ≤ 172 (0.018 ≤ hκ ≤ 0.03) neither the text nor the lemma it cites shows that the two roots of P_l near a(x) are
distinct (F1). They are distinct (computed, and a short proof is given below), so no statement changes; but "every pole
at real part at most 5 is simple" is not proved as written. The same gap sits in P-U71-IS, prop:is-mult, which
R-P-U71-IS did not report.

With (IS): **l_* = 50 is admissible, and the least admissible l_* is L ∈ [39, 50]; K_ι(λ) ≤ 2 on Σ (the text's
bound is l_* + 2 = 52); every raise is 0 or 1.** No value of l_* or K_ι is used in chapter 71, P-U71-assembly or
P-U71-close, so nothing conflicts; several sentences there that call (SP) missing become stale (see "Consistency").

## What I re-derived

- **Moments (lem:sp-moments).** By hand: with g := (v∂_v + ϰ − 3/2 − S̄)u, ∫v^k(−2∂_vg) = 2k∫v^(k−1)g =
  2k(ϰ − k − 3/2 − S̄)𝔪_(k−1)(u), and ∫v^kF(v∂_v)u = F(−k − 1)𝔪_k(u). The continuity (v^k|dv| dg̸ = R^(−k−1)μ_b,
  𝒜^(−k−1) ⊂ H^∞_(b,−k−1−ϵ) ⊂ H^(−s′)_(b,−c), lem:i-c-2-2 (d), (f)) is right.
- **lem:sp-primitive.** (a)–(c) checked step by step: N_sf′ = −2∂_v − 2(v∂_v + ϰ) + a, N_sf″ = −2; the formula
  Iu_j = −∫_v^∞u_j on {v ≥ 4}; v∂_vI = I(v∂_v + 1); the error term O(T^(k+2−c)) in (c). See N3 for one unstated step.
- **thm:sp-reduction.** Injectivity: the descent with c_i = c − i(1 + η) keeps (s + i, c_i) admissible for ϰ_0 − i,
  c_i > 1 and k ≤ K − i − 1 < c_i − 2 at every step, and Re(ϰ_0 − i) ≥ 2 for i ≤ K, so lem:sp-primitive applies;
  Re(ϰ_0 − K − 1) < 2 gives injectivity at the end. Surjectivity: T_N = B(Id − G) with G of finite rank, the
  index count, and the onto map Ψ (the χ_k with ∫v^iχ_k = δ_ik) are right. (b)–(d) follow. lem:sp-pole-order and
  lem:sp-block are right.
- **The matrices.** From the definition [[eq:iii-f-2-1]] in Cartesian coordinates I computed N_s0(ι), S_s0 (4 × 4,
  basis dt̄², dt̄ ⊗_s dr, dr², Σ(dx^i)²) and N_v1(ι), S_v1 (2 × 2, basis dt̄ ⊗_s V̂, dr ⊗_s V̂) for symbolic
  (γ_Υ, e_Υ, γ_C, e_C, v_C). For all parameters
  det N_s0(ι) = −γ_C² ι(ι − 2)(ι − 4)(ι² − 3ι − z)C(ι + 1) and det N_v1(ι) = (ι + 1)(ι − 3)(ι − 4)(ι + 2 + 2γ_Cv_C),
  which is lem:iii-f1-2-1 and the lists s0, v1 of prop:iii-f1-2-3.
- **The two exact identities (lem:sp-two-roots (a), (b)).** Verified symbolically for all parameter values and all ι,
  from the definition of 2L̄ and of S̄ by [[eq:iii-f-2-2]], at two points of ℝ⁴ (r = 5 and r = 13), all 25 components.
  The hand derivation of the text (the six Laplacian and divergence identities, tr Z = 12, Ē^ΥḠh = 0, δ̄Ḡ(r⁻²Z) = 0)
  is right line by line.
- **The kernels at ϰ = 5 (lem:sp-two-roots (c)).** By hand as in the text, and exactly at the computational point
  from the matrices above: dim ker 𝔐_s0 = 1, 1, 2 and dim ker 𝔐_v1 = 0, 1, 2 at ϰ = 3, 4, 5, with
  dim 𝒦_2 = dim 𝒦_1 in each case (no chain of length 2); no kernel at ϰ = 7/2, 9/2.
- **The valuation argument (lem:sp-exceptional).** P_l = det(hN_l) recomputed exactly: c_3 = 10⁻¹⁸ and c_2, c_1 as
  printed; c_0 = (−h(ι − 1)² − (ι − 3))P_0 with P_0 = −(ι − 2)C; the twelve values c_0(q) agree to the last digit, the
  numerators are odd (first nine) and prime to 5 (last three); every coefficient valuation, every lower bound of the
  table and the actual valuations of c_1(q), c_2(q) agree with the table (the lower bounds are attained);
  3218988513000625 = 5⁴·17·23·13172331511. The vector type: each q has denominator 2, 10⁴, 10² or 25.
- **The list (thm:sp-spectrum (a)) and simplicity.** Re-derived from prop:iii-f1-2-3: 𝒮_τ as in lem:sp-roots (a);
  ι_v(1) = 3 (500002² = 250002000004), ι_v(2) = 3.00000499998 ∈ (3, 4), ι_v(l) ≤ 5 ⟺ (l + 1)² ≤ 2000016 ⟺ l ≤ 1413;
  ι_v(l) ∉ {4, 5} (1000009 and 2000016 are not squares). Roots at the point: ι₁ = 2.0000747438…, P_1: 2,
  2.0001201950…, 2.9999580489…; P_2: 2.0000029323…, 2.0001930218…, 2.9998947899…; all in the stated intervals. Every
  difference in lem:sp-roots (c) re-checked. Kernel dimensions: at 3 only s0 (1); at 4 s0, s1, v1 (1 + 4 + 6 = 11); at
  5 s0 (2), s1 (4), s2 (9), v1 (12), v2 (16), t2 (10), total 53.
- **The window 134 ≤ l ≤ 172.** All three roots of real part ≥ 2 computed for every l in it: l = 134, 135 have three
  real roots (separations 0.152, 0.093), l ≥ 136 a real root and a conjugate pair (|Im| from 0.0386 up). Least
  separation of the three roots of real part ≥ 2 over l ≤ 400 and a sample up to 9000: 1.2·10⁻⁴ (at l = 1). The
  inequalities of the fix of F1 are checked in exact rational arithmetic.
- **hκ > 70.** Sample: at l = 8366, 9000 the roots are 72.0, 55.0 ± 25.1i and 83.0, 63.3 ± 26.0i; at l = 20000 all
  real above 234. Sanity only; the text needs, and has (F3), only the conjugation argument.
- **l_* and K_ι.** See "Consistency" below.

## Findings

### Major

**F1 (Major) — l. 302–306 (lem:sp-roots (c)), and so (b) and thm:sp-spectrum (b): for 134 ≤ l ≤ 172 the two roots of
P_l near a(x) are not shown to be distinct.** For 0.018 ≤ x ≤ 0.03, lem:s14-sextic-large (b) gives only that "the
other two roots of P_l in |ι| < 1000 lie in |ι − a(x)| < 0.45" (a Rouché count in one disc); (c) of that lemma, with
its disjoint discs, starts at x = 0.03, and the proof of prop:s14-damping-distance locates real parts only. So "In each
case the three roots are distinct" is unproved for l = 134, …, 172 (x = 0.018224, …, 0.029928). A double real root
ι ∈ (2.06, 2.98) there would make ι − 1 a double root of type sl, c_sl(ι + j) = 2, and the simplicity of the poles at
ι, ι + 1, ι + 2 would fail as proved. The roots are in fact distinct (l = 134, 135: three real roots; l ≥ 136: a
conjugate pair), and the following closes the gap with the bounds already in P-A-indicial.

*Fix.* l. 304, after "([[lem:s14-sextic-large]] and the proof of [[prop:s14-damping-distance]])." insert:

    For 0.018 ≤ x ≤ 0.03 the two roots in |ι − a(x)| < 0.45 are distinct. On that disc |hW| < 9.4·10⁻⁵ (proof of
    [[lem:s14-sextic-large]] (b)); on its real diameter 2 + x − ι ≤ x/4 − 0.05 ≤ −0.0425, and
    𝒬(ι) = 2(ι − a)² − Δ_𝒬(x)/8. If x < x₋, that is l = 134 or 135, then U(a, x) = (2 − x)Δ_𝒬(x)/32 > 2·10⁻³, while
    U(a ± 0.45, x) < −0.0425·0.39 < −0.016, as Δ_𝒬(x) < 0.1 there; so P_l = U + hW is negative, positive and negative at
    a − 0.45, a and a + 0.45, and the two roots are real and separated by a. If x > x₋, that is l ≥ 136 and
    x ≥ 0.018768, then 𝒬 ≥ −Δ_𝒬(0.018768)/8 > 2.87·10⁻³ on ℝ, Δ_𝒬 being decreasing there, so |U| > 1.2·10⁻⁴ > |hW|
    on the real diameter: P_l has no real root in the disc, and its two roots there are a non-real conjugate pair.

(x₋ ∈ (0.01866, 0.01867) and the formulas for U, 𝒬, Δ_𝒬 are lem:s14-sextic-split (iii), (iv); checked exactly:
U(a, x) = 0.0057947 and 0.0021968 at l = 134, 135; −Δ_𝒬(0.018768)/8 = 0.0028797.) The same sentence should go into
prop:is-mult of P-U71-IS (its l. 292–294 cite the same three lemmas for "lie in disjoint sets"); that file is under its
fix round and is not counted here.

### Minor

**F2 (minor) — l. 486–489 (cor:sp-lstar (a)) and l. 516–518 (rem:sp-scope): the values of l_* are not stated, though
(IS) gives them and one bound needs only one line.** The corollary leaves l_* = max(1, L, M) with L and M open, and
the remark calls the multiplicities at real part ≤ 0 and in (4, 5] undetermined. But prop:iii-f1-2-3 (b) gives M ≤ 7
at once (R-P-U71-IS F2), and prop:is-logs gives 39 ≤ L ≤ 50 ((5, 39) ∈ ℰ_ind as constructed; ℰ^ι_ind ≤ 50; the least
ℰ^C_I has order 0, prop:is-ci-pp (a)). So the case "l_* = 1" is vacuous.

*Fix.* l. 488–489, "It equals 1 exactly when L ≤ 1 and M = 1, and is otherwise attained by L or by M." → "Here M ≤ 7,
as at each type and degree n_L ≤ 7 roots have real part at most 0 and n_L real part above 1, counted with multiplicity
([[prop:iii-f1-2-3]] (b)); and for the index sets as constructed 39 ≤ L ≤ 50 ([[prop:is-logs]], [[prop:is-ci-pp]] (a)).
So l_* = 50 is admissible, and the least admissible l_* is L." l. 516–518, "The multiplicities of the indicial roots of
real part at most 0 or in (4, 5], and the logarithmic orders L of [[cor:sp-lstar]] (a), belong to the index sets and are
not determined here." → "The multiplicities of the indicial roots of real part at most 0 or in (4, 5] are at most 7
([[prop:iii-f1-2-3]] (b)) and are not determined here; the logarithmic orders L of [[cor:sp-lstar]] (a) are bounded in
[[prop:is-logs]]." (If the roots in (4, 5] are wanted simple: they are 5 (at s1, s3, v2, v3, t3), 1 + ι^Υ_(s1,3),
1 + ι^Υ_(s2,3), and ι − 1 for the roots ι of P_l and p_(v) with real part in (5, 6]; the argument of lem:sp-roots, with
F1 and F3, gives it.)

**F3 (minor) — l. 307–309: for x > 70 the multiplicity argument is stated for a set.** Simplicity of a non-real root
of P_l with hκ > 70 (the case R-P-U71-IS F1 found unproved in P-U71-IS) rests on this sentence, and it needs the three
roots counted with multiplicity.

*Fix.* "the three roots of real part at least 2 ([[prop:s14-scalar-every-h]]) form a set closed under conjugation, so its
non-real elements form at most one conjugate pair, and two of its elements of real part at most 5 neither coincide nor
differ by a real number." → "the three roots of real part at least 2, counted with multiplicity
([[prop:s14-scalar-every-h]]), are permuted by conjugation, P_l having real coefficients; a non-real one of multiplicity
at least 2 would bring its conjugate with the same multiplicity, four roots in all. So the non-real ones are at most one
conjugate pair of simple roots, the third is real and greater than 51, and two of those of real part at most 5 neither
coincide nor differ by a real number."

With this, the claim that no result depends on where the roots with hκ > 70 lie is right: the description of (a) is
exact for any location, simplicity follows from the conjugation symmetry, and lem:sp-exceptional holds for every
integer κ. It also shows that the "multiplicity at most 3" of R-P-U71-IS F1's fix can be replaced by "simple".

**F4 (minor) — l. 495–497 and 505–506 (cor:sp-lstar (c)): the raise of 𝒮_(λ₀) is cited to the wrong statement, and
"by" should be "by at most".** 𝒮_(λ₀) is the solution of [[cor:iii-g3-3-1]] (1) (ch. 42 l. 738), whose log powers go up
to J + K, K the order of the pole of [[eq:iii-g3-2-2]] at λ₀; on sources without an ℐ⁺-expansion that inverse is the
one of [[thm:iii-g1-3-1]] (2) (ch. 42 l. 779–781), so K ≤ m_ι(λ₀). [[cor:iii-g2-4-3]] is the statement behind the raises
of lem:iii-i10-1-2 (c), which the text treats correctly in its second sentence.

*Fix.* l. 495–496, "𝒮_(λ₀) raises the logarithmic order by m_ι(λ₀) ([[cor:iii-g2-4-3]], l_0 = m_ι(λ₀)): by 1 at the points
of [[thm:sp-spectrum]] (a) and by 0 at every other λ₀ with Re λ₀ ≤ 5." → "𝒮_(λ₀) raises the logarithmic order by at most
m_ι(λ₀) ([[cor:iii-g3-3-1]] (1), whose K is m_ι(λ₀) on these sources, as the proof in [[sec:s23-step]] notes): by at
most 1 at the points of [[thm:sp-spectrum]] (a) and not at all at every other λ₀ with Re λ₀ ≤ 5." l. 505–506, "(c): by
[[cor:iii-g2-4-3]], the logarithmic powers produced are at most k + l_0, l_0 the order of the pole of N_ι⁺(L̄, ·)⁻¹ at the
exponent." → "(c): by [[cor:iii-g3-3-1]] (1) the logarithmic powers produced are at most J + K, and by
[[cor:iii-g2-4-3]] at most k + l_0, with K and l_0 the order of the pole of N_ι⁺(L̄, ·)⁻¹ at the exponent for the
sources in question."

**F5 (minor) — l. 499–501 (cor:sp-lstar (d)): the second half of (SP), which points of Λ lie in spec_ι⁺(L̄), is not
answered.** rem:uc-missing (SP) (P-U71-close l. 339–340) asks "which of these", the points of Λ with
2 ≤ Re λ ≤ 3 + ε_+, lie in spec_ι⁺(L̄). (d) lists spec_ι⁺(L̄) on the strip; Λ there is prop:is-lambda (sums
β + p𝔡₀ + q𝔡₁). The intersection is not stated. It contains 3; whether ι₁ (= 2.0000747…) or a root of some P_l in
(2, 3 + ε_+] lies in Λ is not decided (lem:sp-exceptional covers 5/2 + σ_Υ + ℕ₀ only, not 2 + σ^(2) or
5/2 + σ^(3)). No bound depends on it, every raise being at most 1, and the text should say so.

*Fix.* l. 500, after "All are simple." insert: "Of the points of Λ ∩ {Re ≤ 3 + ε_+} ([[prop:is-lambda]]), 3 is one of
them; whether ι₁ or a root of some P_l in (2, 3 + ε_+] lies in Λ is not decided here, and no bound depends on it, as
each raise is at most 1."

**F6 (minor) — l. 491–493 (cor:sp-lstar (b)): K_ι is bounded only through l_*, though (IS) fixes it.** The bound
K_ι(λ) ≤ 2 + k(ℰ^C_(I,♯), λ) ≤ l_* + 2 holds, but ℰ^C_(I,♯) = (λ_♯, 0) ∪ ℰ^C_I ([[eq:iii-g3-2-1]]) and the least ℰ^C_I
has logarithmic order 0 throughout (prop:is-ci-pp (a)), so m_♯(λ) ≤ 1 and K_ι(λ) ≤ 2 on Σ; and "K_ι(λ) ≤ 3 when
l_* = 1" is vacuous (l_* ≥ 39, F2).

*Fix.* l. 492–493, "≤ l_* + 2, which is at most 2l_* + 1 as l_* ≥ 1, and K_ι(λ) ≤ 3 when l_* = 1." → "≤ l_* + 2, which
is at most 2l_* + 1 as l_* ≥ 1. With the least ℰ^C_I, whose logarithmic orders are 0 ([[prop:is-ci-pp]] (a)),
m_♯(λ) ≤ 1, so K_ι(λ) ≤ 2 for every λ ∈ Σ, and K_ι(λ) ≤ 1 unless λ ∈ spec_ι⁺(L̄) ∩ π_1ℰ^C_I, as at λ = 3."

### Nits

**N1 — l. 167–168.** "≥ 1, and is therefore singular." → "≥ 1, hence > 1, as no root has real part in (0, 1], and is
therefore singular."

**N2 — l. 187–188.** Every admissible pair has c ∈ (Re ϰ_0 − 1, Re ϰ_0) by [[eq:iii-g-2-6]]. "Choose the pair (s, c)
with c ∈ (Re ϰ_0 − 1, Re ϰ_0); the poles and their orders do not depend on the pair ([[thm:iii-g-5-1]] (2))." → "Write
(s, c) for the pair; c ∈ (Re ϰ_0 − 1, Re ϰ_0) by [[eq:iii-g-2-6]]."

**N3 — l. 135–136.** The bound on {v ≥ 4} uses Iu = −∫_v^∞ for W̃^αu_j, which needs 𝔪_0(W̃^αu_j) = 0. After "(both sides
vanish on {v < −1} and have the same v-derivative)" add "and 𝔪_0(W̃^αu_j) = 0, as 𝔪_0((v∂_v + 1)g) = 0 and 𝔪_0
commutes with the ℒ_Ω".

**N4 — l. 451–452.** m_ι of [[prop:iii-g3-2-4]] is defined on {Re < ℓ_I}, and P-U71-close takes ℓ_I < 3.5. "and 0 at
every other point of {Re ϰ ≤ 5}." → "and 0 at every other point of {Re ϰ ≤ 5}, for every ℓ_I > 5 allowed in
[[thm:iii-g1-3-1]] (2) (the principal parts do not depend on ℓ_I)."

**N5 — l. 499–500.** At the computational point ε_+ < δ̄ < 2·10⁻⁸ ([[def:ec-point]], [[eq:iii-i9-1-1]]), while
ι₁ − 2 > δ_C and ι_v(l) ≥ ι_v(2) > 3 + 4·10⁻⁶: "and ι₁ + 1 if ι₁ ≤ 2 + ε_+" and "and the ι_v(l), l ≥ 2, with
ι_v(l) ≤ 3 + ε_+" are empty. Delete both, or say "(none at the point)".

**N6 — symbols inside sec:sp-point.** h = 10⁻⁶ (l. 260) and h := r^(−ι)K, r^(−2)Z (l. 345, 356); x = hκ (l. 260) and
the coordinates x_i (l. 315–343). Rename the tensor in the proof of lem:sp-two-roots ("Let u := r^(−ι)K", "Let
u := r^(−2)Z"), or move lem:sp-two-roots, which holds for all parameters, before the subsection heading. K is used for
K(ϰ_0), for the tensors K_s0, K_v1, for K_1 (l. 204) and for the block count of lem:sp-block; renaming K_1 → F_1 and
the block index range D_0, …, D_K → D_0, …, D_m would remove two of them.

**N7 — l. 176–177.** def:sp-chains is for Banach spaces; 𝔐 acts on 𝒟′(𝕊³; ℂ¹⁵)^(K+1). "onto 𝒦_N(𝔐, ϰ_0) =" → "onto
𝒦_N(𝔐, ϰ_0) := ⊕_π 𝒦_N(𝔐_τ(π) ⊗ Id_π, ϰ_0), the chains of 𝔐 in 𝒟′(𝕊³; ℂ¹⁵)^(K+1),".

**N8 — contract: N.** N is used as an integer (the chain length) at l. 41–71, 115, 120, 176, 203–222 (𝒦_N, T_N, 𝒳^N,
"N ≥ 1"). The contract reserves N. Suggest 𝔫 (or J) throughout def:sp-chains to thm:sp-reduction; N_sf, N_τ, N_L,
N_ι⁺ are the chapters' operators and stay.

**N9 — contract: λ.** λ occurs only in the chapters' notation (λ_♯, λ ∈ Σ, λ₀, K_ι(λ) of ch. 36, 41, 42) at l. 6,
491–496, 501, 504. Where the corollary quantifies on its own (l. 491–496: "For λ ∈ Σ", "K_ι(λ)", "at λ₀"), the
contract asks ϰ: "For ϰ ∈ Σ, K_ι(ϰ) ≤ m_ι(ϰ) + m_♯(ϰ)", "In the step at ϰ₀". λ_♯ is a named constant of ch. 36 and
stays.

**N10 — contract: 𝔪.** The moments are written 𝔪_k, and the contract makes 𝔪 the large weight. The large weight does not
occur in chapter 71, so there is no clash where the block would enter; if a single meaning is wanted, rename the
moments, for instance 𝔮_k(u).

## Consistency with (IS) and the values

- **What l_* ranges over.** def:iii-i10-1-1 (ch. 41 l. 154–156): at real part at most 5, (i) the logarithmic orders of
  ℰ_ind ∪ ℰ^ι_ind ∪ ℰ^C_I, (ii) the orders of the poles of N_ι⁺(L̄, ·)⁻¹, (iii) the multiplicities of the indicial roots
  of L̂_b(0). "At real part at most 5" is the half-plane, as R-P-U71-IS item 3 says; the text's M (l. 488) is read the
  same way, correctly.
- **(i) L.** From P-U71-IS: ℰ_ind ≤ 39 at real part ≤ 5, attained at (5, 39) (prop:is-logs (b), checked by
  R-P-U71-IS); ℰ^ι_ind ≤ 50 (prop:is-logs (c), an upper bound, not shown attained); least ℰ^C_I: order 0
  (prop:is-ci-pp (a)). So **39 ≤ L ≤ 50**.
- **(ii) poles.** All simple at real part ≤ 5 (this text, with F1): contribution **1**.
- **(iii) M.** Every root has multiplicity ≤ 7 at each type (prop:iii-f1-2-3 (b), (C1) holding at the point by
  prop:np-10-54 (i)–(ii)); the roots below −101 enter and are bounded only so. On (1, 4] all simple (this text, with
  F1); on [−101, 5] simple by prop:is-mult as it stands for hκ ≤ 70, with F1 for 134 ≤ l ≤ 172, and by F3's
  conjugation argument for hκ > 70, which is stronger than the "at most 3" of R-P-U71-IS F1. So **1 ≤ M ≤ 7**.
- **l_*.** l_* = max(1, L, M) = L, as L ≥ 39 > 7 ≥ M. **l_* = 50 is admissible; the least admissible l_* lies in
  [39, 50]**, and is 50 unless the bound 50 for ℰ^ι_ind is improved. This is the "(IS) part of l_* = 50" of R-P-U71-IS;
  (SP) does not raise it.
- **K_ι.** For λ ∈ Σ ⊂ {Re < 3 + ε_+}, K_ι(λ) ≤ m_ι(λ) + m_♯(λ) (prop:iii-g3-2-4), m_ι(λ) ∈ {0, 1} (this text),
  m_♯(λ) = k(ℰ^C_(I,♯), λ) + 1 ≤ 1 (ℰ^C_(I,♯) = (λ_♯, 0) ∪ ℰ^C_I, order 0). So **K_ι(λ) ≤ 2**, and K_ι(λ) ≤ 1 unless
  λ ∈ spec_ι⁺(L̄) ∩ π_1ℰ^C_I (3 is such a point: 3 = 1 + 4/2); K_ι(λ_♯) = 1 (ch. 42 l. 628). The text's bound
  K_ι ≤ l_* + 2 gives 52, chapter 42's K_ι ≤ 2l_* + 1 gives 101; both hold, neither is sharp (F6).
- **Raises.** The raise of 𝒮_(λ₀) is at most m_ι(λ₀) ∈ {0, 1} (F4), and each pole raise of lem:iii-i10-1-2 (c) is at most
  1. Chapter 42 l. 781 and lem:iii-j-2-3 allow "at most l_*" = 50, consistent.
- **Chapter 71, P-U71-assembly, P-U71-close.** None assigns a value to l_*, K_ι or a raise: chapter 71 does not mention
  them; the assembly carries l_* as a symbol (l. 632, 636, 648–649); P-U71-close bounds n_ι ≤ N_Λ(k̄_0 + 1) +
  (J_* + 1)(l_* + 1)N_Λ² with l_* symbolic (l. 257–259, 268). So there is **no mismatch of values**. With this text the
  following become false and must change at integration: P-U71-close l. 313–316 (thm:uc-reduction (iii): "of which
  this paper states only that they lie in {Re ≥ 2}"), l. 339–340 and 352 (rem:uc-missing (SP): "(SP) needs an analysis
  that this paper does not contain: of spec_ι⁺(L̄) it states only [[lem:iii-g1-4-2]] (a)"), and P-U71-assembly
  l. 632, 636, 648–649, which defer to (SP). With l_* = 50, P-U71-close's bound reads n_ι ≤ 4N_Λ + 51(J_* + 1)N_Λ²
  (k̄_0 = 3 from prop:is-count). Outside (SP): P-U71-close uses J_* ≤ 34,202,065,807 (η_0 ≥ ε_Υ), P-U71-IS
  J_* = 15,000,015 (η_0 = 𝔡₁); the integration must use one.

## Citations

All 70 distinct cited labels resolve, none missing: 53 in chapters 20, 22, 33, 34, 35, 36, 38, 41, 42, 71 and in
P-A-indicial, P-A3-every-h, and 17 of the section's own 26 labels. Each external one was read and gives what is used,
with one exception in aim: [[cor:iii-g2-4-3]] for the raise of 𝒮_(λ₀) (F4). Noted, not counted:
[[prop:gap-sums]] is defined twice (ch. 71 l. 72 and P-A-indicial l. 421, same statement), as R-P-U71-IS reported; and
the lemma that F1 needs (lem:s14-sextic-large (b)) is cited correctly but does not give distinctness.

## Contract

- Lines: all 518 at most 121 characters (Python len); none longer.
- Wrapped lines beginning with "+ ", "- ", "* ", "> ", "#", "=", "|": none.
- Label keys: 26, all lowercase, prefix sp-.
- No file, program, code or AI words (searched: file, program, code, script, software, computer, computation,
  numerical, algorithm, machine and the like; "computational point" is the paper's term).
- Every proof ends with ∎ (11 proofs).
- Notation: ϰ is the ι⁺ parameter throughout; Θ does not occur; λ only in chapter notation (N9); N used as an integer
  (N8); 𝔪 used for the moments (N10).
