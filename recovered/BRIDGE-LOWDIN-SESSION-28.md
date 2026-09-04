# BRIDGE — THE LÖWDIN SESSION 28 (2026-08-17)
Successor to BRIDGE-LOWDIN-SESSION-27.md. Bank restore-point-2_13 (R 1700) UNCHANGED; nothing written to register/index/store.
Archive verified at open: HANDOFF-27 552/552. Gates 1-31 PASSED at open. §H.10: handoff begun at ~85%.
## 1 · Rulings (M, s28)
(1) F24.1/F25.1 -> ruling D: "define the mechanism mathematically and work it into the solution, then test." (2) correlation form -> "the gap may be
where the answer is; midpoint slightly better; do not state both — combine both into ONE mathematical function." Then "Option (i): lift F26.2 and build."
GENERAL carried: predictions before runs; R 1449 timing flags; comparison decides; no scans; T4 writing chat LAST.
## 2 · Findings (no constant beyond c; no measured input; Cs/Y meas RECALLED-NOT-ENTERED) — files in pack28
(1) F24.1 = F25.1 CLOSED (FINDING-CELLCUT). Mechanism derived: e_c = n·min(eps_c,0) is C0 not C1; v_c jumps by lam0(zeta)/3 at the derived
    crossing r_s* (lam0(1)/3 = 0.005182 == observed Ti/Cu steps, PD0). Nodal theta quantises the step; discrete map has no fixed point. Repair worked
    in: finite-volume in-cell fraction of eps_c<0 (cellcut.py, env SUBCELL=1; unset == s27 exactly). PD0-PD6 all HELD: Ti it 100->34, Cu 100->33,
    all 15 rows converged, max|dE| 2e-5. Recommend SUBCELL=1 as standing convention.
(2) ONE FUNCTION (FINDING-ONEFUNC): E_c(f) on frozen neutral HF orbitals; midpoint == E_c'(1/2) == s26 Delta_c (3e-5); integer == E_c(1)-E_c(0);
    their gap on one function = (1/24)E_c''' ~ 0.001, mostly closed-form (lam0(1)/3)(ln2-1/2)N_e^- (correlation twin of the s25 f^(4/3) law).
    PQ1/PQ2 FAILED (timing flag): the s26/s27 0.008 is NOT curvature — it is first-order orbital relaxation of E_c^SIC (HF orbitals stationary for
    E_HF, not for E_c). Two evaluations of one function on two orbital sets.
(3) F26.2 LIFTED (FINDING-FRACHF): own-shell pair factor c_eff = [q_c(q_c-1)+2 f q_c]/(q_c+f) in t7b_hf/hfc2 (frac; default identical, gates 5,26,30
    rerun PASS). Self-consistent HF+corr fractional path built (frachf.py). Y, Gd: Janak gap <= 6e-4 (PF1), corr midpoint-vs-integer on the sc path
    -0.0008/-0.0009 (PF2), endpoints == hfc2 (PF0). PF3 failed by 0.0003: -eps(1/2) over-binds the exact integral by 0.002 (HF+corr curvature).
    THE LAW'S TERM IS ONE FUNCTION: I = int_0^1 eps_ent(f) df = E(0)-E(1) = -eps(1/2) + derived curvature. Class-row margin in the one function:
    Y 0.2154 (meas 0.2285, RECALLED), Gd 0.2082 — the ~0.013 shortfall is real; s26's <= 0.009 was the frozen-orbital approximant. Not a closure.
STANDING: not a closure. F24.1/F25.1 closed. F26.2 lifted for class rows (q_c = 0); 3d/4f fractional path needs a second radial function (build).
Failed predictions s28: PQ1, PQ2, PF3 (narrow). Timing flags: PQ1 relaxation reading; frachf first run through unlifted run2 (build error, fixed).
## 3 · Next chat, in order (rulings first; predictions before runs)
(1) Ruling: adopt SUBCELL=1 as standing convention (README-28 gates 32-33). (2) Ruling: the law's correlation term stated as the one function
    I = int eps(f) df on the sc path — then restate the s26 (a') table for all six class rows (Cs Sc La Lu unrun; ~90-130 s each; batches <= 2).
(3) The 4f +0.09 as ONE object via Yb (bridge-27 s3(3)) — now with the one-function machinery: needs the second-radial-function build for q_c >= 1
    first (prediction first). (4) Term-resolved SCF Fe/Ni conditional. (5) T4 writing chat LAST: R 1701-1868 + s28: R 1869 F24.1/F25.1 mechanism+
    closure · R 1870 one-function + curvature law + relaxation reading · R 1871 F26.2 lift + Janak-verified path · R 1872 failed predictions s28.
## 4 · Figures (§H.6): MEASURED none entered. RECALLED-NOT-ENTERED Cs 0.14310, Y 0.2285. CHOSEN: prediction thresholds; npts 4000 inherited; eps(0)
linear extrapolation in the Simpson integral (stated). DERIVED: lam0/3 step; r_s*; c_eff; cell fractions. No new constants.
## 5 · Files (pack28): PREDICTION/FINDING-CELLCUT · cellcut.py cellcut_run.py cellcut.jsonl TABLE-CELLCUT · PREDICTION/FINDING-ONEFUNC · onefunc.py
onefunc.jsonl · PREDICTION/FINDING-FRACHF · frachf.py frachf.jsonl · patched t7c_corrz.py t7c_cuaudit.py t7b_hf.py hfc2.py · this bridge · README-28.
## 6 · Unread / owed: unchanged (R 1668; Dabo 2010, Borghi 2014 beyond abstract). Owed: T4 (R 1701-1872); Kitagawara&Barut/Schwarz corrections.
Container clean at close: rt/ holds nothing outside the packs except __pycache__, .so, /tmp backups (discarded).