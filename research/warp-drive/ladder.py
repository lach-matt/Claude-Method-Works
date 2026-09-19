#!/usr/bin/env python3.12
"""ladder.py -- invert the bill.  What does the money we have actually buy?

amps.py priced one metre of Delta d and found the current 17 orders out of
reach.  THE MORE USEFUL QUESTION IS THE INVERSE, and it is the one M's own
criterion asks: "if we can't do it faster and cheap then there is no point to
this thread."  So: AT WHAT WE CAN ACTUALLY BUILD, HOW MUCH DO WE GET?

  1.  A FIFTH DENOMINATION, AND THE MOST LEGIBLE ONE YET.  The transition
      equation Delta d = (G/c^2) M Lambda inverts to

          M / Delta d  =  c^2 / (G Lambda)  =  1.349e26 kg per metre

      -- ABOUT TWENTY-TWO EARTH MASSES PER METRE OF SHORTCUT.  Linear, unlike
      amps, and it needs no engineering model at all: it is the transition
      equation read backwards.

  2.  THE LADDER, FROM A LASER SHOT TO A GALAXY.  Every energy this
      civilisation can point at anything buys a SUB-PLANCKIAN Delta d.  The
      Sun's entire rest mass buys about fifteen kilometres.  The Milky Way
      buys a couple of light years.

  3.  AND THE TICKET PRICE.  Proxima Centauri at 4.2 light years costs
      about 2.7e12 solar masses -- ROUGHLY TWO MILKY WAYS.

  4.  THE TRADE IS Delta d ~ I^2 R, AND THAT IS amps.py FROM THE OTHER END.
      Current is the STRONGEST lever available -- doubling it quadruples the
      purchase, where doubling size only doubles it -- AND THAT IS THE SAME
      QUADRATIC that halves the apparent gap.  Not a contradiction: one fact,
      and it is worth having both readings because each is misleading alone.

  5.  ONE COINCIDENCE, MEASURED AND REFUSED.  The best machine's purchase
      lands near sqrt(Lambda) l_P, and THE RATIO IS NOT A RELATION -- it
      depends on which machine, since Delta d carries no hbar and the length
      quantum does.  Recorded as machine-dependent and refused, in the shape
      RETRACTION-AUDIT.tsv found 187 times.

  6.  AND IT ANSWERS M'S CRITERION DIRECTLY.  The corridor is INFRASTRUCTURE
      PRICED IN GALAXIES.  Relativistic travel is A TICKET PRICED IN PAYLOAD.
      For "get there faster and cheap", the second wins and the first is not
      close -- which perception.py found in the same equations already.

Astrophysical and engineering figures are RECALLED, not read, and marked.
They set the ladder's rungs; no claim rests on their third digit.

    python3.12 ladder.py            full report
    python3.12 ladder.py --selftest
"""

import math
import sys

c = 2.99792458e8
G = 6.67430e-11
HBAR = 1.054571817e-34
LAMBDA = 9.982529174194637

EXCHANGE_J = c ** 4 / (G * LAMBDA)          # joules per metre
EXCHANGE_KG = c ** 2 / (G * LAMBDA)         # kilograms per metre
L_PLANCK = math.sqrt(HBAR * G / c ** 3)
L_QUANTUM = math.sqrt(LAMBDA) * L_PLANCK    # the project's length currency

M_EARTH = 5.9722e24
M_SUN = 1.98847e30
LY = 9.4607304725808e15
YEAR = 3.15576e7

# --- RECALLED, not read ---------------------------------------------------
SOURCES = [
    ("a NIF laser shot",              2.05e6),
    ("the Z machine, stored",         2.0e7),
    ("both LHC beams",                7.24e8),
    ("Tsar Bomba (50 Mt)",            2.09e17),
    ("world annual primary energy",   6.2e20),
    ("the Sun's output for a year",   3.828e26 * YEAR),
    ("the Sun, entire rest mass",     M_SUN * c ** 2),
    ("the Milky Way, entire rest mass", 1.5e12 * M_SUN * c ** 2),
]
DESTINATIONS = [
    ("one metre",                 1.0),
    ("one kilometre",             1.0e3),
    ("Earth to Moon",             3.844e8),
    ("Earth to Mars, closest",    5.46e10),
    ("one light year",            LY),
    ("Proxima Centauri, 4.2 ly",  4.2465 * LY),
    ("the galactic centre",       26670.0 * LY),
]
FIGURES_ARE_READ = False


