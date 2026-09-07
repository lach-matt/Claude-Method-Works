#!/usr/bin/env python3
"""
elements.py -- the shift is a property of the object, so the object's own
measured numbers decide it.

"Only an object can experience transition. It is the object that is shifted."

The physics agrees, and it is not a limitation but the definition. The shift
beta^i is a property of the FOLIATION and is pure gauge unless it is tied to
matter -- which is exactly why a compactly-supported shift in vacuum is
Hawking-Ellis Type IV (GATE-CLOSED.md) while Kerr's, tied to its source's J, is
fine (kerr.py). A shift is not a thing space does. It is a thing MATTER does.

Take that seriously and the whole question collapses onto one measured quantity.

    v_max = Phi f / k_hat                          drivespec.py, WHAT-BINDS.md
    f     = r_s/R = 2GM/(c^2 R)                    compactness
    M     = rho (4/3) pi R^3                       a uniform body
    =>  f = (8 pi G / 3 c^2) rho R^2

So the warp velocity an object can carry is fixed by its DENSITY and its SIZE,
and density is a measured property of the element it is made of. Nothing here
is derived from theory: the densities below are witnessed numbers.

AND THERE IS A CEILING. f = 1 IS the Schwarzschild radius, so f <= 1 always and

    v_warp <= Phi/k_hat = 0.0713 c   FOR ANY OBJECT, EVER

independent of element, of size, of mass. The entire sourcing branch is capped
at 7.1% of light by the definition of the shift.

stdlib only.
"""
import math, sys

G, c = 6.67430e-11, 299792458.0
MSUN, AU = 1.98892e30, 1.495978707e11
PHI  = 0.33         # MEASURED, WHAT-BINDS.md: flux ratio at NEC failure
KHAT = 4.62536      # DERIVED, THE-DESIGN-EQUATION.md: kappa C G(gamma_opt)

# (Z, symbol, name, density kg/m^3).  MEASURED values, standard conditions.
ELEMENTS = [
    (  1, "H",  "hydrogen (solid)",      89.0),
    (  3, "Li", "lithium",              534.0),
    (  6, "C",  "carbon (diamond)",    3510.0),
    ( 13, "Al", "aluminium",           2700.0),
    ( 26, "Fe", "iron",                7874.0),
    ( 29, "Cu", "copper",              8960.0),
    ( 47, "Ag", "silver",             10490.0),
    ( 82, "Pb", "lead",               11340.0),
    ( 74, "W",  "tungsten",           19300.0),
    ( 79, "Au", "gold",               19300.0),
    ( 92, "U",  "uranium",            19100.0),
    ( 78, "Pt", "platinum",           21450.0),
    ( 77, "Ir", "iridium",            22560.0),
    ( 76, "Os", "osmium",             22590.0),
]
DEGENERATE = [
    ("white-dwarf matter",  1.0e9),
    ("neutron-star crust",  1.0e14),
    ("nuclear saturation",  2.3e17),
]

def k_geom():
    """8 pi G / 3 c^2 -- the constant turning density x area into compactness."""
    return 8.0*math.pi*G/(3.0*c**2)

def compactness(rho, R):
    """f = r_s/R for a uniform sphere of density rho and radius R."""
    return k_geom()*rho*R*R

def v_warp(rho, R):
    """The shift such a body can carry, in c.  Capped at the horizon, f = 1."""
    return (PHI/KHAT)*min(compactness(rho, R), 1.0)

def ceiling():
    """v_warp <= Phi/k_hat, for any object whatever."""
    return PHI/KHAT

def radius_for_horizon(rho):
    """The radius at which a body of this density reaches f = 1."""
    return math.sqrt(1.0/(k_geom()*rho))

def mass_at_horizon(rho):
    R = radius_for_horizon(rho)
    return rho*(4.0/3.0)*math.pi*R**3

