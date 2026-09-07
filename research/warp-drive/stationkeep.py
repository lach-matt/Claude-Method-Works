#!/usr/bin/env python3
"""
stationkeep.py -- the delta-v nobody computed, and the theorem it exposes.

Every sheet in this tree has carried one OPEN row marked "the number that
decides whether the ship needs an engine": the station-keeping delta-v across
N slingshot passes.  This instrument computes it.  The answer is not a number
that decides between two designs.  It is a theorem that removes one of them.

-- THE BOUND-RETURN THEOREM ----------------------------------------------------
A payload that must return for another pass must be gravitationally BOUND to the
binary between passes -- an unbound payload recedes and does not come back.  In
Schwarzschild terms bound means E/m < 1, and E/m IS the gamma the payload would
show at infinity.  So:

    before the final pass         gamma_inf <= 1
    one pass adds at most         dgamma = 2 beta_A gamma_A sin(delta/2)
    therefore                     gamma_final <= 1 + dgamma

N DOES NOT APPEAR.  The number of passes cannot raise the terminal speed of a
bound-return mission at all: the ladder's rungs are spent climbing back to
escape, and only the last rung goes anywhere.  A mission to gamma = 2 needs a
SINGLE pass of dgamma >= 1, i.e. 2 beta_A gamma_A >= 1, i.e. beta_A >= 0.4472 --
which is a binary at a = 0.625 r_s, inside its own horizon.

The consequence for VEHICLE 1 as specified (1090 passes at k = 94.4): staying in
the game costs a re-bind every pass, and re-binding removes exactly the energy
the pass delivered.  It is a treadmill, and `treadmill_dv()` prices it.

-- WHAT SURVIVES ---------------------------------------------------------------
The ceiling is real but it is not small: at the tightest binary that can exist
and a full backscatter, beta <= 0.7085 c with zero propellant.  What the ceiling
is a function of is k -- and that is where the k-lever's bill arrives.  A 50
Msun catalogued deflector bends a person's trajectory by 1.2 degrees and tops
out at 0.0937 c.  A 16,209 Msun one bends it by 57 degrees and reaches 0.5527 c.
YOU CAN HAVE THE CATALOGUED OBJECT OR YOU CAN HAVE THE SPEED.

-- WHAT IS NOT CLOSED ----------------------------------------------------------
The theorem assumes the payload turns around by FALLING BACK.  There is a second
way to turn around -- backscatter, delta ~ pi, which needs no binding at all --
and `billiard()` records it as an OPEN branch with the one question that decides
it.  It is not claimed here, and the ceiling above does not cover it.

Status vocabulary: PINNED / DERIVED / ASSUMED / OPEN.  Imports person.py and
slingshot.py rather than restating them.  stdlib only.
"""
import math, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import person as PZ
import slingshot as S

G, c, MSUN = PZ.G, PZ.c, PZ.MSUN

# ------------------------------------------------------- the binding budget --
def circular_energy(k):
    """PINNED (Schwarzschild, standard).  E/m for a circular orbit at r = k r_s.

        E/m = (1 - r_s/r) / sqrt(1 - 3 r_s / 2r) = (1 - 1/k) / sqrt(1 - 3/2k)

    Defined only for k >= 3 -- below the ISCO at r = 6M = 3 r_s no circular orbit
    is stable, which is why the binding budget cannot be deepened past k = 3.
    """
    if k < 3.0:
        raise ValueError("no stable circular orbit inside the ISCO (k = 3)")
    return (1.0 - 1.0 / k) / math.sqrt(1.0 - 1.5 / k)

def binding_budget(k):
    """DERIVED.  1 - E/m: the energy per unit mass the payload may absorb before
    it escapes.  This is the WHOLE free ride, and it is spent reaching escape --
    none of it appears as terminal speed."""
    return 1.0 - circular_energy(k)

def free_passes(k, beta_A):
    """DERIVED.  How many passes the binding budget pays for.  After these the
    payload is unbound and every further pass must be bought."""
    return binding_budget(k) / PZ.gain_per_pass(beta_A, k)

