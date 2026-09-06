# RESULT S93 ITEM 1 -- AT THE SEALED PAIR, P IS AN EIGENVALUE QUANTITY TO 1%; THE s92 0.06 Ha RESIDUE WAS AN OBJECT MISMATCH
# prediction pack93/PREDICTION-S93-ITEM1-DZ.md sha256 580402f4 (hashed before any solve). ruling: Go (M, s93 open).
# can-fails (row 38): A lever-dead (solve B := solve A, dZ'=0) rc=4 PASS; B control-validity (Drep+0.01) rc=4 PASS. Non-vacuous.
# instrument pack93/dz93.py; 4 solves per row, 20 solves, rung 0 x20; Drep reproduced the sealed D(Z*) 5/5 to 5 dp. CORR=False asserted in-instrument.

## Object. Koopmans ionization form on the N+1 systems, SAME pair (Z*-1 -> Z*) and SAME core cfg(Z*-2) as P (swing91.py):
##   dZ' = eps_c[Z*;cfg(Z*-2)+c] - eps_c[Z*-1;cfg(Z*-2)+c]     dN' = eps_c[Z*;cfg(Z*-1)+c] - eps_c[Z*;cfg(Z*-2)+c]     rho' = dN'/|dZ'|
## Table (Ha)
 Z*  own   epsA      epsB      epsC      dZ'       P         P-dZ'     rel_P   dN'      S        rel_S   rho_sealed rho'   diff
 38  5s   -0.14002  -0.38459  -0.18125  -0.24456  -0.24407  +0.00049  +0.002  0.20334  0.20914  -0.028   0.857    0.831  -0.026
 56  6s   -0.12821  -0.34516  -0.16317  -0.21695  -0.21640  +0.00055  +0.003  0.18199  0.18687  -0.026   0.864    0.839  -0.025
 58  5d   -0.23566  -0.56957  -0.28365  -0.33391  -0.33658  -0.00267  -0.008  0.28592  0.29658  -0.036   0.881    0.856  -0.025
 90  6d   -0.17690  -0.46983  -0.21725  -0.29293  -0.29357  -0.00064  -0.002  0.25258  0.26025  -0.029   0.887    0.862  -0.025
 91  6d   -0.21725  -0.52120  -0.25501  -0.30395  -0.30686  -0.00291  -0.009  0.26618  0.27440  -0.030   0.894    0.876  -0.018
## Scoring
K1 HELD 5/5: dZ' < 0.
K2 VALUE HELD 5/5: |P-dZ'|/|P| = 0.002..0.009 < 0.10 (s92 mismatched object: 0.18..0.27). K2 SIGN FALSIFIED 2/5: P-dZ' > 0 at s rows
   (38,56: +0.0005), < 0 at d rows (58,90,91: -0.0006..-0.0029). Signed by l_own, same species as S-S1 in s92 item 1. |P-dZ'| <= 0.003 Ha.
K3 HELD 5/5: |dN'-S|/S = 0.026..0.036 < 0.05 (dN' identical to s92 dN: epsB == s92 eps_ref, same solve).
K4 HELD 5/5 (predicted >=4/5): |rho'-rho_sealed| = 0.018..0.026 < 0.05. rho' is a plateau: 0.831..0.876, spread 0.045; deficit uniform -0.025 (x4), -0.018.
K5 HELD: spread of P-dZ' = 0.0035 Ha < 0.02.
K6 HELD: rung 0 x20; Drep 5/5.

## What is derived
 (i) At the sealed object, BOTH sides of the 0.88 are eigenvalue quantities of the field: P = dZ' to <1%, S = dN' to 3%.
     rho_sealed = rho' + delta, delta = +0.018..+0.026. The 0.88 IS an eigenvalue relation (L5-addressable) up to delta.
 (ii) Exact arithmetic (no new solve): with Rel(Z,core) := D(c;Z,core) - eps_c[Z;core+c] >= 0 (Koopmans inequality; held 15/15, 0.0004..0.038 Ha):
       P - dZ' = Rel(Z*,cfg2) - Rel(Z*-1,cfg2) = +0.0005 (s) / -0.0006..-0.0029 (d)     -- one proton barely moves the relaxation energy
       S - dN' = Rel(Z*,cfg1) - Rel(Z*,cfg2)   = +0.0049..+0.0107, > 0 5/5               -- the own-shell partner adds relaxation energy
     Rel table: s rows 0.0004/0.0009/0.006; d rows 0.019..0.038 (d relaxes 20-30x more than s in the cation-pair solves; in the sealed
     solve 5-6x). delta = (S-dN')/|P| - (dN'/|P|)(P-dZ')/|dZ'| ~ (S-dN')/|P| to leading order: the 0.025 deficit is the screening-side relaxation.
 (iii) s92 §3 conclusion "P is NOT an eigenvalue quantity; L5 cannot close the 0.88 alone" is WITHDRAWN: it compared P (pair Z*-1->Z*,
     core cfg(Z*-2)) to dZ (pair Z*->Z*+1, core cfg(Z*-1)). The s92 residue R = P - dZ ~ 0.06 Ha is DISCHARGED as an object mismatch, not as physics.
## Residue after this item (named, Rule A): delta = rho_sealed - rho' = 5 numbers, +0.018..+0.026, == relaxation-energy differences
##   S-dN' (5 numbers, +0.005..+0.011) and P-dZ' (5 numbers, |.|<=0.003, l-signed). Field-computed. NOT discharged. Item 2 target changes:
##   derive S-dN' = Rel(Z*,cfg1)-Rel(Z*,cfg2) (sign > 0 exact by Koopmans? NO -- Koopmans gives each Rel >= 0, not their difference) and P-dZ'.

## Faults
F93.1 SEVERITY: conclusion-level (s92 §3 and the named residue R = P - dZ); no sealed row, gate, or D1-D5 touched. s92 item 3 scored P
   against a dZ of a different pair and core and filed a structural conclusion from the mismatch. Species: wrong population (12th instance).
   The s92 result itself carried the note; the conclusion was filed anyway. Corrected here; s92 files unedited (sealed).
F93.2 SEVERITY: hygiene. K2 SIGN prediction ("P-dZ' > 0 5/5, relaxation grows with Z") was filed without a mechanism that could distinguish
   s from d; falsified 2/5. Logged, not suppressed.
## Z=90 STOP rule: sealed reproduction at 90 selected 6d (Drep -0.19094 = sealed). No STOP.