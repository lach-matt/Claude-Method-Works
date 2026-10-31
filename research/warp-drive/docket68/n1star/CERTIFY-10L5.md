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
    leaves is 5.3 × 10⁻⁵, against dnsolve5's own 1.0 × 10⁻⁴.
  - *The invariant check (V4, and at the production grid).* The section volume π²∫R³dx is gauge invariant here, since
    the null foliation is the same in both gauges.
    - It agrees between the gauges to 10⁻¹² before the wave arrives (v < 0.5).
    - Later the gap is within each gauge's own (u, v) error, about 10⁻² at 800 × 360, and it falls about 3.5-fold per
      doubling: 1.7 × 10⁻² → 4.8 × 10⁻³ on v ∈ [1, 1.5), 3.5 × 10⁻² → 9.7 × 10⁻³ on [1.5, 2).
  - *λ = 1 at 800 × 360 with `ld 3`, max over 𝒟_q of |Δm| between angular resolutions, per v-band:*

    | v | [1, 1.5) | [1.5, 1.65) | [1.65, 1.8) | [1.8, 2) | [2, 2.5) | [2.5, 3) |
    |---|---|---|---|---|---|---|
    | dnsolve5, M16-M24 | 7.3e-5 | 5.4e-3 | 0.75 | 3.9 | 13 | 10 |
    | dnsolve5, M24-M32 | 1.7e-6 | 3.9e-4 | 0.43 | 3.4 | 12 | 87 |
    | swapped, M16-M24 | 9.6e-4 | 2.7e-3 | 6.3e-3 | 3.0e-2 | 0.53 | 0.60 |
    | swapped, M24-M32 | 7.3e-6 | 2.9e-5 | 4.7e-5 | 2.4e-4 | 0.89 | 1.0 |

    n behaves the same way (swapped M24-M32: 1.6 × 10⁻⁵ on [1.8, 2), 1.7 × 10⁻² on [2, 2.5)).
  - *The drag.* In this gauge the angle is pressed toward an axis by at most e^(−0.92), at x = +1 for v ≈ 2.75.
    dnsolve5's was e^(−13) at x = −1 (`dnsolve5v.py --drift`).
  - *The new limit.* Convergence in angle now holds to v ≈ 2.1 instead of 1.65. |Δm| > 10⁻³ first at v = 2.14,
    u = −1.041, at the axis x = −1. There R = 1.58, outside the horizon, and x_K = 0.001. The M32 Chebyshev tail of m
    there rises from 6 × 10⁻⁸ at v = 1.89 to 3 × 10⁻⁵ at v = 2.14. This is the axis where m drops out of the metric and
    the equations fix only (1 + x) m_uv (D352). So the remaining limit is the axis condition on m, not the drag, and not
    the curvature.
- *G1, so far.* The double-null gauge passes the place where the record's Bondi chart broke, at both seeds. At λ = 1
  the computed solution is a converged approximation on 𝒟_q up to v ≈ 2.1 of 4.5 in the swapped gauge (v ≈ 1.65 in
  dnsolve5's), in (u, v) and in angle; at the second seed, to v ≈ 3-3.5. Beyond, it fails to converge at an axis while
  x_K < 1: at x = −1 for λ = 1 (outside the horizon in the swapped gauge, D386), and at x = +1 for the second seed.
  G1 is not yet answered to the end of the domain.

- *Next.* At λ = 1, the axis condition on m at x = −1: impose regularity of m there in the swapped gauge, by an
  axis-adapted variable or a mapped Chebyshev grid concentrated at the axes. The `reg` division of D352 did not cure
  it in dnsolve5, but there the drag dominated. Then rerun M = 24 and 32. At the second seed, decide
  whether the steepening at x = +1 is the solution's, by an invariant (the Kretschmann scalar along the axis) or by
  angular refinement concentrated at the axes (a mapped Chebyshev grid). Rounding is excluded (D354), and so is the
  curvature cut. Then F3 (the certified linear constant) on the converged part.

## 7. Sources

- READ: [Wu26] arXiv:2609.08421v1, (1.1) p. 2, Theorems 2.1-2.2 pp. 6-7, the residual formulas p. 12; [CCRT07], [MP11]
  and [RT12] as in ROUTES-OPEN.md section 2.

- Computed: dnull5.py; the timings and the pulse's periods (D337); dnsolve5.py and its runs (D344).

- The record: growth5.py, ROUTES-OPEN.md 2 and 4.3, the paper's section 9.
