# PREDICTION — (a') table restated on the ONE function for the four unrun class rows Cs Sc La Lu.  s29. Written BEFORE any run.
Rulings in force: SUBCELL=1 standing (s29); the law's correlation term = I = int_0^1 eps_ent(f) df on the self-consistent HF + chain-Z path (s28).
Runs: python3 frachf.py 55 21 (batch 1), python3 frachf.py 57 71 (batch 2); budget 400 s per batch; no scan; predictions from Y/Gd rows and s26 hfdscf.
PA0 (gate) Cs f=0/1 endpoints reproduce hfc2 obj_2 -0.13013 and D_HF 0.12769 to 1e-4; Sc/La/Lu HF path D_HF reproduce s26 hfdscf D_HF (0.2666, 0.2059, 0.1598) to 1e-3.
PA1 (Janak) |[E(1)-E(0)] - Simpson eps| <= 6e-4 corr and <= 4e-4 HF on every row (Y/Gd max 6.1e-4 / 3.9e-4).
PA2 gap_sc = [Ec(1)-Ec(0)] - Delta_c^sc(1/2) in [-0.0012, 0] on the d rows Sc La Lu; |gap_sc| <= 2e-4 on Cs (frozen path gave +1e-5).
PA3 curvature: -eps^corr(1/2) - I in [0.0015, 0.0030] on Sc La Lu (Y 0.0023, Gd 0.0021); on Cs <= 0.0010.
PA4 (a') margins: I falls short of the banked meas column by 0.010-0.016 on La (meas 0.2386) and Lu (0.1994) — the frozen-orbital form's ~0.008
    relaxation of E_c^SIC is present on every d row; Cs stays at ~0.013 short (0.130 vs 0.14310 RECALLED; relaxation on Cs is 7e-4, no change);
    Sc: s26 frozen over-bound by 0.008 (0.3027 vs 0.2946); relaxation removes ~0.008 of correlation, so I(Sc) in [0.290, 0.298], i.e. Sc lands
    within 0.005 of meas — the only class row that does.
Stop rule: two batches, no rerun; a failed prediction is reported with mechanism, not repaired in-session.
