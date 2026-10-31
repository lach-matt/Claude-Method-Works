# E2-PILOT -- E2 at one operator: □ on 5D Tangherlini, harmonic by harmonic, with explicit constants

Status: written (D350); to be read. Check script: `checks/e2pilot5.py` P1-P2 (computed), both pass, both controls
fail.

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
G(y) dy with K_l(x, y) = u_h(min(x, y)) u_∞(max(x, y))/W and

    |K_l(x, y)| ≤ |σ|⁻¹ exp(I_l/(2|σ|)),     I_l = (l(l+2) + 3/2)/√μ.

So for χ the indicator of an r_*-interval of length Λ, ‖χ R_l(σ) χ‖_(L²(dr_*) → L²(dr_*)) ≤ (Λ/|σ|) exp(I_l/(2|σ|)).

*Proof.* Variation of constants gives K_l, W ≠ 0 by Lemma E2.2. Lemma E2.3 at min(x, y) ≤ max(x, y): |u_h(min)|
|u_∞(max)| ≤ 2 exp((2|σ|)⁻¹(∫_(−∞)^(min) V_l + ∫_(max)^∞ V_l)) ≤ 2 exp(I_l/(2|σ|)), and |W| ≥ 2|σ|. The operator bound is
the Hilbert-Schmidt bound of a kernel bounded by that constant on a square of side Λ. ∎

This is III.D Proposition 6.2's injectivity at real σ, harmonic by harmonic, with a constant: the first N1 step of the
record turned into a number, by inequality alone. P2 checks the lemma's three ingredients against numerical solutions
for l ≤ 6 at four values of σ (it does not prove them).

## 4. What remains for E2 at this operator

- **Uniformity in l (E2.5).** exp(I_l/(2|σ|)) grows like exp(l²/(2|σ|√μ)): Lemma E2.3 ignores that the solutions
  decay, not grow, through the barrier when V_l > σ². For a compact σ-band only finitely many l have max V_l ≤ 2σ²;
  for the others an Agmon-type estimate in the classically forbidden region should give a bound uniform in l. This is
  the next step, to be written with its constants.
- **What a uniform bound must reach (measured, D352).** The actual cut-off norms, from the numerical u_h, u_∞ of P2 on
  the r_*-interval of r ∈ [1.2, 4] (length 3.74), discretised kernel at 161 points:

  | σ | l = 0 | 1 | 2 | 4 | 8 | 16 | 32 |
  |---|---|---|---|---|---|---|---|
  | 0.3 | 4.75 | 1.66 | 0.79 | 0.33 | 0.12 | 0.040 | 0.012 |
  | 1.0 | 1.89 | 3.00 | 1.96 | 0.55 | 0.14 | 0.042 | 0.012 |
  | 3.0 | 0.41 | 0.42 | 0.45 | 0.67 | 0.73 | 0.065 | 0.014 |

  They fall like about 12/(l(l + 2)) once the barrier covers the interval, roughly 1/min V_l there, while Proposition
  E2.4's bound is 10⁶⁰ at (σ, l) = (0.3, 8) and overflows beyond. The missing ingredient is a lower bound on the growth
  of u_h through the barrier, |A| ≳ exp(∫(V_l − σ²)₊^(1/2) dr_*), matching the upper bounds of Lemma E2.3 there; with
  it the kernel is controlled by exp(−∫_x^y (V_l − σ²)^(1/2)) inside the barrier. The route: the Riccati equation for
  u'/u, whose imaginary part is fixed by the flux (Im(ū u') = ∓σ), with comparison in the forbidden region and the WKB
  energy |u'|² + (σ² − V_l)|u|², which is monotone where V_l is (its derivative is −V_l'|u|²), in the allowed regions.
  Labels: computed (the table), not proved.
- **Near σ = 0 and large |σ|.** The bound degenerates as σ → 0 (the record's I.C low-energy analysis) and, uniformly in
  l, at the trapping energies σ² ≈ max V_l for large σ (the photon sphere; E4).
- **The record's norms.** Proposition 6.2 is stated on the variable-order b-Sobolev spaces X_σ, Y_σ of the extended
  domain through the horizon; passing from L²(dr_*) per harmonic to them needs the elliptic and propagation constants of
  I.A-I.B made explicit (E2-E4).
- **Im σ > 0 near the axis.** Lemma E2.1 degenerates as Im σ → 0; joining it to Proposition E2.4 needs the real-axis
  bound to be stable under small Im σ, which the same Wronskian argument should give (the flux identity acquires a sign
  term).

## 5. Labels and sources

Proved here by inequality (Lemmas E2.1-E2.3, Proposition E2.4); computed (P1: (1.1), (1.2); P2: numerical illustration,
scipy solve_ivp at rtol 10⁻¹¹ with the outgoing data started from the exact solution of the inverse-square tail).
Sources: PART-III-D-GAUGEPOT.md Proposition 6.2 and its proof (the ODE fact); EFFECTIVE-CONSTANTS.md section 5 (E2).
