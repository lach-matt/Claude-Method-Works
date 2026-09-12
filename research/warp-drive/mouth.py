#!/usr/bin/env python3.12
"""mouth.py -- fix the mouth at ten feet and see what it buys.

M: "let's assume the size of the mouth only needs to be 10 feet in diameter."

THE ASSUMPTION IS NOW DECIDABLE, BECAUSE closeout.py FIXED THE ASPECT RATIO
EXACTLY, AND IT DECIDES AGAINST -- but the way it fails is more interesting
than the failure, and there is one escape that this pass does NOT close.

  1.  A TEN-FOOT MOUTH FIXES THE SHORTCUT AT 7.6 METRES.  r = 2 Delta d/Lambda
      inverts to Delta d = Lambda r / 2, so a 1.524 m radius gives

              Delta d = 7.606689 m

      NOT four light years.  SEVEN AND A HALF METRES.  You cannot choose the
      mouth and the reach independently; Lambda ties them at 4.991265 and
      that ratio is scale-invariant.

  2.  AND IT STILL COSTS 172 EARTH MASSES.  The mass is 1.026e27 kg -- about
      half a Jupiter -- to move something seven metres.  The price did not
      come down with the mouth; ONLY THE PRODUCT CAME DOWN.

  3.  THE DENSITY IS THE REAL OBJECTION AT THIS SIZE.  Half a Jupiter inside
      a 1.5 m sphere is 6.9e25 kg/m^3, about THREE HUNDRED MILLION TIMES
      NUCLEAR DENSITY -- which is simply what a small black hole is, because
      that is exactly what 2GM/c^2 = 1.524 m describes.

  4.  SO THE QUESTION INVERTS.  What mouth does a USEFUL shortcut need?
      A kilometre needs a 400 m mouth.  Proxima needs one 1.7 LIGHT YEARS
      ACROSS.  And keeping the ten-foot mouth while reaching Proxima would
      need the mass packed 5.3e15 times inside its own gravitational radius.

  5.  AND HERE IS THE ONE ESCAPE, STATED HONESTLY AND NOT CLOSED.  The bound
      r >= 2G|M|/c^2 IS A THEOREM ONLY FOR POSITIVE MASS, where that radius is
      a HORIZON and a throat inside it is not reachable from outside.  For
      NEGATIVE mass there is no horizon and the bound is not a theorem.
      certify.py's contraction condition is m < 0.  SO THE ESCAPE FROM THE
      ASPECT RATIO IS EXACTLY THE NEGATIVE MASS THIS PROJECT HAS NEVER BEEN
      ABLE TO SOURCE -- the same wall, met from a new direction, and this pass
      does NOT resolve the sign bookkeeping between the exchange rate's
      positive M and certify.py's negative m.  THAT IS RECORDED AS OPEN.

    python3.12 mouth.py            full report
    python3.12 mouth.py --selftest
"""

import math
import sys

import ladder
import closeout

c = ladder.c
G = ladder.G
LAMBDA = ladder.LAMBDA
LY = ladder.LY
M_EARTH = ladder.M_EARTH
M_SUN = ladder.M_SUN
M_JUPITER = 1.89813e27          # RECALLED
RHO_NUCLEAR = 2.3e17            # kg/m^3, RECALLED
FOOT = 0.3048                   # exact by definition

MOUTH_DIAMETER_FT = 10.0
FIGURES_ARE_READ = False


def radius_from_feet(ft):
    return ft * FOOT / 2.0


def reach_from_radius(r):
    """Invert closeout's r = 2 Delta d / Lambda."""
    return LAMBDA * r / 2.0


def mass_from_radius(r):
    """M = r c^2/(2G).  Identical to Delta d c^2/(G Lambda) via the ratio."""
    return r * c * c / (2.0 * G)


def radius_for_reach(d):
    return closeout.throat_radius(d)


def density(r):
    M = mass_from_radius(r)
    return M / ((4.0 / 3.0) * math.pi * r ** 3)


def packing_factor(d, r_mouth):
    """How far inside its own gravitational radius the mass would have to sit."""
    return closeout.throat_radius(d) / r_mouth


BOUND_IS_A_THEOREM_FOR_POSITIVE_MASS = True
BOUND_IS_A_THEOREM_FOR_NEGATIVE_MASS = False
SIGN_BOOKKEEPING_RESOLVED = False
TEN_FEET_IS_VIABLE = False
SCOPE = "closeout.py's aspect ratio; the horizon bound holds for M > 0 only"
NOTHING_IS_REPAIRED = True

BAR = "=" * 79


