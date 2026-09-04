# RESULT S79 — ITEM 2. THREE OF THE FIVE HOLES AT Z=89 ARE NOW FOUND STATES.
# F78.2's MECHANISM IS REFUTED AT THIS ROW. F79.1 RAISED: s77 READ ITS OWN FIGURE BACKWARDS.
# Prediction sha256 a2a5e4c8d69ee9045493e92e9a2b9c439ed53f9733d22a6c2251b74017162671, filed first.
# Instrument pack79/refine79.py — FOUR declared lines from sealed pack77/nodespec77.py.

## CAN-FAIL, VERIFIED IN BOTH DIRECTIONS, AND IT GATED
The prediction sha is checked on every invocation; the driver halts without it.
DIRECTION C: control run, tgt := the node count the SEALED solver returned. 6f control
returns CLASS C and bisects a zero at **e = -0.020286239, nd = 3, log(nrm) = 0.0** —
which REPRODUCES the sealed solver's own e_returned = -0.020286, res = 0.0. The instrument
independently recovers a state the sealed runtime found.
DIRECTION B: 7d and 8d return CLASS B on the identical code path in the same run.
**BOTH VERDICTS ARE REACHABLE. The control was run BEFORE the question runs.**

## F78.2 IS REFUTED AT Z=89, ON SEALED DATA, BEFORE ANYTHING NEW WAS RUN
All five seed-A failures at Z=89 (pack77/o89_89_A.jsonl) are **RuntimeError NODE-COUNT
raises. ZERO TypeErrors.** F78.2's signature — `'NoneType' object is not subscriptable`,
a failed bracket EXPANSION — does not occur on this row.
**AND THE REFINED RUN SHOWS WHY, POSITIVELY: res_returned = 0.0, 0.0, 1e-9, 1e-9, 0.0.
The bracket expansion did not fail. IT SUCCEEDED, CONVERGED TO A TRUE ZERO OF log(nrm),
AND THE ZERO BELONGED TO A DIFFERENT STATE.** The three f channels land one node ABOVE
target, the two d channels one node BELOW. **The mechanism is STATE MISIDENTIFICATION,
not search failure.** F78.2 stands as raised at Z=19 under perturbation; it is NOT the
mechanism at Z=89, and the lead is closed here.

## THE MEASUREMENT — NFINE = 3000 vs s77's 160, BOUNDED TO 3x THE SEALED WINDOW
| ch | tgt | s77 | **s79** | win pts | sign chg | s77 minlog | **maxlog** | zero found |
|---|---|---|---|---|---|---|---|---|
| 6f | 2 | B | **C** | 3 -> 353 | 2 | -6.5292 | **+6.4896** | **-0.031600440** |
| 7f | 3 | B | **C** | 4 -> 460 | 2 | -6.0059 | **+7.8502** | **-0.020275522** |
| 8f | 4 | B | **C** | 2 -> 463 | 2 | -5.4466 | **+6.6557** | **-0.014084998** |
| 7d | 4 | B | B | 5 -> 646 | 0 | +0.0897 | +13.0029 | none |
| 8d | 5 | B | B | 3 -> 551 | 0 | +0.0401 | +12.1266 | none |
Every found zero carries its TARGET node count and log(nrm) = 0 to 1e-11.

## F79.1 RAISED AND CLOSED — s77 QUOTED THE WRONG END OF ITS OWN RANGE, BOTH TIMES
`minlog` is `min(log nrm)` over the window. Where log(nrm) is NEGATIVE throughout, the
minimum is the point FARTHEST FROM ZERO, not the nearest; the nearest is the MAXIMUM,
**which the sealed instrument never recorded.** s77 wrote that the f channels "come within
e^-6 of a findable zero" from minlog -6.53/-6.01/-5.45. **In the refined window log(nrm)
runs from about -7 to +7.9 and CROSSES. The quoted figure was the far end.**
**AND THE d CHANNELS ARE THE INVERSE.** There log(nrm) is POSITIVE throughout, so minlog
+0.0897 and +0.0401 ARE the closest approach — 0.04 of a zero — while s77 called the d
failures "not marginal". **Both readings were inverted. The verdict f-near-C survives; the
evidence cited for it did not support it.** Repaired by D2: maxlog is now recorded.
**THIS IS F78.1's STANDING POINT IN A SECOND COSTUME — read the instrument, not the label
on its output column.**

