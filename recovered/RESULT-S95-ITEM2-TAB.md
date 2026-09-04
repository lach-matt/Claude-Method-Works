# RESULT S95 ITEM 2 -- EXCHANGE-PROJECTED zeta AS A SECOND FULL COLUMN (so94 r_x; jsel94 J1-J4 under zeta_x). TABULATION ONLY, NO SOLVE.
# instrument pack95/tab95.py; output pack95/tab95.txt, tab95.json. Consumes pack94/so94.jsonl + sealed rt/nlchain.jsonl.
# can-fails: A column-dead (zeta_x := zeta_loc -> max|r_loc - r_x| = 0) rc=4 PASS; B non-vacuity (zeta_x x10 at 115 -> J3_x 3/4 vs J3_loc 4/4) rc=4 PASS.
## SEVERITY LINE: no verdict changes. VALUE-exact, bound-direction NONE (sensitivity column). Nothing sealed touched.
## Findings
T1 zeta_x/zeta_loc = 0.945..0.999 on all l>0 rows (min at 4f/5f); no row's verdict moves.
T2 so94 under zeta_x: 94/94 scored l>0 rows r_x < 1; max r_x 0.850 (Z=105; loc 0.854); first r>=1 at Z=113 under BOTH columns.
T3 jsel94 under zeta_x: J1 10/10, J2 6/6, J3 4/4, J4 4/4 -- identical to zeta_loc. Tightest j-margin (J3, Z=113, 7p3/2 over 8s) +0.01896 Ha (loc +0.01891).
T4 7p-block r(113..118) = 2.024 2.023 2.030 2.051 2.082 2.124 (spread 0.10). zeta grows 3.80x across the block while m grows 3.62x: the near-constancy
   of r is the near-proportionality of first-order zeta(7p) and the sealed 7p-vs-8s margin across one block.
## OPEN QUESTION (named, NOT a residue; no clause depends on it): OQ-95.1 "Why is Delta_SO(7p)/m(Z) ~ 2 uniformly over 113-118?" Both numerator
## (Z/r^3 expectation of 7p on the SR field) and denominator (D(8s)-D(7p)) scale nearly linearly with the 7p occupancy across the block; a
## mechanism would be a statement about the Dirac field (ledger H V3), outside the evidentiary region. Logged for the Dirac chain if built.
## Hygiene: l=0 rows print "-" for zeta (the raw s-formula value is not a splitting; F94.3 stands). Caught in-session before filing (no fault number:
## the line never left the instrument draft).
## Residue after this item: none. Consumes no L1-L6 clause; changes no row.