# RESULT S81 — ITEM 2. F80.3 IS CLOSED. O-C1's FALSIFIER RUNS AT A SECOND CONFIGURATION.
# THE REPAIR THAT MATTERED WAS NOT THE TOLERANCE. IT WAS J2, AND IT SHRANK THE SCATTER 17x.
# Prediction sha256 933aad7ac13edba70911f0ce364fce1d73d716915cf35b2c0ad0ab866c42975d, filed first.
# Instrument pack81/perturb81.py — J1 measured TOL · J2 stationary-to-stationary · J3 lever · J5 cfg argument.

## §1 · F80.3 CLOSED. s80's TEN ROWS RE-LABELLED AT THE MEASURED FLOOR
TOL = **0.034493 mHa**, F80.2's MEASURED drop at Z=89 6d. No re-run: the raw dE are in
pack80/perturb80.jsonl and the floor is a property of the scheme, not of a run.
| pert | amp | dE (mHa) | s80 label | RE-LABEL |
|---|---|---|---|---|
| noise | 0.02 | +0.009306 | SECOND SOLUTION, HIGHER | **SAME BASIN** |
| noise | 0.02 | −0.005121 | *SECOND BASIN — O-C1 FALSIFIED* | **SAME BASIN** |
| noise | 0.10 | +0.000953 | SAME BASIN | SAME BASIN |
| noise | 0.10 | +0.004141 | SECOND SOLUTION, HIGHER | **SAME BASIN** |
| noise | 0.30 | −0.029527 | *SECOND BASIN — O-C1 FALSIFIED* | **SAME BASIN** |
| noise | 0.60 | −0.033677 | *SECOND BASIN — O-C1 FALSIFIED* | **SAME BASIN** |
| mix | 0.02 | +0.008163 | SECOND SOLUTION, HIGHER | **SAME BASIN** |
| mix | 0.10 | +0.008225 | SECOND SOLUTION, HIGHER | **SAME BASIN** |
| mix | 0.30 / 0.60 | — | NO CONVERGENCE | NO STARTING POINT |
**LOWER-ENERGY BASINS AT THE MEASURED FLOOR: ZERO.** All three of s80's FALSIFIED labels
and all five of its HIGHER labels collapse to SAME BASIN. **F80.3 IS CLOSED.**
Recorded, because it was filed in advance: the deepest row clears the floor by
**0.0008 mHa — 2% of the floor.** This was a near thing and the prediction said so.

## §2 · THE SECOND CONFIGURATION, cfg88+7p, RANK 2 AT Z=89
**J1, MEASURED, NOT CHOSEN: the 7p restart ladder settles at 0.022195 mHa** — and it
**RISES**. See F81.1. TOL := 0.022195 mHa for this configuration.
Can-fails ran first and both passed: **C1** zero perturbation from a stationary reference
returns SAME BASIN with dP = 0.0 and dE = 1.9e−5 mHa; **C2** truncated re-convergence
returns +10167.02 mHa, NOT-SAME. **s80's C1 failed at first attempt and that failure was
F80.2; with both sides stationary it passes by three orders of magnitude.**
| pert | amp | dP | LANDING dE | STATIONARY dE | J2 gain | verdict |
|---|---|---|---|---|---|---|
| noise | 0.02 | 0.02000 | +0.008864 | **+0.000081** | −0.008783 | SAME BASIN |
| noise | 0.10 | 0.10012 | +0.007760 | **+0.000262** | −0.007498 | SAME BASIN |
| noise | 0.30 | 0.29697 | +0.000003 | **+0.001089** | +0.001086 | SAME BASIN |
| noise | 0.60 | 0.55651 | −0.010041 | **+0.001495** | +0.011535 | SAME BASIN |
| mix | 0.02 | 0.02000 | +0.009517 | **+0.001022** | −0.008496 | SAME BASIN |
| mix | 0.10 | 0.10012 | +0.013446 | **+0.001200** | −0.012246 | SAME BASIN |
**O-C1 IS NOT FALSIFIED AT cfg88+7p. IT IS ALSO NOT ESTABLISHED.** This test can only ever
kill the rule, never carry it — filed in advance, again.

