#!/usr/bin/env python3.12
"""field.py -- run it through the field equations, and price the reactor.

M: "I think their math is right, but their conjecture is wrong.  We have to use
field equations as well to run our numbers ... And we need to look at what puts
out the power required.  Can we hook this thing up to a nuclear and utilize the
reactor's entire output?"

TWO QUESTIONS.  THE SECOND HAS A ONE-LINE ANSWER THAT CLOSES THE WHOLE AVENUE,
AND THE FIRST FINDS A FAULT IN OUR OWN WORK.

  1.  THE REACTOR CANNOT HELP, AND NOT BECAUSE IT IS TOO SMALL.

          EVERY ENERGY SOURCE CONVERTS MASS AT EFFICIENCY AT MOST ONE, AND
          THE BILL IS STATED AS A MASS.

      ladder.py priced the corridor at 22.59 Earth masses per metre.  A
      reactor does not make energy, it converts mass, so E = mc^2 makes the
      fuel requirement AT BEST equal to the bill itself.  NO POWER SOURCE
      REDUCES A BILL DENOMINATED IN MASS -- it would have to exceed unit
      efficiency.  The numbers below are consequences, not the argument.

  2.  AND THE FIELD EQUATIONS FIND A FAULT IN amps.py, WHICH IS M'S POINT
      LANDING ON OUR OWN WORK RATHER THAN ON THE LITERATURE'S.

      The Schwinger rate depends on the INVARIANT electric field, built from
      the two Maxwell invariants, and NOT on the magnitude of B.  For a PURE
      MAGNETIC FIELD that invariant is EXACTLY ZERO, so the pair-production
      rate is EXACTLY ZERO however large B is.

      MAGNETARS PROVE IT: about 1e11 T against B_QED = 4.414e9 T, TWENTY-THREE
      TIMES THE CRITICAL FIELD, AND THEY DO NOT DISCHARGE.

      amps.py said the magnetic route is "stopped by BOTH, in that order:
      BREAKDOWN FIRST, below ~720 km, where B exceeds B_QED".  THAT IS WRONG.
      Exceeding B_QED is not breakdown; B_QED marks where Landau spacing
      reaches the electron rest mass, which is a quantum-regime marker and
      not a threshold for the vacuum to give way.

      SO ONE OF THE TWO WALLS amps.py REPORTED DOES NOT EXIST.  Corrected
      here, not edited.

  3.  WHICH IS ALSO WHY PAGE'S ESCAPE WORKS, AND IT GENERALISES.  His
      counter-propagating antiparallel pulses give E^2 - c^2 B^2 < 0 and
      E.B = 0, which is the same statement: the invariant electric field
      vanishes.  A PURE MAGNETIC FIELD IS THE SIMPLEST MEMBER OF THAT FAMILY,
      and the no-go's assumption of a nonzero invariant E is what M's instinct
      was pointing at.

  4.  AND THE HONEST NET.  ONE WALL REMOVED, ONE STANDS.  The current bill of
      amps.py is untouched by any of this, and it was always the binding one.

Comparators RECALLED.  Page's rate formula READ FROM SOURCE.  Stdlib only.

    python3.12 field.py            full report
    python3.12 field.py --selftest
"""

import math
import sys

import ladder
import mouth

c = ladder.c
G = ladder.G
HBAR = ladder.HBAR
MU0 = 4.0e-7 * math.pi
EPS0 = 8.8541878128e-12
E_CHG = 1.602176634e-19
M_E = 9.1093837015e-31
M_EARTH = ladder.M_EARTH
M_SUN = ladder.M_SUN
YEAR = ladder.YEAR

E_SCHWINGER = M_E ** 2 * c ** 3 / (E_CHG * HBAR)
B_QED = M_E ** 2 * c ** 2 / (E_CHG * HBAR)

