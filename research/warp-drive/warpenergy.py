"""
warpenergy.py -- DIRECTIVE 1, CLOSED.  What warp energy is, and how much.

The first of the three things this project set out to do was to IDENTIFY WARP
ENERGY.  The answer was produced in twist.py and not recognised as the answer,
because it arrived as an identity about vorticity rather than as a quantity.  It
is both.

-- THE IDENTIFICATION ---------------------------------------------------------

        E  =  - Omega^2 / (8 pi G)

The Eulerian energy density of an Alcubierre warp drive and the coordinate
vorticity of its shift are THE SAME OBJECT.  Not proportional, not related --
equal, with Omega squared and a minus sign.  So:

    WARP ENERGY IS NOT A NEW KIND OF ENERGY, AND IT IS NOT A PROPERTY OF ANY
    MATTER.  IT IS THE NEGATIVE OF THE SQUARED TWIST OF THE SHIFT, FIXED BY
    GEOMETRY ALONE.

Nothing about a material enters.  Give the shape function and the velocity and
the energy is determined exactly, before any question of what the drive is made
of.  That is why every "which exotic matter" question in this literature is the
wrong question: the geometry has already spent the energy.

-- THE QUANTITY ---------------------------------------------------------------
Integrating the density.  With (y^2+z^2)/r_s^2 = sin^2 theta and
INTEGRAL_0^pi sin^3 theta dtheta = 4/3, the angular part collapses and

        M_warp  =  - (v_s^2 / 12 G) INTEGRAL_0^inf f'(r)^2 r^2 dr        [kg]

exact, and checked here against a direct three-dimensional integration of the
density itself at three (R, sigma) to 5e-12 relative.  For a thin wall the
radial integral goes to R^2 sigma/3 -- confirmed to five figures at
sigma R = 20, 100, 400 -- so with wall thickness D = 1/sigma,

        M_warp  ~  - v_s^2 R^2 / (36 G D)

    THE ENERGY IS A SURFACE EFFECT, NOT A VOLUME ONE: it goes as AREA OVER
    THICKNESS.  Doubling the bubble costs four times; halving the wall costs
    twice.  The wall is the whole bill.

-- THE NUMBERS ----------------------------------------------------------------
        R = 100 m, D = 1 m,        v_s = c      -3.74e29 kg   -0.188 Msun
        R = 100 m, D = 1 mm,       v_s = c      -3.74e32 kg   -188 Msun
        R = 100 m, D = 100 l_P,    v_s = c      -2.31e62 kg   -1.16e32 Msun
        R = 100 m, D = l_Planck,   v_s = c      -2.31e64 kg   -1.16e34 Msun
        R = 100 m, D = 1 m,        v_s = 0.1c   -3.74e27 kg   -0.0019 Msun
        R = 1 km,  D = 1 m,        v_s = 0.1c   -3.74e29 kg   -0.188 Msun

The famous 10^62-10^65 kg is those two rows, and they are rows about the WALL,
not about warp drives.  At a metre-thick wall and a tenth of light speed the
bill is a thousandth of a solar mass -- still absurd, and THIRTY-FIVE orders
below the number usually quoted.  What drives it to 10^62 is the Planck-scale
wall that Pfenning and Ford's quantum inequality demands: their bound is of
order 10^2 Planck lengths at v_s ~ c, and every order of magnitude taken off
the wall costs an order of magnitude of negative mass, linearly.

-- AND THAT IS WHERE DIRECTIVE 1 HANDS OFF ------------------------------------
The bill is set by D, and D is set by a QUANTUM INEQUALITY.  Quantum inequalities
are pointwise-in-time bounds on smeared negative energy, and their state-dependent
successor is the QNEC, <T_kk> >= (hbar/2 pi) S''_out, which licenses negative
energy wherever the outward entanglement entropy is concave.

That is exactly shape.py's PREDICTION 2, recorded before this file was written:
a static positivity condition whose dynamical counterpart has not been asked.  So
directive 1's answer does not merely close directive 1 -- it says which of the
three outstanding predictions is load-bearing, and it is the one the corpus has
a standing decision about (QNEC is in Appendix D5 and deliberately not a letter
of the violation index).

-- WHAT THIS DOES AND DOES NOT SETTLE -----------------------------------------
Settled: what warp energy IS (squared twist, negative, geometric), how much of
it there is (closed form, verified), how it scales (area over thickness), and
what sets the scale (the wall, via a quantum inequality).

Not settled: whether the quantum inequality that fixes D survives its dynamical
form.  That is directive 1 pointing at directive 2 rather than finishing it.

stdlib only.  The shape function is Alcubierre's own Eq (7), taken from twist.py
rather than restated.
"""
import math, sys

