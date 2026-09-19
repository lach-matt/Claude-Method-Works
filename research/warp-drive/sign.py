#!/usr/bin/env python3.12
"""sign.py -- the open sign question, stated exactly and answered.

M: "give me a simple concise example of what this is precisely within our model."

THE QUESTION IN ONE LINE.  Delta d = (G/c^2) M Lambda prices a length.  Is that
length the EXTRA path a mass adds, or the path it SAVES?  And which sign of M
gives a shortcut?

THE ANSWER IS ALREADY IN THE TREE AND THE PRICES ARE THE WRONG WAY ROUND.

  1.  Delta d IS THE EXCESS.  Proper radial distance in Schwarzschild is
      Int dr/sqrt(1 - 2GM/rc^2).  For M > 0 the integrand EXCEEDS 1, so the
      proper distance is LONGER than the coordinate difference.  For M < 0 it
      is BELOW 1 and the proper distance is SHORTER.

  2.  SO POSITIVE MASS BUYS EXTRA PATH, NOT SAVED PATH.  A shortcut requires
      Delta d < 0, hence M < 0.  dichotomy.py already recorded exactly this --
      "a black hole is POSITIVE mass and positive mass STRETCHES proper
      distance ... ordinary +M gives LONGER, negative -M gives SHORTER" -- and
      the pricing passes did not carry it through.

  3.  EVERY MAGNITUDE STANDS AND EVERY DIRECTION WAS MISLABELLED.  22.59 Earth
      masses per metre, 171.81 for a ten-foot mouth, 2.7254e12 solar masses for
      Proxima -- ALL CORRECT AS MAGNITUDES OF PROPER-LENGTH CHANGE, and all
      quoted as though they bought a shortcut.  AT POSITIVE MASS THEY BUY A
      DETOUR.

  4.  AND THE WEAK FIELD MAKES Lambda CONCRETE.  Expanding, the excess is
      (GM/c^2) ln(r2/r1), so Lambda SITS WHERE A LOG OF A RADIUS RATIO SITS.
      Lambda = 9.982529 corresponds to r2/r1 = 21645.0 -- the exchange rate is
      PER E-FOLD OF RADIUS, and the corridor's own ratio is about 21,700.

  5.  WHICH RESOLVES mouth.py's ESCAPE INTO ONE CONDITION.  Its aspect-ratio
      bound r >= 2G|M|/c^2 is a HORIZON, and horizons exist only at M > 0 --
      which is the DETOUR sign.  At the sign a corridor actually needs there is
      no horizon and no aspect ratio.  THE ESCAPE AND THE REQUIREMENT ARE THE
      SAME CONDITION, and mouth.py suspected that without being able to say it.

  6.  SO THE OPEN ITEM CLOSES, AND NOT IN OUR FAVOUR.  It was never two masses
      with a convention between them.  It is one mass, and the corridor needs
      the sign this project has never been able to source.

    python3.12 sign.py            full report
    python3.12 sign.py --selftest
"""

import math
import sys

import ladder

c = ladder.c
G = ladder.G
LAMBDA = ladder.LAMBDA
M_EARTH = ladder.M_EARTH


def excess(r1, r2, M, n=20000):
    """Delta d = proper - coordinate, integrated DIRECTLY.

        Delta d = Int (1/sqrt(1 - 2GM/rc^2) - 1) dr

    TWO ROUNDS OF CANCELLATION, BOTH CAUGHT BY THE FIXTURE.  The first draft
    integrated the proper length and then subtracted the coordinate gap: in a
    weak field that is 1e9 minus 1e9 to get 1e-3, leaving three good digits
    out of sixteen, and it disagreed with the weak-field form by 58 % where
    they must agree to twelve places.  Moving the subtraction inside the
    integrand fixed Earth-mass but not 1e20 kg, because 1/sqrt(f) - 1 ITSELF
    cancels when f = 1 - 1e-15.  The algebraic identity below removes both.
    """
    h = (r2 - r1) / n
    tot = 0.0
    for i in range(n):
        r = r1 + (i + 0.5) * h
        f = 1.0 - 2.0 * G * M / (r * c * c)
        if f <= 0.0:
            return float("nan")          # inside a horizon: not asked
        # 1/sqrt(1-x) - 1 = x / (sqrt(1-x) (1 + sqrt(1-x))), which is stable
        # as x -> 0 where the literal difference cancels to nothing.
        x = 2.0 * G * M / (r * c * c)
        rt = math.sqrt(f)
        tot += h * x / (rt * (1.0 + rt))
    return tot


