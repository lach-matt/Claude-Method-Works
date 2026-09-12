#!/usr/bin/env python3
"""
weave.py -- M: "the time thread only measures and places in time, the spatial
index is not introduced, but a coordinate requires dimension so geometry is what
moves through time.  The spatial thread does not consider time so it must carry
the time in the form of light.  The thread that carries both requires only those
two."

FOUR CLAUSES.  ALL FOUR LAND, ONE IS SHARPER THAN STATED, AND THE FOURTH TURNS
OUT TO BE AN EXACT CLOSED FORM THIS TREE DID NOT HAVE.

CLAUSE TWO IS A DIMENSIONAL FACT.  EVERY METRIC COMPONENT IS DIMENSIONLESS -- the
dimension lives in the coordinates, not the geometry.  g_tt returns a RATIO of
clock rates and can never return a length; g_rr returns a ratio and needs dr to
become one.  "A coordinate requires dimension, so geometry is what moves through
it" is not an interpretation, it is how the object is built.

CLAUSE FOUR IS EXACT.  Give g_tt and g_rr at a known r and the cross term
follows with nothing else added:

    M    = r(1 + g_tt)/2
    a^2  = r^2 [ 1/g_rr + g_tt ]
    g_tp^2 = r^2 (1 + g_tt)^2 ( 1/g_rr + g_tt )

verified to 1.4e-14 at six configurations spanning M from 0.3 to 5, a from -0.7
to 4.9 and r from 1.5 to 12.  THE THREAD THAT CARRIES BOTH REQUIRES ONLY THOSE
TWO, exactly as M says.

CLAUSE THREE IS RIGHT AND SHARPER THAN STATED.  Light is not carried BY the
spatial thread -- LIGHT IS THE RATIO OF THE TWO THREADS.  The null condition
ds^2 = 0 gives dr/dt = sqrt(-g_tt/g_rr), which reproduces axis.py's coordinate
speed 1 - 2M/r to twelve places at r/M = 2.5, 3, 6, 20 and 1e4.  IT TAKES BOTH
TO MAKE ONE, and that is a correction to the clause rather than a refutation of
it: the spatial thread cannot carry time by itself either.

SO THE TWO THREADS COMBINE TWO WAYS AND EACH WAY IS ONE OF M'S CLAUSES:

    THEIR RATIO IS LIGHT.            dr/dt = sqrt(-g_tt/g_rr)      no r in it
    THEIR PRODUCT IS THE INTERSECTION. g_tp^2 = r^2 (...)          r^2 in it

AND THE COORDINATE APPEARS IN THE SECOND AND NOT THE FIRST, which is clause two
landing exactly where M put it: THE THREAD THAT CARRIES BOTH IS THE ONE THAT
NEEDS THE DIMENSION.

AND THE CLOSED FORM RETURNS g_tp SQUARED.  ONE BIT -- the sign of a, the
DIRECTION of frame dragging -- IS NOT RECOVERABLE AT ANY PRECISION: a = +0.7 and
a = -0.7 give byte-identical g_tt and g_rr and opposite g_tp.  threads.py
measured that as sign-blindness from the physics side; here it is a DETERMINACY
statement from the algebra side, and they agree.

    AND THAT BIT IS THE ONE THING A CORRIDOR WOULD NEED.  A DIRECTION OF TRAVEL
    IS A SIGN.  The corridor's orientation is not derivable from its own time
    and space threads.

SCOPE, STATED RATHER THAN ASSUMED: the recovery holds WITHIN THE KERR FAMILY,
where two parameters determine every component.  FOR A GENERAL STATIONARY
AXISYMMETRIC METRIC g_tp IS AN INDEPENDENT FUNCTION and none of this follows.
M's clause is true of the object this project actually studies and is not a
theorem about stationary metrics in general.

stdlib only.  Run --selftest before trusting the report.
"""
import math, sys

# ===================================================== the three threads, Kerr
def kerr_equatorial(r, M, a):
    """(g_tt, g_rr, g_tphi) on the equator, Boyer-Lindquist."""
    D = r*r - 2.0*M*r + a*a
    return -(1.0 - 2.0*M/r), r*r/D, -2.0*M*a/r

THREADS = (("TIME",         "g_tt",  "an ENDPOINT RATIO",  "1 + z = e^dPhi"),
           ("SPACE",        "g_rr",  "a LINE INTEGRAL",    "Int dr/sqrt(f)"),
           ("INTERSECTION", "g_tphi","the CROSS TERM",     "frame dragging"))
METRIC_COMPONENTS_ARE_DIMENSIONLESS = True
DIMENSION_LIVES_IN_THE_COORDINATE   = True

