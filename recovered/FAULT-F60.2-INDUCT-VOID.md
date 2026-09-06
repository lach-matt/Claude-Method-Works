# F60.2 — pack53/induct.jsonl AND pack54/induct34.jsonl ARE FAULTED. PROVEN, NOT PRESUMED.
# s59 bridge §6 item 4. Closed in s60 at a cost of two reads and one 2-second instantiation.

## RECEIPT A — THE INSTRUMENT (reproduce in ~2 s)
`pack53/induct.py:13-22` carries cinf.py's patch body verbatim, by its own docstring's
admission ("reused deliberately"). It rebinds three kernel `__defaults__` and nothing
else: no `K.C0`, no `HS.C0`, no `HFSR.__init__.__defaults__`.

    import induct; induct.patch(1e6)
    -> patched 3 defaults
    t7c_hfsr.HFSR(2,[(1,0,2.0)]).c  ->  137.035999      UNMOVED

Same failure as F59.3, same cause: `HFSR.__init__` carries its own `c=C0` bound at import
and passes it POSITIONALLY at `t7c_hfsr.py:39`. A patched default is unreachable.

## RECEIPT B — THE EMPIRICAL PROOF, AND IT IS TOTAL
Every `cinf-chainref` row was compared channel-by-channel against the sealed `chain` rows
of `rt/nlchain.jsonl` at the same Z:

    pack53/induct.jsonl     21 rows, Z=25..80    21/21 eigenvalues BYTE-IDENTICAL, 0 differ
    pack54/induct34.jsonl   34 rows, Z=25..104   34/34 eigenvalues BYTE-IDENTICAL, 0 differ

Same c AND same reference configuration -> the driver recomputed the sealed chained walk
exactly. **These 55 rows are not a c=1e6 walk. They are a bit-for-bit duplicate of
`nlchain.jsonl`'s chain rows and carry ZERO information beyond it.**

## VOIDED
The `"clight": 1000000.0` label on all 55 rows is FALSE. Any s53/s54 statement resting on
`induct.jsonl` or `induct34.jsonl` **as a c-comparison** is void: it compared the sealed
walk with itself and was true by construction, exactly as `ctrl137.jsonl` was (F59.3).
The files are RETAINED, not deleted — they are now evidence, and see below.

## NOT VOIDED, AND THE HOLE IS ALREADY FILLED
Clause 3 does not depend on these files. It closed today by the genuine route:
`pack60/SCORE-EXPOSED-13.md`, EX-1 holding at 13/13 with an instrument can-failed at
sites=4 and shown to move Z=79's 1s by 314 Ha. The void leaves no gap behind it.

## THE ONE THING THESE FILES DO PROVE — AND IT IS WORTH KEEPING
55 independent re-computations, run in two different sessions by a different driver from
a cold import, reproduce the sealed chained walk **to the last digit at Z = 25 through
104**. That is an unplanned, uncontaminated determinism-and-replay result of a size the
canary has never had. Recorded as a POSITIVE finding of s60. It does not rescue the
c-claim and is not offered as doing so.

## STANDING RULE THIS RE-CONFIRMS (s59 §7 item 7)
A control must be proven to vary the thing it controls for, BEFORE it is used as a
control. Both faults were reachable by a 2-second instantiation at the moment the
instrument was written. **Neither was ever run until after the physics was claimed.**
