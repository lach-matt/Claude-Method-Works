# PREDICTION S93 ITEM 1 -- dZ AT THE SEALED PAIR (same object as P). Written and hashed before any solve (R 1449).
## Object. P = D_fr(c;Z*) - D(c;Z*-1) with the SAME core cfg(Z*-2) on both sides (swing91.py). Channel c = own shell.
## The channel is UNOCCUPIED in cfg(Z*-2) at 38,56,58,90 (occupied, 6d1, at 91), so no virtual eps exists in hfc2 (eps only
## for occupied shells). The eigenvalue analogue is therefore the Koopmans IONIZATION form on the N+1 systems:
##   D(c;Z,core) ~ eps_c[Z; core+c]   (frozen-orbital removal from the N+1 system)
##   dZ' = eps_c[Z*; cfg(Z*-2)+c] - eps_c[Z*-1; cfg(Z*-2)+c]      (proton side, sealed pair, sealed core)
##   dN' = eps_c[Z*; cfg(Z*-1)+c] - eps_c[Z*; cfg(Z*-2)+c]        (screening side, same form)
##   rho' = dN'/|dZ'|.  Four solves per row: A=(Z*-1,cfg2+c) B=(Z*,cfg2+c) C=(Z*,cfg1+c) R=(Z*,cfg1); Drep=E[C]-E[R].
## s92 item 3 used dZ = eps_c[Z*+1;cfg1] - eps_c[Z*;cfg1] (core cfg(Z*-1), pair Z*->Z*+1): a different object. This item
## replaces it. Rule B declarations (bound-direction; sign/value-exact):
K1 SIGN-exact: dZ' < 0 on 5/5. (bound: eps deepens with Z)
K2 VALUE, bound-direction DOWN: |P - dZ'|/|P| < 0.10 on 5/5 (s92 mismatched object gave 0.18..0.27; claim is that >= half of the
   s92 gap was the object mismatch). SIGN: P - dZ' > 0 on 5/5 (relaxation energy of the N+1 system grows with Z).
K3 VALUE: |dN' - S|/S < 0.05 on 5/5 (s92 dN form gave <= 0.036).
K4 VALUE, bound-direction TOWARD 0.88: |rho' - rho_sealed| < 0.05 on >= 4/5 (s92 gave 0.16..0.20 off). If K4 fails while K2
   holds, the 0.06 residue is NOT an object mismatch and item 2 proceeds on R = P - dZ'.
K5 VALUE: P - dZ' spread (max-min) over 5 rows < 0.02 Ha (flatness survives the object change).
K6 HYGIENE: rung 0 on all 20 solves; Drep reproduces the sealed D(Z*) to 1.5e-5 on 5/5.
## Can-fails (non-vacuous, from outside the instrument): A lever-dead: reuse solve A as solve B -> dZ'=0 -> rc=4 expected.
## B control-validity: Drep + 0.01 -> control check fires -> rc=4 expected. CORR=False confirmed read (nlchain.py:17) before filing:
## no correlation claim is made in this item (F92.3 guard).
## Mechanism if K2 fails: the 0.06 is real total-energy relaxation, not Koopmans form; item 2 derives it. If K1 fails: instrument fault.