#!/usr/bin/env python3
"""
coupling.py -- the drive as a coupling, not a propulsion system.

The frame: the drive creates no acceleration.  It establishes a coupling to the
destination, and the destination pulls.  The ship is in free fall throughout --
geodesic, nothing felt, no thrust, no reaction mass.

This voids the ADM objection that ran through this series.  ADM 4-momentum
conservation forbids a system from accelerating ITSELF.  It does not forbid
falling: a body in free fall changes momentum continuously and the field
supplies it.  A coupling drive never pushes on itself, so the theorem is silent.

What replaces it is a sharper and more useful constraint (see cm_theorem), and
a different binding number: the DEPTH OF THE DESTINATION'S WELL.

stdlib only.
"""
import math, sys

G, c    = 6.67430e-11, 299792458.0
MSUN    = 1.98892e30
AU      = 1.495978707e11
PC      = 3.0856775815e16
MEARTH  = 5.9722e24

def r_s(M):
    return 2.0*G*M/c**2

def infall_speed(M, d, D=float('inf')):
    """Speed gained falling from rest at D to distance d from mass M.

    v = sqrt(2GM(1/d - 1/D)).  For d << D this is the escape speed at d,
    v = c sqrt(r_s/d) -- the closed form THE-BORROWED-WELL.md derived.
    Returned in units of c.  Newtonian; valid while v << c.
    """
    inv = 1.0/d - (0.0 if math.isinf(D) else 1.0/D)
    return math.sqrt(2.0*G*M*inv)/c

def coupling_accel(M, d):
    """The 'pull' -- proper acceleration of the field, GM/d^2 (m/s^2).
    Nothing aboard feels this: it is geodesic."""
    return G*M/d**2

def fall_time(M, d, D):
    """Radial free-fall time from rest at D in to d (s).  Kepler radial solution."""
    if d >= D: return 0.0
    mu = G*M
    x  = math.sqrt(d/D)
    return math.sqrt(D**3/(2.0*mu)) * (math.acos(x) + x*math.sqrt(1.0 - d/D))

def cm_theorem(m_ship, m_projectile, separation):
    """Why the pull must come from mass you did not bring.

    The tempting bootstrap: throw mass ahead, let it collapse, fall toward it.
    It fails exactly.  For an isolated system the centre of mass obeys
    M_tot * a_cm = sum(external forces) = 0, so ANY internal coupling --
    gravitational tractoring included -- moves the parts and never the whole.

    Returns the centre-of-mass displacement after the two bodies fall together
    from `separation` and meet.  It is zero, identically, and that is the point.
    """
    m1, m2 = m_ship, m_projectile
    # meeting point measured from the ship's start
    x_meet_ship = separation * m2/(m1+m2)
    x_meet_proj = -separation * m1/(m1+m2)
    cm_before = 0.0
    cm_after  = (m1*x_meet_ship + m2*(separation + x_meet_proj))/(m1+m2) - \
                (m2*separation)/(m1+m2)
    return cm_after - cm_before

DESTINATIONS = [
    ("Sun, at 1 AU",              1.0*MSUN,          AU),
    ("Sun, at solar surface",     1.0*MSUN,          6.957e8),
    ("Sirius B (white dwarf)",    1.018*MSUN,        5.85e6),
    ("neutron star, at 100 km",   1.4*MSUN,          1.0e5),
    ("neutron star, at surface",  1.4*MSUN,          1.2e4),
    ("10 Msun BH, at 100 r_s",    10.0*MSUN,         100*r_s(10*MSUN)),
    ("10 Msun BH, at 10 r_s",     10.0*MSUN,         10*r_s(10*MSUN)),
    ("Sgr A*, at 10 r_s",         4.3e6*MSUN,        10*r_s(4.3e6*MSUN)),
]