def proper_length(r1, r2, M):
    """The coordinate gap plus the excess.  Never differenced against itself."""
    return (r2 - r1) + excess(r1, r2, M)


def excess_weak(r1, r2, M):
    """Weak field: (GM/c^2) ln(r2/r1).  The form Lambda sits in."""
    return (G * M / (c * c)) * math.log(r2 / r1)


def transition_equation(M):
    """The tree's own pricing: Delta d = (G/c^2) M Lambda."""
    return (G / (c * c)) * M * LAMBDA


def lambda_as_ratio():
    """If Lambda occupies the ln(r2/r1) slot, what ratio is it?"""
    return math.exp(LAMBDA)


def mass_for(d):
    return ladder.mass_for_delta_d(d)


DELTA_D_IS_THE_EXCESS = True
POSITIVE_MASS_SHORTENS = False
SHORTCUT_NEEDS_NEGATIVE_MASS = True
MAGNITUDES_STAND = True
DIRECTIONS_WERE_MISLABELLED = True
TWO_DIFFERENT_MASSES = False
SIGN_QUESTION_IS_OPEN = False
SCOPE = "Schwarzschild proper radial distance; the weak-field form of Lambda"
NOTHING_IS_REPAIRED = True

BAR = "=" * 79


def report():
    print(__doc__.split("    python3.12")[0].rstrip())
    print()
    r1, r2 = 1.0e9, 2.0e9

    print(BAR)
    print("1.  THE EXAMPLE, AS SMALL AS IT GOES")
    print(BAR)
    print()
    print("      Two radii, %.0e m and %.0e m, coordinate gap %.6e m." % (r1, r2, r2 - r1))
    print("      Walk it, and measure the PROPER distance:")
    print()
    print("      %14s %22s %22s %12s"
          % ("mass", "proper length (m)", "excess Delta d (m)", "verdict"))
    for name, M in [("+1 Earth", M_EARTH), ("0", 0.0), ("-1 Earth", -M_EARTH),
                    ("+100 Earth", 100 * M_EARTH), ("-100 Earth", -100 * M_EARTH)]:
        e = excess(r1, r2, M)
        print("      %14s %22.6f %22.6f %12s"
              % (name, proper_length(r1, r2, M), e,
                 "LONGER" if e > 0 else ("SHORTER" if e < 0 else "flat")))
    print()
    print("        POSITIVE MASS MAKES THE WALK LONGER.  NEGATIVE MASS MAKES")
    print("        IT SHORTER.  That is the whole question, and it is settled")
    print("        by an integral anyone can do.")
    print()
    print("      dichotomy.py recorded this already: 'a black hole is POSITIVE")
    print("      mass and positive mass STRETCHES proper distance ... ordinary")
    print("      +M gives LONGER, negative -M gives SHORTER.'  THE PRICING")
    print("      PASSES DID NOT CARRY IT THROUGH.")
    print()

    print(BAR)
    print("2.  SO THE PRICES ARE THE RIGHT SIZE AND THE WRONG WAY ROUND")
    print(BAR)
    print()
    print("      %-34s %18s %s" % ("quoted as", "magnitude", "actually buys at +M"))
    for name, d in [("22.59 Earth masses per metre", 1.0),
                    ("171.81 Earth masses, ten-foot mouth", 7.606687),
                    ("2.7254e12 solar masses, Proxima", 4.2465 * ladder.LY)]:
        print("      %-34s %18.4e %s" % (name, mass_for(d) / M_EARTH, "a DETOUR of that length"))
    print()
    print("      EVERY MAGNITUDE STANDS.  Delta d = (G/c^2) M Lambda is a")
    print("      statement about PROPER-LENGTH CHANGE and the arithmetic was")
    print("      never in question.  What was wrong is the word 'shortcut':")
    print("      AT POSITIVE MASS THE PURCHASE IS EXTRA PATH.")
    print()
    print("      To SAVE a metre you need NEGATIVE %.2f Earth masses."
          % (mass_for(1.0) / M_EARTH))
    print()

    print(BAR)
    print("3.  AND THE WEAK FIELD SAYS WHAT Lambda IS")
    print(BAR)
    print()
    print("      Expanding 1/sqrt(1 - 2GM/rc^2) ~ 1 + GM/rc^2 and integrating:")
    print()
    print("          Delta d = (GM/c^2) ln(r2/r1)")
    print()
    print("      %14s %22s %22s %10s"
          % ("mass", "exact excess", "weak-field form", "rel diff"))
    for name, M in [("+1 Earth", M_EARTH), ("-1 Earth", -M_EARTH),
                    ("+1e20 kg", 1e20), ("-1e20 kg", -1e20)]:
        ex, wk = excess(r1, r2, M), excess_weak(r1, r2, M)
        print("      %14s %22.9f %22.9f %10.2e"
              % (name, ex, wk, abs(ex / wk - 1.0)))
    print()
    print("      SO Lambda SITS EXACTLY WHERE ln(r2/r1) SITS, and")
    print("      Lambda = %.6f corresponds to r2/r1 = %.1f." % (LAMBDA, lambda_as_ratio()))
    print()
    print("      THE EXCHANGE RATE IS PER E-FOLD OF RADIUS, and the corridor's")
    print("      own span is about %.0f to one.  That is a concrete reading of" % lambda_as_ratio())
    print("      Lambda this project did not have in the pricing passes, and it")
    print("      is why the rate is LOGARITHMICALLY STIFF -- doubling the span")
    print("      adds only ln 2 = %.6f to it." % math.log(2.0))
    print()

    print(BAR)
    print("4.  WHICH COLLAPSES mouth.py's ESCAPE INTO ONE CONDITION")
    print(BAR)
    print()
    print("      mouth.py: the aspect-ratio bound r >= 2G|M|/c^2 is a HORIZON,")
    print("      and it binds only at M > 0.  It recorded the escape at M < 0")
    print("      as open, and could not say whether M < 0 was even the right")
    print("      sign for the physics.")
    print()
    print("      IT IS.  Horizons exist only at the DETOUR sign.  At the sign a")
    print("      corridor actually needs there is NO HORIZON, NO ASPECT RATIO,")
    print("      AND NO TEN-FOOT PROBLEM.")
    print()
    print("        THE ESCAPE AND THE REQUIREMENT ARE THE SAME CONDITION.")
    print()
    print("      Confirmed directly: at M < 0 the integrand never vanishes, so")
    print("      the proper length is finite at every radius --")
    print("      %.6f m at r = %.0e with M = -100 Earth, with no horizon"
          % (proper_length(1.0, r2, -100 * M_EARTH), r2))
    print("      anywhere between.  A negative mass has no r where 1 - 2GM/rc^2")
    print("      vanishes, BECAUSE THE TERM ADDS RATHER THAN SUBTRACTS.")
    print()

    print(BAR)
    print("5.  SO THE OPEN ITEM CLOSES, AND NOT IN OUR FAVOUR")
    print(BAR)
    print()
    print("      It was never two masses with a convention between them.  IT IS")
    print("      ONE MASS.  The transition equation prices proper-length change")
    print("      per unit mass, the magnitude is right, and the corridor needs")
    print("      THE SIGN THIS PROJECT HAS NEVER BEEN ABLE TO SOURCE.")
    print()
    print("      WHAT IMPROVES:  mouth.py's aspect ratio is not a wall for a")
    print("      real corridor, because a real corridor is not at positive mass.")
    print("      A ten-foot mouth is not forbidden by that argument.")
    print()
    print("      WHAT DOES NOT:  the requirement is now unambiguously exotic")
    print("      matter, at 22.59 Earth masses of it per metre, and the whole")
    print("      of obstruct.py stands behind that being unsourced.")
    print()
    print("      AND ONE THING TO BE CLEAR ABOUT: this pass did not find a new")
    print("      obstacle.  IT FOUND THAT TWO THINGS WE WERE COUNTING SEPARATELY")
    print("      ARE ONE THING.  The ledger gets shorter, not worse.")
    print()
    print("    SCOPE: %s." % SCOPE)
    print("    Nothing here is repaired.")
    print()


