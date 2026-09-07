#!/usr/bin/env python3
"""
torus.py -- THE OPEN GATE.  Does a toroidal warp shell survive the energy conditions?

residue.py closed the three opens into one and showed the sealed gate launches
nothing: the payload must EXIT, and egress needs the same channel ingress did.
So the open torus is not an alternative architecture, it is the only one, and
this question decides whether the gate exists at all.

THE OBSTACLE.  A static torus is not in hydrostatic equilibrium.  A ring under
its own gravity wants to shrink its major radius, so something must hold the
hole open.  Rotation is one answer and brings angular momentum the metric does
not want.  The other is HOOP TENSION -- and tension is negative pressure, which
the dominant energy condition permits only while |p| <= rho.  That is a bound,
and it is closed-form.

THE DERIVATION.  For a thin ring of linear density lam, major radius R0, minor
radius a, the self-attraction per unit length is

    f = G lam^2 ln(8 R0/a) / R0

balanced by a hoop tension F = G lam^2 ln(8 R0/a).  As a stress over the tube
cross-section A that is sigma = F/A, against an energy density rho c^2 =
lam c^2 / A.  THE CROSS-SECTION CANCELS, and DEC (sigma <= rho c^2) gives

    lam <= c^2 / (G ln(8 R0/a))        M <= 2 pi R0 lam

The natural scale is c^2/G -- the same coupling that priced every other result
in this project.  Because the logarithm runs slowly, lam_max is nearly
universal and M_max is LINEAR IN R0, exactly the sphere's M ~ R scaling.

stdlib only.
"""
import math, sys

G, c, MSUN = 6.67430e-11, 299792458.0, 1.98892e30
M_GATE, R1_GATE = 2.200330e30, 4902.0          # the seated design (gate1.py)

def log_factor(R0, a):
    return math.log(8.0*R0/a)

def lambda_max(R0, a):
    """DEC ceiling on linear mass density, kg/m."""
    return c**2/(G*log_factor(R0, a))

def mass_max(R0, a):
    """DEC ceiling on total ring mass, kg."""
    return 2.0*math.pi*R0*lambda_max(R0, a)

def margin(R0, a, M):
    return mass_max(R0, a)/M

def hoop_stress(R0, a, M):
    """Required tension stress, Pa.  sigma = G lam^2 ln(8R0/a) / (pi a^2)."""
    lam = M/(2.0*math.pi*R0)
    return G*lam**2*log_factor(R0, a)/(math.pi*a**2)

def energy_density(R0, a, M):
    """rho c^2 for the tube, Pa (same units as the stress it is compared to)."""
    lam = M/(2.0*math.pi*R0)
    return lam*c**2/(math.pi*a**2)

