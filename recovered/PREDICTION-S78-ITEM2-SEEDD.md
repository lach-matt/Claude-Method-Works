# PREDICTION S78 — ITEM 2, SEED D AT Z=89. Filed before any phase-A or phase-O result.
# TIMING FLAG, DECLARED: two DESIGN PROBES were run before this file (pack78/probeD78.py,
# probeD78b.py). What they showed and what I therefore already know:
#   (i) a bare-Coulomb start CONSTRUCTS cleanly at Z=89 — 16/16 node counts met;
#  (ii) it is the FIRST SCF SWEEP that raises `Z=89 50 nodes 3` (hfc2.py:55, inside the
#       iteration loop). s77's attribution to the SEED CONSTRUCTOR is wrong — F78.1;
# (iii) seed D survives 2 SCF sweeps at Z=89 in 1 s.
# So P0 and P1 below are NOT at risk and are recorded as ARITHMETIC, not as predictions.
# P2..P6 have not been computed in any form and are the risk-bearing set.

## THE INSTRUMENT
pack78/seedD78.py. SEED D = shell-wise screened hydrogenic: orbital (n,l) solved in pure
Coulomb -Zeff(n)/r, Zeff(n) = Z - (electrons in shells of lower n), floored at 1. Integer
screening read off the occupancy. No TFD, no Latter tail, no exchange, no fitted constant.
Driver pack78/o89segD.py runs PHASE A on EVERY invocation and refuses to solve when it
returns non-zero. That is the F77.3 repair: the can-fail is reachable by the driver.

## ARITHMETIC (not predictions — already implied by the probes)
  P0 seed D's constructor succeeds at Z=89 and at Z=19.
  P1 PHASE A PASS: max|d_eps| at Z=89 is ~517 Ha at 1s (Zeff(1)=Z exactly, so 1s is the
     bare-Coulomb value), and the 7s valence displacement is ~+0.192 Ha. Both clear the
     declared thresholds T_MAX=10 Ha and T_VAL=0.05 Ha.

## PREDICTIONS — RISK-BEARING
  P2 Seed D produces a FIELD at Z=89: the reference and at least 7 of the 9 candidates
     that seed A admitted converge under nlguard. **Rationale: 2 sweeps survived at the
     reference occupancy; a candidate adds one electron to an outer channel and does not
     change the inner screening that 5s reads.**
  P3 ENT_MATCH TRUE. The entrant at Z=89 is 6d under seed D.
  P4 ORDER_MATCH FALSE. Some pair below rank 2 reorders, as it did under seed B.
  P5 ADMISSIBILITY MOVES — F77.2. The seed-D candidate set is NOT the same 9 that seed A
     admitted. **Neither rank 1 nor rank 2 is deleted**: a deleted channel is one whose
     node count the shooting could not satisfy, and 6d and 7p are the two most bound and
     the two least marginal.
  P6 The COMMON-SET criterion HOLDS: 2*max|differential| over the channels common to seed
     D and the sealed row is BELOW m(89) = 32.330 mHa. I predict the differential is
     LARGER than seed B's 0.052 mHa — seed D is a far bigger displacement than seed B's
     2.07 Ha — and still below 1.560 mHa, s76's measured bound.
  P7 The raw margin under seed D differs from the sealed 32.330 mHa by less than 1 mHa,
     UNLESS P5's deletion touches rank 1 or rank 2, in which case F76.2's runner-up-
     substitution mechanism fires and the raw margin moves by tens of mHa.

## WHAT WOULD FALSIFY THE ITEM RATHER THAN A PREDICTION
If 2*D EXCEEDS m(89), the tightest row of all 107 is not seed-independent at full
strength, and the entrant at Z=89 is a seed artefact. That is the falsifier this item
exists to run. **It has never been run at Z=89 with a displacement of this size.**