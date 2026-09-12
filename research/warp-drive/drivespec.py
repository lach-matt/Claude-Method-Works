#!/usr/bin/env python3
"""
drivespec.py -- the drive, specified.

Corrects a scaling error that ran through this whole series: every mass and
density figure was quoted at the published example's R1 = 10 m, and the size was
never treated as the free parameter it is.

    M   = f R1 c^2 / 2G                      -- LINEAR in size
    rho = 3 f c^2 / (8 pi G R1^2 (g^3 - 1))  -- falls as 1/R^2

So "666,000 x nuclear density" is a property of a 20 m ship, not of warp shells.
Make it bigger and the material requirement collapses.  The engine is then a
materials-and-scale trade with a real optimum, not a 10^31 wall.

Every closed form below is derived in this series' own papers:
  gamma_opt = 1+sqrt(3), G_min = 3+2sqrt(3)   THE-DESIGN-EQUATION.md
  C = pi^2/2 for a raised-cosine shift         THE-DESIGN-EQUATION.md
  k_hat = kappa * C * G(gamma), kappa = 0.145  THE-DESIGN-EQUATION.md (calibrated)
  Phi ~ 0.33 at NEC failure                    WHAT-BINDS.md
  NEC threshold ~0.045 c (corrected)           NEC-CORRECTION.md

stdlib only.
"""
import math, sys

G, c, MSUN = 6.67430e-11, 299792458.0, 1.98892e30
GAMMA_OPT  = 1.0 + math.sqrt(3.0)          # R2/R1
G_MIN      = 3.0 + 2.0*math.sqrt(3.0)      # G(gamma_opt)
C_COS      = math.pi**2 / 2.0              # max|S''| d^2, raised cosine
KAPPA      = 0.145                         # calibrated, THE-DESIGN-EQUATION.md
PHI        = 0.33                          # flux ratio at NEC failure

MATERIALS = [                              # name, density kg/m^3, note
    ("steel",                 7_850,     "ordinary structural alloy"),
    ("osmium",               22_590,     "densest stable element"),
    ("white-dwarf matter",    1.0e9,     "electron-degenerate"),
    ("neutron-star crust",    1.0e14,    "inner crust, neutron drip"),
    ("nuclear matter",        2.3e17,    "saturation density"),
    ("NS core",               1.0e18,    "a few x saturation"),
]

def shell_mass(R1, f):
    """M = f R1 c^2 / 2G.  Linear in size."""
    return f * R1 * c**2 / (2.0*G)

def shell_density(R1, f, gamma=GAMMA_OPT):
    """rho = 3 f c^2 / (8 pi G R1^2 (gamma^3 - 1)).  Falls as 1/R^2."""
    return 3.0*f*c**2 / (8.0*math.pi*G*R1**2*(gamma**3 - 1.0))

def radius_for_density(rho, f, gamma=GAMMA_OPT):
    """Invert: the smallest ship a given material can make."""
    return math.sqrt(3.0*f*c**2 / (8.0*math.pi*G*rho*(gamma**3 - 1.0)))

def k_hat(gamma=GAMMA_OPT, C=C_COS):
    """k_hat = kappa C G(gamma); independent of fill."""
    Gg = (gamma**2 + gamma + 1.0)/(gamma - 1.0)
    return KAPPA * C * Gg

def v_warp_max(f, gamma=GAMMA_OPT, C=C_COS):
    """Phi = k v  and  k = k_hat/f  =>  v_max = Phi f / k_hat."""
    return PHI * f / k_hat(gamma, C)

def v_circulation(v_warp, f, gamma=GAMMA_OPT, C=C_COS):
    """Internal momentum flux the shell must carry, as |T^0x|/rho = v_circ/c.

    This is the DRIVE MECHANISM: the shell does not move, its matter circulates.
    Gearing is k = k_hat/f -- circulate fast, translate slow.
    """
    return (k_hat(gamma, C)/f) * v_warp

def circulation_stress(rho, v_circ):
    """Dynamic pressure the shell wall must sustain, ~ rho v^2 (Pa)."""
    return rho * (v_circ*c)**2

def circulation_energy(M, v_circ):
    """Kinetic energy stored in the circulation, (gamma-1) M c^2 (J)."""
    return (1.0/math.sqrt(1.0 - v_circ**2) - 1.0) * M * c**2

