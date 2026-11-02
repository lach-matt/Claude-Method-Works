# Existence at the prescribed wavelength 10 l5: the second zero, the certified step, the late region

*Status.* A result note to `CERTIFY-10L5.md` (which it does not edit), begun 2026-11-02. Labels as in the record:
**deduced** (a proof from stated hypotheses, its exact identities checked by a program), **computed** (floating point,
not certified), **certified** (interval or ball arithmetic), **READ**. Programs are in `checks/`, each with its `.out`
and a negative control that must fail. Runs are double-null runs of `dnsolve5.py`, made by `checks/szrun5.py` and
stopped at v = 2 (section 4); "seed 1" is μ0 = 100 l5² (λ = 1 in units of √μ0), "seed 2" is μ0 = 1000 l5² (λ = 1/√10).

## 0. Answers

1. **The second zero is not a second marginally trapped surface.** It is the loss of trapping of the *Bondi chart's
   areal spheres*, which are tilted against the null foliation, while the double-null leaves inside the seed's
   horizon stay outer trapped (negative outgoing expansion at every point).
   - *Deduced (D1, D2):* in any smooth vacuum solution with the record's data in `dnsolve5`'s double-null gauge,
     every leaf with u > −1 has negative outgoing expansion at every point, for as long as the solution exists in
     that gauge. No section of an ingoing cone whose expansion is ≥ 0 at its innermost point has that point at
     u > −1. In particular this holds for every T²-invariant MOTS section (a marginally outer trapped surface that
     is a T²-invariant section of an ingoing cone; corrected in round 2, section 6).
   - *Computed:* the leaves' expansion has one zero per angular node along every ingoing cone of the converged
     region. Every T²-invariant MOTS section of the exact solution on that cone is then confined to a band of width
     0.003–0.007 in u at
     areal radius 1.01–1.05 (seed 1, v ≤ 1.75).
   - *Computed (seed 1):* the Bondi spheres rebuilt from the double-null solution reproduce `growth5.py`'s zero
     structure: the dip of the outer zero, and angular columns with no zero at all on r ≥ 0.64 from v ≈ 1.40
     (`growth5`: 1.419), 28 % of the columns at v = 1.50 against 29 % (counts over unlike radii and columns; at one
     radius the band edges agree within a column spacing to v = 1.525, section 6.1, V3). As the data cone moves out,
     R0 = 10, 20, 40,
     the largest difference of the rebuilt outer zero from `growth5`'s falls from 0.081 to 0.031 to 0.020 (400 rows),
     and from 0.110 to 0.051 at 800 rows (R0 = 10, 20; round 2), while the leaves' own zero stays 0.22 away. But at
     fixed R0 it grows from 400 to 800 rows at v ≥ 1.3 (0.025 → 0.051 at R0 = 20, v = 1.375): the fall with R0 is
     shown at two resolutions, the agreement itself only to v ≈ 1.2 (0.011 at 800 rows, R0 = 20; section 6.1, V2).
     At seed 2 the rebuild does not reach the radii (≤ 0.3) where `growth5`'s second zero sits (section 1.4).
   - *Computed:* the double-null "second zero of R_v" (CERTIFY-10L5.md D344, v = 1.425 at cut 0.54, location not
     recorded) is numerical wherever it lies at u > −1, by D1. In the runs here (cut 0.3) every further zero of R_v up
     to v = 1.8 lies at u > −1 within Nu/40 rows of the cut, at alternate angular nodes, for one or two columns.
2. **Certified, a first step.** For an explicit approximant of the characteristic data on the data cone u = −10,
   the Raychaudhuri constraint holds to a certified bound (Arb), at both seeds (section 2.1).
   - The full residual of a smoothed three-dimensional approximant is *computed* only: 2.5 × 10⁻³ of the curvature
     scale, second order in the grid.
   - **No existence theorem beyond the region where the solution is the seed itself is proved.**
   - The exact obstruction is mathematical, not one of precision. There is no linear estimate with explicit
     constants for the characteristic problem in the class (CERTIFY-10L5.md F5). [Wu26] Theorem 2.2's threshold
     ε(C0) is implicit. So no residual, however small, closes a Newton–Kantorovich argument (section 2.3).
     [Round 2, section 6.2: sharpened. In the formulation the record evolves no linear estimate exists in any Sobolev
     scale, since its principal symbol has a Jordan block.]
