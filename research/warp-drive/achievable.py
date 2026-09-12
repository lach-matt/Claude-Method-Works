#!/usr/bin/env python3
"""
achievable.py -- is there a core that can actually be made?  NO.

M: "we have to determine our core, and it must be something achievable, not
something hypothetical."  That is the right demand and this file answers it, and
the answer is negative by sixty-five orders of magnitude at metre scale.  It is
also bounded by a THEOREM rather than by engineering, and the gap WIDENS with
size, which closes the escape this project has used more than once.

-- THE CENSUS OF KNOWN NEGATIVE ENERGY DENSITY --------------------------------
Everything real, and what bounds it:

  CASIMIR between boundaries      MEASURED.  rho = -pi^2 hbar c/(720 d^4).
  SQUEEZED VACUUM                 MEASURED (LIGO uses it).  Ford-Roman bounded.
  DYNAMICAL CASIMIR               MEASURED (Wilson 2011, superconducting circuit).
  HAWKING / UNRUH flux            analogue-measured; same family.
  VACUUM POLARISATION             MEASURED via the Lamb shift.

    ALL OF THEM OBEY ONE BOUND.  Ford & Roman's quantum inequality caps negative
    energy sustained over a scale L at

            |rho| <~ hbar c / L^4

    and Casimir is that bound saturated, not an exception to it.  This is a
    theorem about quantum field theory, not a limit of apparatus.

TWO THINGS THAT LOOK LIKE EXCEPTIONS AND ARE NOT, named because they are the
most likely next hope:

  DARK ENERGY has negative PRESSURE and POSITIVE energy density.  rho_Lambda > 0.
  It is the wrong sign of the wrong quantity.

  "EFFECTIVE NEGATIVE MASS" in BECs and metamaterials is a curvature of a
  DISPERSION RELATION -- how a quasiparticle responds to a force in a medium.
  It is not T_00, it does not gravitate, and it will not source a metric.  The
  same caution applies to negative-index metamaterials, which are about the
  refractive index.

-- THE PRICE, AND IT IS NOT CLOSE ---------------------------------------------
concentric.py's device at corridor radius b needs a core of size a = 0.02 b
carrying mass m/b >~ 5e-3, so its energy density is

        required  =  (m/b) c^4 / [ G b^2 (4/3) pi (0.02)^3 ]  ~  1.81e46 / b^2  Pa

against what the quantum bound allows over the core's own size:

        available =  hbar c / (0.02 b)^4  ~  1.98e-19 / b^4  Pa

        b               required (Pa)     available (Pa)    avail/req
        1 m             1.806e+46         1.976e-19         1.09e-65
        100 km          1.806e+36         1.976e-39         1.09e-75
        solar system    1.806e+22         1.976e-67         1.09e-89
        1 light-year    1.806e+14         1.976e-83         1.09e-97
        10 kly          1.806e+06         1.976e-99         1.09e-105

-- AND THE GAP WIDENS WITH SIZE, WHICH IS THE PART THAT MATTERS ---------------
Required falls as 1/b^2; available falls as 1/b^4.  So going bigger makes it
WORSE, by two powers.

    THAT CLOSES AN ESCAPE THIS PROJECT HAS USED REPEATEDLY.  seatindex.py found
    universal seating gets cheaper as 1/l -- long and weak beats short and
    strong.  concentric.py found the shell's delay gets cheap when the shell is
    far.  Both were "go bigger".  HERE GOING BIGGER LOSES, and there is no
    large-scale corner to retreat to.

The two curves cross only at

        b = 3.31e-33 m,   core size a = 6.62e-35 m  =  4.09 PLANCK LENGTHS

    THIRD INDEPENDENT ROUTE TO THE PLANCK SCALE.  corridor.py got there twice --
    the Unruh crossover at 5.33e-10 kg and the Casimir one at 0.132 Planck
    lengths -- and this is a different calculation about a different object
    arriving at the same place.  When three unrelated estimates land at the
    Planck scale, that is where the physics is, not where the arithmetic went.

And even taking the BOUND as though it were an apparatus:

        Casimir gap 10 nm (state of the art)  ->  needs b = 7.6e19 m  (8000 ly)
        Casimir gap 0.1 nm (atomic floor)     ->  needs b = 7.6e15 m  (0.8 ly)

    A core 0.02 of that is still 160 astronomical units of continuous
    atomic-separation vacuum apparatus, for the WEAKEST configuration in the
    window.  This is not an engineering programme.

-- WHAT THIS DOES AND DOES NOT SETTLE -----------------------------------------
IT DOES NOT RETRACT THE DEVICE.  concentric.py's configuration is a valid
solution: M_ADM = 0, a vacuum corridor, seats and leads over most of a decade,
a shell of ordinary matter that is radially stable for free, and a Type I core
whose exoticism is exactly one sign.  Every one of those stands.

WHAT IT SETTLES IS THAT THE CORE IS NOT BUILDABLE WITH KNOWN PHYSICS, and that
the shortfall is a theorem rather than a budget.  Naming that precisely is worth
more than another pass looking for a corner, because the corner is now measured
to be absent.

    THE HONEST STATEMENT OF THE PROJECT IS NOW ONE SENTENCE: a complete,
    self-consistent, stability-checked warp architecture whose single unmet
    requirement is a matter type no known physics provides, with the shortfall
    quantified at 65 orders of magnitude and shown to widen with scale.

NOT SETTLED: whether some physics beyond the standard framework supplies it.
That is a question this project cannot ask, and pretending otherwise would be
the failure mode every withdrawal in this tree was about.

stdlib only.  concentric.py supplies the device, seatindex.py the threshold,
corridor.py the two earlier Planck-scale crossings.
"""
import math, sys