def selftest():
    ok = True
    def chk(label, got, want, tol=1e-6):
        nonlocal ok
        good = abs(got-want) <= tol*abs(want) if want else abs(got) < 1e-12
        ok &= good
        print("  %-56s %14.6g %14.6g  %s" % (label, got, want, "ok" if good else "FAIL"))

    # NOTE ON THESE FIXTURES: the decimal values below are REGRESSION PINS taken
    # from the formulae themselves -- they catch a future change to the code but do
    # not independently verify the physics.  The independent checks are the four
    # IDENTITIES in the next block, which fail if the pieces disagree with each
    # other, and the hand derivation in the module docstring.
    print("The closed form")
    chk("natural scale c^2/G (kg/m)", c**2/G, 1.346590922e+27, tol=1e-9)
    chk("ln(8 R0/a) at R0=15, a=5", log_factor(15.0, 5.0), 3.178053830, tol=1e-9)
    chk("lambda_max at R0=15, a=5 (kg/m)", lambda_max(15.0, 5.0), 4.237155798e+26, tol=1e-9)
    chk("M_max at R0=15, a=5 (kg)", mass_max(15.0, 5.0), 3.993425259e+28, tol=1e-9)

    print("\nIdentities -- these fail if the pieces disagree with each other")
    # the bound is exactly the point where stress equals energy density
    R0, a = 15.0, 5.0
    Mb = mass_max(R0, a)
    chk("at M_max the hoop stress equals rho c^2 (identity)",
        hoop_stress(R0, a, Mb)/energy_density(R0, a, Mb), 1.0, tol=1e-12)
    # cross-section cancels: the margin must not depend on a except through the log
    chk("margin is independent of a at fixed ln factor (identity)",
        margin(15.0, 5.0, 1e28)*log_factor(15.0, 5.0),
        margin(15.0, 2.0, 1e28)*log_factor(15.0, 2.0), tol=1e-12)
    chk("M_max is linear in R0 at fixed R0/a (identity)",
        mass_max(30.0, 10.0)/mass_max(15.0, 5.0), 2.0, tol=1e-12)
    chk("stress scales as lam^2 (identity)",
        hoop_stress(R0, a, 2e28)/hoop_stress(R0, a, 1e28), 4.0, tol=1e-12)

    print("\nThe gate")
    chk("M_max at gate scale R0=4902, a=1600 (Msun)",
        mass_max(4902.0, 1600.0)/MSUN, 6.518479128, tol=1e-9)
    chk("seated gate mass (Msun)", M_GATE/MSUN, 1.1062936, tol=1e-6)
    chk("margin at gate scale", margin(4902.0, 1600.0, M_GATE), 5.892176859, tol=1e-9)
    chk("  the open gate is DEC-compliant", margin(4902.0, 1600.0, M_GATE) > 1.0, True)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print("="*78)
    print("THE OPEN GATE -- can a torus hold its hole open within the energy conditions?")
    print("="*78)
    print("""
The sealed gate launches nothing: the payload must EXIT, and egress needs the
same channel ingress did.  So the open torus is the only surviving architecture
and this question decides whether the gate exists.

A static torus is not in equilibrium -- a ring under self-gravity shrinks its
major radius.  Something must hold the hole open.  Hoop tension can, and tension
is negative pressure, which DEC permits only while |p| <= rho.  Closed form:

    lam <= c^2 / (G ln(8 R0/a))          M <= 2 pi R0 lam
    natural scale c^2/G = %.4e kg/m

The tube cross-section CANCELS between the tension stress and the energy
density, so the bound is on linear density alone.  And because the logarithm
runs slowly, M_max is LINEAR IN R0 -- the sphere's own M ~ R scaling, arrived at
from a completely different argument.
""" % (c**2/G))
    print("  %-18s %10s %14s %13s" % ("geometry","ln(8R0/a)","M_max (Msun)","lam_max kg/m"))
    for R0, a in ((15.,5.), (20.,5.), (50.,10.), (1000.,325.), (4902.,1600.), (10000.,3260.)):
        print("  R0=%-7.0f a=%-6.0f %10.3f %14.4f %13.4e"
              % (R0, a, log_factor(R0,a), mass_max(R0,a)/MSUN, lambda_max(R0,a)))
    m = margin(4902.0, 1600.0, M_GATE)
    print("""
-- The gate -----------------------------------------------------------------
  R0 = 4902 m, a = 1600 m   (bore radius 3302 m, matching the seated design)
  DEC ceiling        %.4e kg = %.3f Msun
  seated gate mass   %.4e kg = %.3f Msun
  MARGIN             %.2fx

  THE OPEN GATE IS NOT EXCLUDED.  A static torus holds its hole open by hoop
  tension alone, needs no rotation and therefore carries no unwanted angular
  momentum, and the tension it needs sits a factor of %.1f inside the dominant
  energy condition.  The architecture that the ingress bound forced is the one
  the energy conditions allow.

-- What this is, and is not -------------------------------------------------
  IS:     a closed-form necessary condition, with the same c^2/G scale and the
          same linear-in-R behaviour as every other result here, and a computed
          margin at the design point.
  IS NOT: a full GR solution.  The thin-ring formula is Newtonian and a/R0 =
          0.33 is not thin, so the logarithm is approximate; and this checks the
          hoop stress against DEC, not the whole stress-energy tensor.
  NEXT:   the source-first numerical check -- prescribe the toroidal rho, solve
          the Hamiltonian constraint for the conformal factor, and run the exact
          Hawking-Ellis certifier that closed TARGET-1.  That is the same test,
          on the same apparatus, and it either confirms this margin or finds the
          component this estimate does not see.
""" % (mass_max(4902.,1600.), mass_max(4902.,1600.)/MSUN, M_GATE, M_GATE/MSUN, m, m))
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
