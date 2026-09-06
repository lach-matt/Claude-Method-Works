# F81.2 AND F81.3 — TWO FAULTS IN perturb81.py, RAISED AGAINST MY OWN INSTRUMENT IN THE
# SESSION THAT WROTE IT, BOTH CAUGHT BY THE INSTRUMENT'S OWN GATES, BOTH BEFORE ANY
# QUESTION ROW WAS SCORED.

## F81.2 — THE MEASURED TOLERANCE WAS A THOUSAND TIMES TOO SMALL. THE UNITS.
**WHAT WAS WRITTEN.** `tol = abs(ladder[0] - ladder[-1]) * 1e-3`, with the `1e-3`
intended as a mHa→Ha conversion. **The ladder is stored in Ha, so its difference is
ALREADY in Ha.** TOL came out at 2.2e−8 Ha instead of 2.2e−5 Ha.
**HOW IT SURFACED.** The C1 can-fail printed `dE=1.9e-05 mHa (TOL=2.2e-05)` — a
tolerance three orders of magnitude below the floor J1 had just been built to measure,
printed next to the floor it was supposed to equal. **C1 PASSED ANYWAY, BY LUCK**: the
zero-perturbation residual happened to sit just under the wrong tolerance. **A control
that passes for the wrong reason is not a control**, and the pass was not accepted.
**SEVERITY.** J1 exists to close F80.3, which was a tolerance set below the resolution it
claimed. **This fault would have reinstated F80.3 inside its own repair**, at a thousand
times the severity, and it would have labelled every 7p run a second basin.
**REPAIRED**, declared in the source at the assignment, and both can-fails re-run against
the corrected code before any question row was computed.
**THIS IS F79.2's SPECIES — READ THE UNITS — IN CODE WRITTEN THIS SESSION, ONE FILE AFTER
A SESSION THAT RECORDED THAT LESSON AS STANDING.**

## F81.3 — THE LEVER WAS READ OFF THE WRONG OBJECT. THE LEVER CHECK CAUGHT IT.
**WHAT WAS WRITTEN.** `dp = p.DP`, read AFTER `p, E, ladder2 = stationarise(p, cfg, E)`
had rebound `p` to the last restart instance — which runs at AMP = 0 by construction.
Every perturbed run therefore reported **dP = 0.0** no matter how large the perturbation.
**HOW IT SURFACED.** J3, the standing F54.2 law: *an instrument that varies a parameter
must demonstrate the parameter moves the object, every run.* The first grid invocation
printed **`LEVER DEAD: amp=0.02 produced dP=0.0. NOTHING COMPUTED.`** and exited rc=4.
**THE LAW FIRED ON A LIVE LEVER AND A DEAD READING, AND STOPPED THE RUN EITHER WAY.**
**SEVERITY, AND IT IS THE INTERESTING PART.** The perturbation itself was working — the
six-run grid later returned dP = 0.020 to 0.557, all correct. **The fault was in the
INSTRUMENT'S ABILITY TO SEE ITS OWN LEVER, not in the lever.** Had J3 not been mandatory
every run, this would have produced a full grid of correct results carrying a column of
zeros, and that column is the one the F54.2 law exists to make trustworthy.
**REPAIRED**: the reading is taken from the perturbed object immediately after its own
run2, before J2 replaces it. Declared in the source.

## WHAT THE TWO OF THEM TOGETHER SAY
1. **BOTH WERE CAUGHT BY GATES, NOT BY READING THE CODE.** F81.2 by a can-fail printout,
   F81.3 by the lever law halting the run. Neither was found by review, and I reviewed.
2. **THE GATES COST THREE RE-RUNS OF THE CAN-FAILS, ABOUT FOUR MINUTES**, and they
   returned a grid whose every column can be defended.
3. **THE STANDING ORDER'S THIRD LINE IS NOW EARNED TWICE OVER IN ONE SESSION:** read the
   units; read whether the instrument can see what it claims to have seen.
4. **TIMING FLAG, DECLARED.** Both repairs followed numerical output. Neither followed a
   SCORED result: no question row existed when either was made, the prediction file was
   not touched, and its sha gate held across both amendments.
