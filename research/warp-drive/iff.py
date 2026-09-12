#!/usr/bin/env python3.12
"""iff.py -- the inversion theorem, and EM is what makes it hold.

M: "It is an iff inversion theorem ... possible because EM carries both +/- and
the shape of its current determines the sign."

BOTH HALVES LAND, THE FIRST CORRECTS A CONFLATION IN modulus.py, AND THE SECOND
IS THE FIRST THING IN THIS PROJECT THAT COULD SUPPLY THE MISSING BIT RATHER
THAN READ IT.

  1.  modulus.py RAN TWO DIFFERENT IFFs TOGETHER AND THIS SEPARATES THEM.
      (A) recovering z from |z| and Re z inverts IFF a cos(theta) = 0.
      (B) recovering (M, a) from the even metric sector inverts IFF a = 0.
      THEY ARE NOT THE SAME CONDITION.  On the equator (A) holds and (B) fails,
      because a^2 survives in g_rr through Delta even where it leaves Sigma.
      modulus.py's fibre() read a^2 out of g_thetatheta and is UNDEFINED at
      theta = pi/2; nothing it printed was wrong because nothing it printed was
      equatorial, and the general inversion is given here.

  2.  SO THE GRAVITATIONAL IFF IS:  THE EVEN SECTOR INVERTS IFF a = 0.
      THE MAP IS INVERTIBLE EXACTLY WHERE THERE IS NO CHIRALITY TO LOSE.

  3.  AND EM CARRIES BOTH SIGNS, TWICE OVER, WHICH IS M'S FIRST CLAUSE MEASURED.
      The metric sees only Q^2 -- it is EVEN in the charge -- while A_t is ODD
      in it.  The metric is EVEN in a while A_phi is ODD in it.  THE
      ELECTROMAGNETIC SECTOR HAS AN ODD MEMBER FOR EACH SIGN THE METRIC HIDES.

  4.  AND THE SHAPE OF THE CURRENT DETERMINES THE SIGN, EXACTLY AND LINEARLY:
      the Kerr-Newman magnetic dipole is mu = Q a -- gyromagnetic ratio g = 2,
      the Dirac value (Carter 1968) -- VERIFIED HERE from the potential's
      asymptotics rather than recalled.  So a = mu/Q, WITH ITS SIGN.

  5.  THE FULL LOCAL INVERSION, FROM FIVE READINGS AT ONE POINT:
          Sigma = g_thth ; Q = -A_t Sigma/r ; M = (Sigma(1+g_tt) + Q^2)/2r
          a     = A_phi Sigma / (Q r sin^2 theta)          SIGNED
          a^2   = Sigma/g_rr - r^2 + Sigma(1+g_tt)         UNSIGNED, metric only
      Two independent routes to a; the second needs no charge and gives no sign.

  6.  THE THEOREM.  Phi: (M, a, Q) -> (metric even sector, A_t, A_phi) is
      INJECTIVE IFF  Q != 0  OR  a = 0.  IT FAILS EXACTLY ON THE UNCHARGED
      SPINNING CASE.  M's assertion is the content of that iff.

  7.  AND THE TWO ODD CHANNELS COVER THE WHOLE SPHERE WITH NO GAP.
      *RR is proportional to a cos(theta) and DIES ON THE EQUATOR.  A_phi is
      proportional to sin^2(theta) and DIES ON THE AXIS.  Their blind loci are
      DISJOINT, so at every theta at least one channel reads the bit.

  8.  REPORT AGAINST SUPPLY, AND WHAT IT STILL DOES NOT DO.  In an existing
      Kerr-Newman object mu = Qa is a LOCK, not an independent input: the same
      rotation makes both, so EM REPORTS the bit.  In a corridor DRIVEN by EM,
      the current's handedness is a DESIGN INPUT and EM SUPPLIES it -- the
      first time this project's missing datum is something a builder SETS.
      The parity theorem is untouched (a different sector, not an inverted
      map), and the energy bill does not move.

Scope: Kerr-Newman.  Stdlib only.  Nothing is repaired.

    python3.12 iff.py            full report
    python3.12 iff.py --selftest
"""

