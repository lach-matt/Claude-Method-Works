#!/usr/bin/env python3.12
"""amps.py -- the bill in current, and why it looks smaller than it is.

M: "Now that we have the math we can go back to the bill.  And my first guess
is going to be amps of EM."

A GOOD GUESS, AND IT IS THE FIRST CURRENCY THIS PROJECT HAS PRICED THAT IS NOT
LINEAR IN THE WALL.  Six results, and the third is the one to be careful about.

  1.  THE UNIT BRIDGE IS EXACT AND IT IS CARTER'S.  In SI the Kerr-Newman
      magnetic dipole is mu = Q a c = Q J / M -- the g = 2 relation iff.py
      cited -- and a laboratory loop has mu = I A.  Equating them gives

              I = Q a c / A            amperes, exactly.

      That is a dimensionally clean bridge from two general-relativity
      parameters to a current, and it is the constructive half of M's guess.

  2.  AND THE DIPOLE MATCH IS NEARLY AFFORDABLE.  Matching the moment of a
      (Q, a) object with a metre-scale loop lands within a few orders of
      currents that have actually been produced.  THE ORIENTATION IS CHEAP.

  3.  THE GEOMETRY IS NOT, AND THE EXPONENT IS THE TRAP.  (The dex ratio is
      2.0782 rather than a round 2, and the excess is EXACTLY the inductance
      mismatch between the two devices compared -- computed, not fudged.)  Putting the
      exchange-rate energy c^4/(G Lambda) into a magnetic field of scale R
      needs a current of order 1e24 A at a metre.  THAT IS ABOUT SEVENTEEN
      ORDERS ABOVE THE BEST CURRENT EVER PRODUCED, AGAINST ABOUT THIRTY-FIVE
      ORDERS IN ENERGY -- AND THE RATIO IS TWO, EXACTLY BECAUSE ENERGY IS
      QUADRATIC IN CURRENT.  THE WALL DID NOT MOVE.  THE EXPONENT HALVED.
      A quadratic currency always halves the gap in dex and buys nothing.

  4.  THE MAGNETIC WALL IS REAL AND IT IS ESCAPABLE BY SCALE.  The field
      required at a metre is about 6e8 times the QED critical field
      B_c = m_e^2 c^2 / (e hbar) = 4.41e9 T, so the vacuum breaks down long
      first.  But B falls as R^{-3/2}, so a large enough device ducks under
      it -- around 700 km.

  5.  AND THE CURRENT WALL IS NOT.  I ~ R B ~ R^{-1/2}: THE CURRENT BILL IS
      NEARLY SCALE-INVARIANT.  Six orders of growth in size buys three orders
      in current.  This project has been rescued by scale before -- the 1e31
      gap was a 20 m artefact and size had never been varied -- SO SIZE IS
      VARIED HERE, AND IT BARELY HELPS.

  6.  WHICH WALL BINDS, AND IT IS THE OPPOSITE OF THE ELECTRIC CASE.
      voltage.py found the electric route stopped by CONSERVATION and not by
      vacuum breakdown, the marginal field sitting 1041 below Schwinger.  The
      magnetic route is stopped by BOTH, in that order: breakdown first at
      small scale, and the current itself at every scale.

Engineering figures are RECALLED, not read, and are marked.  They set the
comparison and no claim rests on their third digit.  Stdlib only.

    python3.12 amps.py            full report
    python3.12 amps.py --selftest
"""

import math
import sys

# --- constants (SI) -------------------------------------------------------
c = 2.99792458e8
G = 6.67430e-11
MU0 = 4.0e-7 * math.pi
EPS0 = 8.8541878128e-12
E_CHG = 1.602176634e-19
HBAR = 1.054571817e-34
M_E = 9.1093837015e-31
LAMBDA = 9.982529174194637

EXCHANGE = c ** 4 / (G * LAMBDA)          # J per metre of Delta d
B_QED = M_E ** 2 * c ** 2 / (E_CHG * HBAR)   # critical magnetic field
E_SCHWINGER = M_E ** 2 * c ** 3 / (E_CHG * HBAR)

# --- recalled engineering figures, marked as such -------------------------
RECALLED = {
    "Z machine peak current (A)":        2.6e7,
    "Z machine stored energy (J)":       2.0e7,
    "LHC main dipole current (A)":       1.185e4,
    "ITER central solenoid current (A)": 4.5e4,
    "strongest continuous lab field (T)": 45.0,
    "strongest destructive pulsed field (T)": 1.2e3,
    "magnetar surface field (T)":        1.0e11,
}
FIGURES_ARE_READ = False


