# PREDICTION-XSEAM (s34) — ruling (M): candidate (a) against the exchange seam O_DSCF - E_DSCF (FINDING-B: Sc +0.045 · Y +0.025 · La +0.018 · Gd +0.015 ·
Lu +0.023 · Cs +0.015). Written BEFORE the run. (b) core-relaxation seam deferred to after the handoff by ruling.
Object (frozen orbitals, chain spin-averaged HFS neutral, t5_scf): removal-exchange of the entrant i (spin up, average of configuration) under the two treatments:
  HF:       Dx_HF  = -sum_{j core} (N_j/2) sum_k (l_i k l_j;000)^2 G^k(i,j)   [self term cancels Hartree exactly; no sibling for single entrants]
  LSD+SIC:  Dx_LSD = E_x[n_up=n_c/2+n_i, n_dn=n_c/2] - E_x[n_c/2, n_c/2] - E_x^pol[n_i]   with E_x = -(3/4)(6/pi)^(1/3) sum_s int rho_s^(4/3)  (the chain's Vx = -(6 rho_s/pi)^(1/3))
  Delta_x = Dx_LSD - Dx_HF   (negative = LSD+SIC loses MORE exchange on removal = binds the entrant more = E path over, the seam's sign)
PX-1: Delta_x < 0 on all six rows; sizes nd/6s 0.010-0.030, Sc 0.030-0.060.  PX-2: ratio Sc/mean(nd) in 1.5-3.0 (seam 2.0-3.0).
PX-3: row-by-row Delta_x within a factor 2 of the seam on every row (Lu >= Y > La ~ Gd on nd, as the seam). Failure: any positive row; Sc/nd outside 1.2-4; any
row off by more than x2. Bound stated in advance: frozen local orbitals (no relaxation, no correlation) — a candidate's SHAPE test, not its size closure.
Files: this · xseam.py · xseam.jsonl · TABLE-XSEAM.