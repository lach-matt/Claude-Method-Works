# PREDICTION S93 ITEM 3 -- SLATER'S OCCUPATION IDENTITY IN THE SEALED FIELD. Hashed before any solve (R 1449).
## Claim under test. Along the stationary path in the own-shell occupation q of channel c (core fixed, Z fixed), exactly:
##   D(c;Z,core) = E[core+c] - E[core] = int_0^1 g_c(q) dq,   g_c(q) := dE/dq at frozen orbitals = eps_c(q) + (1/2) u_cc(q)
##   where u_cc = <P_c| (Y0_cc - (2l+1)/(4l+1) sum_{k>=2} c_k Yk_cc)/r |P_c> is the field's own-shell pair interaction (the object the
##   code multiplies by ceff = q-1 in Vloc). The 1/2 u_cc term is there because the functional carries (1/2) q (q-1) u_cc, so dE/dq =
##   eps_c + u_cc/2 (eps_c carries (q-1) u_cc). Hellmann-Feynman in q makes the integral exact; only quadrature error remains.
## Consequences if it holds: S = int [g(q;Z*,cfg1) - g(q;Z*,cfg2)] dq, P = int [g(q;Z*,cfg2) - g(q;Z*-1,cfg2)] dq: the 0.88 is a ratio of
##   two integrals of ONE field eigen-quantity; "relaxation energy" is the curvature of g in q, not a separate object.
## Instrument: 3-point Gauss-Legendre on [0,1] (q = 0.1127, 0.5, 0.8873), frac=None (ceff = q-1, the sealed default), systems A,B,C per row.
## Rule B declarations:
J1 VALUE-exact: |D - GL3| < 1e-4 Ha on 15/15 (A,B,C x 5). Bound direction: identity exact, quadrature only.
J2 LEVER (the 1/2 u term is real): |D - int eps_c dq| > 1e-3 Ha on 15/15, with D - int eps dq = (1/2) int u_cc dq > 0.
J3 VALUE (Slater transition state): |D - g_c(1/2)| < 5e-4 Ha on 15/15 (third-order error).
J4 VALUE: S and P rebuilt from the integrals reproduce the sealed S, P to 2e-4 Ha on 5/5 (follows from J1).
J5 SIGN-exact: g_c(q) is monotone increasing in q at the three nodes, 15/15 (screening by the shell's own partner loosens the channel);
   and int g dq - g(1) < 0 on 15/15, so that Rel = (1/2) u_cc(1) - [g(1) - int g dq]: the relaxation energy of items 1-2 is the own-shell
   pair energy at full occupancy minus the integral deficit -- both signed, both field outputs, no responder decomposition needed.
J6 HYGIENE: all fractional solves converge on the rung ladder; Drep = D at q=1 reproduces the sealed D(Z*) on row C 5/5; rung 0.
## Can-fails (outside the instrument): A lever-dead: u_cc forced to 0 -> J1 check |D - GL3| > 1e-3 -> rc=4 expected.
##   B control-validity: D perturbed by +1e-4 -> J1 fires -> rc=4 expected. CORR=False asserted in-instrument.
## Mechanism if J1 fails: the code's fractional path (frac=None, ceff=q-1) is not Slater's pair-count form, or eps_c at fractional q is
##   not dE/dq - then report which, from the residual's q-dependence; do not adjust the integrand after the fact.