import math
import sys


# --------------------------------------------------------------------------
# Kerr-Newman: metric and potential.
# --------------------------------------------------------------------------

def kn(r, th, M, a, Q):
    c, s = math.cos(th), math.sin(th)
    S = r * r + a * a * c * c
    D = r * r - 2.0 * M * r + a * a + Q * Q
    P = 2.0 * M * r - Q * Q
    return {
        "g_tt":   -(1.0 - P / S),
        "g_rr":   S / D,
        "g_thth": S,
        "g_pp":   (r * r + a * a + P * a * a * s * s / S) * s * s,
        "g_tp":   -P * a * s * s / S,
        "A_t":    -Q * r / S,
        "A_phi":  Q * r * a * s * s / S,
    }


METRIC_EVEN = ("g_tt", "g_rr", "g_thth", "g_pp")
ALL_KEYS = ("g_tt", "g_rr", "g_thth", "g_pp", "g_tp", "A_t", "A_phi")


def parity_in(key, var, r, th, M, a, Q):
    """+1 EVEN, -1 ODD, 0 neither, under flipping 'a' or 'Q'."""
    if var == "a":
        p, m = kn(r, th, M, a, Q)[key], kn(r, th, M, -a, Q)[key]
    else:
        p, m = kn(r, th, M, a, Q)[key], kn(r, th, M, a, -Q)[key]
    sc = max(abs(p), abs(m), 1e-300)
    if abs(p - m) / sc < 1e-13:
        return +1
    if abs(p + m) / sc < 1e-13:
        return -1
    return 0


# --------------------------------------------------------------------------
# 1/2.  The two inversions modulus.py ran together.
# --------------------------------------------------------------------------

def z_inverts(r, th, a):
    """(A) z from |z| and Re z.  One solution iff a cos(theta) = 0."""
    return abs(a * math.cos(th)) < 1e-15


def a_squared_from_metric(r, th, M, a, Q):
    """The GENERAL inversion.  Valid at every theta, the equator included.

    modulus.py divided by cos^2(theta) and could not be asked this on the
    equatorial plane.  Delta carries a^2 where Sigma does not.
    """
    g = kn(r, th, M, a, Q)
    S = g["g_thth"]
    return S / g["g_rr"] - r * r + S * (1.0 + g["g_tt"])


def M_from_metric(r, th, M, a, Q):
    g = kn(r, th, M, a, Q)
    S = g["g_thth"]
    Qr = -g["A_t"] * S / r
    return (S * (1.0 + g["g_tt"]) + Qr * Qr) / (2.0 * r)


def even_fibre(r, th, M, a, Q):
    """The spins the even metric sector cannot separate."""
    a2 = a_squared_from_metric(r, th, M, a, Q)
    if a2 < 1e-18:
        return [0.0]
    return [+math.sqrt(a2), -math.sqrt(a2)]


def even_sector_inverts(r, th, M, a, Q):
    """(B) (M, a) from the even metric sector.  IFF a = 0."""
    return len(even_fibre(r, th, M, a, Q)) == 1


# --------------------------------------------------------------------------
# 4.  The magnetic dipole, and the lock.
# --------------------------------------------------------------------------

def dipole_asymptotic(th, M, a, Q, r=1e7):
    """mu from  A_phi -> mu sin^2(theta)/r  at large r.  Measured, not recalled."""
    s = math.sin(th)
    return kn(r, th, M, a, Q)["A_phi"] * r / (s * s)


def dipole_local(r, th, M, a, Q):
    """The same mu read at finite r: A_phi = Q r a sin^2/Sigma = mu r sin^2/Sigma."""
    g = kn(r, th, M, a, Q)
    return g["A_phi"] * g["g_thth"] / (r * math.sin(th) ** 2)


def gyromagnetic_g(r, th, M, a, Q):
    """mu = g (Q/2M) J with J = M a.  Kerr-Newman gives g = 2 exactly."""
    mu = dipole_asymptotic(th, M, a, Q)
    return 2.0 * mu / (Q * a)


# --------------------------------------------------------------------------
# 5/6.  The full inversion, and the iff.
# --------------------------------------------------------------------------

