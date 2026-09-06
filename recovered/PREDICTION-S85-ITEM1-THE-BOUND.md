# PREDICTION · S85 · ITEM 1 · CLAUSE 1 · THE VARIABLE-q BOUND
# FILED AND HASHED BEFORE pack85/semi85.py EXISTS.  Nothing below may be edited.
# Derivation aid pack85/deriv85.py is SYNTHETIC ONLY and touched no atomic field.

## THE DERIVATION BEING TESTED

In u = 1/r, with S(u) := u q(1/u) = -V(r), f(u) = 2E + 2S(u) - L^2 u^2, and [u1,u2]
the outer allowed region, a := u2 - u1:

  (i)   f - g = 2[S - CHORD], g := L^2 (u-u1)(u2-u) the constant-charge parabola
        through the SAME turning points.  int du/sqrt(g) = pi/L -- s84's anchor.
  (ii)  J = (1/pi) int_0^1 dt / sqrt( t(1-t) - delta(t) ),
        delta := 2[CHORD - S]/(L^2 a^2) >= 0 iff S convex in u iff q'' >= 0.
  (iii) J is CONVEX in delta and delta is AFFINE in S, so J is maximised at an
        extreme point of the admissible set of S; those extreme points are one-kink
        TENTS, each of whose two pieces leaves the radicand quadratic.  Closed form:
           J_tent(b0,b1) = 1 + (2/pi)[ asin sqrt(tk/(1-b0)) - asin sqrt((tk-b1)/(1-b1)) ]
           tk = b1/(b0+b1),  b0 = 2(c*-w_out)/(L^2 a),  b1 = 2(w_in-c*)/(L^2 a)
        with w := q - r q' = S'(u) and c* := [S(u2)-S(u1)]/a.
  (iv)  J_tent = 2 EXACTLY on b0+b1 = 1, for EVERY split.  Hence with

           K := 2 V+ / (L^2 a),   V+ := positive variation of w across the orbit
                                      = int_{r_in}^{r_out} [ -r D'(r) ]_+ dr,  D = 4 pi r^2 rho

           **K < 1  ==>  J < 2  ==>  dg/dl > 0  ==>  G-WITHIN.**

  (v)   L^2 a = 2 sqrt(c*^2 + 2 E L^2), so equivalently
           **K = V+ / ( c* sqrt(1 - (L/nu*)^2) ),  nu* := c*/sqrt(-2E).**
        The tolerance for screening variation is the ECCENTRICITY FACTOR
        eps := sqrt(1-(L/nu*)^2).  A near-circular orbit has almost none.

## THE POPULATIONS, STATED IN THE CLAUSE (F83.1, twelfth appearance, pre-empted)

  **R** = the tested row set, fixed here and not to be extended before scoring:
     FAIL rows (front83 w<=4 failures, Z<60): 13 14 15 16 17 18 19 20 34 35 36 37 38
                                              49 50 51 52 53 55 57
     CONTROL rows (clean at w=4, Z<60):       21 24 26 29 30 32 40 42 44 47 56 58 59
     HEAVY rows:                              88 89 90 91
  **A** = the WIDTH-2 FRONTIER: channels of nu_rank 0 or 1, over R.  This is the
        population every clause below names unless it says B.
  **B** = all l<=3 channels among the five lowest-nu, over R.

## THE CLAUSES

**S1 · THEOREM, CAN-FAIL.** Over B, every single-region channel satisfies
J <= Jbar(K) + 1e-6, Jbar := J_tent(K/2,K/2).  **ZERO violations.**  A violation
falsifies the derivation and is reported as such, not repaired in session.

**S2 · ENTAILED.** K >= 1 at Z=89 6d and at Z=90 5f.  (J>=2 there is already banked;
by (iv) K<1 would be a contradiction.)  If K < 1 at either, instrument or field is wrong.

**S3 · RISKY.** Over A: K < 1 at EVERY l<=1 channel, every row of R.

**S4 · RISKY.** Over A: the set {K >= 1} contains NO l<=1 channel and AT LEAST ONE
l=3 channel.

**S5 · RISKY, THE l-DISCRIMINATION.** Median eps over A: eps(l=0) > 0.90,
eps(l=1) > 0.60, eps(l=3) < 0.45.  At Z=90's 5f specifically, eps < 0.35.

**S6 · RISKY.** K at the s channel of A rises with Z across R and stays in (0.80,1.00);
it never reaches 1.  K(s) tracks 1 - O(1/Z).

**S7 · RISKY.** At Z=91 the 5f channel has K >= 1.

**S8 · RISKY.** Over A, the count of channels with K >= 1 is at most 8.

**S9 · RISKY, WIDENING.** Over A, no l=1 channel has J >= 2, and no l=0 channel has
J >= 2.  J(l=0) stays in 1.15..1.30 and J(l=1) in 1.45..1.90 over ALL of R.

**S10 · ALGEBRAIC CAN-FAIL ON REAL DATA.** V+/sqrt(c*^2+2EL^2) reproduces 2V+/(L^2 a)
to 1e-6 at every channel of B.

## WHAT WOULD CLOSE CLAUSE 1
S1 and S2 hold, S3 holds, and S4 holds.  Then K<1 is a DERIVED sufficient condition for
G-within, it is met at every l<=1 frontier channel of R, and the channels it fails at
are exactly the actinide-opening high-l entrants -- Z=90 accounted for by (v): the 5f
orbit is near-circular, its eccentricity factor is small, and its tolerance for the
core's shed charge is correspondingly small.  **THE MAGNITUDE OF dg/dl IS NOT CLAIMED.**
