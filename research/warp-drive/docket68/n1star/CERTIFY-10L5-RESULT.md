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
     that gauge. No section of an ingoing cone whose
     expansion is ≥ 0 at its innermost point has that point at u > −1. In particular this holds for every
     marginally outer trapped surface (MOTS).
   - *Computed:* the leaves' expansion has one zero per angular node along every ingoing cone of the converged
     region. Every MOTS of the exact solution on that cone is then confined to a band of width 0.003–0.007 in u at
     areal radius 1.01–1.05 (seed 1, v ≤ 1.75).
   - *Computed:* the Bondi spheres rebuilt from the double-null solution reproduce `growth5.py`'s zero structure: the
     dip of the outer zero, and angular columns with no zero at all on r ≥ 0.64 from v ≈ 1.40 (`growth5`: 1.419),
     28 % of the columns at v = 1.50 against 29 %. As the data cone moves out from R0 = 10 to 20, the rebuilt outer
     zero moves to within about 0.03 of `growth5`'s.
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
3. **The late region is not classified.**
   - *Computed:* from v ≈ 1.65 at seed 1 (M = 16) the computed fields violate the Raychaudhuri constraint by the size
     of its own terms. Away from the cut they also violate D1's exact monotonicity. So they are not an approximation
     of any vacuum solution there.
   - *Computed:* the gauge indicators stay moderate (|W| ≤ 1.25, |P + Q| ≤ 0.15). So the failure is not a caustic of
     the outgoing cones, nor a collapse of the lapse.
   - Kretschmann blow-up against a smooth steep feature remains undecided (section 3).

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
- A MOTS of C_v has θ_leaf ≥ 0 at its innermost point and θ_leaf ≤ 0 at its outermost point. So it lies between the
  least and the greatest u of the leaves' zero set on C_v. This is the double-null form of `hf_mirror5.py` X10's
  remark for the Bondi slices.

**What D1–D2 assume.** A smooth vacuum solution in this double-null gauge on the region considered. That is the
existence question itself, so D1–D2 are statements about the exact solution wherever it exists, not an existence
result.

### 1.3 The leaves in the runs (computed, `checks/secondzero5.py` S1–S2)

The runs are at seed 1, cut 0.3: 200 × 90, 400 × 180 and 800 × 360 at M = 16, and 800 × 360 at M = 24. There are
two at seed 2, cut 0.18. Results are in `checks/secondzero5.out`.

- **S1.** On v ≤ 1.8, every kept cell with u > −1 and at least Nu/40 rows from the cut has R_v < 0. The violations of
  D1 all lie within Nu/40 rows of the cut: 12, 429 and 552 cells at 200, 400 and 800 rows.
  - *Control.* The same test over u > −1.02 fails.
  - *Beyond v = 1.8.* At 800 × 360, 1,822 far violations on (1.8, 2], all from v ≈ 1.9: the unconverged region of
    section 3.
- **S2.** Every second or further zero of R_v along an ingoing cone at a node, for v ≤ 1.8, lies at u > −1 within
  Nu/40 rows of the cut. They first appear at v = 1.525–1.65, at alternate angular nodes, and last one or two columns.
  By D1 none is the exact solution's.
  - *Control.* Applied to the first zero, the classifier must place it away from the cut, and it does.
- **The band.** The leaves' one zero per node, the marginal leaf, lies at
  - seed 1 (800 × 360, M = 24): u ∈ [−1.0070, −1.0035] and areal radius at the node 1.013–1.024 at v = 1.5;
    [−1.0121, −1.0056] at v = 1.75; M = 16 agrees to 3 × 10⁻⁵ in u;
  - seed 2 (M = 16): [−1.0029, −1.0014] at v = 1.5 and [−1.0080, −1.0036] at v = 1.9.

  By D2 every MOTS of these cones lies in that band, near areal radius 1.01–1.05. The Bondi second zero sits near the
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

