# E2-PILOT -- E2 at one operator: □ on 5D Tangherlini, harmonic by harmonic, with explicit constants

Status: written (D350); section 3b added (D355) and verified (verifier 165, D356); section 3c added (D359), read by
verifier 167 (D362); section 3d (the band, computed) added (D371); section 3e (Lemma E2.8, a Morawetz bound for every
l ≥ 1 and every real σ, D379; read by verifier 175, D382) added; section 3f (Lemma E2.9 and the certificate:
every l ≥ 1, D384; read by verifier 176, D385: decimals rounded outward) added; section 3g (Lemma E2.8′, l = 0
certified, D387) added; sections 1-3, 3d and 3g to be read.
Check scripts: `checks/e2pilot5.py` P1-P4 (computed), all pass, every control fails; the band: `checks/e2band5.py`;
E2.8: `checks/e2morawetz5.py` M1-M3; E2.9 and the certificate: `checks/e2certify5.py` C1-C5; l = 0:
`checks/e2lzero5.py` Z1-Z5.

EFFECTIVE-CONSTANTS.md section 5 (E2) asks, at Tangherlini, for certified lower bounds at each harmonic up to an
explicit cut-off and explicit coercivity beyond it, to replace the N1 constants at b_0; it calls E2 at one operator
"the first real test". The operator taken here is the one of III.D Proposition 6.2 (PART-III-D-GAUGEPOT.md:360), the
scalar wave operator □ on five-dimensional Schwarzschild-Tangherlini, whose proof of injectivity for Im σ ≥ 0, σ ≠ 0
goes harmonic by harmonic through an ODE fact (lines 378-389) and gives no number. This note makes that step
quantitative where it can be done by inequality alone, and says exactly what remains.

## 1. The radial problem

Mass μ, f := 1 − μ/r², r_* with dr_*/dr = 1/f (r_* → −∞ at the horizon r = √μ, r_* ~ r at infinity). For φ =
r^(−3/2) Φ(r_*) Y_l e^(−iσt), Y_l a harmonic of S³ with −ΔY_l = l(l+2) Y_l, □φ = g becomes

    −Φ'' + V_l Φ − σ² Φ = G,     V_l = f ((l(l+2) + 3/4)/r² + 9μ/(4r⁴)),     ' := d/dr_*,                    (1.1)

with G the corresponding component of the source times f r^(3/2) (computed, P1). V_l > 0 on r > √μ, V_l → 0
exponentially at the horizon and like (l(l+2) + 3/4)/r_*² at infinity, and

    I_l := ∫ V_l dr_* = ∫_(√μ)^∞ ((l(l+2) + 3/4)/r² + 9μ/(4r⁴)) dr = (l(l+2) + 3/2)/√μ                          (1.2)

(computed, P1). For each σ the solution space of the homogeneous equation (1.1) is spanned near each end by the
asymptotic solutions e^(±iσ r_*)(1 + o(1)), V_l being integrable in r_* at both ends (Volterra iteration, as in
III.D Proposition 6.2's proof). Let u_h be the solution with u_h = e^(−iσ r_*)(1 + o(1)) as r_* → −∞ (regular across
the future horizon) and u_∞ the one with u_∞ = e^(iσ r_*)(1 + o(1)) as r_* → ∞ (outgoing).

## 2. Off the real axis: uniform in l

**Lemma E2.1.** For Im σ > 0 and every l, the outgoing resolvent R_l(σ) of (1.1) on L²(dr_*) satisfies

    ‖R_l(σ)‖ ≤ 1/dist(σ², [0, ∞)),

that is ≤ 1/(2|Re σ| Im σ) when |Re σ| ≥ Im σ, and ≤ 1/|σ|² when |Re σ| < Im σ.

