# PREDICTION — 4c: re-read s20 (b1) "TS/dSCF split is a local-exchange property" against UNTAILED dSCF on 5d (La/Gd/Lu), SR object
(t7c_kernel.scf_occ_sr, spin-averaged). Ruled s22. Written BEFORE run. 9 SCFs (q = 0, 1/2, 1 untailed per row).
Banked (tailed): La ts -0.2017 dscf -0.1816 (split +0.020) · Gd -0.1905/-0.1671 (+0.023) · Lu -0.1631/-0.1333 (+0.030).
 P4c1  Untailed Janak holds on the SR object: |int eps dq (Simpson 3-pt ~ eps(1/2)+eps''/24 not available; use E(N)-E(N-1) vs eps(1/2)-kappa)|:
       untailed dSCF_SR - eps_ut,SR(1/2) = -kappa_SR with kappa_SR = 0.002-0.005 (nonrel 5d kappa 0.0024/0.0030/0.0037).
 P4c2  The tailed split (+0.020..+0.030) collapses untailed to |split| <= 0.005 on all three -> s20 (b1)'s split is TAIL-CONDITIONED (F21.1),
       and the SR contribution to the split (tailed SR - tailed NR: La 0.007) is also tail-conditioned.
 P4c3  Untailed SR dSCF vs banked tailed SR TS: |dSCF_ut - ts_tailed| <= 0.003 (the 4b coincidence, SR object) on all three.
No constant, no measured input.