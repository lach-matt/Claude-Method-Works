#!/usr/bin/env python3.12
"""cube.py -- evaluate g_tphi CUBED.

M: "We need to evaluate g_tphi cubed."

weave.py established that the intersection thread is recoverable from the other
two only as a SQUARE, and that the lost bit -- the sign of a, the direction of
frame dragging -- is the one thing a corridor would need.  An ODD power is the
only object that could carry that sign, so the cube is exactly the right thing
to ask for.

This file evaluates it.  Six results:

  1.  THE CUBE IN CLOSED FORM.  g_tphi = -(1 + g_tt) a exactly, so
      g_tphi^3 = -(1 + g_tt)^3 a^3, and therefore

              g_tphi^3 = sgn(g_tphi) * (g_tphi^2)^{3/2}

      EXACTLY.  The cube is the square to the three-halves, times the sign.
      It carries the square's content and the one bit and NOTHING ELSE.

  2.  AND IT CANNOT BE COMPUTED FROM THE OTHER TWO -- AS A PARITY THEOREM,
      not as a numerical failure.  Census of all five nonzero Boyer-Lindquist
      components under a -> -a: FOUR ARE EVEN AND EXACTLY ONE IS ODD, and the
      odd one is g_tphi.  Any function whatever of even quantities is even; any
      odd power of g_tphi is odd.  No closed form of any kind exists.

  3.  THE CIRCULARITY IS EXACT AND HAS A SHAPE THIS PROJECT ALREADY HOLDS.
      To evaluate the cube you need the sign; the sign is what the cube would
      tell you.  That is the algebraic shape of roundtrip.py's one-way speed --
      the measurement presupposes its own answer.  THE PHYSICS STATUS IS NOT
      THE SAME and the disanalogy is recorded rather than glossed: Reichenbach's
      epsilon is a CONVENTION, and sign(a) is a FACT.

  4.  AND KERR'S OWN CURVATURE ALREADY STATES THE CUBE-FROM-SQUARE RELATION.
      The Weyl invariants of a type D vacuum are I = 3 psi2^2 and J = -psi2^3 --
      a square and a CUBE -- and the type D condition is I^3 = 27 J^2.  A cube
      determined by a square, up to one sign.  THE SAME SHAPE, AND IT IS A
      THEOREM ABOUT THIS METRIC RATHER THAN AN ANALOGY.

  5.  THE STRONGEST RESULT GOES THE OTHER WAY.  On the equatorial plane the
      spin is absent from LOCAL CURVATURE ENTIRELY, not merely its sign:
      psi2 = -M/(r - i a cos th)^3 reduces to -M/r^3 at th = pi/2, so the
      Kretschmann scalar EQUALS SCHWARZSCHILD'S EXACTLY at the same r and the
      Chern-Pontryagin scalar VANISHES IDENTICALLY.  a^2 lives in the metric
      COMPONENTS and in no polynomial curvature invariant on that slice.

  6.  SO THERE ARE EXACTLY TWO WAYS TO GET THE BIT, AND BOTH LEAVE WHERE THE
      TWO THREADS ARE.  LOCALLY, LEAVE THE PLANE: *RR is proportional to
      a cos th and its normal derivative at the equator is nonzero and odd.
      NON-LOCALLY, STAY ON THE PLANE AND GO AROUND: the Sagnac difference
      dt = -4 pi g_tphi/g_tt is LINEAR in g_tphi, and the prograde/retrograde
      photon spheres split.  A DIRECTION OF TRAVEL IS A CHIRALITY, AND A
      CHIRALITY IS NOT A LOCAL SCALAR.

Scope: the Kerr family, as in weave.py.  Stdlib only.  Nothing is repaired.

    python3.12 cube.py            full report
    python3.12 cube.py --selftest fixtures are this tree's own recorded numbers
"""

import cmath
import math
import sys

# --------------------------------------------------------------------------
# The metric, general theta.  weave.py's kerr_equatorial is the th = pi/2 case.
# --------------------------------------------------------------------------

