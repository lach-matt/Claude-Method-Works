# SOLVER-FINDING — Löwdin session 4 (2026-08-16). Bridge §4 Step 1 run.
Bank restore-point-2_13 (R 1700) unchanged. Nothing written to register/index/store.
Inputs: CODE-LOWDIN-2_13.txt (ground.py, brack.py hashes verified 3aa24998/659fd11b),
COORDINATES-2_13.csv (358 measured rows), ISOLATE-LOWDIN-3 (manifest 14/14 verified),
R 1258 values via iso.py for Rb I, Y III (register-witnessed only; not in index measured grade).

## 1 · Gates run before any claim
- brack.py reproduces the record: La (0.7071,1.7071) Ac (1.3660,1.9841) Lr (1.9841,2.4409).
- tf.py: neutral TF phi(1)=0.4240, phi(10)=0.0243 (tabulated); ion shooting converges (K+ core x0=15.68).
- rad.py: hydrogen delta = 0 to 4e-6 for l=0,1,2, n<=7.
- Two solver faults found and fixed before results were read: (i) symmetrised log-mesh tridiagonal
  had 1e17 dynamic range and returned one eigenvalue k times — replaced by Numerov shooting;
  (ii) bisection floor -0.6 Z^2 put h^2 q/12 > 1 at deep E, spurious nodes (119 at E=-200) — floor
  set to -0.6 zeta^2, justified by n* >= 1. Both are R 1671's shape: an instrument reporting on what
  it admitted. Recorded, not hidden.

## 2 · Result: TF (ion, Latter tail) delta vs measured, 39 channels, 10 species
rms 0.315, mean signed -0.257 (under-bound throughout). Q.final (fitted) is rms 0.14.
=> Bridge §4 Step 1 gate FAILS as stated: "same values" is not met by a TF/Latter solver.
Prediction stated before the run (rms 0.1-0.3) held at its upper edge.
Where it fails: the collapse channels. K I d .018/.246, Ca II d .052/.634, Sc III d .071/.653,
Ba II f .005/.756, Y III f .004/.147. s and p channels within 0.1-0.4 (Na I within 0.03).

## 3 · Ordering test at the closed-core ions (rung C criterion, TF n* in place of measured)
Sc III 3d ✓ · Y III 4d ✓ · La III 5d ✓ · Ce IV 5d ✗(4f) · Ac III 6d ✓ ·
Th IV 6d (= neutral entrant, ≠ ion ground 5f) · Lr III (5f filled) 6d — the non-relativistic answer.
Reading: TF carries every d-collapse and NO f-collapse — the f defect stays ~0 at all Z. The
two inversions (La 5d, Ac 6d) come out of one-electron TF; the f openings (Ce, Pa) do not.
This is Latter's own boundary: the f drop needs exchange (TFD) or better.

## 4 · What this fixes for the programme
Step 2 (regenerate computed grade to Z=120 from a solver) is NOT unlocked: TF is worse than
the fit it would replace. Candidate next segment: TFD (Latter's exchange term) with the same
gate; if the f channels move to within ~0.1 the collapse steps become computable.
Otherwise the "computed" grade stays Q.final and the index equation is a fit, and the record
must say so.

## 5 · Owed
None new to the register beyond what Session 3 listed; this finding is a candidate R 1713
(TF gate fails at 0.315; d-collapse yes, f-collapse no; two solver faults registered).
Files: tf.py rad.py gate.py gate.json SOLVER-FINDING.md.