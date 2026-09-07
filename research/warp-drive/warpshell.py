#!/usr/bin/env python3
"""
warpshell.py -- the first architecture in this project that closes with no
exotic matter, and what it actually costs.

An T. Le, "Steering a warp drive without exotic matter", arXiv:2606.22531
(v2, 30 June 2026), exhibits an exact solution of the Einstein equations that
is, simultaneously:

    * a warp drive in a precise sense -- an exactly Riemann-flat passenger
      cavity, matched across a timelike shell to a positive-energy exterior;
    * ACCELERATING, by a covariant, matter-derived proper acceleration, which
      no previous positive-energy warp construction achieved;
    * dominant-energy admissible in bulk AND shell, observer-robustly, over all
      timelike and null observers -- not just the comoving Eulerian one;
    * subluminal, causal, and free of closed causal curves.

The exterior is the exact Kinnersley photon rocket (outgoing null dust), the
cavity is vacuum, and the shell is what the field equations return.  Its bulk
energy conditions collapse to one scalar, n_2 >= 0.

WHY THIS MATTERS TO THIS PROJECT, IN TWO SENTENCES.  index3.py's CM-THEOREM
says no isolated system moves its own centre of mass, and this series has
carried it as a hard bound on directive Y since COUPLING.md.  Le's Theorem 1 is
its exact general-relativistic form -- and its exit: an asymptotically flat,
dominant-energy drive with a confined source changes its Bondi four-momentum
ONLY by radiating to null infinity, so the theorem is not evaded, it is PAID.

    CM-THEOREM IS NOT REFUTED.  IT IS SATISFIED, BY RADIATING.

-- THE BUDGET, AND IT IS THE WHOLE ENGINEERING STORY --------------------------
The control law is closed form:                 -m_dot  >=  3 m |a|
integrating to the Tsiolkovsky budget:          m_f/m_0  =  exp(-3 INT|a| du)
and for a rectilinear boost INT|a|du is exactly the net rapidity, so

        m_f / m_0  =  e^{-3 delta_eta}          (universal constant 3)

An ideal photon rocket -- perfect mass-to-light conversion, the best any rocket
can be -- has the same law with constant 1.  So

        (m_f/m_0)_warpshell  =  [ (m_f/m_0)_photon-rocket ]^3

DERIVED HERE, NOT QUOTED: e^{-delta_eta} is the square root of the relativistic
Doppler factor, so the budget has an exact closed form in beta,

        flyby (accelerate only):   m_f/m_0 = [ (1-b)/(1+b) ]^{3/2}
        cruise and stop:           m_f/m_0 = [ (1-b)/(1+b) ]^{3}

which is the SAME Doppler factor beamed.py already uses for the sail, cubed.
At b = 0.2, out and stop, that is exactly 8/27: the ship radiates 70.4% of its
rest mass.  At b = 0.5 it is exactly 1/27 -- 96.3%.  Le's own worked burn is
delta_eta = 0.24, and 1 - e^{-0.72} = 51.32%, reproducing his "about half".

-- WHAT IT DOES NOT BUY, STATED FIRST ------------------------------------------
1. NOT superluminal.  Causal and subluminal, and no claim otherwise.
2. NOT reactionless.  It is a rocket, and a worse one than the best rocket:
   three times the rapidity exponent.
3. NO free fall.  "Passengers feel proper acceleration, not the zero-g free fall
   of an idealized Alcubierre interior."  What vanishes is the TIDAL tensor --
   the cavity is exactly flat, so there is no differential stretching.  That is
   a real result and it is not the popular one.
4. STABILITY IS MARGINAL.  The realized tangential-pressure wall sits exactly on
   the Poisson-Visser marginal curve V''(R) = 0: a radial displacement is a
   neutral zero mode with e-folding time of order a light-crossing time.  Taking
   tau_efold ~= R/c and tau_burn = c delta_eta/a gives the burn-outruns-
   instability criterion delta_eta <= aR/c^2 = lambda <= g(x), COMPUTED BELOW --
   and Le's own worked burn (delta_eta = 0.24, lambda_max = 0.12) misses it by a
   factor 2, consistent with his statement that the safe corner is "restricted".
   A slightly stiffer wall is strictly stable at no cost in dec margin, but is
   "a nearby model, not the realized one".

So the warp feature is exactly one thing: a tidally flat cabin, bought for a
factor 3 in the rocket exponent.  That is the honest trade, and it is the first
one in this project with no negative energy anywhere in it.

-- THE ADMISSIBILITY WINDOWS, ALL UPPER BOUNDS ON COMPACTNESS ------------------
With x = 2m/R (geometric) and lambda = aR/c^2:

    x < 24/25          static thin shell, surface dec strict
    x < 4/5            tangential-pressure wall, dec across its whole width
    x < 2/3            Einstein-Vlasov (collisionless) realization exists
    x + 2 lambda < 4/5 the operative window for the realized radiating wall
    lambda < (1-x)/2   rigorous kinematic ceiling (Prop. 5)
    lambda <~ (24/25 - x)/2   empirical dec envelope, not an inequality
    lambda < 1         Rindler horizon stays off the cavity

There is NO LOWER bound on x, and that is the quiet good news: a low-compactness
warpshell is an ordinary-density object, the acceleration ceiling g(x)c^2/R is
then astronomically loose, and the budget above is mass-independent.  What Le
calls the rocket-warp continuum: at small x the object approaches an idealized
hulled rocket, differing in that its cavity is EXACTLY rather than approximately
Riemann-flat and its exterior is exact null dust.

-- THE DISPUTE, RECORDED AND NOT ADJUDICATED ----------------------------------
Barzegar, Buchert and Vigneron (arXiv:2602.16495) catalogue 37 errors across the
"physical warp drive" literature and prove several no-go theorems, and they are
severe about Lentz, Bobrick-Martire, Fell-Heisenberg and Fuchs et al.  Their
hypotheses are the metric-first, flow-orthogonal, prescribed-shift class.  Le's
construction is worldtube-first and is built explicitly to answer their
covariance and interpretable-matter demands (his Sec. 14.3).  This file records
both and adjudicates neither: what is executable here is the arithmetic of the
budget and the windows, not the standing of the construction.
Note also, since this project cites SSV: BBV report minor errors in
Santiago-Schuster-Visser too, at their Errors 9 and 29.

stdlib only.  Every figure below is computed from the control law; Le's printed
numbers appear only as selftest fixtures, never as sources of a result.
"""
import math, sys

