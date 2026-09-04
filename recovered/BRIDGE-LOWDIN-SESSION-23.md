# BRIDGE — THE LÖWDIN SESSION 23 (2026-08-16)
Successor to BRIDGE-LOWDIN-SESSION-22.md. Bank restore-point-2_13 (R 1700) UNCHANGED; nothing written to register/index/store.
Archive verified at open: HANDOFF-22 421/421. Gates 1-15 PASSED at open (values as bridge-22 + README-22 (13)-(15)); gate-appended rows restored
cmp-identical; F18.1 rt/ clean. Handoff at ~85-90 % on M's standing ruling (finish the running task, then full handoff).
## 1 · Rulings in force (M, s23)
"Continue in order" on bridge-22 s3 (1)-(6). GENERAL: test every candidate, results decide. NEW (s23): F^k convention -- test on SIC and Z densities;
if own-orbital better -> STANDING, marked NEW, BASED ON THE SLATER FORM until a better attribution is found; if none -> PROPOSED, REQUIRING
VERIFICATION BY OTHERS. Applied: own-orbital won on both densities (§2 (3)).
## 2 · Findings (no constant, no measured input; c only) -- files in §5
(1) REGEN under F22.1 (SIC_NOCLAMP=1): all 15 bases shallower +0.0034..+0.0070 (median +0.0056), NO channel ordering (PR3 failed); GB increments
    unchanged (<=2e-4; Cu 7e-4). Score 9 CONTAINED / 4 OVER / 2 SHORT (was 9/5/1): Cs OVER->CONTAINED, Yb CONTAINED->SHORT, Tm ON |U| to 4 dp,
    Cu SHORT worse (+0.0451). PR1 PR2 held; PR4 failed on Cu; PR5 failed by two rows (Yb pre-named, Cs not). Bridge-22 s6 regeneration owed: CLEARED.
(2i) eps0^a(zeta) DERIVED IN-PROJECT: ring_zeta.py (Benites-Rosado-Manousakis arXiv:2411.18371 Eqs 12-14 integrand; GB57 ring sum). c0(zeta)
    agrees with Hoffman/Loos-Gill endpoints (-0.0711/-0.0499) and BRM Table II at all tested zeta to <=5e-5 Ha; Hoffman minimum reproduced.
    PZ1-5 all held. eps0a_table.json (31 zeta, interpolated in (1-zeta)^{1/3}). Hoffman 1992 no longer needed; priority recorded.
(2ii) Z0: pointwise eps_c(r_s(r),zeta(r)) [lam0 WP91 · eps0a in-project · eps0b OMS66], spin-resolved potential, NO chosen constant. rms(resid)
    0.0247 -> 0.0175. THE BRACKET HID THE SPIN: down-entrants (Fe Ni Cu Dy Er Tm Yb) see v_dn deeper than U (PZ6 failed; PZ6' held 9/9).
    Z1 (+lam1 r_s ln r_s, Loos-Gill 2011 Eqs 16-17 in lam1_zeta.py): rms 0.0197 -- d/f entrants sample r_s<1 where r_s ln r_s<0 (PZ9, PZ10 failed).
    UNDER BOTH: single-entrant s/d class Cs Y La Gd Lu closes to <=2.7 mHa; own-shell class Sc Ti Cr Fe Ni Er over-bound 12-31 mHa; Cu short
    +10 mHa; Dy over-bound 52-58 mHa. Truncation order = stated series limitation (O(r_s) not closed), not a fitted element.
(3) F^k: own-orbital beats TS-orbital on SIC and on Z density (rms Er/Tm/Yb 0.0070 vs 0.0117; densities agree to 3e-4). SIC/Z TS orbital falls out
    of neu<ts<ion order (half-weighted SIC on the entrant) -- TS convention has an object-dependence own-orbital lacks. STANDING: own-orbital,
    NEW BASED ON SLATER FORM; candidates flagged not entered: Ziegler-Rauk-Baerends 1977, von Barth 1979.
STANDING AFTER SESSION 23: chain TF/D -> Dirac/Slater/Gaspar -> Slater-Janak TS -> KH SR -> PZ SIC (F22.1 repaired) -> Lande SO / Hund-II
own-orbital F^k -> pointwise GB(zeta) [Z0/Z1]. Not a closure. Failure has THREE named shapes (own-shell partial filling; Cu short; Dy).
Faults: none new. Predictions failed: PR3 PR4 PR5 PZ6 PZ7 PZ9 PZ10 PF1 PF2 (all entered with reasons). Note s23-1: scorer sign inversion caught before reading.
## 3 · Next chat, in order (candidates; each needs a ruling; predictions first; smallest first)
(1) Cu audit (bridge-22 s3(4)): now +0.0103 short under Z; SIC destabilises +0.024 (beta_3d*N_sib=9); test the entrant-down channel's SIC weight.
(2) Own-shell class (Sc Ti Cr Fe Ni Er, -0.012..-0.031 under Z): one shape, six rows -- candidate: the SIC self-term of the entrant vs its own-shell
    siblings (same f_i=1/2 half-weighting that broke the TS F^k order in (3)); state a prediction, test on Sc first.
(3) Dy (bridge-22 s3(5)): over-bound 52-58 mHa under every combination; nothing left in the chain -- state as the object's bound unless M names a candidate.
(4) Attribution search for own-orbital Hund-II (ZRB77, vB79) -- read only.
(5) T4 writing chat LAST: R 1701-1836 + s23: R 1837 REGEN F22.1 9/4/2 · R 1838 eps0a in-project · R 1839 Z0/Z1 bracket->number, spin split ·
    R 1840 single-entrant class closes <=2.7 mHa · R 1841 F^k own-orbital standing (new, Slater-based) · R 1842 failed predictions s23.
## 4 · Figures (§H.6)
MEASURED: none entered. RECALLED-NOT-ENTERED (comparison only): t5/COMPARE meas rows; BRM Table II/VIII; LG Table I. CHOSEN: prediction thresholds
(stated before each run); numerics of ring_zeta (grids, r_s extrapolation ratio 0.575) and eps0a interpolation variable (1-zeta)^{1/3}. c = 137.035999.
No new constants in any object; GB constants replaced by derived functions of zeta.
## 5 · Files (PACK-23, incl. this bridge + MANIFEST): PREDICTION/FINDING-{T7C-REGEN,GB-ZETA-RING,T7C-CORRZ,FK-DENSITY} · TABLE-CHAIN-15-{REGEN,Z,Z1} ·
t7c_regen.py/.jsonl · ring_zeta.py · eps0a_table.py/.json · lam1_zeta.py · t7c_corrz.py · t7c_corrz_run.py · t7c_corrz.jsonl · t7c_corrz1.jsonl ·
t7c_fkdens.py · t7c_fkdens_{SIC,Z}.jsonl · RUN-SESSION-23.txt. Runtime: README-HANDOFF-23. Bring next: LOWDIN-HANDOFF-23 (superset) + project files.
## 6 · Unread / owed
Unread inventory of the compendia unchanged (R 1668). Hoffman 1992 unread (no longer needed). ZRB77 / vB79 unread (attribution candidates).
Owed: T4 writing chat (R 1701-1842); own-orbital Hund on the 4f column regenerated on SIC/Z (shift +0.0004 Er only; carried, stated).
Container clean at close: rt/ holds no file outside the packs except gate-appended rows (restored) and s23 outputs (all in pack23).