def kerr(r, th, M, a):
    """The five nonzero Boyer-Lindquist components.  Returns a dict."""
    c, s = math.cos(th), math.sin(th)
    S = r * r + a * a * c * c            # Sigma
    D = r * r - 2.0 * M * r + a * a      # Delta
    return {
        "g_tt":   -(1.0 - 2.0 * M * r / S),
        "g_rr":   S / D,
        "g_thth": S,
        "g_pp":   (r * r + a * a + 2.0 * M * r * a * a * s * s / S) * s * s,
        "g_tp":   -2.0 * M * r * a * s * s / S,
    }

COMPONENTS = ("g_tt", "g_rr", "g_thth", "g_pp", "g_tp")


def parity(name, r, th, M, a):
    """+1 if the component is EVEN under a -> -a, -1 if ODD, 0 if neither."""
    p = kerr(r, th, M, a)[name]
    m = kerr(r, th, M, -a)[name]
    scale = max(abs(p), abs(m), 1e-300)
    if abs(p - m) / scale < 1e-13:
        return +1
    if abs(p + m) / scale < 1e-13:
        return -1
    return 0


# --------------------------------------------------------------------------
# 1.  The cube in closed form.
# --------------------------------------------------------------------------

def g_tp_from_threads(r, g_tt, g_rr, sign_a):
    """The intersection thread from the other two PLUS the one bit."""
    a = sign_a * r * math.sqrt(1.0 / g_rr + g_tt)
    return -(1.0 + g_tt) * a


def g_tp_squared(r, g_tt, g_rr):
    """weave.py's closed form.  No sign needed and none returned."""
    return r * r * (1.0 + g_tt) ** 2 * (1.0 / g_rr + g_tt)


def g_tp_cubed(r, g_tt, g_rr, sign_a):
    """The cube.  Note the third argument: it is the whole finding."""
    return g_tp_from_threads(r, g_tt, g_rr, sign_a) ** 3


def cube_from_square(sq, sign):
    """g_tphi^3 = sgn * (g_tphi^2)^{3/2}.  Exact, and useless without sgn."""
    return sign * sq ** 1.5


# --------------------------------------------------------------------------
# 4/5.  Curvature.  Type D vacuum: every polynomial invariant is a function
#       of the one Weyl scalar psi2.
# --------------------------------------------------------------------------

def psi2(r, th, M, a):
    return -M / (r - 1j * a * math.cos(th)) ** 3


def kretschmann(r, th, M, a):
    """R_abcd R^abcd = 48 Re(psi2^2) for a type D vacuum."""
    return 48.0 * (psi2(r, th, M, a) ** 2).real


def kretschmann_poly(r, th, M, a):
    """The textbook polynomial form, as an independent cross-check."""
    y = a * math.cos(th)
    S = r * r + y * y
    return 48.0 * M * M * (r ** 6 - 15 * r ** 4 * y * y
                           + 15 * r * r * y ** 4 - y ** 6) / S ** 6


def pontryagin(r, th, M, a):
    """*RR = R_abcd *R^abcd = -96 Im(psi2^2).

    The overall sign convention varies in the literature.  It does not affect
    either finding here: the PARITY in a and the VANISHING at th = pi/2 are
    convention-independent.
    """
    return -96.0 * (psi2(r, th, M, a) ** 2).imag


def pontryagin_poly(r, th, M, a):
    y = a * math.cos(th)
    S = r * r + y * y
    return -192.0 * M * M * r * y * (3.0 * r * r - y * y) * (r * r - 3.0 * y * y) / S ** 6


def speciality(r, th, M, a):
    """S = 27 J^2 / I^3.  Exactly 1 for type D -- the cube-from-square theorem."""
    p = psi2(r, th, M, a)
    I = 3.0 * p ** 2
    J = -(p ** 3)
    return 27.0 * J ** 2 / I ** 3


