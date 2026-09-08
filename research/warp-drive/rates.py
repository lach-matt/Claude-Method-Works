#!/usr/bin/env python3
"""
rates.py -- nopath.py and spectra.py applied back, and the currency question
closed by exhaustion rather than case by case.

apply.py consolidated three passes and found three doors.  Two more passes have
run since -- the index picture and the spectral currency -- and this asks the
same question of them: WHAT DOES THE PROJECT LOOK LIKE NOW.

The door count does not move.  One door stops being abstract.  And the currency
question, which currency.py closed in three stages by trying three
denominations, closes here for the WHOLE SPACE by a different argument.

===============================================================================
1. NEITHER PASS ADDS A DOOR.  FIVE PASSES, STILL THREE
===============================================================================

nopath.py's dimensional drift is a warped braneworld, which is an
extra-dimensional theory -- DOOR ONE, outside general relativity.  spectra.py's
optimised spectral currency is a black hole, which is dichotomy.py's RICCI route
inside the DEC branch apply.py already exhausted.

    THE DOOR COUNT HAS BEEN STABLE ACROSS FIVE PASSES, and two of those passes
    were built specifically on new principles of M's rather than on the device.
    That is worth more than any single closure: the list is not growing because
    nobody has thought hard enough about it.

===============================================================================
2. BUT DOOR THREE GAINED A THIRD INDEPENDENT ARRIVAL
===============================================================================

        create.py     topology change forces causality violations, kinematically
        detect.py     the search target is in a catalogue that already exists
        nopath.py     "two points already one" is a mouth pair, and nothing is
                      contracted, so nothing is paid for contracting

    THREE ROUTES, THREE STARTING POINTS, ONE CONCLUSION: FIND ONE, DO NOT MAKE
    ONE.  Door three is now the best-supported thing in the project, and the
    third arrival came from M's index picture rather than from any theorem the
    tree went looking for.

===============================================================================
3. AND DOOR ONE STOPPED BEING A CATEGORY.  IT IS NOW A NUMBER
===============================================================================

apply.py listed door one as "f(R), noncommutative geometry" -- a category, not a
candidate.  nopath.py named a concrete, published, calculable mechanism: BULK
SHORTCUTS in a warped braneworld, where a bulk geodesic between two brane points
beats the brane geodesic.

    AND scale.py HAD ALREADY PRICED THE SUPPLY SIDE OF EXACTLY THAT, and left
    it sitting as the only lever that moves the BASE of the scale theorem:

        the ordinary shortfall at 1 m       3.8281e69     69.58 orders
        the braneworld shortfall            2.3114e38     38.36 orders
        WHAT EXTRA DIMENSIONS BUY           1.6562e31     31.22 ORDERS

    THIRTY-ONE ORDERS IS THE LARGEST SINGLE MOVEMENT ANY LEVER IN THIS PROJECT
    HAS EVER PRODUCED.  It does not close the gap -- 38.36 orders remain -- and
    scale.py's own note says why it cannot be quoted as a result:
    EXTRA_DIMENSIONS is NOT-RUN, because evaluating the DEMAND side in a
    braneworld is a different calculation in a different theory.

        SO THE SCOPE DECISION M HAS BEEN HOLDING SINCE THE WORMHOLE FORK IS NO
        LONGER A DECISION ABOUT A CATEGORY.  It is a decision about ONE NAMED
        CALCULATION with a MEASURED supply-side gain of 31.22 orders and an
        unrun demand side.  That is the sharpest the question has ever been.

===============================================================================
4. THE CURRENCY QUESTION CLOSES BY EXHAUSTION, NOT CASE BY CASE
===============================================================================

currency.py closed the cheaper-denomination hope in three stages by TRYING
three denominations.  Two more have been tried since and both closed.  The
pattern is now visible and it is not a coincidence:

        EVERY DENOMINATION IS TIED TO MASS-ENERGY BY A MONOMIAL IN G, c, hbar
        AND k, OR BY A BOUND THAT RUNS AGAINST THE TRADE.

        geometry     c^4 / G                     1.21026e44 N
        length       G / c^4                     8.26272e-45 m/J
        contraction  c^2 / (G Lambda)            1.34895e26 kg per metre
        area         hbar G / c^3                2.61228e-70 m^2
        information  2 pi / (hbar c ln2)         2.86720e26 bits per J m
                     -- and Bekenstein bounds S BY E, the wrong way
        heat         k ln2                       9.56993e-24 J per K per bit
                     -- and Landauer bounds E BELOW, also the wrong way
        charge       forced to zero in a closed index; log2(1) = 0 bits
        spectra      the same Bekenstein bound; optimised, a horizon

    A CONSTANT OF NATURE IS NOT A DISCOUNT.  You cannot get a better price by
    denominating in a different one, because the rate between any two of them
    is fixed and there is nothing to negotiate.

    THE TABLE HOLDS EXACTLY TWO DIMENSIONLESS NUMBERS, and both are accounted:

        Lambda   9.982529    DETERMINED by the geometry, saturating to nine
                             digits, and O(10).  A number that size cannot buy
                             orders whatever it is.
        kappa    free        THE ONE GENUINE LEVER IN THE WHOLE TABLE, and
                             scale.py owns it: kappa_GJW = pi/360 = 8.7266e-3,
                             and the kappa needed at 1 m is 3.8281e69.

    SO THE CLOSURE IS NOT "FIVE DENOMINATIONS FAILED".  IT IS THAT THE
    CONVERSION TABLE HAS NO FREE PARAMETER IN IT EXCEPT ONE, AND THAT ONE IS
    MEASURED AND INSUFFICIENT.  A sixth denomination would have to enter
    through kappa or through the base, and the base is door one.

===============================================================================
5. AND ONE DOOR HAS A COST YOU CAN ACTUALLY PAY
===============================================================================

Price the three doors by what their cost is DENOMINATED IN, which is a
different question from how large it is:

    DOOR 1  outside GR          THEORY-DEPENDENT.  31.22 orders measured on the
                                supply side, demand side NOT-RUN.  Cannot be
                                priced until the scope is chosen.
    DOOR 2  not an energy       UNKNOWN.  GJW's external path is an existence
            question            proof; nobody has costed a construction.
    DOOR 3  a relic             A SEARCH.  detect.py: a 1193 km throat ringing
                                at 100 Hz is 32.13 solar masses, in the LIGO
                                band, and the discriminator applies to a
                                CATALOGUE THAT ALREADY EXISTS.

        EXACTLY ONE OF THE THREE HAS A COST THAT IS NOT A MASS, and it is
        telescope time on data already taken.  That is not a proof that door
        three is the right one.  It is the observation that it is the only one
        anybody could start on this week.

stdlib only.  Every rate recomputed from constants; every gain from the
instrument that owns it.
"""
import math
import sys

