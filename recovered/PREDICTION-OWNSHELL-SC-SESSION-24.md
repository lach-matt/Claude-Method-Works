# PREDICTION — bridge-23 s3(2) own-shell class (Sc Ti Cr Fe Ni Er), Sc first. Session 24. Written BEFORE the run.
Object: t7c_cuaudit.py (t7c_corrz VERBATIM + env FENT) extended by env FOCC = entrant occupation used for BOTH the density (k)
and the SIC weight (f) [FOCC=0.5, FENT=0.5 = standing]. corr=Z, SIC_NOCLAMP=1. Sc: EZ -0.3211, meas -0.2946, resid -0.0265.
Input carried from item (1)B: at f=1/2 the entrant's own SIC potential is ~1/9 of a sibling's by cancellation (-f v_H - f^(1/3) v_x).
Sc has NO own-shell siblings (3d^1): the sibling term of the candidate is empty here by construction.
## Test C: SIC decomposition of Sc under Z (mode none / ent / all), same as SICDEC s21 but on the Z chain
PO1: indirect (all - ent) on Sc is |.| <= 0.004 (core/4s SIC only; N_sib = 0), so the Sc over-binding is NOT a sibling effect.
PO2: direct (ent - none) on Sc is in [-0.020, -0.035] (s21 pol chain gave -0.0281).
## Test D: Janak integral of the entrant channel: eps(f) at FOCC = 0.25, 0.5, 0.75, 1.0; DE_J = int_0^1 eps(f) df (Simpson on 0..1
   with the f=0 point taken as the ion's LDA eigenvalue via a fifth run at FOCC=1e-3), compared with eps(1/2) = TS.
Algebra (Janak 1978; PZ-81 SIC scaling U[fn]=f^2 U, E_x[fn]=f^(4/3) E_x): eps_SIC(f) = -2fU - (4/3) f^(1/3) E_x, so
eps_SIC(1/2) - int_0^1 eps_SIC = -0.058 E_x = +0.058 |E_x[n_ent]| -- the TS midpoint sits SHALLOWER than the integrated removal
energy by 0.058 |E_x| of the entrant orbital (Hartree part exact at the midpoint; only the f^(1/3) exchange piece has curvature).
PO3: DE_J - eps(1/2) on Sc is NEGATIVE (deeper), in [-0.035, -0.008]  (|E_x[n_3d]| ~ 0.15-0.6 Ha).
PO4: eps(f) is monotone decreasing in f on Sc (each added tenth of an electron deepens the entrant, SIC dominating over Hartree).
Consequence: if PO3 holds, the SIC/LSD chain over-binds Sc by MORE than the TS row shows -- the class shape is a functional-class
over-binding of the compact nodeless 3d, not a bookkeeping error of the entrant's weight; the TS half-point is an accidental
partial mask. If PO3 fails positive (DE_J shallower), the TS midpoint IS the over-binding and the class closes toward zero.
Thresholds (stated): class-relevant >= 0.005 Ha; "closes" |resid| <= 0.003.
Runs: Sc only in this item; 5 SCF at FOCC in {1e-3, 0.25, 0.5, 0.75, 1.0} + 2 mode runs; ~3-4 s each; timeout 200; jsonl.
