# BRIDGE — THE LÖWDIN SESSION 34 (2026-08-17)
Successor to BRIDGE-LOWDIN-SESSION-33.md. Bank restore-point-2_13 (R 1700) UNCHANGED; nothing written to register/index/store. HANDOFF-33 verified 716/716;
gates 1-57 PASSED at open (GATES-33-OPEN.log, block-diffed against pack33's log: 51 exact, 6/16/52 differ only in timing/duplicate blocks); byte census
clean at open (CENSUS-SESSION-34-OPEN.txt) and at close. §H.10: handoff begun at ~75 %.
## 1 · Rulings (M, s34)
(1) "B first, then A" — bridge-33 §3(1) order. (2) "(i)" — build the second-order entrant-core pair correlation once and run the six class rows and Yb.
GENERAL carried: SUBCELL=1; predictions before runs; R 1449 timing flags; comparison decides; no scans; no constant; residue is not closure (s33 (6)); T4 LAST.
## 2 · Findings (pack34; no constant beyond c; Cs/Y RECALLED-NOT-ENTERED; bench and He second order RECALLED comparison only)
(1) FINDING-B: DE_J^S - eps_S(1/2) = Sc -0.0166 · Y -0.0109 · La -0.0095 · Gd -0.0104 · Lu -0.0099 · Cs -0.0030 (54 SCFs, janak_S.py); the same-functional DSCF is
    DEEPER than TS on every row -> "missing relaxation" REFUSED ON SIGN (E path at DSCF would be over by 0.016-0.020 nd, 0.049 Sc). NEW: both paths at DSCF
    under one correlation S, the exchange-treatment seam O-E = Sc +0.045 · Y +0.025 · La +0.018 · Gd +0.015 · Lu +0.023 · Cs +0.015; T inside on every row
    but Sc. Seam's home by elimination: entrant exchange (LSD+PZ-SIC vs HF). PB-1..3 held. F34.1.
(2) FINDING-A: (a1)/(a2) VOID from record. rz_mech_S: S is DEEPER than the recalled UEG bench in 1<=r_s<=10 on all six rows (+0.0013..+0.0028, class-flat;
    R of record was short) -> an exact-UEG local form moves the diffuse rows SHORTER: Sc -0.0027 · Gd +0.0023 · La +0.0036 · Lu +0.0060 · Y +0.0070 · Cs +0.0102,
    still monotone in rs_w. PA-1/PA-2 FAILED on sign, PA-3 partly. Reading: a shortfall growing with diffuseness under EVERY local form = nonlocal entrant-core
    correlation (s29 corepol: adiabatic form admissible on Cs, not on d). Sc anomaly of R 1887 is a delivered-FRACTION statement; absolute <= 0.003. F34.2.
(3) FINDING-MP2ENT: mp2_ent.py built (log-mesh box spectrum, LS-coupled pairs, l<=3, r_min 1e-3/Z; He gate -0.0490 vs RECALLED HF -0.0374, reported).
    E2_ent: Sc -0.0652 · Y -0.0631 · Gd -0.0554 · La -0.0626 (175 neg-den pairs excluded: local 4f collapse) · Lu -0.0666 · Cs -0.0240 · Yb -0.1786 (siblings 63 %).
    PN-1 FAILED (d rows FLAT at second order); PN-2 HELD: undelivered fraction 1-|DEc|/|E2| = Sc 0.51 · Y 0.56 · Gd 0.56 · La 0.58 · Lu 0.59 · Cs 0.71 ranks with
    resid_O; PN-3 NOT RUN (radial partition owed); PN-4 HELD (Yb sibling term = horizon (3)'s derivable object, 0.11 vs the 0.09 shortfall, bound). F34.3 (the
    O-path class row is R on five rows, S on Gd only — frachf_S owed on Sc/Y/La/Lu/Cs), F34.4 (two eigensolver forms refused for conditioning; RMIN bound).
Failed predictions s34: PA-1, PA-2, PA-3, PN-1. Timing flags: F34.1, F34.2. Record flags: F34.3. Faults closed: F34.4.
## 3 · Next chat, in order (rulings first; predictions before runs) — under (6): CLOSE, do not state
(1) RULING NEEDED — the exchange seam O_DSCF - E_DSCF (0.015-0.025 nd/6s, 0.045 Sc; one correlation form; T inside on 5 of 6 rows): candidates to CLOSE it
    (a) the PZ-SIC one-orbital exchange on the entrant vs the exact-exchange hole (SIC over-binds the compact entrant): testable as E_x^HF[entrant] -
    E_x^LSD-SIC[entrant] on the same orbital, one number/row, class ratio; (b) local exchange of the CORE response to the hole (relaxation seam) — E-path
    frozen-vs-relaxed at DSCF. Both derivable, no constant. (2) FIRST, cheap, OWED: frachf_S on Sc/Y/La/Lu/Cs (F34.3) so the O-path class row is one form.
(3) A: the nonlocal-correlation candidate now has machinery: implement PN-3 (radial partition of E2_ent by entrant r) and the ion-relaxation subtraction
    (E2 of the ion's own pairs, N-1 electrons) so that DELTA E2 (removal, second order) is one number/row; compare its class shape and size with resid_O.
    Bound in advance: frozen second order on local orbitals overestimates ~x1.3 (He gate). (4) 4f +0.09 via Yb: sibling second-order term (2/14)E2(4f,4f) = 0.112
    lower bound at l<=3 — the derivable object for horizon (3); run LMAX=4/5 convergence and the ion-relaxation subtraction before reading. (5) SPEC-WALK-SESSION-32.
(6) Fe/Ni conditional. (7) Law statement ONLY after (1) and A close. (8) T4 writing chat LAST: R 1701-1911 + s34 R 1912-1926 (listed in the three findings).
## 4 · Figures (§H.6): MEASURED none entered. RECALLED-NOT-ENTERED: Cs 0.14310, Y 0.2285; QMC/PW92 bench; He second order -0.0374 (HF orbitals). CHOSEN:
LMAX 3, ECUT 300, r_min 1e-3/Z, r_max 60, 700 pts (numerical bounds, stated); f-grid of janak_S (inherited from janak_table). DERIVED: everything else.
## 5 · Files (pack34): PREDICTION-{B,A,MP2ENT} · FINDING-{B,A,MP2ENT} · TABLE-{B,A,MP2ENT}-SESSION-34.txt · t7c_cuaudit_S.py · janak_S.py/.jsonl · table_B.py ·
rz_mech_S.py/.jsonl · mp2_ent.py/.jsonl · gates_run.sh (54-60 added) · GATES-33-OPEN.log · CENSUS-SESSION-34-{OPEN,CLOSE}.txt · README-34 · this bridge.
## 6 · Unread / owed: unchanged (R 1668; Dabo 2010, Borghi 2014; 2603.23283; Gruneis-Kresse 2009 / Ren 2013). Owed: T4 (R 1701-1926); PR3; the walk test;
frachf_S x5 (F34.3); PN-3. Census loop as bridge-33 §6. Container: rt/ beside the packs; rt/ holds nothing outside the packs except __pycache__, .so, gate-regenerated
derive_P*.json, out/, and GATES-33-OPEN.log/cmpgates.py (session scratch, packed).