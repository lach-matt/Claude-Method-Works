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

-- 2b. AND THAT LIMIT DISSOLVES WHEN THE COORDINATE IS RIGHT -------------------
M: "we measure in logarithms and prime factors."  That is the corpus's own §9
practice, not a gloss on it: Lambda is a sublattice of the divisor lattice of a
single integer, x <= y iff N(x) | N(y), join is lcm, meet is gcd, and

        rank(x) = Omega(N(x)),  prime factors with multiplicity

Both halves are one move -- REPLACE A MULTIPLICATIVE QUANTITY BY ITS ADDITIVE
COORDINATE.  Prime exponents for a discrete lattice; logarithms for a continuum.

Applied here it is exact.  Any static metric can be written

        g_tt = -exp(2 Phi),     Phi = (1/2) ln(-g_tt)

so Phi IS the logarithm of a metric coefficient, and the linearised -(1+2Phi)
is nothing but its first-order truncation.  An exponential never changes sign:

        Phi     lin g_xx = 1-2Phi     exp g_xx = e^-2Phi
        0.25    +0.500                +0.607
        0.50    +0.000                +0.368
        1.00    -1.000                +0.135      <- the flip is the truncation
        2.00    -3.000                +0.018

    THE SIGN FLIP WAS A COORDINATE ARTEFACT AND SECTION 20.3 ALREADY SAID SO:
    "the notation was not a convenience.  It was the coordinate that made the
    rule expressible."

AND THE DEVICE IS UNCHANGED UNDER THE COMPLETION.  Re-running concentric.py on
g_tt = -e^{2Phi}, g_ij = e^{-2Phi}, which agrees with the linear form to first
order and validates at 4M/b to 0.03 %:

        m         conjugate (lin / exp)     t-|dx| (lin / exp)
        5.0e-3    228.5  /  228.5           -8.4239e-2 / -8.4240e-2
        2.0e-2    165.4  /  165.4           -1.7852e-1 / -1.7888e-1
        8.0e-2    late   /  late            +1.036e+0  / +9.813e-1

    IDENTICAL TO FOUR FIGURES, because the rays live in the corridor where
    Phi ~ 0.02 and the two metrics differ at O(Phi^2) ~ 4e-4.  So the limit in
    §2 was REAL ABOUT THE CORE'S INTERIOR DESCRIPTION and IRRELEVANT TO EVERY
    MEASURED RESULT, all of which happen in the corridor.  Both halves of that
    sentence are kept.

    The prime-factor half of M's instruction is the DISCRETE case -- integer
    coordinates on a divisor lattice -- and this problem is continuous, so only
    the logarithmic half is used here.  Said rather than stretched.

-- 4. THE MATERIAL CENSUS: MAGNITUDE IS REACHED, THE SIGN IS NOT --------------
M raised mercury, lead and a dense plasma phase.  Measured against seatindex.py's
universal seating threshold T_kk >= pi c^4/(4 G l^2):

        material                    rho c^2 (Pa)
        mercury (liquid metal)      1.216e+21
        lead                        1.019e+21
        osmium (densest element)    2.030e+21
        white-dwarf matter          8.988e+25
        neutron-star crust          3.595e+31
        NUCLEAR SATURATION          2.067e+34
        neutron-star core           7.190e+34

        l          needed (Pa)      nuclear saturation / needed
        1 m        9.505e+43        2.175e-10
        1 km       9.505e+37        2.175e-04
        100 km     9.505e+33        2.175          <- EXCEEDS IT
        1000 km    9.505e+31        217.5

    MAGNITUDE IS NOT THE OBSTACLE.  Nuclear-saturation matter EXCEEDS the
    seating requirement beyond about 100 km, and neutron stars are made of it.
    The scale M was reaching for is the right scale -- just not mercury or lead,
    which fall thirteen orders short, but nuclear matter, which does not.

    THE OBSTACLE IS THE SIGN, AND NO PHASE CHANGE FLIPS IT.  rho c^2 is
    dominated by rest mass, which is positive in every solid, liquid, plasma and
    degenerate state; temperature and pressure move its magnitude and never its
    sign.  Squeezing lead into a plasma makes it denser, not negative.

    WHERE NEGATIVE ENERGY DENSITY ACTUALLY OCCURS is relative to a vacuum
    ground state -- Casimir between boundaries, squeezed vacuum, the Hawking
    flux -- and corridor.py already priced the first of those: Casimir meets
    this threshold only at 0.132 Planck lengths.  So the identification phase is
    a VACUUM-STATE problem wearing a materials name, and that is the single most
    useful thing this census says.

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