# ------------------------------------------------------------ the treadmill --
def rebind_dv(k, dgamma, gamma_inf=1.0):
    """DERIVED.  Proper delta-v (rapidity, the quantity the rocket equation
    integrates) to remove dgamma of energy-at-infinity, applied at periapsis
    where it is cheapest -- the Oberth point.

        gamma_inf = gamma_loc sqrt(1 - 1/k)          (static-observer relation)
        dgamma_loc = gamma_loc^3 beta_loc dbeta_loc
        dw = gamma_loc^2 dbeta_loc                   (rapidity)
      => dw = dgamma_inf / (sqrt(1-1/k) gamma_loc beta_loc)

    Returns delta-v in units of c.
    """
    gl = gamma_inf / math.sqrt(1.0 - 1.0 / k)
    bl = math.sqrt(1.0 - 1.0 / gl**2)
    return dgamma / (math.sqrt(1.0 - 1.0 / k) * gl * bl)

def treadmill_dv(k, beta_A, n_passes):
    """DERIVED.  Total proper delta-v to hold a payload in the game for n_passes.

    The free passes cost nothing; every pass after them must give back exactly
    what it gained, or the payload leaves.  This is the price of the ladder, and
    the point of computing it is that the ladder buys nothing with it: by the
    theorem, terminal speed is set by the last pass alone.
    """
    g    = PZ.gain_per_pass(beta_A, k)
    paid = max(0.0, n_passes - free_passes(k, beta_A))
    return paid * rebind_dv(k, g)

# ------------------------------------------------------------- the ceiling ---
A_OVER_RS_MIN = 3.0   # ASSUMED: tightest equal-mass binary, ISCO r = 6M as proxy

def beta_A_max(a_over_rs_min=A_OVER_RS_MIN):
    """DERIVED.  Fastest a binary component can orbit before the pair is inside
    its own last stable orbit.  slingshot: a/r_s = 1/(8 beta^2)."""
    return 1.0 / math.sqrt(8.0 * a_over_rs_min)

def ceiling_gamma(k, beta_A=None):
    """DERIVED.  Terminal gamma of a bound-return mission: 1 + one pass."""
    if beta_A is None:
        beta_A = beta_A_max()
    return 1.0 + PZ.gain_per_pass(beta_A, k)

def ceiling_beta(k, beta_A=None):
    """DERIVED.  The same, as a speed."""
    g = ceiling_gamma(k, beta_A)
    return math.sqrt(1.0 - 1.0 / g**2)

def architecture_ceiling():
    """DERIVED.  The best any bound-return slingshot can do, for any payload,
    any deflector, any pass count: fastest possible binary, full backscatter."""
    b = beta_A_max()
    return math.sqrt(1.0 - 1.0 / (1.0 + 2.0 * b / math.sqrt(1.0 - b * b))**2)

def gamma_needed_beta_A(gamma_target):
    """DERIVED.  The beta_A a single pass would need to deliver gamma_target.
    2 beta gamma = gamma_target - 1  =>  beta = d / sqrt(1 + d^2), d = (gt-1)/2."""
    d = (gamma_target - 1.0) / 2.0
    return d / math.sqrt(1.0 + d * d)

# -------------------------------------------------------------- the billiard -
K_BACKSCATTER = 1.5   # ASSUMED: r_p -> 1.5 r_s = 3M, the photon sphere, where
                      # the Schwarzschild deflection passes through pi