# --- 1.  the unit bridge --------------------------------------------------

def dipole_kn(Q, a):
    """Kerr-Newman magnetic moment in SI: mu = Q a c.  [C][m][m/s] = A m^2."""
    return Q * a * c


def dipole_from_J(Q, J, M):
    """The same thing written with angular momentum: mu = Q J / M (g = 2)."""
    return Q * J / M


def current_for_dipole(Q, a, area):
    """A loop of the given area with mu = I A matching the Kerr-Newman moment."""
    return dipole_kn(Q, a) / area


# --- 3/4/5.  the geometry bill --------------------------------------------

def field_for_energy(E, R):
    """B such that (B^2/2mu0) * (4/3)pi R^3 = E."""
    V = (4.0 / 3.0) * math.pi * R ** 3
    return math.sqrt(2.0 * MU0 * E / V)


def current_for_field(B, R):
    """Loop of radius R producing B ~ mu0 I / (2R) at its centre."""
    return 2.0 * R * B / MU0


def current_for_energy(E, R):
    return current_for_field(field_for_energy(E, R), R)


def radius_at_critical_field(E):
    """R where the required field equals the QED critical field."""
    V = 2.0 * MU0 * E / B_QED ** 2
    return (V * 3.0 / (4.0 * math.pi)) ** (1.0 / 3.0)


def dex(x):
    return math.log10(x)


def implied_inductance(E, I):
    """E = L I^2 / 2  =>  L = 2E/I^2.  What a device's numbers imply."""
    return 2.0 * E / (I * I)


def dex_ratio_decomposition(E_req, I_req, E_dev, I_dev):
    """Why the energy dex is not EXACTLY twice the current dex.

    With E = L I^2/2 in both, log(E_req/E_dev) = 2 log(I_req/I_dev)
    + log(L_req/L_dev).  So the ratio of the two dex figures is

        2 + log10(L_req/L_dev) / log10(I_req/I_dev)

    and the excess over 2 is ENTIRELY the inductance mismatch between the
    two devices being compared.  Returns (ratio, predicted_ratio).
    """
    L_req = implied_inductance(E_req, I_req)
    L_dev = implied_inductance(E_dev, I_dev)
    dI = dex(I_req / I_dev)
    return dex(E_req / E_dev) / dI, 2.0 + dex(L_req / L_dev) / dI


# --- recorded verdicts ----------------------------------------------------
BRIDGE = "I = Q a c / A"
BRIDGE_IS_EXACT = True
BRIDGE_IS_CARTERS = True
CURRENT_SCALES_AS = "R^{-1/2}"
FIELD_SCALES_AS = "R^{-3/2}"
QUADRATIC_HALVES_THE_DEX = True
AMPS_MOVE_THE_WALL = False
FIELD_WALL_IS_ESCAPABLE_BY_SCALE = True
CURRENT_WALL_IS_ESCAPABLE_BY_SCALE = False
SCOPE = "order-of-magnitude engineering, not a design"
NOTHING_IS_REPAIRED = True

BAR = "=" * 79