C = 299792458.0
G = 6.67430e-11
M_SUN = 1.98847e30

TSIOLKOVSKY_K = 3.0          # Le, Theorem 5: the universal constant
PHOTON_ROCKET_K = 1.0        # the best any rocket can be

# admissibility thresholds, all in x = 2m/R
X_THIN_SHELL = 24.0 / 25.0
X_TANGENTIAL = 4.0 / 5.0
X_VLASOV     = 2.0 / 3.0

# -- the budget ------------------------------------------------------------

def rapidity(beta):
    return math.atanh(beta)

def doppler(beta):
    """(1-b)/(1+b) -- the same factor beamed.py uses for the sail."""
    return (1.0 - beta) / (1.0 + beta)

def mass_ratio(delta_eta, k=TSIOLKOVSKY_K):
    """m_f/m_0 = exp(-k delta_eta).  k = 3 warpshell, k = 1 photon rocket."""
    return math.exp(-k * delta_eta)

def mass_ratio_from_beta(beta, stop=True, k=TSIOLKOVSKY_K):
    """DERIVED closed form: e^{-eta} = sqrt(doppler), so the budget is a power
    of the Doppler factor -- k/2 per burn, k per out-and-stop pair."""
    burns = 2.0 if stop else 1.0
    return doppler(beta) ** (k * burns / 2.0)

