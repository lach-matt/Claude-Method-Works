# BRIDGE — THE LÖWDIN SESSION 27 (2026-08-16)
Successor to BRIDGE-LOWDIN-SESSION-26.md. Bank restore-point-2_13 (R 1700) UNCHANGED; nothing written to register/index/store.
Archive verified at open: HANDOFF-26 532/532. Gates 1-27 PASSED at open (values as README-18..26); gate-appended rows (G6,G8,G15,G23) restored.
F18.1 rt/ clean. No transcripts mounted; review by project knowledge + bridge-26. §H.10: handoff begun at ~80%, before exhaustion.
## 1 · Rulings in force (M, s27)
"Record corrections first, then proceed with the list in order" (bridge-26 s3(1)-(4)); "Continue" after the s3(1)-(3) report. GENERAL (carried):
predictions before runs; R 1449 timing flags; test every candidate, results decide; no scans; T4 writing chat LAST, not opened.
## 2 · Findings (no constant beyond c, no measured input; Cs/Y meas RECALLED-NOT-ENTERED) -- files in §5
(0) CORRECTIONS written (draft entries): s24 (a) SIC-relaxation misnomer, (b) 3d range -0.019..-0.054; s25 PF8 composition -> M_resp + M_csic;
    gate-13 HFS-not-HF; Kitagawara&Barut->R 1450 and Schwarz 2010 still owed to T4.
(1)+(2) F25.1 = F24.1, DIAGNOSED: the hard eps_c>=0 cutoff in v_gbz (v_c:=0) stepping ONE mesh cell in a diffuse s-orbital's SIC potential where its
    one-orbital r_s ~ 5.2 (Ti 4s-up r=3.63, step -0.0053; Cu 3s-up r=1.54). Exact cycle, amplitude beta-INDEPENDENT (Ti period 7 at 0.3, 4 at 0.15),
    E unchanged -0.38063 / -0.37349. Not mixing, not physics. PL2 FAILED, PL3 HELD. Repair is a RULING: (A) convergence certificate = it + E-stable /
    residual on total potentials only [convergence-only, recommended]; (B) taper the cutoff [changes the object; gate all 15]; (C) leave open.
(3) TERM-RESOLVED exact-exchange DSCF (Hund highest-weight determinant, first order in relaxation) BUILT. PT0 (Slater average reproduced 1e-16),
    PT3, PT4 HELD; PT1 FAILED 5/10; PT2, PT5(Cu,Tm) FAILED. 3d: Ti, Cr repaired (Cr +0.078 -> +0.021), Fe |.| falls but crosses (+0.048), Ni worse
    (+0.044), Cu +0.065. 4f: ALL worse and COLLAPSE TO ONE NUMBER +0.09..+0.10 incl. Yb (no term): the 4f residual is not term-average error.
    Term-HF+chain-corr is +0.02..+0.07 (3d) / +0.09..+0.10 (4f), all positive; the chain is all negative -> two-sided bracket, does not close, no constant.
(4) SECOND-ORDER correlation (HF + self-consistent chain-Z v_c, PZ SIC, integer occ): PC1 HELD; PC2-PC5 FAILED. Piece is POSITIVE and uniform:
    Cs +0.0008, Gd +0.0083, Y control +0.0082. Cs/Gd shortfall is not second-order correlation. LARGER (timing flag): TS-midpoint Delta_c (s26)
    and integer E_c^SIC difference disagree by 0.008 on class rows -> s26 "(a') <= 0.008 on Y La Lu Sc" reads ~+0.013 under the integer form.
    Which form is admissible is a RULING; the chain uses the midpoint form throughout.
STANDING AFTER SESSION 27: not a closure. Single-entrant rows: closed to <=0.009 under the midpoint correlation form, ~0.013 under the integer form
(ruling needed). Compact shells: bracketed from opposite sides by two derived objects. F24.1/F25.1 mechanised, repair pending ruling.
Failed predictions s27: PL1(period), PL2, PT1, PT2, PT5(Cu,Tm), PC2, PC3, PC4, PC5. Timing flags: v_gbz mechanism; 4f collapse reading; midpoint/integer gap.
## 3 · Next chat, in order (each needs a ruling; predictions first; smallest first)
(1) Ruling: F24.1/F25.1 repair A/B/C. If A: implement the certificate (no numbers change), close both faults.
(2) Ruling: correlation form (midpoint vs integer) for the law; then restate s26 (a') margin accordingly (a table, no new physics).
(3) The 4f +0.09 as ONE object: Yb (term-free) — smallest test: is it the F^k-unscreened / HF-vs-correlated 4f shell? Candidate: entrant second-order
    correlation on Yb computed WITHOUT a scan as in frozen_resp (P26.7 style). Prediction first.
(4) Term relaxation (term-resolved SCF) for Fe/Ni: expected small; a build; only if (3) leaves the 3d rows unexplained.
(5) T4 writing chat LAST: R 1701-1863 + s27: R 1864 corrections · R 1865 F24.1=F25.1 mechanism · R 1866 term-resolved result + 4f collapse ·
    R 1867 midpoint/integer correlation gap · R 1868 failed predictions s27.
## 4 · Figures (§H.6)
MEASURED: none entered. RECALLED-NOT-ENTERED: Cs 0.14310, Y 0.2285; TABLE-JANAK-24 meas as chain-resid. CHOSEN: prediction thresholds; beta 0.15
(one diagnostic value, not scanned); finite-difference conventions inherited. DERIVED: all Gaunt/3j coefficients; no new constants.
## 5 · Files (PACK-27): CORRECTIONS-SESSION-27 · PREDICTION/FINDING-LIMITCYCLE · limitcycle.py limitcycle.jsonl lc_diag.py · PREDICTION/FINDING-HFTERM ·
hfterm.py hfterm.jsonl hfterm_table.py TABLE-HFTERM · PREDICTION/FINDING-HFC2 · hfc2.py hfc2.jsonl · this bridge · README-HANDOFF-27. Bring next: LOWDIN-HANDOFF-27.
## 6 · Unread / owed
Unread inventory of the compendia unchanged (R 1668). Dabo 2010, Borghi 2014 unread beyond abstract. Owed: T4 writing chat (R 1701-1868);
Kitagawara&Barut/Schwarz attribution corrections (in CORRECTIONS file, T4). Container clean at close: rt/ holds nothing outside the packs except
__pycache__, .so, and s27 outputs (all in pack27).