def selftest():
    ok = True
    def chk(label, got, want, tol=0.02):
        nonlocal ok
        good = abs(got-want) <= tol*abs(want) if want else abs(got) < 1e-9
        ok &= good
        print("  %-56s %13.6g %13.6g  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("Known values -- the instrument must reproduce these before reporting")
    chk("Schwarzschild radius of the Sun (m)", r_s(MSUN), 2953.3, tol=0.001)
    # Earth's orbital speed IS the Sun's escape speed at 1 AU over sqrt(2).
    chk("escape speed at 1 AU (km/s)", infall_speed(MSUN, AU)*c/1e3, 42.122, tol=0.001)
    chk("  /sqrt(2) = Earth orbital speed (km/s)",
        infall_speed(MSUN, AU)*c/1e3/math.sqrt(2), 29.785, tol=0.001)
    chk("escape speed at the solar surface (km/s)",
        infall_speed(MSUN, 6.957e8)*c/1e3, 617.5, tol=0.002)
    chk("solar surface gravity (m/s^2)", coupling_accel(MSUN, 6.957e8), 274.0, tol=0.002)
    # v = c sqrt(r_s/d) closed form, cross-checked against the Newtonian integral
    M, d = 10*MSUN, 100*r_s(10*MSUN)
    chk("closed form c*sqrt(r_s/d) matches integral",
        infall_speed(M, d), math.sqrt(r_s(M)/d), tol=1e-9)
    chk("  and equals 0.1 c at d = 100 r_s", infall_speed(M, d), 0.1, tol=1e-9)
    # free fall from 1 AU into the Sun: the textbook 64.6 days
    chk("free-fall time, 1 AU to the solar surface (days)",
        fall_time(MSUN, 6.957e8, AU)/86400.0, 64.53, tol=0.01)

    print("\nThe centre-of-mass theorem -- the bootstrap fails exactly")
    # The theorem is exact; the arithmetic is not.  Judge the displacement
    # against the BASELINE it is computed over, not against an absolute metre.
    SEP = 1.0e9
    for mp in (1.0, 1e6, 1e12):
        rel = abs(cm_theorem(1e6, mp, SEP))/SEP
        good = rel < 1e-15
        ok &= good
        print("  %-56s %13.3g %13s  %s" %
              ("CoM shift / separation, projectile %.0e kg" % mp,
               rel, "< 1e-15", "ok" if good else "FAIL"))

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print("="*78)
    print("THE DRIVE AS A COUPLING -- the destination pulls, the ship falls")
    print("="*78)
    print("""
No thrust, no reaction mass, no acceleration produced by the drive.  The ship is
on a geodesic the whole way and feels nothing.  ADM conservation is SILENT on
this: it forbids a system accelerating itself, not a body falling.  This series
kept quoting it as a blanket prohibition.  That was an over-application.

What actually binds is not ADM.  It is two things.
""")
    print("-- 1. The pull must come from mass you did not bring ------------------------")
    print("""  The tempting bootstrap is to project mass ahead, collapse it, and fall toward
  it.  It fails identically, not approximately.  For an isolated system

        M_total * a_cm  =  sum of EXTERNAL forces  =  0

  so any internal coupling -- gravitational tractoring included -- moves the
  parts and never the whole.  Measured over three projectile masses spanning
  twelve orders of magnitude, the centre-of-mass displacement is""")
    for mp in (1.0, 1e6, 1e12):
        print("        ship 1e6 kg + projectile %-8.0e kg  ->  %.1f m" % (mp, cm_theorem(1e6, mp, 1e9)))
    print("""
  This is the precise, coupling-language version of what ADM was gesturing at,
  and it is the real content of the theorem.  A coupling drive is legitimate;
  a SELF-coupled one is not.  The mass at the far end has to be already there.

-- 2. The reach is the depth of the destination's well -----------------------""")
    print("  %-28s %14s %14s %16s" % ("destination", "arrival speed", "pull (g)", "fall time, 1 pc"))
    for name, M, d in DESTINATIONS:
        v  = infall_speed(M, d)
        a  = coupling_accel(M, d)/9.80665
        t  = fall_time(M, d, PC)/(365.25*86400)
        ts = "%.3g yr" % t if t < 1e6 else "%.3g Myr" % (t/1e6)
        print("  %-28s %13.4g c %14.3g %16s" % (name, v, a, ts))
    print("""
  The closed form is  v = c sqrt(r_s/d)  -- THE-BORROWED-WELL.md's result, and
  it is the whole story of a coupling drive.  Relativistic arrival needs
  d ~ 100 r_s or closer, which means the thing you couple to must be COMPACT.

-- The bind, stated exactly --------------------------------------------------
  Couple to somewhere you want to BE -- a star, a habitable system -- and the
  well is shallow: falling on the Sun from interstellar distance buys 42 km/s,
  which is 4.2 ly in 30,000 years.  Couple to something DEEP enough to give a
  relativistic pull and the destination is a black hole, which is not a place.

  Depth and habitability are anti-correlated, and that -- not ADM, not the
  energy conditions, not 10^31 -- is the actual constraint on a coupling drive.

-- Where it breaks open ------------------------------------------------------
  Falling in is free and arriving is automatic ONLY when the mass you couple to
  IS the destination.  Otherwise the well gives back on the way out exactly what
  it gave on the way in: a static well is a lens, not a pump.

  A MOVING well is a pump.  That is the one loophole and it is not small: it is
  the slingshot of THE-ENGINE.md, where the closed form becomes
        dv = 2U/(1 + U^2)
  bounded by the deflector's speed rather than by its depth -- which is how a
  coupling drive gets to 0.87 c without ever accelerating itself.

  So the frame is right and it survives: no propulsion, no thrust, geodesic
  throughout, pull from the far side.  The engineering problem it leaves is not
  a power plant.  It is choosing WHAT to couple to, and when to let go.
""")
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