def report():
    print(__doc__.split("    python3.12")[0].rstrip())
    print()
    r = radius_from_feet(MOUTH_DIAMETER_FT)
    d = reach_from_radius(r)
    M = mass_from_radius(r)

    print(BAR)
    print("1.  A TEN-FOOT MOUTH FIXES THE SHORTCUT AT SEVEN AND A HALF METRES")
    print(BAR)
    print()
    print("      mouth diameter    %.4f m  (%.0f ft)" % (2 * r, MOUTH_DIAMETER_FT))
    print("      mouth radius      %.6f m" % r)
    print("      Delta d = Lambda r / 2 = %.6f m" % d)
    print()
    print("      SEVEN AND A HALF METRES.  Not four light years, not a")
    print("      kilometre.  You cannot choose the mouth and the reach")
    print("      independently -- Lambda ties them at %.6f and closeout.py"
          % closeout.aspect_ratio())
    print("      measured that identical to 1e-15 across sixteen orders of")
    print("      scale.  FIXING THE MOUTH FIXES THE REACH.")
    print()

    print(BAR)
    print("2.  AND IT STILL COSTS 172 EARTH MASSES")
    print(BAR)
    print()
    print("      M = r c^2 / (2G) = %.6e kg" % M)
    print("        = %.2f Earth masses" % (M / M_EARTH))
    print("        = %.4f Jupiter masses" % (M / M_JUPITER))
    print("        = %.4e solar masses" % (M / M_SUN))
    print("      E = M c^2       = %.6e J" % (M * c * c))
    print()
    chk = ladder.mass_for_delta_d(d)
    print("      Cross-checked against the exchange rate: %.6e kg from" % chk)
    print("      22.59 Earth masses per metre, agreeing to %.1e."
          % abs(chk / M - 1.0))
    print()
    print("      HALF A JUPITER TO MOVE SOMETHING SEVEN METRES.  The price did")
    print("      not come down when the mouth did -- ONLY THE PRODUCT CAME")
    print("      DOWN.  The rate is the same 22.59 Earth masses per metre it")
    print("      always was, and a small mouth simply buys fewer metres.")
    print()

    print(BAR)
    print("3.  AND THE DENSITY SAYS WHAT THE OBJECT ACTUALLY IS")
    print(BAR)
    print()
    print("      density  = %.6e kg/m^3" % density(r))
    print("               = %.4e times nuclear density" % (density(r) / RHO_NUCLEAR))
    print()
    print("      That is not a surprise and it is not a separate objection: it")
    print("      IS what 2GM/c^2 = %.4f m describes.  A half-Jupiter mass whose" % r)
    print("      gravitational radius is a metre and a half IS A SMALL BLACK")
    print("      HOLE, and the ten-foot mouth is its horizon.")
    print()

    print(BAR)
    print("4.  SO THE QUESTION INVERTS -- WHAT MOUTH DOES A USEFUL REACH NEED?")
    print(BAR)
    print()
    print("      %-26s %18s %20s %16s"
          % ("reach", "mouth diameter (m)", "mass (kg)", "Earth masses"))
    for name, dd in [("7.6 m (ten-foot mouth)", d), ("one kilometre", 1e3),
                     ("Earth to Moon", 3.844e8), ("one light year", LY),
                     ("Proxima, 4.2 ly", 4.2465 * LY)]:
        rr = radius_for_reach(dd)
        mm = ladder.mass_for_delta_d(dd)
        print("      %-26s %18.6e %20.6e %16.4e"
              % (name, 2 * rr, mm, mm / M_EARTH))
    print()
    print("      A KILOMETRE NEEDS A %.1f METRE MOUTH.  PROXIMA NEEDS ONE"
          % (2 * radius_for_reach(1e3)))
    print("      %.3f LIGHT YEARS ACROSS." % (2 * radius_for_reach(4.2465 * LY) / LY))
    print()
    pf = packing_factor(4.2465 * LY, r)
    print("      And keeping the ten-foot mouth while reaching Proxima would")
    print("      need that mass packed %.4e TIMES INSIDE ITS OWN" % pf)
    print("      GRAVITATIONAL RADIUS.  Not compressed -- INSIDE ITS HORIZON,")
    print("      which is where a throat stops being reachable from outside.")
    print()

    print(BAR)
    print("5.  THE ONE ESCAPE, AND THIS PASS DOES NOT CLOSE IT")
    print(BAR)
    print()
    print("    THE BOUND r >= 2G|M|/c^2 IS A THEOREM ONLY FOR POSITIVE MASS.")
    print("    There, that radius is a HORIZON, and a throat inside a horizon")
    print("    is not reachable from outside -- so the mouth cannot be smaller")
    print("    than it and the aspect ratio binds.")
    print()
    print("    FOR NEGATIVE MASS THERE IS NO HORIZON AND THE BOUND IS NOT A")
    print("    THEOREM.  And certify.py's contraction condition is EXACTLY")
    print("    m < 0: C < 1 if and only if the Misner-Sharp mass is negative.")
    print()
    print("        SO THE ESCAPE FROM THE ASPECT RATIO IS THE NEGATIVE MASS")
    print("        THIS PROJECT HAS NEVER BEEN ABLE TO SOURCE.")
    print()
    print("    The same wall, met from a new direction, and that is worth more")
    print("    than another restatement of it: it says the aspect ratio and the")
    print("    exotic-matter requirement ARE THE SAME CONSTRAINT, not two.")
    print()
    print("    AND ONE THING IS RECORDED OPEN RATHER THAN PAPERED OVER.  This")
    print("    tree prices the transition with a POSITIVE M -- 22.59 Earth")
    print("    masses per metre, a cost -- while certify.py's contraction")
    print("    theorem requires a NEGATIVE m.  Whether those are the same M")
    print("    with a sign convention between them, or two different masses,")
    print("    IS NOT RESOLVED BY THIS PASS and it is not assumed either way.")
    print("    Section 4's numbers are magnitudes and survive the question;")
    print("    section 5's escape depends entirely on its answer.")
    print()
    print("    SO: TEN FEET IS NOT VIABLE, AND IT FAILS FOR A REASON THAT WAS")
    print("    NOT AVAILABLE BEFORE closeout.py -- not cost, WHICH SCALES DOWN")
    print("    HONESTLY WITH THE MOUTH, BUT REACH, WHICH SCALES DOWN WITH IT")
    print("    TOO.  A buildable mouth buys a useless corridor, and the two")
    print("    cannot be separated at positive mass.")
    print()
    print("    SCOPE: %s." % SCOPE)
    print("    Jupiter and nuclear-density figures are RECALLED, not read.")
    print("    Nothing here is repaired.")
    print()


