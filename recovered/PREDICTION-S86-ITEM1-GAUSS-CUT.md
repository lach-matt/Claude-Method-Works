# PREDICTION S86 — ITEM 1 · CLAUSE 1 · DOES THE GAUSS CONSTRAINT CUT THE TENT?
# Filed and hashed BEFORE pack86/semi86.py exists. Its sha gates every run.
# Population A = the width-2 frontier (nu_rank 0,1), 74 channels, 37 rows, as s85.
# Field: s84's, imported unmodified through semi85 (q_native, channel_row).

## THE ORDER'S ROUTE, STATED
The saturating tent (b0+b1 = 1) is claimed to violate Q(u) non-decreasing and/or
1 <= Q <= Z; intersecting the admissible set with those two constraints is claimed to
raise the threshold above K = 1.

## THE ALGEBRA, FILED BEFORE MEASUREMENT
The tent's pieces are the TANGENT LINES of S(u) = u Q(u) at u1 and u2. A tangent of
u Q(u) at u0 is S(u0) + w(u0)(u - u0) with intercept  -u0^2 Q'(u0)  <= 0 wherever
Q' >= 0. On a line of slope b and intercept alpha <= 0, Q_line = b + alpha/u is
NON-DECREASING in u. Hence each tent piece has monotone Q; the two pieces meet
continuously at the kink; Q_tent runs from Q(u1) to Q(u2) and stays inside [Q(u1),Q(u2)]
which is inside [1, Z]. **The tent is Gauss-admissible. Both constraints are satisfied
by the very object they were meant to exclude.** Physically the tent is density
rho ∝ 1/r^2 on each piece plus a thin charged SHELL at the kink: all non-negative.

## CLAUSES (each names its population and its statistic)
S1  For every one of the 74 A-channels, q'(r) <= 0 at BOTH r_out and r_in (tolerance
    1e-9 relative), i.e. both tent intercepts are <= 0.
S2  For every A-channel, Q_tent(u) sampled on 2001 points of [u1,u2] is non-decreasing
    (min forward difference >= -1e-9 * Q(u2)) and lies in [Q(u1)-1e-9, Q(u2)+1e-9].
S3  For every A-channel, Q(u1) >= 1 - 1e-6 and Q(u2) <= Z + 1e-6.
S4  CONSEQUENCE: the constrained extreme point is the unconstrained one; the number of
    A-channels whose K < 1 status changes under the constrained bound is 0 of 74. The
    threshold stays at K = 1. The order's route does not raise it.
S5  The tent's Q equals Q(u1) at u1 and Q(u2) at u2 to 1e-9 (endpoint check that the
    construction is the tent and not something else).
S6  The saturating tent (rescaled to b0+b1 = 1 holding the split tk fixed) is ALSO
    Gauss-admissible for every A-channel: the rescaling multiplies both intercepts by
    a positive factor, so their signs are unchanged. 74 of 74.
S7  WHAT WOULD CUT. A kink in S is a step in 4 pi r^2 rho, i.e. a jump in some |P_nl|^2,
    i.e. a jump in some P_nl: infinite kinetic energy. The constraint that excludes the
    saturating tent is finite kinetic energy (P_nl in H^1), not Gauss. This is a
    different mathematical language (Sobolev), per the standing protocol on nulls. Not
    measured this session; named as the next step. Filed as a claim to be scored
    by whether any A-channel's tent kink corresponds to a finite-T density: prediction
    is that it does not (a tent has a delta in S'' for every channel with K_end > 0).

## CAN-FAILS (run first, gate the run)
CF1 A synthetic S with a tangent intercept > 0 (a line with Q decreasing) must be
    flagged NOT admissible by the same checker.
CF2 A synthetic pure-Coulomb S (q constant) gives a tent equal to the chord, Q_tent
    constant, admissible, intercepts 0.
CF3 Sign sensitivity: flipping the sign of q' at one endpoint on a real channel must
    flip the verdict at that endpoint.
CF4 Lever: the checker on q == 1 must return both intercepts = 0 and K = 0; the live
    arm must move both.