## §3 · WHAT IS ACTUALLY NEW: J2, AND IT IS A BIGGER EFFECT THAN THE TOLERANCE
| | spread over six runs | range |
|---|---|---|
| LANDING (s80's protocol) | −0.010041 .. +0.013446 mHa | **0.023487** |
| STATIONARY (J2) | +0.000081 .. +0.001495 mHa | **0.001414** |
**J2 SHRINKS THE SCATTER BY A FACTOR OF 17, AND MOVES EVERY RUN TO THE SAME SIDE OF THE
REFERENCE.** All six stationary values are POSITIVE: every perturbation returns to a point
at or above the reference, none below, within 0.0015 mHa on a total of −25694 Ha —
**58 parts per trillion.**
**THIS IS THE REPAIR F80.3 SHOULD HAVE SPECIFIED AND DID NOT.** F80.3 said "set TOL from
the measured resolution". That is necessary and it is not sufficient: raising the
tolerance hides the scatter, whereas restarting both sides REMOVES it. s80 compared a
stationary point against a still-descending one, and the bias was of the same size as the
effect it was hunting. **A tolerance is a claim about resolution; J2 improves the
resolution instead of accommodating it.**
**AND IT RAISES THE FLOOR UNDER O-C1's NULL BY MORE THAN AN ORDER OF MAGNITUDE.** s80
could exclude a competing basin only below ~0.035 mHa. At 7p, stationary-to-stationary,
the falsifier resolves a competing basin below **~0.0015 mHa** — the observed spread — and
**0.0015 mHa is 0.005% of m(89) = 32.332 mHa.**

## §4 · A FREE DETERMINISM RECEIPT, RECORDED BECAUSE IT WAS NOT PLANNED
The six-run grid was executed twice in this session by operator error. **The two sets are
identical in every dE to all six recorded decimals**, landing and stationary alike. That
is a reproducibility gate nobody designed, and it is kept as one. The duplicate rows
remain in perturb81.jsonl and are deduplicated in scoring.

## §5 · PREDICTION SCORED — W1 W3 W6 CORRECT, W4 SPLIT, W2 MOSTLY FALSIFIED, W5 UNRESOLVED
  W1 re-label returns zero falsifications . . **CORRECT**, and by 2% of the floor. The
     prediction called it "nearly a coin-toss" and filed the losing branch's honest
     statement in advance. It was not needed.
  W2 J2 gains 0.01-0.06 mHa, SAME direction, spread narrower by ≥2x . . **THE SPREAD
     CLAUSE IS CORRECT AND UNDERSTATED — 17x, not 2x. THE OTHER TWO CLAUSES ARE
     FALSIFIED.** Gains are 0.0011 to 0.0122 mHa, mostly BELOW the predicted band, and
     **they run in BOTH directions** — two runs rise under stationarisation. The filed
     rationale, that the bias is systematic and one-signed, is wrong, and F81.1 is why.
  W3 O-C1 not falsified at 7p . . **CORRECT**, zero rows below −TOL, all six above zero.
  W4 the 7p drop is 0.01-0.10 mHa and differs from 6d's 0.034493 . . **SPLIT.** The
     magnitude is right, 0.022195, and it does differ. **But it is not a DROP: the 7p
     ladder RISES.** The word "drop" was carried from F80.2 without asking whether the
     direction was a property of the scheme or of one configuration. **That is F81.1 and
     the prediction's own wording is where it surfaced.**
  W5 mix breaks on node count at amp ≤ 0.30 . . **UNRESOLVED** — only 0.02 and 0.10 were
     gridded and both converged. Filed in advance as possibly unresolvable. It is.
  W6 C1 passes at first attempt . . **CORRECT ON THE SCIENCE, AND THE RECORD MUST SAY
     MORE:** it passed on the first attempt of the CORRECTED instrument, after two faults
     of my own (F81.2, F81.3) were raised and repaired. The gate was never run against a
     scored question row in a broken state.

## §6 · RECORDED AGAINST THIS RESULT, NOT BURIED
1. **TWO FAULTS WERE RAISED AGAINST THIS INSTRUMENT BEFORE ANY QUESTION ROW WAS SCORED.**
   F81.2 (TOL a thousand times too small — the units) and F81.3 (the lever read off the
   wrong object). **Both were caught by the instrument's own gates, not by inspection.**
2. **ONE Z, TWO CONFIGURATIONS, ONE RUNG, ORBITAL-SPACE PERTURBATIONS ONLY.** A basin
   reachable only by a different occupancy pattern is outside this test by construction.
3. **THE GRID IS SIX RUNS, NOT TEN.** The large-amplitude mix direction at 7p is
   UNTESTED, not tested-and-passed. Declared in the prediction before the run.
4. **O-C1 REMAINS OPEN AND LOAD-BEARING.** A null with a better floor is still a null.
   **THIS IS NOT A PROOF OF GLOBAL MINIMALITY AND MUST NEVER BE QUOTED AS ONE.**
5. **s80's rows were re-labelled at 6d's OWN measured floor (0.034493), not at 7p's.**
   Mixing the two would be F79.2's species. The floors are per-configuration by J1.