def radiated_fraction(delta_eta, k=TSIOLKOVSKY_K):
    return 1.0 - mass_ratio(delta_eta, k)

def cube_relation(delta_eta):
    """(m_f/m_0)_ws - [(m_f/m_0)_pr]^3 -- an exact zero."""
    return mass_ratio(delta_eta, TSIOLKOVSKY_K) - mass_ratio(delta_eta, PHOTON_ROCKET_K) ** 3

def mission(beta, stop=True):
    """(delta_eta_total, m_f/m_0, radiated fraction) for a cruise."""
    eta = (2.0 if stop else 1.0) * rapidity(beta)
    r = mass_ratio(eta)
    return eta, r, 1.0 - r

def mission_energy(beta, m0_kg, stop=True):
    """Joules radiated.  The mass shed leaves as null dust, so it is m c^2."""
    _, r, frac = mission(beta, stop)
    return frac * m0_kg * C * C

def turn_penalty(eta_arc, eta_net):
    """A steering history has INT|a|du >= |delta_eta| -- boosts do not add as
    vectors -- so a turn costs strictly more than the collinear figure.
    Returns the extra mass fraction radiated."""
    if eta_arc < eta_net:
        raise ValueError("arc cannot be shorter than the net rapidity")
    return mass_ratio(eta_net) - mass_ratio(eta_arc)

# -- the geometry ----------------------------------------------------------

def compactness(m_kg, R_m):
    """x = 2Gm/(Rc^2)."""
    return 2.0 * G * m_kg / (R_m * C * C)

def mass_for(x, R_m):
    return x * R_m * C * C / (2.0 * G)

def kinematic_ceiling(x):
    """Prop. 5, rigorous: lambda = aR/c^2 < (1-x)/2."""
    return 0.5 * (1.0 - x)

def dec_envelope(x):
    """Sec. 8 Eq (29), EMPIRICAL, not an inequality: g(x) <~ (24/25 - x)/2.
    Le states plainly that its derivation is heuristic."""
    return 0.5 * (X_THIN_SHELL - x)

def operative_window(x, lam):
    """The realized radiating tangential-pressure wall: x + 2 lambda < 4/5."""
    return x + 2.0 * lam < X_TANGENTIAL

def a_max(x, R_m, rule=dec_envelope):
    """Proper acceleration ceiling in m/s^2 from lambda = a R/c^2 <= g(x)."""
    return rule(x) * C * C / R_m

def desitter_threshold(y):
    """Sec. 12: x_crit(y) = 24/25 - (4/5) y + O(y^2), y = Lambda R^2/3.
    A positive cosmological constant tightens the window linearly."""
    return X_THIN_SHELL - 0.8 * y

# -- stability -------------------------------------------------------------

def efold_time(R_m):
    """tau_efold ~= R/c.  ORDER OF MAGNITUDE: Le gives 'of order a light-
    crossing time' for the marginal Poisson-Visser wall, not a coefficient."""
    return R_m / C

def burn_time(delta_eta, a_ms2):
    """Proper time to gain delta_eta at proper acceleration a: tau = c eta/a."""
    return C * delta_eta / a_ms2

def radius_to_outrun(delta_eta, a_ms2):
    """R needed for the burn to finish inside one e-folding, from
    delta_eta <= aR/c^2.  Solves for R."""
    return delta_eta * C * C / a_ms2

def accel_to_outrun(delta_eta, R_m):
    """The same criterion solved for a instead."""
    return delta_eta * C * C / R_m

def outrun_shortfall(delta_eta, a_ms2, R_m):
    """How far a design misses the criterion: delta_eta / lambda.
    1 or less passes; the value is the factor by which it fails."""
    lam = a_ms2 * R_m / (C * C)
    return delta_eta / lam

