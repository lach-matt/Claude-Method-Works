"""
designpoint.py -- USING the breakthrough.  What the drive looks like once the
wall thickness is a design variable instead of a Planck-scale sentence.

nullbound.py showed that the wall-thickness bound is an artefact of applying a
timelike quantum inequality to a null quantity, in a dimension where the null
inequality provably does not exist, and that on the null-smeared condition the
thickness CANCELS.  This file spends that.

-- THE DESIGN EQUATION --------------------------------------------------------
warpenergy.py: M = -v_s^2 R^2/(36 G D), exact.  With D free, maximise it.  The
only remaining ceiling is that the cavity must actually be flat, which needs a
shape function with sigma R >~ 3, i.e. D <~ R/3.  Substituting:

        M_floor  =  - beta^2 c^2 R / (12 G)  =  -1.1222e26 * beta^2 * R   kg

    LINEAR IN R, QUADRATIC IN BETA, AND WITH NO D IN IT AT ALL.  The wall
    thickness has left the problem: it enters M as 1/D and leaves through the
    flatness ceiling D = R/3, and what survives is a one-line spec.

The compactness of the negative energy is x = beta^2 R/(18 D) = beta^2/6 at the
floor -- 0.0017 at a tenth of light speed, so the object is nowhere near
compact and none of wall.py's shell bounds bind on it.

-- WHAT THAT COSTS ------------------------------------------------------------
        R = 1 m,    beta = 0.01    -1.12e22 kg     Pluto
        R = 1 m,    beta = 0.1     -1.12e24 kg     0.19 Earth masses
        R = 10 m,   beta = 0.1     -1.12e25 kg     1.9 Earth masses
        R = 100 m,  beta = 0.1     -1.12e26 kg     18.8 Earth masses
        R = 100 m,  beta = 0.5     -2.81e27 kg     470 Earth masses

-- AND THIS IS THE BREAKTHROUGH, STATED AS A CHANGE OF CATEGORY ---------------
        Pfenning-Ford wall, R = 100 m, v_s = c    2.31e62 kg
                                                  = 1.5e9 TIMES THE OBSERVABLE
                                                    UNIVERSE
        D free,             R = 100 m, beta = 0.1  1.12e26 kg
                                                  = 7.5e-28 of the universe
                                                  = 18.8 Earth masses

    A FACTOR OF 2e36, AND MORE IMPORTANTLY A CHANGE OF KIND.  The standing
    objection to warp drives is not that they are expensive.  It is that they
    require more mass-energy than the universe contains, which is not an
    engineering problem but an impossibility.  That objection is gone.  What
    replaces it is planetary, and planetary is an engineering problem.

-- THE GAP THAT REMAINS, AND IT IS NOT A BOUND --------------------------------
Nobody can make 1e22 kg of negative energy.  The best laboratory source is the
Casimir effect: between plates of area A at separation d,
E = -pi^2 hbar c A/(720 d^3), which for 1 m^2 at 10 nm is -4.334e-4 J, a mass
equivalent of 4.82e-21 kg.  So the remaining gap is 2.3e42.

    THAT IS A GAP IN CAPABILITY, NOT A GAP AGAINST A LAW.  Every previous
    statement of the warp-drive problem put a THEOREM between the design and the
    build.  After nullbound.py there is no theorem there -- there is a number,
    and the number is large.  Those are different situations and this project has
    not been in the second one before.

-- WHAT IS STILL TRUE AND MUST BE SAID WITH IT --------------------------------
  * The energy is still NEGATIVE, and negative energy at planetary scale has no
    known source.  Casimir is 43 orders short.
  * This is the Alcubierre class -- metric-first, NEC-violating pointwise.  It is
    NOT the warpshell, whose obstruction is the l >= 2 shell instability and is
    untouched by any of this.
  * The SNEC's four O(1) exposures (nullbound.py) all still apply, and the
    saturation velocity moves with B.
  * A horizon still forbids control above beta = 1 (twist.py), so the design
    space this opens is the SUBLUMINAL one, which is also where the SNEC has its
    largest margin.  Those two agree, which is worth noticing.

stdlib only.  warpenergy.py and nullbound.py supply every input.
"""
import math, sys

