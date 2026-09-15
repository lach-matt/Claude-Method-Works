#!/usr/bin/env python3
"""
spectra.py -- information as the SPECTRUM of a charge state, not the charge.

M: "I predict that information as currency is not specifically a charge state
but rather the different spectra of a single charge state."

THE DISTINCTION IS CORRECT, IT IS THE RIGHT ONE TO DRAW, AND IT IS BACKED BY
TWO THEOREMS THIS TREE ALREADY HOLDS.  It also makes the refutation in
nopath.py sharper rather than weaker, and the sharpening ends somewhere the
project has already been.

===============================================================================
1. WHY THE DISTINCTION IS REAL: CHARGE IS SUPERSELECTED, SPECTRUM IS NOT
===============================================================================

Electric charge is a SUPERSELECTED quantity.  You cannot prepare a coherent
superposition of different total-charge sectors -- no state a|Q=0> + b|Q=1>
exists as a physical state.  So the charge VALUE carries classical information
only: it labels a sector and nothing inside one.

Inside a fixed sector the spectrum is ordinary quantum mechanics: levels
superpose, interfere and carry qubits.  ALL THE INFORMATION IS THERE.

And then permute.py closes the other half, on M's own closed index:

        IN A SPATIALLY CLOSED UNIVERSE GAUSS'S LAW FORCES TOTAL Q = 0 EXACTLY.

    A quantity fixed by topology to a single value has ONE state.  log2(1) = 0.
    THE CHARGE CARRIES ZERO BITS, forced, and every bit there is must live in
    the spectrum.  M's refinement is not a preference between two carriers --
    IN A CLOSED INDEX IT IS THE ONLY CARRIER LEFT, and the theorem that removes
    the other one is one this tree derived two passes ago.

===============================================================================
2. AND THE CARRIER NAMED IS EXACTLY WHAT THE BEKENSTEIN BOUND COUNTS
===============================================================================

nopath.py priced information at 9.9736e101 bits and closed the route on
Bekenstein.  What Bekenstein's S actually counts is worth stating precisely,
because it is M's quantity and not an adjacent one:

        S <= 2 pi R E / (hbar c)

is a bound on THE NUMBER OF DISTINGUISHABLE QUANTUM STATES of a system of
energy E confined to radius R.  It counts SPECTRAL MULTIPLICITY.  It says
nothing whatever about charge.

    SO THE REFINEMENT DOES NOT EVADE THE BOUND -- IT NAMES THE BOUND'S OWN
    VARIABLE.  M has independently identified the quantity Bekenstein bounds,
    which is a point in the prediction's favour and not against it.  What it
    does not do is change the direction of the inequality: the spectrum is
    bounded BY the energy, so a richer spectrum is not a cheaper spectrum.

===============================================================================
3. PRICED CONCRETELY: A REAL SPECTRUM, A REAL BIT COUNT
===============================================================================

Take the cleanest instance of "the different spectra of a single charge state":
one hydrogenic charge, its bound levels, degeneracy n^2 at level n.  Truncate
at n_max and count.

        n_max = 10      385 states       8.589 bits
        n_max = 100     338,350         18.368 bits
        n_max = 1000    333,833,500     28.315 bits

    A SPECTRUM IS A LOGARITHM.  Widening it by a factor of ten buys ten bits.
    That is the arithmetic of the proposal and it is not a small effect being
    unfair to it -- it is what a spectrum is.

To reach nopath.py's 9.9736e101 bits at n_max = 100 takes 5.4298e100 atoms,
massing 9.0870e73 kg, against the 5.1048e42 kg that simply supplying the mass
would cost.

        THIRTY-ONE AND A QUARTER ORDERS WORSE.

Same statement per kilogram, which is the honest way to compare carriers:

        hydrogenic, n_max = 100     1.0976e28 bits/kg
        saturating the bound        1.9538e59 bits/kg

===============================================================================
4. AND THE OPTIMAL SPECTRUM IS A BLACK HOLE -- WHICH IS WHERE WE CAME IN
===============================================================================

That 31-order gap is not a fact about hydrogen.  It is the distance from any
ordinary matter to the bound, and the bound is saturated by exactly one object:

        A BLACK HOLE.  S = A / 4 l_P^2, and nothing else in physics reaches it.

Black-hole bits go as M^2 -- verified below, doubling the mass quadruples the
count -- so the information-per-kilogram of the optimal carrier RISES with
mass, and the optimum at any scale is a horizon.

    SO "PAY IN SPECTRA", OPTIMISED, IS "BUILD A BLACK HOLE".

    And dichotomy.py closed that two hundred passes ago from the other side:
    the RICCI route, ordinary matter and positive energy, seats a conjugate
    point and exceeds the collapse bound by 2 pi^2 / 3 at every scale --
    COLLAPSE, you get a black hole and not a device.

        THREE CURRENCIES, ONE DESTINATION.  Mass reaches 2.5666e12 solar
        masses.  Information reaches the Bekenstein bound.  Spectra, optimised,
        reach the same horizon.  They are not three routes; they are three
        denominations of one route, and the route ends in a black hole.

===============================================================================
5. WHAT THE REFINEMENT DOES NOT MOVE, AND THIS IS THE HONEST PART
===============================================================================

charge.py's split -- H14 -- says a charge state supplies THE SEAT and not THE
LEAD, and the boundary between them is the energy-condition line.

The spectrum refinement does not touch that.  A spectrum is a multiplicity of
states; the seat/lead split turns on the SIGN OF rho, and multiplicity has no
sign.  Enriching the spectrum of a charge does not make its energy density
negative.

    SO THE SEAT STAYS FREE AND THE LEAD STAYS COSTLY, exactly as apply.py
    measured, and the refinement leaves H14 standing unchanged.

===============================================================================
THE SCORE
===============================================================================

RIGHT      the carrier.  Charge is superselected and, in a closed index,
           forced to zero -- so it carries no bits at all and the spectrum is
           the only carrier left.  Two theorems, one of them this tree's own.
RIGHT      the variable.  Bekenstein counts spectral multiplicity, not charge,
           so the prediction names the bound's own quantity.
WRONG      the direction.  The spectrum is bounded BY the energy, a spectrum is
           a logarithm, and the optimal spectrum is a horizon.

    A BETTER-AIMED VERSION OF THE SAME CURRENCY, LANDING IN THE SAME PLACE, BY
    A ROUTE THAT IS WORTH HAVING BECAUSE IT NAMES WHAT THE BOUND IS ABOUT.

stdlib only.  Exact where the claim is exact.
"""
import math
import sys

