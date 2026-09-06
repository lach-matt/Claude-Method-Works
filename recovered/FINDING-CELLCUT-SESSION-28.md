# FINDING — F24.1/F25.1 CLOSED under ruling D: the mechanism derived, worked into the solution, tested on all 15 rows.  s28, bridge-27 §3(1)
Files: PREDICTION-CELLCUT-SESSION-28.md (before any change), cellcut.py, cellcut_run.py, cellcut.jsonl, TABLE-CELLCUT-SESSION-28.txt;
t7c_corrz.py and t7c_cuaudit.py patched (two identical v_gbz copies) — SUBCELL unset => byte-identical behaviour (control row reproduces s27 exactly).
No constant beyond c; no measured input; Bank restore-point-2_13 untouched. Convergence, not physics: no standing number moves beyond 2e-5.

## The mechanism as mathematics
e_c[n] = n · min(eps_c(r_s,zeta), 0) — the GB high-density form under the variational constraint E_c <= 0. This is C0 but not C1 in n:
v_c = theta(-eps_c)·[eps_c - lam0(zeta)/3], which JUMPS by lam0(zeta)/3 at the derived crossing r_s* = exp(-(e0a+e0b)/lam0). PD0 HELD: on a
one-orbital (zeta=1) SIC density lam0(1)/3 = 0.0051818 Ha; the s27 observed steps are Cu 0.00518 (ratio 1.000) and Ti 0.00531 (1.025) — the
excess on Ti is |eps_j| at the crossing node. The KS map is discontinuous; the nodal theta quantises the crossing to the mesh, and the discrete
fixed-point map jumps across the diagonal when the continuum crossing lies inside a cell — no fixed point on the lattice, so the residual chatters
between two lattice states (period set by beta). That is F24.1/F25.1 in full.
## The repair (nothing chosen)
Same functional, finite-volume discretisation: each log-mesh cell gets v_c(n_j)·frac_j with frac_j the exact in-cell measure of eps_c<0 for
eps_c piecewise linear between nodes (cellcut.frac_neg). frac_j is continuous in every node value, so the map is continuous, a fixed point exists,
and h->0 recovers the continuum step. r_s* derived; the fraction is geometry; h is the inherited grid. Not a taper: no width, no form parameter.
## Results (TABLE-CELLCUT)
PD1 HELD Ti: it 100->34, converged, E -0.38064 (standing -0.38063).   PD2 HELD Cu: it 100->33, E -0.37350 (-0.37349).
PD3 HELD Sc: it 34 (37), E -0.32113 (-0.32114).   PD4 HELD gate 16 H -0.5 (it 30); gate 18 La noclamp base -0.2161 reprinted.
PD5 HELD (vacuously stated as predicted: converged in 34 < 40; lag-7 autocorrelation 0.043 vs 0.83 in s27, lag-4 0.21).
PD6 HELD all 15 rows: converged=True everywhere, max it 41, max|dE| = 0.00002 Ha, mean |dE| < 1e-5. Control (SUBCELL unset, patched code):
Ti it 100, converged False, tail 0.015961 0.007621 0.005331 ... period 7, ac(7)=0.83 — identical to s27.
Failed predictions s28: none in this item. Timing flags: none (the mechanism statement, the repair form and all six predictions preceded every run).
## Standing
F24.1 and F25.1 close as ONE numerical-analysis fault with a derived cause and a derived resolution. Every table that carried it=100 for Ti/Cu now
carries it=34/33 under SUBCELL=1 with the same E to 1e-5. Recommendation stated, not decided: carry SUBCELL=1 as the standing convention from here
(it is the consistent discretisation of the object the chain already uses); README-28 gates 32-33 = Ti/Cu convergence rows. What this does NOT
touch: the physics that eps_c turns positive at r_s ~ 5.2 (the high-density expansion leaving its domain) — that remains a property of the derived
correlation object, on record, and the constraint min(.,0) is the honest treatment of it, not a fit.