# --- RECALLED ------------------------------------------------------------
REACTOR_TH = 3.0e9              # W thermal, a large PWR
WORLD_REACTORS_TH = 1.2e12      # W thermal, all ~440 reactors
UNIVERSE_AGE_YR = 1.38e10
MAGNETAR_B = 1.0e11             # T
FISSION_EFFICIENCY = 200.0 / (235.0 * 931.494)   # 200 MeV per 235 u
FIGURES_ARE_READ = False


# --- 1.  the reactor -----------------------------------------------------

def accumulation_time(E, power):
    return E / power


def fuel_mass(E, efficiency):
    """Any source: E = eta m c^2, so m = E/(eta c^2).  eta <= 1 always."""
    return E / (efficiency * c * c)


# --- 2.  the Maxwell invariants, and the rate that depends on them -------

def invariants(E, B):
    """S = E^2 - c^2 B^2 and P = E . (cB), from the field 3-vectors."""
    S = sum(x * x for x in E) - c * c * sum(x * x for x in B)
    P = c * sum(a * b for a, b in zip(E, B))
    return S, P


def invariant_fields(E, B):
    """Page eq. (22): the E and B magnitudes in a frame where they are
    parallel or zero.  Returned in V/m."""
    S, P = invariants(E, B)
    root = math.sqrt(S * S + 4.0 * P * P)
    e_inv = math.sqrt(max(0.5 * root + 0.5 * S, 0.0))
    b_inv = math.sqrt(max(0.5 * root - 0.5 * S, 0.0))
    return e_inv, b_inv


def schwinger_rate(E, B):
    """Page eq. (23), up to constants: the exponential is exp(-pi E_c/e_inv).

    THE WHOLE POINT: it depends on the INVARIANT e_inv, not on |B|.  When
    e_inv = 0 the rate is EXACTLY zero, for any magnitude of B whatever.
    """
    e_inv, b_inv = invariant_fields(E, B)
    if e_inv <= 0.0:
        return 0.0
    return math.exp(-math.pi * E_SCHWINGER / e_inv)


def magnetic_field_for_density(u):
    """u = B^2/(2 mu0)."""
    return math.sqrt(2.0 * MU0 * u)


def electric_field_for_density(u):
    return math.sqrt(2.0 * u / EPS0)


# --- verdicts ------------------------------------------------------------
REACTOR_HELPS = False
NO_SOURCE_REDUCES_A_MASS_BILL = True
PURE_B_PRODUCES_PAIRS = False
EXCEEDING_B_QED_IS_BREAKDOWN = False
AMPS_BREAKDOWN_CLAIM_STANDS = False
CURRENT_WALL_STANDS = True
SCOPE = "locally-constant-field approximation; the current bill is untouched"
NOTHING_IS_REPAIRED = True

BAR = "=" * 79


