# PREDICTION S79 — ITEM 2. THE FIVE CLASS-B CHANNELS AT Z=89, RESOLVED.
# FILED BEFORE THE RUN. Nothing below has been executed.
# Written after reading SEALED s77 data only (o89_89_*.jsonl, nodespec77.jsonl, source).

## WHAT THE SEALED DATA ALREADY SETTLES (READ, NOT PREDICTED)
All five failures at Z=89 seed A are RuntimeError NODE-COUNT raises. ZERO TypeErrors.
  6f tgt2 got3 | 7d tgt4 got3 | 7f tgt3 got4 | 8d tgt5 got4 | 8f tgt4 got5
The three f channels return ONE NODE TOO MANY; the two d channels ONE TOO FEW.
win_pts = 3, 5, 4, 3, 2 out of NSCAN=160.

## THE PREDICTIONS
Q1  The node-count boundary at Z=89 moves BETWEEN ADJACENT s77 GRID POINTS for at least
    three of the five, i.e. the s77 scan cannot resolve the edge of its own window.
Q2  For 6f, 7f, 8f, max(log nrm) over {nd==tgt} lies far closer to zero than |minlog|,
    and s77's "the f channels come within e^-6 of a findable zero" is a MISREADING of the
    minimum for the closest approach. PREDICTED TRUE INDEPENDENT OF Q3's OUTCOME.
Q3  **AT REFINED RESOLUTION THE THREE f CHANNELS TURN CLASS C AND THE TWO d CHANNELS
    STAY CLASS B.** Rationale, stated before the run: e_returned lies INSIDE win_e for
    6f, 7f, 8f and OUTSIDE it for 7d, 8d. Where the solver's own zero sits inside the
    target window, the zero and the node boundary are adjacent and a finer grid separates
    them; where it sits outside, they are not adjacent.
Q4  ANY channel that turns CLASS C returns an eigenvalue INSIDE its s77 window, therefore
    still more than 2x the 32.330 mHa margin above rank 2. **THE ENTRANT AT Z=89 DOES NOT
    CHANGE AND NEITHER DOES RANK 1 OR RANK 2.**
Q5  The refined scan raises NO TypeError at Z=89. F78.2's signature is absent from this row.

## THE FALSIFIERS, NAMED
Q3 is falsified if a d channel turns C, or if no f channel does.
Q4 is falsified by any found eigenvalue below -0.15762 + 0.032330 Ha.
If Q3 and Q4 both hold, F76.2's hole at Z=89 closes as FOUND STATES, not brackets.