*Proof.* For Im σ > 0 the solution Φ = R_l(σ)G decays exponentially at both ends with Φ' (it is a multiple of u_h
near the horizon and of u_∞ near infinity, both e^(∓iσ r_*)-decaying), so pairing (1.1) with Φ̄ and integrating has no
boundary terms: ∫(|Φ'|² + V_l|Φ|²) − σ² ∫|Φ|² = ∫ G Φ̄. With V_l ≥ 0 the left side is ⟨(H − σ²)Φ, Φ⟩, H = −∂² + V_l ≥ 0
self-adjoint on L²(dr_*), so ‖Φ‖ ≤ ‖G‖/dist(σ², spec H) ≤ ‖G‖/dist(σ², [0, ∞)). The two cases are the distance of
σ² = (Re σ)² − (Im σ)² + 2i Re σ Im σ from the half-line: |Im σ²| if Re σ² ≥ 0, |σ²| otherwise. ∎

This is the trivial half of E2 and is uniform in l; it degenerates as Im σ → 0, where the content of Proposition 6.2
lies.

## 3. On the real axis: every harmonic, explicitly

**Lemma E2.2 (flux).** For real σ ≠ 0 write u_h = A e^(−iσ r_*) + B e^(iσ r_*) + o(1) as r_* → ∞. Then |A|² = 1 + |B|²,
and the Wronskian W := u_h u_∞' − u_h' u_∞ equals 2iσA. So |W| ≥ 2|σ|.

*Proof.* V_l is real, so Im(ū u') is constant for every solution u. For u_h it is −σ at −∞ and −σ|A|² + σ|B|² at +∞
(the cross terms give a real number, whose imaginary part is 0). W is constant; at +∞, with u_∞ = e^(iσ r_*), W =
(A e^(−iσ r_*) + B e^(iσ r_*)) iσ e^(iσ r_*) − (−iσA e^(−iσ r_*) + iσB e^(iσ r_*)) e^(iσ r_*) = 2iσA. ∎

**Lemma E2.3 (growth through the barrier).** For a solution u of the homogeneous equation and real σ ≠ 0 put E :=
|u'|² + σ²|u|². Then |E'| ≤ (V_l/|σ|) E. Hence

    |u_∞(r_*)|² ≤ 2 exp(|σ|⁻¹ ∫_(r_*)^∞ V_l),     |u_h(r_*)|² ≤ 2 exp(|σ|⁻¹ ∫_(−∞)^(r_*) V_l).

*Proof.* E' = 2Re(ū' u'') + 2σ² Re(ū u') = 2(V_l − σ²) Re(ū' u) + 2σ² Re(ū u') = 2V_l Re(ū' u), and 2|ū' u| ≤
|u'|²/|σ| + |σ||u|² = E/|σ|. Gronwall from the end where E → 2σ² (u_∞ at +∞, u_h at −∞), and σ²|u|² ≤ E. ∎

**Proposition E2.4 (the outgoing resolvent at harmonic l, real σ).** For real σ ≠ 0, every l and G ∈ L² with
compact support, the solution of (1.1) that is u_h-like at the horizon and outgoing at infinity is Φ(x) = ∫ K_l(x, y)
G(y) dy with K_l(x, y) = −u_h(min(x, y)) u_∞(max(x, y))/W (the minus sign because (1.1) is −Φ'' + (V_l − σ²)Φ = G;
corrected D352, a review finding; only |K_l| enters below) and

    |K_l(x, y)| ≤ |σ|⁻¹ exp(I_l/(2|σ|)),     I_l = (l(l+2) + 3/2)/√μ.

So for χ the indicator of an r_*-interval of length Λ, ‖χ R_l(σ) χ‖_(L²(dr_*) → L²(dr_*)) ≤ (Λ/|σ|) exp(I_l/(2|σ|)).

*Proof.* Variation of constants: with Φ := −W⁻¹(u_∞(x) ∫_(−∞)^x u_h G + u_h(x) ∫_x^∞ u_∞ G), Φ'' = (V_l − σ²)Φ − G,
and Φ has the two end behaviours; W ≠ 0 by Lemma E2.2. Lemma E2.3 at min(x, y) ≤ max(x, y): |u_h(min)|
|u_∞(max)| ≤ 2 exp((2|σ|)⁻¹(∫_(−∞)^(min) V_l + ∫_(max)^∞ V_l)) ≤ 2 exp(I_l/(2|σ|)), and |W| ≥ 2|σ|. The operator bound is
the Hilbert-Schmidt bound of a kernel bounded by that constant on a square of side Λ. ∎

This is III.D Proposition 6.2's injectivity at real σ, harmonic by harmonic, with a constant: the first N1 step of the
record turned into a number, by inequality alone. P2 checks the lemma's three ingredients against numerical solutions
for l ≤ 6 at four values of σ (it does not prove them).

## 3b. Uniformly in l (E2.5, D355)

Take σ > 0 (σ < 0 is the complex conjugate), an r_*-interval I = [α, β], and write q := V_l − σ², N := |u|² and
Q := Re(ū u') = N'/2 for a solution u of the homogeneous equation, so that Q' = |u'|² + qN.

**Lemma E2.5a (an energy monotone on each side of the barrier).** Put H := |u'|² + (σ² − V_l)|u|². Then H' = −V_l' N.
So H(u_h) ≤ 2σ² on every interval (−∞, t] on which V_l is non-decreasing, and H(u_∞) ≤ 2σ² on every [t, ∞) on which
V_l is non-increasing.

*Proof.* H' = 2Re(ū' u'') − 2qQ − V_l'N, and 2Re(ū' u'') = 2qQ. At the end where each is normalised, u_h ~ e^(−iσ r_*)
and u_∞ ~ e^(iσ r_*) together with their derivatives (the Volterra equation of section 1 and its derivative, whose
remainders are bounded by the tails of ∫V_l), and V_l → 0, so H → 2σ². ∎

For μ = 1, with L := l(l + 2) and g := (L + 3/4)/r² + 9/(4r⁴), one has −4g/r ≤ g' ≤ −2g/r, so V_l' = f'g + fg' (in r)
lies between (g/r³)(6 − 4r²) and (g/r³)(4 − 2r²): V_l increases in r for r² < 3/2 and decreases for r² > 2, for every l.

