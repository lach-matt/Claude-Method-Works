# Certified existence at the prescribed wavelength 10 l5: feasibility study

*Status.* Phase 0, begun D337 (M, 2026-10-30: "start the feasibility study for the certified computation"). Nothing
here is proved. Labels as in the record: computed, deduced, READ.

## 0. The question

The paper proves its theorem for λ ≤ λ0, with λ0 not evaluated, and states that at the physical wavelength λ = 10 l5
there is no small parameter (section 9, "Physical wavelengths"). There, existence on D_T is a large-data question. The
route the record names is a posteriori: a computed approximate solution, a certified bound on its residual, a certified
linear estimate about it, and a quadratic remainder, closed by a control inequality (ROUTES-OPEN.md section 2; [CCRT07],
[MP11], [RT12], READ there). This study asks whether that route can be carried out, what decides it, and what it costs.

## 1. What is already known

- *The record's scheme breaks.* Its Bondi chart, with the areal radius as a coordinate, breaks before the shell's peak at
  both seeds. The round spheres' expansion acquires a second zero, and the core boundary ceases to be outflow
  (growth5.py, ROUTES 4.3 item 2). No approximant on D_T comes from it.

- *Growth up to the break (computed, non-rigorous).* The radiation field's growth factor exp ∫K_v dv is 1.9 and 2.1. A
  finite-difference amplification of the data along one direction, which is a lower bound for the linear propagator's
  norm, is 1.28 and 1.00. The sup-norm Grönwall factor exp ∫K_all is 17 and 2 × 10⁵ at 10 l5, and 6 × 10³ in the
  control at λ = 0.1.

- *The re-posing.* The record re-poses the problem as the characteristic initial value problem in double-null gauge: the
  incoming wave on an ingoing null hypersurface from past null infinity, and the seed's outgoing cone as the other.

- *[Wu26] (READ again, 2026-10-30).*
  - Theorem 2.1 (p. 6) is Luk's local existence for the characteristic problem in vacuum, without smallness.
  - Theorem 2.2 (pp. 6-7) is the a posteriori structure. It assumes residuals ≤ ϵ in L^∞_u L^∞_v H³(S) and bounds
    ≤ C0 on the approximate solution in H⁴(S). It concludes that a solution exists with ‖g − g̊‖ ≤ ϵ^(1/2) "for ϵ =
    ϵ(C0) sufficiently small".
  - Three things stand between this and a certificate. The threshold ϵ(C0) and the constant C = C(C0) are not
    explicit. The proof is a sketch ("we only write the proof in sketch", p. 7). It is stated in 3+1 dimensions on S²
    sections. Its bootstrap weight exp(D(u+v)) with D ≥ 8C would also cost a factor exp(16C(u+v)) in ϵ, far more than
    the measured growth.
  - So it gives the right structure, but not usable constants.

## 2. Computed in phase 0

**(a) The class in double-null gauge keeps its characteristic structure in five dimensions (`dnull5.py` D1-D5,
computed exact).**

- *The ansatz.* The metric is g5 = −2Ω²(du dv + dv du) + γ(dθ − b du)² + e^(2A)dφ1² + e^(2B)dφ2², with Ω, b, γ, A, B
  functions of (u, v, θ). The sections are T²-symmetric 3-spheres.

