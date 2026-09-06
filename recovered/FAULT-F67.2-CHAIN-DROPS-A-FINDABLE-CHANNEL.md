# F67.2 — THE SEALED CHAIN DROPS A FINDABLE d CHANNEL AT Z=51.
# Raised 2026-08-20, SESSION 67, at SEG B of T-E, the moment the cell returned and
# BEFORE any other clause of the prediction was scored — as `PREDICTION-T-E.md`
# (sha 218396913cf53cf5…, filed 23:28:43Z) requires in terms:
#   "Any CLASS C ... is reported FIRST, before any other clause, as a fault against
#    the chain."
# No sealed file is edited. The measurement is the s67 driver's, whose only difference
# from the sealed pack66 parent is three path constants (diff proved, 3 lines).

## THE MEASUREMENT
    Z=51  5d   tgt=2   CLASS C   nd_max=15   win_pts=5   minlog = -0.2904   6 s
    returned by the sealed chain : nd = 1 at e = -0.062527
    the tgt=2 window             : e in [-0.059756, -0.037346], five grid points
    sign changes of log(nrm) in that window : 2
    node spectrum nd(e) attains  : 0,1,2,3,...,15 — every value up to 15

**log(nrm) GOES NEGATIVE INSIDE THE NODE-CORRECT WINDOW.** The two-node 5d state that
the label (n=5, l=2) demands is present in the self-consistent field, it is
normalisable, and it is findable — a root sits between -0.0598 and -0.0373 Ha. The
sealed chain returned the one-node state at -0.0625 instead, which lies BELOW the
window: the bracket walked down and out, exactly the mechanism s42 described at Z=21
and exactly reading (2) of the s65 bridge.

## WHY THIS IS A FAULT AND NOT A RESULT
s66's T-D measured ten cells and found CLASS C at none, concluding that reading (2)
"occurs at no cell" and was "refuted across a hundred protons." **That conclusion was
drawn from ten cells out of a sealed population of 162 d-channel node-count failures.**
The eleventh cell measured, at the first atom outside s66's set on the pre-collapse
side, is CLASS C. s66's PD-4 is not overturned as scored — it was scored over its own
ten cells and holds there — but the generalisation beyond those ten does not survive.

**The chain is therefore dropping at least one channel it could have found.** Whether
it drops others is not known: 133 of the 162 d failures remain unmeasured, and every
f and g failure is untouched.

## LEDGER CONSEQUENCE — NOT ASSESSED, AND DELIBERATELY NOT GUESSED
The sealed row at Z=51:

    ent 5p  D_ent -0.27973   margin 0.17235 over 6s at -0.10738
    order  5p -0.27973 | 6s -0.10738 | 6p -0.07264 | 4f -0.03129 | 5f -0.02003
           5g -0.02000 | 6f -0.01391 | 6g -0.01389 | 6d +0.00215
    fail   {'5d': 'RuntimeError: Z=51 52 nodes 1'}      nfail 1      ok True

For the recovered 5d to disturb the ordering it would need D < -0.27973. **That cannot
be read off the eigenvalue.** D is a total-energy difference and the window above is an
eigenvalue window; the two are different quantities and this project does not convert
one into the other by assumption. What can be stated: the eigenvalue window
[-0.0598, -0.0373] sits far shallower than the winner's D, and the converged 6d channel
at this atom has D = +0.00215. **A displacement of 5p by 5d would be surprising. It is
not measured, and "surprising" is not a score.**

**Settling it requires one solve that no filed prediction covers**: converge Z=51 with
(5,2) added, with the bracket confined to the measured window, and read D. That is one
cell, of order the cost already spent here. It is NOT run in this session and is NOT
proposed as this session's own remedy — it is entered for M's ruling.

## WHAT IS AND IS NOT WITHDRAWN
NOT WITHDRAWN: Deliverable 1, the ordering clause, any margin, entrant, rung or bound.
Z=51 remains ok=True in the sealed chain and this fault does not by itself change that.
NOT WITHDRAWN: s66's T-D score, which stands over its own ten cells.
**WITHDRAWN: the generalisation that reading (2) is dead.** It is alive at Z=51 5d.
**RAISED: the sealed chain's `fail` set is not provably a set of unfindable channels.**
Until the 162 are measured, "node-count failure" means "this solver did not find it",
not "the field does not carry it there findably".

## STATUS
OPEN, pending M's ruling on (a) the one confirming solve at Z=51 5d, and (b) whether
the remaining 133 d-channel failures are swept for further CLASS C.
