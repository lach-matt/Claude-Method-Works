# PREDICTION — item (1), s26: is the frozen ratio 1.15 derivable? Written BEFORE any run (2026-08-16). Ruling: "continue in order".
Object: mask_fr = DE_J^fr − eps_fr(1/2), s25 frozen scan (chain Z and x-only), 7-pt f grid, f^(1/3) interpolation as janak_table.py.
Method (no constant, no measured input): on the frozen reference densities, every f-dependent term T of the potential has an exact
frozen-orbital derivative dT/df = <n_ent | v_T(f)>, so each term has a MIDPOINT DEFECT M_T = int_0^1 <n_ent|v_T(f)>df − <n_ent|v_T(1/2)>.
Terms: V_H (linear in f -> M=0 exact), V_x[n_sigma0+f n_ent] (M_xtot), V_c[chain Z] (M_ctot), SIC −v_H[f n_ent] (M=0 exact),
SIC −v_x[f n_ent] (M_xsic: closed form 0.0583 E_x[n_ent], 0.0583=(4/3)2^(−1/3)−1), SIC −v_c[f n_ent] (M_csic).
M_exp = sum of M_T (evaluated on the SAME 7-pt grid + interpolation, and on a fine grid). The scan differs from M_exp only by the
entrant orbital's own response to V(f): M_resp = mask_fr − M_exp. Nothing here is fitted; every piece is an integral of the reference SCF.
Files: frozen_split.py, frozen_split.jsonl (chain Z and none), TABLE-FROZEN-SPLIT-SESSION-26.txt. frozen_scan3 CORR=none run on the 13 rows lacking it.
## Predictions
P26.0 (gate) fine-grid M_xsic == 0.0583*E_x[n_ent] to 1e-4 Ha on all 15 rows; 7-pt-grid M_xsic within 3e-4 of it (interpolation error).
P26.1 M_resp < 0 on all 15 rows in BOTH chains (Rayleigh–Ritz: eps_fr(f) <= <psi_ref|H_f|psi_ref>, equality at f=1/2). |M_resp| in ratio
       units [M/(−0.0583|E_x|)] lies in [0.02, 0.12] on the 14 non-Cs rows.
P26.2 x-only chain: (M_xtot + M_resp)/(−0.0583|E_x|) in [0.03, 0.15] on all 14 non-Cs rows; Sc, Yb reproduce PF8's 1.09/1.07 total to ±0.01.
P26.3 chain Z: (M_ctot + M_csic)/(−0.0583|E_x|) in [0.03, 0.12] on the 14 non-Cs rows, and its sign is NEGATIVE (correlation deepens the mask).
P26.4 (derived-form test) |M_resp / mask_fr| <= 0.15 on the 14 non-Cs rows in chain Z: i.e. >=85% of the frozen mask is the exact
       functional midpoint defect on the reference densities, computable WITHOUT any f-scan.
P26.5 (scaling test) In ratio units the correlation part (P26.3) has spread (max−min) <= 0.05 across the 14 rows, i.e. it scales with
       |E_x[n_ent]| at least as tightly as the total ratio did (0.07 spread); against 1/rmean the spread of M_c*rmean is larger.
P26.6 The 3d row trend Sc->Cu (mask_fr/|E_x| ratio 1.14->1.19 in s25) is carried by M_resp, not by M_xtot or the correlation part.
Failure of any of these is recorded, not repaired in place. Cs (mask 0.0025, ratio 0.60) is reported but excluded from the ranges.
