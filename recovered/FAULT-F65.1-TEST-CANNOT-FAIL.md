# F65.1 — THE RULED FIRST TASK OF SESSION 65 CANNOT FAIL, AND SO IS NOT A TEST
# Raised 2026-08-20, SESSION 65, at the open, BEFORE any prediction was filed and
# before any solve was run. Standing 7: a control must be proven to vary the thing
# it controls for. This is the same demand turned on a test.
# No sealed file is edited. Probes are read-only: pack65/circ.py, pack65/circ2.py.

## WHAT WAS RULED
`FINDING-ALPHA-THE-WHY.md` §6 and BRIDGE §4 item 1: define a continuous α valid at
each block's opening Z with the base channel unavailable, file prediction **T-B**
("α at the block's own opening Z is < 1 exactly where the lower-n channel enters
first; PREDICTED: agreement at 11 of 11"), re-run `alpha.py blocks`, and either
convert §5 into a result or kill it. Everything else in the session waits on it.

## WHAT WAS FOUND — TWO IDENTITIES, MEASURED, NOT ARGUED

**(1) α IS THE PAIR COMPARISON, RE-NORMALISED.** With
α = [D(n,l+1) − D(n,l)] / [D(n+1,l) − D(n,l)] and the denominator positive,
α < 1 ⟺ D(A) < D(B) at that same Z. Over all 42 q=1 measurements the sealed chain
supports:

    measurements                        42
    denominator negative                 0     (no sign reversal anywhere)
    (α<1) equals (A deeper at same Z)   42
    disagreements                        0

**(2) AT Z_open THE DEEPER CHANNEL IS THE ENTRANT BY DEFINITION.** Z_open is
min(first[A], first[B]): the Z at which one of the pair first enters. The entrant is
the argmin over available channels, so the member that enters IS the deeper member.
Measured at every block the chain reaches:

    blocks 11   "A first" == "A deeper at Z_open" at 11/11

**COMPOSED: (α<1) ⟺ (A deeper at Z_open) ⟺ (A first). T-B returns 11 of 11 by
construction, for any α that reduces to the pair comparison at Z_open.** It has no
falsifier available to it. Had it been filed and run, the session would have reported
a confirmation of §5 that contained no information about §5.

## WHY THIS IS ENTERED AS A FAULT AND NOT A NOTE
Because the project's whole method is predict-run-score, and a prediction that cannot
fail corrupts the score it enters. §5 — "the tie-break dies at n+l = 7 and 8 because
those are the first blocks whose competing pair spans d and f" — is the current live
explanatory claim. Confirming it with an identity would have promoted a pattern to a
result on no evidence. This is the same failure mode as Standing 7, one level up:
a control that does not vary, and a test that cannot fail, are the same defect.

## WHAT SURVIVES
§5's claim is untouched and still open. §2 (α = 1 is the critical value of the
tie-break clause and nothing else) is untouched: it rests on `alpha.py sources`,
which is a different measurement. **What is withdrawn is the proposed test, not the
finding it was meant to test.**

## STATUS
OPEN pending M's ruling on a replacement. Two candidate replacements, each with a
live falsifier, are set out in `PROPOSED-T-B-REPLACEMENT.md`. No prediction has been
filed and no run has been made, so R 1449 is intact.
