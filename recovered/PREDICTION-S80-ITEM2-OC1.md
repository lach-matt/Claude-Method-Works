# PREDICTION — SESSION 80, ITEM 2.  O-C1's FALSIFIER.
# FILED BEFORE ANY RUN OF perturb80.py.  R 1449.  The driver halts on a sha mismatch.
# THE OBJECT: converge Z=89 cfg88+6d to E* = -25694.541630577907, perturb the CONVERGED
# orbitals, re-converge, and ask whether the field returns to E*.
# A SECOND BASIN AT LOWER ENERGY KILLS THE ADOPTED STEP 0(ii) RULE AS STATED.
# NOTHING BELOW HAS BEEN RUN.

## Y1 · NO SECOND BASIN AT LOWER ENERGY WILL BE FOUND.
Every perturbed run returns SAME BASIN, |E - E*| <= 1e-6 Ha.
Rationale, filed: the four-seed evidence starts 52 Ha away and lands on the same value to
0.005 mHa, and seed D holds at Z=89 from 517 Ha away.  A local perturbation is a WEAKER
displacement than any of those.  **I therefore expect this test to CONFIRM and to be
WEAK EVIDENCE, and I am filing that judgement in advance so that a null result cannot
later be quoted as though it were strong.**
FALSIFIED IF: any run returns E < E* - 1e-6.

## Y2 · THE RETURN IS EXACT, NOT MERELY CLOSE.
Where the run returns SAME BASIN, |E - E*| < 1e-9 Ha, not merely under the 1e-6 tolerance.
Rationale: same rung, same beta, same tol, deterministic code.
FALSIFIED IF: a converged run lands between 1e-9 and 1e-6 of E*.

## Y3 · THE LARGE-AMPLITUDE RUNS WILL NOT ALL CONVERGE.
At amp >= 0.3 I expect at least one run to fail on a NODE COUNT, not on iteration budget.
Rationale: a heavily contaminated orbital has the wrong number of nodes by construction,
and hfc2.run2 raises before it can recover.  **A node-count failure is NOT evidence about
basins and must not be scored as one** -- it is the instrument failing to deliver the
starting point it intended.
FALSIFIED IF: every run converges.

## Y4 · 'mix' IS THE MORE SEVERE PERTURBATION AT EQUAL AMPLITUDE.
At the same amp, 'mix' produces a larger dP than 'noise' and, if anything breaks, breaks
first.  Rationale: noise is isotropic and largely orthogonal to the low-lying directions;
mix is deliberately aligned with the nearest same-l shell, which is where an RHF
instability would lie.
FALSIFIED IF: noise gives the larger dP at equal amp, or breaks first.

## Y5 · THE ITERATION COUNT RISES WITH dP AND STAYS BOUNDED.
Converged perturbed runs take MORE than the reference's 44 iterations, and fewer than 100.
FALSIFIED IF: any converged run takes fewer than 44, or the rung-0 budget is exhausted.

## WHAT THIS TEST CANNOT DO, FILED BEFORE THE RESULT
**A null result does not prove global minimality.**  It probes a NEIGHBOURHOOD of one
converged point, at a handful of amplitudes, in two directions, at one Z, on one
configuration.  O-C1 asks for a proof that the program reaches the GLOBAL minimiser.
**This test can only ever KILL the rule, never establish it, and if it returns null I
will record it as O-C1 STILL OPEN.**

## CAN-FAILS, DECLARED
C1 zero perturbation must return dP = 0 and SAME BASIN -- the comparator can say SAME.
C2 large perturbation with the re-convergence TRUNCATED to 3 iterations must return
   NOT-SAME -- the comparator can say DIFFERENT.  **Without C2 this instrument would be
   one whose only reachable verdict is the one that confirms.**
H2 LEVER: amp > 0 with dP = 0 exits rc=4 and computes nothing.  Every run, not once.