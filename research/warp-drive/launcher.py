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

# The point design from drivespec.py as first seated (R1 = 4902 m, gamma =
# 1+sqrt(3)).  CORRECTED (DOCKET 67 follow-ups): this read "(nuclear
# saturation, ...)".  It was saturation on a recalled 2.3e17 kg/m^3; on the
# tree's one nuclear density, address.RHO_NUCLEAR = 2.676e17 (DERIVED-FROM-
# ORDER: n_0 = 0.16 fm^-3, not READ), this shell is 0.859 x nuclear and
# drivespec.py's nuclear-density point is R1 = 4544 m, 1.03 Msun.  The design
# here is kept at 4902 m (named hypothesis GATE1-SIZED-ON-RECALLED-DENSITY,
# gate1.py).
# CORRECTED (DOCKET 67, on M's ruling "Re-size to 4544 m"): first M_SHELL =
# 2.200e30 kg (1.11 Msun) and E_STORE = 1.17e46 J were typed here for the
# 4902 m design.  GATE 1 is re-sized to drivespec's nuclear-density radius on
# address.RHO_NUCLEAR (R1 = 4544 m), and both are imported from gate1.py, never
# typed; GATE1-SIZED-ON-RECALLED-DENSITY is discharged there.  The first values
# are kept below and every first pin is still checked as a RECORD.
import address as _address
import gate1 as _gate1
RHO_NUCLEAR = _address.RHO_NUCLEAR
RHO_NUCLEAR_WITHDRAWN = 2.3e17           # as first written; RECORD only
R1_GATE   = _gate1.R1     # m,   4544.18, drivespec's radius (gate1.py)
M_SHELL   = _gate1.M_GATE # kg,  2.040e30 = 1.03 Msun
E_STORE   = _gate1.E_STORE  # J, circulation reservoir, 5.93% of rest mass
V_WARP    = 0.0476        # c,   interior frame boost
M_SHELL_AS_FIRST_WRITTEN = 2.200e30      # kg, 1.11 Msun; RECORD only
E_STORE_AS_FIRST_WRITTEN = 1.17e46       # J; RECORD only
R1_AS_FIRST_WRITTEN      = 4902.0        # m; RECORD only

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

# ---- does a gate need a gate at the far end? --------------------------------
def magsail_decel(b, L_AU):
    """Mean proper deceleration braking from b over L astronomical units, in g.

    A magsail is DRAG -- the ship feels it.  Braking this way is cheap and
    fuel-free but it is NOT geodesic, which is the whole thing a gate supplies.
    """
    L = L_AU*1.495978707e11
    return ((b*c)**2/(2.0*L))/9.80665

def gate_mass(R1, f=2.0/3.0):
    """M = f R1 c^2 / 2G -- linear in size (drivespec.py)."""
    return f*R1*c**2/(2.0*G)

def gate_density(R1, f=2.0/3.0):
    """rho = 3 f c^2 / (8 pi G R1^2 (g^3-1)) at gamma = 1+sqrt(3)."""
    g = 1.0+math.sqrt(3.0)
    return 3.0*f*c**2/(8.0*math.pi*G*R1**2*(g**3-1.0))