3. **The late region is not classified.**
   - *Computed:* from v ≈ 1.65 at seed 1 (M = 16; smaller but still of order one at M = 24) the computed fields
     violate the Raychaudhuri constraint by the size of its own terms. Away from the cut they also violate D1's exact
     monotonicity. So they are not an approximation of any vacuum solution there.
   - *Computed:* the gauge indicators stay moderate (|W| ≤ 1.25, |P + Q| ≤ 0.15). So the failure is not a caustic of
     the outgoing cones, nor a collapse of the lapse.
   - Kretschmann blow-up against a smooth steep feature remains undecided (section 3).
   - [Round 2, section 6.4: at M ≥ 32 the Raychaudhuri violation converges at second order in the null step to
     v ≈ 1.9 at areal radius ≥ 1.0. The onset at v ≈ 1.65 was M = 16's angular resolution.]

## 1. The second zero

### 1.1 Two different second zeros

The record names two "second zeros", and they are different objects.

- *(a) `growth5.py`'s.* `growth5` counts the zeros of T, the outgoing expansion of the spheres {v, r} of its Bondi
  chart, along each Bondi column. A column has a fixed angular label, constant along the ingoing generators and set
  at past null infinity, and r varies along it. The breakdown is a second zero held over 0.01 in v: from v = 1.50 at
  seed 1 and 1.583 at seed 2. The breakdown time was measured at one angular resolution, Nx = 16 (section 1.5).
- *(b) CERTIFY-10L5.md D344's.* There R_v, the outgoing expansion of the double-null leaves S_{u,v}, acquired a second
  zero at v = 1.425 along an ingoing cone at a fixed node.

A *marginally trapped surface* (MOTS) of the ingoing cone C_v is a section on which the outgoing expansion vanishes
identically. Neither zero set is one.

### 1.2 Two deductions

The metric is `dnsolve5`'s:

    g5 = −4 e^{2W} du dv + Gx (dx − β du)² + R²(1+x)/2 e^{2P} dφ1² + R²(1−x)/2 e^{2Q} dφ2²,
    β = (1 − x²) s.

The leaves have volume density R³/4. ∂_v is their outgoing null normal, and its integral curves, with (u, x, φ) fixed,
are the outgoing generators. On the first cone v = 0 (Tangherlini, u := −r) the data are R_v = (1 − 1/R²)/2 and
e^{2W} = 1/2.

**D1 (deduced; the identity computed exactly, `checks/sectexp5.py` X1).** Exactly,

    Ric_vv = −(3/R)(R_vv − 2 W_v R_v) − (P_v² + Q_v² + (P_v + Q_v)²),

with no shift and no angular derivative. So in vacuum ∂_v(e^{−2W} R_v) ≤ 0 along every outgoing generator.

*Consequence.* In any smooth vacuum solution with this data in this gauge, e^{−2W} R_v(u, v, x) ≤ 1 − 1/u² < 0 for
u ∈ (−1, 0). Every leaf with u > −1 is outer trapped: its outgoing expansion is negative at every point, for as long as
the solution exists in this gauge. (The ingoing expansion is not used here.)

*Control.* With 2W_v replaced by W_v the identity fails.

**D2 (deduced; the identity computed exactly, `checks/sectexp5.py` X2).** Take a T²-invariant section S of C_v, given
as u = U(ξ), x = X(ξ). Its future outgoing null normal is

    l = ∂_v + a ∂_u + c ∂_x,

with a ≥ 0 and the explicit a, c of X2, and its expansion θ_S is X2's formula.

*The identity.* Where S is tangent to a leaf (U' = 0):

    θ_S = 3R_v/R + 2 e^{2W} U''/Gx.

Coordinate-free, at a critical point of U this is θ_S = θ_leaf + 2e^{2W} Δ_S U. It also holds at an axis, where every
smooth T²-invariant function is critical.

*Checks.* Exact in X2 (a)–(c): the leaf, the tangent point, and invariance under reparametrisation. In X3 the
formula agrees with an independent embedding computation in five-dimensional Minkowski space to 7 × 10⁻⁸. The
controls are the formula without the derivative of l along S, and the leaf's expansion in place of θ_S; both fail, by
0.80 in X3.

*Consequences.*
- At the innermost point p of S (where U is largest), θ_S(p) ≤ θ_leaf(p).
- At the outermost point q, θ_S(q) ≥ θ_leaf(q).
- With D1: no section with θ_S ≥ 0 at its innermost point has that point at u > −1.
- A T²-invariant MOTS section of C_v has θ_leaf ≥ 0 at its innermost point and θ_leaf ≤ 0 at its outermost point. So
  it lies between the
  least and the greatest u of the leaves' zero set on C_v. This is the double-null form of `hf_mirror5.py` X10's
  remark for the Bondi slices.

**What D1–D2 assume.** A smooth vacuum solution in this double-null gauge on the region considered. That is the
existence question itself, so D1–D2 are statements about the exact solution wherever it exists, not an existence
result.

### 1.3 The leaves in the runs (computed, `checks/secondzero5.py` S1–S2)

The runs are at seed 1, cut 0.3: 200 × 90, 400 × 180 and 800 × 360 at M = 16, and 800 × 360 at M = 24. There are
two at seed 2, cut 0.18. Results are in `checks/secondzero5.out`.

- **S1.** On v ≤ 1.8, every kept cell with u > −1 and at least Nu/40 rows from the cut has R_v < 0, in all eight runs.
  The violations of D1 all lie within Nu/40 rows of the cut: at seed 1, 12, 22 and 253 cells at 200, 400 and 800 rows
  (M = 16) and 195 at M = 24; at seed 2, 25 and 20. That band is excluded, not converging: the largest excess of R_v
  over D1's bound there grows with resolution, 1.3, 4.9 and 9.0 × 10³ at 200, 400 and 800 rows (round 2, V7).
  - *Control.* The same test over u > −1.02 fails, in every run.
  - *Beyond v = 1.8.* At seed 1, 800 × 360, there are 1,822 far violations on (1.8, 2] at M = 16 and 441 at M = 24,
    from v ≈ 1.9: the unconverged region of section 3. At seed 2 there are none far from the cut.
- **S2.** Every second or further zero of R_v along an ingoing cone at a node, for v ≤ 1.8, lies at u > −1 within
  Nu/40 rows of the cut, in all eight runs. At seed 1 they first appear at v = 1.65, 1.525, 1.65 and 1.64 (200, 400,
  800 rows, and M = 24), at alternate angular nodes, for one or two columns. By D1 none is the exact solution's.
  - *Control.* Applied to the first zero, the classifier must place it away from the cut, and it does.
- **The band.** The leaves' one zero per node, the marginal leaf, lies at
  - seed 1 (800 × 360, M = 24): u ∈ [−1.0070, −1.0035] and areal radius at the node 1.013–1.024 at v = 1.5;
    [−1.0121, −1.0056] at v = 1.75; M = 16 agrees to 3 × 10⁻⁵ in u;
  - seed 2 (M = 16): [−1.0029, −1.0014] at v = 1.5 and [−1.0080, −1.0036] at v = 1.9.

  By D2 every T²-invariant MOTS section of these cones lies in that band, near areal radius 1.01–1.05. The Bondi
  second zero sits near the
  excision radius 0.54–0.57 (seed 1).

### 1.4 The Bondi spheres rebuilt from the double-null solution

(computed, `checks/bondisph5.py`, `checks/secondzero5.py` S3–S5)

**The rebuild.**
- On C_{v_j}, `dnsolve5`'s ingoing generators obey dx/du = β. Their labels ξ are their angles on the data cone
  u = −R0.
- The areal radius in those labels is R_B = R (∂x/∂ξ)^{1/3}, and ∂x/∂ξ is carried along each generator.
- The sphere R_B = r is the section U(ξ), X(ξ), and θ is X2's formula.
- *S3.* On the seed (v = 0.3) the rebuilt spheres are the leaves (|X − ξ|, |U − Ū|, |θ − 3R_v/R| ≤ 2.4 × 10⁻⁹).

**The outer zero against `growth5`'s own record (S4).** The record is `data/growth5_runs.json`, run
L100_lam1_28x16_d0_y1.6, whose exterior is its data's until its breakdown at 1.41. Max |r_AH(double null) −
r_AH(growth5)| over growth5's 17 columns:

| v | 200, R0 = 10 | 400, R0 = 10 | 800, R0 = 10 | 800, M = 24, R0 = 10 | 400, R0 = 20 | 400, R0 = 40 |
|---|---|---|---|---|---|---|
| 1.0 | 0.005 | 0.004 | 0.004 | 0.004 | 0.002 | 0.002 |
| 1.2 | 0.026 | 0.029 | 0.024 | 0.024 | 0.018 | 0.008 |
| 1.3 | 0.054 | 0.076 | 0.051 | 0.051 | 0.021 | 0.017 |
| 1.35 | 0.052 | 0.068 | 0.082 | 0.082 | 0.031 | 0.015 |
| 1.375 | (1.35) | 0.081 | 0.110 | 0.110 | 0.025 | 0.020 |

M = 16 except where stated. The 200-row grid has no column at 1.375 (its nearest is 1.35). S4's per-run threshold of
0.1 therefore fails on the two 800 × 360 runs at v = 1.375; the truncation test S6 below is the criterion that
matters. `checks/secondzero5.out` accordingly ended in FAILURES three times in round 1: S4 on the two 800-row seed-1
runs, and S4 at seed 2, where its control passes. S1–S3 pass in all eight runs. [Round 2, V4: S4 is now report-only
and S6 is the gate; the regenerated `secondzero5.out` carries no S4 verdict, section 6.1.]

- **What the difference is.** At fixed R0 = 10 the difference does not fall with resolution: it is 0.081 and 0.110 at
  v = 1.375 on 400 and 800 rows, and M = 24 changes nothing to three digits. At fixed resolution it falls by a factor
  1.5–4 at every v ≥ 1.2 when the data cone moves from R0 = 10 to 20, and further at R0 = 40: 0.081, 0.031 and 0.020
  at worst (S6, `checks/secondzero5_trunc.out`, PASS; its control, the leaves' expansion, stays at 0.22).
- *Measured in round 2 (section 6.1, V2):* R0 = 20 on the 800-row grid. The difference falls from R0 = 10 to 20 by
  2.0–2.3 at every v ≥ 1.2 there too, but at R0 = 20 it also grows from 400 to 800 rows at v ≥ 1.3 (0.021 → 0.027,
  0.031 → 0.036, 0.025 → 0.051): at v ≥ 1.3 the remaining difference is not resolved in (u, v).
- *Why.* `dnsolve5` places only the leading Bondi term of the wave on u = −R0 (m = y³G/2, n = y³F/2), and labels by
  the angle there, not at past null infinity. So the remaining difference is the truncation of the data, a property of
  the two problems, not of either scheme.
- **The dip itself is reproduced.** For example, at v = 1.375 and x = cos(10π/16) the outer zero is 0.759 in
  `growth5`, 0.722 (R0 = 10, 400) and 0.765 (R0 = 20).
- *Control.* The leaves' expansion 3R_v/R taken at the same points disagrees with `growth5` by 0.18–0.22: the tilt
  is what makes the Bondi spheres' expansion.

**The untrapped columns (S5).**
- *`growth5`.* Its standard run, re-run with every zero recorded (`checks/g5zeros5.py`, 20 × 16; breakdown 1.5,
  reproducing the pinned value, `checks/g5angle5.py` A1, A3):
  - at v = 1.4355 the columns x = −0.383 and −0.556 already have no zero on r ≥ 0.54: T > 0 along the whole column;
  - the untrapped band widens toward x = −1: x ∈ [−0.83, −0.20] at v = 1.49, and every column x ≤ −0.195 at 1.548;
  - the pinned "second zero" is the pair of zeros at the band's edge, e.g. (0.556, 0.664) at x = −0.707, v = 1.452,
    and (0.566, 0.858) at x = −0.924, v = 1.500. Those are the inner zero rising from the excision boundary and the
    outer zero falling, before they meet.
  - W at the boundary turns positive only at 1.516, so the outflow premise outlives the first wholly untrapped column
    by 0.08 in v.
- *The double-null rebuild (800 × 360, R0 = 10, M = 16), over r ≥ r_min, the least radius reachable before the cut:*
  - columns with no zero first appear at v = 1.40 (r_min = 0.64; none at 1.35);
  - there are 4, 6, 9 and 13 of 32 at v = 1.425, 1.45, 1.50 and 1.55, spreading toward x = −1.
- *The same count in `growth5`'s run over the same radii, r ≥ 0.64:*
  - the first column with no zero is at v = 1.419;
  - there are 2, 2, 5 and 8 of 17 at v = 1.427, 1.452, 1.500 and 1.548.
- *Comparison.* The fractions agree: 28 % and 29 % at v = 1.50, 41 % and 47 % at 1.55. The onset is at most 0.02 earlier
  in the double-null rebuild, whose R0 = 10 dip is the deeper one (see S4). [Round 2, V3: these counts are not over
  the same radii (the rebuild reaches r = 0.71 only at v = 1.50) nor the same columns (32 against 17); S7 compares
  the bands at one radius on growth5's 17 columns, section 6.1.]
- The excision radius 0.54 itself is not reached before the cut at these grids. Over r ≥ 0.54 `growth5`'s first
  zero-less column is at v = 1.4355.
- *Seed 2 (M = 16, 400 × 180 and 800 × 360).*
  - The rebuilt outer zero agrees with `growth5`'s deep run L1000_lam0.3162_20x16_d0_y2.2 to 0.002–0.003, 0.007,
    0.011–0.012, 0.018–0.020, 0.022–0.023 and 0.026–0.027 at v = 1.0, 1.2, 1.3, 1.4, 1.45 and 1.5.
  - But there S4's control passes: the leaves' expansion is within 0.070. Before v = 1.5 the tilt is too small at
    seed 2 to separate the two, so S4 is not informative there and is recorded as FAIL.
  - At 400 rows, columns with more than one zero of θ (inner zeros at r = 0.63–0.79) appear from v = 1.575. At 800 rows
    there are none through v = 1.625, over r ≥ 0.51–0.57, which includes those radii. So the 400-row ones are the
    coarse grid's, near its cut.
  - `growth5`'s second zero at seed 2 holds from v = 1.583 at its excision radius 0.30; its deeper run shows inner
    zeros at r = 0.21–0.27 from v = 1.524. The rebuild does not reach r < 0.5 there, so at seed 2 the second zero is
    neither reproduced nor contradicted. At 800 rows, max θ on the innermost reachable sphere rises to −0.09 at
    v = 1.625.

### 1.5 `growth5` cannot be refined in angle at its own step (computed, `checks/g5angle5.py` A1–A2)

`growth5`'s step is fixed by the radial grid alone: dv = min(λ/8, 2 dy/speed).
- At Nx = 24 and 32 (Ny = 20) that step is unstable in angle on the seed itself, before the wave arrives:
  - K_all, which vanishes on the seed (5.6 × 10⁻¹¹ at Nx = 16), grows by about 2.5–3 per step at Nx = 24 and about
    36 per step at Nx = 32;
  - the solve fails at v = 0.34 and 0.08, and `breakdown()` reports 0.32 and 0.08.
- So the record's breakdown times, "three grids agreeing", are three radial grids at one angular resolution.
- A run at Nx = 24 with the step reduced (`g5zeros5.py ... cfl 0.7`, 2.9 times as many steps) was started and stopped
  unfinished: it had not reached v = 0.25 in about an hour on the shared machine. So `growth5`'s convergence in angle
  remains untested; the step it needs at Nx = 24 is not known.

### 1.6 Verdict on priority 1

- *(b) is numerical:* in every run here it lies at u > −1, where it violates D1, and it sits at the cut. D344's own
  instance was not located, so that one is classified by this pattern, not measured.
- *(a) is the Bondi spheres' own:*
  - two independent formulations and gauges give the same zero structure, and they converge on each other as the
    data truncation is removed;
  - the double-null leaves inside stay outer trapped (D1);
  - any T²-invariant MOTS section lies in a thin band at areal radius ≈ 1.01–1.05 (D2 and S1–S2).
- So (a) is physical as a property of those particular surfaces and of the Bondi chart's excision premise. It is not a
  second marginally trapped surface, and it is no obstruction to existence. It obstructs only the Bondi chart.
- The paper's "round spheres inside the seed's horizon cease to be trapped ... the direction of the untrapping is not a
  measurement of these runs" can now be read precisely. The untrapping is of the areal spheres of the Bondi slicing;
  the outer-trapped leaves inside persist.
- *What is not shown:*
  - convergence of the rebuilt Bondi spheres down to the excision radius 0.54 (the cut stops the rebuild at r_min ≈ 0.64
    at v = 1.4);
  - `growth5`'s own convergence in angle (section 1.5).

## 2. Toward a computer-assisted proof

### 2.1 Certified: the Raychaudhuri constraint on the data cone (`checks/cdata5.py`)

**Along the data cone u = −10.** r is a smooth parameter with
v(r) = 2(r − 10) + ln(11(r − 1)/(9(r + 1))) exactly, W_v = 1/(2r³), and the constraint reads

    R_rr = −(4/(3f²)) R s,   f = 1 − 1/r²,
    s = P_v² + Q_v² + (P_v + Q_v)²,
    Ric_vv = −(3/R)(f/2)² R_rr − s.

**The approximant.** R_app is
- R = r for v ≤ 1/2;
- a tensor Chebyshev series in (r, x) on v ∈ [1/2, 7/2], degrees 40 × 28 at seed 1 and 64 × 28 at seed 2, fitted to a
  floating-point solution and corrected by an affine function of r to match R = r, R_r = 1 at v = 1/2;
- its affine continuation for v ≥ 7/2, which solves R_rr = 0 exactly.

So Ric_vv[g_app] = 0 exactly outside [1/2, 7/2].

**The certificate.** On a grid of boxes in (r, x), the mean-value form in Arb balls:
- the value at the box centre;
- plus the gradient, enclosed over the box by forward-mode jets, times the half-widths;
- Chebyshev polynomials over an interval enclosed by Markov's inequality.

| seed | boxes | certified sup \|Ric_vv[g_app]\| | certified sup s | certified at the box centres |
|---|---|---|---|---|
| 1 | 192 × 64 | 4.97 × 10⁻⁵ | 1.20 × 10⁻³ | 6.6 × 10⁻¹¹ (12,288 points) |
| 2 | 288 × 64 | 2.28 × 10⁻⁵ | 5.28 × 10⁻⁴ | 1.8 × 10⁻¹⁰ (18,432 points) |

*The bound's order.* The mean-value enclosure is of second order in the box size: halving both widths divided the
bound by 4.0, 8.4 × 10⁻⁴ → 2.1 × 10⁻⁴ at 48 × 16 → 96 × 32. So the certified sup lies far above the residual itself,
which the certified point values at the centres show.

*Reading.* The certified sup is 4.1 % (seed 1) and 4.3 % (seed 2) of the terms that cancel in Ric_vv. The certified
values at the box centres are 10⁻¹¹–10⁻¹⁰: the fit's own residual.

*Control.* Perturbing the fitted coefficients by 10⁻⁶ must raise the bound a hundredfold. It raises it to 465 (seed 1)
and 4,259 (seed 2). `checks/cdata5.out`: all checks pass.

*What this is.* A certified constraint residual (corrected in round 2 from "data error") for the Raychaudhuri
constraint of the record's truncated characteristic
problem (data on u = −10, not at past null infinity). The constraint Ric_vx, which fixes the shift on that cone, is not
certified.

### 2.2 Computed: the residual of a smoothed approximant (`checks/resid5.py`)

**The box and the approximant.**
- The box: u ∈ [−4, −1.1], v ∈ [0.55, 1.6], x ∈ [−1, 1], outside the seed's horizon generator. It is converged in
  (u, v) and angle by CERTIFY-10L5.md D399–D432, and S1 here.
- The approximant: per angular node, a tensor Chebyshev least-squares fit in (arcsinh((u + 1)/a), v), degrees
  24 × 30, to the 800 × 360 run (fit error ≤ 7 × 10⁻¹¹), and the run's own interpolant in x.

**The residual.** All eight nonzero Ricci components, in the null-orthonormal frame (l = ∂_v, n̂, e_x, e_φi), at the
midpoints of the run's cells. Max over the box of |Ric| / √K_0, where √K_0 = √72/R⁴:

| run | ll | ln | nn | lx | nx | xx | 11 | 22 |
|---|---|---|---|---|---|---|---|---|
| 800 × 360 | 2.5e-3 | 1.5e-4 | 7.5e-5 | 4.3e-4 | 2.5e-5 | 2.0e-4 | 6.2e-5 | 2.1e-4 |
| 400 × 180 | 9.6e-3 | 5.9e-4 | 2.9e-4 | 1.7e-3 | 8.7e-5 | 7.8e-4 | 2.4e-4 | 8.3e-4 |

- *What it measures.* The ratio is 3.92: the residual is the scheme's second-order (u, v) error. The largest component
  is Ric(l, l) = Ric_vv, the one constraint the scheme never imposes.
- *Control.* A lapse off the solution (W + 0.01 v) gives a residual 140 times larger.

### 2.3 What blocks a Newton–Kantorovich argument: the exact obstruction

The a-posteriori route (CERTIFY-10L5.md sections 1, 2(d), 4) needs four certified ingredients on a domain:
1. the residual ε in the norm the nonlinear step controls (L^∞_u L^∞_v H^s(S) with s ≥ 3 in [Wu26] Theorem 2.2, READ
   there);
2. the data error δ;
3. the constant F of a linear estimate for the linearised characteristic problem about g_app;
4. the quadratic constant G;

with δ + ∫ε < 1/(4 G T F²). Their state:

- **(3) and (4) do not exist as theorems with explicit constants.** This is the obstruction.
  - [Wu26] Theorem 2.2 (READ, CERTIFY-10L5.md section 1) gives the structure. Its threshold ε(C0) and constant C(C0)
    are not explicit, its proof is a sketch, and it is in 3 + 1 dimensions.
  - The five-dimensional version in the class, F5 of CERTIFY-10L5.md's plan, is not written.
  - Without it no residual, however small, closes. The obstruction is the missing theorem, not precision.
- **(1) is computed, not certified, and is far from its target.**
  - In L^∞ of frame components it is 2.5 × 10⁻³ of the curvature scale on the box of section 2.2.
  - The closing condition demands 6 × 10⁻⁴ at F = 2 and 9 × 10⁻⁶ at F = 17 (G = 10, T = 10; CERTIFY-10L5.md 2(d)).
  - Certifying it in three dimensions costs more than here. The 2D certificate of section 2.1, with a mean-value form
    of second order in the box size, needed 12,288 boxes to bound one component with a short explicit expression
    to 4 % of its terms. The 3D residual has eight components, each of them a larger expression than
    Ric_vv's, over three variables instead of two. A certificate tight enough would need third-order Taylor models,
    not the mean-value form.
- **(2)** is certified only for one constraint on one data cone (section 2.1), and for the truncated problem: the data
  on u = −10, not at past null infinity (G3).
- **The domain.** Even with (3)–(4) in hand, the approximant exists only where the numerics converge:
  - at seed 1, on the kept cells to v ≈ 1.65 (constraint convergence here, section 3), and on strips below the cut to
    v ≈ 3.5 (CERTIFY-10L5.md D399);
  - at seed 2, to v ≈ 3.5 at M = 32–40 away from M = 48's mask (D601).

  Neither covers D_T.

### 2.4 The theorem that is proved

**Nothing beyond the exact region is proved.** On the part of D_T where the solution is the seed itself (before the
shell, v ≤ v_start, the record's own result) existence is trivial, and no larger domain is reached.

What is proved (deduced) is conditional and structural. Wherever a smooth vacuum solution with the record's data exists
in `dnsolve5`'s double-null gauge:
- every leaf inside the seed's horizon generator (u > −1) is outer trapped at every point (D1);
- every T²-invariant MOTS section of an ingoing cone has its innermost point at u ≤ −1 (D2).

## 3. The late region (computed, `checks/late5.py`)

The runs are seed 1 at M = 16, 200 × 90, 400 × 180 and 800 × 360, and 800 × 360 at M = 24 for L4, compared per
v-band over kept cells at least Nu/40 rows from the cut.

- **L1, the Raychaudhuri constraint.** ρ := R_vv − 2W_v R_v + (R/3)(P_v² + Q_v² + (P_v + Q_v)²) = −(R/3) Ric_vv is
  never imposed by the scheme.
  - Max |ρ| at the three grids, with ratios:
    - [0.5, 1): 6.8e-3, 2.2e-3, 6.0e-4 (3.2, 3.6);
    - [1, 1.5): 0.135, 0.044, 0.013 (3.1, 3.4);
    - [1.5, 1.65): 0.67, 0.26, 0.064 (2.6, 4.0);
    - [1.65, 1.8): 2.6, 2.6, 3.2 (1.0, 0.8);
    - [1.8, 1.9): 4.4, 13.8, 14.9;
    - [1.9, 1.975): 5.4, 31, 55.
  - Against the largest term on the fine grid: 9.1, 21 and 55 on the last three bands. From v ≈ 1.65 the residual is
    the size of the terms themselves and grows with resolution.
  - *Control.* With W_v in place of 2W_v the residual does not converge on any band.
- **L2, D1's monotone quantity.** The largest increase of e^{−2W} R_v along a generator, relative to its size:
  - 1.3 × 10⁻¹¹ on [0.5, 1) and 1.3 × 10⁻⁴ on [1, 1.5);
  - 0.18 on [1.65, 1.8), 12 on [1.8, 1.9) and 58 on [1.9, 1.975).
- **L3, gauge indicators.** Max |W| is 0.49, 0.87, 1.03, 1.22, 1.25 and 1.25 per band. P + Q ∈ [−0.149, 0.088].
  - Gx ~ e^{−2(P+Q)} does not approach zero, so no caustic of the outgoing cones is forming. The lapse e^{2W} stays
    below 25 times its value on the first cone (e^{2W} = 1/2 there), the growth Tangherlini's own interior shows
    toward the cut.
  - The failure is therefore not a breakdown of the double-null gauge visible in its own functions.
- **L4, the angular resolution.** At 800 × 360, M = 24 against M = 16, max |ρ| on [1.65, 1.8), [1.8, 1.9) and
  [1.9, 1.975) is 1.84, 8.4 and 13.5 against 3.19, 14.9 and 55. It is smaller at the finer angular grid, but stays of the
  order of the terms. The maximum on [1.65, 1.8) is at u = −0.978, x ≈ −0.85, areal radius at the node 0.80, v = 1.79,
  at both M: inside the seed's horizon generator, toward the axis x = −1 where the record's angular failure begins
  (D351–D418).
- **What this classifies.** From v ≈ 1.65 (M = 16; M = 24–40 move the angular onset to 1.65–1.93, CERTIFY-10L5.md
  D418–D499) the computed fields are not an approximation of a vacuum solution in this gauge. They violate an identity
  that every vacuum solution satisfies (Ric_vv = 0) and an inequality that it implies (D1).
  - *Not shown:* whether the exact solution has a curvature singularity there or a smooth feature finer than the grids.
    Neither K nor these invariant-free tests separate the two.
  - Both readings must reconcile with D1–D2 and with K being moderate (≤ 4 K_0) wherever it converged (D475–D601).
  - **Still open.**

## 4. Files, runs and outputs

| file | what |
|---|---|
| `checks/sectexp5.py`, `.out` | X1–X3: Raychaudhuri identity, the section-expansion formula, the Minkowski check |
| `checks/bondisph5.py` | library: the Bondi spheres rebuilt from a double-null run |
| `checks/secondzero5.py`, `.out` | S1–S5 on every run below |
| `checks/secondzero5_trunc.out` | S6: the data truncation, R0 = 10, 20, 40 |
| `checks/szrun5.py` | driver: `dnsolve5.run` stopped at v = 2; options `ld`, `amp`, `R0`, gauge; singular cells masked |
| `checks/g5zeros5.py` | driver: `growth5.run` with every zero recorded, written to scratch; option `cfl` |
| `checks/late5.py`, `.out` | L1–L4 |
| `checks/g5angle5.py`, `.out` | A1–A3: `growth5` re-run, its angular instability, its zero-less columns |
| `checks/resid5.py`, `.out` | Q1–Q2: computed residual of a smoothed approximant |
| `checks/cdata5.py`, `.out` | C1: certified Raychaudhuri constraint on the data cone |

**Runs.** These are scratch runs, not committed. All use `ld 3`, cut 0.3 at seed 1 and 0.18 at seed 2, v to 2.0.
- Seed 1, `python3 checks/szrun5.py 1 0.3 M Nu Nv 2.0 OUT ld 3 [R0 r]`:
  - M = 16 at (Nu, Nv) = (200, 90), (400, 180) and (800, 360); 102 s, 272 s, 600 s;
  - M = 24 at (800, 360), 2,175 s;
  - M = 16 at (400, 180) with R0 = 20 and 40, 639 s and 678 s.
- Seed 2: λ = 0.316228 at M = 16, (400, 180) and (800, 360).
- `growth5`: `python3 checks/g5zeros5.py 100 1 20 Nx 1.56 OUT` at Nx = 16 (1,201 s), 24 and 32; Nx = 24 with
  cfl 0.7 not completed.

*Timings.* The times are wall times on a shared machine.

## 5. Next step

[Round 2: superseded by section 6.6.]

1. **F5 first.** Write the linear estimate for the linearised double-null system in the class with explicit constants
   (energy on characteristic rectangles, Sobolev on the 1D orbit sections, in the axis-regular variables). Until it
   exists, no amount of certified residual decides existence (section 2.3).
2. **For the certificate itself.** Third-order Taylor models in place of the mean-value form; and Ric_vx on the data
   cone, then the data at past null infinity (G3).
3. **For the late region.** A run that imposes or damps the Raychaudhuri constraint (or a constraint-preserving
   formulation), to see whether the onset at v ≈ 1.65–1.9 moves. A fixed point of the onset under refinement would point
   to the solution; a moving one to the scheme.

## 6. Round 2 (2026-11-02): F5, the certified residual, the late region

*Status.* Appended 2026-11-02 after an independent verifier read round 1 at commit 169c9b5. Labels as in section 0.
Sections 0–5 above were corrected in place where the verifier found them wrong, each correction marked "round 2"; the
findings and their dispositions are in 6.1.

### 6.0 Answers

1. **F5. No linear estimate with explicit constants is had. The reason is now proved, not only observed.**
   - *Deduced (exact, `checks/symbol5.py`).* In the formulation the record evolves (dnsolve5's rows Ric_11, Ric_22,
     Ric_xx, Ric(Y, ∂_v)), the linearised principal symbol has a 2 × 2 Jordan block at the eigenvalue 0.
     - Its frozen-coefficient characteristic problem has solutions growing like k²(u − u0)(v − v0) at angular
       frequency k.
     - So no estimate with a constant independent of k exists in any Sobolev scale. No Newton–Kantorovich or a
       posteriori argument closes in that formulation, whatever the residual.
     - *Computed (`checks/jordan5.py`).* Measured in the scheme itself: k = 2 → 8 multiplies the response by 20.4.
   - *Deduced (exact).* Replacing Ric_xx by the Raychaudhuri constraint for R removes the block: the remaining rows are
     three uncoupled wave operators.
     - But the shift still enters the W row through s_x, and its transport row brings the other fields' angular
       derivatives. Any energy estimate built on the metric functions loses one angular derivative there.
     - The estimate has to be made at the curvature (Bianchi) level: the five-dimensional, T²-symmetric form of
       [Wu26] Theorem 2.2. It is not written.
   - *Computed (`checks/ampresp5.py`).* The problem reduces to one inequality, CERTIFY-10L5.md 2(d)'s
     δ + ∫ε < 1/(4GTF²).
     - The record's runs bound F below by 9.2 (and G by 382 in data units). The demand is then δ + ∫ε < 3.0 × 10⁻⁵
       at 2(d)'s G = 10, and 7.8 × 10⁻⁷ at G_low.
     - The record's computed residual, 2.5 × 10⁻³, is 84 and 3.2 × 10³ times too large: orders of magnitude, lower
       bounds on the gap.
2. **The residual is certified at points, not as a sup.**
   - *Certified (`checks/rcert5.py`).* The explicit three-dimensional approximant's Ricci tensor has frame components,
     in units of the curvature scale, ≤ 2.41 × 10⁻³ (ll) and ≤ 4.0 × 10⁻⁴ for the rest. These are Arb enclosures at
     16,128 points of the box u ∈ [−4, −1.1], v ∈ [0.55, 1.6], |x| ≤ cos(π/32), and they agree with resid5's
     computed maxima to 2–11 %.
   - *Certified, but too loose to use.* The sup over the box, by order-3 Taylor models, is ≤ 6.8 × 10⁴ to 1.7 × 10⁸,
     or unbounded, at 416 boxes. So the sup over the box stays computed (resid5).
3. **The late region.**
   - *Computed (`checks/late5b.py`).* Round 1's failure from v ≈ 1.65 is numerical wherever the record's finest runs
     reach: it was M = 16's angular resolution.
     - At M = 32 and 40 (ld 3) the Raychaudhuri residual converges at second order in the null step, ratio
       3.98–4.00, on every band to v = 1.8 at areal radius ≥ 1.0 (3.48–3.89 on [1.8, 1.9)), and to v = 2 at ≥ 1.2
       (2.25 at M = 40).
     - It is independent of M = 24–56 there, and is 2.4 × 10⁻³ of its terms at 1600 × 720 on [1.65, 1.8).
   - *Unresolved.* It stays unresolved from v ≈ 1.9 at areal radius 1.0–1.2, where neither the null step nor M
     reduces it (12–15 % of its terms). It is also unresolved at areal radius < 0.9 from v ≈ 1.65, where
     M = 24 → 32 changes it little and no finer null grid was completed.
   - *Computed (`checks/cpsolve5.py`, `checks/cplate5.py`).* A constraint-preserving scheme, with no Jordan block,
     agrees with the free one below v = 1.8 to within their null-step differences: one solution.
     - Past v ≈ 1.9 at areal radius 1.0–1.2 it runs on to v = 2.25.
     - Its unimposed Ric_xx falls 100–470-fold per null-grid doubling there, but is not yet small. Whether it
       converges needs a third grid.
   - Whether the unresolved part is a curvature singularity or a steep smooth feature is not decided.
4. **The region of existence** (6.5).
   - *Proved:* only where the solution is the seed, v ≤ 1/2.
   - *Certified:* the data cone's Raychaudhuri constraint (C1, C2), and the 3D residual at points (K1).
   - *Computed:* a converged solution at seed 1 on areal radius ≥ 1.0 for v ≤ 1.9 (≥ 1.2 to v ≈ 2), and at seed 2 to
     v ≈ 3.5.
   - No existence theorem beyond v ≤ 1/2.

### 6.1 The verifier's findings and their disposition

The verifier read round 1 at commit 169c9b5 (scripts d1_mine.py, d2_mine.py, d2_axis.py, myrun_check.py).

**Its verdicts on the claims, recorded.**
- D1 and D2 are correct. D1 rules out every zero of R_v at u > −1, not only one between the first zero and u = −1.
  D2 covers only T²-invariant sections of a single ingoing cone.
- Claim 3 (further zeros of R_v near the cut) holds for v ≤ 1.8; past 1.8 some zeros lie far from the cut. Section 1.3
  already stated it for v ≤ 1.8 and counted the far ones beyond.
- Claim 4 (the untrapped Bondi spheres are tilt) holds at seed 1 only. On 200- and 400-row runs the rebuilt spheres
  have θ > 0 at 3–10 of 32 labels, all at u > −1, where the leaves' θ is −0.6 to −2.5: tilt, not a MOTS. At seed 2 the
  rebuild does not reach those radii, as section 1.4 states.
- The Nx = 24 and 32 instability is reproduced, and the Arb certification of section 2.1 is genuine.

**Its findings, each with its disposition.**

- **V1** (minor; RESULT.md:17, 349, "every MOTS"). Applied: "every T²-invariant MOTS section", at 17 and 349 and at
  the four other sites that say the same (sections 0, 1.2, 1.3, 1.6, 2.4).
- **V2** (minor; the gap's fall with R0 shown at 400 rows only, while at R0 = 10 it grows with resolution). Run: R0 = 20
  at 800 × 360 (922 s). The fall with R0 holds at 800 rows too, but the agreement does not converge in (u, v) from
  v = 1.3. The text is corrected (sections 0, 1.4); details below.
- **V3** (minor; S5's counts over different radii and columns). Done: S7 compares the bands at one radius r* on
  growth5's 17 columns; result below.
- **V4** (minor; secondzero5.py's three S4 FAILURES are expected outcomes). Applied: S4 is report-only and S6 is the
  gate; `secondzero5.out` is regenerated, all checks pass.
- **V5** (minor; RESULT.md:284, "certified data error"). Applied: "certified constraint residual".
- **V6** (nit; cdata5.py's R_rr jumps claimed, never computed). Computed in Arb (C2): ≤ 3.1 × 10⁻⁸ and 3.6 × 10⁻⁸ at
  seed 1, ≤ 7.4 × 10⁻⁸ and 8.5 × 10⁻⁸ at seed 2, against sup |R_rr| ≤ 0.024 and 0.011. The perturbed control's jumps
  are 1.2 × 10² to 1.1 × 10³.
- **V7** (nit; near the cut the D1 violation grows with resolution). Applied, and measured over all runs: that band is
  excluded, not converging; details below.

**V2, the data truncation at two resolutions** (S6, `checks/secondzero5_trunc.out`). Max |r_AH(double null) −
r_AH(growth5)| over growth5's 17 columns:

| v | 400, R0 = 10 | 800, R0 = 10 | 400, R0 = 20 | 800, R0 = 20 | 400, R0 = 40 |
|---|---|---|---|---|---|
| 1.0 | 0.004 | 0.004 | 0.002 | 0.002 | 0.002 |
| 1.2 | 0.029 | 0.024 | 0.018 | 0.011 | 0.008 |
| 1.3 | 0.076 | 0.051 | 0.021 | 0.027 | 0.017 |
| 1.35 | 0.068 | 0.082 | 0.031 | 0.036 | 0.015 |
| 1.375 | 0.081 | 0.110 | 0.025 | 0.051 | 0.020 |

- *What holds.* At 800 rows the difference falls from R0 = 10 to 20 by a factor 2.0–2.3 at every v ≥ 1.2, as at 400
  rows.
- *What fails.* S6's bound of 0.05 at R0 = 20 fails at 800 rows, by 0.001 at v = 1.375. At both R0 the difference grows
  from 400 to 800 rows from v = 1.3 on (at R0 = 20: 0.021 → 0.027, 0.031 → 0.036, 0.025 → 0.051).
- *So.* The dependence on the data truncation is shown at two resolutions. The agreement of the two formulations is
  shown only to v ≈ 1.2 (0.011 at 800 rows, R0 = 20); from v = 1.3 the remaining difference is not resolved in (u, v).
  growth5's record is at one resolution of its own, so which side moves is not decided.
- The control (the leaves' expansion) stays at 0.22 at every R0 and grid.
- `secondzero5_trunc.out` ends in FAILURES for that reason. The round-1 sentence "the two formulations converge on
  each other as the data truncation is removed" is withdrawn as stated, and replaced in section 0.

**V3, the bands at one radius** (S7, `checks/secondzero5_edges.out`). At v = 1.425–1.55 and r* = the rebuild's least
reachable radius (0.64–0.78), the columns of growth5's 17 with no zero on [r*, 1.6] are compared with the rebuild's θ
on the sphere r = r*, interpolated to the same columns.

- *R0 = 10.* The counts are equal at v = 1.425–1.525 (2, 3, 4, 5, 6 columns). The rebuilt band is shifted toward x = 0
  by one column at 1.425, 1.50 and 1.525, and every rebuilt edge lies within 0–0.77 of growth5's column spacing of its
  bracketing pair.
- *R0 = 20.* The sets are identical at 1.475 and 1.50, the shift gone. They differ by one column at 1.45 and 1.525, with
  the edges within 0.36 of a spacing.
- *At v = 1.55.* growth5's band reaches the axis x = −1 (8 columns). The rebuild's stops at x = −0.93 (R0 = 10) and
  −0.97 (R0 = 20), so it moves toward the axis as the data cone moves out.
- *Verdict.* S7, gated on equal counts and every edge within one spacing, FAILS at v = 1.55 at both R0 and at 1.45 and
  1.525 at R0 = 20 (counts differ by one).
- *What it shows.* The band edges agree to within one column spacing through v = 1.525 at both R0. The round-1
  fractions (28 % against 29 %) were not a like-for-like comparison, and are replaced by this.
- *Control.* With the leaves' expansion in place of θ, no column is untrapped at any v. The control fails, as it must.

**V7, the band near the cut** (S1, `checks/secondzero5.out`). The largest excess of R_v over D1's bound
e^{2W}(1 − 1/u²) within Nu/40 rows of the cut, v ≤ 1.8, is 1.32, 4.91 and 9.0 × 10³ at 200, 400 and 800 rows
(M = 16, R0 = 10), 229 at M = 24, 2.5 × 10³ and 1.6 × 10⁴ at R0 = 20 (400, 800 rows), and 1.8 × 10²⁰ and 6.0 at seed 2.
It grows with resolution and with nothing else in common. So that band is excluded, not converging. Section 1.3's
S1 bullet is read that way, and nothing there is claimed for it.

### 6.2 F5: the linear estimate, and why it cannot be had in the record's variables

**The structure (deduced; every identity exact, `checks/symbol5.py` Y0–Y5).** dnsolve5 solves, at each point,
M (R, m, n, W)_uv = rhs with the rows Ric_11, Ric_22, Ric_xx and Ric(Y, ∂_v). Linearised, the principal part is

    D_u ∂_v δf + K ∂_x² δf,   K = M⁻¹N = Λ A,   Λ = e^{2W}/Gx = 4(1 − x²) e^{2W + 2(P+Q)}/R² > 0,

with D_u = ∂_u + (1 − x²) s ∂_x in every row (Y0: M⁻¹V = (1 − x²) s I). A is exact and free of the shift.

- **Y1.** The characteristic polynomial of A is l²(l + 1)².
  - The eigenvalue −1 is semisimple, with left eigenvectors (3/(R(1 + x)), 1, 0, 0) and (3/(R(1 − x)), 0, 1, 0): the
    two wave modes δ[3 log R/(1 ± x) + m or n], that is log(g11 √g22) and log(√g11 g22) over 1 ± x, each with the
    scalar wave operator −e^{−2W} D_u ∂_v + Gx⁻¹ ∂_x² as principal part (Y4).
  - The eigenvalue 0 is **not** semisimple (rank A = 3): a 2 × 2 Jordan block. Its left null vector is dζ,
    ζ = W + 2 log R + P + Q, and the ζ row contains no second x-derivative at all (Y4). The generalised left vector η
    with ηA = dζ is computed (Y1).
- **Y3, no estimate.** Freeze the coefficients at any point and take δf = e^{ikx}(a e0 + b e1) in the Jordan basis.
  The principal system is a_uv = −k²Λ b, b_uv = 0. Characteristic data b = 1, a = 0 on u = u0 and v = v0 give the
  exact solution b = 1, a = −k²Λ(u − u0)(v − v0). Data of norm 1 at frequency k produce a solution of norm
  k²Λ(u − u0)(v − v0) in every H^s(x).
  - So no estimate sup ‖δf(u, v)‖_{H^s} ≤ F(‖data‖_{H^s} + ‖source‖) with F independent of k holds, for any s. A
    defect of strong hyperbolicity in the frozen symbol excludes well-posedness in such a scale for the
    variable-coefficient problem too. This is the standard necessity of strong hyperbolicity (Kreiss, Strang), cited
    from memory and not READ here.
  - *Control.* The same construction in the semisimple block gives J_0(2k√(Λ(u − u0)(v − v0))), bounded by 1 for
    every k (exact).
  - **Consequence.** The a posteriori argument needs exactly such an estimate for the evolution system about g_app,
    with the residual as its source. In dnsolve5's formulation it does not exist: no residual, however small and however
    certified, closes a Newton–Kantorovich argument there. This is the precise reason, sharper than round 1's ("the
    theorem is missing").
- **Y2, the constraint-preserving formulation.** Drop Ric_xx and impose the Raychaudhuri constraint Ric_vv = 0 for R
  along every outgoing generator (`checks/cpsolve5.py`).
  - The rows Ric_11, Ric_22, Ric(Y, ∂_v) for (m, n, W) have K₃ = −ΛI exactly: three uncoupled wave operators. The
    Jordan block is gone.
  - R enters them through R_xx, with coefficients −3Λ/(R(1 + x)), 3Λ/(R(x − 1)), 0, and through R_uv, with
    3/(R(1 + x)), −3/(R(x − 1)), 3/(2R) (exact). The Raychaudhuri row has the single second derivative R_vv.
  - *Control.* Y1's Jordan test applied to this block finds none.
- **Y5, the shift.** The obstruction that remains is the shift, in either formulation.
  - The W row contains s_x; on every spherical state its coefficient is −(1 − x²) R_v/R, nonzero wherever R_v is.
  - The shift is transported by Ric_vx, which contains W_vx (coefficient −1) and R_vx (−2/R) beside s_vv.
  - So δs at (u, v, x) is an integral along the outgoing generator of first x-derivatives of the other fields (after
    one integration by parts in v). The W row needs one more x-derivative of it. An energy estimate at level k for
    (m, n, W) then needs the fields at level k + 1.
  - So no energy estimate built on the metric functions closes, at any derivative level. The shift's angular
    derivative must be estimated as a curvature component with its own flux (the Bianchi level). That is what
    [Wu26] Theorem 2.2's H³/H⁴ structure reflects (READ, CERTIFY-10L5.md section 1). Its five-dimensional,
    T²-symmetric version is not written.
  - *Control.* s_xx, which the W row does not contain, is found absent.

**The witness in the schemes themselves (computed, `checks/jordan5.py`).**

The setup:
- Tangherlini (the record's data at amplitude 0), M = 16, 200 × 30 cells (v ≤ 1.5).
- A source εφ(u, v)T_k(x) is added to the W_uv row, with ε = 10⁻⁷ and φ a sin² bump on u ∈ [−6, −3], v ∈ [0.2, 0.5].
- The response is max |δf|/ε over (R, m, n, W) on the kept cells with u ≤ −1.5, v ∈ [0.6, 1.5].

| k | 0 | 2 | 4 | 6 | 8 |
|---|---|---|---|---|---|
| free (dnsolve5's equations), W source | 2.56 | 3.75 | 24.1 | 46.7 | 76.5 |
| constraint-preserving (cpsolve5), W source | 1.27 | 1.06 | 0.91 | 0.87 | 0.94 |
| free, source along a wave-sector eigenvector (control) | 23.8 | 13.4 | 15.5 | 18.2 | 9.0 |

- **J1.** In the free scheme the response grows by 20.4 from k = 2 to 8. Y3's k² predicts 16.
- **J2.** In the constraint-preserving scheme it stays bounded (ratio 0.88).
- *Control.* A source with no component along dζ does not grow in the free scheme either (ratio 0.67). The growth is
  the Jordan block's.
- *What this explains.* Errors injected at angular frequency k (truncation, and the rounding at the axis nodes of
  D354) are amplified in dnsolve5's formulation by about k² times the area of the (u, v) region they cross. That is
  consistent with the record's finding that raising M at a fixed null grid degrades the solution (D418, D524, D571):
  a property of the formulation, not of the solution. It is not shown here that it is their cause.

**The one inequality, and how far the record is from it** (computed, `checks/ampresp5.py`). The a posteriori route
closes if δ + ∫ε < 1/(4 G T F²) (CERTIFY-10L5.md 2(d)), with F the linear estimate's constant and G the quadratic
one.

- *In dnsolve5's formulation.* F = ∞ (Y3).
- *In any formulation where an estimate exists.* F is bounded below by the response of the computed solution to its
  own data, by the mean-value theorem.
  - The record's ld 3 amplitude runs (D445; M = 32, 800 × 360) at A = 1, 7/8 and 3/4 give the response of the
    metric's values, on v ∈ [0.5, 1.65) and areal radius ≥ 1.0 (48,322 cells kept by all three).
  - F_low = 9.2 (Q; P 7.2, W 8.9, log R 1.3). The second difference gives G_low = 382 (in units of the data's sup).
  - *Control.* The data's own second difference is 2 × 10⁻¹², rounding.
- *The demand.* At F_low, T = 10 and 2(d)'s placeholder G = 10, the condition demands δ + ∫ε < 3.0 × 10⁻⁵. At
  G = G_low it demands 7.8 × 10⁻⁷.
- *The record's figure.* Its computed residual, 2.5 × 10⁻³ of the curvature scale, is 84 and 3.2 × 10³ times these.
  The two sides are measured in different norms, so these are orders of magnitude, and lower bounds, since F and G
  can only be larger.
- *Cost at second order.* The null grid would have to be refined by at least √84 ≈ 9 to 57 in each direction:
  7,000 to 45,000 rows, beside the missing theorem.
- **So F5's state is exact.**
  - In the record's variables no estimate exists (proved).
  - In the constraint-preserving variables the principal part is diagonal, and one coupling, the shift's angular
    derivative, must be estimated at the curvature level. That estimate is not written: it is the open theorem.
  - Given it, the closing inequality above is the one condition left. The record's numbers miss it by a factor of at
    least 84, as orders of magnitude.

### 6.3 R: the certified residual of the three-dimensional approximant (`checks/rcert5.py`)

**The approximant.** It is resid5's, made exact: on Q = {u ∈ [−4, −1.1], v ∈ [0.55, 1.6]}, every field is the
polynomial Σ C_ijk T_i(t) T_j(σ) T_k(x).
- The degrees are 24, 30 and 15.
- t is the run's own coordinate arcsinh((u + 1)/a), rescaled, and σ is affine in v.
- The C_ijk are resid5's floating-point least-squares fit, converted in x to the 16-node interpolant's Chebyshev
  coefficients. Floats are exact rationals, so g_app is an explicit metric of the class.
- The certified quantity is each of the eight null-orthonormal frame components of Ric[g_app] over √K_0 = √72/R⁴.
- They are generated from dnsolve5's exact symbolic Ricci tensor and printed as code on Arb balls.
- x is taken over [−x_1, x_1], x_1 = cos(π/32), the outermost angular node. The axis caps are not covered: there the
  frame's 1/(1 − x²) factors cancel only analytically.

**K1 (certified).** Arb enclosures at the 16,128 centres of a 24 × 24 grid in (t, σ) times the 28 graded x-boxes'
centres. The largest certified value of each component, with resid5's computed maximum at the run's cell midpoints in
brackets:

| ll | ln | nn | lx |
|---|---|---|---|
| 2.41e-3 (2.46e-3) | 1.44e-4 (1.53e-4) | 7.23e-5 (7.46e-5) | 4.03e-4 (4.25e-4) |

| nx | xx | 11 | 22 |
|---|---|---|---|
| 2.22e-5 (2.47e-5) | 1.87e-4 (2.02e-4) | 5.55e-5 (6.24e-5) | 1.99e-4 (2.14e-4) |

- The two agree to 2–11 %: the same function, sampled at other points (PASS).
- The fit's own error is ≤ 7 × 10⁻¹¹ (computed).
- *Control.* The approximant with W + 0.01v has certified values up to 0.272, 113 times larger.

**K2 (certified, and too loose to use).** Order-3 Taylor models with the Lagrange remainder, on 416 boxes:
4 × 4 in (t, σ), and 26 in x, graded geometrically toward the axes.
- The certified sup is ≤ 6.8 × 10⁴ for ll, ≤ 1.7 × 10⁸ for nn, and ≤ 6.2 × 10⁷ for xx, 11 and 22.
- For ln, lx and nx it is unbounded: in some box an interval reaches zero under a reciprocal or a square root.
- The worst boxes lie at the corners of the (t, σ) grid, and for 11, 22 and xx in the box next to an axis.

**What this is, and is not.**
- It is a certified residual of an explicit three-dimensional approximant at 16,128 points of Q. The values agree with
  the computed figures at the run's own cell midpoints, so the residual is the run's (u, v) truncation error, certified.
- It is not a certified sup over Q. With Taylor models of order 3 and interval remainders the sup bound is valid, and
  10⁴ to 10⁸ times the residual or unbounded at 416 boxes.
- The reason is the expression, not the precision. Its terms cancel to 10⁻³ of their size, and the interval remainder
  is C h³ with C of the size of the terms' third derivatives, not the residual's.
- A useful sup bound needs either boxes at least a hundred times finer in each variable (beyond this round's machine
  time) or a different enclosure. Candidates are Chebyshev interpolation of the residual with an analyticity bound on
  a polyellipse, or a reformulation in which the cancellation is algebraic.
- Either way it would still not close anything, by section 6.2.

### 6.4 R: the late region

**The record's finest free runs, refined in the null step and in angle** (`checks/late5b.py`, computed; the runs of
CERTIFY-10L5.md D418 and D432, ld 3, cut 0.9, and D410's at cut 0.7). Round 1's L1 asked whether the Raychaudhuri
residual ρ = −(R/3) Ric_vv converges. It is measured here per v-band and per class of areal radius r_A.

- **L5, the null step** (M = 32 and 40; 800 × 360 against 1600 × 720 on the coarse cells both keep). The figures are
  max |ρ|, with its ratio to the band's largest term in brackets.

  | v-band | areal ≥ 1.2, M = 32: 800 / 1600 (ratio) | areal 1.0–1.2, M = 32 | areal 1.0–1.2, M = 40 |
  |---|---|---|---|
  | [1, 1.5) | 9.9e-4 / 2.5e-4 (3.99) | 1.8e-3 / 4.4e-4 (3.99) | 1.8e-3 / 4.4e-4 (3.99) |
  | [1.5, 1.65) | 1.4e-3 / 3.6e-4 (3.99) | 3.3e-3 / 8.2e-4 (3.99) | 3.3e-3 / 8.3e-4 (3.99) |
  | [1.65, 1.8) | 2.1e-3 / 5.2e-4 (3.99) | 9.5e-3 / 2.4e-3 [2.4e-3] (4.00) | 9.6e-3 / 2.4e-3 [2.4e-3] (3.98) |
  | [1.8, 1.9) | 2.8e-3 / 7.1e-4 (3.99) | 3.1e-2 / 9.0e-3 (3.48) | 3.3e-2 / 8.5e-3 (3.89) |
  | [1.9, 2.0) | 4.0e-3 / 1.0e-3 (3.99) | 0.52 / 0.54 [0.15] (0.96) | 0.43 / 0.45 [0.12] (0.95) |
  | [2.0, 2.25) | 6.4e-3 / 3.5e-3 (1.84; 3.56 at M = 40) | 8.8 / 10.4 (0.85) | 10.4 / 11.7 (0.89) |

  - The residual is second order in the null step (ratio 3.98–4.00) on every band to v = 1.8 at areal radius ≥ 1.0,
    nearly so on [1.8, 1.9) (3.48, 3.89), and to v = 2.25 at ≥ 1.2 (M = 40).
  - On [1.65, 1.8), round 1's failing band, it is 2.4 × 10⁻³ of its terms at 1600 × 720 (claim: PASS).
  - From v = 1.9 at areal radius 1.0–1.2 it does not converge, and it is 12–15 % of its terms.
  - *Control.* With W_v in place of 2W_v the residual does not converge where L5's does (ratio 1.01 on [1, 1.5)).
- **L6, angle** (800 × 360, on the cells M = 24, 32, 40, 48 and 56 all keep).
  - Before v = 1.9 max |ρ| is the same at all five M to 3 % at areal radius ≥ 1.2. At 1.0–1.2 it agrees to 6 % before
    v = 1.8 and to 20 % on [1.8, 1.9). So the null step sets it, and M ≥ 24 resolves the angle there.
  - On [1.9, 2.0) at 1.0–1.2 it is 0.61, 0.52, 0.43, 0.37, 0.81, and on [2.0, 2.25) it grows with M, 2.0 to 906: the
    record's D418 pattern, now in the constraint.
- **L7, the small radii** (cut 0.7, 800 × 360, areal radius 0.6–0.9).
  - Max |ρ| over the band's largest term on [1.5, 1.65), [1.65, 1.8), [1.8, 1.9) and [1.9, 2.0) is 5.8 × 10⁻³,
    5.5 × 10⁻², 0.43 and 1.0 at M = 24.
  - At M = 32 it is 5.8 × 10⁻³, 4.3 × 10⁻², 0.38 and 0.68.
  - The largest on [1.65, 1.8) is at u = −0.982, v = 1.788, areal radius 0.86, round 1's place.
  - So round 1's "the size of its own terms from v ≈ 1.65" was M = 16's: at M = 24–32 it is 4–6 % of the terms on
    [1.65, 1.8). It still reaches 40 % on [1.8, 1.9).
  - The null-step test there (`--small`, a 1600 × 720 run at cut 0.7) was not completed.
- **L8, D1's monotone quantity** (areal 1.0–1.2). Its largest increase relative to the band's size is ≤ 10⁻⁴, and
  falling with the null step, to v = 1.9. It is 1.4–3.2 × 10⁻² on [1.9, 2.0) and 0.07–0.21 on [2.0, 2.25), not
  converging: the computed fields there are not a vacuum solution's.

**The constraint-preserving runs** (`checks/cpsolve5.py`, `checks/cplate5.py`). This is the scheme without the
Jordan block (Y2): Ric_vv imposed, Ric_xx dropped and monitored.

- *P1–P3* (selftest, `checks/cpsolve5.out`).
  - On Tangherlini at M = 8 the error of R is 1.2 × 10⁻², 4.6 × 10⁻⁴ and 2.4 × 10⁻⁴ at 100, 200 and 400 rows.
  - On the record's data (M = 8, v ≤ 1.5) the two schemes' difference falls 14.6-fold from 100 to 200 rows: one limit.
  - The scheme has a defect of its own (P3). A mismatch between the marched R_uv and the rows' shifts P and Q
    uniformly, so 2P + Q = (1 + x)m does not vanish at x = −1. Elementary flatness at the axis is violated at the order
    of the truncation error times M²: a spurious m on Tangherlini of 2.0 × 10⁻², 1.0 × 10⁻³ and 1.1 × 10⁻⁴ at 100,
    200 and 400 rows.
  - *Control.* With W_v for 2W_v in the march the error does not fall.
- *J2.* A W_uv source's response is bounded in k: 1.06 at k = 2, 0.94 at k = 8.
- *The record's data* (seed 1, cut 0.9, ld 3, M = 32, v ≤ 2.25, at 400 × 180 and 800 × 360: 1,405 s and 2,551 s at
  this machine's load), against the record's free runs (M = 32, 800 × 360 and 1600 × 720). The figures are max |ΔP|.

  | v-band | areal 1.0–1.2: cp 400–800 | cp 800 − free 800 | free 800–1600 | Ric_xx monitor 400 → 800 |
  |---|---|---|---|---|
  | [1, 1.5) | 1.1e-3 | 6.9e-5 | 1.8e-5 | 3.8 → 0.16 (25) |
  | [1.5, 1.65) | 1.5e-3 | 1.2e-4 | 2.6e-5 | 34 → 0.50 (68) |
  | [1.65, 1.8) | 1.7e-3 | 1.6e-4 | 3.8e-5 | 613 → 6.4 (96) |
  | [1.8, 1.9) | 4.9e-3 | 3.7e-4 | 1.1e-4 | 4.7e3 → 45 (105) |
  | [1.9, 2.0) | 2.0e-2 | 1.5e-3 | 3.8e-4 | 3.4e4 → 345 (99) |
  | [2.0, 2.25) | 0.19 | 1.8e-2 | 2.0e-3 | 4.1e5 → 880 (467) |

  - Below v = 1.8, at areal radius ≥ 1.0, the two formulations agree to within 3 times the larger of their own
    null-step differences (claim: PASS). They converge to one solution, and the free scheme's Raychaudhuri residual
    there is its second-order truncation error.
  - *Control.* The free run at amplitude 7/8, a different solution, differs by 10⁻³–4.5 × 10⁻², beyond that bound on
    every band.
  - The constraint-preserving scheme is the less accurate of the two in P, about ten times at equal grid: its axis
    defect.
  - Its unimposed Ric_xx (a coordinate component, large near the axes) falls 18–27-fold per doubling before v = 1.5,
    and 60–470-fold after. So the 400-row run is not in the asymptotic range, and two grids give no order.
  - It runs through v = 2.25 at every areal radius kept, with no breakdown; the free scheme's residual stops
    converging from v ≈ 1.9. Its own null-step difference in P there is 2 × 10⁻² on [1.9, 2.0) and 0.19 on
    [2.0, 2.25) at 1.0–1.2, so it is not shown to converge either.

**Verdict.** 
- **Before v ≈ 1.8–1.9, at areal radius ≥ 1.0: numerical, and settled.**
  - Round 1's Raychaudhuri violation from v ≈ 1.65 was M = 16's angular under-resolution. At M ≥ 24 it is the null
    step's second-order error, and it converges.
  - Two formulations, one weakly and one strongly hyperbolic in principal part, converge to one solution there.
- **From v ≈ 1.9 at areal radius 1.0–1.2: not decided.**
  - In the free scheme neither refinement converges, and its formulation amplifies angular errors like k² (Y3, J1).
  - The constraint-preserving scheme runs on without breakdown, but its two grids do not establish convergence.
  - The decisive test is the constraint-preserving scheme on a third null grid (1600 × 720) at M = 32 and 40, with
    the Kretschmann scalar compared. It was not run in this round.
  - A singularity and a steep smooth feature are not told apart.
- **From v ≈ 1.65 at areal radius < 0.9: not decided.**
  - At M = 24–32 the residual is 4–6 % of its terms on [1.65, 1.8) (no longer of their size, round 1's M = 16) and
    40 % on [1.8, 1.9).
  - The null-step test there was started and not completed.

### 6.5 The region of existence at 10 l5, with labels

Seed 1 unless stated.
- **v ≤ 1/2, the whole (u, x) range — proved (deduced).** The solution exists: it is the seed (Tangherlini) itself
  (the record; section 2.4).
- **Wherever a smooth vacuum solution with the data exists in dnsolve5's gauge — proved (deduced).** Every leaf with
  u > −1 is outer trapped; every T²-invariant MOTS section has its innermost point at u ≤ −1 (D1–D2, `sectexp5.py`).
- **The data cone u = −10, v ∈ [1/2, 7/2], both seeds — certified.** The Raychaudhuri constraint of an explicit
  approximant is ≤ 5.0 × 10⁻⁵ (seed 1) and 2.3 × 10⁻⁵ (seed 2); R_rr's jumps are ≤ 3.6 × 10⁻⁸ and 8.5 × 10⁻⁸
  (`cdata5.py` C1, C2).
- **u ∈ [−4, −1.1], v ∈ [0.55, 1.6], |x| ≤ cos(π/32) — certified at 16,128 points, computed as a sup.** The 3D
  approximant's Einstein residual is ≤ 2.41 × 10⁻³ of the curvature scale at the points; its sup over the box is
  2.5 × 10⁻³, computed (`rcert5.py` K1; `resid5.py`).
- **Areal radius ≥ 1.0 for v ≤ 1.9 (null-step ratio 3.98–4.00 to v = 1.8, 3.48–3.89 on [1.8, 1.9)); ≥ 1.2 for
  v ≤ 2.0 (2.25 at M = 40) — computed, converged.** The record's free solution at M ≥ 32: the Raychaudhuri residual
  is second order in the null step and independent of M, and a constraint-preserving scheme converges to the same
  solution below v = 1.8; the metric values converge in M and null step to v ≈ 1.8 (`late5b.py` L5–L6, `cplate5.py`;
  CERTIFY-10L5.md D432).
- **Areal radius 1.0–1.2 for v ≥ 1.9, and areal radius < 0.9 for v ≥ 1.65 — computed, not converged.** The
  Raychaudhuri residual is 12–100 % of its terms and not reduced by M. By the null step it is not reduced at 1.0–1.2,
  and not tested below 0.9 (`late5b.py` L5–L7).
- **Seed 2, v ≤ 3.5 at every angle — computed, converged.** Kretschmann converges in M and in the null grid
  (CERTIFY-10L5.md D543, D601).

**No existence theorem beyond v ≤ 1/2 is proved at 10 l5, at either seed.** Two steps are missing between the computed
regions and a proof:
- the linear estimate with explicit constants, which does not exist in the record's formulation (6.2, Y3) and must be
  built at the curvature level in the constraint-preserving one (Y5);
- a residual meeting the closing inequality. The record's misses it by at least two orders of magnitude (6.2,
  `ampresp5.py`), and its certificate is pointwise (6.3).

### 6.6 What remains open, precisely

1. **The theorem (F5).** In the class, in double-null gauge, with Ric_vv imposed and Ric_xx dropped (cpsolve5's
   formulation, diagonal principal part, Y2): an energy estimate for the linearised system at the curvature level.
   - The shift's angular derivative enters as a curvature component with its own flux, so Y5's loss is removed.
   - It needs explicit constants: Sobolev on the 1D orbit sections, and the axes in the regular variables (G4).
   - This is the five-dimensional, T²-symmetric form of [Wu26] Theorem 2.2, whose threshold is not explicit even in
     3 + 1.
2. **Its constants on g_app.** F, and G, evaluated on the converged region. ampresp5 bounds them below (F ≥ 9.2), not
   above.
3. **A residual meeting the closing inequality**, certified as a sup in the theorem's norm.
   - The record's 2.5 × 10⁻³ is at least 84 times too large, so at second order the null grid must be at least 9 times
     finer.
   - A usable certified sup needs a better enclosure than interval Taylor models of this expression (6.3).
4. **The late region's cause.**
   - At areal radius < 0.9 from v ≈ 1.65: the null-step test at M = 32, `szrun5.py 1 0.7 32 1600 720 1.85` read by
     `late5b.py --small`, was started and stopped unfinished at this machine's load.
   - From v ≈ 1.9 at 1.0–1.2: a scheme without the Jordan block at M ≥ 32 on a finer null grid. The
     constraint-preserving runs at 400 and 800 rows (6.4) are the first two grids: run the third (1600 × 720) at
     M = 32 and 40.
   - A singularity against a steep smooth feature is decided by neither, only by a resolved Kretschmann scalar.
5. **The data at past null infinity (G3)** and Ric_vx on the data cone: unchanged since round 1.

### 6.7 Files, runs and outputs (round 2)

| file | what |
|---|---|
| `checks/symbol5.py`, `.out` | Y0–Y5: principal symbol, Jordan block, no-estimate, Y2's block, the shift (exact) |
| `checks/jordan5.py`, `.out` | J1–J2: the Jordan growth in both schemes, with a wave-sector control (computed) |
| `checks/cpsolve5.py`, `.out` | the constraint-preserving scheme; P1–P3 (computed) |
| `checks/cplate5.py`, `.out` | E1–E2: constraint-preserving against free runs (computed) |
| `checks/late5b.py`, `.out` | L5–L8 on the record's finest runs (computed); `--small` not yet run |
| `checks/ampresp5.py`, `.out` | A1–A2: F_low, G_low and the closing condition's demand (computed) |
| `checks/rcert5.py`, `.out` | K1 certified values, K2 certified (loose) sup |
| `checks/cdata5.py`, `.out` | C1 as before; C2 the R_rr jumps (certified, new) |
| `checks/secondzero5.py`, `.out` | S4 report-only; S1's near-cut excess (new) |
| `checks/secondzero5_trunc.out` | S6 at 400 and 800 rows |
| `checks/secondzero5_edges.out` | S7: the bands at one radius (new) |

**Runs** (scratch, not committed).
- `szrun5.py 1 0.3 16 800 360 2.0 OUT ld 3 R0 20`: 922 s.
- `szrun5.py 1 0.7 32 1600 720 1.85 OUT ld 3`: started, and stopped unfinished after 28 min (6.7 CPU-minutes)
  at a load of 20–28, for L7's null-step test; not seated.
- `cpsolve5.py --run 1 0.9 32 Nu Nv 2.25 OUT ld 3` at (400, 180) and (800, 360): 1,405 s and 2,551 s.
- The record's runs of D410, D418, D432 and D445, read in place.

The machine ran at a load of 15–28 on 4 cores throughout, so the wall times are not comparable with round 1's.


### 6.8 A proposed replacement for the paper's section 9 sentences on existence at 10 l5

Proposed to the main session, which seats it; this note does not edit the paper. It replaces the sentences from "A
first certified step is taken" to "remains open":

> Certified so far: on the data cone the Raychaudhuri constraint of an explicit approximant holds to 5.0 × 10⁻⁵ and
> 2.3 × 10⁻⁵ (`docket68/n1star/checks/cdata5.py`), and the Einstein residual of a smoothed three-dimensional
> approximant is enclosed in ball arithmetic at 16,128 points away from the axis caps, ≤ 2.42 × 10⁻³ of the
> curvature scale (`checks/rcert5.py`); its sup over the box is computed only. Existence at 10 l5 is not proved
> beyond the seed. In the metric variables the numerics evolve, the shift's angular derivative is of principal size at
> high angular frequency, so no linear estimate without loss of derivatives holds there (deduced,
> `checks/symbol5s.py`). The class is (2+1)-dimensional gravity coupled to two free waves (deduced, exact:
> `checks/reduce5.py`), and in double-null gauge its Ricci coefficients obey transport equations with no angular loss
> (`checks/null3.py`). So a linear estimate at the curvature level holds, with explicit constants, on domains of
> dependence that avoid the axes (supplement `CERTIFY-10L5-RESULT.md` Theorem 7.L). Two things stop it short of a
> proof. On the computed solution its constant is of order 10^69 before the axes enter, against a measured response of
> 9.2 (`checks/linest5.py`). And the solution's late region lies within three angular crossing times of the axes, where
> the reduction degenerates and the estimate must be made in four-dimensional axisymmetric form; that estimate is not
> written. The computed solution converges at the first seed to v ≈ 1.8 r_h at areal radius ≥ r_h, and is unresolved
> beyond (`checks/late5b.py`).

The verifier of round 2 also found that the paper's section 9 sentence on the rebuilt Bondi spheres ("reproduce the
untrapped columns") claims more than 6.1's S7 supports (within one column spacing to v = 1.525; S7 fails at 1.55). It
reports that it will correct the paper; the text above does not touch that sentence.

### 7.10 The verifier of round 2

No findings reached this session before it closed. When they arrive they are seated here as amendments; earlier
sections are not rewritten.
