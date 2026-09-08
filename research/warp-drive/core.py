#!/usr/bin/env python3
"""
core.py -- what the core has to be.

M: "the core is part of the exotic matter identification phase that happens in
tandem with the build design phase", and then: "we need to identify the core
material to accurately measure stability."  Both are right, and the second is
right for a specific reason -- the l >= 2 analysis needs a boundary condition at
the inner edge of the vacuum region, and that boundary condition IS the core's
response to a non-spherical perturbation.  Running l >= 2 against an
unspecified core would be fitting a free function.

So: the core, specified.  Three results, and the first two are simplifications.

-- 1. THE CORE IS HAWKING-ELLIS TYPE I, AND IT IS MEASURED ---------------------
Martin-Moruno & Visser force Type I for STATIC configurations, and this core is
static and spherically symmetric.  Measured directly on concentric.py's metric
with typefour.py's classifier:

        r          ||T||        max|Im eig|      ratio
        0.005      7.501e+2     7.879e-5         1.05e-7   TYPE I
        0.020      1.347e+3     1.452e-5         1.08e-8   TYPE I
        0.050      4.435e+2     8.705e-6         1.96e-8   TYPE I

    THE TYPE IV PROBLEM DOES NOT APPLY TO THIS DEVICE.  It dominated the middle
    of this project -- typefour.py, universal.py, selfconsistent.py -- and the
    architecture that replaced the Alcubierre bubble does not inherit it.  The
    core has a rest frame, an energy density and pressures, like ordinary matter.

-- 2. BUT concentric.py's METRIC CANNOT DESCRIBE THE CORE, AND SAYS SO ---------
Phi_max = m/a across concentric.py's window is 0.25 (at m = 5e-3) to 1.0 (at
m = 2e-2), and at Phi = 1 the linearised spatial metric (1 - 2 Phi) has FLIPPED
SIGN.  The CORRIDOR is fine -- Phi ~ 0.02 at r = 1, where the geodesics and the
focusing live -- but the core interior is outside its own metric's validity, and
a density read off it disagrees with the analytic Plummer by a factor of 667 at
r = 2a.  So the core is specified below from an EXACT solution, not that one.

    THIS IS A REAL TENSION, NOT A CHOICE OF METHOD.  The vacuum corridor wants
    b/a >~ 50, so a <~ 0.02; the window wants m >~ 5e-3; and Phi_max = m/a is
    then at least 0.25 across the whole window.  THE CORE IS INTRINSICALLY A
    STRONG-FIELD OBJECT in this design and no weak-field description of it will
    do.

-- 3. THE EXACT CORE, AND THE ONLY EXOTIC THING ABOUT IT IS ONE SIGN ----------
Take the interior Schwarzschild solution -- constant density, exact, no
expansion -- and give it NEGATIVE density:

        p(r) = rho [ sqrt(1 - 2M r^2/R^3) - sqrt(1 - 2M/R) ]
                   / [ 3 sqrt(1 - 2M/R) - sqrt(1 - 2M r^2/R^3) ]

with M = (4/3) pi rho R^3 < 0.  Three things follow, and each is a specification.

  THERE IS NO BUCHDAHL LIMIT.  For positive density the central pressure
  diverges at R = 9M/4 and that is what bounds a star.  Here 1 - 2M r^2/R^3 =
  1 + 2|M| r^2/R^3 > 1 for every r, so every square root is real and the
  denominator never vanishes.  Measured finite at compactness 2|M|/R = 83.8.
  NEGATIVE MASS HAS NO COMPACTNESS BOUND, which is exactly what a core needing
  b/a >~ 50 requires.

  THE PRESSURE IS POSITIVE AND CAPPED AT |rho|/3.  p > 0 throughout, largest at
  the centre, zero at the surface.  As |M|/R -> infinity, p(0)/|rho| -> 1/3 FROM
  BELOW -- the radiation value, approached and never exceeded:

        2|M|/R      p(0)/|rho|
        0.084       0.0193
        0.838       0.1160
        8.378       0.2519
        83.78       0.3083     ->  1/3

  SO THE MATERIAL IS EXOTIC IN EXACTLY ONE RESPECT.  Every energy condition
  fails, and all of them fail for the same reason: rho < 0.  The PRESSURES are
  entirely ordinary -- isotropic, positive, and bounded by |rho|/3, which is
  what radiation does.  Flip the sign of rho and this material satisfies the
  dominant energy condition.

    THAT IS THE IDENTIFICATION TARGET, STATED AS NARROWLY AS THIS PROJECT CAN
    STATE IT: a static, spherically symmetric, ISOTROPIC Type I fluid with
    negative energy density and positive pressure not exceeding |rho|/3.  Not a
    no-rest-frame object, not an anisotropic one, not one needing a pressure
    larger than radiation's.  One sign, and nothing else.

-- WHAT IS NOT SETTLED --------------------------------------------------------
 1. CONSTANT DENSITY IS INCOMPRESSIBLE, so its sound speed is formally
    infinite.  That is the known pathology of the constant-density star,
    positive or negative, and it means this is a BOUNDING MODEL rather than a
    physical equation of state.  A realistic EOS is the identification phase's
    job and is NOT-RUN here.
 2. NO CANDIDATE MATERIAL IS PROPOSED.  This file says what the core must DO,
    not what it is.  Per M, identification runs in tandem and afterwards.
 3. THE l >= 2 BOUNDARY CONDITION IS NOW POSABLE BUT NOT POSED.  Knowing the
    core is Type I, isotropic and incompressible fixes how it answers a
    non-spherical perturbation at leading order; using that is the next pass,
    not this one.
 4. Whether a negative-density fluid is stable AS A FLUID -- its own internal
    modes -- is untouched.

stdlib only.  typefour.py supplies the Hawking-Ellis classifier, composite.py
and concentric.py the metric whose limits are reported above.
"""
import math, sys