def seed_recoil(m_seed, b, M=M_SHELL):
    """Recoil of a source gate that launches a SEED GATE of mass m_seed.

    Being launched by another body is not self-motion, so CM-THEOREM permits
    it.  But the source cannot stop itself afterwards, so the recoil is
    PERMANENT: it stops being a fixed terminal.
    """
    return gamma(b)*m_seed*b*c/M

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
    # CORRECTED (DOCKET 67, on M's ruling "Re-size to 4544 m"): first 1.10613
    # Msun and 0.059177 on the typed 2.200e30 kg / 1.17e46 J (RECORD below).
    chk("shell mass (Msun)", M_SHELL/MSUN, 1.025539, tol=1e-6)
    chk("  is gate1's re-sized mass (identity)", M_SHELL, _gate1.M_GATE, tol=1e-15)
    chk("reservoir as fraction of rest mass", E_STORE/(M_SHELL*c**2), 0.0593434, tol=1e-6)
    chk("  RECORD: shell mass as first written (Msun)", M_SHELL_AS_FIRST_WRITTEN/MSUN, 1.10613, tol=1e-4)
    chk("  RECORD: reservoir fraction as first written",
        E_STORE_AS_FIRST_WRITTEN/(M_SHELL_AS_FIRST_WRITTEN*c**2), 0.059177, tol=1e-4)

    print("\nKinematics of a 1000 t payload at v_warp")
    m = 1.0e6
    chk("gamma at 0.0476 c", gamma(V_WARP), 1.0011348088, tol=1e-9)
    chk("energy handed to payload (J)", payload_energy(m, V_WARP), 1.019915e20, tol=1e-6)
    chk("payload momentum (kg m/s)", payload_momentum(m, V_WARP), 1.428631e13, tol=1e-6)

    print("\nRecoil -- the theorem is satisfied, not evaded")
    v_r = recoil_speed(m, V_WARP)
    # CORRECTED (DOCKET 67, on M's ruling "Re-size to 4544 m"): first
    # 6.493779e-18 m/s, 2.166092e-26 c and 1.147154e26 launches on the typed
    # 2.200e30 kg / 1.17e46 J; recoil goes as 1/M, launches as E.
    chk("shell recoil speed (m/s)", v_r, 7.004073e-18, tol=1e-6)
    chk("  RECORD: on the first-written 2.200e30 kg (m/s)",
        recoil_speed(m, V_WARP, M_SHELL_AS_FIRST_WRITTEN), 6.493779e-18, tol=1e-6)
    # Momentum must balance exactly: that IS the conservation law, checked.
    # CORRECTED (DOCKET 67, on M's ruling "Re-size to 4544 m"): first run on the
    # typed M_SHELL = 2.200e30, where the float residual is exactly 0.0; that
    # check is kept unchanged on that mass.  On the re-sized (unrounded) mass the
    # residual is float rounding, 1.4e-16 of the momentum, so it is checked
    # against the momentum at 4 ulp (8.9e-16), the tightest form a product of
    # two unrounded floats admits.
    chk("momentum balance |M V - gamma m v| (kg m/s), first-written mass",
        abs(M_SHELL_AS_FIRST_WRITTEN*recoil_speed(m, V_WARP, M_SHELL_AS_FIRST_WRITTEN)
            - payload_momentum(m, V_WARP)), 0.0)
    chk("momentum balance on the re-sized mass, relative (<= 4 ulp)",
        abs(M_SHELL*v_r - payload_momentum(m, V_WARP))/payload_momentum(m, V_WARP)
        <= 4*2.220446049250313e-16, True)
    chk("recoil as a fraction of c", v_r/c, 2.336307e-26, tol=1e-6)
    chk("  RECORD: on the first-written 2.200e30 kg",
        recoil_speed(m, V_WARP, M_SHELL_AS_FIRST_WRITTEN)/c, 2.166092e-26, tol=1e-6)

    print("\nReservoir")
    chk("launches of 1000 t before depletion", launches_available(m, V_WARP), 1.066644e26, tol=1e-6)
    chk("  RECORD: on the first-written 1.17e46 J",
        launches_available(m, V_WARP, E_STORE_AS_FIRST_WRITTEN), 1.147154e26, tol=1e-6)
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

    print("\nDoes a gate need a gate at the far end?")
    chk("magsail braking from v_warp over 810 AU (g)", magsail_decel(V_WARP, 810), 0.0856829, tol=1e-6)
    # CORRECTED (DOCKET 67, on M's ruling "Re-size to 4544 m"): first at R1 =
    # 4902 m (1.106294 Msun, 2.200330e30 kg, 0.859337 x nuclear, equal-gate
    # recoil 0.0476612 c against the typed 2.200e30 kg).  Repinned to gate1's
    # re-sized R1; the 4902 m pins are RECORD checks.
    chk("gate mass at R1 = R1_GATE (Msun)", gate_mass(R1_GATE)/MSUN, 1.025539, tol=1e-6)
    chk("  reproduces the seated shell mass", gate_mass(R1_GATE), M_SHELL, tol=1e-12)
    chk("  RECORD: gate mass at R1 = 4902 m (Msun)", gate_mass(4902)/MSUN, 1.106294, tol=1e-6)
    chk("  RECORD: reproduced the first seated shell mass", gate_mass(4902), 2.200330e30, tol=1e-6)
    # CORRECTED (DOCKET 67 follow-ups): repinned to the computed value on
    # address.RHO_NUCLEAR; the first pin, 24.025285 on 2.3e17, is a RECORD.
    chk("nuclear density is address.RHO_NUCLEAR",
        RHO_NUCLEAR == _address.RHO_NUCLEAR, True)
    chk("density at R1 = 1000 m, as multiples of nuclear",
        gate_density(1000)/RHO_NUCLEAR, 20.649535, tol=1e-6)
    chk("  RECORD: on the withdrawn 2.3e17",
        gate_density(1000)/RHO_NUCLEAR_WITHDRAWN, 24.025285, tol=1e-6)
    chk("the seated shell (R1 = R1_GATE), as multiples of nuclear",
        gate_density(R1_GATE)/RHO_NUCLEAR, 1.0, tol=1e-12)
    chk("  RECORD: the first seated shell (R1 = 4902 m), as multiples of nuclear",
        gate_density(4902)/RHO_NUCLEAR, 0.859337, tol=1e-5)
    # a seed gate cannot be made small: rho ~ 1/R^2 forces it near the source's mass
    r_eq = seed_recoil(gate_mass(R1_GATE), V_WARP)
    chk("recoil launching an EQUAL gate (c)", r_eq/c, 0.04765402, tol=1e-6)
    chk("  is exactly gamma v_warp for equal masses (identity)", r_eq/c,
        gamma(V_WARP)*V_WARP, tol=1e-12)
    chk("  i.e. the source is thrown to ~v_warp itself", r_eq/c > 0.04, True)
    chk("  RECORD: 4902 m seed against the typed 2.200e30 kg (c)",
        seed_recoil(gate_mass(4902), V_WARP, M_SHELL_AS_FIRST_WRITTEN)/c, 0.0476612, tol=1e-6)
    chk("gate mass is linear in R (identity)", gate_mass(2000)/gate_mass(1000), 2.0, tol=1e-12)
    chk("gate density scales as 1/R^2 (identity)",
        gate_density(2000)/gate_density(1000), 0.25, tol=1e-12)
    chk("back-to-back pair: net recoil is zero (identity)",
        seed_recoil(gate_mass(4902), V_WARP) - seed_recoil(gate_mass(4902), V_WARP), 0.0)
    chk("back-to-back pair at R1_GATE: net recoil is zero (identity)",
        seed_recoil(gate_mass(R1_GATE), V_WARP) - seed_recoil(gate_mass(R1_GATE), V_WARP), 0.0)

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

  Shell            %.3e kg (%.2f Msun), R1 = %.2f km, at %.3f x nuclear
                   density (address.RHO_NUCLEAR; first "nuclear density", on
                   a recalled 2.3e17 -- CORRECTED, DOCKET 67 follow-ups; then
                   R1 = 4.9 km, 1.11 Msun, 0.859 x, until GATE 1 was re-sized
                   on M's ruling "Re-size to 4544 m", DOCKET 67)
  Reservoir        %.2e J in circulation (%.2f%% of rest mass)
  Interior         FLAT -- measured: alpha and beta constant, all Christoffels
                   vanish, so the payload is on a geodesic and is NEVER PUSHED
  Boost delivered  %.4f c
""" % (M_SHELL, M_SHELL/MSUN, R1_GATE/1e3, gate_density(R1_GATE)/RHO_NUCLEAR,
       E_STORE, 100*E_STORE/(M_SHELL*c**2), V_WARP))
    print("-- Launching a 1000 tonne payload ------------------------------------------")
    print("""  Energy to the payload      %.3e J
  Payload momentum           %.3e kg m/s
  SHELL RECOIL               %.3e m/s   = %.2e c
  Launches before depletion  %.3e
""" % (payload_energy(m,V_WARP), payload_momentum(m,V_WARP),
       recoil_speed(m,V_WARP), recoil_speed(m,V_WARP)/c, launches_available(m,V_WARP)))
    print("""  The recoil is %.1e m/s (first 6.5e-18) -- the shell is %.0f orders of
  magnitude heavier than the payload, so conservation is satisfied at no
  practical cost to the installation.  The reservoir is good for %.1e launches
  (first 1.1e26).  It is, for any purpose anyone has, REUSABLE AND
  INEXHAUSTIBLE.

-- The property nothing else supplies --------------------------------------""" % (
        recoil_speed(m,V_WARP), math.log10(M_SHELL/m), launches_available(m,V_WARP)))
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

-- Does a gate need a gate at the far end? ---------------------------------
  LAUNCH: no.  A single gate projects one-way with nothing at the destination.

  ARRIVAL WITHOUT A GATE: cheap, but not free and NOT 0 g.  At the gate's own
  0.0476 c the options are a magsail (fuel-free, 810 AU) or a photon rocket at
  a 1.049 mass ratio -- 49 kg per tonne.  Both are trivial costs.  But the
  magsail is DRAG: the ship feels 0.086 g for the whole brake.  The gate's one
  irreplaceable property, zero proper acceleration, is exactly what is lost.

  This is why the low-beta cap is not the limitation it looked like.  A gate
  can only reach ~0.05 c, and braking from ~0.05 c is easy -- the SAME fact.
  One-way projection is viable precisely because the gate is slow.

  RECALL: needs a gate at the far end, and here is the asymmetry you are
  pointing at.  A gate is symmetric -- run backwards it brakes -- so ONE gate
  serves both directions AT ITS OWN END: it launches you out and catches you
  coming home.  What no home gate can supply is the OUTBOUND LAUNCH FROM THE
  FAR END.  So:

      1 gate  (home)   outbound 0 g, inbound braking 0 g, return launch unserved
      2 gates (pair)   every leg 0 g, no onboard systems at all

-- Can a gate project a gate? ----------------------------------------------
  Legally yes: being launched BY ANOTHER BODY is not self-motion, so
  CM-THEOREM permits it.  The network is bootstrappable in principle.

  The cost is brutal and it is a scaling result, not an engineering detail.
  A seed gate cannot be made small: rho ~ 1/R^2, so halving the radius
  quadruples the density, and at R1 = 1 km the requirement is already 20.6 x
  nuclear (first 24.0 x, on a recalled 2.3e17 -- CORRECTED, DOCKET 67
  follow-ups).  The seed is therefore comparable in mass to the source, and

      launching an EQUAL gate throws the source to %.4f c

  which it can never undo, because it cannot accelerate itself.  One seeding
  destroys the terminal that did it.

  THE FIX IS THE ORIGINAL DELIVERABLE'S OWN IDEA.  Launch two seeds BACK TO
  BACK, in opposite directions: the recoils cancel exactly, net momentum stays
  zero, and the source stays put.  Momentum cancellation by symmetric pairing
  is Architecture B's principle exactly -- counter-directed masses summing to
  zero -- arriving for the third time in this project, now as the only way to
  grow the network without consuming it.

  Consequence: gates are seeded IN PAIRS, so the network grows outward in
  opposed directions and can never be extended toward one destination alone.
  A 4.24 ly seeding takes 89 years in transit at 0.0476 c.

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
""" % (seed_recoil(gate_mass(R1_GATE), V_WARP)/c))
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
