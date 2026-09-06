# BRIDGE — THE LÖWDIN SESSION 24 (2026-08-16)
Successor to BRIDGE-LOWDIN-SESSION-23.md. Bank restore-point-2_13 (R 1700) UNCHANGED; nothing written to register/index/store.
Archive verified at open: HANDOFF-23 453/453. Gates 1-18 PASSED at open (values as README-18..23); gate-appended rows restored cmp-identical;
F18.1 rt/ clean. Handoff on M's standing ruling (finish the running task, then full handoff); M: "Continue" -> archive built.
## 1 · Rulings in force (M, s24)
"Continue in order" on bridge-23 s3 (1)-(4); (3) Dy stated as the object's bound (bridge-23 wording). GENERAL: test every candidate, results decide;
predictions before runs; R 1449 timing flags. Item (5) writing chat LAST, not opened.
## 2 · Findings (no constant, no measured input; Cs/Y comparison values RECALLED-NOT-ENTERED) -- files in §5
(1) Cu audit CLOSED. F24.1: standing Cu Z-row SCF hits maxit=100 in a period-5 residual limit cycle; E stable to 1e-5 across it; EZ -0.3735
    STANDS; `it` was not recorded in s23 rows (owed). Lande zeta_3d(Cu)=0.0042 (TS potential, as 5d): Cu resid +0.0104 -> +0.0146 (PC1 PC2 held).
    Entrant SIC weight f=1 (vs PZ 1/2): Cu -0.371, Cs -0.064, Sc -0.220 -> REJECTED as a rule (PS0 PS2 PS3 held; PS1 magnitude failed:
    at f=1/2 the entrant's own SIC potential is -0.5 v_H + 0.79|v_x| ~ 1/9 of a sibling's, cancellation not scaling).
(2) Own-shell class CLOSED; candidate EXCLUDED as origin. Test C: Sc direct -0.0166 indirect +0.0015 (N_sib 0), over-bound -0.0115 with NO SIC;
    Fe direct -0.0199 indirect +0.0237. Test D (Janak, all 15 rows): eps(f) shallowest at f=1/2..3/4 on every row; DE_J = int eps df:
    resid_J: Cs -0.002 · Y La Gd Lu -0.008..-0.012 · Sc Ti Cr Fe Ni -0.036..-0.044 · Cu -0.019 (SO in) · Er Tm Yb -0.052/-0.043/-0.039 · Dy -0.090.
    ONE monotone shape in entrant compactness + Dy; the three TS shapes reduce to TWO under the functional's own DSCF; TS eps(1/2) is a
    shell-dependent mask (0.002 s, 0.010 5d, 0.017-0.034 3d, 0.037-0.043 4f). PO14 (mask = -0.0583|E_x[n_ent]|, PZ-81 scaling) FAILED as
    stated; ratio plateau 1.40-1.51 on the 8 compact rows, 1.2 diffuse d, 0.52 Cs (exchange scaling ~70 % of the mask; remainder named).
    Held: PO1 PO3 PO5-PO13. Failed: PO2 PO4 PO14 (reasons in FINDING).
(3) Dy: object's bound (ruling). Under Janak Dy is ~0.045 outside a 4f class uniform to +-0.007. Observation only: excess ~ its Hund term.
(4) Attribution (read only, web): ZRB77 = sum method (own-orbital principle present), vB79 = LSD; TS-vs-Janak gap: Slater 1972, Janak 1978,
    PPLB 1982, PZ81 scaling; closest prior Dabo et al. PRB 82, 115121 (2010) (total vs differential IP, curvature of E_N). Nothing entered.
STANDING AFTER SESSION 24: chain of s23 with TWO estimators to be printed side by side (TS eps(1/2); Janak DE_J) pending ruling (b).
Not a closure. Failure has two shapes under DE_J (compact-shell over-binding growing with |E_x[n_ent]|; Dy).
Faults: F24.1. Predictions failed: PS1(mag) PO2 PO4 PO14 (all entered with reasons). Note s24-1: Cs/Y meas absent from t5.jsonl -- runner repaired.
## 3 · Next chat, in order (candidates; each needs a ruling; predictions first; smallest first)
(1) Ruling (b): print DE_J beside eps(1/2) in TABLE-CHAIN-15 (recommended: both). Ruling (c): piecewise-linearity / Koopmans condition as next
    link -- derivability rule decides (Dabo 2010; Borghi 2014). If permitted: state a prediction, test on Cs and Sc first.
(2) The mask remainder (ratio 1.44 vs 1.0): rerun test D with the correlation SIC off on Sc and Yb -- prediction: ratio falls toward 1.0..1.1.
(3) 3d SO/Hund column owed (neutral ground level + ion hole level, Ni Hund-II vs quartet average) -- derivable, same objects as 5d/4f.
(4) Audit which s23 rows hit maxit (record `it`); F24.1 general.
(5) T4 writing chat LAST: R 1701-1842 + s24: R 1843 F24.1 · R 1844 Cu SO +0.0042, weight f=1 rejected · R 1845 Janak class result (two shapes)
    · R 1846 TS mask -0.0583|E_x| x 1.44 · R 1847 attribution note · R 1848 failed predictions s24.
## 4 · Figures (§H.6)
MEASURED: none entered. RECALLED-NOT-ENTERED (comparison only): Cs 0.14310, Y 0.2285; Cu II 3D interval ~720 cm-1. CHOSEN: prediction
thresholds (stated before each run); f grid {0.001,0.05,0.15,0.25,0.5,0.75,1.0} interpolated in f^(1/3); c = 137.035999. No new constants.
## 5 · Files (PACK-24): PREDICTION-CU-AUDIT · FINDING-CU-AUDIT · PREDICTION-OWNSHELL-SC · FINDING-OWNSHELL-JANAK · ATTRIBUTION-NOTE ·
TABLE-JANAK-SESSION-24.txt · ratio.txt · t7c_cuaudit.py · t7c_cuaudit_run.py · t7c_cuaudit.jsonl · t7c_ownshell_run.py · t7c_ownshell.jsonl ·
janak_table.py · exent.py · exent.jsonl · RUN-SESSION-24.txt · this bridge. Runtime: README-HANDOFF-24. Bring next: LOWDIN-HANDOFF-24 (superset).
## 6 · Unread / owed
Unread inventory of the compendia unchanged (R 1668). ZRB77 / vB79 read at abstract level only; Dabo 2010 unread beyond abstract.
Owed: T4 writing chat (R 1701-1848); `it` audit of s23 rows; 3d SO/Hund column. Container clean at close: rt/ holds no file outside the
packs except gate-appended rows (restored), __pycache__, .so, and s24 outputs (all in pack24).
