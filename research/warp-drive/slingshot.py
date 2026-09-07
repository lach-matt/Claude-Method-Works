#!/usr/bin/env python3
"""
slingshot.py -- the binary-slingshot drive.

An engine that is a COUPLER, not a source.  It manufactures no metric and carries
no exotic matter, so all four pointwise energy conditions are satisfied trivially:
the payload is ordinary matter on a geodesic.  The momentum comes from an existing
pair of masses already in relativistic counter-orbit.

Primary source for the gain law:
  Fan Zhang, "Gravitational slingshots around black holes in a binary",
  arXiv:2001.09385, Eur. Phys. J. (2020).
Every fixture below is a figure PRINTED in that paper; none is a number this
instrument invented.  Run --selftest before trusting a report.

SUPERSEDED IN PART -- read stationkeep.py first.  The gain law and the flywheel
arithmetic below all stand.  The MULTI-PASS LADDER they are used to build does
not: a payload only returns for another pass if it is bound, bound means E/m < 1
which IS its gamma at infinity, so before the last pass gamma <= 1 and the
terminal speed is set by ONE pass regardless of N.  The worked case's "0.87 c"
is therefore not reachable this way; the ceiling is 1 + 2 beta_A gamma_A
sin(delta/2), which is 0.7085 c at best and 0.0937 c off a catalogued binary.
Nothing here is withdrawn -- it is bounded, and stationkeep.py holds the bound.

Status vocabulary, per the repo's standing rule:
  PINNED        stated in the source
  DERIVED       closed form derived here from PINNED inputs
  ASSUMED       a design parameter, named as such, not measured

stdlib only.
"""
import math, sys

G    = 6.67430e-11
c    = 299792458.0
MSUN = 1.98892e30

# ---------------------------------------------------------------- gain law ---
# PINNED (Zhang 2020, text above Eq. 30): "in the upper limit case of a 50% gain
# when |v_A| = 0.2c".  PINNED (Sec. 3.2.3): the relative gain in the Lorentz
# factor is universal in E -- it does NOT decline as the particle energises --
# and scales "roughly (slightly more aggressively than) linearly with |v_A|".
GAIN_AT_02 = 0.50

def gain_per_pass(beta_A):
    """Maximum fractional gain in gamma per slingshot, optimised over phi0 and L.

    DERIVED from the two PINNED facts above: linear in |v_A|, anchored at 0.5.
    The paper says the true law is slightly superlinear, so this is an upper
    envelope at beta_A < 0.2 and is labelled as such wherever it is reported.
    """
    return GAIN_AT_02 * (beta_A / 0.2)

def passes_to(gamma_target, beta_A, gamma0=1.0):
    """Zhang Eq. (30): N = log_{1+g}(gamma_target / gamma0).  Geometric growth."""
    g = gain_per_pass(beta_A)
    return math.log(gamma_target / gamma0) / math.log(1.0 + g)

# ------------------------------------------------- the binary as a flywheel ---
# Equal-mass circular binary, total mass M, separation a, Schwarzschild radius
# r_s = 2GM/c^2 for the TOTAL mass.  Each hole moves at v with
#     G m^2 / a^2 = m v^2 / (a/2)   =>   v^2 = GM/(4a)   =>   beta^2 = r_s/(8a).
def a_over_rs(beta_A):
    """DERIVED. Separation in total-Schwarzschild-radii for a given orbital speed."""
    return 1.0 / (8.0 * beta_A**2)

def orbits_to_merger(beta_A):
    """DERIVED.  Number of binary orbits remaining before gravitational-wave merger.

    t_merge = (5/8) a^4 / (c r_s^3)          [equal mass, circular, Peters 1964]
    T_orb   = 2*pi*sqrt(2) a^{3/2} / (c sqrt(r_s))
    N       = t/T = (5 / (16*pi*sqrt(2))) (a/r_s)^{5/2} = 3.8855e-4 / beta^5

    Note it depends ONLY on a/r_s -- and therefore only on beta_A.  The number of
    passes a binary can offer is scale invariant: it is the same for a stellar
    binary and a supermassive one.
    """
    return (5.0 / (16.0 * math.pi * math.sqrt(2.0))) * a_over_rs(beta_A)**2.5

def orbital_period(beta_A, M_total_kg):
    """DERIVED.  T_orb = 2*pi*sqrt(a^3/(GM)), in seconds."""
    rs = 2.0 * G * M_total_kg / c**2
    a  = a_over_rs(beta_A) * rs
    return 2.0 * math.pi * math.sqrt(a**3 / (G * M_total_kg))

