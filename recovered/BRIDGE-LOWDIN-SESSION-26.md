# BRIDGE — THE LÖWDIN SESSION 26 (2026-08-16)
Successor to BRIDGE-LOWDIN-SESSION-25.md. Bank restore-point-2_13 (R 1700) UNCHANGED; nothing written to register/index/store.
Archive verified at open: HANDOFF-25 503/503. Gates 1-23 PASSED at open (values as README-18..25); gate-appended rows (G6,G8,G23) restored. F18.1 rt/ clean.
No transcripts mounted (/mnt/transcripts empty); review by project knowledge + bridge-25. Opening turn stated nothing before the upload landed (R 1697).
## 1 · Rulings in force (M, s26)
"Continue in order" on bridge-25 s3. Item (2): "let the comparison of (a) and (b) decide". Then: "do the build" -> (a') opened. GENERAL: predictions
before runs; R 1449 timing flags; test every candidate, results decide. T4 writing chat LAST, not opened.
## 2 · Findings (no constant, no measured input; Cs/Y meas RECALLED-NOT-ENTERED) -- files in §5
(1) CLOSED. mask_fr = 0.0583 E_x[n_ent] (law, exact) + M_csic (SIC-correlation midpoint defect, r 0.05-0.08) + M_resp (entrant orbital's own 2nd-order
    response to dV_f, negative on all 30 rows, r 0.07-0.12). M_xtot, M_ctot ~ 0 (|r|<=0.013). The "1.15" is 1 + r_csic + r_resp, both derived, row-dependent,
    not a constant. M_resp is linear response computed WITHOUT a scan (P26.7 failed narrowly: 2nd order = 1.07-1.15 x, one-signed higher orders); the
    SIC-x shape alone gives 0.88-1.14 with derived K = 3/5-(3/2)2^(-1/3)+2^(-2/3) = 0.03941 (P26.8). Remainder -0.028..+0.005 law units.
    CORRECTION OWED to s25 record: PF8's "LSD total-x curvature +0.07-0.09" is orbital response; its "correlation" is almost purely SIC-correlation. Failed: P26.5 P26.6 P26.7.
(2)(a) CLOSED -> (b) by default: first-order <K> replacement is Koopmans (unrelaxed) vs the chain's relaxed TS/Janak object; F26.1 (design). PA1-4 failed.
(2)(a') BUILT. F26.2 LATENT: HF 'hf' at fractional occupation carries (Q_a-1)Y^0 -> unphysical at Q=1/2; banked uses all integer. Object switched to
    exact-exchange DSCF (integer, avg-of-config, relaxed) + first-order chain-Z correlation (+SIC) + so/hund. On the like-for-like class Y La Lu Sc:
    resid_HFc +0.005 +0.002 +0.005 -0.008 (mean 0.005) vs resid_J mean 0.019 -> (a') BEATS (b) THERE: the DE_J residual on single-entrant rows IS the
    exchange functional's over-binding. On 3d/4f avg-of-config HF is not like-for-like (term-average error dominates: Cr +0.078, Yb +0.093): OPEN.
    Cs +0.012, Gd +0.018 worse than chain (stated). PB1 PB3 PB4 held; PB2 failed by 0.001. Corrections: gate-13's Sc -0.2686 / La -0.2017 are HFS not HF.
STANDING AFTER SESSION 26: not a closure. TS mask derivable at the 3% level (law + E_c^SIC defect + linear response). Residual on single-entrant rows
explained as exchange-functional over-binding (exact exchange + chain correlation closes to <=0.008). Residual on compact multi-electron shells (3d/4f)
and Dy: OPEN, needs term-resolved exact-exchange DSCF. Faults: F26.1 (design), F26.2 (latent). Timing flags: DSCF switch after seeing Sc TS -0.553.
## 3 · Next chat, in order (each needs a ruling; predictions first; smallest first)
(1) Ti F25.1 limit-cycle audit (bridge-25 s3(3)) and (2) F24.1/F25.1 period-5 repair (s3(4)) -- convergence only, prediction E unchanged to 1e-4. NOT DONE in s26 (carried).
(3) Term-resolved (Hund ground term) exact-exchange DSCF for 3d/4f + chain correlation: prediction on record (resid_HFc < |resid_J| on >=7/10). A build.
(4) Cs/Gd in (a'): why HF-DSCF+corr is worse than the chain there (diffuse 6s; open 4f7 core) -- smallest test: second-order correlation on Cs.
(5) T4 writing chat LAST: R 1701-1856 + s26: R 1857 frozen split (law+csic+resp; s25 misnomer correction) · R 1858 linear-response derivation of M_resp,
    K=0.03941 · R 1859 F26.1 · R 1860 F26.2 latent + gate-13 HFS/HF naming · R 1861 (a') like-for-like class result · R 1862 3d/4f open · R 1863 failed predictions s26.
## 4 · Figures (§H.6)
MEASURED: none entered. RECALLED-NOT-ENTERED: Cs 0.14310, Y 0.2285 (unchanged), plus all meas of TABLE-JANAK-24 re-derived as chain-resid (same values).
CHOSEN: prediction thresholds; f grid and f^(1/3) interpolation (s24); finite-difference d=0.1/0.05 (agree <1e-4); c=137.035999. DERIVED, not chosen:
0.0583 = (4/3)2^(-1/3)-1; K = 0.03941. No new constants.
## 5 · Files (PACK-26): PREDICTION/FINDING-FROZEN-SPLIT · TABLE-FROZEN-SPLIT · frozen_split.py frozen_split_table.py frozen_resp.py · frozen_split.jsonl
frozen_resp.jsonl · frozen_scan_corrnone.jsonl (15 rows, supersedes pack25's 2) · PREDICTION/FINDING-XFOCK · TABLE-XFOCK · xfock.py xfock_table.py xfock.jsonl ·
PREDICTION/FINDING-HFCORR · TABLE-HFCORR · hfcorr.py hfcorr.jsonl hfdscf.py hfdscf.jsonl hfdscf_table.py · this bridge · README-HANDOFF-26. Bring next: LOWDIN-HANDOFF-26 (superset).
## 6 · Unread / owed
Unread inventory of the compendia unchanged (R 1668). Dabo 2010, Borghi 2014 unread beyond abstract. Owed: T4 writing chat (R 1701-1863); s24 record
corrections (a),(b) (bridge-25); s25 correction (PF8 composition, above); F24.1/F25.1 repair; bridge-25 s3(3),(4) carried. Container clean at close:
rt/ holds nothing outside the packs except __pycache__, .so, and s26 outputs (all in pack26).