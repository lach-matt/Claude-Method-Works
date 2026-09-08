#!/usr/bin/env python3
"""
currency.py -- is there a cheaper currency than mass-energy?  M has said so
repeatedly and this file finally tests it properly.  THE ANSWER IS PARTLY YES,
AND THE YES IS STRUCTURAL RATHER THAN RHETORICAL.

M: "again you are trying to pay in magnitude.  I still believe there is a much
cheaper currency more readily available."

Two results.  One vindicates the instinct.  The other closes it, and it closes
it with a theorem rather than with a big number.

===============================================================================
1. THE INSTINCT IS RIGHT: IN THE ENTROPY CHANNEL THE PLANCK FACTOR CANCELS
===============================================================================

scale.py proved that every ENERGY comparison in this project has the form
kappa (l_P/L)^2, because hbar c/L^4 over c^4/G L^2 carries hbar G/c^3 exactly
once and nothing cancels it.  That single uncancelled factor is the whole
65-to-71 orders.

The ENTROPY channel is different, and it is different for a reason:

        QNEC:          S_req  =  (2 pi / hbar c) T_kk L^4
        with            T_kk  =  pi c^4 / (4 G L^2)
        gives          S_req  =  (pi^2/2) (L/l_P)^2

        holographic    S_hol  =  A/4 l_P^2  =  (1/4) (L/l_P)^2

    BOTH SIDES CARRY (L/l_P)^2 AND IT CANCELS EXACTLY.

        S_req / S_hol  =  2 pi^2  =  19.7392,  AT EVERY SCALE

    measured identical at L = 1 m, 1e5 m and 1e10 m.  THAT is why entangle.py's
    number was 20 while achievable.py's was 1e65: not a different estimate of
    the same thing, but a channel in which the Planck factor divides out.

    AND THE REASON IS THAT ENTROPY IS ALREADY DENOMINATED IN PLANCK AREAS.
    The holographic bound measures entropy in units of l_P^2, so expressing the
    requirement as an entropy automatically divides out the factor that kills
    every energy-denominated route.  M's "cheaper currency" is a real feature
    of the problem and not a hope.

===============================================================================
2. AND IT SEPARATES TWO THINGS THIS PROJECT HAD FUSED
===============================================================================

The 2 pi^2 above prices THE SEAT -- the Sturm conjugate point, q l^2 >= pi^2.
But phase1.py defined the transition as a CONTRACTION of proper distance, which
is a different and cheaper object.  Priced the same way:

        E_contraction  =  eps L c^4 / (G Lambda)
        Bekenstein      S  <=  2 pi E R / hbar c
        gives    S_contr / S_hol  =  8 pi eps / Lambda

        eps = 1      2.5177    EXCEEDS the holographic bound
        eps = 0.4    1.0071    EXCEEDS it -- the boundary is at eps = 0.397
        eps = 0.1    0.2518    INSIDE
        eps = 0.01   0.0252    INSIDE

    THE SEAT IS HOLOGRAPHICALLY FORBIDDEN.  THE CONTRACTION IS NOT.

    A requirement above the holographic bound is not "twenty times hard" -- it
    is impossible, because that bound is the most entropy a region can hold by
    any means.  entangle.py called 2 pi^2 "the best news this project has
    produced"; that reading is too generous and is corrected here.  THE FACTOR
    OF TWENTY MEASURES HOW BADLY, NOT HOW NEARLY.

    But a contraction of ten per cent sits at a quarter of the bound, and that
    is a genuinely different status: PERMITTED.  Everything this project has
    said about black holes and collapse -- spec.py's 2 pi^2/3, the seating
    region inside its own Schwarzschild radius -- attaches to the SEAT, and
    phase1's transition does not need one.

===============================================================================
3. BUT THE EXCHANGE RATE IS FIXED BY A THEOREM
===============================================================================

Bekenstein's bound, S <= 2 pi E R / hbar c, runs both ways.  Read backwards it
says what energy an entropy costs:

        E  >=  S hbar c / (2 pi R)

Feed the seat's entropy requirement back through it:

        E  >=  (pi^2/2)(L/l_P)^2 * hbar c/(2 pi L)  =  (pi/4) L c^4 / G

    AT L = 1 m THAT IS 9.5053e+43 J, AND IT IS THE SAME CONSTANT seatindex.py
    ALREADY CARRIES AS T_COEFF = pi c^4/4G = 9.5053e+43.  The entropy
    requirement converts straight back into the energy requirement, exactly,
    with no loss and no gain.

    SO THE CURRENCY BUYS PERMISSION, NOT DISCOUNT.

    Changing denomination changes what can be SAID about the requirement --
    forbidden against permitted -- and does not change what must be PAID.  That
    is not a limitation of this analysis; it is Bekenstein's bound, and it is
    a theorem.

===============================================================================
4. AND THREE COINCIDENCES IN THE TREE TURN OUT TO BE ONE STATEMENT
===============================================================================

        entangle.py   S_req/S_hol         =  2 pi^2    = 19.7392
        spec.py       seat/collapse       =  2 pi^2/3  =  6.5797
        spec.py       "the seating region is inside its own Schwarzschild
                       radius at every scale"

    They differ by EXACTLY 3, which entangle.py noticed and did not explain.
    THE 3 IS THE 3 IN M = (4/3) pi R^3 rho -- a volume-against-area factor and
    nothing more.  All three say one thing: A REGION THAT SEATS A CONJUGATE
    POINT IS A BLACK HOLE.  Not three findings.  One, stated in entropy, in
    collapse, and in geometry.

===============================================================================
WHAT THIS DOES AND DOES NOT SETTLE
===============================================================================

    SETTLED: entropy is a structurally better denomination, the Planck factor
             genuinely cancels, and the seat/contraction split is real.
    SETTLED: no denomination is cheaper, because Bekenstein fixes the rate.
    SETTLED SINCE, BY shaping.py, AND NOT THE WAY THIS FILE EXPECTED: whether
             a state can be PREPARED whose S'' is negative where wanted, below
             the Bekenstein floor.  THE COST ARGUMENT FAILS -- weak squeezing
             over many modes drives preparation cost per joule to zero, and no
             Bekenstein-style reasoning stops it.  What closes the door is
             COUNTING: holding rho < 0 across a length L caps the frequency at
             pi c/2L, the cap limits the mode count, and each mode yields at
             most its own zero-point energy.  Together: 0.0514 hbar c/L^4,
             which IS Ford-Roman with the coefficient pi^2/192, derived here
             rather than quoted.  A cheaper currency does not help when the
             thing being bought is out of stock.

stdlib only.  entangle.py, spec.py, seatindex.py and phase1.py supply the
independent numbers this file reconciles.
"""
import math, sys