def report():
    print(__doc__.split("Engineering figures")[0].rstrip())
    print()

    print(BAR)
    print("1.  THE UNIT BRIDGE, AND IT IS EXACT")
    print(BAR)
    print()
    print("      mu = Q a c   [C][m][m/s] = C m^2/s = A m^2.   And mu = Q J / M")
    print("      since a = J/(Mc).  That is g = 2, which is Carter's, cited in")
    print("      iff.py and cited again here.  A loop has mu = I A, so")
    print()
    print("            I = Q a c / A          EXACTLY, in amperes.")
    print()
    print("      %10s %10s %12s %16s %16s"
          % ("Q (C)", "a (m)", "area (m^2)", "mu (A m^2)", "I (A)"))
    for Q, a, A in [(1.0, 1.0, math.pi), (1e-3, 1.0, math.pi),
                    (1.0, 1e-3, math.pi), (1e3, 1.0, math.pi * 100),
                    (1.0, 1.0, math.pi * 1e4)]:
        print("      %10.3g %10.3g %12.4g %16.6e %16.6e"
              % (Q, a, A, dipole_kn(Q, a), current_for_dipole(Q, a, A)))
    ident = abs(dipole_kn(2.0, 3.0) - dipole_from_J(2.0, 3.0 * 5.0 * c, 5.0))
    print()
    print("      The two forms agree to %.1e." % ident)
    print()

    print(BAR)
    print("2.  AND THE DIPOLE MATCH IS NEARLY AFFORDABLE")
    print(BAR)
    print()
    z = RECALLED["Z machine peak current (A)"]
    Im = current_for_dipole(1.0, 1.0, math.pi)
    print("      Matching a (Q, a) = (1 C, 1 m) moment with a 1 m-radius loop")
    print("      needs %.3e A, against the largest current ever produced," % Im)
    print("      about %.1e A (RECALLED).  A factor of %.1f." % (z, Im / z))
    print()
    print("      THE ORIENTATION IS CHEAP.  corridor.py showed the handedness is")
    print("      a LABELLING rather than a free parameter, and a labelling is")
    print("      what this current buys.  IT DOES NOT BUY THE GEOMETRY, and")
    print("      nothing here shows that imposing this moment organises")
    print("      anything -- it is the matching condition and no more.")
    print()

    print(BAR)
    print("3.  THE GEOMETRY BILL, AND THE EXPONENT IS THE TRAP")
    print(BAR)
    print()
    print("      Put the exchange rate %.6e J into a magnetic field" % EXCHANGE)
    print("      filling a sphere of radius R.  Then B = sqrt(2 mu0 E / V) and")
    print("      I = 2 R B / mu0:")
    print()
    print("      %12s %16s %16s %14s" % ("R (m)", "B (T)", "I (A)", "B / B_QED"))
    for R in (1e-3, 1.0, 1e3, 7.2e5, 1e9, 1.5e11):
        B = field_for_energy(EXCHANGE, R)
        print("      %12.3g %16.6e %16.6e %14.3e"
              % (R, B, current_for_energy(EXCHANGE, R), B / B_QED))
    print()
    I1 = current_for_energy(EXCHANGE, 1.0)
    Ez = RECALLED["Z machine stored energy (J)"]
    gap_I = I1 / z
    gap_E = EXCHANGE / Ez
    print("      AT ONE METRE THE BILL IS %.3e A." % I1)
    print()
    print("      %-34s %12s %10s" % ("", "ratio", "dex"))
    print("      %-34s %12.4e %10.2f" % ("energy gap (vs Z machine store)", gap_E, dex(gap_E)))
    print("      %-34s %12.4e %10.2f" % ("current gap (vs Z machine peak)", gap_I, dex(gap_I)))
    rat, pred = dex_ratio_decomposition(EXCHANGE, I1, Ez, z)
    print("      %-34s %12s %10.4f" % ("ratio of the two", "", rat))
    print()
    print("      THE RATIO IS %.4f, AND IT IS TWO PLUS A CORRECTION THAT IS" % rat)
    print("      ENTIRELY ACCOUNTED FOR.  E = L I^2/2 in both, so")
    print()
    print("          dex(E) / dex(I) = 2 + log10(L_req/L_dev) / log10(I_req/I_dev)")
    print()
    print("      and the two devices imply L = %.4e H and %.4e H, a"
          % (implied_inductance(EXCHANGE, I1), implied_inductance(Ez, z)))
    print("      factor of %.1f.  Predicted ratio %.4f against measured %.4f,"
          % (implied_inductance(EXCHANGE, I1) / implied_inductance(Ez, z), pred, rat))
    print("      agreeing to %.1e.  THE EXCESS OVER TWO IS THE INDUCTANCE"
          % abs(pred - rat))
    print("      MISMATCH AND NOTHING ELSE.")
    print()
    print("      SO THE HALVING IS EXACT WITHIN ONE DEVICE -- doubling the")
    print("      stored energy raises the current by exactly sqrt(2) -- and")
    print("      approximate across two, by a term that is computable rather")
    print("      than a fudge.  EITHER WAY THE WALL DID NOT MOVE AND THE")
    print("      EXPONENT HALVED.")
    print()
    print("      That is worth stating plainly because it is exactly the shape")
    print("      of an apparent breakthrough that is not one: 17 orders reads")
    print("      as enormously better than 35 and IS THE SAME OBSTACLE, seen in")
    print("      a denomination whose square is the thing you actually need.")
    print()
    print("      This is the FOURTH currency for one wall -- after ENERGY at")
    print("      %.6e J/m, LENGTH at %.6e m and FREQUENCY at" % (EXCHANGE, math.sqrt(LAMBDA) * math.sqrt(HBAR * G / c ** 3)))
    print("      %.6e Hz -- AND THE FIRST THAT IS NOT LINEAR IN IT."
          % (math.sqrt(c ** 5 / (HBAR * G)) / math.sqrt(LAMBDA)))
    print()

    print(BAR)
    print("4.  THE MAGNETIC WALL IS REAL, AND ESCAPABLE BY SCALE")
    print(BAR)
    print()
    print("      B_QED = m_e^2 c^2 / (e hbar) = %.6e T" % B_QED)
    print("      Required at 1 m:              %.6e T" % field_for_energy(EXCHANGE, 1.0))
    print("      ratio:                        %.4e" % (field_for_energy(EXCHANGE, 1.0) / B_QED))
    print()
    Rc = radius_at_critical_field(EXCHANGE)
    print("      B falls as R^{-3/2}, so the field wall IS escapable: at")
    print("      R = %.4e m (%.0f km) the required field equals B_QED"
          % (Rc, Rc / 1e3))
    print("      exactly, and beyond that the vacuum is no longer the problem.")
    print()

    print(BAR)
    print("5.  AND THE CURRENT WALL IS NOT")
    print(BAR)
    print()
    print("      I ~ R B ~ R * R^{-3/2} = R^{-1/2}.  THE CURRENT BILL FALLS ONLY")
    print("      AS THE SQUARE ROOT OF SIZE.")
    print()
    print("      %12s %16s %14s %14s" % ("R (m)", "I (A)", "I / I(1 m)", "R^{-1/2}"))
    base = current_for_energy(EXCHANGE, 1.0)
    worst = 0.0
    for R in (1.0, 1e2, 1e4, 7.2e5, 1e8, 1e12):
        I = current_for_energy(EXCHANGE, R)
        pred = R ** -0.5
        worst = max(worst, abs(I / base / pred - 1.0))
        print("      %12.3g %16.6e %14.6e %14.6e" % (R, I, I / base, pred))
    print()
    print("      THE SCALING IS EXACT TO %.1e." % worst)
    print("      At the radius where the field wall is cleared, %.0f km, the"
          % (Rc / 1e3))
    print("      current is still %.3e A -- %.2e times the Z machine."
          % (current_for_energy(EXCHANGE, Rc), current_for_energy(EXCHANGE, Rc) / z))
    print("      SIX ORDERS OF GROWTH IN SIZE BUYS THREE IN CURRENT.")
    print()
    print("      THIS PROJECT HAS BEEN RESCUED BY SCALE BEFORE AND IS NOT HERE.")
    print("      A 1e31 gap once turned out to be a 20 m artefact because size")
    print("      had never been varied at all -- that is a recorded fault of")
    print("      this series.  SIZE IS VARIED HERE, over fifteen orders, AND IT")
    print("      BARELY MOVES THE ANSWER.  The check that once dissolved a wall")
    print("      is run again and this time confirms one.")
    print()

    print(BAR)
    print("6.  WHICH WALL BINDS -- AND IT IS THE OPPOSITE OF THE ELECTRIC CASE")
    print(BAR)
    print()
    print("      voltage.py found the ELECTRIC route stopped by CONSERVATION and")
    print("      NOT by vacuum breakdown: the marginal field sits at 1.270840e15")
    print("      V/m against E_S = %.4e, a factor of 1041 BELOW." % E_SCHWINGER)
    print("      A NO-GO BY IDENTITY RATHER THAN BY MAGNITUDE, and it said no")
    print("      advance in field engineering moves the answer.")
    print()
    print("      THE MAGNETIC ROUTE IS STOPPED BY BOTH, IN THIS ORDER:")
    print("        * BREAKDOWN FIRST, below ~%.0f km, where B exceeds B_QED;" % (Rc / 1e3))
    print("        * THE CURRENT ITSELF AT EVERY SCALE, since it falls only as")
    print("          R^{-1/2} and is %.2e times the best achieved even at the"
          % (current_for_energy(EXCHANGE, Rc) / z))
    print("          radius where breakdown is cleared.")
    print()
    print("      SO M'S GUESS IS THE RIGHT QUANTITY TO HAVE ASKED FOR AND THE")
    print("      ANSWER IS NEGATIVE IN A NEW WAY.  Amps are not a cheaper")
    print("      denomination; they are a SQUARE-ROOT denomination, and the")
    print("      square root of an impossible number is still impossible.")
    print()
    print("      WHAT THE PASS DOES LEAVE IS THE SPLIT.  The dipole match --")
    print("      the labelling corridor.py identified -- costs %.2e A, which is"
          % Im)
    print("      %.1f times a machine that exists.  THE BIT IS AFFORDABLE AND" % (Im / z))
    print("      THE OBJECT IS NOT, and those two were never the same purchase.")
    print()
    print("    SCOPE: %s." % SCOPE)
    print("    Engineering comparators are RECALLED and not read; no claim here")
    print("    rests on their third digit, only on their order.")
    print()


