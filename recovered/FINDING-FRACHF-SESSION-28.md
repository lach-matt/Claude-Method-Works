# FINDING — F26.2 LIFTED; the fully combined function built: self-consistent exact-exchange + chain-Z correlation along the entrant's fractional
# occupation, entrant as ONE spin-orbital. Tested on Y and Gd (Cs, Sc, La, Lu not run: budget).  s28. Files: PREDICTION-FRACHF-SESSION-28.md (first),
# t7b_hf.py (frac / _ceff), hfc2.py (same in run2; default byte-identical: gates 5, 26, 30 rerun PASS), frachf.py, frachf.jsonl. No constant beyond c.
## The lift (derived): own-shell pair factor (Q-1) -> c_eff = [q_c(q_c-1) + 2 f q_c]/(q_c+f); a single spin-orbital has no self-pair. Reduces to (Q-1)
at f = 0, 1 (all banked integer results untouched). Janak exact iff q_c = 0 (every class row) or f = 1. First diagnostic (HFSR.run, Y, HF only):
eps_4d(1/2) = -0.1937 against Delta-SCF 0.1956 — F26.2's -0.553-type value is gone (PF0 second half HELD). PZ SIC of the entrant at f n_e.
## Results (SUBCELL=1; f = 0, 1/4, 1/2, 3/4, 1; eps(0) linearly extrapolated from 1/4 and 1/2 for the Simpson integral, stated)
PF0 HELD: f = 0/1 endpoints reproduce hfc2 obj_2 (Y -0.215395/-0.21539; Gd -0.208219/-0.20822) and Ec_ion-Ec_neu (Y -0.020192/0.02019, Gd -0.017207/0.01721).
PF1 HELD (Janak): [E(1)-E(0)] - Simpson[eps] = -0.0006 (Y corr) / -0.0004 (Y HF) / -0.0005 (Gd corr) / -0.0002 (Gd HF): the path IS one function.
PF2 HELD: on the self-consistent path, correlation integer minus correlation midpoint = -0.0008 (Y), -0.0009 (Gd) — curvature order, same as the
    frozen path (-0.0007, -0.0008). The 0.008 of s26-vs-s27 is now placed BEYOND DOUBT: it is between the two orbital sets, inside neither form.
PF3 FAILED narrowly: -eps^corr(1/2) - obj_2 = 0.0023 (Y), 0.0021 (Gd) against the stated 0.002 — the TS midpoint of the total (HF+corr) function
    over-binds the sc integer by ~0.002 = the HF-path curvature (0.0018/0.0016: eps^HF(1/2) vs D_HF) plus the correlation curvature.
## What stands. THE LAW'S CORRELATION TERM IS ONE FUNCTION: I = int_0^1 eps_ent(f) df on the self-consistent exact-exchange + chain-correlation path,
= E(0)-E(1) exactly (Janak, verified), = -eps(1/2) + curvature (~0.002, derived, both pieces small and of one sign). Midpoint and integer forms are its
one-point quadrature and its exact value; the frozen-orbital form is its first-order approximant in the orbital response. So the class-row margin,
stated in the one function: Y  -eps(1/2) = 0.2131, exact 0.2154 (RECALLED-NOT-ENTERED Y 0.2285: shortfall 0.013 as s27 read); Gd 0.2062 / 0.2082.
The 0.013 is real under the one function; the s26 <= 0.009 was the frozen-orbital approximant. Not a closure. No constant chosen or proposed.
Failed predictions: PF3 (by 0.0003/0.0001). Timing flags: none — F26.2's mechanism and the lift preceded the run; the first frachf run (through the
unlifted hfc2.run2, Janak gap 0.19) was a build error found by the Janak gate and fixed before any reading; on record.
Open: 3d/4f rows need a second radial function for the entrant (q_c >= 1) before their fractional path is exact; Cs/Sc/La/Lu class rows unrun.