| v | 200, R0 = 10 | 400, R0 = 10 | 800, R0 = 10 | 400, R0 = 20 | 400, R0 = 40 |
|---|---|---|---|---|---|
| 1.0 | 0.005 | 0.004 | 0.004 | see .out | see .out |
| 1.2 | 0.026 | 0.029 | 0.024 | 0.014 | see .out |
| 1.3 | 0.054 | 0.076 | 0.051 | 0.029 | see .out |
| 1.35 | 0.052 | 0.068 | 0.082 | 0.031 | see .out |
| 1.375 | — | 0.081 | 0.110 | 0.024 | see .out |

The R0 = 20 column is read off the per-column table in section 4; the .out has the max line per run.

- **What the difference is.** At fixed R0 = 10 the difference does not fall with resolution. At fixed resolution it
  falls by a factor 2–4 when the data cone moves from R0 = 10 to 20.
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
  in the double-null rebuild, whose R0 = 10 dip is the deeper one (see S4).
- The excision radius 0.54 itself is not reached before the cut at these grids. Over r ≥ 0.54 `growth5`'s first
  zero-less column is at v = 1.4355.
- *Seed 2 (400 × 180, M = 16).* The rebuilt outer zero agrees with `growth5`'s deep run L1000_lam0.3162_20x16_d0_y2.2
  to 0.003, 0.007, 0.012, 0.020, 0.022 and 0.026 at v = 1.0, 1.2, 1.3, 1.4, 1.45 and 1.5.
  - But there S4's control passes: the leaves' expansion is within 0.069. Before v = 1.5 the tilt is too small at
    seed 2 to separate the two, so S4 is not informative there and is recorded as FAIL.
  - Columns with more than one zero of θ (r ≥ r_min ≈ 0.59–0.63) first appear at v = 1.575: 2 of 32 there, 5 at 1.60
    and 7 at 1.625, with inner zeros at r = 0.63–0.79. `growth5`'s second zero at seed 2 is from v = 1.583, at its
    excision radius 0.30, which the rebuild does not reach.

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
  - any MOTS lies in a thin band at areal radius ≈ 1.01–1.05 (D2 and S1–S2).
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
| 2 | 288 × 64 | see .out | see .out | see .out |

*The bound's order.* The mean-value enclosure is of second order in the box size: halving both widths divided the
bound by 4.0, 8.4 × 10⁻⁴ → 2.1 × 10⁻⁴ at 48 × 16 → 96 × 32. So the certified sup lies far above the residual itself,
which the certified point values at the centres show.

*Control.* Perturbing the fitted coefficients by 10⁻⁶ must raise the bound a hundredfold.

*What this is.* A certified data error for the Raychaudhuri constraint of the record's truncated characteristic
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
- every MOTS of an ingoing cone has its innermost point at u ≤ −1 (D2).

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
  [1.9, 1.975) is 1.84, 8.4 and 13.5 against 3.19, 14.9 and 55. It is smaller at the finer angular grid, but stays of the order of
  the terms. The maximum on [1.65, 1.8) is at u = −0.978, x ≈ −0.85, areal radius at the node 0.80, v = 1.79, at both M:
  inside the seed's horizon generator, toward the axis x = −1 where the record's angular failure begins (D351–D418).
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

1. **F5 first.** Write the linear estimate for the linearised double-null system in the class with explicit constants
   (energy on characteristic rectangles, Sobolev on the 1D orbit sections, in the axis-regular variables). Until it
   exists, no amount of certified residual decides existence (section 2.3).
2. **For the certificate itself.** Third-order Taylor models in place of the mean-value form; and Ric_vx on the data
   cone, then the data at past null infinity (G3).
3. **For the late region.** A run that imposes or damps the Raychaudhuri constraint (or a constraint-preserving
   formulation), to see whether the onset at v ≈ 1.65–1.9 moves. A fixed point of the onset under refinement would point
   to the solution; a moving one to the scheme.
