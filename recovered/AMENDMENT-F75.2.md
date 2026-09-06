# AMENDMENT — F75.2. THE SEVENTH PERIOD LENGTH. SESSION 75.
# NO SEALED FILE IS EDITED. Standing 4 / F44.1 route.
# FOUND WHILE WRITING THE FORMAL DERIVATION STATEMENT, BEFORE THE CLAIM WAS
# TRANSCRIBED INTO IT. Same class as F75.1, at a site F75.1 did not cover.

## THE FAULT. SEVERITY: RECORD. TOUCHES NO SCORED ROW.
`pack63/ASSEMBLY-RUNG-0.md` SS2 states:
    period starts   Z = 1, 3, 11, 19, 37, 55, 87, 119
    period lengths  **2, 8, 8, 18, 18, 32, 32**
A period length is the DIFFERENCE of consecutive starts. Therefore:
    2  = 3-1     8  = 11-3    8  = 19-11
    18 = 37-19   18 = 55-37   32 = 87-55        <- ALL starts <= 108. SCORED.
    32 = 119-87                                 <- REQUIRES Z=119. OUTPUT.
**SIX OF THE SEVEN LENGTHS ARE DETERMINED ENTIRELY INSIDE THE SCORED REGION
Z=2..108. THE SEVENTH IS NOT.** It depends on the walk's predicted period start at
Z=119, above the boundary, against no measured configuration. Quoting all seven as
derived is the F75.1 class: the walk is correct, **THE DOCUMENT OVERSTATES WHAT IS
SCORED.**

## SS2 — REMOVE:
    period lengths  **2, 8, 8, 18, 18, 32, 32**
## REPLACE WITH:
    period lengths  **2, 8, 8, 18, 18, 32** — six lengths, every one fixed by
    period starts at Z <= 108 and therefore SCORED. The walk's next start falls at
    Z=119, giving a seventh length of 32; **that start lies above the boundary and
    the seventh length is OUTPUT, not evidence.**

## WHAT DOES NOT CHANGE, AND WHY THE RESULT IS NOT WEAKENED.
The Challenge names the sequence 2, 8, 8, 18, 18, 32, 32. **THE DERIVATION SUPPLIES
SIX OF ITS SEVEN TERMS AS SCORED RESULT AND THE SEVENTH AS A PREDICTION THAT AGREES
WITH IT.** Both doublings — 8,8 and 18,18 and the onset of 32 — are inside the
scored region. The structural claim (period lengths are an OUTPUT of a code
containing no notion of a period, no shell capacity sequence, no boundary) is
untouched, as is the CONTROL: forcing a single s-channel change at Z=19 returns
2,8,8,36,32,32.

## STATUS: F75.2 CLOSED. The Formal Derivation Statement carries the corrected form.