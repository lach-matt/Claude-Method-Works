# ADDENDUM TO SCORE-SEED-INDEPENDENCE — P3 RESCORED ON THE INTERSECTION
# 2026-08-20T17:40Z, SESSION 61, SEGMENT 2.
# SUPERSEDES THE WORDING OF §P3 ONLY. Everything else in that file and in
# BRIDGE-LOWDIN-SESSION-61.md STANDS AS FILED AND IS NOT EDITED (§H.4, R 1662).
# New instrument: `pack61/seedscore.py`. New fault: F61.2, F61.3. New data: Z=20 seed C.

## WHY THIS EXISTS
`SCORE-SEED-INDEPENDENCE.md` §P3 reads **"THE ENTRANT CLAUSE HOLDS 3/3. THE ORDER CLAUSE
FAILS AS WORDED"**, and then explains correctly, in prose, that nothing reorders — that
weakly-bound channels simply fail to converge and drop out of the list. **The explanation
was right and it was not an instrument.** A prose caveat beside a FAILS verdict is how a
false negative survives into a later session that reads only the verdict.

F61.2 turned it into a measurement. `seedscore.py` compares each variant against the
harness's own seed-A row, ON THE INTERSECTION OF CHANNELS THAT CONVERGED UNDER BOTH, and
derives every dropped set from `nlchain.candidates()` — deterministic, no SCF, no re-run,
no edit to `seedtest.py`. **It was can-failed in three directions before it was trusted:**
it goes red on a forced entrant, red on an inverted order, red on a 10 mHa depth shift,
and returns to green on reload. A scorer that cannot go red is not a scorer (§4.6).

## THE RESCORE — `SCORE-P3-INTERSECTION.log`

    row          entrant    order on A n X    max|dD|      margin_int A -> X     dmargin_int
    Z=19 A->B    4s = 4s    IDENTICAL (3)     0.020 mHa    0.08967 -> 0.08966    -0.010 mHa
    Z=19 A->C    4s = 4s    IDENTICAL (3)     0.020 mHa    0.08967 -> 0.08969    +0.020 mHa
    Z=20 A->B    4s = 4s    IDENTICAL (4)     0.050 mHa    0.09148 -> 0.09153    +0.050 mHa
    Z=20 A->C    4s = 4s    IDENTICAL (4)     0.080 mHa    0.09148 -> 0.09159    +0.110 mHa
    Z=39 A->B    4d = 4d    IDENTICAL (5)     0.030 mHa    0.04367 -> 0.04368    +0.010 mHa
    Z=39 A->C    NO-DATA — seed C fails its own node count at 4d BEFORE any SCF runs

Every derived dropped-set count reproduces its row's own recorded `nfail` — 9 rows, 9
matches. The derivation is exact, not approximate.

**P3 PASSES ON ALL THREE CLAUSES.** Predicted |dmargin| < 5 mHa; largest observed
**0.110 mHa**, a factor of 45 under. Entrant identical at every converging comparison.
Order identical at every converging comparison.

## THE CORRECT STATEMENT, REPLACING "THE ORDER CLAUSE FAILS AS WORDED"
**THE ORDERING IS SEED-INDEPENDENT. THE COVERAGE IS NOT.**
Two different quantities were sharing one column. Separated, each is clean:
  * ORDERING — winner, order, margin, depth. Moves by <= 0.11 mHa under a 52 Ha change of
    starting potential. PASSES the prediction by a factor of 45.
  * COVERAGE — how many candidates the guard can converge at all. Degrades badly:
    nfail 0->2 (Z=19), 1->6 (Z=20), 2->6 (Z=39). A REAL and UNPREDICTED finding.
**A bad seed costs channels, not accuracy.** The bridge's §2 caveat is therefore retained
in full and is not weakened by this rescore — it moves from being a defect in P3 to being
a finding in its own right, and it belongs to Rung 7 (floor) and Rung 9 (truncation),
where the s62 list already places it.

The caveat that survives untouched and must travel: **the winner survived every seed at
all three rows, and that is an observation at three rows, not a theorem. A seed that
killed a WINNER would change the entrant.**