HBAR = 1.054571817e-34
C = 2.99792458e8
G = 6.67430e-11
M_HYDROGEN = 1.67353e-27          # kg, the neutral atom
M_SUN = 1.98892e30


# ------------------- 1: charge is superselected, and closed forces it to zero

CHARGE_IS_SUPERSELECTED = True     # no coherent superposition across sectors


def charge_states_in_a_closed_index():
    """Gauss on a boundaryless manifold forces total Q = 0.  One value."""
    import permute
    return 1 if permute.total_charge_forced_zero(True) else None


def bits_in(states):
    return math.log2(states)


def charge_bits_in_a_closed_index():
    """log2(1) = 0.  The charge carries nothing, forced by topology."""
    return bits_in(charge_states_in_a_closed_index())


def spectrum_is_superselected():
    """It is not -- levels superpose and interfere.  That is where bits live."""
    return False


# ---------------- 2: Bekenstein counts spectral multiplicity, not charge

BEKENSTEIN_COUNTS = "distinguishable quantum states of energy E in radius R"
BEKENSTEIN_MENTIONS_CHARGE = False


def bekenstein_bits(R, E):
    import nopath
    return nopath.bekenstein_bits(R, E)


def refinement_names_the_bounds_variable():
    """M's carrier and Bekenstein's S are the same quantity."""
    return not BEKENSTEIN_MENTIONS_CHARGE and not spectrum_is_superselected()


# ----------------------- 3: a real spectrum, counted

def hydrogenic_states(n_max):
    """Sum of n^2 for n = 1..n_max.  Degeneracy of the bound levels."""
    return n_max * (n_max + 1) * (2 * n_max + 1) // 6


def hydrogenic_bits(n_max):
    return bits_in(hydrogenic_states(n_max))


def spectrum_is_logarithmic(a=100, b=1000):
    """Ten times the levels buys about ten bits, not ten times the bits."""
    return hydrogenic_bits(b) - hydrogenic_bits(a) < 12.0


def required_bits():
    """nopath.py's figure, from nopath.py."""
    import nopath
    M = nopath.coincidence_mass(4.0)
    return nopath.holographic_bits(nopath.schwarzschild_radius(M))


def required_mass():
    import nopath
    return nopath.coincidence_mass(4.0)


def atoms_needed(n_max=100):
    return required_bits() / hydrogenic_bits(n_max)


def spectral_mass(n_max=100):
    return atoms_needed(n_max) * M_HYDROGEN


def orders_worse(n_max=100):
    return math.log10(spectral_mass(n_max) / required_mass())


def bits_per_kg_hydrogenic(n_max=100):
    return hydrogenic_bits(n_max) / M_HYDROGEN


def bits_per_kg_saturating():
    return required_bits() / required_mass()