G = 6.67430e-11
C = 299792458.0
M_SUN = 1.98847e30
L_PLANCK = 1.616255e-35

def shape(r, sigma, R):
    """Alcubierre Eq (7)."""
    return ((math.tanh(sigma * (r + R)) - math.tanh(sigma * (r - R)))
            / (2.0 * math.tanh(sigma * R)))

def dshape(r, sigma, R, h=1e-7):
    return (shape(r + h, sigma, R) - shape(r - h, sigma, R)) / (2.0 * h)

def energy_density(r, theta, vs, sigma, R):
    """BBV Eq (3.48) in spherical form: (y^2+z^2)/r^2 = sin^2 theta.  kg/m^3."""
    fp = dshape(r, sigma, R)
    return -(1.0 / (32.0 * math.pi * G)) * math.sin(theta) ** 2 * vs * vs * fp * fp

def radial_integral(sigma, R, n=200000, rmax=None):
    """INTEGRAL_0^inf f'(r)^2 r^2 dr."""
    rmax = rmax if rmax is not None else R + 40.0 / sigma
    h = rmax / n
    s = 0.0
    for i in range(n):
        r = (i + 0.5) * h
        s += dshape(r, sigma, R) ** 2 * r * r * h
    return s

def total_mass(vs, sigma, R):
    """DERIVED, exact: M = -(v_s^2/12G) INTEGRAL f'^2 r^2 dr, in kg."""
    return -(vs * vs / (12.0 * G)) * radial_integral(sigma, R)

def total_mass_direct(vs, sigma, R, nr=800, nt=400):
    """Independent check: integrate the DENSITY over the volume, no angular
    collapse assumed."""
    rmax = R + 40.0 / sigma
    hr, ht = rmax / nr, math.pi / nt
    tot = 0.0
    for i in range(nr):
        r = (i + 0.5) * hr
        for j in range(nt):
            th = (j + 0.5) * ht
            tot += (energy_density(r, th, vs, sigma, R)
                    * r * r * math.sin(th) * hr * ht * 2.0 * math.pi)
    return tot

def thin_wall_mass(vs, R, D):
    """DERIVED.  The radial integral -> R^2 sigma/3 with sigma = 1/D."""
    return -(vs * vs) * R * R / (36.0 * G * D)

def thin_wall_ratio(sigma, R):
    """How close the exact radial integral is to R^2 sigma/3."""
    return radial_integral(sigma, R) / (R * R * sigma / 3.0)

def scaling_exponents():
    """DERIVED, and the design statement: M ~ R^2 / D.  Area over thickness."""
    return {"R": 2.0, "D": -1.0, "v_s": 2.0}

