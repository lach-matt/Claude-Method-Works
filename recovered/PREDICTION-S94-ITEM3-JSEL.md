# PREDICTION S94 ITEM 3 (V3) -- LAW B's PREDICTIVE CONTENT: WHICH j-SHELL THE FIRST-ORDER SPLITTING SELECTS AT 109-120. Written before any run.
## Object. From pack94/so94.jsonl (sealed field, rows 109-120): entrant D_ent and sealed runner-up D_run (rt/nlchain.jsonl 'order'[1]),
##   zeta of the entrant. First-order j-levels of the entrant: D(j=l-1/2) = D_ent - zeta*(l+1)/2 ; D(j=l+1/2) = D_ent + zeta*l/2
##   (t7c_so.py convention). A level shift of the entrant orbital shifts D by the same amount to first order (declared; Koopmans-exact field, s93).
##   Reference: Smits et al. 2023 Table 2 (ledger H1): 109-112 6d; Rg hole in 6d5/2; 113-114 7p1/2^k; 115-118 7p1/2^2 7p3/2^k; 119-120 8s.
## Rule B declarations:
J1 SIGN: on every l>0 row 109-118 the lower j-level is j = l-1/2 (d3/2 below d5/2; p1/2 below p3/2). 10/10. (Follows from zeta>0; scored.)
J2 VALUE: rows 113-118: D_7p - zeta < D_run(8s): the 7p1/2 level stays the entrant after splitting. 6/6.
J3 VALUE, bound-direction UP: rows 115-118: D_7p + zeta/2 < D_run(8s): 7p3/2 still beats 8s, so Table 2's 7p3/2 occupation at 115-118
   is reproduced by the field + first-order SO; the 8s entrant at 119 is not pulled forward. 4/4. (Mechanism if it fails: first-order
   zeta on the SR orbital overestimates the 7p3/2 rise; or the j-rule needs the self-consistent Dirac field. Either way Law B's crossing
   remains, but its PREDICTIVE claim at the j level would be falsified.)
J4 VALUE: rows 109-112: D_6d + zeta < D_run(7p): the upper 6d5/2 level still beats 7p. 4/4.  And the Rg (111) hole sits in the UPPER
   level d5/2 -- consistent by J1; reported, not scored (occupancy within a split shell is not a field output).
J5 HYGIENE: rows 119-120 (8s) have no shift; D_ent unchanged. Report.
## Can-fails: A lever-dead: zeta := 0 reduces every j-test to the sealed comparison (all pass trivially) -> rc=4 if J3 is then "decided by
##   nothing" (the instrument must report that J3 margin == sealed margin). B non-vacuity: zeta x 10 at row 115 must flip J3 (7p3/2 above 8s)
##   -> rc=4. If x10 does not flip it the bar is reported with the factor that does.
## Bars: zeta precision 1e-5 Ha; D floor 5e-5 Ha. Margins reported in Ha with sign.