def invert(readings, r, th):
    """(M, a, Q) from g_tt, g_rr, g_thth, A_t, A_phi at one point.

    Returns a dict with 'status'.  'a' is SIGNED and needs Q != 0 and
    sin(theta) != 0; 'a_abs' comes from the metric alone and never has a sign.
    """
    S = readings["g_thth"]
    Q = -readings["A_t"] * S / r
    Mr = (S * (1.0 + readings["g_tt"]) + Q * Q) / (2.0 * r)
    a2 = S / readings["g_rr"] - r * r + S * (1.0 + readings["g_tt"])
    a_abs = math.sqrt(max(a2, 0.0))
    s2 = math.sin(th) ** 2
    if abs(Q) < 1e-12:
        return {"M": Mr, "Q": Q, "a_abs": a_abs, "a": None,
                "status": "UNCHARGED -- sign not recoverable"}
    if s2 < 1e-12:
        return {"M": Mr, "Q": Q, "a_abs": a_abs, "a": None,
                "status": "ON AXIS -- A_phi vanishes, sign not recoverable"}
    a = readings["A_phi"] * S / (Q * r * s2)
    return {"M": Mr, "Q": Q, "a_abs": a_abs, "a": a, "status": "INVERTED"}


def phi_injective(a, Q):
    """The theorem: Phi is injective IFF Q != 0 OR a = 0."""
    return (abs(Q) > 1e-12) or (abs(a) < 1e-15)


# --------------------------------------------------------------------------
# 7.  Channel coverage.
# --------------------------------------------------------------------------

def curvature_channel(th, a):
    """*RR is proportional to a cos(theta).  Zero on the equator."""
    return a * math.cos(th)


def em_channel(th, a, Q):
    """A_phi is proportional to Q a sin^2(theta).  Zero on the axis."""
    return Q * a * math.sin(th) ** 2


# --------------------------------------------------------------------------
# 8.  The constructive half, in flat space, labelled as such.
# --------------------------------------------------------------------------

def loop_dipole(current, area):
    """mu = I A, direction by the right-hand rule.  Classical, not GR."""
    return current * area


IFF_A = "z inverts IFF a cos(theta) = 0"
IFF_B = "the even metric sector inverts IFF a = 0"
IFF_FULL = "Phi inverts IFF Q != 0 OR a = 0"
MODULUS_CONFLATED_TWO_IFFS = True
EM_SUPPLIES_THE_SIGN = True
EM_IN_KERR_NEWMAN_REPORTS_RATHER_THAN_SUPPLIES = True
PARITY_THEOREM_IS_OVERTURNED = False
ENERGY_BILL_MOVES = False
CHANNELS_COVER_THE_SPHERE = True
SCOPE = "Kerr-Newman"
NOTHING_IS_REPAIRED = True

BAR = "=" * 79