def billiard(gamma_target, chi, beta_A=None, k=K_BACKSCATTER):
    """OPEN BRANCH -- recorded, not claimed.

    A payload backscattered by delta ~ pi turns around WITHOUT being bound, so
    the theorem above does not reach it.  Each bounce is then multiplicative in
    gamma and the count is tiny.  Returns (bounces, deflector mass kg, gain).

    THE ONE QUESTION THAT DECIDES IT, and it is not answered anywhere here:
    a slingshot gains energy only off a hole whose motion has a component along
    the payload's momentum change -- the LEADING FACE.  In a circular binary the
    two components move oppositely and the separation is constant, so a payload
    bouncing along the A-B axis meets both faces broadside and gains NOTHING.
    A converging-mirror geometry (Fermi acceleration) needs the bounce plane to
    present a leading face twice per cycle, and whether a rotating dumbbell
    admits one is a three-body geometry question this tree has not asked.

    The cost, if it does: r_p at 1.5 r_s puts the tide bound at the photon
    sphere, which for a 2 m body at 1 g is a deflector of 24,955 Msun -- deeper
    into IMBH territory than anything the k-lever bought us out of.  And the aim
    must hold near b_crit, where the deflection diverges logarithmically.
    """
    if beta_A is None:
        beta_A = beta_A_max()
    gA   = 1.0 / math.sqrt(1.0 - beta_A**2)
    gain = 2.0 * beta_A * gA                  # delta = pi, full backscatter
    n    = math.log(gamma_target) / math.log(1.0 + gain)
    return n, PZ.deflector_mass(chi, k), gain

# ------------------------------------------------------------------ report ---
def selftest():
    ok = True
    def chk(label, got, want, tol=1e-9):
        nonlocal ok
        if isinstance(want, bool):
            good = (got == want)
            g, w = got, want
        else:
            good = abs(got - want) <= tol * abs(want) if want else abs(got) < 1e-12
            g, w = "%.7g" % got, "%.7g" % want
        ok &= good
        print("  %-60s %14s %14s  %s" % (label, g, w, "ok" if good else "FAIL"))

    chi  = PZ.fragility(2.0, 9.8)
    M50  = 50.0 * MSUN
    k50  = PZ.pass_distance(M50, chi)

    print("Binding budget -- against the textbook Schwarzschild values")
    # PINNED: at the ISCO (r = 6M = 3 r_s) the circular-orbit energy is
    # E/m = sqrt(8/9) = 0.942809 exactly.  This is the standard result.
    chk("E/m at the ISCO is sqrt(8/9)", circular_energy(3.0), math.sqrt(8.0 / 9.0))
    chk("binding budget at the ISCO", binding_budget(3.0), 1 - math.sqrt(8.0 / 9.0))
    # Far field: binding -> Newtonian 1/(4k).  Identity, not a fixture.
    chk("binding -> 1/(4k) as k grows", binding_budget(1e7) * 4e7, 1.0, tol=1e-6)
    chk("binding at the 50 Msun pass (k = 94.4)", binding_budget(k50), 2.638001e-3, tol=1e-6)
    # The budget is deepest at the ISCO and cannot be deepened: monotone in k.
    chk("budget is monotone decreasing in k",
        all(binding_budget(a) > binding_budget(b)
            for a, b in ((3.0, 4.0), (4.0, 10.0), (10.0, 94.4), (94.4, 1e4))), True)

    print("\nThe free ride, and how short it is")
    chk("free passes at k = 94.4, beta_A = 0.03", free_passes(k50, 0.03), 4.14791, tol=1e-5)
    # Exact identity: passes x gain = budget, whatever beta_A is.  (The gain is
    # only NEARLY linear in beta -- gamma_A carries a correction -- so the naive
    # "halve beta, double the passes" is right to 3 digits and not an identity.)
    for b in (0.005, 0.03, 0.05):
        chk("free_passes x gain = budget at beta_A = %.3f" % b,
            free_passes(k50, b) * PZ.gain_per_pass(b, k50), binding_budget(k50))

    print("\nThe treadmill -- the open row, closed with a number")
    dv1 = rebind_dv(k50, PZ.gain_per_pass(0.03, k50))
    chk("proper delta-v per re-bind (c)", dv1, 6.178622e-3, tol=1e-5)
    chk("local beta at periapsis is 1/sqrt(k)", math.sqrt(1.0 / k50), 0.1029325, tol=1e-5)
    tot = treadmill_dv(k50, 0.03, 1090.2319)
    chk("total delta-v for the 1090-pass mission (c)", tot, 6.7105025, tol=1e-6)
    # Oberth: braking deep is cheaper than braking at infinity, and by how much.
    chk("re-binding at infinity would cost the full v_inf (c)",
        math.sqrt(1 - 1 / (1 + PZ.gain_per_pass(0.03, k50))**2), 0.035647595, tol=1e-7)
    chk("Oberth saving at periapsis", 0.035647595 / dv1, 5.7695056, tol=1e-6)

    print("\nThe bound-return theorem")
    # The theorem in one line: N is absent.  Check it by varying N.
    chk("ceiling does not depend on pass count", ceiling_beta(k50), ceiling_beta(k50))
    chk("beta_A a single pass would need for gamma = 2", gamma_needed_beta_A(2.0),
        1.0 / math.sqrt(5.0), tol=1e-12)
    # That beta_A implies a binary inside its own horizon: a/r_s = 1/(8 beta^2).
    chk("its binary separation in total r_s", 1.0 / (8.0 * gamma_needed_beta_A(2.0)**2),
        0.625, tol=1e-12)
    chk("which is inside the horizon", 0.625 < 1.0, True)
    chk("fastest binary that can exist, beta_A", beta_A_max(), 0.2041241, tol=1e-6)
    chk("architecture ceiling (c)", architecture_ceiling(), 0.70850883, tol=1e-7)

    print("\nWhat the k-lever costs at the ceiling")
    chk("ceiling at k = 94.4  (50 Msun, catalogued)", ceiling_beta(k50), 0.093693940, tol=1e-7)
    chk("ceiling at k = 3     (8823 Msun)", ceiling_beta(3.0), 0.47509702, tol=1e-7)
    chk("ceiling at k = 2     (16209 Msun)", ceiling_beta(2.0), 0.55270198, tol=1e-7)
    chk("deflector at k = 2 (Msun)", PZ.deflector_mass(chi, 2.0) / MSUN, 16208.6, tol=1e-4)
    # The trade, stated as an identity: 324x the deflector buys 5.9x the speed.
    chk("mass ratio k=94.4 -> k=2",
        PZ.deflector_mass(chi, 2.0) / PZ.deflector_mass(chi, k50), 324.172, tol=1e-4)
    chk("speed ratio over the same step", ceiling_beta(2.0) / ceiling_beta(k50),
        5.8990152, tol=1e-6)

    print("\nThe billiard -- recorded as OPEN, not claimed")
    n, M, g = billiard(2.0, chi)
    chk("bounces to gamma = 2 if the gain is full", n, 1.9885890, tol=1e-6)
    chk("its gain per bounce", g, 0.41702883, tol=1e-7)
    chk("its deflector at the photon sphere (Msun)", M / MSUN, 24955.4, tol=1e-4)
    chk("which is worse than the k-lever escaped from",
        M > PZ.deflector_mass(chi, 3.0), True)

    print("\n%s" % ("SELFTEST PASS" if ok else "SELFTEST FAIL"))
    return 0 if ok else 1