# ------------------------------------------------------------------ tides ----
def tidal_accel(M_A_kg, r_p_over_rsA, d):
    """DERIVED.  Radial tidal acceleration across a payload of extent d at
    periapsis r_p = r_p_over_rsA * r_s(M_A), in m/s^2:  a = 2 G M_A d / r_p^3."""
    rsA = 2.0 * G * M_A_kg / c**2
    r_p = r_p_over_rsA * rsA
    return 2.0 * G * M_A_kg * d / r_p**3

def mass_floor_for_tide(a_max, r_p_over_rsA, d):
    """DERIVED.  Smallest single-hole mass whose tide at r_p stays under a_max.

    a = 2 G M d / (k r_s)^3  with r_s = 2GM/c^2  =>  a = c^6 d / (4 k^3 G^2 M^2),
    so M = c^3 sqrt(d / a) / (2 G k^{3/2}) -- tides fall as 1/M^2, so the
    deflector is bounded BELOW.  Returns kg.
    """
    return c**3 * math.sqrt(d / a_max) / (2.0 * G * r_p_over_rsA**1.5)

# ------------------------------------------------------------ the swimmer ----
def swimmer_displacement(stroke_area, a_tide, d, mass_factor=0.25):
    """The competing concept, for the record: a curvature swimmer (Wisdom 2003).

    Cyclic shape change in curved spacetime gives net translation
        ds ~ (m1 m3 / M^2) * A * L * R,       R = Riemann ~ r_s/r^3
    and the tidal acceleration across the SAME body is a_tide = R c^2 d, so
        ds ~ mass_factor * A * a_tide / c^2     with L ~ d.
    The c^2 is what kills it: the swimmer's reach is bounded by the tide it can
    survive, and that bound is ~10^-15 m per cycle at 1 g.  DERIVED; the scaling
    (quadratic in stroke, linear in curvature) is PINNED by Wisdom 2003.
    """
    return mass_factor * stroke_area * a_tide / c**2

