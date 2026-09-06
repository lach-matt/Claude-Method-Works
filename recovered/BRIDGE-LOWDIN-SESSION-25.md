# BRIDGE — THE LÖWDIN SESSION 25 (2026-08-16)
Successor to BRIDGE-LOWDIN-SESSION-24.md. Bank restore-point-2_13 (R 1700) UNCHANGED; nothing written to register/index/store.
Archive verified at open: HANDOFF-24 476/476. Gates 1-21 PASSED at open (values as README-18..24); gate-appended rows restored. F18.1 rt/ clean
(only pack5 out/, __pycache__, .so, s25 outputs -- all in pack25). No transcripts mounted this session (/mnt/transcripts empty); review by project knowledge + bridge-24.
## 1 · Rulings in force (M, s25)
"Continue in order" on bridge-24 s3 (1)-(4). Ruling (b) applied as recommended (both estimators). Ruling (c) decided by the derivability rule (below).
GENERAL: predictions before runs; R 1449 timing flags; test every candidate, results decide. Item (5) writing chat LAST, not opened.
## 2 · Findings (no constant, no measured input; Cs/Y comparison values RECALLED-NOT-ENTERED) -- files in §5
(1b) TABLE-CHAIN-15-BOTH: eps(1/2) and DE_J side by side, resid_TS/Z1/J. P25.1 FAILED on Cu only (+0.0042 = s24 SO term; my prediction omitted it); P25.2 HELD.
(1c) Ruling (c): unscreened Koopmans (KI, Dabo 2010) is ADMISSIBLE but DEGENERATE -- eps_KI == DE_J identically (PK1 HELD 1e-16 on Cs, Sc; PK2 HELD).
    Non-degenerate variant (KIPZ) needs alpha: chosen -> inadmissible; linear-response -> item (2). FOLDED INTO (2). Not a new link.
