# RESULT S92 ITEM 3 -- THE 0.88 IS NOT AN EIGENVALUE RELATION; THE PROTON SIDE CARRIES A FLAT ~0.06 Ha VARIATIONAL TERM
# prediction pack92/PREDICTION-S92-ITEM3-EPS.md sha256 c00e7835 (hashed first). can-fails A rc=4 PASS, B rc=4 PASS. instrument pack92/eps92.py. rung 0 x15.
 Z*  own  eps_ref    dN       S        dZ        P        rho_eps rho_sealed  dN-S/S  dZ-P/|P|  P-dZ
 38  5s  -0.38459  0.20334  0.20914  -0.30964  -0.24407   0.657   0.857     -0.028   -0.269   +0.06557
 56  6s  -0.34516  0.18199  0.18687  -0.26967  -0.21640   0.675   0.864     -0.026   -0.246   +0.05327
 58  5d  -0.56957  0.28592  0.29658  -0.40448  -0.33658   0.707   0.881     -0.036   -0.202   +0.06790
 90  6d  -0.46983  0.25258  0.26025  -0.35216  -0.29357   0.717   0.887     -0.029   -0.200   +0.05859
 91  6d  -0.52120  0.26618  0.27440  -0.36306  -0.30686   0.733   0.894     -0.030   -0.183   +0.05620
E1 HELD 5/5.  E2 FALSIFIED 0/5 (|rho_eps - rho_sealed| = 0.16..0.20).  E4 FALSIFIED (spread 0.076; monotone in Z, not a plateau).
E3 dN: HELD 5/5 (<= 3.6%): screening is Koopmans-exact -- an eigenvalue quantity.   E3 dZ: FALSIFIED 5/5 (18-27%).
## What is derived
 S is an eigenvalue object (L5-addressable, dN = S to 3%). P is NOT: P - dZ = +0.053..+0.068 Ha, a near-flat variational
 correction (spread 0.015 Ha) across s and d, Z=38..91. The 0.88 plateau is the ratio of an eigenvalue quantity to a
 total-energy quantity; L5 tools cannot close it alone. Residue renamed: R = P - dZ (5 numbers ~ 0.06 Ha). NOT discharged.
## Faults: none new. Note for S93: the eigenvalue analogue of P at the sealed Z pair (Z*-1 -> Z*, core cfg(Z*-2)) was NOT
 computed here (dZ used Z* -> Z*+1, core cfg(Z*-1), as filed); S93 should compute it before interpreting the 0.06 further.