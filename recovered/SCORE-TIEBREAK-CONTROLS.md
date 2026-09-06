# SCORE — THE FOUR TIE-BREAK CONTROL ROWS, RE-RUN UNDER QUARANTINE
# SESSION 64. F63.2 remedy (a), on M's ruling.
# Prediction: pack63/PREDICTION-TIEBREAK-CONTROLS.md
# sha256 0b12ef684c1e39b3b26fc9d0ebf988cda1929e2e658047f8ee2e3b88f0b61c20
# VERIFIED in this container at the open, before any row at these Z was read,
# and re-verified by the scorer at every invocation.
# Scorer: pack64/tbscore.py, can-failed in SEVEN directions before use.
# Rows: pack64/tbctrl64.jsonl. NOT ctrl64.jsonl — see the ruling on naming.

    T1  entrant unchanged, ok=True 4/4         PASS
    T2  the tie-break departure survives       PASS
    T3  margins clear the floor by >= 20x      PASS

    VERDICT: PASS. No falsifier fired. The s63 restatement is NOT withdrawn.

---

## 1 · THE ROWS

Restart mode: the reference is the OBSERVED configuration of Z-1 from `ground.py`,
not the walk's own single-configuration build. c = 137.035999. CORR=False. Every
solve through `nlguard.run_guarded`.

    Z    ref cfg (observed, Z-1)     ent   observed   ok     D_ent      margin
    57   Ba  ...5p6 6s2               5d      5d      True  -0.20585   67.56 mHa
    58   La  ...5p6 5d1 6s2           4f      4f      True  -0.36700  121.15 mHa
    89   Ra  ...6p6 7s2               6d      6d      True  -0.15762   32.33 mHa
    91   Th  ...6p6 6d2 7s2           5f      5f      True  -0.30535   81.95 mHa

**Every one of the four reproduces both the chained entrant AND the measured
differentiating electron under a reference configuration the walk did not build.**

## 2 · T2 — THE DEPARTURE ITSELF, WHICH IS WHAT THE CONTROL WAS FOR

The clause at issue is not the entrant but the head-to-head between the two channels
the Madelung tie-break orders. Depths at the same Z, same field, same reference:

    Z=57    5d  -0.20585    4f  -0.10556    5d deeper by  100.29 mHa   2006x floor
    Z=89    6d  -0.15762    5f  -0.03146    6d deeper by  126.16 mHa   2523x floor

Madelung's tie-break requires the lower n first — 4f at 57, 5f at 89. **The field
puts them second, by margins of 100 and 126 mHa, under the physical reference.** The
departure is not an artefact of the single-configuration reference. It is the field.

## 3 · T3 — AND IT IS NOT NUMERICS

Working floor 0.05 mHa (Rung 7 grid floor 0.0108 mHa; s61 seed-memory floor
<= 0.05 mHa; the larger and more inclusive taken, as everywhere else in this project).

    entrant margin  Z=57   67.56 mHa   1351x floor
    entrant margin  Z=89   32.33 mHa    647x floor
    predicted                          >= 20x

The tightest quantity anywhere in this score is the Z=89 entrant margin at 647x.

**ONE GUARD NOTE, STATED RATHER THAN LEFT IN THE JSON.** At Z=89 the 5f channel
converged at guard rung 1, not rung 0 (320 iterations at beta=0.2). Under F47.3 a
guarded D carries ~1e-5 Ha of rung-mixing in its last stored digit. That is four
orders below the 126.16 mHa gap it enters, and it moves 5f further from contention,
not closer. Every other channel at every other row converged at rung 0.

## 4 · WHAT THE ROWS SHOW THAT THE PREDICTION DID NOT ASK FOR

Predicted nothing about this and it is therefore an OBSERVATION, not a scored result,
and not a theorem. Reading the four rows in pairs:

    Z=57  reference has NO 5d occupied    5d beats 4f by  100.29 mHa
    Z=58  reference has 5d1 occupied      4f beats 5d by  121.15 mHa
    Z=89  reference has NO 6d occupied    6d beats 5f by  126.16 mHa
    Z=91  reference has 6d2 occupied      5f beats 6d by   81.95 mHa

**The ordering inside the block reverses as a function of what is already occupied.**
The f channel is not shallow at these Z; it becomes the deepest channel once the
first d electron is in place. That is the 4f/5f contraction doing the work, and it is
visible here under OBSERVED references, so it cannot be attributed to the chain's own
build. It is four rows. It licenses no claim about any other row, and the assembly's
wording may not be strengthened on it.

## 5 · WHAT THIS DOES NOT LICENSE — CARRIED VERBATIM IN SPIRIT FROM THE PREDICTION

Four rows are four rows. A PASS bounds the single-configuration effect on the
tie-break AT Z = 57, 58, 89, 91 and nowhere else. Nothing here licenses a claim about
the other 103 rows. Rung 2's separate finding — that the first-entry rows and the
anomaly rows have empty intersection — is untouched by this and stands on its own
evidence.

**What the PASS does buy, and it is the thing the session was run for:** the s63
tie-break restatement rested entirely on CHAINED rows, whose reference is the walk's
own single-configuration build. It now also holds under the physical reference at all
four rows where the restatement is made. Rung 2's "the ordering is immune" does not
collapse to n+l <= 6.

## 6 · THE SCORER WENT RED IN SEVEN DIRECTIONS BEFORE IT WAS BELIEVED

    [0] unmodified rows                      -> PASS
    [1] Z=57 entrant forced to 4f            -> WITHDRAW
    [2] Z=89 entrant forced to 5f            -> WITHDRAW
    [3] Z=57 margin driven under the floor   -> NOT-DECIDABLE
    [4] Z=91 row removed                     -> NO-DATA
    [5] Z=58 ok forced False                 -> FAIL
    [6] Z=57 5d/4f depths swapped in order   -> FAIL

**AND IT WENT RED ON THE REAL DATA ONCE, WHICH IS WHY IT IS IN THE LEDGER.** The
first scoring run returned NO-DATA: Z=91 had been computed and reported but not
appended to `tbctrl64.jsonl`. The scorer caught a missing row that a human eye had
already passed over. Had it only been able to return PASS, the session would have
reported four rows on the strength of three.

## 7 · PROVENANCE OF EVERY ROW IN THE FILE

    Z=57  rt/nlchain.py restart 57     sealed instrument, unmodified
    Z=58  rt/nlchain.py restart 58     sealed instrument, unmodified
    Z=89  pack64/tbstep.py 89          resumable driver — see FAULT-F64.2
    Z=91  pack64/tbstep.py 91          resumable driver — see FAULT-F64.2

`tbstep.py` reproduces `nlchain.py restart` bit-for-bit at Z=57 and Z=58, every field
but `sec` and the added `driver` provenance field. Receipts:
`RECEIPT-CANFAIL-TBSTEP-Z57.jsonl`, `RECEIPT-CANFAIL-TBSTEP-Z58.jsonl`.

**NOTHING OF THE QUARANTINED `ctrl64.jsonl` WAS READ, AT ANY POINT, BY ANY MEANS.**
No row, no clause, no count, no margin. It is not present in this container and no
hash of it is held here. §2.13 held.