## NEW DATA THIS SEGMENT — SEED C REACHES Z=20
The score file and bridge were written when Z=20 seed C did not yet exist; both print
`--` for it. **It was run at 17:34:39Z and it PASSES:** entrant 4s, order identical on the
intersection, max|dD| 0.080 mHa, dmargin_int +0.110 mHa. The bare-Coulomb seed — no TFD,
no clamp, no exchange, no screening, no chosen constant — now returns the sealed entrant
at TWO rows rather than one. **P3 rests on five converging comparisons, not three.**

Seed C does NOT reach Z=39: it fails its own node count at 4d in the seed generator,
before any SCF. That is a Z ceiling of the bare-Coulomb start on this grid, not a result
about the field, and it is reported as NO-DATA exactly as the prediction required.

## F61.2 — REGISTERED, CLOSED
`pack61/FAULT-F61.2-DROPPED-CHANNEL-MARGIN.md`. The `dmargin`/`ORDER_MATCH` columns in
`seedO.jsonl` compare unlike channel sets AND use the sealed row as baseline, which
F61.1's own remedy 1 forbade four hours earlier — **the ruling was made and the
instrument was never changed.** General finding entered: **A REMEDY IS DONE WHEN AN
ARTEFACT CHANGES, NOT WHEN A FILE SAYS SO.** The columns remain in `seedO.jsonl` as filed
and the scorer prints them beside the corrected figures, so the discrepancy stays visible.

## F61.3 — TWO WRITERS ON ONE WORK TREE, AND WHAT IT COST
Registered on discovery, 17:38Z. `pack61/` was written by two concurrent processes this
session. Evidence, not inference:
  * `seedO.jsonl` carries **9 rows for 8 distinct (Z, mode) pairs.** Z=39 seed B appears
    TWICE, at 64 s and 65 s.
  * `SCORE-SEED-INDEPENDENCE.md` (17:33Z) and `BRIDGE-LOWDIN-SESSION-61.md` (17:34Z) were
    both written BEFORE Z=20 seed C existed (17:34:39Z), which is why both print `--`.
COST: one duplicated 65 s computation. **NO CONTAMINATION OF ANY RESULT** — the scorer
keys on (Z, mode) and last-wins, and the two rows are identical, so which one it read
cannot matter. Checked rather than assumed.
STANDING RULE PROPOSED FOR s62: **a session appends to a results file from ONE writer, and
any results file is checked for duplicate keys before it is scored.** Cheap, and it is the
only reason the duplicate was found rather than silently averaged into a conclusion.

## UNPLANNED POSITIVE — A FOURTH DETERMINISM RECEIPT, AND THE FIRST OFF THE SEALED SEED
The duplicated Z=39 seed B rows are **BYTE-IDENTICAL in all 13 recorded fields** —
entrant, depth, margin, full order, nfail — differing only in wall-clock seconds:

    order run 1   4d -0.19559  5p -0.15191  4f -0.03138  5g -0.02001  6f -0.01396
    order run 2   4d -0.19559  5p -0.15191  4f -0.03138  5g -0.02001  6f -0.01396

F60.2's receipt B and s61 §4 both established determinism on the SEALED seed. **This is
the first receipt showing the walk is deterministic under a PERTURBED seed as well** — the
non-convergence pattern that costs six channels at Z=39 is itself reproducible to the last
digit, not a stochastic failure. That matters for Rung 7: a coverage floor that reproduces
is a floor that can be measured.

## WHAT THIS ADDENDUM DOES NOT CHANGE
P1, P2, P4, P5 stand exactly as scored. Rungs 3 and 4 close as the score file and bridge
state. The s62 work list is unchanged in content; items 1 (Rung 7 floor) and 3 (Rung 9
truncation) each gain the coverage finding above, which the bridge already anticipated.
Scope is unchanged and may not be overstated: **five converging comparisons at three rows,
not 107.** All rows CHAINED-mode (Rung 8 DERIVED); nothing empirical on either side.