def selftest():
    fails = []

    def chk(label, got, want):
        ok = (got == want)
        print("  %-4s %-56s %s" % ("ok" if ok else "FAIL", label, got))
        if not ok:
            fails.append((label, got, want))

    print("mouth.py --selftest")
    print()
    r = radius_from_feet(MOUTH_DIAMETER_FT)
    d = reach_from_radius(r)
    M = mass_from_radius(r)

    chk("ten feet is 3.048 m exactly", abs(2 * r - 3.048) < 1e-15, True)
    chk("reach inverts closeout's throat radius",
        abs(closeout.throat_radius(d) / r - 1.0) < 1e-15, True)
    chk("and the ratio is Lambda/2",
        abs(d / r / closeout.aspect_ratio() - 1.0) < 1e-15, True)
    chk("the reach is between 7 and 8 metres", 7.0 < d < 8.0, True)

    # the two mass routes must agree: r c^2/2G  and  Delta d c^2/(G Lambda)
    chk("the two mass routes agree",
        abs(M / ladder.mass_for_delta_d(d) - 1.0) < 1e-12, True)
    chk("mass is between 150 and 200 Earth masses",
        150.0 < M / M_EARTH < 200.0, True)
    chk("and under one Jupiter", M / M_JUPITER < 1.0, True)
    chk("energy matches the exchange rate",
        abs(M * c * c / ladder.energy_for_delta_d(d) - 1.0) < 1e-12, True)

    # scaling: halving the mouth halves the reach and the mass
    chk("halving the mouth halves the reach",
        abs(reach_from_radius(r / 2) / d - 0.5) < 1e-15, True)
    chk("and halves the mass",
        abs(mass_from_radius(r / 2) / M - 0.5) < 1e-15, True)
    chk("so the rate per metre is unchanged",
        abs(mass_from_radius(r / 2) / reach_from_radius(r / 2)
            / (M / d) - 1.0) < 1e-15, True)

    # density is the Schwarzschild density of that radius
    chk("density is M over the mouth volume",
        abs(density(r) * (4.0 / 3.0) * math.pi * r ** 3 / M - 1.0) < 1e-12, True)
    chk("and it exceeds nuclear density by over 1e8",
        density(r) / RHO_NUCLEAR > 1e8, True)

    # the inversion
    chk("a kilometre needs a mouth over 100 m",
        2 * radius_for_reach(1e3) > 100.0, True)
    chk("Proxima needs one over a light year across",
        2 * radius_for_reach(4.2465 * LY) / LY > 1.0, True)
    chk("packing factor for Proxima at ten feet exceeds 1e15",
        packing_factor(4.2465 * LY, r) > 1e15, True)

    # the escape, and its status
    chk("the bound is a theorem for positive mass",
        BOUND_IS_A_THEOREM_FOR_POSITIVE_MASS, True)
    chk("but not for negative mass", BOUND_IS_A_THEOREM_FOR_NEGATIVE_MASS, False)
    chk("the sign bookkeeping is resolved here", SIGN_BOOKKEEPING_RESOLVED, False)
    chk("ten feet is viable", TEN_FEET_IS_VIABLE, False)
    chk("figures were read", FIGURES_ARE_READ, False)
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
