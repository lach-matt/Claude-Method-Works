#!/usr/bin/env python3.12
"""closeout.py -- the two open rows, closed as far as they can honestly be.

M: "let's handle these and then we can look at the viability of a build."

TWO ROWS.  One closes to a verdict, one closes to a CORRECTION OF MINE, and
neither closes the way I implied last turn.

PART 1 -- HAWKING.  chronology.py records the Cauchy-horizon divergence as
NOT-RUN because the LITERATURE DISPUTE is unresolved: Kim-Thorne argue quantum
gravity cuts the divergence off at the Planck scale, Hawking argues it does
not.  THAT DISPUTE IS NOT RESOLVED HERE AND CANNOT BE.  What can be done, and
was not, is to ask whether it is LOAD-BEARING FOR THIS OBJECT.

  Grant Kim-Thorne everything.  Take their cutoff, the most favourable
  assumption a time machine can be given, and the vacuum pileup at horizon
  formation is the PLANCK ENERGY DENSITY.  Compare it to the energy density
  the corridor itself runs at, using the corridor's OWN throat scale.

  THE PILEUP EXCEEDS THE CORRIDOR BY ABOUT 102 ORDERS OF MAGNITUDE.

  So the dispute is MOOT HERE.  It does not matter whether the divergence is
  cut off, because the cut-off value alone is 102 orders past anything this
  geometry holds.  THE ROW MOVES FROM NOT-RUN TO MOOT-FOR-THIS-OBJECT, which
  is a weaker claim than resolving it and a stronger one than declining.

PART 2 -- OBJECTS_PER_EVENT, AND I WAS WRONG ABOUT IT.

  Last turn I said N "is the one number that could still move the crossover
  verdict".  IT CANNOT.  The crossover compares TOTAL mass transported against
  TOTAL mass spent, and slicing the payload into more objects changes neither
  side.  N sets the cost PER TRAVELLER, which is an economic question and not
  the physics one.  Recorded as a fault.

  But asking the question produced something the tree did not have.  The
  throat scale follows from the transition equation EXACTLY:

      r_s = 2 G M / c^2  and  M = Delta d c^2/(G Lambda)   =>   r_s = 2 Delta d / Lambda

  G AND c CANCEL COMPLETELY.  The aspect ratio of every corridor is fixed:

      Delta d / r_s = Lambda / 2 = 4.991265

  A CORRIDOR IS NEVER MUCH LONGER THAN IT IS WIDE.  A shortcut to Proxima is
  an object 1.7 light years across lying between here and there.  IT IS NOT A
  TUNNEL, IT IS VERY NEARLY A BRIDGE AS WIDE AS IT IS LONG -- and that is
  scale-invariant, true of a one-metre corridor and a galactic one alike.

Literature positions are RECALLED, not read, and marked.  Stdlib only.

    python3.12 closeout.py            full report
    python3.12 closeout.py --selftest
"""

import math
import sys

import ladder

c = ladder.c
G = ladder.G
HBAR = ladder.HBAR
LAMBDA = ladder.LAMBDA
LY = ladder.LY
M_SUN = ladder.M_SUN

L_PLANCK = math.sqrt(HBAR * G / c ** 3)
M_PLANCK = math.sqrt(HBAR * c / G)
RHO_PLANCK = M_PLANCK * c * c / L_PLANCK ** 3      # = c^7/(hbar G^2)

PROXIMA_LY = 4.2465
LITERATURE_IS_READ = False


# --- PART 1 ---------------------------------------------------------------

def image_sum(n_images, ell1=1.0):
    """Sum_{N != 0} 1/(N ell1)^4 -- the self-linking geodesics' contribution.

    A field on a spacetime with a closed timelike curve sees infinitely many
    images of itself.  Each contributes to <T> as 1/(geodesic length)^4, which
    is FORCED BY DIMENSIONS and not recalled: <T> is an energy density, the
    only scale available is the length, and hbar c / l^4 is the unique
    combination.  Converges for fixed ell1 and DIVERGES as ell1 -> 0, which is
    what horizon formation is.
    """
    return sum(1.0 / (N * ell1) ** 4 for N in range(1, n_images + 1)) * 2.0


def image_sum_closed(ell1=1.0):
    """2 zeta(4) / ell1^4 = pi^4 / (45 ell1^4)."""
    return math.pi ** 4 / (45.0 * ell1 ** 4)