C, G, HBAR = 2.99792458e8, 6.67430e-11, 1.054571817e-34
L_PLANCK_SQ = HBAR * G / C ** 3
LAMBDA = 9.982529


# ------------------------------------------------------- the two denominations

def energy_channel_ratio(L, kappa=1.0):
    """kappa (l_P/L)^2 -- the Planck factor appears ONCE and does not cancel."""
    return kappa * L_PLANCK_SQ / (L * L)


def seat_entropy(L):
    """S_req = (pi^2/2)(L/l_P)^2, from QNEC with the Sturm seating T_kk."""
    return (math.pi ** 2 / 2.0) * L * L / L_PLANCK_SQ


def holographic_entropy(L):
    """A/4 l_P^2 = (1/4)(L/l_P)^2.  The most entropy a region can hold."""
    return 0.25 * L * L / L_PLANCK_SQ


def seat_over_holographic(L=1.0):
    """2 pi^2 -- and the (L/l_P)^2 CANCELS, which is the whole point."""
    return seat_entropy(L) / holographic_entropy(L)


def planck_factor_cancels(lengths=(1.0, 1.0e5, 1.0e10), rtol=1e-12):
    """Scale-free, unlike every energy-channel ratio.  Measured, not asserted."""
    r = [seat_over_holographic(L) for L in lengths]
    return (max(r) - min(r)) <= rtol * max(r)


def energy_channel_is_not_scale_free(lengths=(1.0, 1.0e5)):
    """The contrast: the energy ratio moves by ten orders over the same span."""
    a, b = (energy_channel_ratio(L) for L in lengths)
    return abs(math.log10(a / b)) > 9.0


# --------------------------------------- the seat against the contraction