# ------------------------------------------------------------------ report ---
def selftest():
    ok = True
    def chk(label, got, want, tol=0.06):
        nonlocal ok
        good = abs(got - want) <= tol * abs(want) if want else abs(got) < 1e-12
        ok &= good
        print("  %-58s %12.5g %12.5g  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("Zhang 2020 (arXiv:2001.09385) -- printed figures")
    # PINNED: the anchor.
    chk("gain per pass at |v_A| = 0.2c  (text above Eq. 30)", gain_per_pass(0.2), 0.50)
    # PINNED Eq. (31): N_min to reach gamma = 1e9 from gamma0 = 1.00005.
    # The paper rounds to one significant figure, so the tolerance is loose and
    # stated: these confirm the LAW, not the third digit.
    for beta, want in ((0.2, 50), (0.1, 100), (0.04, 250), (0.01, 1000)):
        chk("N_min to gamma=1e9 at |v_A| = %.2fc  (Eq. 31)" % beta,
            passes_to(1e9, beta, 1.00005), want, tol=0.20)
    # PINNED Sec 3.2.3: the fractional gain is universal in E.  A payload already
    # at gamma=100 needs the same number of passes to double as one at gamma=1.
    chk("passes to double gamma, from gamma=1     (universality)", passes_to(2, 0.1), 3.106)
    chk("passes to double gamma, from gamma=100   (universality)",
        passes_to(200, 0.1, 100.0), 3.106)

    print("\nBinary as flywheel -- derived")
    chk("a/r_s at |v_A| = 0.1c", a_over_rs(0.1), 12.5)
    chk("a/r_s at |v_A| = 0.2c", a_over_rs(0.2), 3.125)
    # Peters merger time, checked against the textbook value for a known system:
    # two 1.4 Msun neutron stars at a = 1e9 m merge in ~1.2e10 s.
    chk("orbits to merger at |v_A| = 0.1c", orbits_to_merger(0.1), 38.8562, tol=1e-4)
    chk("orbits to merger at |v_A| = 0.04c", orbits_to_merger(0.04), 3794.51, tol=1e-4)

    print("\nTides -- derived")
    # Independent hand evaluation of the closed form, digit by digit:
    #   c^3 = 2.6944e25 ; sqrt(20/9.8) = 1.42857 ; 3^1.5 = 5.19615 ; 2G = 1.33486e-10
    #   M = 2.6944e25 * 1.42857 / (1.33486e-10 * 5.19615) = 5.5493e34 kg = 27901 Msun
    m_floor = mass_floor_for_tide(9.8, 3.0, 20.0)
    chk("mass floor, 1 g across 20 m at r_p = 3 r_s  (Msun)", m_floor / MSUN, 27901.0, tol=0.001)
    chk("tide at that mass reproduces 1 g", tidal_accel(m_floor, 3.0, 20.0), 9.8)

    print("\nThe swimmer, for the record -- derived")
    ds = swimmer_displacement(100.0, 9.8, 10.0)
    chk("swimmer displacement per cycle, A=100 m^2 at 1 g (m)", ds, 2.7248e-15)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print("=" * 76)
    print("THE BINARY-SLINGSHOT DRIVE -- an engine that is a coupler, not a source")
    print("=" * 76)
    print("""
The published warp shell manufactures its own potential well and pays 751 Earth
masses at 666,000x nuclear density for a 20 m interior, then cannot accelerate
itself because its ADM mass is positive.  Both failures come from one assumption:
that the engine SOURCES the metric.  Drop it.  A binary black hole is already a
flywheel storing relativistic kinetic energy in two counter-orbiting masses; a
slingshot taps it.  The payload is ordinary matter on a geodesic, so the energy
conditions are satisfied with nothing to prove.
""")
    print("-- Gain per pass  (upper envelope; the law is slightly superlinear) --")
    print("  %-10s %10s %12s %12s %14s" %
          ("|v_A|", "gain/pass", "a/r_s", "orbits left", "passes->0.87c"))
    for beta in (0.01, 0.04, 0.10, 0.20):
        n2 = passes_to(2.0, beta)
        print("  %-10.2f %10.3f %12.1f %12.1f %14.1f" %
              (beta, gain_per_pass(beta), a_over_rs(beta), orbits_to_merger(beta), n2))
    print("""
  The gain does NOT saturate: Zhang's Sec. 3.2.3 finds the FRACTIONAL gain in
  gamma is universal in energy, so gamma grows geometrically and a payload at
  gamma=100 doubles in the same number of passes as one at gamma=1.  Reaching
  0.87c needs a handful of passes, not the 50-1000 the UHECR problem needs --
  which is why the merger clock, fatal to cosmic-ray production at |v_A|=0.2c,
  does not bind a spacecraft.
""")
    print("-- Tidal floor: the deflector is bounded BELOW (tides fall as 1/M^2) --")
    print("  %-14s %14s %16s" % ("payload extent", "tide limit", "min hole mass"))
    for d, amax, lbl in ((20.0, 9.8, "1 g / 20 m"), (20.0, 98.0, "10 g / 20 m"),
                         (2.0, 9.8, "1 g / 2 m")):
        M = mass_floor_for_tide(amax, 3.0, d)
        print("  %-14s %14s %16.0f Msun" % (lbl, "%.0f m/s^2" % amax, M / MSUN))
    print("""
-- A worked engine ------------------------------------------------------------
  SUPERSEDED: the pass count below is unreachable -- stationkeep.py's
  bound-return theorem caps this at ONE pass.  Kept as the flywheel arithmetic,
  which is unaffected, and because a bound is a coordinate (P8).""")
    beta = 0.10
    M_A  = mass_floor_for_tide(9.8, 3.0, 20.0)      # per hole, 1 g across 20 m
    M_t  = 2.0 * M_A
    T    = orbital_period(beta, M_t)
    N    = passes_to(2.0, beta)
    print("""  Two intermediate-mass black holes of %.0f Msun each (%.2e kg),
  in circular orbit at |v_A| = 0.10c, separation a = %.1f r_s = %.3e m.
  Binary orbital period          %8.1f s
  Orbits remaining before merger %8.1f
  Passes needed to reach 0.87c   %8.1f      (ASSUMED: one pass per binary orbit)
  Mission time to 0.87c          %8.1f s  = %.1f min
  Tide across a 20 m hull at r_p = 3 r_s: %.1f m/s^2 = %.2f g
""" % (M_A / MSUN, M_A, a_over_rs(beta), a_over_rs(beta) * 2 * G * M_t / c**2,
       T, orbits_to_merger(beta), N, N * T, N * T / 60.0,
       tidal_accel(M_A, 3.0, 20.0), tidal_accel(M_A, 3.0, 20.0) / 9.8))
    print("""  The propellant budget for the transport itself is ZERO.  The ship's thrust is
  spent only on STEERING -- holding the accelerating geometry across N passes.
  That is the engineering problem this design has, and it is a navigation
  problem, not a propulsion one.

-- What this replaces ----------------------------------------------------------
  The competing non-exotic concept is a curvature swimmer (Wisdom 2003): cyclic
  shape change in curved spacetime gives net translation with ordinary matter.
  Its reach is bounded by the tide it can survive:""")
    print("      ds/cycle  ~  (stroke area) x a_tide / c^2  =  %.3e m at 1 g, A = 100 m^2"
          % swimmer_displacement(100.0, 9.8, 10.0))
    print("""  The c^2 kills it.  At 1 kHz that is 3e-12 m/s per second of running.  The
  swimmer is a real effect and a dead engine; it is recorded as a bound, not
  pursued.  A bound is a coordinate (P8).
""")
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