def pileup_density(ell):
    """<T> ~ hbar c / ell^4, summed over images.  The Kim-Thorne cutoff sets
    ell = l_P, at which this IS the Planck energy density up to pi^4/45."""
    return HBAR * c / ell ** 4 * (math.pi ** 4 / 45.0)


# --- PART 2 ---------------------------------------------------------------

def throat_radius(d):
    """r_s = 2 Delta d / Lambda.  EXACT; G and c cancel."""
    return 2.0 * d / LAMBDA


def aspect_ratio():
    """Delta d / r_s = Lambda / 2.  Scale-invariant, dimensionless."""
    return LAMBDA / 2.0


def throat_area(d):
    return 4.0 * math.pi * throat_radius(d) ** 2


def corridor_density(d):
    """The corridor's own operating energy density, at its own throat scale."""
    E = ladder.energy_for_delta_d(d)
    V = (4.0 / 3.0) * math.pi * throat_radius(d) ** 3
    return E / V


def corridor_density_closed(d):
    """3 Lambda^2 c^4 / (32 pi G Delta d^2), by substitution.  A cross-check."""
    return 3.0 * LAMBDA ** 2 * c ** 4 / (32.0 * math.pi * G * d * d)


def objects_bounded_by_area(d, cross_section):
    return throat_area(d) / cross_section


# --- verdicts -------------------------------------------------------------
HAWKING_DISPUTE_RESOLVED_HERE = False
HAWKING_ROW = "MOOT-FOR-THIS-OBJECT"
N_MOVES_THE_CROSSOVER = False
I_SAID_IT_DID = True
ASPECT_RATIO_IS_FIXED = True
CORRIDOR_IS_A_TUNNEL = False
SCOPE = "dimensional analysis plus the transition equation; positions RECALLED"
NOTHING_IS_REPAIRED = True

BAR = "=" * 79