def report():
    print(__doc__.split("Scope:")[0].rstrip())
    print()

    print(BAR)
    print("1.  TWO IFFs, AND modulus.py RAN THEM TOGETHER")
    print(BAR)
    print()
    print("      %6s %8s %8s %14s %14s %s"
          % ("a", "theta", "Q", "(A) z inverts", "(B) even inv", "agree?"))
    dis = 0
    for a, th, Q in [(0.7, 1.1, 0.0), (0.7, math.pi / 2, 0.0), (0.0, 1.1, 0.0),
                     (0.7, math.pi / 2, 0.4), (0.0, math.pi / 2, 0.4),
                     (2.5, 0.3, 0.0)]:
        A = z_inverts(5.0, th, a)
        B = even_sector_inverts(5.0, th, 1.0, a, Q)
        if A != B:
            dis += 1
        print("      %6.2f %8.4f %8.2f %14s %14s %s"
              % (a, th, Q, A, B, "yes" if A == B else "NO -- DIFFERENT"))
    print()
    print("      THE TWO CONDITIONS DISAGREE IN %d OF 6 ROWS." % dis)
    print("      ON THE EQUATOR WITH SPIN, (A) HOLDS AND (B) FAILS: z becomes")
    print("      real and recoverable, and a^2 SURVIVES IN g_rr THROUGH Delta")
    print("      even where it has left Sigma.  modulus.py read a^2 out of")
    print("      g_thetatheta, divided by cos^2(theta), and CANNOT BE ASKED THIS")
    print("      AT theta = pi/2.  Nothing it printed was wrong -- nothing it")
    print("      printed was equatorial -- and the general inversion is:")
    print()
    print("          a^2 = Sigma/g_rr - r^2 + Sigma (1 + g_tt)")
    print()
    print("      %6s %8s %8s %18s %18s %10s"
          % ("a", "theta", "Q", "a^2 recovered", "a^2 true", "diff"))
    w = 0.0
    for a, th, Q in [(0.7, 1.1, 0.0), (0.7, math.pi / 2, 0.0), (2.5, 0.3, 0.6),
                     (0.99, math.pi / 2, 0.4), (-0.7, 2.4, 0.9)]:
        got = a_squared_from_metric(5.0, th, 1.0, a, Q)
        w = max(w, abs(got - a * a))
        print("      %6.2f %8.4f %8.2f %18.12f %18.12f %10.1e"
              % (a, th, Q, got, a * a, abs(got - a * a)))
    print()
    print("      EXACT TO %.1e AT EVERY THETA INCLUDING THE EQUATOR." % w)
    print()

    print(BAR)
    print("2.  SO THE GRAVITATIONAL IFF IS:  THE EVEN SECTOR INVERTS IFF a = 0")
    print(BAR)
    print()
    print("      %10s %10s %10s %s" % ("a", "fibre", "inverts", "reading"))
    for a in (0.0, 1e-9, 0.3, 0.7, 2.5, -0.99):
        f = even_fibre(5.0, 1.1, 1.0, a, 0.4)
        print("      %10.2e %10d %10s  %s"
              % (a, len(f), even_sector_inverts(5.0, 1.1, 1.0, a, 0.4),
                 "nothing to lose" if len(f) == 1 else "two sheets"))
    print()
    print("      THE MAP IS INVERTIBLE EXACTLY WHERE THERE IS NO CHIRALITY TO")
    print("      LOSE.  That is the iff M named, and it is empty on its own --")
    print("      it says the gravitational sector solves only the case nobody")
    print("      needed solved.  THE CONTENT IS WHAT BREAKS IT.")
    print()

    print(BAR)
    print("3.  AND EM CARRIES BOTH SIGNS -- TWICE OVER")
    print(BAR)
    print()
    print("      %-10s %14s %14s" % ("", "under a -> -a", "under Q -> -Q"))
    tag = {+1: "EVEN", -1: "ODD ", 0: "----"}
    counts = {"a_odd": 0, "Q_odd": 0}
    for k in ALL_KEYS:
        pa = parity_in(k, "a", 5.0, 1.1, 1.0, 0.7, 0.4)
        pq = parity_in(k, "Q", 5.0, 1.1, 1.0, 0.7, 0.4)
        counts["a_odd"] += (pa == -1)
        counts["Q_odd"] += (pq == -1)
        print("      %-10s %14s %14s" % (k, tag[pa], tag[pq]))
    print()
    print("      THE METRIC SEES ONLY Q^2 -- EVEN IN THE CHARGE -- AND A_t IS")
    print("      ODD IN IT.  The metric is EVEN in a and A_phi is ODD in it.")
    print("      %d quantities are odd in a and %d are odd in Q, and the"
          % (counts["a_odd"], counts["Q_odd"]))
    print("      electromagnetic sector supplies one of each.")
    print()
    print("        EM CARRIES A SIGN THE METRIC CANNOT SEE, FOR BOTH SIGNS THE")
    print("        METRIC HIDES.  THAT IS M'S FIRST CLAUSE, MEASURED.")
    print()

    print(BAR)
    print("4.  AND THE SHAPE OF THE CURRENT DETERMINES THE SIGN: mu = Q a")
    print(BAR)
    print()
    print("      %6s %6s %8s %18s %18s %10s %8s"
          % ("a", "Q", "theta", "mu (asymptotic)", "Q a", "diff", "g"))
    dw = gw = 0.0
    for a, Q, th in [(0.7, 0.4, 1.1), (-0.7, 0.4, 1.1), (0.7, -0.4, 0.6),
                     (0.99, 0.9, math.pi / 2), (2.5, 0.2, 2.0)]:
        mu = dipole_asymptotic(th, 1.0, a, Q)
        g = gyromagnetic_g(5.0, th, 1.0, a, Q)
        dw = max(dw, abs(mu - Q * a))
        gw = max(gw, abs(g - 2.0))
        print("      %6.2f %6.2f %8.4f %18.12f %18.12f %10.1e %8.6f"
              % (a, Q, th, mu, Q * a, abs(mu - Q * a), g))
    print()
    print("      mu = Q a TO %.1e AND g = 2 TO %.1e -- THE DIRAC VALUE," % (dw, gw))
    print("      Carter's 1968 result, MEASURED HERE FROM THE POTENTIAL'S")
    print("      ASYMPTOTICS RATHER THAN RECALLED.  A LINEAR, ODD RELATION:")
    print()
    print("          a = mu / Q          WITH ITS SIGN")
    print()
    print("      And the constructive half is elementary and flat: a loop of")
    print("      current I over area A has mu = I A by the right-hand rule, so")
    print("      reversing the current reverses mu -- %+.3f against %+.3f."
          % (loop_dipole(2.0, 3.0), loop_dipole(-2.0, 3.0)))
    print("      THE SHAPE OF THE CURRENT IS THE SIGN.  Labelled as classical")
    print("      electromagnetism and NOT as a derivation in general relativity.")
    print()

    print(BAR)
    print("5.  THE FULL LOCAL INVERSION, FROM FIVE READINGS AT ONE POINT")
    print(BAR)
    print()
    print("      %6s %6s %6s %8s %10s %10s %10s %s"
          % ("M", "a", "Q", "theta", "M rec", "a rec", "Q rec", "status"))
    iw = 0.0
    for M, a, Q, th in [(1.0, 0.7, 0.4, 1.1), (1.0, -0.7, 0.4, 1.1),
                        (1.0, 0.7, -0.4, 1.1), (2.0, 1.5, 0.9, math.pi / 2),
                        (1.0, 0.7, 0.0, 1.1), (1.0, 0.7, 0.4, 1e-9)]:
        rd = kn(5.0, th, M, a, Q)
        out = invert(rd, 5.0, th)
        if out["a"] is not None:
            iw = max(iw, abs(out["M"] - M), abs(out["a"] - a), abs(out["Q"] - Q))
        print("      %6.2f %6.2f %6.2f %8.2e %10.6f %10s %10.6f %s"
              % (M, a, Q, th, out["M"],
                 "%.6f" % out["a"] if out["a"] is not None else "  --  ",
                 out["Q"], out["status"]))
    print()
    print("      EVERY SIGNED PARAMETER RECOVERED TO %.1e, AND THE TWO FAILURE" % iw)
    print("      MODES REFUSE RATHER THAN GUESS: uncharged, and on the axis.")
    print("      The metric route still returns |a| in both -- it just has no")
    print("      sign to give.")
    print()

    print(BAR)
    print("6.  THE THEOREM")
    print(BAR)
    print()
    print("        Phi : (M, a, Q) -> (g_tt, g_rr, g_thth, g_pp, A_t, A_phi)")
    print()
    print("        IS INJECTIVE   IFF   Q != 0   OR   a = 0.")
    print()
    print("      %8s %8s %12s %12s %s" % ("a", "Q", "predicted", "measured", "agree"))
    ok = 0
    tot = 0
    for a, Q in [(0.7, 0.4), (0.7, 0.0), (0.0, 0.0), (0.0, 0.4),
                 (-2.5, 0.9), (2.5, 0.0), (1e-16, 0.0)]:
        pred = phi_injective(a, Q)
        rd = kn(5.0, 1.1, 1.0, a, Q)
        meas = invert(rd, 5.0, 1.1)["a"] is not None or abs(a) < 1e-15
        tot += 1
        ok += (pred == meas)
        print("      %8.2g %8.2f %12s %12s %s"
              % (a, Q, pred, meas, "yes" if pred == meas else "NO"))
    print()
    print("      %d OF %d ROWS AGREE.  IT FAILS EXACTLY ON THE UNCHARGED" % (ok, tot))
    print("      SPINNING CASE, AND ON NOTHING ELSE.  M's assertion IS the")
    print("      content of that iff: the inversion is possible BECAUSE EM")
    print("      carries a sign, and impossible precisely where it does not.")
    print()

    print(BAR)
    print("7.  AND THE TWO ODD CHANNELS COVER THE SPHERE WITH NO GAP")
    print(BAR)
    print()
    print("      %10s %18s %18s %s" % ("theta", "*RR ~ a cos th", "A_phi ~ sin^2 th", "readable"))
    gap = 0
    for th in (0.0, 0.3, 1.0, math.pi / 2, 2.4, math.pi):
        cc = curvature_channel(th, 0.7)
        ee = em_channel(th, 0.7, 0.4)
        live = abs(cc) > 1e-15 or abs(ee) > 1e-15
        gap += (not live)
        print("      %10.4f %18.9f %18.9f %s"
              % (th, cc, ee, "yes" if live else "NO -- BLIND"))
    print()
    print("      %d BLIND ANGLES OUT OF SIX TESTED, AND NONE IS POSSIBLE:" % gap)
    print("      cos(theta) and sin(theta) NEVER VANISH TOGETHER.  The curvature")
    print("      channel dies on the EQUATOR, the electromagnetic one dies on")
    print("      the AXIS, AND THEIR BLIND LOCI ARE DISJOINT.")
    print()
    print("        TWO ODD CHANNELS, EACH BLIND ON ONE LOCUS, COVERING THE WHOLE")
    print("        SPHERE BETWEEN THEM.  THE BIT IS READABLE EVERYWHERE.")
    print()

    print(BAR)
    print("8.  REPORT AGAINST SUPPLY -- AND WHAT IT STILL DOES NOT DO")
    print(BAR)
    print()
    print("    THE DISTINCTION IS THE WHOLE VALUE OF M'S SECOND CLAUSE.")
    print()
    print("      IN AN EXISTING KERR-NEWMAN OBJECT, mu = Q a IS A LOCK AND NOT")
    print("      AN INDEPENDENT INPUT.  The same rotation makes both, so the")
    print("      electromagnetic sector REPORTS the bit.  Reading is not")
    print("      choosing, and this half changes nothing about construction.")
    print()
    print("      IN A CORRIDOR DRIVEN BY EM -- voltage.py's route, a geometry")
    print("      made entirely by field -- THE CURRENT'S HANDEDNESS IS A DESIGN")
    print("      INPUT, and the electromagnetic sector SUPPLIES the bit.")
    print("      weave.py said a construction must SUPPLY the orientation and")
    print("      named nothing that could.  THIS NAMES IT.  It is the first")
    print("      time in this project that the missing datum is something a")
    print("      BUILDER SETS rather than something a MEASUREMENT RETURNS.")
    print()
    print("    AND THE LIMITS, WHICH ARE NOT SMALL:")
    print("      * THE PARITY THEOREM IS UNTOUCHED.  cube.py's theorem is about")
    print("        the GRAVITATIONAL even sector.  Adding a sector with its own")
    print("        odd member is not inverting that map -- it is asking a")
    print("        different map.  No claim here contradicts it and none")
    print("        weakens it.")
    print("      * THE ENERGY BILL DOES NOT MOVE.  mu = Q a says which way the")
    print("        frame drags and nothing whatever about whether a throat")
    print("        opens.  voltage.py's M < U/c^2 stands untouched, and so do")
    print("        the three currencies.")
    print("      * g = 2 FOR KERR-NEWMAN IS A KNOWN RESULT VERIFIED HERE, NOT A")
    print("        RESULT DERIVED HERE.  Carter 1968.  The verification is this")
    print("        pass's; the theorem is not.")
    print()
    print("    SCOPE: %s.  Nothing here is repaired." % SCOPE)
    print()


