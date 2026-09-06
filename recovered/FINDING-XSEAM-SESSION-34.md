# FINDING-XSEAM (s34) — candidate (a) HELD ON SHAPE: the frozen-orbital exchange-treatment difference on the removed entrant, LSD+PZ-SIC minus HF (Slater
average of configuration), has the seam's sign, its class ratio and its row size within x1.2-1.9 on every row. The exchange seam's home is NAMED, not closed.
Run: xseam.py, chain spin-averaged HFS neutral orbitals (t5_scf), six rows, one tool call. TABLE below (Ha; Delta_x = Dx_LSD+SIC - Dx_HF; seam = O_DSCF - E_DSCF, FINDING-B).
  Sc 3d  Dx_HF -0.2890  Dx_LSD -0.3440  Delta_x -0.0550 | seam 0.045 | ratio 1.22
  Y  4d         -0.2088         -0.2443          -0.0356 |      0.025 |       1.42
  La 5d         -0.2073         -0.2365          -0.0292 |      0.018 |       1.62
  Gd 5d         -0.2309         -0.2598          -0.0289 |      0.015 |       1.93   (4f7 at average-of-configuration weight)
  Lu 5d         -0.2300         -0.2588          -0.0287 |      0.023 |       1.25
  Cs 6s         -0.0229         -0.0333          -0.0104 |      0.015 |       0.69
PX-1 HELD (sign on all six; sizes: Sc 0.055 in [0.03,0.06]; nd 0.029-0.036 vs predicted 0.010-0.030 — Y 0.006 above the window, stated). PX-2 HELD: Sc/mean(nd)
= 1.8 (window 1.5-3.0). PX-3 HELD: every row within x2 (0.69-1.93). Reading (bound): the E-path over-delivery IS the local+SIC exchange of the entrant against
exact exchange — the frozen number OVERSHOOTS the seam by 20-90 % on d rows and undershoots by 30 % on Cs, which is the room the deferred candidate (b) (core
relaxation at DSCF, and the correlation difference between the paths) must fill; the seam is thus (a) minus a relaxation/correlation remainder of 0.005-0.014
on d rows and +0.005 on Cs. Nothing entered; no constant; frozen local orbitals (stated).
Owed to T4: R 1929 xseam built · R 1930 PX-1..3 held: exchange seam's home named · R 1931 remainder for (b) stated as a bound.
Files (pack34): PREDICTION-XSEAM · xseam.py · xseam.jsonl · this finding.