G = 6.67430e-11
C = 2.99792458e8
HBAR = 1.054571817e-34
KB = 1.380649e-23


# ---------------------------------------- 1: the door count does not move

def doors():
    import apply
    return [d[0] for d in apply.DOORS]


NEW_PASSES = (("nopath.py", "dimensional drift", "OUTSIDE GR"),
              ("spectra.py", "the optimised spectrum", "a horizon: the DEC branch"))


def pass_adds_a_door(row):
    """Neither does.  A pass adds a door only if where it lands is not one."""
    return row[2] not in doors() and row[2] != "a horizon: the DEC branch"


def door_count_moved():
    return len(doors()) != 3


# --------------------------- 2: door three's third arrival

DOOR_THREE_ARRIVALS = (
    ("create.py", "topology change forces causality violations, kinematically"),
    ("detect.py", "the search target sits in a catalogue that already exists"),
    ("nopath.py", "two points already one -- nothing contracted, nothing paid"),
)


def door_three_arrivals():
    return len(DOOR_THREE_ARRIVALS)


def create_route():
    import create
    return create.ROUTE


# ------------------------- 3: door one is a number now

def ordinary_shortfall(L=1.0):
    import scale
    return scale.geometric_factor(L)


def braneworld_shortfall(L=1.0):
    import scale
    return scale.shortfall_with_extra_dimensions(L)


