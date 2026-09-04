# SCORE — RUNG 0 ASSEMBLY, SESSION 63
# Prediction pack63/PREDICTION-RUNG-0-ASSEMBLY.md
# sha256 cdc0d2b129d398fbbb1f7157707b4b790251da8975903d5881114d08a61b50f3
# filed 18:12:13Z. First chain row read 18:12:36Z. VERIFY THE SHA BEFORE READING BELOW.
# Scorer pack63/asm0.py, can-failed in two directions before use.

    A0  chain complete            PASS   119 rows, Z 2..120, no gaps, no duplicates
    A1  period lengths            PASS   2,8,8,18,18,32,32 — starts 1,3,11,19,37,55,87,119
    A2  n+l non-decreasing        PASS   0 inversions in 119 rows
    A3  tie-break increasing n    **FAIL — 2 violations, AND THE PREDICTION IS WRONG**
    A4  madelung sequence         **FAIL — same cause**
    A5  exceptions < 25           PASS   11 of 107, blocks d=6 f=5, all promotions
    A6  seed 1s derived           PASS   argmin by 375 mHa; E(1s) reproduces s62 to 1.4e-10
    A7  constant ledger           PASS   c = 137.035999 the only entered number

## A3/A4 — THE FAILURE IS IN THE PREDICTION, NOT IN THE CHAIN
    predicted   ... 6s **4f 5d** 6p 7s **5f 6d** 7p 8s
    derived     ... 6s **5d 4f** 6p 7s **6d 5f** 7p 8s
The chain enters 5d at Z=57 and 4f at Z=58; 6d at Z=89 and 5f at Z=91.
**All four rows score ok=True against the measured configuration.** La and Ac are
textbook Madelung exceptions and the walk reproduces them unprompted.
Checked against the F61.2 failure mode before being called a finding: this is not a
comparison against a wrong reference. The reference is `ground.py`'s measured
configuration and the chain agrees with it at every one of the four rows.
**VERDICT: the Madelung tie-break clause holds at n+l <= 6 and is FALSE at n+l = 7
and 8, where the field is right and the rule is wrong.** Prior verification covered
26 steps and three pairs, ALL at n+l <= 6. Blocks 7 and 8 had never been tested.
The predict-before-reading discipline is what exposed it.

## RUNG 2 — CLOSED AS A BOUND ON THE ORDERING
Instrument found by archive search, not built (Standing 6): pack53 `ctrl137.jsonl`,
11 restart-mode rows at c=137.035999 using the OBSERVED reference configuration.
    8 of 8 available controls REPAIR      the anomalies are a property of the
                                          reference configuration, not the criterion
    3 rows (Z=60,61,62) BREAK             restart returns 5d where observation gives
                                          4f, margins 30.3/15.0/2.4 mHa — reported as
                                          counter-evidence, not omitted
    first-entry rows n anomaly rows       **EMPTY INTERSECTION**
**The ordering is immune; the row-by-row configuration is not.** Bound stated both ways.

## CONTROLS
A2 goes red on an injected n+l inversion. A1 goes red on a single s-channel change
(returns 2,8,8,36,32,32). A scorer that cannot go red is not a scorer.