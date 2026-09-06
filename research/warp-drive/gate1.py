#!/usr/bin/env python3
"""
gate1.py -- GATE 1: materials, power, schematic, and what must vary gate to gate.

Builds on the seated point design (drivespec.py) and the launcher role
(launcher.py).  Everything here is engineering ON TOP of measurements already
taken; where a step is unsolved it is marked OPEN at the place it occurs and
not swept to the end.

stdlib only.
"""
import math, sys

G, c, MSUN = 6.67430e-11, 299792458.0, 1.98892e30
LY, AU, YR = 9.4607304726e15, 1.495978707e11, 3.15576e7
SIGMA_T, M_P = 6.6524587e-29, 1.67262192e-27

# ---- the seated design -------------------------------------------------------
F_FILL   = 2.0/3.0
GAMMA_G  = 1.0 + math.sqrt(3.0)        # R2/R1
R1       = 4902.0                      # m
R2       = GAMMA_G*R1
M_GATE   = F_FILL*R1*c**2/(2.0*G)      # kg
RHO      = 3.0*F_FILL*c**2/(8.0*math.pi*G*R1**2*(GAMMA_G**3-1.0))
V_WARP   = 0.0476                      # c
V_CIRC   = 0.330                       # c, wall circulation
E_STORE  = 1.17e46                     # J, circulation reservoir

# ---- materials ---------------------------------------------------------------
RHO_NUC   = 2.3e17                     # kg/m^3, nuclear saturation
P_DEGEN   = 1.0e34                     # Pa, degenerate matter at saturation
P_ANVIL   = 1.0e12                     # Pa, best static laboratory pressure
P_LASER   = 1.0e13                     # Pa, best dynamic (laser shock)

def confinement_gap(P_lab=P_ANVIL):
    """How far any pressure vessel falls short of confining the shell material."""
    return P_DEGEN/P_lab

def self_gravity_pressure(M=M_GATE, R=R2):
    """Central pressure scale of a self-gravitating body, ~ G M^2 / R^4."""
    return G*M**2/R**4

# ---- power -------------------------------------------------------------------
def eddington_luminosity(M=M_GATE):
    """L_Edd = 4 pi G M m_p c / sigma_T  (W)."""
    return 4.0*math.pi*G*M*M_P*c/SIGMA_T

def accretion_efficiency(M=M_GATE, R=R2):
    """eta = GM/(R c^2): fraction of rest mass released landing on the surface."""
    return G*M/(R*c**2)

def accreted_mass_for(E, M=M_GATE, R=R2):
    """Rest mass that must be accreted to release E joules."""
    return E/(accretion_efficiency(M, R)*c**2)

def accretion_time(E, M=M_GATE, R=R2):
    """Seconds at the Eddington limit to release E joules."""
    return E/eddington_luminosity(M)

# ---- variance between gates --------------------------------------------------
def transit_years(dist_ly, b=V_WARP):
    return dist_ly/b

def lead_angle(dist_ly, v_transverse, b=V_WARP):
    """Aim-ahead angle, radians: the target moves during transit."""
    t = transit_years(dist_ly, b)*YR
    return (v_transverse*t)/(dist_ly*LY)

def matched_vwarp(v_radial, b=V_WARP):
    """v_warp retuned so the payload arrives AT REST in the destination frame.

    Relativistic composition, not subtraction: the gate's boost and the target's
    motion compose.  v_radial > 0 means the target is receding.
    """
    return (b + v_radial/c)/(1.0 + b*v_radial/c)

# Nearby systems: distance ly, radial km/s (+ receding), transverse km/s
SYSTEMS = [
    ("Proxima Centauri",   4.246, -22.2, 24.6),
    ("Alpha Cen A/B",      4.344, -22.4, 23.0),
    ("Barnard's Star",     5.963, -110.6, 89.7),
    ("Sirius",             8.611,  -5.5, 16.8),
]