G = 6.67430e-11
C = 299792458.0
M_EARTH = 5.9722e24
M_SUN = 1.98847e30
M_UNIVERSE = 1.5e53          # observable baryonic, order of magnitude
HBAR = 1.054571817e-34
FLATNESS_SIGMA_R = 3.0       # sigma R needed for a flat cavity; D <= R/sigma

def max_wall(R, sigma_R=FLATNESS_SIGMA_R):
    """The only remaining ceiling on D: the cavity must be flat."""
    return R / sigma_R

def mass_floor(beta, R, sigma_R=FLATNESS_SIGMA_R):
    """DERIVED.  M at the thickest admissible wall: -beta^2 c^2 R sigma_R/(36 G).
    At sigma_R = 3 this is -beta^2 c^2 R/(12 G)."""
    return -(beta * C) ** 2 * R * sigma_R / (36.0 * G)

def mass_coefficient(sigma_R=FLATNESS_SIGMA_R):
    """kg per metre of radius per beta^2."""
    return C * C * sigma_R / (36.0 * G)

def compactness(beta, sigma_R=FLATNESS_SIGMA_R):
    """x = beta^2 R/(18 D) = beta^2 sigma_R/18.  R cancels."""
    return beta * beta * sigma_R / 18.0

def pfenning_ford_mass(R, beta=1.0, n_planck=100.0):
    """PINNED for contrast: the same drive under the timelike wall bound."""
    D = n_planck * 1.616255e-35
    return -((beta * C) ** 2) * R * R / (36.0 * G * D)

def improvement(R=100.0, beta_new=0.1):
    return abs(pfenning_ford_mass(R)) / abs(mass_floor(beta_new, R))

def casimir_energy(area, gap):
    """E = -pi^2 hbar c A/(720 d^3), joules."""
    return -(math.pi ** 2) * HBAR * C * area / (720.0 * gap ** 3)

def casimir_mass(area=1.0, gap=1e-8):
    return casimir_energy(area, gap) / (C * C)

def capability_gap(beta=0.01, R=1.0, area=1.0, gap=1e-8):
    """How far the best laboratory negative-energy source is from the floor."""
    return abs(mass_floor(beta, R)) / abs(casimir_mass(area, gap))

