# FINDING — T7c-OCC: occupation dependence of the local TS object (session 21). Bridge-20 §3(2). Files: t7c_occ.py .jsonl (tailed),
t7c_occ_diag.py .jsonl (tail term + untailed), RUN-T7C-OCC-SESSION-21.txt, PREDICTION-T7C-OCC-SESSION-21.md, FAULT-F21_1-SESSION-21.md.
Object: t5_scf.scf_occ (spin-AVERAGED local HFS, Dirac exchange), nonrel. Rows Sc 3d, Y 4d, Cs 6s; eps(q), Etot(q), q = 0..1.
## F21.1 (registered before reading, then CLOSED): Janak identity FAILS on the banked tailed object, J - D = +0.068/+0.059/+0.051 Ha.
Cause tested and confirmed: the Latter tail. Etot carries int n (V_tailed - V_HFS) = -0.089 Ha at q = 1 (Sc), ~0 at q = 0; and on a
tailed potential eps is not dE/dq at any q. UNTAILED (qtail = 0) the identity holds to <= 0.0003 Ha on all three rows.
CONSEQUENCE (for the register): every banked `dscf` from scf_occ/t7c_kernel Etot is a TAIL-CONVENTION number, not a functional property
(Sc dSCF moves 0.11 Ha between tail choices; banked t5 -0.2494 used tails 1/2). s20 (b1)'s "TS/dSCF split is a local-exchange property"
must be re-read: the split it measured is tail-conditioned. TS EIGENVALUES ARE UNAFFECTED (eps(1/2) = -0.2752 banked reproduced exactly).
## Score (untailed, where kappa = eps(1/2) - int eps dq is defined)
Sc 3d  eps(1/2) -0.2693  J = D = -0.2756  kappa +0.0063 · Y 4d  -0.2034  J -0.2071 D -0.2072  kappa +0.0037 · Cs 6s  -0.1174  J -0.1173  kappa -0.0001.
P2a  held only after F21.1 (untailed) -- on the banked object it FAILED (that was the fault).
P2b  Cs HELD (|kappa| <= 0.005). Sc/Y FAILED on magnitude: kappa 0.004-0.006, predicted 0.01-0.03; sign (>0) held.
P2c  FAILED: kappa(Y) < kappa(Sc), opposite to the SHELL ordering Sc +0.011 < Y +0.013.
## Reading (bound, P8): the half-occupation TS approximation owns AT MOST 0.006 Ha of the d-class shallowness and its ordering is wrong.
The shallowness sits in the FUNCTIONAL, not in the TS step. Slater's exact TS (Janak integral) is NOT the derivable replacement.
Additional bound read off the same rows: the Latter tail carries binding of 0.006 (Sc 3d) / 0.005 (Y 4d) / 0.014 (Cs 6s) Ha at q = 1/2 --
an asymptotic self-interaction fix that reaches the diffuse s entrant and barely the compact d one. Interpretation offered, not claimed:
the residual local-exchange self-interaction on the LOCALISED entrant is what the tail cannot remove, which is the shell order s < d < f
of bridge-20's finding. This is consistent with s17's PZ-SIC magnitudes (-0.001..-0.010, deepening) but SIC on 5d is UNRUN (s21 read (1)).
Faults: F21.1 (closed). Predictions failed: P2b (Sc, Y magnitude), P2c. No constant, no measured input; recalled Sc 3d removal 0.2946,
Y IP 0.2285, Cs IP 0.1431 comparison only.