def selftest():
    ok = True
    def chk(label, got, want, tol=1e-9):
        nonlocal ok
        good = (got == want) if isinstance(want, bool) else abs(got-want) <= tol*abs(want)
        g = got if isinstance(want, bool) else "%.8g" % got
        w = want if isinstance(want, bool) else "%.8g" % want
        ok &= good
        print("  %-52s %14s %14s  %s" % (label, g, w, "ok" if good else "FAIL"))

    print("The chain")
    chk("8 pi G / 3 c^2", k_geom(), 8.0*math.pi*G/(3.0*c**2), tol=1e-15)
    chk("ceiling Phi/k_hat (c)", ceiling(), PHI/KHAT, tol=1e-15)
    chk("  numerically", ceiling(), 0.071345798, tol=1e-8)

    print("\nIdentities -- these fail if the pieces disagree")
    chk("f is quadratic in R (identity)",
        compactness(1e4, 200.0)/compactness(1e4, 100.0), 4.0, tol=1e-12)
    chk("f is linear in rho (identity)",
        compactness(2e4, 100.0)/compactness(1e4, 100.0), 2.0, tol=1e-12)
    chk("f = 1 exactly at the horizon radius (identity)",
        compactness(2.3e17, radius_for_horizon(2.3e17)), 1.0, tol=1e-12)
    chk("v_warp saturates at the ceiling there (identity)",
        v_warp(2.3e17, radius_for_horizon(2.3e17)), ceiling(), tol=1e-12)
    chk("v_warp cannot exceed the ceiling however large R (identity)",
        v_warp(2.3e17, 1e12), ceiling(), tol=1e-12)
    # the horizon radius must reproduce the Schwarzschild radius of its own mass
    rho = 2.3e17; R = radius_for_horizon(rho); M = mass_at_horizon(rho)
    chk("r_s(M) == R at f = 1 (identity)", 2.0*G*M/c**2, R, tol=1e-9)

    print("\nAgainst this project's own measured design point")
    # drivespec.py: R1 = 4902 m at nuclear saturation, f = 2/3, v = 0.0476 c
    chk("v_warp at f = 2/3", (PHI/KHAT)*(2.0/3.0), 0.04756391, tol=1e-6)
    chk("  which is drivespec's seated 0.0476 c", (PHI/KHAT)*(2.0/3.0), 0.0476, tol=1e-3)

    print("\nWhat the densest element can do")
    chk("osmium, 10 m sphere (c)", v_warp(22590.0, 10.0), 1.002692e-21, tol=1e-6)
    chk("osmium horizon radius (AU)", radius_for_horizon(22590.0)/AU, 0.56386484, tol=1e-7)
    chk("osmium horizon mass (Msun)", mass_at_horizon(22590.0)/MSUN, 2.8555436e7, tol=1e-6)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print("="*78)
    print("THE OBJECT IS WHAT IS SHIFTED -- so the element decides")
    print("="*78)
    print("""
A shift is not something space does; it is something MATTER does.  beta^i is
pure gauge unless it is tied to a source, which is why a compactly-supported
vacuum shift is Type IV and Kerr's, tied to its J, is not.  Taking that as the
definition rather than an obstacle, the whole question reduces to one measured
number -- the density of the stuff the object is made of:

    f = (8 pi G / 3 c^2) rho R^2 = %.4e rho R^2
    v_warp = (Phi/k_hat) f = %.6f f
""" % (k_geom(), PHI/KHAT))
    print("  %-4s %-20s %11s %13s %13s %12s" %
          ("Z","element","rho kg/m^3","v at R=10 m","v at R=1000 km","R for f=1"))
    for Z, sym, name, rho in ELEMENTS:
        Rf = radius_for_horizon(rho)
        rs = "%.3g AU" % (Rf/AU) if Rf > 1e10 else "%.3g km" % (Rf/1e3)
        print("  %-4d %-20s %11.4g %13.3e %13.3e %12s" %
              (Z, name, rho, v_warp(rho,10.0), v_warp(rho,1e6), rs))
    print()
    for name, rho in DEGENERATE:
        Rf = radius_for_horizon(rho)
        rs = "%.3g AU" % (Rf/AU) if Rf > 1e10 else "%.3g km" % (Rf/1e3)
        print("  %-4s %-20s %11.4g %13.3e %13.3e %12s" %
              ("--", name, rho, v_warp(rho,10.0), v_warp(rho,1e6), rs))
    print("""
-- The ceiling --------------------------------------------------------------
  f = 1 IS the Schwarzschild radius, so f <= 1 always, and

      v_warp <= Phi / k_hat = %.6f c    =  %.3f%% of light

  FOR ANY OBJECT, EVER.  Independent of element, of size, of mass, of budget.
  The whole sourcing branch is capped at seven percent of light by the
  definition of what a shift is.  This project's measured design point sits at
  0.0476 c, which is f = 2/3 of that ceiling -- it was already near the wall.

-- What the periodic table decides ------------------------------------------
  Chemistry caps density at OSMIUM, 22,590 kg/m^3, and that is a witnessed
  number, not a derived one.  A 10 m osmium ship carries a shift of 1.0e-21 c.
  To reach the ceiling out of osmium you need a radius of 0.56 AU and a mass of
  2.9e7 Msun -- a supermassive black hole made of the densest element there is.

  Only degenerate matter escapes chemistry, and it does so by ceasing to be
  chemistry: nuclear saturation reaches f = 1 at 26 km.  That is why every
  buildable answer in this project turned out to be a compact star.  Not a
  choice, and not a failure of imagination -- the element sets the density, the
  density sets the compactness, and the compactness IS the shift.

-- Where this leaves the object ---------------------------------------------
  An object can shift itself, and the amount is its own gravitational radius
  divided by its own size.  For anything made of atoms that number is between
  1e-24 and 1e-21.  The shift is real, it is measured, it is not zero, and it
  is not useful -- which is a bound, and by P8 an answer.

  It also says exactly where to stop looking: not for a better material, since
  osmium is the end of the table, and not for a bigger ship, since the ceiling
  does not move.  The object cannot carry itself. Only a gradient it did not
  make can carry it, which is the coupling family, and that is the one branch
  none of this touches.
""" % (ceiling(), 100*ceiling()))
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
