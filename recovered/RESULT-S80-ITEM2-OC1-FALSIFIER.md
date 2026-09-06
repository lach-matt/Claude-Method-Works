# RESULT S80 — ITEM 2. O-C1's FALSIFIER IS RUN, FOR THE FIRST TIME.
# O-C1 IS NOT FALSIFIED. IT IS ALSO NOT ESTABLISHED. WHAT IS NEW IS A MEASURED FLOOR.
# Prediction sha256 e2beb3edd604e6786e1d8a62e993350c2df61167cf0516ca6b348a7eec48f085, filed first.
# Instrument pack80/perturb80.py — FIVE declared lines from sealed hfc2.py.

## THE OBLIGATION, AS s79 REGISTERED IT
RULING-S79: "THE FALSIFIER IS CHEAP AND IS NOT YET RUN: perturb a CONVERGED solution and
re-converge. A second basin at lower energy kills the rule as stated." It is now run.
**Seeds probe where the iteration STARTS. This probes the neighbourhood of where it LANDS.**

## CAN-FAILS — C2 PASSED, C1 FAILED AND THE FAILURE WAS THE SESSION'S BEST FINDING
C2 (comparator can say NOT-SAME): truncated re-convergence returned +10173.8 mHa. PASS.
C1 (comparator can say SAME): **FAILED at first attempt** — a ZERO perturbation returned
0.021 mHa LOWER. **That is F80.2: the sealed energies are not stationary under restart.**
The reference was repaired to restart-to-stationarity (H5) and C1 then PASSED at 3e-6 mHa
with dP = 0.0. **A can-fail that fails is doing its job; this one found a property of the
scheme that four sessions of seed tests did not.**
LEVER (H2, the F54.2 law): dP verified on every run. amp=0.02 gave dP=0.0200, amp=0.60
gave dP=0.5634. The lever moves the object, every run, not once.

## THE GRID — TWO KINDS, FOUR AMPLITUDES, REFERENCE E* = -25694.541665071
| pert | amp | dP | dE (mHa) | it | outcome |
|---|---|---|---|---|---|
| noise | 0.02 | 0.0200 | +0.0093 | 27 | returned |
| noise | 0.02 | 0.0200 | -0.0051 | 26 | returned |
| noise | 0.10 | 0.1001 | +0.0010 | 30 | returned |
| noise | 0.10 | 0.1001 | +0.0041 | 30 | returned |
| noise | 0.30 | 0.2986 | -0.0295 | 33 | returned |
| noise | 0.60 | 0.5634 | -0.0337 | 38 | returned |
| mix | 0.02 | 0.0200 | +0.0082 | 34 | returned |
| mix | 0.10 | 0.1001 | +0.0082 | 38 | returned |
| mix | 0.30 | 0.2967 | — | — | **NODE-COUNT RAISE, not basin evidence** |
| mix | 0.60 | 0.5554 | — | — | **NODE-COUNT RAISE, not basin evidence** |

## THE VERDICT, AND THE INSTRUMENT'S OWN LABELS ARE OVERRIDDEN
The instrument labelled three rows "SECOND BASIN, LOWER -- O-C1 FALSIFIED". **THOSE
LABELS ARE WRONG AND ARE OVERRIDDEN HERE. SEE F80.3.** Its TOL was 1e-6 Ha; F80.2 measured
the scheme's stopping resolution at 0.0345 mHa in the same session. **The full spread of
the eight converged runs, -0.0337 to +0.0093 mHa, IS THAT RESOLUTION.** All eight agree to
4e-5 Ha on a total of -25694 Ha — **1.7 parts per billion.**
**NO SECOND BASIN IS RESOLVED. O-C1 IS NOT FALSIFIED.**
**AND IT IS NOT ESTABLISHED. THIS TEST CAN ONLY EVER KILL THE RULE, NEVER CARRY IT** —
filed in advance, in the prediction, before the result was seen.

## WHAT IS GENUINELY NEW: THE NULL NOW HAS A FLOOR
**The falsifier resolves a competing basin only if it lies deeper than about 0.035 mHa
below the reference.** Before this session the evidence for O-C1 was four starts landing
on one value. It is now four starts PLUS a local neighbourhood probed in two directions at
four amplitudes with a STATED SENSITIVITY. **A bare null says nothing. A null with a
measured floor says how much has been excluded, and 0.035 mHa is 0.11% of m(89).**
**O-C1 REMAINS OPEN AND LOAD-BEARING. THIS IS NOT A PROOF OF GLOBAL MINIMALITY AND MUST
NEVER BE QUOTED AS ONE.**

## PREDICTION SCORED — Y1 CORRECT, Y3 CORRECT, Y4 SPLIT, Y2 AND Y5 FALSIFIED
  Y1 no second basin at lower energy . . **CORRECT IN SUBSTANCE.** Recorded honestly:
     **the instrument as filed would have scored Y1 FALSIFIED three times.** It is scored
     correct only because F80.3 was raised against my own tolerance. The prediction also
     filed IN ADVANCE that this test would be WEAK EVIDENCE — that judgement holds.
  Y2 return exact to 1e-9 Ha . . **FALSIFIED.** Scatter is 4e-5 Ha, forty thousand times
     the predicted figure. The rationale — same rung, deterministic code — ignored that
     the STOPPING TEST is path-dependent. This is F80.2 seen from the other side.
  Y3 large amplitudes fail on NODE COUNT, and must not be scored as basin evidence
     . . **CORRECT ON BOTH CLAUSES** — mix at 0.30 and 0.60, both node-count raises.
  Y4 mix more severe than noise at equal amp . . **SPLIT.** It BREAKS FIRST — correct,
     noise survives 0.60 where mix fails at 0.30. But dP at equal amp is not larger
     (0.0200066 vs 0.0200098). **The severity is in the DIRECTION, not the size**, which
     is what H3 was built to separate and what the dP clause got wrong.
  Y5 perturbed runs take MORE than the reference's 44 iterations . . **FALSIFIED.**
     They take 26-38. The reference's 44 is a cold numerov start; a perturbed converged
     solution is a WARM start even at amp=0.6. Predicted from the wrong baseline.

## RECORDED AGAINST THIS RESULT
1. **ONE Z, ONE CONFIGURATION, ONE RUNG.** Z=89, cfg88+6d, rung 0.
2. **THE PERTURBATIONS ARE ORBITAL-SPACE, NOT OCCUPANCY-SPACE.** A basin reachable only by
   a different occupancy pattern is outside this test by construction.
3. **TWO OF TEN RUNS DELIVERED NO STARTING POINT AT ALL** (node-count raise). The
   large-amplitude mix direction is therefore UNTESTED, not tested-and-passed.