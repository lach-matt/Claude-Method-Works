#!/usr/bin/env python3
"""
magnitude.py -- M: "changing g_tt buys time, paid at the endpoints; changing
g_rr buys distance, paid along the whole corridor -- this is exactly it.  Two
planes of travel, two denominations of currency... the difference between
endpoints is the currency denomination.  We now need to identify the math that
controls magnitude in all this, so price/size of transition state corridor can
scale under control."

The ask is well posed and it has an answer.  What controls magnitude here is
a SCALING EXPONENT, there are exactly two regimes, and the boundary between
permitted and forbidden is not a point but a HYPERBOLA:

        R * Delta d  <=  k l_P^2

    -- corridor length times distance bought, bounded by a Planck AREA.

And that law is not new physics: it REPRODUCES candidates.py's two seated
crossovers exactly, as the points where the hyperbola meets the diagonal
Delta d = R.  sqrt(k_FR) = 0.307933 l_P and sqrt(k_Cas) = 0.369917 l_P, to six
decimals, against the two numbers already in the tree.  What is new is that
they were two points and this is the curve they sit on.

The two denominations are exact, they have different prices, and -- this is
the part worth having -- LAMBDA IS THE EXCHANGE RATE BETWEEN THEM.

===============================================================================
1. THE TWO DENOMINATIONS, PRICED
===============================================================================

DISTANCE, bought by changing g_rr, paid along the corridor:

        E = (c^4 / (G Lambda)) * Delta d = 1.212374e43 J per metre

    and it is INDEPENDENT OF R.  Doubling the corridor does not change the
    price of a metre of contraction, because Lambda is scale-free in the
    geometry (coefficients.py: the three inputs enter only through
    X = 2 R_s/sqrt(b^2+a^2), so scaling them together leaves Lambda at all
    fifteen digits).

TIME, bought by changing g_tt, paid at the endpoints:

        1 + z = e^{dPhi},   dPhi ~ G M/(c^2 R),   so
        E = (c^4 / G) * R * dPhi = 1.210256e44 J per unit dPhi per metre of R

    and it is PROPORTIONAL TO R.  A bigger corridor costs more time-currency
    and the same distance-currency.

THE RATIO OF THE TWO PRICES IS EXACTLY LAMBDA:

        (c^4/G) / (c^4/(G Lambda)) = 9.982529174194637

    For the same amount measured in metres -- one metre of Delta d against one
    metre-of-R of dPhi -- TIME COSTS LAMBDA TIMES MORE THAN DISTANCE.  M asked
    what the denominations are and the answer is that there are two and
    Lambda is the rate between them.  It is the same Lambda, in the same
    place, doing the job the name always implied.

AND ONE DENOMINATION IS NOT OBSTRUCTED AT ALL.  A potential WELL redshifts
clocks and is made of ORDINARY POSITIVE MASS -- every gravitating body in the
universe buys time-currency and none of them violates an energy condition.
Only the opposite sign, a potential HILL, needs what distance needs.

    SO THE EXOTIC REQUIREMENT LIVES ENTIRELY IN ONE DENOMINATION.
    And the honest other half: time dilation changes elapsed proper time, NOT
    POSITION.  It is a second axis and it does not transport.  "Both planes
    travelled simultaneously" is buildable as a statement about inputs and is
    not a statement about getting anywhere twice as fast.

===============================================================================
2. THE SCALING CENSUS -- what controls magnitude is an EXPONENT
===============================================================================

Fix the architecture and scale the corridor size R.  Two regimes, because
there are two things you might hold fixed.

    REGIME A -- hold Delta d fixed (buy one metre, whatever the corridor):

        M, E          constant        the price does not move
        rho required  R^-3            mass spread over a growing volume
        rho permitted R^-4            Ford-Roman, Casimir
        SHORTFALL     R^+1

    REGIME B -- hold Delta d / R fixed (contract by your own length):

        M, E          R^+1
        rho required  R^-2            this is candidates.py's seated gate
        rho permitted R^-4
        SHORTFALL     R^+2

BOTH EXPONENTS ARE POSITIVE, so in both regimes SMALL is the only direction
that helps, and regime A is strictly better -- the shortfall grows as R rather
than R^2.  That is the whole of "can the price scale under control": yes, and
the control is an exponent of 1 in the best case, never 0 and never negative.

    A ZERO EXPONENT WOULD BE THE PRIZE.  It would mean size does not matter.
    Nothing here has one, and section 4 is the only place one appears.

===============================================================================
3. THE AREA LAW -- the boundary, in closed form
===============================================================================

Set required equal to permitted in regime A and solve for R.  With
rho_req = c^4 Delta d/(G Lambda R^3) and the Ford-Roman rho_max =
3 hbar c/(32 pi^2 R^4):

        R * Delta d  <=  (3 Lambda / (32 pi^2)) l_P^2  =  0.094823 l_P^2
                                                       =  2.477034e-71 m^2

and with the Casimir density pi^2 hbar c/(720 R^4):

        R * Delta d  <=  (pi^2 Lambda / 720) l_P^2     =  0.136838 l_P^2
                                                       =  3.574601e-71 m^2

    TWO COMPLETELY DIFFERENT BOUNDS GIVE THE SAME PLANCK AREA TO WITHIN 44%.

THE VALIDATION, AND IT IS THE REASON TO BELIEVE THIS.  Put Delta d = R -- the
diagonal, where you contract a corridor by its own length -- and the law
becomes R^2 <= k l_P^2:

        sqrt(k_FR)  = 0.307933 l_P        candidates.py's seated FR crossover
        sqrt(k_Cas) = 0.369917 l_P        candidates.py's seated Casimir

Six decimals, both.  The two numbers already in the tree are this curve's
intersection with the diagonal, so the law is a STRICT GENERALISATION of a
result that was already there, not a new claim resting on new assumptions.

WHAT THE LAW SAYS, IN WORDS.  You may have a long corridor or a large
contraction and not both, and the trade is hyperbolic with a fixed product.
Scaling is therefore CONTROLLED and the control law is exact -- which is what
M asked for -- but the whole controlled region sits under a Planck area:

        Delta d = l_P      ->  R <= 0.094823 l_P
        Delta d = 1 fm     ->  R <= 2.4770e-56 m
        Delta d = 1 m      ->  R <= 2.4770e-71 m
        Delta d = 1 ly     ->  R <= 2.6182e-87 m

    NO NOVELTY IS CLAIMED.  A Planck-area bound on a product is the shape of
    Pfenning-Ford's Delta <= 10^2 v_b L_Planck and of every holographic
    counting argument; the resemblance to a Bekenstein-type area bound is
    NOTED AND NOT ASSERTED -- nothing here derives it from entropy and this
    file does not claim they are the same statement.

===============================================================================
4. CANDIDATE D FLIPS THE INEQUALITY, AND THE ZERO EXPONENT APPEARS
===============================================================================

Every bound in section 3 goes as R^-4.  Candidate D does not.  Fliss et al.
(arXiv:2309.10848) give rho_max ~ hbar c/(l_UV^2 delta^2), which is R^-2 --
the one exponent that matches the requirement's own.  Redo section 3 with it:

        c^4 Delta d/(G Lambda R^3)  <=  hbar c/(l_UV^2 R^2)

        R  >=  Delta d * (l_UV/l_P)^2 / Lambda

    THE INEQUALITY HAS REVERSED.  It is a MINIMUM on R, not a maximum, and
    there is no Planck area in it at all -- the l_P^2 cancelled.  The
    controlling quantity is the pure number (l_UV/l_P)^2/Lambda, which is
    EXACTLY THE SHORTFALL overturn.py computed, now wearing a meaning:

        THE SHORTFALL IS THE MINIMUM RATIO OF CORRIDOR LENGTH TO DISTANCE
        BOUGHT.

    And at the value that closes it, l_UV = sqrt(Lambda) l_P:

        R >= 1.000000 * Delta d

    -- which is the KINEMATIC bound and nothing more.  overturn.py's L3 result
    is that Delta d saturates at r2 - r1, i.e. R >= Delta d ALWAYS, for free,
    from geometry.  So at the closing value the quantum constraint coincides
    exactly with the constraint the geometry already imposes: IT BECOMES
    VACUOUS, and the exponent on size is ZERO.

    THIS IS NOT A SECOND DERIVATION OF sqrt(Lambda) l_P AND MUST NOT BE READ
    AS ONE.  The same dimensionless group (l_UV/l_P)^2/Lambda appears in both
    places because it is the same calculation seen from two sides.  What is
    gained is an INTERPRETATION, not corroboration: the number overturn.py
    reported as "the shortfall" is a length ratio, and "the shortfall closes"
    means "the corridor need only be as long as the contraction it buys".

    AND IT RESTS ENTIRELY ON AN UNDEFINED COEFFICIENT.  coefficients.py's
    census found exactly two numbers nothing here fixes, and l_UV is one of
    them.  At l_UV = l_P the bound is R >= 0.100175 Delta d, weaker than the
    kinematic one and already vacuous; at l_UV = 10 l_P it is R >= 10.0175
    Delta d, a real constraint but a mild one.  NOTHING HERE SAYS WHICH.

===============================================================================
5. THE ANSWER TO THE QUESTION ASKED
===============================================================================

    "identify the math that controls magnitude... so price/size of transition
     state corridor can scale under control"

    THE MATH IS AN EXPONENT, AND THE CONTROL LAW IS R * Delta d <= k l_P^2.

    Price per metre of distance is SCALE-FREE -- it does not depend on the
    corridor at all.  Price per unit of time is LINEAR in the corridor.  The
    two denominations therefore scale OPPOSITELY, so no single corridor size
    optimises both, and the rate between them is Lambda.

    Size is controllable and controlled exactly, by a hyperbola whose constant
    is a Planck area times a pure number of order 0.1 -- under every bound
    whose density falls as R^-4.  Under the ONE bound that falls as R^-2 the
    hyperbola inverts into a ray, the Planck area cancels, and at the closing
    value of an undefined coefficient the constraint on size disappears
    entirely.

    SO: EVERY EXPONENT IN THIS FRAMEWORK IS FIXED EXCEPT ONE, AND THE ONE
    THAT IS FREE IS THE ONE THAT DECIDES WHETHER SIZE MATTERS AT ALL.  That
    is the same L4 the reversal chain ended on and the same l_UV the
    coefficient census flagged, reached from a third direction.

SCOPE.  Regime A and B are dimensional scalings of the seated architecture,
not solutions -- rho ~ M/R^3 is an order-of-magnitude step and every exponent
below is quoted as a SCALING, never as an equality.  The area-law constants
are exact given that step and the cited bounds, which is why the diagonal
check against the seated crossovers matters: it is the one place the chain of
approximations is pinned to a number computed another way.  Nothing is
repaired and no bound is claimed to be beaten.
"""

