# RESULT S90 ITEM 1 -- L3-ACROSS dl=2 AT THE s->d COLLAPSE. Rows 36 37 38 54 55 56.
Prediction d5cd81ff..82e00 hashed before chain90.py existed. Can-fail gate PASS (CF1-CF4,
non-vacuous: delta moves with screening, well count moves with the barrier). Lever LIVE.
P6: every J already sealed in chain89-out.json reproduced to 4 dp (4d 1.0111/2.2337, 5d 1.0358/2.4407).

## Scoring
P1 HELD exactly: d well count 2 at 36,37,54,55; 1 at 38,56.
P2 HELD: delta_outer(d) pre-collapse = 0.0040, 0.0010, 0.0110, 0.0030 (all < 0.15). Can-fail
   (delta_outer > 0.5) did not occur. The outer well IS hydrogenic to 1e-2 in the defect.
P3 FALSIFIED everywhere. Semiclassical delta_sc is BELOW banked delta at every channel:
   s: by 0.175 0.213 0.169 0.229 0.267 0.224 (filed 0.10); one-well d: by 0.50 (38), 0.43 (56);
   two-well d: by 0.26 0.28 0.28 0.35 (filed 0.25). Systematic, one-signed, size 0.2-0.5.
P4 (b) FALSIFIED as filed. Testable at 36, 38, 56 only (F90.2): errors 1.02, 0.14, 0.22.
   Strict "within 0.2 at all six" fails at 36 (by 1.0) and 56 (0.22). My weaker filing: held at
   38, marginal-failed at 56, failed at 36 as expected. (b) can-fail (error > 1 post-merge) did
   not occur. Inserting the p channel does NOT remove the pre-collapse discontinuity: the d's
   outer-well slope (+0.96) says nothing about its g, because 0.83 of its defect sits in the
   INNER well (Ph_in = 2.6 at Z=37, 5.9 at Z=55) which the trapezoid never sees.
P5 COMPARISON: NEITHER carries the clause. (a) is WRONG-SIDED (F90.1): g_outer = l + delta_outer
   is a LOWER bound on g(d) (all phases positive), and the n+l clause g(d) - g(s) < 1 needs an
   UPPER bound on g(d). (a)'s "across" value is -1.1, -1.1, -0.3, -2.0, -2.0, -0.15 against banked
   +0.03, -0.001, +0.42, +0.21, +0.20, +0.73: it proves the clause trivially and wrongly.

## The finding
The n+l clause at the collapse, read in defects, is delta(s) - delta(d) > 1: measured
margins (1 - banked across) = 0.97, 1.00, 0.58, 0.79, 0.80, 0.27. The margin at Z=56 is 0.274.
P3 shows every semiclassical magnitude in this chain carries a one-signed bias of 0.2-0.5 in
delta. Therefore, as s88 T1 said of J<2 for the tie-break: NO MAGNITUDE BOUND OF SEMICLASSICAL
TYPE CAN CERTIFY g(d)-g(s) < 1 AT Z=56 (margin 0.27 < bias 0.43 at 5d there). The route must
go through the converged eigenvalues themselves (L5), not the action (L2-L3).

## STATUS
L3-across dl=2 (37, 55, 56): OPEN, and now with a reason: the across clause is a magnitude
statement and the chain's magnitudes (L2-L4) are derivative/sign-exact, not value-exact.
Closed form available: delta(s) - delta(d) > 1 is a LOWER bound on s-penetration relative to d,
COMPUTED 6/6 from the banked ladder (L1-level identity), not derived from L2-L4.

## FAULTS
F90.1 Candidate (a) in ORDER-FOR-S90 was filed on the wrong side of the inequality (lower bound
      offered for an upper-bound clause). Detected at scoring, not at filing.
F90.2 chain90.py reads candidates from the banked row's channel list; 5p at 37 and 6p at 54, 55
      are not in that list, so (b) is untestable at three rows from disk. The field itself has
      them; a direct-field eigenvalue call would fill them. Not pursued: (b) is already
      falsified at 36 and the hypothesis was "all six".