def dPontryagin_dtheta(r, M, a, h=1e-5):
    """The normal derivative of the chirality invariant AT the equator."""
    th = math.pi / 2.0
    return (pontryagin(r, th + h, M, a) - pontryagin(r, th - h, M, a)) / (2.0 * h)


def dPontryagin_dtheta_exact(r, M, a):
    """Closed form: d/dth of -192 M^2 r y (3r^2-y^2)(r^2-3y^2)/Sigma^6 at y=0,
    where y = a cos th and dy/dth = -a at th = pi/2."""
    return +192.0 * M * M * a * 3.0 * r ** 5 / r ** 12


# --------------------------------------------------------------------------
# 6.  The two recoveries.
# --------------------------------------------------------------------------

def sagnac(r, th, M, a):
    """Prograde minus retrograde coordinate time for a circular light path.

    Returns (t_prograde, t_retrograde, difference).  The difference is LINEAR
    in g_tphi and therefore ODD in a.
    """
    g = kerr(r, th, M, a)
    disc = g["g_tp"] ** 2 - g["g_tt"] * g["g_pp"]
    root = math.sqrt(disc)
    p1 = (-g["g_tp"] + root) / g["g_tt"]
    p2 = (-g["g_tp"] - root) / g["g_tt"]
    hi, lo = max(p1, p2), min(p1, p2)
    t_pro = 2.0 * math.pi * hi          # dphi = +2pi
    t_ret = -2.0 * math.pi * lo         # dphi = -2pi
    return t_pro, t_ret, t_pro - t_ret


def sagnac_closed(r, th, M, a):
    g = kerr(r, th, M, a)
    return -4.0 * math.pi * g["g_tp"] / g["g_tt"]


def photon_sphere(M, a, prograde=True):
    """Equatorial circular photon orbit.  |a| <= M."""
    x = (-a / M) if prograde else (a / M)
    return 2.0 * M * (1.0 + math.cos((2.0 / 3.0) * math.acos(x)))


def zamo_omega(r, th, M, a):
    g = kerr(r, th, M, a)
    return -g["g_tp"] / g["g_pp"]


# --------------------------------------------------------------------------
# Recorded verdicts.  A status is never flattened.
# --------------------------------------------------------------------------

CUBE_IS_INDEPENDENT_OF_THE_SQUARE = False
CUBE_RECOVERABLE_FROM_TWO_THREADS = False
OBSTRUCTION_IS = "parity: four components even in a, exactly one odd"
OBSTRUCTION_IS_NUMERICAL = False
BITS_MISSING_FROM_THE_CUBE = 1
EQUATORIAL_CURVATURE_CARRIES_a = False
LOCAL_RECOVERY_REQUIRES = "leaving the equatorial plane"
NONLOCAL_RECOVERY_REQUIRES = "circulation, not reciprocation"
SIGN_OF_a_IS_A_CONVENTION = False
SCOPE = "the Kerr family only, as in weave.py"
NOTHING_IS_REPAIRED = True


# --------------------------------------------------------------------------

BAR = "=" * 79


