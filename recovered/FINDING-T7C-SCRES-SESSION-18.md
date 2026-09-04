# FINDING — self-consistent SR re-probe of the corridor residues (session 18, bridge-18 s3(1), ruled by M "continue")
Object: probe pair on the SELF-CONSISTENT HFS core of the ion (scf_occ / scf_occ_sr, tail Z-N_core), eigen/eigen_sr zeta=2. No constant.
Gate: Ra II c=1e6 regenerates nonrel d exactly (-0.04177). Predictions PS1-PS4 stated in chat before the run.
## Result (RUN-T7C-SCRES-SESSION-18.txt; d = E(second)-E(first), Ha)
Ra II 6d-7s : meas +0.055 | nr -0.042 | SC-SR +0.041 (shift +0.083; 7s deeper 0.047, 6d shallower 0.036 = indirect effect now present).
              Order corrected; 74 % of meas; 0.014 short. PS1 fails on magnitude only. Frozen-kernel value was +0.045 (s18 earlier).
Th IV 5f-6d : hold | -0.337 -> -0.155 : PS2 HOLDS.
Lr I  7p-6d : 7p<6d | +0.150 -> +0.068 : PS3 HOLDS (moves down 0.082, indirect 6d destabilisation +0.097). Remaining +0.068
              is the spin-orbit gap (7p1/2), the Eliav 1995 / Sato 2015 boundary now quantified at scalar level.
Sr II 4d-5s : meas +0.070 | +0.004 -> +0.022 (+0.018): marginal; residue mostly nonrelativistic.
Ce IV 4f-5d : meas -0.227 | -0.544 -> -0.423 (+0.121 toward): PS4 FAILS. Pr V 4f-5d : meas -0.524 | -0.886 -> -0.745 (+0.141 toward): PS4 FAILS.
## Reading (after the run, flagged)
Relativity is a substantial part of the f-onset residues too: Ce IV and Pr V move 0.12-0.14 Ha toward measurement by the indirect 4f
destabilisation, leaving 0.20 / 0.22 Ha — the same magnitude as the nonrelativistic shell-constant 4f offset of T5 (0.20-0.22 Ha),
which SR removed on the neutral 4f species. Observation only; whether the SC-SR-POL object (t7c_pol) closes Ce IV / Pr V is the next
smallest test (candidate; needs a ruling; prediction to be written first). Sr II remains the one nonrelativistic d-onset residue.
Standing: SC-SR corrects the ORDER of every relativistic residue (Ra II, Th IV) and locates the two boundaries (Lr I spin-orbit gap
+0.068; Ce IV/Pr V remaining -0.20/-0.22). No constant, no measured input, at any point.
## Files: t7c_scres.py t7c_scres.jsonl RUN-T7C-SCRES-SESSION-18.txt FINDING-T7C-SCRES-SESSION-18.md