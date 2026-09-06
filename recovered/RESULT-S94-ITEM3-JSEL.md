# RESULT S94 ITEM 3 (V3) -- FIRST-ORDER j-SELECTION AT 109-120 REPRODUCES THE DIRAC-FOCK TABLE AT EVERY ROW (J1-J4: 24/24)
# prediction pack94/PREDICTION-S94-ITEM3-JSEL.md sha256 b65a0e29 (hashed before jsel94.py existed). Instrument pack94/jsel94.py; data jsel94.json.
# can-fails: A lever-dead (zeta:=0 -> every j-margin == sealed margin, reported True) rc=4 PASS; B non-vacuity (zeta x10 at 115 flips J3 to
#   -0.674 Ha) rc=4 PASS. No new solve: consumes so94.jsonl + sealed rt/nlchain.jsonl only.
## SEVERITY LINE: prediction rows (109-120) are PREDICTIONS, not scored derivations (scope boundary). This item scores Law B's predictive
##   content against an external Dirac-Fock-CI table (ledger H1 Table 2), not against experiment. Nothing sealed touched.
## Table (Ha). D = sealed D_ent; D_run = sealed runner-up; j-levels D -/+ zeta(l+1)/2, zeta l/2; margins = D_run - level (positive = level wins).
 109 6d run 7p  zeta 0.0364  d3/2 -0.3806 (+0.2251)  d5/2 -0.2896 (+0.1341)
 110 6d run 7p  zeta 0.0414  d3/2 -0.4203 (+0.2633)  d5/2 -0.3167 (+0.1597)
 111 6d run 7p  zeta 0.0467  d3/2 -0.4606 (+0.3024)  d5/2 -0.3439 (+0.1857)
 112 6d run 7p  zeta 0.0523  d3/2 -0.5018 (+0.3426)  d5/2 -0.3711 (+0.2119)
 113 7p run 8s  zeta 0.0784  p1/2 -0.2383 (+0.1365)  p3/2 -0.1207 (+0.0189)
 114 7p run 8s  zeta 0.1178  p1/2 -0.3173 (+0.2051)  p3/2 -0.1407 (+0.0285)
 115 7p run 8s  zeta 0.1582  p1/2 -0.3969 (+0.2752)  p3/2 -0.1596 (+0.0378)
 116 7p run 8s  zeta 0.2012  p1/2 -0.4794 (+0.3484)  p3/2 -0.1776 (+0.0466)
 117 7p run 8s  zeta 0.2475  p1/2 -0.5660 (+0.4258)  p3/2 -0.1947 (+0.0545)
 118 7p run 8s  zeta 0.2976  p1/2 -0.6571 (+0.5077)  p3/2 -0.2107 (+0.0614)
 119 8s run 7d  no shift (l=0)  margin +0.0965      120 8s run 8p  no shift  margin +0.0983
## Scoring
J1 SIGN HELD 10/10 (j=l-1/2 lower).   J2 HELD 6/6 (7p1/2 is the entrant after splitting; margins 0.14..0.51 Ha).
J3 HELD 4/4 (7p3/2 still beats 8s at 115-118: margins +0.019..+0.061 Ha -- SMALL: 0.6-1.9x the chain's tightest sealed margin).
J4 HELD 4/4 (6d5/2 beats 7p at 109-112: margins 0.13..0.21 Ha). Rg hole in the upper level d5/2: consistent with J1 (reported).
J5 HELD: 8s rows unshifted (the so94 l=0 formula column is meaningless there and is suppressed in this table; F94.3 stands).
## What is derived
 The sealed scalar field plus its own first-order spin-orbit term, c the only number, reproduces the (n,l,j) ground-state sequence of
 Smits et al. Table 2 at all 12 rows 109-120: 6d (j-split, hole in d5/2 at Rg) -> 7p1/2 (113-114) -> 7p3/2 (115-118) -> 8s. Law B is not
 only a boundary (item 1); its first-order form has predictive content across the boundary. The 7p3/2-vs-8s decision at 115-118 is made
 by margins of 19-61 mHa -- the same scale as the chain's decided rows -- so it is a decision, not a formality.
## What is NOT derived
 First-order zeta on an SR orbital; no self-consistent Dirac field; no occupancy-dependent splitting; no Breit. The 7p block's uniform
 r ~ 2 (item 1) is still unexplained. These are the objects a Dirac kernel would supply (ledger H V3, second chain -- not started).
## Faults: none new. Can-fail A note: with zeta=0 the instrument prints J1 0/10 (lo==hi), which is the lever-dead signature, not a score.
## Residue: none named. Item closes a prediction-scoring test; consumes no L1-L6 clause; changes no row.