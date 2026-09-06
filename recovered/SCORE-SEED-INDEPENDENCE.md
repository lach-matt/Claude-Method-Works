# SCORE — RUNG 3/4 SEED-INDEPENDENCE, SESSION 61
# Prediction `pack61/PREDICTION-SEED-INDEPENDENCE.md`
# sha256 192d08537bf28e9ecdd9ed8afae9d92a6fd9b2a72406ddd1b6e70a750aa19713
# filed 17:23:49Z. First line of test code written 17:24Z. First result read 17:24:48Z.
# VERIFY THE SHA BEFORE READING ANY LINE BELOW.

## THE CONTROL CAME FIRST, AND IT PAID
PHASE A, 17:24:48Z — the seed switch is LIVE, not vacuous (Standing 7):
    seed A (TFD, qtail=1)  valence 3p = -0.86290 Ha
    seed B (TFD, qtail=6)  valence 3p = -2.93021 Ha    d = -2.07 Ha
    seed C (bare -Z/r)     valence 3p = -20.05556 Ha   d = -19.19 Ha, max|d| = 51.95 Ha
Seed C is exactly hydrogenic (-Z^2/2n^2 at Z=19: 1s -180.500, 2s -45.125, 3s -20.056),
confirming it carries no TFD, no Latter clamp, no exchange, no screening, no constant.
**P1 HOLDS. The test is not VOID.**

## P2 — THE CONVERGED ENERGY FORGETS ITS SEED. **HOLDS.**
Fixed configuration, ruling path (run_guarded -> run2), CORR=False:
    Z=19  A -601.378794570   B -601.378802809   C -601.378799287
          dE(A->B) = -0.008 mHa      dE(A->C) = -0.005 mHa
    Z=39  A -3383.296482285  B -3383.296471907  C NO-DATA (node failure in SCF)
          dE(A->B) = +0.010 mHa
**A 52 Ha disagreement at the starting point converges to an 8 microhartree
disagreement in the answer.** Predicted < 1 mHa; observed 0.005-0.010 mHa, a hundredfold
inside the prediction. The Gaspar-Kohn-Sham alpha=2/3 form and the TFD potential do not
survive convergence. **Rung 3's "seed-only" is now demonstrated, not assumed.**

## P3 — THE ORDERING. **THE ENTRANT CLAUSE HOLDS 3/3. THE ORDER CLAUSE FAILS AS WORDED.**
    Z    seed A ent   seed B ent   seed C ent   margin A    margin B    common-channel max|dD|
    19   4s           4s           4s           0.05216     (see below) 0.00004 Ha
    20   4s           4s           --           0.06058     --          0.00005 Ha
    39   4d           4d           --           0.04367     0.04368     0.00003 Ha
**Every channel that converges under both seeds returns the same number to <= 0.05 mHa,
and the survivors are in the same relative order at all three rows.** At Z=39 — the 4d/5p
tie-break row — the MARGIN moves by 0.00001 Ha against a margin of 0.04367 Ha: a factor
of 4000. Predicted |dmargin| < 5 mHa; observed 0.01 mHa where the comparison is clean.

**WHAT DID NOT HOLD, STATED PLAINLY.** The full ORDER is not identical, because the
perturbed seed makes weakly-bound channels FAIL TO CONVERGE and drop out of the ordering
entirely — not because anything reorders.
    Z=19  nfail 0 -> 2   dropped 4p, 4d
    Z=20  nfail 1 -> 6   dropped 4p, 4d, 5s, 5p, 5f
    Z=39  nfail 2 -> 6   dropped 5f, 6s, 6p, 6g
**At Z=20 the dropped 4p was the RUNNER-UP.** The reported dmargin of +0.031 Ha at Z=19
and Z=20 is therefore NOT a shift in any margin; it is the arithmetic of a runner-up
vanishing from the list. It must never be quoted as a seed effect on a margin.

**THE CONSEQUENCE, AND IT IS NOT A SMALL ONE.** The seed does not move the winner or the
order of the survivors. It DOES decide which candidates the guard can converge at all.
The winner was never among the casualties at these three rows — it is the most tightly
bound channel and converges from every seed tried — but **that is an observation at three
rows, not a theorem.** A seed that killed a WINNER would change the entrant. The sealed
seed is the one where nfail is lowest (0-2), and it is the mode the solution is claimed
in. Rung 3 is closed FOR THE CONVERGED ORDERING and carries this caveat explicitly.

## P4 — THE LATTER CLAMP IS SEED-SIDE ONLY. **HOLDS. RUNG 4'S OPEN QUESTION IS ANSWERED.**
s60 recorded this as "UNVERIFIED, do not assert either way." Now verified, by measurement
and not by reading alone: run2 takes `qtail` ONLY as the argument of `self.seed(qtail)`
(hfc2.py:40); its own Vloc (hfc2.py:45, :64) is built with no `np.minimum(...,-qtail/r)`.
Changing the tail from -1/r to -6/r — which moves the STARTING eigenvalues by up to
2.07 Ha — moves the CONVERGED energy by 0.008-0.010 mHa. Had the clamp been live inside
run2's iteration, a sixfold tail could not have left the answer at the 10-microhartree
level. **The Latter clamp and the TFD potential are both confined to the seed, and the
seed is forgotten. Rung 4 folds into Rung 3 and closes with it.**

## P5 — THE SEED-MEMORY FLOOR, RECORDED, NOT CLAIMED AS THE RUNG 7 FLOOR
**<= 0.05 mHa** on every channel converging under two seeds, at Z=19, 20, 39. This is the
answer's residual memory of its starting point. It is a LOWER bound on the walk's
numerical floor and nothing else. The Rung 7 convergence floor (grid, tolerance, mixing)
is a different measurement and remains item 1 of the s62 list. Whatever it returns may
not contradict this number without an explanation.

## THE UNPLANNED RESULT — A THIRD INDEPENDENT DETERMINISM RECEIPT
Seed-A re-runs at Z=20 and Z=39 reproduced the sealed rows **BIT-IDENTICALLY in every
channel and in the margin** (dmargin = 0.00000). Z=19 differed in exactly one channel,
diagnosed as F61.1 and not as noise. Following F60.2's receipt B (55 cold rows to the
last digit), the chain has now been reproduced by a third driver in a third session.

## FAULT REGISTERED THIS SESSION
    F61.1  The sealed chain is heterogeneous: Z=2..56 (55 rows) predate nlguard, Z=57..120
           (64 rows) postdate it. At Z=19 the pre-guard 4p carries a value 1.95 mHa off
           the guarded one. Caught by this test's OWN identity control, before any variant
           was read. Full entry: `pack61/FAULT-F61.1-PREGUARD-ROWS.md`. The seed test's
           baseline was moved to the harness's own seed-A row in consequence (Standing 8).

## VERDICT
**RUNG 3 CLOSES for the converged ordering, with the convergence-of-candidates caveat
stated above. RUNG 4 CLOSES with it.** Item 1 of the s61 work list — "the highest-value
single measurement left on this ladder" — is discharged. The defence that TFD and the
KS exchange form are iterated away is no longer assumed: it is measured, at 0.005 mHa,
from a starting point 52 Ha away.
