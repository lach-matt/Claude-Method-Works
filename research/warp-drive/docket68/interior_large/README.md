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
