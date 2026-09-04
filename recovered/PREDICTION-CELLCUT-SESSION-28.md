# PREDICTION — F24.1/F25.1 repair, ruling D (M, s28): "define the mechanism mathematically and work it into the solution, then test."
Written BEFORE any code change or run. Session 28. No constant beyond c; no measured input; Bank restore-point-2_13 untouched.

## The mechanism, stated as mathematics (from FINDING-LIMITCYCLE-27, now derived rather than described)
Correlation energy density in the chain-Z object: e_c[n] = n · min(eps_c(r_s,zeta), 0), where eps_c = lam0(zeta) ln r_s + e0a(zeta) + e0b (GB high-density
form, parameter-free) and min(.,0) is the variational constraint E_c <= 0 (a theorem, not a choice). This functional is C0 but NOT C1 in n:
   v_c = d e_c/dn = theta(-eps_c) · [eps_c - (r_s/3) d eps_c/d r_s] = theta(-eps_c) · [eps_c - lam0/3]  (LAM1=0).
At the crossing eps_c = 0 (r_s* = exp(-(e0a+e0b)/lam0), a DERIVED number) v_c jumps by exactly lam0(zeta)/3. On a one-orbital (fully polarised) SIC
density lam0(1)/3 = 0.0051818 Ha. The Kohn-Sham map n -> v[n] is therefore discontinuous. On the log mesh the step is placed at a NODE, so its
position is quantised in units of h; the continuum crossing x* lies inside a cell, and the discrete map T has no fixed point when T jumps across the
diagonal there (n_j slightly below n* is mapped above, and vice versa) — the residual chatters between two lattice states forever. That is F24.1/F25.1.
The Filippov/sliding solution of the continuum problem is the convex combination of the two potential values that holds n_j = n*.

## The repair worked INTO the solution (not a taper, no width chosen)
Discretise the SAME functional by finite volume: cell j = [x_j - h/2, x_j + h/2]; eps_c piecewise linear between nodes; the cell's potential is
v_c(n_j) · frac_j where frac_j = measure of {x in cell j : eps_c(x) < 0} / h — the exact in-cell fraction of the derived step. frac_j is continuous
in every node value, so the discrete map is continuous and has a fixed point (Brouwer on the compact potential set); as h -> 0 it converges to the
continuum step, whereas the nodal theta does not (its O(h) quantisation of x* is what cycles). Nothing is chosen: the crossing r_s* is derived, the
fraction is geometry, the cell width h is the inherited grid (npts=4000). Implemented as env SUBCELL=1 in v_gbz (t7c_corrz.py and t7c_cuaudit.py,
identical copies); SUBCELL unset => byte-identical to s27 (all 31 gates unchanged).

## Predictions (each can fail)
PD0  The observed steps (Ti 4s-up 0.00531, Cu 3s-up 0.00518, FINDING-LIMITCYCLE) equal lam0(1)/3 = 0.00518 to within |eps_j| at the crossing node
     (< 5%). Cu exact; Ti within 3%. Fails if the ratio is outside [0.95, 1.05].
PD1  Ti (Z=22, standing beta 0.3, SIC_NOCLAMP=1, tol 2e-5): converges (d < tol) in it < 100 under SUBCELL=1; E_ent = -0.38063 to 1e-4.
PD2  Cu (Z=29, beta 0.3): converges it < 100; E_ent = -0.37349 to 1e-4.
PD3  Sc control (Z=21): E to 1e-5 of the standing -0.32114 (frozen_scan f=0.5 reference) / gate value; it within +-5 of 37.
PD4  Gate 16 (H 1s, corr=Z, SIC) reprints -0.5 under SUBCELL=1; gate 18 t7c_regen La row (deleted then rerun) reprints noclamp base -0.2161.
PD5  The convergence-history tail under SUBCELL=1 for Ti has NO period structure: |autocorrelation| at lags 4 and 7 over the last 40 iterations < 0.3
     (s27: 0.83 at lag 7). Vacuous if it converges before 40 iterations — then reported as such.
Stop rule: no beta scan, no npts scan. If PD1 fails the mechanism statement is wrong or incomplete; report, do not tune.
Then, if PD1-PD4 hold: rerun the 15-row TS reference (frozen_scan / cuaudit chain) under SUBCELL=1 in batches <= 3, expecting every entrant E to 1e-4
of standing and it <= 100 with converged=True on all rows (PD6). Only after PD6 is the ruling's "test" complete.
