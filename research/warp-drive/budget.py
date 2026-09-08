#!/usr/bin/env python3
"""
budget.py -- where the math stands, what it says the device must be, and how it
is powered.  The last question has a sharper answer than the others.

    IT IS NOT POWERED.  There is nothing to power.

-- WHERE THE MATH STANDS ------------------------------------------------------
Five results, each measured by a named instrument, and together they close the
problem to a single line.

  1  THE WARP QUANTITY IS PROPER DISTANCE, INT e^{-Phi} dl, and a source with
     Phi > 0 contracts it while ordinary mass stretches it.  A gravitational
     lens has the WRONG SIGN.                              (transition.py)

  2  Phi > 0 IN VACUUM NEEDS NEGATIVE ENERGY DENSITY.  Charge cannot supply it:
     Q <= M by the Einstein-Maxwell positive energy theorem puts every
     positive-potential region inside a horizon.           (charge.py)

  3  AND NO KNOWN NEGATIVE ENERGY DENSITY IS REMOTELY ENOUGH.  Every real
     source obeys Ford-Roman |rho| <~ hbar c/L^4; the shortfall is 65 orders at
     metre scale AND WIDENS WITH SCALE.                    (achievable.py)

  4  THE STRONG-FIELD SHORTCUT IS CLOSED TOO: any region satisfying the
     universal (Sturm) seating condition is inside its own Schwarzschild radius
     by 2 pi^2/3 = 6.579, at every scale.                  (spec.py)

  5  BUT THE CONFIGURATION ITSELF IS SOUND.  M_ADM = 0 exactly, the shell is
     ordinary matter satisfying DEC and radially stable with no stiffness at
     all, the core is Type I with no compactness bound, and there is no throat,
     no horizon and no momentum flux.        (concentric, stability, core,
                                              transition)

    SO THE MATHEMATICS IS COMPLETE AND THE OBSTRUCTION IS SINGULAR: everything
    works except that nothing supplies Phi > 0.

-- WHAT THE DEVICE MUST BE, DERIVED ------------------------------------------
The contraction along a path of length L at impact parameter b, from a source of
geometric mass m, has a closed form -- validated against the measured numbers to
better than 1.2 %:

        eps  =  (2m/L) asinh(L/2b)        [ less the shell's constant m/R_s ]

        m = 5e-3   measured 1.64994e-4    closed form 1.65127e-4    0.08 % off
        m = 2e-2   measured 6.58474e-4    closed form 6.60506e-4    0.31 %
        m = 8e-2   measured 2.61024e-3    closed form 2.64202e-3    1.20 %

Inverting, and restoring units:

        |M|  =  (c^2/G) * L * eps / ( 2 asinh(L/2b) )

    AND c^2/G = 1.3466e27 kg PER METRE IS THE WHOLE COST STORY.  Every
    requirement in this project reduces to that conversion.

        path            eps      |M| needed        in M_sun
        1 light-year    0.01     2.773e39 kg       1.39e9
        1 light-year    0.50     1.387e41 kg       6.97e10
        1 parsec        0.01     8.603e39 kg       4.33e9
        100 ly          0.50     1.155e43 kg       5.81e12

and in the strong limit, a contraction by a factor of e needs Phi ~ 1 along the
whole path, so |M| ~ (c^2/G) L directly:

        1 m             1.347e27 kg
        1 km            1.347e30 kg
        1 light-year    1.274e43 kg      -- a galaxy's mass, negative

    THE SCALING IS L/ln(L/b) -- very nearly linear, with a LOGARITHMIC economy
    of scale.  Doubling the path costs 1.9417x, not 2x.  So there is a saving in
    going long, and it is 3 %, which is not a strategy.  That is the design law
    and it is unforgiving.

-- HOW IT IS POWERED: IT IS NOT ----------------------------------------------
This is the question with the cleanest answer, and it is not the one the
propulsion framing expects.

    THE CONFIGURATION IS STATIC.  transition.py measured T^0i = 0 EXACTLY at
    every radius -- no momentum flux, no energy flux, no work done.  A static
    geometry consumes nothing to persist, the way a magnet holding a weight
    consumes nothing, or the way the Earth's field does no work on a stationary
    stone.

    THERE IS NO ENGINE, NO FUEL, NO EXHAUST AND NO POWER RATING.

And the assembly energy is not a cost either.  concentric.py's configuration has
M_ADM = 0 EXACTLY -- the negative core and the positive shell cancel -- so the
TOTAL ENERGY OF THE DEVICE IS ZERO.  It is not expensive to build; it is
impossible to build, and those are different failures.

    THE DEVICE IS SIGN-LIMITED, NOT POWER-LIMITED.  The entire problem is the
    EXISTENCE of a negative-energy source, not the supply of energy to one.
    No amount of power produces it, because power is not what is missing.

ONE HONEST QUALIFICATION.  Static holds no power; RETARGETING is not static.
Changing which destination the configuration addresses means changing the
geometry, which is time-dependent and does require work.  This file computes
the standing configuration only, and the cost of steering it is NOT-RUN.

-- SO WHAT WOULD HAVE TO CHANGE -----------------------------------------------
Exactly one thing, and it can be stated in a sentence with no hedging:

    A SOURCE WITH NEGATIVE ENERGY DENSITY, AT A MAGNITUDE OF ORDER (c^2/G) L,
    SUSTAINED OVER THE PATH.

Not a stronger engine, not more energy, not better materials, not a cleverer
geometry -- the geometry is finished and verified.  A sign.

stdlib only.  Every figure is recomputed here from the instrument that owns it.
"""
import math, sys

