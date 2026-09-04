# PREDICTION — T-B′. THE REPLACEMENT FOR THE VOID TEST T-B.
# FILED SESSION 65, 2026-08-20T22:04:38Z, BEFORE `pack65/ablocks.py` EXISTED AND
# BEFORE ANY BLOCK VALUE WAS COMPUTED UNDER EITHER DEFINITION. R 1449 / §2.13.
# M's ruling this session: RUN BOTH CANDIDATES. Scored only after this file's sha
# is verified against pack65/PREDICTION-T-B-PRIME.sha256.
# Instrument to be written: pack65/ablocks.py. `alpha.py` is sealed and is not edited.

## WHAT IS BEING TESTED, AND WHAT IS NOT
The claim under test is **FINDING-ALPHA §5**: that α is a property of *which l values
collide*, ≈0.5 at s→p and ≈1.1–1.5 once d and f are involved, and that the tie-break
therefore holds at n+l ≤ 6 and dies at 7 and 8 because those are the first blocks
whose competing pair spans d and f.

NOT under test: §2 (α = 1 is the critical value of the tie-break clause and nothing
else). That rests on `alpha.py sources` and is untouched by this file either way.

F65.1 governs the design: no predictor may contain the outcome it predicts. Both
candidates below are displaced from the A-vs-B comparison at Z_open — A in the base
it is measured from, B in the Z it is measured at.

## THE ELEVEN BLOCKS, AND THE OBSERVED ORDER THEY ARE SCORED AGAINST
Fixed by the sealed chain, already in hand from `pack65/circ2.py`, and NOT a
prediction — it is the target:

    blk  A(lower n)  B     Z_open   l-pair of the deciding step   A first?
     3      3p      4s       13            s->p                    True
     4      4p      5s       31            s->p                    True
     4      3d      4p       21            p->d                    True
     5      5p      6s       49            s->p                    True
     5      4d      5p       39            p->d                    True
     6      6p      7s       81            s->p                    True
     6      5d      6p       57            p->d                    True
     6      4f      5d       57            d->f                    False
     7      7p      8s      113            s->p                    True
     7      6d      7p       89            p->d                    True
     7      5f      6d       89            d->f                    False

Four blocks span p↔d, not three. **The count in
`pack65/PROPOSED-T-B-REPLACEMENT.md` (three, and 8/11) is corrected here to four and
7/11 BEFORE the run.** The corrected figure is what is scored.

## CANDIDATE B — TRANSFER. THE PREDICTION IS SHARP AND IT IS NOT 11/11.
Predictor: the median α over all sealed q=1 measurements of the same l→l+1 step,
measured at atoms where all three channels are available, EXCLUDING any measurement
taken at that block's own Z_open. Medians already in hand (`pack65/avail.py`):
s→p 0.528 (n=6), p→d 1.069 (n=19), d→f 1.502 (n=17).

    B PREDICTS: α<1 → A first. So A first at every s→p block; B first at every p→d
    and every d→f block.

    PREDICTED SCORE  **7 of 11 AGREE, 4 DISAGREE.**
    PREDICTED FAILURES, NAMED IN ADVANCE: the four p↔d blocks — 3d/4p at Z=21,
    4d/5p at Z=39, 5d/6p at Z=57, 6d/7p at Z=89. In all four the field puts the
    lower-n d channel first (α<1 required) against a transferred median of 1.069.
    PREDICTED PASSES: four s→p blocks and both d↔f blocks.

INTERPRETATION FIXED IN ADVANCE, so it cannot be chosen after the fact:
  * **7/11 with exactly the four named p↔d blocks failing → α IS NOT A FUNCTION OF
    THE l-PAIR ALONE.** §5 is not confirmed and not simply false: the l-pair sets the
    sign correctly at s→p and d→f and gets it wrong at p→d, so something else — n, or
    the state of the core at Z_open — moves α across the critical value. §5 must then
    be REFINED to name that dependence or WITHDRAWN. It may not be left as written.
  * **11/11 → §5 stands as written and the transfer is exact.** This would be a
    genuine result and is NOT what is predicted.
  * **Failures other than the four named, or fewer than four → the prediction is
    wrong in its detail and the pattern is not the l-pair at all.** Report first.
  * Any block returning NO-DATA is NOT a pass and is counted separately.

## CANDIDATE A — SHIFTED BASE. SAME ATOM, ONE SHELL OUT.
    α_shift = [D(n+1,l+1) − D(n+1,l)] / [D(n+2,l) − D(n+1,l)]   at Z_open
Same l→l+1 step as the block itself, so §5's logic predicts the SAME per-block
outcome as Candidate B.

    PREDICTED SCORE  **7 of 11, failing at the same four p↔d blocks.**
    PREDICTED: at least 2 blocks return NO-DATA where (n+2,l) or (n+1,l+1) is absent
    from the order list at Z_open. NO-DATA is not a pass and is reported separately;
    if a NO-DATA block is one of the four named failures, the A score is reported over
    the blocks it actually covers and is NOT compared to B's 11.
    FALSIFIER OF THE SIGN CHECK: any block where α_shift and α_transfer of the same
    l-pair fall on OPPOSITE sides of 1.

**THE COMPARISON IS THE POINT, AND ITS READING IS FIXED HERE:**
  * A and B agree block by block → α depends on the l-pair and on nothing this
    project can currently vary. The evaluation point is irrelevant.
  * **A returns 11/11 where B returns 7/11 → α IS STRONGLY DEPENDENT ON THE
    EVALUATION POINT.** The l-pair sets the shape, the atom sets the value, and §5's
    explanation is incomplete in a way this test would have localised: the four p↔d
    blocks would then be telling us that at Z_open, with the base shell just closed,
    the d channel is cheaper than the same l-step measured anywhere else.
  * A returns worse than B → the shifted base is measuring block N+2 and not block N
    (the weakness declared in the proposal), and Candidate A is withdrawn as a
    predictor, not treated as evidence against §5.

## WHAT NEITHER CANDIDATE CAN DO
Neither is a derivation. Both are tests of whether a proposed *explanation* has
predictive content across atoms. A pass would not derive Δδ; a failure would not
touch the sealed chain, any margin, any entrant, or the ordering clause. **The
Löwdin deliverable is unaffected by the outcome of this file in either direction.**
What is at stake is exactly one paragraph: FINDING-ALPHA §5.

## BUDGET, DECLARED (§2.20)
No solves. Sealed `rt/nlchain.jsonl` only. Whole task < 60 s wall. If it exceeds
that, something is wrong with the driver and the run reports OVERRUN, not a result.
The driver is can-failed in both directions before any real score is read.
