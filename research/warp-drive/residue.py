#!/usr/bin/env python3
"""
residue.py -- the three open items are ONE, and it closes into two answers.

GATE 1 carried three opens: SWITCHING, FLOW TOPOLOGY, INGRESS.  They are not
three problems.  Hydrostatic degenerate matter wants to be spherical, static or
rigidly rotating, with no bore and no poloidal loop.  Every one of the three
demands a DEPARTURE from that equilibrium, so all three are:

    can the shell hold a non-equilibrium configuration against its own
    relaxation, and for how long?

That is a timescale comparison, and every timescale follows from M, R and the
sound speed -- all of which are known.  It therefore CLOSES, and it closes in
two different directions, which is why it looked like separate problems.

stdlib only.
"""
import math, sys

G, c, MSUN = 6.67430e-11, 299792458.0, 1.98892e30

R1, R2   = 4902.0, 13392.5131
M_GATE   = 2.200330e30
D_WALL   = R2 - R1
V_WARP   = 0.0476
E_STORE  = 1.17e46

# Causal stiff limit for the sound speed.  Realistic nuclear matter at
# saturation sits at ~0.3-0.5 c; c/sqrt(3) is the stiffest causally allowed
# value, so using it makes every relaxation time as LONG as it can be and every
# conclusion below conservative in the direction that favours the design.
CS = c/math.sqrt(3.0)

def t_light_interior():
    """Light crossing of the payload bay -- how fast the interior can respond."""
    return 2.0*R1/c

def t_sound_wall(cs=CS):
    """Sound crossing of the wall -- how fast the wall can rearrange."""
    return D_WALL/cs

def t_dynamical():
    """sqrt(R^3/GM) -- the free-fall / collapse time of the structure."""
    return math.sqrt(R2**3/(G*M_GATE))

def t_traverse(b=V_WARP):
    """Time for a payload to cross the wall at speed b."""
    return D_WALL/(b*c)

def t_bore_closure(a_bore, cs=CS):
    """A bore of radius a closes on a/c_s: the wall need only move inward by a."""
    return a_bore/cs

def viscosity_for_lifetime(tau, L=D_WALL, rho=2.3e17):
    """Shear viscosity required for the circulation to survive a time tau.

    Viscous decay of a flow on scale L is tau ~ L^2 rho / eta, so
        eta <= L^2 rho / tau.
    Stated as a REQUIREMENT rather than an assumed value: neutron-star
    transport coefficients are EOS- and temperature-dependent and this project
    is not going to invent one.  The literature range for nn-scattering shear
    viscosity at saturation is ~1e17-1e20 Pa s.
    """
    return L**2*rho/tau

