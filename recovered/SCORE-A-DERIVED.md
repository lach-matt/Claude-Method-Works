# SCORE — CANDIDATE A, ON DERIVED CHANNELS. M'S RULING: A IS EXECUTABLE.
# SESSION 65. Same prediction, pack65/PREDICTION-T-B-PRIME.md, sha 39bbebfc…,
# filed 22:04:38Z. No new prediction is filed and none is owed: the filed one already
# says A predicts 7/11 failing at the same four p↔d blocks.
# Instrument pack65/aderive.py. Cache pack65/aderive.jsonl. `nlchain.py` not edited.

## THE RULING WAS RIGHT AND THE EARLIER REPORT WAS WRONG
s65 first reported Candidate A as "unexecutable on sealed data". **That was a
statement about the walk's candidate list, not about the field**, and M rejected it.
The channels A needs are one solve each: D(ch) = E(cfg(Z−1)+ch) − E(cfg(Z−1)) at
nuclear charge Z, which is `nlchain.step`'s own definition. Five were run.

## EVERY DERIVED Z CARRIES A DETERMINISM CHECK, AND ALL FIVE MATCHED
One channel already sealed at that Z was recomputed under the new driver first:

    Z=13  4s  −0.09711  sealed −0.09711  MATCH
    Z=21  4p  −0.16901  sealed −0.16901  MATCH
    Z=31  5s  −0.09995  sealed −0.09995  MATCH
    Z=39  5p  −0.15194  sealed −0.15194  MATCH
    Z=49  6s  −0.09373  sealed −0.09373  MATCH

The derived channels are therefore commensurable with the chain. Seventh session in
which a determinism receipt has been produced.

## WHAT WAS DERIVED

    Z=13  5s  −0.04616      Z=31  6s  −0.04707      Z=49  7s  −0.04496

## CANDIDATE A — THE THREE COMPLETED BLOCKS

    blk  A vs B    Zopen  base   α_shift   α<1   A first?  agree   α_transfer
     3   3p vs 4s    13    4s    0.6196   True    True      YES      0.5276
     4   4p vs 5s    31    5s    0.6471   True    True      YES      0.5276
     5   5p vs 6s    49    6s    0.6322   True    True      YES      0.5276

**3 of 3 agree. A and B fall on the SAME side of 1 at every block where both run.**
α_shift is systematically higher than α_transfer (0.62–0.65 against 0.53) — the
evaluation point moves the VALUE by about 0.1 — but not across the critical value.

## THE FOUR BLOCKS THAT WOULD HAVE DISCRIMINATED RETURN NO-DATA, AND THE REASON IS
## NOT THE HARNESS

    Z=21  4d  RuntimeError: Z=21 42 nodes 0
    Z=39  5d  RuntimeError: Z=39 52 nodes 1

**These are reproduced VERBATIM from the sealed chain's own `fail` dictionary** —
`rows[21]['fail']['4d']` and `rows[39]['fail']['5d']` carry the identical strings.
An eighth determinism receipt, this one on the failure side.

The channel the p↔d blocks need is the one the guard cannot label. The solve for
(n=4,ℓ=2) at Z=21 returns a state with **0 nodes where the label requires 1**; at
Z=39, (n=5,ℓ=2) returns **1 node where the label requires 2**. In both cases the
search lands one state below the one asked for. The same failure sits at Z=31 and
Z=49 for 4d/5d and at Z=49 for 6d.

**READ CONSERVATIVELY, WHICH IS THE ONLY WAY IT MAY BE READ HERE:** the excited d
channel is not resolvable by this instrument at these atoms. That is consistent with
the lower d state having collapsed into the inner well and the shooting solve falling
into it, and that reading is CONSISTENT WITH but NOT ESTABLISHED BY what is measured.
No mechanism is claimed. What is established is that the NO-DATA is a property of the
sealed field's own solve, not of the candidate list, and that the earlier "starved by
the harness" line is withdrawn for these two blocks.

## SCORE AS IT STANDS

    CANDIDATE A   3 of 3 agree on completed blocks.
                  4 blocks NO-DATA from the field (p↔d, node-count fail).
                  4 blocks NOT RUN (Z = 57, 81, 89, 113 — heavy, see the bridge).
    Predicted 7/11 with the four p↔d blocks failing. **The four predicted failures
    cannot be evaluated on this definition.** A is therefore NOT scored against 11 and
    is not compared to B's 7/11. Standing 8 in spirit: the comparison did not hold its
    reference fixed, so it is not made.

## WHAT THIS SETTLES AND WHAT IT DOES NOT
SETTLED: α is not wildly sensitive to the evaluation point where both definitions can
be measured — 0.1 of movement, no sign change, at three blocks.
NOT SETTLED, AND IT IS THE WHOLE QUESTION: whether α crosses 1 at the p↔d openings.
The definition that would answer it is blocked by a node-count failure at exactly
those atoms. **A different definition, or a different solve, is required — and that
is a real result about the instrument, reached by running M's ruling rather than by
declining it.**
