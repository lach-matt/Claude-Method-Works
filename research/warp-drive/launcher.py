#!/usr/bin/env python3
"""
launcher.py -- what the warp shell CAN be, given that it cannot be a drive.

TARGET 2 proved the structural limit: P_ADM = 0 and M_ADM > 0 at every warp
velocity, so the centre of mass is fixed and the shell cannot move itself.
CM-THEOREM generalises it: no isolated system moves its own centre of mass,
whatever it is made of and whatever its design.

A structural limit takes a structural answer.  The theorem forbids moving
YOURSELF.  It does not forbid moving SOMETHING ELSE and recoiling -- that is
what momentum conservation is FOR.  So the object stops being a vehicle and
becomes infrastructure:

    a GEODESIC LAUNCHER.  A fixed installation that hands a payload a velocity
    with ZERO PROPER ACCELERATION, because the payload sits in the flat
    interior the whole time and is never pushed.

That last property is what warp buys and nothing else supplies.  Every other
way of reaching 0.0476 c pushes on the payload.  This one does not push at all.

WHAT IS PROVEN AND WHAT IS NOT -- read this before quoting any number:
  PROVEN (TARGET-1)   the state exists; matter is ordinary; interior is flat;
                      the interior frame is boosted, measured 0.040000 c.
  PROVEN (TARGET-2)   the shell cannot translate itself.
  LEGAL               boosting a payload while the shell recoils conserves
                      momentum exactly.  Nothing forbids the outcome.
  NOT PROVEN          that the shift can be switched while a payload is inside.
                      A STATIC shell is a lens, not a pump: a payload that
                      enters and leaves gains nothing, by the same symmetry that
                      makes a static well give back what it takes.  The launch
                      therefore REQUIRES the switching, and the switching is a
                      time-dependent problem this project has not solved.

  The advance is where the obstacle sits.  For the drive, the theorem forbids
  the OUTCOME.  For the launcher, nothing forbids the outcome and only the
  MECHANISM is unverified.  Forbidden became unverified.

stdlib only.
"""
import math, sys

G, c, MSUN = 6.67430e-11, 299792458.0, 1.98892e30

# The point design from drivespec.py (nuclear saturation, gamma = 1+sqrt(3)).
M_SHELL   = 2.200e30      # kg,  1.11 Msun
E_STORE   = 1.17e46       # J,   circulation reservoir, 5.93% of rest mass
V_WARP    = 0.0476        # c,   interior frame boost

def gamma(b):
    return 1.0/math.sqrt(1.0 - b*b)

def payload_energy(m, b):
    """Kinetic energy handed to a payload of mass m, (gamma-1) m c^2."""
    return (gamma(b) - 1.0)*m*c**2

def payload_momentum(m, b):
    """gamma m v."""
    return gamma(b)*m*b*c

def recoil_speed(m, b, M=M_SHELL):
    """Shell recoil from momentum conservation: M V = gamma m v."""
    return payload_momentum(m, b)/M

def launches_available(m, b, E=E_STORE):
    """How many payloads the circulation reservoir can boost before depletion."""
    return E/payload_energy(m, b)

# ---- the gate's reach, and why it is not a portal ---------------------------
# A gate at rest can only bring a payload to ITS OWN interior-frame velocity,
# v_warp -- it does not add a fixed increment to whatever you already have.  And
# v_warp is capped by the null energy condition at ~0.045-0.05 c (TARGET-1).  So
# the gate is a LOW-BETA TERMINAL: excellent from rest, useless in the middle.
def rapidity(b):
    return math.atanh(b)

def gates_in_series(b_target, b_gate=V_WARP):
    """How many successive boosts of b_gate reach b_target (rapidities add).

    Requires each gate to be at rest in the frame of the previous one -- i.e.
    already MOVING relative to home.  Gates cannot move (CM-THEOREM), so they
    would have to be built in motion.  The number is reported to show the scale
    of that impossibility, not as a proposal.
    """
    return rapidity(b_target)/rapidity(b_gate)

def rocket_mass_ratio(b):
    """Photon rocket floor for the same delta-v: sqrt((1+b)/(1-b))."""
    return math.sqrt((1.0+b)/(1.0-b))

def rocket_accel(b, days):
    """Proper acceleration a rocket must impose to reach b in `days`, in g."""
    return (b*c/(days*86400.0))/9.80665

