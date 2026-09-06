# PREDICTION — Z=89 RE-SEED. FILED BEFORE ANY Z=89 RESULT IS READ. R 1449.
# Instrument: pack77/seedtest77.py phase O, seeds A/B/C. Delta from sealed pack61/seedtest.py
# is THREE LINES, all output paths (pack61 -> pack77). No sealed file is appended to.
# LEVER VERIFIED FIRST (R-A): phase A PASS. A->B max|d_eps| 2.070841 Ha (valence 3p
# -2.06731 Ha); A->C 51.948837 Ha (valence -19.19266 Ha). The seed moves the field.

## THE SEALED ROW BEING RE-SEEDED
Z=89, ent 6d, margin 0.03233 Ha = **32.330 mHa — the tightest of all 107 rows**.
order: 6d -0.15762, 7p -0.12529, 8s -0.07065, 8p -0.04917, 5f -0.03146,
       5g -0.02000, 6g -0.01389, 7g -0.01021, 8g -0.00781.   nfail 5 (6f 7d 7f 8d 8f).
5f converged only at RUNG 1 (it=320); every other converged channel at rung 0.

## PREDICTIONS
**P1 DETERMINISM.** Seed A reproduces the sealed row exactly: ent 6d, margin 0.03233,
identical 9-channel order, nfail 5. *Any deviation is an environment fault, not a result.*
**P2 ENTRANT.** ENT_MATCH TRUE at all three seeds — 6d wins at A, B and C.
  *Basis: 9/9 across three Z at s76, and a 32.330 mHa margin against a measured
  differential spread of <= 1.560 mHa (factor 20.7).* **CONFIDENT.**
**P3 ORDER.** ORDER_MATCH FALSE for at least one of B, C. *The four g-channels are
separated by 6.1, 3.7 and 2.4 mHa; those gaps are the size of the spread, not the margin.*
**P4 CANDIDATE SET.** nfail DIFFERS FROM 5 at seed C. *Node-count failure is decided by
the shooting on the seeded radial functions, and seed C is a bare Coulomb start 52 Ha away.*
**P5 THE CRITERION AT ITS TIGHTEST ROW.** On a COMMON candidate set, max|DIFFERENTIAL|
<= 1.560 mHa and 2*D(89) < m(89) = 32.330 mHa. **This is the measurement s76 said would
decide the question and did not run.**
**P6 THE F76.2 ARTEFACT REAPPEARS.** If P4 holds, the RAW dmargin at seed C exceeds
1 mHa while the common-set differential does not — the same truncation artefact,
reproduced deliberately at a row where it was never measured.

## WHAT FALSIFICATION COSTS
**If ENT_MATCH fails at any seed, the entrant at the tightest row depends on which
critical point the algorithm reaches. The selection rule is then LOAD-BEARING, not a
formality, and Deliverable 1 inherits a dependency it does not currently declare.**
If ENT_MATCH holds, NOTHING IS PROVED — one more row survives one more falsifier.
Three seeds are not the critical set; Lions' family is not sampled by this instrument.