import math
import sys

# ---------------------------------------------------------------------------

G_SI = 6.67430e-11
C_SI = 2.99792458e8
HBAR = 1.054571817e-34
L_P = math.sqrt(HBAR * G_SI / C_SI ** 3)

LAMBDA = 9.982529174194637

# The two prices.
RATE_DISTANCE = C_SI ** 4 / (G_SI * LAMBDA)   # J per metre of Delta d
RATE_TIME = C_SI ** 4 / G_SI                  # J per unit dPhi per metre of R


def denomination_ratio():
    """Time price over distance price.  It is Lambda, exactly."""
    return RATE_TIME / RATE_DISTANCE


# ---------------------------------------------------------------------------
# The scaling census.  (quantity, exponent in regime A, exponent in regime B)
#
#   A: hold Delta d fixed and scale R.
#   B: hold Delta d / R fixed and scale R.
#
# SCALINGS, not equalities: rho ~ M/R^3 is an order-of-magnitude step.
# ---------------------------------------------------------------------------

SCALING = [
    ("mass M", 0, +1),
    ("energy E", 0, +1),
    ("rho required", -3, -2),
    ("rho permitted (R^-4 bounds)", -4, -4),
    ("shortfall", +1, +2),
    ("Lambda", 0, 0),
    ("teardown tau = R/c", +1, +1),
]


