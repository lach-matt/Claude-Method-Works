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

## 6a. F2 design: the evolution scheme (computed, D338)

The second derivatives in each component of Ric(g5) for the class in double-null gauge (computed from `dnull5.py`'s
metric; θ derivatives written t):

| component | second derivatives | role |
|---|---|---|
| Ric_vv | A_vv, B_vv, γ_vv | the outgoing constraint: an ODE in v on u = u0 |
| Ric(Y, Y) | A_uu, B_uu, γ_uu, b_uv, ... | the ingoing constraint: an ODE in u on v = v0 |
| Ric_vθ | b_vv, A_tv, B_tv, Ω_tv | transport of the shift b in v |
| Ric_11, Ric_22 | A_uv, A_tv, A_tt (and B) | wave equations for A, B |
| Ric_θθ | γ_uv, γ_tv, A_tt, B_tt, Ω_tt, b_tv | wave equation for γ |
| Ric_uv | Ω_uv, Ω_tv, Ω_tt, A_uv, B_uv, γ_uv, b_vv | wave equation for Ω |
| Ric_uθ | A_tu, B_tu, Ω_tu, γ_uv, b_uv, ... | a constraint |

No other component is nonzero. So the scheme is the following.

- *Evolution.* Evolve (A, B, γ, Ω) by their four (u, v) wave equations, with b from its v-transport.

- *Data.* Solve the two characteristic constraints for the data on u = u0 and v = v0.

- *Monitoring.* Monitor Ric_vv, Ric(Y, Y) and Ric_uθ, which the Bianchi identities propagate.

- *Discretisation.* In θ, the regular parts Â := A − log(r cos θ), B̂ := B − log(r sin θ) and γ/r² are expanded in cos
  2kθ, which is even at both axes. In (u, v), a second-order diamond scheme.

- *Coordinates.* On the ingoing initial cone v = v0 (exact Tangherlini, before the shell), take u := −r, which is
  regular across the horizon. On the outgoing initial cone u = u0, take v Eddington-Finkelstein. Ω is then fixed by
  these choices on the two cones.

## 6b. F2: the prototype and what it measured (computed, D344; non-rigorous)

- *The instrument.* `dnsolve5.py` evolves the class in double-null gauge. The section metric is written with the
  record's regular combinations (hf_mirror5.py's F, G): with P = (2(1+x)m − (1−x)n)/3 and Q = (2(1−x)n − (1+x)m)/3,
  the axis conditions 2P + Q = 0 at x = −1 and P + 2Q = 0 at x = 1 hold identically. Ric_11, Ric_22, Ric_xx give the
  mixed derivatives of R, m, n; Ric(Y, ∂_v) = Ric_uv + β Ric_vx gives W's (its second v-derivatives cancel); Ric_vx
  transports the shift along each outgoing cone. A second-order diamond scheme in (u, v), Chebyshev–Gauss in x. Its
  selftest: Tangherlini at second order (S1), the Kretschmann scalar on flat space and Tangherlini (S2), and a control
  with inconsistent data that does not converge (S3).

- *The coordinate.* With u := −r on the first ingoing cone, the late interior is squeezed into an exponentially thin
  u-interval (r − 1 ≈ (r₀ − 1)e^v): at v = 1.6 the region 0.54 ≤ R ≤ 1 spanned about four rows of a uniform grid, and
  the scheme failed there at a v that moved with the cut and with resolution. A grid logarithmic in |1 + u| gives 107
  rows there at v = 1.6 and 43 at v = 4.

- *λ = 1 (L = 100).*
  - *The record's break is passed.* Along an ingoing cone the outgoing expansion R_v acquires a second zero at
    v = 1.425, earlier than the record's Bondi chart broke at the first seed: 1.500 by the persistence criterion (Ny =
    20; 1.496 at Ny = 28), the 1.4516 once stated there being a single-step excursion of the root count (LOG D43-D44);
    at the second seed the break is 1.583. The double-null evolution continues through the second zero and past v =
    1.5 (corrected D346: this line had compared with the transient 1.45).
  - *Constraints.* Ric_vv, Ric(Y, Y) and Ric_ux, by differences on the solution, converge at second order or better
    on common points up to v = 1.5 (ratios 4.1 to 16 between 380 and 760 rows).
  - *The domain.* The curvature exceeds the record's bound near the inner cut from v ≈ 1.45 (x_K = 1.22 at R ≈ 0.58),
    because the wave adds to the seed's curvature. So 𝒟_q is smaller than {R ≥ r_core}. Computed on the interior
    strip u > −1.3 at 800 rows by 360 columns, M = 8: 113,682 of 125,265 cells, reaching v = 4.5.
  - *Convergence on 𝒟_q* (400 against 800 rows, common points). Every field converges up to v ≈ 2.0: for
    1.4 ≤ v < 2.0 the fine–coarse differences are 3 × 10⁻³ in R, 0.04 in m (of 0.85) and 2.5 in s (of 122). Beyond
    v = 2 the shears m, n do not converge (differences comparable to their size), while R and W do (≤ 0.1 and 0.04).
    W stays in [−0.35, 1.29] on 𝒟_q: no sign of a degenerate lapse.
  - *Outside 𝒟_q.* Where x_K > 1 on the past, an axis growth starts at v ≈ 1.61, reproducibly (400 and 800 rows;
    M = 12 at 1.64). 𝒟_q is a past set, so it does not reach 𝒟_q.

- *λ = 0.3162 (L = 1000).*
  - The second zero of R_v appears, and the evolution continues through it.
  - It runs to v ≈ 3.3–3.4 of 4.5. There an axis growth starts at x = +1 just outside the horizon (R ≈ 1.2), where x_K
    is small. Its onset moves later with angular resolution (M = 6, 8, 12: v = 1.86, 3.28, 3.44) and with (u, v)
    resolution (3.28, 3.36): a resolution limit of the prototype, not a gauge breakdown. 𝒟_q is not yet computed here.

- *Angular resolution (D351).* An exponential filter in x (order 32 at M = 12, order 64 at M = 16, 24) keeps the
  shears bounded on 𝒟_q where the unfiltered runs grow to m ≈ 100, but does not make them converge. On 𝒟_q, with 𝒟_q
  recomputed on the filtered M = 12 run at 800 × 360 (111,891 of 123,975 strip cells): every field converges in (u, v)
  and in M up to v ≈ 1.5 (M = 16 against 24: |Δm| ≤ 4 × 10⁻⁵); on 1.5 ≤ v < 2, m differs by 0.36 to 0.44 between M =
  12, 16 and 24 (of 0.44 to 0.55), and the unfiltered M = 8 and 12 runs of D344 differ by 0.85 there. Refining v by 4
  changes the M = 16 solution by 0.03 there while M = 12 against 16 stays at 0.38: not a step-size limit. The
  difference starts at the axis x = −1 near the seed's horizon generator (u ≈ −0.95 to −1, R ≈ 0.7 to 1), from v ≈
  1.6, where the Chebyshev spectrum of m, decaying to 3 × 10⁻⁷ at v = 1.6, flattens to 10⁻³ by v = 1.75 and is
  unresolved by v = 2.2. M = 24 at the finer v-step and M = 32 stop on a singular 4 × 4 solve. So the solution steepens
  at that axis faster than M = 24 resolves; whether that is the solution or the axis treatment is the next question.
  D344's "converged on 𝒟_q up to v ≈ 2.0" held in (u, v) only (corrected D351).

