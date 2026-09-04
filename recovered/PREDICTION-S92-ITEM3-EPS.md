# PREDICTION S92 ITEM 3 -- IS THE 0.88 AN EIGENVALUE RELATION?  Filed before any solve. Instrument pack92/eps92.py.
# Own rows only (38:5s 56:6s 58:5d 90:6d 91:6d). c the only number.
## Definitions (all full SCF, rung ladder, eps = Fock eigenvalue of the own shell)
  ref   = (Z*, cfg(Z*-1))          eps_ref  = eps_own(ref)
  +N    = (Z*, cfg(Z*-1)+own)      dN = eps_own(+N) - eps_ref     (one more own electron: screening, > 0)
  +Z    = (Z*+1, cfg(Z*-1))        dZ = eps_own(+Z) - eps_ref     (one more proton, same configuration: collapse, < 0)
  rho_eps = dN / |dZ|
## Predictions
  E1 SIGN  dN > 0 and dZ < 0 on 5/5.
  E2 VALUE |rho_eps - rho_sealed| <= 0.05 on 5/5  (rho_sealed = 0.857 0.864 0.881 0.887 0.894).
  E3 VALUE |dN - S|/S <= 0.15 and |dZ - P|/|P| <= 0.15 on 5/5 (the total-energy pieces are eigenvalue pieces to 15%).
  E4 PLATEAU rho_eps spread over the 5 rows <= 0.06.
  If E2,E4 hold: the residue R is the eigenvalue relation dN = rho * |dZ| with rho ~ 0.88, one object, L5-addressable.
## Can-fails: A lever dead (+N solve replaced by ref -> dN = 0 -> rc=4). B control: ref solve must reproduce sealed
  D(Z*,own) = E(+N)-E(ref) to 5 dp, perturbed +0.01 -> rc=4.