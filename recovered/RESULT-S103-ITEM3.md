# RESULT-S103-ITEM3 -- G4 per-row consumer-bound table (pack100 flag discharged per row).
# Pure tabulation from named sealed receipts; only arithmetic is the bound formula. Rule B line:
# for every V5 row, B_row < m_row AND dm2_lo,row - B_row > 0 (direction: strictly positive;
# value-exact from receipts; conservative substitutions DECLARED where a per-row denominator
# is not named).
# Bound: B_row = |dm2|_hi x (4e-4 / Dmin_row). 4e-4 = two eigenvalues x 2e-4 per-eigenvalue
# v5a operator-content offset (DERIVED, s100 G1: sqrt(M) exchange weight + Vloc slots; measured
# 1.8351e-4 worst named case). Dmin = smallest energy denominator of eps-den content actually
# CONSUMED in dm2 (cfg-gap objects from gap97/gap98 SCF totals do not carry the v5a spectrum
# offset at all -- applying the bound to them anyway is conservative).

row   m(sealed)  dm2 [lo,hi]        B          m-B>0  dm2lo-B>0  m/offset  Dmin source
 38   0.05639   [0.07500,0.07500]  3.16e-05     Y       Y        282x     run-side own-slot den 1.9 Ha (s98)
 56   0.03914   [0.04840,0.04840]  3.80e-04     Y       Y        196x     SUBSTITUTED record-min 0.102 Ha (declared)
 72   0.04507   [0.11592,0.12325]  9.67e-04     Y       Y        225x     3 mHa eps-den remedied to Delta_cfg; substituted 0.102 (declared)
 89   0.03233   [0.10700,0.15800]  1.24e-03     Y       Y        162x     Delta_cfg 0.102-0.137 (s97); eps end 0.47
105   0.05440   [0.11747,0.11747]  4.20e-04     Y       Y        272x     consumed two-state Delta_cfg 0.22358 (s98)

## VERDICT: ALL FIVE ROWS PASS BOTH INEQUALITIES. Worst case row 89: B = 1.24e-3 vs
## dm2_lo = 0.107 (86x clearance) and m = 0.0323 (26x clearance). The WIDENING verdict at every
## V5 row survives the v5a offset class with >= 26x headroom under the most conservative
## (non-common-mode, smallest-denominator-everywhere) assumptions; common-mode cancellation
## (same-instrument differential, s100 flag) only enlarges these clearances.
## The pack100 consumer flag is DISCHARGED per row. Declared substitution at rows 56/72 is the
## only non-receipt element; a per-row Dmin read at those rows can only RAISE their clearance
## (1.9 Ha at the analogous row 38 object suggests ~19x more headroom than tabulated).