- *The axis nodes (D354).* The singular 4 × 4 solves at M = 24 and 32, and part of D351's angular disagreement, were
  rounding in that solve. At the nodes next to an axis its error grows like (1 − |x|)^(−4.5) times the machine
  epsilon.
  - A spherical state's error at the node next to the axis, in double precision, is 1.3 × 10⁻¹⁰, 3.8 × 10⁻⁹,
    9.8 × 10⁻⁸, 3.7 × 10⁻⁶ and 3.9 × 10⁻⁶ at M = 8, 12, 16, 24, 32.
  - Tangherlini with no injected noise acquires a spurious m of 8.6 × 10⁻⁹, 8.7 × 10⁻⁷ and 7.9 × 10⁻⁵ at M = 8, 16,
    24; with the fix, 5.2 × 10⁻¹¹, 4.3 × 10⁻⁹ and 6.3 × 10⁻⁸.
  - The fix solves at k nodes per axis in 80-bit long double, the expressions' rational constants exact
    (`dnsolve5.py ... ld k`; selftest S4: 9.8 × 10⁻⁸ becomes 7.4 × 10⁻¹¹). Dividing by the Chebyshev axis factor
    (`reg`) does not cure it.
  - The iteration parameter q = du dv |λ_max|/4 exceeds 1 at 400 × 180 (1.89 at M = 24, 3.27 at M = 32), but runs at
    800 × 360 show that it is not what limits convergence.
- *𝒟_q with |K| (D354).* K is negative where the runs disagree (K/K_c down to −29), so 𝒟_q is now built from
  x_K := |K| r_c⁸/72. It has 111,623 cells at M = 24 and 111,506 at M = 32, of 224,181 strip cells, the same in each
  v-band to 1 %. On their intersection (111,370 cells), at 800 × 360 with `ld`:
  - every field converges in M up to v = 1.5. On [1, 1.5), d(M16, M24) in m is 6.0 × 10⁻⁵ and d(M24, M32) is
    9.8 × 10⁻⁷;
  - beyond, it does not: d(M24, M32) in m is 0.68 on [1.5, 2), 5.8 on [2, 2.5), and between 3 and 20 later;
  - the onset is at the axis x = −1 inside the horizon. d > 10⁻⁴ first at u = −0.964, v = 1.650 (the node x = −0.995),
    and d > 10⁻³ at v = 1.688. There x_K = 0.81, and the maximum of x_K over the cell's past is the same: the onset is
    inside the curvature domain, not beyond it. The shift s is large there (about 200 to 370).
  So the curvature cut does not remove the disagreement. It is a resolution or axis-treatment limit of the scheme at
  x = −1 inside the horizon. At the second seed (λ = 0.3162), with `ld`, the run converges in angle to v ≈ 3-3.5
  (on [2.5, 3), d(M16, M24) is 1.3 × 10⁻³ in m and 1.1 × 10⁻² in n). Beyond that n steepens at the axis x = +1 near
  R ≈ 0.93-1.0, where x_K ≤ 0.025, and the Chebyshev tail rises from 5.8 × 10⁻⁶ to 5.6 × 10⁻³.

- *The shift's drag at the axes (D381; `checks/axisdrift5.py` on the saved runs, computed).* The angle enters the metric
  as dx − (1 − x²)s du. So along an ingoing null generator orthogonal to the orbits, the curves that carry the ingoing
  wave, x moves by dx/du = (1 − x²)s: ln(1 + x) changes at the rate 2s(x = −1) near x = −1, and ln(1 − x) at −2s(x = +1)
  near x = +1. Integrated in u from the first cone, at the node next to each axis:
  - *λ = 1, x = −1.* A fixed geometric angle near the axis has been pressed toward it by e^(−1.2) at v = 1.5, e^(−3.2)
    at 1.6, e^(−5.0) at 1.65, e^(−8.1) at 1.7 and e^(−13) at 1.8, the strongest in each column at R ≈ 0.52 inside the
    horizon (u ≈ −0.95 to −0.97). The first Chebyshev node is at ln(1 + x) = −6.15 (M = 24) and −6.7 (M = 32). So the
    disagreement's onset (v = 1.65, u = −0.964, where the drag is e^(−1.7) and e^(−5.0) one row inward) is where the
    ingoing wave's angular structure is pressed inside the first node. The shift there is −60 to −1600. This is a
    property of the coordinate, so the non-convergence at x = −1 is at least in large part the gauge's: the shift
    condition drags the angle into the axis faster than any fixed grid resolves.
  - *λ = 0.3162, x = +1.* At the failure (v ≈ 3.3, R ≈ 0.93-1.0) the drag is below e^(0.02) everywhere in the column.
    So the second seed's steepening is not this effect, and stays open.