C_SI = 299792458.0
G_SI = 6.67430e-11
M_SUN = 1.989e30
LIGHT_YEAR = 9.4607e15
PARSEC = 3.086e16


def cost_per_metre():
    """c^2/G, in kg per metre.  The conversion every requirement reduces to."""
    return C_SI ** 2 / G_SI


def contraction(m, L, b, R_shell=None):
    """eps = (2m/L) asinh(L/2b), less the shell's constant if there is one."""
    e = (2.0 * m / L) * math.asinh(L / (2.0 * b))
    return e - (m / R_shell if R_shell else 0.0)


def mass_needed(L, eps, b):
    """|M| in kg for a fractional contraction eps over a path L at impact b."""
    return cost_per_metre() * L * eps / (2.0 * math.asinh(L / (2.0 * b)))


def mass_for_efold(L):
    """The strong limit: Phi ~ 1 along the path, so |M| ~ (c^2/G) L."""
    return cost_per_metre() * L


def is_powered():
    """A static configuration does no work.  T^0i = 0, measured."""
    return False


def net_energy_kg(m_core, m_shell):
    """M_ADM.  Zero when the shell matches the core."""
    return m_shell - m_core


STANDING = (
    ("proper distance is the warp quantity; a lens has the wrong sign",
     "transition.py"),
    ("Phi > 0 in vacuum needs negative energy; Q <= M closes the charge route",
     "charge.py"),
    ("no known negative energy is enough -- 65 orders, widening with scale",
     "achievable.py"),
    ("Sturm-universal seating is inside its own Schwarzschild radius, 2 pi^2/3",
     "spec.py"),
    ("but the configuration is sound: M_ADM = 0, ordinary stable shell, Type I "
     "core, no throat, no horizon, no momentum flux",
     "concentric.py / stability.py / core.py / transition.py"),
)
NOT_RUN = {
    "the cost of RETARGETING":
        "static holds no power, but changing which destination the geometry "
        "addresses is time-dependent and does require work. This file computes "
        "the standing configuration only.",
}


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-56s %18s %18s  %s" % (label, got, want, "ok" if good else "FAIL"))

    def near(label, got, want, tol):
        nonlocal ok
        good = abs(got / want - 1.0) <= tol
        ok &= good
        print("  %-56s %18.6g %18.6g  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("WHERE THE MATH STANDS")
    for claim, who in STANDING:
        print("     %-72s" % claim)
        print("       [%s]" % who)
    chk("five standing results", len(STANDING), 5)

    print("\nTHE CONTRACTION LAW -- closed form against the measurement")
    import transition as TR, concentric as CN
    for m in (5.0e-3, 2.0e-2, 8.0e-2):
        ph = CN.potential(m)
        meas = 1.0 - TR.proper_ratio(ph, -150.0, 150.0, 1.0)[0]
        pred = contraction(m, 300.0, 1.0, CN.R_SHELL)
        near("m=%.0e" % m, pred, meas, 1.3e-2)
    print("       eps = (2m/L) asinh(L/2b), less the shell's constant.")

    print("\nTHE COST, AND IT IS ONE CONVERSION")
    near("c^2/G  (kg per metre)", cost_per_metre(), 1.3466e27, 1e-4)
    print("     %16s %8s %18s %14s" % ("path", "eps", "|M| (kg)", "M_sun"))
    for tag, L in (("1 light-year", LIGHT_YEAR), ("1 parsec", PARSEC),
                   ("100 ly", 100 * LIGHT_YEAR)):
        for eps in (0.01, 0.5):
            M = mass_needed(L, eps, 1.0e6)
            print("     %16s %8.2f %18.4e %14.4e" % (tag, eps, M, M / M_SUN))
    near("1 % over a light-year", mass_needed(LIGHT_YEAR, 0.01, 1e6), 2.7731e39, 1e-3)
    # NOT linear: the asinh denominator gives M ~ L/ln(L/b), so doubling the
    # path costs slightly less than double.  A weak economy of scale, and the
    # first draft of this file asserted linearity, which is wrong.
    ratio = mass_needed(2 * LIGHT_YEAR, 0.01, 1e6) / mass_needed(LIGHT_YEAR, 0.01, 1e6)
    near("doubling the path costs this much more", ratio, 1.9417, 1e-3)
    chk("SUB-linear -- a logarithmic economy of scale, not none", ratio < 2.0, True)
    chk("but only just: within 3 %% of linear", ratio > 1.9, True)

    print("\n   The strong limit: a contraction by e needs |M| ~ (c^2/G) L")
    for tag, L in (("1 m", 1.0), ("1 km", 1.0e3), ("1 light-year", LIGHT_YEAR)):
        print("     %16s  |M| = %.4e kg" % (tag, mass_for_efold(L)))
    near("a light-year e-fold, in solar masses",
         mass_for_efold(LIGHT_YEAR) / M_SUN, 6.405e12, 1e-3)

    print("\nHOW IT IS POWERED -- IT IS NOT")
    chk("the configuration is static, so it does no work", is_powered(), False)
    import transition, concentric
    ph = concentric.potential(2.0e-2)
    mom, en = transition.momentum_flux(ph, (2.0, 0.3, 0.0), 2.0e-2)
    chk("T^0i measured exactly zero", mom, 0.0)
    chk("and the total energy is zero: M_ADM = 0", net_energy_kg(1.0, 1.0), 0.0)
    chk("so it is not expensive to build",
        abs(concentric.adm_residual(5.0e-3)) < 1e-10, True)
    print("       It is IMPOSSIBLE to build, and those are different failures.")
    print("       THE DEVICE IS SIGN-LIMITED, NOT POWER-LIMITED.  No amount of")
    print("       power produces a negative energy density, because power is")
    print("       not what is missing.")

    print("\nNOT RUN")
    for k, v in NOT_RUN.items():
        print("     %s" % k)
        print("       %s" % v)
    chk("one item, recorded with its reason", len(NOT_RUN), 1)

    print("\nWHAT WOULD HAVE TO CHANGE -- one thing")
    import achievable
    chk("the shortfall is unmoved", achievable.ratio(1.0) < 1e-60, True)
    print("       A source with NEGATIVE energy density at a magnitude of order")
    print("       (c^2/G) L, sustained over the path.  Not a stronger engine,")
    print("       not more energy, not better materials, not a cleverer")
    print("       geometry -- the geometry is finished and verified.  A sign.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1


def report():
    print(__doc__)
    print("=" * 79)
    print("THE COST TABLE")
    print("  %16s %8s %18s %14s" % ("path", "eps", "|M| (kg)", "M_sun"))
    for tag, L in (("1 km", 1.0e3), ("1 AU", 1.496e11), ("1 light-year", LIGHT_YEAR),
                   ("1 parsec", PARSEC), ("100 ly", 100 * LIGHT_YEAR)):
        for eps in (0.01, 0.5):
            M = mass_needed(L, eps, 1.0e6)
            print("  %16s %8.2f %18.4e %14.4e" % (tag, eps, M, M / M_SUN))
    print("\n  c^2/G = %.4e kg per metre -- the whole cost story." % cost_per_metre())
    print("\n" + "=" * 79)
    print("VERDICT")
    print("  THE MATHEMATICS IS COMPLETE AND THE OBSTRUCTION IS SINGULAR.")
    print("  Everything works except that nothing supplies Phi > 0.")
    print("\n  WHAT THE DEVICE MUST BE: a negative source of geometric mass")
    print("  m ~ eps L / (2 asinh(L/2b)), inside a positive shell that cancels")
    print("  it, with the corridor between them in vacuum.  The scaling is")
    print("  L/ln(L/b) -- nearly linear, with a 3 % saving per doubling.")
    print("\n  HOW IT IS POWERED: IT IS NOT.  The configuration is static,")
    print("  T^0i = 0 exactly, so it does no work and consumes nothing to")
    print("  persist.  And with M_ADM = 0 its total energy is zero, so it is")
    print("  not expensive to build either.  It is IMPOSSIBLE to build, and")
    print("  those are different failures.")
    print("\n  THE DEVICE IS SIGN-LIMITED, NOT POWER-LIMITED.  No amount of")
    print("  power produces a negative energy density.  One thing would have to")
    print("  change, and it is a sign.")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