def selftest():
    ok = True
    def chk(label, got, want, tol=0.02):
        nonlocal ok
        good = abs(got-want) <= tol*abs(want) if want else abs(got) < 1e-12
        ok &= good
        print("  %-58s %13.6g %13.6g  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("Closed forms carried from this series' own papers")
    chk("gamma_opt = 1+sqrt(3)", GAMMA_OPT, 2.7320508)
    chk("G(gamma_opt) = 3+2sqrt(3)", (GAMMA_OPT**2+GAMMA_OPT+1)/(GAMMA_OPT-1), G_MIN)
    chk("C for raised cosine = pi^2/2", C_COS, 4.9348022)
    chk("k_hat = kappa C G_min", k_hat(), 0.145*4.9348022*6.4641016)

    print("\nReproduce the published 20 m example (f = 2/3, gamma = 2)")
    # The published shell: R1 = 10 m, R2 = 20 m, m = R2 c^2/(2G)/3.
    M20 = shell_mass(10.0, 2.0/3.0)
    chk("published shell mass (kg)", M20, 4.4886e27, tol=0.001)
    chk("  as Earth masses", M20/5.972e24, 751.6, tol=0.002)
    rho20 = shell_density(10.0, 2.0/3.0, gamma=2.0)
    chk("published shell density (kg/m^3)", rho20, 1.5314e23, tol=0.002)
    chk("  as multiples of nuclear", rho20/2.3e17, 665_800.0, tol=0.01)

    print("\nThe scaling that was missed")
    # Same physics, same f, optimal geometry -- solve for nuclear density.
    Rn = radius_for_density(2.3e17, 2.0/3.0)
    chk("radius at which rho = nuclear (m)", Rn, 4903.0, tol=0.01)
    chk("  mass there (Msun)", shell_mass(Rn, 2.0/3.0)/MSUN, 1.1088, tol=0.01)
    # 1/R^2 scaling check: 10x the radius is 100x less dense.
    chk("rho(49 km)/rho(4.9 km) = 1/100",
        shell_density(10*Rn, 2.0/3.0)/shell_density(Rn, 2.0/3.0), 0.01)
    # linear mass scaling
    chk("M(49 km)/M(4.9 km) = 10", shell_mass(10*Rn, 2/3.)/shell_mass(Rn, 2/3.), 10.0)

    print("\nDrive mechanism")
    vmax = v_warp_max(2.0/3.0)
    chk("v_warp max at f = 2/3 (c)", vmax, 0.047557, tol=0.01)
    chk("required circulation at v_max (c)", v_circulation(vmax, 2/3.), PHI, tol=0.01)
    chk("gearing k = k_hat/f", k_hat()/(2/3.), 6.9384, tol=0.01)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    f = 2.0/3.0
    print("="*78)
    print("THE DRIVE, SPECIFIED -- size is the free parameter, and it was never varied")
    print("="*78)
    print("""
  M   = f R1 c^2 / 2G                      LINEAR in size
  rho = 3 f c^2 / (8 pi G R1^2 (g^3 - 1))  falls as 1/R^2

The "666,000 x nuclear" figure this series kept quoting is a property of a 20 m
ship, not of warp shells.  Scale is free.  Here is the whole trade:
""")
    print("  %-22s %14s %14s %14s" % ("material", "density", "min radius", "mass"))
    for name, rho, note in MATERIALS:
        R = radius_for_density(rho, f)
        M = shell_mass(R, f)
        rs = "%.3g km" % (R/1e3) if R > 1e3 else "%.3g m" % R
        ms = "%.3g Msun" % (M/MSUN) if M > 0.001*MSUN else "%.3g Mearth" % (M/5.972e24)
        print("  %-22s %14.3g %14s %14s   %s" % (name, rho, rs, ms, note))
    print("""
Read the table the right way round.  There is no material that makes a SMALL
warp shell: shrinking it drives the density up as 1/R^2 and no substance can
follow.  But there is a size at which ORDINARY DENSE MATTER suffices -- and the
price of getting there is mass, because mass grows linearly all the way.

The knee is neutron-star matter at ~5 km.  That is not a coincidence: it is the
statement that a warp shell of this class IS a compact star.  And unlike 751
Earth masses at 666,000 x nuclear -- which is nothing that exists -- there are
of order 10^8 objects of that description in this galaxy.
""")
    print("-- The point design ----------------------------------------------------------")
    R1  = radius_for_density(2.3e17, f)
    M   = shell_mass(R1, f)
    vw  = v_warp_max(f)
    vc  = v_circulation(vw, f)
    rho = shell_density(R1, f)
    print("""  Geometry      R1 = %.0f m, R2 = %.0f m  (gamma = 1+sqrt(3), the derived optimum)
  Shell         %.3e kg = %.2f Msun, at %.3g kg/m^3 (nuclear saturation)
  Compactness   f = r_s/R1 = %.3f
  Shift profile raised cosine, C = pi^2/2 = %.4f  (bang-bang bound is 4)
  Cruise        v_warp = %.4f c, geodesic -- the interior is flat, crew feel nothing
  MECHANISM     shell matter circulates at %.3f c; gearing k = %.2f to 1
  Wall stress   %.3g Pa   (NS matter sustains ~1e34 Pa at this density)
  Spin-up cost  %.3g J = %.4f of the shell rest mass
""" % (R1, GAMMA_OPT*R1, M, M/MSUN, rho, f, C_COS, vw, vc, k_hat()/f,
       circulation_stress(rho, vc), circulation_energy(M, vc),
       circulation_energy(M, vc)/(M*c**2)))
    print("""-- What the mechanism actually is --------------------------------------------
The shell does not move.  Its MATTER circulates, in a closed loop with zero net
momentum, and that circulation is the momentum flux T^0x the metric needs.  The
gearing is k = k_hat/f = %.2f : circulate at %.2f c to translate at %.3f c.

That is exactly the topology of Architecture B in the original deliverable --
counter-rotating masses, net angular momentum zero, momentum flux on the axis.
It was never the wrong idea.  It was the wrong SCALE by a factor of 500,000 and
the wrong material by twelve orders of magnitude.  Copper at 20 m cannot do it;
neutron-star matter at 5 km can.

-- The limit that does not move ----------------------------------------------
ADM 4-momentum conservation still forbids self-acceleration at positive ADM
mass.  This drive CRUISES; it cannot start itself.  Something must supply the
initial %.3f c -- and the binary slingshot in THE-ENGINE.md supplies far more
than that, for free.  The two designs are complements, not rivals:
      slingshot  = the launcher   (0.87 c, zero propellant, found object)
      warp shell = the cruiser    (geodesic ride, flat interior, %.3f c)
and on these numbers the launcher is faster than the cruiser, which is the
honest reason to build the launcher first.
""" % (k_hat()/f, vc, vw, vw, vw))
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