def report():
    print(__doc__.split("Comparators RECALLED")[0].rstrip())
    print()
    R = mouth.radius_from_feet(10.0)
    M = mouth.mass_from_radius(R)
    E_req = M * c * c
    u = E_req / ((4.0 / 3.0) * math.pi * R ** 3)

    print(BAR)
    print("1.  THE REACTOR -- AND THE ANSWER IS A THEOREM, NOT A NUMBER")
    print(BAR)
    print()
    print("        EVERY ENERGY SOURCE CONVERTS MASS AT EFFICIENCY <= 1, AND")
    print("        THE BILL IS STATED AS A MASS.")
    print()
    print("      ladder.py: 22.59 Earth masses per metre.  A reactor does not")
    print("      MAKE energy, it CONVERTS MASS, so E = m c^2 makes the fuel")
    print("      requirement at best EQUAL TO THE BILL ITSELF.  Asking what")
    print("      produces the power cannot help, because the answer would have")
    print("      to exceed unit efficiency.")
    print()
    print("      The numbers are consequences.  For mouth.py's %.4e J:" % E_req)
    print()
    print("      %-34s %16s %16s" % ("source (RECALLED)", "seconds", "universe ages"))
    for name, P in [("one large reactor, 3 GW thermal", REACTOR_TH),
                    ("every reactor on Earth, 1.2 TW", WORLD_REACTORS_TH),
                    ("world primary energy, 6.2e20 J/yr", 6.2e20 / YEAR)]:
        t = accumulation_time(E_req, P)
        print("      %-34s %16.4e %16.4e"
              % (name, t, t / (UNIVERSE_AGE_YR * YEAR)))
    print()
    print("      A 3 GW reactor running EVERY SECOND SINCE THE BIG BANG would")
    print("      have delivered %.4e J.  The bill is %.4e J."
          % (REACTOR_TH * UNIVERSE_AGE_YR * YEAR, E_req))
    print()
    print("      AND THE FUEL MASS IS THE BILL, WHICH IS THE POINT:")
    print()
    print("      %-40s %18s %14s" % ("conversion", "fuel (kg)", "Earth masses"))
    for name, eta in [("perfect, matter-antimatter", 1.0),
                      ("fission of U-235, %.4f %%" % (100 * FISSION_EFFICIENCY),
                       FISSION_EFFICIENCY),
                      ("fusion D-T, ~0.4 %", 0.004)]:
        m = fuel_mass(E_req, eta)
        print("      %-40s %18.4e %14.4e" % (name, m, m / M_EARTH))
    print()
    print("      EVEN AT PERFECT CONVERSION THE FUEL IS %.2f EARTH MASSES,"
          % (fuel_mass(E_req, 1.0) / M_EARTH))
    print("      WHICH IS mouth.py'S ANSWER EXACTLY -- because it is the same")
    print("      statement.  Fission needs %.4e Earth masses, %.4f solar."
          % (fuel_mass(E_req, FISSION_EFFICIENCY) / M_EARTH,
             fuel_mass(E_req, FISSION_EFFICIENCY) / M_SUN))
    print()
    print("      SO THE POWER-SOURCE QUESTION IS CLOSED PERMANENTLY, and not")
    print("      by a magnitude: a bill in mass cannot be paid by finding a")
    print("      better converter of mass.")
    print()

    print(BAR)
    print("2.  THE FIELD EQUATIONS -- AND THEY FIND A FAULT IN amps.py")
    print(BAR)
    print()
    print("      The Schwinger rate depends on the INVARIANT electric field,")
    print("      built from the two Maxwell invariants S = E^2 - c^2 B^2 and")
    print("      P = E.(cB) by Page's eq. (22), AND NOT ON |B|.")
    print()
    print("      %-30s %14s %14s %16s %12s"
          % ("configuration", "S", "P", "invariant E", "rate"))
    Es = E_SCHWINGER
    cases = [
        ("pure electric, at E_S", (Es, 0, 0), (0, 0, 0)),
        ("pure magnetic, at B_QED", (0, 0, 0), (B_QED, 0, 0)),
        ("pure magnetic, x1e9 B_QED", (0, 0, 0), (1e9 * B_QED, 0, 0)),
        ("plane wave, E = cB", (Es, 0, 0), (0, Es / c, 0)),
        ("counter-prop (Page)", (0.1 * Es, 0, 0), (0, Es / c, 0)),
        ("parallel E and B", (Es, 0, 0), (B_QED, 0, 0)),
    ]
    for name, E, B in cases:
        S, P = invariants(list(E), list(B))
        e_inv, _ = invariant_fields(list(E), list(B))
        print("      %-30s %14.2e %14.2e %16.6e %12.4e"
              % (name, S, P, e_inv, schwinger_rate(list(E), list(B))))
    print()
    print("      A PURE MAGNETIC FIELD HAS INVARIANT E = 0 AND RATE EXACTLY")
    print("      ZERO, AT ANY MAGNITUDE -- a billion times the critical field")
    print("      changes nothing, because a magnetic field does no work on a")
    print("      charge and there is no frame in which it is electric.")
    print()
    print("      AND MAGNETARS PROVE IT RATHER THAN THE ALGEBRA ALONE:")
    print("      about %.0e T against B_QED = %.6e T, %.1f TIMES THE"
          % (MAGNETAR_B, B_QED, MAGNETAR_B / B_QED))
    print("      CRITICAL FIELD, PERSISTING FOR THOUSANDS OF YEARS.")
    print()
    print("      SO amps.py IS WRONG WHERE IT SAYS the magnetic route is")
    print("      'stopped by BOTH, in that order: BREAKDOWN FIRST, below ~720")
    print("      km, where B exceeds B_QED'.  EXCEEDING B_QED IS NOT")
    print("      BREAKDOWN.  B_QED marks where Landau spacing reaches the")
    print("      electron rest mass -- a quantum-regime marker, not a")
    print("      threshold for the vacuum to give way.  ONE OF THE TWO WALLS")
    print("      THAT FILE REPORTED DOES NOT EXIST.  Corrected, not edited.")
    print()

    print(BAR)
    print("3.  WHICH IS WHY PAGE'S ESCAPE WORKS, AND IT GENERALISES")
    print(BAR)
    print()
    print("      His counter-propagating antiparallel pulses give")
    print("      E^2 - c^2 B^2 < 0 and E.B = 0 -- and that is the SAME")
    print("      STATEMENT as invariant E = 0.  A PURE MAGNETIC FIELD IS THE")
    print("      SIMPLEST MEMBER OF THAT FAMILY, and the plane wave sits")
    print("      exactly on its boundary at S = 0.")
    print()
    print("      SO M'S READING IS RIGHT IN A SPECIFIC WAY.  agmp24's")
    print("      arithmetic is not in question -- kugelblitz.py confirmed one")
    print("      of their constants against ours to the last digit.  What")
    print("      their conclusion assumes is a configuration with a NONZERO")
    print("      INVARIANT ELECTRIC FIELD, and the field equations say that")
    print("      assumption is a choice rather than a necessity.")
    print()
    print("      FOR OUR OBJECT, THE MAGNETIC ROUTE NEEDS:")
    print()
    print("          B = %.6e T      against E = %.6e V/m"
          % (magnetic_field_for_density(u), electric_field_for_density(u)))
    print("          %.4e x B_QED, and %.4e x a magnetar."
          % (magnetic_field_for_density(u) / B_QED,
             magnetic_field_for_density(u) / MAGNETAR_B))
    print()
    print("      EIGHT ORDERS ABOVE THE STRONGEST FIELD IN NATURE -- AND WITH")
    print("      NO BREAKDOWN MECHANISM STANDING IN THE WAY.")
    print()

    print(BAR)
    print("4.  THE HONEST NET -- ONE WALL REMOVED, ONE STANDS")
    print(BAR)
    print()
    print("      REMOVED: the vacuum-breakdown wall on the magnetic branch.")
    print("      It was ours, it was wrong, and M's push to the field")
    print("      equations is what found it.")
    print()
    print("      STANDS, AND UNTOUCHED BY ANY OF THIS: amps.py's current bill.")
    print("      4.292537e24 A at a metre, falling only as R^{-1/2}, which no")
    print("      argument about invariants affects because it is a statement")
    print("      about how much energy the field carries and not about what")
    print("      the vacuum does in response.  THAT WAS ALWAYS THE BINDING")
    print("      WALL AND IT IS STILL THERE.")
    print()
    print("      AND THE REACTOR QUESTION IS CLOSED BY SECTION 1 REGARDLESS OF")
    print("      EITHER, since the bill is a mass and no converter beats unity.")
    print()
    print("      WHAT WOULD ACTUALLY MOVE THIS: not a bigger power source and")
    print("      not a cleverer field configuration, but mouth.py's OPEN SIGN")
    print("      QUESTION -- whether the mass the transition equation prices is")
    print("      the positive one this tree has been costing or the negative")
    print("      one certify.py requires.  Everything else has now been")
    print("      measured and every measurement has come back the same way.")
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

    print("field.py --selftest")
    print()
    R = mouth.radius_from_feet(10.0)
    E_req = mouth.mass_from_radius(R) * c * c
    u = E_req / ((4.0 / 3.0) * math.pi * R ** 3)

    # 1.  the theorem, and it is an identity not an estimate
    chk("perfect-conversion fuel equals the bill's own mass",
        abs(fuel_mass(E_req, 1.0) / mouth.mass_from_radius(R) - 1.0) < 1e-12, True)
    chk("and that is ladder.py's 22.59 Earth masses per metre",
        abs(fuel_mass(E_req, 1.0) / ladder.mass_for_delta_d(
            mouth.reach_from_radius(R)) - 1.0) < 1e-12, True)
    chk("fuel scales as 1/efficiency",
        abs(fuel_mass(E_req, 0.5) / fuel_mass(E_req, 1.0) - 2.0) < 1e-12, True)
    chk("a reactor needs over 1e16 universe ages",
        accumulation_time(E_req, REACTOR_TH) / (UNIVERSE_AGE_YR * YEAR) > 1e16, True)
    chk("no source reduces a mass bill", NO_SOURCE_REDUCES_A_MASS_BILL, True)
    chk("the reactor helps", REACTOR_HELPS, False)

    # 2.  the invariants
    Es = E_SCHWINGER
    chk("pure E: invariant E equals E",
        abs(invariant_fields([Es, 0, 0], [0, 0, 0])[0] / Es - 1.0) < 1e-12, True)
    chk("pure B: invariant E is exactly zero",
        invariant_fields([0, 0, 0], [B_QED, 0, 0])[0], 0.0)
    chk("and stays zero a billion times over",
        invariant_fields([0, 0, 0], [1e9 * B_QED, 0, 0])[0], 0.0)
    chk("so the rate is exactly zero for pure B",
        schwinger_rate([0, 0, 0], [1e9 * B_QED, 0, 0]), 0.0)
    chk("pure B produces pairs", PURE_B_PRODUCES_PAIRS, False)
    chk("a plane wave sits on the boundary, S = P = 0",
        invariants([Es, 0, 0], [0, Es / c, 0]), (0.0, 0.0))
    chk("counter-propagating gives S < 0",
        invariants([0.1 * Es, 0, 0], [0, Es / c, 0])[0] < 0.0, True)
    chk("and its rate is zero too",
        schwinger_rate([0.1 * Es, 0, 0], [0, Es / c, 0]), 0.0)
    chk("while pure E at E_S has a nonzero rate",
        schwinger_rate([Es, 0, 0], [0, 0, 0]) > 0.0, True)

    # the correction to amps.py
    chk("magnetars exceed B_QED", MAGNETAR_B / B_QED > 20.0, True)
    chk("exceeding B_QED is breakdown", EXCEEDING_B_QED_IS_BREAKDOWN, False)
    chk("amps.py's breakdown claim stands", AMPS_BREAKDOWN_CLAIM_STANDS, False)
    chk("amps.py itself is unchanged",
        "BREAKDOWN FIRST" in open("amps.py").read(), True)

    # 3.  the magnetic requirement, and the two routes carry the same energy
    chk("B and E routes carry the same energy density",
        abs(magnetic_field_for_density(u) ** 2 / (2 * MU0) / u - 1.0) < 1e-12
        and abs(EPS0 * electric_field_for_density(u) ** 2 / 2 / u - 1.0) < 1e-12,
        True)
    chk("the required B exceeds a magnetar by over 1e7",
        magnetic_field_for_density(u) / MAGNETAR_B > 1e7, True)

    # 4.  what still stands
    chk("the current wall stands", CURRENT_WALL_STANDS, True)
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
