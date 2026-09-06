# RESULT S77b — THE FIVE FAILED CHANNELS AT Z=89 ARE ALL BRACKETED, AND NONE REACHES 6d.
# Prediction sha256 e74a7e248b8906e5ce48ad61efa6a4c201a2a1e3b253d709c72acf7cde11da0e, filed first.
# Instrument pack77/nodespec77.py — FOUR declared lines from sealed rt/nodespec.py; scan
# geometry untouched. CAN-FAIL PASSED: 5f and 5g, both converged in the walk, return
# NO-RAISE through the widened l=3 path. The instrument can return both verdicts.

## CHECKING PREVIOUS WORK PAID: TWO OF THE FIVE WERE ALREADY ANSWERED AT s66 AND UNREAD
pack66/nodespec.jsonl already carried Z=89 7d and 8d, CLASS B, with windows. s66 scoped
itself to `l != 2: continue`, **so no f channel had ever been scanned, at any Z.** That is
a scope limit of s66, declared in its own source — not a fault.

## THE MEASUREMENT
| ch | tgt nodes | class | window Ha | vs winner |
|---|---|---|---|---|
| 7d | 4 | B | **[-0.053839, -0.032719]** | 103.8 mHa above 6d |
| 6f | 2 | B | **[-0.037058, -0.019884]** | 120.6 mHa above 6d |
| 8d | 5 | B | **[-0.028889, -0.022521]** | 128.7 mHa above 6d |
| 7f | 3 | B | **[-0.028889, -0.013686]** | 128.7 mHa above 6d |
| 8f | 4 | B | **[-0.017556, -0.015501]** | 140.1 mHa above 6d |
Sealed: 6d **-0.15762**, 7p **-0.12529**, 5f -0.03146.
**ALL FIVE ARE CLASS B — the target node count IS attained in the field. The state exists;
the SCF shooting does not find it. A node-count failure at Z=89 is a failure to FIND, and
that is now measured rather than assumed.**
**THE MOST BOUND EDGE OF THE MOST BOUND MISSING CHANNEL IS 7d AT -0.053839 Ha. That is
71.45 mHa ABOVE THE RUNNER-UP and 103.78 mHa ABOVE THE WINNER — 2.2 and 3.2 times the
32.330 mHa argmin margin.** Neither rank 1 nor rank 2 at Z=89 is reachable by any of them.

## PREDICTION SCORED — 3 CORRECT, 1 WRONG, 1 EXECUTED LATE
  N1 can-fail: l=3 must not raise on a converged channel . **CORRECT — BUT NOT RUN BY THE
     DRIVER.** `cells()` iterates the sealed `fail` map, so 5f was never offered to it.
     **I ran it separately afterwards. The can-fail passed, and it should have gated the
     scan rather than following it. Recorded as a sequencing error, mine.**
  N2 all CLASS B or C . . . . . . . . . . . . . . . . . **CORRECT** — five of five, B
  N3 every window above -0.0400 Ha . . . . . . . . . . . **WRONG** — 7d reaches -0.053839
  N4 none changes the entrant; ranking only . . . . . . **CORRECT**; and 7d's window
     straddles 8p (-0.04917), 8d's sits below 5f, as predicted

## AN OBSERVATION, NOT A CONCLUSION
The three f channels return **minlog -6.53, -6.01, -5.45**; the two d channels **+0.09,
+0.04**. CLASS B means log(nrm) has no zero in the window; the f channels come within
e^-6 of having one. **The f failures are numerically marginal — near-CLASS-C — and the d
failures are not.** That is a lead for whoever builds Rung B, since a near-zero is exactly
where an eigenindex selector would bite. It is not evidence about the ordering.

## WHAT THIS CLOSES AND WHAT IT DOES NOT
**CLOSED: the sealed Z=89 row no longer has a silent hole.** Every one of the fourteen
admissible channels is now either converged or bracketed, and the bracket for all five
non-converged channels excludes the top two ranks by more than twice the margin.
**NOT CLOSED, AND THE DISTINCTION MATTERS:** a node-spectrum window is a ONE-ELECTRON
bracket in a field, not a converged total energy and not a lower bound on E^RHF at that
occupancy. **Proving 6f lies above 6d needs a LOWER bound, and the variational principle
supplies only upper bounds. This is a strong measured argument and it is not a proof.**
The proof is Rung C's, and Rung C is open here and open in the literature.