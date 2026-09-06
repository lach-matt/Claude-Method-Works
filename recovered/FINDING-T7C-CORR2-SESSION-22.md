# FINDING — T7c-CORR2: 4a repair (F22.1) and GB exact constants, gated and probed on La (session 22, budget-limited).
Files: t7c_corr2.py (t7c_corr + env switches SIC_NOCLAMP / GB_EXACT; both off = banked behaviour), t7c_corr2.jsonl, PREDICTION-T7C-CORR2, FAULT-F22_1.
PR1 HELD EXACTLY: H 1s half-occupied, SIC on, no clamp: eps -0.50001 for corr None AND corr P (was -0.533 / 0.0014 residual). PZ-81 exactness of
orbital SIC on one electron is recovered; the tail-clamp asymmetry (bridge-21 s3(4a)) was the clamp, as the established math said.
PR2 FAILED by 1e-4: La 5d sr_sic no-clamp -0.2161 vs banked -0.2202 (+0.0041 > 0.004). The clamp was BINDING the SIC'd 5d entrant by 0.004:
the double asymptote deepens. Consequence: every SIC/GB row is ~0.004 (5d) shallower once repaired -> the 5d residual grows from +0.014 to ~+0.018;
regeneration of the 15-row table under the repair is OWED (bridge-22 s3(1)).
PR3 FAILED (smaller than predicted): exact constants move U by +0.0002, P by +0.0003 (predicted +0.0008..+0.0015): the PZ orbital SIC of v_c
removes most of a constant shift in eps_c. Attribution refinement stands; numerically immaterial (<= 3e-4).
Faults: F22.1 registered and repaired in the new object. Predictions failed: PR2 (1e-4 over), PR3 (magnitude). No constant, no measured input.