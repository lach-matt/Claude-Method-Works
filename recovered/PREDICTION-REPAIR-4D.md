# PREDICTION-REPAIR-4D (s42, item 0b) — WRITTEN BEFORE ANY REPAIR CODE IS BUILT (R 1449)
M's ruling s42 (2): "Test all three candidates and let the comparison decide." No a priori selection.

## 0 · THE OBJECT, AS MEASURED (FINDING-PROBE-4D)
At Z=21, config [Ar]4s^2 4d^1: it1 returns the correct 4d (nd=1, e=-0.047224); it2's field has NO normalised
1-node solution anywhere (421-point scan, zero sign changes, min log(nrm) = +0.892 -> norm 2.44x). The
channel's own diffuse orbital feeds its own exchange source and boundary (`Yk(P[a],P[b],k)`, `yold=Pold*e^(-x/2)`),
destroying its own root. The bracket then walks DOWN out of the node-1 window and returns the nd=0 state.

## 1 · THE THREE CANDIDATES, DEFINED SO THEY ARE DISTINGUISHABLE
**(i) NODE-GATED BRACKET.** `tgt = n-l-1` is computed by solve_one and NEVER USED. Restrict the root search
to the contiguous e-window where nd == tgt; bisect log(nrm) inside it; if there is no sign change there,
raise a NAMED exception rather than returning another state's root. Changes WHICH root is accepted. Changes
no field, no physics, no converged fixed point.
**(ii) MIXING DAMPING.** No change to solve_one at all. Reduce the SCF mixing beta (CHOSEN = 0.4) so the
diffuse orbital enters gradually. **The property that makes this admissible: beta cannot change the converged
answer.** At a fixed point P = (1-b)P + bU implies P = U for any b in (0,1]. beta is convergence control,
not a constant of the theory, so this adds NO parameter to the law. Tested at b = 0.2, 0.1, 0.05.
**(iii) CHANNEL HOLD.** On nd != tgt for one channel, do not accept that channel's update this iteration:
hold P[a], eps[a] at their previous values, let the other shells relax, retry next iteration. Fail loudly
only if the mismatch survives to convergence. Changes the PATH, not the fixed point.

## 2 · DECISION CRITERIA, FIXED NOW SO THE COMPARISON CANNOT BE READ AFTER THE FACT
    D1 INERTNESS (disqualifying). On the HEALTHY Z=21 3d candidate, the converged D must reproduce the
       banked s41 chain value to < 1e-5 Ha. A candidate that moves a healthy number is DISQUALIFIED
       whatever it does for 4d. Comparison to the parent, not to itself.
    D2 PRODUCES 4d. run2 converges on [Ar]4s^2 4d^1 with nd == 1 at every iteration and returns E.
    D3 AGREEMENT (the decider). Every candidate passing D1+D2 must give the same 4d D to < 1e-4 Ha.
       **IF TWO SURVIVORS DISAGREE, THE COMPARISON HAS NOT DECIDED AND NEITHER IS ADOPTED** — a repair that
       changes the number it recovers is a new field, not a repair.
    D4 GATES. t7c_hfsr.py / t7b_hf.py / hfc2.py NOT edited; gates 1-71 stay byte-identical; census clean.
    D5 FURTHERS n+l (M's standing test). f392_guard UNSAFE count stays 0 and the 4d channel becomes scoreable.

## 3 · PREDICTIONS, WITH REASONS, SO FAILURES ARE SCORED NOT EXPLAINED AFTER
    PR-1  (i) PASSES D1, FAILS D2.                                                      PREDICT: TRUE
          Reason: at it2 there is no node-1 root to bracket onto. A node gate cannot conjure one. Its
          value is that it converts a SILENT WRONG STATE into a LOUD CORRECT FAILURE — real, but it does
          not open the 4d row alone.
    PR-2  (ii) PASSES D1 and D2 at some b <= 0.1.                                       PREDICT: TRUE
          Reason: the instability is driven by the SIZE of the orbital change per iteration; a smaller
          step keeps the field inside the region where the node-1 root exists.
    PR-3  (iii) PASSES D1 and D2.                                                       PREDICT: TRUE
          Reason: holding the offending channel is (ii) applied to one orbital instead of all of them.
    PR-4  (ii) and (iii) AGREE to < 1e-4 Ha (D3 satisfied).                             PREDICT: TRUE
          Reason: both change only the path; if a fixed point exists it is the same one.
    PR-5  The converged 4d eigenvalue lies in (-0.12, -0.015) Ha, diffuse outer-well.   PREDICT: TRUE
    PR-6  (i) combined with a survivor of (ii)/(iii) is INERT on all 29 banked chain steps.
                                                                                        PREDICT: TRUE

## 4 · THE FOURTH OUTCOME, REGISTERED IN ADVANCE SO A NULL IS NOT MISREAD
If ALL THREE fail D2, the reading is that **the self-consistent fixed point itself has no node-1 solution** —
the diffuse 4d is not merely destroyed on the path to convergence but absent at convergence. That is NOT a
numerics fault and it IS the PV-3 object (frozen-vs-relaxed, UNBOUNDED), restoring s41 §2b(11)'s conclusion
by a different and better-evidenced route. It would be a finding, not a null, and it must be reported as one.
DIAGNOSTIC THAT SEPARATES IT: run (ii) at b = 0.05 and read whether min log(nrm) in the node-1 window
DECREASES toward 0 across iterations (approaching a root) or INCREASES (receding from one).

## 5 · HELD
No record value entered. c = 137.035999 only. Grid 4000 / 2e-5, qtail 1, maxit, seed, frozen avg-of-config
all unchanged. beta is varied and is declared CHOSEN-CONVERGENCE-CONTROL, not a constant of the law; any
adopted value travels with that label. No banked number is overwritten by this comparison.
