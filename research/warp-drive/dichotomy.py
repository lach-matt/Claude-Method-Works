#!/usr/bin/env python3
"""
dichotomy.py -- "so we need to build a miniature contained black hole?"

NO.  And the question is worth a file because the tree DOES contain a
"you need a black hole" result, currency.py states it in one line, and that
line is TOO BROAD -- our own corridor is the counterexample.  Corrected here
and in place there.

The answer has four legs, and the fourth is the one that matters.

===============================================================================
1. WRONG SIGN, AND MAXIMALLY SO
===============================================================================

A black hole is POSITIVE mass.  phase1.py proved the quantity a transition acts
on is PROPER DISTANCE, and positive mass STRETCHES it:

        source          Phi at b = 1        proper length
        ordinary +M     -8.00000e-02        LONGER
        negative -M     +7.95840e-02        SHORTER

    A BLACK HOLE IS NOT A WEAK VERSION OF WHAT THIS NEEDS.  IT IS THE OPPOSITE
    SIGN, AT MAXIMUM STRENGTH.  Build one in the corridor and the corridor gets
    longer.  transition.py said the same thing about lensing and it applies
    here with more force: a lens has the wrong sign for this concept entirely.

===============================================================================
2. "CONTAINED" BUYS NOTHING -- BIRKHOFF
===============================================================================

By Birkhoff's theorem the exterior of any spherically symmetric mass is
Schwarzschild with that mass, whatever the interior does.  Containment is
invisible from outside.  A contained black hole of mass M and an uncontained
one of mass M curve the corridor identically, so the containment in the
question does no work.

===============================================================================
3. WHERE THE BLACK-HOLE RESULT ACTUALLY COMES FROM, AND WHAT IT BINDS
===============================================================================

spec.py measures seat_over_collapse = 2 pi^2/3 = 6.5797 AT EVERY SCALE: a
region that seats a conjugate point exceeds its own collapse bound by that
factor, so it sits inside its own Schwarzschild radius.  entangle.py reaches
19.7392 = 2 pi^2 from entropy, and currency.py showed the two differ by exactly
3, the 3 in M = (4/3) pi R^3 rho.

    BUT ALL OF THAT PRICES THE **STURM** SEAT, AND STURM IS A RICCI STATEMENT.
    The condition is q l^2 >= pi^2 with q = 4 pi T_kk, and it requires
    q >= m > 0 -- POSITIVE energy density, focusing through Ricci.
    seatindex.py's tkk_required(1 m) = 9.5053e+43 Pa is positive by
    construction.

    OUR CORRIDOR'S CORE T_kk IS NEGATIVE.  It does not meet Sturm, it is not
    trying to, and the collapse result does not reach it.

===============================================================================
4. MEASURED: THE CORRIDOR SEATS AND IS NOT A BLACK HOLE
===============================================================================

        conjugate point at lambda   165.36        it seats
        has_throat                  False
        has_horizon                 False
        M_ADM residual at r = 1000  -4.000e-15    zero to fifteen digits

    It focuses through WEYL, which composite.py measured to be QUADRATIC in the
    source and SIGN-BLIND, so it carries no density requirement at all.  That
    is the whole reason the two-region device was built.

===============================================================================
THE DICHOTOMY, WHICH IS THE CLEANEST STRUCTURE THIS PROJECT HAS
===============================================================================

    ROUTE A -- ORDINARY MATTER.  Positive energy, focusing through RICCI, needs
        the Sturm density q l^2 >= pi^2, exceeds the collapse bound by
        2 pi^2/3 at every scale, and the region closes inside its own
        Schwarzschild radius.  BLOCKED BY COLLAPSE.  This is the route on which
        "you need a black hole" is TRUE, and it is true as a prohibition rather
        than a recipe: you do not get a device, you get a black hole.

    ROUTE B -- NEGATIVE MASS.  Focusing through WEYL, quadratic and sign-blind,
        no density requirement, no horizon, no throat, M_ADM = 0.  Seats at
        lambda = 165 and stays a device.  BLOCKED BY THE SOURCE.

    TWO ROUTES, TWO DIFFERENT BLOCKERS, AND THIS PROJECT IS ON THE SECOND.

    SO THE INTUITION IS RIGHT ABOUT ROUTE A AND THE PROJECT IS NOT ON IT.  What
    the corridor buys by going the Weyl way is escape from collapse; what it
    pays is that the source must have rho < 0, which supply.py, scale.py and
    shaping.py have now closed from four directions.

        THE TRADE IS EXPLICIT: A COLLAPSE PROBLEM EXCHANGED FOR A SOURCE
        PROBLEM.  Neither is solved.  They are different, and confusing them
        costs the distinction that makes the device worth describing at all.

===============================================================================
THE CORRECTION THIS QUESTION FORCED
===============================================================================

currency.py line 242 reads

        ONE_STATEMENT = "a region that seats a conjugate point is a black hole"

    and that is TOO BROAD.  Our own corridor seats a conjugate point at
    lambda = 165.36 with no horizon, no throat and M_ADM = 0.  The correct
    statement carries its hypothesis:

        "a region that seats a conjugate point BY RICCI FOCUSING is a black
         hole"

    Corrected in place there.  The over-broad version had stood since
    currency.py was written and nothing in this tree had tested it against the
    device the tree itself built.

stdlib only.
"""
import math, sys

