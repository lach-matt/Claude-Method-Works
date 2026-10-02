#!/usr/bin/env python3
"""
ARRIVAL.py -- stopping.  The hole this project deferred four times.

A drive that cannot stop is not an engine.  Three braking routes, priced.

  1 REVERSE SLINGSHOT.  The coupling is time-symmetric: a pass with the
    deflector receding is the time reverse of a head-on pass from rest, so
    a ship arriving at exactly 2U/(1+U^2) is returned to rest.  The law is
    additive in RAPIDITY, not in speed: head-on theta_f = theta_w + 2 artanh U,
    tail-on theta_f = 2 artanh U - theta_w.  Hypotheses: H-ISOLATED (an
    isolated deflector, unaccelerated during the encounter) and H-TEST
    (test-particle limit, no radiation reaction).  Free of propellant --
    the steering precision is not priced -- but it needs a deflector AT THE
    DESTINATION, which turns the drive into a NETWORK with nodes.
  2 PHOTON BRAKING.  Relativistic rocket, exhaust at c:
        M0/M1 = sqrt((1+beta)/(1-beta)) = gamma(1+beta)
    This is a floor on the REST-MASS ratio for self-contained reaction
    propulsion (H-SELF: momentum leaves only through the vehicle's own
    exhaust; Le 2606.22531v4 Lemma 2.1, READ), in flat spacetime with a
    collimated exhaust and a straight burn -- relaxing any of those three
    only raises the ratio.  It is not a floor per unit energy LIBERATED:
    photon exhaust carries the least momentum per unit liberated energy.
    Routes 1 and 3 lie outside H-SELF.
  3 MAGNETIC SAIL against the interstellar medium.  Drag on an effective
    area A; no reaction mass, but it needs distance.

Kinematics throughout: flat spacetime, an inertial Earth frame at rest with
respect to the destination, and the clock hypothesis.  Trip times are at
constant beta and are FLOORS for any real speed profile (d(beta gamma)/d beta
= gamma^3 > 0).

CORRECTED (DOCKET 67).  As first written this file said: the receding pass
gives "dv = 2U/(1+U^2) either way" / "the same magnitude negative" (true as a
velocity change only for incoming speed 2U/(1+U^2): at 0.866 c and U = 0.35 c
the speed falls by 0.339, not 0.624); "no propulsion does better per unit
energy" (drops H-SELF, and the bound is on rest mass, not energy); "2.73 tonnes
of perfect antimatter" (2.73 t is the total converted mass; the antimatter
share is 1.37 t); "76x the fuel ratio" (computes to 55.99); a magsail that
"brakes ... inside 810 AU" and needs "2.6 ly" from 0.87 c (the function gives
floors of 2001.64 AU and 0.084 ly at A = 1e12 m^2, and a floor is not a
distance to rest); and N_ISM labelled "warm neutral medium".  The selftest pin
3.7314 is now the computed 3.731672.  No verdict moved.

stdlib only.
"""
import math, sys

c    = 299792458.0
AU   = 1.495978707e11
LY   = 9.4607304726e15
PC   = 3.0856775815e16
M_P  = 1.67262192e-27  # CODATA 2018 m_p (1.67262192369e-27) cut to 9 figures: -2.21e-9
N_ISM = 1.0e6          # 1 H/cm^3 in m^-3 -- the all-phase space AVERAGE (Ferriere 2001 p.5);
                       # not the warm neutral medium (0.2-0.5 cm^-3, Ferriere Table I)
RHO_ISM = N_ISM*M_P    # H-H-ONLY: rho = n m_p, without Ferriere's x1.42 helium/metal factor

def gamma(b):
    return 1.0/math.sqrt(1.0-b*b)

def photon_mass_ratio(b):
    """M0/M1 to change speed by beta with exhaust at c.  Equals gamma(1+beta)."""
    return math.sqrt((1.0+b)/(1.0-b))

def slingshot_dv(U, head_on=True):
    """dv = 2U/(1+U^2), the strong-field (full-reversal) limit, for a ship
    initially at rest in the frame where the deflector moves at U.  Sign is
    the encounter geometry.  head_on=False is the time reverse: it returns a
    ship arriving at exactly 2U/(1+U^2) to rest, and holds for that incoming
    speed only -- for any other, add rapidities, not speeds.  H-ISOLATED,
    H-TEST (module docstring)."""
    d = 2.0*U/(1.0+U*U)
    return d if head_on else -d

