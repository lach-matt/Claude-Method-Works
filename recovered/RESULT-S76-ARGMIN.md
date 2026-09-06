# RESULT S76 — ARGMIN UNIQUENESS AND MARGIN. STEP 0(iii).
# Prediction PREDICTION-S76-ARGMIN.md, sha256 1db4610399e899a8a6d45e8a8f250a1a5e8d47d1dbd77e124ff5883b3b5b3c08
# filed and hashed BEFORE any margin number was read. 107 rows, Z=2..108. No sealed file edited.

## INSTRUMENT
nlchain.jsonl carries per row: `ent` (winner), `order` (FULL ranked candidate list
with energies), `margin`. Margin recomputed independently as order[1] - order[0] and
checked against the stored column. Winner checked against order[0] at every row.

## RESULT
  * **EXACT TIES: 0 of 107.** The argmin is attained once at every scored row.
  * **TIGHTEST MARGIN: 32.330 mHa at Z = 89 (6d over 7p).** Candidate set 9.
  * min 32.330 / median 207.0 / max 695.5 mHa. Rows below 1 mHa: 0. Below the
    0.05 mHa numerical floor: 0. **Floor-to-margin factor 646.**
  * Winner/order agreement: 107/107. Margin-column disagreements: **0 of 107** — the
    stored column and the recomputed difference agree everywhere.
  * Tightest six: Z=89 6d/7p 32.33 · Z=56 6s/5d 39.14 · Z=39 4d/5p 43.67 ·
    Z=72 5d/6p 45.07 · Z=90 6d/5f 54.05 · Z=19 4s/4p 54.11.

## PREDICTION SCORED — 3 OF 5, AND THE MISS IS THE ONE THAT MATTERS
  P1 zero exact ties . . . . . . . . . . . . . . . . . . . **CORRECT**
  P2 min above the 0.05 floor, in 1..60 mHa . . . . . . . . **CORRECT** (32.33)
  P3 tightest row in the d/f region, Z 55..60 or 88..92 . . **CORRECT** (Z=89)
  P4 per-row argmin margin NOT identical to the owned 32.33 **WRONG**
  P5 margins narrow as Z grows . . . . . . . . . . . . . . . **WRONG**
  P6 no stored runner-up column, result VOID . . . . . . . . did not occur

**P4 IS A SELF-FLAG AND IT FIRED. I WROTE: "If they come out equal, that is a flag
that I have re-read the same column, not measured a new one." THEY CAME OUT EQUAL,
TO THE DIGIT. The ledger's "tightest chain margin 32.33 mHa at Z=89" IS the minimum
over rows of the per-row argmin margin. STEP 0(iii)'s central number was already
owned and I did not measure a new one. Reported as a re-read.**

**P5 WRONG AND WORTH KEEPING:** the two widest rows after helium are Z=104 (591.9)
and Z=103 (556.5) — heavy, not light. Margins do not narrow with Z. **The tight rows
are where CHANNELS CROSS, not where Z is large**, which is the same statement the
tie-break failures already make from the other direction.

## WHAT IS NEW, STATED AT ITS ACTUAL WEIGHT — WHICH IS SMALL BUT NOT ZERO
  1. **Ties are excluded by MEASUREMENT, not by assumption.** Step 0(iii) asked for
     ties to be "excluded or handled". They are excluded, at every scored row.
  2. The stored margin column is now VERIFIED against the ranked list it derives
     from, 107/107, a check that could have gone red and did not.
  3. Runner-up IDENTITIES are now on the record per row. At Z=89 the runner-up is
     **7p, not 5f** — the contest Ac loses is not the one the tie-break story names.

## WHAT THIS DOES AND DOES NOT CLOSE
**CLOSES for the STATEMENT:** the argmin of §3 step 3 is unique at all 107 scored
rows, by a margin 646x the numerical floor.
**DOES NOT CLOSE for a PROOF:** uniqueness at 107 measured rows is not uniqueness of
the argmin as a property of Φ. Route A's target is unchanged and now sharper: **the
certified enclosure width must come in strictly under 32.330 mHa**, and the candidate
truncation must still be proved rather than sampled — note the candidate set is not
of fixed size (it ranges 3 to 13 across the rows measured).