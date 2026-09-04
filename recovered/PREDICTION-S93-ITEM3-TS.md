# PREDICTION S93 ITEM 3 -- SLATER'S RELATION IN THE FIELD: D = INT_0^1 g(q) dq, g = dE/dq AT FIXED ORBITALS. Hashed before any solve.
## Objects. For each system X in {A=(Z*-1,cfg2), B=(Z*,cfg2), C=(Z*,cfg1)} and own channel c: SCF solve at q_c = q for the three
##   Gauss-Legendre nodes q = 1/2 -/+ sqrt(3/20), 1/2 (exact for polynomials of degree <= 5 in q). At each node:
##   g(q) = dE/dq_c at fixed orbitals, from the frozen functional E[Q;P] by central difference (E is exactly quadratic in Q at fixed P,
##   so the central difference is exact to roundoff). eps_c(q) = the SCF eigenvalue at that q. D from the integer solves (item 2 jsons).
## Rule B declarations:
T1 VALUE-exact: | sum_k w_k g(q_k) - D | < 3e-5 Ha on 15/15 systems. (Hellmann-Feynman in q along the stationary path; can fail if the
   fractional-q functional the SCF minimizes is not the one the integer solves minimize, or if g is not smooth in q.)
T2 VALUE: |g(1/2) - eps_c(1/2)| > 1e-3 Ha on 15/15: the Koopmans eigenvalue is NOT dE/dq in this functional (c_eff = Q-1); the
   difference is the self-shell 1/2-pair term. Bound-direction: g(1/2) < eps_c(1/2) (the extra term is -1/2 x positive Slater integral combination).
T3 VALUE (Slater transition state, third-order accuracy): |g(1/2) - D| < 5e-4 Ha on 15/15.
T4 VALUE: rho_TS := [g_C(1/2) - g_B(1/2)] / |g_B(1/2) - g_A(1/2)| within 0.010 of rho_sealed on 5/5 (the 0.88 closes at the
   transition-state point to 1%; items 1-2's relaxation remainders are the difference between the endpoint q=1 and the midpoint).
T5 HYGIENE: rung 0 on all 45 fractional solves; D reproduces item-2 D to 1e-6 (same integer solves, read not re-run).
## Can-fails (outside the instrument): A lever-dead: all three nodes solved at q=1 (no q variation) -> quadrature != D -> T1 check fires rc=4.
##   B control-validity: D perturbed by +1e-4 -> T1 fires rc=4. CORR=False asserted.
## Mechanism if T1 fails: the functional's fractional path is not Slater's; file, and the identity is stated only at integers (Koopmans).
## If T1 holds: S = int [g_C - g_B] dq and P = int [g_B - g_A] dq EXACTLY; the 0.88 is a ratio of four eigenvalue-integrals of the
##   field, c the only number, and the named residues (a),(b) of item 2 are the q-curvature of g, not separate objects.