TYPE_I, TYPE_IV = "TYPE-I", "TYPE-IV"


def mass_of(rho, R):
    """M = (4/3) pi rho R^3.  Negative when rho is."""
    return (4.0 / 3.0) * math.pi * rho * R ** 3


def pressure(r, R, rho):
    """Exact interior-Schwarzschild pressure, valid for rho of either sign."""
    M = mass_of(rho, R)
    a = math.sqrt(1.0 - 2.0 * M * r * r / R ** 3)
    b = math.sqrt(1.0 - 2.0 * M / R)
    return rho * (a - b) / (3.0 * b - a)


def central_ratio(rho, R=1.0):
    """p(0) / |rho|.  Tends to 1/3 from below as the core gets compact."""
    return pressure(0.0, R, rho) / abs(rho)


def compactness(rho, R=1.0):
    return 2.0 * abs(mass_of(rho, R)) / R


def buchdahl_safe(rho, R=1.0):
    """Is every square root real and the denominator non-zero?  For rho < 0 the
    argument 1 - 2M r^2/R^3 = 1 + 2|M| r^2/R^3 exceeds one everywhere."""
    M = mass_of(rho, R)
    if M >= 0.0:
        return R > 9.0 * M / 4.0            # the ordinary Buchdahl bound
    return True                              # negative mass has none


def phi_max(m, a):
    """concentric.py's linearisation parameter at the core.  Not small."""
    return m / a


def energy_conditions(r, R, rho):
    p = pressure(r, R, rho)
    return {"NEC": (rho + p) >= 0.0,
            "WEC": rho >= 0.0 and (rho + p) >= 0.0,
            "DEC": rho >= 0.0 and abs(p) <= abs(rho),
            "SEC": (rho + 3.0 * p) >= 0.0}


def only_sign_is_exotic(rho, R=1.0, samples=(0.0, 0.3, 0.6, 0.9)):
    """Flip the sign of rho and does the material satisfy DEC?  If yes, the
    exoticism is exactly one sign and the pressures are ordinary."""
    return all(abs(pressure(x * R, R, rho)) <= abs(rho) for x in samples)