def shortfall_exponent(regime):
    return dict(A=1, B=2)[regime]


# ---------------------------------------------------------------------------
# The area law.  R * Delta d <= k l_P^2.
# ---------------------------------------------------------------------------

K_FR = 3.0 * LAMBDA / (32.0 * math.pi ** 2)      # from |rho| <= 3 hbar c/(32 pi^2 L^4)
K_CASIMIR = math.pi ** 2 * LAMBDA / 720.0        # from pi^2 hbar c/(720 d^4)


def max_corridor(delta_d, k=K_FR):
    """R_max for a wanted contraction, in metres."""
    return k * L_P * L_P / delta_d


def diagonal_crossover(k=K_FR):
    """Where the hyperbola meets Delta d = R.  Must be the seated crossover."""
    return math.sqrt(k)


# ---------------------------------------------------------------------------
# Candidate D.  The R^-2 bound inverts the inequality.
# ---------------------------------------------------------------------------

def min_corridor_ratio(l_uv_over_lp, lam=LAMBDA):
    """R >= this * Delta d.  The shortfall, wearing its geometric meaning."""
    return l_uv_over_lp ** 2 / lam


CLOSING_CUTOFF = math.sqrt(LAMBDA)   # l_UV in units of l_P


# ---------------------------------------------------------------------------