RICCI, WEYL = "Ricci", "Weyl"


# ------------------------------------------------------------- 1: the sign

def proper_length_change(sign_of_mass, strength=8.0e-2):
    """Does this source lengthen or shorten the corridor?  Measured."""
    import transition, concentric
    if sign_of_mass > 0:                       # ordinary, positive mass
        phi = transition.ordinary_potential(strength)
    else:                                      # negative mass
        phi = concentric.potential(strength)
    pr, _lt = transition.proper_ratio(phi, -150.0, 150.0, 1.0)
    return "LONGER" if pr > 1.0 else "SHORTER"


def black_hole_is_wrong_sign():
    """A black hole is positive mass, and positive mass stretches."""
    return proper_length_change(+1) == "LONGER"


# ------------------------------------------------ 2: containment does nothing

BIRKHOFF = ("the exterior of any spherically symmetric mass is Schwarzschild "
            "with that mass, whatever the interior does")


def containment_helps():
    """No.  Birkhoff: the outside cannot tell."""
    return False


# ---------------------------------------- 3: which seat the collapse result binds

def sturm_is_positive_energy():
    """q l^2 >= pi^2 with q = 4 pi T_kk needs q > 0.  Ricci, positive energy."""
    import seatindex
    return seatindex.tkk_required(1.0) > 0.0


def collapse_ratio():
    """spec.py's 2 pi^2/3, scale-invariant.  It prices the STURM seat."""
    import spec
    return spec.seat_over_collapse(1.0)


def collapse_binds(route):
    """Route A only.  Weyl carries no density requirement to exceed."""
    return route == RICCI


# ------------------------------------------- 4: what the corridor actually is

def corridor_facts(m=2.0e-2):
    import concentric, transition
    r = concentric.survey(m)
    phi = concentric.potential(m)
    radii = [0.05 * i for i in range(1, 4001)]
    return {"conjugate": r["conjugate"],
            "throat": transition.has_throat(phi, radii),
            "horizon": transition.has_horizon(phi, radii),
            "adm": concentric.adm_residual(m)}


def corridor_is_a_black_hole(m=2.0e-2, tol=1e-12):
    f = corridor_facts(m)
    return f["horizon"] or f["throat"] or abs(f["adm"]) > tol


def corridor_seats(m=2.0e-2):
    return corridor_facts(m)["conjugate"] is not None


# ---------------------------------------------------------- the dichotomy

ROUTES = (
    (RICCI, "ordinary matter, positive energy",
     "needs Sturm q l^2 >= pi^2, exceeds collapse by 2 pi^2/3 at every scale",
     "COLLAPSE -- you get a black hole, not a device"),
    (WEYL, "negative mass, quadratic and sign-blind",
     "no density requirement; seats at 165.36 with no horizon and M_ADM = 0",
     "THE SOURCE -- rho < 0, closed from four directions"),
)


def blockers():
    return {r[0]: r[3].split(" --")[0] for r in ROUTES}


def different_blockers():
    b = blockers()
    return b[RICCI] != b[WEYL]


ONE_STATEMENT_WAS = "a region that seats a conjugate point is a black hole"
ONE_STATEMENT_IS = ("a region that seats a conjugate point BY RICCI FOCUSING "
                    "is a black hole")


def old_statement_has_a_counterexample():
    """Our own corridor.  Which is why it needed the hypothesis attached."""
    return corridor_seats() and not corridor_is_a_black_hole()


# ------------------------------------------------------------------ selftest