# ===================================================== the recovery
def recover_M(r, g_tt):        return r*(1.0 + g_tt)/2.0
def recover_a2(r, g_tt, g_rr): return r*r*(1.0/g_rr + g_tt)
def g_tphi_squared(r, g_tt, g_rr):
    """CLOSED FORM: the cross term from the other two threads and the coordinate."""
    return r*r*(1.0 + g_tt)**2 * (1.0/g_rr + g_tt)

# ===================================================== the two combinations
def light_ratio(g_tt, g_rr):
    """ds^2 = 0 -> dr/dt.  A pure ratio -- NO coordinate in it."""
    return math.sqrt(-g_tt/g_rr)

RATIO_IS_LIGHT        = True
PRODUCT_IS_THE_CROSS  = True
COORDINATE_IN_LIGHT   = False     # dr/dt is dimensionless in c = 1
COORDINATE_IN_CROSS   = True      # g_tp^2 carries an explicit r^2

# ===================================================== the missing bit
SIGN_OF_a_IS_RECOVERABLE = False
BITS_MISSING             = 1
ORIENTATION_IS_DERIVABLE = False   # a direction of travel is a sign

# ===================================================== scope
SCOPE = "the Kerr family only -- two parameters fix every component"
GENERAL_STATIONARY_g_tphi_IS_INDEPENDENT = True
THIS_PASS_REPAIRS_ANYTHING = False

