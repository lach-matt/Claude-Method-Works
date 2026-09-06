# BRIDGE — THE LÖWDIN SESSION 20 (2026-08-16)
Successor to BRIDGE-LOWDIN-SESSION-19.md. Bank restore-point-2_13 (R 1700) UNCHANGED; nothing written to register/index/store.
Archive verified at open: HANDOFF-19 316/316 (manifest sha 16bde877b4aa2284). Gates 1-7 PASSED at open (derive_P3 byte-identical; probe13 exact;
t5_scf Sc/La banked; t7c H 1s -0.5000064, Z=70 -2634.8449, pol 26 -0.378; t7b He -0.91796 Ne -0.85041, hfs-switch Sc/Fe; Ce IV bare -0.42268;
La 5d E_ts -0.2079 zeta 0.00308). Container clean at open and at close (F18.1: rt/ has no file outside the packs; out/ is pack5's checkpoints).
Project knowledge read first (§H, R 1697). Handoff begun at ~80 % (deviation from M's "after 90 %", stated in chat: build cost ~10 %, R 1667).
## 1 · Rulings in force (M, this session)
Order (c)(b)(a)(d) smallest-first CONFIRMED and executed. Then (i)(ii)(iii) ALL run and compared. R 1449 reclassification of s19 PM1 RULED and
written (RECLASS-R1449-S19-PM1-SESSION-20.md). Handoff trigger 90 % (M: handoff READY before 100 %, not begun at 90 % exhaustion). Chapter 34
gated on closure. T4 writing chat LAST. Standing: both objects; no constant; no measured input; recalled values comparison only.
## 2 · Findings (all no constant, no measured input; c = 137.035999 only) — files in §5
(c) TAIL: floor -(q-1/2)/r moves 5d by +0.004/+0.005/+0.006 La/Gd/Lu, SR and nr equally -> WRONG SIGN, ruled out. PC1 failed at Lu (0.0057).
(b1) TS/dSCF split is a LOCAL-EXCHANGE property (nr -0.019/-0.022/-0.025; HF +0.002..+0.003); SR adds <= 0.005 -> not the missing relaxation.
(b2) SR DECOMPOSITION (t7c_srdec.py, c per orbital): the SR 5d shift is ENTIRELY INDIRECT: La all +0.0266 = 5d-only -0.0083 + not-5d +0.0335
   (6s +0.0172, core +0.0174); Lu all +0.0398 = -0.0159 + 0.0512 (6s +0.033). Direct-magnitude clause FAILED (>0.005), sign held.
(a) MacDonald-Vosko relativistic exchange: -0.0008 on 5d La and Lu (3 % of edge) -> ruled out; Dy 4f -0.006 (PA2 failed marginally).
(d) LEVEL-TO-LEVEL SO on 4f (Lande, zeta_4f derived 0.0094/0.0117/0.0130/0.0143 Dy/Er/Tm/Yb; E' = corr + (zeta/2)(L_ion-L_n)):
   Dy -7.8 %, Er +4.2, Tm +6.6, Yb +6.5 (Yb shift = 1.5 zeta = 0.0215 exactly). PD1 held (Dy not closed); PD2 failed (Dy stays over-bound).
   -> R 1449 RECLASSIFICATION (ruled): s19 PM1 4/4 was centroid-vs-level; on levels 1/4; structural claim (R 1665) stands; Yb 0->0 accidental.
(iii) 4f decomposition at Yb: total +0.1923 = direct -0.0153 + indirect +0.2033 (6s 22 %, core 78 %). Shared 0.02 shallowness is 10 % of the 4f
   SR term, ~90 % of the 5d one -> not a common fractional fault; what shells share is ADDITIVE ~0.02.
(i) SR s-contraction is RIGHT: hydrogenic Z=57 5s/6s SR == Dirac s1/2 to 4 decimals; Cs/Ba 6s SR-pol TS +2.0/+3.1 % vs recalled IPs, SR shift
   -0.005/-0.006. Bound read: nonrel HF-HFS on entrant -0.005..-0.001 (5d) but +0.105..+0.123 (4f); SR-HF 4f object never run.
(ii) Hund-II CI AUDIT: degeneracies, particle-hole symmetry (f4==f3, f5==f2), f2 closed forms to 5 decimals ALL HELD. s19 f3 4F/4S flag RESOLVED
   as structural (E(3F) = f2 triplet-manifold average is an exact identity). Dy over-binding is not a bookkeeping fault. F^k scale is a constant: excluded.
SHELL FINDING (read across banked rows, then tested predictively on Y 4d): the local-exchange spin-polarised TS object UNDER-BINDS the entrant,
   s <= 0.006 (Cs/Ba), d 0.01-0.03 in EVERY period (Sc +0.018, Y +0.028, Fe +0.030, Cu +0.014, La/Gd/Lu +0.026/+0.025/+0.022 after SO),
   f 0.011-0.0215 (Er/Tm/Yb after Hund-II + level SO); Dy -0.021 the sole over-bound row. Present NONREL (Sc +0.011, Y +0.013, La +0.004);
   NOT created by SR (which is right where testable). Indirect SR destabilisation of d entrants monotone: 3d +0.007, 4d +0.014, 5d +0.027.
   Bridge-19's "5d-specific SR-step edge" is superseded: the 5d edge is the d-class shallowness, which on 5d happens to equal the SR shift.
STANDING AFTER SESSION 20: THE ONE OPEN SYSTEMATIC is a shell-ordered additive under-binding (~0.01-0.03 Ha) of the local-exchange TS object on
   localised entrants (d, f) at occupation 1/2, plus Dy over-bound by 0.021. Interpretation offered, not claimed: local-exchange self-interaction
   not removed by Slater TS -- but bridge-19 records a SIC trial that did not change the 5d sign (magnitude not on record; ask before re-opening).
Faults this session: none. Predictions failed: PC1(Lu), direct-magnitude clauses in (b2)/(iii), PA2, PD2, Y SR-shift clause. All in the FINDINGs.
## 3 · Next chat, in order (candidates; each needs a ruling; predictions first; smallest first)
(1) Locate the s19/earlier SIC trial in the packs (grep 'sic' in packs 12-18) and READ its magnitude on 5d before anything else. Read, not run.
(2) A DERIVABLE occupation-dependence test on the cleanest rows (Sc 3d, Y 4d, Cs 6s): TS at q = 0.5 vs Slater's exact TS (dE/dq integrated) vs
    dSCF, all in the local object -- does the d-class shallowness sit in the TS approximation or in the functional? Cheap; nonrel suffices.
(3) The SR-HF entrant object: NOT a one-block job (needs an SR inhomogeneous Numerov: shoot_x.c + the numerov_wf_sr transformation). Prediction
    on record (FINDING-T7C-SHELL): 5d edge ~unchanged; 4f ~0.1 SHALLOW under HF -> HF is not a closure for f. Open only by ruling.
(4) Dy: the only over-bound row. Level bookkeeping of the hole (Dy II 4f9 6s2 6H15/2) is the audit target; CI cleared.
(5) T4 writing chat LAST: R 1701-1808 (bridge-19) + s20: R 1809 (c) out · R 1810 (b1)(b2) indirect · R 1811 (a) out · R 1812 level SO on 4f ·
    R 1813 RECLASS s19 PM1 per R 1449 · R 1814 (i)(ii)(iii) compared · R 1815 f3 4F/4S resolved structural · R 1816 SHELL finding + Y 4d ·
    R 1817 handoff begun at 80 % by R 1667 (deviation stated).
## 4 · Figures (§H.6)
MEASURED: none entered. RECALLED-NOT-ENTERED (comparison only): Cs IP 0.14310, Ba 0.19153, Y 0.2285 Ha; Yb II zeta_4f ~0.013.
CHOSEN: prediction thresholds 0.005 / 0.010 / 5 % / 0.01-0.03, each stated before its run. c = 137.035999 CODATA. No new constants in any object.
## 5 · Files (PACK-20, 29 files): t7c_tail.py .jsonl RUN-T7C-TAIL FINDING-T7C-TAIL · t7c_srdec.py .jsonl RUN-T7C-SRDEC RUN-T7C-SRDEC-4F
FINDING-T7C-SRDEC · t7c_mv.py .jsonl RUN-T7C-MV FINDING-T7C-MV · t7c_so4f.py .jsonl RUN-T7C-SO4F FINDING-T7C-SO4F · t7c_6s.py .jsonl RUN-T7C-6S ·
t7c_mult_audit.py RUN-T7C-MULT-AUDIT · FINDING-T7C-COMPARE · RECLASS-R1449-S19-PM1 · FINDING-T7C-SHELL · t7c_4d.py .jsonl RUN-T7C-4D ·
BRIDGE-LOWDIN-SESSION-20.md · MANIFEST-PACK-20.txt (all -SESSION-20). Runtime: README-HANDOFF-20 (adds cp pack20/*.py pack20/*.jsonl rt/).
Bring next: LOWDIN-HANDOFF-20 (single superset: HANDOFF-19 + PACK-20 + README + verify20.sh) + project files.
## 6 · Unread / owed
Unread inventory of the compendia unchanged (R 1668, ~150,000 words). Owed: T4 writing chat (R 1701-1817). Chapter 34 gated on closure.
Handoff verified below by verify20.sh and gate rerun (see README-HANDOFF-20).
