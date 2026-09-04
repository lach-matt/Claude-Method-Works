# PREDICTION-CAND (s33) — M: test (a) against the three candidate homes of the d-row object. Written BEFORE any run.
Target (from record, frachf-R path, FINDING-RING/COMPARE-RZ): resid_R (+ = short) Y +0.0054 · Lu +0.0043 · La +0.0019 · Cs +0.0086 · Sc -0.0040 (OVER); S moves
these <= 0.0007 (PS-4). A candidate BEATS (a) only if it (c1) deepens Y/La/Gd/Lu by 0.002-0.007, (c2) does NOT deepen Sc by more than 0.002, (c3) is class-flat on
the nd rows within 0.003. (a) = null: no derived local-trunk term meets c1-c3; the 0.005 stays a stated non-local residual.
CORRECTION to the D-table before its numbers are re-used: the chain's SIC line acts on f*n_i with f = 1/2 for the entrant (t7c_corrz line 124), so the one-orbital
line is (n_ent/2, zeta=1), not (n_ent, 1). Column A_half recomputes A there (bench anchors r_s 5,10 cover r_s(ent/2) ~ 6.3). Prediction: |A_half - A| <= 0.0005, sign of D unchanged.
CANDIDATE (i) inhomogeneity: the PBE-form gradient correction H(r_s,zeta,t) built ON THE CHAIN'S OWN eps_c^S: H = gamma phi^3 ln[1 + (beta/gamma) t^2 (1+A t^2)/(1+A t^2+A^2 t^4)],
A = (beta/gamma)/(exp(-eps_S/(gamma phi^3)) - 1), t = |grad n|/(2 phi k_s n), k_s = sqrt(4 k_F/pi). gamma = (1-ln2)/pi^2 (derived: the high-density log
coefficient), beta = 0.066725 (Ma-Brueckner 1968 RPA gradient coefficient — derived, RECALLED numerically, comparison only). Both limits derived: t->0 GEA, t->inf H -> -eps_c.
Delta_i = <H(n_tot,zeta_tot,t_tot)>_ent - <H(n_ent/2, 1, t_ent)>_ent (cancellation law, eps level, no window; radial gradients by np.gradient on the SCF grid).
  P-i-1: nd rows Delta_i in [-0.015, -0.003] (deepening: the one-orbital line has large t, its H is the larger positive term).
  P-i-2: |Delta_i(Sc)| >= |Delta_i(Y)| (t^2 ~ s^2 n^(1/3): the compact entrant has the larger t AND the larger |eps_c| ceiling) -> (i) fails c2 if P-i-1 holds.
  P-i-3: 4f |Delta_i| >= nd |Delta_i|.  Also reported: <H_ent>, <H_tot>, and <eps_S(n_ent/2,1)>_ent = the whole SIC-correlation line (bound for (ii)).
CANDIDATE (ii) the SIC one-orbital line's own defect: two bounds from record, one new column. Bounds: |A_half| (bench-vs-S on that line) and M_csic (s26 midpoint
defect, Y -0.00071, chain Z). Prediction: both <= 0.0012 on every nd row -> (ii) fails c1 by a factor >= 3.
CANDIDATE (iii) "same object as the 5d 0.013 flat": test from record — is the 0.013 (chain Z, delivered 0.61 of required) the SAME row-set and sign as the
0.005 (chain R/S, delivered 0.85)? Prediction: yes (Y/La/Lu/Cs, one sign, 0.013 -> 0.005 by the ring gain): (iii) is not a separate home; it is the object's history.
Tool: pack33/cand_i.py -> cand_i.jsonl (append, done-set, <= 3 rows/call). Timing flags: none on this file.