# BRIDGE — THE LÖWDIN SESSION 18 (2026-08-16)
Successor to BRIDGE-LOWDIN-SESSION-17.md. Bank restore-point-2_13 (R 1700) UNCHANGED; nothing written to register/index/store.
Archive verified: HANDOFF-17 271/271 (sha e13cf90c). Gates 1-4 PASSED at open (derive_P3 byte-identical; probe13 exact; t5_scf
Sc/La banked; t7c H 1s -0.5000064, Z=70 -2634.8449, pol gate 26 -0.378). Chats/transcripts reviewed first (LCP15 = session 17).
## 1 · Rulings in force
T7 all three run; comparison decided for T7c (session 17-18). M (this session): T7b Go; F18.1 foreign builder: audit and adopt if
gates pass (adopted); sum test RUN (retired on the run); Ra II/Th/Lr SR re-probe RUN. T4 writing chat LAST. Chapter 34 gated
on closure. Standing preference: always both objects. Handoff = single superset archive per session; §H.10 at 90 %.
## 2 · Findings
T7b CLOSED (FINDING-T7B-SESSION-18.md, RUN-T7B-SESSION-18.txt): numerical HF, av-config, inhomogeneous Numerov (shoot_x.c), no
constant. Gates: He 1s -0.91796, Ne 2p -0.85041 (Fischer 1977, exact to 5 digits); Dirac switch regenerates T5 HFS-TS exactly;
Janak form HF-TS = eps(N-1/2)+J~/2 verified vs dSCF (Sc -0.2681/-0.2736). Exact exchange removes about HALF the 4f offset (+0.105
Dy -> +0.123 Yb, growing), NO leverage on 5d (|shift| <= 0.005), BREAKS Cu (+27 %). PB1 FAILS 1/4, PB2 HOLDS 10/10 (TS/dSCF <= 2 %),
PB3 FAILS (Cu), PB4 cannot fire. Direction stays T7c. Answer to bridge-17 s3(1): exchange language moves neither the 5d edge nor
the mixed-sign 4f scatter. Provenance F18.1: builder + 5 rows found in the container from an abandoned branch of this chat (no
other chat open, per M); quarantined with SHAs (pack18/foreign/), audited (3 gates), rows reproduced to the digit, then adopted.
SUM T7c+T7b RETIRED (SUM-T7-SESSION-18.txt): additive form (additivity <= 0.003 validated s17); 4f overshoot shallow +14..+35 %
(avg) / +30..+47 % (pol); 1/4 in band; Cu breaks. R 1449 timing on the sum. Prediction (overshoot) held.
SR RE-PROBE (FINDING-T7C-RESIDUE-SESSION-18.md): Ra II d(6d-7s) -0.0018 -> +0.0451 vs meas +0.055 -> Ra II residue CLOSED to
0.010 Ha by relativity alone (PR1 holds). Th IV hold preserved (PR2 holds). Lr I moves AWAY (+0.028; nonrel already +0.18):
scalar frozen kernel cannot reach 7p<6d — spin-orbit + self-consistency needed (Eliav 1995/Sato 2015 boundary, now located,
PR3 fails). Sr II control +0.011 only: not relativistic.
Faults: F18.1 (foreign artefacts, quarantined not overwritten); F18.2 (snap guard refused a deliberate dedupe of a duplicated
Gd row; duplicate kept as pack18/foreign/t7b_dup6.jsonl; guard rule stands).
STANDING AFTER SESSION 18: relativity owns the 4f offset AND the Ra II residue; SIC and exact exchange have no leverage on the
observable. Open residues: mixed-sign 4f scatter (0.02-0.04 Ha, SR-pol), 5d shallow systematic growing La->Lu (relativistic
destabilisation), Sr II / Ce IV / Pr V nonrelativistic onsets (T0 family, closed negative), Lr I (spin-orbit boundary).
## 3 · Next chat, in order (candidates; each needs a ruling)
(1) SELF-CONSISTENT SR re-probe of Ra II, Th IV, Sr II, Ce IV, Pr V, Lr I with t7c_kernel.scf_occ_sr (indirect effect included) —
    smallest build, gate = c->inf regenerates T0b_pairs SCF column. Predictions to be written BEFORE the run.
(2) Spin-orbit kernel (j-resolved, two-component) for Lr I and the 5d edge — larger build; only if (1) leaves Lr/5d open.
(3) The 4f scatter under SR-pol: is it the channel/multiplet coordinate (R 1665 mult question) rather than the kernel? Ruling.
(4) T4 writing chat LAST: R 1701-1792 (bridge-17) + R 1793 T7b closure · R 1794 sum retired · R 1795 Ra II closed by SR ·
    R 1796 Lr boundary located · R 1797 F18.1 · R 1798 F18.2 · R 1799 Janak-form HF-TS as the observable-consistent TS.
## 4 · Figures (§H.6)
MEASURED: none new. RECALLED-NOT-ENTERED: Fischer 1977 He/Ne HF eps and totals used as gate standards (quoted from PREDICTION-T7);
Lr I 7p<6d order (Eliav 1995 / Sato 2015) used as ORDER only, no number entered. CHOSEN: none. c = 137.035999 CODATA.
## 5 · Files (PACK-18): t7b_hf.py t7b_run.py t7b_gate.py t7b_score.py t7sum.py t7c_residue.py shoot_x.c t7b.jsonl
RUN-T7B-SESSION-18.txt SUM-T7-SESSION-18.txt RUN-T7C-RESIDUE-SESSION-18.txt FINDING-T7B-SESSION-18.md
FINDING-T7C-RESIDUE-SESSION-18.md BRIDGE-LOWDIN-SESSION-18.md MANIFEST-PACK-18.txt foreign/ (quarantine record).
Runtime: as README-HANDOFF-18 (rt/): pack18/*.py *.c *.jsonl into rt/, gcc shoot_x.c -> libshoot_x.so.
Bring next: LOWDIN-HANDOFF-18 (single superset: HANDOFF-17 + PACK-18 + README + verify18.sh) + project files.