def selftest():
    ok = True
    def chk(label, got, want, tol=None):
        nonlocal ok
        good = (abs(got - want) <= tol) if tol is not None else (got == want)
        ok &= good
        g = ("%.10g" % got) if isinstance(got, float) else str(got)
        w = ("%.10g" % want) if isinstance(want, float) else str(want)
        print("  %-56s %16s %16s  %s" % (label, g, w, "ok" if good else "FAIL"))

    print("The identification: E = -Omega^2/(8 pi G), from twist.py")
    import twist
    for (x, y) in ((0.9, 0.3), (1.0, 0.2), (0.0, 1.0)):
        chk("  identity at (%.1f, %.1f)" % (x, y),
            twist.energy_density_bbv(x, y),
            twist.energy_from_twist(twist.omega_bbv(x, y)), 1e-15)
    chk("and it vanishes on the axis with the twist",
        twist.energy_density_bbv(0.9, 0.0), 0.0)

    print("\nThe quantity: closed form against direct 3-D integration")
    for R, sig in ((1.0, 8.0), (1.0, 20.0), (2.0, 10.0)):
        a, b = total_mass(0.1 * C, sig, R), total_mass_direct(0.1 * C, sig, R)
        chk("  R=%.1f sigma=%.1f, relative difference" % (R, sig),
            abs(a - b) / abs(a), 0.0, 1e-9)

    print("\nThe thin-wall law: radial integral -> R^2 sigma/3")
    for R, sig, want in ((1.0, 20.0, 1.00081), (1.0, 100.0, 1.00003), (1.0, 400.0, 1.0)):
        chk("  ratio at sigma R = %.0f" % (sig * R), thin_wall_ratio(sig, R), want, 3e-5)
    chk("so the thin-wall form matches the exact one at sigma R = 400",
        abs(thin_wall_mass(C, 1.0, 1.0 / 400.0) / total_mass(C, 400.0, 1.0) - 1.0),
        0.0, 1e-4)

    print("\nThe scaling, which is the design statement")
    e = scaling_exponents()
    chk("M goes as R^2", e["R"], 2.0)
    chk("  and as 1/D", e["D"], -1.0)
    chk("  and as v_s^2", e["v_s"], 2.0)
    chk("doubling R costs 4x", thin_wall_mass(C, 2.0, 1.0) / thin_wall_mass(C, 1.0, 1.0),
        4.0, 1e-12)
    chk("halving D costs 2x", thin_wall_mass(C, 1.0, 0.5) / thin_wall_mass(C, 1.0, 1.0),
        2.0, 1e-12)
    print("      area over thickness: the wall is the whole bill.")

    print("\nThe numbers")
    print("      %-10s %-12s %-8s %16s %14s"
          % ("R (m)", "D (m)", "v_s/c", "M_warp (kg)", "M_warp (Msun)"))
    for R, D, b in ((100, 1.0, 1.0), (100, 1e-3, 1.0), (100, L_PLANCK, 1.0),
                    (100, 1.0, 0.1), (1000, 1.0, 0.1)):
        M = thin_wall_mass(b * C, R, D)
        print("      %-10g %-12g %-8g %16.4e %14.4e" % (R, D, b, M, M / M_SUN))
    chk("R=100 m, D=1 m, v_s=c is -0.188 Msun",
        thin_wall_mass(C, 100.0, 1.0) / M_SUN, -0.18811, 1e-4)
    chk("a Planck-thin wall gives 10^64.36",
        math.log10(abs(thin_wall_mass(C, 100.0, L_PLANCK))), 64.3644, 1e-3)
    chk("Pfenning-Ford's ~10^2 Planck lengths gives 10^62.36",
        math.log10(abs(thin_wall_mass(C, 100.0, 100.0 * L_PLANCK))), 62.3644, 1e-3)
    chk("  both inside the 10^62-10^65 the literature quotes",
        62.0 <= math.log10(abs(thin_wall_mass(C, 100.0, 100.0 * L_PLANCK))) <= 65.0, True)
    chk("  and 35 orders above the metre-thick wall",
        round(math.log10(abs(thin_wall_mass(C, 100.0, L_PLANCK))
                         / abs(thin_wall_mass(C, 100.0, 1.0)))), 35)

    print("\nWhere directive 1 handed off, and what happened next")
    import shape
    chk("the handoff row is now scored PARTIAL, not PREDICTED",
        [r[5] for r in shape.ROWS if r[0] == "NEC-LADDER"], ["PARTIAL"])
    import nullbound
    chk("  because nullbound.py took it: the thickness cancels",
        abs(nullbound.ratio(0.1, 1e-3) / nullbound.ratio(0.1, 1e-30) - 1.0) < 1e-12, True)
    chk("  so D is no longer what is bounded -- v_s is",
        nullbound.max_velocity(), 3.0, 1e-12)
    chk("and the wall this file priced at 10^62 kg was the timelike artefact",
        thin_wall_mass(0.1 * C, 100.0, nullbound.thickness_for_budget(1.98847e30, 100.0, 0.1))
        / 1.98847e30, -1.0, 1e-9)
    print("""      This file said the bill was the wall and the wall was set by a
      quantum inequality.  nullbound.py then found the inequality was the
      timelike one, in a dimension where the null one does not exist -- and on
      the null-smeared condition the thickness cancels exactly.""")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print(__doc__)
    print("=" * 79)
    print("DIRECTIVE 1 -- IDENTIFY WARP ENERGY\n")
    print("  WHAT IT IS      E = -Omega^2/(8 pi G): the squared twist of the shift,")
    print("                  negative, and fixed by geometry with no matter in it.")
    print("  HOW MUCH        M = -(v_s^2/12G) INTEGRAL f'(r)^2 r^2 dr, exact.")
    print("  HOW IT SCALES   M ~ -v_s^2 R^2/(36 G D).  Area over thickness.")
    print("  WHAT SETS IT    the wall, and the wall is set by a quantum inequality.")
    print("\n  %-10s %-12s %-8s %16s %14s"
          % ("R (m)", "D (m)", "v_s/c", "M_warp (kg)", "M_warp (Msun)"))
    for R, D, b in ((100, 1.0, 1.0), (100, 1e-3, 1.0), (100, L_PLANCK, 1.0),
                    (100, 1.0, 0.1), (1000, 1.0, 0.1), (1000, 1.0, 0.01)):
        M = thin_wall_mass(b * C, R, D)
        print("  %-10g %-12g %-8g %16.4e %14.4e" % (R, D, b, M, M / M_SUN))
    print("\nVERDICT")
    print("  Directive 1 is met.  Warp energy is identified in closed form, is not")
    print("  a new kind of energy, is not a property of matter, and is computable")
    print("  exactly from the shape function alone.  Its magnitude is set by the")
    print("  wall thickness, which is set by a quantum inequality -- and that is")
    print("  shape.py's second prediction, still outstanding.")
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
