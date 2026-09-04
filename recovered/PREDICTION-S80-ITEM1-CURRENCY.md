# PREDICTION — SESSION 80, ITEM 1.  F79.2's CURRENCY REPAIR.
# FILED BEFORE ANY RUN OF de80.py.  R 1449.  The driver halts on a sha mismatch.
# THE OBJECT: dE = E(cfg88 + ch) - E(ref), E(ref) = -25694.38401018016, ch in {6f,7f,8f}.
# WHAT IS ALREADY KNOWN AND IS NOT PREDICTED HERE:
#   the three eigenvalues, from sealed pack79/refine79.jsonl —
#     eps(6f) = -0.031600440   eps(7f) = -0.020275522   eps(8f) = -0.014084998
#   the sealed dE comparands, from pack77/o89_89_A.jsonl —
#     6d dE = -0.157621 (rank 1)   7p dE = -0.125290 (rank 2)   m(89) = 32.330 mHa
#   the measured currency offset at 6d — dE - eps = -0.157621 - (-0.176898) = +19.277 mHa
# NOTHING BELOW HAS BEEN RUN.  The instrument has never been executed.

## X1 · THE FALLBACK CONVERGES AT LEAST ONE f CHANNEL TO A TOTAL ENERGY.
refine79 found TRUE zeros — target node count, log(nrm) = 0 to 1e-11, res 0.0 — so the
state exists in the iteration-1 field.  I predict it persists under the SCF's own damping
and that the run reaches `conv=True`.  **I predict ALL THREE converge.**
FALSIFIED IF: any channel returns conv=False, or the fallback raises "FOUND NO
TARGET-NODE ZERO".

## X2 · THE ENTRANT AT Z=89 IS UNCHANGED.  ALL THREE dE LIE ABOVE 6d's -0.157621.
Rationale, filed: the eigenvalue margins above 6d were 126.0 / 137.3 / 143.5 mHa.  The
ONLY measured currency offset is +19.277 mHa at 6d.  For an f channel to overtake 6d its
own offset would have to be about SIX TIMES the 6d offset AND of the opposite sign.
**AND I PREDICT MORE THAN THE VERDICT: all three lie above 7p's -0.125290 as well, so
neither rank 1 nor rank 2 is touched.**
FALSIFIED IF: any dE < -0.157621, or any dE < -0.125290.

## X3 · THE ORDERING AMONG THE THREE SURVIVES THE CHANGE OF CURRENCY.
dE(6f) < dE(7f) < dE(8f), the same order as their eigenvalues.
FALSIFIED IF: any adjacent pair inverts.
**THIS IS THE CLAUSE MOST LIKELY TO FAIL.** The three differ by 11.3 and 6.2 mHa in
eigenvalue, and the offset is 19.3 mHa at 6d — an offset that varies by a few mHa across
n at fixed l would reorder them.  I file it as predicted-correct and expect it to be the
one that costs me.

## X4 · THE OFFSET IS SMALLER AT f THAN AT d, AND OF THE SAME SIGN.
0 < dE(ch) - eps(ch) < 19.277 mHa for all three, i.e. dE less bound than eps, by less
than the 6d figure.  Rationale: the offset is core relaxation plus the correlation
potential, and a 6f/7f/8f orbital at Z=89 is far more diffuse than 6d — it perturbs the
[Rn] core less, so it should pay less relaxation.
FALSIFIED IF: any offset is negative, or any exceeds 19.277 mHa.

## X5 · THE FALLBACK FIRES ON EVERY ITERATION, NOT A FEW.
n_fb == it for each converged run, to within 1.  Rationale: F78.2 is refuted and the
mechanism is STATE MISIDENTIFICATION.  eigen_sr's initial guess carries no knowledge of
the target node count, so the standard bracket should misidentify the state at EVERY
iteration, not heal as the field settles.
FALSIFIED IF: n_fb is materially less than it — which would mean the channel becomes
healthy on its own and the misidentification is a start-up artefact, not structural.

## X6 · NO SCAN-BOUND EDGE FLAG ON ANY CONVERGED CHANNEL.
The window spans a factor of 40 in |e| and the iteration-1 zero/e_std ratios were 1.56,
1.44, 1.36.  As the field settles e_std should approach the zero, moving it further from
both edges.  **This is F79.1's clause and it is the one I have built the instrument to
be able to fail: edge_lo/edge_hi are recorded on every firing.**
FALSIFIED IF: any converged channel carries an edge flag on its final firing.

## X7 · THE WITHDRAWN MULTIPLES COME BACK SMALLER, NOT LARGER.
Restated in dE, the margins above 7p will be LESS than s79's withdrawn 2.898 m / 3.248 m
/ 3.440 m.  Rationale: the offset is positive at 6d and I have predicted it positive and
smaller at f (X4); 7p's own dE is fixed, so a positive f offset moves the f channels
DOWN toward 7p in dE relative to their eigenvalue positions... **NO — it moves them UP,
away from 7p, because a positive offset makes them LESS bound.**  Corrected before
filing: I predict the margins come back LARGER than the withdrawn multiples, but by less
than 20 mHa in absolute terms.
FALSIFIED IF: any restated margin is smaller than its withdrawn eigenvalue-currency
counterpart, or larger by more than 20 mHa.

## THE CAN-FAILS, DECLARED, AND WHAT THEY MUST RETURN
C1 machinery: 6d with the fallback INERT must return E = -25694.541630577907, the sealed
   value, to 1e-9.  If it does not, the driver is not the sealed solver and nothing below
   it counts.
C2 fallback path: 6d with the fallback FORCED on the 6d channel must fire at least once
   and land on the SAME energy to 1e-6.  **This is the control s79 did not have: it tests
   that the fallback RETURNS what the ruling path returns, on a channel where the ruling
   path works.**
C3 scorer: 6d against baseline 7p must return ENTRANT CHANGES; 5f against baseline 6d
   must return ROW HOLDS.  **Both verdicts reachable, as M's order requires — the
   instrument must not be one whose only answer is that the row holds.**
ALL THREE RUN BEFORE ANY QUESTION RUN AND GATE IT.