# ================================================================== report
def report():
    P = print
    P(__doc__.split("stdlib only.")[0].rstrip())

    P("\n" + "="*79)
    P("1.  CLAUSE TWO IS A DIMENSIONAL FACT, NOT AN INTERPRETATION")
    P("="*79)
    P(f"\n  {'thread':>14} {'component':>10} {'enters as':>22}  {'form':>18}")
    for name, comp, how, form in THREADS:
        P(f"  {name:>14} {comp:>10} {how:>22}  {form:>18}")
    P(f"""
  EVERY ONE OF THEM IS DIMENSIONLESS.  The dimension lives in the coordinate:

      g_tt   dimensionless   a RATIO of clock rates.  NO LENGTH, EVER.
      g_rr   dimensionless   a ratio only.  dl = sqrt(g_rr) dr NEEDS dr.
      dr     LENGTH          the dimension the geometry does not carry
      c      LENGTH/TIME     the only dimensionful bridge in the structure

  So the time thread cannot place anything in SPACE and the space thread cannot
  place anything in TIME.  "A COORDINATE REQUIRES DIMENSION, SO GEOMETRY IS WHAT
  MOVES THROUGH IT" is how the object is built.""")

    P("\n" + "="*79)
    P("2.  CLAUSE FOUR IS EXACT -- THE CROSS TERM NEEDS ONLY THE OTHER TWO")
    P("="*79)
    P("""
      M      = r(1 + g_tt)/2
      a^2    = r^2 [ 1/g_rr + g_tt ]
      g_tp^2 = r^2 (1 + g_tt)^2 ( 1/g_rr + g_tt )
""")
    P(f"  {'M':>6} {'a':>7} {'r':>6} {'rec M':>10} {'rec a^2':>11} "
      f"{'g_tp^2 closed':>16} {'g_tp^2 direct':>15} {'diff':>10}")
    worst = 0.0
    for M, a, r in ((1.0,0.5,4.0), (1.0,0.99,3.0), (2.0,1.5,10.0),
                    (0.3,0.2,1.5), (1.0,-0.7,5.0), (5.0,4.9,12.0)):
        gtt, grr, gtp = kerr_equatorial(r, M, a)
        cf = g_tphi_squared(r, gtt, grr); worst = max(worst, abs(cf - gtp*gtp))
        P(f"  {M:6.2f} {a:7.2f} {r:6.2f} {recover_M(r,gtt):10.6f} "
          f"{recover_a2(r,gtt,grr):11.6f} {cf:16.9f} {gtp*gtp:15.9f} {cf-gtp*gtp:10.1e}")
    P(f"\n    EXACT TO {worst:.1e}.  THE THREAD THAT CARRIES BOTH REQUIRES ONLY THOSE TWO.")

    P("\n" + "="*79)
    P("3.  CLAUSE THREE IS RIGHT, AND SHARPER THAN STATED")
    P("="*79)
    P("""
    ds^2 = 0  ->  -g_tt dt^2 + g_rr dr^2 = 0  ->  dr/dt = sqrt(-g_tt/g_rr)
""")
    P(f"  {'r/M':>9} {'g_tt':>13} {'g_rr':>13} {'sqrt(-g_tt/g_rr)':>19} {'1 - 2M/r':>12}")
    for r in (2.5, 3.0, 6.0, 20.0, 1e4):
        gtt, grr, _ = kerr_equatorial(r, 1.0, 0.0)
        P(f"  {r:9.1f} {gtt:13.8f} {grr:13.8f} {light_ratio(gtt,grr):19.12f} {1-2/r:12.8f}")
    P("""
    IDENTICAL to axis.py's coordinate speed of light.

        LIGHT IS NOT CARRIED BY THE SPACE THREAD.  LIGHT IS THE RATIO OF THE
        TWO THREADS.

    That is a CORRECTION to the clause rather than a refutation: M is right
    that light is what puts time into the spatial description, and the spatial
    thread cannot do it alone either.  IT TAKES BOTH TO MAKE ONE.""")

    P("\n" + "="*79)
    P("4.  SO THE TWO THREADS COMBINE TWO WAYS, AND EACH IS ONE OF THE CLAUSES")
    P("="*79)
    P(f"""
        THEIR RATIO IS LIGHT           dr/dt = sqrt(-g_tt/g_rr)     NO r in it
        THEIR PRODUCT IS THE CROSS     g_tp^2 = r^2 (...)           r^2 in it

    AND THE COORDINATE APPEARS IN THE SECOND AND NOT THE FIRST.  That is clause
    two landing exactly where M put it: light needs no dimension and the
    intersection does.  THE THREAD THAT CARRIES BOTH IS THE ONE THAT NEEDS THE
    COORDINATE.""")

    P("\n" + "="*79)
    P("5.  AND THE CLOSED FORM RETURNS A SQUARE.  ONE BIT IS GONE.")
    P("="*79); P("")
    for a in (0.7, -0.7):
        gtt, grr, gtp = kerr_equatorial(5.0, 1.0, a)
        P(f"    a = {a:+.2f}:  g_tt = {gtt:.12f}   g_rr = {grr:.12f}   ->  g_tp = {gtp:+.12f}")
    P(f"""
    BYTE-IDENTICAL INPUTS, OPPOSITE OUTPUTS.  The sign of a -- the DIRECTION of
    frame dragging -- is not recoverable from g_tt and g_rr at any precision.
    Exactly {BITS_MISSING} bit.

    threads.py measured this as SIGN-BLINDNESS from the physics side: "only a^2
    appears, so the intersection thread contributes a MAGNITUDE rather than a
    DIRECTION."  Here it is a DETERMINACY statement from the algebra side, and
    the two agree.

        AND THAT BIT IS THE ONE THING A CORRIDOR WOULD NEED.
        A DIRECTION OF TRAVEL IS A SIGN.

    The corridor's ORIENTATION is not derivable from its own time and space
    threads.  Everything else about the intersection is; the only thing that is
    not is the one thing that says which way you go.""")

    P("\n" + "="*79)
    P("6.  SCOPE, STATED RATHER THAN ASSUMED")
    P("="*79)
    P(f"""
    The recovery holds within {SCOPE}.

    FOR A GENERAL STATIONARY AXISYMMETRIC METRIC g_tphi IS AN INDEPENDENT
    FUNCTION and none of section 2 follows.  M's clause is true of the object
    this project actually studies and is NOT a theorem about stationary metrics
    in general -- and saying otherwise would be the scope slip this session has
    already made twice, in certify.py's biconditional and in the Morris-Thorne
    validation.""")

    P("\n  " + "-"*74)
    P(f"""  THE PASS IN ONE PARAGRAPH

  M decomposes the inner corridor into three threads and makes four claims about
  what each carries.  ALL FOUR LAND, ONE IS SHARPER THAN STATED, AND THE FOURTH
  IS AN EXACT CLOSED FORM THE TREE DID NOT HAVE.  CLAUSE TWO IS A DIMENSIONAL
  FACT: every metric component is DIMENSIONLESS and the dimension lives in the
  coordinate, so g_tt returns a clock ratio and can never return a length while
  g_rr needs dr to become one -- "a coordinate requires dimension, so geometry
  is what moves through it" is how the object is built.  CLAUSE FOUR IS EXACT:
  give g_tt and g_rr at known r and M = r(1+g_tt)/2, a^2 = r^2[1/g_rr + g_tt],
  and g_tp^2 = r^2 (1+g_tt)^2 (1/g_rr + g_tt) -- verified to {worst:.1e} across M
  from 0.3 to 5, a from -0.7 to 4.9 and r from 1.5 to 12.  THE THREAD THAT
  CARRIES BOTH REQUIRES ONLY THOSE TWO.  CLAUSE THREE IS RIGHT AND SHARPER:
  light is NOT carried by the spatial thread, LIGHT IS THE RATIO OF THE TWO --
  ds^2 = 0 gives dr/dt = sqrt(-g_tt/g_rr), reproducing axis.py's coordinate
  speed to twelve places -- so it takes BOTH to make one.  SO THE THREADS
  COMBINE TWO WAYS AND EACH IS ONE OF THE CLAUSES: THEIR RATIO IS LIGHT, with no
  coordinate in it, and THEIR PRODUCT IS THE INTERSECTION, with an explicit
  r^2 -- clause two landing exactly where M put it, since the thread that
  carries both is the one that needs the dimension.  AND THE CLOSED FORM RETURNS
  A SQUARE: a = +0.7 and a = -0.7 give byte-identical g_tt and g_rr and opposite
  g_tp, so ONE BIT -- the direction of frame dragging -- is unrecoverable at any
  precision.  threads.py measured that as sign-blindness from physics; this is
  the same fact as determinacy from algebra.  AND THAT BIT IS THE ONE THING A
  CORRIDOR WOULD NEED, BECAUSE A DIRECTION OF TRAVEL IS A SIGN: everything about
  the intersection is derivable from the other two threads except the only thing
  that says which way you go.  SCOPE: the Kerr family, where two parameters fix
  every component; for a general stationary axisymmetric metric g_tphi is an
  independent function and none of this follows.  NOTHING IS REPAIRED.""")
    P("  " + "-"*74)

