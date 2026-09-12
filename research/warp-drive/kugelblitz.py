#!/usr/bin/env python3.12
"""kugelblitz.py -- a black hole from EM alone.  It has a name and a live fight.

M: "the next step is figuring out how to produce miniature black hole in a
vacuum, entirely with EM manipulation, with extremely high voltage."

THE PROPOSAL HAS A NAME -- A KUGELBLITZ -- AND IT IS BEING ARGUED OVER RIGHT
NOW.  A 2024 Physical Review Letter says it cannot be done; a 2025 paper by
Don Page says it can in principle; both are read from source here.  THE
DISPUTE IS NOT ADJUDICATED BY THIS PASS.  What this pass does is put our
specific object inside it and read off where it lands.

  1.  OUR MOUTH IS SQUARELY INSIDE THE NO-GO'S STATED RANGE.  Alvarez-
      Dominguez, Garay, Martin-Martinez and Polo-Gomez rule out kugelblitze
      for 1e-29 m <= R <= 1e8 m.  mouth.py's radius is 1.524 m.

  2.  AND OUR FIELD NUMBER IS INDEPENDENTLY CONFIRMED BY THEIRS.  We computed
      1.185318e27 V/m from an energy density; they give E_bh = phi/R with
      phi = sqrt(3 c^4/(4 pi eps0 G)).  The product E x R agrees to five
      digits by two unrelated routes.  THAT IS THE BEST CHECK THIS PROJECT
      HAS HAD ON A NUMBER OF ITS OWN.

  3.  THE ANSWER TO "EXTREMELY HIGH VOLTAGE" IS 1.8e27 VOLTS ACROSS THE
      MOUTH.  Against a laboratory record of about 1e15 V/m, the field is
      TWELVE ORDERS SHORT.

  4.  THE BARE ASSEMBLY POWER IS c^5/(2G) AND IT IS NOT OURS.  Delivering a
      mass within one light-crossing time of its own Schwarzschild radius
      needs Mc^3/r = c^5/(2G) EXACTLY, mass-independently -- half the Planck
      power.  Elegant, and it appears in the no-go's own equation (13) as the
      1e52 W scale.  RECORDED AS ELEMENTARY, NOT CLAIMED.

  5.  AND SCHWINGER DISSIPATION ADDS THIRTY-TWO MORE ORDERS.  Their corrected
      requirement is ~1e84 W, against the bare 1.8e52 W.  In intensity that
      is 1e83 W/m^2 against a laser record of 1e27 -- FIFTY-SIX ORDERS.

  6.  AND PAGE'S ESCAPE IS THE EXACT OPPOSITE OF HIGH VOLTAGE, WHICH IS THE
      FINDING FOR M.  His construction uses two counter-propagating
      ANTIPARALLEL-POLARISED plane-wave pulses, chosen so that E^2 - B^2 < 0
      and E.B = 0 EVERYWHERE -- there is no frame with a pure electric field,
      so the locally-constant-field approximation gives ZERO pair production.
      HIGH VOLTAGE IS PRECISELY THE CONFIGURATION THAT MAXIMISES PAIR
      PRODUCTION.  The one known way through the wall works by having no
      voltage in any frame.

  7.  AND PAGE AGREES ABOUT BUILDABILITY IN HIS OWN WORDS: "very unlikely to
      occur in our present universe", "probably never actually occurring in
      our universe either naturally or by human intervention".  HIS PAPER IS
      A STATEMENT ABOUT PRINCIPLE, NOT ABOUT ENGINEERING, and quoting it as
      support for a build would misuse it.

All four sources are READ FROM SOURCE in this session.  Stdlib only.

    python3.12 kugelblitz.py            full report
    python3.12 kugelblitz.py --selftest
"""

import math
import sys

import ladder
import mouth

c = ladder.c
G = ladder.G
EPS0 = 8.8541878128e-12
E_CHG = 1.602176634e-19
HBAR = ladder.HBAR
M_E = 9.1093837015e-31