def magsail_distance(m, b, A, rho=RHO_ISM):
    """Distance to brake mass m from beta to rest on drag F = rho v^2 A.

    Relativistic kinetic energy (gamma-1)mc^2 dissipated at F dx = rho v^2 A dx.
    v falls during the brake; integrating dE/dx = -rho v^2 A with E = (gamma-1)mc^2
    is not closed-form, so this uses the ENERGY/INITIAL-DRAG estimate
        L ~ (gamma-1) m c^2 / (rho (beta c)^2 A)
    which UNDERSTATES the true distance (drag weakens as it slows).  Labelled
    accordingly wherever reported: it is a floor, not an answer -- under this
    law no finite distance brings the ship to rest (at x = L it still has
    60.7% of its speed), so L is never a distance to rest.

    Hypotheses, each narrower than every READ magsail law (Gros 2017):
      H-CONST-A    constant effective area; every READ law makes A depend on v
      coefficient 1 (momentum absorbed); full reflection is 2 (Gros eq. 1)
      H-ALL-NUCLEI rho counts every nucleus; a magsail reflects ions only
                   (READ local ion density 0.05-0.21 cm^-3, 0.005-0.04 in the
                   Local Bubble)
      low beta     every READ model is non-relativistic
    No magsail source is cited by this file.
    """
    E = (gamma(b)-1.0)*m*c**2
    return E/(rho*(b*c)**2*A)

def trip_time_ly(dist_ly, b):
    """Coordinate (Earth-frame) years to cross dist_ly at constant beta."""
    return dist_ly/b

def proper_time_ly(dist_ly, b):
    """Shipboard years -- the crew's clock -- at constant beta."""
    return dist_ly/(b*gamma(b))