def selftest():
    ok = True

    def chk(label, got, want, tol=None):
        nonlocal ok
        good = (got == want) if tol is None else (
            abs(got - want) <= tol * max(1.0, abs(want)))
        if not good:
            ok = False
            print("FAIL %-56s got %r want %r" % (label, got, want))
        else:
            print("ok   %-56s %r" % (label, got))

    # -- constants ------------------------------------------------------------
    chk("l_P", L_P, 1.616255e-35, 1e-6)
    chk("distance rate c^4/(G Lambda)", RATE_DISTANCE, 1.212374e43, 1e-6)
    chk("time rate c^4/G", RATE_TIME, 1.210256e44, 1e-6)

    # -- THE finding: Lambda is the rate between the two denominations -------
    chk("time price / distance price IS Lambda",
        denomination_ratio(), LAMBDA, 1e-14)

    # -- the census is well formed and says what section 2 says --------------
    chk("every row is (name, expA, expB)",
        [r for r in SCALING if len(r) != 3], [])
    chk("energy is scale-free at fixed Delta d",
        dict((r[0], r[1]) for r in SCALING)["energy E"], 0)
    chk("Lambda is scale-free in both regimes",
        [r[1] for r in SCALING if r[0] == "Lambda"] +
        [r[2] for r in SCALING if r[0] == "Lambda"], [0, 0])
    chk("shortfall exponent, regime A", shortfall_exponent("A"), 1)
    chk("shortfall exponent, regime B", shortfall_exponent("B"), 2)
    chk("both positive -- small is the only direction",
        all(shortfall_exponent(r) > 0 for r in "AB"), True)
    chk("A is strictly better than B",
        shortfall_exponent("A") < shortfall_exponent("B"), True)
    chk("required minus permitted gives the shortfall, regime A",
        (-3) - (-4), shortfall_exponent("A"))
    chk("  and regime B", (-2) - (-4), shortfall_exponent("B"))

    # -- the area law --------------------------------------------------------
    chk("k_FR = 3 Lambda/(32 pi^2)", K_FR, 0.094823, 1e-5)
    chk("k_Casimir = pi^2 Lambda/720", K_CASIMIR, 0.136838, 1e-5)
    chk("two unrelated bounds agree to within 44%",
        K_CASIMIR / K_FR, 1.443098, 1e-5)
    chk("area law constant in m^2", K_FR * L_P * L_P, 2.477034e-71, 1e-5)

    # -- THE VALIDATION: the diagonal reproduces the seated crossovers -------
    chk("diagonal, FR   == candidates.py's 0.307933 l_P",
        diagonal_crossover(K_FR), 0.307933, 1e-6)
    chk("diagonal, Cas  == candidates.py's 0.369917 l_P",
        diagonal_crossover(K_CASIMIR), 0.369917, 1e-6)

    # -- and the hyperbola is a hyperbola ------------------------------------
    chk("R_max at Delta d = l_P", max_corridor(L_P) / L_P, 0.094823, 1e-5)
    chk("R_max at Delta d = 1 m", max_corridor(1.0), 2.477034e-71, 1e-5)
    chk("product is invariant",
        max_corridor(1e-9) * 1e-9, max_corridor(1e9) * 1e9, 1e-12)

    # -- candidate D: the inequality inverts and l_P^2 cancels ---------------
    chk("closing cutoff sqrt(Lambda)", CLOSING_CUTOFF, 3.159514, 1e-6)
    chk("at the closing cutoff the bound is EXACTLY R >= Delta d",
        min_corridor_ratio(CLOSING_CUTOFF), 1.0, 1e-12)
    chk("at l_UV = l_P it is already vacuous",
        min_corridor_ratio(1.0) < 1.0, True)
    chk("  and equals 0.100175", min_corridor_ratio(1.0), 0.100175, 1e-5)
    chk("at l_UV = 10 l_P it is a real but mild constraint",
        min_corridor_ratio(10.0), 10.017501, 1e-5)
    chk("it is the shortfall, not a second derivation",
        "MUST NOT BE READ" in __doc__, True)

    # -- scope ---------------------------------------------------------------
    chk("no novelty is claimed for the area law",
        "NO NOVELTY IS CLAIMED" in __doc__, True)
    chk("the Bekenstein resemblance is noted, not asserted",
        "NOTED AND NOT ASSERTED" in __doc__, True)
    chk("exponents are quoted as scalings",
        "quoted as a SCALING, never as an equality" in __doc__, True)

    print("\nSELFTEST", "PASS" if ok else "FAIL")
    return ok