def selftest():
    ok = True
    def chk(label, got, want, tol=1e-5):
        nonlocal ok
        good = abs(got-want) <= tol*abs(want) if want else abs(got) < 1e-12
        ok &= good
        print("  %-56s %14.6g %14.6g  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("Carried design -- must reproduce drivespec.py")
    chk("gate mass (Msun)", M_GATE/MSUN, 1.1062936, tol=1e-7)
    chk("R2 (m)", R2, 13392.5131, tol=1e-8)
    chk("shell density / nuclear saturation", RHO/RHO_NUC, 1.0000, tol=2e-3)

    print("\nMaterials -- why there is no pressure vessel")
    chk("degenerate pressure / best static lab pressure", confinement_gap(), 1.0e22)
    chk("degenerate pressure / best laser shock", confinement_gap(P_LASER), 1.0e21)
    # self-gravity must supply the confining pressure, so it has to REACH it
    chk("self-gravity pressure scale (Pa)", self_gravity_pressure(), 1.004461e34, tol=1e-6)
    chk("  and that is within an order of the degenerate pressure",
        0.1 < self_gravity_pressure()/P_DEGEN < 10.0, True)

    print("\nPower -- accretion")
    # My hand value was 2.76e31 -- off by exactly 2x. The standard form
    # L_Edd = 1.26e31 (M/Msun) W gives 1.394e31, agreeing with the code.
    chk("Eddington luminosity (W)", eddington_luminosity(), 1.391040e31, tol=1e-6)
    # 1.26e31 is a 3-significant-figure textbook constant (pure hydrogen,
    # rounded), so its own precision is the tolerance here -- not the code's.
    chk("  agrees with L_Edd = 1.26e31 (M/Msun) W", eddington_luminosity(),
        1.26e31*(M_GATE/MSUN), tol=5e-3)
    chk("accretion efficiency eta", accretion_efficiency(), 0.1220085, tol=1e-6)
    chk("accreted mass for the reservoir (Msun)",
        accreted_mass_for(E_STORE)/MSUN, 0.5364598, tol=1e-6)
    chk("time at Eddington (Myr)", accretion_time(E_STORE)/YR/1e6, 26.65277, tol=1e-6)
    # identity: mass * eta * c^2 must be the energy asked for
    chk("accreted mass x eta c^2 == E (identity)",
        accreted_mass_for(E_STORE)*accretion_efficiency()*c**2, E_STORE, tol=1e-12)

    print("\nVariance between gates")
    chk("transit to Alpha Cen at v_warp (yr)", transit_years(4.344), 91.2605, tol=1e-5)
    chk("lead angle for Alpha Cen (arcsec)",
        lead_angle(4.344, 23.0e3)*206264.806, 332.4492, tol=1e-6)
    chk("matched v_warp for Alpha Cen (approaching)",
        matched_vwarp(-22.4e3), 0.04752545, tol=1e-7)
    # identity: zero relative velocity must leave v_warp untouched
    chk("zero relative velocity leaves v_warp unchanged (identity)",
        matched_vwarp(0.0), V_WARP, tol=1e-15)
    # identity: composition is antisymmetric about the sign of v_radial
    chk("receding needs more, approaching needs less (identity)",
        matched_vwarp(1e4) > V_WARP > matched_vwarp(-1e4), True)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print("="*78); print("GATE 1 -- BUILD SPECIFICATION"); print("="*78)

    print("""
1. MATERIALS
------------
  The shell is %.3e kg at %.3g kg/m^3 -- nuclear saturation.  That is not a
  material in the chemical sense: it is DEGENERATE NUCLEAR MATTER, neutrons and
  protons at beta equilibrium with electrons and muons, held by degeneracy
  pressure and the strong force.  There is no alloy, no lattice, no chemistry.

  IT CANNOT BE HELD IN A VESSEL.  Confining it needs ~1e34 Pa against""" % (M_GATE, RHO))
    print("""      best static laboratory pressure (diamond anvil)   1e12 Pa
      best dynamic pressure (laser shock)                1e13 Pa
      SHORTFALL                                          %.0e

  Nothing bridges twenty-one orders of magnitude.  The only agent that reaches
  1e34 Pa is SELF-GRAVITY, and it does: G M^2 / R^4 = %.3e Pa for this design,
  within an order of the degeneracy pressure it must balance.  That is not a
  coincidence -- it is the statement that the object IS a compact star, and the
  reason the radius is 4.9 km and not 4.9 m.

  MATERIAL SOURCE: a neutron star.  Found, not manufactured.  Nothing else in
  the universe makes this substance, and it exists only while its own gravity
  holds it.  Take a ~1.1 Msun neutron star as feedstock.""" % (confinement_gap(P_LASER), self_gravity_pressure()))

    print("""
2. POWER
--------
  Standing reservoir      %.2e J   (circulation, %.2f%% of rest mass)
  Per launch, 1000 t      1.02e20 J  (one part in 1.1e26 of the reservoir)
  Spin-up, one time       %.2e J
  Hollowing, one time     ~1e46 J    [OPEN -- no method, see 3]

  PREFERRED SOURCE: ACCRETION.  It is the only process demonstrated to move
  1e46 J onto a neutron star, and nature already runs it -- millisecond pulsars
  are spun to ~0.15 c equatorial this way.

      Eddington luminosity      %.3e W
      accretion efficiency      %.4f  (GM/Rc^2, landing on the surface)
      rest mass to accrete      %.3f Msun
      time at the Eddington limit  %.1f Myr

  Two consequences, both first-order and neither a detail:

  (a) THE GATE'S FINAL MASS IS NOT CHOSEN, IT IS ACCUMULATED.  Delivering the
      reservoir requires accreting %.2f Msun onto a %.2f Msun star -- a ~49%%
      increase.  You do not build a gate to a mass; you start with a lighter
      star and stop accreting when the reservoir is full.  R1 then follows from
      the mass it ended at.

  (b) [OPEN] ACCRETION DELIVERS THE WRONG FLOW TOPOLOGY.  Accretion spins a star
      about an axis: rigid TOROIDAL rotation with net angular momentum J != 0
      and momentum density that is azimuthal.  The metric needs a closed
      POLOIDAL loop with J = 0 and momentum density along x, because g_tx must
      be -S(r)v with the shell itself unmoving.  The energy source is
      identified at the right scale; the coupling to the required flow is not.
      This is a distinct open problem from the switching one.""" % (
        E_STORE, 100*E_STORE/(M_GATE*c**2), E_STORE,
        eddington_luminosity(), accretion_efficiency(),
        accreted_mass_for(E_STORE)/MSUN, accretion_time(E_STORE)/YR/1e6,
        accreted_mass_for(E_STORE)/MSUN, M_GATE/MSUN))

    print("""
3. SCHEMATIC -- GATE 1, MERIDIONAL SECTION
------------------------------------------
  Axis of launch is x, horizontal.  Drawn to scale in kilometres.

                              ^ equator: PEAK LOAD
                              |  binding ratio 0.4508 at 75 deg
              . - - - - - - - | - - - - - - - .
          .   |               |               |   .
       .      |    S(r) ramp, raised cosine   |      .
     .        |    C = pi^2/2 = 4.935         |        .
    .         |                               |         .
   |          |    +---------------------+    |          |
   |          |    |                     |    |          |
 ==+==========+====|   FLAT INTERIOR     |====+==========+==>  x
   |  BORE    |    |   R1 = 4.902 km     |    |  BORE    |     launch
   |  (pole,  |    |   alpha = 0.7628    |    |          |
   |   least  |    |   beta  = 0.0476 c  |    |          |
    .  loaded)|    |   0 g throughout    |    |         .
     .        |    +---------------------+    |        .
       .      |                               |      .
          .   |     WALL: degenerate matter   |   .
              ` - - - - - - - - - - - - - - - '
                   R2 = 13.393 km
                   wall thickness 8.490 km
                   circulation 0.330 c, poloidal, J = 0

  DIMENSIONS        R1 4.902 km   R2 13.393 km   gamma = 1+sqrt(3) = 2.7321
  INTERIOR          4.93e11 m^3 of flat spacetime; every Christoffel vanishes
  WALL              %.3g kg/m^3, 2.25e33 Pa dynamic stress, 4.4x margin
  SHIFT PROFILE     raised cosine, the best C^1 profile; bang-bang bound is 4

  THE AXIAL BORE is placed on the poles, and that placement is measured rather
  than assumed.  SPHERICITY.md found the binding load is an EQUATORIAL BELT --
  0.4508 at 75 degrees from the axis of motion against 0.1363 at the pole, a
  ratio of 3.31.  The pole is the least-loaded direction on the shell, so it is
  the only place a channel can be cut.  It is also, exactly, the central bore
  of Architecture B in the original deliverable -- reached here from a load
  measurement rather than from intuition.

  [OPEN] INGRESS.  A bore through 8.5 km of self-gravitating degenerate matter
  is a defect in hydrostatic equilibrium and will close unless it is held.  The
  pole is where that is cheapest, and "cheapest" is not "solved".  This is the
  third open problem and it is independent of the other two.""" % RHO)

    print("""
4. DOES EACH GATE VARY?  YES -- IN TWO PARAMETERS, AND ONLY TWO
---------------------------------------------------------------
  WHAT IS FIXED, AND WHY IT CANNOT VARY:

    RADIUS AND MASS.  rho ~ 1/R^2 pins the radius: at 4.9 km the requirement is
    exactly nuclear saturation, at 1 km it is 24x saturation, at 50 km it is
    1/100th.  Gates must be built where the material actually exists, so every
    gate is a few kilometres and about a solar mass.  There is ONE gate design.

    v_warp CEILING.  v_max = Phi f / k_hat carries no R at all -- performance is
    scale-free.  A big gate is no faster than a small one, which is why there is
    nothing to gain by varying size.

  WHAT MUST VARY, GATE BY GATE:

  (i) v_warp, TUNED TO THE PARTNER'S RADIAL VELOCITY.  A gate delivers its
      payload to v_warp in ITS OWN frame.  Stars move, so arriving at rest at
      the far end requires composing out the relative motion:
          v_launch = (v_warp + v_rad/c) / (1 + v_warp v_rad/c)
      Tuned by adjusting the circulation, since v_warp = v_circ / k.

  (ii) ORIENTATION, WITH A LEAD ANGLE.  The shift is a VECTOR along x, so a gate
      is AIMED, and the target moves during a transit measured in decades.""")
    print("\n  %-20s %8s %10s %12s %14s" % ("destination","dist ly","transit yr","lead arcsec","matched v_warp"))
    for name, d, vr, vt in SYSTEMS:
        print("  %-20s %8.3f %10.1f %12.1f %14.6f"
              % (name, d, transit_years(d), lead_angle(d, vt*1e3)*206264.806,
                 matched_vwarp(vr*1e3)))
    print("""
      Alpha Centauri needs a lead of 333 arcsec -- five and a half arcminutes,
      a fifth of the Moon's width -- and Barnard's Star, fast and near, needs
      1297.  These are not pointing tolerances, they are aiming OFFSETS, and
      they are why a gate cannot simply be pointed at where its partner looks.

      Because the shift is a vector, ONE GATE SERVES ONE DIRECTION.  Re-aiming
      means restructuring the whole %.1e J circulation pattern, so a gate is
      committed to its partner at construction, and a hub serving several
      destinations is several gates.

  SO: identical hardware, two settings.  Every gate is the same ~1.1 Msun,
  4.9 km object; each is aimed at exactly one partner and tuned to that
  partner's radial velocity.  A route is a MATCHED PAIR, built to each other.

5. OPEN, AND WHERE
------------------
  1  SWITCHING the shift while a payload is inside      (launcher.py)
  2  FLOW TOPOLOGY: accretion is toroidal, the metric needs poloidal   (2b)
  3  INGRESS: holding a bore open through the wall      (3)
  None is forbidden by any theorem. All three are mechanism, not permission.
""" % E_STORE)
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