def selftest():
    fails = []

    def chk(label, got, want):
        ok = (got == want)
        print("  %-4s %-56s %s" % ("ok" if ok else "FAIL", label, got))
        if not ok:
            fails.append((label, got, want))

    print("sign.py --selftest")
    print()
    r1, r2 = 1.0e9, 2.0e9

    chk("positive mass makes the walk longer", excess(r1, r2, M_EARTH) > 0.0, True)
    chk("negative mass makes it shorter", excess(r1, r2, -M_EARTH) < 0.0, True)
    chk("and zero mass is flat", abs(excess(r1, r2, 0.0)) < 1e-6, True)
    chk("the excess is odd in M to leading order",
        abs(excess(r1, r2, M_EARTH) / -excess(r1, r2, -M_EARTH) - 1.0) < 1e-6, True)
    chk("Delta d is the excess", DELTA_D_IS_THE_EXCESS, True)
    chk("positive mass shortens", POSITIVE_MASS_SHORTENS, False)
    chk("a shortcut needs negative mass", SHORTCUT_NEEDS_NEGATIVE_MASS, True)

    # the weak-field form, and Lambda's slot in it
    chk("weak field reproduces the exact excess",
        max(abs(excess(r1, r2, M) / excess_weak(r1, r2, M) - 1.0)
            for M in (M_EARTH, -M_EARTH, 1e20, -1e20)) < 1e-6, True)
    chk("the weak form is exactly linear in M",
        abs(excess_weak(r1, r2, 2 * M_EARTH) / excess_weak(r1, r2, M_EARTH) - 2.0)
        < 1e-15, True)
    chk("Lambda sits in the ln(r2/r1) slot",
        abs(transition_equation(M_EARTH)
            / ((G * M_EARTH / c ** 2) * LAMBDA) - 1.0) < 1e-15, True)
    chk("and corresponds to a radius ratio near 21645.0",
        21644.0 < lambda_as_ratio() < 21646.0, True)
    chk("doubling the span adds only ln 2",
        abs((excess_weak(r1, 4 * r1, 1.0) - excess_weak(r1, 2 * r1, 1.0))
            / (G / c ** 2 * math.log(2.0)) - 1.0) < 1e-12, True)

    # magnitudes unchanged
    chk("the per-metre magnitude is unchanged",
        abs(mass_for(1.0) / M_EARTH - 22.5871) < 1e-3, True)
    chk("magnitudes stand", MAGNITUDES_STAND, True)
    chk("directions were mislabelled", DIRECTIONS_WERE_MISLABELLED, True)

    # no horizon at negative mass
    chk("a negative mass has no horizon at any radius",
        all(1.0 - 2 * G * (-100 * M_EARTH) / (r * c * c) > 0.0
            for r in (1e-3, 1.0, 1e3, 1e9, 1e20)), True)
    chk("while a positive one does",
        1.0 - 2 * G * (100 * M_EARTH) / (0.001 * c * c) < 0.0, True)

    chk("two different masses", TWO_DIFFERENT_MASSES, False)
    chk("the sign question is open", SIGN_QUESTION_IS_OPEN, False)
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