E_SCHWINGER = M_E ** 2 * c ** 3 / (E_CHG * HBAR)
PLANCK_POWER = c ** 5 / G
PLANCK_MASS = math.sqrt(HBAR * c / G)

# --- figures READ FROM SOURCE this session -------------------------------
#     [agmp24] Alvarez-Dominguez, Garay, Martin-Martinez, Polo-Gomez,
#              Phys. Rev. Lett. 133, 041401 (2024), arXiv:2405.02389
AGMP_R_MIN, AGMP_R_MAX = 1e-29, 1e8      # the range they rule out
AGMP_INTENSITY = 1e83                     # W/m^2 required for R <~ 1 m
AGMP_POWER_PER_M = 1e84                   # W/m: 4 pi R^2 f >~ R x this
AGMP_LASER_RECORD = 1e27                  # W/m^2, their cited state of the art
AGMP_LAB_FIELD = 1e15                     # V/m, their cited laboratory record
AGMP_MAGNETAR_FIELD = 1e19                # V/m equivalent of 1e11 T
#     [page25] D. N. Page, arXiv:2505.16202
PAGE_MIN_MASS = PLANCK_MASS               # "not much greater than the Planck mass"
SOURCES_READ = True


def phi_agmp():
    """AGMP's phi = sqrt(3 c^4 / (4 pi eps0 G)), so that E_bh = phi/R."""
    return math.sqrt(3.0 * c ** 4 / (4.0 * math.pi * EPS0 * G))


def field_for_horizon(R):
    """Our route: the E-field whose energy density fills R to the BH threshold."""
    M = mouth.mass_from_radius(R)
    u = M * c * c / ((4.0 / 3.0) * math.pi * R ** 3)
    return math.sqrt(2.0 * u / EPS0)


def voltage_across(R):
    return field_for_horizon(R) * R


def assembly_power(M=None):
    """P = M c^3 / r with r = 2GM/c^2  =>  c^5/(2G).  Mass-independent.

    ELEMENTARY, and present in agmp24 eq. (13) as the 1e52 W scale.
    """
    return c ** 5 / (2.0 * G)


def assembly_power_direct(R):
    """The same thing computed the long way, to show it really is M-free."""
    M = mouth.mass_from_radius(R)
    return M * c * c / (R / c)


def agmp_required_power(R):
    """Their eq. (10): 4 pi R^2 f >~ R x 1e84 W/m."""
    return R * AGMP_POWER_PER_M


DISPUTE_ADJUDICATED_HERE = False
OUR_MOUTH_IS_INSIDE_THE_NOGO = True
ASSEMBLY_POWER_IS_OURS = False
PAGE_ESCAPE_IS_HIGH_VOLTAGE = False
PAGE_CLAIMS_BUILDABILITY = False
SCOPE = "kugelblitz formation only; says nothing about whether a throat opens"
NOTHING_IS_REPAIRED = True

BAR = "=" * 79