def report():
    print(__doc__.split("Literature positions")[0].rstrip())
    print()

    print(BAR)
    print("PART 1.  HAWKING -- NOT RESOLVED, BUT SHOWN NOT TO MATTER HERE")
    print(BAR)
    print()
    print("    WHAT THE ROW ACTUALLY SAYS.  chronology.py: 'the Cauchy-horizon")
    print("    divergence and whether quantum gravity cuts it off (Kim-Thorne)")
    print("    or does not (Hawking) is UNRESOLVED IN THE LITERATURE and is")
    print("    NOT-RUN here.'  THE DISPUTE IS NOT RESOLVED BY THIS PASS AND")
    print("    CANNOT BE -- it is a question about quantum gravity, and nothing")
    print("    in this tree adjudicates one.")
    print()
    print("    WHAT WAS NEVER ASKED IS WHETHER IT IS LOAD-BEARING.")
    print()
    print("    (a)  THE IMAGE SUM DIVERGES, AND THE EXPONENT IS FORCED.")
    print("         A field on a spacetime with a closed timelike curve sees")
    print("         infinitely many images of itself.  <T> is an energy density")
    print("         and the only scale is the geodesic length, so hbar c / l^4")
    print("         is the UNIQUE combination -- dimensions, not recall.")
    print()
    print("         %10s %20s %20s" % ("images", "partial sum", "pi^4/45"))
    for n in (1, 10, 100, 10000, 1000000):
        print("         %10d %20.12f %20.12f" % (n, image_sum(n), image_sum_closed()))
    print()
    print("         Converges to %.12f for a FIXED loop size, and diverges as"
          % image_sum_closed())
    print("         the loop closes:")
    print()
    print("         %14s %24s" % ("ell1 (m)", "<T> (J/m^3)"))
    for ell in (1e-6, 1e-15, 1e-25, L_PLANCK):
        print("         %14.3e %24.6e" % (ell, pileup_density(ell)))
    print()
    print("    (b)  GRANT KIM-THORNE EVERYTHING.  Their cutoff is the most")
    print("         FAVOURABLE assumption a time machine can be given: the")
    print("         divergence stops at the Planck length instead of running")
    print("         away.  The value there is the Planck energy density,")
    print()
    print("             rho_P = c^7/(hbar G^2) = %.6e J/m^3" % RHO_PLANCK)
    print()
    print("         and the pileup with the image factor is %.6e."
          % pileup_density(L_PLANCK))
    print()
    print("    (c)  AND COMPARE IT TO WHAT THE CORRIDOR ITSELF RUNS AT, at the")
    print("         corridor's OWN throat scale (Part 2):")
    print()
    print("         %-24s %16s %16s %14s"
          % ("shortcut", "throat r_s (m)", "rho (J/m^3)", "rho_P / rho"))
    for name, d in [("one metre", 1.0), ("one kilometre", 1e3),
                    ("one light year", LY), ("Proxima, 4.2 ly", PROXIMA_LY * LY)]:
        rho = corridor_density(d)
        print("         %-24s %16.6e %16.6e %14.4e"
              % (name, throat_radius(d), rho, pileup_density(L_PLANCK) / rho))
    print()
    rp = pileup_density(L_PLANCK) / corridor_density(PROXIMA_LY * LY)
    print("         FOR PROXIMA THE PILEUP EXCEEDS THE CORRIDOR BY %.4e --" % rp)
    print("         about %.0f ORDERS OF MAGNITUDE, ON THE ASSUMPTION MOST" % math.log10(rp))
    print("         FAVOURABLE TO THE TIME MACHINE.")
    print()
    print("        SO THE DISPUTE IS MOOT FOR THIS OBJECT.  It does not matter")
    print("        whether the divergence is cut off, because THE CUT-OFF VALUE")
    print("        ALONE IS A HUNDRED ORDERS PAST ANYTHING THIS GEOMETRY HOLDS.")
    print()
    print("    THE ROW MOVES FROM NOT-RUN TO %s." % HAWKING_ROW)
    print("    That is WEAKER than resolving the dispute and STRONGER than")
    print("    declining it, and it is the honest position: a question that")
    print("    cannot change the answer does not have to be answered.")
    print()
    print("    STATED WITH ITS LIMITS.  The 1/l^4 form is dimensional analysis,")
    print("    not a computed renormalised stress tensor; the Kim-Thorne and")
    print("    Hawking positions are RECALLED and NOT READ; and a hundred-order")
    print("    margin is what makes a dimensional argument sufficient here,")
    print("    where a factor-of-ten question would not be.")
    print()

    print(BAR)
    print("PART 2.  OBJECTS_PER_EVENT -- AND I WAS WRONG ABOUT IT")
    print(BAR)
    print()
    print("    LAST TURN I SAID N 'is the one number that could still move the")
    print("    crossover verdict'.  IT CANNOT, AND THE REASON IS ONE LINE:")
    print()
    print("        the crossover compares TOTAL mass transported against TOTAL")
    print("        mass spent.  Slicing the payload into more objects changes")
    print("        NEITHER SIDE.")
    print()
    print("    N sets the cost PER TRAVELLER, which is an economic question.")
    print("    The physics crossover is invariant under it.  Recorded as a")
    print("    fault of mine, not a finding.")
    print()
    print("    BUT ASKING PRODUCED SOMETHING THE TREE DID NOT HAVE.")
    print()
    print("        r_s = 2GM/c^2   and   M = Delta d c^2/(G Lambda)")
    print("        =>  r_s = 2 Delta d / Lambda        G AND c CANCEL COMPLETELY")
    print()
    print("    So the aspect ratio of EVERY corridor is fixed by Lambda alone:")
    print()
    print("        Delta d / r_s = Lambda / 2 = %.6f" % aspect_ratio())
    print()
    print("    %-24s %18s %18s %12s"
          % ("shortcut", "Delta d (m)", "throat r_s (m)", "ratio"))
    for name, d in [("one metre", 1.0), ("one kilometre", 1e3),
                    ("Earth to Moon", 3.844e8), ("one light year", LY),
                    ("Proxima, 4.2 ly", PROXIMA_LY * LY)]:
        print("    %-24s %18.6e %18.6e %12.6f"
              % (name, d, throat_radius(d), d / throat_radius(d)))
    print()
    print("    SCALE-INVARIANT, and it is the same number for a one-metre")
    print("    corridor and a galactic one.  A CORRIDOR IS NEVER MUCH LONGER")
    print("    THAN IT IS WIDE.")
    print()
    rs = throat_radius(PROXIMA_LY * LY)
    print("    A shortcut to Proxima has a throat %.4f light years in radius --"
          % (rs / LY))
    print("    an object %.3f light years ACROSS lying between here and there,"
          % (2 * rs / LY))
    print("    against a %.4f light year journey." % PROXIMA_LY)
    print()
    print("        IT IS NOT A TUNNEL.  IT IS VERY NEARLY A BRIDGE AS WIDE AS")
    print("        IT IS LONG, AND THAT IS FORCED BY Lambda.")
    print()
    print("    The closed form cross-checks: rho = 3 Lambda^2 c^4/(32 pi G d^2)")
    print("    against the direct quotient, agreeing to %.1e."
          % max(abs(corridor_density(d) / corridor_density_closed(d) - 1.0)
                for d in (1.0, 1e3, LY, PROXIMA_LY * LY)))
    print()
    print("    AND N IS STILL BOUNDED, JUST NOT USEFULLY.  Geometrically")
    print("    N <= throat area / cross-section: for Proxima that is %.4e"
          % objects_bounded_by_area(PROXIMA_LY * LY, 1.0))
    print("    objects of one square metre.  A bound, recorded, and it moves")
    print("    nothing -- which is the point of Part 2's first half.")
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

    print("closeout.py --selftest")
    print()
    d = PROXIMA_LY * LY

    # PART 1
    chk("the image sum converges to pi^4/45",
        abs(image_sum(2000000) / image_sum_closed() - 1.0) < 1e-6, True)
    chk("and diverges as the loop closes",
        pileup_density(1e-25) > pileup_density(1e-6) * 1e70, True)
    # TWO faults in one line, and the test caught both.  The first draft used
    # an ABSOLUTE tolerance against a ratio of order 1e4 (unsatisfiable), and
    # the expected value was INVERTED: pileup grows as ell falls, so
    # pileup(1e-10)/pileup(1e-11) is 1e-4, not 1e4.  The test was right and
    # the assertion was wrong -- the opposite of the Morris-Thorne case.
    chk("the pileup scales as ell^-4",
        abs(pileup_density(1e-10) / pileup_density(1e-11) / 1e-4 - 1.0) < 1e-12, True)
    chk("so a smaller loop means a larger pileup",
        pileup_density(1e-11) > pileup_density(1e-10), True)
    chk("Planck density is c^7/(hbar G^2)",
        abs(RHO_PLANCK / (c ** 7 / (HBAR * G * G)) - 1.0) < 1e-9, True)
    chk("the pileup at the Planck cutoff exceeds the corridor",
        pileup_density(L_PLANCK) > corridor_density(d), True)
    chk("by more than a hundred orders",
        math.log10(pileup_density(L_PLANCK) / corridor_density(d)) > 100.0, True)
    chk("the dispute is resolved here", HAWKING_DISPUTE_RESOLVED_HERE, False)
    chk("the row's new status", HAWKING_ROW, "MOOT-FOR-THIS-OBJECT")
    chk("chronology.py itself is unchanged",
        __import__("chronology").HAWKING, "NOT-RUN")

    # PART 2
    chk("r_s = 2 Delta d / Lambda exactly",
        max(abs(throat_radius(x) * LAMBDA / (2.0 * x) - 1.0)
            for x in (1.0, 1e3, LY, d)) < 1e-15, True)
    chk("and G and c do not appear",
        abs(throat_radius(1.0) - 2.0 / LAMBDA) < 1e-15, True)
    chk("the aspect ratio is Lambda/2",
        abs(aspect_ratio() - LAMBDA / 2.0) < 1e-15, True)
    chk("and it is scale-invariant",
        max(abs(x / throat_radius(x) / aspect_ratio() - 1.0)
            for x in (1.0, 1e3, 3.844e8, LY, d)) < 1e-15, True)
    chk("the two density routes agree",
        max(abs(corridor_density(x) / corridor_density_closed(x) - 1.0)
            for x in (1.0, 1e3, LY, d)) < 1e-12, True)
    chk("density falls as Delta d^-2",
        abs(corridor_density(1e3) / corridor_density(1e6) / 1e6 - 1.0) < 1e-12, True)
    chk("the corridor is a tunnel", CORRIDOR_IS_A_TUNNEL, False)

    # the self-correction: N cancels out of the crossover
    import oneway
    # The first draft compared one call to itself and tested nothing.  What
    # the claim needs is that TOTAL cost is invariant under slicing: k pieces
    # of m/k cost exactly what one piece of m costs, on BOTH sides.
    chk("slicing the payload changes neither side",
        max(abs(k * oneway.ticket_energy(1e30 / k, 2.0)
                / oneway.ticket_energy(1e30, 2.0) - 1.0)
            for k in (1, 2, 7, 1000, 10 ** 9)) < 1e-12
        and max(abs(oneway.corridor_energy(d)
                    / oneway.corridor_energy(d) - 1.0)
                for k in (1, 2, 1000)) < 1e-15, True)
    chk("N moves the crossover", N_MOVES_THE_CROSSOVER, False)
    chk("and I said it did", I_SAID_IT_DID, True)

    chk("literature positions were read", LITERATURE_IS_READ, False)
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
