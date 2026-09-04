# AMENDMENT — F75.1. THE ASSEMBLY'S COVERAGE CLAIM. SESSION 75.
# NO SEALED FILE IS EDITED. Standing 4 / F44.1 route: exact replacement text only.
# RAISED BEFORE THE FORMAL DERIVATION STATEMENT WAS WRITTEN, because that statement
# quotes this document and would otherwise inherit the defect.

## THE FAULT. SEVERITY: RECORD. TOUCHES NO SCORED ROW.
`pack63/ASSEMBLY-RUNG-0.md` claims coverage of **119 rows** at three sites. The
standing boundary rule (DELIVERABLE-1 SS232, carried in every bridge since s72) is:
**107 ROWS, Z=2..108, SCORED. Z=109..120 ARE OUTPUT - PREDICTED AND UNSCORED. Any
claim of 119 derived rows is a boundary violation.** Neither pack64's revision nor
pack70's stale-lines amendment touches it. The walk itself is correct; **THE
DOCUMENT OVERSTATES WHAT THE WALK IS SCORED ON.**

## LINE 201 — REMOVE:
    ### THE ORDERING CLAUSE OF MADELUNG — **DERIVED. ZERO INVERSIONS IN 119 ROWS.**
## REPLACE WITH:
    ### THE ORDERING CLAUSE OF MADELUNG — **DERIVED. ZERO INVERSIONS IN 107 SCORED
    ### ROWS, Z=2..108.** The walk continues to Z=120 and inverts nowhere there
    ### either, but Z=109..120 carry PREDICTED labels against no measured
    ### configuration and are OUTPUT, not evidence.

## LINE 337 — REMOVE:
      * The n+l ORDERING clause — zero inversions in 119 rows.
## REPLACE WITH:
      * The n+l ORDERING clause — zero inversions in 107 scored rows, Z=2..108.

## LINE 380 — REMOVE:
    single exception in 119 steps; and departs from the n+l tie-break at precisely
## REPLACE WITH:
    single exception in the 107 scored steps Z=2..108; and departs from the n+l
    tie-break at precisely

## NOT AMENDED, AND WHY.
Lines 192 and 281 name **Z = 119 as a period start and as a first-entry row**.
These are STRUCTURAL OUTPUTS of the walk in the predicted region, not claims of
scored coverage. **THEY ARE CORRECT AS WRITTEN AND ARE LEFT ALONE.** The fault is
the coverage claim, not the integer.

## STATUS: F75.1 CLOSED.