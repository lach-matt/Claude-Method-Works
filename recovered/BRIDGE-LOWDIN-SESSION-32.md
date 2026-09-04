# BRIDGE — THE LÖWDIN SESSION 32 (2026-08-17)
Successor to BRIDGE-LOWDIN-SESSION-31.md. Bank restore-point-2_13 (R 1700) UNCHANGED; nothing written to register/index/store. HANDOFF-31 verified 656/656;
gates 1-48 PASSED at open (pack32/GATES-1-48-SESSION-32-OPEN.log). §H.10: handoff begun at ~78 %, no running task left open.
## 1 · Rulings (M, s32)
(1) The two owed additions (s31 close): eps_L named Maxwell's eps of the medium in SPEC-SOSEX (§A1); f-sum + compressibility sum rules as gates (§A2) ->
done, certified (FINDING-SUMRULES). (2) "Continue where we left off" -> bridge-31 §3 (1) opened: candidate S built end to end (PREDICTION-SOSEX first).
GENERAL carried: SUBCELL=1; predictions before runs; R 1449 timing flags; comparison decides; no scans; no constant; T4 writing chat LAST.
## 2 · Findings (pack32; no constant beyond c; Cs/Y RECALLED-NOT-ENTERED; QMC bench RECALLED, comparison only)
(1) FINDING-SUMRULES: on the chain's own Lindhard g: g(q,nu->inf) -> (2/3)q^2/nu^2 (f-sum: K^2X^2 Pi -> 4 al rs/(3pi), zeta-independent) and g(0,0) -> 2
    (compressibility: K^2 Pi(K,0) -> 2 al rs (x_up+x_dn)/pi; zeta1/zeta0 = 2^(1/3)/2). Both derived first, both PASS to 1e-4/1e-7; lam-linear; sumrule_gates.py.
(2) FINDING-SOSEX: candidate S = ring/2 + coupling-averaged statically-screened SOX built by the pair-density reduction (g_2b(q~) once; table by re-weighting).
    G-S1 (∫g_2b = E0B +1.5e-5, zeta 0 & 1), G-S2, G-S3 (MC z <= 1) PASS. PS-1 HELD (ratio 0.675 at (2,0)); PS-2a HELD; PS-2b FAILED (zeta 1 screens LESS:
    N(E_F) 2^(-2/3), momenta 2^(1/3)); PS-3 HELD (|S - bench| <= 0.0018 on rs 1..5: R's underbinding was the vacuum exchange line); PS-4 FAILED: 15 rows
    corr='S' move <= 0.001 from R (Cr +0.0019); the d-row object is NOT closed; class ratios stay at R's.
    THE MECHANISM (F32.2 diagnostic): the PZ SIC of correlation subtracts the one-orbital (zeta=1) form; the local S-R on Y is -0.0081 total vs -0.0073
    one-orbital -> net -0.0008 = SCF. SIC-CANCELLATION LAW: Delta_ent ≈ <Delta eps_c(n_tot,zeta_tot)> - <Delta eps_c(n_ent,1)>; a spin-flat form change
    cannot move the entrant. COROLLARY: the d-row object (0.004-0.006 nd>=4) must be spin-DIFFERENTIAL correlation (~0.005 Ha of zeta-dependence at
    rs ~ 2 beyond the ring's) or lie outside local correlation. RZMECH's "missing screened exchange" WITHDRAWN; its trigger and one-mechanism stand.
    COMPARE-RZS: S admissible, the correct derived local form, carried as the chain form; NOT decisive against R on the rows.
(3) FAULT-F32.1: F18.1-shape recurred DURING the session (branch files in pack32/ and rt/, and an IN-PLACE edit of rt/t7c_corrz.py that a name census
    cannot see). Quarantined to pack32/foreign/, pack31 copy restored, hook re-made by this thread; census is now BYTE-LEVEL (README-32 Known).
Failed predictions s32: PS-2b · PS-4. Timing flags: F32.2. Numerical fix before any read: P_perp^2 grid -> ln(w_q^2+v) grid (was 1 % low on g_2b).
## 3 · Next chat, in order (rulings first; predictions before runs)
(1) RULING NEEDED: carry S as chain form (this bridge's recommendation) or hold R — the rows do not distinguish; the law statement's correlation clause
    depends on it. (2) The spin-differential question (from the corollary): compute, prediction first, the entrant-weighted zeta-differential
    D = <eps_c^bench(n_ent,1) - eps_c^S(n_ent,1)> - <eps_c^bench(n_tot,z_tot) - eps_c^S(n_tot,z_tot)> on Y/La/Gd/Lu vs 3d/4f (RECALLED bench, comparison
    only): if D ~ 0.004-0.006 on nd>=4 and small on 3d/4f, the d-row object is the zeta-dependence of eps_c at rs ~ 2 — one table, one tool call/row.
    (3) SPEC-WALK-SESSION-32 (unchanged, gated behind (1)). (4) 4f +0.09 via Yb (second radial function) under S. (5) Fe/Ni term-resolved conditional.
(6) Law statement (bridge-31 §3(5) text) with the correlation clause reading "ring + medium-screened exchange, SIC'd" and the three-trunk spine.
(7) T4 writing chat LAST: R 1701-1890 + s32: R 1891 sum-rule gates (Maxwell's eps named) · R 1892 SOSEX built, G-S1..3 · R 1893 PS-2b (one sphere screens
    less) · R 1894 PS-3 (S closes the UEG bench) · R 1895 PS-4 + SIC-cancellation law · R 1896 RZMECH inference withdrawn · R 1897 F32.1 (byte census).
## 4 · Figures (§H.6): MEASURED none entered. RECALLED-NOT-ENTERED: Cs 0.14310, Y 0.2285; QMC eps_c bench (comparison). CHOSEN: grids (NZ,NU,NPP,NPV)=
(80,80,64,128), q~ 1e-3..40 x100, MC 8e6/Gamma(3,1); tolerances G-S1 1e-4, G-S4 1e-3, G-S5 1e-4. DERIVED: g(q,inf) 2q^2/3nu^2, g(0,0)=2, S(Pi) closed form,
prefactor 3/(16pi^5) confirmed by E0B, g_2b(q~) table, eps_2x^scr table, SIC-cancellation law.
## 5 · Files (pack32): SPEC-SOSEX-32 (superseding) · PREDICTION-SOSEX · FINDING-{SUMRULES,SOSEX} · FAULT-F32.1 · sumrule_gates.py · sox_qres.py/.jsonl ·
sox_table.py/.json · sox_mc.py · sox_bench_compare.json · corr_sosex.py · t7c_corrz.py · t7c_corrRZ_run.py · t7c_corrS.jsonl · GATES log · foreign/ · this bridge · README-32.
## 6 · Unread / owed: unchanged (R 1668; Dabo 2010, Borghi 2014; 2603.23283; Gruneis-Kresse 2009 / Ren 2013). Owed: T4 (R 1701-1897); PR3 (A/B/R under R);
the walk test; the spin-differential table (3(2)).
Container: rt/ beside the packs; rt/ holds nothing outside the packs except __pycache__, the .so files and gate-regenerated derive_P*.json (byte census).