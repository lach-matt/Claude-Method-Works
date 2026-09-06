# FAULT F21.1 (session 21) — Janak identity fails on t5_scf.scf_occ's total energy. Registered BEFORE kappa is read.
Observed (t7c_occ.jsonl, RUN-T7C-OCC-SESSION-21.txt): J = int_0^1 eps(q) dq vs D = Etot(1) - Etot(0):
  Sc 3d  J -0.2886  D -0.3561  J-D +0.0676 · Y 4d  J -0.2188  D -0.2783  +0.0594 · Cs 6s  J -0.1381  D -0.1891  +0.0510.
P2a predicted |J-D| <= 0.001. Failed by 50-70x. Same sign, similar size, on s and d alike -> systematic in the OBJECT, not the rows.
Candidate cause (stated before test): the Latter tail. Eigenvalues come from V_tailed = min(V_HFS, -1/r); Etot subtracts
-1/2 int n V_H - 1/4 int n V_x built from the UNTAILED V_H, V_x. So Etot = E_HFS[n] + int n (V_tailed - V_HFS), a NEGATIVE
term that grows with q (the entrant is the diffuse density). That makes D too negative and J - D > 0 -- the sign observed.
Consequence if confirmed: every banked "dSCF" from scf_occ Etot (and any t7c_kernel Etot with the same form, line 109) carries a
tail contamination of order 0.05 Ha per removed electron; the (b1) TS/dSCF split of s20 must be re-read against the corrected Etot.
Test: recompute D with E_HFS[n] proper (subtract the tail term); predict |J - D_corr| <= 0.002 on all three rows.
Status: OPEN until the test runs. kappa NOT read until this closes.