**Lemma E2.5b (the signs at the ends of I).** Let t_1 < α and t_2 > β be points with q(t_1) = q(t_2) = 0 and q ≥ 0 on
[t_1, t_2], with V_l non-decreasing on (−∞, t_1] and non-increasing on [t_2, ∞). Put A_− := ∫_(t_1)^α q^(1/2) dr_*,
A_+ := ∫_β^(t_2) q^(1/2) dr_*, and for t < t_1 < t_2 < t' with V_l(t) < σ² and V_l(t') < σ²

    B_−(t) := (2σ²/(σ² − V_l(t)))^(1/2) + √2 σ (t_1 − t),     B_+(t') := (2σ²/(σ² − V_l(t')))^(1/2) + √2 σ (t' − t_2).

Then Q(u_h)(α) ≥ 2σA_− − √2 σ B_−(t) and Q(u_∞)(β) ≤ √2 σ B_+(t') − 2σA_+.

*Proof* (u_h; u_∞ is the mirror image, with flux Im(ū_∞ u_∞') = +σ). On (−∞, t_1], σ² − V_l ≥ 0 and H ≤ 2σ² give
|u'|² ≤ 2σ² and (σ² − V_l)N ≤ 2σ²; and, N being positive because the flux is not zero, |(N^(1/2))'| = |Q|/N^(1/2) ≤
|u'| ≤ √2 σ. So N(t_1)^(1/2) ≤ B_−(t), while
|u'(t_1)|² = H(t_1) ≤ 2σ², and |Q(t_1)| ≤ N^(1/2)|u'| ≤ √2 σ B_−(t). On [t_1, α], |u'| ≥ |Im(ū u')|/|u| = σ N^(−1/2)
(Lemma E2.2's flux), so Q' ≥ σ²/N + qN ≥ 2σ q^(1/2). Integrate from t_1 to α. ∎

**Proposition E2.5.** If κ_I² := min_I q > 0, Q(u_h)(α) ≥ 0 and Q(u_∞)(β) ≤ 0 (by Lemma E2.5b it suffices that
A_− ≥ B_−(t)/√2 and A_+ ≥ B_+(t')/√2 for some t, t'), then ‖χ_I R_l(σ) χ_I‖_(L²(dr_*) → L²(dr_*)) ≤ 1/κ_I².

*Proof.* For G supported in I, Φ = R_l(σ)G is c_h u_h on (−∞, α] and c_∞ u_∞ on [β, ∞) (Proposition E2.4's formula).
Pairing −Φ'' + qΦ = G with Φ̄ over I: ∫_I (|Φ'|² + q|Φ|²) = Re ∫_I GΦ̄ + |c_∞|² Q(u_∞)(β) − |c_h|² Q(u_h)(α) ≤ ‖G‖ ‖Φ‖_I,
and the left side is at least κ_I² ‖Φ‖_I². ∎

**Corollary E2.6 (closed form; μ = 1, I the r_*-interval of r ∈ [1.2, 4]).** Let c := (15/16)(L + 3/4). The hypotheses
of Proposition E2.5 hold, and so ‖χ_I R_l(σ) χ_I‖ ≤ 1/((15/256)(L + 3/4) − σ²), whenever

- (i) (15/256)(L + 3/4) > σ² and (0.21/1.4641)(L + 3/4) > σ²;
- (ii) 0.32727 (0.120523 (L + 3/4) − σ²)^(1/2) > (2 + 1.1248 σ)/√2;
- (iii) c^(1/2) > 8σ and (√3/2) c^(1/2) ln(c^(1/2)/(8σ)) > (2 + 0.79217 (L + 1)^(1/2))/√2.

Each of (i)-(iii), once true, stays true as l grows. So with l_0(σ) the least l at which they hold, the bound holds
for every l ≥ l_0(σ). It equals (256/15)/(L + 3/4 − (256/15)σ²), asymptotically 17.07/L.

*Proof.* (i): min over [1.2, 4] of f/r² is f(4)/16 = 15/256 (f/r² rises to r = √2 and falls after), and V_l(1.1) ≥
(L + 3/4)f(1.1)/1.21 > σ², so t_1 lies at r < 1.1; t_2 lies at r > 4. (ii): on [1.1, 1.2], 1/f ≥ 1/f(1.2) = 3.2727 and
V_l ≥ (L + 3/4)f(1.1)/1.44, so A_− ≥ 0.32727(0.120523(L + 3/4) − σ²)^(1/2). Take t where V_l = σ²/2: on (1, 1.1],
d ln V_l/dr_* ≥ (6 − 4r²)/r³ ≥ 0.87152, so t_1 − t ≤ ln 2/0.87152 and B_−(t) ≤ 2 + 1.1248σ. (iii): for r ≥ 4, 1/f ≥ 1
and V_l ≥ c/r²; on [4, ρ], ρ := c^(1/2)/(2σ), q ≥ (3/4)c/r², so A_+ ≥ (√3/2)c^(1/2) ln(ρ/4). Take t' where V_l = σ²/2:
for r ≥ 4, |d ln V_l/dr_*| ≥ (2/r)(1 − 2/r²) ≥ 1.75/r and V_l ≤ (L + 1)/r², so r(t') ≤ (2(L + 1))^(1/2)/σ, t' − t_2 ≤
(ln 2/1.75) r(t') and B_+(t') ≤ 2 + 0.79217(L + 1)^(1/2). Monotonicity: the left sides of (i)-(ii) increase with L and
their right sides do not. Divide (iii) by (L + 3/4)^(1/2): the left side becomes (√3/2)(15/16)^(1/2) ln(c^(1/2)/(8σ)),
which increases, and the right side becomes (2(L + 3/4)^(−1/2) + 0.79217((L + 1)/(L + 3/4))^(1/2))/√2, which
decreases. ∎

**Computed (P3).** The closed form gives l_0 = 14, 19, 50 at σ = 0.3, 1, 3. Evaluating Proposition E2.5's conditions
by quadrature (A_±, and B_± minimised over sample points) gives them from l = 3, 7, 18 up to the closed-form l_0, and
the closed form gives them beyond. Against the numerical kernels of section 4 the end signs hold. The bound is within a
factor 2 of the measured norm (ratios 1.3 to 1.9). The rows (0.3, 8), (1, 8) and (1, 16) lie below the proved l_0;
there the bound rests on the hypotheses as computed by quadrature:

| σ | l | ‖χ_I R_l χ_I‖ (computed) | 1/κ_I² |
|---|---|---|---|
| 0.3 | 8, 16, 32 | 0.121, 0.0399, 0.0120 | 0.215, 0.0594, 0.0157 |
| 1.0 | 8, 16, 32 | 0.139, 0.0415, 0.0122 | 0.267, 0.0628, 0.0159 |
| 3.0 | 32 | 0.0135 | 0.0182 |

Control: 1/(4κ_I²) falls below the measured norm somewhere.

## 3c. Above the barrier (E2.7, D359)

**Lemma E2.7.** For every l, V_l has one maximum and no other critical point. If σ is real and σ² > V_max := max V_l,
then |u_h|² ≤ 2σ²/(σ² − V_max) and |u_∞|² ≤ 2σ²/(σ² − V_max) everywhere. Hence, for an r_*-interval I of length Λ,

    ‖χ_I R_l(σ) χ_I‖ ≤ Λ |σ|/(σ² − V_max).

*Proof.* With a := L + 3/4, b := 9/4 (μ = 1) and y := 1/r², r³V_l' (in r) is −2a + 4(a − b)y + 6by². That is a convex
quadratic with a negative value at y = 0, so it changes sign once on (0, 1): V_l rises, then falls.
- *Where V_l rises,* H = |u'|² + (σ² − V_l)|u|² is non-increasing (Lemma E2.5a), so H(u_h) ≤ 2σ² up to the peak.
- *Where V_l falls,* G := H/(σ² − V_l) satisfies G' = V_l'|u'|²/(σ² − V_l)² ≤ 0, because H' = −V_l'N and
  H − (σ² − V_l)N = |u'|².
- *So* on both sides N ≤ G ≤ 2σ²/(σ² − V_max) for u_h, and the mirror argument gives the same for u_∞.
- *The kernel* is then |K_l| ≤ |u_h||u_∞|/|W| ≤ σ/(σ² − V_max), since |W| ≥ 2σ, and the Hilbert–Schmidt bound on a
  square of side Λ follows. ∎

**Computed (P4).** One sign change of V_l' for l ≤ 40. On I (Λ = 3.74), against the numerical kernels: σ = 1, l = 0:
1.89 ≤ 7.57; σ = 3, l = 0, …, 4: 0.41, 0.42, 0.45, 0.51, 0.67 ≤ 1.32, 1.45, 1.72, 2.35, 4.44. Control: a tenth of the
bound fails. So above the barrier the constant is polynomial: Proposition E2.4's exp(I_l/(2σ)) is needed only for the
l with V_max ≥ σ² below l_0(σ): 5 ≤ l < 50 at σ = 3, by the proved thresholds. Of these, 12 ≤ l < 50 have κ_I² > 0 and
lack only the end signs; 5 ≤ l < 12 are those whose barrier top lies above σ² without covering I.

## 3d. The band between the two bounds, computed (D371)

At σ = 3, E2.7 covers l ≤ 4 (σ² > max V_l) and E2.5 covers l ≥ 50 (closed form), or l ≥ 18 by quadrature (computed).
For 5 ≤ l ≤ 17 only Proposition E2.4's constant holds, up to e^54. `checks/e2band5.py` computes the band with P2's
solver (r ∈ [1.2, 4], 161-point kernel; output `checks/e2band5_s3.out`, l = 0-25). Labels: computed, not certified.

| l | max V_l | κ_I² | ‖χ_I R χ_I‖ | 1/κ_I² | \|W\|/(2σ) | max \|u_h\|² on I |
|---|---|---|---|---|---|---|
| 4 | 6.47 | −7.54 | 0.672 | - | 1.01 | 2.22 |
| 5 | 9.22 | −6.90 | 1.132 | - | 1.46 | 11.6 |
| 6 | 12.47 | −6.14 | 0.983 | - | 10.4 | 737 |
| 8 | 20.47 | −4.26 | 0.725 | - | 1.42 × 10³ | 1.39 × 10⁷ |
| 11 | 36.22 | −0.57 | 0.287 | - | 4.72 × 10⁶ | 9.18 × 10¹³ |
| 12 | 42.47 | 0.90 | 0.193 | 1.116 | 8.29 × 10⁷ | 1.15 × 10¹⁶ |
| 17 | 81.22 | 9.98 | 0.0551 | 0.1002 | 3.74 × 10¹⁴ | 7.17 × 10²⁵ |
| 25 | 169.22 | 30.60 | 0.0225 | 0.0327 | 2.39 × 10²⁶ | 5.29 × 10⁴⁰ |

What it shows (computed):

- The norm peaks at l = 5, at 1.132: the harmonic whose barrier top, 9.22, is nearest σ² = 9, the trapping energy of
  this harmonic. It is at most 1.132 for every l ≤ 25, and falls like about 1/(l(l + 2)) beyond the band.
- Where E2.5's quantity applies (κ_I² > 0, l ≥ 12), the computed norm is below 1/κ_I² at every l, including
  12 ≤ l ≤ 17, where the proof's end-sign conditions fail. So a sharper Lemma E2.5b is consistent with the numbers.
- For 5 ≤ l ≤ 11 the barrier does not cover I (κ_I² ≤ 0). There max |u_h|² grows to 10¹⁴, but |W|/(2σ) grows in step,
  and the kernel u_h(x_<) u_∞(x_>)/W stays O(1).

**What a bound for the band must use (proposed, not proved).** Proposition E2.4 used only |W| ≥ 2|σ|. That is the only
place the e^54 enters. W = 2iσA, with |A|² = 1 + |B|² the transmission factor, and A carries the whole tunnelling
growth through the forbidden region F = {V_l > σ²}.

- A bound O(1) would bound |u_h(x)| above by |A| times the decay e^(−∫_x^(x_2) κ), with κ := (V_l − σ²)^(1/2), on F and
  to its right, and |u_∞(y)| by its mirror.
- Then for x ≤ y the kernel is at most e^(−∫_x^y κ) up to constants.
- On F, N = |u|² is convex (N″ = 2|u′|² + 2(V − σ²)N ≥ 0). With the energy H′ = −V′N and the flux this should give
  the two bounds without WKB asymptotics, as Lemma E2.5a does at the ends of I.
- Writing it, as Lemma E2.8, is the next step for the band.

## 3e. A Morawetz bound for every harmonic l ≥ 1 and every real σ (E2.8, D379)

**Lemma E2.8.** Let φ be smooth and increasing, with φ(±∞) = ±1 and φ′, φ″ → 0 at ±∞, and put w := −φV_l′ − ½φ‴
(derivatives in r_*). Suppose w ≥ 0 on ℝ, and let m′ := min_I φ′, M′ := max_I φ′ and w_I := min_I w > 0. For real
σ ≠ 0 and f ∈ L²(I), let u := R_l(σ)f be the outgoing solution, u ~ c_± e^(±iσr_*) at ±∞. Then

    2 ∫ φ′|u′|² + ∫ w|u|² = Re ∫ f (2φū′ + φ′ū) + 2σ²(|c_+|² + |c_−|²),                                   (3.4)

    ‖χ_I R_l(σ) χ_I‖ ≤ B_l(σ) := ((2/m′ + (M′ + 2|σ|)²/w_I)/w_I)^(1/2).

*Proof.*

- Multiply −u″ + (V_l − σ²)u = f by 2φū′ + φ′ū, take real parts and integrate. The integrand on the right of (3.4)
  minus the one on the left is an exact derivative (M1, exact). Its limits at ±∞ give −2σ²(φ(∞)|c_+|² −
  φ(−∞)|c_−|²) = −2σ²(|c_+|² + |c_−|²), since V_l → 0 and u′ ∓ iσu → 0 there. That is (3.4).
- The flux identity σ(|c_+|² + |c_−|²) = −Im ∫ f ū bounds the last term by 2|σ| ‖f‖ ‖u‖_I.
- Both integrands on the left are ≥ 0, so drop them off I. With X := ‖u′‖_I, Y := ‖u‖_I and |φ| ≤ 1,
  2m′X² + w_I Y² ≤ ‖f‖ (2X + (M′ + 2|σ|) Y).
- By Cauchy-Schwarz, (2m′X² + w_I Y²)^(1/2) ≤ ‖f‖ (2/m′ + (M′ + 2|σ|)²/w_I)^(1/2), and Y ≤ B_l(σ) ‖f‖. ∎

**Instantiated (`checks/e2morawetz5.py` M1-M3; M1 exact, M2-M3 computed in floating point, not certified).**

- Take φ := tanh((r_* − x_p)/s), x_p the peak of V_l. Then −φV_l′ ≥ 0, since V_l rises and then falls (E2.7), and
  −½φ‴ = s^(−3) > 0 at the peak.
- Near the horizon V_l′ decays like e^(2r_*) and φ‴ like e^(2r_*/s), so w ≥ 0 needs s ≤ 1; at s = 1 it is a
  comparison of constants, which s = 1 passes at l = 1 (verifier 175). The control s = 1.5 fails.
- Beyond the grid (r_* < −59 or r_* > 120) the tails are asymptotic. On the left, the ratio of ½|φ‴| to −φV_l′ is
  K e^(2r_*(1/s − 1))(1 + O(e^(2r_*))), which decreases to 0 for s < 1; the instrument checks it is at most 1 and
  decreasing on [−59, −20]. On the right, −φV_l′ ~ 2a/r_*³ against |φ‴| ~ e^(−2r_*/s).
- At l = 0, no s in [0.2, 0.98] gives w ≥ 0. For 1 ≤ l ≤ 30, s = 0.98 does; for l ≥ 6 the minimum of w on I is at the
  peak, w_I = s^(−3) = 1.0625.

| l | 1 | 2 | 3 | 4 | 5 | 6 | 10 | 17 | 25 |
|---|---|---|---|---|---|---|---|---|---|
| B_l(3) | 253 | 53.3 | 35.5 | 26.6 | 21.3 | 19.5 | 19.3 | 19.2 | 19.2 |
| computed norm (`checks/e2band5_s3.out`) | 0.423 | 0.451 | 0.508 | 0.672 | 1.132 | 0.983 | 0.421 | 0.0551 | 0.0225 |

At the other frequencies of section 4's table (B_l(σ) against the computed norm):

| l | 1 | 2 | 4 | 8 | 16 |
|---|---|---|---|---|---|
| σ = 0.3 | 132 / 1.66 | 43.4 / 0.79 | 24.3 / 0.33 | 18.3 / 0.12 | 18.1 / 0.040 |
| σ = 1 | 155 / 3.00 | 44.9 / 1.96 | 24.6 / 0.55 | 18.4 / 0.14 | 18.3 / 0.042 |

For l ≥ 6, B_l(1) ≈ 18.3 and B_l(10) ≈ 26.8 (`--table 30`). A hundredth of B_5(3) is below the computed norm, so the
comparison is not vacuous. The selftest checks l ≤ 25 at σ = 3; `--table` extends the constants to l = 30.

What it gives:

- *The band.* For 5 ≤ l ≤ 17 at σ = 3, where only Proposition E2.4's e^54 held, B ≤ 21.3. That is within a factor of
  about 19 of the computed norm at the barrier-top harmonic l = 5. At large l the bound is loose by up to about 10³.
  There E2.5's 1/κ_I² is the better one where it is a bound: proved from l_0(σ) (50 at σ = 3), and by quadrature from
  18 (computed); at 12 ≤ l ≤ 17 it is not a bound (section 3d).
- *In σ.* B_l is uniform on compact sets of real σ ≠ 0, and grows linearly in |σ|. As σ → 0 it stays bounded,
  B_l(0+) = ((2/m′ + M′²/w_I)/w_I)^(1/2): 126 at l = 1, about 18.1 for l ≥ 6. It does not degenerate at the
  barrier-top energy σ² = max V_l of a single harmonic.
- *In l.* For 6 ≤ l ≤ 30 the constants are nearly constant: they depend on l only through x_p, which tends to the
  photon sphere. Beyond l = 30 this is expected, as −φV_l′ grows like l², but the instrument does not compute it;
  verifier 175's scans at l = 60, 100 and 200 also give w ≥ 0.
- *With E2.5 and E2.7,* every harmonic 1 ≤ l ≤ 30 now has an explicit bound at every real σ ≠ 0 (computed
  constants), and every l ≥ l_0(σ) one by E2.5 (proved). At σ = 3 that leaves 31 ≤ l ≤ 49 with Proposition E2.4's
  constant, or E2.5 by quadrature from l = 18 (computed). A proof of w ≥ 0 for large l, with a finite check below
  it, would close that gap (verifier 175's A1); Lemma E2.9 closes it (section 3f, D384). For l = 0, E2.7 holds for
  σ² > max V_0 and Proposition E2.4 otherwise.

What it does not give:

- a certificate: w ≥ 0 and the constants are checked on a grid, and an interval-arithmetic check per l is a finite
  step (answered in section 3f, D384);
- l = 0, and l > 30 in the instrument (l > 30 answered in section 3f, l = 0 in section 3g);
- a good constant: B is dominated by the cut-off term 2/m′, where m′ = φ′ at the end r = 4 of I is about 0.0058. As
  σ → 0 that term is almost all of B_l² w_I, and m′ decays like e^(−2Λ/s) as I lengthens, so the bound is
  exponentially poor in the length of I;
- uniformity in σ: B_l grows linearly in |σ|, the price of bounding the flux term 2σ²(|c_+|² + |c_−|²) by
  2|σ|‖f‖‖u‖_I, not a trapping effect; the constants are nearly uniform in l;
- the record's norms (section 4), or Im σ > 0.

## 3f. Every harmonic l ≥ 1, certified (E2.9, D384)

E2.8 needs only w ≥ 0 on ℝ for some multiplier; its centre need not be the peak of V_l. Fix it at the photon sphere.

**Lemma E2.9.** Let φ_* := tanh((r_* − x_*)/s), x_* := r_*(√2), and write V_l = aU + bQ with U := f/r², Q := f/r⁴,
a = l(l + 2) + 3/4, b = 9/4. Then, with y = 1/r² and derivatives in r_*,

    U′ = (2f/r³)(2y − 1),    Q′ = (2f/r³) y(3y − 2),    w_l := −φ_*V_l′ − ½φ_*‴ = w_1 + (a − a_1)(−φ_*U′),

and −φ_*U′ ≥ 0 on ℝ. So w_l ≥ w_1 for every l ≥ 1, and min_I w_l ≥ min_I w_(l_0) for every l ≥ l_0. As m′ and M′ do
not depend on l, B_l(σ) ≤ B_(l_0)(σ) for every l ≥ l_0.

*Proof.* U = (1 − y)y and Q = (1 − y)y², with dy/dr = −2/r³ and d/dr_* = f d/dr, give U′ and Q′. U′ changes sign
exactly at y = ½, that is r = √2, where φ_* does, and the two have opposite signs on each side. w_l is affine in a with
slope −φ_*U′. ∎

**Certified (`checks/e2certify5.py` C1-C5; interval arithmetic, mpmath.iv at 30 digits, with outward rounding).** s =
49/50.

- *C1.* w_1 ≥ 0 on r_* ∈ [x(t = −120), x(r = 120)], t := ln(r − 1), by adaptive bisection in t (445 enclosures
  evaluated, 223 pieces accepted): every accepted piece's enclosure of w_1 has a non-negative lower end, and the
  pieces cover the range exactly, their endpoints carried at the intervals' own 103 bits. Away from the centre, sech²
  is computed from e^(−2|z|), as 1 − tanh² cancels below 30 digits there.
- *C2, the tails.* Below that range, ½|φ_*‴| ≤ (8/s³)e^(2z) and −φ_*V_1′ ≥ tanh|z_L| C e^(2r_*), with
  C = 8(a + b)(1 − 6e_L)e^(−2r_L)/r_L⁵ (using a ≥ b, true at l = 1). So the ratio is at most K e^(2r_*(1/s − 1)),
  which decreases toward the horizon as s < 1; at the left end it is ≤ 0.03913. Above the range, the ratio is at most
  (8/s³)e^(−2z)(r_* + d_R)³/(2a c_R tanh z_R), decreasing once r_* + d_R > 3s/2; at the right end it is
  ≤ 2.61 × 10⁻¹⁰⁰. With E2.9, w_l ≥ 0 on ℝ for every l ≥ 1.
- *C3, C5, the constants.* m′ ≥ 0.005793 (an end of I) and M′ ≤ 1/s = 1.02041. Certified lower bounds for min_I w_l,
  with φ_* (C3) or with φ centred at a float near V_l's own peak (C5, certified the same way, w_l ≥ 0 on ℝ included),
  give the upper bounds below, every decimal rounded outward from the enclosure (upper bounds up, lower bounds down,
  D385). For l ≥ 6 the row is E2.9's bound with l_0 = 6, min_I w_6 ≥ 1.0610. At l = 1 the photon-sphere centre gives
  only min_I w_1 ≥ 2.645 × 10⁻⁵ from C3's 2000 fixed pieces, coarse where w_1 is small (point values put the minimum
  near 1.5 × 10⁻³ at r ≈ 2.19), so B_1(3) ≤ 2.66 × 10⁵ there; the peak centre (C5) gives the row below. At l = 2-5
  C3 is the better of the two.

| l | multiplier | B_l(0+) | B_l(1) | B_l(3) | B_l(10) |
|---|---|---|---|---|---|
| 1 | peak (C5) | 129.7 | 160.4 | 264.5 | 708.9 |
| 2 | φ_* (C3) | 40.03 | 42.09 | 51.12 | 104.2 |
| 3 | φ_* (C3) | 29.61 | 30.46 | 34.39 | 60.62 |
| 4 | φ_* (C3) | 23.54 | 23.97 | 26.02 | 40.96 |
| 5 | φ_* (C3) | 19.55 | 19.80 | 20.99 | 30.30 |
| every l ≥ 6 | φ_* (C3, E2.9) | 18.07 | 18.27 | 19.22 | 26.80 |

D384 printed this table, m′ and the left ratio rounded to nearest, which put some printed bounds below the certified
ones (m′ ≥ 0.005794 against 0.0057939…, B_6(3) ≤ 19.21 against 19.2122…); verifier 176 found it (D385).

At every real σ ≠ 0, B_l(σ) ≤ ((2/m′ + (M′ + 2|σ|)²/w_l)/w_l)^(1/2) with these certified m′, M′ and w_l.

- *C4, controls.* With the centre moved to r = 1.6, −φU′ < 0 at r = 1.5, so the monotonicity fails. With s = 3/2 the
  left tail's exponent 2(1/s − 1) is negative, so the bound grows toward the horizon. And C1's bisection itself fails
  where it must: at l = 0 with φ_* (w_0 ≤ −0.01125 at t = 0.8, certified) and at l = 1 with s = 3/2 (w_1 ≤ −0.004912
  at t = −8).

What this gives: for every harmonic l ≥ 1 and every real σ ≠ 0, an explicit bound for ‖χ_I R_l(σ) χ_I‖, certified,
and uniform in l ≥ 6. In particular E2.8's "1 ≤ l ≤ 30, computed" (section 3e) becomes "every l ≥ 1, certified", and
the band at σ = 3 has the certified bound 20.99 for 5 ≤ l ≤ 17.

What it does not give:

- l = 0: with the photon-sphere centre w_0 < 0 near r ≈ 3.2 (w_0 ≤ −0.01125 at t = 0.8, certified), where −½φ_*‴ < 0
  and a = 3/4 makes −φ_*V_0′ too small to absorb it; the left tail's proof also needs a ≥ b, false there; and every
  peak-centred s failed too (section 3e); answered in section 3g, which adds a Lagrangian term to the multiplier;
- constants away from I = {r ∈ [1.2, 4]} and s = 49/50: both are fixed here;
- a sharp constant: the cut-off term 2/m′ still dominates, and the growth in |σ| is the flux step's (section 3e);
- the correctness of mpmath.iv itself, which the certificate assumes;
- the record's norms (section 4), or Im σ > 0.

## 3g. The harmonic l = 0, certified (E2.8′, D387)

No tanh multiplier tried gives w_0 ≥ 0 (sections 3e-3f), so the multiplier takes one more term.

**Lemma E2.8′.** Let φ be as in Lemma E2.8, and let q ∈ C² with q ≥ 0 and q, q′ → 0 at ±∞. For u the outgoing solution
of −u″ + (V − σ²)u = f, f ∈ L²(I), σ real and nonzero,

    2 ∫ (φ′ − q)|u′|² + ∫ W_q |u|² + 2σ² ∫ q|u|² = Re ∫ f (2φū′ + (φ′ − 2q)ū) + 2σ²(|c_+|² + |c_−|²),
    W_q := −φV′ − ½φ‴ + q″ − 2qV.

If φ′ − q ≥ 0 and W_q ≥ 0 on ℝ, and m′ := min_I (φ′ − q) > 0 and w_I := min_I W_q > 0, then
‖χ_I R(σ) χ_I‖ ≤ ((2/m′ + (M′ + 2|σ|)²/w_I)/w_I)^(1/2), with M′ := max_I |φ′ − 2q|.

*Proof.* The identity is E2.8's with −2qū added to the multiplier. The added term contributes
Re ∫ f(−2qū) = −2∫ q|u′|² + ∫ q″|u|² − 2∫ q(V − σ²)|u|², by two integrations by parts. Its boundary terms
q(|u|²)′ − q′|u|² vanish at ±∞ because q, q′ → 0 and u and u′ are bounded. The flux identity
σ(|c_+|² + |c_−|²) = −Im ∫ f ū is unchanged. On the left, the σ²q term is nonnegative and is dropped, and the integrands outside I are nonnegative. The
pairing on the right is at most ‖f‖(2‖u′‖_I + M′‖u‖_I). So E2.8's algebra applies with m′, M′ and w_I as defined. ∎

**Certified (`checks/e2lzero5.py` Z1-Z5; interval arithmetic as in section 3f).**

- *The multiplier.* φ = tanh((r_* − x_c)/s), s = 49/50, x_c = r_*(√2) − 3/10. q = Σ_k c_k sech²((r_* − x_k)/κ_k) is a
  sum of 43 bumps. The x_k lie on a lattice of 1/4 about the photon sphere, κ_k ∈ {3/10, 1/2, 9/10}·s, and the
  c_k ≥ 0 are rounded to four digits.
  - The c_k came from a linear program over that dictionary: maximise min_I W_q subject to W_q ≥ φ′/30 and q ≤ φ′/2 on
    a grid.
  - The certificate checks this q, not the program.
  - Each κ_k < s, so q decays faster than φ′ at both ends.
- *Z1.* The identity, as an exact derivative (sympy). With q″ entering at −1 it fails.
- *Z2.* W_q ≥ 0 (4669 enclosures) and φ′ − q ≥ 0 (155 enclosures) on t ∈ [−120, ln 119], by adaptive bisection.
- *Z3, the tails.*
  - *Below the range.* Every bump is past its inflection, so q″ ≥ 0, and W_q ≥ −φV′(1 − ρ_3 − ρ_q).
    - ρ_3 ≤ K e^(2r_*(1/s − 1)) as in section 3f. Its V′ bound now uses a(2y − 1) + by(3y − 2) ≥ (a + b) − e(4a + 8b),
      which holds for every a, b > 0; section 3f's a ≥ b fails at l = 0.
    - ρ_q := 2qV/(−φV′) is at most a sum of exponentials, each increasing in r_*.
    - Certified: ρ_3 + ρ_q ≤ 0.145 at the end of the range, and q/φ′ ≤ 2.32 × 10⁻⁶ (increasing in r_*).
  - *Above it.* ρ_3 + ρ_q ≤ 7.03 × 10⁻¹⁰⁰ and q/φ′ ≤ 1.32 × 10⁻¹⁷, both decreasing in r_*.
- *Z4, the constants.* Over 2000 pieces of I: min_I W_q ≥ 0.02886, m′ ≥ 0.002580, M′ ≤ 0.3809. So
  B_0(0+) ≤ 164.5, B_0(1) ≤ 183.5, B_0(3) ≤ 275.2 and B_0(10) ≤ 725.0. B is computed from the enclosures, not from
  the four-digit constants, which give the slightly larger 275.218 at σ = 3 (verifier 177, D391).
- *Z5, controls.* Without q, w_0 ≤ −0.1775 at t = −0.04 (certified). With q″ entering at −1, the bisection fails and
  W ≤ −0.490 at t = −0.12.

What this gives: with section 3f, every harmonic l ≥ 0 has a certified bound for ‖χ_I R_l(σ) χ_I‖ at every real σ ≠ 0.
B_0(3) ≤ 275.2, and the l ≥ 1 bounds are section 3f's. The same Lagrangian term with an asymmetric φ (width s_L < 1
toward the horizon, wider outside) gives B_1(3) ≈ 86 against 264.5 (computed, not certified, D387).

What it does not give: a sharp constant (m′ is small, so the cut-off term dominates as before); constants away from
I and s = 49/50; and the record's norms (section 4) or Im σ > 0.

## 4. What remains for E2 at this operator

- **Uniformity in l (E2.5): done for real σ on a fixed interval (section 3b, D355).** exp(I_l/(2|σ|)) grows like
  exp(l²/(2|σ|√μ)). The reason is that Proposition E2.4 uses only |W| ≥ 2|σ|. W = 2iσA grows by the same tunnelling
  factor as the solutions, so E2.4 throws away the kernel's decay off the diagonal. Proposition E2.5 and Corollary E2.6
  replace it, for l ≥ l_0(σ), by 1/((15/256)(L + 3/4) − σ²), asymptotically 17.07/L. They rest on Lemma E2.5a's
  monotone energy and the flux.
  - *Above the barrier* (σ² > max V_l) Lemma E2.7 gives the polynomial Λσ/(σ² − max V_l) (section 3c, D359).
  - *The other harmonics, l < l_0(σ) with max V_l ≥ σ²,* kept Proposition E2.4's constant, which is finite but
    astronomically large, until Lemma E2.8 (section 3e, D379) gave 1 ≤ l ≤ 30 an explicit one (about 19-21 at σ = 3;
    constants computed), and Lemma E2.9 with its certificate (section 3f, D384) every l ≥ 1 (certified: 20.99 for 5 ≤ l ≤
    17 at σ = 3, 19.22 for every l ≥ 6), and Lemma E2.8′ (section 3g, D387) l = 0 (certified: 275.2 at σ = 3).
    Section 3d computes their actual norms at σ = 3, at most 1.132 (D371). Below the proved l_0 = 50 at σ = 3 it
    reaches e^417 at l = 49 (e^54 at l = 17, just below the threshold 18 that quadrature gives, which is computed, not
    proved).
  - *Two kinds of l below l_0.*
    - Where κ_I² > 0 (from l = 12 at σ = 3, by (i)), only the end signs are missing; a sharper Lemma E2.5b would cover
      them.
    - Where κ_I² ≤ 0, the barrier does not cover I. Proposition E2.5 cannot apply there, and those l need another
      argument.
  - *On a compact band of σ* every closed-form threshold is monotone in σ. Take the band's largest σ for l_0 and for the
    bound 1/κ_I², and its smallest for Proposition E2.4.
- **What a uniform bound must reach (measured, D352).** The actual cut-off norms, from the numerical u_h, u_∞ of P2 on
  the r_*-interval of r ∈ [1.2, 4] (length 3.74), discretised kernel at 161 points:

  | σ | l = 0 | 1 | 2 | 4 | 8 | 16 | 32 |
  |---|---|---|---|---|---|---|---|
  | 0.3 | 4.75 | 1.66 | 0.79 | 0.33 | 0.12 | 0.040 | 0.012 |
  | 1.0 | 1.89 | 3.00 | 1.96 | 0.55 | 0.14 | 0.042 | 0.012 |
  | 3.0 | 0.41 | 0.42 | 0.45 | 0.67 | 0.73 | 0.065 | 0.014 |

  They fall like about 12/(l(l + 2)) once the barrier covers the interval, roughly 1/min V_l there, while Proposition
  E2.4's bound is 10⁶⁰ at (σ, l) = (0.3, 8) and overflows beyond. The missing ingredient was a lower bound on how fast
  u_h grows through the barrier. Section 3b supplies the part of it that is needed: the signs of (|u_h|²)' and
  (|u_∞|²)' at the ends of I, from the WKB energy and the flux. Labels: computed (the table); section 3b proved.
- **Near σ = 0 and large |σ|.** The bounds of sections 3b-3c degenerate as σ → 0 (the record's I.C low-energy analysis),
  while E2.8 stays bounded there for every l ≥ 1 in this cut-off norm (certified, section 3f), and E2.8′ for l = 0
  (certified, section 3g). Uniformly in l, they
  degenerate at the trapping energies σ² ≈ max V_l for large σ (the photon sphere; E4), and E2.8 grows linearly in |σ|.
- **The record's norms.** Proposition 6.2 is stated on the variable-order b-Sobolev spaces X_σ, Y_σ of the extended
  domain through the horizon; passing from L²(dr_*) per harmonic to them needs the elliptic and propagation constants of
  I.A-I.B made explicit (E2-E4).
- **Im σ > 0 near the axis.** Lemma E2.1 degenerates as Im σ → 0; joining it to Proposition E2.4 needs the real-axis
  bound to be stable under small Im σ, which the same Wronskian argument should give (the flux identity acquires a sign
  term).

## 5. Labels and sources

Proved here by inequality (Lemmas E2.1-E2.3, Proposition E2.4; Lemmas E2.5a-b, Proposition E2.5, Corollary E2.6; Lemma
E2.7; Lemma E2.8 given w ≥ 0; Lemma E2.9; Lemma E2.8′ given W_q ≥ 0); computed (P1: (1.1), (1.2); P2: numerical
illustration, scipy solve_ivp at rtol 10⁻¹¹ with the outgoing data started from the exact solution of the
inverse-square tail; P3: Corollary E2.6's
thresholds, Proposition E2.5's conditions by quadrature, and the bound against the numerical kernels; P4: unimodality
for l ≤ 40, and Lemma E2.7 against the numerical kernels on I; `checks/e2morawetz5.py` M1: identity (3.4) as an exact
derivative, sympy; M2-M3: w ≥ 0 and the constants on a grid, and B_l(3) against the computed norms, floating point, not
certified); certified (`checks/e2certify5.py` C1-C5: w ≥ 0 on ℝ for every l ≥ 1 by Lemma E2.9, and the constants, by
interval arithmetic with explicit tail bounds; `checks/e2lzero5.py` Z1-Z5: l = 0 by Lemma E2.8′, the same way).
Sources: PART-III-D-GAUGEPOT.md Proposition 6.2 and its proof (the ODE
fact); EFFECTIVE-CONSTANTS.md section 5 (E2).