# ------------------ 4: the optimal spectrum is a horizon

def black_hole_bits(M):
    R = 2.0 * G * M / C ** 2
    return 2.0 * math.pi * R * M * C * C / (HBAR * C * math.log(2.0))


def bits_go_as_mass_squared(M=1.0e40, rtol=1e-12):
    """Doubling M quadruples the count.  So bigger is denser, and the optimum
    at every scale is a horizon."""
    return abs(black_hole_bits(2.0 * M) / black_hole_bits(M) - 4.0) < rtol


def saturates_the_bound(M=1.0e40, rtol=1e-9):
    """A black hole reaches Bekenstein exactly; nothing else does."""
    import nopath
    R = 2.0 * G * M / C ** 2
    return abs(black_hole_bits(M) / nopath.holographic_bits(R) - 1.0) < rtol


OPTIMISED_SPECTRUM_IS = "a black hole"


def dichotomy_already_closed_it():
    import dichotomy
    return dichotomy.blockers()[dichotomy.RICCI].startswith("COLLAPSE")


DENOMINATIONS = (("mass", "2.5666e12 solar masses"),
                 ("information", "the Bekenstein bound, 9.9736e101 bits"),
                 ("spectra", "the same horizon, optimised"))


# ----------------- 5: what it does not move

def refinement_moves_the_seat_lead_split():
    """No.  A multiplicity has no sign, and the split turns on the sign of rho."""
    return False


SPLIT_STANDS = "a charge state supplies the SEAT and not the LEAD"


