# BRIDGE — THE LÖWDIN SESSION 22 (2026-08-16)
Successor to BRIDGE-LOWDIN-SESSION-21.md. Bank restore-point-2_13 (R 1700) UNCHANGED; nothing written to register/index/store.
Archive verified at open: HANDOFF-21 386/386. Gates 1-12 PASSED at open (derive_P3 byte-identical; probe13 exact; t5 Sc/La; t7c H 1s -0.5000064,
Z=70 -2634.8449, Fe pol -0.378; He/Ne, hfs-switch Sc/Fe; Ce IV bare -0.42268; La 5d E_ts -0.2079 zeta 0.00308; srdec 0.0266; mult-audit f2 (11,7,3)
f4 (13,8,9,5); G10 -0.2202; G11 -0.2284; G12 Z=26 SKIP). Gate-appended rows restored, cmp-identical. F18.1 check: rt/ clean. Handoff at ~90 % on M's word.
## 1 · Rulings in force (M, s22)
Bridge-21 s3: (1) stands -> run; (2) do; (3) do (read only); (4a) established math says; (4b) derive; (4c) do; (5) do FIRST; (6) T4 stands LAST.
F^k convention: "test both and let the comparison decide"; GENERAL RULING: whenever a candidate choice exists, test each candidate, results decide
the fit along the road to derivation. 4a: REPAIR. GB-zeta: test all three candidates (i)(ii)(iii). Handoff at 90 %: finish the running task, then full handoff.
## 2 · Findings (no constant, no measured input; c only) -- files in §5
(5.4) DYAUDIT: every Dy hole-bookkeeping element forced except the F^k orbital; own-orbital moves Dy +0.0055 (still -0.016 after SO), Er/Tm +0.004/+0.001,
     Yb 0 (PY1-4 held). COMPARE: TS-orbital vs own-orbital TIED (rms 0.0186/0.0182); own-orbital proposed (attributed, Slater form). NOT a Dy anomaly.
(5.3) HFSR: SR-HF entrant object built (t7c_hfsr, KH operator on the local Fock part; gates exact: He, Sc c=1e6, hfs-mode = t7c_ts). SR-HF 5d edge
     +0.035/+0.053/+0.043 (wider than the local chain), 4f +0.06..+0.14 shallow, 3d 0.007-0.013. PH1/2/4 held, PH3 magnitude failed. Unpredicted:
     SR destabilisation ~14 % larger under exact exchange on every 5d/4f row. Bridge-20 (3) confirmed: HF is not a closure.
(1)+(2) CORR-ALL: GB U/P bracket on all 15 rows; TABLE-CHAIN-15: CONTAINED 9 (Fe Ni Y La Gd Lu Er Tm Yb), OVER 5 (Cs Sc Ti Cr Dy), SHORT 1 (Cu).
     PG2/PG3 held; PG1 (6s U, U/P ratio) and PG4 (magnitude) failed. NEW: SIC-SR commutation (bridge-21 C) FAILS on 4f by +0.011..+0.014
     (held on 4d/5d only) -- entered per R 1449. Er/Tm/Yb residuals after SR-SIC + own-orbital Hund + level SO: +0.023/+0.032/+0.037.
(3)  READ-GB-ZETA: lam0(zeta) closed form (Wang-Perdew 91); eps0^b const (Onsager 66); eps0^a(zeta) exact-numeric (Hoffman 92, unfetched;
     endpoints -0.0711/-0.0499, Misawa scaling checked); lam1(zeta) closed form (Loos-Gill 11). Exact B_U -0.0469, B_P -0.0257 (PZ quoted -0.048/-0.0269).
(4a) PZ-81: SIC replaces the Latter tail; clamp on a SIC channel is a double asymptote -> F22.1 REGISTERED, repaired in t7c_corr2 (SIC_NOCLAMP=1):
     H 1s half -0.50001 (was -0.533 / 0.0014). La 5d no-clamp +0.0041 shallower (PR2 failed by 1e-4). GB exact constants: +0.0002/+0.0003 (PR3 failed, smaller).
(4b) DERIVED: kappa = -eps''(1/2)/24 = -(1/24) d^3E/dq^3, to 1 % on all 15 untailed rows (new, stands). "TS(-1/r) == dSCF_ut" DROPPED as law
     (first-order tail vs third-order curvature; Cs counter-example T -0.014, kappa 0.000); kept as a d/f coincidence.