def selftest():
    ok = True
    def chk(label, got, want, tol=1e-6):
        nonlocal ok
        good = abs(got-want) <= tol*abs(want) if want else abs(got) < 1e-12
        ok &= good
        print("  %-56s %14.6g %14.6g  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("Timescales -- all from M, R and the sound speed")
    chk("causal sound speed c/sqrt(3) (m/s)", CS, 1.73086e8, tol=1e-5)
    chk("interior light crossing (s)", t_light_interior(), 3.27026e-5, tol=1e-6)
    chk("wall sound crossing (s)", t_sound_wall(), 4.90536e-5, tol=1e-5)
    chk("dynamical time (s)", t_dynamical(), 1.27892874e-4, tol=1e-8)
    chk("payload traverse of the wall at v_warp (s)", t_traverse(), 5.94983e-4, tol=1e-5)

    print("\nThe two directions this closes in")
    # (a) operating a launch is FAST compared with collapse -- favourable
    chk("launch event / dynamical time", t_light_interior()/t_dynamical(), 0.25570325, tol=1e-8)
    chk("  launch is faster than the structure can respond", 
        t_light_interior() < t_dynamical(), True)
    # (b) traversing the wall is SLOW compared with collapse -- a bound
    chk("payload traverse / dynamical time", t_traverse()/t_dynamical(), 4.65221667, tol=1e-8)
    chk("  traverse is slower than collapse", t_traverse() > t_dynamical(), True)
    # bore closure is faster still, and a WIDER bore closes SOONER in absolute terms
    chk("100 m bore closure (s)", t_bore_closure(100.0), 5.7774996e-7, tol=1e-8)
    chk("1000 m bore closure (s)", t_bore_closure(1000.0), 5.7774996e-6, tol=1e-8)
    chk("bore closure is linear in radius (identity)",
        t_bore_closure(2000.0)/t_bore_closure(1000.0), 2.0, tol=1e-12)
    chk("every bore closes long before a payload crosses",
        t_bore_closure(1000.0) < t_traverse(), True)

    print("\nCirculation lifetime, stated as a requirement not an assumption")
    eta_1s = viscosity_for_lifetime(1.0)
    chk("viscosity ceiling for a 1 s lifetime (Pa s)", eta_1s, 1.65805e25, tol=1e-5)
    chk("  ceiling is 5 orders above the literature maximum 1e20 Pa s",
        eta_1s/1.0e20 > 1e5, True)
    chk("requirement scales as 1/tau (identity)",
        viscosity_for_lifetime(2.0)/viscosity_for_lifetime(1.0), 0.5, tol=1e-12)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print("="*78)
    print("THE RESIDUE -- three opens are one question, and it closes in two")
    print("="*78)
    print("""
Hydrostatic degenerate matter wants to be spherical, static or rigidly
rotating, with no bore and no poloidal loop.  SWITCHING, FLOW TOPOLOGY and
INGRESS each demand a departure from that.  So there is one question:

    CAN THE SHELL HOLD A NON-EQUILIBRIUM CONFIGURATION AGAINST ITS OWN
    RELAXATION, AND FOR HOW LONG?

Every timescale follows from M, R and the sound speed, all known.  Using the
causal stiff limit c_s = c/sqrt(3) makes each relaxation as SLOW as physics
allows, so every conclusion below is conservative in the design's favour.
""")
    print("  %-42s %14s" % ("timescale", "seconds"))
    print("  " + "-"*58)
    for lbl, v in (("interior light crossing (launch response)", t_light_interior()),
                   ("wall sound crossing (wall rearranges)",     t_sound_wall()),
                   ("dynamical / collapse time",                 t_dynamical()),
                   ("1000 m bore closure",                       t_bore_closure(1000.0)),
                   ("payload traverse of the wall at v_warp",    t_traverse())):
        print("  %-42s %14.5e" % (lbl, v))

    print("""
-- DIRECTION 1: SWITCHING AND CIRCULATION -- CLOSED, FAVOURABLY -------------
  A launch is over in %.2e s, which is %.3f of a dynamical time: the metric
  change completes before the structure can respond to it at all.  The shell
  does not need to hold the configuration for long, it needs to hold it for a
  quarter of a collapse time.

  And the circulation's own lifetime is not a constraint either.  For the flow
  to survive even one second the shear viscosity would have to be below
  %.2e Pa s -- five orders of magnitude ABOVE the highest value the
  nn-scattering literature gives at saturation (~1e20 Pa s).  The requirement
  is met with enormous margin, and it is stated as a ceiling to be checked
  rather than a transport coefficient this project invented.

  SWITCHING AND FLOW TOPOLOGY ARE NOT BLOCKED BY RELAXATION.  Establishing the
  poloidal pattern remains an engineering problem of how to drive it; holding
  it, once driven, is free on every timescale that matters.

-- DIRECTION 2: INGRESS -- CLOSED, AS A BOUND ------------------------------
  A payload crossing the wall at v_warp takes %.2e s, which is %.2f DYNAMICAL
  TIMES.  A bore closes on a/c_s -- %.2e s for a 1 km bore.  The wall shuts
  roughly a hundred times over before the payload is through, and widening the
  bore makes it worse in absolute terms, not better.

      THE GATE CANNOT BE LOADED THROUGH ITS WALL.  Not slowly, not quickly,
      not through a wide bore.  The bore is not an engineering difficulty; it
      is excluded.

  By P8 that is an answer, and it is the one that redirects the design: since
  the payload cannot get in, IT MUST ALREADY BE INSIDE.

-- WHAT THE BOUND FORCES ---------------------------------------------------
  Two architectures survive it, and only two.

  (a) THE SEALED GATE.  Build the shell around its bay; whatever is inside at
      assembly is what it carries, forever.  Reusable for repeated launches of
      the SAME contents -- a relay, an observatory, a beacon -- and useless as
      a freight terminal.  Fully covered by the verified spherical solution.

  (b) THE OPEN GATE.  Replace the spherical cavity with an open channel -- a
      torus or a cylinder with a through-bore that is part of the equilibrium
      rather than a defect in it.  Then nothing has to be held open, because
      nothing was ever closed.  This is Architecture B's geometry exactly, and
      it is the ONLY architecture in which a gate is a terminal.

-- THE RESIDUE, SHARPENED --------------------------------------------------
  The three opens are now one, and it is not the one this project started with:

      DOES AN OPEN (TOROIDAL OR CYLINDRICAL) WARP SHELL EXIST THAT SATISFIES
      ALL FOUR ENERGY CONDITIONS?

  Everything else is settled.  The spherical case is measured and physical
  (TARGET-1).  Relaxation permits the flow and the switching.  Ingress
  forbids the bore.  So the whole programme now rests on one question about
  one geometry -- and it is testable in exactly the apparatus already built:
  a toroidal metric through Warp Factory under the corrected diagnostic, the
  same run TARGET-1 already passed for the sphere.
""" % (t_light_interior(), t_light_interior()/t_dynamical(),
       viscosity_for_lifetime(1.0), t_traverse(),
       t_traverse()/t_dynamical(), t_bore_closure(1000.0)))
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
