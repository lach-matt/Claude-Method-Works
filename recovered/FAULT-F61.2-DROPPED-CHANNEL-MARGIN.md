# F61.2 — THE SEED ROWS' `dmargin` AND `ORDER_MATCH` COMPARE UNLIKE CHANNEL SETS
# Raised 2026-08-20T17:33Z, SESSION 61. Registered BEFORE P3 was scored.
# Standing 8 (s60) is what caught it. This is F44.2 / F59.1 / F60.3's failure mode,
# fourth appearance, and the FIRST time it was caught by the standing rule rather than
# by luck or by a later session.

## WHAT IS WRONG

`pack61/seedtest.py:120-127` scores every seed row against the SEALED row:

    o["ORDER_MATCH"] = ([k for k,_ in o["order"]] == [k for k,_ in sealed["order"]])
    o["dmargin"]     = o["margin"] - sealed["margin"]

TWO INDEPENDENT DEFECTS, EITHER SUFFICIENT TO INVALIDATE THE COLUMN.

**(a) THE BASELINE IS THE SEALED ROW, WHICH F61.1's OWN REMEDY #1 FORBIDS.**
F61.1 established four hours ago that the sealed rows at Z<=56 are PRE-GUARD and
heterogeneous in construction, and ruled: *"The seed test does not compare to the sealed
row. Its baseline is the harness's own seed-A row, same construction, seed varied and
nothing else."* The remedy file records that as **Done**. IT WAS NOT DONE IN THE CODE.
The ruling was made and the instrument was never changed. A ruling that reaches no
artefact is R 1670's finding exactly: a practice with no file behind it.

**(b) `margin` IS COMPUTED OVER SURVIVING CHANNELS ONLY, AND THE SEEDS DROP DIFFERENT
CHANNELS.** Receipt, `rt/nlchain.py`:

    :80   ok  = {k:v for k,v in D.items() if v.get('D') is not None}
    :83   srt = sorted(ok, key=...)
    :84   marg = ok[srt[1]]['D'] - ok[srt[0]]['D']
    :95   order = [[k, ok[k]['D']] for k in srt],  nfail = len(D) - len(ok)

A channel that does not converge under a given seed is REMOVED from `order` and cannot
be the runner-up. The margin then measures the winner against whatever is left.
**A seed that kills the runner-up widens the margin without moving a single eigenvalue.**

## THE SIZE OF THE ARTIFACT, MEASURED

Dropped sets derived from `nlchain.candidates(cfg_prev)`, which is deterministic and
needs no SCF — NO ROW WAS RE-RUN AND THE HARNESS WAS NOT EDITED (see REMEDY 2):

    Z=19  candidates 5  : 3d 4s 4p 4d 4f
          seedA  order 5   dropped {}          nfail 0
          seedB  order 3   dropped {4p,4d}     nfail 2
          seedC  order 3   dropped {4p,4d}     nfail 2
    Z=20  candidates 10 : 3d 4s 4p 4d 4f 5s 5p 5d 5f 5g
          seedA  order 9   dropped {5d}        nfail 1
          seedB  order 4   dropped {4p,4d,5s,5p,5d,5f}   nfail 6
    Z=39  candidates 11 : 4d 4f 5p 5d 5f 5g 6s 6p 6d 6f 6g
          seedA  order 9   dropped {5d,6d}     nfail 2

Every derived count reproduces the row's own recorded `nfail`. The derivation is exact.

At Z=19 the runner-up **4p is dropped under B and C**. The printed `dmargin` is +0.03555
(B) and +0.03558 (C) — quoted against a sealed margin whose runner-up is 4p. Recomputed
on the A n B intersection {4s,3d,4f}, the SAME quantity on the SAME channels:

    margin_int   A 0.08967   B 0.08966   C 0.08969      |d| <= 0.02 mHa

**THE ENTIRE 35 mHa "SEED EFFECT" ON THE MARGIN IS THE MISSING RUNNER-UP.** Had this
column been read as filed, s61 would have reported a 35 mHa seed sensitivity at the
tightest row in the light chain — a false alarm three orders of magnitude too large, in
the one place the ordering result is most exposed.

## WHAT IS *NOT* AN ARTIFACT, AND IS KEPT

`nfail` rising 0 -> 2 (Z=19) and 1 -> 6 (Z=20) is a REAL AND UNPREDICTED FINDING about
the seeds and it is not explained away by this fault. **A worse starting potential does
not move the converged answer; it costs CHANNELS.** That is a statement about the
CONVERGENCE FLOOR, which is item 2 of the s61 work list, and it is entered there rather
than banked here. It is also why the prediction's NO-DATA clause was written.

## WHAT THIS DOES AND DOES NOT TOUCH

DOES NOT touch P1, P2, P4 — none of them reads `margin` or `order`. Their receipts are
`seedA.json`, `seedE19.json`, `seedE39.json` and stand unaffected.
DOES NOT touch `ENT_MATCH`: the entrant is the MINIMUM over survivors, the entrant is
4s / 4s / 4d and is never among the dropped, and a dropped channel can only remove a
competitor, never install one. The entrant column is sound as printed — but it is sound
by argument, and the argument is written here rather than assumed.
DOES invalidate `ORDER_MATCH=false` at Z=19 seedB, Z=19 seedC, Z=20 seedB. **Those three
FALSE values are not order changes.** On the intersection the order is identical in all
three. P3 must be scored on the intersection or not at all.

## REMEDY
1. **P3 is scored by `pack61/seedscore.py`, on the A n X intersection, against the
   harness's own seed-A row.** The sealed-row columns remain in `seedO.jsonl` as filed —
   NOT edited, NOT deleted — and the scorer prints them beside the corrected figures so
   the discrepancy is visible rather than tidied away (R 1662, §H.4).
2. **`seedtest.py` IS NOT EDITED.** Three rows remain to be run (Z=20 C, Z=39 B, Z=39 C)
   and changing the instrument between rows is the heterogeneity F61.1 registered this
   morning. The dropped-set information is RECOVERED WITHOUT THE HARNESS, from
   `candidates()`. Cost of the alternative was measured before it was refused: an edit
   would have been additive to the output dict only, but "additive only" is what every
   heterogeneity looks like from inside the session that introduces it.
3. `seedtest.py:121` discards the `fail` dict that `nlchain.step` returns, so the ERROR
   TEXT of each dropped channel is lost for all six rows already run. Recorded as a loss,
   not repaired. A future seed or floor study should retain it.
4. F61.1's remedy #1 is re-marked **DECLARED, NOT IMPLEMENTED**, and the general finding
   entered: **A REMEDY IS DONE WHEN AN ARTEFACT CHANGES, NOT WHEN A FILE SAYS SO.**