def outruns_instability(delta_eta, x, R_m, lam=None):
    """tau_burn <= tau_efold reduces to delta_eta <= lambda.  Returns
    (verdict, delta_eta, lambda) with lambda = aR/c^2 at the ceiling if unset."""
    if lam is None:
        lam = dec_envelope(x)
    return (delta_eta <= lam), delta_eta, lam

# -- the control law, checked rather than assumed ---------------------------

def control_law_ok(mdot, m, a):
    """-m_dot >= 3 m |a| (geometric units)."""
    return -mdot >= TSIOLKOVSKY_K * m * abs(a)

def saturating_mdot(m, a):
    return -TSIOLKOVSKY_K * m * abs(a)

def integrate_burn(a_peak, duration, m0=1.0, steps=200000):
    """Integrate m_dot = -3 m |a| over a sin^2 bump, Le's App. K profile
    a(u) = a_max sin^2(pi u/T).  Returns (m_f/m_0, INT|a|du)."""
    dt = duration / steps
    m = m0
    eta = 0.0
    for i in range(steps):
        u = (i + 0.5) * dt
        a = a_peak * math.sin(math.pi * u / duration) ** 2
        m += saturating_mdot(m, a) * dt
        eta += a * dt
    return m / m0, eta

# -- selftest ---------------------------------------------------------------

