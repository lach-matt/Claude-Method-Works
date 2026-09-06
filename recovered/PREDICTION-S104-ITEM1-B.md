# PREDICTION-S104-ITEM1-B -- branch B: is the 3.3e-6 rot residual instrument or physics?
# Filed and hashed BEFORE any arithmetic. c the only number. Triggered by PA.3 MISS per the
# branch-A prediction's protocol. D2 probe located the asymmetry on (endpoint|partner) cross
# elements (~1.3e-4; m|p ~ 1e-6): operator inhomogeneity across hybrid SCF potentials.
# Two repairs run in ONE instrument (w104b.py, shared solves) -- comparison decides:
#   B1: tighter SCF (run2 tol 2e-6 -> 2e-9, ladder beta/maxit extended), same eigen-relation
#       T-action, same valence-only basis as branch A. Shells 6s, 5s only (5p/5d are exact-zero
#       by construction; recomputing them is undeclared spend).
#   B2: direct-quadrature one-body I on the same basis vectors:
#       I[u,v] = 0.5 Int u'v' + 0.5 l(l+1) Int uv/r^2 - Z Int uv/r  (symmetric by construction),
#       scored at 6s against the sealed chord gate.

RULE B LINE: PB.1/PB.3/PB.4 value-exact; PB.2 value-exact AND sign-exact; direction: BELOW bound.

PB.1 (B1 instrument gate): worst cross-element asym at 6s and 5s drops >= 10x under tight SCF:
  asym_tight <= 1.4e-5 (loose reference 1.36e-4). If this fails, the asymmetry is not
  SCF-residual content and B1's premise is falsified -- scored as a MISS, not reinterpreted.

PB.2 (decisive): at tight SCF, the filed linear law holds in the clean basis:
  |rot_val(6s) - (+4.0626e-06)| <= 2e-6  AND  |rot_val(5s) - (-7.8432e-06)| <= 2e-6,
  signs matching. Grounds: the S103-open derivation (quadratic Taylor cancellation) is exact for
  a clean self-adjoint I; D2 shows the residual asymmetry is SCF-potential inhomogeneity, which
  tightening removes. IF PB.2 MISSES with PB.1 HIT, the residual is physical (Hessian asymmetry;
  D1 quadratic hypothesis becomes the named next object). That fork is the comparison's verdict
  either way -- both outcomes are informative; only the stated inequality is the prediction.

PB.3 (chord stability, sanity): |chord_tight - chord_sealed| <= 1e-6 at 6s and 5s (chords are
  physical F-differences; SCF tightening moves them by at most the old tolerance scale).

PB.4 (B2 scored at 6s): the direct-quadrature I is the WRONG operator for the sealed
  scalar-relativistic kernel; predicted to FAIL the chord gate: |chord_B2 - chord_sealed| > 1e-8
  (expected O(alpha^2 Z^2) kinetic content >> gate). If it unexpectedly PASSES, B2 is a valid
  symmetric-by-construction repair and competes with B1 on PB.2's clauses -- comparison decides.

CAN-FAIL (non-vacuous, conditional per S103 precedent): if PB.2 scores HIT, rerun 6s with
  --canfail (Dr skew 1e-5 * P_5s); PB.2's 6s clause must then MISS -> rc=4 BREAK OK, else rc=5
  VACUOUS. If PB.2 scores MISS on the primary run, the lever is uninformative and is deferred.

Scored against sealed w102b-58.json chords and sealed w103a-58.json law terms only. No sealed
file edited. All work in pack104/.
