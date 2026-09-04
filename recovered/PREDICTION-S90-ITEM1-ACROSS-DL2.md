# PREDICTION S90 ITEM 1 -- L3-ACROSS dl=2 AT THE s->d COLLAPSE (rows 36 37 38 54 55 56)
# Filed and hashed BEFORE chain90.py exists and before any row runs. R 1449.
# Clause under test: G-across, g(d) - g(s) < 1 at Z=37, 55, 56 (banked: +0.199? no -- banked
# values are NOT consulted here beyond s89's record: Z37 -0.001, Z55 +0.199, Z56 +0.726 (=2*0.363)).

## DEFINITIONS (mine, stated before running)
Phase of a well: Phi = int p dr over one allowed region, p = sqrt(2E + 2q(r)/r - L^2/r^2), L=l+1/2.
Coulomb reference at the same E, L, same region end-points: Phi_C = same integrand with q == 1.
  delta_outer = (Phi_outer - Phi_C[outer region]) / pi     -> 0 exactly when q==1 on the well.
  delta_sc    = (Phi_outer + Phi_inner - Phi_C[full Coulomb, r=0..r_turn]) / pi   (semiclassical
                total defect; consistency against banked delta = n - nu).
Path (b): two dl=1 trapezoids through the p channel of the s's own n (5p at 36-38, 6p at 54-56):
  Dg_b = [dgdl(s)+dgdl(p)]/2 + [dgdl(p)+dgdl(d)]/2,  dgdl = 2 - J_outer (L2).  Compared to
  banked g(d) - g(s).

## PREDICTIONS
P1 LEVER: region count of the d candidate takes values {2} at 36,37,54,55 and {1} at 38,56.
   If all six are the same count the lever is dead, rc=4, nothing scored.
P2 (a) delta_outer(d) < 0.5 at all four pre-collapse rows (36,37,54,55); my point estimate
   |delta_outer| < 0.15 there. CAN-FAIL: any pre-collapse row with delta_outer > 0.5.
P3 (a) delta_sc agrees with banked delta within 0.10 at all 6 rows for the s channel and the
   one-well d rows; at two-well d rows within 0.25 (barrier tunnelling not in the action).
P4 (b) |Dg_b - banked (g_d - g_s)| <= 0.2 at all six rows (filed hypothesis of the order).
   My own expectation is WEAKER: holds at 38 and 56 (post-merge), FAILS by > 0.5 at 37 and 55,
   because the p channel does not remove the two-well/merge discontinuity in g(l) at the d.
   CAN-FAIL direction for (b): error > 1 at a post-merge row.
P5 COMPARISON: if P2 holds and P4-strict fails, path (a) carries the clause: the n+l clause at
   the collapse is g_outer(d) - g(s) < 1 with g_outer = l + delta_outer. If P4-strict holds,
   (b) carries. If both hold, (b) is preferred (no new definition). If neither, L3-across dl=2
   stays OPEN and is written as such.
P6 Sealed J reproduced to 4 dp at every channel already in chain89-out.json (37, 55, 56).