- *The swapped gauge (D386; `dnsolve5v.py` V1-V4, computed).* The shift moved to dv: dx − (1 − x²)s dv, so x is
  constant along the ingoing generators that carry the wave, and the drag moves to the outgoing ones.
  - *The equations.* The two Ricci tensors are exact mirror images under u ↔ v (V1). So the scheme is dnsolve5's
    mirrored: Ric_ux transports s along each ingoing cone.
  - *The new datum.* The one new quantity is s_u on the wave's cone u = −R0, where s = 0 is the gauge. It comes from
    Ric_vx, an ODE in v along that cone once the transverse derivatives R_u, m_u, n_u, W_u are carried by the
    uv-equations from Tangherlini at the corner. With Tangherlini data it returns Tangherlini's R_u at second order
    (V3).
  - *Checks.* Tangherlini on the stretched grid is second order (V2). The spurious s that the axis rounding of D354
    leaves on the kept cells is 6.3 × 10⁻⁵ at 200 × 90 and 5.3 × 10⁻⁵ at 400 × 180, against dnsolve5's own
    1.7 × 10⁻⁴ and 1.0 × 10⁻⁴.
    At λ = 1, s_u on the wave's cone agrees with the marched s to 7.5 × 10⁻⁷ and then 1.6 × 10⁻⁷, against
    |s_u| ≤ 3.5 × 10⁻⁵ (V4, D391).
  - *The invariant check (V4, and at the production grid).* The section volume π²∫R³dx is gauge invariant here, since
    the null foliation is the same in both gauges.
    - It agrees between the gauges to 10⁻¹² before the wave arrives (v < 0.5).
    - Later the gap is within the swapped gauge's own (u, v) error, which is about three times dnsolve5's: between
      400 × 180 and 800 × 360 at M = 16, 2.9 × 10⁻² against 8.7 × 10⁻³ on [1.5, 2). Over that one doubling the gap
      falls about 3.5-fold: 1.7 × 10⁻² → 4.8 × 10⁻³ on v ∈ [1, 1.5), 3.5 × 10⁻² → 9.7 × 10⁻³ on [1.5, 2). In the
      section volume itself, 400 against 800 at M = 24 and k = 10 on the cells both keep, the factor is 1 to 14,
      equal on [0.5, 1) (D399, corrected D402 and D405).
  - *λ = 1 at 800 × 360 with `ld 3`, max over 𝒟_q of |Δm| between angular resolutions, per v-band:*

    | v | [1, 1.5) | [1.5, 1.65) | [1.65, 1.8) | [1.8, 2) | [2, 2.5) | [2.5, 3) |
    |---|---|---|---|---|---|---|
    | dnsolve5, M16-M24 | 7.3e-5 | 5.4e-3 | 0.75 | 3.9 | 13 | 10 |
    | dnsolve5, M24-M32 | 1.7e-6 | 3.9e-4 | 0.43 | 3.4 | 12 | 87 |
    | swapped, M16-M24 | 9.6e-4 | 2.7e-3 | 6.3e-3 | 3.0e-2 | 0.53 | 0.60 |
    | swapped, M24-M32 | 7.3e-6 | 2.9e-5 | 4.7e-5 | 2.4e-4 | 0.89 | 1.0 |

    n behaves the same way (swapped M24-M32: 1.6 × 10⁻⁵ on [1.8, 2), 1.7 × 10⁻² on [2, 2.5)). Each row is over 𝒟_q
    ∩ that gauge's kept cells, and the sets differ: the swapped gauge drops 12,520 of the record's cells there, and on
    the cells both keep the comparison comes out otherwise (D399, corrected D402).
  - *The drag.* In this gauge the angle is pressed toward an axis by at most e^(−0.92), at x = +1 for v ≈ 2.75.
    dnsolve5's was e^(−13) at x = −1. But the angle is drawn away from x = −1, by up to e^(+2.35) at v = 2.14 and
    e^(+2.52) at v = 2.5, along the last unmasked rows (`dnsolve5v.py --drift`, both signs since D391; the first
    version reported the pressing sign only).
  - *The new limit (corrected D391, verifier 177).* Convergence in angle now holds to v ≈ 2.1 instead of 1.65.
    |Δm| > 10⁻³ first at v = 2.14, u = −1.041, at the axis x = −1.
    - There R = 0.54 at the axis node. That is the run's own cut (a cell is dropped when R < r_cut at any node), and
      R reaches it there under this gauge's outward drift at x = −1. At the same (u, v), R at dnsolve5's axis node is
      1.23.
    - R at a node is not invariant (V4's control), so neither the horizon nor the cut is located by it.
    - The M32 Chebyshev tail of m there rises from 6 × 10⁻⁸ at v = 1.89 to 3 × 10⁻⁵ at v = 2.14.
    - Whether the limit is the axis condition on m (only (1 + x) m_uv is fixed there, D352) or this drift and the cut
      it drives is not yet separated.
    - D386 printed "R = 1.58, outside the horizon" and "the axis condition on m, not the drag". That R was read at the
      node next to x = +1, and x_K = 0.001 came from dnsolve5's run, which is not converged there. Both are
      withdrawn.
- *An invariant cut (D392; `dnsolve5v.py ... vol`, computed).* The cut was moved to the areal radius (V/2π²)^(1/3) of
  the invariant section volume, with R ≥ r_cut/2 at every node as a floor for the solve. The runs keep 4,867 more cells
  at 800 × 360 at M = 24 and 4,045 at M = 32 (169,722 at M = 24, against 164,855 with the node cut). Those cells are
  where R at the x = −1 node falls to 0.27-0.34 while the areal radius stays at or above 0.54, and they do not converge
  in angle: |Δm| between M = 24 and 32 exceeds 10⁻⁴ from v = 1.46 (u = −0.940, x = −0.9988, areal radius 0.545, node R
  0.34) and 10⁻² from v = 1.58. So under either cut the converged region of the swapped gauge lies within the cells
  where R at every node stays at or above about 0.54: a necessary condition, not a sufficient one, since node-cut cells
  fail too from v ≈ 2.25 (D395). The failure follows small R at the x = −1 axis node. The curvature at those cells
  cannot be evaluated, as they border the cut and the Kretschmann stencil reaches masked neighbours. Inward, at v = 1.9,
  x_K = 0.048 on the section. In dnsolve5's gauge, too, the onset was at the x = −1 axis with R about 0.52 there (D381).
  Whether this is the axis treatment at small R or the approach of the axis to the singularity is not decided by these
  runs.
- *The metric's own fields (D393, corrected D395 after verifier 178).* m is absent from the metric's values at
  x = −1 (P = −2n/3, Q = 4n/3 there) but enters its x-derivative there and the axis curvature. Holding R constant in
  x, the Gauss curvature of the (x, φ1) plane at x = −1 is (3 − 28m − 8n + 16 ∂_x n) e^(4n/3)/(3R²) (verifier 178,
  sympy). The fields' values P, Q, R, W converge more easily than that, as |ΔP| is damped by (1 + x) near the axis.
  - *Values, away from the cut.* The swapped gauge's metric values converge in angle on a strip that stops short of
    the cut. Measured with each v-column's last k kept rows dropped, M24-M32 against M16-M24:
    - k = 3: converged to v ≈ 2.25 (|ΔP| 2.2 × 10⁻⁴ against 8.3 × 10⁻⁴ on [2.25, 2.5); growing on [3, 3.5));
    - k = 10: to v ≈ 3 (|ΔP| 1.7 × 10⁻⁶, 2.0 × 10⁻⁵, 3.7 × 10⁻⁵ against 8.3 × 10⁻⁵, 2.1 × 10⁻⁴, 2.3 × 10⁻⁴ on
      [2, 2.25), [2.25, 2.5), [2.5, 3));
    - k = 20: to v ≈ 3.5;
    - k = 40: falling 10-20 fold in every band to v = 4.6.

    In every band the largest difference sits exactly k rows from the cut, so the error rises steadily toward the cut.
    From v ≈ 2.4 the last kept row is frozen at u = −1.0557, where R is 0.92-1.43: the mask there is inherited from
    earlier columns, not a fresh cut. So the converged region is a strip in u below the cut, and no single v marks
    its end.
  - *The axis.* m does not converge at x = −1 beyond v ≈ 2.25: 6.1 × 10⁻² → 2.45 × 10⁻² on [2.25, 2.5) and
    6.6 × 10⁻² → 3.4 × 10⁻² on [2.5, 3). Off the axis (x > −0.9) it does: 3.4 × 10⁻³ → 2.8 × 10⁻⁴ on [2.25, 2.5). So the
    metric converges in its values but not in its first and second x-derivatives at the axis, and the axis curvature
    is not converged beyond v ≈ 2.25.
  - *The axis circle.* g_22 = R²e^(8n/3) on x = −1 is the same function of (u, v) in both gauges. In the swapped gauge
    its M24-M32 difference is 1.1 × 10⁻⁶ on [2, 2.25) and 1.8 × 10⁻⁵ on [2.25, 2.5). But over the kept cells the
    M32 run's last Chebyshev coefficient exceeds M24's from v ≈ 2 (for m 4.2 × 10⁻⁶ against 2.5 × 10⁻⁶ on [2, 2.25),
    for R 3.2 × 10⁻⁶ against 2.3 × 10⁻⁶). An endpoint value carries the tail undamped (T_k(−1) = (−1)^k), so the
    extrapolation to the axis is noise-limited from there. Between the gauges the maxima, 1.85 × 10⁻³ on [0.5, 1) and
    1.4 × 10⁻² on [1, 1.5), are on the last kept row, with medians 5.9 × 10⁻⁶ and 2.8 × 10⁻⁴. Their attribution to
    (u, v) error is not measured, as no (u, v) refinement of g_22 was run.
  - *Next to the cut and late.* Over all kept cells (k = 0), |ΔP| between M24 and M32 is 3.4 × 10⁻³ on [3, 3.5) and
    7.0 × 10⁻³ on [3.5, 4.6), and |ΔW| 5.8 × 10⁻³. For v ≥ 3 these sit at x = +1 on the last kept row. Beyond v ≈ 3
    (at k = 10) the differences grow with M, so no error estimate is available there. D393's "resolved to below
    7 × 10⁻⁴ beyond" is withdrawn.
  - *dnsolve5, the same measure.* |ΔP| between M24 and M32 is 0.019 on [1.65, 1.8) and 2.75 on [2, 2.25) (k = 10).
  - *The shift s* (compared since D395) converges in angle too, less tightly. At k = 10, M16-M24 against M24-M32 is
    3.6 × 10⁻² → 1.5 × 10⁻³ on [2.25, 3) and 1.1 × 10⁻² → 3.7 × 10⁻³ on [3, 3.5). At k = 40 it falls in every band,
    for example 1.8 × 10⁻³ → 2.8 × 10⁻⁵ on [3.5, 4.6). D393's "converges to v ≈ 3 away from the cut" is withdrawn as stated: the
    extent depends on k, as above (`checks/g1geom5.py LOW HIGH 3 10 20 40`).
- *In (u, v), and both gauges on one set of cells (D399; `checks/g1uv5.py`, `checks/g1cells5.py`, computed).* At
  λ = 1 and M = 24, on the nested grids 200 × 90, 400 × 180 and 800 × 360 (the u-grid linspace in arcsinh, the v-grid
  linspace, so every second point of a finer grid is a point of the coarser):
  - *The swapped gauge on its own kept cells.* With each v-column's last 10 kept rows dropped, the ratio of successive
    differences is 2.9-4.9 for P, Q, R, W and m and 3.4-6.9 for s, in every band to v = 4.6: about second order. The
    400-800 differences peak on [1.65, 1.8), at 9.7 × 10⁻³ in P (2.5 % of max |P|), 2.7 × 10⁻² in R, 4.8 × 10⁻² in W,
    1.1 × 10⁻² in m and 0.26 in s (11 % of max |s|), and fall to 1.6 × 10⁻³ in P on [3.5, 4.6).
    - So the (u, v) error of the 800 × 360 runs exceeds the angular differences above in every band. On like cells
      (10 coarse rows, about 40 of the 800 grid, dropped from each column; M24-M32 at k = 40) P's 400-800 difference
      is about 700 times its angular one on [3.5, 4.6), 2.3 × 10³ times on [3, 3.5) and 10⁴ to 8 × 10⁵ times before
      v = 3 (D402, D405; D399's factors compared different cells). The grid in (u, v), not M, sets their error.
    - Over all kept cells (k = 0) the coarsest grid is not in the asymptotic range on [2.25, 3) in P, Q, s and m
      (ratios 24 to 1.1 × 10⁴), nor in W on [2.25, 2.5) (58.6), nor in m from v = 1.8 (13.7); R stays at 4.4-5.7
      there. Beyond v = 3 P (6.8, 175), R (21.9) and m (1.3 × 10³, 2.5 × 10⁴) are off too (D402, D405).
  - *Both gauges on the cells both keep.* A cell (u_i, v_j) is the same pair of null hypersurfaces in either gauge, so
    the gauges can be compared cell by cell. The swapped gauge keeps fewer: at 800 × 360 the record's gauge keeps
    181,444 cells at all three M and the swapped gauge 164,847, all but 20 of them among the record's. On the 164,827
    common cells, and on the 9,764 coarse cells all six (u, v) runs keep:
    - In (u, v) the record's gauge converges at ratio 3.7-4.5 for P and m and 3.3-5.8 for s, in every band at k = 3, 10
      and 50. Its errors are smaller at k = 10 from v = 1: in the invariant section volume V(u, v) = π²∫R³dx by 1 to
      14 (equal on [0.5, 1)); in W at equal labels by 2 to 29 (W is one scalar, but the gauges' x labels agree only on
      u = −R0, and at equal (u, v, x) the two W differ by up to 0.25, so this is not a gauge-free figure); in P, which
      depends on the gauge, by 12 to 56 before v = 2.5 and 1.7 to 6 after (5.9 to 27 relative to max |P| before
      v = 2.5). (D405, verifier 180.) In P, 400-800 is at most 9.4 × 10⁻⁴ (on [3.5, 4.6)) against the swapped
      gauge's 9.7 × 10⁻³ (on [1.65, 1.8)). (Corrected D402: D399 gave 14 to 57 in P.)
    - In angle, at k = 10, the record's gauge converges to v ≈ 3.5 in P and in m, the axis x = −1 included (m, M16-M24
      against M24-M32: 6.0 × 10⁻³ → 1.1 × 10⁻³ on [2, 2.25), 4.1 × 10⁻² → 1.0 × 10⁻² on [3, 3.5)). The swapped
      gauge's m stops at v ≈ 2.25 (above). On [1.8, 2.25) the swapped gauge is the better in angle, by up to 11 in P
      (M24-M32 4.7 × 10⁻⁷ and 1.7 × 10⁻⁶ against 5.1 × 10⁻⁶ and 8.5 × 10⁻⁶; D402).
    - The swapped gauge is the better of the two in s near the cut (k = 10, [1.65, 3): M24-M32 1.6 × 10⁻⁴ to 1.5 × 10⁻³
      against 2.4 × 10⁻⁴ to 1.3 × 10⁻²). On [3.5, 4.6) neither converges in m at k = 10.
  - *The record's gauge on its other cells.* The failures reported for it lie on the 16,617 cells that only it keeps,
    between the swapped gauge's cut and its own, from v = 1.5 on. These are the dnsolve5 rows of the table above and
    the |ΔP| of 0.019 and 2.75 in the bullet before. At k = 0, |ΔP| there is 5.8 × 10⁻³ on [1.5, 1.65), 0.85 on
    [1.65, 1.8), and up to 1.7 × 10⁵; |Δm| is up to 1.1 × 10⁸. The 4,867 cells that D392's invariant cut adds to the
    swapped gauge fail too.
    - Its own k-scan (D403, `checks/g1geom5.py` on its M16, M24, M32 runs): with the last 60 of its kept rows dropped
      it still fails on [1.8, 2.25) (|ΔP| M16-M24 → M24-M32: 2.6 × 10⁻² → 1.4 × 10⁻², 1.27 → 0.64). There it keeps
      on average about 230 rows per column more than the swapped gauge (238 and 226; 90 to 291). Extended to 250 rows
      (verifier 180), its M24-M32 |ΔP| falls steadily, with no edge: 1.0 × 10⁻² and 0.16 at 100 rows, 8.9 × 10⁻³ and
      2.6 × 10⁻² at 150, 4.9 × 10⁻³ and 6.9 × 10⁻³ at 200, 7.5 × 10⁻⁴ and 1.0 × 10⁻³ at 250, against 5.1 × 10⁻⁶ and
      8.5 × 10⁻⁶ on the common cells. So its error falls from its own cut to about the swapped gauge's, where it
      converges: in both gauges the convergence improves toward the same events, without a measured edge (D405).
  - *What this changes.* D386-D395 compared each gauge over its own kept cells, so the gain the table above shows
    from dnsolve5 to the swapped gauge is a difference of cell sets more than of gauges. On one set of cells the
    record's gauge is better in angle from v ≈ 2.25 to 3.5 and worse on [1.8, 2.25), s near the cut aside, and better
    in (u, v) from v = 1 (D402, D405). In both gauges the cells that fail
    border the cut near the x = −1 axis at small R (D381, D391-D392). Whether that is the axis treatment, the cut or
    the geometry is still not decided.
  - *The swapped gauge's order in (u, v).* Its ratio for P stays at 2.9-3.0 on [1, 1.8) at every k from 3 to 50, so
    these three grids do not separate a pre-asymptotic second order from an order near log₂ 3 ≈ 1.6. The fourth grid
    does (D403): on 400 × 180, 800 × 360 and 1600 × 720 (the last 2,772 s), with 20 rows of the 400 grid dropped (the
    distance of 10 rows of the 200 grid), the ratios are 3.5-4.3 for P, 3.6-4.4 for W, 3.8-4.9 for s and 3.4-5.5 for
    m in every band, and with 100 rows dropped 3.5-4.1 for P. So the order approaches second, and the coarser triple
    was not yet asymptotic; on [1, 1.8) the P ratio is 3.52-3.54 at both 20 and 100 rows, an order of about 1.8
    (D405). The 800-1600 differences peak on [1.65, 2) at 3.8 × 10⁻³ in P and 0.10 in s, so by Richardson the
    1600 × 720 run's own error there is about 1.4 × 10⁻³ in P, 0.3 % of the band's max |P| (0.45).
- *The cut moved (D410; `checks/g1cut5.py`, computed).* dnsolve5's gauge at λ = 1, M = 24 and 32, 800 × 360, with
  r_cut = 0.54, 0.7 and 0.9. The grids differ between cuts (u runs to −r_cut), so events are compared through the
  areal radius (V/2π²)^(1/3).
  - *The onset is where the kept set ends.* |Δm| first exceeds 10⁻³ next to the cut each time: at v = 1.550 (0 rows
    from the cut, areal radius 0.614), 1.675 (1 row, 0.761) and 1.825 (6 rows, 0.933). Along the column through
    v = 1.99 it is 1.4 × 10³ at the cut for r_cut = 0.54 and 1.8 for r_cut = 0.9.
  - *The cut cannot reach a kept cell (corrected D413, verifier 181).* dnsolve5 masks a cell whenever one of its three
    past neighbours is masked (dnsolve5.py:305-306), so every kept cell's discrete past is kept, and the cut changes a
    kept cell only through the u-grid (u1 = −r_cut changes du by about 11 %). At the last row kept by r_cut = 0.9, and
    1, 5 and 20 rows before it, the r_cut = 0.54 run has the same |Δm| at the same (u, v): 8.9 × 10⁻³ against
    8.6 × 10⁻³ at v = 1.85, 0.11 against 0.11 at v = 1.90, 2.2 against 2.1 at v = 2.00 (verifier 181's `same.py`).
    So the onset following the cut is a selection effect: the first kept cell above τ is at the edge of the kept set.
    D410's split into a part "next to the cut, that belongs to the cut-off" and a part at the axis is withdrawn. There
    is one failure, a property of the events: it starts at the x = −1 axis at areal radius about 1 near v = 2 and
    spreads toward small R and late v, and the cut decides only how much of it is kept.
  - *At the event.* u = −1.003, v = 1.988, x = −0.989, areal radius 1.000: |Δm| (M24-M32) is 0.227 at r_cut = 0.54 and
    0.232 at 0.9, 191 and 145 rows from the respective cut, and M16-M24 there is 0.278, so it barely converges. In x
    it peaks at x = −0.989 (Lobatto node 61 of 65, 0.23), with 0.07 at x = −1 (corrected D413). Over the cells of
    areal radius ≥ 1.0 on [1.8, 2) the maxima are 0.23 in m and 5.8 × 10⁻³ in P at every cut; that agreement could
    not have come out otherwise, since those cells are kept by every cut. Beyond v = 2 the sets "areal ≥ ρ" are not
    the same region across cuts, as the kept sets differ.
  - *A second axis treatment fails the same way (D413).* dnsolve5's `reg` option, which recovers m_uv at the axis by
    exact division (D352), at r_cut = 0.9, M = 24 and 32 (881 s and 1028 s; `checks/g1axis5.py`): |Δm| at the event
    is 0.308, against 0.232 without it. Over areal radius ≥ 1.0 the band maxima of |Δm| are 2.3 × 10⁻¹ / 3.1 × 10⁻¹ on
    [1.8, 2) (plain / reg) and 2.0 × 10⁻⁶ / 6.8 × 10⁻⁷ on [1.65, 1.8). The two treatments agree to 2.3 × 10⁻⁷ at M32
    up to v = 1.8 (areal ≥ 1). At the event's node they differ by 0.18 at M24 and 0.10 at M32 (0.51 and 0.45 at the
    worst node of that cell, x = −1). [D420, verifier 182: at x = −1 plain m = 0.708, 0.779, 0.791, 0.765 and 1.000 at
    M24-56
    and reg 1.217, 1.229 at M24, 32: plain m(−1) has not settled by M56, and at M32 the treatments differ by 0.45
    (corrected D429, verifier 183). So "the same order as
    the resolutions' differences" holds only at node 61, and "neither treatment is the cause on its own" is withdrawn.
    What the two disagree on is a derivative of the metric, not its values: see the D420 bullet below.]
- *M alone does not resolve it (D418; `checks/g1axis5.py --sweep`, computed).* Plain runs at M = 24, 32, 40, 48 and 56,
  800 × 360, r_cut = 0.9 (863-1532 s each), compared on the 182,741 cells all five keep.
  - At the event's node the successive differences |m_M − m_M′| are 0.232, 0.112, 0.0024 and 0.083. The maximum over
    x in that cell is 0.23, 0.17, 0.12 and 0.24. The band maxima over areal radius ≥ 1 on [1.8, 2) are 0.23, 0.17,
    0.12 and 0.49. So there is no convergence in M, and M40's 0.0024 at the node is not representative of the cell.
  - Before v = 1.8 the successive differences grow with M, from 2.0 × 10⁻⁶, 4.6 × 10⁻⁶ and 4.3 × 10⁻⁵ to
    9.0 × 10⁻⁵ on [1.65, 1.8), where an angular truncation error would fall.
  - So at a fixed null grid, raising M degrades the solution: the successive differences grow with M in every band,
    [0.5, 1) included (7.8 × 10⁻⁸, 4.0 × 10⁻⁷, 9.2 × 10⁻⁶, 1.0 × 10⁻⁵, the sweep's output as verifier 183 read it).
    An M-amplified error dominates, for instance D354's axis-node round-off; a null-step error would be shared by the
    runs and cancel in their differences. Whether the null step cures it is the running test ("the null step, not M,
    sets the error", D399, withdrawn D429). D410's
    "barely converges" (M16-M32) is withdrawn as a statement about angle.
  - The test is joint refinement: M = 32 and 40 at 1600 × 720, run in D432 (below).
- *The metric's values at the event, and its axis derivative (D420, corrected D429;
  `checks/g1axis5.py --nodes`, computed).*
  - m enters the metric only through the regular combinations P = (2(1 + x)m − (1 − x)n)/3 and Q (g1geom5.fields).
    Near x = −1 the equations fix only (1 + x) m_uv (dnsolve5.py:30-31). So m's value there is m(−1) =
    (3P′(−1) − n(−1) + 2n′(−1))/2, a first derivative of the metric at the axis, and geometric: it enters the axis
    curvature (g1geom5.py:3-4). Near the axis m enters P with the
    weight 2(1 + x)/3, so a |Δm| there exceeds the change it makes in P by about 140 at the event's node. D410-D418
    measured |Δm|.
  - At the event's node P differs by 2.5 × 10⁻³ between the treatments at M24 (0.05818 plain, 0.06065 reg;
    2.4 × 10⁻³ at node 62), so "agrees to 10⁻³ across treatments" is withdrawn (D429, verifier 183). At x = −1,
    P = −2n(−1)/3 does not contain m, so its values there, 0.0697 and 0.0696 (plain M24, M32) against 0.0707 and
    0.0701 (reg), and 0.0697, 0.0696, 0.0695, 0.0694, 0.0694 over M = 24-56, measure n only.
  - The band maxima of |ΔP| between successive M, over areal radius ≥ 1, are as follows.
    - On [1.8, 2): 5.9 × 10⁻³, 3.0 × 10⁻³, 1.6 × 10⁻³ and 1.6 × 10⁻³ (M24-56). There the decrease has stalled: the last
      two are equal.
    - On [2, 2.25): 3.2 × 10⁻², 4.3 × 10⁻², 5.7 × 10⁻² and 1.1 × 10³. On [2.25, 2.5): 1.1 × 10⁻², 8.2 × 10⁻³, 0.44 and
      1.6. Here it does not converge, and grows with M.
  - So in the metric's values the differences grow sharply with M from [2, 2.25) on, and refining M alone makes them
    worse (D418). Where the failure begins these runs do not fix, since on [1.8, 2) the decrease has stalled ("begins
    at v ≈ 2" withdrawn, D429).
  - The treatments' disagreement in m(−1), 0.45 at M32, is a disagreement in the metric's first derivatives at the
    axis, and plain m(−1) moves by 0.24 from M48 to M56, so the axis treatment matters there. The axis curvature, which
    needs second derivatives, is the invariant to compare
    next.
- *Joint refinement in the metric's values (D432; `checks/g1axis5.py --refine`, computed).* M = 32 and 40 at
  800 × 360 and at 1600 × 720 (the fine runs 3731 s and 4511 s), compared through P on the 186,869 coarse cells all four
  keep. Band maxima of |ΔP| over areal radius ≥ 1.0, on the v-bands [0.5, 1), [1, 1.5), [1.5, 1.65), [1.65, 1.8):
  - halving the null step at fixed M: 2.1 × 10⁻⁶, 1.8 × 10⁻⁵, 2.6 × 10⁻⁵ and 3.8 × 10⁻⁵, the same at M32 and M40;
  - M from 32 to 40 at fixed (u, v): 5.8 × 10⁻¹⁰, 1.3 × 10⁻⁹, 1.7 × 10⁻⁹ and 2.5 × 10⁻⁹ (8.4 × 10⁻¹⁰ to 3.4 × 10⁻⁹
    on the fine grid).
  - So before v = 1.8 the null step sets the error in the metric's values: its differences are 10³-10⁴ times the
    angular ones and do not depend on M. D418's M32-40 difference was measured in m, which near the axis is a
    derivative (D420); in P the M32-40 difference there is 10⁻⁹. Whether D418's larger M40-56 differences are also
    confined to m is not tested (D433).
  - On [1.8, 2) the null-step differences are 3.8 × 10⁻⁴ (M32) and 4.1 × 10⁻⁴ (M40), and the M differences 3.0 × 10⁻³
    and 3.2 × 10⁻³ (coarse and fine): there the error depends on M and not on the null step, and halving the null step
    leaves it unchanged. Over
    areal radius ≥ 1.2 the M differences there fall to 1.5 × 10⁻⁸ and 1.1 × 10⁻⁸, so it is confined to areal radius in
    [1.0, 1.2).
  - From v = 2, over areal radius ≥ 1.0, neither refinement converges (M differences 4.5 × 10⁻²-0.22, null-step ones up
    to
    0.26 at M40). Over areal radius ≥ 1.2 both stay below 2.2 × 10⁻³ up to v = 3 (on [2, 2.25): 2.0 × 10⁻⁴ and
    6.9 × 10⁻⁵).
  - Two grids give no convergence order, and one M pair no trend in M.
- *The amplitude scan (D445; `checks/g1amp5.py`, computed).* The first seed at amplitude A = 1, 7/8, 3/4, 1/2 and 1/4
  (`dnsolve5.py --run 1 0.9 M 800 360 out 0 ld 3 amp A`, D432's options with the amplitude added; at A = 1 the runs
  reproduce D432's bit for bit), M = 32 and 40, compared on the 186,934 cells all ten keep. The background has no
  x-dependence, so P is carried by the waves alone.
  - Band maxima of |P_32 − P_40| over areal radius ≥ 1.0: on [2, 2.25), 0.15, 1.9 × 10⁻³, 7.7 × 10⁻⁵, 2.0 × 10⁻⁸ and 3.5
    × 10⁻⁹ for A = 1, 7/8, 3/4, 1/2 and 1/4; on [3.5, 4.6), 0.22, 2.0 × 10⁻⁴, 5.2 × 10⁻⁶, 2.2 × 10⁻⁸ and 5.6 × 10⁻⁹.
    Before v = 1.8 every amplitude sits at about 10⁻⁹.
  - So at A ≤ 1/2 the angular refinement converges at the 10⁻⁸ level to the end of the grid, the axis x = −1 included
    (cells with areal radius in [1.0, 1.2) reach v = 3 at these amplitudes): there the axis treatment and the scheme are
    sound, although the response is already nonlinear (P/A changes by up to about 20 % of the band maximum between A =
    1/4 and 1/2 on [2.25, 3); D446). The non-convergence rises steeply between A = 1/2 and 3/4 and then like a high power
    of A (local exponents about 20-50).
  - It follows the angular resolution. The relative Chebyshev tail of m and n at M = 40 (the largest of the last four
    coefficients in x over the largest) on [2, 2.25) is 1.0, 6.3 × 10⁻², 8.5 × 10⁻⁴ and at most 2.3 × 10⁻⁶ for A = 1,
    7/8, 3/4 and ≤ 1/2 (about 2 × 10⁻⁴ on [0.5, 1), where the waves switch on); cell by cell it tracks |P_32 − P_40|
    (correlation 0.84-0.98, verifier 191). The angular structure steepens past M = 40 as the amplitude grows. At A = 1
    the largest |P_32 − P_40| on [2, 2.25) sits at x = +0.71; the values on the axis alone tell the same story (D446).
  - So the axis treatment is sound wherever the runs converge, A ≤ 1/2, and D432's failure comes with angular structure
    outrunning M = 40. The scan cannot separate the cases at A = 1: a singularity, which would answer G1 no for the
    record's data; a steep smooth feature; or an axis defect that appears only at large amplitude (any non-convergence
    that grows with M would fill the tail the same way; D446). M = 48 and 56 did not converge either (D418).
  - Without the long-double axis solve the same picture holds on a floor of 10⁻⁶ to 10⁻⁵, and at A = 1 an excursion
    appears, apparently from rounding (|P/A| = 2.1 on [2, 2.25), against 0.32 with ld 3): at full amplitude the option
    matters.
  - *The onset (D458; `checks/g1map5.py --onset`, computed).* At A = 1 the failure starts at the node next to the axis in
    m, the field the metric multiplies by 1 + x there, and becomes a node-to-node alternation growing toward the axis (m
    = 0.44, −0.37, 0.87, −0.65, 1.75, −1.86, 2.27, −28.1 at the eight nodes next to x = −1, v = 2.2, M = 40), its
    Chebyshev spectrum flat to the last coefficient. The tail of (1 + x)m and (1 − x)n, the parts the metric carries,
    jumps from the floor by four to five orders within 0.1 in v at A = 1 (from v ≈ 1.8) and within 0.2 at 7/8 and 3/4
    (from 1.8 and 1.9), a tenfold rise at 2.1 at 1/2, none at 1/4 (D462).
    - *Seed test.* Without the long-double axis solve the rounding at the axis node is about 800 times larger (S4's state
      at M = 32: 4 × 10⁻⁶ against 5 × 10⁻⁹) and the tail's floor 10³-10⁴ times higher. At M = 32 the jump lands in the
      same band at the same level (A = 1: 5 × 10⁻⁶ against 1 × 10⁻⁵ in [1.8, 1.9), both 3 × 10⁻³ in [1.9, 2.0); A = 3/4
      the same through [2.0, 2.2)), so there it is not amplified rounding. At M = 40 it is 100 times higher without, so
      there the long-double solve matters. Halving the null step does not move it (D432).
  - *A mapped angular grid (D458; `dnsolve5.py --run ... map 0.3`, `checks/g1map5.py`, computed).* Nodes concentrated at
    x = −1, the angular spacing there 0.7 times the plain one (as a plain M of 46 and 57 would give), with ld 3 at M = 32
    and ld 4 at M = 40 (the mapped node next to the axis sits closer; its long-double residual on S4's state is 4.6 ×
    10⁻⁸ and 1.4 × 10⁻⁶, the latter with ld 3 or 4 alike and 40 times plain M = 40's 3.3 × 10⁻⁸), at A = 1 and 3/4.
    - The mapped pair's difference is carried by its M = 40 run alone (verifier 197, D462). The mapped M = 32 run tracks
      the plain runs: at A = 1, |P_m32 − P_p40| is 1.6 × 10⁻³ in [1.8, 2) against the plain pair's 3.4 × 10⁻³, and 3.3 ×
      10⁻³ against 3.0 × 10⁻³ in [2, 2.25); at A = 3/4 it is 3.4 × 10⁻³ in [2, 2.25), 17 times the plain pair's but not
      O(1). The mapped M = 40 run departs from v ≈ 1.65 and is O(1) from 1.8 at A = 1 (from 2 at 3/4); it has 40 times
      the axis-node rounding, and the mapped pair's difference peaks near x = +1, the mapped grid's coarser side (1 −
      x_max = 2 × 10⁻³ at M = 32, as a plain M of about 25), not at the axis.
    - Over the four grids the onset tail grows as the first node approaches the axis: 1 + x_0 = 1.2 × 10⁻³, 7.7 × 10⁻⁴,
      5.9 × 10⁻⁴ and 3.8 × 10⁻⁴ (plain 32, plain 40, mapped 32, mapped 40) give tails in [1.65, 1.8) of 3 × 10⁻¹⁰, 2 ×
      10⁻⁹, 2 × 10⁻⁷ and 8 × 10⁻⁵. The same order holds for the axis-node rounding (long-double residuals 4.7 × 10⁻⁹, 3.3
      × 10⁻⁸, 4.6 × 10⁻⁸ and 1.4 × 10⁻⁶), so the two are not separated; plain M = 40 and mapped M = 32 have nearly equal
      residuals but tails 100 times apart, which favours node proximity without establishing it (D462).
    - So the mapped grid does not separate the readings (D462, withdrawing D458's inference): its one failing run is also
      its most rounding-affected, its error sits on the coarser side, and its D2 is about four times the plain grid's
      (2.7 × 10⁵ against 6.4 × 10⁴ at M = 32); the mapped M = 32 run, with the axis spacing of a plain M of about 46,
      converges neither better nor worse. Every alternative found is the scheme's rather than the solution's, but no
      mechanism is shown.
    - The invariant g_22 = R² e^(8n/3) at x = −1, the circle that does not shrink, converges better than P on the plain
      grid: M = 32 and 40 agree to 5 × 10⁻⁴ at A = 1 through [1.8, 2.25) and to 6 × 10⁻⁵ after, against |ΔP| up to 3 ×
      10⁻³ (8.7 × 10⁻⁵ at A = 3/4, in [2.25, 2.5)); on the mapped pair it fails with P.
- *G1, so far.* The double-null gauge passes the place where the record's Bondi chart broke, at both seeds.
  - At λ = 1, over its own kept cells, the computed solution is a converged approximation up to v ≈ 1.65 of 4.5 in
    dnsolve5's gauge (on 𝒟_q, in (u, v) and in angle).
  - On the cells the swapped gauge keeps, a strip below that gauge's cut, it converges in dnsolve5's gauge further: in
    (u, v) at second order in every band, and in angle to v ≈ 3.5 at k = 10, the axis included (D399).
  - In the swapped gauge, on the same cells, the values converge in angle on a strip below the cut whose extent
    depends on how far from the cut one measures. m on the axis x = −1, and with it the axis curvature, does not
    converge beyond v ≈ 2.25 (D393, corrected D395), and the (u, v) error is larger than dnsolve5's from v = 1, up to
    14 times in the section volume (D399, corrected D402 and D405).
  - At the second seed it holds to v ≈ 3-3.5.
  - Beyond, it fails to converge at an axis: at x = −1 for λ = 1 (in both gauges; D391, D399), from areal radius about 1
    near v = 2, with either axis treatment and whatever the cut (D410, corrected D413), and only from an amplitude
    between 1/2 and 3/4 of the record's, with the angular structure outrunning M = 40 (D445-D446), where a grid
    concentrated at the axis does not separate the readings, its one failing run being its most rounding-affected (D458,
    D462); and at x = +1 for the second seed. G1 is not yet answered to the end of the domain.
  - The curvature invariant (D475, corrected D485 and D499; `checks/g1curv5.py`, 24 of the 438 u-rows with R ∈ [1, 1.4];
    on amplitude runs at 800 × 360 without `ld 3`, not on D445's runs as stated: the cached rows match those runs, not
    the `ld 3` ones, verifier 211, D499): the Kretschmann scalar K, assembled from exact Christoffels, against
    Tangherlini's K_0 = 72/R⁸ at the same areal radius (the volume radius of the 3-sphere), at M = 32 and 40 with (u, v)
    held at 800 × 360, so 'converges' means in M, in angle. dev = max |K/K_0 − 1| also carries the rise in mass the
    ingoing wave brings, not only the wave's own curvature. Wherever K converges in M its departure from the background
    is of order 1, growing like A^p with p from 0.58 to 2.22 over the converged bands (near the axis, x = −0.97, dev from
    0.51 at A = 1/4 to 3.9 at A = 1 on v ∈ [1.5, 1.75), the M-difference under 1.3 × 10⁻³ of K_0, which is the floor of
    the linear interpolation between nodes that differ with M, and 10⁻⁶ or less with the Chebyshev interpolant at A = 1,
    D499): on v < 1.75 at every amplitude and on v < 2.25 at A ≤ 1/2, with no resolved growth before the failure (column
    by column, dev at x = −0.97 peaks at 3.3 at A = 7/8 and 4.3 at A = 1 near v = 1.84, and falls before the M-difference
    rises). Convergence is lost at A = 3/4 inside [2, 2.25) (at x = −0.97 K still converges to v = 2.1), at A = 7/8 off
    the axis already on [1.75, 2), and at A = 1 first off the axis, near v = 1.875 to 1.9 at x = 0 and 0.5 and 1.95 to
    1.975 at x = −0.97. These runs and D445's `ld 3` runs agree to three digits on [1.5, 1.75), but not later (D499): at
    A = 1 the `ld 3` runs lose convergence at v = 1.925 to 1.94 at every angle, and off the axis on [1.75, 2) their dev
    is 2.9 to 3.2, against 142 to 226 here (2 to 7 × 10⁶ from v = 2, against up to 1.4 × 10⁵), so 'first off the axis' at
    A = 1 is these runs' and the values past v = 1.75 are not the `ld 3` solution's. Beyond, K is unresolved at every
    angle computed, x = −0.97 to 0.5: values from about 3 K_0 to 10⁷ K_0, with M = 32 and 40 differing by as much, so
    they are not a resolved growth of the curvature. K's angular derivatives are the collocation's, global in x, so this
    neither localises the cause at the axis nor excludes it (at A = 7/8 and 1 the loss begins off the axis): the
    invariant does not tell a singularity from a defect of the scheme, but it shows the failure reaches the geometry, not
    only the gauge functions, and that the curvature is moderate wherever it is resolved in angle; the (u, v) resolution
    was not varied. (A first run read the saved mask, which marks excluded cells, the wrong way round and returned only
    NaN; corrected, b6fb8e7.)
  - The curvature invariant in the null grid (D489, corrected D499; `checks/g1curv5.py --null`, on D432's runs at A = 1,
    M = 32 and 40 at 800 × 360 and 1600 × 720, all with `ld 3`, 24 u-rows of the coarse grid and the same rows of the
    fine one, compared at the coarse nodes). On v ∈ [1.5, 1.75), where K departs from the background by 0.42 to 3.9 (the
    departure at x = −0.97, 3.86, is D475's 3.9 at A = 1: D475's runs lack `ld 3`, but on this band the two agree to
    three digits), K converges in the null grid as well as in angle: the 800 × 360 and 1600 × 720 values differ by 2.5 to
    5.2 × 10⁻³ of K_0 at x = −0.97 to 0.5 (1.0 × 10⁻² at the node next to the axis, x = −0.999), and M = 32 and 40 by 1.3
    × 10⁻⁷ to 1.0 × 10⁻⁶ with the Chebyshev interpolant; D489's 2 × 10⁻⁴ to 1.3 × 10⁻³ was the error of interpolating
    linearly between nodes that differ with M (verifier 211, D499). So there the null step sets the error, by 10³ to 10⁴,
    as D432 found for P; two null grids show agreement, not an order (at second order the coarse grid's error would be
    about 4/3 of the difference, at most 7 × 10⁻³ against departures of 0.42 or more). On [1.75, 2) the angular
    difference (1.4 to 3 of K_0 with any interpolant) dominates the null one (0.045 to 0.74 on these rows, up to 0.99 at
    x = 0 on seven others) at the band maxima, which come from v ≥ 1.95, and is the same at both null grids there to 15
    %; but near the axis the null difference rises first (at x = −0.97 from 4.4 × 10⁻³ at v = 1.75 to 4.7 × 10⁻² at 1.90,
    the angular one staying at or below 1.4 × 10⁻², and on v = 1.825 to 1.875 the fine grid's angular difference 30 to 40
    % below the coarse one's), and the angular difference overtakes it from v ≈ 1.9. So in that band M sets the loss from
    v ≈ 1.9, and before it near the axis the null step does. From v = 2 both are as large as the departure (the null
    difference reaching 1.8 × 10⁵ K_0, at x = 0 on [2.25, 2.5)): unresolved in both. So the finding that the curvature is
    moderate wherever it is resolved, with no resolved growth before the failure, holds under refinement of the null grid
    in D432's `ld 3` runs at the record's amplitude; D475's own runs were not refined.

- *Next.* At λ = 1: the invariant cut is tried (D392) and does not move the limit. Gauges and cuts are compared on the
  cells both keep from now on (`checks/g1cells5.py`, D399), where dnsolve5's gauge is the better solver in (u, v).
  dnsolve5's k-scan and the swapped gauge's fourth grid are done (D403). The axis treatment at small R is now tested
  (D445-D446): at A ≤ 1/2 the runs converge there, and the failure needs more than half the amplitude and comes with the
  angular structure outrunning M = 40; at A = 1 a singularity, a steep smooth feature and a large-amplitude axis defect
  are not yet told apart. On the axis x = −1 the circle that does not shrink, g_22 = R²(1 − x)e^(2Q)/2, has an invariant
  size, so compare it across gauges and resolutions where the runs stop; and recompute x_K and 𝒟_q from this run with a
  stencil that stops at the cut. Candidates for the axis are an axis-adapted variable, a mapped Chebyshev grid
  concentrated at the axes, and a shift condition between the two gauges. The `reg` division of D352 did not cure the
  axis in dnsolve5, either under the drag (D352) or at the event of D410 (D413). A cut experiment cannot separate the
  axis treatment from the geometry (D413). M alone, at 800 × 360, does not converge there and degrades the smooth region
  (D418); refining (u, v) with M does not converge it either (D432). The mapped grid concentrated at x = −1 is tried and
  does not separate the readings: its M = 40 run is dominated by its own axis rounding, its error at its coarser side
  (D458, D462). Next at λ = 1: an axis treatment that does not lose digits near the axis (the regular combinations (1 +
  x)m and (1 − x)n as unknowns, or Gauss-Radau nodes at the axes with the regularity conditions imposed there), then the
  same comparison; and the invariant g_22 at x = −1 followed as A rises to 1 (D458 has it at A = 3/4 and 1). The
  Kretschmann scalar is now followed (D475, D485): moderate and converged in angle up to the failure, unresolved at every
  angle after it (at the two largest amplitudes first off the axis in the runs without `ld 3`; at A = 1 with it, at v ≈
  1.93 at every angle, D499), so an axis treatment must be judged by K's convergence at all angles, not near the axis
  alone. At the second seed, decide whether the steepening at x = +1 is the solution's, by an invariant (the Kretschmann
  scalar along the axis) or by angular refinement concentrated at the axes (a mapped Chebyshev grid). Rounding is
  excluded (D354), and so is the curvature cut. Then F3 (the certified linear constant) on the converged part.

## 7. Sources

- READ: [Wu26] arXiv:2609.08421v1, (1.1) p. 2, Theorems 2.1-2.2 pp. 6-7, the residual formulas p. 12; [CCRT07], [MP11]
  and [RT12] as in ROUTES-OPEN.md section 2.

- Computed: dnull5.py; the timings and the pulse's periods (D337); dnsolve5.py and its runs (D344).

- The record: growth5.py, ROUTES-OPEN.md 2 and 4.3, the paper's section 9.
