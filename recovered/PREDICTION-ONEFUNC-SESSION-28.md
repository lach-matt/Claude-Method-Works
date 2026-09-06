# PREDICTION — item (2), ruling (M, s28): "the gap may be where the answer is; midpoint slightly better; do not state both — combine both into ONE
mathematical function." Written BEFORE any run. No constant beyond c; no measured input.

## The one function
On the neutral exact-exchange (HFSR 'hf') orbitals P, entrant density n_e = P_ent^2, core density n_c (all other shells at integer occupation):
   E_c(f) := E_c[n_c + f n_e]  -  f · E_c^{pol}[f n_e]  -  (SIC of the other shells, f-independent),   f in [0,1],
with E_c[n] = int n eps_c(r_s,zeta) (GB high-density chain-Z object, min(.,0) constraint) and eps_c evaluated exactly as v_gbz.
Both standing forms are functionals of THIS function:
   midpoint (s26 hfdscf Delta_c)  = E_c'(1/2)                 [Janak: d/df of int n eps_c is int n_e v_c; SIC part likewise]
   integer  (s27 hfc2)            = E_c(1) - E_c(0)  (+ orbital relaxation, |.| < 0.0005 by FINDING-HFC2)
   and E_c(1) - E_c(0) = int_0^1 E_c'(f) df exactly, of which the midpoint is the one-point Gauss quadrature, exact iff E_c is quadratic in f.
So the GAP := [E_c(1)-E_c(0)] - E_c'(1/2) = (1/24) E_c'''(xi), xi in (0,1): a derived curvature of the correlation object in the occupation. The law's
correlation term is stated as the ONE expression  I_c = E_c'(1/2) + (1/24) E_c'''(1/2) + O(E^(5)), i.e. midpoint PLUS its derived curvature
completion — one function, no choice, both prior forms recovered as its truncations.
Closed-form content of the curvature (eps_c = lam0(zeta) ln r_s + const => n eps_c = -(lam0/3) n ln n + c n):
   SIC piece: -f E_c[f n_e] = -f^2 E_c[n_e] + (lam0(1)/3) N_e^- f^2 ln f, N_e^- = int n_e over the eps<0 region: the f^2 ln f is the correlation
   analogue of the s25 f^(4/3) exchange law; its contribution to GAP is +(lam0(1)/3)(ln 2 - 1/2) N_e^- = +0.00100 N_e^- Ha (sign as GAP defined above).
   Total-density piece: T'''(f) = +(lam0/3) int n_e^3/(n_c+f n_e)^2 (zeta-dependence of lam0 and the moving eps<0 boundary neglected).

## Predictions
PQ0 (gate) E_c'(1/2) by central difference on the 5-point path (f = 0, 1/4, 1/2, 3/4, 1) equals hfdscf Delta_c to 5e-4 on every class row (Y, La, Lu,
    Sc, Gd, Cs), and the analytic potential-expectation derivative equals it to 1e-5.
PQ1 E_c(1)-E_c(0) on frozen neutral orbitals equals hfc2's (Ec_ion - Ec_neu) to 1e-3 (relaxation bound) on Y, Gd, Cs (the three hfc2 rows).
PQ2 GAP is POSITIVE on all six rows in the sense |midpoint| > |integer| (as s27 read it: Y 0.0280 vs 0.0202) and lies in [0.006, 0.010] on the
    d rows, < 0.002 on Cs.
PQ3 The 5-point Simpson integral of E_c'(f) (from the analytic slopes at f = 0, 1/2, 1) reproduces E_c(1)-E_c(0) to 3e-4 — i.e. the one function
    is smooth enough that its integral is captured by three slopes; the whole gap is the curvature and nothing else.
PQ4 The finite-difference (1/24)E_c'''(1/2) from the 5 points accounts for >= 70% of GAP on the d rows (the remainder O(E^(5)) and the moving eps<0
    boundary), and the closed-form SIC f^2 ln f piece is 0.001 +- 0.0005 Ha on each of them.
Stop rule: no scan in f beyond the five fixed points; no new orbitals; if PQ0 fails the identification of the two forms with one function is wrong
and the item returns to M with that on record.
Failure mode of the whole idea: if PQ3 fails (integral not captured by the slopes) the gap contains something that is not curvature of E_c(f)
— e.g. the moving cutoff boundary — and "one function" is not sufficient; report, do not tune.
