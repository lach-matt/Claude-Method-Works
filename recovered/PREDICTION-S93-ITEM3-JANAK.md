# PREDICTION S93 ITEM 3 -- THE ADDITION ENERGY AS AN EXACT OCCUPATION INTEGRAL OF A FIELD EIGEN-QUANTITY (Slater relation). Hashed first.
## Ruling (M, s93): literature re-read; Slater's relation dE/dn = eps (HF, 1972 TS) and Koopmans (1934) attributed; test the identity, not subdivide.
## The field's functional (t7b_hf.py, s28 lift F26.2) supports a fractional electron f added to an own shell holding qc integer electrons:
##   pair factor ceff(f) = [qc(qc-1) + 2 f qc]/(qc+f), so the shell's self-pair energy is [qc(qc-1)/2 + f qc] U_cc: LINEAR in f.
## Hence, with orbitals stationary at every f (Hellmann-Feynman in f), the derivative along the stationary path is
##   dE/df = eps_c(f) + [qc - ceff(f)] U_cc(f) = eps_c(f) + qc(1-f)/(qc+f) U_cc(f),   U_cc = <c| (Y0_cc - w sum_k c3j F_k) / r |c>  (w=(2l+1)/(4l+1))
##   = eps_c(f) exactly when qc = 0 (pure Slater/Janak), and = eps_c(1) at f = 1 (Koopmans, item 2).
## IDENTITY under test:  D(c;Z,core) = E[core+c] - E[core] = INT_0^1 (dE/df) df.  (5-point Gauss-Legendre in f; every node a full SCF solve.)
## If it holds, S and P are each a difference of two such integrals and the 0.88 is an exact ratio of eigen-quantity integrals of the field:
##   no relaxation object remains to be named; "relaxation" is the f-dependence of the integrand. c the only number.
## Rule B declarations:
J1 VALUE-exact: |D - INT(dE/df)| < 2e-5 Ha on 15/15 systems (A,B,C x 5 rows). (can fail: if the frac functional is not stationary-consistent,
   or if the Y_k self-term is not linear in f, the integral misses D by O(U_cc) ~ 0.1-0.5 Ha.)
J2 VALUE-exact: central finite difference [E(f+0.02) - E(f-0.02)]/0.04 at f = 1/2 agrees with the formula dE/df(1/2) to < 2e-5 on 15/15.
J3 SIGN-exact: dE/df is monotone DECREASING in f at the 5 nodes on 15/15 (forced on average by Rel >= 0 of item 2; monotonicity is the prediction).
J4 VALUE (Slater transition state): |D - dE/df(1/2)| < 2e-3 Ha on 15/15 (third-order error of the midpoint).
J5 VALUE: rho_TS = [dE/df(1/2;C) - dE/df(1/2;B)] / |dE/df(1/2;B) - dE/df(1/2;A)| within 0.01 of rho_sealed on 5/5.
J6 HYGIENE: rung 0 on all solves; nodes sweep f in (0,1) open interval (shell present at every node); Drep 5/5.
## Can-fails (outside the instrument): A: drop the [qc-ceff]U correction (use eps alone) on the C system of row 38 (qc=1) -> J1 check fires
##   (expected miss ~ INT qc(1-f)/(qc+f) U df ~ 0.4 U_cc ~ 0.05-0.1 Ha) -> rc=4.  B: D perturbed by +1e-4 -> rc=4.
## Mechanism if J1 fails at qc=0 systems too: the code's fractional path is not the stationary path of a single functional (F26.2 lift
##   incomplete) -- then Slater's relation does not hold in this field and the integer Koopmans form of item 2 is the last exact statement.