def classify_core(m, a, r):
    """Hawking-Ellis type of concentric.py's core, measured from the metric."""
    import composite, typefour, concentric
    composite.phi = concentric.potential(m, a)
    g = composite.metric((r, 0.0, 0.0), m)
    gi = typefour.inverse(g)
    R = composite.riemann_lower((r, 0.0, 0.0), m)
    Ric = [[sum(gi[i][k] * R[i][j][k][l] for i in range(4) for k in range(4))
            for l in range(4)] for j in range(4)]
    Rs = sum(gi[j][l] * Ric[j][l] for j in range(4) for l in range(4))
    G = [[Ric[j][l] - 0.5 * g[j][l] * Rs for l in range(4)] for j in range(4)]
    T = [[sum(gi[i][j] * G[j][l] for j in range(4)) / (8.0 * math.pi)
          for l in range(4)] for i in range(4)]
    n = typefour.frobenius(T)
    im = max(abs(z.imag) for z in typefour.roots(typefour.char_poly(T)))
    return (TYPE_IV if (n > 1e-12 and im / n > 1e-3) else TYPE_I), (im / n if n else 0.0)


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-58s %16s %16s  %s" % (label, got, want, "ok" if good else "FAIL"))

    def near(label, got, want, tol):
        nonlocal ok
        good = abs(got - want) <= tol
        ok &= good
        print("  %-58s %16.6g %16.6g  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("1. THE CORE IS TYPE I -- measured, not assumed")
    for r in (0.005, 0.02, 0.05):
        t, ratio = classify_core(2.0e-2, 0.02, r)
        print("     r=%.3f  |Im|/||T|| = %.2e  ->  %s" % (r, ratio, t))
    chk("static and spherically symmetric gives Type I, as MMV require",
        all(classify_core(2.0e-2, 0.02, r)[0] == TYPE_I for r in (0.005, 0.02, 0.05)),
        True)
    print("       The Type IV problem does NOT transfer to this architecture.")

    print("\n2. AND concentric.py's METRIC CANNOT DESCRIBE THE CORE")
    near("Phi_max at the window's lower edge (m=5e-3, a=0.02)",
         phi_max(5.0e-3, 0.02), 0.25, 1e-12)
    near("Phi_max at m = 2e-2", phi_max(2.0e-2, 0.02), 1.0, 1e-12)
    chk("at Phi = 1 the linearised spatial metric has flipped sign",
        (1.0 - 2.0 * phi_max(2.0e-2, 0.02)) < 0.0, True)
    chk("and it is >= 0.25 across the WHOLE window, so no weak field anywhere",
        min(phi_max(m, 0.02) for m in (5e-3, 1e-2, 2e-2, 4e-2)) >= 0.25, True)
    print("       The corridor is fine; the core is not.  Hence the exact model.")

    print("\n3. THE EXACT CORE -- no Buchdahl limit, at any compactness")
    print("     %10s %12s %14s %12s" % ("rho", "2|M|/R", "p(0)", "p(0)/|rho|"))
    for rho in (-0.01, -0.1, -1.0, -10.0, -1000.0):
        print("     %10.2f %12.4f %14.6e %12.5f"
              % (rho, compactness(rho), pressure(0.0, 1.0, rho), central_ratio(rho)))
    chk("every negative-density core is Buchdahl-safe",
        all(buchdahl_safe(r) for r in (-0.01, -1.0, -1000.0)), True)
    chk("and the ordinary bound still bites for positive density",
        buchdahl_safe(1.0, R=1.0), False)
    chk("the pressure is POSITIVE throughout",
        all(pressure(x, 1.0, -1.0) > 0 for x in (0.0, 0.3, 0.6, 0.9)), True)
    chk("and it vanishes at the surface", abs(pressure(1.0, 1.0, -1.0)) < 1e-12, True)

    print("\n   p(0)/|rho| approaches 1/3 FROM BELOW -- the radiation value")
    ratios = [central_ratio(r) for r in (-0.01, -1.0, -100.0, -10000.0)]
    chk("monotone increasing", all(a < b for a, b in zip(ratios, ratios[1:])), True)
    chk("never exceeding 1/3", max(ratios) < 1.0 / 3.0, True)
    near("and reaching it in the limit", ratios[-1], 1.0 / 3.0, 5e-3)

    print("\n   THE ONLY EXOTIC THING IS ONE SIGN")
    for r in (0.0, 0.5, 0.9):
        ec = energy_conditions(r, 1.0, -1.0)
        print("     r=%.1f  NEC %-4s WEC %-4s DEC %-4s SEC %-4s"
              % (r, ec["NEC"], ec["WEC"], ec["DEC"], ec["SEC"]))
    chk("all four fail", not any(energy_conditions(0.5, 1.0, -1.0).values()), True)
    chk("but flip the sign of rho and DEC holds -- the pressures are ordinary",
        only_sign_is_exotic(-1.0), True)
    chk("even at extreme compactness", only_sign_is_exotic(-1000.0), True)
    print("       Isotropic, positive, capped at |rho|/3.  One sign, nothing else.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1


def report():
    print(__doc__)
    print("=" * 79)
    print("THE CORE, EXACTLY")
    print("  %10s %12s %14s %12s %8s" % ("rho", "2|M|/R", "p(0)", "p(0)/|rho|", "regular"))
    for rho in (-0.01, -0.1, -1.0, -10.0, -100.0, -10000.0):
        print("  %10.2f %12.4f %14.6e %12.5f %8s"
              % (rho, compactness(rho), pressure(0.0, 1.0, rho), central_ratio(rho),
                 "yes" if buchdahl_safe(rho) else "NO"))
    print("\n" + "=" * 79)
    print("VERDICT -- the identification target, as narrowly as this can state it")
    print("  A static, spherically symmetric, ISOTROPIC Hawking-Ellis TYPE I")
    print("  fluid with NEGATIVE energy density and POSITIVE pressure not")
    print("  exceeding |rho|/3.  No rest-frame pathology, no anisotropy, no")
    print("  pressure beyond radiation's, and NO COMPACTNESS BOUND -- negative")
    print("  mass has no Buchdahl limit, which is what a core needing b/a >~ 50")
    print("  requires.  Every energy condition fails, and all of them fail for")
    print("  the same single reason: the sign of rho.")
    print("\n  Constant density is incompressible, so this is a BOUNDING MODEL,")
    print("  not an equation of state.  No candidate material is proposed here.")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