def report():
    W = 1.0  # M = 1 throughout unless stated

    print(__doc__.split("Scope:")[0].rstrip())
    print()
    print(BAR)
    print("1.  THE CUBE IN CLOSED FORM -- AND IT IS THE SQUARE TO THE 3/2")
    print(BAR)
    print()
    print("    g_tphi = -(1 + g_tt) a          so       g_tphi^3 = -(1 + g_tt)^3 a^3")
    print("    g_tphi^2 = r^2 (1+g_tt)^2 (1/g_rr + g_tt)        [weave.py, exact]")
    print()
    print("      %5s %6s %6s %16s %16s %16s %9s"
          % ("M", "a", "r", "g_tphi", "g_tphi^3", "sgn*(sq)^1.5", "ratio"))
    cases = [(1.0, 0.5, 4.0), (1.0, 0.99, 3.0), (1.0, -0.7, 5.0),
             (2.0, 1.5, 10.0), (0.3, 0.2, 1.5), (5.0, 4.9, 12.0)]
    worst = 0.0
    for M, a, r in cases:
        g = kerr(r, math.pi / 2, M, a)
        sgn = 1.0 if g["g_tp"] >= 0 else -1.0
        sq = g_tp_squared(r, g["g_tt"], g["g_rr"])
        cu = g["g_tp"] ** 3
        cs = cube_from_square(sq, sgn)
        ratio = cu / cs
        worst = max(worst, abs(ratio - 1.0))
        print("      %5.2f %6.2f %6.2f %16.9f %16.9f %16.9f %9.6f"
              % (M, a, r, g["g_tp"], cu, cs, ratio))
    print()
    print("      IDENTICAL TO %.1e.  THE CUBE IS THE SQUARE TO THE THREE-HALVES," % worst)
    print("      TIMES THE SIGN.  It adds the one bit and NOTHING ELSE -- and the")
    print("      sign is the input the two threads cannot supply.")
    print()
    print("      g_tphi^3 / g_tphi^2 = g_tphi.  Knowing the cube IS knowing the")
    print("      third thread.  THE CUBE IS NOT A DERIVATION OF THE INTERSECTION")
    print("      FROM THE OTHER TWO; IT IS THE INTERSECTION.")
    print()

    print(BAR)
    print("2.  AND IT CANNOT BE DERIVED -- A PARITY THEOREM, NOT A SEARCH FAILURE")
    print(BAR)
    print()
    print("    Census of every nonzero component under  a -> -a  (M=1, a=0.7,")
    print("    r=5, th=1.1 rad, off the plane so nothing is degenerate):")
    print()
    print("      %-8s %18s %18s   %s" % ("", "a = +0.7", "a = -0.7", "parity"))
    npar = {}
    for name in COMPONENTS:
        p = kerr(5.0, 1.1, 1.0, 0.7)[name]
        m = kerr(5.0, 1.1, 1.0, -0.7)[name]
        par = parity(name, 5.0, 1.1, 1.0, 0.7)
        npar[name] = par
        tag = {+1: "EVEN", -1: "ODD ", 0: "----"}[par]
        print("      %-8s %18.12f %18.12f   %s" % (name, p, m, tag))
    n_even = sum(1 for v in npar.values() if v == +1)
    n_odd = sum(1 for v in npar.values() if v == -1)
    print()
    print("      %d EVEN, %d ODD.  The odd one is %s."
          % (n_even, n_odd, [k for k, v in npar.items() if v == -1][0]))
    print()
    print("      THEOREM.  Any function whatever of even quantities is even.")
    print("      g_tphi^(2k+1) is odd.  So NO closed form in g_tt, g_rr, g_thth")
    print("      and g_pp returns any odd power of g_tphi -- not the cube, not")
    print("      the first power, not at any precision and not with any amount")
    print("      of cleverness.  THE OBSTRUCTION IS A SYMMETRY, NOT A DIFFICULTY.")
    print()

    print(BAR)
    print("3.  THE CIRCULARITY, AND THE DISANALOGY THAT MUST NOT BE GLOSSED")
    print(BAR)
    print()
    print("      To evaluate g_tphi^3 you need sgn(a).")
    print("      sgn(a) is what g_tphi^3 would tell you.")
    print()
    print("    That is exactly roundtrip.py's shape: THE MEASUREMENT PRESUPPOSES")
    print("    ITS OWN ANSWER.  To measure a one-way speed you must synchronise")
    print("    two clocks; to synchronise them you must assume a one-way time.")
    print()
    print("    AND THE PHYSICS STATUS IS DIFFERENT, WHICH IS THE PART WORTH")
    print("    SAYING.  Reichenbach's epsilon is a CONVENTION -- no experiment")
    print("    distinguishes eps = 0.1 from eps = 0.5.  sgn(a) IS A FACT: two")
    print("    experiments below return it.  SAME ALGEBRA, OPPOSITE STANDING.")
    print("    A shape shared is not a status shared.")
    print()

    print(BAR)
    print("4.  KERR'S OWN CURVATURE ALREADY STATES CUBE-FROM-SQUARE")
    print(BAR)
    print()
    print("    For a type D vacuum every polynomial Weyl invariant is a function")
    print("    of one scalar:  I = 3 psi2^2   (a SQUARE)   J = -psi2^3  (a CUBE)")
    print()
    print("      and the type D condition is        I^3 = 27 J^2")
    print()
    print("      %6s %6s %8s %26s %20s" % ("a", "r", "theta", "27 J^2 / I^3", "|dev from 1|"))
    sworst = 0.0
    for a, r, th in [(0.7, 5.0, 1.1), (0.99, 3.0, 0.4), (-0.5, 8.0, 2.0),
                     (0.3, 20.0, math.pi / 2), (4.9, 12.0, 0.9)]:
        S = speciality(r, th, 1.0, a)
        d = abs(S - 1.0)
        sworst = max(sworst, d)
        print("      %6.2f %6.2f %8.4f %26s %20.1e"
              % (a, r, th, "%.12f%+.12fj" % (S.real, S.imag), d))
    print()
    print("      EXACT TO %.1e.  A CUBE FIXED BY A SQUARE, UP TO ONE SIGN --" % sworst)
    print("      J = +/- sqrt(I^3/27), THE SAME ONE BIT.  M's question is not an")
    print("      analogy to Kerr's algebraic type; IT IS KERR'S ALGEBRAIC TYPE.")
    print()

    print(BAR)
    print("5.  AND ON THE EQUATOR THE SPIN IS ABSENT FROM CURVATURE ENTIRELY")
    print(BAR)
    print()
    print("    psi2 = -M/(r - i a cos th)^3.  At th = pi/2, cos th = 0, so")
    print("    psi2 = -M/r^3 -- SCHWARZSCHILD'S, WITH NO a IN IT AT ALL.")
    print()
    print("      %7s %16s %16s %16s %14s"
          % ("a", "K (Kerr, eq)", "K (Schw, same r)", "K (polynomial)", "*RR (eq)"))
    r = 5.0
    Kschw = 48.0 * 1.0 / r ** 6
    kworst = pworst = 0.0
    for a in (0.0, 0.3, 0.7, 0.99, 2.5, -0.7):
        K = kretschmann(r, math.pi / 2, 1.0, a)
        Kp = kretschmann_poly(r, math.pi / 2, 1.0, a)
        P = pontryagin(r, math.pi / 2, 1.0, a)
        kworst = max(kworst, abs(K - Kschw), abs(K - Kp))
        pworst = max(pworst, abs(P))
        print("      %7.2f %16.12f %16.12f %16.12f %14.1e" % (a, K, Kschw, Kp, P))
    print()
    print("      KRETSCHMANN AGREES WITH SCHWARZSCHILD TO %.1e -- and the two" % kworst)
    print("      independent expressions (psi2 route, textbook polynomial) agree")
    print("      to the same.  CHERN-PONTRYAGIN IS %.1e, i.e. ZERO." % pworst)
    print()
    print("      SO a^2 LIVES IN THE METRIC COMPONENTS AND IN NO POLYNOMIAL")
    print("      CURVATURE INVARIANT ON THAT SLICE.  weave.py recovered a^2 from")
    print("      g_tt and g_rr, and that recovery is a statement about COORDINATE")
    print("      COMPONENTS, not about local curvature.  Both are true and the")
    print("      distinction is the finding.")
    print()
    print("      SCOPE, NARROW AND DELIBERATE: this is the POLYNOMIAL (zeroth")
    print("      order) invariants.  DIFFERENTIAL invariants are NOT functions of")
    print("      psi2 alone and are NOT covered -- and section 6 shows one that")
    print("      does see a.  Saying 'the curvature cannot see the spin' without")
    print("      that qualifier would be false.")
    print()

    print(BAR)
    print("6.  TWO RECOVERIES, AND BOTH LEAVE WHERE THE TWO THREADS ARE")
    print(BAR)
    print()
    print("  (a)  LOCAL -- LEAVE THE PLANE.  *RR is proportional to a cos th.")
    print()
    print("      %8s %16s %16s %14s" % ("theta", "*RR (a=+0.7)", "*RR (a=-0.7)", "parity"))
    for th in (0.3, 0.8, math.pi / 2, 2.4, 2.9):
        pp = pontryagin(5.0, th, 1.0, 0.7)
        pm = pontryagin(5.0, th, 1.0, -0.7)
        tag = "ODD" if abs(pp + pm) < 1e-13 * max(abs(pp), 1e-300) or (pp == 0 and pm == 0) else "?"
        print("      %8.4f %16.9e %16.9e %14s" % (th, pp, pm, tag))
    d_num = dPontryagin_dtheta(5.0, 1.0, 0.7)
    d_exa = dPontryagin_dtheta_exact(5.0, 1.0, 0.7)
    d_neg = dPontryagin_dtheta(5.0, 1.0, -0.7)
    print()
    print("      AND THE NORMAL DERIVATIVE AT THE EQUATOR IS NOT ZERO:")
    print("        d(*RR)/dtheta at th=pi/2, a=+0.7 : %+.9f  (closed form %+.9f)"
          % (d_num, d_exa))
    print("        d(*RR)/dtheta at th=pi/2, a=-0.7 : %+.9f" % d_neg)
    print("        sum %.1e -- ODD, so the sign IS a local fact one derivative"
          % abs(d_num + d_neg))
    print("        off the plane, even though it is not one ON the plane.")
    print()
    print("  (b)  NON-LOCAL -- STAY ON THE PLANE AND GO AROUND.")
    print()
    print("      %6s %6s %14s %14s %14s %14s"
          % ("a", "r", "t_prograde", "t_retrograde", "difference", "-4pi g_tp/g_tt"))
    sworst2 = 0.0
    for a, r in [(0.7, 5.0), (-0.7, 5.0), (0.99, 6.0), (0.0, 5.0), (0.3, 20.0)]:
        tp, tr, dt = sagnac(r, math.pi / 2, 1.0, a)
        cl = sagnac_closed(r, math.pi / 2, 1.0, a)
        sworst2 = max(sworst2, abs(dt - cl))
        print("      %6.2f %6.2f %14.9f %14.9f %+14.9f %+14.9f" % (a, r, tp, tr, dt, cl))
    print()
    print("      The two routes agree to %.1e.  THE DIFFERENCE IS LINEAR IN" % sworst2)
    print("      g_tphi AND THEREFORE ODD IN a: it is zero at a = 0 and it flips.")
    print("      A prograde and a retrograde loop are DIFFERENT LOOPS; an")
    print("      out-and-back along one radius is not.  THE DISCRIMINATOR IS")
    print("      CIRCULATION, NOT RECIPROCATION.")
    print()
    print("      And the photon spheres split the same way:")
    print("      %8s %14s %14s %14s" % ("a", "prograde", "retrograde", "split"))
    for a in (0.0, 0.3, 0.7, 0.99, 1.0):
        pr, re = photon_sphere(1.0, a, True), photon_sphere(1.0, a, False)
        print("      %8.2f %14.9f %14.9f %14.9f" % (a, pr, re, re - pr))
    print()
    print("      Extremal: prograde %.6f M, retrograde %.6f M -- a factor of %.1f."
          % (photon_sphere(1.0, 1.0, True), photon_sphere(1.0, 1.0, False),
             photon_sphere(1.0, 1.0, False) / photon_sphere(1.0, 1.0, True)))
    print()

    print(BAR)
    print("WHAT IT MEANS FOR THE CORRIDOR")
    print(BAR)
    print()
    print("    weave.py: the corridor's ORIENTATION is not derivable from its own")
    print("    time and space threads.  THE CUBE DOES NOT FIX THAT AND CANNOT,")
    print("    and now we know why rather than merely that: THE OBSTRUCTION IS A")
    print("    PARITY, AND A PARITY IS NOT DEFEATED BY A HIGHER POWER.")
    print()
    print("    A DIRECTION OF TRAVEL IS A CHIRALITY, AND A CHIRALITY IS NOT A")
    print("    LOCAL SCALAR ON THE PLANE IT LIVES IN.  To install one you must")
    print("    either LEAVE THE PLANE or GO AROUND THE RING.  Both are things a")
    print("    construction must SUPPLY -- a source that rotates, or a path that")
    print("    circulates -- and neither is read off a point.")
    print()
    print("    THAT IS M'S OWN METHOD CLAIM LANDING LITERALLY: axis.py recorded")
    print("    'all perceptions are one whole viewed from a different axis or")
    print("    plane or dimension position'.  Here the missing datum is invisible")
    print("    AT th = pi/2 AND VISIBLE AT th != pi/2.  The plane position is not")
    print("    a metaphor in this instance -- IT IS THE POLAR ANGLE.")
    print()
    print("    SCOPE: %s." % SCOPE)
    print("    Nothing here is repaired.")
    print()


