# BRIDGE — THE LÖWDIN SESSION 31 (2026-08-17)
Successor to BRIDGE-LOWDIN-SESSION-30.md. Bank restore-point-2_13 (R 1700) UNCHANGED; nothing written to register/index/store. HANDOFF-30 verified 630/630;
gates 1-45 PASSED at open (values in the s31 transcript; the standing gate list is README-30's). §H.10: handoff begun at ~70 %, no running task left open.
## 1 · Rulings (M, s31)
(1) "Continue in order" -> bridge-30 §3 (1)(i)-(iv) and (2) executed. (2) M: "look at R and Z more exhaustively ... perhaps two parts of one mechanism,
triggered in each subshell" -> RZMECH opened (prediction first). (3) M: the solution is "a tree of mechanisms/truncations ... beginning at hydrogen"; Z+1
from Z is the target's walk (LCP3 Rule B; T0 ruling LCP10; R 1374) -> SPEC-WALK written, NOT opened (gated on the correlation form). (4) "Continue" -> third
form (ring + screened SOX) is the candidate: SPEC-SOSEX written; the build needs a full session and was NOT started (§H.10: do not open what cannot close).
GENERAL carried: SUBCELL=1; predictions before runs; R 1449 timing flags; comparison decides; no scans; no constant; T4 writing chat LAST.
## 2 · Findings (pack31; no constant beyond c; Cs/Y RECALLED-NOT-ENTERED; QMC benchmark values RECALLED, comparison only, NOT ENTERED)
(1) FINDING-E0B: E0B(zeta) = E0B(0) EXACTLY (scaling argument; Loos-Gill 2011 Tab.I Upsilon_0^b = 1). No code change; (1)(ii) is a no-op. Timing flag F31.1.
(2) COMPARE-RZ: 15 rows, corr='R' hook, both forms SUBCELL=1. PZ0 held (Z == s23 to 1e-4). R deeper on every row; R/Z shift ratio CLASS-RESOLVED, ordered by
    diffuseness: 3d 1.18 · 4f 1.16 · nd>=4 1.41 · 6s 2.32; sc-path and corrz-path agree (Sc 1.22/1.24, Y 1.38/1.38). 4f deepens only 0.006-0.007. Under R
    14/15 rows below the s23 U edge (bracket built under Z). Class-spread criterion NOT decisive (~0.002). PZ4 FAILED (Cs 2.32).
(3) FINDING-SCEPS0: Sc eps(f=1e-3) = -0.24630 vs linear extrapolation -0.23865 -> Sc Janak gap 1.2e-3 -> 8.7e-5 (quadrature, not Janak; flag closed).
    Extension (flagged): HF-path gap <= 1.1e-4 on all six class rows; corr-path gap 2-3.5e-4 stays on Y La Gd Lu (bound, not opened).
(4) FAULT-F31.2 (before PM3 read): FINDING-RING's "RPA overbinding" reading is FALSE for form R = ring + BARE E0B: against the benchmark UEG both forms
    UNDERBIND at all r_s >= 1 (R - bench +0.005..+0.012, Z +0.013..+0.043; both zeta). Its inference "d-row object is not local" is withdrawn.
(5) FINDING-RZMECH: R and Z are ONE local eps_c evaluated to two orders; the per-subshell trigger is the entrant's correlation-weighted r_s: 4f 0.39-0.46,
    3d 0.65-1.25, nd>=4 1.87-2.07, 6s 6.8 (PM1 held). PM2 FAILED (R never over) and PM3 FAILED: the entrant-weighted local shortfall of R on nd>=4 is
    0.0044-0.0058 Ha = THE SIZE OF THE d-row OBJECT (Y +0.0051 Lu +0.0038 La +0.0016); 3d 0.0002-0.0034 (Sc largest), 4f 0.0006. The object is (at least
    mostly) the LOCAL form's missing screened exchange, triggered at r_s ~ 2; Sc is the anomaly (over under any local form). Cs: 40 % of 6s weight at r_s > 10.
    Timing flag F31.3 (window 0.5 -> 1.0 after first read; first pass kept). (6) FAULT-F31.4: the open-time foreign-file check was head-truncated; rerun
    to file: rt/ clean (only pack5's out/).
Failed predictions s31: PZ4 · PM2 · PM3 (PM2/PM3 are the findings). Timing flags: F31.1, F31.3.
## 3 · Next chat, in order (rulings first; predictions before runs)
(1) SPEC-SOSEX-SESSION-32: build candidate S = ring + coupling-averaged statically-screened (Lindhard, the ring's own) second-order exchange; gates G-S1
    (kappa->0 = E0B to 1e-4 at zeta 0 AND 1), G-S2, G-S3 (one MC point); PREDICTION-SOSEX first (PS-1..4 in the spec); table on the ring grid; corr_sosex.py;
    t7c_corrz corr='S'; 15 rows SUBCELL=1; COMPARE-RZS decides. Cost: one session. (2) SPEC-WALK-SESSION-32: the Z->Z+1 mechanism-increment test on banked rows
    (reading + one table; PW1-4) — after (1). (3) 4f +0.09 via Yb (second radial function; prediction first) — after (1), under form S. (4) Term-resolved
    Fe/Ni conditional. (5) Law statement: "one Hamiltonian, one chain of derived corrections, each with a physically fixed shell coordinate (n-l-1, l, N_sib,
    r_s window) that sets its weight; the aufbau is the map from those coordinates to the dominant correction; rooted at H" — after (1)-(3).
(6) T4 writing chat LAST: R 1701-1882 + s31: R 1883 E0B zeta-independent (derivation, F31.1) · R 1884 COMPARE-RZ (class-resolved ratio; not decisive) ·
    R 1885 Sc eps(0) by run (flag closed) · R 1886 F31.2 · R 1887 RZMECH (one mechanism; local d-row object; Sc anomaly) · R 1888 F31.4 · R 1889 tree/walk
    (M's frame; SPEC-WALK; prior art) · R 1890 candidate S opened by spec.
## 4 · Figures (§H.6): MEASURED none entered. RECALLED-NOT-ENTERED: Cs 0.14310, Y 0.2285; QMC eps_c(r_s,zeta) benchmark points (rz_mech.py, comparison only).
CHOSEN: prediction thresholds; rz_mech window r_s in [1,10]; f=1e-3 for eps(0). DERIVED: E0B(zeta)=E0B; ER, shift ratios; rs_w, rs_wc, dR_loc/dZ_loc (bounds).
## 5 · Files (pack31, 22): PREDICTION-{E0B,RZ,SCEPS0,RZMECH} · FINDING-{E0B,SCEPS0,RZMECH} · COMPARE-RZ · FAULT-F31.2, F31.4 · SPEC-SOSEX-32, SPEC-WALK-32 ·
t7c_corrz.py (hook) · t7c_corrRZ_run.py · t7c_corrz_sc.jsonl · t7c_corrR.jsonl · frachf_eps0.py/.jsonl · rz_mech.py/.jsonl/rz_mech_win05.jsonl · this bridge · README-31.
## 6 · Unread / owed: unchanged (R 1668; Dabo 2010, Borghi 2014); + 2603.23283 (single-pole SOSEX reduction, model only), Gruneis-Kresse 2009 / Ren 2013 (SOSEX
forms). Owed: T4 (R 1701-1890); PR3 (A/B/R under R); the walk test; candidate S build.
Container: rt/ beside the packs (t5_scf reads ../pack9/); rt/ holds nothing outside the packs except __pycache__ and the .so files (F31.4 census).