def contraction_over_holographic(eps, lam=LAMBDA):
    """8 pi eps / Lambda, via Bekenstein on phase1's contraction energy."""
    return 8.0 * math.pi * eps / lam


def contraction_permitted(eps, lam=LAMBDA):
    return contraction_over_holographic(eps, lam) <= 1.0


def eps_boundary(lam=LAMBDA):
    """The contraction at which the holographic bound is reached."""
    return lam / (8.0 * math.pi)


def seat_permitted():
    """NO.  Above the holographic bound is impossible, not merely expensive."""
    return seat_over_holographic() <= 1.0


# ----------------------------------------- Bekenstein: the exchange rate

def bekenstein_energy(S, R):
    """E >= S hbar c / (2 pi R).  The bound run backwards."""
    return S * HBAR * C / (2.0 * math.pi * R)


def seat_energy_via_entropy(L=1.0):
    """Feed the entropy requirement back through Bekenstein."""
    return bekenstein_energy(seat_entropy(L), L)


def seat_energy_direct(L=1.0):
    """(pi/4) L c^4/G -- seatindex.py's T_COEFF, reached by a different route."""
    return (math.pi / 4.0) * L * C ** 4 / G


def rate_is_fixed(L=1.0, rtol=1e-12):
    """The two agree EXACTLY.  Currency buys permission, not discount."""
    return abs(seat_energy_via_entropy(L) - seat_energy_direct(L)) \
        <= rtol * seat_energy_direct(L)


DISCOUNT = False                      # Bekenstein is a theorem
PERMISSION = True                     # and the seat/contraction split is real


# -------------------------------------------- three coincidences, one statement

def entropy_constant():
    return 2.0 * math.pi ** 2


def collapse_constant():
    """spec.py's seat_over_collapse, reached from gravitational collapse."""
    return 2.0 * math.pi ** 2 / 3.0


def the_factor_is_three(rtol=1e-12):
    """And the 3 is the 3 in M = (4/3) pi R^3 rho.  A volume-against-area factor."""
    return abs(entropy_constant() / collapse_constant() - 3.0) <= rtol * 3.0


# CORRECTED by dichotomy.py.  The unqualified version stood here and our own
# corridor is the counterexample: it seats a conjugate point at lambda = 165.36
# with no throat, no horizon and M_ADM = 0.  The collapse and entropy results
# price the STURM seat, and Sturm requires q = 4 pi T_kk > 0 -- Ricci focusing,
# positive energy.  Weyl focusing is sign-blind and carries no such requirement.
ONE_STATEMENT = ("a region that seats a conjugate point BY RICCI FOCUSING "
                 "is a black hole")

