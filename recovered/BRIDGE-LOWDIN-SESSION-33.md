# BRIDGE — THE LÖWDIN SESSION 33 (2026-08-17)
Successor to BRIDGE-LOWDIN-SESSION-32.md. Bank restore-point-2_13 (R 1700) UNCHANGED; nothing written to register/index/store. HANDOFF-32 verified 686/686;
gates 1-53 PASSED at open (pack33/GATES-1-53-SESSION-33.log), 1/16/52 re-run at close; byte census clean at open, twice mid-session, and at close. §H.10: handoff begun at ~87 %.
## 1 · Rulings (M, s33)
(1) "Carry S" -> S is the chain correlation form; R comparison only. (2) "Open the table" -> bridge-32 §3(2) D-table run. (3) Test (a) [trunk closed at S; d-row
0.005 a stated non-local residual] against candidates (i) inhomogeneity (ii) SIC-line defect (iii) 5d-0.013 identity. (4) Open (iv) eigenvalue/observable seam
and (v) frachf convention against (a). (5) The Gd exchange seam first, then hand off. GENERAL carried: SUBCELL=1; predictions before runs; R 1449 timing flags;
comparison decides; no scans; no constant; T4 writing chat LAST.
## 2 · Findings (pack33; no constant beyond c; Cs/Y RECALLED-NOT-ENTERED; bench RECALLED comparison only)
(1) FINDING-DZETA: D = A - B (bench-vs-S on the SIC one-orbital line minus the total line, entrant-weighted) = -0.0029 (lin-z) / -0.0016 (f(zeta)) on Y/La/Gd/Lu, one
    number; PD-1 FAILED ON SIGN (bench-ward zeta-differential SHALLOWS the entrant); |D| <= 0.003 bound. First horn of the bridge-32 corollary refused. F33.1 (fx column).
    CORRECTION (FINDING-CAND): the chain SICs f*n_i, f=1/2 on the entrant -> A_half = -0.0008; every clause unchanged.
(2) FINDING-CAND: (i) PBE-form gradient term on the chain's own eps_S (gamma derived, beta Ma-Brueckner RECALLED): Delta_i = +0.012..+0.016 on ALL 15 rows,
    class-flat, wrong sign, x3 — refused (P-i-1..3 all failed: t^2 grows with diffuseness, H saturates). (ii) refused by three bounds <= 0.001. (iii) resolved from
    record: the 0.013 (chain Z, delivered 0.61) IS the 0.005 (R/S, 0.85) — history, not a home. NEW BOUND: any GGA-form correction shifts every class shallower 0.010-0.016.
(3) FINDING-SEAM (F33.2): (v) g_v = TS-midpoint minus endpoint DEc = +0.0007..0.0010 class rows, one sign, scales with |DEc| — refused. (iv) the E path (local-
    exchange TS eigenvalue, S) is OVER on every row (Sc -0.032, Y -0.009, La -0.007, Gd -0.005, Lu -0.009, Cs -0.0035) while the O path (frachf R) is SHORT (Y +0.005,
    La +0.002, Lu +0.004, Cs +0.008; Sc -0.004): seam 0.009-0.014 nd, 0.028 Sc — a SECOND, class-resolved object; T lies BETWEEN the paths on every non-3d row.
    The d-row object is neither the seam nor its midpoint (off 0.003 on La/Lu) — refused as home. Five candidates run: (a) STANDS.
(4) FINDING-GDSEAM: Gd 4f7(8S)5d 9D-vs-average exchange seam = +0.01908 (hfterm machinery; D_avg == frachf D_HF); frozen-orbital closed form 1/2 sum G^k Q_k =
    0.02159 (PG-2 failed by 0.0025 = 4f relaxation, 12 %). Applied to the O path Gd goes from +0.016 above the class to ~ -0.001 (R/S): the observable-path class
    row is Sc -0.004 · Gd ~-0.001 · La +0.002 · Lu +0.004 · Y +0.005 (Cs +0.008): a SPREAD of 0.009 with a sign change inside the class. Seam does not apply to E path.
Failed predictions s33: PD-1 (sign), PD-3, fx-magnitude clause (compact rows), P-i-1, P-i-2, P-i-3, P-v-1 magnitude, PG-2. Timing flags: F33.1, F33.2.
## 3 · Next chat, in order (rulings first; predictions before runs)
(1) RULING NEEDED: accept (a) as closed after five candidates — the law statement's correlation clause reads "ring + medium-screened exchange, SIC'd (S)", with TWO
    stated residual objects: the observable-path class spread (-0.004..+0.005, sign change; Cs +0.008) and the eigenvalue seam (E over by 0.005-0.009 nd, 0.032 Sc).
(2) RULING NEEDED: is the E-vs-O bracketing of T (every non-3d row) a finding for the law statement (the observable lies between the local TS eigenvalue and the
    exact-exchange DSCF + local correlation) or a coincidence to be tested — test: Gd on the O path under S (frachf_ring with FORM=S, one row, ~90 s), predicted ~ -0.001.
(3) SPEC-WALK-SESSION-32 (ungated since (1) of bridge-32). (4) 4f +0.09 via Yb (second radial function) under S. (5) Fe/Ni term-resolved conditional.
(6) Law statement (bridge-31 §3(5) text + this bridge's (1)). (7) T4 writing chat LAST: R 1701-1897 + s33: R 1898 D-table · R 1899 (i)-(iii) refused, (a) stands ·
    R 1900 uniform GGA-shift bound · R 1901 A_half correction · R 1902 (v) refused · R 1903 (iv) refused, seam = second object, T bracketed · R 1904 Gd seam named ·
    R 1905 F33.2 · R 1906 Gd seam +0.019 / 0.0216 closed form · R 1907 class row is a spread with sign change · R 1908 F33.1.
## 4 · Figures (§H.6): MEASURED none entered. RECALLED-NOT-ENTERED: Cs 0.14310, Y 0.2285; QMC/PW92 bench (rz_mech B0/B1); beta = 0.066725 Ma-Brueckner (comparison
only). CHOSEN: windows 1<=r_s<=10 (bench anchors), f(zeta) spin-scaling as sensitivity form, criteria c1-c3 (from the record's residual sizes). DERIVED: D, A_half,
Delta_i (H form with gamma=(1-ln2)/pi^2), g_v, seam tables, Gd seam and its closed form (Q_k = 7(2 k 3;000)^2).
## 5 · Files (pack33): PREDICTION-{DZETA,CAND,SEAM,GDSEAM} · FINDING-{DZETA,CAND,SEAM,GDSEAM} · TABLE-{DZETA,CAND,SEAM} · dzeta.py/.jsonl/dzeta_fx.jsonl ·
cand_i.py/.jsonl · gd_seam.py/.json · gates_run.sh · GATES-1-53-SESSION-33.log · CENSUS-SESSION-33.txt · README-33 · this bridge.
## 6 · Unread / owed: unchanged (R 1668; Dabo 2010, Borghi 2014; 2603.23283; Gruneis-Kresse 2009 / Ren 2013). Owed: T4 (R 1701-1908); PR3; the walk test; Gd-under-S row (3(2)).
Census loop used (byte-level, to a file): for f in rt/* (excluding __pycache__, *.so, derive_P*.json, out/): cmp against every pack copy; a file matching none is FOREIGN.
Container: rt/ beside the packs; rt/ holds nothing outside the packs except __pycache__, the .so files, gate-regenerated derive_P*.json and out/ (pack5 dir).