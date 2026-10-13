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