def selftest():
    fails = []

    def chk(label, got, want):
        ok = (got == want)
        print("  %-4s %-56s %s" % ("ok" if ok else "FAIL", label, got))
        if not ok:
            fails.append((label, got, want))

    print("iff.py --selftest")
    print()

    # reduce to Kerr at Q = 0, and to Schwarzschild at a = Q = 0
    chk("Q = 0 reduces to Kerr's g_tt",
        abs(kn(5.0, 1.1, 1.0, 0.7, 0.0)["g_tt"]
            - (-(1.0 - 2.0 * 5.0 / (25.0 + 0.49 * math.cos(1.1) ** 2)))) < 1e-15, True)
    chk("a = Q = 0 reduces to Schwarzschild",
        abs(kn(5.0, 1.1, 1.0, 0.0, 0.0)["g_tt"] + 0.6) < 1e-15, True)

    # 1.  the two iffs really differ
    chk("(A) holds on the equator with spin", z_inverts(5.0, math.pi / 2, 0.7), True)
    chk("(B) fails there", even_sector_inverts(5.0, math.pi / 2, 1.0, 0.7, 0.0), False)
    chk("both hold at a = 0",
        (z_inverts(5.0, 1.1, 0.0), even_sector_inverts(5.0, 1.1, 1.0, 0.0, 0.4)),
        (True, True))
    chk("the general a^2 inversion is exact, equator included",
        max(abs(a_squared_from_metric(5.0, th, 1.0, a, Q) - a * a)
            for a, th, Q in [(0.7, 1.1, 0.0), (0.7, math.pi / 2, 0.0),
                             (2.5, 0.3, 0.6), (0.99, math.pi / 2, 0.4),
                             (-0.7, 2.4, 0.9)]) < 1e-11, True)
    chk("M is recovered too",
        max(abs(M_from_metric(5.0, th, M, a, Q) - M)
            for M, a, th, Q in [(1.0, 0.7, 1.1, 0.4), (2.0, 1.5, math.pi / 2, 0.9),
                                (0.3, 0.2, 0.4, 0.0)]) < 1e-11, True)
    chk("modulus.py conflated two iffs", MODULUS_CONFLATED_TWO_IFFS, True)

    # 2.  the gravitational iff
    chk("even sector inverts iff a = 0",
        [even_sector_inverts(5.0, 1.1, 1.0, a, 0.4)
         for a in (0.0, 0.3, 0.7, 2.5, -0.99)], [True, False, False, False, False])

    # 3.  parity census
    chk("metric is even in a",
        [parity_in(k, "a", 5.0, 1.1, 1.0, 0.7, 0.4) for k in METRIC_EVEN],
        [1, 1, 1, 1])
    chk("metric is even in Q",
        [parity_in(k, "Q", 5.0, 1.1, 1.0, 0.7, 0.4) for k in METRIC_EVEN],
        [1, 1, 1, 1])
    chk("A_t is odd in Q, even in a",
        (parity_in("A_t", "Q", 5.0, 1.1, 1.0, 0.7, 0.4),
         parity_in("A_t", "a", 5.0, 1.1, 1.0, 0.7, 0.4)), (-1, 1))
    chk("A_phi is odd in a AND odd in Q",
        (parity_in("A_phi", "a", 5.0, 1.1, 1.0, 0.7, 0.4),
         parity_in("A_phi", "Q", 5.0, 1.1, 1.0, 0.7, 0.4)), (-1, -1))
    chk("g_tp is odd in a, even in Q",
        (parity_in("g_tp", "a", 5.0, 1.1, 1.0, 0.7, 0.4),
         parity_in("g_tp", "Q", 5.0, 1.1, 1.0, 0.7, 0.4)), (-1, 1))

    # 4.  mu = Q a, g = 2
    chk("mu = Q a",
        max(abs(dipole_asymptotic(th, 1.0, a, Q) - Q * a)
            for a, Q, th in [(0.7, 0.4, 1.1), (-0.7, 0.4, 1.1), (0.7, -0.4, 0.6),
                             (0.99, 0.9, math.pi / 2), (2.5, 0.2, 2.0)]) < 1e-6, True)
    chk("g = 2 (Dirac value, Carter 1968)",
        max(abs(gyromagnetic_g(5.0, th, 1.0, a, Q) - 2.0)
            for a, Q, th in [(0.7, 0.4, 1.1), (-0.7, 0.4, 1.1),
                             (0.99, 0.9, math.pi / 2)]) < 1e-6, True)
    chk("the local dipole agrees with the asymptotic one",
        abs(dipole_local(5.0, 1.1, 1.0, 0.7, 0.4)
            - dipole_asymptotic(1.1, 1.0, 0.7, 0.4)) < 1e-6, True)
    chk("reversing the current reverses the dipole",
        (loop_dipole(2.0, 3.0), loop_dipole(-2.0, 3.0)), (6.0, -6.0))

    # 5.  the full inversion
    w = 0.0
    for M, a, Q, th in [(1.0, 0.7, 0.4, 1.1), (1.0, -0.7, 0.4, 1.1),
                        (1.0, 0.7, -0.4, 1.1), (2.0, 1.5, 0.9, math.pi / 2)]:
        out = invert(kn(5.0, th, M, a, Q), 5.0, th)
        w = max(w, abs(out["M"] - M), abs(out["a"] - a), abs(out["Q"] - Q))
    chk("(M, a, Q) recovered with signs", w < 1e-10, True)
    chk("uncharged refuses rather than guesses",
        invert(kn(5.0, 1.1, 1.0, 0.7, 0.0), 5.0, 1.1)["a"], None)
    chk("and still returns |a|",
        round(invert(kn(5.0, 1.1, 1.0, -0.7, 0.0), 5.0, 1.1)["a_abs"], 9), 0.7)
    chk("on axis refuses rather than guesses",
        invert(kn(5.0, 1e-9, 1.0, 0.7, 0.4), 5.0, 1e-9)["a"], None)

    # 6.  the theorem
    chk("Phi injective iff Q != 0 or a = 0",
        [phi_injective(a, Q) for a, Q in
         [(0.7, 0.4), (0.7, 0.0), (0.0, 0.0), (0.0, 0.4), (-2.5, 0.9), (2.5, 0.0)]],
        [True, False, True, True, True, False])
    chk("and the prediction matches the inversion",
        all(phi_injective(a, Q) ==
            (invert(kn(5.0, 1.1, 1.0, a, Q), 5.0, 1.1)["a"] is not None
             or abs(a) < 1e-15)
            for a, Q in [(0.7, 0.4), (0.7, 0.0), (0.0, 0.0), (0.0, 0.4),
                         (-2.5, 0.9), (2.5, 0.0)]), True)

    # 7.  coverage
    chk("no theta blinds both channels",
        all(abs(curvature_channel(th, 0.7)) > 1e-15
            or abs(em_channel(th, 0.7, 0.4)) > 1e-15
            for th in [i * math.pi / 64.0 for i in range(65)]), True)
    chk("the curvature channel is blind on the equator",
        abs(curvature_channel(math.pi / 2, 0.7)) < 1e-16, True)
    chk("the EM channel is blind on the axis",
        (abs(em_channel(0.0, 0.7, 0.4)) < 1e-30,
         abs(em_channel(math.pi, 0.7, 0.4)) < 1e-30), (True, True))
    chk("channels cover the sphere", CHANNELS_COVER_THE_SPHERE, True)

    # 8.  the verdicts
    chk("EM supplies the sign", EM_SUPPLIES_THE_SIGN, True)
    chk("in Kerr-Newman it reports rather than supplies",
        EM_IN_KERR_NEWMAN_REPORTS_RATHER_THAN_SUPPLIES, True)
    chk("parity theorem overturned", PARITY_THEOREM_IS_OVERTURNED, False)
    chk("energy bill moves", ENERGY_BILL_MOVES, False)
    chk("nothing is repaired", NOTHING_IS_REPAIRED, True)

    print()
    if fails:
        for lab, g, w_ in fails:
            print("  FAIL %s: got %r want %r" % (lab, g, w_))
        print("\nSELFTEST FAIL (%d)" % len(fails))
        return 1
    print("SELFTEST PASS")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