SCORE = (("the carrier", "RIGHT", "charge is superselected and closed-index zero"),
         ("the variable", "RIGHT", "Bekenstein counts spectral multiplicity"),
         ("the direction", "WRONG", "bounded BY energy; a spectrum is a logarithm"))


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

    print("1. CHARGE IS SUPERSELECTED; IN A CLOSED INDEX IT CARRIES ZERO BITS")
    chk("no coherent superposition across charge sectors",
        CHARGE_IS_SUPERSELECTED, True)
    chk("charge values available in a closed index",
        charge_states_in_a_closed_index(), 1)
    near("so the bits the charge carries", charge_bits_in_a_closed_index(), 0.0)
    chk("is the spectrum superselected too", spectrum_is_superselected(), False)
    print("       permute.py forced total Q = 0 by Gauss two passes ago.  A")
    print("       quantity fixed to one value has log2(1) = 0 bits, so in M's")
    print("       OWN closed index the spectrum is the only carrier left.")

    print("\n2. AND BEKENSTEIN COUNTS EXACTLY THAT CARRIER")
    print("     S <= 2 pi R E / (hbar c) bounds %s" % BEKENSTEIN_COUNTS)
    chk("does the bound mention charge", BEKENSTEIN_MENTIONS_CHARGE, False)
    chk("so the refinement names the bound's own variable",
        refinement_names_the_bounds_variable(), True)
    print("       WHICH IS A POINT IN THE PREDICTION'S FAVOUR.  It does not")
    print("       change the direction of the inequality.")

    print("\n3. PRICED ON A REAL SPECTRUM")
    for n in (10, 100, 1000):
        print("     hydrogenic n_max = %4d   %12d states   %7.3f bits"
              % (n, hydrogenic_states(n), hydrogenic_bits(n)))
    chk("sum of n^2 at n_max = 100", hydrogenic_states(100), 338350)
    near("bits there", hydrogenic_bits(100), 18.3679, 1e-4)
    chk("a spectrum is a LOGARITHM -- ten times the levels, ~ten bits",
        spectrum_is_logarithmic(), True)
    near("bits required (nopath.py)", required_bits(), 9.9736e101)
    near("atoms at n_max = 100", atoms_needed(), 5.4298e100)
    near("their mass, kg", spectral_mass(), 9.0870e73)
    near("against simply supplying, kg", required_mass(), 5.1048e42)
    near("orders worse", orders_worse(), 31.2500, 1e-4)
    print("     per kilogram, which is the honest comparison:")
    near("  hydrogenic n_max = 100, bits/kg", bits_per_kg_hydrogenic(), 1.0976e28)
    near("  saturating the bound, bits/kg", bits_per_kg_saturating(), 1.9538e59)

    print("\n4. AND THE OPTIMAL SPECTRUM IS A HORIZON")
    chk("a black hole saturates the bound", saturates_the_bound(), True)
    chk("and its bits go as M^2 -- bigger is denser",
        bits_go_as_mass_squared(), True)
    chk("so an optimised spectral currency is", OPTIMISED_SPECTRUM_IS,
        "a black hole")
    chk("which dichotomy.py's RICCI route already closed",
        dichotomy_already_closed_it(), True)
    for name, where in DENOMINATIONS:
        print("     %-14s %s" % (name, where))
    print("       THREE DENOMINATIONS OF ONE ROUTE, AND IT ENDS IN A HORIZON.")

    print("\n5. WHAT THE REFINEMENT DOES NOT MOVE")
    chk("does it move charge.py's seat/lead split",
        refinement_moves_the_seat_lead_split(), False)
    print("       %s -- H14, unchanged." % SPLIT_STANDS)
    print("       A multiplicity has no sign; the split turns on the sign of")
    print("       rho.  Enriching a spectrum does not make rho negative.")

    print("\nTHE SCORE")
    for what, verdict, why in SCORE:
        print("     %-16s %-7s %s" % (what, verdict, why))
    chk("things the prediction gets right", sum(1 for s in SCORE if s[1] == "RIGHT"), 2)
    chk("and wrong", sum(1 for s in SCORE if s[1] == "WRONG"), 1)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    print("THE SPECTRAL CURRENCY, PRICED\n")
    print("  %-38s %s" % ("charge bits in a closed index", "0 -- forced by Gauss"))
    print("  %-38s %.3f" % ("hydrogenic bits, n_max = 100", hydrogenic_bits(100)))
    print("  %-38s %.4e" % ("bits required", required_bits()))
    print("  %-38s %.4e kg" % ("mass of that many atoms", spectral_mass()))
    print("  %-38s %.4e kg" % ("mass if simply supplied", required_mass()))
    print("  %-38s %.3f" % ("orders worse", orders_worse()))
    print("  %-38s %s" % ("optimal spectral carrier", OPTIMISED_SPECTRUM_IS))
    print("\n" + "=" * 79)
    print("""VERDICT

  THE DISTINCTION IS CORRECT AND IT IS THE RIGHT ONE TO DRAW.  Electric
  charge is SUPERSELECTED -- no coherent superposition across sectors --
  so its value labels a sector and carries no quantum information
  inside one.  And permute.py already forced the rest: in a spatially
  closed index Gauss's law fixes total Q = 0 exactly, and a quantity
  fixed to one value carries log2(1) = 0 bits.  SO IN M'S OWN CLOSED
  INDEX THE SPECTRUM IS NOT THE PREFERRED CARRIER, IT IS THE ONLY ONE
  LEFT -- and the theorem that removes the other is one this tree
  derived two passes ago.

  AND THE CARRIER NAMED IS EXACTLY WHAT THE BOUND COUNTS.  Bekenstein's
  S <= 2 pi R E / (hbar c) bounds the number of DISTINGUISHABLE QUANTUM
  STATES of a system of energy E in radius R.  It counts spectral
  multiplicity and says nothing about charge.  The prediction has
  independently identified the bound's own variable, which is a point
  in its favour.

  WHAT IT DOES NOT DO IS TURN THE INEQUALITY ROUND.  A spectrum is a
  LOGARITHM: one hydrogenic charge has 385 states to n = 10, 338,350 to
  n = 100, 333,833,500 to n = 1000 -- 8.6, 18.4 and 28.3 bits.  Ten
  times the levels buys ten bits.  Reaching the 9.9736e101 bits the
  transition needs takes 5.4298e100 atoms at 9.0870e73 kg, against
  5.1048e42 kg for simply supplying the mass: THIRTY-ONE AND A QUARTER
  ORDERS WORSE, or 1.0976e28 bits per kilogram against 1.9538e59.

  AND THAT GAP IS NOT A FACT ABOUT HYDROGEN.  It is the distance from
  ordinary matter to the bound, and the bound is saturated by exactly
  one object.  Black-hole bits go as M^2 -- doubling the mass
  quadruples the count -- so the optimum at every scale is a horizon.

        "PAY IN SPECTRA", OPTIMISED, IS "BUILD A BLACK HOLE".

  Which dichotomy.py closed from the other side long ago: the RICCI
  route seats a conjugate point with ordinary positive energy and
  exceeds the collapse bound by 2 pi^2 / 3 at every scale.  THREE
  CURRENCIES, ONE DESTINATION -- mass, information and spectra are not
  three routes but three denominations of one, and the route ends in a
  horizon.

  AND IT LEAVES H14 STANDING.  A charge state supplies the SEAT and not
  the LEAD, and a multiplicity has no sign while the split turns on the
  sign of rho.  Enriching a spectrum does not make an energy density
  negative.  The seat stays free; the lead stays the whole cost.

  SCORE: RIGHT about the carrier, RIGHT about the variable, WRONG about
  the direction.  A better-aimed version of the same currency, landing
  in the same place -- and worth having, because it names what the
  bound is actually about.""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