HBAR_C = 1.054571817e-34 * 299792458.0
C_SI = 299792458.0
G_SI = 6.67430e-11
L_PLANCK = 1.616255e-35

M_OVER_B = 5.0e-3          # concentric.py's window, weakest end
A_OVER_B = 0.02            # the vacuum-corridor constraint


def required_density(b, m_over_b=M_OVER_B, a_over_b=A_OVER_B):
    """|rho| c^2 the core must carry, in Pa, at corridor radius b."""
    M = m_over_b * b * C_SI ** 2 / G_SI
    V = (4.0 / 3.0) * math.pi * (a_over_b * b) ** 3
    return M * C_SI ** 2 / V


def quantum_bound(L):
    """Ford-Roman: negative energy sustained over scale L is capped at hbar c/L^4."""
    return HBAR_C / L ** 4


def available_density(b, a_over_b=A_OVER_B):
    return quantum_bound(a_over_b * b)


def ratio(b):
    return available_density(b) / required_density(b)


def crossing_radius(m_over_b=M_OVER_B, a_over_b=A_OVER_B):
    """Where available meets required.  required ~ 1/b^2, available ~ 1/b^4."""
    k = m_over_b / ((4.0 / 3.0) * math.pi * a_over_b ** 3)
    return math.sqrt(HBAR_C / a_over_b ** 4 / (k * C_SI ** 4 / G_SI))


def casimir_density(gap):
    """The measured effect, at plate separation `gap`."""
    return (math.pi ** 2) * HBAR_C / (720.0 * gap ** 4)


def b_needed_for(rho_available, m_over_b=M_OVER_B, a_over_b=A_OVER_B):
    k = m_over_b / ((4.0 / 3.0) * math.pi * a_over_b ** 3)
    return math.sqrt(k * C_SI ** 4 / G_SI / rho_available)


# Things that look like exceptions and are not.
NOT_EXCEPTIONS = {
    "dark energy": "negative PRESSURE, positive energy density. Wrong sign of "
                   "the wrong quantity.",
    "effective negative mass (BEC, metamaterial)":
        "a curvature of a DISPERSION RELATION, not T_00. Does not gravitate.",
    "negative-index metamaterial":
        "the refractive index, not the energy density.",
}