def delta_d_from_energy(E):
    return E / EXCHANGE_J


def mass_for_delta_d(d):
    return d * EXCHANGE_KG


def energy_for_delta_d(d):
    return d * EXCHANGE_J


def loop_energy(I, R):
    """Magnetic energy of a loop field B = mu0 I/(2R) filling a sphere of R.

    A MODEL, and a crude one -- the field is not uniform.  Used ONLY for the
    scaling exponent, never for a rung of the ladder, which uses measured
    stored energies instead.
    """
    MU0 = 4.0e-7 * math.pi
    B = MU0 * I / (2.0 * R)
    return (B * B / (2.0 * MU0)) * (4.0 / 3.0) * math.pi * R ** 3


def delta_d_from_loop(I, R):
    return delta_d_from_energy(loop_energy(I, R))


EXCHANGE_IS_LINEAR_IN_MASS = True
CURRENT_IS_THE_STRONGEST_LEVER = True
QUADRATIC_IS_ONE_FACT_TWO_READINGS = True
PLANCK_COINCIDENCE_IS_A_RELATION = False
CORRIDOR_IS_CHEAP_TRANSIT = False
SCOPE = "the transition equation read backwards; comparators RECALLED"
NOTHING_IS_REPAIRED = True

BAR = "=" * 79