# --------------------------------------------------------------------------

def selftest():
    fails = []

    def chk(label, got, want, tol=None):
        if tol is None:
            ok = (got == want)
        else:
            ok = abs(got - want) <= tol
        print("  %-4s %-58s %s" % ("ok" if ok else "FAIL", label, got))
        if not ok:
            fails.append((label, got, want))

    print("cube.py --selftest")
    print()

    # weave.py's own recorded configuration.
    g = kerr(5.0, math.pi / 2, 1.0, 0.7)
    chk("weave.py's g_tt at M=1 a=0.7 r=5", round(g["g_tt"], 12), -0.6)
    chk("weave.py's g_rr", round(g["g_rr"], 12), 1.613944480310)
    chk("weave.py's g_tp", round(g["g_tp"], 12), -0.28)
    gm = kerr(5.0, math.pi / 2, 1.0, -0.7)
    chk("g_tp flips with a", round(gm["g_tp"], 12), +0.28)

    # 1.  cube = sign * square^{3/2}
    worst = 0.0
    for M, a, r in [(1.0, 0.5, 4.0), (1.0, -0.7, 5.0), (5.0, 4.9, 12.0), (0.3, 0.2, 1.5)]:
        gg = kerr(r, math.pi / 2, M, a)
        sq = g_tp_squared(r, gg["g_tt"], gg["g_rr"])
        sgn = 1.0 if gg["g_tp"] >= 0 else -1.0
        worst = max(worst, abs(gg["g_tp"] ** 3 - cube_from_square(sq, sgn)))
    chk("cube = sgn * square^1.5", worst < 1e-12, True)

    # the cube reconstructed with the bit supplied
    gg = kerr(5.0, math.pi / 2, 1.0, 0.7)
    chk("cube from threads + bit", round(g_tp_cubed(5.0, gg["g_tt"], gg["g_rr"], +1.0), 12),
        round(gg["g_tp"] ** 3, 12))

    # 2.  parity census
    pars = {n: parity(n, 5.0, 1.1, 1.0, 0.7) for n in COMPONENTS}
    chk("components even in a", sum(1 for v in pars.values() if v == +1), 4)
    chk("components odd in a", sum(1 for v in pars.values() if v == -1), 1)
    chk("the odd one is g_tp", [k for k, v in pars.items() if v == -1], ["g_tp"])
    chk("cube recoverable from the two threads", CUBE_RECOVERABLE_FROM_TWO_THREADS, False)
    chk("bits missing from the cube", BITS_MISSING_FROM_THE_CUBE, 1)

    # 4.  speciality index
    sworst = 0.0
    for a, r, th in [(0.7, 5.0, 1.1), (0.99, 3.0, 0.4), (-0.5, 8.0, 2.0), (4.9, 12.0, 0.9)]:
        sworst = max(sworst, abs(speciality(r, th, 1.0, a) - 1.0))
    chk("27 J^2 / I^3 = 1 (type D)", sworst < 1e-12, True)

    # 5.  equatorial curvature
    Kschw = 48.0 / 5.0 ** 6
    kw = pw = xw = 0.0
    for a in (0.0, 0.3, 0.7, 0.99, 2.5, -0.7):
        K = kretschmann(5.0, math.pi / 2, 1.0, a)
        kw = max(kw, abs(K - Kschw))
        xw = max(xw, abs(K - kretschmann_poly(5.0, math.pi / 2, 1.0, a)))
        pw = max(pw, abs(pontryagin(5.0, math.pi / 2, 1.0, a)))
    chk("equatorial K equals Schwarzschild's", kw < 1e-15, True)
    chk("psi2 route agrees with the polynomial", xw < 1e-15, True)
    chk("equatorial *RR vanishes", pw < 1e-15, True)
    chk("equatorial curvature carries a", EQUATORIAL_CURVATURE_CARRIES_a, False)

    # 6a.  off-plane, and the normal derivative
    chk("*RR is nonzero off the plane",
        abs(pontryagin(5.0, 0.8, 1.0, 0.7)) > 1e-6, True)
    chk("*RR is odd in a",
        abs(pontryagin(5.0, 0.8, 1.0, 0.7) + pontryagin(5.0, 0.8, 1.0, -0.7)) < 1e-18, True)
    chk("*RR closed form agrees",
        abs(pontryagin(5.0, 0.8, 1.0, 0.7) - pontryagin_poly(5.0, 0.8, 1.0, 0.7)) < 1e-15, True)
    dn, de = dPontryagin_dtheta(5.0, 1.0, 0.7), dPontryagin_dtheta_exact(5.0, 1.0, 0.7)
    chk("d(*RR)/dtheta at the equator, numeric vs closed",
        abs(dn - de) < 1e-4 * abs(de), True)
    chk("that derivative is nonzero", abs(de) > 1e-6, True)
    chk("and odd in a",
        abs(dPontryagin_dtheta(5.0, 1.0, 0.7) + dPontryagin_dtheta(5.0, 1.0, -0.7)) < 1e-6, True)

    # 6b.  Sagnac
    sw = 0.0
    for a, r in [(0.7, 5.0), (-0.7, 5.0), (0.99, 6.0), (0.0, 5.0), (0.3, 20.0)]:
        _, _, dt = sagnac(r, math.pi / 2, 1.0, a)
        sw = max(sw, abs(dt - sagnac_closed(r, math.pi / 2, 1.0, a)))
    chk("Sagnac: explicit roots vs -4pi g_tp/g_tt", sw < 1e-9, True)
    _, _, d_p = sagnac(5.0, math.pi / 2, 1.0, 0.7)
    _, _, d_m = sagnac(5.0, math.pi / 2, 1.0, -0.7)
    chk("Sagnac is odd in a", abs(d_p + d_m) < 1e-9, True)
    chk("Sagnac vanishes at a = 0",
        abs(sagnac(5.0, math.pi / 2, 1.0, 0.0)[2]) < 1e-12, True)
    chk("prograde returns sooner for a > 0", d_p < 0.0, True)

    # photon spheres: the known extremal values
    chk("extremal prograde photon sphere = M",
        round(photon_sphere(1.0, 1.0, True), 9), 1.0)
    chk("extremal retrograde photon sphere = 4M",
        round(photon_sphere(1.0, 1.0, False), 9), 4.0)
    chk("Schwarzschild photon sphere = 3M",
        round(photon_sphere(1.0, 0.0, True), 9), 3.0)

    chk("sign of a is a convention", SIGN_OF_a_IS_A_CONVENTION, False)
    chk("scope stated", SCOPE, "the Kerr family only, as in weave.py")
    chk("nothing is repaired", NOTHING_IS_REPAIRED, True)

    print()
    if fails:
        for label, got, want in fails:
            print("  FAIL %s: got %r want %r" % (label, got, want))
        print("\nSELFTEST FAIL (%d)" % len(fails))
        return 1
    print("SELFTEST PASS")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
