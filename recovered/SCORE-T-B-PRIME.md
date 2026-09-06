# SCORE — T-B′. BOTH CANDIDATES, ON M'S RULING TO RUN BOTH.
# SESSION 65. Prediction pack65/PREDICTION-T-B-PRIME.md
# sha 39bbebfcd6681b1c104fe338425651ae466704cc6071610933df81c673607990,
# filed 2026-08-20T22:04:38Z before pack65/ablocks.py existed. Verified at every
# invocation by the scorer, which halts without it (can-fail direction [5]).
# Instrument pack65/ablocks.py. Log pack65/SCORE-T-B-PRIME.log. No solves.

## THE HEADLINE

    CANDIDATE B (transfer)      7 of 11 agree.  EXACTLY AS PREDICTED, INCLUDING THE
                                FOUR NAMED FAILURES AND NO OTHERS.
    CANDIDATE A (shifted base)  NO-DATA at 11 of 11. UNEXECUTABLE, NOT A PASS.

**§5 OF FINDING-ALPHA IS NOT CONFIRMED. Under the interpretation fixed in advance,
α is NOT a function of the l-pair alone and §5 must be refined or withdrawn.**

## CANDIDATE B — THE ROWS

    blk  A vs B      l-pair  Zopen  A first?   α transferred   agree?
     3   3p vs 4s     s->p     13     True        0.5276        YES
     4   4p vs 5s     s->p     31     True        0.5276        YES
     4   3d vs 4p     p->d     21     True        1.0688      **NO**
     5   5p vs 6s     s->p     49     True        0.5276        YES
     5   4d vs 5p     p->d     39     True        1.0688      **NO**
     6   6p vs 7s     s->p     81     True        0.5276        YES
     6   5d vs 6p     p->d     57     True        1.0688      **NO**
     6   4f vs 5d     d->f     57    False        1.5017        YES
     7   7p vs 8s     s->p    113     True        0.5276        YES
     7   6d vs 7p     p->d     89     True        1.0688      **NO**
     7   5f vs 6d     d->f     89    False        1.5017        YES

Predicted 7/11. Measured 7/11. Predicted failures: blocks 4, 5, 6, 7 at p↔d, named
individually in the prediction as 3d/4p at 21, 4d/5p at 39, 5d/6p at 57, 6d/7p at 89.
**Those are the four that failed and the only four.** Every s→p block passed and both
d↔f blocks passed, as predicted.

## CANDIDATE A — WHY IT RETURNED NOTHING, AND IT IS NOT A PHYSICS RESULT
α_shift needs (n+1,l), (n+1,l+1) and (n+2,l) in the walk's candidate list at Z_open.
The list is short — at Z=21 it is 3d, 4p, 5s, 5p, 4f, 5f, 5g — and the shifted triple
is never complete. The prediction allowed for "at least 2" NO-DATA; the truth is 11.
**Candidate A is starved by the candidate list, not by the field**, and supplying it
would take fresh solves at eleven atoms including Z = 81, 89, 113. That is outside the
declared budget (§2.20: no solves) and is not done here. A is reported as
UNEXECUTABLE ON SEALED DATA and is not scored, not passed, and not used as evidence
against §5. The A-vs-B comparison the prediction set up therefore did not run.

## THE DRIVER WENT RED BEFORE IT WAS BELIEVED

    [0] unmodified                                   -> A 0/0   B 7/11
    [1] block 6 4f/5d observed order flipped         -> B 6/11
    [2] every observed order flipped                 -> B 4/11
    [3] s->p blocks relabelled d->f                  -> B 2/11
    [4] Z_open of block 6 moved to a wrong atom      -> B 7/11 (insensitive, declared)
    [5] prediction sha tampered                      -> HALT, nothing scored
    [6] every block's l-pair driven out of range     -> RAISED KeyError, i.e. red

Direction [4] is declared as a NON-discriminating direction: Candidate B's predictor
does not read Z_open at all, so moving Z_open cannot move B's α. It moves only which
Z is excluded from the pool. **That is a property of the test, stated rather than
hidden.** Direction [6] crashed rather than reporting; a crash is red, and the driver
was NOT edited after the can-fail to make it graceful (rule 4 in spirit).

## THE DIAGNOSTIC — WHAT THE FOUR FAILURES HAVE IN COMMON
Filed as DIAGNOSTIC, NOT AS A TEST. Nothing below is scored against anything.

The p→d ratio is not scattered and does not depend on n. Grouped by base shell:

    base 3p  7 measurements  median 1.0755    base 6p  3   median 1.0580
    base 4p  4               median 1.0837    base 7p  1   median 1.0493
    base 5p  4               median 1.0584

It is the same number everywhere it can be measured — and it is measured only while
the base p shell is still open. **At Z_open the base p shell has just closed.** So
the head-to-head gap was looked at directly, D(A) − D(B) in mHa, across Z:

    3d vs 4p    Z=19 +35.56   Z=20 +30.90   **Z=21 −97.63**   Z=22 −131.26
    4f vs 5d    Z=56 +86.82   Z=57 +100.29  **Z=58 −121.15**  Z=59 −147.99
    5f vs 6d    Z=89 +126.16  Z=90 +54.05   **Z=91 −81.95**   Z=92 −126.38

**THE SIGN DOES NOT DRIFT ACROSS 1. IT JUMPS** — 129 mHa in one unit of Z at the
3d crossing, 221 mHa at 4f, 136 mHa at 5f. That is the collapse of the higher-l
channel, already a deliverable of this project (DELIVERABLE-3-COLLAPSE-CONDITION).
The transfer failed because the pool is measured entirely on the far side of a
discontinuity that lands between the last measurable atom and Z_open.

**AND THE TIMING IS THE WHOLE STORY:**

    3d/4p   collapse lands AT the block opening (20→21)        tie-break HOLDS
    4f/5d   collapse lands ONE atom LATE (57→58)               tie-break FAILS at La
    5f/6d   collapse lands TWO atoms LATE (90→91)              tie-break FAILS at Ac

**Madelung's tie-break is the assertion that the (n,l+1) channel has collapsed by the
Z at which its block opens. It is true through p↔d and it is late by one atom at 4f
and two at 5f.** That is a sharper statement than §5's "it is about which l values
collide", it is measured, and it explains why the exceptions are exactly La and Ac.

## WHAT IS CIRCULAR HERE AND MUST NOT BE SOLD AS CONTENT
"Collapsed by Z_open" ⟺ "A deeper at Z_open" ⟺ "A enters first" — the same identity
F65.1 registered. **The equivalence is definitional and is not the result.** What is
NOT definitional, and is what the diagnostic adds: (i) the crossing is a
discontinuity of 130–220 mHa in one unit of Z, not a drift through the critical
value; (ii) the miss at n+l = 7 and 8 is one atom and two atoms, which is a
quantity; (iii) it points at an independently-derived quantity — the collapse
condition — as the predictor.

## THE NON-CIRCULAR TEST THIS OPENS, PROPOSED AND NOT RUN
**T-C.** Predict Z_collapse for each block's (n,l+1) channel from the sealed collapse
condition ALONE (PREDICTION-COLLAPSE-KAPPA / DELIVERABLE-3), with no reference to
D(A) − D(B) at any Z, and compare it to Z_open. Agreement would make the tie-break a
COROLLARY of the collapse condition rather than a separate empirical clause — and
that is a derivation, not a demonstration. Disagreement kills the route cleanly.
**Prediction to be filed before any run. Not started this session.**

## LEDGER CONSEQUENCE
None. No margin, entrant, ordering, rung or bound is touched. What changes is exactly
one paragraph of one finding document, as the prediction said it would.
