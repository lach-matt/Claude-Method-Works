# PREDICTION-PROBE-4D (s42, item 0) — WRITTEN BEFORE ANY PROBE CODE IS RUN (R 1449)
M's ruling s42 (1): "Prob first." Bridge s41 §3(0). Object: distinguish
  (a) 4d is GENUINELY UNBOUND in the field of the failing step  → F39.2 is PV-3, not numerics
  (b) 4d is BOUND but OUTSIDE THE BRACKET'S REACH               → F39.2 is numerics, repairable by re-bracketing

## 0 · WHAT THE MACHINERY ACTUALLY IS (read before predicting, so the prediction is against the real object)
Two corrections to the bridge's own wording, entered here because they change the probe:
- THE FIELD IS NOT FROZEN. `nlchain.step` calls `H.HFC(Z, cfg+cand, c=C0).run2()` — a FULL SCF per candidate.
  The failing object is the l=2 channel inside the SCF of Z=21 with config cfg_prev(Ca) + 4d^1, i.e. a
  21-electron NEUTRAL system at nuclear charge 21. "Sc+ frozen potential" in bridge §3(0) is WRONG on both counts.
- SOLVE_ONE DOES NOT RAISE. It RETURNS (u, e, nd=0, res) and `hfc2.py`'s `if nd!=n-l-1` raises afterwards.
  So the failing inputs (Vloc, X, e0) can be captured by a subclass with NO exception handling and NO edit to
  t7c_hfsr.py or hfc2.py (gates 1-71 must stay byte-identical).
- THE EIGENVALUE CONDITION IS NORM-BASED. With exchange carried as an inhomogeneous source s, the solution
  scale is fixed by that source and the eigenvalue is where the norm passes 1; `solve_one` brackets on
  log(nrm) and bisects. This admits MULTIPLE ROOTS, one per state, and the search is a single monotone
  expansion from the eigen_sr seed. That is the structure a "missed state" would hide in.

## 1 · PP-0 — MACHINERY GATE, TO PASS BEFORE ANY 4d NUMBER IS READ (can-fail, PC-0 pattern)
The probe re-expresses `shoot(e)` outside its closure, using the SAME module-level objects
(`qlog`, `_derivs`, `_lib.shoot_x`, `_D` from t7c_hfsr) and the SAME grid. It is not new numerics; it is the
parent kernel called directly. That claim must be TESTED, not asserted:
  PP-0a  On the HEALTHY l=2 channel at the same step (n=3, tgt=0), the probe's own root of log(nrm)=0
         reproduces the parent `solve_one`'s returned e to |de| < 1e-8, and returns nd = 0.
  PP-0b  The probe's shoot at the parent's returned e gives log(nrm) within 1e-6 of 0.
IF PP-0 FAILS the probe is an instrument fault and NO (a)/(b) verdict may be read from it. The scan is not run.

## 2 · PP-1 — THE VERDICT. PREDICTED: (b) BOUND, NOT (a) UNBOUND.
Stated with its reason so a failure is scored against the reason, not re-explained after:
The added electron sees nucleus +21 against 20 other electrons. If `_ceff` removes the 4d shell's
self-Coulomb (q=1 in that shell, so the shell contributes no other electron), the ASYMPTOTIC TAIL IS -1/r.
A -1/r tail carries an INFINITE Rydberg series. 4d cannot be unbound in a field with that tail. Therefore:
  PP-1  There EXISTS e < 0 at which the l=2 outward solution has nd = 1.               PREDICT: TRUE
  PP-2  The node-1 window's root lies in e in (-0.12, -0.015) Ha — hydrogenic-scale, diffuse outer-well
        state, NOT an inner-well collapsed state.                                       PREDICT: TRUE
  PP-3  nd(e) is MONOTONE NON-DECREASING in e across the scan (0 then 1 then 2 ...).    PREDICT: TRUE
  PP-4  The parent's returned nd=0 root and the node-1 root are SEPARATED by a region the single monotone
        log(nrm) expansion from the eigen_sr seed does not traverse — i.e. the seed eh sits BELOW the
        node-1 window and the first sign change above it is still the nd=0 state's.     PREDICT: TRUE

### IF PP-1 IS FALSE (nd never reaches 1 for any e < 0), THE MECHANISM IS NAMED IN ADVANCE
Then the tail is NOT -1/r: `_ceff` is leaving a residual self-Coulomb (or the avg-of-config occupancy
weighting is charging the channel), the field is effectively that of an ANION tail or a screened
short-range well, and the d well then holds exactly ONE state (3d, collapsed). That is verdict (a),
it is PV-3, and PV-3 becomes the prerequisite for the 4d row exactly as s41 §2b(11) states.
DIAGNOSTIC THAT SEPARATES THE TWO IN THE SAME RUN: read Vloc(r)*r at large r. It must approach -1.0 for the
Rydberg reading. If it approaches -0.0 or a positive value, PP-1's reason is refuted at its root and the
verdict is (a) with a MECHANISM, not merely a null.

## 3 · PP-5 — THE THIRD OUTCOME, SO A NULL IS NOT MISREAD AS EITHER
  PP-5  nd(e) jumps 0 -> 2 with NO e giving nd = 1, or nd is non-monotone.              PREDICT: FALSE
If PP-5 is TRUE the finding is an INSTRUMENT fault in node counting (the count runs only over u[:m+1], the
region inside the outer turning point m, and a diffuse state can carry its node OUTSIDE m), NOT a physical
verdict. Neither (a) nor (b) may then be entered. This is registered in advance because a 0->2 jump would
otherwise read as "unbound" and close a live object on an artefact.

## 4 · WHAT IS NOT PREDICTED HERE
No repair is designed in this file. No chain row is produced. No banked number is touched. Whether a
successful (b) verdict licenses re-bracketing by node label is a SEPARATE prediction, written only after
this one is scored. PV-3 itself (frozen-vs-relaxed, UNBOUNDED) is NOT attempted here.

## 5 · HELD
No record value is entered. c = 137.035999 only. Grid, seed, qtail, maxit unchanged from s41 CHOSEN.