def selftest():
    ok = True
    def chk(label, got, want, tol=None):
        nonlocal ok
        good = (abs(got - want) <= tol) if tol is not None else (got == want)
        ok &= good
        g = ("%.10g" % got) if isinstance(got, float) else str(got)
        w = ("%.10g" % want) if isinstance(want, float) else str(want)
        print("  %-56s %16s %16s  %s" % (label, g, w, "ok" if good else "FAIL"))

    print("The budget is the cube of the ideal photon rocket's")
    for eta in (0.1, 0.24, 0.5, 1.0, 2.5):
        chk("  exact at delta_eta = %.2f" % eta, cube_relation(eta), 0.0, 1e-15)

    print("\n...and therefore a power of the relativistic Doppler factor")
    for b in (0.05, 0.1, 0.2, 0.5, 0.9):
        eta, r, _ = mission(b, stop=True)
        chk("  stop at b = %.2f: closed form == integrated" % b,
            r, mass_ratio_from_beta(b, stop=True), 1e-15)
        eta1, r1, _ = mission(b, stop=False)
        chk("  flyby at b = %.2f" % b, r1, mass_ratio_from_beta(b, stop=False), 1e-15)
    print("      the closed forms are EXACT RATIONALS at nice beta:")
    chk("  b = 0.2, out and stop, is 8/27", mission(0.2)[1], 8.0 / 27.0, 1e-15)
    chk("  b = 0.5, out and stop, is 1/27", mission(0.5)[1], 1.0 / 27.0, 1e-15)
    chk("  b = 0.2 flyby is (2/3)^{3/2}", mission(0.2, False)[1], (2.0/3.0) ** 1.5, 1e-15)

    print("\nLe's printed figures, as fixtures")
    chk("worked burn delta_eta = 0.24 radiates ~51%",
        radiated_fraction(0.24), 0.5132477440, 1e-9)
    chk("thin-shell surface dec window", X_THIN_SHELL, 0.96, 1e-15)
    chk("tangential-pressure wall window", X_TANGENTIAL, 0.8, 1e-15)
    chk("Einstein-Vlasov realization", X_VLASOV, 2.0 / 3.0, 1e-15)
    chk("threshold ordering 2/3 < 4/5 < 24/25",
        X_VLASOV < X_TANGENTIAL < X_THIN_SHELL, True)
    chk("kinematic ceiling at the operating point x* = 0.3",
        kinematic_ceiling(0.3), 0.35, 1e-15)
    chk("envelope at x* = 0.3", dec_envelope(0.3), 0.33, 1e-15)
    chk("Le's lambda_max = 0.12 is inside the envelope at x* = 0.3",
        0.12 < dec_envelope(0.3), True)
    chk("the worked burn is inside the operative window x + 2L < 4/5",
        operative_window(0.3, 0.12), True)
    chk("de Sitter tightens the window: x_crit(0) = 24/25",
        desitter_threshold(0.0), X_THIN_SHELL, 1e-15)
    chk("  ...and x_crit(0.1) = 24/25 - 0.08", desitter_threshold(0.1),
        X_THIN_SHELL - 0.08, 1e-15)

    print("\nThe control law integrates to the budget (sin^2 bump, App. K shape)")
    r_num, eta_num = integrate_burn(a_peak=1.0, duration=0.48)
    chk("  INT|a|du over the bump", eta_num, 0.24, 1e-6)
    chk("  integrated m_f/m_0 == e^{-3 eta}", r_num, mass_ratio(eta_num), 1e-5)
    chk("saturating m_dot satisfies the law", control_law_ok(saturating_mdot(1.0, 0.3), 1.0, 0.3), True)
    chk("anything less does not", control_law_ok(-0.5 * TSIOLKOVSKY_K * 0.3, 1.0, 0.3), False)

    print("\nA turn costs strictly more than the collinear figure")
    chk("arc 0.5 vs net 0.4 sheds extra mass", turn_penalty(0.5, 0.4) > 0.0, True)
    chk("arc == net is free", turn_penalty(0.4, 0.4), 0.0, 1e-15)

    print("\nGeometry: there is no lower bound on compactness")
    chk("x is round-trippable", compactness(mass_for(0.3, 10.0), 10.0), 0.3, 1e-12)
    x_ship = compactness(1.0e6, 10.0)
    chk("a 1000-tonne, 10 m ship is far inside every window",
        x_ship < 1e-20, True)
    print("      x for 1e6 kg at R = 10 m: %.4e" % x_ship)
    print("      a_max there:              %.4e m/s^2 = %.2e g"
          % (a_max(x_ship, 10.0), a_max(x_ship, 10.0) / 9.80665))
    chk("the acceleration ceiling is not the binding constraint",
        a_max(x_ship, 10.0) / 9.80665 > 1e12, True)

    print("\nStability: the criterion, and the paper's own worked burn failing it")
    v, eta, lam = outruns_instability(0.24, 0.3, 10.0, lam=0.12)
    chk("  delta_eta = 0.24 against lambda = 0.12", v, False)
    chk("  it misses by a factor 2", eta / lam, 2.0, 1e-12)
    v2, _, _ = outruns_instability(0.10, 0.3, 10.0, lam=0.12)
    chk("  a briefer burn, delta_eta = 0.10, does outrun it", v2, True)
    chk("tau_efold for R = 10 m", efold_time(10.0), 10.0 / C, 1e-20)
    chk("tau_burn at 1 g for delta_eta = 0.24",
        burn_time(0.24, 9.80665), 0.24 * C / 9.80665, 1e-6)

    print("\n  ...and the SAME criterion applied to a habitable ship")
    short = outrun_shortfall(0.2, 9.80665, 10.0)
    print("      delta_eta = 0.2 at 1 g in a 10 m cavity misses by %.3e" % short)
    chk("  a habitable design misses by more than 10^13", short > 1e13, True)
    chk("  ...to pass at 1 g it needs R (m)", radius_to_outrun(0.2, 9.80665),
        0.2 * C * C / 9.80665, 1e-3)
    print("      that is %.4e m = %.0f AU = %.4f light-year"
          % (radius_to_outrun(0.2, 9.80665),
             radius_to_outrun(0.2, 9.80665) / 1.495978707e11,
             radius_to_outrun(0.2, 9.80665) / 9.4607304726e15))
    print("      or, at R = 10 m, an acceleration of %.4e m/s^2 = %.2e g"
          % (accel_to_outrun(0.2, 10.0), accel_to_outrun(0.2, 10.0) / 9.80665))
    chk("  no O(1) coefficient in tau_efold rescues 14 orders",
        math.log10(short) > 13.0, True)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print(__doc__)
    print("=" * 79)
    print("THE MISSION TABLE -- what a cruise costs in rest mass\n")
    print("  %-6s %8s %10s %12s %12s %12s"
          % ("beta", "eta_tot", "m_f/m_0", "radiated", "photon rkt", "penalty"))
    for b in (0.01, 0.05, 0.1, 0.2, 0.3, 0.5, 0.9):
        eta, r, frac = mission(b, stop=True)
        pr = mass_ratio(eta, PHOTON_ROCKET_K)
        print("  %-6.2f %8.5f %10.6f %11.2f%% %12.6f %11.2fx"
              % (b, eta, r, 100 * frac, pr, pr / r))
    print("\n  (out and stop; a flyby is the square root of each ratio)")

    print("\nENERGY, for a 1000-tonne ship (1e6 kg all-up)\n")
    print("  %-6s %16s %18s" % ("beta", "radiated (J)", "vs world annual"))
    world = 6.0e20
    for b in (0.05, 0.1, 0.2, 0.5):
        e = mission_energy(b, 1.0e6, stop=True)
        print("  %-6.2f %16.4e %14.1f yr" % (b, e, e / world))

    print("\nTHE WINDOWS (x = 2m/R, lambda = aR/c^2)\n")
    print("  %-6s %14s %14s %16s" % ("x", "ceiling", "envelope", "operative L<"))
    for x in (0.0, 0.1, 0.3, 0.5, 0.7, 0.8, 0.96):
        lam_op = max(0.0, 0.5 * (X_TANGENTIAL - x))
        print("  %-6.2f %14.5f %14.5f %16.5f"
              % (x, kinematic_ceiling(x), dec_envelope(x), lam_op))

    print("\nSTABILITY IS THE BINDING CONSTRAINT, NOT THE BUDGET\n")
    print("  criterion: delta_eta <= lambda = aR/c^2   (tau_burn <= tau_efold ~ R/c)")
    print("  %-30s %14s %16s" % ("design", "shortfall", "verdict"))
    for lbl, eta, a, R in (("Le App. K worked burn", 0.24, None, None),
                           ("1 g, 10 m cavity", 0.2, 9.80665, 10.0),
                           ("1 g, 1 km cavity", 0.2, 9.80665, 1000.0),
                           ("1e6 g, 10 m cavity", 0.2, 9.80665e6, 10.0)):
        if a is None:
            sf = 0.24 / 0.12
        else:
            sf = outrun_shortfall(eta, a, R)
        print("  %-30s %14.3e %16s" % (lbl, sf, "passes" if sf <= 1.0 else "FAILS"))
    print()
    print("  to pass at 1 g with delta_eta = 0.2 the cavity must be %.3e m"
          % radius_to_outrun(0.2, 9.80665))
    print("  (%.0f AU); at R = 10 m the ship must pull %.2e g."
          % (radius_to_outrun(0.2, 9.80665) / 1.495978707e11,
             accel_to_outrun(0.2, 10.0) / 9.80665))
    print("  tau_efold ~ R/c is Le's order of magnitude, not a coefficient --")
    print("  but a 14-order shortfall is not an O(1) problem.  The escape he")
    print("  names is a stiffer wall, strictly stable at no cost in dec margin,")
    print("  and it is a nearby model rather than the realized one.")

    print("\nVERDICT")
    print("  Directive Y: an accelerating, positive-energy, dominant-energy-")
    print("  admissible warp drive EXISTS as an exact solution.  It is subluminal,")
    print("  it is a rocket, and it costs the cube of an ideal photon rocket's")
    print("  mass ratio.  CM-THEOREM is not refuted -- it is paid, in radiation.")
    print("  What it buys is one thing: an exactly tidally flat cabin.")
    print("  Open against it: marginal linear stability of the realized wall, which")
    print("  on the light-crossing criterion excludes the habitable regime by 14")
    print("  orders of magnitude.  THAT, not the energy budget, is the wall.")
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