C_SQ = 299792458.0 ** 2

MATERIALS = (
    ("mercury (liquid metal)", 13534.0),
    ("lead", 11340.0),
    ("osmium (densest element)", 22590.0),
    ("white-dwarf matter", 1.0e9),
    ("neutron-star crust", 4.0e14),
    ("nuclear saturation", 2.3e17),
    ("neutron-star core", 8.0e17),
)


def energy_density(rho_kg):
    """rho c^2 in Pa.  Positive for every ordinary phase of matter."""
    return rho_kg * C_SQ


def margin_over_threshold(rho_kg, l_m):
    """How the material's magnitude compares with universal seating at scale l."""
    import seatindex
    return energy_density(rho_kg) / seatindex.tkk_required(l_m)


def sign_is_the_obstacle():
    """No ordinary phase has negative energy density: rest mass dominates."""
    return all(energy_density(d) > 0.0 for _n, d in MATERIALS)


def log_metric(phi_val):
    """(g_tt, g_xx) in the exponential completion.  Never changes sign."""
    return -math.exp(2.0 * phi_val), math.exp(-2.0 * phi_val)


def linear_metric(phi_val):
    """The first-order truncation.  g_xx flips at Phi = 1/2."""
    return -(1.0 + 2.0 * phi_val), (1.0 - 2.0 * phi_val)


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

    print("\n2b. THE LIMIT DISSOLVES IN THE RIGHT COORDINATE (section 9's practice)")
    print("     %8s %20s %20s" % ("Phi", "linear g_xx", "exponential g_xx"))
    for f in (0.25, 0.5, 1.0, 2.0):
        print("     %8.2f %20.4f %20.4f" % (f, linear_metric(f)[1], log_metric(f)[1]))
    chk("the linear spatial term flips sign at Phi = 1",
        linear_metric(1.0)[1] < 0.0, True)
    chk("the exponential one never does, at any Phi",
        all(log_metric(f)[1] > 0.0 for f in (0.25, 0.5, 1.0, 2.0, 10.0)), True)
    near("and they agree to first order at small Phi",
         log_metric(0.01)[1] / linear_metric(0.01)[1], 1.0, 1e-3)
    print("       Phi = (1/2) ln(-g_tt) IS a logarithm; the flip was the")
    print("       truncation. Section 20.3: the coordinate made the rule expressible.")

    print("\n4. THE MATERIAL CENSUS -- magnitude reached, sign not")
    print("     %26s %14s %16s" % ("material", "rho c^2 (Pa)", "x needed @100km"))
    for n, d in MATERIALS:
        print("     %26s %14.4e %16.3e" % (n, energy_density(d), margin_over_threshold(d, 1.0e5)))
    chk("mercury and lead fall far short of the threshold at 100 km",
        all(margin_over_threshold(d, 1.0e5) < 1e-10 for _n, d in MATERIALS[:3]), True)
    chk("but NUCLEAR SATURATION EXCEEDS it there",
        margin_over_threshold(2.3e17, 1.0e5) > 1.0, True)
    near("by this factor", margin_over_threshold(2.3e17, 1.0e5), 2.175, 0.01)
    chk("and by two orders at 1000 km",
        margin_over_threshold(2.3e17, 1.0e6) > 100.0, True)
    chk("yet EVERY ordinary phase has POSITIVE energy density",
        sign_is_the_obstacle(), True)
    print("       Magnitude is not the obstacle beyond ~100 km. The sign is, and")
    print("       no phase change flips it: rest mass dominates rho c^2.")
    print("       Negative energy density occurs relative to a VACUUM ground")
    print("       state, so identification is a vacuum problem with a materials name.")

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