(2) Frozen-orbital f-scan CLOSED (15 rows, ref f=1/2): the mask DE_J-eps(1/2) is DOMINANTLY FIXED-ORBITAL: frozen fraction 6s ~1, 4d/5d 0.94-0.99,
    3d 0.94(Sc)->0.77(Cu), 4f 0.78 incl. Dy 0.79; relaxation |.|<=0.0095 on ALL 15 (PF6 HELD, Dy -0.0078). PF2 FAILED: s24 §2(2b)'s
    "SIC-relaxation part" (Sc -0.006, Yb -0.032) is MISNAMED -- present with every orbital frozen; correction owed to s24 record.
    Split is REFERENCE-DEPENDENT (PF4 HELD: Sc ref f=1 -> relaxation +0.0656): the admissible statement is "at the TS reference the mask is
    what the functional does at fixed orbitals". PF7 HELD: mask_fr/(-0.0583|E_x[n_ent]|) = 1.12-1.19 on 14 non-Cs rows INCLUDING Dy (PO14's
    1.19-1.51 structure was relaxation); 0.0583 = (4/3)2^(-1/3)-1 = entrant PZ exchange-SIC f^(4/3) law. PF8 (x-only chain): 1.09/1.07 (Sc/Yb):
    composition = x-SIC law 1.00 + LSD total-x curvature ~+0.07-0.09 + correlation ~+0.05-0.08. Whether the +0.15 is derivable: NEXT candidate.
    Dy: frozen fraction and relaxation equal the 4f class; its -0.045 excess is in neither (object's bound stands).
(3) 3d SO/Hund column DERIVED (t7c_so.zeta + t7c_mult CI at L=2, Lande A=+-zeta/(2S) shown general): Sc -0.0008 Ti -0.0178 Cr +0.0017 Fe -0.0022
    Ni +0.0000 EXACT (d8/d7-hole stab identical, SO identical; quartet-avg alt -0.0259 printed) Cu +0.0042 (s24 reproduced). PH1-PH4 HELD.
    3d class under J with column: -0.0537 (Ti) .. -0.0194 (Cu), spread 0.034 (was 0.025): NO tightening; s24 range "-0.019..-0.044" -> "-0.019..-0.054".
(4) `it` audit CLOSED: 2/15 s23 rows hit maxit=100 (Ti new = F25.1, Cu = F24.1); E stable to 1e-4; `it` per row on record. Limit cycle not repaired.
STANDING AFTER SESSION 25: not a closure. Under DE_J (+ derived SO/Hund) the residual is a compact-shell over-binding whose TS-mask part is a
fixed-orbital scaling law (1.15 x PZ f^(4/3)) and whose remainder (resid_J itself, -0.002 s .. -0.05 3d/4f) is the functional's over-binding
of the compact entrant; plus Dy. Faults: F25.1. Predictions failed: P25.1(Cu) PF1(Cs) PF2(Sc,Yb) PF5(Cs) PF8 (all with reasons in files).
Corrections owed to the s24 record: (a) "SIC-relaxation part" -> fixed-orbital functional f-nonlinearity; (b) 3d class range.
## 3 · Next chat, in order (candidates; each needs a ruling; predictions first; smallest first)
(1) Is the frozen ratio 1.15 derivable? Split LSD-total-x curvature vs correlation per row (frozen_scan3 CORR=none on all 15 with exfr E_x); test whether
    each is a scaling in |E_x[n_ent]| or in rmean; a derived form would make the whole TS mask closed-form. Prediction first.
(2) With mask closed-form, the object becomes eps(1/2) + mask(E_x[n_ent]) + SO/Hund; remaining residual = functional over-binding of compact entrants.
    Candidate: this is the entrant's own SIC-correlation/exchange treatment (s24 test C: Sc over-bound -0.0115 with NO SIC) -- ruling needed on scope.
(3) Ti: now the 3d deep edge (-0.054) -- audit F25.1 limit cycle on Ti (beta/mixing) before reading Ti as physics.
(4) F24.1/F25.1 general: repair the period-5 limit cycle (Ti, Cu) -- convergence, not physics; prediction: E unchanged to 1e-4.
(5) T4 writing chat LAST: R 1701-1848 + s25: R 1849 F25.1 · R 1850 KI degenerate with DE_J (ruling c) · R 1851 frozen-scan class result + reference
    dependence + s24 misnomer correction · R 1852 frozen mask 1.15 x PZ f^(4/3) plateau incl Dy · R 1853 3d SO/Hund column, Ni exact cancellation ·
    R 1854 3d class range correction · R 1855 it audit · R 1856 failed predictions s25.
## 4 · Figures (§H.6)
MEASURED: none entered. RECALLED-NOT-ENTERED: Cs 0.14310, Y 0.2285 (unchanged). CHOSEN: prediction thresholds; f grid {0.001,0.05,0.15,0.25,0.5,0.75,1.0}
interpolated in f^(1/3) (s24); reference f=1/2 (standing TS point) and f=1 (PF4 test); c=137.035999. DERIVED, not chosen: 0.0583 = (4/3)2^(-1/3)-1. No new constants.
## 5 · Files (PACK-25): TABLE-CHAIN-15-BOTH · PREDICTION/FINDING-KOOPMANS-LINK · PREDICTION/FINDING-FROZEN-SCAN · TABLE-FROZEN-SCAN ·
PREDICTION/FINDING-3D-SOHUND · TABLE-3D-SOHUND · FINDING-IT-AUDIT · PREDICTION-TABLE-BOTH · frozen_scan.py frozen_scan2.py frozen_scan3.py exfr.py
t7c_3dhund.py · frozen_scan.jsonl frozen_scan_ref1.0.jsonl frozen_scan_corrnone.jsonl t7c_3dhund.jsonl · this bridge. Runtime: README-HANDOFF-25.
Bring next: LOWDIN-HANDOFF-25 (superset).
## 6 · Unread / owed
Unread inventory of the compendia unchanged (R 1668). Dabo 2010, Borghi 2014 unread beyond abstract. Owed: T4 writing chat (R 1701-1856); s24
record corrections (a),(b) above; F24.1/F25.1 repair. Container clean at close: rt/ holds no file outside the packs except gate-appended rows
(restored), __pycache__, .so, and s25 outputs (all in pack25).