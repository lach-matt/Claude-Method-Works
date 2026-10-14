# The large hole's interior (item 360)

M chose to settle O1b and O1c at the large end by computing the large brane hole's interior (item 360,
M-COMPUTE-THE-INTERIOR). No source computes it: Figueras-Wiseman (1105.2558) and Abdolrahimi et al. (1206.0708)
build only the exterior, and Wang-Choptuik (1604.04832) and Emparan et al. (2301.02587) excise it. The build
starts from the large-hole limit, Figueras, Lucietti and Wiseman's AdS5-CFT4 solution with Schwarzschild boundary
(1104.4489, FLW), which the RSII holes approach as r0/ell grows (FW, READ).

## Stages

- **A. The static exterior (done, 2026-10-13).** FLW's ansatz (4.6), ell = R0 = 1, Einstein-DeTurck equation with
  their reference metric (4.14) and boundary conditions (4.9)-(4.12), solved by Newton on a Chebyshev-Gauss-Lobatto
  grid in (r, x) with an exact Jacobian. Regularity at the horizon r = 0 is T = A (the boundary metric's period
  4 pi R0); on the axis S = B.
- **B. The interior.** The functions are smooth in s = r^2; for s < 0 the same equations are the Lorentzian
  interior, an evolution in s from the horizon inward.