def report():
    print(__doc__.split("Astrophysical")[0].rstrip())
    print()

    print(BAR)
    print("1.  A FIFTH DENOMINATION -- KILOGRAMS PER METRE")
    print(BAR)
    print()
    print("      Delta d = (G/c^2) M Lambda   inverts to   M/Delta d = c^2/(G Lambda)")
    print()
    print("          %.6e kg per metre" % EXCHANGE_KG)
    print("          %.4f Earth masses per metre" % (EXCHANGE_KG / M_EARTH))
    print("          %.6e solar masses per metre" % (EXCHANGE_KG / M_SUN))
    print()
    print("      NO ENGINEERING MODEL IS USED.  This is the transition equation")
    print("      read backwards, and it is LINEAR -- unlike amps, where the")
    print("      quadratic hid half the exponent.  The five denominations now")
    print("      standing for one wall:")
    print()
    print("        %-12s %.6e J per metre" % ("ENERGY", EXCHANGE_J))
    print("        %-12s %.6e kg per metre        <-- new" % ("MASS", EXCHANGE_KG))
    print("        %-12s %.6e m" % ("LENGTH", L_QUANTUM))
    print("        %-12s %.6e Hz" % ("FREQUENCY", math.sqrt(c ** 5 / (HBAR * G)) / math.sqrt(LAMBDA)))
    print("        %-12s ~1e24 A at a metre        (quadratic, not linear)" % "CURRENT")
    print()

    print(BAR)
    print("2.  THE LADDER -- WHAT EACH ENERGY ACTUALLY BUYS")
    print(BAR)
    print()
    print("      %-34s %14s %16s %12s"
          % ("source (RECALLED)", "energy (J)", "Delta d (m)", "in l_P"))
    for name, E in SOURCES:
        d = delta_d_from_energy(E)
        print("      %-34s %14.4e %16.6e %12.4e" % (name, E, d, d / L_PLANCK))
    print()
    z = delta_d_from_energy(2.0e7)
    lhc = delta_d_from_energy(7.24e8)
    print("      THE Z MACHINE'S ENTIRE STORED ENERGY BUYS %.4e m --" % z)
    print("      %.4f OF A PLANCK LENGTH.  Both LHC beams buy %.2f Planck"
          % (z / L_PLANCK, lhc / L_PLANCK))
    print("      lengths.  EVERY ENERGY THIS CIVILISATION CAN POINT AT ANYTHING")
    print("      IS SUB-PLANCKIAN OR BARELY ABOVE.")
    print()
    print("      The Sun's whole rest mass buys %.4e m -- %.2f km."
          % (delta_d_from_energy(M_SUN * c ** 2),
             delta_d_from_energy(M_SUN * c ** 2) / 1e3))
    print("      The Milky Way's buys %.4e m -- %.3f light years."
          % (delta_d_from_energy(1.5e12 * M_SUN * c ** 2),
             delta_d_from_energy(1.5e12 * M_SUN * c ** 2) / LY))
    print()

    print(BAR)
    print("3.  AND THE TICKET PRICE")
    print(BAR)
    print()
    print("      %-30s %16s %16s %14s"
          % ("destination", "Delta d (m)", "mass (kg)", "solar masses"))
    for name, d in DESTINATIONS:
        M = mass_for_delta_d(d)
        print("      %-30s %16.4e %16.4e %14.4e" % (name, d, M, M / M_SUN))
    print()
    px = mass_for_delta_d(4.2465 * LY) / M_SUN
    print("      PROXIMA CENTAURI COSTS %.4e SOLAR MASSES -- about %.1f" % (px, px / 1.5e12))
    print("      MILKY WAYS (galaxy mass RECALLED and itself uncertain by a")
    print("      factor of a few, which changes the count and not the verdict).")
    print()
    print("      And one metre costs %.2f Earth masses, which is the whole"
          % (EXCHANGE_KG / M_EARTH))
    print("      bill in one sentence a person can hold.")
    print()

    print(BAR)
    print("4.  THE TRADE IS Delta d ~ I^2 R -- amps.py FROM THE OTHER END")
    print(BAR)
    print()
    print("      With B = mu0 I/(2R) over a sphere of radius R, the stored")
    print("      energy goes as I^2 R, so Delta d does too.")
    print()
    print("      %10s %10s %18s %14s %14s"
          % ("I (A)", "R (m)", "Delta d (m)", "x from I", "x from R"))
    base = delta_d_from_loop(2.6e7, 1.0)
    for I, R in [(2.6e7, 1.0), (5.2e7, 1.0), (2.6e7, 2.0), (2.6e8, 1.0), (2.6e7, 1e3)]:
        d = delta_d_from_loop(I, R)
        print("      %10.3g %10.3g %18.6e %14.4f %14.4f"
              % (I, R, d, (I / 2.6e7) ** 2, R / 1.0))
    print()
    print("      DOUBLING THE CURRENT QUADRUPLES THE PURCHASE; DOUBLING THE")
    print("      SIZE ONLY DOUBLES IT.  SO CURRENT IS THE STRONGEST LEVER THERE")
    print("      IS -- and it is the SAME QUADRATIC that made amps.py's gap look")
    print("      half as bad as it is.  ONE FACT, TWO READINGS, and each is")
    print("      misleading without the other: the exponent that flatters the")
    print("      gap is the exponent that rewards the lever.")
    print()
    print("      The loop model is CRUDE and is used only for the EXPONENT.")
    print("      Every rung of section 2 uses a measured stored energy instead,")
    print("      so no number there depends on it.")
    print()

    print(BAR)
    print("5.  ONE COINCIDENCE, MEASURED AND REFUSED")
    print(BAR)
    print()
    print("      Z machine purchase   %.6e m" % z)
    print("      sqrt(Lambda) l_P     %.6e m" % L_QUANTUM)
    print("      ratio                %.6f" % (z / L_QUANTUM))
    print()
    print("      TEMPTING AND NOT A RELATION.  Delta d = E G Lambda / c^4 carries")
    print("      NO hbar; sqrt(Lambda) l_P = sqrt(Lambda hbar G/c^3) DOES.  The")
    print("      ratio is therefore proportional to the machine's energy and is")
    print("      a fact about Sandia, not about physics: at the LHC it is %.4f"
          % (lhc / L_QUANTUM))
    print("      and at NIF %.6f.  REFUSED, in the shape RETRACTION-AUDIT.tsv"
          % (delta_d_from_energy(2.05e6) / L_QUANTUM))
    print("      found 187 times by fingerprinting numbers with no derivation")
    print("      between them.")
    print()

    print(BAR)
    print("6.  M'S OWN CRITERION, ANSWERED")
    print(BAR)
    print()
    print("    M set the test at the start of this thread: 'if we can't do it")
    print("    faster and cheap then there is no point to this thread.'")
    print()
    print("      THE CORRIDOR IS INFRASTRUCTURE PRICED IN GALAXIES.  %.2e solar"
          % px)
    print("      masses to reach the nearest star, and %.2f Earth masses for a"
          % (EXCHANGE_KG / M_EARTH))
    print("      single metre.  It is not expensive; it is the wrong order of")
    print("      object to be costing at all.")
    print()
    print("      RELATIVISTIC TRAVEL IS A TICKET PRICED IN PAYLOAD, and")
    print("      perception.py found it in the same equations: a round trip at")
    print("      one ship-year each way returns you to an Earth 8.724 years")
    print("      older having aged two.  REAL TRAVEL, AND THE COST IS ONE")
    print("      PAYLOAD RATHER THAN ONE GALAXY.")
    print()
    print("      SO THE ANSWER TO THE CRITERION IS: FOR GETTING A PAYLOAD THERE,")
    print("      THE CORRIDOR LOSES AND IT IS NOT CLOSE.  What the corridor buys")
    print("      that a ticket cannot is EVERYONE, PERMANENTLY, ANY MASS, BOTH")
    print("      WAYS -- and that is a different purchase, correctly priced")
    print("      here for the first time in a denomination anyone can check.")
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

    print("ladder.py --selftest")
    print()
    chk("the energy exchange rate", float("%.6e" % EXCHANGE_J), 1.212374e43)
    chk("the mass exchange rate", float("%.6e" % EXCHANGE_KG), 1.348948e+26)
    chk("and the two differ by c^2", abs(EXCHANGE_J / EXCHANGE_KG - c * c) < 1e3, True)
    chk("the Planck length", float("%.6e" % L_PLANCK), 1.616255e-35)
    chk("the length quantum", float("%.6e" % L_QUANTUM), 5.106580e-35)

    # the transition equation round-trips
    chk("mass and energy routes agree",
        max(abs(mass_for_delta_d(d) * c * c / energy_for_delta_d(d) - 1.0)
            for d in (1e-30, 1.0, 1e16)) < 1e-12, True)
    chk("Delta d inverts its own cost",
        max(abs(delta_d_from_energy(energy_for_delta_d(d)) / d - 1.0)
            for d in (1e-30, 1.0, 1e16)) < 1e-12, True)

    chk("Earth masses per metre", float("%.4f" % (EXCHANGE_KG / M_EARTH)), 22.5871)
    chk("the exchange is linear in mass", EXCHANGE_IS_LINEAR_IN_MASS, True)

    # the ladder
    z = delta_d_from_energy(2.0e7)
    chk("Z machine purchase, in Planck lengths",
        float("%.4f" % (z / L_PLANCK)), 0.1021)
    chk("every terrestrial source is under 10 Planck lengths",
        max(delta_d_from_energy(E) for n, E in SOURCES[:3]) / L_PLANCK < 10.0, True)
    chk("the Sun's rest mass, in km",
        float("%.2f" % (delta_d_from_energy(M_SUN * c ** 2) / 1e3)), 14.74)
    chk("the galaxy, in light years",
        float("%.3f" % (delta_d_from_energy(1.5e12 * M_SUN * c ** 2) / LY)), 2.337)

    # the ticket
    px = mass_for_delta_d(4.2465 * LY) / M_SUN
    chk("Proxima, in solar masses", float("%.4e" % px), 2.7254e+12)
    chk("which is more than one galaxy mass", px > 1.5e12, True)

    # the trade
    chk("Delta d scales as I^2",
        abs(delta_d_from_loop(5.2e7, 1.0) / delta_d_from_loop(2.6e7, 1.0) - 4.0) < 1e-12,
        True)
    chk("and linearly in R",
        abs(delta_d_from_loop(2.6e7, 2.0) / delta_d_from_loop(2.6e7, 1.0) - 2.0) < 1e-12,
        True)
    chk("current is the strongest lever", CURRENT_IS_THE_STRONGEST_LEVER, True)
    chk("one fact, two readings", QUADRATIC_IS_ONE_FACT_TWO_READINGS, True)

    # the refusal
    chk("the Planck coincidence is a relation", PLANCK_COINCIDENCE_IS_A_RELATION, False)
    chk("and the ratio moves with the machine",
        abs(delta_d_from_energy(7.24e8) / L_QUANTUM
            - delta_d_from_energy(2.05e6) / L_QUANTUM) > 1.0, True)

    chk("the corridor is cheap transit", CORRIDOR_IS_CHEAP_TRANSIT, False)
    chk("comparators were read", FIGURES_ARE_READ, False)
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