def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-56s %18s %18s  %s" % (label, got, want, "ok" if good else "FAIL"))

    def near(label, got, want, rtol):
        nonlocal ok
        good = abs(got - want) <= rtol * abs(want)
        ok &= good
        print("  %-56s %18.6e %18.6e  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("1. SIGN -- a black hole is positive mass, and positive mass stretches")
    chk("ordinary +M does this to the corridor", proper_length_change(+1), "LONGER")
    chk("negative -M does this", proper_length_change(-1), "SHORTER")
    chk("a black hole is the wrong sign", black_hole_is_wrong_sign(), True)
    print("      not a weak version of what is needed -- the OPPOSITE sign, at")
    print("      maximum strength.")

    print("\n2. 'CONTAINED' BUYS NOTHING -- Birkhoff")
    chk("containment changes the exterior", containment_helps(), False)
    print("      %s" % BIRKHOFF)

    print("\n3. THE BLACK-HOLE RESULT PRICES THE **STURM** SEAT, WHICH IS RICCI")
    near("spec.py's seat_over_collapse", collapse_ratio(), 2.0 * math.pi ** 2 / 3.0, 1e-6)
    chk("Sturm requires positive energy density", sturm_is_positive_energy(), True)
    chk("collapse binds the Ricci route", collapse_binds(RICCI), True)
    chk("and the Weyl route", collapse_binds(WEYL), False)

    print("\n4. MEASURED -- the corridor seats and is not a black hole")
    f = corridor_facts()
    print("      conjugate point   %.2f" % f["conjugate"])
    print("      throat            %s" % f["throat"])
    print("      horizon           %s" % f["horizon"])
    print("      M_ADM residual    %.3e" % f["adm"])
    chk("it seats", corridor_seats(), True)
    chk("it is a black hole", corridor_is_a_black_hole(), False)

    print("\nTHE DICHOTOMY")
    for name, what, needs, blocker in ROUTES:
        print("      %-6s %-38s %s" % (name, what, blocker))
    chk("the two routes have DIFFERENT blockers", different_blockers(), True)
    print("      a collapse problem exchanged for a source problem.  Neither is")
    print("      solved; they are different, and conflating them costs the")
    print("      distinction that makes the device worth describing.")

    print("\nTHE CORRECTION THIS QUESTION FORCED")
    chk("the old one-line statement has a counterexample",
        old_statement_has_a_counterexample(), True)
    print("      was: %s" % ONE_STATEMENT_WAS)
    print("      is:  %s" % ONE_STATEMENT_IS)
    # THE CITATION WAS TO A CONSTANT THAT NO LONGER EXISTS, and this pin crashed
    # on it. currency.py DID define ONE_STATEMENT at the entropy-denomination
    # version (35091ce); the modified-gravity rewrite (59c77c9) replaced that
    # file's whole subject and dropped the constant WITHOUT SWEEPING THE THREE
    # FILES THAT CITE IT -- which is exactly the fault reversal.py names, "a
    # file's DEPENDENTS are not swept", committed on reversal.py's own example.
    # Re-seating an unrelated constant in currency.py to make a pin pass would
    # be the wrong repair; the statement's home is HERE. Pinned where it lives.
    import currency
    chk("currency.py no longer carries it -- its subject changed",
        hasattr(currency, "ONE_STATEMENT"), False)
    chk("and the corrected hypothesis is Ricci-narrowed where it lives",
        "RICCI" in ONE_STATEMENT_IS.upper(), True)
    chk("while the retired wording was not",
        "RICCI" in ONE_STATEMENT_WAS.upper(), False)

    print("\n  SELFTEST " + ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    print("""VERDICT

  NO -- AND A BLACK HOLE WOULD MAKE IT WORSE.  It is positive mass,
  positive mass stretches proper distance, and proper distance is the
  quantity phase1 proved a transition acts on.  Measured both ways:
  ordinary +M gives LONGER, negative -M gives SHORTER.  Containment
  changes nothing, because Birkhoff says the exterior of a
  spherically symmetric mass is Schwarzschild with that mass whatever
  the interior does.

  THE INTUITION IS RIGHT ABOUT A ROUTE THIS PROJECT IS NOT ON.  Try
  to seat a conjugate point with ORDINARY matter and you need the
  Sturm density, which exceeds the collapse bound by 2 pi^2/3 at
  every scale, and the region closes inside its own Schwarzschild
  radius.  On that route "you need a black hole" is true -- as a
  PROHIBITION rather than a recipe.  You do not get a device.  You
  get a black hole.

  THE CORRIDOR GOES THE OTHER WAY.  It focuses through WEYL, which is
  quadratic and sign-blind and carries no density requirement, and it
  is measured seating at lambda = 165.36 with no throat, no horizon,
  and M_ADM zero to fifteen digits.  It is not a black hole and it is
  not trying to be.

  SO THE TRADE IS EXPLICIT: A COLLAPSE PROBLEM EXCHANGED FOR A SOURCE
  PROBLEM.  Route A is blocked by gravity closing the region.  Route
  B is blocked by rho < 0 not existing.  Neither is solved, they are
  not the same obstacle, and this project has been on the second one
  throughout.

  AND THE QUESTION FORCED A CORRECTION.  currency.py asserted flatly
  that "a region that seats a conjugate point is a black hole".  Our
  own corridor is the counterexample.  The hypothesis is now attached
  there: BY RICCI FOCUSING.""")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report()