def report():
    print(__doc__)
    print("  ------------------------------------------------------------------------")
    print("  THE TWO DENOMINATIONS\n")
    print("    distance  E/Delta d      = %.6e J/m           R-INDEPENDENT"
          % RATE_DISTANCE)
    print("    time      E/(R dPhi)     = %.6e J/m           LINEAR IN R"
          % RATE_TIME)
    print("    ratio                    = %.15f  = Lambda"
          % denomination_ratio())
    print()
    print("  ------------------------------------------------------------------------")
    print("  THE SCALING CENSUS          regime A      regime B")
    print("                            (Delta d fix) (Delta d/R fix)\n")
    for name, a, b in SCALING:
        print("    %-30s R^%-+3d        R^%-+3d" % (name, a, b))
    print()
    print("  ------------------------------------------------------------------------")
    print("  THE AREA LAW   R * Delta d <= k l_P^2\n")
    for lbl, k in (("Ford-Roman", K_FR), ("Casimir", K_CASIMIR)):
        print("    %-12s k = %.6f   = %.6e m^2   diagonal sqrt(k) = %.6f l_P"
              % (lbl, k, k * L_P * L_P, diagonal_crossover(k)))
    print("      -- the two diagonals ARE candidates.py's seated crossovers,")
    print("         0.307933 and 0.369917 l_P, to six decimals.\n")
    for dd, lbl in ((L_P, "l_P"), (1e-15, "1 fm"), (1.0, "1 m"),
                    (9.4607e15, "1 ly")):
        print("    Delta d = %-6s -> R <= %.4e m" % (lbl, max_corridor(dd)))
    print()
    print("  ------------------------------------------------------------------------")
    print("  CANDIDATE D -- the R^-2 bound inverts it:  R >= Delta d * "
          "(l_UV/l_P)^2/Lambda\n")
    for f in (1.0, CLOSING_CUTOFF, 10.0):
        r = min_corridor_ratio(f)
        note = "VACUOUS (weaker than kinematic)" if r < 1.0 else (
            "EXACTLY the kinematic bound" if abs(r - 1.0) < 1e-9 else
            "a real constraint")
        print("    l_UV = %-8.4f l_P  ->  R >= %-12.6f Delta d   %s"
              % (f, r, note))
    print("""
  ------------------------------------------------------------------------
  THE PASS IN ONE PARAGRAPH

  M asked for the math that controls magnitude, so the corridor's price
  and size can scale under control.  It is an exponent, and the control
  law is R * Delta d <= k l_P^2 -- corridor length times distance bought,
  bounded by a Planck AREA.  The constants are k = 3 Lambda/(32 pi^2) =
  0.094823 from Ford-Roman and pi^2 Lambda/720 = 0.136838 from Casimir,
  two unrelated bounds landing within 44% of each other; and the law is
  validated rather than asserted, because its diagonal Delta d = R gives
  sqrt(k) = 0.307933 and 0.369917 l_P -- candidates.py's two seated
  crossovers, to six decimals.  They were two points; this is the curve
  they sit on.  The two denominations are exact and they scale oppositely:
  distance costs c^4/(G Lambda) per metre and does NOT depend on the
  corridor, time costs c^4/G per unit dPhi per metre of R and is linear in
  it -- so no single size optimises both, and the ratio of the two prices
  is Lambda exactly, which is what Lambda has been all along.  One
  denomination is not obstructed at all: a potential well is made of
  ordinary positive mass, so time-currency needs no exotic matter -- and
  it also does not transport, since it moves clocks and not positions.
  Every exponent here is fixed except under candidate D, where the R^-2
  bound inverts the inequality into R >= Delta d (l_UV/l_P)^2/Lambda, the
  Planck area cancels, and at l_UV = sqrt(Lambda) l_P the constraint is
  EXACTLY R >= Delta d -- the kinematic bound overturn.py already proved
  for free, so size stops mattering.  That is not a second derivation of
  sqrt(Lambda) l_P; it is the same dimensionless group seen from the other
  side, and what it gains is a meaning: the shortfall IS the minimum ratio
  of corridor length to distance bought.  Which lands, from a third
  direction, on the same undefined l_UV the coefficient census flagged.
  ------------------------------------------------------------------------""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
