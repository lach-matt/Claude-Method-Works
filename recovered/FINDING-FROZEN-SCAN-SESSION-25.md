# FINDING — item (2), s25: frozen-orbital f-scan splits shape (ii). Files: frozen_scan.py (ref 1/2), frozen_scan2.py (FREF), frozen_scan3.py (CORR),
exfr.py, frozen_scan*.jsonl, TABLE-FROZEN-SCAN-SESSION-25.txt, PREDICTION-FROZEN-SCAN-SESSION-25.md (PF0–PF8 written before each run).
No constant, no measured input. Chain Z, SIC_NOCLAMP=1. Same f grid and f^(1/3) interpolation as s24 janak_table.py.
## Method: SCF at f=1/2 (TS reference); all radial densities frozen; entrant weight f varied in V_H, V_x, V_c and its own PZ SIC; one solve per f.
Gate PF0: eps_fr(1/2) == banked eps(1/2) to 1e-4 on all 15 rows (Ti, Cu at maxit=100, F25.1, values match).
## Result 1 (all 15 rows): the mask DE_J − eps(1/2) is DOMINANTLY A FIXED-ORBITAL PROPERTY OF THE FUNCTIONAL. Frozen fraction:
6s ~1.0 (Cs 1.14 on a 0.0025 mask) · 4d/5d 0.94–0.99 · 3d 0.94 (Sc) → 0.77 (Cu), falling across the row · 4f 0.78 (Er Tm Yb AND Dy 0.79).
Relaxation part DE_J − DE_J^fr: |.| <= 0.0095 on ALL 15 rows (Dy −0.0078). PF2 FAILED: s24 §2(2b)'s "SIC-relaxation part growing with
compactness (Sc −0.006, Yb −0.032)" is MISNAMED — that quantity is present with every orbital frozen. Correction owed to the s24 record.
Dy: frozen fraction and relaxation both equal the 4f class; Dy's −0.045 excess is in NEITHER. Object's bound (ruling) stands.
## Result 2 (Sc, PF4): the split is REFERENCE-DEPENDENT. Reference at f=1: relaxation part +0.0656 (frozen DE_J −0.4038). Around f=1/2
first-order relaxation cancels in the integral (Slater 1972 TS stationarity; Janak 1978); around f=1 it dominates. So the admissible
statement is "at the TS reference the mask is what the functional produces at fixed orbitals", not a reference-free decomposition.
## Result 3 (PF7): mask_fr / (−0.0583|E_x[n_ent]|) = 1.12–1.19 on all 14 non-Cs rows (Y La Gd Lu 1.13–1.17; Sc..Cu 1.14–1.19; Er Tm Yb Dy 1.12–1.14).
The compactness structure PO14 saw (1.19→1.51) was the relaxation part; frozen, it is a plateau incl. Dy. Cs 0.60 (diffuse; mask 0.0025).
0.0583 = (4/3)2^(−1/3) − 1 is the entrant PZ exchange-SIC f^(4/3) law: DE_J − eps(1/2) = A[1 − (4/3)2^(−1/3)] for E_SIC-x = f^(4/3) A. Ratio 1.00 = that law alone.
## Result 4 (PF8, Sc Yb, x-only chain, self-consistent E_x): ratio 1.09/1.07 (chain Z 1.17/1.12). Composition of the frozen mask:
exchange-SIC f^(4/3) law 1.00 + LSD total-density exchange curvature ~+0.07–0.09 + correlation ~+0.05–0.08. All three are what the functional
does at fixed orbitals; none is a chosen constant. Whether the +0.15 is a derivable scaling is a NEXT candidate, not claimed here.
## Not a closure. Failed predictions: PF1(Cs) PF2(Sc,Yb) PF5(Cs) PF8 (all with reasons above). Held: PF0 PF3 PF4 PF6 PF7.
Cs, Y meas RECALLED-NOT-ENTERED unchanged. Cross-ref: item (1)(c) folded here — KIPZ screening alpha by linear response is this same relaxed/frozen object.