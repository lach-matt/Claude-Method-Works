# PREDICTION-FK-SCALE (s39, item 1) — WRITTEN BEFORE ANY PER-ROW gap_avg IS READ OR ANY ARITHMETIC IS RUN (R 1449).

M's ruling, s39: "run it as a feasibility interval." The interval is the measurement. NO VALUE OF lambda IS ADOPTED FROM THE ANSWER —
that would be a fitted constant and is forbidden (no constant beyond c = 137.035999). The output is an interval, reported feasible or
infeasible, and its consistency with the independently known HF F^k overestimate is a SECOND and SEPARATE leg.

## 0 · The object, stated exactly
The LS term correction enters the gap linearly in F^k. Define, per row, the one-parameter family

    gap(lambda) = gap_avg + lambda * D,     D = gap_term - gap_avg,     lambda in [0,1]

lambda = 0 is the walk's ruling HF field (12/13, banked s37/s38). lambda = 1 is the full LS term correction (9/13, banked s38).
A row is CORRECT when sign(gap) matches the record's first-ionised subshell (record column RECALLED-NOT-ENTERED, comparison only).
Each row is linear, so it has AT MOST ONE crossing, at lambda* = -gap_avg / D.
FEASIBLE means: there exists lambda in [0,1] with all 13 rows correct simultaneously.

## 1 · What is already banked and is therefore NOT predicted
At lambda = 0: Th alone is wrong (12/13). At lambda = 1: Th correct, Hf/Pa/U/Cm wrong (9/13).
Th gap_avg +0.0083, gap_term -0.0304, D = -0.0387. Ac gap_avg +0.0240, gap_term +0.0149, D = -0.0091.
Class mean shifts: A -0.0077, B -0.0438, C -0.0389. gapTERM column for all 13 rows (TABLE-SO-SESSION-38).
Per-row gap_avg for the other 11 rows is NOT read at the time of writing. The four crossings that decide the answer are unknown here.

## 2 · Predictions (falsifiable; failure is logged, not suppressed)

PF-1  THE INTERVAL IS NON-EMPTY. Feasible.
      Reason: the lower bound is Th's crossing, and Th's D is the largest single-row shift on the pair while its gap_avg is small
      (+0.0083), so Th flips EARLY. The four rows that break are class B/C with gap_avg near +0.015..+0.038 against shifts of
      -0.039..-0.044, so they flip LATE. Early-low against late-high is the shape that leaves a window.

PF-2  THE LOWER BOUND IS Th AND IS lambda_Th = 0.214 +- 0.002. (Arithmetic on banked Th figures only: 0.0083/0.0387. Stated as a
      derived value, not a blind guess — flagged so it cannot later be read as a successful prediction of an unknown.)

PF-3  THE UPPER BOUND IS SET BY U (Z=92), NOT BY Hf, Pa OR Cm, at lambda_U = 0.39 +- 0.08.
      Estimated from class-C mean shift -0.0389 and U's gapTERM -0.0237 => gap_avg ~ +0.015 => 0.015/0.039.
      Ordering predicted: lambda_Th 0.21 < lambda_U 0.39 < lambda_Pa 0.49 < lambda_Hf 0.62 < lambda_Cm 0.98.

PF-4  NONE OF THE EIGHT ROWS CORRECT AT BOTH ENDS CROSSES ZERO INSIDE [0,1]. Sc, Y, La, Ce, Gd stay s-first; Lu, Ac, Rf stay d-first.
      Ac is the row at risk (margin +0.0149 at lambda=1, the smallest correct margin in the table) and is predicted to SURVIVE,
      because Ac's D is -0.0091, far too small to carry +0.0240 through zero. Score as a function of lambda: 12 -> 13 -> 12 -> ... -> 9.

PF-5  AND THE CANDIDATE DIES ON THE SECOND LEG, NOT THE FIRST. A window near lambda ~ 0.21-0.39 means F^k reduced to roughly a
      QUARTER to A THIRD of their HF values — a 60-80% reduction. The physical screening of Slater-Condon parameters is of order
      10-30% (RECALLED-NOT-ENTERED, source owed; no primary reached this session). PREDICTED VERDICT: FEASIBLE BUT INCONSISTENT.
      The required reduction is several times the physical one, so a uniform F^k scale is refused as the mechanism even though a
      window exists. THE INTERVAL IS THEN A MEASUREMENT OF HOW FAR THE RESIDUAL IS FROM SCREENING, which is what was asked for.

PF-6  IF INSTEAD THE INTERVAL IS EMPTY (lambda_Th >= min of the four), the finding is stronger and simpler: no uniform scale can
      work at any magnitude, the linear-in-F^k family is closed out entirely, and the row-differential residual is NOT a multipole
      magnitude problem. PF-1 would be falsified and this is the branch that closes the candidate outright.

## 3 · Held / not in this run
No lambda adopted. No SCF re-run — arithmetic on banked gap_avg and gap_term only. No per-row F^k recomputation, no screened-F^k
derivation (that would be the mechanism, and it is only reached if PF-5 fails). SO stays eliminated (PS-1, s38). Frozen convention
unchanged; PV-3 untouched. The physical-screening magnitude of PF-5 is RECALLED and carries a source debt: if the verdict turns on
it, a primary must be reached before the verdict is registered.