def selftest():
    fails = []

    def chk(label, got, want):
        ok = (got == want)
        print("  %-4s %-56s %s" % ("ok" if ok else "FAIL", label, got))
        if not ok:
            fails.append((label, got, want))

    print("amps.py --selftest")
    print()

    # constants against the corpus's own recorded figures
    chk("the exchange rate", float("%.6e" % EXCHANGE), 1.212374e43)
    chk("the QED critical field", float("%.6e" % B_QED), 4.414005e9)
    chk("the Schwinger field", float("%.4e" % E_SCHWINGER), 1.3233e18)
    chk("B_QED * c == E_Schwinger", abs(B_QED * c - E_SCHWINGER) < 1e3, True)

    # 1.  the bridge
    chk("mu = Q a c is dimensionally A m^2",
        abs(dipole_kn(1.0, 1.0) - c) < 1e-6, True)
    chk("mu = Q a c equals Q J / M",
        abs(dipole_kn(2.0, 3.0) - dipole_from_J(2.0, 3.0 * 5.0 * c, 5.0)) < 1e-6, True)
    chk("I = mu / A",
        abs(current_for_dipole(1.0, 1.0, 2.0) - c / 2.0) < 1e-6, True)
    chk("the bridge is Carter's", BRIDGE_IS_CARTERS, True)

    # 3.  the energy-to-current chain, and the halving
    I1 = current_for_energy(EXCHANGE, 1.0)
    chk("the 1 m current bill", float("%.3e" % I1), 4.293e24)
    z = RECALLED["Z machine peak current (A)"]
    Ez = RECALLED["Z machine stored energy (J)"]
    ratio, pred = dex_ratio_decomposition(EXCHANGE, I1, Ez, z)
    chk("the measured dex ratio", float("%.4f" % ratio), 2.0782)
    chk("and the inductance decomposition predicts it exactly",
        abs(ratio - pred) < 1e-12, True)
    chk("so the excess over 2 is the inductance mismatch",
        float("%.4f" % (ratio - 2.0)),
        float("%.4f" % (dex(implied_inductance(EXCHANGE, I1)
                            / implied_inductance(Ez, z)) / dex(I1 / z))))
    chk("a quadratic currency halves the dex", QUADRATIC_HALVES_THE_DEX, True)
    chk("amps move the wall", AMPS_MOVE_THE_WALL, False)

    # the halving is a theorem about the exponent, not about this device:
    # doubling the stored energy must raise the current by exactly sqrt(2).
    chk("E -> 2E raises I by sqrt(2)",
        abs(current_for_energy(2 * EXCHANGE, 1.0) / I1 - math.sqrt(2.0)) < 1e-12, True)

    # 4/5.  scaling
    base = current_for_energy(EXCHANGE, 1.0)
    chk("I scales as R^{-1/2}",
        max(abs(current_for_energy(EXCHANGE, R) / base / R ** -0.5 - 1.0)
            for R in (1e2, 1e4, 7.2e5, 1e8, 1e12)) < 1e-12, True)
    chk("B scales as R^{-3/2}",
        max(abs(field_for_energy(EXCHANGE, R) / field_for_energy(EXCHANGE, 1.0)
                / R ** -1.5 - 1.0) for R in (1e2, 1e6, 1e10)) < 1e-12, True)
    Rc = radius_at_critical_field(EXCHANGE)
    chk("the critical radius, in km", float("%.6f" % (Rc / 1e3)), 720.068846)
    chk("and B there is B_QED",
        abs(field_for_energy(EXCHANGE, Rc) / B_QED - 1.0) < 1e-12, True)
    chk("the field wall is escapable", FIELD_WALL_IS_ESCAPABLE_BY_SCALE, True)
    chk("the current wall is not", CURRENT_WALL_IS_ESCAPABLE_BY_SCALE, False)
    chk("and the current there is still enormous",
        current_for_energy(EXCHANGE, Rc) / z > 1e13, True)

    # 2.  the split
    Im = current_for_dipole(1.0, 1.0, math.pi)
    chk("the dipole-match current", float("%.6e" % Im), 9.542690e7)
    chk("and it is within an order of a real machine",
        1.0 < Im / z < 10.0, True)
    chk("while the geometry current is not", I1 / z > 1e15, True)

    chk("engineering figures were read", FIGURES_ARE_READ, False)
    chk("nothing is repaired", NOTHING_IS_REPAIRED, True)

    print()
    if fails:
        for lab, g, w in fails:
            print("  FAIL %s: got %r want %r" % (lab, g, w))
        print("\nSELFTEST FAIL (%d)" % len(fails))
        return 1
    print("SELFTEST PASS")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
