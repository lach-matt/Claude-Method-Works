# PREDICTION — item (2)(a'), s26: like-for-like test of the DE_J residual. Ruling: "do the build". Written BEFORE any run.
CORRECTION to FINDING-XFOCK: gate 13's banked entrant (Sc -0.2686, La -0.2017) is mode 'hfs' = Hartree-Fock-SLATER (local unpolarised X-alpha,
no SIC), not exact HF. The like-for-like object is t7c_hfsr.HFSR(...).run('hf'): scalar-relativistic exact-exchange HF, average of configuration,
entrant at f=1/2 (Slater TS). No constant beyond c=137.035999 (in force).
Build: eps_HF(1/2) from HFSR 'hf'; chain-Z correlation added at FIRST ORDER on the HF orbitals: Delta_c = <n_ent| v_c[n_u,n_d] - v_c^SIC[f n_ent] >
(v_gbz of t7c_cuaudit, LAM1 off, the standing chain-Z correlation with its PZ SIC), spin densities: closed shells split evenly, entrant f=1/2 in
spin up, open siblings all spin up (Hund). Rows: the s/d class where average-of-configuration HF is exact or nearly so: Cs Y La Gd Lu Sc, then
Ti..Cu, 4f only if time permits (siblings make HF-avg differ from the chain's spin-polarised object: caveat stated). resid_HFc = eps_HF + Delta_c - meas,
meas RECALLED via TABLE-JANAK-24 (chain - resid_TS). Files: hfcorr.py, hfcorr.jsonl, TABLE-HFCORR-SESSION-26.txt.
PB1 eps_HF(1/2) is SHALLOWER than chain-Z eps(1/2) on all rows (HF has no correlation; SIC-LSD-Z has it): eps_HF - eps_Z in [+0.01,+0.06] on Sc, La.
PB2 Delta_c < 0 on all rows, |Delta_c| in [0.010, 0.035] on Sc..Lu (chain-Z x-only vs Z references differ by -0.0245 Sc, -0.0169 La: same order).
PB3 (the (a') claim) |resid_HFc| <= 0.015 on Sc and La at TS level.
PB4 resid_HFc has SMALLER mean |.| than resid_J over the s/d rows {Y La Gd Lu Sc}: mean|resid_J| there is 0.0169; predict mean|resid_HFc| <= 0.012.
PB5 The HFS banked value is NOT reproduced by 'hf' mode: |eps_hf - eps_hfs| > 0.02 on Sc (they are different functionals).
If PB3 and PB4 hold, item (2)'s residual is exchange-functional over-binding (SIC-LSD vs exact exchange at the RELAXED TS level) and (a') beats (b);
if they fail, (b) stands with (a') tested and on record.