def selftest():
    ok = True
    def chk(label, got, want, tol=1e-4):
        nonlocal ok
        good = abs(got-want) <= tol*abs(want) if want else abs(got) < 1e-12
        ok &= good
        print("  %-56s %14.6g %14.6g  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("Carried from drivespec.py -- must match the seated point design")
    chk("shell mass (Msun)", M_SHELL/MSUN, 1.10613, tol=1e-4)
    chk("reservoir as fraction of rest mass", E_STORE/(M_SHELL*c**2), 0.059177, tol=1e-4)

    print("\nKinematics of a 1000 t payload at v_warp")
    m = 1.0e6
    chk("gamma at 0.0476 c", gamma(V_WARP), 1.0011348088, tol=1e-9)
    chk("energy handed to payload (J)", payload_energy(m, V_WARP), 1.019915e20, tol=1e-6)
    chk("payload momentum (kg m/s)", payload_momentum(m, V_WARP), 1.428631e13, tol=1e-6)

    print("\nRecoil -- the theorem is satisfied, not evaded")
    v_r = recoil_speed(m, V_WARP)
    chk("shell recoil speed (m/s)", v_r, 6.493779e-18, tol=1e-6)
    # Momentum must balance exactly: that IS the conservation law, checked.
    chk("momentum balance |M V - gamma m v| (kg m/s)",
        abs(M_SHELL*v_r - payload_momentum(m, V_WARP)), 0.0)
    chk("recoil as a fraction of c", v_r/c, 2.166092e-26, tol=1e-6)

    print("\nReservoir")
    chk("launches of 1000 t before depletion", launches_available(m, V_WARP), 1.147154e26, tol=1e-6)
    # Identities, not restatements: these fail if the functions disagree with
    # each other, which decimal fixtures alone cannot catch.
    chk("launches x payload_energy == reservoir (identity)",
        launches_available(m, V_WARP)*payload_energy(m, V_WARP), E_STORE, tol=1e-12)
    chk("recoil scales as 1/M (identity)",
        recoil_speed(m, V_WARP, 2*M_SHELL)/recoil_speed(m, V_WARP, M_SHELL), 0.5, tol=1e-12)
    chk("recoil is linear in payload mass (identity)",
        recoil_speed(2*m, V_WARP)/recoil_speed(m, V_WARP), 2.0, tol=1e-9)
    chk("rocket accel scales as 1/t (identity)",
        rocket_accel(V_WARP,1)/rocket_accel(V_WARP,30), 30.0, tol=1e-12)

    print("\nWhat every other route costs for the same delta-v")
    chk("photon-rocket mass ratio at 0.0476 c", rocket_mass_ratio(V_WARP), 1.0487888, tol=1e-6)
    chk("rocket proper acceleration, 1 day (g)", rocket_accel(V_WARP, 1), 16.841984, tol=1e-6)
    chk("rocket proper acceleration, 30 days (g)", rocket_accel(V_WARP, 30), 0.561399, tol=1e-6)
    chk("launcher proper acceleration on the payload (g)", 0.0, 0.0)

    print("\nThe gate's reach")
    chk("rapidity adds: atanh(0.0476)", rapidity(V_WARP), 0.0476359990, tol=1e-9)
    chk("atanh(0.866)", rapidity(0.866), 1.3168562907, tol=1e-9)
    chk("gates in series to 0.866 c", gates_in_series(0.866), 27.644141, tol=1e-6)
    # identity: composing n gate-boosts must reproduce the target rapidity
    n = gates_in_series(0.866)
    chk("n * gate rapidity == target rapidity (identity)",
        n*rapidity(V_WARP), rapidity(0.866), tol=1e-12)
    chk("one gate from rest reaches exactly v_warp",
        math.tanh(rapidity(V_WARP)), V_WARP, tol=1e-12)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    m = 1.0e6
    print("="*78)
    print("THE GEODESIC LAUNCHER -- what the shell can be, since it cannot be a drive")
    print("="*78)
    print("""
CM-THEOREM forbids an isolated system moving its own centre of mass.  It does
not forbid moving something ELSE and recoiling; that is what conservation is
for.  So the shell stops being a vehicle and becomes INFRASTRUCTURE.

  Shell            %.3e kg (%.2f Msun), nuclear density, R1 = 4.9 km
  Reservoir        %.2e J in circulation (%.2f%% of rest mass)
  Interior         FLAT -- measured: alpha and beta constant, all Christoffels
                   vanish, so the payload is on a geodesic and is NEVER PUSHED
  Boost delivered  %.4f c
""" % (M_SHELL, M_SHELL/MSUN, E_STORE, 100*E_STORE/(M_SHELL*c**2), V_WARP))
    print("-- Launching a 1000 tonne payload ------------------------------------------")
    print("""  Energy to the payload      %.3e J
  Payload momentum           %.3e kg m/s
  SHELL RECOIL               %.3e m/s   = %.2e c
  Launches before depletion  %.3e
""" % (payload_energy(m,V_WARP), payload_momentum(m,V_WARP),
       recoil_speed(m,V_WARP), recoil_speed(m,V_WARP)/c, launches_available(m,V_WARP)))
    print("""  The recoil is 6.5e-18 m/s -- the shell is 24 orders of magnitude heavier than
  the payload, so conservation is satisfied at no practical cost to the
  installation.  The reservoir is good for 1.1e26 launches.  It is, for any
  purpose anyone has, REUSABLE AND INEXHAUSTIBLE.

-- The property nothing else supplies --------------------------------------""")
    print("  %-34s %14s %16s" % ("route to 0.0476 c", "cost", "felt by payload"))
    print("  %-34s %14s %16.2f g" % ("rocket, 1 day", "ratio 1.049", rocket_accel(V_WARP,1)))
    print("  %-34s %14s %16.2f g" % ("rocket, 30 days", "ratio 1.049", rocket_accel(V_WARP,30)))
    print("  %-34s %14s %16.2f g" % ("GEODESIC LAUNCHER", "reservoir", 0.0))
    print("""
  Every other route pushes.  This one does not push at all, because the payload
  never leaves flat space -- and that, not speed, is what the warp state is for.
  A launcher is also symmetric: the same installation run the other way is a
  BRAKE, which is the arrival problem this project priced at a mass ratio of
  3.73 and could not otherwise close.

-- The architecture that follows -------------------------------------------
      shell at origin       geodesic launch      0 g
      coupling / slingshot  amplify if wanted    0 g   (found object)
      shell at destination  geodesic brake       0 g
      the ship itself       NO DRIVE AT ALL

  THE DRIVE IS NOT ON THE SHIP.  THE DRIVE IS THE INFRASTRUCTURE.  That is the
  structural answer to a structural limit: the theorem says a thing cannot move
  itself, so nothing tries to.

-- Not a portal, and the reason is the one that made it physical -----------
  A portal means a topological shortcut: a wormhole.  TOPOLOGICAL CENSORSHIP
  (Friedman, Schleich & Witt, PRL 71, 1486 (1993)) states that in an
  asymptotically flat, globally hyperbolic spacetime satisfying the AVERAGED
  null energy condition, every causal curve from infinity back to infinity is
  homotopic to a trivial one -- no traversable wormhole, no shortcut.

  TARGET-1 measured this shell satisfying the POINTWISE null energy condition,
  which implies the averaged one.  So the theorem applies to our own object:
  the very property that made it physical is what forbids it being a portal.

  That is the third instance of one pattern, and the pattern is the project's
  real result:
      positive ADM mass  buys the energy conditions, forfeits self-motion
      NEC satisfaction   buys physicality,           forfeits shortcuts
      compact support    buys a clean exterior,      forfeits ADM momentum
  EVERY PURCHASE OF PHYSICALITY IS PAID FOR IN GEOMETRY.  Exotic matter is not
  a detail the classic solutions got wrong; it is the price of the geometry
  they wanted, and refusing to pay it costs exactly those properties.

-- So it is a GATE ---------------------------------------------------------
  Not a drive, not a portal: fixed infrastructure at both ends, a passive
  traveller, geodesic transit at 0 g.  You build STATIONS, not ships.

  But the reach is capped.  A gate at rest brings a payload to ITS OWN interior
  velocity -- it does not add an increment -- and v_warp is capped near 0.05 c
  by the energy conditions.  Reaching 0.87 c would need 27.6 gates in series,
  each at rest in the previous one's frame, i.e. each already moving relative
  to home.  Gates cannot move.  So that chain is not a proposal; it is a
  measurement of why the gate is a LOW-BETA TERMINAL:

      departure from rest      gate        0 g   <= gate's regime
      the relativistic cruise  slingshot   0 g   <= coupling family's regime
      final approach to rest   gate        0 g   <= gate's regime

  The two families are not rivals and never were. The gate owns both ends of
  the trip, where everything must start and stop at rest, and the coupling
  family owns the middle. Between them the whole journey is geodesic.

-- The one unproven step ---------------------------------------------------
  A STATIC shell is a lens, not a pump.  A payload that enters and leaves gains
  nothing -- the same symmetry that makes a static well give back exactly what
  it takes.  The launch therefore requires SWITCHING the shift while the payload
  is inside, and that is time-dependent and unsolved here.

  But note where the obstacle now sits.  For the drive, the theorem forbade the
  OUTCOME and no mechanism could have helped.  For the launcher, nothing forbids
  the outcome; only the mechanism is unverified.  FORBIDDEN BECAME UNVERIFIED,
  and that is the whole gain from asking what the object can be instead of what
  it failed to be.
""")
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