(4c) Untailed SR dSCF on La/Gd/Lu: tailed split 0.020-0.030 collapses to kappa_SR 0.003-0.004; dSCF_ut - ts_tailed 0.0016 flat. s20 (b1) "TS/dSCF split
     is a local-exchange property" WITHDRAWN AS STATED (R 1449); its indirect-SR clause stands.
STANDING AFTER SESSION 22: one attributed chain (TF/D -> Dirac/Slater/Gaspar -> Slater-Janak TS -> KH SR -> PZ SIC -> Lande SO/Hund-II (own-orbital F^k)
-> GB bracket) brackets 9 of 15 rows and over-shoots the 5 that SIC alone closes; Cu unreachable; Dy every term deepens. The clamp repair (F22.1)
will shift every SIC/GB row ~+0.004 (5d) once regenerated. Not a closure; the failure now has one shape on all 15 rows.
Faults: F22.1 (repaired in object, banked rows not regenerated). Predictions failed: PH3, PG1(2 clauses), PG4, PR2, PR3.
## 3 · Next chat, in order (candidates; each needs a ruling; predictions first; smallest first)
(1) REGENERATE the 15-row chain under F22.1 repair (SIC_NOCLAMP=1) -- t7a_all/t7c_sic/t7c_corr_all equivalents; then re-score containment.
(2) GB-zeta (i)/(ii): obtain Hoffman eps0^a(zeta) (paywalled; try Gori-Giorgi & Perdew PRB 69 041103 or Perdew-Wang 92 appendix as routes) ->
    pointwise eps_c(r_s(r),zeta(r)) with lam1 term -> bracket becomes a number. (iii) DONE (immaterial, 3e-4).
(3) Ruling owed: F^k own-orbital as standing (COMPARE file). (4) Cu: SIC destabilises +0.024 (beta_3d*N_sib=9) -- the one SHORT row; audit target.
(5) Dy: over-bound on every term; nothing left in the chain to test -- state as the object's bound unless M rules a new candidate.
(6) T4 writing chat LAST: R 1701-1825 + s22: R 1826 DYAUDIT · R 1827 F^k tie/own-orbital · R 1828 HFSR confirmation · R 1829 GB all rows 9/5/1 ·
    R 1830 SIC-SR 4f non-commutation (C qualified) · R 1831 READ GB-zeta + attributions · R 1832 F22.1 · R 1833 kappa = -eps''/24, 4b dropped ·
    R 1834 s20 (b1) withdrawn as stated · R 1835 general ruling: test every candidate · R 1836 handoff at 90 %.
## 4 · Figures (§H.6)
MEASURED: none entered. RECALLED-NOT-ENTERED (comparison only): t5 meas rows; Y IP 0.2285; Cs IP 0.1431. CHOSEN: prediction thresholds, stated
before each run. c = 137.035999. GB constants analytic/quoted-exact (attributed): PZ-quoted -0.048/-0.0269 in banked object; exact -0.046908/-0.025725
(Loos-Gill/Onsager) in t7c_corr2 under GB_EXACT=1. No new constants in any object.
## 5 · Files (PACK-22, incl. this bridge + MANIFEST): see MANIFEST-PACK-22.txt (t7c_dyaudit/.jsonl · t7c_hfsr/_run/.jsonl · t7c_corr_all/.jsonl ·
t7c_pol_s22.jsonl · t7c_4c/.jsonl · t7c_corr2/.jsonl · PREDICTION/FINDING-{DYAUDIT,HFSR,CORR-ALL,4C,CORR2} · COMPARE-FK · READ-GB-ZETA ·
DERIVE-4AB · DERIVE-4B-KAPPA · TABLE-CHAIN-15 · RUN-{HFSR,CORR-ALL,CORR2} · FAULT-F22_1). Runtime: README-HANDOFF-22.
Bring next: LOWDIN-HANDOFF-22 (single superset: HANDOFF-21 + PACK-22 + README + verify22.sh) + project files.
## 6 · Unread / owed
Unread inventory of the compendia unchanged (R 1668). Hoffman 1992 unread. Owed: T4 writing chat (R 1701-1836); regeneration under F22.1.
Container clean at close: rt/ holds no file outside the packs except gate-appended rows already restored.