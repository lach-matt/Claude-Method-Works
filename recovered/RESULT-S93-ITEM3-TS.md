# RESULT S93 ITEM 3 (PARTIAL, 3 of 5 rows) -- SLATER'S RELATION HOLDS AT THE s ROWS (7/7 systems <= 2.5e-5) AND FAILS AT 58-B BY 8e-5
# prediction pack93/PREDICTION-S93-ITEM3-TS.md sha256 79d5b4ca (hashed first). can-fails A (no q-variation) rc=4, B (D+1e-4) rc=4 PASS, non-vacuous.
# instruments pack93/ts93.py (3-pt Gauss; --nodes5 added AFTER the 58 failure, declared), ffun93.py (verbatim copy of rel93 functions),
# tight93.py, stat93.py (follow-ups, declared). Ledger addendum pack93/LEDGER-F-S93.md (F1-F5; Slater/Koopmans/Janak/Baerends).
## SEVERITY LINE: T1 is a hashed VALUE-exact claim and it FAILED at one system. Nothing downstream of T1 is scored at 58. Rows 90, 91 NOT RUN.
## Table. g(q)=dE/dq at fixed orbitals (exact central difference of the quadratic functional); quad = 3-pt Gauss int_0^1 g dq; D from rel93.
 row sys  Z  N   g(q1)     g(1/2)    g(q3)     quad        D           T1        T2(g-eps at 1/2)  T3(g(1/2)-D)
 38  A   37 36  -0.20703  -0.13775  -0.07526  -0.139638  -0.139640  +2.0e-6     +0.08943   +0.00189
 38  B   38 36  -0.47206  -0.38249  -0.29736  -0.383724  -0.383708  -1.6e-5     +0.11629   +0.00122
 38  C   38 37  -0.25004  -0.17292  -0.10173  -0.174568  -0.174575  +7.0e-6     +0.10540   +0.00165
 56  A   55 54  -0.18887  -0.12614  -0.06927  -0.127767  -0.127792  +2.5e-5     +0.08113   +0.00165
 56  B   56 54  -0.42279  -0.34315  -0.26727  -0.344197  -0.344187  -1.0e-5     +0.10362   +0.00103
 56  C   56 55  -0.22498  -0.15590  -0.09189  -0.157308  -0.157320  +1.2e-5     +0.09434   +0.00142
 58  A   57 56  -0.30691  -0.20356  -0.10851  -0.205868  -0.205848  -2.0e-5     +0.16102   +0.00229
 58  B   58 56  -0.66690  -0.54095  -0.42067  -0.542526  -0.542431  -9.5e-5  FAIL  (5-pt: quad -0.5425255, same; tol 2e-8: D -0.5424437, T1 -8.1e-5)
## Scoring (rows 38, 56 complete; 58 stopped at B)
T1 HELD 7/7 at 38, 56, 58-A (|.| <= 2.5e-5). FAILED at 58-B: -9.5e-5, robust to quadrature order (5-pt identical to 1e-6) and to SCF tolerance
   (2e-8: -8.1e-5). g(q) and eps(q) are smooth at 5 nodes; eps extrapolates to the integer value (-0.5696). NOT quadrature, NOT convergence.
T2 magnitude HELD 8/8 (0.08..0.16 Ha); bound-direction FALSIFIED 8/8: g(1/2) > eps(1/2), not <. (F93.5: sign guessed, not derived.)
T3 FALSIFIED 8/8: g(1/2) - D = +0.0010..+0.0023 > 5e-4. Slater's transition-state point is accurate to ~1e-3 here, not third order at 5e-4.
T4 HELD 2/2 where scorable: rho_TS = 0.8563 vs 0.8569 (38); 0.8629 vs 0.8635 (56): the 0.88 closes at the transition-state point to 0.0006.
   Also exact: S_quad = 0.20916 vs S 0.20914; P_quad = -0.24409 vs P -0.24407 (38); 0.18689/0.18687, -0.21643/-0.21640 (56).
T5 HELD: rung 0 on all 27 fractional solves; D read from rel93 (not re-run).
## What is derived (s rows only)
 At 38 and 56, S = int_0^1 [g_C - g_B] dq and P = int_0^1 [g_B - g_A] dq to 2e-5: the 0.88 is a ratio of two eigenvalue-integrals of the
 field (g is the occupation-derivative eigenvalue, not the Koopmans eps; they differ by the self-shell half-pair term, +0.08..+0.16 Ha).
 At the transition-state point alone the ratio is 0.856/0.863 vs sealed 0.857/0.864. No relaxation object appears.
## What is NOT derived
 The identity fails by 8e-5 Ha at (Z=58, Ba core, 5d^q). Hypothesis (UNTESTED, stat93 inconclusive -- its kinetic integral is 0.012 Ha off
 the code's implicit one): at fractional q with l>0 the eigen-equations the code solves are not the Euler-Lagrange equations of the energy
 functional it reports, so dE_SCF/dq != dE/dq|_P and the Hellmann-Feynman step fails. At integers this is invisible (K = 0 is algebraic).
 If true, fractional occupation is NOT a sealed-field object for d shells and item 3 cannot be stated there; the s-row result stands.
 8e-5 Ha is 1.6x the chain's numerical floor (5e-5) and 400x below the tightest chain margin: no sealed row is affected.
## Faults
F93.4 SEVERITY: prediction hygiene. T1 bar (3e-5) set below the chain's own floor (5e-5) at |E| ~ 9e3-2.4e4 Ha. Does NOT rescue 58-B (8e-5 > 5e-5).
F93.5 SEVERITY: hygiene. T2 bound-direction asserted from a guessed sign of the half-pair term; opposite 8/8.
F93.6 SEVERITY: instrument design (open). Fractional-q SCF stationarity in the sealed functional for l>0 is unverified; item 3's exact identity
   fails there by 8e-5. Carried OPEN. Test required: stationarity with the kernel's own kinetic integral, or the Euler-Lagrange check by hand.
## Residue after item 3: none closed. Open: F93.6; rows 90, 91 unrun; items 1-2 residues (a),(b) stand as named.