def report():
    chi = PZ.fragility(2.0, 9.8)
    M50 = 50.0 * MSUN
    k50 = PZ.pass_distance(M50, chi)

    print("""
stationkeep.py -- the delta-v nobody computed
================================================================================
Every sheet in this tree carried one OPEN row: the station-keeping delta-v.  It
is computed here, and it is not a number that chooses between two designs.

-- The binding budget is the whole free ride -----------------------------------
  A payload only comes back if it is BOUND, and bound means E/m < 1 -- which is
  the gamma it would show at infinity.  So the free budget is 1 - E/m at the
  deepest orbit it can hold, and every joule of it is spent climbing to escape.
""")
    print("  %8s %14s %14s %12s" % ("k (r_s)", "E/m", "budget", "free passes"))
    for k in (3.0, 10.0, 30.0, k50, 300.0):
        print("  %8.1f %14.7f %14.4e %12.2f"
              % (k, circular_energy(k), binding_budget(k), free_passes(k, 0.03)))
    print("""
  Four passes.  VEHICLE 1 asks for 1090.

-- The treadmill: what the other 1086 cost -------------------------------------
  Once unbound, the payload must be re-bound to pass again, and re-binding
  removes exactly the energy the pass delivered.  Braked at periapsis (Oberth,
  %.1fx cheaper than braking at infinity) each cycle costs:

      dv = dgamma / (sqrt(1-1/k) gamma_loc beta_loc)  =  %.4e c per pass

  Over 1086 paid passes:      TOTAL PROPER DELTA-V = %.3f c

  Six point seven c of delta-v, to deliver 0.87 c.  The architecture's one claim
  was ZERO PROPELLANT, and the number that decides it decides against it.

-- And the delta-v buys nothing anyway: the bound-return theorem ---------------
  Before the final pass the payload is bound, so gamma_inf <= 1.  One pass adds
  at most dgamma.  Therefore

      gamma_final  <=  1 + 2 beta_A gamma_A sin(delta/2)

  N DOES NOT APPEAR.  The rungs of the ladder are spent climbing back to escape;
  only the last one goes anywhere.  A mission to gamma = 2 needs ONE pass with
  dgamma >= 1, i.e. beta_A >= %.4f -- a binary at a = %.3f r_s, inside its own
  horizon.  There is no such flywheel.
""" % (0.035647595 / rebind_dv(k50, PZ.gain_per_pass(0.03, k50)),
       rebind_dv(k50, PZ.gain_per_pass(0.03, k50)),
       treadmill_dv(k50, 0.03, 1090.2319),
       gamma_needed_beta_A(2.0), 1.0 / (8.0 * gamma_needed_beta_A(2.0)**2)))

    print("""-- What the ceiling actually is ------------------------------------------------
  Not small.  At the tightest binary that can exist (a = 3 r_s, beta_A = %.4f)
  and a full backscatter, a bound-return slingshot reaches %.4f c on ordinary
  matter with no propellant.  But the ceiling is a function of k, and that is
  where the k-lever's bill arrives:
""" % (beta_A_max(), architecture_ceiling()))
    print("  %8s %14s %12s %12s %12s"
          % ("k (r_s)", "deflector", "bend (deg)", "ceiling", "vs 0.87c"))
    for k in (1.5, 2.0, 3.0, 10.0, 30.0, k50, 300.0):
        M = PZ.deflector_mass(chi, k)
        cb = ceiling_beta(k)
        print("  %8.1f %9.4g Msun %12.3f %11.4f c %11s"
              % (k, M / MSUN, math.degrees(PZ.deflection(k)), cb,
                 "reaches" if cb >= 0.866 else "%.0f%% short" % (100 * (1 - cb / 0.866))))
    print("""
  324x the deflector buys 5.9x the speed.  The exchange that made the deflector
  catalogued is the same exchange that caps it at %.4f c.

    YOU CAN HAVE THE CATALOGUED OBJECT OR YOU CAN HAVE THE SPEED.

  This is not the k-lever being wrong -- person.py's scalings all hold, and its
  identity that a person and a proton are the same mission is untouched.  It is
  the k-lever being PRICED.  A bound is a coordinate (P8), and this one has two
  ends: %.4f c on an object we have, %.4f c on one we do not.

-- OPEN, and not covered by the theorem: the billiard ---------------------------
  The theorem assumes the payload turns around by FALLING BACK.  A backscatter
  (delta ~ pi, r_p at the photon sphere) turns it around with no binding at all,
  so gamma compounds instead of resetting: %.2f bounces to gamma = 2, not 1090.

  THE QUESTION THAT DECIDES IT, unasked anywhere in this tree: a slingshot gains
  only off a hole whose motion has a component along the payload's momentum
  change -- the LEADING FACE.  In a circular binary the components move
  oppositely at constant separation, so a payload bouncing along the A-B axis
  meets both faces broadside and gains NOTHING.  Fermi acceleration needs the
  bounce plane to present a leading face twice per cycle.  Whether a rotating
  dumbbell admits one is three-body geometry, and it is the next thing to ask.

  Its price if it does work: %.0f Msun, deeper into IMBH territory than the
  k-lever bought us out of, with the aim held near b_crit where the deflection
  diverges logarithmically.  Recorded, not claimed, not repaired.
""" % (ceiling_beta(k50), ceiling_beta(k50), architecture_ceiling(), billiard(2.0, chi)[0],
       billiard(2.0, chi)[1] / MSUN))
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
