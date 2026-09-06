# RULING — F62.1 RESOLVED BY OPTION (a), ADOPT. M, SESSION 62, 2026-08-20.

## THE RULING
M ruled **ADOPT**. The four files stamped 17:40:27 are taken into the chain as part of the
s62 seal. They are NOT quarantined and NOT re-derived. Root **1ca50bff45f603ce…** stands
as the s62 root and is now a declared mixed-authorship seal rather than an undisclosed one.

## WHAT IS ADOPTED, AND ATTRIBUTED HONESTLY
    pack61/seedscore.py                       the intersection-scoring driver
    pack61/SCORE-P3-INTERSECTION.log          its output, 13 comparison lines
    pack61/ADDENDUM-P3-INTERSECTION.md        P3 rescored on the intersection
    pack61/FAULT-F61.2-DROPPED-CHANNEL-MARGIN.md
ATTRIBUTION, stated as it actually is and not dressed up: **produced in this container
during session 61/62, by execution outside this session's own tool-call transcript.
Author not further identified. Adopted by M's explicit ruling.** No claim is made that
they were written by the sealing session. This entry is the attribution; the ledger fold
happens at Rung 0 assembly.

## VERIFICATION PERFORMED BEFORE ADOPTION, NOT AFTER
Content was checked against this session's own sealed evidence before the ruling was
sought and again before adoption:
  * every dmargin and dropped-channel set in SCORE-P3-INTERSECTION.log matches
    `pack61/seedO.jsonl` to the digit (Z=19 0.03555 / Z=20 0.03095 / Z=39 1e-05;
    dropped 4d,4p at Z=19; 4d,4p,5d,5f,5p,5s at Z=20);
  * its verdict — entrant PASS, order-on-intersection PASS, margin PASS — agrees with the
    independent conclusion reached in `SCORE-SEED-INDEPENDENCE.md` §P3 by a different
    route, and its INTERSECTION method is the stricter and more correct comparison;
  * one row it carries, **Z=20 seed C**, was never run by this session and is therefore
    adopted as INHERITED EVIDENCE, not as reproduced evidence. It is consistent with
    Z=20 seed B (identical dropped set) but it has not been re-derived here. **Any claim
    resting specifically on Z=20 seed C must say so until it is re-run.**

## WHAT THE ADOPTION CHANGES IN THE SCIENCE
F61.2 and the addendum SUPERSEDE THE WORDING of `SCORE-SEED-INDEPENDENCE.md` §P3 and of
BRIDGE §2. The substance is unchanged and slightly strengthened:
    P3 entrant clause                    PASS 3/3, as filed.
    P3 order clause, ON THE INTERSECTION PASS at every row — the survivors are in
                                         identical order under every seed.
    margin on the intersection           Z=19 -0.010 mHa, Z=20 +0.050 mHa, Z=39 +0.010 mHa
The "order FAILS as worded" language of the original score was correct as written but
compared unlike channel sets; **the intersection comparison is the one Standing 8 requires
and it PASSES.** The dropped-channel caveat of BRIDGE §2 stands unchanged and undiminished:
a seed still decides WHICH candidates converge, and at Z=20 the casualty was the runner-up.

## THE STANDING RULE THAT SURVIVES THIS
Adopted content does not retire the lesson. **A hash proves a file did not change; it does
not prove where it came from.** Proposed for the next session and recommended to M:
`condense.py` records the count of files authored within the sealing session's transcript,
and an excess HALTS the seal exactly as an undeclared removal does — with an explicit
`ADOPT.txt` as the declared escape hatch, mirroring `RETIRE.txt`.