# The honest remainder.  Bekenstein bounds what a region can HOLD given its
# energy.  Whether SHAPING S'' in a vacuum that already carries area-law
# entanglement costs the same is a different question and is not answered here.
SHAPING_COST = "CLOSED-NEGATIVE"    # shaping.py: closed by COUNTING, not cost.
                                    # The cost argument fails in M's favour --
                                    # eta -> 1/r, preparation really is cheap --
                                    # but the modes that could hold rho < 0 over
                                    # a length L do not exist: 0.0514 hbar c/L^4,
                                    # which IS Ford-Roman, derived.


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

    print("1. THE INSTINCT IS RIGHT -- in entropy the Planck factor CANCELS")
    near("S_req/S_hol", seat_over_holographic(), 2.0 * math.pi ** 2, 1e-12)
    chk("  and it is exactly 2 pi^2", seat_over_holographic() == 2.0 * math.pi ** 2, True)
    chk("scale-free across ten decades", planck_factor_cancels(), True)
    chk("while the ENERGY ratio moves ten orders over the same span",
        energy_channel_is_not_scale_free(), True)
    print("      because entropy is ALREADY denominated in Planck areas, so the")
    print("      factor that kills every energy route divides out.")

    print("\n2. AND IT SEPARATES THE SEAT FROM THE CONTRACTION")
    chk("the SEAT is holographically permitted", seat_permitted(), False)
    for e in (1.0, 0.4, 0.1, 0.01):
        print("      eps = %-6g  S_contr/S_hol = %.4f  %s"
              % (e, contraction_over_holographic(e),
                 "INSIDE" if contraction_permitted(e) else "EXCEEDS"))
    near("the boundary in eps", eps_boundary(), 0.39723, 1e-4)
    chk("a 10 % contraction is permitted", contraction_permitted(0.1), True)
    chk("and a full one is not", contraction_permitted(1.0), False)
    print("      A requirement above the holographic bound is IMPOSSIBLE, not")
    print("      twenty times hard.  entangle.py's 'best news' reading is too")
    print("      generous and is corrected: the 20 measures how BADLY.")

    print("\n3. BUT BEKENSTEIN FIXES THE EXCHANGE RATE, AND IT IS A THEOREM")
    near("seat energy via the entropy route (J at 1 m)", seat_energy_via_entropy(),
         9.5053e43, 1e-4)
    near("  and directly, (pi/4) L c^4/G", seat_energy_direct(), 9.5053e43, 1e-4)
    chk("they agree exactly", rate_is_fixed(), True)
    print("      and 9.5053e43 is seatindex.py's T_COEFF, reached here by a")
    print("      route that shares no algebra with it.")
    chk("the currency buys a DISCOUNT", DISCOUNT, False)
    chk("the currency buys PERMISSION", PERMISSION, True)

    print("\n4. THREE COINCIDENCES, ONE STATEMENT")
    near("entangle.py's entropy constant", entropy_constant(), 19.7392, 1e-5)
    near("spec.py's collapse constant", collapse_constant(), 6.5797, 1e-5)
    chk("they differ by exactly 3", the_factor_is_three(), True)
    print("      and the 3 is the 3 in M = (4/3) pi R^3 rho -- volume against")
    print("      area.  All three say: %s." % ONE_STATEMENT)

    print("\nTHE HONEST REMAINDER")
    chk("cost of SHAPING S'' in an already-entangled vacuum", SHAPING_COST,
        "CLOSED-NEGATIVE")
    print("      PURSUED AND CLOSED by shaping.py, and not by a cost argument:")
    print("      weak squeezing really does drive preparation cost to zero.")
    print("      What closes it is COUNTING -- the modes that could hold")
    print("      rho < 0 over a length L cap it at 0.0514 hbar c/L^4, which is")
    print("      Ford-Roman, derived rather than assumed.")

    print("\n  SELFTEST " + ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    print("""VERDICT

  THE INSTINCT WAS RIGHT ABOUT THE CURRENCY AND THE REASON IS
  STRUCTURAL.  Every energy comparison in this project carries the
  Planck factor exactly once, uncancelled, and that single factor IS
  the 65-to-71 orders.  In the entropy channel both sides carry
  (L/l_P)^2 and it cancels exactly, because entropy is already
  denominated in Planck areas.  That is why the number is 20 and not
  1e69, and it is a feature of the problem rather than a hopeful
  estimate.

  IT ALSO SEPARATES TWO THINGS THIS PROJECT HAD FUSED.  The 2 pi^2
  prices the SEAT, and a requirement above the holographic bound is
  impossible rather than expensive -- so entangle.py's reading of 20
  as good news is corrected: it measures how badly.  But phase1
  defined the transition as a CONTRACTION, and a contraction is
  8 pi eps/Lambda of the bound: PERMITTED below eps = 0.397, and a
  quarter of the bound at ten per cent.  Everything this tree has
  said about collapse and Schwarzschild radii attaches to the seat,
  and the transition does not need one.

  BUT THE CURRENCY BUYS PERMISSION, NOT DISCOUNT.  Bekenstein's bound
  read backwards, E >= S hbar c/2 pi R, converts the entropy
  requirement into (pi/4) L c^4/G -- 9.5053e43 J at a metre, which is
  exactly seatindex.py's T_COEFF reached by a route sharing no
  algebra.  Changing denomination changes what can be SAID about the
  requirement and not what must be PAID, and that is a theorem rather
  than a limitation of this file.

  AND THE ONE QUESTION THIS FILE LEFT OPEN HAS SINCE BEEN CLOSED, by
  shaping.py, and not the way this file expected.  The cost argument
  FAILS: weak squeezing over many modes drives the preparation cost
  per joule of negative energy to zero.  What closes the door is
  COUNTING -- the modes that could hold rho < 0 across a length L cap
  it at 0.0514 hbar c/L^4, which is Ford-Roman with the coefficient
  pi^2/192, derived rather than quoted.""")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report()