- **C. The brane and the Planck curvature.** The brane at z = eps (FW's construction), and the evolution followed
  until the curvature reaches the five-dimensional Planck scale, where 273's region begins (360 (c)).

## Stage A: what was computed and checked

| N | max residual | phi_max = xi.xi | T(0, 0) |
|---|---|---|---|
| 8 | 9.1e-12 | 8.6e-2 | 0.0686080 |
| 12 | 1.1e-11 | 1.7e-3 | 0.0677620 |
| 16 | 2.7e-11 | 8.0e-5 | 0.0676829 |
| 20 | 4.0e-11 | 3.2e-6 | 0.0676839 |
| 24 | 6.8e-11 | 2.3e-8 | 0.0676840 |

Checked against what is READ:
- phi_max falls exponentially with N, as FLW's Fig. 3: the solution is Einstein, not a Ricci soliton.
- FLW's (4.15): (1 - T)/(1 - x^2)^2 -> 1 - r^2 at the boundary, reproduced to six digits for r >= 0.7.
- FLW's Fig. 7: t4(R) R -> -1/4 at large R; computed -0.221, -0.268, -0.283, -0.271 at R = 2.0, 2.8, 5.3, 10.3,
  approaching it.
- The Weyl length (C^2)^(-1/4): minimum 0.1977 (N = 20), 0.1968 (N = 24), at the horizon-axis corner; FLW's value
  as Abdolrahimi et al. report it, 0.198 (their own 0.206).

Files: `gen_eqs.py` (the equations, symbolic), `solver.py` (Newton), `run_conv.py` (N = 8-24 and phi_max),
`check_asym.py` (4.15 and t4), `gen_kretsch.py` and `weyl.py` (the Weyl length). Generated `.pkl` and `.npy` files are
not kept; `gen_*.py` regenerate them in a few minutes.

## Stage B: what has been computed (2026-10-13, items 361-362)

**B1. The exterior in s = r^2.** In (s, y = x^2) the horizon's regularity T = A comes out with no condition imposed
(Radau nodes excluding s = 0; T - A on the horizon to 1e-9), but the axis condition S = B does not, and y resolves the
horizon-axis corner poorly (T(0,0) 0.067526, 0.067666, 0.067682 at Ny = 20, 28, 36). Writing S = B + y W made it worse.
In (s, x) -- Radau in s, Lobatto in x with stage A's axis rows -- the exterior converges to stage A's solution:
T(0,0) = 0.0676839991 at Ns = 28 against 0.0676839985 in (r, x) at N = 32, phi_max 3.4e-9.

**B2. The interior against the AdS boundary: unstable.** Marching the same equations into s < 0 by the method of lines
(Lobatto in x, Dirichlet at the AdS boundary) blows up within Delta s = 0.02. The linearised system's growing modes
sit in F at the nodes nearest the AdS boundary (x = 0.990, 0.962, 0.916), growing about 610 per unit s, in +/- pairs:
a spurious mode of a plain Dirichlet row at a singular boundary, not the physics (the continuum problem is
hyperbolic there: with s = -rho^2 the radial part changes sign).

**B3. Figueras-Wiseman's RSII problem instead.** FW's ansatz (9), Delta = 1/bt + (1 - x^2)/(1 - s) -- FLW's z shifted
by the brane depth 1/bt -- with the brane at x = 1 carrying FW's conditions: vacuum Israel K_ab = gamma_ab for the
outward normal (the sign fixed on the AdS slice), xi^x = 0 and F = 0. This removes the AdS boundary and is the
physical large end. Static holes (N = 24): R4/ell = 1.1293 (bt = 1), 1.611, 2.095, 3.073, 4.060, 5.050, 6.040, 8.021,
10.025, 11.984, 15.006, 20.019 (bt = 1.5 ... 20), phi_max 1e-9 to 3e-4 (the largest needing more resolution, as FW
say). READ against FW's Fig. 4: their solutions R4/ell = 1.13 and 5.04/5.08 (caption/legend), ours 1.129 and 5.050.

**B4. The brane-bounded interior: stable and converged.** With the brane rows solved at each evaluation (with F = 0 and
F_s = 0 on the brane the Israel rows and xi^x carry no s-derivatives, so they fix the brane values; the brane's
s-derivatives follow by implicit differentiation) the evolution is stable. Starting data matter: extrapolating the
static solution's degree-24 polynomial to s = -0.02 put phi at 6.8e-2; a second-order Taylor start from s = 0 at
s0 = -0.002 puts it at 7.6e-6. From there to s = -0.3 at bt = 1: Nx = 16 and 20 agree to six digits (T on the axis
0.110627 at s = -0.3 in both); phi rises to 5.4e-4 at both resolutions and flattens (the starting data's, not a
growth); T stays positive (axis 0.186 -> 0.111, brane 0.740 -> 0.603): no inner horizon in that range.

Files added: `gen_eqs_sy.py`, `core_sy.py`, `solver_sy.py`, `gen_eqs_syw.py`, `gen_eqs_sx.py`, `core_sx.py`,
`solver_sx.py`, `interior2.py`, `short_run.py`, `eig_diag.py` (B1-B2); `gen_eqs_fw.py`, `core_fw.py`, `solver_fw.py`,
`fw_scan.py`, `fw_eval.py`, `interior_fw.py`, `phi_start.py`, `gen_kretsch_fw.py` (B3-B4).

## Stage B, continued (2026-10-13, item 362)

**B5. The deep interior at bt = 1, and what limits it.** Run to s = -3 at Nx = 16 and 20, the brane solve marched in
order from the static brane values (warm-starting it from a later state finds another root: T(brane) = 39.8, K ~ 1e45,
garbage). The DeTurck norm phi = g_ab xi^a xi^b, zero for an Einstein metric, is the test:

| s | phi_max, Nx = 16 | phi_max, Nx = 20 | where |
|---|---|---|---|
| -0.002 | 7.6e-6 | 7.6e-6 | near the axis |
| -1.0 | 3.6e-3 | 7.6e-4 | brane (16), axis (20) |
| -1.6 | 3.8e-2 | 9.5e-4 | brane |
| -2.2 | 3.9e-1 | 4.2e-2 | brane |
| -3.0 | 2.9e+1 | 7.6e-1 | brane |

The metric functions agree between the two resolutions at s = -3 (T on the axis 1.3675e-2 against 1.3676e-2, on the
brane 0.17151 against 0.17156; A on the axis and B on the brane differ by 4 and 2 per cent), but the brane's
Kretschmann scalar does not (591 against 92.5 at s = -1.1): the growth at the brane is not physics. The linearised
right-hand side has no fast brane mode (its most negative Re mu, growth toward decreasing s, is -1.0 to -1.5, an F mode
near the axis; `eig_brane.py`); the fields' Chebyshev tails in x rise from 1e-6 at s = -0.3 to 5e-5 at s = -1.6 and
1e-3 at s = -3 (`cheb_tail.py`). The blow-up is loss of x-resolution, delayed by resolution. Trusted range at Nx = 20:
s >= -1.6.

Constraint damping (`gen_damp_fw.py`, `interior_damp.py`): kap [n_(a xi_b) - (1/3) g_ab n.xi] with n unit, future
directed (decreasing s) and tilted toward the bulk so that Codazzi's Robin condition on xi_s at the brane falls below
the threshold of the brane-bound zero mode (in RS-AdS that mode is exactly the brane's translation Killing vector, a
static solution of the constraint system satisfying xi^x = 0 and Codazzi's condition). 1 + rho = 2/3 makes the
principal constraint system triangular and damped in five dimensions. At kap = 4, tilt 0.5, Nx = 16: phi at s = -0.3
is 9.3e-5 against 5.5e-4 undamped (the bulk is damped), but the brane growth starts as before (1.5e-2 at s = -1.24).
xi from the new generator equals eqs_fw's phi to 7e-16 (`xi_check.py`).

**B6. The chart ends before the singularity.** Across every x the lapse of the s-slices falls as |s|^-2.1 (brane
0.144 at s = -1, 0.0138 at s = -3; near the axis 0.0354 and 0.00334), so s = -infinity lies at finite proper time from
the bifurcation surface: about 0.26 ell near the axis and about 1.07 ell on the brane (estimate, from the power law).
Over the trusted range the curvature there is finite and slowly varying (near the axis 2.2e3 -> 2.7e3, at x = 0.5
3.2e2 -> 3.0e2, on the brane 74 -> 130, ell^-4), and the brane's area radius levels off (1.128 at the horizon, 0.817
at s = -1.6, 0.790 at s = -3) where four-dimensional Schwarzschild would go to zero. So the DeTurck chart's
s = -infinity is a coordinate boundary, not the singularity: the fields approach power laws in u = 1/(1 - s) -- A and
T ~ u, S and B ~ u^-2, F ~ u^-1 (fitted over the trusted range) -- under which the bulk metric in (u, x) stays
nondegenerate at u = 0 (g_uu ~ u^2 but g_ux finite), while the reference metric (T = A = B = S = 1, F = 0) degenerates
there. Reaching the singularity, and 273's region, needs the evolution continued past s = -infinity: a new time u, the
fields rescaled by those powers, and a reference metric regular across u = 0, blended in smoothly while the old one is
still regular (a gauge source may change in time without disturbing xi = 0, if it changes smoothly).

Files added: `analyze_fw.py`, `curv_march.py`, `reanalyze.py`, `lam_run.py`, `phi_march.py` (B5 diagnostics);
`gen_damp_fw.py`, `interior_damp.py`, `xi_check.py`, `analyze_damp.py` (damping; proper time, Kasner exponents and the
brane against four-dimensional Schwarzschild), `eig_brane.py`, `cheb_tail.py`, `profile.py`.

**B7. Damping and resolution together (Nx = 28).** Damped (kap = 4, tilt 0.5) at Nx = 28, the run to s = -1 keeps
phi <= 9.6e-5 everywhere -- no brane growth -- and agrees with Nx = 20 near the axis (K 2505 against 2509 at s = -1)
while correcting the brane's K by 4 per cent (93.5 against 90.1). Figueras and Wiseman state the brane condition the
B5 analysis found (READ, 1105.2558): "Furthermore they imply d_n xi^r = (2/ell) xi^r on the brane ... which is
compatible with obtaining an Einstein solution with xi = 0 everywhere. Note that imposing the Israel vacuum condition
and both xi^r = 0 and xi^x = 0 on the brane does not give a regular elliptic system."

## Stage C: past the chart's end (2026-10-13, item 362)

The DeTurck chart's slices freeze: their lapse falls as |s|^-2.1 and s = -infinity lies at finite proper time with
finite curvature over the trusted range (B6). That is harmonic slicing's collapse of the lapse with the volume element,
here at a place that is not the singularity. A gauge source may be any function of the coordinates and the metric (no
derivatives) without touching the principal part or the constraint system's homogeneity, so the slicing can be steered.
The lapse driver (`gen_gauge_fw.py`, `interior_gauge.py`, `gauge_run.py`): xi~ = xi - h with h^s = -Fbar^s + mu (Nst
c(s) - N)/N^3 and h^x = 0, where N = 1/sqrt(-g^ss), Fbar^s = g^cd Gammabar^s_cd is the reference's pull on the slicing,
and c(s) = (1 - s1)/(1 - s) holds the lapse per unit lambda = ln(1 - s) near Nst. Then dN/d(-s) = mu (Nst c - N) + K N^2
(computed from box s), so the slices keep advancing in proper time. Switched on at s1 with Nst = N + Fbar^s N^3/mu, xi~
equals xi on the switch slice (8.2e-5 at s1 = -0.503 from the Nx = 28 run), and the constraint keeps zero from there as
it would for any gauge source. The brane rows are unchanged (h^x = 0).

**C1. The lapse driver loses the constraint by s ~ -1, through x-resolution (2026-10-13, item 362).** Every run is
bt = 1, switched on at s1 ~ -0.50 from a damped run (kap = 4, tilt 0.5). On the switch slice the lapse is 0.1065 near the
axis and 0.4326 on the brane, and phi = phi~ = 8.3e-5 (Nx = 16) or 8.1e-5 (Nx = 28). The variants, in order (computed;
phi~ is the largest |g(xi~, xi~)| over x):

| run | what changed | phi~ | outcome |
|---|---|---|---|
| `gauge_16` | wF = 1, no ramp: h^s jumps on at s1 | -- | NaN in the first steps |
| `gauge_16c` | wF = 1, C^1 ramp R(s) over 0.3, mu = 5 | 4.4 by s = -0.67 | step size to 2e-8 at s = -1.771 |
| `gauge3_16` | wF = 0 (reference pull kept), mu = 50, kap = 4 acting on xi | 0.79 at -0.617 | collapse at -1.281 |
| `gauge3_16_k0` | damping off (damping on xi is wrong; see below) | 0.17 at -0.761, 4.0 at -1.053 | collapse at -1.254 |
| `gauge4_16_k0` | h^s tapered by (1 - x^2), zero on the brane | 3.0e-2 at -0.822, 13 at -1.044 | collapse at -1.200 |
| `gauge3_28_k0` | Nx = 28, damping off | 1.1e-3 at -0.747, 0.20 at -1.064, 1.2e3 at -1.565 | stopped |
| `gauge3_28_k4` | Nx = 28, kap = 4 on xi~ | 1.5e-3 at -0.751, 0.66 at -1.200, 1.1e4 at -1.618 | collapse at -1.624 |

The third row was a fault: under the driver the constraint is xi~ = xi - h, so damping built from xi feeds an h-sized
term into it. `gen_damph_fw.py` removes it (computed: the damping term on h, subtracted). With that fixed, damping makes
no difference: at Nx = 28 the runs with and without it agree within a factor 1.5 at every s. The violation appears
first on the brane (6.6e-4 there at s = -0.55, Nx = 16) and spreads inward. Tapering h to zero at the brane does not
help. Resolution helps but does not stop it: Nx = 28 is 150 times lower than Nx = 16 at s ~ -0.75 and 20 times lower
at s ~ -1.06.

The brane's boundary conditions are not the cause (deduced). Israel's condition K_ab = gamma_ab/ell makes the
Codazzi side vanish, so G(n, e_b) = 0 on the brane for every tangential e_b. The field equation carries xi~, so this
reads grad_(n xi~_b) = 0. Given xi~_n proportional to xi~^x = xi^x - h^x = 0, that is Figueras and Wiseman's Robin
condition for xi~ instead of xi. The driver leaves the constraint's brane conditions as they were.

The Chebyshev tails in x locate the problem (computed, `cheb_tail_gauge.py`). Each figure below is the largest of the
last three |c_k|/max, at Nx = 28, with damping on xi~:

| s | phi~ driven | phi undriven | B tail, driven | B tail, undriven | A tail, driven | A tail, undriven |
|---|---|---|---|---|---|---|
| -0.55 | 8.1e-5 | 8.1e-5 | 6.7e-7 | 3.3e-7 | 1.2e-6 | 1.1e-6 |
| -0.65 | 3.0e-4 | 7.9e-5 | 2.9e-6 | 6.3e-7 | 1.9e-6 | 1.7e-6 |
| -0.75 | 1.5e-3 | 7.8e-5 | 2.5e-5 | 4.5e-7 | 1.6e-5 | 2.4e-6 |
| -0.90 | 8.5e-3 | 8.3e-5 | 5.6e-5 | 5.6e-7 | 5.3e-5 | 1.3e-6 |
| -0.99 | 6.8e-3 | 8.3e-5 | 3.7e-4 | 8.8e-7 | 3.0e-5 | 3.3e-6 |
| -1.20 | 0.66 | -- | 8.4e-4 | -- | 1.1e-3 | -- |
| -1.40 | 37 | -- | 9.8e-3 | -- | 7.4e-3 | -- |

The undriven run holds its tails near 1e-6 and phi at 8e-5 to s = -1. The driven run's tails rise with phi~, 420
times the undriven B tail by s = -0.99. The driver drives x-structure into the fields faster than 28 points resolve
it. The violation is that structure going unresolved, as in B5, and not an instability of the constraint system.
A driver acting pointwise in x with mu = 50 relaxes each x on its own, at a rate set by that x's extrinsic curvature,
so the lapse target pins differences across x that the free evolution would smooth (estimate; not separated from
other causes by a run). What would test it: a driver steering one function of s (the lapse at one x, or its x-mean),
which is still a gauge source algebraic in g. Or a lower mu, or more points in x. None of these has been run.
*Corrected in C2 (item 365).* The pinning estimate is wrong: the lapse falls at one relative rate across x, so
the pointwise driver and a one-function driver act nearly alike. "Not an instability" holds at mu = 5, where
more points reduce phi~; at mu = 50 they do not (Nx = 40 against 28).

**The old gauge's own reach at Nx = 28 (computed, `hr_resume.py`, `lam_phi.py`).** The damped Nx = 28 run continued in
lambda = ln(1 - s) without a driver keeps phi near 7e-5 to s ~ -2.07. Then phi rises: 3.2e-4 at s = -2.76 (largest
at x = 0.109), 3.2e-3 at -3.66 (x = 0.556), 1.68 at -4.53, 4.8e10 at -6.03. The peak is mid-bulk (x ~ 0.44 to 0.56),
not on the brane. The old gauge's trusted range at Nx = 28, damped, is s >= -2.1, beyond B5's -1.6 at Nx = 20.
Stage C's driver currently does worse than that, so O1b and O1c at the large end stay open on the interior.

Files added or changed: `gen_gauge3_fw.py` (the driver with the wF weight and the ramp), `gen_gauge4_fw.py` (the same,
tapered at the brane), `gen_damph_fw.py` (the damping term on h, to be subtracted), `interior_gauge.py` (the driver
class; `GAUGE_PKL` picks the generator's output; `run_steps` steps the Radau solver by hand and writes a checkpoint
every 25 steps), `gauge_run.py` (switch on at s1; arguments src s1 mu lam_end [rtol ramp kap_driven]),
`analyze_gauge.py`, `phit_profile.py` (phi~ and N (1 - s) across x), `hr_resume.py` (the restartable lambda leg),
`lam_phi.py` (phi along it), `cheb_tail_gauge.py` and `cheb_tail_fn.py` (tails, driven against undriven). The generated
`.pkl` and checkpoint files are not committed (sizes 1.7 to 3.9 MB each); every one is regenerated by the scripts above.

**C2. Item 365's three steps, in order (2026-10-13).** All at bt = 1, switched on at s1 ~ -0.50, damping kap = 4 acting
on xi~. Step 1 is a driver steering one function of s (`gen_gauge5_fw.py`, `interior_gauge5.py`, `gauge5_run.py`):
h^s = R(s) mu E(s)/N^2, h^x = 0. By the identity behind the first driver, it adds mu E to d ln N/d(-s) at every x.
E(s) is one number per slice: minus the Clenshaw-Curtis x-mean of ln(N/(Nst c(s))) ("x-mean"), or the brane value
alone. Its derivative E_s is exact from the fields' s-derivatives. Before any run: the weights integrate x^0..x^40
exactly (2e-16), and N_s matches N along the Nx = 28 run to 8e-5 per step of 7e-3 (second order). Step 2 lowers mu to
5. Step 3 adds points (Nx = 40, from `hr_sleg.py`'s damped s-leg, 965 s to s = -0.6), with Nx = 16 as a third
resolution. The runs, as the largest phi~ near a given s (computed):

| run | driver | Nx | mu | near s = -1.0 | near -1.5 | near -2.1 | near -2.35 | collapse |
|---|---|---|---|---|---|---|---|---|
| C1 `gauge3_28_k4` | x-local | 28 | 50 | 6.8e-3 (-0.99) | 5.2e2 (-1.52) | -- | -- | -1.624 |
| `gauge3_16_k4_mu50_fixed` | x-local | 16 | 50 | 1.9 (-1.02) | -- | -- | -- | -1.255 |
| `gauge3_40_k4_mu50` | x-local | 40 | 50 | 6.7e-2 (-0.98) | -- | -- | -- | -1.444 |
| `g5mean_28` | x-mean | 28 | 50 | 1.8e-2 (-1.05) | 2.0e-2 (-1.53) | 1.6 (-2.07) | 74 (-2.35) | -2.554 |
| `gauge3_28_k4_mu5` | x-local | 28 | 5 | 9.2e-5 (-0.96) | 4.1e-3 (-1.50) | 1.9 (-2.08) | 5.1e4 (-2.33) | -2.36 |
| `g5mean_28_mu5` | x-mean | 28 | 5 | 1.2e-4 (-1.00) | 5.6e-3 (-1.50) | 1.9e-2 (-2.11) | 0.51 (-2.37) | -2.713 |
| `g5mean_40_mu5` | x-mean | 40 | 5 | 7.0e-5 (-1.00) | 7.2e-5 (-1.50) | 1.4e-3 (-2.12) | 4.3e-2 (-2.34) | -2.870 |

Step 1 (computed unless marked). The driver does what it is built to do. At mu = 50 the lapse per unit lambda holds
mid-bulk at 0.94-0.97 of its switch value. The profile is left free: the axis falls to 0.50 and the brane rises to
1.14. On the switch slice the lapse falls at one relative rate across x (d ln N/d ln|s| = -1.37 at the axis, -1.36 on
the brane). So C1's pointwise driver and this one act nearly alike, and C1's pinning estimate is wrong. Even so, the
one-function driver gets further: phi~ at s = -1.2 is 2.6e-2 against C1's 0.66, and the run reaches -2.55 against
-1.62. Its violation sits on the brane, about 1e-2 from s = -0.75 to -1.7. There the brane's Kretschmann scalar jumps
by factors of ten between samples (76, 876, 328, 5283, 16420, 2881). That reads as a fast brane-localized oscillation
(deduced from the samples; not resolved in time). The brane-value variant agreed with the x-mean to s = -1.0 (1.3e-2
against 1.8e-2). It was stopped at -1.02: E_s from one node carries the brane solve's finite-difference noise, and the
steps fell to 3e-7.

Step 2 (computed). At mu = 5 both drivers stay near 1e-4 to s ~ -1.0 at Nx = 28; the x-mean stays at or below 1.9e-2
to -2.11. The lapse lags its target more at mu = 5 (mid-bulk 0.65-0.75 of the switch value, E = 0.30-0.47), but the
slices still advance.

Step 3 (computed; the reading deduced). At mu = 50, more points do not help. Between Nx = 28 and 40 the brane
violation starts later but grows faster: 21 against 41 per unit s from -0.92 to -1.05. It reaches phi~ = 1 sooner
(-1.16 against -1.26) and collapses sooner (-1.44 against -1.62). Nx = 16 crosses 1 at -0.98 and collapses at -1.255.
The three resolutions show no clean scaling with Nx, so the growth rate is not tied to a power of the point count. What
stands is that at mu = 50 the brane violation does not converge between 28 and 40 points. At mu = 5 it does: Nx = 40 is
80 times below Nx = 28 at s = -1.5 (7.2e-5 against 5.6e-3) and 14 times below at -2.1 (1.4e-3 against 1.9e-2).

What the best run reaches (`g5mean_40_mu5`; computed by `analyze_gauge5.py`, `g5_profile.py`, `old_tau.py`). The
proper time along the s-lines since the horizon:

| | near-axis node | mid-bulk | brane |
|---|---|---|---|
| old chart, to s = -infinity (to -2.07 integrated, power law beyond) | 0.2658 | 0.5185 | 1.0723 |
| driven, s = -2.121, phi~ 1.4e-3 | 0.2752 | 0.5451 | 1.1608 |
| driven, s = -2.231, phi~ 3.2e-3 | 0.2776 | 0.5524 | 1.1765 |

With the constraint held, the driven slices go past every point the old chart can reach. The margin is about 0.09 ell
of brane proper time and 0.01 near the axis. The brane's area radius keeps falling, to 0.688 at s = -2.12, where the
old chart levels it off at 0.79. The curvature near the axis has risen from 2.55e3 at s = -1.0 to 3.3e3 ell^-4;
mid-bulk it is 386. The brane's values scatter (536 to 6584 between neighbouring samples) and are not trusted: they are
read from second derivatives at the boundary node. All of these are far below the five-dimensional Planck scale.

The remaining failure is mid-bulk, at x ~ 0.6-0.7, from s ~ -2.2: phi~ goes from 3.2e-3 to 9.5 by -2.70. From -2.23 to
-2.34 phi~ grows 30 times while the tails stay near 1e-4, so this is not under-resolution. It comes at the same s, and
in the same part of the bulk, as the old gauge's own loss (x ~ 0.44-0.56 past -2.1 at Nx = 28), under a different
slicing. What the two share is the x-coordinate condition and the reference metric, which the driver (h^s only) leaves
as they were. The reference metric degenerates as s -> -infinity (B6). That is a candidate cause (deduced; not
tested). Two things would test it: a reference metric regular across u = 0 (B6's proposal), or a second driver acting on
h^x. Neither has been run.

O1b and O1c at the large end stay open. With the constraint held (phi~ <= 1.4e-3), the interior is now computed about
0.09 ell of brane proper time past the old chart's end, at curvatures far from the Planck scale.

Files: `gen_gauge5_fw.py`, `interior_gauge5.py`, `gauge5_run.py` (the one-function driver; arguments src s1 mu lam_end
[rtol ramp kap_driven mode]), `g5_profile.py`, `analyze_gauge5.py`, `old_tau.py`, `hr_sleg.py` (the damped s-leg
alone). `interior_gauge.py`'s `run_steps` now reports a driver class's own phi~. `cheb_tail_gauge.py` also prints where
phi~ peaks.

**C3. Literature (item 366).** `LITERATURE-366.md` records what a search found before any further run, each finding
READ, search summary or deduced. Four findings change the approach.
- The only dynamical RSII evolution (Wang and Choptuik) met our brane constraint violation, non-convergent with
  resolution. They cured it by imposing every constraint component at the brane.
- Harmonic time is marginally singularity-avoiding and reaches the singularity as its time goes to infinity
  (Garfinkle; Alcubierre). B6's chart instead collapses the lapse while the volume stays finite, through the reference
  metric's pull.
- An exact brane-localised hole interior (the AdS4 C-metric) exists to validate against.
- Our lapse driver is Pretorius's, which was built to stop the lapse collapsing, not to reach a singularity.
Proposed order (nothing run): new brane rows, then pure harmonic time, then the C-metric test.

**C4. Item 367, steps 1 and 2 (2026-10-13).** Both steps follow item 366's literature proposals, at bt = 1 from the
damped runs at s1 ~ -0.50, kap = 4. phi~ is the largest |g(xi~, xi~)| over x.

*Step 1: every constraint component at the brane* (`interior_cb.py`; Wang and Choptuik's cure, LITERATURE-366 L1).
The brane rows for T, S, A, B stay as they were. Substituting F = F_s = 0 removes F_x from every one of them (checked).
The remaining component is now imposed too: xi~^s = xi^s - h^s = 0 at x = 1. On the brane xi^s is affine in F_x, with
coefficient s (1 - s)^3/(8 A B bt^2) and no x-derivative of T, S, A, B (checked), so the row fixes the brane slope of F.
F(1) = 0 is kept by writing F = (1 - x) p(x).

Checks before any run (computed):
- On the old undriven run the row's slope matches the old interpolant's to about 1e-3 relative (`cb_t0.py`).
- The representation reproduces exact derivatives to 8e-15.

Two numerical faults were found and fixed before any result was trusted:
- The row's s-derivative, taken by finite difference, carried the brane solve's noise. It made an apparent mode
  growing at 16 per unit s, an artefact; with the noise removed every variant matches the old rows' 1.05
  (`cb_diag.py`, `cb_diag2.py`). F_s now keeps its plain interpolant (`fs_mode = "plain"`). Near the brane the term it
  feeds is multiplied by g^sx, which vanishes there with F.
- Radau stalls on the new right-hand side, taking steps of 1e-6 to 2e-4 even with a fixed-step Jacobian. RK45 steps
  the same interval at 5e-3, so the solution carries no fast dynamics (`cb_diag3.py`, `cb_diag4.py`). The runs use
  DOP853 (`run_steps(method=...)`). An old-row control under DOP853 collapses exactly where its Radau run did (-1.624).

The results (computed; s in brackets, then where each run ends):

| run | rows | phi~ along the run | ends |
|---|---|---|---|
| mu = 50, Nx = 28 | new | 9.8e-4 (-0.78), 6.5e-3 (-0.99), 130 (-1.33) | stalls at -1.434 |
| mu = 50, Nx = 28 | old (DOP853) | 1.5e-3 (-0.80), 0.41 (-1.11), 300 (-1.46) | -1.624 |
| mu = 50, Nx = 40 | new | 1.9e-4 (-0.79), 2.0e-3 (-0.92), 39 (-1.17) | -1.32 |
| one-function, mu = 5, Nx = 28 | new | 4.1e-3 (-1.79), 0.13 (-2.14), 32 (-2.49) | -2.797 (old rows -2.713) |
| one-function, mu = 5, Nx = 40 | new | 5.6e-4 (-1.79), 2.4e-2 (-2.18), 1.5 (-2.36) | -2.673 (old rows -2.870) |
| undriven, Nx = 28 | new | <= 8e-5 to -2.05, 1.8e-4 (-2.70), 0.15 (-3.50) | 9.7 at -4.00 (old rows 1.68 at -4.53) |

The step fails its test: the mu = 50 violation does not converge with Nx. With the brane node now held exactly, the
violation peaks at the node next to it (x = 0.997) and oscillates there: 2.1e-3, then 4.4e-4, then 2.2e-2 across
s = -0.71 to -0.91 (`cb_profile.py`). It then moves inward. So it is a high-frequency mode in the boundary layer, not a
constraint mode let in by the boundary (deduced). In this code the new rows are no better than the old, and somewhat
worse past s ~ -2.

*Step 2: pure harmonic time* (`gen_harm_fw.py`, the `HarmCB` and `HarmOld` classes; LITERATURE-366 L2-L3). The source
is h^s = -R(s) Fbar^s, so once R = 1, xi~^s = -box s; it is ramped in over Delta s = 0.5. The reference metric's pull on
the slicing is gone; the x-gauge keeps it. First, a check on the old chart (computed, `harm_check.py`, along coordinate
lines): from s = -0.1 to -2.03, N/sqrt(gamma) falls 500 times near the axis, 170 mid-bulk and 32 on the brane. Harmonic
slicing would keep it constant. The shift is large (|beta|/N up to 0.97), so this suggests rather than proves that the
DeTurck time is not harmonic.

The runs (computed, `hm_analyze.py`):
- *The constraint through the switch.* phi~ stays at its switch value, about 7e-5, through the whole ramp at Nx = 28
  and 40. The drivers had lost it by s ~ -0.62.
- *The lapse.* The lapse per unit lambda rises after the switch instead of collapsing (mid-bulk 0.24 to 0.47).
  N/sqrt(gamma) settles roughly constant mid-bulk (0.43-0.50) and on the brane (0.69-0.80), the harmonic relation. Near
  the axis it does not, where the coordinate-line reading is least faithful.
- *Past the old chart's end.* At s = -1.60, Nx = 40, phi~ is 5.9e-5 and the proper time since the horizon is 0.2769
  near the axis, 0.5349 mid-bulk and 1.0756 on the brane. That is beyond the old chart's totals everywhere (0.2658,
  0.5185, 1.0723). At s = -1.90, with phi~ 8.5e-3, the margins are 0.034, 0.065 and 0.060: further than the mu = 5
  driver near the axis and mid-bulk (0.009, 0.027), less on the brane (0.089). The brane's area radius falls to 0.711.
- *The failure.* It is the same as everywhere else: loss mid-bulk and near the axis (x ~ 0.07-0.76) from s ~ -1.75,
  blow-up by -2.0 to -2.07. Old rows and new behave alike at Nx = 40 (-2.065, -2.067). At Nx = 28 the old rows fail
  earlier (4.3e-3 at -1.63).

Across gauges the loss sets in at about the same mid-bulk proper time: tau_mid ~ 0.55-0.56 for the mu = 5 driver and
for harmonic time. That points to the solution at that place and time, not to the slicing (deduced). In harmonic time
the mid-bulk curvature climbs from 450 to 2500 ell^-4 between s = -1.75 and -1.90. If that is Kasner's K proportional to
(tau_s - tau)^-4, the singularity is near tau_mid ~ 0.63 (estimate, from two points). Step 3, an exact interior to test
against, is what can tell a real approach to the singularity from a numerical failure.

Files: `interior_cb.py` (the CB mixin; DampedCB, GaugeCB, Gauge5CB, HarmCB, HarmOld; `fd_jac`), `cb_run.py` (modes
damped, gauge3, gauge5, harm, harmold; DOP853), `cb_t0.py`, `cb_diag.py` to `cb_diag4.py`, `cb_profile.py`,
`gen_harm_fw.py`, `hm_analyze.py`, `harm_check.py`. `interior_gauge.py`'s `run_steps` takes `jac=` and `method=`, or the
environment variable RUN_METHOD.

**C5. Item 367 step 3, the AdS4 C-metric test, and a proper-time correction (2026-10-13; items 367-373).**
LITERATURE-366 L9's exact brane-localised hole, Emparan, Horowitz and Myers' flat-brane AdS4 C-metric, is put in the
RSII chart one dimension down (`gen_eqs_cm.py`): f = mu/r = 1 - s, tau = t/mu, xc = x1 (1 - x^2), phi = 2 psi/P1, so
the exact metric is Dl^-2 [s dtau^2 + ds^2/(f^4 s) + c0 (dx^2/p + x^2 p dpsi^2)/f^2] with Dl = 1/mu + xc/f -- FW's
ansatz with S^2 -> S^1, axis x = 0, brane x = 1. Here x1 = 2/3, mu = 15/8 (the brane horizon's radius 0.978 ell, near
bt = 1's 1.13). The reference is this metric deformed by eps (p and Dl multiplied by factors 1 + eps w x^2-type, w =
2f/(1 + f)); eps = 0 is the exact chart. The environment variable PROB selects the pickles, so `core_fw.py`,
`interior_fw.py`, `interior_damp.py`, `interior_cb.py` and `solver_fw.py` run the C-metric unchanged; the RSII path
was checked bit-identical after that switch (computed).
- The generator against the exact solution (`cm_exact.py --selftest`, 46/46): at eps = 0 the exact chart solves every
  Einstein-DeTurck row and the brane rows to 1e-12 (Israel K_ab = +h_ab, as for the RSII brane); the generated
  Kretschmann is 24 + 12 mu^2 (1 + xc r)^6/r^6, the closed form. Both Killing norms are invariants (tau and psi fixed
  by regularity), so each computed point maps to its exact (r, xc), and the computed curvature is compared there.
- The exact-reference interior (eps = 0, Nx = 16, kap = 4, DeTurck slicing, Radau to s = -0.5 with `fd_jac`, then
  DOP853 in lambda; `cm_run.py`, `cm_analyze.py`): to lambda = 3 (s = -19.1) phi stays below 2.2e-16; at every node
  r/mu falls to 0.0498 and the computed K reaches 9.2e7, agreeing with the exact K to 9e-11 to 3e-9; the brane's xc
  stays at 0 to 1e-13; proper time from the horizon agrees with the exact chart's to 1e-4 at the axis, mid-bulk and
  brane (1.5573, 1.7555, 2.9311 against totals to r = 0 of 1.5708, 1.7692, 2.9452). So with a reference that is the
  solution's own chart, the pipeline -- brane rows, damping, both steppers -- carries the interior to r = 0.05 mu with
  no growth of the constraint (computed). That is the stability half of the test; the deformed reference is the half
  that probes the gauge.
- **A correction the test exposed (computed).** The proper times quoted for the RSII interior in B5-C4 start at s0 =
  -0.002 and omit the stretch from the horizon, where N ~ |s|^(-1/2): it is 2 |s0| N(s0) = 0.0192 (near-axis node),
  0.0342 (mid) and 0.0766 (brane) at bt = 1, Nx = 28; the trapezoid's own error is below 1e-4. Every RSII tau in this
  file is low by those amounts: the old chart's totals become about 0.285, 0.553 and 1.149, the harmonic run's tau at
  s = -1.60 about 0.296, 0.569 and 1.152, the loss onset tau_mid ~ 0.55-0.56 about 0.58-0.59, and the Kasner estimate
  tau_s ~ 0.63 about 0.66. Comparisons between runs, which share s0, do not move. `cm_analyze.py` now adds the stretch
  and integrates in sqrt|s|. The figures above are kept as written; this line corrects them.

**C6. Where the interior stands at item 377 (2026-10-14).** M stopped every run (377): too much time had gone into
failed tests and into runs left stalling with waiters on them. What the record holds, by status:
- *Holds (computed).* The RSII hole at bt = 1 (R4/ell = 1.13, the large end's start) evolved inward stably on the brane
  rows with constraint damping. The DeTurck chart ends at s = -infinity, which lies at finite proper time (B5-B6). Pure
  harmonic time carries it further: at s = -1.60 (Nx = 40) phi~ = 5.9e-5 and the proper time is about 0.296, 0.569 and
  1.152 ell at the near-axis node, mid-bulk and brane (C4, with C5's correction), beyond the old chart everywhere. The
  mid-bulk curvature then climbs from 450 to 2500 ell^-4 between s = -1.75 and -1.90, Kasner-like.
- *Holds (computed), the method's stability.* On the exact AdS4 C-metric, with the reference equal to the solution's
  own chart, the same pipeline holds the exact interior to r = 0.05 mu (K = 9.2e7), matching it to 3e-9 (C5).
- *Fails or undecided.* (a) Every RSII run loses the constraint mid-bulk near tau_mid ~ 0.58-0.59 (corrected), in both
  slicings; whether that is the solution nearing its singularity or the method failing is not decided. (b) Wang and
  Choptuik's extra brane row did worse (C4). (c) The C-metric's gauge half -- a deformed reference -- converges in phi
  but not in the solution with the deformation's falloff ~ f (T at the horizon 1.37 at N = 12, 1.23 at N = 20), and
  near the axis the computed norms have no exact preimage; the f^3 falloff was being regenerated when stopped (its
  symbolic simplification stalled twice). (d) The calibrated top: the static 20 ell hole loses resolution at N = 32
  (phi 1.9e-2); 10 ell is clean at N = 28 (phi 5.9e-7), but its interior's Radau phase stalled at s = -0.186 with steps
  of 7e-7 and a diverging Newton iteration (py-spy on the process, 376), and was stopped.
- *What none of this can do alone.* Item 360 (c) puts 273's region where the curvature reaches the five-dimensional
  Planck scale. In units of ell that is about (ell/l5)^4: 7e79 with ell at its ceiling (l5 = 1.5e-25 m), about 4e3 at
  the floor 22.4 l_P (computed, l5^3 = l_P^2 ell). No evolution spans the first; the runs reach K ~ 2.5e3. The large
  end's interior to the Planck curvature therefore needs an asymptotic regime established from the computed solution
  and carried by analysis, for every ell above the floor (deduced). WARPTHEOREM.md's item-377 reassessment takes it up.

## Item 392: Zeno's halves (2026-10-14; considered, not run)

M asked that testing, sampling and measurement over a large range be considered in Zeno's form: halves, and halves of
the remainder. The method is checked where the answer is exact in `../lemmas/zeno_method.py`. On the 4D interior, 45
halves of 40 steps reach 1.4e-14 of the radius, each to 1e-10, while 1,800 uniform steps fail at 0.01. It answers this
directory's two limits: the loss of x-resolution at the brane (B5, C1), and the chart's end at finite proper time (B6).
- **In time:** each half is restarted with the fields rescaled by B6's power laws.
- **In x:** a halving mesh toward the brane.
- **In r0:** sampling by doubling.

The plan and the first run's question, criterion and time are in `../lemmas/INTERIOR-REQUIRED.md`, "Item 392". Nothing
is run until M approves.

## Item 393: the first Zeno half, run (2026-10-14) -- it failed its criterion

Approved at item 393: one rescaled restart at bt = 1 from the trusted state near s = -0.5, over one halving of
u = 1/(1 - s), at one fixed resolution per mesh part. It passes if the DeTurck norm phi <= 1e-4 and the Chebyshev
tails <= 1e-6 at the half's end, and it stops at 20 minutes. `zeno_run.py`.

**Rebuilt first.** The generated files had not been kept: `gen_eqs_fw.py` 320 s, `gen_damp_fw.py` 224 s and
`gen_eqs_sy.py` 65 s. The static hole (`solver_fw.py 1 24 24`) gave R4/ell = 1.12926, phi_max 1.9e-7, against B3's
1.1293. The trusted state, B7's damped Nx = 28 run from s = -0.002 to -0.503 (660 steps, 353 s), gave at s = -0.503:
- phi_max 8.24e-5 (C1: 8.1e-5);
- lapse 0.1061 at the axis and 0.4313 at the brane (C1: 0.1065 and 0.4326).

**The half.** On a halving mesh of four parts, [0, 1/2], [1/2, 3/4], [3/4, 7/8] and [7/8, 1], with 12 Lobatto intervals
each and x-derivative continuity at the interfaces. Evolved in lambda = ln(1 - s), with B6's rescaling. The mesh's
algebra was checked on cos 3x + x^4: axis and interface values to 4e-16, derivatives at inner nodes to 1e-13. The run
went from s = -0.503 to -2.006: status 0, 327 steps, 335 s.

**The first evaluation was wrong, and the error was the board's.** After the run, the brane root was solved starting from
the end state. That finds B5's spurious root (phi 1e39 even at the restart slice). Re-assessed with the root marched in
order along the saved steps, as `rescaled.py` does (`zeno_run.py reassess`, no rerun):

| s | phi_max | where | phi at the brane | worst tail, by part |
|---|---|---|---|---|
| -0.503 | 8.2e-5 | x = 0.009 | 1.9e-10 | 3.4e-5, 2.8e-7, 2.2e-9, 1.3e-6 |
| -0.789 | 7.7e-5 | x = 0.034 | 3.3e-8 | 1.1e-4, 2.6e-6, 9.2e-8, 8.4e-8 |
| -1.131 | 1.6e-4 | x = 0.125 | 6.6e-9 | 1.4e-4, 4.0e-5, 6.4e-7, 2.2e-7 |
| -1.539 | 7.8e-2 | x = 0.500 | 5.9e-9 | 1.2e-4, 5.7e-4, 6.6e-5, 1.4e-6 |
| -2.006 | 6.4 | x = 0.500 | 4.7e-4 | 3.4e-4, 4.4e-3, 3.3e-3, 2.7e-4 |

**Verdict: FAIL** (phi 6.4 > 1e-4; tails up to 4.4e-3 > 1e-6). So the second half is not run (item 393).

What the failure locates (computed from the saved run):
- **The brane is resolved.** phi there stays at or below 5e-4 through s = -2, where B5's single grids grew. The halving
  toward the brane did what it was for.
- **The error grows at the first interface, x = 1/2, and in the axis part.** From s = -1.5 phi peaks at the interface
  node itself.
- **The axis part was under-resolved from the start** (tail 3.4e-5 at the restart). The axis region carries the
  largest curvature (B6: about 2.5e3 against about 1e2 at the brane, ell^-4), and the mesh gave it the fewest points
  per unit length.

The joining of parts by derivative continuity alone is the weak point. Characteristic or penalty coupling is the usual
treatment of a hyperbolic system across interfaces; it is not used here.

What a second attempt at the same half would change, for M to approve or not:
- halve toward both ends -- the axis as well as the brane;
- give the axis part more points;
- couple the parts by penalty rather than by derivative continuity.

The same question, criterion and stop.

## Item 394: the joining checked, then the second attempt at the half (2026-10-14) -- it failed earlier

**The check on a known solution** (`zeno_interface_check.py`). A wave equation with the interior's principal structure:
u_ss = a u_xx + 2 b u_sx + F, with a = 1 + x^2, b = 0.3 x, b = 0 on the axis, and F made so that a chosen u is exact.
The mesh is the six parts [0, 1/8, 1/4, 1/2, 3/4, 7/8, 1], run to s = 40 (about 50 crossings), with eigenvalues of the
semi-discrete operator alongside. Computed:

| joining | pure wave, max Re | a, b varying, max Re | error at s = 40 (n = 12) |
|---|---|---|---|
| single grid (no parts) | 1e-14 | +0.88 | 27 |
| item 393's derivative continuity | 1e-14 | +6.2 | 1e93 |
| characteristic penalty, guessed | -- | +21 | blew up by s = 0.4 |
| energy-derived coupling, axis algebraic | +6.3 | +10 | -- |
| energy-derived coupling, axis weak | 1e-13 | +0.10 | 1e-12 |
| energy-derived coupling, axis folded | 7e-14 | **-0.06** | **2.5e-13** |

Two corrections of the board's own along the way:
- The guessed penalty acted on the characteristics leaving each part, not those entering it: (d_s - lambda d_x) w = 0
  carries w at velocity -lambda.
- The derived coupling had the right copy's slope-jump term with the wrong sign. A term-by-term energy check found it,
  and with it fixed d/ds [E - a m_phi J_u + tau J_u^2/2] is exactly zero on random states.

What the check also showed:
- **An algebraic slope condition at an end node is itself unstable in this scheme.** With strong Neumann at x = 1 even
  the single grid grows (+0.93 for the pure wave; +60 with a and b varying). The coupling's symmetric spread cannot be
  absorbed by a node whose value is fixed algebraically while it moves.
- So the axis was folded away. All five fields are even in x (g_sx ~ x F is odd), so the axis part is the symmetric
  [-1/8, 1/8] with an odd number of nodes and only x > 0 stored.

**The second attempt** (`zeno_run.py half 10 sat`, the class FoldedSAT). Folded axis part with 15 intervals; parts of
10, 10, 10, 10 and 14 intervals halving to the brane (restart tails 6.5e-7). The energy-derived coupling per field, with
a = -g_ss/g_xx and b = g_sx/g_xx. The brane rows unchanged. Run from the trusted state:

| s | phi_max | tail |
|---|---|---|
| -0.503 | 8.2e-5 | 6.5e-7 |
| -0.544 | 8.1e-5 | 9.4e-7 |
| -0.564 | 2.0e-3 | 6.0e-5 |
| -0.585 | 9.8e-1 | 1.6e-3 |
| -0.627 | 2.0e25 | 4.4e-1 |

The solver stopped at s = -0.627 (status -1, step size below the spacing of numbers; 1,596 steps, 473 s). The blow-up
starts at the brane node, x = 1 (phi 9e31 there at the stop).

**Verdict: FAIL**, earlier than item 393's. The run printed "pass: True", read from the restart slice alone, because the
board's check did not require the half's end. Fixed: a pass now needs status 0 and the criterion at the end.

The cause is the one the model check predicted. The coupling's spread from the last interface reaches the brane node,
which the record's Israel rows fix algebraically. In item 393 the derivative-continuity joining left that node alone,
and the brane held there.

**What a third attempt would change, for M to approve or not.** Impose the brane conditions weakly, in the same energy
form:
- the brane node evolved;
- the Israel rows -- linear in the brane's x-derivatives -- solved for the slopes T_x, S_x, A_x and B_x given the brane
  values;
- each field's slope pulled to that value by the penalty (a/h)(phi* - phi) that replaces the boundary's energy term;
- F = 0 kept strongly (its node does not move).

First checked on the model, with a prescribed slope at x = 1.

## Item 395: the third attempt -- the brane imposed weakly (2026-10-14)

**The model check** (`zeno_interface_check.py` FoldedWeak). The far end imposed weakly: its node evolved, its slope
pulled to the prescribed value by -(a/h_N)(u_x - g).
- Exactly neutral for the pure wave, for the Neumann case and for an Israel-like Robin u_x = kappa u + g with
  kappa = -1.
- With b = 0.3 x, nonzero at the end, it is unstable: the boundary keeps an energy term b v_N^2. In the interior
  b = g_sx/g_xx is zero at the brane (g_sx ~ x F, F = 0 there).
- With b vanishing at both ends the error stays at 2-4e-12 to s = 40 (n = 12).

**The port** (`zeno_run.py` FoldedSATWeak). The brane node is evolved (the equations are regular at x = 1). The four
Israel rows -- affine in the brane's slopes, checked to 9e-16, a 4 x 4 system of condition 9 -- are solved each step for
T_x, S_x, A_x and B_x, and F = 0 is held exactly. At the trusted state the rows' slopes match the mesh's to 1e-6.

**Run 1: died inside the solver**, a NaN in the Jacobian, with nothing saved. The solver was then stepped one step at a
time with its history kept.

**Run 2: failed at s = -0.628**, as item 394's had. The spectrum of the semi-discrete system (its Jacobian takes 6 s)
located the cause:
- Spurious modes, one per field, growing at 186 per unit -s on the x = 7/8 joining, present already at the restart.
- **The board's error:** the coupling's dissipative term -gam J_v was derived for time running forward in s. The
  interior evolves toward decreasing s, so it pumped energy in at about gam/h -- largest where the end weight h is
  smallest, the joining before the brane. The principal parts were checked to be exactly a X_xx + 2b X_sx for every
  field, as the coupling assumes (a = 0.1073 and 2b = -0.0746 at x = 7/8, diagonal); the first-order terms are sizable
  (to 7 across fields) but a model with them stays tame.
- With the damping along the evolution the top growth rate falls from 186 to 1.05, a slow mode in F near the axis.

**Run 3, the sign corrected:** stopped at s = -0.80 (159 steps, 86 s):

| s | phi_max | tail |
|---|---|---|
| -0.503 | 8.2e-5 | 6.5e-7 |
| -0.790 | 7.5e-5 | 3.1e-6 |
| -0.798 | 7.5e-5 | 3.3e-6 |

The DeTurck norm held under 1e-4 throughout, for the first time past s = -0.63. It stopped because **A turned negative at
x = 0.22** (-3.2e-4), so g_ss >= 0 there: s is no longer timelike, and a = -g_ss/g_xx changes sign. A fell smoothly and
nearly linearly (min A 0.073 at s = -0.50, 0.027 at -0.70, 0.013 at -0.75), its minimum moving out from x = 0.14 to
0.22, and it was resolved there (tails 1e-8 to 1e-7). The other fields were healthy (T, B, S > 0).

**Verdict: FAIL** -- the half's end was not reached, and the tails (3.3e-6) were above 1e-6. The second half is not run.

**What is not known: whether A -> 0 is the solution or the scheme.** g_ss -> 0 means the DeTurck s-slicing degenerates
there, a coordinate matter (B6 found the chart ends at finite proper time). But the record's single-grid runs reached
s = -1.6 (Nx = 20) without reporting it.

The deciding comparison: the record's own scheme (B7's damped Nx = 28 single grid), continued from the trusted state to
s = -0.8, with A(x) compared at the same s. It takes about 5 minutes, and it is for M to approve.
