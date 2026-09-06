# FINDING — T7B, exact (Fock) exchange on the entrant channel (session 18, 2026-08-16)
Bank restore-point-2_13 (R 1700) unchanged. Findings only. Species per T7-BUILD-SPEC (Dy Er Tm Yb | Fe | La Gd Lu | Sc Cu).
## Instrument
t7b_hf.py: numerical HF, average-of-configuration (Slater; Froese Fischer 1977 method), inhomogeneous two-sided Numerov
(shoot_x.c) in y = r^-1/2 P on x = ln r, eps fixed by ||P|| = 1, nodes checked; direct (q_b - d_ab) Y0_bb/r; within-shell
exchange (q_a-1)(2l+1)/(4l+1) sum_{k>0} c_k Y^k_aa/r local; cross-shell 1/2 q_b sum_k c_k Y^k_ab P_b/r inhomogeneity;
E = 1/2 sum q(eps+I). No constant. Same 4000-pt log mesh, same seed (scf_occ), same objects as T5.
PROVENANCE (F18.1): builder + first five rows were found in the container at session-18 open, written by an abandoned
branch of this chat (no other chat open — M). Quarantined (s18-foreign/, sha a15586c8dcf04d1b t7b_hf.py, b7d2458412c8552a
t7b_run.py, ac6c4bbaff5d5d4f shoot_x.c, 595748499c8a28c9 t7b.jsonl with a duplicated Gd row). M ruled: audit and adopt if gates pass.
## Gates (all before any new row was read)
A  He 1s eps -0.91796 (std -0.91796), E -2.86170 (HF -2.86168); Ne 2p eps -0.85041 (std -0.85041), E -128.54706 (HF -128.5471).
B  mode='hfs' (Dirac local, Latter tail) regenerates T5 HFS-TS: Sc -0.2752, Fe -0.4925 exactly.
C  Janak form: av-config HF has dE/dq = eps + J~/2 (within-shell term q(q-1)/2 J~); Sc eps_half -0.5624, J~ 0.5886,
   eps+J~/2 -0.2681 vs dSCF -0.2736; identical to the branch's Sc row -> foreign rows reproduce. ADOPTED.
   HF-TS := eps(N-1/2) + J~/2 (raw eps kept as hf_eps_half). This is the observable-consistent TS in this language.
## Results (RUN-T7B-SESSION-18.txt; Ha; % vs measurement)
4f  HF-TS Dy -0.3889 (-42%), Er -0.3997 (-56%), Tm -0.4030 (-42%), Yb -0.4048 (-24%). Shift vs HFS-TS +0.105/+0.114/+0.119/+0.123,
    growing Dy->Yb: exact exchange removes about HALF the shell-constant 4f offset (offset 0.20-0.22 Ha) and leaves the
    nonrelativistic Dy->Yb deepening. dSCF within 1.2% of TS everywhere.
5d  La -0.2329 (+2.4%), Gd -0.2262 (+6.4%), Lu -0.2038 (-2.2%): shifts -0.005/-0.003/-0.001 -> exchange language has NO
    leverage on 5d. The 5d band-edge under SR (T7c) is relativistic, not exchange.
3d  Sc -0.2681 (+9%), Fe -0.4413 (-11%) hold; Cu -0.2806 (+27%) BREAKS the control (shift +0.116; HFS had Cu at -3%).
## Predictions scored (PREDICTION-T7-SESSION-16, unchanged)
PB1 FAILS (1/4 within 30%: Yb only). PB2 HOLDS (10/10 within 10%; in fact <= 2.2%). PB3 FAILS (5/6; Cu). PB4 cannot fire.
## Reading (flagged as after-the-run, R 1449 timing on any use)
Comparison rule: T7c moved all four 4f into the band without breaking 3d; T7b moves 4f half-way, breaks Cu, leaves 5d.
Direction stays T7c. The candidate SUM (bridge-17 s3(2)) computed as arithmetic only, not run: t7c_ts + shift_ts gives
Dy -0.223 (+19%), Er -0.221 (+14%), Tm -0.217 (+24%), Yb -0.212 (+35%) -- overshoot; on the SR-pol object worse. Not
"each partly right": HF's half-shift is not additive to a relativistic shift that already closed the offset. Ruling owed.
Answer to bridge-17 s3(1): the exchange LANGUAGE does not move the 5d edge and does not address the mixed-sign 4f scatter.
## Faults
F18.1 foreign artefacts of unknown provenance in the working container (abandoned branch); quarantined and audited, not overwritten.
F18.2 snap guard refused a deliberate dedupe (6->5 rows); archived duplicate kept as t7b_dup6.jsonl, guard rule stands.
## Files
t7b_hf.py t7b_run.py t7b_gate.py t7b_score.py shoot_x.c t7b.jsonl RUN-T7B-SESSION-18.txt FINDING-T7B-SESSION-18.md