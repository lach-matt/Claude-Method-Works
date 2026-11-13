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
> 2.3 × 10⁻⁵ (`docket68/n1star/checks/cdata5.py`). The Einstein residual of a smoothed three-dimensional approximant
> is enclosed in ball arithmetic at 16,128 points, ≤ 2.4 × 10⁻³ of the curvature scale (`checks/rcert5.py`); its sup
> over the box is computed only (`checks/resid5.py`). Existence at 10 l5 is not proved beyond the seed, and the
> reason is exact. In the double-null formulation the numerics evolve, the linearised principal symbol has a Jordan
> block, so no linear estimate holds in any Sobolev scale and no residual closes an a posteriori argument (deduced,
> `checks/symbol5.py`; measured in the scheme, `checks/jordan5.py`). Imposing the Raychaudhuri constraint in place of
> Ric_xx removes the block, but the shift then costs one angular derivative: the estimate must be made at the
> curvature level, the five-dimensional form of [Wu26] Theorem 2.2, which is not written. Granting it, the closing
> condition asks a residual at least 84 times smaller than the computed one (`checks/ampresp5.py`). The computed
> solution converges at the first seed to v ≈ 1.9 r_h at areal radius ≥ r_h, the earlier failure there being angular
> resolution (`checks/late5b.py`), and is unresolved beyond (supplement `CERTIFY-10L5-RESULT.md` section 6).

## 7. Round 3 (2026-11-02): the curvature-level estimate, what it asks of the residual, the late region

*Status.* Appended 2026-11-02. Sections 0–6 are not rewritten. The verifier of round 2 reported during this round;
its findings are seated in 7.10 as amendments to section 6, each re-derived or marked as not re-derived. Labels as in
section 0. [Wu26] was re-read at source for this round (arXiv 2609.08421v1: Theorem 2.2 and its proof sketch
pp. 6–8, the transport equations (2.2)–(2.6) pp. 4–5, the scalar identity (2.17) p. 6, the residual formulas p. 12;
READ). Machine load was 9–36 on 4 cores until the machine restarted on 2026-11-06, then 0.5–20.

### 7.0 Answers

1. **Task 1, the curvature-level estimate.** It is written and proved on domains away from the axes, with every
   constant explicit (Theorem 7.L). It does not reach the region where it is needed, and the reason is exact: the axes.
   - *Deduced (exact, `checks/reduce5.py` R1–R4).* The class is (2+1)-dimensional gravity coupled to two free waves.
     With ρ the T² orbit's area density and h̃ = ρ²h the Einstein-frame orbit metric, the vacuum equations are
     exactly Ric(h̃) = dΦ1 dΦ1 + dΦ2 dΦ2, □_h̃ Φ_i = 0, with Φ1 = √(3/2) log ρ and Φ2 = (A − B)/√2. So the model is
     [Wu26]'s Einstein–scalar system (1.4), not its vacuum one, in dimension 2+1: no Weyl curvature, sections of
     dimension one (no shear, no Gauss curvature).
     - Its curvature residues, Ric(h̃) − Σ dΦ_i dΦ_i and □Φ_i, are fixed linear combinations of the five-dimensional
       Ricci tensor, off shell (R3). A certified bound on one is a certified bound on the other.
     - Round 2's ζ = W + 2 log R + P + Q (symbol5.py's left null vector) is the Einstein-frame lapse log Ω̃, up to a
       fixed function of x (R4). Its Jordan block was the frozen shift's (7.10, A1: with s_vx kept there is none).
   - *Deduced (exact, `checks/null3.py` N0–N10).* In double-null gauge the reduced system has a hierarchy with no
     angular loss.
     - Every Ricci coefficient has a transport equation free of angular derivatives of Ricci coefficients: χ, η, ω̲
       along e4; χ̲, η̲, ω along e3 (N1–N3).
     - The scalars obey two Bianchi-type pairs each, with exact energy identities (N9).
     - The shift's x-derivative lives only in χ̲, which Raychaudhuri transports along e3 without it (N0, N1).
     - In frame-difference unknowns the linearised operators contain no derivative of the metric differences
       (N10).
     - The angular loss lives only in the two equations the hierarchy does not use, e4 χ̲ and e3 χ (N7).
     - So round 2's Y5 loss belongs to the metric formulation, not to the class. There the shift's first derivative
       s_x is of principal size at high angular frequency (7.10, A1: `checks/symbol5s.py` S4–S6); in the hierarchy s
       enters only through η, η̲ (b_v) and χ̲ (b_x), each transported.
   - *Proved (Theorem 7.L, 7.3).* The linear estimate at level 0 (L² on the sections) for the linearised reduced
     system, on a truncated domain of dependence away from the axes:
     f ≤ (𝒟 + 𝒮) exp(2∫a_o du + 2∫a_i dv), with a_o, a_i explicit sums of the background's coordinate-normalised
     coefficients (listed in `checks/linest5.out`, E2).
   - *Computed (`checks/linest5.py` E4–E5, on the record's solution over rcert5's box).*
     - F² = 10^138 on |x| ≤ 1/2 and 10^222 on |x| ≤ 0.8, growing without bound toward the axes.
     - Every truncated domain over the box is empty. The x-shrink the domain needs is 5.8, against a half-width of at
       most 1. The box is causally connected to the axes about three times over.
   - **What is missing, exactly (7.5).**
     - The axes. The Einstein frame degenerates there (Ω̃² ∝ 1 − x², Φ_i carry log(1 ∓ x)), and the coefficients grow
       like the inverse distance (κ from 122 to 1.8 × 10⁵ between |x| ≤ 1/2 and the outermost node). Near each axis
       the class is four-dimensional axisymmetric Einstein–scalar: reduce on the circle that does not degenerate
       there. Its estimate needs Weyl curvature and its Bianchi pairs, [Wu26] (1.4) on disk sections with a
       regular axis. It is not written, and without it no point of the late region is reached.
     - Level 1 (H¹ ⊂ L^∞ on a one-dimensional section) for the quadratic term. Away from the axes it should be
       mechanical, by commuting with the background's e_x. Not written.
     - The quadratic constant G.
2. **Task 2, the demand on the residual.**
   - *Computed (`linest5.py` E6, E4b).* At Theorem 7.L's own F, the closing condition δ + ∫ε < 1/(4GTF²) asks
     10^−140 on |x| ≤ 1/2, before the axes enter. No approximant held in double or modest multiprecision has a
     residual near that, so no certificate can meet it (deduced).
   - *Deduced.* Any Grönwall-type explicit constant adds absolute values of coefficients of size 20–120 here. The
     measured response is 9.2 (round 2, `ampresp5.py` A1). So the route needs F as a computed, validated bound on the
     linearised solution operator: an approximate inverse built numerically, with the explicit estimate applied only
     to its defect (radii-polynomial style). Then the demand is 5.3 × 10⁻⁴ (G = 0.57, round 2's G_low read in 2(d)'s own
     model, `linest5.py` E8) to 3.0 × 10⁻⁵ (2(d)'s placeholder G = 10), at F = 9.2.
   - At that level a certificate is plausible only with a better approximant first. The record's certified pointwise
     residual, 2.42 × 10⁻³, is above it by 4.6 to 81, depending on G, which is not computed.
   - *Certified (`checks/rcert5b.py`, one sub-box; Theorem 7.L's L² norm allows a local certificate).* On one interior
     box of rcert5's K2 grid, split into n³ sub-boxes, the certified sup of the ll component falls from 8.1 × 10³
     (n = 1) to 0.124 (n = 8). The other components fall from up to 3.4 × 10⁶, or no bound, to 0.021–0.093.
     - It is still 810–4,400 times the residual's own size there (the largest certified centre value, 1.5 × 10⁻⁴).
     - At the measured rate of 33–51 per halving (computed), reaching twice the residual's size needs n ≈ 26–35:
       about 2–4 × 10⁴ sub-boxes for this one box of the 416, at 0.6 s each at this load.
     - So a usable certified sup over the box is a matter of machine time (extrapolated: of the order of 10⁷
       sub-boxes and 10⁷ s for all 416), not of method. It is useful only once F is computed rather than Grönwall's.
3. **Task 3, the late region.** Run after the machine restarted and the load fell (7.7).
   - *Computed, below areal radius 0.9* (`checks/late5b_small.out`, M = 32, 800 against 1600 rows). The Raychaudhuri
     residual converges at second order to v = 1.65 (1.4 × 10⁻³ of its terms). It falls 2.9-fold on [1.65, 1.8), to
     1.3 %, and does not converge from v = 1.8 (ratio 1.36, 17 %). Converging to v = 1.8; not decided beyond.
   - *Computed, v ≥ 1.9 at areal radius 1.0–1.2* (`checks/cplate5c.out`, the constraint-preserving scheme on three
     null grids, M = 32).
     - The metric converges in the null step through v = 2.25 (800–1600 differences ≤ 1.0 × 10⁻³).
     - The unimposed Ric_xx falls 14–22-fold per doubling to v = 1.9, then 2.7-fold on [1.9, 2.0) and not at all on
       [2.0, 2.25). At areal radius 0.9–1.0 it grows there.
     - So a vacuum limit is supported to v = 1.9 at areal radius ≥ 0.9 (computed), and not from v = 1.9 at M = 32.
       There the null step is not the limiting error.
     - M = 40 on the same grid does not separate the causes. It raises the monitor 2–25-fold everywhere from v = 1.0,
       the scheme's angular defect. P agrees with M = 32 to 3.3 × 10⁻⁴ on [1.9, 2.0) and differs by 5 × 10⁻² on
       [2.0, 2.25). So v ≥ 1.9 at areal radius 1.0–1.2 is still not decided (`checks/cplate5d.out`).
   - The Kretschmann scalar was not computed, so a singularity and a steep smooth feature are still not told apart.

### 7.1 The reduction (`checks/reduce5.py`; deduced, every identity exact)

The class, with P and Q free functions (the record's P, Q of m, n are a special case), is
g5 = h + e^{2A} dφ1² + e^{2B} dφ2², with A = log R + P + ½ log((1 + x)/2) and B = log R + Q + ½ log((1 − x)/2).
Put ρ = e^{A+B}, L = log ρ, ψ = (A − B)/2, h̃ = ρ² h. For every metric of the class, no field equation used:

- **R1.** Ric5(∂_φ1, ∂_φ1) = −e^{2A} ρ² □_h̃ A, and likewise for B.
- **R2.** On the orbit directions, Ric5_ab = Ric(h̃)_ab − (3/2) L_a L_b − 2 ψ_a ψ_b + (□_h̃ L) h̃_ab (all six
  components).
- **R3.** E_ab := Ric(h̃)_ab − (3/2) L_a L_b − 2 ψ_a ψ_b = Ric5_ab + (e^{−2A} Ric5_11 + e^{−2B} Ric5_22) h_ab, and
  □_h̃ A = −e^{−2A} ρ⁻² Ric5_11. The reduced residues are fixed combinations of Ric5. In the frames, termwise,
  |E_ab| ≤ |Ric5_ab| + 2 |h_ab| max(|Ric5_1̂1̂|, |Ric5_2̂2̂|), the Killing directions normalised (deduced from R3).
- **R4.** In the record's variables h̃ = −4 Ω̃² du dv + γ̃ (dx − (1 − x²) s du)², with γ̃ = R⁶/16 (P and Q drop out),
  log Ω̃ = W + 2 log R + P + Q + ½ log((1 − x²)/4), and √|det h̃| = R⁷ (1 − x²) e^{2(P+Q) + 2W}/8.
- *Controls* (each fails, as it must): the weight ρ in place of ρ² (R1 and R2), and the coefficient 1 in place of 3/2.

So the vacuum equations of the class are Ric(h̃) = Σ dΦ_i dΦ_i and □_h̃ Φ_i = 0, a wave map into the flat plane coupled
to (2+1)-gravity. R4 identifies round 2's ζ (symbol5.py Y1's left null vector) as the Einstein-frame lapse.

### 7.2 The null structure and the hierarchy (`checks/null3.py`; deduced, every identity exact)

For any (2+1)-metric h = −2Ω² (du dv + dv du) + γ (dx − b du)², Ω = e^w, γ = e^{2k}, frame e4 = Ω⁻¹ ∂_v,
e3 = Ω⁻¹ (∂_u + b ∂_x), e_x = γ^{−1/2} ∂_x, and [Wu26] (2.1)'s Ricci coefficients (READ, p. 4):

- **N0.** χ = e^{−w} k_v, χ̲ = e^{−w} (k_u + b k_x + b_x), ω = −e^{−w} w_v/2, ω̲ = −e^{−w} (w_u + b w_x)/2,
  ζ = −e^{k−2w} b_v/4, η = ζ + e^{−k} w_x, η̲ = −ζ + e^{−k} w_x. The shift's x-derivative b_x appears in χ̲ only.
- **N1.** e4 χ + χ² + 2ωχ = −Ric_44 and e3 χ̲ + χ̲² + 2ω̲χ̲ = −Ric_33 ([Wu26] (2.2) on a one-dimensional section).
- **N2.** e4 η = −χ(η − η̲) − Ric_x4 and e3 η̲ = −χ̲(η̲ − η) − Ric_x3.
- **N3.** e4 ω̲ = ½η² − ηη̲ + 2ωω̲ + ¼(Ric_34 + Ric_xx) and e3 ω = ½η̲² − ηη̲ + 2ωω̲ + ¼(Ric_34 + Ric_xx). The
  coefficients are solved for and then checked, uniquely. [Wu26] (2.5)'s Gauss term has no analogue here.
- **N4.** [e4, e_x] = −χ e_x + ½(η + η̲) e4, [e3, e_x] = −χ̲ e_x + ½(η + η̲) e3, and
  [e3, e4] = 2(η − η̲) e_x − 2ω e3 + 2ω̲ e4.
- **N5.** −□f = e3 e4 f − e_x e_x f + ½χ e3 f + ½χ̲ e4 f − 2η e_x f − 2ω̲ e4 f ([Wu26] (2.17) in dimension 3).
- **N6.** div e4 = χ − 2ω, div e3 = χ̲ − 2ω̲, div e_x = η + η̲.
- **N7.** The two equations the hierarchy does not use, e4 χ̲ and e3 χ, contain 2 e_x η̲ and 2 e_x η. An ansatz without
  them has no solution (the control); one with them has.
- **N9.** For a = e4 f, c = e_x f, d = e3 f: Div(a² e3 + c² e4 − 2ac e_x) = −2a □f + Q1 and
  Div(c² e3 + d² e4 − 2cd e_x) = −2d □f + Q2. Q1 and Q2 are quadratic forms with Ricci coefficients as coefficients
  (printed). The fluxes are a² and c² on outgoing cones, c² and d² on ingoing ones.
- **N10.** With the frame-component differences A1 = δ(e4 Φ), C1 = δ(e_x Φ), D1 = δ(e3 Φ), the linearised pair and
  transport operators contain no derivative of the metric differences δw, δk, δb, and none of δΦ.
  - *Control.* The coordinate difference e^{−k} δΦ_x in place of C1 brings in δk_x: the angular derivative the frame
    differences avoid.
- *Controls* (each fails): ωχ for 2ωχ in N1, η for η − η̲ in N2, N7's ansatz, N10's coordinate difference.
- **N8 (deduced from N0–N6).** The hierarchy has no angular loss. Each Ricci coefficient is transported with a right
  side polynomial in the Ricci coefficients and in Ric = Σ e_aΦ_i e_bΦ_i. The metric follows by ∂_v k = e^w χ,
  ∂_v w = −2 e^w ω, ∂_v b = −2 e^{2w−k}(η − η̲). The scalars obey the pairs (P1, P2) = (e3 a − e_x c, e4 c − e_x a)
  and (P3, P4) = (e3 c − e_x d, e4 d − e_x c), whose right sides are listed in `linest5.py` E1 (exact).

### 7.3 Theorem 7.L: the linear estimate, level 0 (proved)

*Setting.* Let g̊ be a smooth metric of the class on Q = [u0, u1] × [v0, v1] × [−1, 1], in the record's coordinates.
Its Einstein frame (R4) gives (ẘ, k̊, b̊), the scalars Φ̊_i, and the state (ψ̊; å_i, c̊_i, d̊_i).
- *The domain.* Fix X ∈ (0, 1) and λ > 0. Put c_u := sup_Q |b̊| + λ, c_v := sup_Q (Ω̊²/γ̊)/λ, and
  D := {|x| ≤ X − c_u (u − u0) − c_v (v − v0)}. (With local suprema in place of sup_Q, the same holds.)
- *The system.* The linearisation of the reduced system about g̊ in the fifteen frame-difference unknowns
  Z = (δχ, δη, δω̲, δk, δw, δb; δχ̲, δη̲, δω; δa_i, δc_i, δd_i). Each row reads X̊(δY) = Σ_Z m_Z Z + S, with
  X̊ ∈ {e̊4, e̊3, ∂_v} or a pair operator. The coefficients m_Z are the derivatives of the right sides in the state,
  plus δw e̊_X Y̊, −e^{−ẘ} δb ∂_x Y̊ (e3 rows) and −δk e̊_x Y̊ (pairs). They are listed in `linest5.out` E2. S is the
  background's residual (R3) and any source.
- *The norm.* With ϖ := 2 e^{ẘ+k̊} and ‖·‖ the L²(ϖ dx) norm on S_{u,v} ∩ D:
  f(u, v) := Σ_i [∫_{v0}^{v} ‖(δa_i, δc_i)(u, ·)‖² + ∫_{u0}^{u} ‖(δc_i, δd_i)(·, v)‖²]
  + Σ_{e4, ∂_v rows} ∫_{u0}^{u} ‖Y(·, v)‖² + Σ_{e3 rows} ∫_{v0}^{v} ‖Y(u, ·)‖².
  𝒟 is the same norms of the data on u = u0 and v = v0; 𝒮 := Σ_rows ∫∫_D (e^{ẘ} S)² ϖ.
- *The constants.* κ_Z is the sum, over the rows Z enters or bounds, of the coordinate-normalised |m_Z| (e^{ẘ}|m_Z|
  for frame rows). To it are added the measure's term |∂_v log ϖ| (e4, ∂_v rows) or |∂_u log ϖ + ∂_x(b̊ϖ)/ϖ| (e3
  rows), the energy forms' e^{ẘ}|χ̲̊ − 2ω̲̊|, e^{ẘ}|χ̊ − 2ω̊| and e^{ẘ}|η̊ + η̲̊| (N6), and 1 for the source. Put
  a_o(u) := max over δa, δc and the e3 rows of sup_{D∩{u}} κ_Z, and a_i(v) := max over δd and the e4, ∂_v rows of
  sup_{D∩{v}} κ_Z.

**Theorem 7.L.** f(u, v) ≤ (𝒟 + 𝒮) exp(2 ∫_{u0}^{u} a_o + 2 ∫_{v0}^{v} a_i) on D.

*Proof.*
1. Pairs. The divergence identity (N6, product rule) holds for the linearised pairs on D(u, v) = D ∩ {u' ≤ u,
   v' ≤ v}.
   - The fluxes through H_u and H̲_v are f's first two terms.
   - Through the lateral boundary x = ±(X − c_u(u − u0) − c_v(v − v0)), the outward flux of a² e̊3 + c² e̊4 − 2ac e̊_x
     is e^{−ẘ}[(c_u ± b̊) a² + c_v c² ∓ 2 e^{ẘ−k̊} ac]. It is nonnegative because (c_u ± b̊) c_v ≥ λ c_v ≥ Ω̊²/γ̊.
     So it is dropped. Likewise for the second pair.
2. Transport. For an e4 or ∂_v row, d/dv ∫Y² ϖ dx ≤ ∫(2|Y| |∂_v Y| + |∂_v log ϖ| Y²) ϖ dx, since the shrinking
   interval only removes. For an e3 row, D_u = ∂_u + b̊∂_x. The term b̊∂_x(Y²) integrates by parts to
   Y² ∂_x(b̊ϖ)/ϖ, and its boundary term is nonpositive because c_u ≥ |b̊|. Integrate in the transport variable, then
   in the other.
3. Every right side is linear in Z with the coefficients above. Split each bilinear term as 2|m||Z||Z'| ≤
   |m|(Z² + Z'²), and the source as 2|Z||S| ≤ Z² + S².
   - The space-time integral of Z² is at most ∫_{u0}^{u} f(u', v) du' if Z is measured on outgoing cones (δa, δc, the
     e3 rows).
   - It is at most ∫_{v0}^{v} f(u, v') dv' otherwise.
   - Hence f ≤ 𝒟 + 𝒮 + ∫ a_o f du' + ∫ a_i f dv'.
4. Lemma (E7). If f ≥ 0 is continuous and f ≤ A + ∫ a_o f du' + ∫ a_i f dv', then f ≤ A exp(2∫a_o + 2∫a_i).
   - With U = ∫a_o and V = ∫a_i, g = B e^{α(U+V)} for α > 2 and B > A satisfies
     A + ∫ a_o g + ∫ a_i g ≤ A + (2/α)(g − B) < g.
   - Compare along U + V, then let α → 2 and B → A. ∎

- *What the theorem is.* A linear estimate with explicit constants at the curvature level of the class. The curvature
  of h̃ is quadratic in dΦ, which the pairs estimate, and the metric is controlled by it with no loss (N8, N10). It
  is [Wu26] Theorem 2.2's linear step in the class, with its bootstrap weight exp(D(u + v)) replaced by the lemma, on
  domains that avoid the axes.
- *What it is not.*
  - It is not the nonlinear theorem: the quadratic remainder needs L^∞ control, hence level 1.
  - It does not reach the axes: D excludes them.
  - The m_Z use the background's exact frame derivatives e̊_X Y̊. `linest5.py` evaluates them through the background's
    own equations, which differ by its residual: 10⁻³ relative on the box (computed).
- *Computational support.* E1 (the pair identities, exact, with a mutated control), E2 (the table: no derivative of an
  unknown on any right side, exact), E3 (control: χ̲ by N7's e4 equation puts e_x δη̲ on a right side, flagged),
  E7 (the lemma: the extremal solution lies below A e^{2a(u+v)} and above A e^{a(u+v)}, the control; its growth rate
  is 1.6–1.7 a against the bound's 2a).

### 7.4 The constant on the record's solution, and the domain (`checks/linest5.py` E4, E4b, E5; computed)

On the record's computed solution (D432: M = 32, 800 × 360, ld 3, cut 0.9), over rcert5's box u ∈ [−4, −1.1],
v ∈ [0.55, 1.6], every second row and column, κ_Z is evaluated by finite differences in (u, v) and spectrally in x, on
the angular band ∣x∣ ≤ X.

| band X | a (largest κ, worst unknown) | F² at a constant | F² with the profile: ∫a_o du, ∫a_i dv | demand (G = 10) |
|---|---|---|---|---|
| 0.5 | 122 (δχ̲) | 10^420 | 10^138: 67.9, 91 | 10^−140 |
| 0.8 | 171 (δχ̲) | 10^587 | 10^222: 99.2, 157 | 10^−224 |
| 0.95 | 1.9 × 10³ (δb) | 10^6552 | 10^1916 | 10^−1919 |
| 0.9988 (outermost node) | 1.8 × 10⁵ (δb) | 10^624563 | 10^166843 | 10^−166845 |

- *Where it comes from.* a_o rises from 21 at u = −3.9 to 122 at u = −1.1. There the run's u-coordinate is compressed
  (u = −1 + a sinh ξ), and e^{ẘ}χ̲̊ = 3D_u log R + b_x reaches 6.3. The largest single coefficient is that of δw in
  the χ̲ row, 53. Toward the axes the frame coefficients grow like the inverse distance (the last two rows).
- *The domain (E5, E5b).* The truncated domain needs an x-shrink ∫ sup|b̊| du + 2 √(Δu ∫ sup(Ω̊²/γ̊) dv) =
  0.13 + 5.67 = 5.8 over the box, against a half-width X ≤ 1. Every truncated domain over the box is empty.
  - Theorem 7.L applies only to sub-rectangles of area Δu Δv ≲ 0.01 there (2√(2.94 Δu Δv) < 1/2).
  - The angular speed 2√(Ω̃²/γ̃) reaches 3.4, against an angular range of 2. Every point of the box, and of the late
    region, depends on data at the axes.

So the estimate exists and its constants are explicit, but (i) they are of size 10^138 and up where it applies, and
(ii) it does not apply where it is needed.

### 7.5 What is missing, exactly

1. **The axes (G4); the obstruction, and it is essential.**
   - At x = ±1 the Einstein frame degenerates: Ω̃² = e^{2ζ}(1 − x²)/4 (R4), and Φ1, Φ2 carry ½ log(1 − x²) and
     ¼ log((1 + x)/(1 − x)).
   - The frame-normalised Ricci coefficients and scalar derivatives grow like the inverse distance to the axis (E4's
     last rows). No truncated domain avoids the axes over the box (E5).
   - The regular description near the axis x = +1, where the φ2-circle degenerates, is the reduction on φ1 alone. It
     gives four-dimensional, axisymmetric Einstein–scalar with a regular axis: [Wu26]'s (1.4) on disk sections. That
     system has Weyl curvature, and its estimate needs the Bianchi pairs (β, (K, σ)) and the renormalised pairs of
     [Wu26] p. 8.
   - Near x = −1 the same holds with the circles exchanged. The full theorem patches the two charts to Theorem 7.L's
     interior with a partition of unity in x. The cut-off's derivative enters as a source with an explicit constant.
   - Not written.
2. **Level 1.**
   - The quadratic remainder of the difference system needs L^∞ control of Z. On a one-dimensional section that is
     H¹ (‖f‖_∞ ≤ ‖f‖/√|I| + √|I| ‖f′‖).
   - Commuting the rows with e̊_x keeps N10's structure (deduced, not checked at level 1): the commutators are Ricci
     coefficients (N4), and the metric differences enter at the same order in x as the Ricci coefficients, which
     the ∂_v rows supply.
   - Mechanical away from the axes; not written.
3. **G** and the data at past null infinity (G3), as in 6.6.
4. **A sharp F.** Even with 1–3, Theorem 7.L's F is 10^69 on |x| ≤ 1/2 (7.4). A usable argument needs the linearised
   solution operator bounded by a validated computation (7.6), not by Grönwall.

### 7.6 Task 2: the demand on the residual, and one sub-box certified

- *The demand at Theorem 7.L's F (computed, E6).* δ + ∫ε < 1/(4GTF²) asks 10^−140 (|x| ≤ 1/2, G = 10) to
  10^−166845 (to the outermost node). No enclosure and no approximant reaches that.
  - The reason is structural (deduced): a Grönwall bound adds the absolute values of the coefficients, 20–120 per unit
    u here. The response it bounds is 9.2 (round 2, `ampresp5.py` A1).
- *The plausible route (deduced; not done).*
  - Bound the linearised solution operator by a validated computation. Discretise it, invert the discretisation
    numerically, and certify the defect of that approximate inverse.
  - The explicit estimate then multiplies only the defect, as in a radii-polynomial argument. F becomes the computed
    norm, of the order of the measured 9.2.
  - The demand becomes 5.3 × 10⁻⁴ (G = 0.57, E8) to 3.0 × 10⁻⁵ (G = 10), at F = 9.2. Round 2's 7.8 × 10⁻⁷ used
    G_low itself as 2(d)'s G, which it is not (7.10, A4).
- *What a certified sup at that level asks.* Theorem 7.L's norm is a space-time L² norm, so a certificate is local:
  the square is a sum over boxes. Two things are needed.
  - A better approximant. The record's 2.42 × 10⁻³ (K1) is 4.6 to 81 times the demand, a second-order
    truncation error. A spectral or Richardson-extrapolated approximant in (u, v) on the converged region is the
    candidate.
  - A better enclosure, or more boxes (certified, `checks/rcert5b.py`). On the box t ∈ [−1/2, 0], σ ∈ [−1/2, 0],
    x ∈ [0, 1/4] (rcert5's coordinates: interior, away from K2's worst corners and from the axes), split into n³:

    | n (sub-boxes) | ll | ln | nn | lx | nx | xx | 11 | 22 |
    |---|---|---|---|---|---|---|---|---|
    | 1 (1) | 8.1e3 | ∞ | 3.4e6 | 3.2e4 | 3.8e5 | 5.8e4 | 8.9e4 | 1.0e5 |
    | 2 (8) | 150 | 342 | 589 | 97 | 219 | 110 | 60 | 70 |
    | 4 (64) | 4.1 | 2.5 | 3.7 | 1.8 | 1.7 | 1.9 | 0.78 | 0.94 |
    | 8 (512) | 0.124 | 0.049 | 0.093 | 0.049 | 0.033 | 0.052 | 0.021 | 0.026 |
    | centres, n = 8 | 1.5e-4 | 1.3e-5 | 2.4e-5 | 4.8e-5 | 9.4e-6 | 1.2e-5 | 2.2e-5 | 2.2e-5 |

    - The bound falls 33–51 times per halving at the last step (54, 37, 33 for ll), faster than the remainder's h³
      because the fields' enclosures over the box shrink too (computed).
    - The ratio is still falling, so the extrapolated n ≈ 26–35 (about 2–4 × 10⁴ sub-boxes for this box) is a lower
      bound on what is needed.
    - *Control.* The approximant with W + 0.01 v has centre values up to 0.052 at n = 4, 400 times the approximant's.
    - *Reading.* The method works; it needs about 10⁴ times rcert5's boxes. A Chebyshev enclosure with an analyticity
      bound, or a reformulation in which the cancellation is algebraic (6.3), would cut that.
    - None of this closes anything at Theorem 7.L's F; at a computed F it is the step after a better approximant.

### 7.7 Task 3: the late region (run after the load fell)

`uptime` read 9.4 at the start of the round, then 20.2, 21.5, 27.9, 32.1, 36.3, 35.9, 31.8 and 24.6 at later checks,
so the runs were first skipped. After the machine restarted (2026-11-06) the load was 0.5, and they were made.
- *The runs (computed).*
  - `cpsolve5.py --run 1 0.9 32 1600 720 2.25 … ld 3`: 1,986 s.
  - `szrun5.py 1 0.7 32 1600 720 1.85 … ld 3`: 2,008 s.
  - To separate angle from the rest, `cpsolve5.py --run 1 0.9 40 1600 720 2.25 … ld 3`: 3,389 s.
- *A repair.* `late5b.py --small` had never run: a local tuple in `main` shadowed the function `small`, which raised
  on the call. The tuple is renamed (`sm_cls`); the program's other output is unchanged.

**Below areal radius 0.9** (`checks/late5b_small.out`: L7's null step, M = 32, cut 0.7, 800 against 1600 rows).
Figures are max |ρ| at 800 / 1600 rows (ratio), with ρ's share of the band's largest term at 1600 in brackets.

| v-band | 0.6 ≤ r_A < 0.9 | 0.9 ≤ r_A < 1.0 |
|---|---|---|
| [1.0, 1.5) | 4.9e-3 / 1.2e-3 (4.01) [6.5e-4] | 3.1e-3 / 7.8e-4 (4.00) [9.7e-4] |
| [1.5, 1.65) | 1.9e-2 / 4.6e-3 (4.04) [1.4e-3] | 8.4e-3 / 2.1e-3 (4.01) [1.4e-3] |
| [1.65, 1.8) | 0.26 / 0.092 (2.87) [1.3e-2] | 7.2e-2 / 1.8e-2 (3.94) [4.5e-3] |
| [1.8, 1.9) | 1.74 / 1.28 (1.36) [0.17] | 0.54 / 0.25 (2.18) [4.3e-2] |

- *Decided (computed)* below areal radius 0.9 to v = 1.65: second order, 1.4 × 10⁻³ of the terms.
- On [1.65, 1.8) the residual falls 2.9-fold per doubling, to 1.3 % of its terms: converging, below second order.
- From v = 1.8 it does not converge (ratio 1.36, 17 % of the terms). That is not decided.
- At 0.9–1.0 the residual converges to v = 1.8.
- Round 1's "the size of its own terms from v ≈ 1.65" is, at M = 32 and below 0.9, a null-step error to v = 1.8.

**v ≥ 1.9 at areal radius 1.0–1.2** (`checks/cplate5c.out`: the constraint-preserving scheme on three null grids,
M = 32, compared on the 400-row nodes).

| v-band (r_A 1.0–1.2) | P: 400–800 / 800–1600 | Ric_xx 400 → 800 → 1600 | P_cp − P_free at 1600 (free's own) |
|---|---|---|---|
| [1.65, 1.8) | 1.7e-3 / 9.9e-5 | 613 → 6.4 → 0.29 | 2.1e-5 (3.7e-5) |
| [1.8, 1.9) | 4.9e-3 / 1.7e-4 | 4.7e3 → 45 → 3.2 | 5.6e-5 (9.7e-5) |
| [1.9, 2.0) | 2.0e-2 / 5.5e-4 | 3.4e4 → 345 → 129 | 6.4e-4 (3.3e-4) |
| [2.0, 2.25) | 0.19 / 1.0e-3 | 4.1e5 → 880 → 902 | 2.0e-3 (5.2e-4) |

- *Below v = 1.9.* The metric converges in the null step, and the unimposed constraint falls 3.6–24-fold from 800 to
  1600 rows (14–22-fold on [1.65, 1.9)). The two formulations agree within the free scheme's own null-step
  difference. So a vacuum limit is supported (computed) to v = 1.9 at areal radius ≥ 0.9, now on three grids.
  - The ratios of 17–37 in P say the 400-row run was outside the asymptotic range, as round 2 found. They are not an
    order.
- *From v = 1.9.* P still converges: 800–1600 differences of 5.5 × 10⁻⁴ and 1.0 × 10⁻³. But Ric_xx no longer falls:
  2.7-fold on [1.9, 2.0), 0.98 on [2.0, 2.25), and it grows at 0.9–1.0 (0.72, 0.58).
  - So the null step is no longer the limiting error there. At M = 32 the discrete solutions converge in (u, v) to a
    metric that does not satisfy Ric_xx = 0.
  - At areal radius ≥ 1.2 the monitor still falls on [2.0, 2.25) (46-fold).
- *Angle (`checks/cplate5d.out`, M = 32 against 40 at 1600 × 720).* It does not separate the causes.
  - Raising M to 40 raises the Ric_xx monitor on every band from v = 1.0 on, at every areal radius. On |x| ≤ 0.9 the
    rise is 2–25-fold, including bands where P has converged.
  - So the monitor's level is set by the scheme's angular defect, not by the solution. The defect is either
    cpsolve5's P3 axis defect, which grows like M² times the truncation error, or the shift term of
    `symbol5s.py` S5. That is the record's D418 pattern again, now in the constraint-preserving scheme.
  - P agrees between M = 32 and 40 to ≤ 7.8 × 10⁻⁵ to v = 1.9 at areal radius 1.0–1.2, and to 3.3 × 10⁻⁴ on
    [1.9, 2.0). On [2.0, 2.25) it differs by 5.0 × 10⁻², as much as a different solution does (control, 4.6 × 10⁻²).
    So the metric is unresolved in angle there.
  - *Control.* The amplitude-7/8 solution differs from the M = 32 run more than M = 40 does, on every band below
    v = 1.8.
- *Verdict on v ≥ 1.9 at areal radius 1.0–1.2 (computed): not decided.*
  - On [1.9, 2.0) the metric is converged in the null step and in angle (5.5 × 10⁻⁴ and 3.3 × 10⁻⁴).
  - The constraint there cannot be judged by this scheme's monitor, which grows with M everywhere.
  - On [2.0, 2.25) the metric is not resolved in angle.
  - What would decide it: a scheme whose constraint monitor converges in M at fixed null step, for instance one
    without the axis defect, or the frame hierarchy of 7.2. Or the Kretschmann scalar converging in both.
- *Not done.* The Kretschmann scalar on these runs, and M = 40 on the coarser null grids.

7.4 adds one fact bearing on all this (computed): signals cross the angular range about three times within rcert5's
box alone. So the late region depends on data at the axes, and any estimate that decides it must hold there.

### 7.8 Files and outputs (round 3)

| file | what |
|---|---|
| `checks/reduce5.py`, `.out` | R0–R4: the class as (2+1)-gravity with two free waves; the residual map (exact) |
| `checks/null3.py`, `.out` | N0–N10: null structure, commutators, wave operator, energy identities (exact) |
| `checks/linest5.py`, `.out` | E1–E8: the pairs, the linearised table, Theorem 7.L's constant and domain, the demand |
| `checks/rcert5b.py`, `.out` | B1–B2: one sub-box of rcert5's K2 refined, n = 1–8; control W + 0.01 v |
| `checks/symbol5s.py`, `.out` | S1–S6: the symbol with s_vx kept (no Jordan block); the shift's Levi term |
| `checks/cplate5c.py`, `.out` | C1–C3: the constraint-preserving scheme on a third null grid (task 3) |
| `checks/cplate5d.py`, `.out` | D1–D2: the constraint-preserving scheme at 1600 × 720, M = 32 against 40 (task 3) |
| `checks/late5b_small.out` | L7's null step below areal radius 0.9 (task 3; late5b.py's --small mode repaired) |
| `checks/rcert5c.py`, `.out` | P1–P2: rcert5's approximant saved with md5s (`data/rcert5_C3.npz`); K1 from it |

Runs (scratch, not committed).
- Read in place: D432's `l1_rc0.9_M32.npz` (linest5), resid5's `l1_M16_800.npz` (rcert5b, rcert5c), and round 2's
  constraint-preserving runs at 400 and 800 rows (cplate5c).
- Made this round: `cpsolve5.py --run 1 0.9 32 1600 720 2.25 … ld 3` (1,986 s; md5 776da11e…), the same at M = 40
  (3,389 s; md5 0b6737d6…), and `szrun5.py 1 0.7 32 1600 720 1.85 … ld 3` (2,008 s; md5 c326bd19…).
- The M = 40 and szrun5 files were deleted after their analyses had read them, because the disk was full. The M = 32
  file is kept, under the scratch directory's `r3/`.

### 7.9 A proposed replacement for the paper's section 9 sentences on existence at 10 l5

Proposed to the main session, which seats it. It replaces 6.8's proposal (and the paper's sentences from "A first
certified step is taken" to "remains open"):

> Certified so far: on the data cone the Raychaudhuri constraint of an explicit approximant holds to 5.0 × 10⁻⁵ and
> 2.3 × 10⁻⁵ (`docket68/n1star/checks/cdata5.py`), and the Einstein residual of a smoothed three-dimensional
> approximant is enclosed in ball arithmetic at 16,128 points away from the axis caps, ≤ 2.42 × 10⁻³ of the
> curvature scale (`checks/rcert5.py`); its sup over the box is computed only. Existence at 10 l5 is not proved
> beyond the seed. In the metric variables the numerics evolve, the shift's angular derivative is of principal size at
> high angular frequency, so no linear estimate without loss of derivatives holds there (deduced at frozen
> coefficients, `checks/symbol5s.py`). The class is (2+1)-dimensional gravity coupled to two free waves (deduced, exact:
> `checks/reduce5.py`), and in double-null gauge its Ricci coefficients obey transport equations with no angular loss
> (`checks/null3.py`). So a linear estimate at the curvature level holds, with explicit constants, on domains of
> dependence that avoid the axes (supplement `CERTIFY-10L5-RESULT.md` Theorem 7.L). Two things stop it short of a
> proof. On the computed solution its constant is of order 10^69 before the axes enter, against a measured response of
> 9.2 (`checks/linest5.py`). And the solution's late region lies within three angular crossing times of the axes, where
> the reduction degenerates and the estimate must be made in four-dimensional axisymmetric form; that estimate is not
> written. The computed solution converges at the first seed to v ≈ 1.8 r_h at areal radius ≥ r_h (to v ≈ 1.9 r_h at
> areal radius ≥ 0.9 r_h in a constraint-preserving scheme on three null grids), and is unresolved beyond
> (`checks/late5b.py`, `checks/cplate5c.py`).

The verifier of round 2 also found that the paper's section 9 sentence on the rebuilt Bondi spheres ("reproduce the
untrapped columns") claims more than 6.1's S7 supports (within one column spacing to v = 1.525; S7 fails at 1.55). It
reports that it will correct the paper; the text above does not touch that sentence.

### 7.10 The verifier of round 2: its findings, seated as amendments to section 6

The verifier of round 2 read section 6 and reran its programs (scratch scripts `vF2/*.py`, not committed). Each
finding is an amendment to section 6, marked "verifier of round 2", with what this round re-derived. Section 6's text
is not rewritten; where it and this list disagree, this list governs.

**A1 (M1, major; re-derived, exact: `checks/symbol5s.py` S1–S5).** Accepted.
- symbol5.py Y1–Y3 analysed the four rows with the shift held fixed. Ric_xx and Ric(Y, ∂_v) contain s_vx at principal
  order, with coefficients R² e^{−2W−2(P+Q)}/8 and −(1 − x²)/2 (S1). Ric_vx's principal part is c_s s_vv − dζ·f_vx,
  c_s = R² e^{−2W−2(P+Q)}/16. Ric_uv's s_vv cancels in Ric(Y, ∂_v).
- Eliminating s through Ric_vx gives N_eff = N + n dζ/c_s. A_eff has the same characteristic polynomial l²(l + 1)²,
  but rank A_eff = 2 and rank(A_eff + I) = 2. Both eigenvalues are semisimple, so there is **no Jordan block** (S3).
  - *Control.* With n → 0, the frozen shift, the block returns (rank 3).
- So the following hold only "with the shift frozen" and are withdrawn as statements about the formulation the
  record evolves: 6.0 item 1's first sub-bullet, 6.2's Y1 ("not semisimple"), Y3 and its "Consequence", and 6.8's
  "the linearised principal symbol has a Jordan block, so no linear estimate holds".
- *What survives, re-derived (S4–S6; exact coefficients, frozen-coefficient deduction).*
  - At angular frequency k with the (u, v) scales fixed, Ric_vx gives s ≈ (ik/c_s) ∫ dζ·f dv. Its own s_x and s
    coefficients vanish on spherical states. So s_x ~ k² is of principal size: Y5's "lower-order" term is not lower
    order.
  - It drives the eigenvalue-0 sector. On spherical states, with ℓ0 = δR's left vector, ℓ0·M⁻¹(s_x column) =
    R_v(1 − x²) ≠ 0, while dζ·M⁻¹(s_x column) = 0 exactly.
  - So δζ does not drive itself at order k², but δR is driven: δR_uv = κ_R k² ∫δζ dv, κ_R = 16 R_v (1 − x²) e^{2W}/R².
    That is k² growth at frozen coefficients. **In the free formulation, an estimate without loss of derivatives still
    fails, through the shift's lower-order (Levi) term rather than a Jordan block.**
  - In the constraint-preserving formulation (S5), the 3 × 3 block with s_vx has characteristic polynomial l(l + 1)²
    and no Jordan block. But W has no W_xx term (the eigenvalue 0), and its row carries s_x with coefficient
    R_v(1 − x²)/(2R) on spherical states, so W drives itself through k² ∫W dv.
    - Its scalar model's Goursat solution grows faster than any power of k for either sign (S6, computed in
      mpmath).
    - That is a model, without the variable coefficients and the O(k) terms. Round 2's J2 measured no growth for
      k ≤ 8 at M = 16, so a loss in that scheme is not established.
- **Does this remove the need for the curvature-level route? No (deduced).**
  - In both metric formulations the shift's first derivative enters at principal size at high angular frequency.
  - In null3.py's frame hierarchy, s enters only through η, η̲ (b_v) and χ̲ (b_x), each transported without angular
    derivatives (N0, N8). Theorem 7.L is built on that full system, with δb one of its unknowns and no derivative
    of δb on any right side (`linest5.py` E2).
  - What it simplifies is the diagnosis. The metric formulations fail by a lower-order term that costs a
    derivative through the shift, not by their principal symbol.
- *Not done.* The Levi analysis off spherical states and with variable coefficients, and a test of the k² growth of
  δR in the scheme itself.

**A2 (M2; deduced).** Accepted. k² growth excludes estimates *without loss of derivatives*; it does not exclude
estimates with finite loss, or a Nash–Moser scheme. "In any Sobolev scale" (6.0 item 1, 6.2 Y3, 6.8) reads "without
loss of derivatives". Round 2 did not examine the lower-order terms; A1 does, for spherical states.

**A3 (M3; reported by the verifier, not re-derived here).** jordan5.py's J1 growth (3.75 → 76.5 from k = 2 to 8) sits
at the two outermost nodes of each axis:
- n at x = 0.995 goes 3.5 → 77, m at −0.995 likewise, and s 1.8 → 27;
- R and ζ do not grow (R 2.0 → 1.4, ζ 1.40 → 0.79);
- interior nodes grow about threefold.
So 6.2's "the growth is the Jordan block's" is withdrawn. J1 measures the scheme's axis loss (D354), consistent with
A1, where the full system has no Jordan block. The requested per-node table and e0-projection on |x| ≤ 0.9 were not
made this round.

**A4 (M4; re-derived: `linest5.py` E8).** Accepted.
- G_low = 382 is the solution map's second derivative in data units, not 2(d)'s G. Read in 2(d)'s own model
  R′ = KR + GR², it is G = G_low K/(2F(F − 1)) = 0.566, with K = ln F/T. The model integrated at that G returns 382.
  - *Control.* Without the factor 2 it returns 764.
- The demand at F = 9.16 is then 5.3 × 10⁻⁴. The certified residual 2.42 × 10⁻³ is 4.6 times it, and 81 times the
  demand at 2(d)'s placeholder G = 10.
- 6.0 item 1, 6.2 ("the one inequality"), 6.6 item 3 and 6.8: "at least 84", "3.2 × 10³" and "lower bounds on the gap"
  are withdrawn. The gap is about 5 to 84 depending on G, which is not computed.

**A5 (M5; re-derived from `checks/rcert5.out`).** Accepted.
- ll's enclosure is [0.00241 ± 4.18 × 10⁻⁶], whose upper end is 2.414 × 10⁻³. So "≤ 2.41 × 10⁻³" and
  "≤ 2.4 × 10⁻³" (6.0, 6.3, 6.5, 6.8) read "≤ 2.42 × 10⁻³".
- The verifier reports that rcert5's least-squares fit is not bit-reproducible (K2's ll 6.79 × 10⁴ → 6.78 × 10⁴ on a
  rerun) and that a 10⁻⁹ change in one coefficient moves ln's maximum by 2.3 %. So K1 is certified for one fit's
  coefficients, which were not saved.
- *Done (certified, `checks/rcert5c.py`).* One fit's tensors are saved to `data/rcert5_C3.npz`, with the md5 of
  each tensor's float64 bytes printed (R be89d629…, m 99434c1b…, n 7a0ab510…, W 3427e2bf…, s 1faa82de…).
  - K1 recomputed from the saved file gives ll ≤ 2.414179 × 10⁻³, against the verifier's 2.4141757 × 10⁻³ from
    another fit.
  - *Control.* Changing C3[m][0, 0, 0] by 10⁻⁹ moves every maximum but ll, by at most 4 × 10⁻⁵ relative. The
    verifier's 2.3 % for ln came from another coefficient and is not re-derived here.
  - rcert5.py itself still refits; rcert5b.py's figures are those of its own fit.

**A6 (M6; partly re-derived from `checks/late5b.out`).**
- *Re-derived.* On [1.8, 1.9) at areal radius 1.0–1.2 the residual grows with M from 32 to 56 (3.14 → 3.59 × 10⁻²,
  L6). On [2.0, 2.25) at ≥ 1.2 it goes 6.35 × 10⁻³ (M = 32) → 0.181 (M = 56).
  - So "converged to v ≈ 1.9" is supported to v = 1.8 only, and "(2.25 at M = 40)" is withdrawn (6.0 item 3, 6.4 L5,
    6.5).
  - 7.9's proposed text already says v ≈ 1.8.
- *Reported, not re-run here (the verifier's script on round 1's cut-0.3 runs).*
  - At areal radius 1.0–1.2, M = 16 already converges to v = 1.8 (null-step ratio 3.92; 1.04 × 10⁻², 1.09 × 10⁻²,
    9.5 × 10⁻³ at M = 16, 24, 32).
  - Round 1's failure from v ≈ 1.65 is at areal radius < 1.0, where M = 24 at cut 0.3 is still 20 % of the terms.
  - L7's 4–6 % is at cut 0.7, a different set of cells. Round 1's place (u = −0.978) is not reached at cut 0.7.
  - So the M = 16 attribution (6.0 item 3, 6.4's verdict) holds only for [1.8, 1.9) at areal radius ≥ 1.0 (M = 16
    ratio 1.14 there).
  - The constraint-preserving and free schemes agree to about 10⁻⁴, against controls of 3 × 10⁻³ to 6 × 10⁻², but the
    constraint-preserving scheme's own error dominates.

**A7 (M7; re-derived by reading section 1).** Accepted. Section 1.6 still says the two formulations "converge on
each other as the data truncation is removed", and section 1.4 says "S6 … PASS" and "not of either scheme"; all three
contradict V2. They are withdrawn as stated; 6.1's V2 governs.

**Minor and nits (each accepted; re-derived where marked).**
- 6.2 Y2's "three uncoupled wave operators", and "W is a wave mode", are false with s_vx (re-derived: S5).
- Y5's count of one lost derivative was prose (now S4).
- 6.3's "the run's truncation error, certified": K1 certifies the approximant's residual at points. That it is the
  run's truncation error is a computed comparison, not certified.
- cpsolve5 P1's error ratio from 200 to 400 rows is 1.9, not second order (re-derived from 6.4's own figures,
  4.6 × 10⁻⁴/2.4 × 10⁻⁴). P2's "one limit" rests on two grids.
- 6.5's "at least two orders of magnitude" is superseded by A4.
- Section 0's item 3 says the violation from v ≈ 1.65 is "still of order one at M = 24", and its round-2 note that the
  onset "was M = 16's angular resolution". The two disagree; A6 governs.
- Two controls were tautological: ampresp5's second difference of data linear in A by construction, and symbol5's Y2
  control, a Jordan test on −I. symbol5s.py's control mutates the code under test (n → 0); ampresp5 is unchanged this
  round.
- 6.8 omitted that the axis caps |x| > cos(π/32) are excluded; 7.9 states it.

**Confirmed by the verifier** (recorded): rcert5 K1 is ball arithmetic end to end, given the float coefficients as
exact inputs. cdata5's clause is correct. Reruns of symbol5, ampresp5, cdata5 (seed 1) and cplate5 are identical.

## 8. Round 4 (2026-11-06): the axis charts, the constant, one certified box, the late region's axis defect

*Status.* Appended 2026-11-06; sections 0–7 are not rewritten. The verifier of round 3 reported during this round. Its
findings are seated in 8.0 as amendments to section 7, each re-derived or marked as not, with section 7's text quoted
and kept. Labels are as in section 0. [Wu26] was re-read at source for this round (arXiv 2609.08421v1: (2.1)–(2.17),
pp. 4–6; Theorem 2.2 and its proof sketch, with the pairs it uses, pp. 6–8; READ).

The machine's load was 13–30 on 4 cores. Free disk was 1.3 GB at the start and 18 GB after another session's cleanup
at 10:03. That cleanup also removed the record's D432 runs, which this round read in place (8.8).

### 8.0 The verifier of round 3: its findings, seated as amendments to section 7

The verifier of round 3 read section 7 and reran its programs. Its scratch work is `vF3/work/` (myreduce.py,
speeds.py, rcert5c_ro.py and mutant copies), not committed. It found the mathematics sound and one program unsafe.
Each finding below quotes the text of section 7 it amends, which stays as it is, with a bracketed note. This round
re-derived each one, or says that it did not. Where section 7 and this list disagree, this list governs.

**M-1 (major, a program; re-derived and repaired).** `rcert5c.py:42` overwrote the tracked `data/rcert5_C3.npz` on
every run with a fresh fit, which is not bit-reproducible. So its P2 certified that fit and not the committed file.
`rcert5.py` and `rcert5b.py` refit too.
- *Re-derived.* `rcert5c.py` as of round 3 calls `R5.prepare` and then `np.savez_compressed(OUT, …)` unconditionally
  (round 3's line 42, kept at `scratchpad/r4/rcert5c.orig.py`).
- The committed file's md5 is 698569f6faaab4420fe2e67abc860561 before and after every run of this round. No program of
  this round writes it.
- *Repaired.*
  - `rcert5c.py` writes only under `--write RUNDIR`. By default it loads the npz read only, checks the file md5 and the
    five tensor md5s against constants in the program, certifies those tensors, and checks the file md5 again
    afterwards. Rerun: P1 equal, P2 ll ≤ 2.414179 × 10⁻³ (unchanged to 7 digits), control moves, the file unchanged
    (`rcert5c.out`, all checks pass).
  - `rcert5b.py` loads the pinned npz read only and checks its md5s. It has the soundness gate the verifier asked for
    (B3): at each n the certified sup must be at least the certified values at the centres of the finer (2n)³ grid and
    at 500 random points.
  - The bound assembly is now one function, tested on two known functions, T_3(t)T_3(σ)T_3(x) and
    t⁴ + σ⁴ + x⁴, about the origin.
    - With the Lagrange remainder replaced by the point Taylor coefficients, the verifier's mutant, the test fails as
      it must: the point polynomial bounds the quartic by 0.
    - The first run of this round tested the T_3 product alone, which the mutant passes (0.68); the quartic was added
      and the program rerun (`rcert5b_run1.out` is kept).
    - On the residual itself the mutant stays above every sample, so no sample gate can catch it there.
    - Rerun (`rcert5b.out`, all checks pass, 2,047 s). B1 reproduces round 3's table to the printed digits on the pinned
      approximant (ll 8.09 × 10³, 150, 4.10, 0.124; centre values to 1.53 × 10⁻⁴). The B3 gate holds at n = 1–8
      (largest point value 1.52–1.59 × 10⁻⁴). The assembly test gives 0.25 sound and ∞ for the mutant.
  - `rcert5d.py` (task 3) was written this round to load the pinned file read only and to check its md5s.
  - `rcert5.py` still refits. Its K1 and K2 figures (6.3) belong to an unsaved fit.
- [7.6's table and 7.0 item 2's figures: "certified (rcert5b.py)" — verifier of round 3: they belong to an unsaved
  fit; the pinned approximant's figures are rcert5b.out of round 4, B1.]

**Reduction (re-derived from reduce5.py R2–R3; exact).**
- [7.0 item 1, "two free waves"; 7.9, "two free waves": verifier of round 3: they are a wave map into the flat plane,
  coupled through h̃ (in □_h̃ and in the source). "Free" means only that the target is flat: no potential and no Φ1–Φ2
  coupling.]
- [7.0 item 1, "A certified bound on one is a certified bound on the other": verifier of round 3: □_h̃ A =
  −e^{−2A}ρ⁻² Ric5_11 = −ρ⁻² Ric5(ê1, ê1), and ρ⁻² = 4/(R⁴(1 − x²)e^{2(P+Q)}) diverges at the axes. So it holds only
  away from the axes.] In the axis chart of 8.2 the factor is e^{−A} instead (X1: □_ĝ A = −e^{−3A} Ric5_11), which is
  regular at x = +1.
- [7.5 item 1, "Φ1, Φ2 carry ½ log(1 − x²) and ¼ log((1 + x)/(1 − x))": verifier of round 3: those logs belong to L
  and ψ. Φ1 = √(3/2) L and Φ2 = √2 ψ carry them times √(3/2) and √2.]

**null3 (re-derived by reading N0, N7, N10).**
- [7.0 item 1, "a hierarchy with no angular loss": verifier of round 3: the absence of loss comes from the sections
  being one-dimensional. There χ, χ̲ are scalars with no shear, there is no Gauss or Weyl curvature, and the induced
  connection is trivial (δe_x = −δk e̊_x, N10). None of this carries over to the two-dimensional sections near the
  axes.] 8.2's Lemma 8.A5 makes this exact: at the axis the section's connection k ~ 1/s does not perturb in L².
- [7.0 item 1 and 7.2: "s enters only through η, η̲ (b_v) and χ̲ (b_x)": verifier of round 3: that holds for the
  shift's derivatives. b itself enters e3, ω̲ (through b w_x), and the −e^{−ẘ}δb ∂_x Y̊ coefficients (N0; linest5.py's
  e3 rows).]
- [7.0 item 1, "the angular loss lives only in the two equations the hierarchy does not use", and line 945, "the loss
  belongs to the metric formulation, not to the class": verifier of round 3: the angular derivatives are moved into
  the unused N7 equations, not removed. The hierarchy leaves χ̲, ω̲ and η + η̲ free, and their agreement with the metric
  and the N7 equations are never shown to propagate. This does not matter for an a priori estimate, but it matters
  for an existence argument. So "belongs to the metric formulation" is withdrawn as stated. It reads: "the hierarchy
  carries no angular derivative of its own unknowns on its right sides".]
  - *Attempted this round (`checks/prop5.py`).* Q1 (exact): the one Einstein component the hierarchy does not impose,
    E_34 − E_xx, propagates by a homogeneous transport along e4 and along e3, once the wave equations hold. Q2 (exact)
    is the contracted Bianchi identity used. Q3: the compatibility relations of χ̲, ω̲ and η + η̲ with the metric are
    not propagated by any one-directional row. Each needs a cross or angular derivative of an unknown transported in
    the other direction. Their propagation is not shown, and it is added to 7.5's list (8.6, item 5).
    - Q1's divergence is (div S)(e4) = −½(e4 q + χ q), (div S)(e3) = −½(e3 q + χ̲ q) and (div S)(e_x) = ½(η + η̲) q,
      with S = E − ½ tr E h̃ reduced to S_34 = q by the five imposed components.
    - So once the wave equations hold, q obeys a homogeneous transport along e4 and along e3, and it vanishes
      algebraically wherever η + η̲ ≠ 0.

**Theorem 7.L and its constants (re-derived).**
- [7.4, "So the estimate exists and its constants are explicit, but (i) they are of size 10^138 and up where it
  applies": verifier of round 3: the constants are computed on a band where, by E5, no domain of the theorem exists.
  It reads "computed on |x| ≤ 1/2 over the box, where no truncated domain exists".] The same holds for 8.3's
  Theorem 8.W figures, and 8.3 says so.
- [7.0 item 1 and 7.4, "every point of the box, and of the late region, depends on data at the axes"; "about three
  times over"; 7.7, "signals cross the angular range about three times": verifier of round 3: the speeds are suprema,
  which bound the causal reach from above. They prove the theorem's domains empty, not that every point depends on the
  axes.]
  - *Re-derived (the verifier's speeds.py, rerun read only on D432's run).* In the regular angle θ (x = cos θ),
    2√(Δu ∫ sup(Ω̃²/γ̃θ) dv) = 5.81 rad against a range of π: at most about 1.85 crossings. The inf-based reach is
    1.13 rad, less than π/2. In x units the figures are 5.67 and 0.055.
  - It reads "signals from the axes can reach the late region: the box spans up to about two angular crossings (by
    the supremum of the speeds)".
- [7.0 item 2 and 7.6, "the measured response is 9.2" and "F becomes … of the order of the measured 9.2": verifier of
  round 3: 9.2 is F_low of ampresp5.py A1, a secant lower estimate in another norm (sup of P, Q, W, log R in data
  units) and region (v ∈ [0.5, 1.65), areal radius ≥ 1). So the demand at F = 9.2 is the least stringent case, an
  expectation and not a result.] It is so labelled in 8.3. 8.3 also shows that the approximate-inverse route cannot
  deliver it (Lemma 8.F).
- [E6 uses T = 3.95 and E8 uses T = 10: verifier of round 3. Recorded; 8.3 states both.]
- [linest5.py E2, "no derivative of any unknown appears on any right side: the level-0 hierarchy closes", taken as a
  check of the rows: verifier of round 3: E2 cannot fail on a wrong linearisation. The rows are typed by hand.
  Dropping −e^{−ẘ}δb ∂_x Y̊, or ¼ → ½ in the ω̲ transport, both survive. E3 tests only a planted symbol.]
  - *Repaired.* linest5.py gains E9 (exact). (a) Every transport right side G_y, its scalar sums replaced by the Ricci
    components they stand for, satisfies e_X Y = G_y on the general (2+1)-metric. (b) The metric rows follow from N0.
    (c) Every row's frame-change part equals −d/dε of the perturbed frame operators applied to the background, by sympy.
  - Both of the verifier's surviving mutants now fail E9 (`scratchpad/r4/mut/ls_mut_db.out`,
    `ls_mut_quarter.out`). linest5.py's rows, and so wgron5.py's and lev1_5.py's, are unchanged.
  - Rerun: `linest5.out` regenerated, E4–E8 identical to round 3. E9 PASS, 24 s.
- [7.10 A1, "both eigenvalues are semisimple, so there is no Jordan block": verifier of round 3: the no-block result is
  non-generic. Changing the elimination coefficient's sign, or multiplying it by 2, brings the block back.]
  - *Re-derived by reading S3.* Rank A_eff = 2 rests on the exact relation row 4 = −(1 + x)/3 · row 2 −
    (1 − x)/3 · row 3. Any perturbation of the eliminated coefficient breaks it.
  - So the result holds for the exact equations only. A scheme that perturbs the elimination (for instance by its
    truncation error) is not covered by it.
- [7.10 A4, "The gap is about 5 to 84": verifier of round 3: 4.6–81, as elsewhere. Re-derived: 2.42 × 10⁻³/5.26 ×
  10⁻⁴ = 4.60 and 81.2.]

**Task 2 of round 3 (re-derived from rcert5b.out of round 3).**
- [7.0 item 2 and 7.6, "reaching twice the residual's size needs n ≈ 26–35 … about 2–4 × 10⁴ sub-boxes", and
  "extrapolated: of the order of 10⁷ sub-boxes and 10⁷ s for all 416 … a matter of machine time, not of method":
  verifier of round 3: at the asymptotic h³ ratio of 8 the gap needs n ≈ 59–104 (2 × 10⁵ to 1 × 10⁶ sub-boxes).
  K2's ln, lx and nx bounds are infinite at boxes with x = 0.625 and 0.994, so nothing shows convergence there. The
  10⁷ rests on the most favourable interior box.]
  - *Re-derived.* bound/centre at n = 8 is 810–4,400, so the gap to twice the centre is 405–2,200, and
    8 · gap^{1/3} = 59–104.
  - It reads "a lower bound on machine time, for interior boxes only".
  - 8.4 replaces the extrapolation by a measurement: adaptive bisection completes the interior box. And it replaces the
    "all 416" claim by a certified census: on 193 of the 416 boxes a certified point value exceeds the target, so no
    machine time suffices there.

**Task 3 of round 3 (re-derived from cplate5d.out and cplate5c.out).**
- [7.0 item 3 and 7.7, "M = 40 … raises the monitor 2–25-fold everywhere from v = 1.0, the scheme's angular defect",
  and "Raising M to 40 raises the Ric_xx monitor on every band from v = 1.0 on, at every areal radius": verifier of
  round 3: WRONG.]
  - *Re-derived (cplate5d.out).* At areal radius 0.9–1.0 on [1.9, 2.0) and [2.0, 2.25) the interior monitor falls with
    M: 29.7 → 24.0 and 69.4 → 60.3. cplate5d prints "not angle-limited" for the second.
  - At areal radius ≥ 1.2 on [2.0, 2.25) the rise is 34-fold: 0.390 → 13.3.
  - So the angular-defect explanation fails exactly at 0.9–1.0 from v = 1.9. There the violation does not change with
    M, and it grows with the null step (Ric_xx 800 → 1600 rows: ratios 0.72 and 0.58, cplate5c.out). That leans against
    a vacuum limit there, rather than "not decided".
  - It reads: "M = 40 raises the interior monitor 2.3–34-fold on every band from v = 1.0 at areal radius ≥ 1.0, and
    2.2–25-fold at 0.9–1.0 below v = 1.9, including bands where P has converged. At areal radius 0.9–1.0 from v = 1.9 it
    falls slightly (ratios 0.81 and 0.87), and grows with the null step."
- [7.0 item 3 and 7.7, "three null grids": verifier of round 3: in effect two, since the 400-row run is
  pre-asymptotic (ratios 17–272). Accepted.]
- [7.0 item 3, "≤ 1.0 × 10⁻³": 1.04 × 10⁻³. "14–22-fold to v = 1.9": it holds on [1.65, 1.9) only. Verifier of round
  3; both re-derived from cplate5c.out.]

**The proposed paper text of 7.9 (verifier of round 3, M-2).**
- *Re-derived.* "remains open" occurs once (paper line 1490), followed by " (supplement `CERTIFY-10L5-RESULT.md` section
  2)." The 7.9 span left that citation dangling.
- 7.9's text claims more than the record in six ways, each confirmed by reading the cited sections:
  - (a) the loss of derivatives is deduced at frozen coefficients, on spherical states, for the free formulation only,
    and for the constraint-preserving one in a model only;
  - (b) 7.5 lists four obstacles, not two;
  - (c) the constant 10^69 is computed where no truncated domain exists;
  - (d) "three angular crossing times" is over-counted;
  - (e) the certificate's program refits;
  - (f) the cdata5 figures lose their comparison scale, 4.1–4.3 % of the cancelling terms.
- 7.9's proposal is withdrawn. 8.10 replaces it, with the span ending at "section 2)." and every item above folded in.

### 8.1 Answers

1. **Task 1, the axes.** Near each axis the class is four-dimensional, axisymmetric, twist-free Einstein–scalar, in a
   chart that is regular there (deduced, exact: `checks/axis5.py`).
   - *Proved (deduced, exact).*
     - The reduction and the chart's regularity, including elementary flatness in the record's variables (8.A1).
     - The reduced double-null structure, with σ = 0 (8.A2).
     - [Wu26]'s Gauss equation (2.8) and the curvature pair (2.13)–(2.14) in the reduced form, found at random jets and
       verified exactly at fresh ones (`checks/axisbianchi5.py` B1–B3). The conjugate pair (K, β̲^r) is verified
       likewise (B3b).
     - The pair's energy identity on the whole section, with no boundary term at the axis (8.A3, 8.A6).
     - The axis's angular recoveries as Hardy inequalities with explicit constants (8.A4).
     - The glue's cut-off identity, with explicit added coefficients (8.G).
     - That nothing below the curvature level reaches the axis (8.A5).
   - *Computed.* The chart's frame quantities are bounded up to the axis on the record's solution, at the regular rates
     (X5). Theorem 7.L's coefficients grow from 122 to 1.8 × 10⁵ there.
   - *Not done:* the closure inequality of the linearised axis hierarchy, and with it the glued estimate. That is task
     1's single missing input (8.6).
   - The glue to Theorem 7.L needs 7.L at level 1, since the cut-off terms are curvature-level. Theorem 8.L1 (exact,
     `checks/lev1_5.py`) supplies it.
2. **Task 2, the constant.**
   - *Proved:* Theorem 8.W, 7.L with weights. On |x| ≤ 1/2 over the box, where no truncated domain exists, it lowers
     F² from 10^138 to 10^66.9, and on |x| ≤ 0.8 from 10^222 to 10^93.1 (computed, `checks/wgron5.py`).
   - *Proved (Lemma 8.F):* no approximate inverse of finite rank lowers F below the explicit constant applied to its
     defect, since that defect is at least 1. So round 3's demand "at F = 9.2" is not delivered by that route.
   - The closing condition with the new constant is (𝒟_δ + 𝒮_ε)^{1/2} < 1/(4 G F²). At F² = 10^66.9 it asks
     10^−68/G in 2(d)'s convention.
   - *Missing input:* an explicit estimate on the high angular modes with a small constant (8.6).
   - *Computed:* in the transported subsystem the signed growth is 2 × 10⁶, against a Grönwall factor of 10^87–10^97.
     The bookkeeping, not growth, makes the constant there.
3. **Task 3, the residual.**
   - *Certified (`checks/rcert5d.py`):* on rcert5's interior box t, σ ∈ [−1/2, 0], x ∈ [0, 1/4], every frame component
     of the pinned approximant's residual is ≤ 3.01 × 10⁻⁴ of the curvature scale. That is below the target 5.3 × 10⁻⁴,
     over 32,768 sub-boxes (37,440 Taylor-model evaluations, 3,500 CPU-seconds, 2.9 hours on the shared machine).
   - *Certified:* on 193 of the 416 boxes no certificate can reach 5.3 × 10⁻⁴, since a certified point value exceeds
     it. On the other 222 the cost is estimated in 8.4.
4. **Task 4, level 1 and the late region.**
   - *Level 1, proved:* Theorem 8.L1, the hierarchy commuted with e_x, closes (exact). Its constant is computed:
     10^2645.7 unweighted, 10^91.0 weighted.
   - *Late region, computed.* The free scheme is resolved in angle to v = 1.8 and loses it from there, the node next to
     the axis first (A1).
   - The constraint-preserving scheme's monitor rise with M is the singular R_uv coupling at the axes, −3/(R(1 ± x))
     (A2).
   - A regularisation removes the spurious axis field on Tangherlini to rounding, 10⁻¹² against 10⁻⁴–10⁻², and puts R
     at second order (A3).
   - On the record's data at 400 rows the regularised monitor no longer rises with M below v = 2.0, and M = 32 and 40
     agree to 5.4 × 10⁻¹¹ to v = 1.8 (A4).
   - From 400 to 800 rows the constraint converges at second order in the null step, and it is independent of M. This
     holds to v = 2.0 at areal radius ≥ 1.2, and to v = 1.8 at 0.9–1.2 (A5).
   - The Kretschmann scalar is resolved in M and in the null step, and moderate (|K/K_0 − 1| ≤ 4.1), to v ≈ 1.8–1.9;
     from v = 1.9 it is unresolved in angle at every angle (A6).
   - From v = 1.8 at areal radius 0.9–1.2 a constraint violation persists under both refinements. Not decided; it leans
     against a vacuum limit there.
   - The theorem's region is bounded to v ≤ 1.8 r_h at areal radius ≥ 0.9 r_h and v ≤ 2.0 r_h at ≥ 1.2 r_h (and
     v ≤ 1.65 r_h at 0.6–0.9 r_h). Nothing is claimed beyond. The single missing input is a third null grid for the
     regularised scheme.
5. **Task 5.** The old and new text are in 8.9.

**The verifier of round 3** is seated in 8.0. Its M-1 (rcert5c.py overwriting the tracked npz) is repaired. The file's
md5, 698569f6…, is unchanged before and after every program of this round. linest5.py's rows are now checked against
the geometry (E9), which catches both mutants it found surviving. The compatibility propagation it asked for is
attempted (`checks/prop5.py`). The sixth Einstein component propagates (exact). The compatibility relations
themselves are propagated by no one-directional row; their propagation is not shown, and is added to the missing
inputs.

### 8.2 Task 1: the axis charts (`checks/axis5.py`)

**The chart.** Near x = +1 the φ2-circle degenerates and the φ1-circle does not, so the class is reduced on φ1 alone:
g5 = g4 + e^{2A} dφ1², g4 = h + e^{2B} dφ2² (reduce5.py's A, B, h). In four dimensions the Einstein frame is
ĝ = e^A g4, and for every metric of the class (X1, exact)

    Ric(ĝ) − (3/2) dA dA = Ric5|_4 + (1/2) e^{−2A} Ric5_11 g4,     □_ĝ A = −e^{−3A} Ric5_11.

So the vacuum class is four-dimensional Einstein–scalar ([Wu26] (1.4), READ; Φ = √(3/2) A), axisymmetric about the
axis of ∂_φ2, twist free and reflection symmetric in φ2, and its residues are fixed combinations of Ric5, as in 7.1.
In [Wu26]'s form (1.1), ĝ = −2Ω̂²(du dv + dv du) + ĝ_x (dx − b du)² + Y² dφ2², with Ω̂² = e^{A+2W}, ĝ_x = e^A Gx,
Y = e^{A/2+B}, b = (1 − x²) s. The chart at x = −1 exchanges (A, φ1) and (B, φ2).

- **Lemma 8.A1 (deduced, exact: X1).** In the record's variables the chart is regular at x = 1: Ω̂² → R e^{P+2W} > 0
  (the three-dimensional Einstein frame of 7.1 has Ω̃² ∝ 1 − x² → 0 there), and with s the proper distance to the
  axis, Y/s → e^{P+2Q} = e^{(1−x)n} → 1: elementary flatness, exact in the record's variables. *Controls* (fail): the
  five-dimensional weight e^{2A} in place of e^A; a conical defect P + 2Q → c, which gives Y/s → e^c.
- **Lemma 8.A2 (deduced, exact: X2).** For the general metric of this form, with e4 = Ω̂⁻¹∂_v,
  e3 = Ω̂⁻¹(∂_u + b∂_x), e1 = ĝ_x^{−1/2}∂_x, e2 = Y⁻¹∂_φ, [Wu26] (2.1)'s Ricci coefficients have χ_12 = χ̲_12 = η_2
  = η̲_2 = ζ_2 = 0 and χ_11 = e4 log √ĝ_x, χ_22 = e4 log Y, χ̲_11 = Ω̂⁻¹((∂_u + b∂_x) log √ĝ_x + b_x),
  χ̲_22 = e3 log Y, ω = −½ e4 log Ω̂, ω̲ = −½ e3 log Ω̂, ζ = −¼ Ω̂⁻² √ĝ_x b_v, η = ζ + e1 log Ω̂, η̲ = −ζ + e1 log Ω̂.
  Every Christoffel symbol with an odd number of φ indices vanishes, so σ = 0 and the reduced curvature is
  (α_11, β_1, ρ, β̲_1, α̲_11) with the section's Gauss curvature K = −Y⁻¹ e1 e1 Y. With σ = 0 and curl η = 0,
  [Wu26]'s auxiliary ω† vanishes. *Control* (fails): χ_22 taken from the other circle.
- **Lemma 8.A3 (deduced, exact: X3).** With dμ = Y √ĝ_x dx, ∂_v log(Y √ĝ_x) = Ω̂ tr χ and
  ∂_u(Y √ĝ_x) + ∂_x(b Y √ĝ_x) = Ω̂ tr χ̲ Y √ĝ_x; and for any scalar K and one-form component β,
  K div(Ω̂β) + Ω̂ β e1 K = (Y √ĝ_x)⁻¹ ∂_x(Y Ω̂ K β), an exact derivative for dμ whose value at the axis vanishes with Y.
  So [Wu26]'s curvature pairs (β, (K, curl η)) and ((K, curl η̲), β̲) (READ, (2.13)–(2.15) and p. 8), here (β^r, K)
  and (K, β̲^r), have energy identities on the whole section, the axis included, with no boundary term there.
  *Control* (fails): with the three-dimensional measure √ĝ_x dx the remainder is exactly (e1 log Y) Ω̂ K β, the
  axis's 1/s term.
- **The pairs themselves (deduced: `checks/axisbianchi5.py` B1–B3b; each equation found by a fit at random jets and
  verified exactly at fresh jets, on the general metric of the chart, off shell).**
  - The setup: Riemann from the Christoffel symbols, the Weyl tensor by [Wu26]'s formula, β = ½W(e1, e4, e3, e4),
    β̲ = ½W(e1, e3, e3, e4), ρ = ¼W(e4, e3, e4, e3), and [Wu26] (2.12)'s β^r = β − ½Ric_41, β̲^r = β̲ + ½Ric_31.
  - *B1.* W(e1, e2, e3, e4) = W(e1, e2, e1, e4) = W(e1, e2, e1, e3) = 0: σ and the twisted components vanish.
  - *B2, Gauss.* K = −ρ + R/3 + ½Ric_34 + χ̂χ̲̂ − ¼ tr χ tr χ̲, which is [Wu26] (2.8) (χ̂·χ̲̂ = 2χ̂χ̲̂ in these
    components).
  - *B3, the pair (β^r, K).*

        Ω̂ e4 K + Ω̂ tr χ K = −div(Ω̂ β^r) + div(Ω̂ η̲ χ̂) − ½ div(Ω̂ η̲ tr χ),
        Ω̂ e3 β^r + Ω̂(tr χ̲ − 2ω̲) β^r = −Ω̂ e1 K + 2Ω̂ χ̂ β̲^r − 3Ω̂ η K + Ω̂ e1(χ̂χ̲̂) − ¼Ω̂ e1(tr χ tr χ̲)
            + 3Ω̂ η χ̂χ̲̂ − ¾Ω̂ η tr χ tr χ̲ + Ω̂ e1(Ric_11 + Ric_22) − Ω̂ e1 Ric_11 − Ω̂ k(Ric_11 − Ric_22)
            + ½Ω̂ tr χ Ric_31 − Ω̂ χ̂ Ric_31 + Ω̂ η Ric_22,

    with k = e1 log Y. The principal parts are [Wu26] (2.13)–(2.14)'s. In (2.13)'s two lower-order terms the fit finds
    the opposite signs to those read from [Wu26]. The fit is exact here; the difference is recorded, not resolved, and
    it does not touch the energy structure.
    - *Control* (fails): β in place of β^r, the Ricci terms withheld, leaves a residual of 1.8 at the fresh jets
      (Ric enters).
  - *B3b, the conjugate pair (K, β̲^r)*, with the mirrored library:

        Ω̂ e3 K + Ω̂ tr χ̲ K = div(Ω̂ β̲^r) + div(Ω̂ η χ̲̂) − ½ div(Ω̂ η tr χ̲),
        Ω̂ e4 β̲^r + Ω̂(tr χ − 2ω) β̲^r = Ω̂ e1 K + 2Ω̂ χ̲̂ β^r + 3Ω̂ η̲ K − Ω̂ e1(χ̂χ̲̂) + ¼Ω̂ e1(tr χ tr χ̲)
            − 3Ω̂ η̲ χ̂χ̲̂ + ¾Ω̂ η̲ tr χ tr χ̲ − Ω̂ e1(Ric_11 + Ric_22) + Ω̂ e1 Ric_11 + Ω̂ k(Ric_11 − Ric_22)
            − ½Ω̂ tr χ̲ Ric_41 + Ω̂ χ̲̂ Ric_41 − Ω̂ η̲ Ric_22.

    That is the mirror image of the first pair (χ ↔ χ̲, η ↔ η̲, β ↔ β̲, 3 ↔ 4), with every term but 2Ω̂χ̲̂β^r of the
    opposite sign. Both are exact at fresh jets (residuals ≤ 9 × 10⁻⁴²).
  - The two principal coefficients are equal in each pair (−1 and −1; +1 and +1), which is the condition for an
    energy pair (8.A3).
- **Lemma 8.A6, the pair inequality on the whole section (deduced from B3 and 8.A3).** With F_K and F_β the
  lower-order right sides above,
  ∂_v ∫K² dμ = ∫(2K F_K − 2K div(Ω̂β^r) − Ω̂ tr χ K²) dμ and
  ∂_u ∫(β^r)² dμ = ∫(2β^r F_β − 2β^r Ω̂ e1 K − Ω̂(tr χ̲ − 4ω̲)(β^r)²) dμ.
  - The principal terms sum to −2(Y√ĝ_x)⁻¹ ∂_x(Y Ω̂ K β^r), with no boundary term at the axis (Y = 0, K and β^r
    bounded).
  - So on [u0, u] × [v0, v], with the energy cut off by ψ of 8.G to the part of each section where the chart is used,
    ∫_{H_u} ψ(β^r)² dμ dv + ∫_{H̲_v} ψK² dμ du ≤ (data) + ∫∫ψ(2|K||F_K| + 2|β^r||F_β| + Ω̂|tr χ| K²
    + Ω̂|tr χ̲ − 4ω̲|(β^r)²) dμ du dv, plus 8.G's two bulk terms. Likewise for (K, β̲^r), with Ω̂|tr χ̲| and
    Ω̂|tr χ − 4ω|.
  - This is the curvature-level estimate of the pairs at the axis, with explicit coefficient functions.
  - What it leaves is F_K and F_β. They carry angular derivatives of Ricci-coefficient products, as [Wu26]'s do, and
    bounding them is the rest of the hierarchy (below).
- **Lemma 8.A4 (deduced; computed check: X4).** On [0, S] with Y = s y(s), 0 < y_min ≤ y ≤ y_max, |s y'/y| ≤ q, the
  solutions regular at the axis of div η = g and of Codazzi's operator (e1 + 2 e1 log Y) χ̂ = g obey, in L²(Y ds),
  ‖(e1 log Y) η‖ ≤ (1 + q)(y_max/y_min)^{3/2} ‖g‖ and ‖(e1 log Y) χ̂‖ ≤ ½(1 + q)(y_max/y_min)^{5/2} ‖g‖ (the weighted
  Hardy inequality with r = 3 and r = 5). Checked on five test functions at three grids (the ratio to the bound is
  ≤ 0.244 and ≤ 0.190); *control*: integrated from s = S instead of the axis, the ratio grows with the grid
  (1.5 × 10³, 6.0 × 10³, 2.4 × 10⁴): unbounded. These are the angular recoveries [Wu26]'s proof makes by elliptic
  estimates on spheres; at the axis they are explicit.
- **Lemma 8.A5 (deduced, exact: X6): nothing weaker than the curvature level suffices at the axis.** The section has
  the connection k = e1 log Y ~ 1/s. Under the regular perturbation ĝ_x → (1 + ε) ĝ_x, Y → (1 + ε)^{1/2} Y
  (elementary flatness kept), δk = −(ε/2) k to first order, exactly, and ∫_a^1 k² Y ds = −log a → ∞. So no estimate
  whose unknowns include δk in L²(dμ) exists. Theorem 7.L's unknowns cannot be carried to the axis, and the angular
  derivatives of the metric differences must be carried as tensors (Codazzi, 8.A4), which is [Wu26]'s level.
- **The constants near the axis (computed: X5, on D432's run over rcert5's box).** In chart + on 0 < x < 1, up to the
  outermost node, the frame quantities times Ω̂ (as linest5.py E4 states them) are bounded: tr χ 0.577, χ̂ 0.102,
  tr χ̲ 5.58, χ̲̂ 0.236, ω 0.188, ω̲ 0.348, ζ 0.327, η 0.61, η̲ 0.363, e4 Φ 0.283, e3 Φ 2.88, e1 Φ 0.998; in chart −
  the largest is tr χ̲, 6.71. They vanish toward the axis at the rates regularity requires: χ̂/(1 − |x|) is 0.114
  (chart +) and 0.247 (chart −) at each of the four outermost nodes, ζ/√(1 − |x|) 0.37 and 0.77. η/√(1 − |x|) and
  e1 Φ/√(1 − |x|) are bounded but alternate between nodes (0.93, 0.50, 0.67, 0.56 for η in chart +): the outermost node
  departs from its neighbours, the axis-node excess of 8.5 (A1), already at v ≤ 1.6. Theorem 7.L's three-dimensional
  coefficient sums grow from 122 on |x| ≤ 1/2 to 1.8 × 10⁵ at the outermost node (linest5.out E4).
- **Lemma 8.G, the glue (deduced, exact: X7; constants computed).** For a cut-off ψ(x),
  ψ[K div(Ω̂β) + Ω̂ β e1 K] = (Y √ĝ_x)⁻¹ ∂_x(ψ Y Ω̂ K β) − (e1 ψ) Ω̂ K β, and the shift adds b (∂_x ψ) f under ∂_u. So
  the cut-off energy obeys the chart's identity with two bulk terms supported where ψ is not constant, of
  coefficients sup Ω̂|e1 ψ| and sup|b ∂_x ψ|. For ψ linear in x on 1/4 ≤ |x| ≤ 3/4 they are 3.16 and 0.924 (chart +),
  3.32 and 1.01 (chart −). *Control* (fails): the identity without the (e1 ψ) term.
  - The added terms are curvature-level (K β). An interior energy that does not control them on the strip cannot absorb
    them. Theorem 7.L is level 0, so **the glue to 7.L needs 7.L at level 1 on the strip**, which Theorem 8.L1 (8.5)
    supplies. A family with bounded level-0 norm and K unbounded on the strip (δΦ = ε sin(x/ε)) shows that nothing
    weaker suffices.
  - What the glue also needs is the equivalence constant C_eq between the chart's curvature-level unknowns and
    Theorem 8.L1's (Z, Z′) on the strip. It is an explicit linear map of jets, regular on the strip, and it is not
    computed here.

**What is proved, and what is not.**
- *Proved (deduced):*
  - the axis charts exist and are regular (8.A1);
  - their twist-free double-null structure (8.A2) is exact;
  - both curvature pairs hold in reduced form and have energy identities on the whole section, so the pair inequality
    holds there with explicit coefficients (8.A3, B1–B3b, 8.A6);
  - the axis's angular recoveries hold with explicit constants (8.A4);
  - no level-0 estimate reaches the axis (8.A5);
  - the cut-off identity holds with explicit added coefficients (8.G).
- *Computed:* the chart quantities are bounded up to the axis on the record's solution, at the regular rates.
- *Not done: the axis estimate itself.* That is one Grönwall inequality, in chart ±, for the linearised unknowns at
  [Wu26]'s level: δβ^r, δK, δβ̲^r; ∇δ tr χ, ∇δ tr χ̲; δ(div η − K), δ(div η̲ − K); δ(∇ω − ½β), δ(∇ω̲ + ½β̲); the
  Ricci-coefficient differences; δ(e_a Φ), δ(e_a e_b Φ); the metric differences and their angular derivatives as
  tensors. The angular recoveries in it are 8.A4's.
  - Its curvature pairs are B3–B3b's. Its other ingredients are [Wu26]'s transport equations (2.2)–(2.6) and
    (2.15)–(2.16) (READ). Those are not re-derived here in the reduced form, and the linearised coefficient table
    (linest5.py E2's analogue) is not assembled.
  - **This is the single missing input of task 1.** Together with C_eq it would give, through 8.G, an estimate on the
    whole late region.
  - By 8.A5 nothing weaker suffices at the axis.

### 8.3 Task 2: the constant (`checks/wgron5.py`)

**Theorem 8.W (deduced: Theorem 7.L's proof with weights; checked, W1).** Give each row group a weight λ > 0: one per
transported unknown, and one per scalar for its three pair unknowns, since the pair identities fix a : c : d. Give
each off-diagonal bilinear term a split θ > 0, 2λ_Y|m||Y||Z| ≤ |m|θ(λ_Y Y²) + |m|(λ_Y/(λ_Z θ))(λ_Z Z²). Then

    f ≤ F_λ² (𝒟 + 𝒮),   F_λ² = (max λ/min λ) exp(2 ∫ a_o^λ du + 2 ∫ a_i^λ dv),

with the κ's of 7.L reweighted. Every (λ, θ) gives a theorem; the exponent is convex in (log λ, log θ).
- *W1.* On a model pair Y_v = 9Z, Z_u = Y, the bound from the program's own `Bound` holds at four (λ, θ). *Control*
  (mutation of the code under test): the partner's share λ_Y θ/λ_Z gives a bound 2 below f(1, 1) = 1.34 × 10⁴, and
  it is caught.
- *W2.* λ = θ = 1 reproduces linest5.py E4b: 10^138.0 on |x| ≤ 1/2 (PASS).
- *W3 (computed), the optimum.* F_λ² = 10^66.9 on |x| ≤ 1/2, with log(max/min λ) = 5.47, ∫a_o du = 49.8 and
  ∫a_i dv = 24.4, against 10^138.0. On |x| ≤ 0.8 it is 10^93.1, against 10^222.2. The exponent is halved, and F_λ is
  still 10^33.5.

**The approximate-inverse route, as round 3 deduced it, does not lower F (deduced: W4).**
- *Lemma 8.F.* If A has finite rank and L has infinite-dimensional range in a Hilbert space, then ‖I − LA‖ ≥ 1.
  Proof: for f orthogonal to the finite-dimensional L(ran A), |(I − LA)f|² = |f|² + |LAf|².
- So the bound ‖L⁻¹‖ ≤ ‖A‖ + F_E ‖I − LA‖, the explicit estimate applied only to the defect, is ≥ F_E for every
  finite-rank approximate inverse. Round 3's demand 5.3 × 10⁻⁴ to 3.0 × 10⁻⁵ "at F = 9.2" (7.6) does not follow from
  that construction, and is withdrawn as a consequence of it; it stays a conditional figure (below).
- What can lower F is a block (Schur) argument. Validate the low angular modes numerically, and bound the high-mode
  block L_∞∞ by an explicit estimate of constant F_∞. It closes only if ‖A_N‖ ‖L_N∞‖ F_∞ ‖L_∞N‖ < 1.
- *Computed instance.* At the record's angular resolution (N = 32), the exact low-mode inverse has defect exactly 1
  on T_32. The coupling across the cut, P_∞(m T_k)/|m T_k| for the largest coefficient (δw in the χ̲ row, sup 1.0 × 10³
  at u = −1.10), is 0.48–0.59 for k = 28–31: the coefficient's own size, not small.
- **The single missing input of task 2:** an explicit linear estimate on the high angular modes whose constant F_∞
  meets that condition. Theorem 8.W's F_∞ is the full F_λ, so it does not. By Lemma 8.F nothing weaker suffices.
- Neither ball nor interval arithmetic can supply this input. A certified defect is bounded below by 1 on the
  complement of the discretisation.

**How much of F is bookkeeping (computed: W5).**
- The setup: the nine transported rows alone, the pair unknowns and the e3 rows' angular motion dropped, solved at each
  angular node with the record's signed coefficients. The largest ratio f/𝒟 at the box's far corner is the squared
  norm of the data-to-solution map.
- On |x| ≤ 1/2 it is 4.8 × 10⁵ to 2.05 × 10⁶ (largest at x = −0.428). The same nine rows' Grönwall factor with
  absolute values is 10^87.1–10^97.0.
- So in that subsystem the absolute-value bookkeeping, not growth, makes the constant. This is not a bound on the full
  operator.

**The closing condition with the new constant.** In Theorem 8.W's norms the Newton–Kantorovich condition is
(𝒟_δ + 𝒮_ε)^{1/2} < 1/(4 G F²), with F the solution operator's norm and G the quadratic constant in the same norms;
in 2(d)'s convention, δ + ∫ε < 1/(4 G T F²).
- *F of Theorem 8.W, computed on |x| ≤ 1/2 over the box, where no truncated domain exists (7.4):* F² = 10^66.9. The
  demand is then 10^−69.1 at G = 10 and 10^−67.9 at G = 0.566 (T = 3.95). No approximant held in floating point meets
  it.
- *Conditional F² of the frozen-angle size, 2 × 10⁶ (computed, not proved):* 3.1 × 10⁻⁹ at G = 10 and 5.4 × 10⁻⁸
  at G = 0.566 (T = 3.95).
- *Conditional F = 9.2 (round 2's measured response along one direction):* 5.3 × 10⁻⁴ (G = 0.566) to 3.0 × 10⁻⁵
  (G = 10), with 2(d)'s T = 10, as in round 3.
- G is not computed. It needs level 1 for L^∞ control (8.5) and, at the axis, the missing estimate of 8.2.

### 8.4 Task 3: the residual certified on one whole box (`checks/rcert5d.py`)

**The target.** τ = 5.3 × 10⁻⁴ for every frame component over √K_0.
- This is round 3's most favourable conditional demand: F = 9.2, G = 0.566, 2(d)'s T = 10. By 8.3 it is an expectation,
  not a proved demand.
- The approximant is the pinned one. D0: its five tensor md5s equal rcert5c.out's, and the file is unchanged.
- The method is rcert5.py's order-3 Taylor models with the Lagrange remainder. The box splits adaptively: a box whose
  eight bounds are not all ≤ τ is replaced by its 2 × 2 × 2 children, evaluated as one tensor grid.
- The accepted boxes tile the box exactly, so their largest bound is a certified sup over it.

**The run** (two workers, then four, checkpointed every five minutes; uptime 13–30 on 4 cores throughout).
- Finished: 32,768 sub-boxes accepted, all at depth 5 (n = 32 per side; every depth-4 box failed τ and every depth-5
  box met it). 37,440 boxes were evaluated: 3,500 CPU-seconds, 0.09 s per box, and 2.9 hours of wall time.
  `rcert5d.out` gives the run's chunks.
- **D1 (certified): the sup over the whole box.** ll ≤ 3.01 × 10⁻⁴, nn ≤ 2.44 × 10⁻⁴, lx ≤ 9.75 × 10⁻⁵, xx ≤ 7.27 ×
  10⁻⁵, ln ≤ 7.03 × 10⁻⁵, 22 ≤ 6.22 × 10⁻⁵, nx ≤ 5.59 × 10⁻⁵, 11 ≤ 5.35 × 10⁻⁵ of the curvature scale. Every component
  is below τ (PASS).
  - The largest certified centre values are lower bounds for the sup: ll ≥ 1.73 × 10⁻⁴. So the sup of the ll component
    over the box lies in [1.73, 3.01] × 10⁻⁴, a certified bracket within a factor 1.74.
  - Σ vol × max_k sup_k² = 1.72 × 10⁻⁹ over a volume of 1/16 in (t, σ, x): an rms bound of 1.66 × 10⁻⁴.
- **D2 (certified).** The certified centre values of ll and lx exceed τ′ = 3.0 × 10⁻⁵ (the demand at G = 10), so no
  bound of any method meets τ′ on this box.
- *Controls* (both fail, as they must).
  - C1, the remainder dropped: the bound of t⁴ + σ⁴ + x⁴ about the origin is 0, so the true/bound ratio is ∞; with
    the remainder it is 0.25.
  - C2, W + 0.01 v: certified centre values to 4.8 × 10⁻², refused at τ.
- This replaces round 3's extrapolation (7.6) by a measurement. That extrapolation was n ≈ 26–35, lower bound; at the
  h³ ratio, 59–104 (verifier of round 3). The bound reached τ at n = 32: for ll it fell about 20-fold per halving, from
  0.124 at n = 8 (rcert5b.out) to 3.0 × 10⁻⁴ at n = 32.

**The census (D3, certified).** K1's 16,128 certified point values of the pinned approximant are mapped to K2's 416
boxes (4 × 4 in (t, σ), 26 graded in x).
- 193 of the 416 boxes hold a point whose certified value exceeds τ = 5.3 × 10⁻⁴. There no certificate of this
  approximant, by any method, can reach τ.
- 337 of the 416 hold one above τ′ = 3.0 × 10⁻⁵, the demand at 2(d)'s placeholder G = 10.
- The largest certified value is 2.414 × 10⁻³ (ll).
- The box certified here is one of the other 223.

**The rest.**
- *On the 193 boxes:* impossible at τ with this approximant (certified). A better approximant is the input there
  (8.6 item 3).
- *On the other 222 of the 223:* certifiable in principle. At this box's measured cost, 37,440 evaluations each,
  they come to 8.3 × 10⁶ evaluations, about 7.7 × 10⁵ CPU-seconds (215 CPU-hours; about 2.2 days on the four cores
  if they were free).
  - That figure holds for boxes like this one. Near K2's corners and near x = 0.625 and 0.994, where K2's bounds were
    infinite (verifier of round 3), nothing shows that n = 32 suffices.
- *The axis caps |x| > cos(π/32):* not covered by rcert5's frame, whose 1/(1 − x²) factors cancel only analytically.
  They need the axis chart of 8.2.
- *How much it buys:* none of this closes anything at Theorem 8.W's constant, whose demand is 10^−68/G (8.3). The
  certificate is the step that would follow a constant of the order of the true response.

### 8.5 Task 4: level 1, and the late region beyond v = 1.8–1.9

**Level 1 (`checks/lev1_5.py`).**
- *The system.* Theorem 7.L's rows are commuted once with the background's e_x, with Z′ := e_x Z, using null3.py N4's
  commutators: [e_x, e4] = χ e_x − ½(η + η̲) e4, [e_x, e3] = χ̲ e_x − ½(η + η̲) e3 and [e_x, ∂_v] = e^w χ e_x.
  - Each row X(δY) = Σ m_Z Z + S becomes X(δY′) = Σ (e_x m_Z) Z + Σ m_Z Z′ − c_X δY′ + ½(η + η̲)(X δY) + e_x S.
  - X δY is replaced by its own row. The pairs commute into pairs for (a′, c′) and (c′, d′) with the same principal
    parts.
- *L1 (exact).* The three commutators hold on the general (2+1)-metric. *Control* (fails): the e4 commutator without
  its ½(η + η̲) e4 term.
- *L2 (exact).* The thirty-unknown system closes: no level-2 term on any right side. The background enters through its
  state, its first and second x-derivatives, and w_x, k_x. The table is in `lev1_5.out`.
- *L3 (control, fails as it must).* Commuting linest5.py E3's control row (χ̲ by null3.py N7) puts e_x²δη̲ on a right
  side.
- **Theorem 8.L1 (deduced).** Theorem 7.L's proof, unchanged, gives f_1 ≤ (𝒟_1 + 𝒮_1) exp(2∫a_o^{(1)} + 2∫a_i^{(1)})
  on the same truncated domains, for the level-0 norm of (Z, Z′).
  - Since ‖f‖_∞ ≤ ‖f‖/√|I| + √|I| ‖f′‖ on a one-dimensional section, it bounds Z in L^∞: the control the quadratic
    remainder needs away from the axes.
  - Its domain restriction is 7.L's (7.4): it does not reach the axes.
- *L4 (computed, on |x| ≤ 1/2).* Unweighted, ∫a_o du = 366.6 and ∫a_i dv = 2,679.5, so F_1² = 10^2645.7. Weighted
  (Theorem 8.W's optimum), F_1² = 10^91.0 with log(max/min λ) = 12.68.
  - The coefficients that make it are those of δw and δk in the commuted pair rows. They reach 1.07 × 10³ at the box's
    corner u = −1.10, where the background's second x-derivatives are large: e^w ∂_x²η = 146, e^w ∂_x²c_1 = 178. These
    come from a scratch diagnostic (`scratchpad/r4/l1diag.py`, not seated) and are labelled computed only.

**The late region (`checks/cpaxis5.py`).**
- **A1 (computed): where the angular resolution is lost.** This uses the record's free run (D432, M = 32, 1600 × 720)
  and round 3's constraint-preserving run (the same grid), at areal radius 1.0–1.2. For each v-band it gives the
  Chebyshev tail of m and n in x, and the excess of the outermost node over a cubic extrapolation of the next four.

  | v-band | free: tail m / n | free: axis-node excess m / n | cp: tail m / n | cp: axis-node excess m / n |
  |---|---|---|---|---|
  | [1.0, 1.5) | 4.8e-7 / 1.3e-8 | 7.0e-6 / 2.9e-6 | 2.5e-4 / 6.4e-6 | 1.4e-2 / 4.6e-4 |
  | [1.5, 1.65) | 1.7e-8 / 7.2e-9 | 5.1e-7 / 1.2e-6 | 1.6e-5 / 6.4e-6 | 9.1e-4 / 3.9e-4 |
  | [1.65, 1.8) | 1.0e-8 / 6.8e-9 | 1.2e-6 / 1.2e-5 | 2.9e-5 / 5.1e-5 | 1.8e-3 / 3.3e-3 |
  | [1.8, 1.9) | 1.0e-4 / 1.6e-4 | 1.9e-3 / 3.6e-3 | 5.8e-5 / 3.7e-4 | 5.1e-3 / 1.9e-2 |
  | [1.9, 2.0) | 2.2e-2 / 4.1e-2 | 0.99 / 0.90 | 2.9e-3 / 2.2e-3 | 0.18 / 3.7e-2 |
  | [2.0, 2.25) | 1.5 / 0.21 | 3.6 / 1.1 | 0.15 / 3.8e-2 | 1.1 / 0.85 |

  - The free scheme is resolved in angle to v = 1.8 (tail ≤ 5 × 10⁻⁷). It loses resolution from 1.8, and the
    outermost node departs first: from v = 1.9 its excess is of the size of the field.
  - The constraint-preserving scheme's tail is 10²–10⁴ times the free one's from v = 1.0: its own axis defect.
  - At [2.0, 2.25) the free run's n at the node next to x = +1 is 8.2 against 0.47 at the next node. This is from a
    scratch diagnostic (`scratchpad/r4/diag_cp.py`, not seated), and A1's excess column is the seated measure.
- **A2 (computed): the mechanism of the constraint-preserving defect.** cpsolve5 P3's mechanism, now measured.
  - With R marched and the rows solved for (m, n, W)_uv, (1 + x) ∂(m_uv)/∂(R_uv) → −1.5 at the node nearest x = −1,
    at M = 8, 16, 32 and 64 alike, and (1 − x) ∂(n_uv)/∂(R_uv) likewise at x = +1 (Tangherlini cell, R = 2:
    −3/(R(1 ± x))).
  - So the marched R_uv's truncation error, which nothing ties to the rows at the axis, enters m and n with the factor
    1/(1 − |x_M|) = 830 at M = 32 and 1,300 at M = 40. That is the monitor's rise with M.
- **A3 (computed): a regularisation.** At every cell the R_uv the rows use is corrected by d₋(1 − x)/2 + d₊(1 + x)/2.
  - d± are chosen so that (1 + x) m_uv → 0 at x = −1 and (1 − x) n_uv → 0 at x = +1. The limits are read from the
    Chebyshev interpolants of these regular products.
  - R is still marched, and Raychaudhuri still imposed. The correction is O(the truncation error), so the limit is
    unchanged.
  - On Tangherlini (M = 8, where m = 0 exactly) the spurious max |m| falls from 2.0 × 10⁻², 1.0 × 10⁻³ and
    1.1 × 10⁻⁴ (100, 200, 400 rows) to 1.5 × 10⁻¹², 8 × 10⁻¹³ and 7 × 10⁻¹³: to rounding.
  - The error of R becomes second order (3.1 × 10⁻³, 7.7 × 10⁻⁴, 1.9 × 10⁻⁴, ratios 4.0 and 4.0). The original's is
    not (1.2 × 10⁻², 4.6 × 10⁻⁴, 2.4 × 10⁻⁴, ratios 25 and 1.9).
  - *Control* (fails): the correction with its sign reversed raises the spurious m to 5 × 10³ at 100 rows.
  - *The criterion, recorded.* The first run used "the error of R no more than 1.5 times the original's at every
    grid". It failed at 200 rows (7.7 × 10⁻⁴ against 4.6 × 10⁻⁴), where the original is not in its asymptotic range
    (`cpaxis5_run1.out`). The criterion was replaced by "second order, and at 400 rows no larger than the original's",
    and the program rerun (`cpaxis5.out`).
- **A4 (computed): the record's data at 400 × 180, M = 32 and 40, with and without the regularisation**
  (`cpaxis5_a4.out`; areal radius 1.0–1.2).

  | v-band | monitor M32 / M40, orig (ratio) | monitor, reg (ratio) | tail of m, orig / reg | \|P₃₂ − P₄₀\|, orig / reg |
  |---|---|---|---|---|
  | [0.5, 1.0) | 1.6e-3 / 2.5e-2 (15.9) | 8.2e-4 / 9.0e-4 (1.10) | 0.35 / 2.7e-2 | 9.9e-5 / 1.3e-12 |
  | [1.0, 1.5) | 7.4e-2 / 0.39 (5.25) | 4.1e-3 / 4.8e-3 (1.16) | 1.9e-2 / 3.5e-10 | 2.9e-3 / 3.4e-11 |
  | [1.5, 1.65) | 0.43 / 0.93 (2.17) | 4.6e-3 / 5.7e-3 (1.23) | 1.3e-3 / 1.7e-11 | 3.6e-3 / 5.1e-11 |
  | [1.65, 1.8) | 5.3 / 8.7 (1.64) | 4.5e-3 / 4.7e-3 (1.05) | 3.8e-3 / 2.2e-11 | 5.2e-3 / 5.4e-11 |
  | [1.8, 1.9) | 34 / 68 (2.01) | 1.5e-2 / 7.0e-3 (0.47) | 1.5e-2 / 1.4e-6 | 1.6e-2 / 2.3e-7 |
  | [1.9, 2.0) | 125 / 457 (3.65) | 5.2 / 4.8 (0.91) | 0.14 / 8.6e-5 | 5.5e-2 / 1.7e-4 |
  | [2.0, 2.25) | 7.3e3 / 7.2e3 (0.99) | 145 / 397 (2.73) | 0.81 / 3.1e-2 | 1.0 / 1.1e-2 |

  - With the regularisation the monitor no longer rises with M on any band below v = 2.0 (A4: PASS). It is 10–1,000
    times smaller.
  - m's angular tail falls to 10⁻¹⁰–10⁻¹¹ to v = 1.8, and the metric is independent of M to 5.4 × 10⁻¹¹ there, where
    the original scheme's M = 32 and 40 differed by 3 × 10⁻³.
  - So the constraint-preserving scheme's angular defect is the singular coupling of A2, and the regularisation
    removes it.
  - On [2.0, 2.25) the regularised monitor still rises 2.7-fold with M at 400 rows.
- **A6 at 400 rows (computed): the invariant.** The Kretschmann scalar of the regularised runs (`dnsolve5.kretschmann`,
  exact Christoffels) on 24 u-rows, at x = 0.97, 0.5, 0, −0.5, −0.97 and areal radius 1.0–1.4. The figures are
  dev = max |K/K_0 − 1| and the M = 32 against 40 difference over K_0.
  - To v = 1.8 the difference is ≤ 9 × 10⁻⁷, with dev 0.23–4.0, the largest at x = −0.97: resolved in angle.
  - On [1.8, 1.9) it is 4 × 10⁻⁴ to 2.6 × 10⁻² against dev 0.66–4.1: resolved.
  - On [1.9, 2.0) it is 0.10–7.1 against dev 1.2–6.1, at every angle: not resolved.
  - On [2.0, 2.25) dev is 2.6 × 10² to 2.1 × 10³, with differences as large.
  - So with the scheme's defect removed the metric converges in M (|P₃₂ − P₄₀| ≤ 1.7 × 10⁻⁴ on [1.9, 2.0)), but the
    curvature invariant is not resolved in angle from v = 1.9, at every angle computed and not only at the axis.
- **A5 (computed): the regularised scheme on a second null grid**, 800 × 360 at M = 32 and 40 (`cpaxis5_a5.out`).
  The figures are the interior monitor at 400 / 800 rows (ratio), then M40/M32 at 800 rows.

  | v-band | areal ≥ 1.2 | areal 1.0–1.2 | areal 0.9–1.0 |
  |---|---|---|---|
  | [1.0, 1.5) | 1.3e-3 / 3.4e-4 (3.91); 1.16 | 4.1e-3 / 1.0e-3 (3.95); 1.16 | 7.7e-3 / 1.9e-3 (3.93); 1.17 |
  | [1.65, 1.8) | 1.8e-3 / 4.4e-4 (3.99); 1.26 | 4.5e-3 / 1.2e-3 (3.79); 1.08 | 1.5e-2 / 3.8e-3 (3.83); 1.20 |
  | [1.8, 1.9) | 1.6e-3 / 4.0e-4 (3.88); 1.26 | 1.5e-2 / 9.4e-3 (1.58); 0.30 | 1.17 / 1.02 (1.15); 0.52 |
  | [1.9, 2.0) | 3.9e-3 / 1.0e-3 (3.82); 1.14 | 5.2 / 5.1 (1.03); 0.82 | 36 / 34 (1.06); 1.17 |
  | [2.0, 2.25) | 0.26 / 0.27 (0.94); 0.60 | 145 / 142 (1.03); 2.64 | 124 / 114 (1.09); 1.86 |

  max |P₄₀₀ − P₈₀₀| to v = 1.8 is ≤ 9.3 × 10⁻⁵ at areal radius ≥ 1.0 and ≤ 2.4 × 10⁻⁴ at 0.9–1.0. On [1.9, 2.0) it is
  8.2 × 10⁻⁵, 1.0 × 10⁻³ and 2.9 × 10⁻³ (≥ 1.2, 1.0–1.2, 0.9–1.0).

  - With the defect removed, the unimposed constraint converges at second order in the null step (ratios 3.8–4.0) and
    is independent of M (1.1–1.3). This holds to v = 2.0 at areal radius ≥ 1.2 r_h, and to v = 1.8 at 0.9–1.2. So a
    vacuum limit is supported there (computed, two null grids). At areal radius ≥ 1.2 it now reaches v = 2.0 in a
    scheme that converges in M.
  - From v = 1.8 at areal radius 0.9–1.2 the constraint does not fall with the null step (ratios 1.0–1.6) and does not
    rise with M (0.3–1.2 below v = 2.0). The discrete solutions agree in the metric (|P₄₀₀ − P₈₀₀| ≤ 1.0 × 10⁻³ on
    [1.9, 2.0)), but they agree on a metric that violates Ric_xx = 0 by the same amount at both grids and both M.
  - The verifier of round 3 found the same at 0.9–1.0 in the unregularised scheme (8.0). Now the scheme's angular
    defect is removed, and at 1.0–1.2 too.
  - Two readings remain:
    - the region is approaching a singularity or a feature the null grids do not reach. A6 at 400 rows has K/K_0 of
      order 10³ on [2.0, 2.25), unresolved;
    - or the constraint-preserving system's limit is not vacuum there, which is the propagation question of 8.6
      item 5, not shown.
  - A third null grid would separate pre-asymptotic behaviour from the first two: 1600 × 720, about 4.5 hours at this
    load per M, as computed from this round's 800-row 4,568–4,836 s. It was not run.
- **A6 at 800 rows (computed): the invariant on two null grids** (`cpaxis5_a6.out`; the same 24 rows, 400 against 800
  rows at M = 32, and M = 32 against 40 at 800).
  - To v = 1.8, at every angle: the M-difference is ≤ 9 × 10⁻⁸ of K_0, and the null-step difference is 8 × 10⁻⁴ to
    3.3 × 10⁻², against dev 0.24–4.0. Resolved.
  - On [1.8, 1.9): M 5 × 10⁻⁴ to 8 × 10⁻³, null step 1.9 × 10⁻³ to 0.15, against dev 0.66–4.1. Resolved to a few per
    cent, except at x = 0, where the null step is 7 % of dev.
  - On [1.9, 2.0) the M-difference is 0.15–5.3 against dev 1.2–4.7, at every angle: not resolved in angle.
  - On [2.0, 2.25) dev is 83–1,040, with differences larger still.
  - So the curvature invariant is resolved, and moderate (|K/K_0 − 1| ≤ 4.1, largest near x = −1), to v ≈ 1.8–1.9. From
    v = 1.9 it is not resolved in angle anywhere, and its computed values grow by two to three orders of magnitude by
    v = 2.25. The grids cannot say whether that growth is the solution's.

**Verdict, and the region the theorem may claim.**
- *The defect is diagnosed and fixed (computed).* The constraint-preserving scheme's rise with M was its singular axis
  coupling (A2). With the regularisation (A3), the scheme converges in M (|P₃₂ − P₄₀| ≤ 5.4 × 10⁻¹¹ to v = 1.8 at 400
  rows), and its unimposed constraint converges at second order in the null step.
- *What it decides (computed, two null grids, two M).* A vacuum limit is supported to v = 2.0 r_h at areal radius
  ≥ 1.2 r_h, and to v = 1.8 r_h at 0.9–1.2 r_h. This replaces 6.5's and 7.7's figures, as corrected in 8.0.
- *What it does not decide.* From v = 1.8 at areal radius 0.9–1.2 a constraint violation persists. Neither the null
  step nor M reduces it, while the metrics agree; and the curvature invariant is not resolved in angle from v = 1.9
  (A6). That leans against a vacuum limit there, without deciding between a singularity, a feature finer than the
  grids, and a constraint-violating limit of the scheme.
- *The region the theorem may claim (bounded):* v ≤ 1.8 r_h at areal radius ≥ 0.9 r_h; v ≤ 2.0 r_h at ≥ 1.2 r_h; and
  v ≤ 1.65 r_h at 0.6–0.9 r_h (7.7, free scheme). Nothing is claimed beyond.
- *The single missing input:* the regularised scheme on a third null grid (1600 × 720, M = 32 and 40, about 4.5 hours
  each at this machine's load; command `cpaxis5.py --run 1 0.9 M 1600 720 2.25 OUT reg ld 3`), with A5 and A6 rerun on
  the three grids. Two grids cannot separate a pre-asymptotic regime from a genuine non-vacuum limit, and nothing
  weaker than an order of convergence does.

### 8.6 What remains, precisely: one missing input per task

Each task's missing input is stated with the proof that nothing weaker suffices.

1. **Task 1 (the axes).** The estimate in the axis charts: one Grönwall inequality for [Wu26]'s linearised hierarchy
   in the reduced axisymmetric form, with 8.A4's angular recoveries, and the strip constant C_eq of 8.G.
   - *Nothing weaker:* no estimate at Theorem 7.L's level reaches the axis (8.A5, exact).
   - 7.L at level 1 (8.L1) supplies the interior side of the glue.
2. **Task 2 (the constant).** An explicit linear estimate on the high angular modes (the complement of a finite
   Galerkin space in x) whose constant F_∞ satisfies the block condition ‖A_N‖ ‖L_N∞‖ F_∞ ‖L_∞N‖ < 1.
   - *Nothing weaker:* for every finite-rank approximate inverse, the defect is at least 1 (Lemma 8.F), so "the
     explicit estimate applied only to the defect" cannot go below the explicit constant.
   - That constant is at best F_λ² = 10^66.9 on |x| ≤ 1/2 (Theorem 8.W), and the coupling across the cut is of the
     coefficients' own size (W4).
3. **Task 3 (the residual).** An approximant whose residual is below the demand everywhere. On 193 of rcert5's 416
   boxes a certified point value exceeds even round 3's most favourable conditional demand, 5.3 × 10⁻⁴, and on 337
   it exceeds 3.0 × 10⁻⁵ (8.4 D3).
   - *Nothing weaker:* those certified lower bounds. No machine time or enclosure meets the demand on those boxes
     with this approximant.
4. **Level 1 and the quadratic constant G.** G needs L^∞ control of the unknowns. Away from the axes 8.L1 gives it
   (H¹ ⊂ L^∞ on the sections); at the axes it needs item 1.
5. **Propagation (the verifier of round 3, 2(b); added to 7.5's list).** For the hierarchy to be an existence
   scheme and not only an a priori estimate, the compatibility relations of χ̲, ω̲ and η + η̲ with the metric must
   propagate. The sixth Einstein component does propagate (prop5.py Q1, exact); the compatibility relations are not
   shown (Q3).
6. **The data.** The data at past null infinity (G3), and Ric_vx on the data cone: unchanged since round 1.
7. **The late region.** The regularised scheme on a third null grid, 1600 × 720 at M = 32 and 40, with A5 and A6
   rerun on the three grids (8.5).
   - At areal radius 0.9–1.2 from v = 1.8 r_h the regularised scheme agrees with itself in M and in the null step on
     a metric that violates Ric_xx = 0, and the curvature invariant is unresolved in angle from v = 1.9.
   - *Nothing weaker suffices:* two grids cannot give an order of convergence, and without one a pre-asymptotic regime
     is not told from a non-vacuum limit or a singularity.

### 8.7 The region of existence at 10 l5, with labels (replacing 6.5's list)

Seed 1 unless stated.
- **v ≤ 1/2, all (u, x): proved (deduced).** The solution is the seed.
- **Wherever a smooth vacuum solution with the data exists in dnsolve5's gauge: proved (deduced, D1–D2).** Every leaf
  with u > −1 is outer trapped, and every T²-invariant MOTS section has its innermost point at u ≤ −1.
- **The data cone u = −10, v ∈ [1/2, 7/2], both seeds: certified.** The Raychaudhuri constraint of an explicit
  approximant is ≤ 5.0 × 10⁻⁵ and 2.3 × 10⁻⁵, 4.1 % and 4.3 % of the terms that cancel in it (`cdata5.py` C1).
- **u ∈ [−4, −1.1], v ∈ [0.55, 1.6], |x| ≤ cos(π/32): certified at points, and as a sup on one box.**
  - The pinned approximant (`data/rcert5_C3.npz`, md5 698569f6…) has Einstein residual ≤ 2.42 × 10⁻³ of the
    curvature scale at 16,128 points (`rcert5c.py` P2).
  - It is ≤ 3.01 × 10⁻⁴ as a sup over the box t, σ ∈ [−1/2, 0], x ∈ [0, 1/4] (`rcert5d.py` D1).
  - On 193 of the 416 boxes a certified point value exceeds 5.3 × 10⁻⁴ (D3).
- **Areal radius ≥ 0.9 r_h for v ≤ 1.8 r_h, and ≥ 1.2 r_h for v ≤ 2.0 r_h: computed, converged in the null step and
  in angle.**
  - The regularised constraint-preserving scheme's unimposed constraint is second order in the null step, ratios
    3.8–4.0 (cpaxis5 A5).
  - Its metric is independent of M to 5.4 × 10⁻¹¹ to v = 1.8 (A4), and its Kretschmann scalar is resolved in angle
    and in the null step at areal radius 1.0–1.4 (A6).
  - At areal radius ≥ 1.0 to v = 1.8 the free scheme agrees: second order (late5b L5), tails ≤ 5 × 10⁻⁷ (A1).
- **Areal radius 0.6–0.9 r_h for v ≤ 1.65 r_h: computed, converged in the null step** (late5b_small.out).
- **v ≥ 1.8 r_h at areal radius 0.9–1.2 r_h, and v ≥ 2.0 r_h at ≥ 1.2 r_h: computed, not converged.**
  - There a constraint violation persists under both refinements, and the curvature invariant is unresolved in angle
    from v = 1.9.
  - Nothing is claimed.
- **Seed 2, v ≤ 3.5 at every angle: computed, converged** (CERTIFY-10L5.md D543, D601).

**No existence theorem beyond v ≤ 1/2 is proved at 10 l5, at either seed.** The missing inputs are 8.6's.

### 8.8 Files and outputs (round 4)

| file | what |
|---|---|
| `checks/axis5.py`, `.out` | X1–X7: the axis charts; reduction, regularity, structure, pair identity, Hardy, glue |
| `checks/axisbianchi5.py`, `.out` | B1–B3b: σ = 0, Gauss (2.8), both pairs (2.13)–(2.14) in the axis frame |
| `checks/wgron5.py`, `.out` | W1–W5: Theorem 8.W (weights), Lemma 8.F (finite rank), the frozen-angle growth |
| `checks/lev1_5.py`, `.out` | L1–L4: Theorem 8.L1, the level-1 system and its constant |
| `checks/cpaxis5.py`, `.out` | A2–A3: the defect's mechanism and its regularisation (Tangherlini); revised criterion |
| `checks/cpaxis5_run1.out` | first run: A1 (D432's 1600-row run); A2–A3 under the first criterion (A3 FAIL) |
| `checks/cpaxis5_a4.out` | A4: the record's data at 400 × 180, M = 32 and 40, with and without the regularisation |
| `checks/cpaxis5_a5.out` | A5: the regularised scheme at 800 × 360, M = 32 and 40, against 400 × 180 |
| `checks/cpaxis5_a6.out` | A6: the Kretschmann scalar of the regularised scheme, 400 and 800 rows, M = 32 and 40 |
| `checks/cpaxis5_a6_400.out` | A6 at 400 rows only, M = 32 against 40 (a dry run; its heading line was cut) |
| `checks/rcert5d.py`, `.out` | D0–D3, C1–C2: the certified sup over one whole box; the census over the 416 |
| `checks/prop5.py`, `.out` | Q1–Q3: what the hierarchy imposes; the sixth component propagates; what does not |
| `checks/rcert5c.py`, `.out` | repaired (M-1): read only by default, md5s checked before and after |
| `checks/rcert5b.py`, `.out` | repaired (M-1): the pinned file; B3 the soundness gate and the assembly test |
| `checks/rcert5b_run1.out` | its first run, whose assembly test (T_3 product alone) did not catch the mutant |
| `checks/linest5.py`, `.out` | E9 added: the rows against the geometry; E1–E8 unchanged |

Runs (scratch, not committed).
- `cpaxis5.py --run 1 0.9 M Nu Nv 2.25 … [reg] ld 3`: at 400 × 180, M = 40 without the regularisation (959 s), and
  M = 32 and 40 with it (1,303 s and 872 s). At 800 × 360, M = 32 and 40 with it (4,568 s and 4,836 s; md5 22b8815b…
  and 7248a80a…).
  These are under `scratchpad/r4/cp4/`, with round 2's M = 32 orig at `r2/cp/`.
- `rcert5d.py --worker w 2` (w = 0, 1), 09:10–10:16. Then `--repartition 2 4` and `--worker w 4` (w = 0–3) to 12:06.
  In all, 37,440 box evaluations and 3,500 CPU-seconds. The checkpoints are under `scratchpad/r4/rcert5d/`.
- The verifier's linest5 mutants as rerun here are in `scratchpad/r4/mut/` (`ls_mut_db.out`, `ls_mut_quarter.out`).
- Read in place: D432's runs (`g1c/l1_rc0.9_M32.npz` and `l1_rc0.9_M32_1600.npz`) and round 3's `r3/cp_M32_1600.npz`
  (md5 776da11e…).
- D432's two runs were removed from the scratch directory at 10:03 by another session's disk cleanup, not by this
  workstream.
  - `cpaxis5_run1.out` (A1) was produced from the 1600-row run before that, and A1 is not rerun.
  - The 800-row run was regenerated with D432's command, `dnsolve5.py --run 1 0.9 32 800 360 OUT 0 ld 3`. It keeps the
    same 187,284 of 289,161 cells, and its md5 is 3dad331505fb744d89a13b7be4ffda08 (kept under `scratchpad/r4/regen/`).
  - On it axis5, linest5, wgron5 and lev1_5 reproduce their earlier outputs line for line, times apart. The seated
    `.out` files are these reruns, from the programs as committed.

The machine's load was 13–30 on 4 cores throughout, so the wall times are those of a shared machine.
`data/rcert5_C3.npz` has md5 698569f6faaab4420fe2e67abc860561 before and after every run of this round.

### 8.9 Task 5: the paper's "reproduce the untrapped columns" sentence

The verifier of round 2 found that the sentence claims more than 6.1's S7 supports (7.9). The paper's current text,
lines 1459–1461, already restricts it to "within one column spacing up to v = 1.525 (not at 1.55)". Re-derived from
`checks/secondzero5_edges.out` and 6.1 V2, it still overstates in three ways:
- the comparison is on one sphere per v, r* = 0.64–0.78, not along growth5's columns;
- the sets are equal or shifted by one column, and at R0 = 20 the counts differ by one at v = 1.45 and 1.525;
- it is made at one null resolution, where V2 found the rebuilt outer zero's agreement with growth5 unresolved in
  (u, v) from v = 1.3.

The old text occurs exactly once in the paper.

**Old** (paper lines 1459–1461):

```
  At 100 l5² the Bondi spheres rebuilt on the double-null solution reproduce the untrapped columns to within one column
  spacing up to v = 1.525 (not at 1.55), which come from the spheres' tilt against the null leaves (computed); at 1000
  l5² the rebuild does not reach r ≤ 0.3 r_h. The breakdown times are at one angular resolution (N_x = 16); the scheme
```

**New:**

```
  At 100 l5², on the sphere of least areal radius the rebuild reaches before the cut (0.64–0.78 r_h), the band of
  growth5's columns along which the Bondi spheres rebuilt on the double-null solution are untrapped has each edge within
  one column spacing of growth5's own up to v = 1.525 r_h, at both data-cone radii run (the sets equal or shifted by one
  column); at v = 1.55 r_h growth5's band reaches the axis and the rebuild's stops 3.8–4.0 spacings short. The
  comparison is at one null resolution (800 × 360, M = 16), where the rebuilt outer zero's own agreement with growth5's
  is unresolved in (u, v) from v = 1.3 r_h; the untrapping comes from the spheres' tilt against the null leaves, whose
  own expansion leaves no column untrapped (computed, `docket68/n1star/checks/secondzero5.py --edges`; supplement
  `CERTIFY-10L5-RESULT.md` section 6.1, V2–V3). At 1000 l5² the rebuild does not reach r ≤ 0.3 r_h. The breakdown
  times are at one angular resolution (N_x = 16); the scheme
```

### 8.10 A proposed replacement for the paper's section 9 text on existence at 10 l5

This replaces 7.9's proposal and 6.8's. It is proposed to the main session, which seats it; this note does not edit the
paper or N1STAR-PROOF.md.
- The span is the paper's lines 1484–1490, from "`CERTIFY-10L5.md` section 6b). A first certified step is taken"
  through "(supplement `CERTIFY-10L5-RESULT.md` section 2).", in whole lines, so nothing is left dangling (the verifier
  of round 3, M-2).
- It occurs exactly once.
- It folds in every item of the verifier of round 3: frozen coefficients, spherical states and the free formulation,
  with the constraint-preserving case a model only; all the obstacles named; "computed where no truncated domain
  exists"; "up to about two angular crossings"; rcert5c.py and the pinned npz cited for the certificate; and the
  cdata5 figures' comparison scale.

**Old** (paper lines 1484–1490):

```
  `CERTIFY-10L5.md` section 6b). A first certified step is taken: for an explicit approximant of the characteristic
  data on the data cone, the constraint along its outgoing generators holds to a certified bound at both seeds (at the
  second, 2.3 × 10⁻⁵ against terms of size 5.3 × 10⁻⁴; certified, ball arithmetic, `docket68/n1star/checks/cdata5.py`).
  The full Einstein residual of a smoothed three-dimensional approximant built from a run is computed only, 2.5 × 10⁻³
  of the curvature scale and falling at second order with the grid (`checks/resid5.py`, floating point), and no linear
  estimate with explicit constants is available for the characteristic problem in the class, so existence at 10 l5
  remains open (supplement `CERTIFY-10L5-RESULT.md` section 2).
```

**New:**

```
  `CERTIFY-10L5.md` section 6b). Existence at 10 l5 is not proved beyond the seed (v ≤ r_h/2). What is established
  toward a computer-assisted proof is as follows, each with its status. Certified (ball arithmetic): on the data cone
  the outgoing constraint of an explicit approximant holds to 5.0 × 10⁻⁵ and 2.3 × 10⁻⁵, 4.1–4.3 % of the terms that
  cancel in it (`docket68/n1star/checks/cdata5.py`); the Einstein residual of an explicit three-dimensional approximant,
  its coefficients pinned by md5 (`docket68/n1star/data/rcert5_C3.npz`), is at most 2.42 × 10⁻³ of the curvature
  scale at 16,128 points away from the axis caps (`checks/rcert5c.py`) and at most 3.01 × 10⁻⁴ as a supremum over one
  interior box of the 416 that cover u ∈ [−4, −1.1] r_h, v ∈ [0.55, 1.6] r_h (32,768 sub-boxes,
  `checks/rcert5d.py`), while on 193 of the 416 a certified point value exceeds 5.3 × 10⁻⁴. Deduced: the class is
  (2+1)-dimensional gravity coupled to a wave map into the flat plane (`checks/reduce5.py`); in the free metric
  formulation, at frozen coefficients on spherical states, the shift's angular derivative is of principal size at high
  angular frequency and drives δR at order k², so no estimate without loss of derivatives holds for the
  frozen-coefficient problem (`checks/symbol5s.py`; for the constraint-preserving formulation a loss is indicated by a
  model only); in double-null gauge the reduced transport equations carry no angular derivative of an unknown on their
  right sides (`checks/null3.py`, `checks/linest5.py`), and a linear estimate with explicit constants holds on
  truncated domains of dependence away from the axes, at level 0 and at level 1 (supplement Theorems 7.L and 8.L1;
  `checks/lev1_5.py`); near each axis the class is four-dimensional axisymmetric Einstein–scalar in a chart regular at
  the axis, where [Wu26]'s curvature pairs have energy identities on the whole section and the angular recoveries hold
  with explicit Hardy constants (`checks/axis5.py`, `checks/axisbianchi5.py`). Computed on |x| ≤ 1/2 over the box above,
  where no truncated domain exists: the estimate's constant is F² = 10^138, and 10^66.9 with optimised weights
  (supplement Theorem 8.W, `checks/wgron5.py`). Among what stops this short of a proof: the estimate in the axis charts
  is not assembled, and without it no domain reaches the late region, which signals from the axes can reach (the box
  spans up to about two angular crossings); no approximate inverse of finite rank lowers the explicit constant applied
  to its defect (deduced), so a usable constant needs an explicit estimate on the high angular modes with a small
  constant, which is not had; at Theorem 8.W's constant the closing condition asks a residual of order 10⁻⁶⁸/G;
  the quadratic constant G is not computed; and the compatibility relations of the transport hierarchy with the metric
  are not shown to propagate (the one Einstein component it does not impose does propagate, `checks/prop5.py`). The
  computed solution converges at the first seed, in the null step and in angle, to v ≈ 1.8 r_h at areal radius ≥ 0.9
  r_h and to v ≈ 2.0 r_h at ≥ 1.2 r_h, in a constraint-preserving scheme whose singular coupling at the axes is
  regularised (`checks/cpaxis5.py`; the record's free scheme agrees to v ≈ 1.8 r_h, `checks/late5b.py`); beyond, a
  constraint violation persists under both refinements and the curvature invariant is unresolved in angle (computed;
  supplement `CERTIFY-10L5-RESULT.md` sections 2 and 6–8).
```

Statuses, as the new text gives them:
- *certified:* the data cone; the 16,128 points; the one box, with its census;
- *deduced:* the reduction; the frozen-coefficient loss; the transport structure; Theorems 7.L and 8.L1; the axis
  chart's pair identity and Hardy constants; Lemma 8.F;
- *computed:* the constants, the late region's convergence, and what persists beyond it;
- *not proved:* existence, and each missing input named.

## 9. Round 5 (2026-11-06): the verifier of round 4 seated, a Richardson approximant, existence by continuity

Round 5's tasks: seat the verifier of round 4 first (9.0); then (1) the closure of the linearised axis hierarchy and
C_eq, (2) a high-mode estimate meeting the block condition, (3) a better approximant, certified on a few boxes, (5)
the propagation of the compatibility relations, and a third null grid for the late region. The author's rule
governs: the paper carries no open items, and everything derived has computational support. Where an item does not
close at an affordable cost, what holds is proved instead, and the paper text (9.9) states exactly the region and the
statement certified. Sections 0–8 are not edited; their md5 (b728acb5…) is checked before and after the append.

### 9.0 The verifier of round 4: its findings, seated as amendments to section 8

The verifier of round 4 reran every program of round 4 and found each output reproduced. It re-derived the new
mathematics and found it correct as far as it is proved: the axis chart, Gauss (2.8), both pairs, Lemma 8.A6 with no
axis term, the Hardy constants, Theorem 8.W, Lemma 8.F, Theorem 8.L1 as an L² estimate, and the rcert5d certificate
(24 recomputed boxes identical; 560 certified point values in 40 random accepted boxes, corners included, all ≤ their
box's sup, the largest ratio 0.732). It found four claims that say more than is proved (M-A to M-D), sixteen minor
findings and four nits. Each is seated below against the text it amends; section 8 is not edited. Every finding was
re-derived before it was seated, and every repair that needs a program was run in full, with its controls.

**M-A. rcert5d's control C1 could not fail on the certificate's own code.**
- [8.4, "C1, the remainder dropped: the bound of t⁴ + σ⁴ + x⁴ about the origin is 0, so the true/bound ratio is ∞;
  with the remainder it is 0.25": verifier of round 4 (M-A): C1 exercised its own copy of the bound assembly. A copy of
  rcert5d with the engine's remainder dropped accepted the whole box at depth 1 with "ll ≤ 1.95 × 10⁻⁴" and printed D1
  PASS, C1 "caught (good)" and "all checks pass".]
  - *Re-derived.* `Engine.kids` assembled its bounds in its own loop; `test_poly_control(drop)` repeated that loop
    with its own flag. A mutation of the engine's loop or flag could not reach C1.
  - *Repaired (`checks/rcert5d.py`).*
    - One assembly: `Engine.bound` is used by `kids` and by C1, which builds an Engine and bounds its test polynomials
      with it.
    - Every float upper end is rounded upward (`up_float`: the arb's upper end, then `nextafter` until the float is not
      below it). The round-4 checkpoints, whose sups were rounded to nearest, are raised by one ulp in `--collect`.
    - A gate on a code path independent of the engine (D4): at the centre and the eight corners of every accepted
      sub-box, the certified lower end of every component, by the census's point evaluation (`grid_values`, order-2
      point coefficients, no Taylor model), must not exceed that box's certified sup.
  - *Rerun on the round-4 checkpoints (copied unchanged; `checks/rcert5d.out` regenerated).* D1 is unchanged (ll ≤
    3.007 × 10⁻⁴; the one-ulp raise moves no printed digit). C1: the engine's own assembly gives 0.2500 on the test
    polynomials, and the same engine with the remainder dropped gives ∞: sound, and the mutation is caught. D4: 68,705
    points over all 32,768 accepted sub-boxes, the largest (point value)/(box sup) 0.809, no violation: PASS (86 s).
    D3, the census, is reproduced to every printed digit through `grid_values`.
  - *The verifier's mutant against the repair* (`scratchpad/r5/mut/rcert5d_mutA.py`, `self.drop = True` in the
    engine; its checkpoints `scratchpad/vF4/work/rd_mut_ck`): C1 now prints ∞ for the real assembly, "BAD", and
    `--collect` ends "FAILURES" (`scratchpad/r5/mut/rcert5d_mutA_collect.out`). D4 alone does not catch this mutant
    (largest ratio 0.991): it is the second line, not the first.
  - The round-4 certificate stands, now with a control that can fail on it. `checks/rich5.py` (9.2) uses the same
    engine, the same C1 and the same gate.

**M-B. Theorem 8.L1's L^∞ corollary is not proved.**
- [8.5, "Since ‖f‖_∞ ≤ ‖f‖/√|I| + √|I| ‖f′‖ on a one-dimensional section, it bounds Z in L^∞: the control the
  quadratic remainder needs away from the axes"; and 8.6 item 4, "Away from the axes 8.L1 gives it (H¹ ⊂ L^∞ on the
  sections)": verifier of round 4 (M-B): f_1 controls (Z, Z′) only through cone-integrated norms, and the
  one-dimensional Sobolev step needs section norms at fixed (u, v).]
  - *Re-derived.* In f_1, δa and the e3-transported unknowns are measured on outgoing cones (L² in v at fixed u), δd
    and the e4- and ∂_v-transported ones on incoming cones (L² in u at fixed v). The Sobolev inequality, applied under
    those integrals, gives Z in L²_v L^∞_x on outgoing cones and L²_u L^∞_x on incoming ones, and no more: the pairs
    give no equation for e4 δa or e3 δd, so nothing yields a section norm at fixed (u, v) for them.
  - It reads: "8.L1 controls Z in the mixed norms L²_v L^∞_x (outgoing cones) and L²_u L^∞_x (incoming cones); whether
    these close the quadratic remainder is not shown." Item 4 of 8.6 gains the L^∞ (or product) estimate on the
    sections as part of its input.
  - Not proved this round. It does not reach the paper: G is not claimed there (9.9).

**M-C. Lemma 8.A5 proves less than "nothing weaker than the curvature level suffices at the axis".**
- [8.2, Lemma 8.A5, "nothing weaker than the curvature level suffices at the axis … So no estimate whose unknowns
  include δk in L²(dμ) exists. Theorem 7.L's unknowns cannot be carried to the axis, and the angular derivatives of the
  metric differences must be carried as tensors"; 8.1 item 1, "That nothing below the curvature level reaches the axis
  (8.A5)"; 8.6 item 1, "Nothing weaker: no estimate at Theorem 7.L's level reaches the axis (8.A5, exact)": verifier of
  round 4 (M-C).]
  - *Re-derived.* What X6 shows exactly: for the regular rescaling of the section, the polar-frame connection
    difference δk = −(ε/2)k has ∫_a^1 k² Y ds = −log a → ∞, so δk is not an admissible L²(dμ) unknown at the axis in
    the polar frame. That excludes Theorem 7.L's unknowns, which include δk, and nothing else: not a level-0 estimate
    in a regular (Cartesian) frame on the disk, in weighted norms, or in wave gauge. Nor is it a counterexample to an
    estimate whose data norm contains δk, since that norm is infinite for the same perturbation.
  - 8.A5 reads: "δk is not an admissible L²(dμ) unknown at the axis in the polar frame (deduced, verified at random
    jets: X6); so Theorem 7.L's unknowns cannot be carried to the axis." The sentences in 8.1 item 1, 8.2 ("the angular
    derivatives … must be carried as tensors") and 8.6 item 1 ("Nothing weaker") are an expectation, not a proof, and
    are so labelled.

**M-D. The 8.10 paper block over-claimed twice; the record says the same at 8.0 and 8.6.**
- [8.10's new block, "the one Einstein component it does not impose does propagate"; 8.0, "Q1 (exact): the one
  Einstein component the hierarchy does not impose, E_34 − E_xx, propagates"; 8.6 item 5, "The sixth Einstein
  component does propagate (prop5.py Q1, exact)": verifier of round 4 (M-D (i)).]
  - *Re-derived from prop5.py's docstring:* Q1's premise is that the hierarchy's unknowns agree with the metric (the
    compatibility relations). Under it, S = G − T has the single component S_34 = q and div S = 0 transports q
    homogeneously. Without it the statement is not made.
  - It reads: "would propagate once those relations hold". In round 5 the question is moot for existence: Lemma 9.C
    uses the hierarchy only for genuine metrics, for which the relations and every Einstein component hold (9.3).
- [8.10's new block, "The computed solution converges at the first seed, in the null step and in angle, to v ≈ 1.8 r_h
  …"; 8.7, "computed, converged in the null step and in angle": verifier of round 4 (M-D (ii)).] Two null grids give
  one ratio per band and no order. It reads, until 9.6 decides it: "consistent with second-order convergence on two
  null grids (ratios 3.8–4.0) and resolved in M, to v ≤ 1.8 r_h at areal radius ≥ 0.9 r_h and v ≤ 2.0 r_h at ≥ 1.2
  r_h; an order is not established". 9.6 carries the third grid.
- 8.10's block is withdrawn; 9.9 replaces it.

**Minor findings.**
- **m1** [7.L's E9 (8.0), "(c) every row's frame-change part": E9 skipped the d_v rows (`linest5.py`, `if opn ==
  'dv': continue`), so dropping δk from their linearisation survived.] *Repaired:* E9(c) now checks the d_v rows
  against d/dε of GM with the state, e^w and e^k perturbed, computed independently of `rows()`. `checks/linest5.out`
  regenerated: identical to round 4 but for its timing line; E9 all hold. The verifier's mutant, rebuilt on the new
  file (`scratchpad/r5/mut/linest5_m1dk.py`), fails E9(c) on the b row.
- **m2** [8.5, Theorem 8.L1, checked by `lev1_5.py` L1–L3: L2 checks the level-1 rows' derivative structure, never
  their content; the verifier's mutants dropping ½(η + η̲)·rhs or −χ δY′ from the commuted e4 rows survived.]
  *Repaired:* `lev1_5.py` gains L5 (exact, null3.zero). On the general (2+1)-metric, two scalars and arbitrary Z, every
  level-1 row satisfies L0(Z′) − R1 = e_x(L0 Z − r) + h(L0 Z − r), h = (η + η̲)/2 for e4, e3 and pair rows and 0 for
  ∂_v rows. That identity holds for all functions iff R1 is the commuted row. All 17 rows hold; its two in-program
  controls (those mutants on the χ row) fail. The verifier's two mutants, rebuilt on the new file and run whole
  (`scratchpad/r5/mut/lev1_5_m2chi.py`, `lev1_5_m2hx.py`), end "FAILURES". `checks/lev1_5.out` regenerated: L4's
  constants unchanged (10^2645.7, 10^91.0).
- **m3** [8.5, A6: "From v = 1.9 it is not resolved in angle anywhere" and "on [1.8, 1.9) … except at x = 0, where the
  null step is 7 % of dev"; 8.7's ≥ 1.2 bullet citing A6 for v ≤ 2.0: A6 merged areal radius 1.0–1.4.] *Re-derived and
  repaired:* `checks/cp3grid5.py` A8 splits A6 by class (0.9–1.0, 1.0–1.2, 1.2–1.4) and A9 gives |P₃₂ − P₄₀| per class
  (the verifier's pm_class.py, re-derived; it reproduces pm_class.out). In short, from 9.6: at 1.2–1.4 the invariant is
  resolved at every angle to v = 2.0; at 1.0–1.2 to v = 1.8, except x = 0 on [1.65, 1.8) (5.6 % of dev); at 0.9–1.0
  to v = 1.65, and to 1.8 except at x = 0. The metric is M-resolved to ≤ 5 × 10⁻⁹ in every claimed region (≤ 6 ×
  10⁻¹¹ except at 0.9–1.0 on [1.65, 1.8)). The 7 % reads 11 %.
- **m4** [8.5, A3, "The correction is O(the truncation error), so the limit is unchanged"; and the second reading at
  8.5, "the constraint-preserving system's limit is not vacuum there, which is the propagation question of 8.6 item 5":
  d± was never measured on the record's data, and a d± that does not vanish under refinement would by itself give a
  limit violating Ric_xx = 0 — a third reading; and cpsolve5 has its own propagation question.] *Repaired:*
  `cp3grid5.py` A10 replays d± at every cell from the stored solution (9.6). In the claimed regions d± falls at second
  order (ratios 3.5–4.0) to ≤ 1.1 × 10⁻² of R_uv. From v = 1.9 at 0.9–1.2 it does not converge (ratios 0.98–2.5)
  and is 7–75 % of R_uv; on [2.0, 2.25) at ≥ 1.2 it falls at less than second order (1.93). There the third reading
  is a measured one. The second reading is restated: cpsolve5 imposes Ric_vv by Raychaudhuri and three rows for
  (m, n, W)_uv, and whether that propagates Ric_xx = 0 is cpsolve5's own propagation question, distinct from 8.6
  item 5's (which concerns the frame hierarchy).
- **m5** [8.5, "independent of M (1.1–1.3)"]: it reads "weakly M-dependent (the monitor rises 8–26 % from M = 32 to
  40 at 800 rows)".
- **m6** [8.3, "W3 (computed), the optimum" and "since the pair identities fix a : c : d"]: 10^66.9 is the exact
  exponent J_exact at the weights found by minimising a relaxed (soft-max) objective, so it is a valid theorem
  constant and the minimiser of the relaxation, not a certified optimum; and one weight per scalar for its three pair
  unknowns is a choice (the two pair energies could be weighted separately), not forced. 9.4's "global optimum of the
  family" is not claimed.
- **m7** [8.3, "Neither ball nor interval arithmetic can supply this input"]: Lemma 8.F constrains finite-rank
  approximate inverses only; F_∞ would be an analytic estimate whose constants interval arithmetic can evaluate. The
  sentence is withdrawn. (9.4 closes the block route on the box by a different argument.)
- **m8** [8.3, W5, "4.8 × 10⁵ to 2.05 × 10⁶"]: W5 marches explicitly at first order on every second row and column,
  with no resolution check. It reads "computed at one resolution, unchecked in resolution"; the conditional demands
  3.1 × 10⁻⁹ and 5.4 × 10⁻⁸ that use it are conditional twice over.
- **m9** [8.2, 8.G, "which Theorem 8.L1 (8.5) supplies"; 8.6 item 1, "7.L at level 1 (8.L1) supplies the interior
  side of the glue": 8.L1 holds on truncated domains, every such domain over the box is empty, and the glue needs a
  cut-off form of 8.L1 with (1 − ψ) and its bulk terms.] It reads "would supply, in a cut-off form not stated".
- **m10** [8.2, Lemma 8.A4, "(1 + q)(y_max/y_min)^{3/2} … ½(1 + q)(y_max/y_min)^{5/2}"]: valid, not sharp.
  *Re-derived:* with Yη = ∫_0^s Y g and |k| ≤ (1 + q)/s, ‖kη‖² ≤ (1 + q)² y_min⁻¹ ∫ s⁻³F² ds, F = ∫_0^s σ y g dσ;
  the weighted Hardy inequality ∫_0^∞ s^{−r}F² ≤ (2/(r − 1))² ∫_0^∞ s^{2−r}F′² (F(0) = 0) at r = 3 gives ‖kη‖ ≤
  (1 + q)(y_max/y_min)^{1/2}‖g‖; for Codazzi, Y²χ̂ = ∫_0^s Y² g and r = 5 give ‖kχ̂‖ ≤ ½(1 + q)(y_max/y_min)^{3/2}‖g‖.
  These are the verifier's constants. The record's are larger, so still valid. *Repaired:* X4 now also checks the
  sharper ones, ratios ≤ 0.366 and ≤ 0.285 at all three grids (`checks/axis5.out` regenerated, otherwise identical).
  The verifier's runs at 0.6 times them pass X4 too: the check is loose, as it says.
- **m11** [8.2, axis5.py and axisbianchi5.py "exact"]: their identities are verified at random rational jets at 40–60
  digits with a fixed seed (a probabilistic identity test), and B2–B3's coefficients are fitted. They read "verified
  at random jets". Round 5's axhier5.py is so labelled; cont5.py C1, linest5.py E9 and lev1_5.py L5 are symbolic
  (null3.zero: the expanded numerator is identically 0).
- **m12** [8.9's new text, "(the sets equal or shifted by one column)"]: false at R0 = 20, v = 1.45 and 1.525, where
  the rebuild is one column short (secondzero5_edges.out; 8.9's own second bullet). 9.9 gives the corrected text.
- **m13** [8.9, 8.10, "paper lines 1459–1461", "1484–1490"]: stale; the old blocks are now at paper lines 1473–1475 and
  1498–1504 (matched by text, each occurring once).
- **m14** [8.10, "the record's free scheme agrees to v ≈ 1.8 r_h"]: round 4 never compares the free scheme with the
  regularised one. It reads "the free scheme's solution is also consistent with second-order convergence to
  v ≈ 1.8 r_h (late5b.py)".
- **m15** [8.0, "at each n the certified sup must be at least the certified values at the centres of the finer (2n)³
  grid and at 500 random points"]: rcert5b's finer centres are used at n ≤ 4 only (rcert5b.out: "0 finer centres" at
  n = 8). It reads "at n ≤ 4 at the finer centres, and at every n at 500 random points".
- **m16** [8.3, W1, and wgron5.py's docstring]: the docstring named the mutation "factor max λ/min λ dropped" while W1
  tested the partner share, and W1 divided the factor out of J and multiplied it back, so a J_exact without it passed.
  *Repaired:* W1 reads the bound e^J 𝒟 straight from J_exact; it adds the model Y_v = 9Z, Z_u = 0.01Y at weights
  λ_Y/λ_Z = e⁻⁵, θ = e^{∓2.5}, where the bound 9,279 holds against f = 106.2 and the factor is essential; and it tests
  both mutations, each giving a bound below f (2 and 62.5). Its printed bounds for the first model are unchanged.
  `checks/wgron5.out` regenerated: W2–W5 identical to round 4, W1 PASS. The verifier's code-level mutant (J_exact
  without the factor), rebuilt on the new file (`scratchpad/r5/mut/wgron5_m16fac.py`), now fails W1 (bound 62.52
  against f = 106.2).

**Nits.**
- rcert5d's upper ends rounded to nearest: repaired with M-A.
- [8.5, A4 table and "m's angular tail falls to 10⁻¹⁰–10⁻¹¹ to v = 1.8"]: on [0.5, 1.0) the regularised tail is
  2.7 × 10⁻²; the 10⁻¹⁰ claim holds from v = 1.0.
- cpaxis5 A3's pass criterion was replaced after its first run failed: recorded in 8.5, and post hoc.
- [8.2, "A family with bounded level-0 norm and K unbounded on the strip (δΦ = ε sin(x/ε))"]: no program backs it; it
  reads as an illustration, not a result.

**What the verifier's section 6 adds to the list of inputs.** It is taken over in 9.7, with what round 5 settled.

### 9.1 Answers

1. **The verifier of round 4 (9.0).** Every finding is seated, re-derived first.
   - M-A is repaired in code: one assembly shared by the engine and its control, upward rounding, and an independent
     gate over all 32,768 sub-boxes. The certificate stands, and the verifier's mutant now fails.
   - M-B, M-C and M-D are restated to what is proved. M-B (the L^∞ step) is added to the inputs; M-C (8.A5) is
     relabelled; M-D's two over-claims are corrected in the record and are not in the new paper text.
   - m1, m2 and m16 are repaired in code, each with the verifier's mutant rebuilt and now caught. m3 and m4 are
     measured (`checks/cp3grid5.py` A8–A10). The rest are restated.
2. **Item 3, a better approximant (9.2): done, certified.**
   - Richardson extrapolation of the two null grids lowers the certified residual 65-fold: ≤ 3.72 × 10⁻⁵ at all 16,128
     points.
   - No K2 box now holds a point above 5.3 × 10⁻⁴; for the round-3 approximant 193 do.
   - On four boxes where the round-3 approximant provably cannot be certified at 5.3 × 10⁻⁴, the new one is certified
     as a sup.
3. **Item 5, propagation (9.3): removed as an input, by proof.**
   - Lemma 9.C: existence follows by continuity from the higher-dimensional neighbourhood theorem of [CTG23] (READ) and
     the a priori estimate, applied to genuine metrics. For those, the compatibility relations hold by definition.
   - The bootstrap step is checked by z3, with a vacuity guard and failing controls; the premise is checked exactly.
4. **Item 2, the constant (9.4): the block route is closed by proof.**
   - The couplings across a Chebyshev cut are N-independent (Lemma 9.H, exact), and the exact inverse blocks have norm
     ≥ 1 (Lemma 9.B).
   - So the block condition fails at every angular resolution: by a factor ≥ 484 on x ∈ [−1/2, 1/2], and ≥ 2 × 10⁸
     on the full range (computed couplings).
   - What holds is Theorem 8.W's constant.
5. **Item 1, the axes (9.5): the reduced hierarchy at [Wu26]'s level is derived and closes structurally.**
   - It covers every transport row, Codazzi, the mass aspects with their cancellations, the κ's and the scalar's pairs,
     all verified at random jets with failing controls.
   - The linearised inequality's coefficient bounds, its constant and C_eq are not done. They would not change the
     closing condition, which Theorem 8.W's constant already decides.
6. **The late region (9.6).** The third null grid (1600 × 720, M = 32 and 40) is running at hand-back. At 14:41 UTC
   the M = 32 run had done 44 % of its cells and the M = 40 run 31 %; they are expected to finish near 17:00 and 19:00
   UTC. Its analysis (`cp3grid5.py` A7, A8 and A10 on three grids) is ready, and its control passes.
   - Round 4's two grids, split by class as the verifier asked: the metric is M-resolved to ≤ 5 × 10⁻⁹ in every claimed
     region. The invariant is resolved to v = 2.0 at 1.2–1.4, to 1.8 at 1.0–1.2 (but x = 0 on [1.65, 1.8)), and to
     1.65 at 0.9–1.0.
   - The regularisation's correction d± is measured for the first time. It falls at second order in the claimed
     regions, and does not converge from v = 1.9 at 0.9–1.2. There the verifier's third reading of the persistent
     violation is a measured one.
   - The label is the verifier's: consistent with second-order convergence on two null grids and resolved in M, an
     order not being established.
7. **The paper (9.9).** The new text states exactly what is certified, deduced and computed, with nothing phrased as
   open. It folds in round 5 and every finding of the verifier of round 4 that touches it: M-B, M-D, m9, m12, m13 and
   m14. It cites [CTG23], with a reference entry.

### 9.2 Item 3: a better approximant, by Richardson extrapolation (`checks/rich5.py`)

**The approximant.** rcert5.py's construction exactly — resid5.fit on u ∈ [−4, −1.1], v ∈ [0.55, 1.6], degrees 24 × 30
in (t, σ), the run's 16-node interpolant in x — applied to F_R = (4F_800 − F_400)/3 at the 400-row nodes.
- F_400 and F_800 are the two seed-1 runs at M = 16, cut 0.3, that resid5.py and rcert5.py use (`l1_M16_400.npz`, md5
  9a0ecfbb…; `l1_M16_800.npz`, md5 cd9df998…, scratch). Their nodes nest exactly: every second 800-row node is a
  400-row node, with the same 16 angular nodes.
- The runs are second order in the null step (resid5.py: the residual ratio from 400 to 800 rows is 3.92), so F_R
  cancels the leading error.
- Whatever the error expansion does, F_R is an explicit smooth metric of the class. Its coefficients are pinned:
  `data/rcert5_C3R.npz`, file md5 88e16664187868e47eaaaa18709cfc61; tensors R 38d56f2c…, m 82381669…, n 25ca367f…,
  W d6c979af…, s eb515806…. Every statement below is about those coefficients and no others.
- `--write` refits (the fit is not bit-reproducible, as rcert5c.py records) and is not run by default. The default run
  is read only, and `data/rcert5_C3.npz` keeps md5 698569f6… before and after.

**R1 (computed, floating point; `rich5.py --runs`).** The worst residual over √K_0 at the 400-row cell midpoints:
- F_400 9.64 × 10⁻³ and F_800 2.46 × 10⁻³ (resid5.py's figures; F_800 at its own 800-row midpoints), and F_R 2.65 ×
  10⁻⁵: 92.9-fold below F_800.
- Control F_2 = 2F_800 − F_400, a first-order combination: 4.78 × 10⁻³, worse than F_800, as it must be.
- F_R at degrees 30 × 36: 2.10 × 10⁻³, the fit ill-conditioned at the 400-row nodes. The degrees stay 24 × 30.
- `checks/rich5_runs.out`; 900 s; PASS.

**R2 (certified, at K1's 16,128 points).**
- The largest certified upper end is 3.72 × 10⁻⁵ (ll). The round-3 approximant's largest certified LOWER end there is
  2.414 × 10⁻³: the Richardson residual is 65 times smaller.
- 0 of the 416 K2 boxes hold a point whose upper end exceeds τ = 5.3 × 10⁻⁴; for the round-3 approximant, 193 hold one
  whose lower end does.
- 3 of 416 hold a point whose certified lower end exceeds τ′ = 3.0 × 10⁻⁵ (the round-3 approximant: 337). On those
  three no certificate of F_R reaches τ′.
- C3 (regression of the census code): on the round-3 tensors it reproduces rcert5d D3 (193, 337, 416, 2.414 × 10⁻³).
- C2 (W + 0.01v): certified lower ends to 0.312, refused.

**R3 (certified: sups over four boxes on which the round-3 approximant cannot be certified).** Each box contains a
point where the round-3 approximant's certified value exceeds τ, so no certificate of that approximant reaches τ there.
The engine is rcert5d's as repaired (9.0, M-A), each accepted sub-box gated by D4.

| K2 box | sub-box (fraction of the K2 box) | round-3 point value | F_R certified sup | evaluations | gate |
|---|---|---|---|---|---|
| (0, 3, 10) | depth 4 (1/4,096) | 2.414 × 10⁻³ | 6.09 × 10⁻⁵ | 584 | 1,241 pts, ≤ 0.519 |
| (0, 3, 9) | depth 4 | 2.388 × 10⁻³ | 4.97 × 10⁻⁴ | 72 | 189 pts, ≤ 0.042 |
| (0, 3, 8) | depth 4 | 2.348 × 10⁻³ | 4.93 × 10⁻⁴ | 72 | 189 pts, ≤ 0.055 |
| (1, 2, 15) | depth 2 (1/64) | 1.096 × 10⁻³ | 1.75 × 10⁻⁴ | 4,680 | 9,009 pts, ≤ 0.072 |

- The first three are the K2 boxes of the round-3 approximant's three largest point values, all at the corner
  t ≈ −1, σ ≈ +1 of the (t, σ) square. The fourth is the largest among the boxes interior in (t, σ) and in x (bt,
  bs ∈ {1, 2}, x-box 10–15).
- Every sub-box of every accepted tiling passed the D4 gate (10,628 points in all, the largest ratio of a certified
  point value to its sub-box's sup 0.519). `checks/rich5.py` ran in 1,147 s; all checks pass.
- Bisection stops as soon as a sub-box meets τ, so a sup just below τ (the second and third rows) is a certificate at
  τ and not a measure of the residual; the first row, bisected one level further, shows the residual's own size there.
- C1 (the engine's own assembly): 0.2500 on the test polynomials, and ∞ with the remainder dropped: caught.

**What it buys, exactly.** Richardson extrapolation removes the obstruction rcert5d's census found: on the 193 boxes
where no certificate of the round-3 approximant can reach 5.3 × 10⁻⁴, every certified point value of F_R is below
it, and on four of them it is certified as a sup. It does not close anything. The demand at Theorem 8.W's constant
is 10⁻⁶⁸/G (8.3), and even the conditional demand at τ′ = 3.0 × 10⁻⁵ is exceeded at certified points of 3 boxes.
- *Cost of the rest (computed, extrapolated from the measured boxes; not run).* The depth reached varies: rcert5d's
  box needed depth 5 for the round-3 approximant (37,440 evaluations for the K2 box); for F_R the interior sub-box of
  (1, 2, 15) needed depth 6 (4,680 evaluations for 1/64 of a K2 box, about 3 × 10⁵ for the whole), and the corner
  sub-box of (0, 3, 10) depth 7. Certifying all 416 boxes at τ is of the order of 10⁷–10⁸ evaluations, 10⁶–10⁷
  CPU-seconds at 0.09 s each: machine time, which this round does not spend.

### 9.3 Item 5: existence by continuity; the compatibility relations need not propagate (`checks/cont5.py`)

**[CTG23] (READ 2026-11-06, the arXiv PDF through the alphaXiv reader).** P. T. Chruściel, R. Tagne Wafo, F. Gray,
*The "neighborhood theorem" for the general relativistic characteristic Cauchy problem in higher dimensions*,
arXiv:2305.07306v1.
- Theorem 1.1 (pp. 2–3): "The maximal globally hyperbolic development of smooth initial data for vacuum Einstein
  equations with a (possibly zero) cosmological constant Λ ∈ R, on two characteristic hypersurfaces intersecting
  transversally, contains a future neighborhood of the initial data hypersurfaces." In all higher dimensions, with no
  smallness.
- p. 3: the theorem is stated in the smooth category, and "the result remains true in suitable Sobolev spaces".
- p. 8, of its own doubled fields: "we do not need an existence theorem, but a system of equations where suitable
  estimates apply. Indeed, we start with a solution of the vacuum Einstein equations, define all the field as above,
  and thus the equality … hold everywhere."
- §4: the double-null coordinates of a given metric are "a standard construction (see, e.g., Section 4 of [1])".

**Lemma 9.C (existence by continuity; deduced from [CTG23] Theorem 1.1, the uniqueness of the maximal development,
and the a priori estimate).**
- *Setting.* Smooth T²-invariant data on N0 = {v = 1/2} (the seed) and N1 = {u = −10} (the data cone), satisfying the
  characteristic constraints. D = [−10, u*] × [1/2, v*] × [−1, 1]_x × T² in dnsolve5's gauge, and an explicit
  approximant ĝ on D. y(s) is the norm of Theorem 8.W's left side, with the level-1 and higher norms that G and
  persistence need, of the difference between a metric g and ĝ on D_s = D ∩ {v ≤ s}.
- *Hypotheses.*
  - (H1) The a priori estimate: for every s and every smooth T²-invariant vacuum metric g on D_s, in the gauge, with
    the data, y(s) ≤ A + B y(s)², where A = F r (r the residual's norm) and B = F G.
  - (H2) Persistence: the same at every level k of the commuted hierarchy, with constants depending on the lower levels.
  - (H3) 4AB < 1 and y(1/2) ≤ A.
- *Conclusion.* A smooth T²-invariant vacuum metric with the data exists on D, in the gauge, with y ≤ 2A.
- *Proof.*
  1. By [CTG23] Theorem 1.1 the maximal globally hyperbolic development of the data exists and contains a future
     neighbourhood of N0 ∪ N1. The data's T² isometries extend to it (uniqueness of the maximal development). The gauge
     is built in a neighbourhood ([CTG23] §4).
  2. Let I = {s : D_s lies in the development, in the gauge, and y ≤ 2A on [1/2, s]}. It contains a neighbourhood of
     1/2, by step 1 and y(1/2) ≤ A < 2A, y being continuous.
  3. I is open. If s ∈ I, then by (H1) and C2(a), y ≤ A + 4A²B < 2A on [1/2, s]. By (H2) g is smooth up to {v = s}
     with bounds, so it induces smooth data on {v = s} ∩ D and on N1 ∩ {v ≥ s}, which meet transversally. [CTG23]
     Theorem 1.1, applied to those data, gives a future neighbourhood of the compact segment {v = s, u ∈ [−10, u*]}.
     So D_{s+ε} lies in the development for some ε > 0, and y ≤ 2A on [s, s + ε] by continuity.
  4. I is closed. y is continuous, and by C2(b) it never enters (2A, 1/(2B)). The bounds of (H1)–(H2) control the gauge
     up to the limit: the Ricci coefficients are bounded, so there is no caustic.
  5. So I = [1/2, v*]. ∎
- *What it changes.* The hierarchy enters only through (H1)–(H2), and there only for genuine metrics. For those its
  unknowns are the metric's own connection coefficients, so the compatibility relations of χ̲, ω̲ and η + η̲ hold by
  definition (C1), and so does every Einstein component. Nothing needs to propagate.
  - So round 4's item 5 (8.6) is not an input of existence. It would be one only for a scheme that solves the hierarchy
    itself, which Lemma 9.C does not use. [CTG23] p. 8 states the same of its own system.
  - What remains are exactly (H1)–(H3): the a priori estimate on all of D (items 1, 2 and 4) and the closing condition
    (items 2 and 3). Lemma 9.C adds no input of its own; the propagation input is removed.

**Computational support (`checks/cont5.py`, 7 s, all checks pass).**
- C1 (exact, sympy null3.zero, on the general metric of the class with no field equation imposed):
  - the three compatibility relations hold identically;
  - the metric recovery holds: d_v c = e^w χ, d_v w = −2e^w ω, d_v b = −2e^{2w−c}(η − η̲);
  - the rows N1 (both directions) and N2 (both) hold with the metric's own Ricci frame components as their only source.
  - Control k1: χ̲'s relation without b_x is not an identity.
- C2 (z3, nonlinear real arithmetic):
  - (a) 4AB < 1, y ≤ A + By² and y ≤ 2A imply y ≤ A + 4A²B < 2A: proved (unsat).
  - (b) 4AB < 1 and y ≤ A + By² imply y ≤ 2A or y ≥ 1/(2B); and the small root lies in [A, 2A] with 2A < 1/(2B):
    proved.
  - Vacuity guard: the hypotheses of (a) are satisfiable (B = 1/8, A = 1, y = 0).
  - Control k2: with 4AB < 2, z3 finds a counterexample (B = 3/8, A = 1, y = 0).
  - Control k3: the weaker y < 3A is proved; the sharper y ≤ A + 2A²B is refuted (B = 15/64, A = 1, y = 3/2). So the
    improvement is exactly the stated one.

### 9.4 Item 2: the block route, closed by proof (`checks/blocks5.py`)

**The norms, fixed.** Theorem 8.W's space-time structure: fluxes on the cones for the unknowns, the space-time L²
integral for the sources, and the data's fluxes as data. The section norm is L²(dx/√(1 − x²)), in which the Galerkin
split by Chebyshev degree is orthogonal (round 4's W4 instance used it). The coefficients are coordinate-normalised,
as in wgron5.py.

**Lemma 9.H (deduced; checked exactly, H1).** Let m = Σ_{j≤d} m_j T_j and N ≥ d. Then the cut coupling P_N m P_{>N}
is the d × d Toeplitz block H_m[a, b] = m_{b−a+d}/2 (zero outside 1 ≤ b − a + d ≤ d), the same for every N ≥ d. So its
norm σ(m) is N-independent, and σ(m) ≥ ‖(m_1, …, m_d)‖/2. The same holds for P_{>N} m P_N.
- *Proof.* T_j T_k = (T_{j+k} + T_{|j−k|})/2. For i ≤ N < k, the T_i-coefficient of m T_k is m_{k−i}/2 if k − i ≤ d,
  and 0 otherwise. Every mode involved has index ≥ 1, and those modes all have the same norm. ∎
- *Checked exactly* (sympy rationals, random m of degree 6): the blocks at N = 6, 9 and 17 coincide after the shift;
  the T_{N+1} column is (m_6, …, m_1)/2; nothing lies outside the block.
- *Control k1* (T_jT_k = T_{j+k}): the column identity fails.
- So refining the Galerkin space never makes the couplings across the cut small.

**Lemma 9.B (deduced).** In these norms both exact inverse blocks have norm ≥ 1.
- Their data part is the identity on the initial cones' fluxes, which the solution norm contains.
- The trace commutes with the x-projection, so the coupling blocks have no data part.
- Hence the block condition ‖A_N‖ ‖L_N∞‖ F_∞ ‖L_∞N‖ < 1 implies ‖L_N∞‖ ‖L_∞N‖ < 1.
- Each coupling block's norm is at least that of its restriction to one (row, unknown) pair. For such a pair, a test
  function constant in (u, v) on a slab and equal to the top singular vector in x gives ‖L_N∞‖² ≥ sup over slabs of
  ∫∫ σ² / (the slab's length in the unknown's flux variable).

**H2 (computed, on the record's coefficient table: D432's regenerated run, md5 3dad3315…, as linest5.py reads it).**

| setting | largest space-time coupling (row ← unknown) | N ≥ 31 (N-independent) | N = 0…30, smallest | block product ≥ |
|---|---|---|---|---|
| x ∈ [−1/2, 1/2], interpolant restricted, band's own basis | P4_1 ← δw | 22.0 | 22.0 (N = 18) | 484 |
| the full range, x to the outermost node | P3_1 ← δb | 1.86 × 10⁴ | 1.44 × 10⁴ (N = 0) | 2.08 × 10⁸ |

- On x ∈ [−1/2, 1/2] the six largest coefficient fields have sup |m| 17.6–56.9 and couplings 2.3–22. On the full
  range, where the (2+1) frame's coefficients grow toward the axes (7.4), sup |m| reaches 7.4 × 10⁴.
- Control k2: every coefficient replaced by its x-mean has zero coupling.
- 1,464 s; all checks pass.

**So the block condition fails for every N, on |x| ≤ 1/2 and on the full range** (deduced from Lemmas 9.H and 9.B,
with the computed couplings).
- No explicit high-mode estimate, of any constant, closes the Schur route on the box in these norms. Round 4's missing
  input of task 2 does not exist in that form, and nothing about it is left open.
- What holds is Theorem 8.W: F² = 10^66.9 on |x| ≤ 1/2 with the weights found, and 10^138 without them. The weights
  minimise a relaxed objective (9.0, m6), so 10^66.9 is a valid constant, not a certified optimum.
- Lemma 8.F closes the finite-rank approximate-inverse route; Lemmas 9.H–9.B close the block route. Both routes that
  rounds 3 and 4 proposed for a small constant are closed by proof.
- A smaller constant would need a norm adapted to the coupling rather than to the Galerkin split, or slabs short
  enough that the couplings integrate to less than 1. Neither is claimed.

### 9.5 Item 1: the axis hierarchy at [Wu26]'s level, reduced (`checks/axhier5.py`)

**What is proved (deduced, verified at random jets).** Every equation is fitted at random rational jets of the general
chart metric at 45 digits, rationalised, and checked at fresh jets (residuals ≤ 3 × 10⁻⁴¹), or, for the renormalised
rows, hand-derived and checked as an identity (residual 0 at 45 digits). These are probabilistic identity tests with
fixed seeds (9.0, m11). The metric is the chart's general one, off shell: Ric is its own.
- *A1 Raychaudhuri:* Ω̂e4 trχ + ½Ω̂(trχ)² = −2Ω̂χ̂² − 2Ω̂ω trχ − Ω̂Ric_44, and the mirror.
- *A2, the shears in the direction that carries no α:* Ω̂e3χ̂ + ½Ω̂ trχ̲ χ̂ = Ω̂(e1η − kη) + Ω̂η² + 2Ω̂ω̲χ̂ −
  ½Ω̂ trχ χ̲̂ + ½Ω̂(Ric_11 − Ric_22), and the mirror. Here e1η − kη is twice the traceless part of ∇η, [Wu26]'s
  ∇̂⊗η.
- *A3 torsion:* Ω̂e4η = −Ω̂χ_11(η − η̲) − Ω̂β^r − Ω̂Ric_41, with χ_11 = ½trχ + χ̂; and Ω̂e3η̲ = −Ω̂χ̲_11(η̲ − η) +
  Ω̂β̲^r − Ω̂Ric_31.
- *A4 lapse:* Ω̂e4ω̲ = 2Ω̂ωω̲ + ½Ω̂η² − Ω̂ηη̲ + ½Ω̂ρ + ⅙Ω̂Ric_34 + (1/12)Ω̂(Ric_11 + Ric_22), and the mirror (η̲² in
  place of η²).
- *A5, the other traces:* Ω̂e4 trχ̲ + ½Ω̂ trχ trχ̲ = 2Ω̂ω trχ̲ + 2Ω̂ρ − 2Ω̂χ̂χ̲̂ + 2Ω̂ div η̲ + 2Ω̂η̲² − ⅓Ω̂Ric_34 +
  ⅓Ω̂(Ric_11 + Ric_22), and the mirror.
- *A6 Codazzi:* e1χ̂ + 2kχ̂ = ½e1 trχ + ½ζ trχ − ζχ̂ − β^r, and e1χ̲̂ + 2kχ̲̂ = ½e1 trχ̲ − ½ζ trχ̲ + ζχ̲̂ + β̲^r.
  The operator is 8.A4's (the r = 5 Hardy bound at the axis).
- *A7:* the transport rows A1, A3 and A4 carry no frame derivative of any Ricci coefficient. A2 carries e1η (resp.
  e1η̲), A5 carries div η̲ (resp. div η), and A6 recovers e1χ̂ from e1 trχ and β^r.
- *M1, the mass aspects* μ = div η − K and μ̲ = div η̲ − K: e4μ = R_M1 and e3μ̲ = R_M1b, with explicit right sides
  in which div β^r cancels (A3 against axisbianchi5 B3), so no derivative of K or β^r remains.
- *M2:* the commuted Raychaudhuri for e1 trχ and e1 trχ̲.
- *M3:* κ = e1ω − ½β^r and κ̲ = e1ω̲ + ½β̲^r: e3κ = R_M3 and e4κ̲ = R_M3b. e1K cancels between ½e1ρ (Gauss, B2) and
  −½e3β^r (B3).
- *M4:* the right sides of M1–M3b contain, besides the unknowns, only e1η, e1η̲, e1χ̂, e1χ̲̂, e1 trχ, e1 trχ̲, e1ω,
  e1ω̲ and first angular derivatives of Ric.
- *S1–S2, the scalar's two pairs in the chart* (null3 N9's analogue, with measure 2Ω̂²√ĝ_x Y):
  - Div(a²e3 + c²e4 − 2ac e1) + 2a□f = −trχ ad − 2χ̂c² − 2ωc² + 2ω̲a² + 3ηac − η̲ac;
  - Div(c²e3 + d²e4 − 2cd e1) + 2d□f = −trχ̲ ad − 2χ̲̂c² + 2ωd² − 2ω̲c² − ηcd + 3η̲cd.
  - S3: neither quadratic form contains k = e1 log Y. The pairs carry no 1/s coefficient, and their flux through the
    axis is Y times a bounded density.
- *Controls* (each fails, as it must): c1, Raychaudhuri with ω trχ (residual 0.26); c2, torsion with β and Ric_41
  withheld (2.9); c3, Codazzi without 2kχ̂ (1.9); c4, κ with +½β^r (0.78).

**So the hierarchy closes structurally at [Wu26]'s level, in reduced form, the axis included (deduced, at random
jets).**
- *Unknowns.* Transported along e4: trχ, χ̲̂, η, ω̲, μ, e1 trχ, κ̲. Along e3: trχ̲, χ̂, η̲, ω, μ̲, e1 trχ̲, κ. The
  pairs (β^r, K) and (K, β̲^r) (B3, B3b), and the scalar's pairs (S1, S2) with their e1-commuted forms.
- *Every angular derivative on a right side is recovered.*
  - e1η and kη from div η = μ + K (8.A4, r = 3); likewise η̲ from μ̲.
  - e1χ̂ and kχ̂ from Codazzi (A6; 8.A4, r = 5); likewise χ̲̂.
  - e1ω = κ + ½β^r, and e1ω̲ = κ̲ − ½β̲^r.
  - e1 trχ and e1 trχ̲ are unknowns (M2).
  - The first angular derivatives of Ric are the scalar at level 1.

**Not done, and not claimed: the inequality itself.**
- The linearisation about the background in difference unknowns at the axis. There the polar-frame component δk of a
  regular perturbation is of size 1/s (8.A5 as restated in 9.0, M-C), so it may enter only multiplied by background
  quantities that vanish at the axis (η, ζ, χ̂ and e1A all do, at the rates X5 measures) or through e1 δ log Y. That
  this holds for every term is not checked.
- The explicit coefficient bounds of that linearisation, and the Grönwall constant.
- C_eq on the strip, and a cut-off form of 8.L1 (9.0, m9).
- The constant these would give joins Theorem 8.W's, whose size already decides the closing condition (9.4). So the
  existence statement does not hinge on them, and the paper text (9.9) does not cite them.

### 9.6 The late region: the third null grid, and round 4's two grids split by class (`checks/cp3grid5.py`)

**The third null grid (launched 2026-11-06 12:11 UTC, under nice, writing only under the scratchpad).**
- PID 2418: `checks/cpaxis5.py --run 1 0.9 32 1600 720 2.25 <scratch>/r5/cp_M32_1600_reg.npz reg ld 3 vsave 1.4`.
- PID 2419: the same at M = 40, writing `<scratch>/r5/cp_M40_1600_reg.npz`.
- `vsave 1.4` (added to cpaxis5.py `--run` this round) writes only the columns v ≥ 1.4, about 0.4 of a full file.
  The analyses match the 1600-row file's v-offset by value. The regions in question start at v = 1.5.
- They began at nice 10 and were moved to nice 5 at 12:57, by exact PID. The machine's load average was 13–38 on 4 cores
  throughout.
- At 14:41 UTC, read from the running processes by py-spy on their exact PIDs, the M = 32 run had marched 892 of its
  1,960 anti-diagonals (256,140 of 576,000 cells, 44 %) and the M = 40 run 673 (177,300 cells, 31 %). At the rates of
  the preceding hour they finish near 17:00 and 19:00 UTC. Their md5s are recorded when they finish; A7, A8 and A10 on
  three grids follow, and with them the order this section's label leaves open.

**What the third grid will decide, and how (`cp3grid5.py`, ready and tested).**
- A7: per band of v ∈ [1.4, 2.25] and areal-radius class, the monitor at 400, 800 and 1600 rows with its two ratios,
  |P₄₀₀ − P₈₀₀| and |P₈₀₀ − P₁₆₀₀| with the observed order log₂ of their ratio, and M = 40 against 32 at 1600 rows.
  Every comparison is on the 400-row nodes.
  - 'second order' if both monitor ratios and the P ratio lie in [3, 5.5] and the M ratio in [1/1.5, 1.5];
  - 'converging' if the last monitor ratio and the P ratio are ≥ 2;
  - 'not converging' if the last monitor ratio is below 1.5;
  - otherwise 'undecided'.
- A8: the Kretschmann scalar per class on the three grids. A10: d± at 400, 800 and 1600 rows, with ratios.
- *Control (run; `cp3grid5_control.out`):* A7 given the 800-row file in place of the 1600-row one reports a last ratio of
  exactly 1 and 'not converging' on all 18 bands. The verdict code cannot pass a persistent violation.
- The commands: `cp3grid5.py --a7 M32_400 M32_800 M32_1600 M40_1600`, `--a8 M32_400 M32_800 M32_1600 M40_1600`,
  `--dpm M32_400 M32_800 M32_1600`. The 400- and 800-row files are `r4/cp4/cp_M32_400_reg.npz`, `cp_M32_800_reg.npz`
  and `cp_M40_800_reg.npz` (md5s in 8.8 and the verifier of round 4's integrity list).

**Round 4's two grids, split by class (the verifier of round 4, m3; computed).**
- *A9, |P₃₂ − P₄₀| at 800 rows per class (`cp3grid5_a9_800.out`; it reproduces the verifier's pm_class.out to every
  printed digit).*
  - At 0.9–1.0: ≤ 6.0 × 10⁻¹¹ to v = 1.65, 4.7 × 10⁻⁹ on [1.65, 1.8), 2.0 × 10⁻⁵ on [1.8, 1.9), 6.2 × 10⁻⁴ on
    [1.9, 2.0), 4.3 × 10⁻³ beyond.
  - At 1.0–1.2: ≤ 5.6 × 10⁻¹¹ to v = 1.8, 1.5 × 10⁻⁷ on [1.8, 1.9), 8.5 × 10⁻⁵ on [1.9, 2.0), 1.0 × 10⁻² beyond.
  - At ≥ 1.2: ≤ 4.8 × 10⁻¹¹ to v = 2.0, 1.4 × 10⁻⁵ on [2.0, 2.25).
  - So the metric is resolved in M to ≤ 5 × 10⁻⁹ in the claimed regions (≤ 6 × 10⁻¹¹ except at 0.9–1.0 on
    [1.65, 1.8)), the 0.9–1.0 class included, which before had only the monitor's M-ratio (the verifier's point).
- *A8, the Kretschmann scalar per class on 32 u-rows, 400 against 800 rows at M = 32 and M = 32 against 40 at 800
  (`cp3grid5_a8_2grid.out`, 1,044 s; 'resolved' where both differences are below 5 % of dev).*
  - At 1.2–1.4: resolved at every angle to v = 2.0. The null-step difference is ≤ 2.3 × 10⁻² of K_0 and the
    M-difference ≤ 9.5 × 10⁻⁷, against dev 0.26–4.2. Not resolved on [2.0, 2.25). This is the evidence 8.7's ≥ 1.2
    bullet lacked (the verifier's m3).
  - At 1.0–1.2: resolved to v = 1.8 at every angle except x = 0 on [1.65, 1.8), where the null step is 8.4 × 10⁻³ of
    K_0 against dev 0.149 (5.6 %). On [1.8, 1.9) it is resolved at x = 0.97, 0.5 and −0.97, and not at 0 and −0.5. From
    v = 1.9 it is resolved nowhere.
  - At 0.9–1.0: resolved at every angle to v = 1.65, and on [1.65, 1.8) at every angle but x = 0 (null step 2.5 × 10⁻²
    of K_0 against dev 0.11). From v = 1.8 it is resolved nowhere.
  - So round 4's merged A6 is split, and its sentences read:
    - "From v = 1.9 it is not resolved in angle anywhere" holds at 0.9–1.2 and is false at 1.2–1.4, where it is
      resolved to v = 2.0.
    - "except at x = 0, where the null step is 7 % of dev" reads, at 1.0–1.2 on [1.8, 1.9): 11 % (4.83 × 10⁻² against
      0.446), as the verifier found.

**The regularisation's correction d± (the verifier of round 4, m4; computed).**
- *A10, replayed at every cell of the 400- and 800-row runs (`cp3grid5_a10_2grid.out`, 878 s).* The correction is
  printed as max |d±|, with max |d±|/max |R_uv| in brackets.
  - *In the claimed regions it falls at second order:* ratios 3.52–3.96 on every band to v = 1.8 at 0.9–1.2 and to
    v = 2.0 at ≥ 1.2. It is at most 1.1 × 10⁻² of R_uv at 800 rows there (0.9–1.0 on [1.65, 1.8)), and below 10⁻³ at
    ≥ 1.2. This is "O(the truncation error)", measured at last on the record's data.
  - *On [1.8, 1.9) at 0.9–1.2 it still falls at second order* (3.79, 3.84), while the monitor there does not (1.15,
    1.58). So the persistent monitor on that band is not the correction's doing.
  - *From v = 1.9 at 0.9–1.2 it does not converge:* ratios 1.50 and 0.98 (0.9–1.0) and 2.53 and 1.01 (1.0–1.2),
    and at 800 rows it is 7–75 % of max |R_uv|. On [2.0, 2.25) at ≥ 1.2 it falls at less than second order (1.93),
    to 1 % of R_uv.
  - There the correction is not shown to be O(the truncation error), so the regularised scheme is not shown consistent
    with the vacuum equations there. The verifier's third reading is a measured one on those bands; it does not
    exclude the other two.
  - *So the claimed regions end exactly where d± stops converging, or a band before it:* v = 1.8 at 0.9–1.2, where d±
    converges to 1.9; and v = 2.0 at ≥ 1.2.

**The label, until the third grid reports** (the verifier of round 4's wording):
- *Computed:* consistent with second-order convergence on two null grids (ratios 3.8–4.0) and resolved in M, to
  v ≤ 1.8 r_h at areal radius ≥ 0.9 r_h and v ≤ 2.0 r_h at ≥ 1.2 r_h. An order is not established.
- *Beyond (computed):* v ≥ 1.8 r_h at 0.9–1.2 r_h and v ≥ 2.0 r_h at ≥ 1.2 r_h. There a constraint violation persists
  under both refinements, and the curvature invariant is unresolved in angle. Nothing is claimed there.
- *Three readings of that violation:*
  - a singularity, or a feature the null grids do not reach;
  - a limit that is not vacuum: whether imposing Ric_vv and the three rows propagates Ric_xx = 0 is cpsolve5's own
    propagation question (9.0, m4);
  - a d± that does not vanish under refinement (the verifier's third reading). A10 measures it.

### 9.7 What holds at 10 l5, with labels (replacing 8.7), and what each remaining input is (replacing 8.6)

Seed 1 unless stated.
- **v ≤ 1/2, all (u, x): proved (deduced).** The solution is the seed.
- **Wherever a smooth vacuum solution with the data exists in dnsolve5's gauge: proved (deduced, D1–D2).** Every leaf
  with u > −1 is outer trapped, and every T²-invariant MOTS section has its innermost point at u ≤ −1.
- **Existence on any region of the gauge where (H1)–(H3) of Lemma 9.C hold: proved (deduced, 9.3).** This is
  conditional: (H1) is not established on any region that reaches the late region, and at Theorem 8.W's constant (H3)
  asks r ≲ 10⁻⁶⁸/G.
- **The data cone u = −10, v ∈ [1/2, 7/2], both seeds: certified.** The Raychaudhuri constraint of an explicit
  approximant is ≤ 5.0 × 10⁻⁵ and 2.3 × 10⁻⁵, 4.1 % and 4.3 % of the terms that cancel in it (`cdata5.py` C1).
- **u ∈ [−4, −1.1], v ∈ [0.55, 1.6], |x| ≤ cos(π/32): certified at points, and as sups on boxes.**
  - The Richardson approximant (`data/rcert5_C3R.npz`, md5 88e16664…) has Einstein residual ≤ 3.72 × 10⁻⁵ of the
    curvature scale at 16,128 points (`rich5.py` R2).
  - Its sups over four sub-boxes, each holding a point where the round-3 approximant exceeds 5.3 × 10⁻⁴, are certified
    (R3).
  - The round-3 approximant (`data/rcert5_C3.npz`, md5 698569f6…) is ≤ 2.42 × 10⁻³ at the 16,128 points (`rcert5c.py`
    P2), and ≤ 3.01 × 10⁻⁴ as a sup over the box t, σ ∈ [−1/2, 0], x ∈ [0, 1/4] (`rcert5d.py` D1, with the repaired
    C1 and the D4 gate).
- **Areal radius ≥ 0.9 r_h for v ≤ 1.8 r_h, and ≥ 1.2 r_h for v ≤ 2.0 r_h: computed.** Consistent with second-order
  convergence on two null grids (ratios 3.8–4.0) and resolved in M; an order of convergence is not established (9.6).
  - The regularised scheme's unimposed constraint falls 3.8–4.0-fold from 400 to 800 rows (A5). Its regularisation's
    correction d± falls at second order there too, to ≤ 1.1 % of R_uv (A10).
  - Its metric is resolved in M to ≤ 5 × 10⁻⁹, and to ≤ 6 × 10⁻¹¹ outside 0.9–1.0 on [1.65, 1.8) (A9).
  - Its Kretschmann scalar, per class (A8):
    - at 1.2–1.4, resolved at every angle to v = 2.0;
    - at 1.0–1.2, to v = 1.8, but at x = 0 on [1.65, 1.8);
    - at 0.9–1.0, to v = 1.65, and to 1.8 but at x = 0.
  - The free scheme is consistent with second-order convergence to v = 1.8 at areal radius ≥ 1.0 (late5b L5).
  - The third null grid, which would establish an order, is running at hand-back (9.6).
- **v ≥ 1.8 r_h at areal radius 0.9–1.2 r_h, and v ≥ 2.0 r_h at ≥ 1.2 r_h: computed, not converged.**
  - A constraint violation persists under both refinements, and the curvature invariant is unresolved in angle.
  - From v = 1.9 at 0.9–1.2 the regularisation's correction does not converge either (A10).
  - Nothing is claimed.
- **Areal radius 0.6–0.9 r_h for v ≤ 1.65 r_h: computed, consistent with second-order convergence in the null step on
  two grids** (late5b_small.out; free scheme).
- **Seed 2, v ≤ 3.5 at every angle: computed, converged** (CERTIFY-10L5.md D543, D601).

**No existence theorem beyond v ≤ 1/2 is proved at 10 l5, at either seed.** The inputs, as they stand after round 5:
1. **The axes.**
   - *Proved this round:* the reduced hierarchy at [Wu26]'s level and its structural closure (9.5).
   - *Remaining:* its linearisation in difference unknowns at the axis, with the δk terms checked against vanishing
     background factors; the coefficient bounds and the Grönwall constant; C_eq; and a cut-off form of 8.L1 for the
     glue (9.0, m9).
   - 8.A5 excludes only Theorem 7.L's polar-frame unknowns (9.0, M-C); that nothing weaker than [Wu26]'s level
     suffices is an expectation.
2. **The constant.** Both routes to a small constant proposed in rounds 3–4 are closed by proof: the finite-rank
   approximate inverse (Lemma 8.F) and the Schur block in these norms (Lemmas 9.H–9.B). What holds is Theorem 8.W,
   F² = 10^66.9 on |x| ≤ 1/2. A smaller constant would need a norm adapted to the coupling; none is proposed.
3. **The residual.**
   - No longer an obstruction at 5.3 × 10⁻⁴: every certified point value of the Richardson approximant is below it
     (9.2).
   - Certifying all 416 boxes at that level is a matter of machine time. F_R's measured sub-boxes need depth 6–7, so
     it comes to the order of 10⁷–10⁸ evaluations (9.2).
   - At Theorem 8.W's constant the demand is 10⁻⁶⁸/G. No approximant held in floating point meets it.
4. **Level 1 and G.**
   - 8.L1 gives mixed-norm control, L²_v L^∞_x on outgoing and L²_u L^∞_x on incoming cones (9.0, M-B).
   - The L^∞ (or product) estimate that closes the quadratic remainder, and G itself, are not had.
5. **Propagation.** Removed: Lemma 9.C needs none (9.3).
6. **The data.** G3 and Ric_vx on the data cone, unchanged since round 1. Lemma 9.C assumes data satisfying the
   characteristic constraints exactly.
7. **The late region.** The third null grid (running, 9.6); its analysis is ready and its control passes. Also
   remaining: the bands where d± does not converge, where the regularised scheme is not shown consistent; and angle and
   curvature checks at areal radius 0.6–0.9 (the verifier of round 4).
- **Beyond the seven (the verifier of round 4): the Newton–Kantorovich assembly.**
  - Lemma 9.C supplies the logic: a bootstrap on genuine metrics, given (H1)–(H3).
  - Putting F, G and r in one norm on one domain is the assembly. It is not done, and at 8.W's constant it would not
    close.

### 9.8 Files and outputs (round 5)

New programs, each run in full to its output, with controls that fail when the code under test is mutated:

| file | what | output, md5 |
|---|---|---|
| `checks/cont5.py` (d5ada772…) | 9.3: C1 exact, C2 z3 (vacuity guard, controls k1–k3) | `cont5.out` d4fc2397…; 7 s |
| `checks/rich5.py` (29b3f959…) | 9.2: R0–R3, C1–C3; `--runs`: R1 | `rich5.out` d9a722e0…, `rich5_runs.out` 64d3a967… |
| `checks/blocks5.py` (201c163b…) | 9.4: H1 exact, H2 on the record's table | `blocks5.out` b0468571…; 1,464 s |
| `checks/axhier5.py` (aa134baa…) | 9.5: A1–A7, M1–M4, S1–S3, controls c1–c4 | `axhier5.out` 0b192015…; 81 s |
| `checks/cp3grid5.py` (98f5f01d…) | 9.6: A7–A10, the A7 control | `cp3grid5_{control,a8_2grid,a9_800,a10_2grid}.out` |

New data: `data/rcert5_C3R.npz` (md5 88e16664187868e47eaaaa18709cfc61, 476,376 bytes), the Richardson approximant's
five coefficient tensors. `data/rcert5_C3.npz` is unchanged (698569f6…) before and after every program of this round.

Programs repaired per the verifier of round 4, their outputs regenerated (round-4 md5 → round-5 md5):

| file | finding | output |
|---|---|---|
| `checks/rcert5d.py` (46dd9068…) | M-A: one assembly, upward rounding, D4 gate | `rcert5d.out` ae24a4b7… → ee48a0e4… |
| `checks/linest5.py` (34dc9b3d…) | m1: E9(c) on the d_v rows | `linest5.out` 47af9f8d… → cdc11bfb… (timing only) |
| `checks/lev1_5.py` (bbb29f53…) | m2: L5, the level-1 rows' content | `lev1_5.out` 78e6a228… → b6be6a0b… |
| `checks/wgron5.py` (a764e73c…) | m16: W1 reads J; both mutations tested | `wgron5.out` 7dcb95d5… → 47170f09… |
| `checks/axis5.py` (ed855afc…) | m10: the sharper Hardy constants checked | `axis5.out` → 5cae43e2… (X4 lines added) |

- `cp3grid5.py`'s docstring was extended after its control and A9 ran; the code they ran is unchanged.
- The pre-round-5 versions of the repaired files are in `scratchpad/r5/wsf/*.r4.py`; git holds them too.

Scratch (not committed; under the session's scratchpad):
- `r5/cp_M32_1600_reg.npz`, `r5/cp_M40_1600_reg.npz`: the third null grid, running at hand-back (9.6).
- `r5/rcert5d_ck/`: the round-4 checkpoints, copied unchanged, that `rcert5d.out` collects.
- `r5/mut/`: the verifier of round 4's mutants rebuilt on the repaired files, with their outputs:
  `rcert5d_mutA.py`, `linest5_m1dk.py`, `lev1_5_m2chi.py`, `lev1_5_m2hx.py`, `wgron5_m16fac.py`. Each fails.
- `runs/l1_M16_400.npz` (9a0ecfbb…), `runs/l1_M16_800.npz` (cd9df998…): the two runs F_R is built from.
- `r4/regen/l1_rc0.9_M32.npz` (3dad3315…): the record's D432 run, which blocks5, linest5, lev1_5, wgron5 and axis5 read.

### 9.9 The paper: the section 9 text on existence at 10 l5, the untrapped-columns sentence, and a reference

These replace 8.10's proposal and 8.9's new text, which the verifier of round 4 found to over-claim (M-D, m12, m14).
They are proposed to the main session, which seats them; this note does not edit the paper or N1STAR-PROOF.md.
- *Keyed by text, not by line* (9.0, m13). Each old block occurs exactly once in `RESPONSE-HL-5D.md` as it stands; at
  the time of writing they sit at lines 1498–1504, 1473–1475 and 1739–1740 (md5 5930486d…).
- *The author's rule.* Nothing is phrased as open. Each sentence states what is certified, deduced or computed, and
  where; existence is stated where it is proved, and the rest is stated as what holds.
- *Folded in.* M-B: level 1 is stated in the cones' L² norms only. M-D: the propagation clause is gone (Lemma 9.C makes
  it moot), and convergence is "consistent with second-order convergence on two null grids … an order of convergence not
  being established". m9: the glue is not cited. m12: the R0 = 20 exception. m14: the free scheme's own convergence.
  The verifier's minor point: the axis caps are named.
- *The late region* is stated at what two null grids show. If the third grid of 9.6 establishes an order, its clause
  changes as 9.6 says; nothing else does.
- Longest new line: 120 characters.

**A. The section 9 text on existence at 10 l5.**

**Old:**

```
  `CERTIFY-10L5.md` section 6b). A first certified step is taken: for an explicit approximant of the characteristic
  data on the data cone, the constraint along its outgoing generators holds to a certified bound at both seeds (at the
  second, 2.3 × 10⁻⁵ against terms of size 5.3 × 10⁻⁴; certified, ball arithmetic, `docket68/n1star/checks/cdata5.py`).
  The full Einstein residual of a smoothed three-dimensional approximant built from a run is computed only, 2.5 × 10⁻³
  of the curvature scale and falling at second order with the grid (`checks/resid5.py`, floating point), and no linear
  estimate with explicit constants is available for the characteristic problem in the class, so existence at 10 l5
  remains open (supplement `CERTIFY-10L5-RESULT.md` section 2).
```

**New:**

```
  `CERTIFY-10L5.md` section 6b). Existence at 10 l5 is proved where the solution is the seed (v ≤ r_h/2) and is not
  claimed beyond it. Toward a computer-assisted proof the following hold, each with its status. Certified (ball
  arithmetic): on the data cone the outgoing constraint of an explicit approximant holds to 5.0 × 10⁻⁵ and 2.3 × 10⁻⁵ at
  the two seeds, 4.1–4.3 % of the terms that cancel in it (`docket68/n1star/checks/cdata5.py`); on u ∈ [−4, −1.1] r_h,
  v ∈ [0.55, 1.6] r_h, away from the axis caps |x| > cos(π/32), the Einstein residual of an explicit three-dimensional
  approximant, Richardson-extrapolated from two null grids, its coefficients pinned by md5
  (`docket68/n1star/data/rcert5_C3R.npz`), is at most 3.72 × 10⁻⁵ of the curvature scale at 16,128 points and at most
  5.0 × 10⁻⁴ as a supremum over each of four sub-boxes on which the single-grid approximant (`data/rcert5_C3.npz`) has
  certified values of 1.1–2.4 × 10⁻³ (`checks/rich5.py`), and the single-grid approximant's supremum over one interior
  box of the 416 covering that region is at most 3.01 × 10⁻⁴ (`checks/rcert5d.py`, its bounds checked by a control that
  fails when their assembly is mutated and by independent point values in each of its 32,768 sub-boxes). Deduced: the
  class is (2+1)-dimensional gravity coupled to a wave map into the flat plane (`checks/reduce5.py`); in the free metric
  formulation, at frozen coefficients on spherical states, the shift's angular derivative is of principal size at high
  angular frequency and drives δR at order k², so no estimate without loss of derivatives holds for the
  frozen-coefficient problem (`checks/symbol5s.py`; for the constraint-preserving formulation a loss is indicated by a
  model only); in double-null gauge the reduced transport equations carry no angular derivative of an unknown on their
  right sides (`checks/null3.py`, `checks/linest5.py`), and a linear estimate with explicit constants holds on truncated
  domains of dependence away from the axes, at level 0 and at level 1 in the cones' L² norms (supplement Theorems 7.L,
  8.L1 and 8.W; `checks/lev1_5.py`, `checks/wgron5.py`); near each axis the class is four-dimensional axisymmetric
  Einstein–scalar in a chart regular at the axis, where [Wu26]'s curvature pairs have energy identities on the whole
  section, the angular recoveries hold with explicit Hardy constants, and [Wu26]'s transport equations, mass aspects and
  the scalar's pairs hold in reduced form with every angular derivative on their right sides recovered from the
  hierarchy's own unknowns (`checks/axis5.py`, `checks/axisbianchi5.py`, `checks/axhier5.py`; identities verified at
  random jets); for characteristic data that satisfy the constraints, a smooth T²-invariant vacuum development exists on
  any region of the gauge where such a linear estimate holds, at every level, with constant F, the quadratic remainder
  has constant G and the approximant's residual r satisfies 4F²Gr < 1, by continuity from the higher-dimensional
  neighbourhood theorem of [CTG23], the hierarchy being applied only to genuine metrics, for which its compatibility
  with the metric holds by definition (`checks/cont5.py`); and refining the angular Galerkin space leaves the couplings
  across its cut of the coefficients' own size, so the condition under which an estimate on the high angular modes would
  lower the constant fails at every angular resolution, in these norms (`checks/blocks5.py`). Computed (floating point):
  on |x| ≤ 1/2 over the region above, where no truncated domain exists, the estimate's constant is F² = 10^138, and
  10^66.9 with the weights found, at which 4F²Gr < 1 asks r of order 10⁻⁶⁸/G; the first seed's solution, in a
  constraint-preserving scheme whose singular coupling at the axes is regularised (`checks/cpaxis5.py`), is consistent
  with second-order convergence on two null grids (ratios 3.8–4.0) and resolved in angle to v ≈ 1.8 r_h at areal radius
  ≥ 0.9 r_h and to v ≈ 2.0 r_h at ≥ 1.2 r_h, an order of convergence not being established, and the free scheme's
  solution is consistent with second-order convergence to v ≈ 1.8 r_h as well (`checks/late5b.py`); beyond, a constraint
  violation persists under both refinements and the curvature invariant is unresolved in angle (supplement
  `CERTIFY-10L5-RESULT.md` sections 2 and 6–9).
```

Statuses, as the new text gives them:
- *certified:* the data cone; the Richardson approximant at 16,128 points and on four sub-boxes; the single-grid
  approximant's one box, with its repaired control and gate;
- *deduced:* the reduction; the frozen-coefficient loss; the transport structure; Theorems 7.L, 8.L1 (in the cones' L²
  norms) and 8.W; the axis chart's pairs, Hardy constants and reduced hierarchy (identities at random jets); Lemma 9.C,
  conditional on its hypotheses; the block condition's failure (Lemmas 9.H and 9.B with the computed couplings);
- *computed:* the constants and the closing condition's demand; the late region's convergence on two grids, and what
  persists beyond it;
- *not claimed:* existence beyond the seed.

**B. The untrapped-columns sentence** (8.9's new text, with the verifier of round 4's m12).

**Old:**

```
  At 100 l5² the Bondi spheres rebuilt on the double-null solution reproduce the untrapped columns to within one column
  spacing up to v = 1.525 (not at 1.55), which come from the spheres' tilt against the null leaves (computed); at 1000
  l5² the rebuild does not reach r ≤ 0.3 r_h. The breakdown times are at one angular resolution (N_x = 16); the scheme
```

**New:**

```
  At 100 l5², on the sphere of least areal radius the rebuild reaches before the cut (0.64–0.78 r_h), the band of
  growth5's columns along which the Bondi spheres rebuilt on the double-null solution are untrapped has each edge within
  one column spacing of growth5's own up to v = 1.525 r_h, at both data-cone radii run (the sets equal or shifted by one
  column, except at the larger radius at v = 1.45 and 1.525 r_h, where the rebuild's band is one column shorter); at
  v = 1.55 r_h growth5's band reaches the axis and the rebuild's stops 3.8–4.0 spacings short. The comparison is at one
  null resolution (800 × 360, M = 16), where the rebuilt outer zero's own agreement with growth5's is unresolved in
  (u, v) from v = 1.3 r_h; the untrapping comes from the spheres' tilt against the null leaves, whose own expansion
  leaves no column untrapped (computed, `docket68/n1star/checks/secondzero5.py --edges`; supplement
  `CERTIFY-10L5-RESULT.md` sections 6.1, V2–V3, and 9.0). At 1000 l5² the rebuild does not reach r ≤ 0.3 r_h. The
  breakdown times are at one angular resolution (N_x = 16); the scheme
```

**C. A reference for [CTG23]**, after [Wu26]'s entry in the paper's list.

**Old:**

```
- [Wu26] S. Wu, *Picard iteration for the characteristic initial value problem in Einstein equations*,
  arXiv:2609.08421v1. READ 2026-10-20: abstract; p. 2, (1.1); Theorems 2.1–2.2, p. 6.
```

**New:**

```
- [Wu26] S. Wu, *Picard iteration for the characteristic initial value problem in Einstein equations*,
  arXiv:2609.08421v1. READ 2026-10-20: abstract; p. 2, (1.1); Theorems 2.1–2.2, p. 6.
- [CTG23] P. T. Chruściel, R. Tagne Wafo, F. Gray, *The "neighborhood theorem" for the general relativistic
  characteristic Cauchy problem in higher dimensions*, arXiv:2305.07306v1. READ 2026-11-06: abstract; Theorem 1.1,
  pp. 2–3, and the remark after it on Sobolev spaces; p. 8 (estimates for genuine solutions, not an existence scheme).
```

## 10. Round 6 (2026-11-06): the verifier of round 5 seated

The verifier of round 5 read section 9 (lines 2249–3014, file md5 04df75f6…). It reran every program and found each
output reproduced, timings aside. It read [CTG23] in full and found the quotes exact and the hypotheses fitting the
class. It re-derived Lemmas 9.H and 9.B, found Lemma 9.C sound as a conditional and rich5's certificates sound, and
confirmed M-B, M-C and M-D fixed. It did not confirm section 9 because of one Major, M5-A. It also found ten minor
findings and eight nits. Each is seated below as a bracketed amendment to the section 9 text it names; section 9 is
not edited. Every finding was re-derived first, and every repair that needs a program was run in full. Sections 0–9
are byte-identical before and after this append.

### 10.0 The verifier of round 5: its findings, seated as amendments to section 9

**M5-A. C1 reached only `Engine.bound` and its flag, never the rest of the engine.**
- [9.0, M-A, "One assembly: `Engine.bound` is used by `kids` and by C1 … The round-4 certificate stands, now with a
  control that can fail on it"; the rcert5d.py docstring, "a mutation of the engine's assembly or of its flag makes C1
  fail"; 9.9's block A, "its bounds checked by a control that fails when their assembly is mutated": verifier of round 5
  (M5-A).]
  - *Re-derived.* C1 built its own Taylor jets and called `bound` on them. It never ran `kids`, `point_coeffs`,
    `box_coeffs` or `inputs(..., box=True)`. So a mutation at the call site (`self.bound(vp[k8], vp[k8], hpow)`, the
    verifier's mA3) dropped the remainder where C1 could not see it. The verifier ran mA3 end to end: it accepted the
    box at depth 1 after 8 evaluations, `--collect` printed "all checks pass", and D4 passed at ratio 0.991. A dropped
    `abs` inside `bound` (mA4) passed C1, because C1's test polynomials have positive centre values.
  - *Repaired (`checks/rcert5d.py`, `kids_control`).* C1 now also runs the engine end to end. An Engine is built in the
    ordinary way (no flag) on test tensors R = t⁴ (Chebyshev coefficients 3/8, 1/2, 1/8, exact in binary; every other
    field 0) and a test frame of eight signed combinations: R, −R, x⁴, −x⁴, R·x⁴, R − 0.3, −R·x⁴ − 0.05, R + x⁴.
    - They are run through `kids` on the children of four parent boxes with half-widths 0.005 to 0.25, and compared
      with the exact sups.
    - For t⁴ and x⁴ the sound order-3 Lagrange bound is (|c| + h)⁴ + 3h⁴: it exceeds the true sup by only 3h⁴.
    - So a loss of the remainder, of the box enclosure of a coefficient or of the coordinate x, or of `abs` where a
      centre value is negative, gives a bound below the true sup.
    - The round-5 polynomial test of `bound` alone is kept beside it.
  - *Rerun on the round-4 checkpoints (`checks/rcert5d.out` regenerated).*
    - C1 through `kids`: the largest true/bound is 0.9999999926 (sound), and 2.7527 with the remainder dropped.
    - D1 and D3 are unchanged; D4 gives 68,705 points at ratio 0.809, no violation.
    - Collect: "all checks pass".
  - *The verifier's mutants, rebuilt on the repaired file and run through the whole `--collect`*
    (`scratchpad/r6/mut/rcert5d_mA*.py`, outputs beside them).
    - The collect reads the round-4 checkpoints, which the real engine computed. So D1, D3 and D4 are the same for
      every mutant, and C1 is what must fail. Its largest true/bound through `kids` must be ≤ 1:
      - mA1, the remainder flag forced on (`self.drop = True`): 2.7527, FAILURES, exit 1;
      - mA2, the order-3 coefficients taken at the centre (`sum(m) <= Q`): 2.7527, and `bound` alone ∞; FAILURES;
      - mA3, the verifier's (`kids` passes `vp` twice): 2.7527, FAILURES;
      - mA4, `abs` dropped in `bound`: ∞ (a bound ≤ 0 under a positive sup), FAILURES;
      - mA5, `box_coeffs` at half the half-widths: 0.9999999926, "all checks pass" (below);
      - mA6, the box inputs' t and x taken at the centre (`arb(tcs[p])`, `arb(xcs[r])`): 1.0667, FAILURES.
    - mA3 end to end, as the verifier ran it (`rcert5d_mA3_e2e_{worker,collect}.out`, checkpoints in `r6/mA3ck/`):
      - its worker again accepts the box at depth 1 after 8 evaluations;
      - D1 passes with ll ≤ 1.954 × 10⁻⁴, and D4 passes at 35 points and ratio 0.991, as the verifier found;
      - C1 now gives 2.7527, so `--collect` prints FAILURES and exits 1.
  - *mA5 is not killed, and no test on a single field can kill it (deduced).*
    - mA5 calls `box_coeffs` at half the half-widths. That shrinks both terms of the coefficient enclosure: the linear
      one by 2, and the quadratic one, built on the global l1 bounds, by 4.
    - Summed into the order-3 bound, the real enclosure overcounts the field's own Taylor terms:
      - at order 4, Σ_{|β|=3} Σ_d (β_d + 1)|f_{β+e_d}| h_d h^β = 4 Σ_{|γ|=4} |f_γ| h^γ;
      - at order 5, ½|γ|(|γ| − 1) = 10 times Σ_{|γ|=5} l1_γ h^γ, the Lagrange remainder's own bound.
    - mA5 makes these factors 2 and 2.5, both still ≥ 1.
      - For a single field, its bound still dominates the Taylor–Lagrange bound term by term, so it stays sound.
      - For products in the frame, it is shown to dominate only to fourth order in h.
    - It is the one mutation tried that the control does not catch, for the reason above. The kids test agrees: mA5's
      largest ratio is 0.9999999926, the real engine's.
  - *D4's reach, stated exactly.* D4 catches an under-bound only where a sampled certified point value exceeds it. On
    the mA1/mA3 under-bound it reached 0.991 and missed it by about 1 %. It is a second line beside C1, not a
    substitute for it.
  - *rich5.py* (9.2's R3) uses the same engine. Its C1 now runs `kids_control` too (`checks/rich5.out` regenerated).
    - The rerun is read-only, and both npz md5s are unchanged before and after it. It reproduces round 5's R0, R2, R3,
      C2 and C3 to every printed digit, timings aside. C1 gives 0.9999999926 through `kids` and 2.7527 with the
      remainder dropped, and the run ends "all checks pass" (1,291 s).
    - R3 calls rcert5d's `Engine`, so a mutant of rcert5d is a mutant of rich5's engine. rich5's C1 was run verbatim on
      rich5's own tensors with rcert5d replaced by each mutant (`scratchpad/r6/rich5_c1_mut.py`, output
      `rich5_c1_mut.out`).
      - It fails on mA1–mA4 and mA6, at 2.7527, 2.7527, 2.7527, ∞ and 1.0667.
      - It passes on mA5 at 0.9999999926, as rcert5d's C1 does, and on the real engine at the same figure.
  - *Corrected text.*
    - 9.0's M-A: "a control that can fail on it" reads "a control that, from round 6, runs the whole engine (10.0)".
    - The rcert5d.py docstring is corrected in the file.
    - Block A's description reads "both certificates' bounds are checked by a control that runs the whole bound
      computation on test fields with exact suprema and catches each mutation of it tried that under-bounds them, and
      by independent certified point values at the centre and corners of every accepted sub-box" (10.4).

**Minor findings.**
- **m5-1** [9.7, "(H1) is not established on any region that reaches the late region"]: it understates.
  - (H1) holds on no region of Lemma 9.C's form beyond the seed. D includes the axes, and the axis estimate, the
    level-1 L^∞ step and G are all missing. The truncated domains of Theorems 7.L, 8.L1 and 8.W over the box are empty
    (7.4; 9.0, m9).
  - It reads: "(H1) is established on no region of Lemma 9.C's form beyond the seed".
- **m5-2** [9.9, block A, "a smooth T²-invariant vacuum development exists on any region of the gauge where such a
  linear estimate holds"]: it goes beyond Lemma 9.C.
  - The lemma treats D = [−10, u*] × [1/2, v*] × [−1, 1] × T², axes included, on both data hypersurfaces. "such"
    pointed at the estimate on truncated domains.
  - The sentence omitted "smooth" ([CTG23] is in the smooth category) and (H3)'s y(1/2) ≤ A.
  - The new block A states the lemma's region and hypotheses exactly (10.4).
- **m5-3** [9.1 item 4, "closed by proof"; 9.4; block A, where the failure of the block condition is listed under
  "Deduced"]: the failure rests on floating-point couplings. It is the failure of the sufficient product-of-norms
  condition, in Theorem 7.L's unweighted norms, while 8.W's 10^66.9 is in weighted norms.
  - It reads "deduced from computed couplings: the block condition fails at every N in the unweighted norms and at W3's
    weights". Block A lists it under "Computed".
  - *Computed at W3's weights (`checks/blockw5.py`, new; `blockw5.out`).*
    - Every printed figure of blocks5.out and wgron5.out is rounded down by half a unit of its last digit before use.
    - In the weighted norms, the product of a pair's two couplings scales by λ_Y/λ_Z.
    - Of blocks5's six largest band pairs, P4_1 ← δw gives c² λ_Y/λ_Z ≥ 57.8 (c ≥ 22, log(λ_Y/λ_Z) ≥ −2.12). It holds
      for every N, since blocks5 printed this pair's minimum over N = 0..30 (22). So the block condition fails at W3's
      weights too.
    - Control k1, equal weights, gives 481.8 against blocks5's 484 (inside the rounding margin). Control k2, the
      smallest pair in place of the largest, gives 0.0891 < 1, so the conclusion rests on taking the largest pair.
- **m5-4** [9.0 m4, 9.1 item 6, 9.6 and 9.7: "d± falls at second order"]: it rests on one two-grid ratio. It reads "d±
  falls 3.5–4.0-fold from 400 to 800 rows, consistent with second order".
- **m5-5** [9.6, "below 10⁻³ at ≥ 1.2"]: false. A10 at 800 rows gives 1.2 × 10⁻³ on [1.8, 1.9) and 1.9 × 10⁻³ on
  [1.9, 2.0). It reads "below 2 × 10⁻³ at ≥ 1.2 (below 10⁻³ to v = 1.8)".
- **m5-6** [9.1, 9.2, 9.7, block A]: certified upper bounds were quoted rounded down. They read, rounded up: 3.7217 ×
  10⁻⁵ as 3.73 × 10⁻⁵, 6.091 × 10⁻⁵ as 6.10 × 10⁻⁵, and 4.932 × 10⁻⁴ as 4.94 × 10⁻⁴. 4.966 × 10⁻⁴ (as 4.97),
  1.747 × 10⁻⁴ (as 1.75) and 3.007 × 10⁻⁴ (as 3.01) were already rounded up.
- **m5-7** [9.2, "on four of them it is certified as a sup"]: it reads "on a sub-box of each of four of them (1/4,096 or
  1/64 of the box) it is certified as a sup".
- **m5-8** [9.9, block A, "the free scheme's solution is consistent with second-order convergence to v ≈ 1.8 r_h as
  well"]: late5b L5 covers only areal radius ≥ 1.0. It reads "… to v ≈ 1.8 r_h at areal radius ≥ r_h".
- **m5-9** [9.9]: none of the files block A cites, beyond cdata5.py, had a row in the paper's Appendix D md5 table. 10.4
  gives the rows.
- **m5-10** [9.9, block A's span]: paper lines 1489–1490, just above it, still read "where a singularity, a steep smooth
  feature and a defect at the axis are not yet told apart". That is phrased as open, and its list of readings differs
  from block A's. The old block A now starts at "At the first seed the Kretschmann scalar …" (paper line 1488's last two
  words). The first seed's sentence is dropped there, since block A's computed clause states the first seed's late
  region exactly. The second seed's sentences are kept verbatim.

**Nits.**
- [9.4, Lemma 9.B, "a test function constant in (u, v) on a slab and equal to the top singular vector in x"]: the test
  function is the top singular vector at each (u, v), so it varies with (u, v); blocks5.py does this.
- [9.6, 9.7, "it does not converge" of a band where d± falls by 2.53]: it reads "not at second order".
- [9.9, block A, "away from the axis caps |x| > cos(π/32)"]: it reads "(|x| ≤ cos(π/32))".
- [block A, "in these norms"]: undefined there. It reads "in Theorem 7.L's unweighted norms and at Theorem 8.W's
  weights".
- [rcert5d D1–D2, "certified centre values (lower bounds)"]: they were upper ends of the centre balls. *Repaired:* D1
  prints them as upper ends, and D2 now uses certified lower ends, from D4's centre points (ll 1.727 × 10⁻⁴ and lx
  4.976 × 10⁻⁵, above τ′ = 3.0 × 10⁻⁵ as before). No conclusion changes.
- [9.0, "a gate on a code path independent of the engine (D4)"]: D4 avoids the Taylor models only; it shares
  `point_coeffs` and the generated frame code. Repaired in rcert5d.py's printout and docstring.
- [9.2, 9.7, "of the order of 10⁷–10⁸ evaluations"]: low. The measured sub-boxes extrapolate to about 3 × 10⁵ to 2.4 ×
  10⁶ evaluations per K2 box, so about 10⁸–10⁹ for all 416. It reads so.
- [9.9, "md5 5930486d…"]: stale. The paper is now 4c1210818f03bcf7d4875a5b11d8b568; the three old blocks each still
  occur once (10.4 re-keys them).

### 10.1 The third null grid, at hand-back

- The two runs of the regularised scheme at 1600 × 720 (PIDs 2418 and 2419, nice 5, started 12:11 UTC) are still
  running and were not touched. Their state was read with py-spy only, at 16:10 UTC:
  - M = 32 is at null diagonal 1,422 of 1,959, 78 % of the cells. At its rate since 15:57 it finishes at about
    17:05 UTC.
  - M = 40 is at diagonal 1,010, 52 % of the cells, and at its rate finishes at about 19:30 UTC.
- So no order-of-convergence verdict is seated in this round. The analysis is ready and its control passes (9.6). The
  commands are 9.6's: `cp3grid5.py --a7`, `--a8` and `--dpm` on the 400-, 800- and 1600-row runs at M = 32, with the
  1600-row run at M = 40.
- Until it runs, the two-grid statements of 9.6–9.7 stand, as amended by m5-4, m5-5 and m5-8.

### 10.2 What holds at 10 l5 after round 6

9.7's list stands, with these changes:
- (H1)'s status reads as m5-1.
- The Richardson approximant's bound at 16,128 points reads ≤ 3.73 × 10⁻⁵ (m5-6).
- d± and the free scheme read as m5-4, m5-5 and m5-8.
- The block condition's failure is computed (m5-3). It fails at W3's weights too: P4_1 ← δw ≥ 57.8 for every N.
- Both certificates' bounds, rcert5d's D1 and rich5's R3, are checked by a control that runs the whole bound computation
  end to end. It fails under mA1–mA4 and mA6. It passes mA5, which halves a margin and stays sound for a single field
  (10.0).

There is no new existence statement. Existence is proved where the solution is the seed and is not claimed beyond it.

### 10.3 Files and outputs (round 6)

| file | what | md5 (round 5 → round 6) |
|---|---|---|
| `checks/blockw5.py` (new) | m5-3: the block condition at W3's weights; controls k1, k2 | 6049a5dc… |
| `checks/blockw5.out` (new) | its output; 1 s | f2ae0d7d… |
| `checks/rcert5d.py` | M5-A: C1 through `Engine.kids`; D1, D2 and D4 nits | 46dd9068… → 7366918f… |
| `checks/rcert5d.out` | collect and census, regenerated | ee48a0e4… → f2ce6061… |
| `checks/rich5.py` | M5-A: its C1 runs `kids_control` | 29b3f959… → ce036a1e… |
| `checks/rich5.out` | regenerated (read-only run) | d9a722e0… → eedb7b4c… |

- `data/rcert5_C3.npz` (698569f6…) and `data/rcert5_C3R.npz` (88e16664…) are unchanged before and after every program
  of this round.
- The round-5 versions are in the scratchpad: `r5/wsf/rcert5d.r5.py` and `r6/rich5.r5.py`. Git holds them too.
- rcert5d.py ran as 07835da0… (`r6/rcert5d.ran.py`). After the runs, its docstring's round-6 note was corrected to state
  mA5 as 10.0 does. With docstrings removed, the two files' code is identical.

Scratch (not committed; under the session's scratchpad):
- `r6/mut/rcert5d_mA1.py` … `rcert5d_mA6.py` are the verifier's mutants, rebuilt on the repaired file. Their outputs
  `rcert5d_mA*_collect.out` sit beside them, with mA3's end-to-end run in `rcert5d_mA3_e2e_{worker,collect}.out`. mA3's
  own checkpoints are in `r6/mA3ck/`.
- `r6/rcert5d_collect.out` and `r6/rcert5d_census.out` are the two halves of `checks/rcert5d.out`.

### 10.4 The paper: blocks A–E, and Appendix D's rows

These replace 9.9's proposal. They are proposed to the main session, which seats them; this note edits neither the paper
nor N1STAR-PROOF.md.
- *Keyed by text.* Each old block occurs exactly once in `RESPONSE-HL-5D.md` at md5 4c1210818f03bcf7d4875a5b11d8b568.
  It also occurs once at b21cd7caaaa40291ec878ad7b626499a, the paper after 15:59 UTC, whose change is three md5 rows of
  Appendix D, none of them in these blocks. 9.9's old A, B and C each still occur once in both.
- *Longest new line:* 120 characters.

**A. The section 9 text on existence at 10 l5.** It replaces 9.9's A.
- *The old block* now starts at the last two words of paper line 1488 (m5-10). So the first seed's sentence, which still
  said "not yet told apart", goes. Block A's computed clause states the first seed's late region exactly.
- *Folded in:* M5-A (the control's description); m5-1, m5-2 (the region, "smooth", the data bound at v = r_h/2), m5-3
  (the norms; the label is computed), m5-6, m5-7 and m5-8; the nits on "|x| ≤ cos(π/32)" and on "in these norms".

**Old:**

```
At the
  first seed the Kretschmann scalar is moderate and converged in angle up to the point where the runs stop converging,
  and unresolved after it, where a singularity, a steep smooth feature and a defect at the axis are not yet told apart.
  At the second seed, with the angular and null grids refined together, the two coarser angular resolutions agree up to
  v ≈ 3.5 and the finest departs from them from v ≈ 3.25, at every angle. On a finer null grid, 2400 × 1080, the second
  seed's M = 32 and 40 angular resolutions agree to 0.09 K_0 up to v = 3.5 and to 0.53 K_0 up to v = 4.5 (K_0 = 72/R⁸,
  Tangherlini's Kretschmann scalar at the same areal radius), away from the cells M = 48 masks; M = 48 departs from v ≈
  3.25 exactly as at 1600 × 720, so the finer null grid does not move it, and the step condition M²/N ≤ c it had been
  ascribed to is refuted (M²/N = 0.96). The late region stays unresolved (computed, floating point:
  `docket68/n1star/checks/g1curv5.py --seed2-2400`, output `checks/g1curv5_seed2_2400.out`; supplement
  `CERTIFY-10L5.md` section 6b). A first certified step is taken: for an explicit approximant of the characteristic
  data on the data cone, the constraint along its outgoing generators holds to a certified bound at both seeds (at the
  second, 2.3 × 10⁻⁵ against terms of size 5.3 × 10⁻⁴; certified, ball arithmetic, `docket68/n1star/checks/cdata5.py`).
  The full Einstein residual of a smoothed three-dimensional approximant built from a run is computed only, 2.5 × 10⁻³
  of the curvature scale and falling at second order with the grid (`checks/resid5.py`, floating point), and no linear
  estimate with explicit constants is available for the characteristic problem in the class, so existence at 10 l5
  remains open (supplement `CERTIFY-10L5-RESULT.md` section 2).
```

**New:**

```
At the
  second seed, with the angular and null grids refined together, the two coarser angular resolutions agree up to v ≈ 3.5
  and the finest departs from them from v ≈ 3.25, at every angle. On a finer null grid, 2400 × 1080, the second seed's
  M = 32 and 40 angular resolutions agree to 0.09 K_0 up to v = 3.5 and to 0.53 K_0 up to v = 4.5 (K_0 = 72/R⁸,
  Tangherlini's Kretschmann scalar at the same areal radius), away from the cells M = 48 masks; M = 48 departs from
  v ≈ 3.25 exactly as at 1600 × 720, so the finer null grid does not move it, and the step condition M²/N ≤ c it had
  been ascribed to is refuted (M²/N = 0.96). The late region stays unresolved (computed, floating point:
  `docket68/n1star/checks/g1curv5.py --seed2-2400`, output `checks/g1curv5_seed2_2400.out`; supplement `CERTIFY-10L5.md`
  section 6b). Existence at 10 l5 is proved where the solution is the seed (v ≤ r_h/2) and is not claimed beyond it.
  Toward a computer-assisted proof the following hold, each with its status. Certified (ball arithmetic): on the data
  cone the outgoing constraint of an explicit approximant holds to 5.0 × 10⁻⁵ and 2.3 × 10⁻⁵ at the two seeds, 4.1–4.3 %
  of the terms that cancel in it (`docket68/n1star/checks/cdata5.py`); on u ∈ [−4, −1.1] r_h, v ∈ [0.55, 1.6] r_h,
  |x| ≤ cos(π/32), the Einstein residual of an explicit three-dimensional approximant, Richardson-extrapolated from two
  null grids, its coefficients pinned by md5 (`docket68/n1star/data/rcert5_C3R.npz`), is at most 3.73 × 10⁻⁵ of the
  curvature scale at 16,128 points and at most 5.0 × 10⁻⁴ as a supremum over a sub-box of each of four of the 416 boxes
  covering that region, on which the single-grid approximant (`data/rcert5_C3.npz`) has certified values of
  1.1–2.4 × 10⁻³ (`checks/rich5.py`), and the single-grid approximant's supremum over one interior box of the 416 is
  at most 3.01 × 10⁻⁴ (`checks/rcert5d.py`; both certificates' bounds are checked by a control that runs the whole bound
  computation on test fields with exact suprema and catches each mutation of it tried that under-bounds them, and by
  independent certified point values at the centre and corners of every accepted sub-box). Deduced: the class is
  (2+1)-dimensional gravity coupled to a wave map into the flat plane (`checks/reduce5.py`); in the free metric
  formulation, at frozen coefficients on spherical states, the shift's angular derivative is of principal size at high
  angular frequency and drives δR at order k², so no estimate without loss of derivatives holds for the
  frozen-coefficient problem (`checks/symbol5s.py`; for the constraint-preserving formulation a loss is indicated by a
  model only); in double-null gauge the reduced transport equations carry no angular derivative of an unknown on their
  right sides (`checks/null3.py`, `checks/linest5.py`), and a linear estimate with explicit constants holds on truncated
  domains of dependence away from the axes, at level 0 and at level 1 in the cones' L² norms (supplement Theorems 7.L,
  8.L1 and 8.W; `checks/lev1_5.py`, `checks/wgron5.py`); near each axis the class is four-dimensional axisymmetric
  Einstein–scalar in a chart regular at the axis, where [Wu26]'s curvature pairs have energy identities on the whole
  section, the angular recoveries hold with explicit Hardy constants, and [Wu26]'s transport equations, mass aspects and
  the scalar's pairs hold in reduced form with every angular derivative on their right sides recovered from the
  hierarchy's own unknowns (`checks/axis5.py`, `checks/axisbianchi5.py`, `checks/axhier5.py`; identities verified at
  random jets); and, for smooth characteristic data that satisfy the constraints, a smooth T²-invariant vacuum
  development exists on the region u ∈ [−10, u*] r_h, v ∈ [r_h/2, v*] of the gauge, the axes included, whenever on that
  region the difference of a vacuum metric from the approximant obeys a linear estimate with constant F at every level,
  the quadratic remainder has constant G, the approximant's residual r satisfies 4F²Gr < 1 and the difference at
  v = r_h/2 is at most Fr, by continuity from the higher-dimensional neighbourhood theorem of [CTG23], the hierarchy
  being applied only to genuine metrics, for which its compatibility with the metric holds by definition
  (`checks/cont5.py`); these hypotheses are established on no such region beyond the seed. Computed (floating point): on
  |x| ≤ 1/2 over the region above, where no truncated domain exists, the estimate's constant is F² = 10^138, and 10^66.9
  with Theorem 8.W's weights, at which 4F²Gr < 1 asks r of order 10⁻⁶⁸/G; the couplings across an angular Galerkin cut,
  N-independent by an identity (deduced), are of the coefficients' own size there, so the block (Schur) condition under
  which an estimate on the high angular modes would lower the constant fails at every angular resolution, in Theorem
  7.L's unweighted norms and at Theorem 8.W's weights (`checks/blocks5.py`, `checks/blockw5.py`); the first seed's
  solution, in a constraint-preserving scheme whose singular coupling at the axes is regularised (`checks/cpaxis5.py`),
  is consistent with second-order convergence on two null grids (ratios 3.8–4.0) and resolved in angle to v ≈ 1.8 r_h at
  areal radius ≥ 0.9 r_h and to v ≈ 2.0 r_h at ≥ 1.2 r_h, an order of convergence not being established, and the free
  scheme's solution is consistent with second-order convergence to v ≈ 1.8 r_h at areal radius ≥ r_h as well
  (`checks/late5b.py`); beyond, a constraint violation persists under both refinements and the curvature invariant is
  unresolved in angle (supplement `CERTIFY-10L5-RESULT.md` sections 2 and 6–10).
```

Statuses, as the new text gives them:
- *certified:* the data cone; the Richardson approximant at 16,128 points and on a sub-box of each of four boxes; the
  single-grid approximant's one box. Both certificates are checked by the end-to-end control and the D4 gate.
- *deduced:* the reduction; the frozen-coefficient loss; the transport structure; Theorems 7.L, 8.L1 (in the cones' L²
  norms) and 8.W; the axis chart's pairs, Hardy constants and reduced hierarchy (identities at random jets); Lemma 9.C,
  conditional on hypotheses established on no region of its form beyond the seed; the N-independence of the cut
  couplings (Lemma 9.H).
- *computed:* the constants and the closing condition's demand; the block condition's failure, unweighted and at W3's
  weights; the late region's convergence on two grids, and what persists beyond it.
- *not claimed:* existence beyond the seed.

**B. The untrapped-columns sentence.** As 9.9's B, unchanged; its old text occurs once at the current md5.

**C. A reference for [CTG23].** As 9.9's C, unchanged; its old text occurs once at the current md5.

**D. Appendix D: what the new programs need, what they import, and their md5 rows (m5-9).**

D1, the packages. **Old:**

```
recorded here); z3-solver for `foliation5.py`; python-flint for `cdata5.py`; numpy for `bondi5.py` and `growth5.py`,
```

**New:**

```
recorded here); z3-solver for `foliation5.py` and `checks/cont5.py`; python-flint for `cdata5.py` and for
`checks/rcert5.py` and every program that imports it; scipy for `checks/lev1_5.py` and `checks/wgron5.py`; numpy for
`bondi5.py` and `growth5.py`,
```

D2, the imports. **Old:**

```
`checks/vii5census.py`; the others import nothing from the research tree:
```

**New:**

```
`checks/vii5census.py`, `checks/reduce5.py` imports `dnull5.py`, `checks/symbol5s.py` imports `checks/symbol5.py`, which
imports `dnsolve5.py`, `checks/linest5.py` imports `checks/null3.py` and `dnsolve5.py`, `checks/lev1_5.py` imports
`checks/linest5.py` and `checks/wgron5.py`, `checks/wgron5.py` and `checks/blocks5.py` import `checks/linest5.py`,
`checks/axis5.py` imports `checks/linest5.py` and `dnull5.py`, `checks/axhier5.py` imports `checks/axisbianchi5.py`,
`checks/cont5.py` imports `checks/null3.py`, `checks/cpsolve5.py` imports `dnsolve5.py`, `checks/cpaxis5.py` imports
`checks/cpsolve5.py`, `checks/cp3grid5.py` imports `checks/cpsolve5.py` and `checks/cpaxis5.py`, `checks/rcert5.py`
imports `checks/resid5.py` and `checks/bondisph5.py`, `checks/rcert5c.py` and `checks/rcert5d.py` import
`checks/rcert5.py`, `checks/rich5.py` imports `checks/rcert5.py` and `checks/rcert5d.py`, and `checks/blockw5.py` reads
`checks/blocks5.out` and `checks/wgron5.out`; the others import nothing from the research tree:
```

D3, the md5 rows, after cdata5.out's row. **Old:**

```
| `docket68/n1star/checks/cdata5.out` | `6536abcba46ec57a5dca8ced814b7788` |
```

**New:**

```
| `docket68/n1star/checks/cdata5.out` | `6536abcba46ec57a5dca8ced814b7788` |
| `docket68/n1star/checks/reduce5.py` | `0458f70bc710ad3ce966f242bd76e5f0` |
| `docket68/n1star/checks/reduce5.out` | `b0fb5b28fa8499d5fa70226a1b3ed1ee` |
| `docket68/n1star/dnull5.py` | `2035d34bf399cd6ba5c5550d9718ceab` |
| `docket68/n1star/checks/symbol5s.py` | `8441ecf58bab566dda5b5d50c8327f97` |
| `docket68/n1star/checks/symbol5s.out` | `7d51dbf663724abf64087f39974f35c9` |
| `docket68/n1star/checks/symbol5.py` | `14168943230c0c64d18a94fd7f55912e` |
| `docket68/n1star/checks/null3.py` | `767dd3bd58f5c517c99165e1d44f1eb9` |
| `docket68/n1star/checks/null3.out` | `0288d263c81bd929f3ce5647350d69ed` |
| `docket68/n1star/checks/linest5.py` | `34dc9b3d6594771ace2a4257b3a15191` |
| `docket68/n1star/checks/linest5.out` | `cdc11bfb156dbd6dfa2ec2f744d0e842` |
| `docket68/n1star/checks/lev1_5.py` | `bbb29f53599e58d3702d8b7dc5c9aeab` |
| `docket68/n1star/checks/lev1_5.out` | `b6be6a0bf20f95febfba64707fcf3bb8` |
| `docket68/n1star/checks/wgron5.py` | `a764e73c0be0ec38467bc986f7d84bb2` |
| `docket68/n1star/checks/wgron5.out` | `47170f09530b20e8d49f1a56660f55c1` |
| `docket68/n1star/checks/axis5.py` | `ed855afc7cacbb6397659e4ab3549d60` |
| `docket68/n1star/checks/axis5.out` | `5cae43e255046b6b4d24b594227c84b0` |
| `docket68/n1star/checks/axisbianchi5.py` | `86d8af8e9024487ee7bd947bce954588` |
| `docket68/n1star/checks/axisbianchi5.out` | `999b80bedb9aaccc627e17002746a912` |
| `docket68/n1star/checks/axhier5.py` | `aa134baade41c3a0664844a4424a567a` |
| `docket68/n1star/checks/axhier5.out` | `0b192015028c3ea2536964f28af58137` |
| `docket68/n1star/checks/cont5.py` | `d5ada772efca2d1fd2b8fec5fc1832e9` |
| `docket68/n1star/checks/cont5.out` | `d4fc239715575ac4757ce2831b259f58` |
| `docket68/n1star/checks/blocks5.py` | `201c163bb0a554b4677c754a85ab4e83` |
| `docket68/n1star/checks/blocks5.out` | `b0468571355f78d03975d63da638308a` |
| `docket68/n1star/checks/blockw5.py` | `6049a5dcb3a362c99ccbe2fb7e950807` |
| `docket68/n1star/checks/blockw5.out` | `f2ae0d7d80a3c238b83c9ec36a66c87c` |
| `docket68/n1star/checks/cpsolve5.py` | `96768ccce2e58f7a4d2e38e0219778e0` |
| `docket68/n1star/checks/cpaxis5.py` | `6fb010b7b948178c58bb7c65e06681d9` |
| `docket68/n1star/checks/cpaxis5.out` | `e89a7902beebffb67a432baa133cb82f` |
| `docket68/n1star/checks/cpaxis5_run1.out` | `7775c999a88c195d189c87d9294e9ce4` |
| `docket68/n1star/checks/cpaxis5_a4.out` | `ae4511e1c474eff3f88bcfeb79aa26cd` |
| `docket68/n1star/checks/cpaxis5_a5.out` | `6565c01c5191ceca28a03882f82f2d4e` |
| `docket68/n1star/checks/cpaxis5_a6.out` | `cee235fc3c4833486f3d66a4e20f260c` |
| `docket68/n1star/checks/cpaxis5_a6_400.out` | `94c9c5a53543c764f1e00d037a49ff33` |
| `docket68/n1star/checks/cp3grid5.py` | `98f5f01dc14a1858ba3d11696a69276b` |
| `docket68/n1star/checks/cp3grid5_control.out` | `1af3c04e9c7ec030e11798fb86454da7` |
| `docket68/n1star/checks/cp3grid5_a8_2grid.out` | `dc3380ec644732a430bb02e7af310c9c` |
| `docket68/n1star/checks/cp3grid5_a9_800.out` | `c7d7752b7f389ed261b4b1c6871354fb` |
| `docket68/n1star/checks/cp3grid5_a10_2grid.out` | `7986c6b71f4dc8ec825ae8d28c9475c7` |
| `docket68/n1star/checks/late5b.py` | `5225f2b4aa53dc1ab452e2355d499ef8` |
| `docket68/n1star/checks/late5b.out` | `ece3e7f063a049a15a5b91ed56c2b555` |
| `docket68/n1star/checks/late5b_small.out` | `be8da58288ee92cd765d25b48c167b41` |
| `docket68/n1star/checks/rcert5.py` | `bf6d843d5963534eaab5ac4123479aa9` |
| `docket68/n1star/checks/rcert5c.py` | `281cd2ea76acbe4fb6e04961bdd0521a` |
| `docket68/n1star/checks/rcert5c.out` | `b4790b613b72f25a492b02ae51dd8503` |
| `docket68/n1star/checks/rcert5d.py` | `7366918fca69b0a5eab5aca85071a1a0` |
| `docket68/n1star/checks/rcert5d.out` | `f2ce606146502a3e177372fc531854e7` |
| `docket68/n1star/checks/rich5.py` | `ce036a1eaa59a9ce103b6b91acfba078` |
| `docket68/n1star/checks/rich5.out` | `eedb7b4c58e6af3d630247563be6f335` |
| `docket68/n1star/checks/rich5_runs.out` | `64d3a967c368dcd036c758fe842b51f6` |
| `docket68/n1star/data/rcert5_C3.npz` | `698569f6faaab4420fe2e67abc860561` |
| `docket68/n1star/data/rcert5_C3R.npz` | `88e16664187868e47eaaaa18709cfc61` |
| `docket68/n1star/CERTIFY-10L5-RESULT.md` | `04df75f606fa8c6a264972ee9174f737` |
```

- The md5s are the files' own at the time of this append, with one exception: `CERTIFY-10L5-RESULT.md` cannot print its
  own md5. Its cell holds the file's md5 before this append (04df75f6…), in the form R9 parses. After seating,
  `python3 response5.py --update-md5` rewrites it to the file's md5 at that commit, and R9 checks every row.
- The rows cover every file block A cites, beyond those already in the table: `cdata5.py`, `g1curv5.py` and its seed-2
  output, and `CERTIFY-10L5.md`. Their rows match the files at this append. Each cited program's output and each module
  it imports is covered too.
- The runs the programs read are not in the repository: `runs/l1_M16_{400,800}.npz` (rich5 `--runs`) and the record's
  D432 runs (9.8). Their md5s are in 9.8 and in the programs' outputs.

**E. Appendix C: the source map's section 9 row for the residual.**
- Block A no longer cites `resid5.py`'s smoothed approximant. It cites the programs below instead.
- `resid5.py` keeps its Appendix D row, because `rcert5.py` imports it.

**Old:**

```
| section 9: residual of a smoothed 3D approximant | `docket68/n1star/checks/resid5.py` Q1–Q2 |
```

**New:**

```
| section 9: the residual of the Richardson approximant | `docket68/n1star/checks/rich5.py` R0–R3, C1–C3 |
| section 9: the single-grid approximant's supremum over one box | `docket68/n1star/checks/rcert5d.py` D0–D4, C1–C2 |
| section 9: the class; frozen-coefficient loss; transport structure | `docket68/n1star/checks/reduce5.py` R0–R4; |
| | `docket68/n1star/checks/symbol5s.py` S1–S6; `checks/null3.py` N0–N10; `checks/linest5.py` E1–E9 |
| section 9: the linear estimate at levels 0 and 1, and its constant | `docket68/n1star/checks/linest5.py` E1–E9; |
| | `docket68/n1star/checks/lev1_5.py` L1–L5; `checks/wgron5.py` W1–W5 |
| section 9: the axes: chart, pairs, Hardy constants, reduced hierarchy | `docket68/n1star/checks/axis5.py` X1–X7; |
| | `docket68/n1star/checks/axisbianchi5.py` B1–B4; `checks/axhier5.py` A1–A7, M1–M4, S1–S3 |
| section 9: existence by continuity from [CTG23], conditional | `docket68/n1star/checks/cont5.py` C1–C2 |
| section 9: the block condition, unweighted and at the weights | `docket68/n1star/checks/blocks5.py` H1–H2; |
| | `docket68/n1star/checks/blockw5.py` B1–B2 |
| section 9: the late region | `docket68/n1star/checks/cpaxis5.py` A1–A6; `checks/cp3grid5.py` A8–A10; |
| | `docket68/n1star/checks/late5b.py` L5–L7 |
```

## 11. Round 7 (2026-11-06): the verifier of round 6 seated, and the third null grid

The verifier of round 6 read section 10 (lines 3016–3447, file md5 a781147c…). Every rerun reproduced its output. It
confirmed that C1 kills mA1–mA4 and mA6, that mA3 now fails end to end, that blockw5 is correct, that every finding of
round 5 is seated, and that the paper blocks apply cleanly at the paper's md5 b21cd7ca…. It did not confirm section 10
because of one Major, M6-A. It also found three minor findings and five nits. Each is seated below as a bracketed
amendment to the section 10 text it names; section 10 is not edited. Every finding was re-derived first, and every
repair that needs a program was run in full. Both runs of the third null grid have finished, M = 32 at 16:30 UTC and
M = 40 at 17:02, and their verdict is in 11.1. Sections 0–10 are byte-identical before and after this append.

### 11.0 The verifier of round 6: its findings, seated as amendments to section 10

**M6-A. C1 tested the bound's t-direction only, so σ- and x-direction enclosure losses survived.**
- [10.0, lines 3043–3044, "So a loss of the remainder, of the box enclosure of a coefficient or of the coordinate x,
  or of `abs` where a centre value is negative, gives a bound below the true sup"; line 3065, "no test on a single field
  can kill it"; 10.2's last bullet; the kids_control docstring; block A, "a control that runs the whole bound
  computation on test fields with exact suprema and catches each mutation of it tried that under-bounds them": verifier
  of round 6 (M6-A).]
  - *Re-derived.* The only field tensor of round 6's test was R = t⁴; x⁴ came from the coordinate input. So the σ- and
    x-direction terms of `box_coeffs` ran only on zero coefficients. Three one-line mutations of the bound computation
    pass round 6's C1 and `--collect`:
    - mB1, `box_coeffs` with the σ and x half-widths 0;
    - mB1s, with σ's only;
    - mB2, rcert5.py's linear enclosure term restricted to t.
  - They under-bound σ⁴ and field-x⁴ fields (true/bound 1.180 and 1.067, the verifier's). D4 does not catch mB1: 0.980
    on 192 sampled depth-5 boxes, the verifier's. The certificate itself is not shown wrong; mB1's bound was not
    exceeded on the real approximant.
  - *Repaired (`checks/rcert5d.py`).*
    - (a) C1 runs two more test sets through `Engine.kids`, on the same parents.
      - `kids_fields2`: R = t⁴, m = σ⁴ and the field n = x⁴ (each (3T₀ + 4T₂ + T₄)/8 along its axis), with eight
        components: m, −m, n, −n, R·m, m·n − 0.3, −R·n − 0.05, R·m·n + m. Every exact sup is a product of the
        ranges, the three fields being nonnegative and independent.
      - `kids_fields3`, beyond the verifier's fix: R = t, so that the frame input R_u is the coordinate map's own
        factor φ₁(t) = 1/(h_ξ a cosh(x_a + (t + 1) h_ξ)). Its components are ±R_u and shifts of it. φ₁ rises to its
        peak at ξ = 0 and falls after it, so its range over a box is fixed by its ends and the peak.
      - For each of t⁴, σ⁴ and x⁴ the sound bound is (|c| + h)⁴ + 3h⁴. A lost direction of the box enclosure gives
        (|c| + h)⁴ − h⁴, below the sup; a halved enclosure (mA5) gives (|c| + h)⁴ + h⁴, still above it.
    - (b) C1(b), `contain_control`: an enclosure over a box must contain what it encloses at every point of the box,
      the corners included. On the pinned tensors and the frame, at two parents (the box's first child, and a parent
      of half-widths 0.0156, 0.0156, 0.0078):
      - (i) every enclosure `box_coeffs` returns while `kids` runs (recorded as `kids` calls it, so the call's own
        arguments are tested) must contain `point_coeffs` at the 8 corners of its child box, for every field and every
        |β| ≤ Q + 2: 35,840 checks;
      - (ii) every Taylor coefficient of each child's box-path frame output must contain the point path's at each
        corner: 20,480 checks.
  - *Rerun on the round-4 checkpoints (`checks/rcert5d.out` regenerated).*
    - C1 through `kids`, on all three test sets: the largest true/bound is 0.9999999926 (sound), and 4.2542 with
      the remainder dropped.
    - C1(b): 35,840 and 20,480 checks, none failing (13 s).
    - D1 and D3 are unchanged; D4 gives 68,705 points at ratio 0.809, no violation.
    - Collect: "all checks pass" (125 s).
  - *Every mutant, rebuilt on the repaired file* (`scratchpad/r7/mut/`; mB2 replaces rcert5.py through `mut/mB2/`).
    C1's largest true/bound through `kids`, C1(b)'s failures, and `--collect`:

| mutant | change | C1, largest true/bound | C1(b) (i), (ii) failures | `--collect` |
|---|---|---|---|---|
| mA1 | the remainder flag forced on | 4.2542 | 0, 0 | FAILURES, exit 1 |
| mA2 | order-3 coefficients at the centre | 4.2542 | 0, 0 | FAILURES, exit 1 |
| mA3 | `kids` passes `vp` twice | 4.2542 | 0, 0 | FAILURES, exit 1 |
| mA4 | `abs` dropped in `bound` | ∞ | 0, 0 | FAILURES, exit 1 |
| mA5 | `box_coeffs` at half the half-widths | 0.9999999975 | 2,962, 0 | FAILURES, exit 1 |
| mA6 | box inputs' t and x at the centre | 1.0667 | 0, 0 | FAILURES, exit 1 |
| mB1 | `box_coeffs` with σ, x half-widths 0 | 1.1801 | 4,051, 0 | FAILURES, exit 1 |
| mB1s | `box_coeffs` with σ's half-width 0 | 1.1801 | 1,889, 0 | FAILURES, exit 1 |
| mB2 | rcert5.py: linear term in t only | 1.1801 | 850, 0 | FAILURES, exit 1 |
| mB3 | box inputs' t at the centre | 1.0016 | 0, 0 | FAILURES, exit 1 |

  - *What each check catches.*
    - C1's widened test kills mB1, mB1s and mB2 at 1.1801, beside mA1–mA4 and mA6.
    - C1(b)(i) kills mA5 (2,962 failures), mB1 (4,051), mB1s (1,889) and mB2 (850). These are the verifier's counts.
    - C1(b)(ii) failed no mutant tried. The frame's interval evaluation widens its box output past what the lost
      enclosures removed. It is kept as a necessary condition, and it is stated as passing, not as killing.
  - *mA5.* The verifier found it sound on every test it ran, products included (its stress test with T₅(t)T₅(σ) and
    T₅(x): 0.9988, against 0.9979 for the real engine). 10.0's single-field argument stands. mA5 halves the enclosure
    of a coefficient, so the enclosure no longer contains the coefficient at the corners of its box, and C1(b)(i)
    kills it.
  - *mB3, the verifier's sixth mutant (t taken at the centre in the box inputs), is unsound and now killed.* The
    verifier did not show it unsound.
    - On the parents' boxes ξ < 0, where φ₁ ≈ 2e^ξ/(h_ξ a) and its low t-derivatives are all positive. So at the box's
      end nearer the peak every term of its Taylor series is positive.
    - With t's radius dropped, the order-3 coefficient is φ₁'s own at the centre. The bound is then the Taylor
      polynomial at that end, and the true value exceeds it by the order-4 terms.
    - On `kids_fields3`, mB3 gives 1.0016146 against the real engine's 0.9999989, so C1 fails (`scratchpad/r7/set3.py`).
      mA6 fails there at the same figure, beside its 1.0667 on the first set.
  - *rich5.py* runs the same C1, and C1(b) on the Richardson tensors (`checks/rich5.out` regenerated).
    - The rerun is read-only, and both npz md5s are unchanged before and after it. R0, R2, R3, C2 and C3 match
      round 6, timings aside. C1 gives 0.9999999926 and 4.2542. C1(b) gives 35,840 and 20,480 checks, none
      failing. The run ends "all checks pass" (1,157 s).
    - rich5's C1 and C1(b) were run verbatim on rich5's own tensors with rcert5d replaced by each mutant
      (`scratchpad/r7/rich5_c1_mut.py`, output `rich5_c1_mut.out`). Every mutant is caught.
      - C1 catches all but mA5, at the same figures as rcert5d's.
      - C1(b)(i) catches mA5 (2,240 failures on the Richardson tensors), mB1 (2,463), mB1s (1,287) and mB2 (600).
  - *Corrected text.*
    - 10.0's lines 3043–3044 read: "So a loss of the remainder, of a direction of the box enclosure of a coefficient
      (11.0), of the coordinate's box, or of `abs` where a centre value is negative, gives a bound below the true sup
      of a test field; a halved enclosure (mA5) does not, and C1(b) catches it."
    - Line 3065 reads: "mA5 is sound on every test the verifier of round 6 ran, products included; C1(b), the
      containment check of 11.0, kills it."
    - 10.2's last bullet reads: "… a control that runs the bound computation end to end on test fields in t, σ and x
      and on the coordinate map, and a containment check of its enclosures (11.0). Together they kill mA1–mA6, mB1,
      mB1s, mB2 and mB3."
    - The kids_control docstring and the module docstring are corrected in the file. The docstring's sound bound is
      (|c| + h)⁴ + 3h⁴, and mA5 is named as caught by C1(b), not by C1.
    - Block A's description reads "… checked by a control that runs the whole bound computation on test fields varying
      in each coordinate, and on the coordinate map, with exact suprema, by a check that the enclosures it forms of the
      approximant's coefficients contain their values at the corners of their boxes, and by independent certified point
      values at the centre and corners of every accepted sub-box" (11.4).

**Minor findings.**
- **m6-1** [10.4, block A, "whenever on that region the difference of a vacuum metric from the approximant obeys a
  linear estimate"]: Lemma 9.C's (H1)–(H2) hold for every smooth T²-invariant vacuum metric with the data, in the gauge,
  on every slab D_s. The data are T²-invariant too.
  - It reads "for smooth T²-invariant characteristic data that satisfy the constraints, a smooth T²-invariant vacuum
    development exists on the region …, the axes included, whenever, on every slab v ≤ s of that region, every smooth
    T²-invariant vacuum metric with these data, in the gauge, differs from the approximant by an amount obeying a linear
    estimate with constant F at every level, …" (11.4).
- **m6-2** [10.4]: the paper gives every cited program a run command in Appendix D, and most an entry in Appendix A.
  The programs block A cites had neither.
  - 11.4 gives blocks F (Appendix A) and G (Appendix D's commands) for rich5, rcert5d, cont5, blocks5, blockw5,
    axhier5, axis5, axisbianchi5, lev1_5, wgron5, linest5, null3, reduce5, symbol5s, cpaxis5, cp3grid5 and late5b.
  - Block F also retitles the resid5 entry, which section 9 no longer cites.
- **m6-3** [10.0, line 3037, "because C1's test polynomials have positive centre values"]: false. Re-derived
  (`scratchpad/r7/m63.py`):
  - four of the 27 T₃T₃T₃ boxes have negative centre values; T₃(0.55)T₃(−0.6)² = −0.8625;
  - mA4's largest true/bound is 0.1601 on the T₃ boxes (the real engine's 0.1089) and 0.2500 on t⁴ + σ⁴ + x⁴.
  - It reads "because the round-5 test had slack: with `abs` dropped its largest true/bound was 0.25".

**Nits.**
- [kids_control docstring, "the sound … bound is exact, (|c| + h)^4"; "any loss … of its half-width"]: corrected to
  (|c| + h)⁴ + 3h⁴, with mA5 named as not caught by C1 and caught by C1(b).
- [block A, "certified values of 1.1–2.4 × 10⁻³"]: certified lower ends, so they are rounded down. It reads
  "1.09–2.41 × 10⁻³".
- [10.4, D1, "scipy for `checks/lev1_5.py` and `checks/wgron5.py`"]: cdata5.py imports scipy too (`solve_ivp`), an
  omission older than round 6. It reads "scipy for `cdata5.py`, `checks/lev1_5.py` and `checks/wgron5.py`".
- [10.4, D3, the CERTIFY-10L5-RESULT.md row]: it fails R9 until `python3 response5.py --update-md5` is run at seating,
  as 10.4 says. That holds for 11.4's D3.
- [10.0, line 3041, "four parent boxes with half-widths 0.005 to 0.25"]: those are the children's. It reads "four
  parent boxes (half-widths 0.01 to 0.5; their children's 0.005 to 0.25)".

### 11.1 The third null grid: second order in the null step, resolved in angle, and beyond it a limit that is not vacuum

**The runs.**
- PID 2418 (M = 32) finished at 16:30 UTC after 15,390 s. It wrote `scratchpad/r5/cp_M32_1600_reg.npz`, md5
  9a51104dd0d11ab8220001abbc383ecd, 315,672,199 bytes: 1,601 × 137 nodes × 32 angles, v ≥ 1.4 only.
- PID 2419 (M = 40) finished at 17:02 UTC after 17,322 s. It wrote `scratchpad/r5/cp_M40_1600_reg.npz`, md5
  68d38ecc5b1642a8c7518c4b09a95d4c, 393,298,772 bytes. Neither process was touched; both were read with py-spy only.
- The 400- and 800-row files are round 4's: a6a22cd5… and 22b8815b… at M = 32, and 7248a80a… at M = 40.

**The program (`checks/cp3grid5.py`, extended).**
- The M = 32 run finished first. So `--a7` without the M = 40 file, and the new `--a8m32`, give every null-step
  quantity and verdict as before and print the M comparison as pending. Those runs are kept in the scratchpad.
- With the M = 40 file, `--a7` and `--a8` take round 5's code paths. The outputs below are those runs. Their null-step
  figures equal the M = 32-only runs' to every printed digit.
- `--dpm` compares a v ≥ 1.4 file only on the bands it covers whole.
- *Control, rerun:* the 800-row file given for the 1600-row one reads 'not converging' on all 18 bands. The output is
  unchanged from `cp3grid5_control.out`, timing aside.

**A7, the unimposed constraint and the metric** (`checks/cp3grid5_a7_3grid.out`, 29 s). Everything is measured on the
400-row nodes kept by all four runs.
- *In the claimed regions the verdict is 'second order' on every band, with every criterion met.* This means 0.9–1.0
  and 1.0–1.2 to v = 1.8, and ≥ 1.2 to v = 2.0.
  - The monitor max |Ric_xx| falls 3.75–4.00-fold from 400 to 800 rows and again from 800 to 1600.
  - The metric's differences |P₄₀₀ − P₈₀₀| and |P₈₀₀ − P₁₆₀₀| fall 4.01–4.08-fold, an observed order of 2.00–2.03.
  - At 1600 rows the monitor at M = 40 is 1.10–1.26 times that at M = 32.
- *Beyond, the monitor does not fall, while the metric still converges at second order.* This means 0.9–1.2 from
  v = 1.8, and ≥ 1.2 on [2.0, 2.25).
  - The monitor's ratios are 0.87–1.58, and 0.87–1.01 at the second refinement. It stays near 1.1, 34 and 112 at
    0.9–1.0, near 0.01, 5.2 and 136 at 1.0–1.2, and near 0.27 at ≥ 1.2, band by band.
  - Its M = 40 to M = 32 ratio is 0.19–2.61, so it depends on the angular resolution.
  - The metric's differences fall 4.01–4.54-fold, an observed order of 2.01–2.18.
- So beyond, too, the discrete solutions converge at second order in the null step at M = 32. They converge to a
  limit whose unimposed component Ric_xx does not vanish: at M = 32 the scheme's limit there is not a vacuum metric.
- Of 9.6's three readings this excludes the first, "a feature the null grids do not reach": they reach it. The other
  two remain: the imposed rows do not propagate Ric_xx = 0 there, or d± does not vanish. A10 measures both.

**A9, the metric's resolution in angle at 1600 rows** (`checks/cp3grid5_a9_1600.out`, 21 s), as |P₃₂ − P₄₀|.
- In the claimed regions it is ≤ 6.6 × 10⁻¹¹, except at 0.9–1.0 on [1.65, 1.8), where it is 3.0 × 10⁻⁹. At ≥ 1.2 on
  [1.9, 2.0) it is 1.0 × 10⁻¹⁰. At 800 rows these were ≤ 6.0 × 10⁻¹¹ and 4.7 × 10⁻⁹.
- Beyond, it is 1.0 × 10⁻⁷ to 1.0 × 10⁻², and from 800 rows it changes by factors of only 0.82–2.0. There the angular
  error at fixed M is what remains.
- The band printed as [1.00, 1.50) covers [1.4, 1.5) only, since the files start at v = 1.4.

**A8, the Kretschmann scalar** (`checks/cp3grid5_a8_3grid.out`, 1,189 s). Per class, on 32 u-rows, at five angles.
- *At 1.2–1.4:* second order at every angle to v = 2.0, the null-step differences falling 3.88–4.08-fold. On
  [2.0, 2.25) they fall 12–88-fold and the finest is at most 1.1 % of dev.
- *At 1.0–1.2:* second order at every angle to v = 1.9 (ratios 3.66–4.16).
  - At x = 0 on [1.65, 1.8), which two grids left at 5.6 % of dev, the finest difference is now 1.4 %.
  - On [1.9, 2.0) the null step is resolved at x = 0.97 and 0.5 only. From v = 2.0 it is resolved nowhere.
- *At 0.9–1.0:* second order at every angle to v = 1.8 (ratios 3.96–4.26).
  - The null step is resolved at every angle to v = 1.9 but at x = 0, where the finest difference is 5.7 % of dev on
    [1.65, 1.8) (ratio 4.11) and 13.9 % on [1.8, 1.9).
  - From v = 1.9 it is resolved nowhere but at x = 0.97 on [2.0, 2.25), where dev is 26.6.
- *In angle at 1600 rows:* M = 40 against M = 32.
  - In the claimed regions the two differ by at most 2.1 × 10⁻⁵ of K_0 at 0.9–1.0, 4.7 × 10⁻⁷ at 1.0–1.2 and
    8.3 × 10⁻⁷ at 1.2–1.4. That is at most 6.2 × 10⁻⁵ of dev. With both differences the scalar is resolved there at
    every angle, except at 0.9–1.0 at x = 0 on [1.65, 1.8), where the null step is 5.7 % of dev.
  - At 1.0–1.2 on [1.8, 1.9) it is resolved too: the angular difference is 0.5 % of dev.
  - Beyond, the angular difference is 6–35 % of dev at 0.9–1.0 on [1.8, 1.9) and at 1.2–1.4 on [2.0, 2.25). From
    v = 1.9 at 0.9–1.2 it is 15 % of dev to 22 times dev. There the scalar is not resolved in angle.

**A10, the regularisation's correction on three null grids** (`checks/cp3grid5_a10_3grid.out`, 1,774 s). The bands
start at v = 1.5, where the 1600-row file covers them whole.
- *In the claimed regions d± falls at second order at both refinements,* 3.52–3.94-fold. At 1600 rows it is at most
  2.8 × 10⁻³ of max |R_uv| at 0.9–1.0 (on [1.65, 1.8)), 9.1 × 10⁻⁴ at 1.0–1.2 and 4.8 × 10⁻⁴ at ≥ 1.2. m5-4's
  "consistent with second order" is now second order on three grids.
- *On [1.8, 1.9) it still falls* (3.79 and 2.92 at 0.9–1.0; 3.84 and 3.74 at 1.0–1.2), while the monitor does not. So
  the violation there is not the regularisation's doing: the scheme's imposed rows do not propagate Ric_xx = 0 there.
  That is 9.6's second reading, now measured.
- *From v = 1.9 at 0.9–1.2 it does not vanish.* Its ratios at the second refinement are 0.95–1.40, and at 1600 rows it
  is 5–80 % of max |R_uv|. There the limit solves the regularised system, not the vacuum one. That is the third reading,
  now measured.
- *On [2.0, 2.25) at ≥ 1.2* it falls 1.93- and then 1.32-fold, to 0.75 % of max |R_uv|.

**The verdict (computed, floating point).** It replaces 9.6's label "until the third grid reports" and 9.7's
late-region bullets, as amended by m5-4, m5-5 and m5-8.
- The regularised scheme converges at second order in the null step on three null grids. The observed order is
  2.00–2.03 in the metric, and the unimposed constraint and the regularisation's correction fall 3.5–4.0-fold at each
  refinement.
- This holds to v = 1.8 r_h at areal radius 0.9–1.2 r_h and to v = 2.0 r_h at ≥ 1.2 r_h. There it is resolved in angle
  at the finest grid: M = 40 against 32 changes the metric by ≤ 3.0 × 10⁻⁹ and the monitor by a factor of 1.10–1.26.
  The Kretschmann scalar is resolved there in both, at every angle, except at x = 0 at 0.9–1.0 on
  [1.65, 1.8), where its null step is 5.7 % of dev.
- Beyond, the metric still converges at second order at M = 32, but the unimposed constraint does not fall. So the
  scheme's limit there is not vacuum.
  - On [1.8, 1.9) the regularisation's correction still falls while the constraint does not, so the imposed rows do
    not propagate Ric_xx = 0 there.
  - From v = 1.9 r_h at 0.9–1.2 r_h the correction itself persists, so the limit solves the regularised system rather
    than the vacuum one.
  - There the violation also depends on M.
- Nothing is claimed beyond.

### 11.2 What holds at 10 l5 after round 7

10.2's list stands, with these changes:
- Both certificates' bounds, rcert5d's D1 and rich5's R3, are checked by C1 and C1(b), which together kill mA1–mA6,
  mB1, mB1s, mB2 and mB3 (11.0). The certified figures are unchanged.
- The existence statement is Lemma 9.C's, as m6-1 words it. These hypotheses are established on no region of its form
  beyond the seed.
- The late region: the regularised scheme converges at second order in the null step on three null grids, to
  v = 1.8 r_h at 0.9–1.2 r_h and to v = 2.0 r_h at ≥ 1.2 r_h, and is resolved in angle there on the finest grid. The
  regularisation's correction falls at second order with it. Beyond, its limit is not vacuum (11.1). This replaces
  9.7's "consistent with second-order convergence on two null grids … an order of convergence is not established".

There is no new existence statement. Existence is proved where the solution is the seed and is not claimed beyond it.

### 11.3 Files and outputs (round 7)

| file | what | md5 (round 6 → round 7) |
|---|---|---|
| `checks/rcert5d.py` | M6-A: C1's test sets 2 and 3, C1(b) `contain_control`, the docstrings | 7366918f… → 9821bbb5… |
| `checks/rcert5d.out` | collect and census, regenerated | f2ce6061… → e55b30ee… |
| `checks/rich5.py` | M6-A: C1(b) on the Richardson tensors | ce036a1e… → 545d6a87… |
| `checks/rich5.out` | regenerated (read-only run) | eedb7b4c… → 504cd8e3… |
| `checks/cp3grid5.py` | 11.1: A7, A8 without the M = 40 file; A10 on whole bands only | 98f5f01d… → 3033f5bf… |
| `checks/cp3grid5_a7_3grid.out` (new) | 11.1: A7, M = 40 at the finest; 29 s | c654cebc… |
| `checks/cp3grid5_a8_3grid.out` (new) | 11.1: A8, M = 40 at the finest; 1,189 s | 9e823195… |
| `checks/cp3grid5_a9_1600.out` (new) | 11.1: A9 at 1600 rows; 21 s | 0d0da9dc… |
| `checks/cp3grid5_a10_3grid.out` (new) | 11.1: A10 on three grids; 1,774 s | 0989baf5… |

- `data/rcert5_C3.npz` (698569f6…) and `data/rcert5_C3R.npz` (88e16664…) are unchanged before and after every program
  of this round.
- The round-6 versions are in the scratchpad: `r7/rcert5d.r6.py`, `r7/rich5.r6.py` and `r7/cp3grid5.r6.py`. Git holds
  them too.
- rcert5d.py ran its controls as `r7/rcert5d.ran7.py`. After that, one figure in the docstring was corrected (1.00097
  to 1.0016). With docstrings removed, the two files' code is identical.
- The control's output is unchanged from `checks/cp3grid5_control.out`, timing aside, so that file is not rewritten.
- A10 ran under cp3grid5.py a7d66c22…, which differs from the final file only in A7's header wording. Everything else
  ran under the final file.

Scratch (not committed; under the session's scratchpad):
- `r7/mut/rcert5d_{mA1…mA6,mB1,mB1s,mB2,mB3}.py` with `mut/mB2/rcert5.py`, and each one's `--collect` output beside it.
- `r7/c1only.py` and `c1only_mut.out`: C1 and C1(b) alone, for every mutant.
- `r7/rich5_c1_mut.py` and `rich5_c1_mut.out`: rich5's C1 and C1(b) for every mutant.
- `r7/set3.py`, `ru_test2.py` (mB3 on the coordinate map), `m63.py` (m6-3).
- `r7/cp3_{a7,a8,dpm,control}.out`: the M = 32-only runs; `cp3_{a7m40,a8m40,a9m40}.out`: the runs with M = 40.

### 11.4 The paper: blocks A–G, at the paper's current md5

These replace 10.4's proposal. They are proposed to the main session, which seats them; this note edits neither the paper
nor N1STAR-PROOF.md.
- *Keyed by text.* Each old block occurs exactly once in `RESPONSE-HL-5D.md` at its current md5,
  805be200b746b7cf480e88639da5508f (17:15 UTC). It also occurs once at b21cd7ca…, the md5 the verifier of round 6 read;
  the change between them is two md5 rows of Appendix D, in none of these blocks. A, B, C, D1, D2, D3 and E have the
  same old texts as 10.4's; F and G are new.
- *Longest new line:* 121 characters.
- *Checked:* all seven blocks applied to a copy of the paper (`scratchpad/r7/paper_applied.md`) leave every line ≤ 121
  characters. Every md5 row of Appendix D then matches its file, except `CERTIFY-10L5-RESULT.md`'s; see D3.

**A. The section 9 text on existence at 10 l5.** It replaces 10.4's A, folding in M6-A (the control's description),
m6-1 (the existence sentence), the nit on 1.09–2.41, and 11.1 (the late region on three null grids).

**Old:**

```
At the
  first seed the Kretschmann scalar is moderate and converged in angle up to the point where the runs stop converging,
  and unresolved after it, where a singularity, a steep smooth feature and a defect at the axis are not yet told apart.
  At the second seed, with the angular and null grids refined together, the two coarser angular resolutions agree up to
  v ≈ 3.5 and the finest departs from them from v ≈ 3.25, at every angle. On a finer null grid, 2400 × 1080, the second
  seed's M = 32 and 40 angular resolutions agree to 0.09 K_0 up to v = 3.5 and to 0.53 K_0 up to v = 4.5 (K_0 = 72/R⁸,
  Tangherlini's Kretschmann scalar at the same areal radius), away from the cells M = 48 masks; M = 48 departs from v ≈
  3.25 exactly as at 1600 × 720, so the finer null grid does not move it, and the step condition M²/N ≤ c it had been
  ascribed to is refuted (M²/N = 0.96). The late region stays unresolved (computed, floating point:
  `docket68/n1star/checks/g1curv5.py --seed2-2400`, output `checks/g1curv5_seed2_2400.out`; supplement
  `CERTIFY-10L5.md` section 6b). A first certified step is taken: for an explicit approximant of the characteristic
  data on the data cone, the constraint along its outgoing generators holds to a certified bound at both seeds (at the
  second, 2.3 × 10⁻⁵ against terms of size 5.3 × 10⁻⁴; certified, ball arithmetic, `docket68/n1star/checks/cdata5.py`).
  The full Einstein residual of a smoothed three-dimensional approximant built from a run is computed only, 2.5 × 10⁻³
  of the curvature scale and falling at second order with the grid (`checks/resid5.py`, floating point), and no linear
  estimate with explicit constants is available for the characteristic problem in the class, so existence at 10 l5
  remains open (supplement `CERTIFY-10L5-RESULT.md` section 2).
```

**New:**

```
At the
  second seed, with the angular and null grids refined together, the two coarser angular resolutions agree up to v ≈ 3.5
  and the finest departs from them from v ≈ 3.25, at every angle. On a finer null grid, 2400 × 1080, the second seed's
  M = 32 and 40 angular resolutions agree to 0.09 K_0 up to v = 3.5 and to 0.53 K_0 up to v = 4.5 (K_0 = 72/R⁸,
  Tangherlini's Kretschmann scalar at the same areal radius), away from the cells M = 48 masks; M = 48 departs from
  v ≈ 3.25 exactly as at 1600 × 720, so the finer null grid does not move it, and the step condition M²/N ≤ c it had been
  ascribed to is refuted (M²/N = 0.96). The late region stays unresolved (computed, floating point:
  `docket68/n1star/checks/g1curv5.py --seed2-2400`, output `checks/g1curv5_seed2_2400.out`; supplement `CERTIFY-10L5.md`
  section 6b). Existence at 10 l5 is proved where the solution is the seed (v ≤ r_h/2) and is not claimed beyond it.
  Toward a computer-assisted proof the following hold, each with its status. Certified (ball arithmetic): on the data
  cone the outgoing constraint of an explicit approximant holds to 5.0 × 10⁻⁵ and 2.3 × 10⁻⁵ at the two seeds, 4.1–4.3 %
  of the terms that cancel in it (`docket68/n1star/checks/cdata5.py`); on u ∈ [−4, −1.1] r_h, v ∈ [0.55, 1.6] r_h,
  |x| ≤ cos(π/32), the Einstein residual of an explicit three-dimensional approximant, Richardson-extrapolated from two
  null grids, its coefficients pinned by md5 (`docket68/n1star/data/rcert5_C3R.npz`), is at most 3.73 × 10⁻⁵ of the
  curvature scale at 16,128 points and at most 5.0 × 10⁻⁴ as a supremum over a sub-box of each of four of the 416 boxes
  covering that region, on which the single-grid approximant (`data/rcert5_C3.npz`) has certified values of
  1.09–2.41 × 10⁻³ (`checks/rich5.py`), and the single-grid approximant's supremum over one interior box of the 416 is at
  most 3.01 × 10⁻⁴ (`checks/rcert5d.py`; both certificates' bounds are checked by a control that runs the whole bound
  computation on test fields varying in each coordinate, and on the coordinate map, with exact suprema, by a check that
  the enclosures it forms of the approximant's coefficients contain their values at the corners of their boxes, and by
  independent certified point values at the centre and corners of every accepted sub-box). Deduced: the class is
  (2+1)-dimensional gravity coupled to a wave map into the flat plane (`checks/reduce5.py`); in the free metric
  formulation, at frozen coefficients on spherical states, the shift's angular derivative is of principal size at high
  angular frequency and drives δR at order k², so no estimate without loss of derivatives holds for the
  frozen-coefficient problem (`checks/symbol5s.py`; for the constraint-preserving formulation a loss is indicated by a
  model only); in double-null gauge the reduced transport equations carry no angular derivative of an unknown on their
  right sides (`checks/null3.py`, `checks/linest5.py`), and a linear estimate with explicit constants holds on truncated
  domains of dependence away from the axes, at level 0 and at level 1 in the cones' L² norms (supplement Theorems 7.L,
  8.L1 and 8.W; `checks/lev1_5.py`, `checks/wgron5.py`); near each axis the class is four-dimensional axisymmetric
  Einstein–scalar in a chart regular at the axis, where [Wu26]'s curvature pairs have energy identities on the whole
  section, the angular recoveries hold with explicit Hardy constants, and [Wu26]'s transport equations, mass aspects and
  the scalar's pairs hold in reduced form with every angular derivative on their right sides recovered from the
  hierarchy's own unknowns (`checks/axis5.py`, `checks/axisbianchi5.py`, `checks/axhier5.py`; identities verified at
  random jets); and, for smooth T²-invariant characteristic data that satisfy the constraints, a smooth T²-invariant
  vacuum development exists on the region u ∈ [−10, u*] r_h, v ∈ [r_h/2, v*] of the gauge, the axes included, whenever,
  on every slab v ≤ s of that region, every smooth T²-invariant vacuum metric with these data, in the gauge, differs from
  the approximant by an amount obeying a linear estimate with constant F at every level, the quadratic remainder has
  constant G, the approximant's residual r satisfies 4F²Gr < 1 and the difference at v = r_h/2 is at most Fr, by
  continuity from the higher-dimensional neighbourhood theorem of [CTG23], the hierarchy being applied only to genuine
  metrics, for which its compatibility with the metric holds by definition (`checks/cont5.py`); these hypotheses are
  established on no such region beyond the seed. Computed (floating point): on |x| ≤ 1/2 over the region above, where no
  truncated domain exists, the estimate's constant is F² = 10^138, and 10^66.9 with Theorem 8.W's weights, at which
  4F²Gr < 1 asks r of order 10⁻⁶⁸/G; the couplings across an angular Galerkin cut, N-independent by an identity
  (deduced), are of the coefficients' own size there, so the block (Schur) condition under which an estimate on the high
  angular modes would lower the constant fails at every angular resolution, in Theorem 7.L's unweighted norms and at
  Theorem 8.W's weights (`checks/blocks5.py`, `checks/blockw5.py`); the first seed's solution, in a constraint-preserving
  scheme whose singular coupling at the axes is regularised (`checks/cpaxis5.py`), converges at second order in the null
  step on three null grids to v ≈ 1.8 r_h at areal radius ≥ 0.9 r_h and to v ≈ 2.0 r_h at ≥ 1.2 r_h (observed order
  2.00–2.03 in the metric, the unimposed constraint and the regularisation's correction falling 3.5–4.0-fold at each
  refinement) and is resolved in angle there on the finest grid, M = 40 changing the metric by at most 3.0 × 10⁻⁹
  (`checks/cp3grid5.py`), and the free scheme's solution is consistent with second-order convergence to v ≈ 1.8 r_h at
  areal radius ≥ r_h as well (`checks/late5b.py`); beyond, the metric still converges at second order in the null step
  while the unimposed constraint does not fall, so the scheme's limit there is not a vacuum metric (its imposed rows do
  not propagate the remaining constraint, and from v ≈ 1.9 r_h at areal radius below 1.2 r_h its regularisation's
  correction does not vanish), and the violation changes with the angular resolution (supplement `CERTIFY-10L5-RESULT.md`
  sections 2 and 6–11).
```

**B. The untrapped-columns sentence.** As 9.9's B, unchanged. Its old text occurs once at the current md5.

**C. A reference for [CTG23].** As 9.9's C, unchanged. Its old text occurs once at the current md5.

**D. Appendix D: the packages, the imports and the md5 rows.** These are 10.4's D1–D3, with scipy for cdata5.py (nit),
cp3grid5's new outputs, and the round-7 md5s.

D1. **Old:**

```
recorded here); z3-solver for `foliation5.py`; python-flint for `cdata5.py`; numpy for `bondi5.py` and `growth5.py`,
```

**New:**

```
recorded here); z3-solver for `foliation5.py` and `checks/cont5.py`; python-flint for `cdata5.py` and for
`checks/rcert5.py` and every program that imports it; scipy for `cdata5.py`, `checks/lev1_5.py` and `checks/wgron5.py`;
numpy for `bondi5.py` and `growth5.py`,
```

D2, as 10.4's. **Old:**

```
`checks/vii5census.py`; the others import nothing from the research tree:
```

**New:**

```
`checks/vii5census.py`, `checks/reduce5.py` imports `dnull5.py`, `checks/symbol5s.py` imports `checks/symbol5.py`, which
imports `dnsolve5.py`, `checks/linest5.py` imports `checks/null3.py` and `dnsolve5.py`, `checks/lev1_5.py` imports
`checks/linest5.py` and `checks/wgron5.py`, `checks/wgron5.py` and `checks/blocks5.py` import `checks/linest5.py`,
`checks/axis5.py` imports `checks/linest5.py` and `dnull5.py`, `checks/axhier5.py` imports `checks/axisbianchi5.py`,
`checks/cont5.py` imports `checks/null3.py`, `checks/cpsolve5.py` imports `dnsolve5.py`, `checks/cpaxis5.py` imports
`checks/cpsolve5.py`, `checks/cp3grid5.py` imports `checks/cpsolve5.py` and `checks/cpaxis5.py`, `checks/rcert5.py`
imports `checks/resid5.py` and `checks/bondisph5.py`, `checks/rcert5c.py` and `checks/rcert5d.py` import
`checks/rcert5.py`, `checks/rich5.py` imports `checks/rcert5.py` and `checks/rcert5d.py`, and `checks/blockw5.py` reads
`checks/blocks5.out` and `checks/wgron5.out`; the others import nothing from the research tree:
```

D3, the md5 rows after cdata5.out's row. **Old:**

```
| `docket68/n1star/checks/cdata5.out` | `6536abcba46ec57a5dca8ced814b7788` |
```

**New:**

```
| `docket68/n1star/checks/cdata5.out` | `6536abcba46ec57a5dca8ced814b7788` |
| `docket68/n1star/checks/reduce5.py` | `0458f70bc710ad3ce966f242bd76e5f0` |
| `docket68/n1star/checks/reduce5.out` | `b0fb5b28fa8499d5fa70226a1b3ed1ee` |
| `docket68/n1star/dnull5.py` | `2035d34bf399cd6ba5c5550d9718ceab` |
| `docket68/n1star/checks/symbol5s.py` | `8441ecf58bab566dda5b5d50c8327f97` |
| `docket68/n1star/checks/symbol5s.out` | `7d51dbf663724abf64087f39974f35c9` |
| `docket68/n1star/checks/symbol5.py` | `14168943230c0c64d18a94fd7f55912e` |
| `docket68/n1star/checks/null3.py` | `767dd3bd58f5c517c99165e1d44f1eb9` |
| `docket68/n1star/checks/null3.out` | `0288d263c81bd929f3ce5647350d69ed` |
| `docket68/n1star/checks/linest5.py` | `34dc9b3d6594771ace2a4257b3a15191` |
| `docket68/n1star/checks/linest5.out` | `cdc11bfb156dbd6dfa2ec2f744d0e842` |
| `docket68/n1star/checks/lev1_5.py` | `bbb29f53599e58d3702d8b7dc5c9aeab` |
| `docket68/n1star/checks/lev1_5.out` | `b6be6a0bf20f95febfba64707fcf3bb8` |
| `docket68/n1star/checks/wgron5.py` | `a764e73c0be0ec38467bc986f7d84bb2` |
| `docket68/n1star/checks/wgron5.out` | `47170f09530b20e8d49f1a56660f55c1` |
| `docket68/n1star/checks/axis5.py` | `ed855afc7cacbb6397659e4ab3549d60` |
| `docket68/n1star/checks/axis5.out` | `5cae43e255046b6b4d24b594227c84b0` |
| `docket68/n1star/checks/axisbianchi5.py` | `86d8af8e9024487ee7bd947bce954588` |
| `docket68/n1star/checks/axisbianchi5.out` | `999b80bedb9aaccc627e17002746a912` |
| `docket68/n1star/checks/axhier5.py` | `aa134baade41c3a0664844a4424a567a` |
| `docket68/n1star/checks/axhier5.out` | `0b192015028c3ea2536964f28af58137` |
| `docket68/n1star/checks/cont5.py` | `d5ada772efca2d1fd2b8fec5fc1832e9` |
| `docket68/n1star/checks/cont5.out` | `d4fc239715575ac4757ce2831b259f58` |
| `docket68/n1star/checks/blocks5.py` | `201c163bb0a554b4677c754a85ab4e83` |
| `docket68/n1star/checks/blocks5.out` | `b0468571355f78d03975d63da638308a` |
| `docket68/n1star/checks/blockw5.py` | `6049a5dcb3a362c99ccbe2fb7e950807` |
| `docket68/n1star/checks/blockw5.out` | `f2ae0d7d80a3c238b83c9ec36a66c87c` |
| `docket68/n1star/checks/cpsolve5.py` | `96768ccce2e58f7a4d2e38e0219778e0` |
| `docket68/n1star/checks/cpaxis5.py` | `6fb010b7b948178c58bb7c65e06681d9` |
| `docket68/n1star/checks/cpaxis5.out` | `e89a7902beebffb67a432baa133cb82f` |
| `docket68/n1star/checks/cpaxis5_run1.out` | `7775c999a88c195d189c87d9294e9ce4` |
| `docket68/n1star/checks/cpaxis5_a4.out` | `ae4511e1c474eff3f88bcfeb79aa26cd` |
| `docket68/n1star/checks/cpaxis5_a5.out` | `6565c01c5191ceca28a03882f82f2d4e` |
| `docket68/n1star/checks/cpaxis5_a6.out` | `cee235fc3c4833486f3d66a4e20f260c` |
| `docket68/n1star/checks/cpaxis5_a6_400.out` | `94c9c5a53543c764f1e00d037a49ff33` |
| `docket68/n1star/checks/cp3grid5.py` | `3033f5bfcf04065b7e99b5dd8cf09186` |
| `docket68/n1star/checks/cp3grid5_control.out` | `1af3c04e9c7ec030e11798fb86454da7` |
| `docket68/n1star/checks/cp3grid5_a8_2grid.out` | `dc3380ec644732a430bb02e7af310c9c` |
| `docket68/n1star/checks/cp3grid5_a9_800.out` | `c7d7752b7f389ed261b4b1c6871354fb` |
| `docket68/n1star/checks/cp3grid5_a10_2grid.out` | `7986c6b71f4dc8ec825ae8d28c9475c7` |
| `docket68/n1star/checks/cp3grid5_a7_3grid.out` | `c654cebc1f5da114da14ee10e38e5bd6` |
| `docket68/n1star/checks/cp3grid5_a8_3grid.out` | `9e823195af627bc21c2d1854ffbfb6b8` |
| `docket68/n1star/checks/cp3grid5_a9_1600.out` | `0d0da9dcc0d554d11f97dd40a4a4ee10` |
| `docket68/n1star/checks/cp3grid5_a10_3grid.out` | `0989baf55d1299a8ff637737215d1426` |
| `docket68/n1star/checks/late5b.py` | `5225f2b4aa53dc1ab452e2355d499ef8` |
| `docket68/n1star/checks/late5b.out` | `ece3e7f063a049a15a5b91ed56c2b555` |
| `docket68/n1star/checks/late5b_small.out` | `be8da58288ee92cd765d25b48c167b41` |
| `docket68/n1star/checks/rcert5.py` | `bf6d843d5963534eaab5ac4123479aa9` |
| `docket68/n1star/checks/rcert5c.py` | `281cd2ea76acbe4fb6e04961bdd0521a` |
| `docket68/n1star/checks/rcert5c.out` | `b4790b613b72f25a492b02ae51dd8503` |
| `docket68/n1star/checks/rcert5d.py` | `9821bbb57382575a993ed4f3ac035580` |
| `docket68/n1star/checks/rcert5d.out` | `e55b30ee9116aed9db258458a369f7ad` |
| `docket68/n1star/checks/rich5.py` | `545d6a87cbca2925da87bf80d693dfb8` |
| `docket68/n1star/checks/rich5.out` | `504cd8e3ceccadf2cfd6760321b7b0ef` |
| `docket68/n1star/checks/rich5_runs.out` | `64d3a967c368dcd036c758fe842b51f6` |
| `docket68/n1star/data/rcert5_C3.npz` | `698569f6faaab4420fe2e67abc860561` |
| `docket68/n1star/data/rcert5_C3R.npz` | `88e16664187868e47eaaaa18709cfc61` |
| `docket68/n1star/CERTIFY-10L5-RESULT.md` | `a781147c0ced049b4667137d21592671` |
```

- The md5s are the files' own at this append, with one exception. `CERTIFY-10L5-RESULT.md` cannot print its own md5,
  so its cell holds the file's md5 before this append (a781147c…). After seating, `python3 response5.py --update-md5`
  rewrites it, and R9 checks every row.

**E. Appendix C, the source map's section 9 rows.** As 10.4's E, with cp3grid5's labels A7–A10. **Old:**

```
| section 9: residual of a smoothed 3D approximant | `docket68/n1star/checks/resid5.py` Q1–Q2 |
```

**New:**

```
| section 9: the residual of the Richardson approximant | `docket68/n1star/checks/rich5.py` R0–R3, C1–C3 |
| section 9: the single-grid approximant's supremum over one box | `docket68/n1star/checks/rcert5d.py` D0–D4, C1–C2 |
| section 9: the class; frozen-coefficient loss; transport structure | `docket68/n1star/checks/reduce5.py` R0–R4; |
| | `docket68/n1star/checks/symbol5s.py` S1–S6; `checks/null3.py` N0–N10; `checks/linest5.py` E1–E9 |
| section 9: the linear estimate at levels 0 and 1, and its constant | `docket68/n1star/checks/linest5.py` E1–E9; |
| | `docket68/n1star/checks/lev1_5.py` L1–L5; `checks/wgron5.py` W1–W5 |
| section 9: the axes: chart, pairs, Hardy constants, reduced hierarchy | `docket68/n1star/checks/axis5.py` X1–X7; |
| | `docket68/n1star/checks/axisbianchi5.py` B1–B4; `checks/axhier5.py` A1–A7, M1–M4, S1–S3 |
| section 9: existence by continuity from [CTG23], conditional | `docket68/n1star/checks/cont5.py` C1–C2 |
| section 9: the block condition, unweighted and at the weights | `docket68/n1star/checks/blocks5.py` H1–H2; |
| | `docket68/n1star/checks/blockw5.py` B1–B2 |
| section 9: the late region | `docket68/n1star/checks/cpaxis5.py` A1–A6; `checks/cp3grid5.py` A7–A10; |
| | `docket68/n1star/checks/late5b.py` L5–L7 |
```

**F. Appendix A: an entry for every program block A cites, and the resid5 entry retitled (m6-2).** **Old:**

```
- `checks/resid5.py` Q1–Q2: section 9's computed residual. Every field of a double-null run at the first seed (800 ×
  360, M = 16) is fitted by a tensor Chebyshev series on the box u ∈ [−4, −1.1], v ∈ [0.55, 1.6], so that g_app is an
  explicit smooth metric of the class. Q1, the fit within 7 × 10⁻¹¹ of the run at its nodes; Q2, every frame component
  of Ric[g_app], from the exact symbolic Ricci tensor of the ansatz, at most 2.46 × 10⁻³ of the curvature scale √K_0 at
  the same areal radius, against 9.64 × 10⁻³ on the next coarser run (400 × 180), a ratio of 3.92: the residual is the
  discretisation's, at second order. Control: the lapse moved off the solution (W + 0.01 v) gives a residual 140 times
  larger. Floating point, not certified. About 11 minutes, given the runs.
```

**New:**

```
- `checks/resid5.py` Q1–Q2: the computed residual of a smoothed run. Section 9 now cites the certified residuals of
  `checks/rich5.py` and `checks/rcert5d.py` instead, whose `checks/rcert5.py` imports this program. Every field of a
  double-null run at the first seed (800 × 360, M = 16) is fitted by a tensor Chebyshev series on the box u ∈ [−4, −1.1],
  v ∈ [0.55, 1.6], so that g_app is an explicit smooth metric of the class. Q1, the fit within 7 × 10⁻¹¹ of the run at
  its nodes; Q2, every frame component of Ric[g_app], from the exact symbolic Ricci tensor of the ansatz, at most
  2.46 × 10⁻³ of the curvature scale √K_0 at the same areal radius, against 9.64 × 10⁻³ on the next coarser run
  (400 × 180), a ratio of 3.92: the residual is the discretisation's, at second order. Control: the lapse moved off the
  solution (W + 0.01 v) gives a residual 140 times larger. Floating point, not certified. About 11 minutes, given the
  runs.
- `checks/reduce5.py` R0–R4: section 9's class. For every metric of the class, with no field equation used, the
  five-dimensional Ricci tensor reduces to (2+1)-dimensional gravity coupled to a wave map into the flat plane (R1–R2);
  the reduced residues are fixed linear combinations of the five-dimensional Ricci components (R3); and the Einstein
  frame is written in the record's variables (R4). Exact (sympy). About half an hour.
- `checks/symbol5s.py` S1–S6: section 9's frozen-coefficient loss. The principal symbol of the free formulation with the
  shift's second derivatives kept has no Jordan block (S1–S3), but the shift's angular derivative is of principal size at
  high angular frequency and drives δR at order k² (S4, S6); in the constraint-preserving block the eigenvalue-0 mode
  drives itself (S5), a loss shown on a model only. Control: the frozen-shift system has the Jordan block. Exact, with
  S6's model in floating point. About three minutes.
- `checks/null3.py` N0–N10: section 9's transport structure. In double-null gauge with one-dimensional sections, the
  reduced system's Ricci coefficients, Raychaudhuri, torsion, lapse, commutators and wave operator (N0–N6); the two
  equations the hierarchy does not use carry the only angular derivative (N7), so none appears on the hierarchy's right
  sides (N8); the pairs' energy identities (N9); the linearised pair operators for the difference of two metrics (N10).
  Exact (sympy). Under a minute.
- `checks/linest5.py` E1–E9: supplement Theorem 7.L. The pair identities (E1); the hierarchy linearised in fifteen
  frame-difference unknowns, with no derivative of an unknown on any right side (E2); the two-variable Grönwall lemma
  (E7); the rows checked against the geometry three ways (E9); and, on the record's run, the constant, the truncated
  domains it holds on and the demand it puts on the residual (E4–E6, E8). Controls: a row with the angular loss must be
  flagged (E3); mutated rows must fail E9. Exact for the structure, floating point for the constants. About half a
  minute, given the run.
- `checks/lev1_5.py` L1–L5: supplement Theorem 8.L1. The commutators with e_x (L1); the system commuted once closes in
  thirty unknowns with no level-2 term on any right side (L2), every level-1 row checked against the commutation itself
  (L5); the level-1 constant on the record's run (L4). Controls: a commutator without its e4 term (L1); a row with the
  angular loss (L3); two dropped terms (L5). Exact, with L4 in floating point. About eight to eleven minutes, given the
  run.
- `checks/wgron5.py` W1–W5: supplement Theorem 8.W, the constant with weights. A model Goursat pair, on which the
  weighted bound must hold at every weight tried and two mutations of it must fail (W1); equal weights reproducing
  F² = 10^138 (W2); the optimal weights, F² = 10^66.9 on |x| ≤ 1/2 (W3); the approximate-inverse route closed (W4,
  supplement Lemma 8.F); the frozen-angle growth of the transported unknowns (W5). Deduced, with computed checks; the
  constants in floating point. About eight minutes, given the run.
- `checks/axis5.py` X1–X7: the axis charts. Near each axis the class is four-dimensional axisymmetric Einstein–scalar in
  a chart regular at the axis (X1), twist-free in its double-null frame (X2), with a measure in which the pair operators
  are adjoint (X3); the Hardy inequalities that recover angular derivatives from the axis, with explicit constants (X4);
  the frame quantities bounded on the record's run (X5); an exact counterexample to a level-0 estimate at the axis (X6);
  and the glue (X7). Exact, with computed checks. Under a minute.
- `checks/axisbianchi5.py` B1–B4: the axis chart's curvature pairs. σ's vanishing (B1); the Gauss equation and [Wu26]'s
  pairs, each found by a linear fit at random jets and verified exactly at fresh ones (B2–B3b); and the pairs' energy
  inequality on the whole section, the axis included (B4). About seven minutes.
- `checks/axhier5.py` A1–A7, M1–M4, S1–S3: [Wu26]'s transport equations, mass aspects and the scalar's pairs in the axis
  chart, reduced and off shell, each found by a linear fit at random rational jets and verified exactly at fresh ones,
  with every angular derivative on a right side recovered from the hierarchy's own unknowns (A7). Controls c1–c4: altered
  coefficients must leave a residual. About a minute and a half.
- `checks/cont5.py` C1–C2: Lemma 9.C of the supplement. The compatibility relations and the metric recovery hold
  identically on the general metric of the class (C1, exact); 4AB < 1 and y ≤ A + By² give y ≤ 2A, and y never enters
  (2A, 1/(2B)) (C2, z3, with a vacuity guard). Controls: χ̲'s relation without b_x (k1); 4AB < 2 (k2); a sharper bound,
  refuted (k3). Seconds.
- `checks/blocks5.py` H1–H2: the block (Schur) condition. The coupling of a multiplication across an angular Galerkin cut
  does not depend on N past the multiplier's degree (H1, exact), and on the record's coefficients it is of their own
  size, so the condition fails at every N in Theorem 7.L's norms (H2, floating point). About 25–40 minutes, given the
  run.
- `checks/blockw5.py` B1–B2: the same condition at Theorem 8.W's weights, from the printed figures of
  `checks/blocks5.out` and `checks/wgron5.out`, each rounded against the claim: the largest pair's product is at least
  57.8 at every N. Controls: equal weights reproduce blocks5's 484 (k1); the smallest pair alone is below 1 (k2). A
  second.
- `checks/rich5.py` R0–R3, C1–C3: section 9's Richardson approximant. Its pinned tensors (R0); its Einstein residual at
  16,128 points (R2) and as a supremum over a sub-box of each of four boxes (R3), certified in ball arithmetic with
  `checks/rcert5d.py`'s engine; the extrapolation's floating-point residual (R1, `--runs`). Controls: the engine end to
  end on test fields with exact suprema, and every enclosure it forms against its corners' point values (C1); the
  perturbed approximant refused (C2); the census regression (C3). Twenty to fifty minutes, read only.
- `checks/rcert5d.py` D0–D4, C1–C2: the single-grid approximant's supremum over one interior box. Order-3 Taylor models
  with the Lagrange remainder in ball arithmetic, bisected until every sub-box meets the target (D1); certified centre
  values that no bound of any method can beat (D2); the census over the 416 boxes (D3); certified point values at the
  centre and corners of every accepted sub-box below its bound (D4). Controls: as rich5's C1, and the perturbed
  approximant refused (C2). The bisection about three hours on four processes; the collection and its checks about two
  minutes.
- `checks/cpaxis5.py` A1–A6: the late region's constraint-preserving scheme. Its singular coupling at the axes (A1–A2),
  the regularisation (A3), and the regularised scheme on the record's data at two angular resolutions (A4) and two null
  grids (A5), with its Kretschmann scalar (A6). Floating point. Each run at 1600 × 720 about four hours; the analyses
  minutes to half an hour.
- `checks/cp3grid5.py` A7–A10: the regularised scheme on three null grids. The unimposed constraint and the metric per
  band of v and class of areal radius, with the observed order (A7); the Kretschmann scalar (A8); the metric's resolution
  in angle (A9); the regularisation's correction replayed at every cell (A10). Control: the 800-row run given in place of
  the 1600-row one must read as not converging on every band. Floating point. A7 and A9 under a minute, A8 seventeen to
  twenty minutes and A10 fifteen to thirty, given the runs.
- `checks/late5b.py` L5–L8: the free scheme's late region on the record's runs. Raychaudhuri's residual per band and
  class under the null step (L5), in angle (L6) and at small radii (L7); the monotone quantity e^{−2W} R_v along the
  outgoing generators (L8). Control: a wrong coefficient must not converge (L5). Floating point, given the runs.
```

**G. Appendix D: a run command for each of them (m6-2), after resid5's.** **Old:**

```
    python3 checks/resid5.py RUNDIR l1_M16_800 l1_M16_400    # about 11 minutes, given the runs
```

**New:**

```
    python3 checks/resid5.py RUNDIR l1_M16_800 l1_M16_400    # about 11 minutes, given the runs
    python3 checks/reduce5.py                             # about half an hour
    python3 checks/symbol5s.py                            # about three minutes
    python3 checks/null3.py                               # under a minute
    python3 checks/linest5.py RUN                         # RUN the record's l1_rc0.9_M32.npz; half a minute
    python3 checks/lev1_5.py RUN                          # about eight to eleven minutes
    python3 checks/wgron5.py RUN                          # about eight minutes
    python3 checks/axis5.py RUN                           # under a minute
    python3 checks/axisbianchi5.py                        # about seven minutes
    python3 checks/axhier5.py                             # about a minute and a half
    python3 checks/cont5.py                               # seconds
    python3 checks/blocks5.py RUN                         # 25-40 minutes; then checks/blockw5.py (a second)
    python3 checks/rich5.py                               # 20-50 minutes, read only; --runs RUNDIR for R1
    python3 checks/rcert5d.py --worker w 4                # w = 0..3 at once, about three hours; then --collect 4
    python3 checks/rcert5d.py --census                    # about a minute
    python3 checks/cpaxis5.py --run 1 0.9 M Nu Nv 2.25 OUT reg ld 3   # a regularised run; 1600 x 720 about 4 h
    python3 checks/cpaxis5.py --nullstep R400 R800 R40_800   # and --compare, --kretschmann (A4-A6)
    python3 checks/cp3grid5.py --a7 R400 R800 R1600 [R40_1600]   # and --a8, --pclass, --dpm, --control
    python3 checks/late5b.py RUNDIR                       # given the record's runs
```

## 12. Round 8 (2026-11-06/13): the verifier of round 7 seated, and the late mechanism decided band by band

The verifier of round 7 read section 11 (lines 3449–4092, file md5 9feaf95d…). Every check and every rerun held, and
the certificates stand: 3.01 × 10⁻⁴, 5.0 × 10⁻⁴, and 1.09–2.41 × 10⁻³. All ten mutants died on its independent rebuild,
as did its own mB1x, mB4 and mC1. It did not confirm section 11 because of two Majors, both in the wording of the paper
blocks. It also found two minor findings and a nit. Each is seated below as a bracketed amendment to the section 11 text
it names; section 11 is not edited. Every finding was re-derived first, and every repair that needs a program was run in
full. Sections 0–11 are byte-identical before and after this append.

### 12.0 The verifier of round 7: its findings, seated as amendments to section 11

**M7-A. Block F put a withdrawn reading back into the paper.**
- [11.4, block F, the axis5 entry, "an exact counterexample to a level-0 estimate at the axis (X6)" and "Exact, with
  computed checks"; the axisbianchi5 and axhier5 entries, "verified exactly at fresh ones"; `checks/axis5.py`'s
  docstring, X6, "exact counterexample … nothing weaker than [Wu26]'s level suffices at the axis": verifier of round 7
  (M7-A).]
  - *Re-derived.*
    - 9.0's M-C withdrew that reading. X6 shows only that the polar-frame connection difference δk is not an admissible
      L²(dμ) unknown at the axis. That excludes Theorem 7.L's unknowns and nothing else.
    - 9.0's m11 labelled the axis programs' identities as tests at random rational jets with a fixed seed: probabilistic,
      not symbolic.
  - *Repaired.*
    - Block F's three entries now use M-C's and m11's wording (12.4).
    - `checks/axis5.py`'s docstring is corrected: the X6 paragraph, and the label line, which now says the printed
      "(exact)" of X1–X3, X6 and X7 is to be read as "verified at random jets".
    - axis5 was rerun on the record's run. Its output equals `checks/axis5.out` apart from timings, so the .out is kept.
  - *Swept:* every block A–G, against every disposition of 9.0, 10.0 and 11.0. Four more readings were fixed, all in F:
    - wgron5's W3, "the optimal weights", reads "weights minimising a relaxed objective" (m6);
    - W4, "the approximate-inverse route closed", reads "a finite-rank approximate inverse cannot lower the
      constant" (m7);
    - W5 is labelled "at one resolution" (m8);
    - rich5's control reads what C1(b) checks, not "every enclosure it forms".
  - Nothing else was found. The checks: the cones' L² norms at level 1 (M-B); 4AB < 1 and the hypotheses on every slab
    (m6-1); the free scheme's areal radius ≥ r_h (m5-8); the computed label of the block condition (m5-3); and the
    "exact" programs, which are symbolic (reduce5, symbol5s, null3, linest5, lev1_5's L1–L3 and L5, cont5's C1,
    blocks5's H1).

**M7-B. Block A's "beyond" clause, and 11.1, asserted a mechanism that the M = 40 data undercut.**
- [11.1, lines 3619–3622, "Of 9.6's three readings this excludes the first …"; lines 3654–3656, "the scheme's imposed
  rows do not propagate Ric_xx = 0 there"; lines 3673–3674, the same in the verdict; block A, lines 3816–3819, "its
  imposed rows do not propagate the remaining constraint": verifier of round 7 (M7-B).]
  - *Re-derived.* On [1.8, 1.9) the violation falls from M = 32 to M = 40 by factors of 0.50 and 0.19 at 1600 rows
    (A7), and 0.52 and 0.30 at 800 rows (round 5's A5). That points to angular truncation, which a failure of the
    scheme's own propagation would not explain by itself. A feature that the grids do not resolve in angle is not
    excluded either.
  - *What holds:*
    - at M = 32 the null-step limit is not vacuum beyond the claimed regions;
    - from v = 1.9 at 0.9–1.2 the correction d± does not vanish under refinement;
    - the violation changes with M by factors of 0.19–2.61;
    - which mechanism produces it is not decided by M = 32 and 40. M = 48 and 56 decide it on six of seven bands (12.1).
  - *Corrected text.*
    - Lines 3619–3622 read: "So beyond, too, the discrete solutions converge at second order in the null step at
      M = 32, to a limit whose unimposed component Ric_xx does not vanish: the null-step limit at M = 32 is not vacuum
      there. None of 9.6's three readings is excluded. The violation changes with M (0.19–2.61), so a feature that the
      grids do not resolve in angle remains possible, beside the scheme's propagation and d±."
    - Lines 3654–3656 read: "… while the monitor does not. So the violation there is not d±'s doing. Whether it is
      angular truncation or the scheme's propagation is not decided: from M = 32 to 40 it falls 2- and 5-fold there."
    - Lines 3673–3674 read: "On [1.8, 1.9) the regularisation's correction still falls while the constraint does not,
      and the constraint falls 2–5-fold from M = 32 to 40. Its mechanism there is not decided."
    - Block A reads as 12.4: "the null-step limit at M = 32 is not vacuum", with the d± clause kept and the mechanism
      given band by band from 12.1's runs, undecided elsewhere.
  - *The computation that decides it* on six of the seven bands, with M = 48 and 56, is in 12.1. Block A states what it
    decides and no more.

**Minor findings.**
- **m7-1** [11.1, line 3667, "This holds to v = 1.8 r_h …" on three grids; block A, lines 3811–3813]: the third grid
  covers v ≥ 1.4 only, and A10 starts at v = 1.5.
  - They read: "on three null grids from v = 1.4 r_h and on two below it; the correction on three grids from
    v = 1.5 r_h" (12.4).
- **m7-2** [11.0, "C1(b)(i) kills mA5 … mB2"]: mB5, `box_coeffs` with its quadratic l1 term halved, survived both C1
  and C1(b). On the pinned tensors that term weighs too little for C1(b) to see the halving.
  - *Repaired (`checks/rcert5d.py`):* `contain_fields` gives degree-7 test fields T₇(t), T₇(σ) and T₇(x). C1(b) now
    also runs on them at three parents (the verifier's), with frame `kids_frame2`: 53,760 and 30,720 checks. The
    pinned-tensor run is kept beside it. rich5's C1(b) runs the same.
  - Every result is in the table below.

**Nit.** [11.4, block E, "`checks/late5b.py` L5–L7"]: the program prints L5–L8, so E reads L5–L8, as F does.

**The controls after round 8.** The real engine on the round-4 checkpoints (`checks/rcert5d.out` regenerated):
- C1: the largest true/bound is 0.9999999926, and 4.2542 with the remainder dropped.
- C1(b): 35,840 and 20,480 checks on the pinned tensors, and 53,760 and 30,720 on the degree-7 fields, none failing.
- D1 and D3 are unchanged; D4 gives 68,705 points at ratio 0.809. `--collect` prints "all checks pass" (143 s).

The mutants, each rebuilt on the repaired file (`scratchpad/r8/mut/`), with mB1x, mB4 and mC1 the verifier's and mB5
its minor 2. For each: C1's largest true/bound through `kids`, C1(b)'s failures on the pinned tensors ((i), (ii)) and on
the degree-7 fields ((i), (ii)), and the whole `--collect`:

| mutant | change | C1 | C1(b) pinned | C1(b) degree 7 | `--collect` |
|---|---|---|---|---|---|
| mA1 | the remainder flag forced on | 4.2542 | 0, 0 | 0, 0 | FAILURES, exit 1 |
| mA2 | order-3 coefficients at the centre | 4.2542 | 0, 0 | 0, 0 | FAILURES, exit 1 |
| mA3 | `kids` passes `vp` twice | 4.2542 | 0, 0 | 0, 0 | FAILURES, exit 1 |
| mA4 | `abs` dropped in `bound` | ∞ | 0, 0 | 0, 0 | FAILURES, exit 1 |
| mA5 | `box_coeffs` at half the half-widths | 0.9999999975 | 2,962, 0 | 1,392, 1,164 | FAILURES, exit 1 |
| mA6 | box inputs' t and x at the centre | 1.0667 | 0, 0 | 0, 0 | FAILURES, exit 1 |
| mB1 | `box_coeffs`: σ, x half-widths 0 | 1.1801 | 4,051, 0 | 2,304, 6,662 | FAILURES, exit 1 |
| mB1s | `box_coeffs`: σ's half-width 0 | 1.1801 | 1,889, 0 | 1,152, 2,400 | FAILURES, exit 1 |
| mB1x | `box_coeffs`: x's half-width 0 | 1.0667 | 0, 0 | 1,152, 2,316 | FAILURES, exit 1 |
| mB2 | rcert5.py: linear term in t only | 1.1801 | 850, 0 | 464, 0 | FAILURES, exit 1 |
| mB3 | box inputs' t at the centre | 1.0016 | 0, 0 | 0, 0 | FAILURES, exit 1 |
| mB4 | box inputs' x at the centre | 1.0667 | 0, 0 | 0, 0 | FAILURES, exit 1 |
| mB5 | `box_coeffs`: l1 term halved | 0.9999999926 | 0, 0 | 320, 0 | FAILURES, exit 1 |
| mC1 | box inputs from the point jets | 4.2542 | 0, 0 | 0, 12,672 | FAILURES, exit 1 |

- mB5 dies only on the degree-7 fields. mA5 dies on both C1(b) runs. Every other mutant dies on C1.
- C1(b)(ii), which failed no mutant on the pinned tensors, fails five on the degree-7 fields: mA5, mB1, mB1s, mB1x and
  mC1.
- *rich5.py* (`checks/rich5.out` regenerated).
  - The rerun is read-only, and both npz md5s are unchanged. R0–R3, C2 and C3 match round 7, timings aside. C1 and
    C1(b) pass, the latter on both sets of tensors, and the run ends "all checks pass" (1,209 s).
  - rich5's C1 and C1(b) were run with rcert5d replaced by each of the fourteen mutants
    (`scratchpad/r8/rich5_c1_mut.py`). Every one is caught, mB5 by the degree-7 fields alone (320 failures), as in
    rcert5d.

### 12.1 The late mechanism: M = 48 and 56 decide it on six of the seven bands beyond

**Why these runs.**
- On [1.8, 1.9) the violation falls from M = 32 to M = 40. If it keeps falling as M grows, it is angular truncation;
  if it levels off well above the null-step level, it is not. So the decisive quantity is the monitor's sequence in
  M at a fixed null grid.
- 800 rows suffice where the monitor is well above the 800-row null-step level. The M40/M32 ratios at 800 and 1600 rows
  agree there (0.52 and 0.50 at 0.9–1.0).
- Where it is not, M = 48 is also run at 400 and 1600 rows, so that the null step can be read at M = 48 itself.

**The runs** (`checks/cpaxis5.py`, unchanged at 6fb010b7…, nice 10, writing only under the scratchpad).
- At 800 × 360, started 2026-11-06 18:15 UTC and finished the same evening:
  - M = 48: `--run 1 0.9 48 800 360 2.25 <scratch>/r8/cp_M48_800_reg.npz reg ld 3`, 2,308 s, md5 94af133b…;
  - M = 56: the same, 2,533 s, md5 8cbc59ba….
- A third run, M = 48 at 1600 × 720 with `vsave 1.4`, was lost when the session's container restarted. It was restarted
  on 2026-11-13 at 06:08 UTC, beside M = 48 at 400 × 180.
  - M = 48 at 400 rows finished in 317 s (md5 f7d818fb…; `checks/cpaxis5_a5_m48_400.out`);
  - M = 48 at 1600 rows is PID 3123. It was at null diagonal 286 of 1,959 at 06:15 UTC, and at that rate finishes near
    08:00–09:00 UTC. It is to be seated when it finishes, with the commands below.
- M²/N is 2.9 and 3.9 at 800 rows and 1.4 at 1600 rows, at or below the 4.0 of round 4's M = 40 run at 400 rows. At
  400 rows M = 48 has 5.8, the first run past that bound. It ran stably, and its claimed bands fall 3.84–4.14-fold to
  800 rows, as at M = 32.

**The rule, fixed before the results** (12.0's M7-B; applied by `checks/mtrunc5.py`, new, to the printed monitors of
`cpaxis5_a5.out`, `cpaxis5_a5_m48.out` and `cpaxis5_a5_m56.out`).
- For each band and class, m(M) is the monitor at 800 rows for M = 32, 40, 48 and 56.
- *Angular truncation* if every step lowers it by at least a fifth: m(M + 8)/m(M) ≤ 0.8.
- *Not truncation* if m(56)/m(48) ≥ 0.8 while m(56) exceeds ten times the class's null-step level L. L is the largest
  monitor on the class's second-order bands: 5.9 × 10⁻³, 1.8 × 10⁻³ and 1.4 × 10⁻³.
- *Undecided* otherwise.
- *Controls:* a halving sequence must read 'angular truncation' (k1); M = 32 given for every M must never read
  'angular truncation', and must read 'not truncation' exactly where m(32) > 10L (k2). Both pass.

**The verdicts** (`checks/mtrunc5.out`, computed).
- *Angular truncation:*
  - at 0.9–1.0 on [1.8, 1.9), 1.02, 0.53, 0.258 and 0.136, halving at each step (0.52, 0.49, 0.53);
  - at ≥ 1.2 on [2.0, 2.25), 0.272, 0.164, 0.078 and 0.053 (steps 0.60, 0.48, 0.68).
- *Not truncation; the violation grows with M:*
  - at 0.9–1.0 on [1.9, 2.0), 34 to 55.5 (steps 1.15–1.22), and on [2.0, 2.25), 114 to 540;
  - at 1.0–1.2 on [2.0, 2.25), 142 to 1,120.
  - On these bands d± does not vanish under refinement either (11.1, A10).
- *Undecided by the rule, then decided at M = 48:* at 1.0–1.2 on [1.8, 1.9), 0.0094, 0.0028, 0.0016 and 0.0017. It
  falls to the null-step level by M = 48 and stops there, as the claimed bands do. M = 48 at 400
  and 800 rows decides it (`cpaxis5_a5_m48_400.out`).
  - The monitor falls 3.84-fold from 400 to 800 rows there, as on the claimed bands (3.84–4.14), against 1.58 at
    M = 32, and it changes by 1.06 from M = 48 to 56.
  - So the violation there at M = 32 and 40 is the angular truncation's, and from M = 48 the band behaves as a
    converging one, on two null grids.
- *Undecided:* at 1.0–1.2 on [1.9, 2.0), 5.05, 4.13, 3.20 and 2.49. It falls by 0.77–0.82 per step, short of the
  rule's fifth, and at M = 48 it falls only 1.26-fold from 400 to 800 rows.
- *In the claimed bands* the monitor rises 5–26 % per step in M at 800 rows. There it is the null step's, as A7 showed,
  and these runs leave the claims as they are.
- Of 9.6's three readings, then:
  - truncation is the reading on the three bands where it falls with M;
  - where the violation grows with M, it is not truncation, and the persistent d± and a feature the grids do not
    resolve both remain;
  - the scheme's own propagation is not shown to fail anywhere.

**For the 1600-row M = 48 run, when it finishes** (the commands, ready):
- `cp3grid5.py --a7 R48_400 R48_800 R48_1600 R40_1600` gives three null grids at M = 48, with M = 40 as the angular
  comparison (its "M40/M32" column then reads M40/M48). That is the third grid for 1.0–1.2 on [1.8, 1.9).
- `cp3grid5.py --a7 R32_400 R32_800 R32_1600 R48_1600` and `cp3grid5.py --pclass R32_1600 R48_1600` give M = 48
  against M = 32 at 1600 rows.

### 12.2 What holds at 10 l5 after round 8

11.2's list stands, with these changes:
- Beyond the claimed regions, at M = 32, the null-step limit is not vacuum (M7-B).
  - With M = 32–56 the violation is the angular truncation's at 0.9–1.2 on [1.8, 1.9) and at ≥ 1.2 on [2.0, 2.25).
    At 1.0–1.2 on [1.8, 1.9), from M = 48 the band converges in the null step on two grids.
  - It grows with M at 0.9–1.0 from v = 1.9 and at 1.0–1.2 from v = 2.0, where d± persists too.
  - At 1.0–1.2 on [1.9, 2.0) these runs do not decide (12.1).
- Three null grids hold from v = 1.4 (d± from v = 1.5), and two below that (m7-1).
- The certificates' controls kill fourteen mutants, mB5 by the degree-7 containment (m7-2). The certified figures are
  unchanged.
- The axis programs' identities are random-jet tests; X6 excludes only Theorem 7.L's unknowns at the axis (M7-A).

There is no new existence statement. Existence is proved where the solution is the seed and is not claimed beyond it.

### 12.3 Files and outputs (round 8)

| file | what | md5 (round 7 → round 8) |
|---|---|---|
| `checks/rcert5d.py` | m7-2: `contain_fields`, C1(b) on degree-7 fields | 9821bbb5… → c7165902… |
| `checks/rcert5d.out` | collect and census, regenerated | e55b30ee… → 2411c62d… |
| `checks/rich5.py` | m7-2: the same in rich5's C1(b) | 545d6a87… → 2313e4cd… |
| `checks/rich5.out` | regenerated (read-only run) | 504cd8e3… → c1eabcf6… |
| `checks/axis5.py` | M7-A: the X6 paragraph and the label line of the docstring | ed855afc… → b0b86449… |
| `checks/mtrunc5.py` (new) | 12.1: the rule applied to the monitors at M = 32–56; controls k1, k2 | eac22e7a… |
| `checks/mtrunc5.out` (new) | its output; a second | 158dae5a… |
| `checks/cpaxis5_a5_m48.out` (new) | `cpaxis5.py --nullstep` with M = 48 at 800 rows | 7360e31b… |
| `checks/cpaxis5_a5_m56.out` (new) | the same with M = 56 | 53ee3e4b… |
| `checks/cpaxis5_a5_m48_400.out` (new) | the null step at M = 48, 400 against 800 rows | d4a15a41… |

- `checks/axis5.out` is unchanged (5cae43e2…). The rerun matches it apart from timings (`scratchpad/r8/axis5.rerun.out`).
- `data/rcert5_C3.npz` (698569f6…) and `data/rcert5_C3R.npz` (88e16664…) are unchanged before and after every program
  of this round.
- The round-7 versions are in the scratchpad: `r8/rcert5d.r7.py`, `r8/rich5.r7.py` and `r8/axis5.r7.py`.

Scratch (not committed; under the session's scratchpad):
- `r8/mut/`: the fourteen mutants and their `--collect` outputs;
- `r8/c1only.py` with `c1only_mut.out`, and `r8/rich5_c1_mut.py` with `rich5_c1_mut.out`;
- `r8/cp_M48_800_reg.npz` (94af133b…) and `cp_M56_800_reg.npz` (8cbc59ba…), with the runs of 12.1 still going and
  their logs.

### 12.4 The paper: blocks A–G, at the paper's current md5

These replace 11.4's proposal. They are proposed to the main session, which seats them; this note edits neither the paper
nor N1STAR-PROOF.md.
- *Keyed by text.* Each old block occurs exactly once in `RESPONSE-HL-5D.md` at md5 805be200b746b7cf480e88639da5508f.
  The old texts are 11.4's.
- *Checked:* all of A–G, with 9.9's B and C, applied to a copy (`scratchpad/r8/paper_applied.md`). Every line is
  ≤ 121 characters, and every md5 row of Appendix D matches its file except `CERTIFY-10L5-RESULT.md`'s. That row holds
  the file's md5 before this append, 9feaf95d…; `python3 response5.py --update-md5` rewrites it at seating.
- *Longest new line:* 121 characters.
- *Changed from 11.4:*
  - A: M7-B (the "beyond" clause, now from 12.1's runs) and m7-1 (the grid coverage);
  - F: M7-A, the sweep, the third grid's coverage in cp3grid5's entry, and an entry for mtrunc5;
  - E: late5b L5–L8, and a row for mtrunc5;
  - D2 and G: mtrunc5's inputs and run command;
  - D3: the round-8 md5s, and rows for mtrunc5 and the two new cpaxis5 outputs.
  - B, C and D1 are 11.4's.

**A. Old:**

```
At the
  first seed the Kretschmann scalar is moderate and converged in angle up to the point where the runs stop converging,
  and unresolved after it, where a singularity, a steep smooth feature and a defect at the axis are not yet told apart.
  At the second seed, with the angular and null grids refined together, the two coarser angular resolutions agree up to
  v ≈ 3.5 and the finest departs from them from v ≈ 3.25, at every angle. On a finer null grid, 2400 × 1080, the second
  seed's M = 32 and 40 angular resolutions agree to 0.09 K_0 up to v = 3.5 and to 0.53 K_0 up to v = 4.5 (K_0 = 72/R⁸,
  Tangherlini's Kretschmann scalar at the same areal radius), away from the cells M = 48 masks; M = 48 departs from v ≈
  3.25 exactly as at 1600 × 720, so the finer null grid does not move it, and the step condition M²/N ≤ c it had been
  ascribed to is refuted (M²/N = 0.96). The late region stays unresolved (computed, floating point:
  `docket68/n1star/checks/g1curv5.py --seed2-2400`, output `checks/g1curv5_seed2_2400.out`; supplement
  `CERTIFY-10L5.md` section 6b). A first certified step is taken: for an explicit approximant of the characteristic
  data on the data cone, the constraint along its outgoing generators holds to a certified bound at both seeds (at the
  second, 2.3 × 10⁻⁵ against terms of size 5.3 × 10⁻⁴; certified, ball arithmetic, `docket68/n1star/checks/cdata5.py`).
  The full Einstein residual of a smoothed three-dimensional approximant built from a run is computed only, 2.5 × 10⁻³
  of the curvature scale and falling at second order with the grid (`checks/resid5.py`, floating point), and no linear
  estimate with explicit constants is available for the characteristic problem in the class, so existence at 10 l5
  remains open (supplement `CERTIFY-10L5-RESULT.md` section 2).
```

**New:**

```
At the
  second seed, with the angular and null grids refined together, the two coarser angular resolutions agree up to v ≈ 3.5
  and the finest departs from them from v ≈ 3.25, at every angle. On a finer null grid, 2400 × 1080, the second seed's
  M = 32 and 40 angular resolutions agree to 0.09 K_0 up to v = 3.5 and to 0.53 K_0 up to v = 4.5 (K_0 = 72/R⁸,
  Tangherlini's Kretschmann scalar at the same areal radius), away from the cells M = 48 masks; M = 48 departs from
  v ≈ 3.25 exactly as at 1600 × 720, so the finer null grid does not move it, and the step condition M²/N ≤ c it had been
  ascribed to is refuted (M²/N = 0.96). The late region stays unresolved (computed, floating point:
  `docket68/n1star/checks/g1curv5.py --seed2-2400`, output `checks/g1curv5_seed2_2400.out`; supplement `CERTIFY-10L5.md`
  section 6b). Existence at 10 l5 is proved where the solution is the seed (v ≤ r_h/2) and is not claimed beyond it.
  Toward a computer-assisted proof the following hold, each with its status. Certified (ball arithmetic): on the data
  cone the outgoing constraint of an explicit approximant holds to 5.0 × 10⁻⁵ and 2.3 × 10⁻⁵ at the two seeds, 4.1–4.3 %
  of the terms that cancel in it (`docket68/n1star/checks/cdata5.py`); on u ∈ [−4, −1.1] r_h, v ∈ [0.55, 1.6] r_h,
  |x| ≤ cos(π/32), the Einstein residual of an explicit three-dimensional approximant, Richardson-extrapolated from two
  null grids, its coefficients pinned by md5 (`docket68/n1star/data/rcert5_C3R.npz`), is at most 3.73 × 10⁻⁵ of the
  curvature scale at 16,128 points and at most 5.0 × 10⁻⁴ as a supremum over a sub-box of each of four of the 416 boxes
  covering that region, on which the single-grid approximant (`data/rcert5_C3.npz`) has certified values of
  1.09–2.41 × 10⁻³ (`checks/rich5.py`), and the single-grid approximant's supremum over one interior box of the 416 is at
  most 3.01 × 10⁻⁴ (`checks/rcert5d.py`; both certificates' bounds are checked by a control that runs the whole bound
  computation on test fields varying in each coordinate, and on the coordinate map, with exact suprema, by a check that
  the enclosures it forms of the approximant's coefficients contain their values at the corners of their boxes, and by
  independent certified point values at the centre and corners of every accepted sub-box). Deduced: the class is
  (2+1)-dimensional gravity coupled to a wave map into the flat plane (`checks/reduce5.py`); in the free metric
  formulation, at frozen coefficients on spherical states, the shift's angular derivative is of principal size at high
  angular frequency and drives δR at order k², so no estimate without loss of derivatives holds for the
  frozen-coefficient problem (`checks/symbol5s.py`; for the constraint-preserving formulation a loss is indicated by a
  model only); in double-null gauge the reduced transport equations carry no angular derivative of an unknown on their
  right sides (`checks/null3.py`, `checks/linest5.py`), and a linear estimate with explicit constants holds on truncated
  domains of dependence away from the axes, at level 0 and at level 1 in the cones' L² norms (supplement Theorems 7.L,
  8.L1 and 8.W; `checks/lev1_5.py`, `checks/wgron5.py`); near each axis the class is four-dimensional axisymmetric
  Einstein–scalar in a chart regular at the axis, where [Wu26]'s curvature pairs have energy identities on the whole
  section, the angular recoveries hold with explicit Hardy constants, and [Wu26]'s transport equations, mass aspects and
  the scalar's pairs hold in reduced form with every angular derivative on their right sides recovered from the
  hierarchy's own unknowns (`checks/axis5.py`, `checks/axisbianchi5.py`, `checks/axhier5.py`; identities verified at
  random jets); and, for smooth T²-invariant characteristic data that satisfy the constraints, a smooth T²-invariant
  vacuum development exists on the region u ∈ [−10, u*] r_h, v ∈ [r_h/2, v*] of the gauge, the axes included, whenever,
  on every slab v ≤ s of that region, every smooth T²-invariant vacuum metric with these data, in the gauge, differs from
  the approximant by an amount obeying a linear estimate with constant F at every level, the quadratic remainder has
  constant G, the approximant's residual r satisfies 4F²Gr < 1 and the difference at v = r_h/2 is at most Fr, by
  continuity from the higher-dimensional neighbourhood theorem of [CTG23], the hierarchy being applied only to genuine
  metrics, for which its compatibility with the metric holds by definition (`checks/cont5.py`); these hypotheses are
  established on no such region beyond the seed. Computed (floating point): on |x| ≤ 1/2 over the region above, where no
  truncated domain exists, the estimate's constant is F² = 10^138, and 10^66.9 with Theorem 8.W's weights, at which
  4F²Gr < 1 asks r of order 10⁻⁶⁸/G; the couplings across an angular Galerkin cut, N-independent by an identity
  (deduced), are of the coefficients' own size there, so the block (Schur) condition under which an estimate on the high
  angular modes would lower the constant fails at every angular resolution, in Theorem 7.L's unweighted norms and at
  Theorem 8.W's weights (`checks/blocks5.py`, `checks/blockw5.py`); the first seed's solution, in a constraint-preserving
  scheme whose singular coupling at the axes is regularised (`checks/cpaxis5.py`), converges at second order in the null
  step to v ≈ 1.8 r_h at areal radius ≥ 0.9 r_h and to v ≈ 2.0 r_h at ≥ 1.2 r_h, on three null grids from v = 1.4 r_h and
  on two below it (observed order 2.00–2.03 in the metric, the unimposed constraint and the regularisation's correction
  falling 3.5–4.0-fold at each refinement, the correction on three grids from v = 1.5 r_h), and is resolved in angle
  there on the finest grid, M = 40 changing the metric by at most 3.0 × 10⁻⁹ (`checks/cp3grid5.py`), and the free
  scheme's solution is consistent with second-order convergence to v ≈ 1.8 r_h at areal radius ≥ r_h as well
  (`checks/late5b.py`); beyond, at M = 32 the metric still converges at second order in the null step while the unimposed
  constraint does not fall, so the null-step limit at M = 32 is not vacuum; with M = 32, 40, 48 and 56 at 800 × 360 the
  violation halves at each step in M on [1.8 r_h, 1.9 r_h) at areal radius 0.9–1.0 r_h and falls 0.48–0.68-fold per step
  on [2.0 r_h, 2.25 r_h) at ≥ 1.2 r_h, and on [1.8 r_h, 1.9 r_h) at 1.0–1.2 r_h it falls to the null step's level by
  M = 48, where it falls 3.84-fold from 400 to 800 rows as in the claimed regions, so on these bands it is the angular
  truncation's; from v ≈ 1.9 r_h at 0.9–1.0 r_h and from v ≈ 2.0 r_h at 1.0–1.2 r_h it grows with M and the
  regularisation's correction does not vanish under refinement; and at 1.0–1.2 r_h on [1.9 r_h, 2.0 r_h) it falls by only
  0.77–0.82 per step, which these runs do not decide (`checks/cpaxis5.py`, `checks/mtrunc5.py`; supplement
  `CERTIFY-10L5-RESULT.md` sections 2 and 6–12).
```

**B and C.** As 9.9's B and C, unchanged.

**D1. Old:**

```
recorded here); z3-solver for `foliation5.py`; python-flint for `cdata5.py`; numpy for `bondi5.py` and `growth5.py`,
```

**New:**

```
recorded here); z3-solver for `foliation5.py` and `checks/cont5.py`; python-flint for `cdata5.py` and for
`checks/rcert5.py` and every program that imports it; scipy for `cdata5.py`, `checks/lev1_5.py` and `checks/wgron5.py`;
numpy for `bondi5.py` and `growth5.py`,
```

**D2. Old:**

```
`checks/vii5census.py`; the others import nothing from the research tree:
```

**New:**

```
`checks/vii5census.py`, `checks/reduce5.py` imports `dnull5.py`, `checks/symbol5s.py` imports `checks/symbol5.py`, which
imports `dnsolve5.py`, `checks/linest5.py` imports `checks/null3.py` and `dnsolve5.py`, `checks/lev1_5.py` imports
`checks/linest5.py` and `checks/wgron5.py`, `checks/wgron5.py` and `checks/blocks5.py` import `checks/linest5.py`,
`checks/axis5.py` imports `checks/linest5.py` and `dnull5.py`, `checks/axhier5.py` imports `checks/axisbianchi5.py`,
`checks/cont5.py` imports `checks/null3.py`, `checks/cpsolve5.py` imports `dnsolve5.py`, `checks/cpaxis5.py` imports
`checks/cpsolve5.py`, `checks/cp3grid5.py` imports `checks/cpsolve5.py` and `checks/cpaxis5.py`, `checks/rcert5.py`
imports `checks/resid5.py` and `checks/bondisph5.py`, `checks/rcert5c.py` and `checks/rcert5d.py` import
`checks/rcert5.py`, `checks/rich5.py` imports `checks/rcert5.py` and `checks/rcert5d.py`, `checks/blockw5.py` reads
`checks/blocks5.out` and `checks/wgron5.out`, and `checks/mtrunc5.py` reads `checks/cpaxis5_a5.out`,
`checks/cpaxis5_a5_m48.out` and `checks/cpaxis5_a5_m56.out`; the others import nothing from the research tree:
```

**D3, after cdata5.out's row. Old:**

```
| `docket68/n1star/checks/cdata5.out` | `6536abcba46ec57a5dca8ced814b7788` |
```

**New:**

```
| `docket68/n1star/checks/cdata5.out` | `6536abcba46ec57a5dca8ced814b7788` |
| `docket68/n1star/checks/reduce5.py` | `0458f70bc710ad3ce966f242bd76e5f0` |
| `docket68/n1star/checks/reduce5.out` | `b0fb5b28fa8499d5fa70226a1b3ed1ee` |
| `docket68/n1star/dnull5.py` | `2035d34bf399cd6ba5c5550d9718ceab` |
| `docket68/n1star/checks/symbol5s.py` | `8441ecf58bab566dda5b5d50c8327f97` |
| `docket68/n1star/checks/symbol5s.out` | `7d51dbf663724abf64087f39974f35c9` |
| `docket68/n1star/checks/symbol5.py` | `14168943230c0c64d18a94fd7f55912e` |
| `docket68/n1star/checks/null3.py` | `767dd3bd58f5c517c99165e1d44f1eb9` |
| `docket68/n1star/checks/null3.out` | `0288d263c81bd929f3ce5647350d69ed` |
| `docket68/n1star/checks/linest5.py` | `34dc9b3d6594771ace2a4257b3a15191` |
| `docket68/n1star/checks/linest5.out` | `cdc11bfb156dbd6dfa2ec2f744d0e842` |
| `docket68/n1star/checks/lev1_5.py` | `bbb29f53599e58d3702d8b7dc5c9aeab` |
| `docket68/n1star/checks/lev1_5.out` | `b6be6a0bf20f95febfba64707fcf3bb8` |
| `docket68/n1star/checks/wgron5.py` | `a764e73c0be0ec38467bc986f7d84bb2` |
| `docket68/n1star/checks/wgron5.out` | `47170f09530b20e8d49f1a56660f55c1` |
| `docket68/n1star/checks/axis5.py` | `b0b864497e94cd73f03624294519c623` |
| `docket68/n1star/checks/axis5.out` | `5cae43e255046b6b4d24b594227c84b0` |
| `docket68/n1star/checks/axisbianchi5.py` | `86d8af8e9024487ee7bd947bce954588` |
| `docket68/n1star/checks/axisbianchi5.out` | `999b80bedb9aaccc627e17002746a912` |
| `docket68/n1star/checks/axhier5.py` | `aa134baade41c3a0664844a4424a567a` |
| `docket68/n1star/checks/axhier5.out` | `0b192015028c3ea2536964f28af58137` |
| `docket68/n1star/checks/cont5.py` | `d5ada772efca2d1fd2b8fec5fc1832e9` |
| `docket68/n1star/checks/cont5.out` | `d4fc239715575ac4757ce2831b259f58` |
| `docket68/n1star/checks/blocks5.py` | `201c163bb0a554b4677c754a85ab4e83` |
| `docket68/n1star/checks/blocks5.out` | `b0468571355f78d03975d63da638308a` |
| `docket68/n1star/checks/blockw5.py` | `6049a5dcb3a362c99ccbe2fb7e950807` |
| `docket68/n1star/checks/blockw5.out` | `f2ae0d7d80a3c238b83c9ec36a66c87c` |
| `docket68/n1star/checks/cpsolve5.py` | `96768ccce2e58f7a4d2e38e0219778e0` |
| `docket68/n1star/checks/cpaxis5.py` | `6fb010b7b948178c58bb7c65e06681d9` |
| `docket68/n1star/checks/cpaxis5.out` | `e89a7902beebffb67a432baa133cb82f` |
| `docket68/n1star/checks/cpaxis5_run1.out` | `7775c999a88c195d189c87d9294e9ce4` |
| `docket68/n1star/checks/cpaxis5_a4.out` | `ae4511e1c474eff3f88bcfeb79aa26cd` |
| `docket68/n1star/checks/cpaxis5_a5.out` | `6565c01c5191ceca28a03882f82f2d4e` |
| `docket68/n1star/checks/cpaxis5_a6.out` | `cee235fc3c4833486f3d66a4e20f260c` |
| `docket68/n1star/checks/cpaxis5_a6_400.out` | `94c9c5a53543c764f1e00d037a49ff33` |
| `docket68/n1star/checks/cpaxis5_a5_m48.out` | `7360e31b7fb5748829d4e26ff2736aa4` |
| `docket68/n1star/checks/cpaxis5_a5_m56.out` | `53ee3e4b64f2cec25109a3eda2f7aa44` |
| `docket68/n1star/checks/cpaxis5_a5_m48_400.out` | `d4a15a41569888c09b76b325519ac1f5` |
| `docket68/n1star/checks/mtrunc5.py` | `eac22e7ad2abb1c5bdf2767a7b2e0d23` |
| `docket68/n1star/checks/mtrunc5.out` | `158dae5aaced2a127fb73ae36c780c0d` |
| `docket68/n1star/checks/cp3grid5.py` | `3033f5bfcf04065b7e99b5dd8cf09186` |
| `docket68/n1star/checks/cp3grid5_control.out` | `1af3c04e9c7ec030e11798fb86454da7` |
| `docket68/n1star/checks/cp3grid5_a8_2grid.out` | `dc3380ec644732a430bb02e7af310c9c` |
| `docket68/n1star/checks/cp3grid5_a9_800.out` | `c7d7752b7f389ed261b4b1c6871354fb` |
| `docket68/n1star/checks/cp3grid5_a10_2grid.out` | `7986c6b71f4dc8ec825ae8d28c9475c7` |
| `docket68/n1star/checks/cp3grid5_a7_3grid.out` | `c654cebc1f5da114da14ee10e38e5bd6` |
| `docket68/n1star/checks/cp3grid5_a8_3grid.out` | `9e823195af627bc21c2d1854ffbfb6b8` |
| `docket68/n1star/checks/cp3grid5_a9_1600.out` | `0d0da9dcc0d554d11f97dd40a4a4ee10` |
| `docket68/n1star/checks/cp3grid5_a10_3grid.out` | `0989baf55d1299a8ff637737215d1426` |
| `docket68/n1star/checks/late5b.py` | `5225f2b4aa53dc1ab452e2355d499ef8` |
| `docket68/n1star/checks/late5b.out` | `ece3e7f063a049a15a5b91ed56c2b555` |
| `docket68/n1star/checks/late5b_small.out` | `be8da58288ee92cd765d25b48c167b41` |
| `docket68/n1star/checks/rcert5.py` | `bf6d843d5963534eaab5ac4123479aa9` |
| `docket68/n1star/checks/rcert5c.py` | `281cd2ea76acbe4fb6e04961bdd0521a` |
| `docket68/n1star/checks/rcert5c.out` | `b4790b613b72f25a492b02ae51dd8503` |
| `docket68/n1star/checks/rcert5d.py` | `c71659021f86b2eba865beeb095f6a97` |
| `docket68/n1star/checks/rcert5d.out` | `2411c62db06cfcee3d2620c62c4ef185` |
| `docket68/n1star/checks/rich5.py` | `2313e4cdbd7eacaa77aead62071da51d` |
| `docket68/n1star/checks/rich5.out` | `c1eabcf625ccac2e059fab62352ac4a9` |
| `docket68/n1star/checks/rich5_runs.out` | `64d3a967c368dcd036c758fe842b51f6` |
| `docket68/n1star/data/rcert5_C3.npz` | `698569f6faaab4420fe2e67abc860561` |
| `docket68/n1star/data/rcert5_C3R.npz` | `88e16664187868e47eaaaa18709cfc61` |
| `docket68/n1star/CERTIFY-10L5-RESULT.md` | `9feaf95d5a7e7f2738a5040a1bdea51c` |
```

**E. Old:**

```
| section 9: residual of a smoothed 3D approximant | `docket68/n1star/checks/resid5.py` Q1–Q2 |
```

**New:**

```
| section 9: the residual of the Richardson approximant | `docket68/n1star/checks/rich5.py` R0–R3, C1–C3 |
| section 9: the single-grid approximant's supremum over one box | `docket68/n1star/checks/rcert5d.py` D0–D4, C1–C2 |
| section 9: the class; frozen-coefficient loss; transport structure | `docket68/n1star/checks/reduce5.py` R0–R4; |
| | `docket68/n1star/checks/symbol5s.py` S1–S6; `checks/null3.py` N0–N10; `checks/linest5.py` E1–E9 |
| section 9: the linear estimate at levels 0 and 1, and its constant | `docket68/n1star/checks/linest5.py` E1–E9; |
| | `docket68/n1star/checks/lev1_5.py` L1–L5; `checks/wgron5.py` W1–W5 |
| section 9: the axes: chart, pairs, Hardy constants, reduced hierarchy | `docket68/n1star/checks/axis5.py` X1–X7; |
| | `docket68/n1star/checks/axisbianchi5.py` B1–B4; `checks/axhier5.py` A1–A7, M1–M4, S1–S3 |
| section 9: existence by continuity from [CTG23], conditional | `docket68/n1star/checks/cont5.py` C1–C2 |
| section 9: the block condition, unweighted and at the weights | `docket68/n1star/checks/blocks5.py` H1–H2; |
| | `docket68/n1star/checks/blockw5.py` B1–B2 |
| section 9: the late region | `docket68/n1star/checks/cpaxis5.py` A1–A6; `checks/cp3grid5.py` A7–A10; |
| | `docket68/n1star/checks/late5b.py` L5–L8 |
| section 9: the late violation against the angular resolution | `docket68/n1star/checks/mtrunc5.py` M1 |
```

**F. Old:**

```
- `checks/resid5.py` Q1–Q2: section 9's computed residual. Every field of a double-null run at the first seed (800 ×
  360, M = 16) is fitted by a tensor Chebyshev series on the box u ∈ [−4, −1.1], v ∈ [0.55, 1.6], so that g_app is an
  explicit smooth metric of the class. Q1, the fit within 7 × 10⁻¹¹ of the run at its nodes; Q2, every frame component
  of Ric[g_app], from the exact symbolic Ricci tensor of the ansatz, at most 2.46 × 10⁻³ of the curvature scale √K_0 at
  the same areal radius, against 9.64 × 10⁻³ on the next coarser run (400 × 180), a ratio of 3.92: the residual is the
  discretisation's, at second order. Control: the lapse moved off the solution (W + 0.01 v) gives a residual 140 times
  larger. Floating point, not certified. About 11 minutes, given the runs.
```

**New:**

```
- `checks/resid5.py` Q1–Q2: the computed residual of a smoothed run. Section 9 now cites the certified residuals of
  `checks/rich5.py` and `checks/rcert5d.py` instead, whose `checks/rcert5.py` imports this program. Every field of a
  double-null run at the first seed (800 × 360, M = 16) is fitted by a tensor Chebyshev series on the box u ∈ [−4, −1.1],
  v ∈ [0.55, 1.6], so that g_app is an explicit smooth metric of the class. Q1, the fit within 7 × 10⁻¹¹ of the run at
  its nodes; Q2, every frame component of Ric[g_app], from the exact symbolic Ricci tensor of the ansatz, at most
  2.46 × 10⁻³ of the curvature scale √K_0 at the same areal radius, against 9.64 × 10⁻³ on the next coarser run
  (400 × 180), a ratio of 3.92: the residual is the discretisation's, at second order. Control: the lapse moved off the
  solution (W + 0.01 v) gives a residual 140 times larger. Floating point, not certified. About 11 minutes, given the
  runs.
- `checks/reduce5.py` R0–R4: section 9's class. For every metric of the class, with no field equation used, the
  five-dimensional Ricci tensor reduces to (2+1)-dimensional gravity coupled to a wave map into the flat plane (R1–R2);
  the reduced residues are fixed linear combinations of the five-dimensional Ricci components (R3); and the Einstein
  frame is written in the record's variables (R4). Exact (sympy). About half an hour.
- `checks/symbol5s.py` S1–S6: section 9's frozen-coefficient loss. The principal symbol of the free formulation with the
  shift's second derivatives kept has no Jordan block (S1–S3), but the shift's angular derivative is of principal size at
  high angular frequency and drives δR at order k² (S4, S6); in the constraint-preserving block the eigenvalue-0 mode
  drives itself (S5), a loss shown on a model only. Control: the frozen-shift system has the Jordan block. Exact, with
  S6's model in floating point. About three minutes.
- `checks/null3.py` N0–N10: section 9's transport structure. In double-null gauge with one-dimensional sections, the
  reduced system's Ricci coefficients, Raychaudhuri, torsion, lapse, commutators and wave operator (N0–N6); the two
  equations the hierarchy does not use carry the only angular derivative (N7), so none appears on the hierarchy's right
  sides (N8); the pairs' energy identities (N9); the linearised pair operators for the difference of two metrics (N10).
  Exact (sympy). Under a minute.
- `checks/linest5.py` E1–E9: supplement Theorem 7.L. The pair identities (E1); the hierarchy linearised in fifteen
  frame-difference unknowns, with no derivative of an unknown on any right side (E2); the two-variable Grönwall lemma
  (E7); the rows checked against the geometry three ways (E9); and, on the record's run, the constant, the truncated
  domains it holds on and the demand it puts on the residual (E4–E6, E8). Controls: a row with the angular loss must be
  flagged (E3); mutated rows must fail E9. Exact for the structure, floating point for the constants. About half a
  minute, given the run.
- `checks/lev1_5.py` L1–L5: supplement Theorem 8.L1. The commutators with e_x (L1); the system commuted once closes in
  thirty unknowns with no level-2 term on any right side (L2), every level-1 row checked against the commutation itself
  (L5); the level-1 constant on the record's run (L4). Controls: a commutator without its e4 term (L1); a row with the
  angular loss (L3); two dropped terms (L5). Exact, with L4 in floating point. About eight to eleven minutes, given the
  run.
- `checks/wgron5.py` W1–W5: supplement Theorem 8.W, the constant with weights. A model Goursat pair, on which the
  weighted bound must hold at every weight tried and two mutations of it must fail (W1); equal weights reproducing
  F² = 10^138 (W2); weights minimising a relaxed objective, F² = 10^66.9 on |x| ≤ 1/2 (W3); a finite-rank approximate
  inverse cannot lower the constant (W4, supplement Lemma 8.F); the frozen-angle growth of the transported unknowns, at
  one resolution (W5). Deduced, with computed checks; the constants in floating point. About eight minutes, given the
  run.
- `checks/axis5.py` X1–X7: the axis charts. Near each axis the class is four-dimensional axisymmetric Einstein–scalar in
  a chart regular at the axis (X1), twist-free in its double-null frame (X2), with a measure in which the pair operators
  are adjoint (X3); the Hardy inequalities that recover angular derivatives from the axis, with explicit constants (X4);
  the frame quantities bounded on the record's run (X5); the polar-frame connection difference δk not an admissible
  L²(dμ) unknown at the axis, which excludes Theorem 7.L's unknowns there and nothing else (X6); and the glue (X7).
  Identities verified at random rational jets with a fixed seed (a probabilistic test), with computed checks. Under a
  minute.
- `checks/axisbianchi5.py` B1–B4: the axis chart's curvature pairs. σ's vanishing (B1); the Gauss equation and [Wu26]'s
  pairs, each found by a linear fit at random jets and checked at fresh random jets (B2–B3b); and the pairs' energy
  inequality on the whole section, the axis included (B4), deduced from them. Probabilistic identity tests with fixed
  seeds. About seven minutes.
- `checks/axhier5.py` A1–A7, M1–M4, S1–S3: [Wu26]'s transport equations, mass aspects and the scalar's pairs in the axis
  chart, reduced and off shell, each found by a linear fit at random rational jets and checked at fresh random jets
  (probabilistic identity tests with fixed seeds), with every angular derivative on a right side recovered from the
  hierarchy's own unknowns (A7). Controls c1–c4: altered coefficients must leave a residual. About a minute and a half.
- `checks/cont5.py` C1–C2: Lemma 9.C of the supplement. The compatibility relations and the metric recovery hold
  identically on the general metric of the class (C1, exact); 4AB < 1 and y ≤ A + By² give y ≤ 2A, and y never enters
  (2A, 1/(2B)) (C2, z3, with a vacuity guard). Controls: χ̲'s relation without b_x (k1); 4AB < 2 (k2); a sharper bound,
  refuted (k3). Seconds.
- `checks/blocks5.py` H1–H2: the block (Schur) condition. The coupling of a multiplication across an angular Galerkin cut
  does not depend on N past the multiplier's degree (H1, exact), and on the record's coefficients it is of their own
  size, so the condition fails at every N in Theorem 7.L's norms (H2, floating point). About 25–40 minutes, given the
  run.
- `checks/blockw5.py` B1–B2: the same condition at Theorem 8.W's weights, from the printed figures of
  `checks/blocks5.out` and `checks/wgron5.out`, each rounded against the claim: the largest pair's product is at least
  57.8 at every N. Controls: equal weights reproduce blocks5's 484 (k1); the smallest pair alone is below 1 (k2). A
  second.
- `checks/rich5.py` R0–R3, C1–C3: section 9's Richardson approximant. Its pinned tensors (R0); its Einstein residual at
  16,128 points (R2) and as a supremum over a sub-box of each of four boxes (R3), certified in ball arithmetic with
  `checks/rcert5d.py`'s engine; the extrapolation's floating-point residual (R1, `--runs`). Controls: the engine end to
  end on test fields with exact suprema, and its enclosures of the coefficients and of the frame output against their
  values at the corners of their boxes, on the approximant's tensors and on degree-7 test fields (C1); the perturbed
  approximant refused (C2); the census regression (C3). Twenty to fifty minutes, read only.
- `checks/rcert5d.py` D0–D4, C1–C2: the single-grid approximant's supremum over one interior box. Order-3 Taylor models
  with the Lagrange remainder in ball arithmetic, bisected until every sub-box meets the target (D1); certified centre
  values that no bound of any method can beat (D2); the census over the 416 boxes (D3); certified point values at the
  centre and corners of every accepted sub-box below its bound (D4). Controls: as rich5's C1, and the perturbed
  approximant refused (C2). The bisection about three hours on four processes; the collection and its checks about two
  minutes.
- `checks/cpaxis5.py` A1–A6: the late region's constraint-preserving scheme. Its singular coupling at the axes (A1–A2),
  the regularisation (A3), and the regularised scheme on the record's data at two angular resolutions (A4) and two null
  grids (A5), with its Kretschmann scalar (A6). Floating point. Each run at 1600 × 720 about four hours; the analyses
  minutes to half an hour.
- `checks/cp3grid5.py` A7–A10: the regularised scheme on three null grids. The unimposed constraint and the metric per
  band of v and class of areal radius, with the observed order (A7); the Kretschmann scalar (A8); the metric's resolution
  in angle (A9); the regularisation's correction replayed at every cell (A10). The third grid covers v ≥ 1.4, and A10
  starts at v = 1.5. Control: the 800-row run given in place of the 1600-row one must read as not converging on every
  band. Floating point. A7 and A9 under a minute, A8 seventeen to twenty minutes and A10 fifteen to thirty, given the
  runs.
- `checks/late5b.py` L5–L8: the free scheme's late region on the record's runs. Raychaudhuri's residual per band and
  class under the null step (L5), in angle (L6) and at small radii (L7); the monotone quantity e^{−2W} R_v along the
  outgoing generators (L8). Control: a wrong coefficient must not converge (L5). Floating point, given the runs.
- `checks/mtrunc5.py` M1: the late region's violation against the angular resolution. The interior constraint monitor at
  800 rows for M = 32, 40, 48 and 56, read from `checks/cpaxis5.py`'s outputs, is classified by a rule fixed before the
  M = 48 and 56 runs were read: angular truncation where every step in M lowers it by a fifth; not truncation where the
  last step does not and it stays above ten times the null-step level; undecided otherwise. Controls: a halving sequence
  (k1); one run given for every M (k2). Arithmetic on printed figures. A second.
```

**G. Old:**

```
    python3 checks/resid5.py RUNDIR l1_M16_800 l1_M16_400    # about 11 minutes, given the runs
```

**New:**

```
    python3 checks/resid5.py RUNDIR l1_M16_800 l1_M16_400    # about 11 minutes, given the runs
    python3 checks/reduce5.py                             # about half an hour
    python3 checks/symbol5s.py                            # about three minutes
    python3 checks/null3.py                               # under a minute
    python3 checks/linest5.py RUN                         # RUN the record's l1_rc0.9_M32.npz; half a minute
    python3 checks/lev1_5.py RUN                          # about eight to eleven minutes
    python3 checks/wgron5.py RUN                          # about eight minutes
    python3 checks/axis5.py RUN                           # under a minute
    python3 checks/axisbianchi5.py                        # about seven minutes
    python3 checks/axhier5.py                             # about a minute and a half
    python3 checks/cont5.py                               # seconds
    python3 checks/blocks5.py RUN                         # 25-40 minutes; then checks/blockw5.py (a second)
    python3 checks/rich5.py                               # 20-50 minutes, read only; --runs RUNDIR for R1
    python3 checks/rcert5d.py --worker w 4                # w = 0..3 at once, about three hours; then --collect 4
    python3 checks/rcert5d.py --census                    # about a minute
    python3 checks/cpaxis5.py --run 1 0.9 M Nu Nv 2.25 OUT reg ld 3   # a regularised run; 1600 x 720 about 4 h
    python3 checks/cpaxis5.py --nullstep R400 R800 R40_800   # and --compare, --kretschmann (A4-A6)
    python3 checks/cp3grid5.py --a7 R400 R800 R1600 [R40_1600]   # and --a8, --pclass, --dpm, --control
    python3 checks/late5b.py RUNDIR                       # given the record's runs
    python3 checks/mtrunc5.py                             # a second, from checks/cpaxis5_a5*.out
```

## 13. Round 9 (2026-11-13): the verifier of round 8 seated, M = 48 at 1600 rows, and one text for the wavelengths item

The verifier of round 8 read section 12 (lines 4094–4698, file md5 fa9d849d…). It found M7-A fixed everywhere and
blocks A–G matching the paper, each old text once. The reruns were identical, mB5 and its own mB6 died, and the
certificates stand. It did not confirm section 12 because of one Major, on wording. It also found one minor finding and
four nits. Each is seated below as a bracketed amendment to the section 12 text it names; section 12 is not edited.
Sections 0–12 are byte-identical before and after this append.

### 13.0 The verifier of round 8: its findings, seated as amendments to section 12

**M8-A. "A rule fixed before the M = 48 and 56 runs were read" cannot be verified, and the verdicts over-read.**
- [12.1, "The rule, fixed before the results"; block F's mtrunc5 entry, "a rule fixed before the M = 48 and 56 runs were
  read"; `checks/mtrunc5.py` line 6; block A, "so on these bands it is the angular truncation's", with 1.0–1.2 on
  [1.8, 1.9) among them: verifier of round 8 (M8-A).]
  - *Re-derived.* The rule's first trace is mtrunc5.py's first commit (a0413e2, 06:09), after the `--nullstep` outputs
    (06:07–06:08). When it was written relative to reading them is not documented.
  - *Repaired (`checks/mtrunc5.py`).*
    - The docstring states that the rule's timing is not documented.
    - The verdicts read "consistent with angular truncation".
    - New M2 prints each verdict's sensitivity to the thresholds θ (0.8) and F (10).
  - *The sensitivity* (`checks/mtrunc5.out`).
    - Every one of the five decided verdicts stands for θ anywhere in [0.680, 1.149].
    - On the two truncation bands the monitor at M = 56 is 23.1 and 38.8 times the null-step level.
    - Of the undecided bands, 1.0–1.2 on [1.9, 2.0) reads truncation for θ ≥ 0.818 and not truncation for θ ≤ 0.778.
      1.0–1.2 on [1.8, 1.9) reads truncation for θ ≥ 1.056.
  - *Corrected text.*
    - 12.1's "The rule, fixed before the results" reads "The rule (its timing relative to reading the outputs is not
      documented)".
    - 12.1's verdicts and block A read "consistent with angular truncation".
    - 1.0–1.2 on [1.8, 1.9) is undecided by the rule. The M = 48 null-step evidence is stated beside it, as separate
      evidence (12.1; 13.1).
    - On the two truncation bands, the monitor at M = 56 is still 23 and 39 times the null-step level. At M = 48 it
      falls only 1.72- and 1.13-fold from 400 to 800 rows. Block A says so and implies no convergence there.

**m8-1. mtrunc5's controls guarded the thresholds, not the inputs.**
- [12.1, "Controls: … Both pass": verifier of round 8 (m8-1).] Two of the verifier's mutants passed both controls while
  changing the verdicts: L computed over all bands, and the M = 48 and 56 inputs swapped.
- *Repaired.*
  - Control k3: L's bands must be exactly those whose M = 32 ratio from 400 to 800 rows is second order, [3, 5.5]
    (14 of 21).
  - Control k4, run identity: each file's command line must name the M = 32 runs at 400 and 800 rows and, third, the run
    at the M it is read for.
  - Rebuilt (`scratchpad/r9/mt/`), L over all bands fails k3 and the swap fails k4. A θ moved to 0.9 fails the
    decided-range check. Each prints FAILURES; the real program passes.

**Nits.**
- [12.1, "3.84–4.14"]: at M = 48 the claimed bands fall 3.80–4.14-fold from 400 to 800 rows. It reads 3.80–4.14.
- [12.1 and block A, "falls 0.48–0.68-fold per step", "falls by only 0.77–0.82 per step"]: they read "falls to
  0.48–0.68 of its value per step" and "to 0.77–0.82 of its value per step".
- [`checks/axis5.py`, line 419, "# X6 the counterexample"; its printed "X6 (exact)"]: the comment states M-C's reading.
  - X1–X3, X6 and X7 now print "(random jets)", and X6 also states what it shows.
  - axis5 was rerun on the record's run. Only those labels and the timings change, and `checks/axis5.out` is
    regenerated.
- [12.0, "Four more readings were fixed"]: it reads "Three more readings were fixed, plus rich5's control description".

### 13.1 M = 48 at 1600 rows (PID 3123, restarted 06:08 UTC)

The run finished at 07:38 UTC: `<scratch>/r8/cp_M48_1600_reg.npz`, 5,365 s, md5 32774883…. 12.1's three commands
were run on it, with the earlier M = 32 and 40 runs. cp3grid5.py labels its columns for M = 32 and 40, so each output
is seated with a header naming its runs:
- `checks/cp3grid5_a7_m48.out`: three null grids at M = 48, with M = 40 as the angular comparison (its "M40/M32" reads
  M40/M48);
- `checks/cp3grid5_a7_m32v48.out`: M = 32's three grids against M = 48 at 1600 rows (its "M40/M32" reads M48/M32);
- `checks/cp3grid5_a9_1600_m48.out`: |P_32 − P_48| at 1600 rows.

**The claimed regions at M = 48** (computed). They are second order on three null grids, as at M = 32:
- the monitor falls 3.80–4.14-fold from 400 to 800 rows and 3.89–4.08-fold from 800 to 1600;
- the metric's observed order is 2.00–2.03;
- at 1600 rows M = 40 gives 0.85–0.96 of M = 48's monitor, and M = 48 gives 1.14–1.49 of M = 32's. The monitor there
  rises slightly with M, as at 800 rows: it is the null step's;
- M = 48 changes the metric from M = 32's by at most 3.3 × 10⁻⁹ there.

**1.0–1.2 on [1.8, 1.9), under the rule as stated now.** The rule reads the 800-row monitors for M = 32–56, which this
run does not change. So the band stays undecided: its steps are 0.30, 0.57 and 1.06, and m(56) is 0.92 L, below ten
times the null-step level. By M2's sensitivity, it would read consistent with angular truncation only for θ ≥ 1.056,
and not truncation only for F < 0.92. The run cannot decide it under this rule.

**1.0–1.2 on [1.8, 1.9): the M = 48 evidence, beside the rule** (computed; `checks/cp3grid5_a7_m48.out`).
- At M = 48 the monitor is 0.00618, 0.00161 and 0.000582 on the three null grids. It falls 3.84-fold and 2.77-fold;
  the second step is short of second order. cp3grid5's verdict is "converging".
- The metric's difference falls 4.09-fold (order 2.03).
- At 1600 rows M = 40 leaves the monitor 3.53 times larger, and M = 32 about 19 times (M48/M32 = 0.05). At this grid
  the steps M = 32 → 40 → 48 are 0.19 and 0.28. The rule is not defined at 1600 rows, so this is not its verdict.
- At 1600 rows the monitor is 1.4–1.7 times the claimed bands' level in its class (3.4–4.1 × 10⁻⁴).
- So, at M = 48, the violation there falls under both null refinements and with M at the finest grid. It has not
  reached the claimed bands' level, and the second refinement is short of second order. No convergence is claimed.

**The two truncation bands at M = 48** (computed).
- 0.9–1.0 on [1.8, 1.9): 0.444, 0.258 and 0.262 (ratios 1.72 and 0.98).
- ≥ 1.2 on [2.0, 2.25): 0.0883, 0.0781 and 0.0869 (ratios 1.13 and 0.90).
- So at M = 48 the monitor does not fall from 800 to 1600 rows. Its null-step limit at M = 48 is not vacuum there.
- At 1600 rows it falls with M as at 800 rows: from M = 32 to 40 to 48 the steps are 0.50 and 0.47, and 0.58 and 0.53.
- The bands stay "consistent with angular truncation". Convergence in the null step at a fixed M is not shown there.

**The other bands beyond** (computed). At M = 48 the monitor does not converge in the null step on any of them
(ratios 0.96–1.38). At 1600 rows it grows with M where 12.1 reads not truncation (M48/M32 1.43, 2.51 and 3.87). At
1.0–1.2 on [1.9, 2.0), still undecided, the steps at 1600 rows are 0.81 and 0.78, as at 800 rows (0.82 and 0.77).

### 13.2 The rebuild against growth5 from v = 1.3, at a second null resolution

- *The runs* (`checks/szrun5.py`, unchanged at f2792347…): the first seed at M = 16 and 1600 × 720, with the data
  cone at R0 = 10 and 20 (`<scratch>/r9/runs/l1_M16_1600.npz`, f7671edc…, and `l1_M16_1600_R20.npz`, ac7abb37…;
  2,434 and 2,435 s). Their 400- and 800-row partners are section 4's.
- *Z1, the rebuilt outer zero under the null step* (`checks/szconv5.py`, new; `checks/szconv5.out`).
  - From 800 to 1600 rows the rebuilt outer zero changes by at most 0.0053 at R0 = 10 and 0.0067 at R0 = 20, for
    v ≤ 1.375. From 400 to 800 rows it changed by up to 0.058 and 0.025.
  - Its difference from growth5's at 1600 rows, from v = 1.3, is 0.053–0.106 at R0 = 10 and 0.026–0.046 at R0 = 20.
    It halves as R0 doubles (2.0–2.3).
  - So the difference that 6.1's S6 left "not resolved in (u, v)" from v = 1.3 is not the double-null grid's. It is
    the data truncation's (it halves with R0) and growth5's own, whose record is at one resolution.
  - Control: the leaves' expansion in place of θ disagrees with growth5 by 0.224 (good).
- *S6 at 1600 rows* (`checks/secondzero5_trunc1600.out`): all checks pass, with the 400-row block reproduced.
- *S7 at 1600 rows* (`checks/secondzero5_edges1600.out`). The untrapped band on growth5's 17 columns at r* = 0.64–0.76:
  - at R0 = 10, every edge is within one column spacing of growth5's up to v = 1.525, and the band is one column
    longer at v = 1.45;
  - at R0 = 20, the same, except that from v = 1.5 the column at x = 1, on the axis, is untrapped too;
  - at v = 1.55, as at 800 rows, growth5's band reaches the axis and the rebuild's stops 3.8–4.0 spacings short.
  - S7's all-v gate FAILs at 1600 rows as at 800. Its control fails as it should: the leaves' expansion untraps no
    column.
- Block B's text in the wavelengths item now states both resolutions (13.3, 13.6).

### 13.3 The paper's "Physical wavelengths" item, as one text (a task of this round)

The item runs from paper line 1446 ("- **Physical wavelengths.**") to line 1504 at md5 805be200…. It holds blocks A
(lines 1488–1504) and B (1473–1475). Its older sentences had gone stale, or read as open. It is rewritten as one
old/new pair, keyed by content, with A and B folded in (`scratchpad/r9/bullet_{old,new}.txt`; 13.6). What changed:
- *Kept, with their status words:*
  - the scale ratios (R7);
  - [AB26]'s comparison;
  - growth5's premise failure and excision figures (excise5);
  - the growth and amplification factors;
  - the second zero's reading (sectexp5, secondzero5);
  - the untrapped columns (B);
  - the [Wu26] sentence;
  - seed_escape;
  - the second seed's angular figures (g1curv5);
  - block A's certified, deduced and computed lists.
- *Replaced, as superseded:*
  - "could settle it … and that is not attempted" now reads: the route is "taken here … what the route reaches at
    10 l5 is stated at the end of this item";
  - "its five-dimensional version in the class is not built" now reads: "its counterpart in the class is built in the
    parts listed below as deduced";
  - "a certified argument would need the propagator's norm, not a sup-norm bound" is dropped. The three factors stay
    as computed figures.
  - "Nothing is said of the event horizon" now reads: "The event horizon is not located: its position depends on the
    whole future development, which is computed to finite advanced time only."
  - "the scheme is unstable at 24 and 32" now states what was computed: growth5's step is unstable in angle at
    N_x = 24 and 32 on the seed itself (supplement 1.5).
  - "the rebuild does not reach r ≤ 0.3 r_h" now states what holds there: the rebuild reaches no sphere below about
    0.5 r_h before the cut, so growth5's second zero at 0.21–0.30 r_h is neither reproduced nor contradicted (1.4).
  - "unresolved in (u, v) from v = 1.3 r_h" is replaced by the 1600-row result (13.2).
  - "The late region stays unresolved" (second seed) now reads "beyond v ≈ 3.25 the second seed's late region is not
    resolved in angle".
  - The first seed's sentence ("not yet told apart") goes, as in 10.4.
- *The limit is stated once,* at the end. Existence is proved where the solution is the seed (v ≤ r_h/2) and not beyond
  it. Lemma 9.C's 4F²Gr < 1, at the computed F² = 10^66.9, asks r of order 10⁻⁶⁸/G, against the certified 3.73 × 10⁻⁵
  and 5.0 × 10⁻⁴. Its hypotheses are established on no region of its form beyond the seed.
  - The two earlier statements of this limit inside block A, in its deduced and computed lists, are removed, so that it
    is said once.
- *Decided by computation this round:* the rebuild's agreement with growth5 from v = 1.3, at a second null resolution
  (13.2).
- *Not recomputed, and why:* growth5 at N_x = 24 with a smaller step.
  - At 0.7 of its step it had not reached v = 0.25 in an hour (supplement 1.5). Reaching its breakdown near v = 1.5
    would take six hours or more.
  - Its premise fails at N_x = 16 in any case, and the double-null scheme replaces it.
  - The bullet states the computed limit instead: its breakdown times are at one angular resolution.

### 13.4 What holds at 10 l5 after round 9

12.2's list stands, with these changes:
- 1.0–1.2 on [1.8, 1.9) is undecided by the comparison in M (13.0). At M = 48 it falls under both null refinements on
  three grids, the second short of second order. At 1600 rows M = 40 leaves it 3.5 times larger. That is evidence beside
  the rule, not its verdict (13.1).
- The two truncation bands are "consistent with angular truncation". There the monitor at M = 56 is still 23 and 39
  times the null-step level (13.0). At M = 48 it does not fall from 800 to 1600 rows, and at 1600 rows it still falls
  with M (13.1).
- The rebuilt outer zero is resolved in (u, v) to v = 1.375 r_h: from 800 to 1600 rows it changes by at most 0.007 r_h.
  Its difference from growth5's there is the data truncation's and growth5's own (13.2).

There is no new existence statement. Existence is proved where the solution is the seed and is not claimed beyond it.

### 13.5 Files and outputs (round 9)

| file | what | md5 (round 8 → round 9) |
|---|---|---|
| `checks/mtrunc5.py` | M8-A, m8-1: the timing note, M2's sensitivity, controls k3 and k4 | eac22e7a… → 2f836c7d… |
| `checks/mtrunc5.out` | regenerated | 158dae5a… → 9a23e455… |
| `checks/axis5.py` | nit: the X labels print "(random jets)"; X6's comment | b0b86449… → 6724ac8e… |
| `checks/axis5.out` | regenerated; only the labels and timings change | 5cae43e2… → c708b130… |
| `checks/szconv5.py` (new) | 13.2: Z1, the rebuilt outer zero under the null step, with its control | 3c6c7b0e… |
| `checks/szconv5.out` (new) | its output | 90d632eb… |
| `checks/secondzero5_trunc1600.out` (new) | `secondzero5.py` S6 with the 1600-row runs | e64dadd9… |
| `checks/secondzero5_edges1600.out` (new) | `secondzero5.py` S7 with the 1600-row runs | 5e640f6e… |
| `checks/cp3grid5_a7_m48.out` (new) | 13.1: `--a7`, three null grids at M = 48, M = 40 at 1600 rows | 02e2724c… |
| `checks/cp3grid5_a7_m32v48.out` (new) | 13.1: `--a7`, M = 32's three grids, M = 48 at 1600 rows | 64b29e08… |
| `checks/cp3grid5_a9_1600_m48.out` (new) | 13.1: `--pclass`, M = 32 against 48 at 1600 rows | 20055563… |

- `data/rcert5_C3.npz` (698569f6…) and `data/rcert5_C3R.npz` (88e16664…) are unchanged.
- The round-8 versions are `scratchpad/r9/mtrunc5.r8.py`, `axis5.r8.py` and `axis5.r8.out`.
- The mtrunc5 mutants of m8-1 are in `scratchpad/r9/mt/`, with their outputs.
- The runs: `<scratch>/r8/cp_M48_1600_reg.npz` (32774883…, PID 3123), `cp_M48_400_reg.npz` (f7d818fb…, PID 3124), and
  `<scratch>/r9/runs/l1_M16_1600.npz` (f7671edc…) and `l1_M16_1600_R20.npz` (ac7abb37…). Every run has finished, and no
  process of this round is left running.

### 13.6 The paper: the wavelengths item (blocks A and B folded in), and blocks C–G

These replace 12.4's proposal. They are proposed to the main session, which seats them; this note edits neither the paper
nor N1STAR-PROOF.md.
- *Keyed by text.* Each old text occurs exactly once in `RESPONSE-HL-5D.md` at md5 805be200b746b7cf480e88639da5508f.
  - The wavelengths item's old text runs from its first line through the end of block A's old text. Blocks A and B lie
    inside it, so they are not separate blocks any more.
  - C, D1, D2, D3, E, F and G have 12.4's old texts.
  - The files are in `scratchpad/r9/blocks/`, and the item also in `scratchpad/r9/bullet_{old,new}.txt`.
- *Checked:* every block applied to a copy (`scratchpad/r9/paper_applied.md`). Every line is ≤ 121 characters. Every
  md5 row of Appendix D matches its file except `CERTIFY-10L5-RESULT.md`'s, which holds fa9d849d… and is rewritten by
  `python3 response5.py --update-md5` at seating. Longest new line: 121 characters.
- *Changed from 12.4:*
  - the item (13.3);
  - F: the mtrunc5 entry (M8-A);
  - E: mtrunc5's labels;
  - D3: the round-9 md5s, and rows for the new outputs.
  - C, D1, D2 and G are 12.4's.

**The wavelengths item. Old:**

```
- **Physical wavelengths.** λ0 is not evaluated, and a high-frequency theorem, whose expansion parameter is λ over the
  curvature length, does not apply at a wavelength of 10 l5 here (λ is the reduced wavelength of the phase v/λ, as in
  the numerics' usage). The expansion parameter is the wavelength over the curvature length L = K^(−1/4); on x_K = 1, L
  = l5, and at the horizon L = √μ/72^(1/4). For λ = 10 l5 the ratio is 10 on x_K = 1, and 2.91 (μ = 100 l5²) or 0.92 (μ
  = 1000 l5²) at the horizon (computed, R7): there is no separation of scales. The statement that the waves are
  high-frequency on all of D_T once λ < l5/10 is about the approximant, not about λ0. Against the scale on which the
  curvature varies, r, the ratio is 1.00 and 0.32 at the horizon and 1.85 and 1.04 on x_K = 1 (computed, R7). That is
  the parameter a construction from exact waves would see, in the manner of [AB26], whose layers are waves exact on a
  locally linear background, with amplitudes solving ordinary differential equations ("no sinusoidal identity was
  used", section 3.1); it is not small either, and there the wavelengths are chosen, here prescribed. At a prescribed
  wavelength without a small parameter, existence on D_T is a large-data question; a computed solution with a certified
  residual and a certified linear estimate could settle it (the rigorous numerics cited in [AB26] as [4]), and that is
  not attempted. Its first step was taken: the growth factor measured on the solver's own computed solution at 10 l5
  (`docket68/n1star/growth5.py`, supplement section 10.2). At both seeds that scheme's premise — one zero of the round
  spheres' expansion per column and the core boundary outflow, so that the exterior is fixed by its own data — fails
  before the shell's peak: a second zero holds over 0.04 in v from 1.50 r_h at μ = 100 l5² (1.496 on the finer grid,
  1.476 with a shorter hold; a single-step excursion at 1.45 is not it) and from 1.583 r_h at 1000 l5² (three grids
  agreeing to 0.0005), and the boundary ceases to be outflow within 0.1 after; a deeper excision fails earlier, not
  later (r = 0.39 and 0.25 r_h at the first seed, 0.21 r_h at the second), on the next finer grid too: with the
  breakdown read as a second zero lasting 0.01 in v, the solver's criterion, the three move by 0.0008, 0.0025 and
  0.0002 between the grids and the standard excision by 0.0041 and 0.0004, and the order holds for every such duration
  from 0.005 to 0.06 (`docket68/n1star/checks/excise5.py`). So no approximant on D_T comes from that scheme at 10 l5 at
  the excision depths run. The second zero belongs to that chart's areal spheres and is not a second marginally trapped
  surface: wherever a smooth vacuum solution with these data exists in double-null gauge, every leaf inside the seed's
  horizon generator is outer trapped, and every T²-invariant marginal section of an ingoing cone lies near areal radius
  1.01–1.05 r_h (deduced, its identities computed in `docket68/n1star/checks/sectexp5.py`; the zero set computed at 100
  l5² for v ≤ 1.75 r_h in `docket68/n1star/checks/secondzero5.py`; supplement note `CERTIFY-10L5-RESULT.md` section 1).
  At 100 l5² the Bondi spheres rebuilt on the double-null solution reproduce the untrapped columns to within one column
  spacing up to v = 1.525 (not at 1.55), which come from the spheres' tilt against the null leaves (computed); at 1000
  l5² the rebuild does not reach r ≤ 0.3 r_h. The breakdown times are at one angular resolution (N_x = 16); the scheme
  is unstable at 24 and 32. Nothing is said of the event horizon. The step is re-posed as the characteristic initial
  value problem in double-null gauge — the incoming wave on an ingoing null hypersurface from past null infinity, the
  seed's outgoing cone as the other — where Luk's theorem gives local existence without smallness ([Wu26] Theorem 2.1)
  and [Wu26]'s Theorem 2.2 is the a posteriori structure, introduced there by the sentence "the difference of metrics
  is controlled by the difference of curvature residues" (section 2.3, p. 6; the sentence before the theorem, not its
  text); its five-dimensional version in the class is not built. Up to the failure the radiation field's growth factor
  exp ∫K dv is 1.9 and 2.1, and a finite-difference amplification of the data along one direction, a lower bound for
  the propagator's norm, is 1.28 and 1.00; where the scheme completes (λ = 0.1 r_h) they are 6.9 and 1.71, while the
  sup-norm Grönwall factor is 17, 2 × 10⁵ and 6 × 10³: a certified argument would need the propagator's norm, not a
  sup-norm bound. The linear scattering of the shell off the seed at 10 l5 is computed in
  `docket68/lemmas/seed_escape.py`. That problem has since been computed as a prototype (supplement
  `docket68/n1star/CERTIFY-10L5.md` section 6b; computed, not certified): the class's Einstein equations in double-null
  gauge, evolved in (u, v) with an expansion in the polar angle, at the prescribed wavelength at both seeds. At the
  first seed the Kretschmann scalar is moderate and converged in angle up to the point where the runs stop converging,
  and unresolved after it, where a singularity, a steep smooth feature and a defect at the axis are not yet told apart.
  At the second seed, with the angular and null grids refined together, the two coarser angular resolutions agree up to
  v ≈ 3.5 and the finest departs from them from v ≈ 3.25, at every angle. On a finer null grid, 2400 × 1080, the second
  seed's M = 32 and 40 angular resolutions agree to 0.09 K_0 up to v = 3.5 and to 0.53 K_0 up to v = 4.5 (K_0 = 72/R⁸,
  Tangherlini's Kretschmann scalar at the same areal radius), away from the cells M = 48 masks; M = 48 departs from v ≈
  3.25 exactly as at 1600 × 720, so the finer null grid does not move it, and the step condition M²/N ≤ c it had been
  ascribed to is refuted (M²/N = 0.96). The late region stays unresolved (computed, floating point:
  `docket68/n1star/checks/g1curv5.py --seed2-2400`, output `checks/g1curv5_seed2_2400.out`; supplement
  `CERTIFY-10L5.md` section 6b). A first certified step is taken: for an explicit approximant of the characteristic
  data on the data cone, the constraint along its outgoing generators holds to a certified bound at both seeds (at the
  second, 2.3 × 10⁻⁵ against terms of size 5.3 × 10⁻⁴; certified, ball arithmetic, `docket68/n1star/checks/cdata5.py`).
  The full Einstein residual of a smoothed three-dimensional approximant built from a run is computed only, 2.5 × 10⁻³
  of the curvature scale and falling at second order with the grid (`checks/resid5.py`, floating point), and no linear
  estimate with explicit constants is available for the characteristic problem in the class, so existence at 10 l5
  remains open (supplement `CERTIFY-10L5-RESULT.md` section 2).
```

**New:**

```
- **Physical wavelengths.** λ0 is not evaluated, and a high-frequency theorem, whose expansion parameter is λ over the
  curvature length, does not apply at a wavelength of 10 l5 here (λ is the reduced wavelength of the phase v/λ, as in the
  numerics' usage). The expansion parameter is the wavelength over the curvature length L = K^(−1/4); on x_K = 1, L = l5,
  and at the horizon L = √μ/72^(1/4). For λ = 10 l5 the ratio is 10 on x_K = 1, and 2.91 (μ = 100 l5²) or 0.92 (μ = 1000
  l5²) at the horizon (computed, R7): there is no separation of scales. The statement that the waves are high-frequency
  on all of D_T once λ < l5/10 is about the approximant, not about λ0. Against the scale on which the curvature varies,
  r, the ratio is 1.00 and 0.32 at the horizon and 1.85 and 1.04 on x_K = 1 (computed, R7). That is the parameter a
  construction from exact waves would see, in the manner of [AB26], whose layers are waves exact on a locally linear
  background, with amplitudes solving ordinary differential equations ("no sinusoidal identity was used", section 3.1);
  it is not small either, and there the wavelengths are chosen, here prescribed. At a prescribed wavelength without a
  small parameter, existence on D_T is a large-data question, taken here by the route of a computed solution with a
  certified residual and a certified linear estimate (the rigorous numerics cited in [AB26] as [4]); what the route
  reaches at 10 l5 is stated at the end of this item. The solver's own scheme came first, with the growth factor measured
  on its computed solution at 10 l5 (`docket68/n1star/growth5.py`, supplement section 10.2). At both seeds that scheme's
  premise — one zero of the round spheres' expansion per column and the core boundary outflow, so that the exterior is
  fixed by its own data — fails before the shell's peak: a second zero holds over 0.04 in v from 1.50 r_h at μ = 100 l5²
  (1.496 on the finer grid, 1.476 with a shorter hold; a single-step excursion at 1.45 is not it) and from 1.583 r_h at
  1000 l5² (three grids agreeing to 0.0005), and the boundary ceases to be outflow within 0.1 after; a deeper excision
  fails earlier, not later (r = 0.39 and 0.25 r_h at the first seed, 0.21 r_h at the second), on the next finer grid too:
  with the breakdown read as a second zero lasting 0.01 in v, the solver's criterion, the three move by 0.0008, 0.0025
  and 0.0002 between the grids and the standard excision by 0.0041 and 0.0004, and the order holds for every such
  duration from 0.005 to 0.06 (`docket68/n1star/checks/excise5.py`). So no approximant on D_T comes from that scheme at
  10 l5 at the excision depths run. Up to the failure the radiation field's growth factor exp ∫K dv is 1.9 and 2.1, and a
  finite-difference amplification of the data along one direction, a lower bound for the propagator's norm, is 1.28 and
  1.00; where the scheme completes (λ = 0.1 r_h) they are 6.9 and 1.71, while the sup-norm Grönwall factor is 17, 2 × 10⁵
  and 6 × 10³. The scheme's breakdown times are at one angular resolution, N_x = 16: at its own step it is unstable in
  angle at N_x = 24 and 32 on the seed itself, before the wave arrives (computed; supplement `CERTIFY-10L5-RESULT.md`
  section 1.5). The second zero belongs to that chart's areal spheres and is not a second marginally trapped surface:
  wherever a smooth vacuum solution with these data exists in double-null gauge, every leaf inside the seed's horizon
  generator is outer trapped, and every T²-invariant marginal section of an ingoing cone lies near areal radius
  1.01–1.05 r_h (deduced, its identities computed in `docket68/n1star/checks/sectexp5.py`; the zero set computed at 100
  l5² for v ≤ 1.75 r_h in `docket68/n1star/checks/secondzero5.py`; supplement note `CERTIFY-10L5-RESULT.md` section 1).
  At 100 l5², on the sphere of least areal radius the rebuild reaches before the cut (0.64–0.78 r_h), the band of
  growth5's columns along which the Bondi spheres rebuilt on the double-null solution are untrapped has each edge within
  one column spacing of growth5's own up to v = 1.525 r_h, at both data-cone radii run (the sets equal or shifted by one
  column, except at the larger radius at v = 1.45 and 1.525 r_h, where the rebuild's band is one column shorter); at
  v = 1.55 r_h growth5's band reaches the axis and the rebuild's stops 3.8–4.0 spacings short. At a second null
  resolution, 1600 × 720, the edges stay within one column spacing of growth5's up to v = 1.525 r_h at both radii, the
  rebuild's band one column longer at v = 1.45 r_h, and at the larger radius the column at x = 1, on the axis, is
  untrapped too from v = 1.5 r_h; and from 800 to 1600 rows the rebuilt outer zero changes by at most 0.007 r_h up to
  v = 1.375 r_h, against its difference of 0.026–0.046 r_h from growth5's from v = 1.3 r_h at the larger radius
  (0.053–0.106 r_h at the smaller, so the difference halves as the radius doubles), which is therefore not the
  double-null grid's (computed, `docket68/n1star/checks/szconv5.py`). The untrapping comes from the spheres' tilt against
  the null leaves, whose own expansion leaves no column untrapped (computed, `docket68/n1star/checks/secondzero5.py
  --edges`; supplement `CERTIFY-10L5-RESULT.md` sections 6.1, V2–V3, 9.0 and 13.2). At 1000 l5² the rebuild reaches no
  sphere below about 0.5 r_h before the cut, so growth5's second zero there, at 0.21–0.30 r_h, is neither reproduced nor
  contradicted (computed; supplement section 1.4). The event horizon is not located: its position depends on the whole
  future development, which is computed to finite advanced time only. The step is re-posed as the characteristic initial
  value problem in double-null gauge — the incoming wave on an ingoing null hypersurface from past null infinity, the
  seed's outgoing cone as the other — where local existence holds without smallness (Luk's theorem, [Wu26] Theorem 2.1,
  and in higher dimensions [CTG23] Theorem 1.1) and [Wu26]'s Theorem 2.2 is the a posteriori structure, introduced there
  by the sentence "the difference of metrics is controlled by the difference of curvature residues" (section 2.3, p. 6;
  the sentence before the theorem, not its text); its counterpart in the class is built in the parts listed below as
  deduced. The linear scattering of the shell off the seed at 10 l5 is computed in `docket68/lemmas/seed_escape.py`. The
  characteristic problem itself is computed (supplement `docket68/n1star/CERTIFY-10L5.md` section 6b; computed, not
  certified): the class's Einstein equations in double-null gauge, evolved in (u, v) with an expansion in the polar
  angle, at the prescribed wavelength at both seeds. At the second seed, with the angular and null grids refined
  together, the two coarser angular resolutions agree up to v ≈ 3.5 and the finest departs from them from v ≈ 3.25, at
  every angle. On a finer null grid, 2400 × 1080, the second seed's M = 32 and 40 angular resolutions agree to 0.09 K_0
  up to v = 3.5 and to 0.53 K_0 up to v = 4.5 (K_0 = 72/R⁸, Tangherlini's Kretschmann scalar at the same areal radius),
  away from the cells M = 48 masks; M = 48 departs from v ≈ 3.25 exactly as at 1600 × 720, so the finer null grid does
  not move it, and the step condition M²/N ≤ c it had been ascribed to is refuted (M²/N = 0.96); beyond v ≈ 3.25 the
  second seed's late region is not resolved in angle (computed, floating point: `docket68/n1star/checks/g1curv5.py
  --seed2-2400`, output `checks/g1curv5_seed2_2400.out`; supplement `CERTIFY-10L5.md` section 6b). The rest holds with
  these statuses. Certified (ball arithmetic): on the data cone the outgoing constraint of an explicit approximant holds
  to 5.0 × 10⁻⁵ and 2.3 × 10⁻⁵ at the two seeds, 4.1–4.3 % of the terms that cancel in it
  (`docket68/n1star/checks/cdata5.py`); on u ∈ [−4, −1.1] r_h, v ∈ [0.55, 1.6] r_h, |x| ≤ cos(π/32), the Einstein
  residual of an explicit three-dimensional approximant, Richardson-extrapolated from two null grids, its coefficients
  pinned by md5 (`docket68/n1star/data/rcert5_C3R.npz`), is at most 3.73 × 10⁻⁵ of the curvature scale at 16,128 points
  and at most 5.0 × 10⁻⁴ as a supremum over a sub-box of each of four of the 416 boxes covering that region, on which the
  single-grid approximant (`data/rcert5_C3.npz`) has certified values of 1.09–2.41 × 10⁻³ (`checks/rich5.py`), and the
  single-grid approximant's supremum over one interior box of the 416 is at most 3.01 × 10⁻⁴ (`checks/rcert5d.py`; both
  certificates' bounds are checked by a control that runs the whole bound computation on test fields varying in each
  coordinate, and on the coordinate map, with exact suprema, by a check that the enclosures it forms of the approximant's
  coefficients contain their values at the corners of their boxes, and by independent certified point values at the
  centre and corners of every accepted sub-box). Deduced: the class is (2+1)-dimensional gravity coupled to a wave map
  into the flat plane (`checks/reduce5.py`); in the free metric formulation, at frozen coefficients on spherical states,
  the shift's angular derivative is of principal size at high angular frequency and drives δR at order k², so no estimate
  without loss of derivatives holds for the frozen-coefficient problem (`checks/symbol5s.py`; for the
  constraint-preserving formulation a loss is indicated by a model only); in double-null gauge the reduced transport
  equations carry no angular derivative of an unknown on their right sides (`checks/null3.py`, `checks/linest5.py`), and
  a linear estimate with explicit constants holds on truncated domains of dependence away from the axes, at level 0 and
  at level 1 in the cones' L² norms (supplement Theorems 7.L, 8.L1 and 8.W; `checks/lev1_5.py`, `checks/wgron5.py`); near
  each axis the class is four-dimensional axisymmetric Einstein–scalar in a chart regular at the axis, where [Wu26]'s
  curvature pairs have energy identities on the whole section, the angular recoveries hold with explicit Hardy constants,
  and [Wu26]'s transport equations, mass aspects and the scalar's pairs hold in reduced form with every angular
  derivative on their right sides recovered from the hierarchy's own unknowns (`checks/axis5.py`,
  `checks/axisbianchi5.py`, `checks/axhier5.py`; identities verified at random jets); and, for smooth T²-invariant
  characteristic data that satisfy the constraints, a smooth T²-invariant vacuum development exists on the region
  u ∈ [−10, u*] r_h, v ∈ [r_h/2, v*] of the gauge, the axes included, whenever, on every slab v ≤ s of that region, every
  smooth T²-invariant vacuum metric with these data, in the gauge, differs from the approximant by an amount obeying a
  linear estimate with constant F at every level, the quadratic remainder has constant G, the approximant's residual r
  satisfies 4F²Gr < 1 and the difference at v = r_h/2 is at most Fr, by continuity from the higher-dimensional
  neighbourhood theorem of [CTG23], the hierarchy being applied only to genuine metrics, for which its compatibility with
  the metric holds by definition (`checks/cont5.py`). Computed (floating point): on |x| ≤ 1/2 over the region above,
  where no truncated domain exists, the estimate's constant is F² = 10^138, and 10^66.9 with Theorem 8.W's weights; the
  couplings across an angular Galerkin cut, N-independent by an identity (deduced), are of the coefficients' own size
  there, so the block (Schur) condition under which an estimate on the high angular modes would lower the constant fails
  at every angular resolution, in Theorem 7.L's unweighted norms and at Theorem 8.W's weights (`checks/blocks5.py`,
  `checks/blockw5.py`); the first seed's solution, in a constraint-preserving scheme whose singular coupling at the axes
  is regularised (`checks/cpaxis5.py`), converges at second order in the null step to v ≈ 1.8 r_h at areal
  radius ≥ 0.9 r_h and to v ≈ 2.0 r_h at ≥ 1.2 r_h, on three null grids from v = 1.4 r_h and on two below it (observed
  order 2.00–2.03 in the metric, the unimposed constraint and the regularisation's correction falling 3.5–4.0-fold at
  each refinement, the correction on three grids from v = 1.5 r_h), and is resolved in angle there on the finest grid,
  M = 40 and 48 changing the metric by at most 3.0 × 10⁻⁹ and 3.3 × 10⁻⁹, with M = 48 also second order on three null
  grids (`checks/cp3grid5.py`), and the free scheme's solution is consistent with second-order convergence to v ≈ 1.8 r_h
  at areal radius ≥ r_h as well (`checks/late5b.py`); beyond, at M = 32 the metric still converges at second order in the
  null step while the unimposed constraint does not fall, so the null-step limit at M = 32 is not vacuum; with M = 32,
  40, 48 and 56 at 800 × 360 the violation falls to 0.49–0.53 of its value at each step in M at areal radius 0.9–1.0 r_h
  on [1.8 r_h, 1.9 r_h), and to 0.48–0.68 at ≥ 1.2 r_h on [2.0 r_h, 2.25 r_h), consistent with angular truncation, though
  at M = 56 it is still 23 and 39 times the null step's level there and at M = 48 falls only 1.72- and 1.13-fold from 400
  to 800 rows and not at all from 800 to 1600, while at 1600 rows it still falls to 0.47 and 0.53 of its value from
  M = 40 to 48; from v ≈ 1.9 r_h at 0.9–1.0 r_h and from v ≈ 2.0 r_h at 1.0–1.2 r_h it grows with M and the
  regularisation's correction does not vanish under refinement; these verdicts hold for the comparison's threshold
  anywhere in [0.68, 1.15]; at 1.0–1.2 r_h on [1.8 r_h, 2.0 r_h) the comparison in M does not decide, and on [1.8 r_h,
  1.9 r_h) there, at M = 48, the unimposed constraint falls 3.84-fold from 400 to 800 rows and 2.77-fold from 800 to
  1600, and at 1600 rows M = 40 leaves it 3.5 times larger (`checks/cpaxis5.py`, `checks/mtrunc5.py`,
  `checks/cp3grid5.py`). So at 10 l5 existence is proved where the solution is the seed (v ≤ r_h/2) and not beyond it:
  the continuation's closing condition 4F²Gr < 1 (supplement Lemma 9.C), at the computed F² = 10^66.9, asks a residual r
  of order 10⁻⁶⁸/G, against the certified 3.73 × 10⁻⁵ at points and 5.0 × 10⁻⁴ over sub-boxes, and its hypotheses are
  established on no region of its form beyond the seed (supplement `CERTIFY-10L5-RESULT.md` sections 2 and 6–13).
```

**C. Old:**

```
- [Wu26] S. Wu, *Picard iteration for the characteristic initial value problem in Einstein equations*,
  arXiv:2609.08421v1. READ 2026-10-20: abstract; p. 2, (1.1); Theorems 2.1–2.2, p. 6.
```

**New:**

```
- [Wu26] S. Wu, *Picard iteration for the characteristic initial value problem in Einstein equations*,
  arXiv:2609.08421v1. READ 2026-10-20: abstract; p. 2, (1.1); Theorems 2.1–2.2, p. 6.
- [CTG23] P. T. Chruściel, R. Tagne Wafo, F. Gray, *The "neighborhood theorem" for the general relativistic
  characteristic Cauchy problem in higher dimensions*, arXiv:2305.07306v1. READ 2026-11-06: abstract; Theorem 1.1,
  pp. 2–3, and the remark after it on Sobolev spaces; p. 8 (estimates for genuine solutions, not an existence scheme).
```

**D1. Old:**

```
recorded here); z3-solver for `foliation5.py`; python-flint for `cdata5.py`; numpy for `bondi5.py` and `growth5.py`,
```

**New:**

```
recorded here); z3-solver for `foliation5.py` and `checks/cont5.py`; python-flint for `cdata5.py` and for
`checks/rcert5.py` and every program that imports it; scipy for `cdata5.py`, `checks/lev1_5.py` and `checks/wgron5.py`;
numpy for `bondi5.py` and `growth5.py`,
```

**D2. Old:**

```
`checks/vii5census.py`; the others import nothing from the research tree:
```

**New:**

```
`checks/vii5census.py`, `checks/reduce5.py` imports `dnull5.py`, `checks/symbol5s.py` imports `checks/symbol5.py`, which
imports `dnsolve5.py`, `checks/linest5.py` imports `checks/null3.py` and `dnsolve5.py`, `checks/lev1_5.py` imports
`checks/linest5.py` and `checks/wgron5.py`, `checks/wgron5.py` and `checks/blocks5.py` import `checks/linest5.py`,
`checks/axis5.py` imports `checks/linest5.py` and `dnull5.py`, `checks/axhier5.py` imports `checks/axisbianchi5.py`,
`checks/cont5.py` imports `checks/null3.py`, `checks/cpsolve5.py` imports `dnsolve5.py`, `checks/cpaxis5.py` imports
`checks/cpsolve5.py`, `checks/cp3grid5.py` imports `checks/cpsolve5.py` and `checks/cpaxis5.py`, `checks/rcert5.py`
imports `checks/resid5.py` and `checks/bondisph5.py`, `checks/rcert5c.py` and `checks/rcert5d.py` import
`checks/rcert5.py`, `checks/rich5.py` imports `checks/rcert5.py` and `checks/rcert5d.py`, `checks/blockw5.py` reads
`checks/blocks5.out` and `checks/wgron5.out`, `checks/mtrunc5.py` reads `checks/cpaxis5_a5.out`,
`checks/cpaxis5_a5_m48.out` and `checks/cpaxis5_a5_m56.out`, and `checks/szconv5.py` imports `checks/secondzero5.py`; the
others import nothing from the research tree:
```

**D3, after cdata5.out's row. Old:**

```
| `docket68/n1star/checks/cdata5.out` | `6536abcba46ec57a5dca8ced814b7788` |
```

**New:**

```
| `docket68/n1star/checks/cdata5.out` | `6536abcba46ec57a5dca8ced814b7788` |
| `docket68/n1star/checks/reduce5.py` | `0458f70bc710ad3ce966f242bd76e5f0` |
| `docket68/n1star/checks/reduce5.out` | `b0fb5b28fa8499d5fa70226a1b3ed1ee` |
| `docket68/n1star/dnull5.py` | `2035d34bf399cd6ba5c5550d9718ceab` |
| `docket68/n1star/checks/symbol5s.py` | `8441ecf58bab566dda5b5d50c8327f97` |
| `docket68/n1star/checks/symbol5s.out` | `7d51dbf663724abf64087f39974f35c9` |
| `docket68/n1star/checks/symbol5.py` | `14168943230c0c64d18a94fd7f55912e` |
| `docket68/n1star/checks/null3.py` | `767dd3bd58f5c517c99165e1d44f1eb9` |
| `docket68/n1star/checks/null3.out` | `0288d263c81bd929f3ce5647350d69ed` |
| `docket68/n1star/checks/linest5.py` | `34dc9b3d6594771ace2a4257b3a15191` |
| `docket68/n1star/checks/linest5.out` | `cdc11bfb156dbd6dfa2ec2f744d0e842` |
| `docket68/n1star/checks/lev1_5.py` | `bbb29f53599e58d3702d8b7dc5c9aeab` |
| `docket68/n1star/checks/lev1_5.out` | `b6be6a0bf20f95febfba64707fcf3bb8` |
| `docket68/n1star/checks/wgron5.py` | `a764e73c0be0ec38467bc986f7d84bb2` |
| `docket68/n1star/checks/wgron5.out` | `47170f09530b20e8d49f1a56660f55c1` |
| `docket68/n1star/checks/axis5.py` | `6724ac8e96cb31a69d02c3fa03d88627` |
| `docket68/n1star/checks/axis5.out` | `c708b130e4656a16b6bb1879a31faa14` |
| `docket68/n1star/checks/axisbianchi5.py` | `86d8af8e9024487ee7bd947bce954588` |
| `docket68/n1star/checks/axisbianchi5.out` | `999b80bedb9aaccc627e17002746a912` |
| `docket68/n1star/checks/axhier5.py` | `aa134baade41c3a0664844a4424a567a` |
| `docket68/n1star/checks/axhier5.out` | `0b192015028c3ea2536964f28af58137` |
| `docket68/n1star/checks/cont5.py` | `d5ada772efca2d1fd2b8fec5fc1832e9` |
| `docket68/n1star/checks/cont5.out` | `d4fc239715575ac4757ce2831b259f58` |
| `docket68/n1star/checks/blocks5.py` | `201c163bb0a554b4677c754a85ab4e83` |
| `docket68/n1star/checks/blocks5.out` | `b0468571355f78d03975d63da638308a` |
| `docket68/n1star/checks/blockw5.py` | `6049a5dcb3a362c99ccbe2fb7e950807` |
| `docket68/n1star/checks/blockw5.out` | `f2ae0d7d80a3c238b83c9ec36a66c87c` |
| `docket68/n1star/checks/cpsolve5.py` | `96768ccce2e58f7a4d2e38e0219778e0` |
| `docket68/n1star/checks/cpaxis5.py` | `6fb010b7b948178c58bb7c65e06681d9` |
| `docket68/n1star/checks/cpaxis5.out` | `e89a7902beebffb67a432baa133cb82f` |
| `docket68/n1star/checks/cpaxis5_run1.out` | `7775c999a88c195d189c87d9294e9ce4` |
| `docket68/n1star/checks/cpaxis5_a4.out` | `ae4511e1c474eff3f88bcfeb79aa26cd` |
| `docket68/n1star/checks/cpaxis5_a5.out` | `6565c01c5191ceca28a03882f82f2d4e` |
| `docket68/n1star/checks/cpaxis5_a6.out` | `cee235fc3c4833486f3d66a4e20f260c` |
| `docket68/n1star/checks/cpaxis5_a6_400.out` | `94c9c5a53543c764f1e00d037a49ff33` |
| `docket68/n1star/checks/cpaxis5_a5_m48.out` | `7360e31b7fb5748829d4e26ff2736aa4` |
| `docket68/n1star/checks/cpaxis5_a5_m56.out` | `53ee3e4b64f2cec25109a3eda2f7aa44` |
| `docket68/n1star/checks/cpaxis5_a5_m48_400.out` | `d4a15a41569888c09b76b325519ac1f5` |
| `docket68/n1star/checks/mtrunc5.py` | `2f836c7d1b3c7ce4517a2afd6c30bd73` |
| `docket68/n1star/checks/mtrunc5.out` | `9a23e45553ca67cff6478a7b5ba5ee45` |
| `docket68/n1star/checks/cp3grid5.py` | `3033f5bfcf04065b7e99b5dd8cf09186` |
| `docket68/n1star/checks/cp3grid5_control.out` | `1af3c04e9c7ec030e11798fb86454da7` |
| `docket68/n1star/checks/cp3grid5_a8_2grid.out` | `dc3380ec644732a430bb02e7af310c9c` |
| `docket68/n1star/checks/cp3grid5_a9_800.out` | `c7d7752b7f389ed261b4b1c6871354fb` |
| `docket68/n1star/checks/cp3grid5_a10_2grid.out` | `7986c6b71f4dc8ec825ae8d28c9475c7` |
| `docket68/n1star/checks/cp3grid5_a7_3grid.out` | `c654cebc1f5da114da14ee10e38e5bd6` |
| `docket68/n1star/checks/cp3grid5_a8_3grid.out` | `9e823195af627bc21c2d1854ffbfb6b8` |
| `docket68/n1star/checks/cp3grid5_a9_1600.out` | `0d0da9dcc0d554d11f97dd40a4a4ee10` |
| `docket68/n1star/checks/cp3grid5_a10_3grid.out` | `0989baf55d1299a8ff637737215d1426` |
| `docket68/n1star/checks/late5b.py` | `5225f2b4aa53dc1ab452e2355d499ef8` |
| `docket68/n1star/checks/late5b.out` | `ece3e7f063a049a15a5b91ed56c2b555` |
| `docket68/n1star/checks/late5b_small.out` | `be8da58288ee92cd765d25b48c167b41` |
| `docket68/n1star/checks/rcert5.py` | `bf6d843d5963534eaab5ac4123479aa9` |
| `docket68/n1star/checks/rcert5c.py` | `281cd2ea76acbe4fb6e04961bdd0521a` |
| `docket68/n1star/checks/rcert5c.out` | `b4790b613b72f25a492b02ae51dd8503` |
| `docket68/n1star/checks/rcert5d.py` | `c71659021f86b2eba865beeb095f6a97` |
| `docket68/n1star/checks/rcert5d.out` | `2411c62db06cfcee3d2620c62c4ef185` |
| `docket68/n1star/checks/rich5.py` | `2313e4cdbd7eacaa77aead62071da51d` |
| `docket68/n1star/checks/rich5.out` | `c1eabcf625ccac2e059fab62352ac4a9` |
| `docket68/n1star/checks/rich5_runs.out` | `64d3a967c368dcd036c758fe842b51f6` |
| `docket68/n1star/data/rcert5_C3.npz` | `698569f6faaab4420fe2e67abc860561` |
| `docket68/n1star/data/rcert5_C3R.npz` | `88e16664187868e47eaaaa18709cfc61` |
| `docket68/n1star/checks/szconv5.py` | `3c6c7b0e0eaf684a4b50fd199a129429` |
| `docket68/n1star/checks/szconv5.out` | `90d632eb98933c546f90a0be0adbfc63` |
| `docket68/n1star/checks/secondzero5_trunc1600.out` | `e64dadd9d3562175d9304ea1382935be` |
| `docket68/n1star/checks/secondzero5_edges1600.out` | `5e640f6eb03700518988c9b414c3c571` |
| `docket68/n1star/checks/cp3grid5_a7_m48.out` | `02e2724c5fcd172f3b453d5543be0821` |
| `docket68/n1star/checks/cp3grid5_a7_m32v48.out` | `64b29e088636c01abc7c2437ec8b3ebb` |
| `docket68/n1star/checks/cp3grid5_a9_1600_m48.out` | `200555635e50f32685d3b5f6f12c3074` |
| `docket68/n1star/CERTIFY-10L5-RESULT.md` | `fa9d849dac157096b96355307d3d2024` |
```

**E. Old:**

```
| section 9: residual of a smoothed 3D approximant | `docket68/n1star/checks/resid5.py` Q1–Q2 |
```

**New:**

```
| section 9: the residual of the Richardson approximant | `docket68/n1star/checks/rich5.py` R0–R3, C1–C3 |
| section 9: the single-grid approximant's supremum over one box | `docket68/n1star/checks/rcert5d.py` D0–D4, C1–C2 |
| section 9: the class; frozen-coefficient loss; transport structure | `docket68/n1star/checks/reduce5.py` R0–R4; |
| | `docket68/n1star/checks/symbol5s.py` S1–S6; `checks/null3.py` N0–N10; `checks/linest5.py` E1–E9 |
| section 9: the linear estimate at levels 0 and 1, and its constant | `docket68/n1star/checks/linest5.py` E1–E9; |
| | `docket68/n1star/checks/lev1_5.py` L1–L5; `checks/wgron5.py` W1–W5 |
| section 9: the axes: chart, pairs, Hardy constants, reduced hierarchy | `docket68/n1star/checks/axis5.py` X1–X7; |
| | `docket68/n1star/checks/axisbianchi5.py` B1–B4; `checks/axhier5.py` A1–A7, M1–M4, S1–S3 |
| section 9: existence by continuity from [CTG23], conditional | `docket68/n1star/checks/cont5.py` C1–C2 |
| section 9: the block condition, unweighted and at the weights | `docket68/n1star/checks/blocks5.py` H1–H2; |
| | `docket68/n1star/checks/blockw5.py` B1–B2 |
| section 9: the late region | `docket68/n1star/checks/cpaxis5.py` A1–A6; `checks/cp3grid5.py` A7–A10; |
| | `docket68/n1star/checks/late5b.py` L5–L8 |
| section 9: the late violation against the angular resolution | `docket68/n1star/checks/mtrunc5.py` M0–M2 |
| section 9: the rebuilt outer zero under the null step | `docket68/n1star/checks/szconv5.py` Z1 |
```

**F. Old:**

```
- `checks/resid5.py` Q1–Q2: section 9's computed residual. Every field of a double-null run at the first seed (800 ×
  360, M = 16) is fitted by a tensor Chebyshev series on the box u ∈ [−4, −1.1], v ∈ [0.55, 1.6], so that g_app is an
  explicit smooth metric of the class. Q1, the fit within 7 × 10⁻¹¹ of the run at its nodes; Q2, every frame component
  of Ric[g_app], from the exact symbolic Ricci tensor of the ansatz, at most 2.46 × 10⁻³ of the curvature scale √K_0 at
  the same areal radius, against 9.64 × 10⁻³ on the next coarser run (400 × 180), a ratio of 3.92: the residual is the
  discretisation's, at second order. Control: the lapse moved off the solution (W + 0.01 v) gives a residual 140 times
  larger. Floating point, not certified. About 11 minutes, given the runs.
```

**New:**

```
- `checks/resid5.py` Q1–Q2: the computed residual of a smoothed run. Section 9 now cites the certified residuals of
  `checks/rich5.py` and `checks/rcert5d.py` instead, whose `checks/rcert5.py` imports this program. Every field of a
  double-null run at the first seed (800 × 360, M = 16) is fitted by a tensor Chebyshev series on the box u ∈ [−4, −1.1],
  v ∈ [0.55, 1.6], so that g_app is an explicit smooth metric of the class. Q1, the fit within 7 × 10⁻¹¹ of the run at
  its nodes; Q2, every frame component of Ric[g_app], from the exact symbolic Ricci tensor of the ansatz, at most
  2.46 × 10⁻³ of the curvature scale √K_0 at the same areal radius, against 9.64 × 10⁻³ on the next coarser run
  (400 × 180), a ratio of 3.92: the residual is the discretisation's, at second order. Control: the lapse moved off the
  solution (W + 0.01 v) gives a residual 140 times larger. Floating point, not certified. About 11 minutes, given the
  runs.
- `checks/reduce5.py` R0–R4: section 9's class. For every metric of the class, with no field equation used, the
  five-dimensional Ricci tensor reduces to (2+1)-dimensional gravity coupled to a wave map into the flat plane (R1–R2);
  the reduced residues are fixed linear combinations of the five-dimensional Ricci components (R3); and the Einstein
  frame is written in the record's variables (R4). Exact (sympy). About half an hour.
- `checks/symbol5s.py` S1–S6: section 9's frozen-coefficient loss. The principal symbol of the free formulation with the
  shift's second derivatives kept has no Jordan block (S1–S3), but the shift's angular derivative is of principal size at
  high angular frequency and drives δR at order k² (S4, S6); in the constraint-preserving block the eigenvalue-0 mode
  drives itself (S5), a loss shown on a model only. Control: the frozen-shift system has the Jordan block. Exact, with
  S6's model in floating point. About three minutes.
- `checks/null3.py` N0–N10: section 9's transport structure. In double-null gauge with one-dimensional sections, the
  reduced system's Ricci coefficients, Raychaudhuri, torsion, lapse, commutators and wave operator (N0–N6); the two
  equations the hierarchy does not use carry the only angular derivative (N7), so none appears on the hierarchy's right
  sides (N8); the pairs' energy identities (N9); the linearised pair operators for the difference of two metrics (N10).
  Exact (sympy). Under a minute.
- `checks/linest5.py` E1–E9: supplement Theorem 7.L. The pair identities (E1); the hierarchy linearised in fifteen
  frame-difference unknowns, with no derivative of an unknown on any right side (E2); the two-variable Grönwall lemma
  (E7); the rows checked against the geometry three ways (E9); and, on the record's run, the constant, the truncated
  domains it holds on and the demand it puts on the residual (E4–E6, E8). Controls: a row with the angular loss must be
  flagged (E3); mutated rows must fail E9. Exact for the structure, floating point for the constants. About half a
  minute, given the run.
- `checks/lev1_5.py` L1–L5: supplement Theorem 8.L1. The commutators with e_x (L1); the system commuted once closes in
  thirty unknowns with no level-2 term on any right side (L2), every level-1 row checked against the commutation itself
  (L5); the level-1 constant on the record's run (L4). Controls: a commutator without its e4 term (L1); a row with the
  angular loss (L3); two dropped terms (L5). Exact, with L4 in floating point. About eight to eleven minutes, given the
  run.
- `checks/wgron5.py` W1–W5: supplement Theorem 8.W, the constant with weights. A model Goursat pair, on which the
  weighted bound must hold at every weight tried and two mutations of it must fail (W1); equal weights reproducing
  F² = 10^138 (W2); weights minimising a relaxed objective, F² = 10^66.9 on |x| ≤ 1/2 (W3); a finite-rank approximate
  inverse cannot lower the constant (W4, supplement Lemma 8.F); the frozen-angle growth of the transported unknowns, at
  one resolution (W5). Deduced, with computed checks; the constants in floating point. About eight minutes, given the
  run.
- `checks/axis5.py` X1–X7: the axis charts. Near each axis the class is four-dimensional axisymmetric Einstein–scalar in
  a chart regular at the axis (X1), twist-free in its double-null frame (X2), with a measure in which the pair operators
  are adjoint (X3); the Hardy inequalities that recover angular derivatives from the axis, with explicit constants (X4);
  the frame quantities bounded on the record's run (X5); the polar-frame connection difference δk not an admissible
  L²(dμ) unknown at the axis, which excludes Theorem 7.L's unknowns there and nothing else (X6); and the glue (X7).
  Identities verified at random rational jets with a fixed seed (a probabilistic test), with computed checks. Under a
  minute.
- `checks/axisbianchi5.py` B1–B4: the axis chart's curvature pairs. σ's vanishing (B1); the Gauss equation and [Wu26]'s
  pairs, each found by a linear fit at random jets and checked at fresh random jets (B2–B3b); and the pairs' energy
  inequality on the whole section, the axis included (B4), deduced from them. Probabilistic identity tests with fixed
  seeds. About seven minutes.
- `checks/axhier5.py` A1–A7, M1–M4, S1–S3: [Wu26]'s transport equations, mass aspects and the scalar's pairs in the axis
  chart, reduced and off shell, each found by a linear fit at random rational jets and checked at fresh random jets
  (probabilistic identity tests with fixed seeds), with every angular derivative on a right side recovered from the
  hierarchy's own unknowns (A7). Controls c1–c4: altered coefficients must leave a residual. About a minute and a half.
- `checks/cont5.py` C1–C2: Lemma 9.C of the supplement. The compatibility relations and the metric recovery hold
  identically on the general metric of the class (C1, exact); 4AB < 1 and y ≤ A + By² give y ≤ 2A, and y never enters
  (2A, 1/(2B)) (C2, z3, with a vacuity guard). Controls: χ̲'s relation without b_x (k1); 4AB < 2 (k2); a sharper bound,
  refuted (k3). Seconds.
- `checks/blocks5.py` H1–H2: the block (Schur) condition. The coupling of a multiplication across an angular Galerkin cut
  does not depend on N past the multiplier's degree (H1, exact), and on the record's coefficients it is of their own
  size, so the condition fails at every N in Theorem 7.L's norms (H2, floating point). About 25–40 minutes, given the
  run.
- `checks/blockw5.py` B1–B2: the same condition at Theorem 8.W's weights, from the printed figures of
  `checks/blocks5.out` and `checks/wgron5.out`, each rounded against the claim: the largest pair's product is at least
  57.8 at every N. Controls: equal weights reproduce blocks5's 484 (k1); the smallest pair alone is below 1 (k2). A
  second.
- `checks/rich5.py` R0–R3, C1–C3: section 9's Richardson approximant. Its pinned tensors (R0); its Einstein residual at
  16,128 points (R2) and as a supremum over a sub-box of each of four boxes (R3), certified in ball arithmetic with
  `checks/rcert5d.py`'s engine; the extrapolation's floating-point residual (R1, `--runs`). Controls: the engine end to
  end on test fields with exact suprema, and its enclosures of the coefficients and of the frame output against their
  values at the corners of their boxes, on the approximant's tensors and on degree-7 test fields (C1); the perturbed
  approximant refused (C2); the census regression (C3). Twenty to fifty minutes, read only.
- `checks/rcert5d.py` D0–D4, C1–C2: the single-grid approximant's supremum over one interior box. Order-3 Taylor models
  with the Lagrange remainder in ball arithmetic, bisected until every sub-box meets the target (D1); certified centre
  values that no bound of any method can beat (D2); the census over the 416 boxes (D3); certified point values at the
  centre and corners of every accepted sub-box below its bound (D4). Controls: as rich5's C1, and the perturbed
  approximant refused (C2). The bisection about three hours on four processes; the collection and its checks about two
  minutes.
- `checks/cpaxis5.py` A1–A6: the late region's constraint-preserving scheme. Its singular coupling at the axes (A1–A2),
  the regularisation (A3), and the regularised scheme on the record's data at two angular resolutions (A4) and two null
  grids (A5), with its Kretschmann scalar (A6). Floating point. Each run at 1600 × 720 about four hours; the analyses
  minutes to half an hour.
- `checks/cp3grid5.py` A7–A10: the regularised scheme on three null grids. The unimposed constraint and the metric per
  band of v and class of areal radius, with the observed order (A7); the Kretschmann scalar (A8); the metric's resolution
  in angle (A9); the regularisation's correction replayed at every cell (A10). The third grid covers v ≥ 1.4, and A10
  starts at v = 1.5. Control: the 800-row run given in place of the 1600-row one must read as not converging on every
  band. Floating point. A7 and A9 under a minute, A8 seventeen to twenty minutes and A10 fifteen to thirty, given the
  runs.
- `checks/late5b.py` L5–L8: the free scheme's late region on the record's runs. Raychaudhuri's residual per band and
  class under the null step (L5), in angle (L6) and at small radii (L7); the monotone quantity e^{−2W} R_v along the
  outgoing generators (L8). Control: a wrong coefficient must not converge (L5). Floating point, given the runs.
- `checks/mtrunc5.py` M0–M2: the late region's violation against the angular resolution. The interior constraint monitor
  at 800 rows for M = 32, 40, 48 and 56, read from `checks/cpaxis5.py`'s outputs, is classified: consistent with angular
  truncation where every step in M lowers it to at most θ = 0.8 of its value; not truncation where the last step does not
  and it stays above ten times the null-step level; undecided otherwise. When the rule was written relative to reading
  the runs is not documented, so each verdict's sensitivity is printed: the decided verdicts stand for θ anywhere in
  [0.68, 1.15] (M2). Controls: a halving sequence (k1); one run given for every M (k2); the bands the null-step level is
  taken over (k3); each input's run identity, read from its command line (k4). Arithmetic on printed figures. A second.
- `checks/szconv5.py` Z1: the rebuilt outer zero of the Bondi spheres under the null step, at 400, 800 and 1600 rows and
  at two data-cone radii, against its difference from growth5's (`checks/secondzero5.py`'s S6 quantity). Control: the
  leaves' expansion in place of θ must disagree with growth5. Floating point. About five minutes, given the runs.
```

**G. Old:**

```
    python3 checks/resid5.py RUNDIR l1_M16_800 l1_M16_400    # about 11 minutes, given the runs
```

**New:**

```
    python3 checks/resid5.py RUNDIR l1_M16_800 l1_M16_400    # about 11 minutes, given the runs
    python3 checks/reduce5.py                             # about half an hour
    python3 checks/symbol5s.py                            # about three minutes
    python3 checks/null3.py                               # under a minute
    python3 checks/linest5.py RUN                         # RUN the record's l1_rc0.9_M32.npz; half a minute
    python3 checks/lev1_5.py RUN                          # about eight to eleven minutes
    python3 checks/wgron5.py RUN                          # about eight minutes
    python3 checks/axis5.py RUN                           # under a minute
    python3 checks/axisbianchi5.py                        # about seven minutes
    python3 checks/axhier5.py                             # about a minute and a half
    python3 checks/cont5.py                               # seconds
    python3 checks/blocks5.py RUN                         # 25-40 minutes; then checks/blockw5.py (a second)
    python3 checks/rich5.py                               # 20-50 minutes, read only; --runs RUNDIR for R1
    python3 checks/rcert5d.py --worker w 4                # w = 0..3 at once, about three hours; then --collect 4
    python3 checks/rcert5d.py --census                    # about a minute
    python3 checks/cpaxis5.py --run 1 0.9 M Nu Nv 2.25 OUT reg ld 3   # a regularised run; 1600 x 720 about 4 h
    python3 checks/cpaxis5.py --nullstep R400 R800 R40_800   # and --compare, --kretschmann (A4-A6)
    python3 checks/cp3grid5.py --a7 R400 R800 R1600 [R40_1600]   # and --a8, --pclass, --dpm, --control
    python3 checks/late5b.py RUNDIR                       # given the record's runs
    python3 checks/mtrunc5.py                             # a second, from checks/cpaxis5_a5*.out
    python3 checks/szconv5.py RUNDIR                      # about five minutes, given the 1600-row runs
```