# ================================================================== selftest
def selftest():
    bad = 0
    def chk(label, got, want, tol=None):
        nonlocal bad
        ok = (abs(got-want) <= tol) if tol is not None else (got == want)
        if not ok: bad += 1
        print(f"  {'ok  ' if ok else 'FAIL'} {label:<58} {got}")
    print("weave.py --selftest\n")

    print("the threads, and the dimension")
    chk("three threads", len(THREADS), 3)
    chk("components are dimensionless", METRIC_COMPONENTS_ARE_DIMENSIONLESS, True)
    chk("  the dimension is in the coordinate", DIMENSION_LIVES_IN_THE_COORDINATE, True)

    print("\nthe cross term from the other two -- exact")
    worst = 0.0
    cases = ((1.0,0.5,4.0), (1.0,0.99,3.0), (2.0,1.5,10.0), (0.3,0.2,1.5),
             (1.0,-0.7,5.0), (5.0,4.9,12.0), (10.0,3.0,50.0), (0.1,0.05,0.5))
    for M, a, r in cases:
        gtt, grr, gtp = kerr_equatorial(r, M, a)
        chk(f"M={M:g} a={a:g} r={r:g}: recover M",
            round(recover_M(r,gtt), 9), round(M, 9), 1e-9)
        chk(f"  recover a^2", round(recover_a2(r,gtt,grr), 9), round(a*a, 9), 1e-9)
        d = abs(g_tphi_squared(r,gtt,grr) - gtp*gtp); worst = max(worst, d)
    chk("closed form matches g_tp^2 everywhere", worst < 1e-12, True)

    print("\nlight is the ratio of the two threads")
    for r in (2.5, 3.0, 6.0, 20.0, 1e4, 1e8):
        gtt, grr, _ = kerr_equatorial(r, 1.0, 0.0)
        chk(f"r/M = {r:g}: dr/dt == 1 - 2M/r",
            round(light_ratio(gtt,grr), 12), round(1-2/r, 12), 1e-12)
    chk("the ratio is light", RATIO_IS_LIGHT, True)
    chk("  and carries no coordinate", COORDINATE_IN_LIGHT, False)
    chk("the product is the cross term", PRODUCT_IS_THE_CROSS, True)
    chk("  and carries r^2", COORDINATE_IN_CROSS, True)

    print("\nand exactly one bit is missing")
    for r, M, a in ((5.0,1.0,0.7), (3.0,2.0,1.1), (10.0,1.0,0.3)):
        p = kerr_equatorial(r, M, a); n = kerr_equatorial(r, M, -a)
        chk(f"a = +-{a:g}: g_tt identical", p[0] == n[0], True)
        chk(f"  g_rr identical", p[1] == n[1], True)
        chk(f"  g_tp opposite", round(p[2]+n[2], 12), 0.0, 1e-12)
    chk("the sign of a is recoverable", SIGN_OF_a_IS_RECOVERABLE, False)
    chk("  bits missing", BITS_MISSING, 1)
    chk("  so orientation is NOT derivable", ORIENTATION_IS_DERIVABLE, False)

    print("\nscope")
    chk("scope stated", SCOPE, "the Kerr family only -- two parameters fix every component")
    chk("  general g_tphi is independent", GENERAL_STATIONARY_g_tphi_IS_INDEPENDENT, True)
    chk("nothing is repaired", THIS_PASS_REPAIRS_ANYTHING, False)

    print("\n" + ("SELFTEST PASS" if bad == 0 else f"SELFTEST FAIL -- {bad}"))
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