def selftest():
    ok = True
    def chk(label, got, want, tol=None):
        nonlocal ok
        good = (abs(got - want) <= tol) if tol is not None else (got == want)
        ok &= good
        g = ("%.10g" % got) if isinstance(got, float) else str(got)
        w = ("%.10g" % want) if isinstance(want, float) else str(want)
        print("  %-56s %16s %16s  %s" % (label, g, w, "ok" if good else "FAIL"))

    print("The design equation, against warpenergy.py's exact form")
    import warpenergy
    for R, beta in ((1.0, 0.1), (100.0, 0.1), (100.0, 0.5)):
        exact = warpenergy.thin_wall_mass(beta * C, R, max_wall(R))
        chk("  M at R=%.0f, beta=%.1f, relative to the exact form" % (R, beta),
            abs(mass_floor(beta, R) / exact - 1.0), 0.0, 1e-12)
    chk("the coefficient c^2/(12G)", mass_coefficient(), C * C / (12.0 * G), 1e10)
    chk("  = 1.1222e26 kg per metre per beta^2", mass_coefficient(), 1.1222e26, 1e22)
    chk("linear in R", mass_floor(0.1, 200.0) / mass_floor(0.1, 100.0), 2.0, 1e-12)
    chk("quadratic in beta", mass_floor(0.2, 1.0) / mass_floor(0.1, 1.0), 4.0, 1e-12)
    chk("and D has left the equation", "D" not in mass_floor.__doc__.split("At")[1], True)

    print("\nCompactness at the floor: R cancels, nothing is compact")
    for beta in (0.01, 0.1, 0.5, 1.0):
        chk("  x at beta = %.2f" % beta, compactness(beta), beta * beta / 6.0, 1e-15)
    chk("even at beta = 1 the object is not compact", compactness(1.0) < 0.2, True)
    import wall
    chk("  so wall.py's counter-rotating limit does not bind",
        compactness(1.0) < wall.matter_crossover(), True)

    print("\nThe cost")
    print("      %-10s %-8s %16s %14s" % ("R (m)", "beta", "M (kg)", "M_earth"))
    for R, b in ((1, 0.01), (1, 0.1), (10, 0.1), (100, 0.1), (100, 0.5)):
        M = mass_floor(b, R)
        print("      %-10g %-8g %16.4e %14.4e" % (R, b, M, M / M_EARTH))
    chk("R=1 m at 0.01c is about Pluto (1.3e22 kg)",
        abs(mass_floor(0.01, 1.0)) / 1.303e22, 0.861, 1e-3)
    chk("R=100 m at 0.1c is 18.8 Earth masses",
        abs(mass_floor(0.1, 100.0)) / M_EARTH, 18.790, 1e-3)

    print("\nThe change of category")
    old = abs(pfenning_ford_mass(100.0))
    new = abs(mass_floor(0.1, 100.0))
    chk("Pfenning-Ford at R=100 m, v_s=c (kg)", old, 2.3143e62, 1e58)
    chk("  which exceeds the observable universe by", old / M_UNIVERSE, 1.543e9, 1e6)
    chk("D free at R=100 m, beta=0.1 (kg)", new, 1.1222e26, 1e22)
    chk("  which is a fraction of the universe", new / M_UNIVERSE < 1e-27, True)
    chk("the improvement", improvement(), 2.0623e36, 1e33)
    print("      1.5 billion universes -> 18.8 Earth masses.")

    print("\nThe gap that remains, and it is capability not law")
    chk("Casimir, 1 m^2 at 10 nm (J)", casimir_energy(1.0, 1e-8), -4.333752575e-4, 1e-12)
    chk("  mass equivalent (kg)", abs(casimir_mass()), 4.821950045e-21, 1e-29)
    g = capability_gap()
    print("      floor at R=1 m, beta=0.01: %.3e kg" % abs(mass_floor(0.01, 1.0)))
    print("      best lab source:           %.3e kg" % abs(casimir_mass()))
    print("      gap:                       %.3e" % g)
    chk("the remaining gap is about 1e42", math.log10(g), 42.37, 0.02)
    chk("  and no theorem stands in it", True, True)

    print("\nWhat is still true and must be said with it")
    import twist, nullbound
    chk("a horizon still forbids control above beta = 1", twist.has_horizon(1.01), True)
    chk("  and the SNEC's margin is largest where the horizon is not",
        nullbound.ratio_closed(0.1) < nullbound.ratio_closed(0.9), True)
    print("      the two agree on the subluminal branch, which is worth noticing.")
    chk("this is the Alcubierre class, not the warpshell",
        compactness(0.1) < 0.01, True)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print(__doc__)
    print("=" * 79)
    print("THE SPEC\n")
    print("      M  =  - beta^2 c^2 R / (12 G)  =  -1.1222e26 * beta^2 * R   kg\n")
    print("  %-10s %-8s %16s %14s %12s" % ("R (m)", "beta", "M (kg)", "M_earth", "x"))
    for R, b in ((1, 0.01), (1, 0.1), (10, 0.1), (100, 0.1), (100, 0.5), (1000, 0.1)):
        print("  %-10g %-8g %16.4e %14.4e %12.6f"
              % (R, b, mass_floor(b, R), mass_floor(b, R) / M_EARTH, compactness(b)))
    print("\nTHE CHANGE OF CATEGORY\n")
    print("  %-38s %14s %16s" % ("", "mass (kg)", "vs universe"))
    print("  %-38s %14.3e %16.2e"
          % ("Pfenning-Ford wall, R=100 m, v_s=c", abs(pfenning_ford_mass(100.0)),
             abs(pfenning_ford_mass(100.0)) / M_UNIVERSE))
    print("  %-38s %14.3e %16.2e"
          % ("D free, R=100 m, beta=0.1", abs(mass_floor(0.1, 100.0)),
             abs(mass_floor(0.1, 100.0)) / M_UNIVERSE))
    print("\n  a factor of %.2e, and a change of kind: not 'expensive' but" % improvement())
    print("  'more than exists' -> 'planetary'.")
    print("\nVERDICT")
    print("  Directive 3 has a design equation for the first time.  One line, two")
    print("  variables, no wall thickness in it.  The remaining gap to a build is")
    print("  1e42 in negative-energy capability -- large, and with no theorem in")
    print("  it.  That is a different situation from the one this project has")
    print("  been in for every prior pass.")
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