## WHAT THE FOUND STATES SAY ABOUT THE ROW — THE ORDERING IS UNTOUCHED AND BETTER SUPPORTED
Sealed: 6d **-0.15762** (rank 1), 7p **-0.12529** (rank 2), m(89) = **32.330 mHa**.
| found | above 6d | above 7p |
|---|---|---|
| 6f -0.031600 | **126.020 mHa = 3.898 m** | **93.690 mHa = 2.898 m** |
| 7f -0.020276 | 137.344 mHa = 4.248 m | 105.014 mHa = 3.248 m |
| 8f -0.014085 | 143.535 mHa = 4.440 m | 111.205 mHa = 3.440 m |
**THE ENTRANT AT Z=89 IS UNCHANGED AND NEITHER RANK 1 NOR RANK 2 IS TOUCHED.**
**AND THE REPORTED ZEROS ARE THE MOST BOUND CANDIDATES.** sign_changes = 2 for all three
f channels: there are TWO energies with target node count and nrm = 1, and the instrument
bisects the FIRST, which is the more bound. **The conclusion is therefore robust to that
choice — even the most bound candidate sits 2.9 margins above rank 2.**

## THREE THINGS RECORDED AGAINST THIS RESULT, NOT BURIED
1. **sign_changes = 2 IS NOT EXPLAINED.** Two zeros at one node count is a fact about
   nrm = 1 under an exchange source, not a two-fold spectrum. Undiagnosed.
2. **6f AT -0.031600 IS 0.140 mHa MORE BOUND THAN SEALED 5f AT -0.03146.** Within one
   fixed field min-max forbids that ordering (6f has 2 nodes, 5f has 1). These are two
   DIFFERENT SCF fields, so no theorem is violated — but the figure is small, it is
   adjacent to the tie-break question, and it is flagged, not smoothed.
3. **8f's zero at -0.014085 LIES OUTSIDE its s77 bracket [-0.017556, -0.015501]**, 1.416
   mHa on the less-bound side. The s77 window was a grid artefact; the bracket did not
   contain the state it was a bracket for. It moves 8f FURTHER from rank 2, not nearer.

## PREDICTION SCORED — Q1 Q2 Q3 Q5 CORRECT, Q4 SPLIT
  Q1 s77 grid cannot resolve its own window edge . . **CORRECT** — every refined window is
     wider on both sides; win_pts 3,4,2,5,3 -> 353,460,463,646,551.
  Q2 maxlog is the right proximity figure; s77 misread . **CORRECT.**
  Q3 **the three f turn C, the two d stay B** . . . . **CORRECT, BOTH HALVES, AND ON THE
     RATIONALE FILED** — e_returned inside win_e for f, outside for d.
  Q4 found states inside their s77 windows; entrant unchanged . **SPLIT. The verdict is
     CORRECT — entrant, rank 1 and rank 2 all unchanged. The containment clause is WRONG:
     8f fell outside. Recorded as wrong.**
  Q5 no TypeError . . . . . . . . . . . . . . . . . . **CORRECT** — none, in any run.

## WHAT THIS CLOSES
**F76.2's Z=89 hole is now THREE FOUND STATES AND TWO BRACKETS, where s77 had five
brackets.** M's item 2 asked for a measured argument converted into a found state. Three of
five are converted. **F78.2 is closed at this row as REFUTED, with its mechanism replaced.**

## WHAT THIS DOES NOT CLOSE, AND IT IS THE IMPORTANT ONE
**THESE ARE THREE DIFFERENT FIELDS, NOT ONE.** Each f value is the SCF converged with that
f channel occupied. **CLOSE-S78 §3 states the residual clause-1 claim at ONE FIXED FIELD:
eps_3^{l=3}(F[Phi_d*]) > eps_4^{l=2}(F[Phi_d*]).** Nothing here is that object.
**BUT THE OBSTACLE TO COMPUTING IT HAS JUST BEEN REMOVED.** s77 could not reach the f
channels at Z=89 at all; the refined scan reaches them. **The fixed-field comparison —
freeze the field at the converged 6d solution and locate the l=3 zero in it — is now a
REACHABLE COMPUTATION, and it is the exact object clause 1 is about.**