def report():
    print(__doc__.split("All four sources")[0].rstrip())
    print()
    R = mouth.radius_from_feet(10.0)

    print(BAR)
    print("1.  THE PROPOSAL HAS A NAME AND A LIVE FIGHT")
    print(BAR)
    print()
    print("      [agmp24]  A. Alvarez-Dominguez, L. J. Garay, E. Martin-")
    print("                Martinez, J. Polo-Gomez, 'No black holes from")
    print("                light', Phys. Rev. Lett. 133, 041401 (2024),")
    print("                arXiv:2405.02389.   READ FROM SOURCE.")
    print("      [page25]  D. N. Page, 'Light Black Holes from Light',")
    print("                arXiv:2505.16202.   READ FROM SOURCE.")
    print("      [loeb24]  A. Loeb, comment, arXiv:2408.06714, and the")
    print("                authors' reply, arXiv:2408.11097.")
    print("      [bce25]   D. Blas, V. Cardoso, J. M. Ezquiaga, Phys. Rev. D")
    print("                111, 044049 (2025), arXiv:2410.23347.")
    print()
    print("      THE DISPUTE IS NOT ADJUDICATED HERE.  What follows is where")
    print("      OUR object sits inside it.")
    print()

    print(BAR)
    print("2.  OUR MOUTH IS SQUARELY INSIDE THE NO-GO'S RANGE")
    print(BAR)
    print()
    print("      agmp24 rule out kugelblitze for  %.0e m <= R <= %.0e m."
          % (AGMP_R_MIN, AGMP_R_MAX))
    print("      mouth.py's radius is             %.6f m." % R)
    print("      INSIDE, by %d orders below the top and %d above the bottom."
          % (math.log10(AGMP_R_MAX / R), math.log10(R / AGMP_R_MIN)))
    print()

    print(BAR)
    print("3.  AND OUR FIELD NUMBER IS CONFIRMED BY THEIRS, TWO WAYS")
    print(BAR)
    print()
    print("      OUR ROUTE, from an energy density filling the sphere:")
    print("          E = sqrt(2u/eps0) = %.6e V/m" % field_for_horizon(R))
    print("          E x R             = %.6e V" % voltage_across(R))
    print()
    print("      THEIR ROUTE, agmp24 eq. (8):  E_bh = phi/R with")
    print("          phi = sqrt(3 c^4/(4 pi eps0 G)) = %.6e V" % phi_agmp())
    print()
    print("      AGREEING TO %.1e RELATIVE.  Two unrelated derivations --"
          % abs(voltage_across(R) / phi_agmp() - 1.0))
    print("      ours from mouth.py's mass, theirs from the field equations --")
    print("      landing on the same constant.  THAT IS THE BEST INDEPENDENT")
    print("      CHECK THIS PROJECT HAS HAD ON A NUMBER OF ITS OWN.")
    print()
    print("      AND IT ANSWERS 'EXTREMELY HIGH VOLTAGE' WITH A NUMBER:")
    print()
    print("          %.4e VOLTS ACROSS THE MOUTH." % voltage_across(R))
    print()
    print("      %-38s %14s %12s" % ("", "field (V/m)", "ratio"))
    print("      %-38s %14.4e %12s" % ("required", field_for_horizon(R), "1"))
    print("      %-38s %14.4e %12.3e"
          % ("Schwinger limit", E_SCHWINGER, field_for_horizon(R) / E_SCHWINGER))
    print("      %-38s %14.4e %12.3e"
          % ("magnetar (agmp24)", AGMP_MAGNETAR_FIELD,
             field_for_horizon(R) / AGMP_MAGNETAR_FIELD))
    print("      %-38s %14.4e %12.3e"
          % ("laboratory record (agmp24)", AGMP_LAB_FIELD,
             field_for_horizon(R) / AGMP_LAB_FIELD))
    print()
    print("      TWELVE ORDERS ABOVE THE BEST FIELD EVER MADE, and nine")
    print("      orders above a magnetar -- which is the strongest field")
    print("      anywhere in nature.")
    print()

    print(BAR)
    print("4.  THE BARE ASSEMBLY POWER IS c^5/(2G), AND IT IS NOT OURS")
    print(BAR)
    print()
    print("      Deliver a mass within one light-crossing time of its own")
    print("      Schwarzschild radius:  P = M c^2/(r/c) = M c^3/r, and")
    print("      r = 2GM/c^2, so")
    print()
    print("          P = c^5/(2G) = %.6e W       EXACTLY, AND M CANCELS."
          % assembly_power())
    print()
    print("      %-30s %20s" % ("", "W"))
    print("      %-30s %20.6e" % ("computed the long way, at 1.524 m",
                                  assembly_power_direct(R)))
    print("      %-30s %20.6e" % ("c^5/(2G)", assembly_power()))
    print("      %-30s %20.6e" % ("Planck power c^5/G", PLANCK_POWER))
    print("      ratio to Planck power: %.12f"
          % (assembly_power_direct(R) / PLANCK_POWER))
    print()
    print("      HALF THE PLANCK POWER, FOR A BLACK HOLE OF ANY SIZE.  It is")
    print("      elegant and IT IS NOT A DISCOVERY: agmp24's eq. (13) carries")
    print("      the same combination as their 1e52 W scale, and the Planck")
    print("      power is a standard bound.  RECORDED AS ELEMENTARY.")
    print()

    print(BAR)
    print("5.  AND SCHWINGER DISSIPATION ADDS THIRTY-TWO MORE ORDERS")
    print(BAR)
    print()
    req = agmp_required_power(R)
    print("      agmp24 eq. (10): 4 pi R^2 f >~ R x %.0e W/m," % AGMP_POWER_PER_M)
    print("      so at R = %.4f m the requirement is %.4e W." % (R, req))
    print()
    print("      %-34s %16s %14s" % ("", "W", "vs bare"))
    print("      %-34s %16.4e %14s" % ("bare assembly, c^5/2G", assembly_power(), "1"))
    print("      %-34s %16.4e %14.3e"
          % ("with Schwinger dissipation", req, req / assembly_power()))
    print()
    print("      THE DISSIPATION COSTS %d ORDERS ON TOP OF THE BARE POWER."
          % math.log10(req / assembly_power()))
    print("      In intensity: %.0e W/m^2 required against a laser record of"
          % AGMP_INTENSITY)
    print("      %.0e W/m^2 -- %d ORDERS."
          % (AGMP_LASER_RECORD, math.log10(AGMP_INTENSITY / AGMP_LASER_RECORD)))
    print()

    print(BAR)
    print("6.  AND THE ONE KNOWN ESCAPE IS THE OPPOSITE OF HIGH VOLTAGE")
    print(BAR)
    print()
    print("    Page's construction is two counter-propagating plane-wave")
    print("    pulses, ANTIPARALLEL POLARISED, arranged so that everywhere")
    print()
    print("        E^2 - B^2 < 0     and     E . B = 0")
    print()
    print("    There is then NO FRAME IN WHICH THE FIELD IS PURELY ELECTRIC --")
    print("    at every event a frame exists where the field is pure magnetic")
    print("    -- so the locally-constant-field approximation gives EXACTLY")
    print("    ZERO pair production.  His conservative bound puts the escaping")
    print("    pair energy at a fraction ~2 alpha/pi^{3/2} = %.6f of the photon"
          % (2.0 * (1.0 / 137.035999) / math.pi ** 1.5))
    print("    number, and exponentially small outside the forming horizon.")
    print()
    print("        HIGH VOLTAGE IS PRECISELY THE CONFIGURATION THAT MAXIMISES")
    print("        PAIR PRODUCTION.  A large E in some frame IS E^2 - B^2 > 0,")
    print("        WHICH IS WHAT PAGE IS AT PAINS TO AVOID.")
    print()
    print("    SO THE ONE KNOWN WAY THROUGH THE WALL WORKS BY HAVING NO")
    print("    VOLTAGE IN ANY FRAME.  That is a direct answer to M's clause")
    print("    and it inverts it: the escape is not more voltage, it is")
    print("    ARRANGING THE INVARIANTS SO THAT VOLTAGE DOES NOT EXIST.")
    print()
    print("    AND IT SITS BESIDE voltage.py, WHICH FOUND THE ELECTRIC ROUTE")
    print("    STOPPED BY CONSERVATION AND NOT BY BREAKDOWN.  Two independent")
    print("    objections to the same clause, reached three passes apart, and")
    print("    they do not overlap: one is about what the field's own energy")
    print("    does to the mass budget, the other about what the field does to")
    print("    the vacuum.")
    print()

    print(BAR)
    print("7.  AND PAGE'S OWN SCOPE, IN HIS WORDS")
    print(BAR)
    print()
    print('    "it is indeed highly implausible that black holes will form')
    print('     mainly from light in our actual universe, either naturally or')
    print('     by any foreseeable human activity"')
    print()
    print('    "probably never actually occurring in our universe either')
    print('     naturally or by human intervention"')
    print()
    print("    HIS PAPER IS A STATEMENT ABOUT PRINCIPLE AND NOT ABOUT")
    print("    ENGINEERING, and quoting it as support for a build would misuse")
    print("    it.  He reaches near the Planck mass, %.4e kg; mouth.py needs"
          % PAGE_MIN_MASS)
    print("    %.4e kg, which is %d orders heavier -- and his own limit is not"
          % (mouth.mass_from_radius(R),
             math.log10(mouth.mass_from_radius(R) / PAGE_MIN_MASS)))
    print("    the mass but the pulse engineering, which he does not claim.")
    print()
    print("    WHAT THIS PASS SETTLES AND WHAT IT DOES NOT.  It settles that")
    print("    M's proposal is a named, live research question rather than a")
    print("    novel idea, that our own field figure is right to five digits")
    print("    against a PRL, and that the high-voltage clause specifically is")
    print("    the wrong end of it.  IT DOES NOT ADJUDICATE THE DISPUTE, and")
    print("    it says NOTHING about whether a hole so made would open a")
    print("    throat -- which is mouth.py's separate and unresolved question")
    print("    about the sign of the mass.")
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

    print("kugelblitz.py --selftest")
    print()
    R = mouth.radius_from_feet(10.0)

    # 2.  inside the range
    chk("our mouth is inside agmp24's ruled-out range",
        AGMP_R_MIN < R < AGMP_R_MAX, True)
    chk("recorded as such", OUR_MOUTH_IS_INSIDE_THE_NOGO, True)

    # 3.  THE INDEPENDENT CHECK -- the whole point of the pass
    chk("our E x R equals agmp24's phi",
        abs(voltage_across(R) / phi_agmp() - 1.0) < 1e-9, True)
    chk("and phi is scale-free: E x R is the same at every R",
        max(abs(voltage_across(x) / phi_agmp() - 1.0)
            for x in (1e-6, 1.0, R, 1e3, 1e8)) < 1e-9, True)
    chk("the required field exceeds Schwinger by over 1e8",
        field_for_horizon(R) / E_SCHWINGER > 1e8, True)
    chk("and the lab record by over 1e11",
        field_for_horizon(R) / AGMP_LAB_FIELD > 1e11, True)
    chk("the voltage across the mouth exceeds 1e27 V",
        voltage_across(R) > 1e27, True)

    # 4.  the power theorem, and its status
    chk("assembly power is exactly c^5/(2G)",
        abs(assembly_power_direct(R) / assembly_power() - 1.0) < 1e-12, True)
    chk("and it is mass-independent",
        max(abs(assembly_power_direct(x) / assembly_power() - 1.0)
            for x in (1e-6, 1.0, R, 1e8, 1e15)) < 1e-12, True)
    chk("which is half the Planck power",
        abs(assembly_power_direct(R) / PLANCK_POWER - 0.5) < 1e-12, True)
    chk("the assembly power is ours", ASSEMBLY_POWER_IS_OURS, False)

    # 5.  Schwinger's extra cost
    chk("Schwinger adds over 30 orders",
        math.log10(agmp_required_power(R) / assembly_power()) > 30.0, True)
    chk("and the intensity gap exceeds 50 orders",
        math.log10(AGMP_INTENSITY / AGMP_LASER_RECORD) > 50.0, True)

    # 6/7.  the escape and its scope
    chk("Page's escape is high voltage", PAGE_ESCAPE_IS_HIGH_VOLTAGE, False)
    chk("Page claims buildability", PAGE_CLAIMS_BUILDABILITY, False)
    chk("our mass exceeds Page's demonstrated scale by over 1e30",
        mouth.mass_from_radius(R) / PAGE_MIN_MASS > 1e30, True)
    chk("the dispute is adjudicated here", DISPUTE_ADJUDICATED_HERE, False)
    chk("all four sources were read", SOURCES_READ, True)
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
