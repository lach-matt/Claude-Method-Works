# PREDICTION S101 ROUTE (a) -- FILED AND HASHED BEFORE THE BUILD (Zeno)
## OBJECT: analytic per-shell gradient of Efun on the shooting path at 58-B midpoint:
##   part_c = 2 q_c <dP_c/dq | F^grad_c | P_c>, F^grad_c = grad_{P_c} Efun / (2 q_c), assembled from
##   NAMED term families: (T-elim) kinetic eliminated via the pointwise shoot relation with M-weighted
##   exchange source; (Uc) own-slot direct incl. ceff; (Xc) own-slot exchange kernel; (BW-J) both-ways
##   direct from other shells' Vloc containing Y0(c); (BW-K) both-ways exchange from other shells' X_b
##   containing P_c; (OWN4) own-shell quartic direct/exchange derivative content.
## RULE B LINE: VALUE-exact per shell within max(15 percent of |R2part_c|, 4e-6 Ha) and SIGN-exact for
##   every shell with |R2part_c| > 1e-5, against the d101-58 R2_parts receipt (13 shells). SUM within
##   15 percent of R2 = +1.059e-4. Instrument is VALUE-exact class.
## PA1: per-shell match as above, 13/13.
## PA2 (conditional on PA1): the same assembly at 90-A and 91-A reproduces the NEGATIVE sign of the
##   sealed defects (-5.90e-5, -4.10e-5) with the sign carried by named terms (d-selectivity exhibited).
## CAN-FAIL (non-vacuous, demonstrated): dropping the BW blocks reduces the assembly to the F101.4
##   falsified form (wrong sign, 4x magnitude) -- the lever is known to fire.
## SCORING: PA1+PA2 held => the defect VALUE is derived term-by-term from the construction => G5b
##   closure statement submitted to M (zero-residue standard). Any miss => fault, mechanism, no rewrite.