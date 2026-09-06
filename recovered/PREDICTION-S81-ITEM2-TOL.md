# PREDICTION — SESSION 81, ITEM 2. F80.3's REPAIR AND O-C1's FALSIFIER AT cfg88+7p.
# FILED BEFORE ANY RUN OF perturb81.py. R 1449.
# Instrument: pack81/perturb81.py. J1 measured TOL · J2 stationary-to-stationary.

## WHAT IS KNOWN BEFORE THE RUN
F80.2 measured the Z=89 6d restart drop at **0.034493 mHa**, monotone, ratio ~0.3.
s81 item 1 measured the Z=90 6d² drop at **0.025471 mHa** and the Z=90 5f drop at
**0.060204 mHa** — so the drop is NOT a constant of the scheme; it varies by a factor of
2.4 across three configurations already measured.
s80's ten perturbed 6d runs landed within **−0.0337 to +0.0093 mHa** of a stationary
reference, and three were mislabelled FALSIFIED at a chosen TOL of 1e-6 Ha.
**s80 restarted the REFERENCE only. The perturbed landings were NOT restarted.**

## THE CLAUSES

**W1 · THE RE-LABEL RETURNS ZERO FALSIFICATIONS.** All eight converged s80 rows fall
within F80.2's measured 0.034493 mHa and re-label to SAME BASIN.
*Rationale: the deepest is −0.0337 mHa against a floor of 0.034493. **It clears by 0.0008
mHa — 2% of the floor.** This clause is nearly a coin-toss and I am filing it as the
expected outcome anyway, because the floor was measured before the rows were looked at.
If it lands the other side, F80.3's repair does NOT clear s80's labels and the honest
statement is that one row remains unresolved at the measured floor.*

**W2 · J2 IS THE LARGER EFFECT, AND IT PULLS EVERY PERTURBED LANDING DOWN BY ROUGHLY THE
LADDER DROP.** Each perturbed run gains between 0.01 and 0.06 mHa when restarted to
stationarity, in the SAME direction, and the stationary spread is NARROWER than the
landing spread by at least a factor of two.
*Rationale: the perturbed run stops on the same eigenvalue-drift test, so it lands above
its own floor by the same kind of amount. s80 compared a stationary point against a
still-descending one; the bias is systematic and of the size of the effect being looked
for. **If the stationary spread is NOT narrower, then the scatter is not the stopping
test and F80.2's diagnosis is incomplete.***

**W3 · O-C1 IS NOT FALSIFIED AT cfg88+7p EITHER.** No perturbed 7p run returns below the
stationary reference by more than that configuration's measured TOL.
*Rationale: none of the four seeds or ten perturbations has ever found a second basin at
Z=89. **AND THIS TEST CAN ONLY EVER KILL O-C1, NEVER CARRY IT** — filed again, in advance,
because it was the clause s80 got right and it is worth restating rather than assuming.*

**W4 · THE 7p LADDER DROP IS BETWEEN 0.01 AND 0.10 mHa AND DIFFERS FROM 6d's 0.034493.**
*Rationale: three measurements now span 0.025 to 0.060 mHa. A configuration-specific TOL
is only worth the machinery if the drop is configuration-specific; if 7p returns 0.0345
to within a few percent, J1's per-configuration measurement is unnecessary and a single
scheme-wide floor would do. **That outcome would simplify the instrument and I would take
it.***

**W5 · THE mix PERTURBATION AT 7p BREAKS ON NODE COUNT AT AN AMPLITUDE AT OR BELOW 0.30**,
as it did at 6d, and those runs are NOT scored as basin evidence.
*Rationale: mix contaminates each shell with the next of the same l, which is exactly the
direction that raises the node count. It is a property of the perturbation, not of the
configuration. Only amplitudes 0.02 and 0.10 are gridded for mix here, so this clause may
go unresolved — recorded as such in advance.*

**W6 · THE C1 CONTROL PASSES AT FIRST ATTEMPT THIS TIME.** A zero perturbation from a
stationary reference, itself restarted to stationarity, returns SAME BASIN with dP = 0.
*Rationale: s80's C1 failed and that failure WAS F80.2. With both sides stationary the
failure mode is removed by construction. **If C1 fails again, the repair does not work and
nothing below it may be scored.***

## FILED IN ADVANCE, AGAINST THIS RESULT
1. **A NULL WITH A MEASURED FLOOR IS STILL A NULL.** O-C1 remains open and load-bearing
   whatever this returns. It is not a proof of global minimality and must never be quoted
   as one.
2. **THE GRID IS SIX RUNS, NOT TEN**, to fit the session. The reduction is declared: two
   kinds, four amplitudes on noise, two on mix. The large-amplitude mix direction is
   UNTESTED at 7p, not tested-and-passed.
3. **ONE Z, TWO CONFIGURATIONS, ONE RUNG, ORBITAL-SPACE PERTURBATIONS ONLY.** A basin
   reachable only by a different occupancy pattern is outside this test by construction.
