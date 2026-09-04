# BRIDGE — THE LÖWDIN SESSION 30 (2026-08-17)
Successor to BRIDGE-LOWDIN-SESSION-29.md. Bank restore-point-2_13 (R 1700) UNCHANGED; nothing written to register/index/store.
Archive verified at open: HANDOFF-29 595/595. Gates 1-40 PASSED at open (pack30/GATES-1-40-SESSION-30-OPEN.log). §H.10: handoff begun at ~80 %.
## 1 · Rulings (M, s30)
(1) F30.1 foreign branch: option B — its PREDICTION-DROW adopted as the prediction of record; its .py audited by read; its .jsonl admitted only row-for-row on
    fresh rerun (none was: Q_mid/box differed) — see FAULT-F30.1. (2) Node test opened ("Open the test"). (3) Outside search opened ("search outside literature").
(4) Candidate C opened ("Continue"). (5) FORM R vs Z: "try BOTH and let the comparison decide" — both forms are carried; s31 runs the comparison; NEITHER is
    the chain's correlation until it does. (6) The d-row object: NOT ruled; stays open as stated in COMPARE-DROW.
GENERAL carried: SUBCELL=1; predictions before runs; R 1449 timing flags; comparison decides; no scans; no constant; T4 writing chat LAST.
## 2 · Findings (no constant beyond c; Cs/Y RECALLED-NOT-ENTERED) — files in pack30
(1) ROUTE P (FINDING-DROW-P): B (entrant self-SIC) Sc 0.0110 Y 0.0061 La 0.0044 Lu 0.0052 Cs 1e-5; B/excess flat 0.60-0.63 on Y La Lu, 7.9 on Sc -> not the
    object; g = excess/Q_mid not one number (Sc 0.15 of Y); R (ns2 relaxation) ~ -0.65 B on every d row (PP3 FAILED: frozen pieces not quotable alone).
(2) ROUTE N (FINDING-DROW-N): box basis in the ion HFS potential (r>=3e-4, regular inner condition, eps<3, l<=4), adiabatic closure reproduces corepol <=3.3 %;
    |E2_closed| uncoupled Sc 0.030 Y 0.037 La 0.055 Lu 0.036 Cs 0.021 — the size of the WHOLE delivered correlation, Sc/Y 0.82: no 3d/nd>=4 discrimination.
    eps_e convention moves it 13-15 % (flagged). PN1 PN2 PN4 FAILED.
(3) COMPARE-DROW: neither route -> NEW OBJECT, class property of nd>=4 rows, absent at 3d.
(4) NODE TEST (FINDING-NODESPLIT): inner lobes 2-3 % of the entrant, B_in 0.0002-0.0003 (3-5 % of the excess) -> node REFUSED. Frozen single-SCF A exceeds
    two-SCF ΔA by ~60 % (relaxation signal, same as PP3).
(5) CANDIDATE C (FINDING-RING): form R = full RPA ring (ring_zeta integrand, tabulated 41 r_s x 11 zeta) + E0B. Delivered: Sc 0.93->1.15, Y 0.61->0.85,
    La 0.65->0.94, Lu 0.62->0.87, Cs 0.16->0.45; excess halved-quartered; Cs's cut = the truncation (one object with B). GAIN UNIFORM (+0.22..0.29, Sc/Y 0.95):
    the 3d/nd>=4 contrast survives both forms (Sc over 15 % vs Y La Lu under 6-15 %) -> the d-row object is NON-LOCAL, size ~0.005-0.008 vs an exact local form.
    Literature carried: Nozieres-Pines 1958 (GB valid r_s<~1); RPA overbinding ~0.035 Ry flat; GB57 / Onsager-Mittag-Stephen 1966 / BRM 2024. Cs still cut 31 %
    at zeta~1 because E0B is zeta-independent in the chain — derivable refinement OWED (SOX constant at zeta=1) before the R/Z comparison is fair on Cs.
Failed predictions s30: PP1(Sc) PP3 · PN1 PN2 PN3(order) PN4 · PQ1-4 (all, by design negative) · PR0(no-cut half) PR1(Y 0.005, Cs) PR2(Y) PR4.
Timing flags: F30.2 (r_peak shell definition, after Sc read); eps_e convention comparison (after PN1). Build errors caught by gate before scoring: F30.3 (box
conditioning), F30.3b (eps_e roundoff), nodesplit tail-noise nodes, drow_p r_peak. Foreign branch F30.1 quarantined in pack30/foreign/.
## 3 · Next chat, in order (rulings first; predictions before runs)
(1) R/Z COMPARISON (ruled): (i) derive E0B(zeta) — the second-order exchange constant's spin dependence — and put it in corr_ring (and, for symmetry, in the
    chain's Z form as a stated variant); prediction first; (ii) rerun the six class rows f=1/f=0 under R with E0B(zeta); (iii) the 15 chain rows (Cs Y La Gd Lu
    Fe Ni Sc Cu Dy Er Tm Yb Ti + …) full chain under R vs Z where the chain's own scripts allow (t7c_corrz corr='Z' -> a corr='R' hook, same interface);
    (iv) COMPARE-RZ decides: which form is the chain's correlation; the d-row object's size is then read against the winner. (2) Sc eps(0) slope run (small).
(3) 4f +0.09 as ONE object via Yb (second radial function; prediction first) — note form R changes 4f rows too; do after (1). (4) Term-resolved SCF Fe/Ni conditional.
(5) T4 writing chat LAST: R 1701-1876 + s30: R 1877 F30.1 foreign branch · R 1878 Routes P/N and the new object · R 1879 node refused · R 1880 candidate C
    (truncation = Cs cut; uniform gain; non-local d-row object) · R 1881 failed predictions s30 · R 1882 ruling: both forms carried.
## 4 · Figures (§H.6): MEASURED none entered. RECALLED-NOT-ENTERED Cs 0.14310, Y 0.2285. CHOSEN: all prediction thresholds; box r_min 3e-4, ECUT 3, LMAX 4;
ring grids nk=nx=1400, table 41x11, nan-mask; EPSE convention (ion default). DERIVED: E2, A/B/R, Q_mid, Q_in, eps_R/v_R (from the ring integral), E0B (chain).
No new constants. INHERITED reading: uncoupled-HFS inflation ~1.8x on Route N (enters nothing).
## 5 · Files (pack30): PREDICTION-{DROW,NODESPLIT,RING} · FINDING-{DROW-P,DROW-N,NODESPLIT,RING} · COMPARE-DROW · FAULT-F30.1 · drow_p/drow_n/nodesplit/
ring_table/corr_ring/frachf_ring .py + .jsonl/.json · GATES-1-40 log · SPEC-DROW (s29) · foreign/ (8 files, quarantined) · this bridge · README-30.
## 6 · Unread / owed: unchanged (R 1668; Dabo 2010, Borghi 2014). Owed: T4 (R 1701-1882); E0B(zeta) derivation; PR3 (A/B/R under R); Kitagawara&Barut/Schwarz.
Container: rt/ relocated beside the packs (t5_scf reads ../pack9/); rt/ holds nothing outside the packs except __pycache__, .so, foreign/ (copied to pack30).