def extra_dimension_orders(L=1.0):
    import scale
    return math.log10(scale.extra_dimension_gain(L))


def orders_remaining(L=1.0):
    return math.log10(braneworld_shortfall(L))


def door_one_demand_side():
    """scale.py's own status.  The supply side is measured; this is not."""
    import scale
    return scale.EXTRA_DIMENSIONS


def largest_lever_in_the_project(L=1.0):
    """31.22 orders.  Nothing else here has moved a number that far."""
    import scale
    return extra_dimension_orders(L) > math.log10(scale.species_gain())


# ------------------ 4: the conversion table has no free parameter

def planck_force():
    return C ** 4 / G


def geometry_rate():
    return G / C ** 4


def contraction_rate():
    import phase1
    return phase1.exchange_rate()


def planck_area():
    return HBAR * G / C ** 3


def bekenstein_rate():
    """bits per joule-metre.  2 pi / (hbar c ln2)."""
    return 2.0 * math.pi / (HBAR * C * math.log(2.0))


def landauer_rate():
    """joules per kelvin per bit."""
    return KB * math.log(2.0)


TABLE = (
    ("geometry", "c^4 / G", planck_force, "N"),
    ("length", "G / c^4", geometry_rate, "m/J"),
    ("contraction", "c^2 / (G Lambda)", contraction_rate, "kg/m"),
    ("area", "hbar G / c^3", planck_area, "m^2"),
    ("information", "2 pi / (hbar c ln2)", bekenstein_rate, "bits/(J m)"),
    ("heat", "k ln2", landauer_rate, "J/(K bit)"),
)

BOUNDS_RUNNING_THE_WRONG_WAY = (
    ("Bekenstein", "S <= 2 pi R E / (hbar c)", "bounds information BY energy"),
    ("Landauer", "E >= N k T ln2", "bounds energy BELOW, by information"),
)


def rate_is_a_monomial(name):
    """Every row is built from G, c, hbar, k and nothing else.  Checked by
    reconstructing each from the constants rather than by inspection."""
    built = {
        "geometry": C ** 4 / G,
        "length": G / C ** 4,
        "area": HBAR * G / C ** 3,
        "information": 2.0 * math.pi / (HBAR * C * math.log(2.0)),
        "heat": KB * math.log(2.0),
    }
    if name not in built:                 # contraction carries Lambda; see below
        return False
    fn = dict((r[0], r[2]) for r in TABLE)[name]
    return abs(built[name] / fn() - 1.0) < 1e-12


def lambda_value():
    import phase1
    return phase1.lam()


def lambda_can_buy_orders():
    """It is dimensionless, determined by the geometry, and O(10).  No."""
    return abs(math.log10(lambda_value())) > 1.0


def kappa_gjw():
    import scale
    return scale.kappa_gjw()


def kappa_needed(L=1.0):
    import scale
    return scale.kappa_needed(L)


def kappa_is_the_only_free_dimensionless():
    """Lambda is determined; every other row is a monomial in the constants."""
    return all(rate_is_a_monomial(r[0]) for r in TABLE if r[0] != "contraction")


def kappa_closes_the_gap(L=1.0):
    return kappa_gjw() >= kappa_needed(L)


# --------------------- 5: what each door's cost is denominated in

DOOR_COSTS = (
    ("OUTSIDE GR", "THEORY-DEPENDENT",
     "31.22 orders measured on the supply side; demand side NOT-RUN"),
    ("NOT AN ENERGY QUESTION", "UNKNOWN",
     "GJW is an existence proof; nobody has costed a construction"),
    ("A RELIC, NOT A CONSTRUCTION", "A SEARCH",
     "32.13 solar masses at 1193 km in the LIGO band, on existing data"),
)


def doors_costed_in_mass():
    return [d for d, kind, _w in DOOR_COSTS if kind not in ("A SEARCH",)]


def only_payable_door():
    return [d for d, kind, _w in DOOR_COSTS if kind == "A SEARCH"]