- *Raychaudhuri.* The outgoing equation holds with the coefficient 1/3 (one over the section's dimension) in place of
  [Wu26]'s 1/2. The ingoing one holds with the shift. A control fails in each case.

- *Tangherlini.* Five-dimensional Tangherlini in Eddington-Finkelstein double-null coordinates is vacuum, and the
  four-dimensional lapse is not.

- *Constraints.* Ric(∂_v, ∂_v) has no u-derivative, and Ric(Y, Y) no second v-derivative. So the characteristic
  constraints are ODEs along the two initial cones, as in [Wu26] Theorem 2.1.

**(b) At 10 l5 the data are one broad pulse (computed).**

- *Periods.* The phase is v/λ, with λ/√μ0 = 10/√(μ0/l5²). This is 1.000 at μ0 = 100 l5² and 0.3162 at 1000 l5². So
  there are 0.48 and 1.51 periods across the envelope's support [1/2, 7/2].

- *Consequence.* The solution is smooth on the scale of the domain. A spectral approximant at modest resolution should
  reach small residuals. So the problem is analytically hard, but it is not numerically hard.

**(c) Ball arithmetic is available and cheap (computed).**

- *Tool.* python-flint 0.9.0 (Arb balls, from PyPI) installs in this container.

- *Timings at 128 bits.* 3.2 × 10⁶ ball multiply-adds per second; 1.4 × 10⁶ enclosures of a degree-8 polynomial over
  an interval per second; 5 × 10⁵ products of degree-8 polynomials per second.

- *A rough cost.* At this rate, a residual enclosed cell by cell on 10⁶ cells, at about 10³ ball operations per cell,
  takes of the order of 10³ s. The certified evaluation is not the bottleneck.

**(d) The closing condition (deduced).**

- *The inequality.* Write the control inequality as R′ ≤ K R + G R² + ε(t), R(0) = δ, on an interval of length T, with
  F := exp ∫K.

- *A sufficient condition.* R stays below 2F(δ + ∫ε) provided δ + ∫ε < 1/(4 G T F²).

- *What it demands.* With G = 10 and T = 10 the bound is: 6 × 10⁻⁴ at F = 2; 9 × 10⁻⁶ at F = 17; 6 × 10⁻¹⁴ at F =
  2 × 10⁵; 3 × 10⁻²³ at F = 10¹⁰; 10⁻⁴⁶ at F = e⁵⁰.

- *What this means.* A smooth single pulse with a multiprecision approximant can meet any of these in principle. What
  decides feasibility is F: whether the certified linear estimate's constant stays near the measured propagator's
  (≈ 1-2), or degrades to the sup-norm Grönwall factor (2 × 10⁵), or further.

## 3. What decides it: four go/no-go questions

1. **G1, the gauge survives.**
   - *Question.* Does a double-null evolution in the class reach the end of the domain at 10 l5?
   - *Why it may.* The Bondi chart broke at a zero of the round spheres' expansion. The double-null gauge does not use
     the areal radius as a coordinate, so that particular break should not occur.
   - *What could still break it.* Null focusing (caustics of the null foliation), the axes θ = 0 and π/2, and the region
     near x_K = 1.
   - *How to test.* A prototype solver: spectral in θ with the axes' parity, marching in (u, v). This is the cheapest
     question to falsify, so it comes first.
2. **G2, the certified constant.**
   - *Question.* Is there an energy estimate for the linearised double-null system in the class whose constant F,
     evaluated on the computed solution, is within a modest factor of the measured propagator's? Section 2 (d) turns
     that factor into the number of digits the approximant needs.
   - *What it needs.* [Wu26]'s exponential bootstrap would be replaced by [MP11]'s control inequality with the actual
     coefficients. On 1D orbit sections the Sobolev and Moser constants are explicit.
3. **G3, the data.**
   - *Question.* The incoming wave starts at past null infinity. A finite computational domain needs the far-field part
     of the data with a certified tail.
   - *What exists.* The record's Bondi-series machinery at I⁻ (bondi5.py, past5.py) is the starting point. Whether it
     certifies is open.
4. **G4, the axes.**
   - *Question.* At θ = 0 and π/2 one orbit circle degenerates. The reduced estimates must hold uniformly there.
   - *Why it should work.* The five-dimensional formulation of (a) is regular there: A − log(r cos θ) and B − log(r sin
     θ) are smooth even functions. The estimates have to be written in those variables.

## 4. The target statement (proposed)

- *The rectangle.* Let Q be a characteristic rectangle carrying the record's data at λ = 10 l5. Let 𝒟_q := {p ∈ Q :
  x_K ≤ 1 on J⁻(p) ∩ Q}, a past set by definition, so the problem posed on it needs no boundary condition.

- *The claim.* Given a computed g_app on 𝒟_q, with certified residual, data error and constants satisfying the closing
  condition, there is a vacuum metric g in the class on 𝒟_q with the record's data and ‖g − g_app‖ ≤ R(u, v), R
  explicit.

- *Relation to D_T.* D_T is defined in the background's coordinates. The certified statement would be made in the
  computed solution's own double-null coordinates, and its relation to D_T stated through x_K and the areal radius. That
  correspondence is part of the statement, not an afterthought.

## 5. Plan

| step | content | output | decides |
|---|---|---|---|
| F1 | the class in double-null gauge | `dnull5.py` D1-D5 (done) | structure |
| F2 | prototype double-null solver in the class at 10 l5, both seeds | the solution on 𝒟_q, or the place it breaks | G1 |
| F3 | the linearised double-null system and an explicit energy estimate; its constant F on F2's solution | F, and the digits needed | G2 |
| F4 | the far-field data with a certified tail | data error δ | G3 |
| F5 | the a posteriori theorem in the class with explicit constants, written to proof5's standard and read by verifiers | the theorem | G2, G4 |
| F6 | multiprecision approximant; residual and data error enclosed in Arb balls; the closing condition checked | the certificate | the result |

F2 and F3 are measurements, and they come first because they can stop the study cheaply. F5 is the expensive step. It
is comparable to one of proof5's parts, but simpler in kind: a finite region, one angular variable, no decay at
infinity.

## 6. Phase-0 verdict

No blocker has been found. What is already known about the propagator (amplification 1.0-1.3 up to the break) suggests
that G2 can be met, but that is a non-rigorous measurement on a scheme that breaks, not a bound. The decisive unknown is
G1. The next step is F2.

## 7. Sources

- READ: [Wu26] arXiv:2609.08421v1, (1.1) p. 2, Theorems 2.1-2.2 pp. 6-7, the residual formulas p. 12; [CCRT07], [MP11]
  and [RT12] as in ROUTES-OPEN.md section 2.

- Computed: dnull5.py; the timings and the pulse's periods (D337).

- The record: growth5.py, ROUTES-OPEN.md 2 and 4.3, the paper's section 9.