def selftest():
    ok = True
    def chk(label, got, want, tol=1e-6):
        nonlocal ok
        good = abs(got-want) <= tol*abs(want) if want else abs(got) < 1e-12
        ok &= good
        print("  %-56s %14.8g %14.8g  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("Relativistic rocket -- two independent forms must agree")
    for b in (0.0476, 0.5, 0.866, 0.99):
        chk("M0/M1 at beta=%.4f  == gamma(1+beta)" % b,
            photon_mass_ratio(b), gamma(b)*(1.0+b), tol=1e-12)
    # CORRECTED (DOCKET 67): first pinned 3.7314 at tol 1e-4; computed 3.7316716.
    chk("M0/M1 at beta = 0.866 (gamma = 2)", photon_mass_ratio(0.866), 3.7316716, tol=1e-6)
    chk("M0/M1 at the shell's 0.0476 c", photon_mass_ratio(0.0476), 1.0487888, tol=1e-6)
    chk("M0/M1 -> 1 as beta -> 0", photon_mass_ratio(1e-9), 1.0, tol=1e-8)

    print("\nTime symmetry of the coupling -- braking is departure run backwards")
    chk("head-on gain at U = 0.35 c", slingshot_dv(0.35), 0.6236080, tol=1e-6)
    # This row checks the sign flip only: it is d + (-d), zero by construction.
    chk("sign flip: tail-on is the negative of head-on",
        slingshot_dv(0.35) + slingshot_dv(0.35, head_on=False), 0.0)
    # The time-symmetry check proper: arriving at 2U/(1+U^2) against a
    # deflector receding at U ends at rest (rapidities add).
    chk("time reverse: arrive at 2U/(1+U^2), recede at U -> rest",
        math.tanh(math.atanh(slingshot_dv(0.35)) - 2.0*math.atanh(0.35)), 0.0)
    # Limits, not a restatement of the formula:
    chk("dv -> 2U as U -> 0 (Newtonian slingshot)", slingshot_dv(1e-6)/1e-6, 2.0, tol=1e-9)
    chk("dv -> c as U -> c (full reversal)", slingshot_dv(1.0), 1.0, tol=1e-12)
    chk("dv is maximal at U = c", max(slingshot_dv(u/1000.0) for u in range(1,1001)), 1.0, tol=1e-12)

    print("\nKinematics")
    chk("gamma at 0.866 c", gamma(0.866), 2.0, tol=1e-3)
    chk("4.24 ly at 0.866 c, Earth frame (yr)", trip_time_ly(4.24, 0.866), 4.8961, tol=1e-4)
    chk("  shipboard (yr)", proper_time_ly(4.24, 0.866), 2.4487, tol=1e-3)
    chk("4.24 ly at 0.0476 c, Earth frame (yr)", trip_time_ly(4.24, 0.0476), 89.076, tol=1e-4)

    print("\nMagsail floor (understates: drag weakens as it slows)")
    d = magsail_distance(1e6, 0.0476, 1e12)/AU
    chk("1e6 kg, beta=0.0476, 1e12 m^2 sail (AU)", d, 2001.64, tol=1e-4)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print("="*78)
    print("ARRIVAL -- the hole this project deferred four times")
    print("="*78)
    print("""
A drive that cannot stop is not an engine.  THE-BORROWED-WELL, THE-GR-FLYBY,
THE-ENGINE and COUPLING each flagged arrival and each deferred it.  Priced:

-- 1. Reverse slingshot: free, and it changes what the drive IS -------------
  The coupling is TIME-SYMMETRIC.  dv = 2U/(1+U^2) from rest with the
  deflector approaching; with it receding, a ship arriving at exactly
  2U/(1+U^2) is returned to rest.  Speeds do not add between passes,
  rapidities do.  Braking is departure run backwards and costs no
  propellant.  The steering is not priced: full reversal at 0.35 c around
  Schwarzschild needs the impact parameter held to |db| ~ 0.01 M.
  Hypotheses: H-ISOLATED, H-TEST.

  But it needs a deflector AT THE DESTINATION.  That is the real finding:
  the drive is not a vehicle capability, it is a NETWORK.  You can travel
  between nodes that carry a compact moving mass, and nowhere else.  The
  reachable set is the set of BH and NS binaries -- which are not places
  anyone wants to be, so the last leg is always someone else's problem.

-- 2. Photon braking: the floor, and it is brutal at high beta -------------""")
    print("  %-14s %10s %14s %16s" % ("arrival speed", "gamma", "M0/M1", "fuel per tonne"))
    for b, lbl in ((0.0476,"shell 0.048c"), (0.100,"0.10 c"), (0.316,"0.32 c"),
                   (0.622,"flyby 0.62c"), (0.866,"engine 0.87c"), (0.99,"0.99 c")):
        r = photon_mass_ratio(b)
        print("  %-14s %10.3f %14.4f %13.2f t" % (lbl, gamma(b), r, r-1.0))
    print("""
  Read the first and last rows together.  This is the trade the project never
  made: THE-ENGINE's 0.87 c costs 2.73 tonnes converted wholly to photons per
  tonne landed (1.37 t of it antimatter), while THE-DRIVE's 0.048 c costs 49
  KILOGRAMS (24 kg antimatter).  The slingshot's speed
  is free to acquire and expensive to shed, and the shell's is neither.

  So the shell is NOT strictly dominated, and this project said it was.  The
  two designs occupy different regimes (constant-beta cruise: the times are
  floors, and at 0.866 c a 1 g accelerate-and-brake profile takes 3.881 yr
  shipboard, not 2.448):""")
    for b, lbl in ((0.0476,"shell"), (0.866,"slingshot")):
        print("     %-10s 4.24 ly in %7.1f yr Earth / %6.1f yr shipboard, M0/M1 = %.3f"
              % (lbl, trip_time_ly(4.24,b), proper_time_ly(4.24,b), photon_mass_ratio(b)))
    print("""
  18x the speed for 56x the fuel per tonne landed.  Whether that is worth it is a mission
  question, not a physics one -- but it is a question, and the project had
  been answering it by assumption.

-- 3. Magnetic sail: no reaction mass, but it needs room -------------------
  Drag against the ISM at 1 H/cm^3, the all-phase average, every
  nucleus counted (H-ALL-NUCLEI; a magsail reflects ions only).  Distances are
  FLOORS -- drag weakens as the ship slows, so the true figure is larger.""")
    print("  %-16s %14s %18s" % ("sail area", "from 0.048 c", "from 0.87 c"))
    for A, lbl in ((1e10,"100 km"), (1e12,"1000 km"), (1e14,"10,000 km")):
        d1 = magsail_distance(1e6, 0.0476, A)/AU
        d2 = magsail_distance(1e6, 0.866, A)/LY
        print("  %-16s %11.0f AU %15.2f ly" % (lbl, d1, d2))
    print("""
  A 1000 km magsail (A = 1e12 m^2) needs at least 2002 AU to brake a 1000 t
  ship from the shell's 0.048 c, with NO fuel -- a floor under H-CONST-A,
  coefficient 1 and H-ALL-NUCLEI, not a distance to rest.  At the READ ion
  densities, 0.21 to 0.005 cm^-3, the floor is 9,532 to 400,328 AU: not
  within a target system.  From 0.87 c the same law gives a floor of 0.084 ly,
  but 0.87 c is outside every READ magsail model, all of them
  non-relativistic.  The READ magsail models are low-beta models, and that is
  a second reason the two designs are not competing for the same mission.

-- The conclusion the project needed and did not have ----------------------
  ARRIVAL IS SOLVED AT LOW BETA AND UNSOLVED AT HIGH BETA.

  * 0.048 c  -- magsail, no fuel, a 2002 AU floor under H-CONST-A and
                H-ALL-NUCLEI (9,532-400,328 AU at READ ion densities).  Closed.
  * 0.87 c   -- reverse slingshot IF the destination has a deflector receding
                at U = 0.577 c (one pass), or a binary that returns and
                re-steers the ship (1.8 passes at U = 0.35 c, 3.2 at 0.20 c,
                16 at 0.04 c); else a mass ratio of 3.73 at 100% conversion
                (H-SELF).  Open.

  The engine's speed advantage is real going out and is charged back on the
  way in.  Any honest mission profile must carry BOTH numbers, and none of
  the nine papers before this one did.
""")
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