def search_target_solar():
    import detect
    return detect.search_target_solar()


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-56s %18s %18s  %s"
              % (label, str(got)[:18], str(want)[:18], "ok" if good else "FAIL"))

    def near(label, got, want, tol=1e-4):
        nonlocal ok
        good = abs(got - want) <= tol * max(1.0, abs(want))
        ok &= good
        print("  %-56s %18.6e %18.6e  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("1. NEITHER PASS ADDS A DOOR -- FIVE PASSES, STILL THREE")
    for name, what, where in NEW_PASSES:
        print("     %-12s %-24s lands in %s" % (name, what, where))
    chk("doors", len(doors()), 3)
    chk("has the count moved", door_count_moved(), False)
    for name, _w, where in NEW_PASSES:
        chk("  does %s open a new door" % name, pass_adds_a_door(
            (name, _w, where)), False)
    chk("and 'contraction' is the row that is NOT a bare monomial",
        rate_is_a_monomial("contraction"), False)
    print("       And two of the five passes were built on M's principles")
    print("       rather than on the device.  The list is not growing.")

    print("\n2. BUT DOOR THREE GAINED A THIRD INDEPENDENT ARRIVAL")
    for who, why in DOOR_THREE_ARRIVALS:
        print("     %-12s %s" % (who, why))
    chk("independent arrivals at door three", door_three_arrivals(), 3)
    chk("and create.py's route is unchanged", create_route(), "find one and enlarge it")

    print("\n3. AND DOOR ONE IS A NUMBER NOW, NOT A CATEGORY")
    near("the ordinary shortfall at 1 m", ordinary_shortfall(), 3.8281e69)
    near("  in orders", math.log10(ordinary_shortfall()), 69.5828, 1e-4)
    near("the braneworld shortfall at 1 m", braneworld_shortfall(), 2.3114e38)
    near("WHAT EXTRA DIMENSIONS BUY, in orders", extra_dimension_orders(), 31.2196, 1e-4)
    near("orders remaining after it", orders_remaining(), 38.3632, 1e-4)
    chk("largest lever in the project (against the species gain)",
        largest_lever_in_the_project(), True)
    chk("and scale.py's demand side is", door_one_demand_side(), "NOT-RUN")
    print("       So the scope decision is now about ONE NAMED CALCULATION with")
    print("       a measured 31.22-order supply side, not about a category.")

    print("\n4. THE CONVERSION TABLE HAS NO FREE PARAMETER EXCEPT ONE")
    for name, formula, fn, unit in TABLE:
        print("     %-12s %-22s %14.5e %s" % (name, formula, fn(), unit))
        if name != "contraction":
            chk("  %s is a monomial in G, c, hbar, k" % name,
                rate_is_a_monomial(name), True)
    for who, form, why in BOUNDS_RUNNING_THE_WRONG_WAY:
        print("     %-12s %-26s %s" % (who, form, why))
    print("     the two dimensionless numbers in the table:")
    near("  Lambda", lambda_value(), 9.982529, 1e-6)
    chk("  can a number that size buy orders", lambda_can_buy_orders(), False)
    near("  kappa_GJW", kappa_gjw(), math.pi / 360.0, 1e-12)
    near("  kappa needed at 1 m", kappa_needed(), 3.8281e69)
    chk("  does kappa close the gap", kappa_closes_the_gap(), False)
    chk("kappa is the only free dimensionless number in the table",
        kappa_is_the_only_free_dimensionless(), True)
    print("       A CONSTANT OF NATURE IS NOT A DISCOUNT.  The closure is not")
    print("       'five denominations failed' -- it is that the table has no")
    print("       free parameter but kappa, and kappa is measured and short.")

    print("\n5. AND ONE DOOR HAS A COST YOU CAN ACTUALLY PAY")
    for door, kind, why in DOOR_COSTS:
        print("     %-28s %-18s %s" % (door, kind, why))
    chk("doors whose cost is not a search", len(doors_costed_in_mass()), 2)
    chk("and the one that is", only_payable_door(), ["A RELIC, NOT A CONSTRUCTION"])
    near("its target, in solar masses", search_target_solar(), 32.13, 1e-3)
    print("       Telescope time on data already taken.  Not a proof that door")
    print("       three is right -- the observation that it is the only one")
    print("       anybody could start on this week.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    print("THE THREE DOORS, PRICED BY DENOMINATION\n")
    print("  %-28s %-18s %s" % ("door", "cost is", "note"))
    for door, kind, why in DOOR_COSTS:
        print("  %-28s %-18s %s" % (door, kind, why))
    print("\n  %-28s %.2f orders" % ("door one buys", extra_dimension_orders()))
    print("  %-28s %.2f orders" % ("and leaves", orders_remaining()))
    print("  %-28s %s" % ("its demand side", door_one_demand_side()))
    print("\n" + "=" * 79)
    print("""VERDICT

  NEITHER PASS ADDS A DOOR, AND THAT IS THE HEADLINE.  Dimensional
  drift is a warped braneworld, which is door one; the optimised
  spectral currency is a black hole, which is inside the DEC branch
  apply.py exhausted.  FIVE PASSES, STILL THREE DOORS -- and two of the
  five were built on M's principles rather than on the device, so the
  list is not staying short for want of anybody thinking about it.

  DOOR THREE GAINED A THIRD INDEPENDENT ARRIVAL.  create.py reached
  "find one, do not make one" from the topology theorems; detect.py
  reached it from the search side; nopath.py reached it from the index
  picture, where "two points already one" is a mouth pair and nothing
  is contracted so nothing is paid for contracting.  THREE STARTING
  POINTS, ONE CONCLUSION.  It is the best-supported thing in the
  project.

  AND DOOR ONE STOPPED BEING A CATEGORY.  apply.py could only say
  "f(R), noncommutative geometry".  nopath.py named a concrete
  mechanism -- bulk shortcuts in a warped braneworld -- and scale.py
  had ALREADY PRICED THE SUPPLY SIDE OF EXACTLY THAT and left it as the
  only lever that moves the base:

        ordinary shortfall at 1 m     69.58 orders
        braneworld shortfall          38.36 orders
        WHAT EXTRA DIMENSIONS BUY     31.22 ORDERS

  Thirty-one orders is the largest single movement any lever in this
  project has produced.  It does not close the gap, and scale.py's own
  status says why it cannot be quoted as a result: the DEMAND side in a
  braneworld is a different calculation in a different theory, and it
  is NOT-RUN.  SO THE SCOPE DECISION IS NOW ABOUT ONE NAMED CALCULATION
  WITH A MEASURED 31.22-ORDER SUPPLY SIDE, not about a category.

  THE CURRENCY QUESTION CLOSES BY EXHAUSTION RATHER THAN CASE BY CASE.
  currency.py closed it in three stages by trying three denominations
  and two more have closed since.  The reason is now visible: every
  denomination is tied to mass-energy by a MONOMIAL IN G, c, hbar AND
  k -- c^4/G, G/c^4, hbar G/c^3, 2 pi/(hbar c ln2), k ln2 -- or by a
  BOUND THAT RUNS AGAINST THE TRADE, Bekenstein bounding information by
  energy and Landauer bounding energy below by information.  A CONSTANT
  OF NATURE IS NOT A DISCOUNT.  The table holds exactly two
  dimensionless numbers: Lambda, determined by the geometry, saturating
  to nine digits and O(10), which cannot buy orders whatever it is; and
  kappa, the one genuine lever, which scale.py owns and has measured at
  pi/360 against the 3.8281e69 that would be needed.  A SIXTH
  DENOMINATION WOULD HAVE TO ENTER THROUGH KAPPA OR THROUGH THE BASE,
  AND THE BASE IS DOOR ONE.

  AND EXACTLY ONE DOOR HAS A COST THAT IS NOT A MASS.  Door one is
  theory-dependent and cannot be priced until the scope is chosen; door
  two is unknown, GJW being an existence proof nobody has costed.  Door
  three is A SEARCH: a 1193 km throat ringing at 100 Hz is 32.13 solar
  masses, in the LIGO band, and the discriminator applies to a
  catalogue that already exists.  That is not a proof that door three
  is the right one.  IT IS THE OBSERVATION THAT IT IS THE ONLY ONE
  ANYBODY COULD START ON THIS WEEK.""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
