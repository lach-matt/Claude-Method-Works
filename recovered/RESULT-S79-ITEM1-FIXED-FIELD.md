# RESULT S79 — ITEM 1. THE FIXED-FIELD CROSS-CHANNEL COMPARISON, COMPUTED FOR THE FIRST TIME.
# CLOSE-S78 §3's RESIDUAL CLAIM HOLDS AT Z=89 BY 155.4 mHa. THE RELAXATION TERM IS 10.07 mHa.
# Prediction sha256 34068ce51a1f65ed661ff30a6c6625672cde1d983592ebe73ab60fb4515fb505, filed first.
# Instrument pack79/fixed79.py — FIVE declared lines from sealed rt/hfc2.py run2.

## CAN-FAIL, RUN FIRST, PASSED
The comparator must be able to return ORDERING FAILS. Control: 4f, deep in the [Rn] core.
**Control returned eps(4f) = -12.666044 Ha, eps(6d) = -0.176897, gap = -12489.147 mHa,
ORDERING FAILS.** The instrument returns both verdicts. Prediction sha checked on every
invocation; the driver halts without it.

## MACHINERY CROSS-CHECK — THE FROZEN PROBE REPRODUCES THE SELF-CONSISTENT SOLUTION
Phi_d* converged in 44 iterations, E = **-25694.541630577907 Ha**, which is the sealed
pack77/o89_89_A.jsonl 6d row **to every digit**. eps(6d) = -0.176898.
Re-solving 6d as a FROZEN-CORE PROBE, with the core built independently, returns
**-0.176897146** — agreement to 1e-6 Ha. The frozen construction is the same operator.

## THE MEASUREMENT
| object | value |
|---|---|
| eps_4^{l=2}(F_core[Phi_d*])  — 6d, 3 nodes | **-0.176897 Ha** |
| eps_3^{l=3}(F_core[Phi_d*])  — 6f, 2 nodes, beta=0.4 | **-0.021528 Ha** |
| eps_3^{l=3}(F_core[Phi_d*])  — 6f, 2 nodes, beta=0.15 | -0.021077 Ha |
| **GAP, ONE FIELD** | **+155.369 mHa (beta=0.4), +155.820 (beta=0.15)** |
**eps_3^{l=3} > eps_4^{l=2} AT ONE FIXED FIELD AT Z=89. THE ORDERING HOLDS.**
Both probes carry their TARGET node count: 6d nd=3, 6f nd=2.

## AND THE RELAXATION TERM — s78's ONE GENUINELY OPEN, GENUINELY SEPARATE OBJECT — IS MEASURED
CLOSE-S78 §4.2: *"What remains genuinely open and genuinely separate is the RELAXATION
term alone."* In eigenvalue currency, at Z=89:
  * TWO FIELDS   eps(6f in Phi_f*) - eps(6d in Phi_d*) = -0.031600 - (-0.176897) = **145.297 mHa**
  * ONE FIELD    eps(6f in Phi_d*) - eps(6d in Phi_d*) = -0.021528 - (-0.176897) = **155.369 mHa**
  * **RELAXATION TERM = 10.072 mHa, and it acts to CLOSE the gap, not open it.**
**THE TERM IS 15.4 TIMES SMALLER THAN THE FIXED-FIELD GAP IT WOULD HAVE TO ERASE.**
This is the first number ever put on that object. It is a MEASUREMENT AT ONE Z, not a bound.

## PREDICTION SCORED — W1 W2 W4 W5 CORRECT, W3 CORRECT IN ITS CHECK AND WRONG IN ITS COMPARAND
  W1 the ordering holds at fixed field . . . . . . **CORRECT**, +155.369 mHa
  W2 frozen gap exceeds relaxed gap; frozen 6f above relaxed 6f . **CORRECT ON BOTH
     CLAUSES AND ON THE FILED RATIONALE** — 155.369 > 145.297, and frozen 6f is
     10.07 mHa less bound than relaxed 6f. Denying 6f its own core relaxation cost it
     exactly that.
  W3 the l=2 probe reproduces the sealed 6d . . . **THE CHECK PASSED TO 1e-6 — BUT THE
     PREDICTION NAMED -0.15762 AS THE COMPARAND AND THAT IS THE WRONG OBJECT. See F79.2.
     Recorded as a hit on the check and an error in the statement.**
  W4 the l=3 probe needs the refined scan . . . . **CORRECT** — fine_used 2 at beta=0.4,
     4 at beta=0.15. The standard bracket misidentified the state in the frozen field too.
  W5 gap between 126 and 250 mHa . . . . . . . . **CORRECT** — 155.4.

## RECORDED AGAINST THIS RESULT, NOT BURIED
1. **THE INSTRUMENT'S FIRST RUN RETURNED "NO ZERO AT TARGET NODE COUNT" AND THAT WAS AN
   ARTEFACT OF ITS OWN SCAN BOUND.** The shallow bound was 0.15*e = -0.0265 and W2 had
   already predicted the state lies ABOVE -0.0316. **The instrument reported on what it
   admitted — F79.1's shape, one file later, in code I wrote this session.** Caught before
   scoring, bound widened to -2e-4, amendment declared as E5 in the source. **Had W2 not
   been filed first, "no zero" would have been reported as a finding.**
2. **beta-DEPENDENCE OF 0.451 mHa** between beta=0.4 and beta=0.15 on the 6f probe. The
   frozen probe carries a resolution limit of that order — F47.3's shape. It is 340 times
   smaller than the gap and does not touch the verdict, and it is NOT to be quoted as
   precision better than ~0.5 mHa.
3. **Vc = 0 FOR THE PROBE** is a declared choice, applied identically to both channels.
   The 19.3 mHa difference between eps(6d) and the sealed dE is where Vc and the core
   relaxation live. A different choice moves both channels, not one.
4. **ONE Z. ONE PAIR. ONE FIELD.** This is a measurement of the clause-1 inequality at its
   tightest instance. **IT IS NOT A DERIVATION OF IT AND MUST NEVER BE QUOTED AS ONE.**

## WHAT THIS CHANGES FOR CLAUSE 1
CLOSE-S78 established that the lower bound IS clause 1, that freezing the field does not
make the inequality free, and that what remains is a cross-channel property of F_core.
**THAT STRUCTURE IS UNCHANGED — NO PROPERTY HAS BEEN DERIVED HERE.** What has changed:
  * the fixed-field object is now **COMPUTABLE AND COMPUTED**, where s77 could not reach
    the f channels at Z=89 at all;
  * the target inequality has a **MEASURED MARGIN, 155.4 mHa**, so any candidate property
    can now be tested against a number instead of argued about;
  * the relaxation term is **10.072 mHa AND CLOSES THE GAP**, so a property proving the
    fixed-field inequality with more than 10.1 mHa to spare would carry the full claim
    at this Z. **THAT IS A QUANTITATIVE TARGET FOR ROUTE B, AND THERE WAS NONE BEFORE.**