def gap_widens_with_size(b1=1.0, b2=1.0e6):
    """required ~ 1/b^2 and available ~ 1/b^4, so bigger is worse."""
    return ratio(b2) < ratio(b1)


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-58s %16s %16s  %s" % (label, got, want, "ok" if good else "FAIL"))

    def near(label, got, want, tol):
        nonlocal ok
        good = abs(got / want - 1.0) <= tol
        ok &= good
        print("  %-58s %16.6g %16.6g  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("THE PRICE")
    print("     %14s %18s %18s %14s" % ("b", "required (Pa)", "available (Pa)", "avail/req"))
    for b, tag in ((1.0, "1 m"), (1.0e5, "100 km"), (1.0e12, "solar system"),
                   (1.0e16, "1 light-year")):
        print("     %14s %18.4e %18.4e %14.3e"
              % (tag, required_density(b), available_density(b), ratio(b)))
    near("shortfall at metre scale", ratio(1.0), 1.094e-65, 1e-3)
    chk("nowhere close at any scale tried",
        all(ratio(b) < 1e-60 for b in (1.0, 1e5, 1e12, 1e16)), True)

    print("\nAND THE GAP WIDENS WITH SIZE -- the 'go bigger' escape is closed")
    chk("bigger is worse", gap_widens_with_size(), True)
    near("required falls as 1/b^2", required_density(1.0) / required_density(10.0),
         100.0, 1e-9)
    near("available falls as 1/b^4", available_density(1.0) / available_density(10.0),
         1.0e4, 1e-9)
    print("       seatindex.py's 1/l saving and concentric.py's far shell were")
    print("       both 'go bigger'.  Here two powers run the other way.")

    print("\nTHE CROSSING IS AT THE PLANCK SCALE -- a third independent route")
    bc = crossing_radius()
    near("crossing corridor radius (m)", bc, 3.3079e-33, 1e-3)
    near("core size there, in Planck lengths", bc * A_OVER_B / L_PLANCK, 4.09, 1e-2)
    chk("which is Planck scale, not merely small",
        bc * A_OVER_B / L_PLANCK < 10.0, True)
    print("       corridor.py reached the Planck scale twice, by Unruh and by")
    print("       Casimir.  This is a third calculation about a different object")
    print("       landing in the same place.")

    print("\nEVEN TAKING THE BOUND AS AN APPARATUS")
    for gap, tag in ((1.0e-8, "10 nm, state of the art"),
                     (1.0e-10, "0.1 nm, atomic floor")):
        rho = quantum_bound(gap)
        b = b_needed_for(rho)
        print("     %24s  |rho| = %.3e Pa  ->  b = %.3e m = %.2e ly"
              % (tag, rho, b, b / 9.461e15))
    chk("the atomic floor still needs a corridor near a light-year",
        b_needed_for(quantum_bound(1.0e-10)) > 1.0e15, True)

    print("\nTWO THINGS THAT LOOK LIKE EXCEPTIONS AND ARE NOT")
    for k, v in NOT_EXCEPTIONS.items():
        print("     %-42s %s" % (k, v))
    chk("three of them, named so they are not reached for later",
        len(NOT_EXCEPTIONS), 3)

    print("\nWHAT IS NOT RETRACTED")
    import concentric, stability, core
    chk("the device still seats and leads", concentric.works(5.0e-3), True)
    chk("with M_ADM = 0", abs(concentric.adm_residual(5.0e-3)) < 1e-10, True)
    chk("a shell of ordinary matter",
        stability.dec_holds(*stability.device(0.1)), True)
    chk("radially stable for free",
        stability.V_second(*stability.device(0.1), beta2=0.0) > 0, True)
    chk("and a Type I core", core.classify_core(2.0e-2, 0.02, 0.02)[0], core.TYPE_I)
    print("       Every one of those stands.  What is settled is that the CORE")
    print("       is not buildable with known physics, and that the shortfall is")
    print("       a THEOREM rather than a budget.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1


def report():
    print(__doc__)
    print("=" * 79)
    print("THE PRICE")
    print("  %16s %18s %18s %14s" % ("b", "required (Pa)", "available (Pa)", "avail/req"))
    for b, tag in ((1.0, "1 m"), (1.0e3, "1 km"), (1.0e5, "100 km"),
                   (1.0e12, "solar system"), (1.0e16, "1 light-year"),
                   (1.0e20, "10 kly")):
        print("  %16s %18.4e %18.4e %14.3e"
              % (tag, required_density(b), available_density(b), ratio(b)))
    print("\n  crossing at b = %.4e m, core size %.2f Planck lengths"
          % (crossing_radius(), crossing_radius() * A_OVER_B / L_PLANCK))
    print("\n" + "=" * 79)
    print("VERDICT")
    print("  THERE IS NO ACHIEVABLE CORE.  Every known source of negative energy")
    print("  density obeys |rho| <~ hbar c / L^4, and the core needs 65 orders")
    print("  more than that at metre scale.  The gap WIDENS with size -- required")
    print("  falls as 1/b^2, available as 1/b^4 -- so the 'go bigger' escape this")
    print("  project used twice is closed here.  The curves cross at four Planck")
    print("  lengths, a third independent route to the same scale.")
    print("\n  THE DEVICE IS NOT RETRACTED: it seats and leads, M_ADM = 0, the")
    print("  shell is ordinary matter and stable, the core is Type I with a")
    print("  one-sign exoticism.  What is settled is that the core is not")
    print("  buildable with known physics, and that this is a theorem and not a")
    print("  budget.  Whether physics beyond the standard framework supplies it")
    print("  is a question this project cannot ask.")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
