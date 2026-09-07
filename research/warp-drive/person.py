#!/usr/bin/env python3
"""
person.py -- from a proton to a person.

Zhang's slingshot law is a law about TEST PARTICLES.  A test particle has no
extent, so it feels no tide, so it may pass as close as it likes and take the
full gain.  A person has extent, and the whole difference between the two is
that one number.  This instrument asks what the extent costs and answers in a
single dimensionless group.

    FRAGILITY      chi   = sqrt(d / a_max)          seconds
                   d     = the payload's extent
                   a_max = the tidal acceleration it survives

    DEFLECTOR      tau_s = 2 G M / c^3 = r_s / c    seconds
                   the light-crossing time of the deflector's Schwarzschild
                   radius -- the only thing about the hole that enters.

    THE INVARIANT  chi / tau_s

Everything dimensionless about the mission -- how far out you must pass, how
much you gain per pass, how many passes you need -- is a function of chi/tau_s
alone.  The dimensional part (the clock) scales as M.

  Pass distance   k = r_p / r_s = (chi / tau_s)^(2/3)        DERIVED
  Deflection      delta = 2 / k                              DERIVED (weak field)
  Gain per pass   g = 2 beta gamma_A sin(delta/2)            DERIVED
  Passes          N = ln(gamma_target) / ln(1 + g)           PINNED (Zhang Eq. 30)

The consequence, and it is the point of the file: a PERSON at a 50 Msun binary
and a PROTON at a 1.2e9 kg binary have the SAME chi/tau_s, and are therefore the
same mission -- same k, same gain, same pass count.  The person is not a harder
problem than the proton.  The person needs a bigger flywheel, and the flywheel
is in the LIGO catalogue.

-- A RECORDED FAULT, not repaired ---------------------------------------------
An earlier pass of this calculation fixed the pass distance at a constant
fraction of the binary SEPARATION (r_p = a/3) rather than of the Schwarzschild
radius.  That gives a mass floor scaling as M ~ beta^3, and a headline: a person
needs only 51 Msun at beta = 0.03 instead of 15,241 Msun at beta = 0.2.  The
mass was very nearly right -- and the reasoning was wrong.  At r_p = a/3 the
payload sits 92.6 r_s from the hole, where an ultrarelativistic particle bends
by 1.24 degrees.  The gain there is 6.48e-4 per pass, not the 0.075 that
"gain = 2.5 beta" asserts: overstated by 115.7x.  Slowing the binary does buy
mass cubed, but it buys it at a distance where the slingshot does not slingshot.
The correct lever is k, not beta, and `retracted_beta3_gain()` below computes
the refutation so it cannot be quietly re-derived.  P8: a bound is a coordinate.

Status vocabulary: PINNED (stated in a source) / DERIVED / ASSUMED.
Imports slingshot.py rather than restating its law.  stdlib only.
"""
import math, sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import slingshot as S

G, c, MSUN = S.G, S.c, S.MSUN

# ------------------------------------------------------------- the group -----
def fragility(d, a_max):
    """DERIVED.  chi = sqrt(d / a_max), in seconds.  The payload's whole
    contribution to the problem: extent divided by the tide it survives."""
    return math.sqrt(d / a_max)

def tau_s(M_kg):
    """DERIVED.  r_s / c = 2GM/c^3, in seconds.  The deflector's whole
    contribution."""
    return 2.0 * G * M_kg / c**3

def pass_distance(M_kg, chi):
    """DERIVED.  k = r_p / r_s, the closest pass the payload survives.

    a_tide = 2 G M d / r_p^3 with r_p = k r_s = 2kGM/c^2 gives
        a_tide = c^6 d / (4 k^3 G^2 M^2),
    and setting a_tide = a_max = d / chi^2 gives
        k = (c^3 chi / (2 G M))^(2/3) = (chi / tau_s)^(2/3).
    Note d cancels out of k except through chi.  The extent and the tolerance
    never enter separately -- only their ratio, and only as a 2/3 power.
    """
    return (chi / tau_s(M_kg))**(2.0 / 3.0)

def deflector_mass(chi, k):
    """DERIVED.  Inverse of pass_distance: the hole that puts a payload of
    fragility chi at k Schwarzschild radii.  M = c^3 chi / (2 G k^{3/2}).

    M ~ k^{-3/2}: a smaller deflector is not forbidden, it is bought by passing
    further out.  Since N ~ k, halving the deflector costs 2^{2/3} = 1.587x the
    passes.  That is the exchange rate this file exists to state.
    """
    return c**3 * chi / (2.0 * G * k**1.5)

# ------------------------------------------------------------- the gain ------
def deflection(k):
    """DERIVED.  Bend angle of an ultrarelativistic particle at impact
    parameter b = k r_s:  delta = 4GM/(c^2 b) = 2/k, capped at pi.

    The weak-field formula understates the true GR bend as k -> 1; the cap is
    where it stops being usable at all, and the fixture below records the size
    of the error against Zhang's measured saturation."""
    return min(math.pi, 2.0 / k)

def gain_per_pass(beta_A, k):
    """DERIVED.  Fractional gain in gamma from one pass of a hole moving at
    beta_A, deflecting the payload by delta.

    In the hole's frame the energy is conserved and the direction rotates by
    delta.  Boosting back,  E = gamma_A (E' + v_A p'_x), so for an
    ultrarelativistic payload the best-case change over the entry angle is
        Delta gamma / gamma = 2 beta_A gamma_A sin(delta/2).
    At delta = pi this saturates at 2 beta_A gamma_A -- 0.408 at beta_A = 0.2,
    against the 0.50 Zhang measures.  The 22.5% shortfall is the flat-space
    deflection formula missing the GR excess, and it is recorded, not fitted.
    """
    gA = 1.0 / math.sqrt(1.0 - beta_A**2)
    return 2.0 * beta_A * gA * math.sin(deflection(k) / 2.0)

def passes_to(gamma_target, beta_A, k, gamma0=1.0):
    """PINNED (Zhang Eq. 30), evaluated at the gain this payload can take."""
    return math.log(gamma_target / gamma0) / math.log(1.0 + gain_per_pass(beta_A, k))

# ------------------------------------------------------- the merger budget ---
def margin(gamma_target, beta_A, k):
    """DERIVED.  Orbits the binary has left, divided by the passes needed.

    orbits_to_merger ~ beta^-5 (Peters, via slingshot.py) and N ~ 1/g ~ 1/beta,
    so margin ~ beta^-4: the binary's patience is a STEEP function of how slow
    it is.  Below 1 the flywheel merges mid-mission.
    """
    return S.orbits_to_merger(beta_A) / passes_to(gamma_target, beta_A, k)

def beta_ceiling(gamma_target, k, lo=1e-4, hi=0.25):
    """DERIVED.  Largest orbital speed whose binary survives the mission.
    Bisection on margin = 1; margin is monotone decreasing in beta."""
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if margin(gamma_target, mid, k) > 1.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)

def mission_time(gamma_target, beta_A, k, M_component_kg):
    """DERIVED.  N passes at one pass per binary orbit (ASSUMED cadence,
    inherited from slingshot.py).  Scales linearly with M at fixed beta and k."""
    return passes_to(gamma_target, beta_A, k) * S.orbital_period(beta_A, 2.0 * M_component_kg)

def separation(M_component_kg, beta_A):
    """DERIVED.  a = GM/(2 c^2 beta^2) for an equal-mass circular binary of
    component mass M -- slingshot.a_over_rs written per component."""
    return G * M_component_kg / (2.0 * c**2 * beta_A**2)

# ------------------------------------------------------- the mass ratio ------
# k depends on the DEFLECTOR alone, so the lever above is indifferent to the
# binary's mass ratio.  The ratio is decided somewhere else entirely, and this
# section finds out where.
ROUTH = (9.0 - math.sqrt(69.0)) / 18.0      # PINNED: 0.0385208965, navigate.py

def routh_q_max():
    """DERIVED.  Largest m2/m1 with L4/L5 linearly stable:  mu = q/(1+q) < ROUTH."""
    return ROUTH / (1.0 - ROUTH)

def routh_heavy_floor(M_deflector_kg):
    """DERIVED.  If the deflector is to have a stable co-orbital parking point,
    the OTHER component cannot be lighter than this.  m1 > m2 / q_max."""
    return M_deflector_kg / routh_q_max()

def unequal_binary(M_deflector_kg, q, beta_A):
    """DERIVED.  (separation, period, orbits to merger) for a binary whose FAST
    (light) component is the deflector, moving at beta_A.

    m2 = q m1 orbits the barycentre at r2 = a m1/M_t with
        beta_A^2 = G m1^2 / (a M_t c^2)   =>   a = G m1^2 / (beta_A^2 M_t c^2).
    Peters:  t = (5/256) c^5 a^4 / (G^3 m1 m2 M_t),  T = 2 pi sqrt(a^3/(G M_t)).
    Reduces to slingshot.orbits_to_merger at q = 1; the selftest checks that.
    """
    m2 = M_deflector_kg
    m1 = m2 / q
    Mt = m1 + m2
    a  = G * m1**2 / (beta_A**2 * Mt * c**2)
    T  = 2.0 * math.pi * math.sqrt(a**3 / (G * Mt))
    t  = (5.0 / 256.0) * c**5 * a**4 / (G**3 * m1 * m2 * Mt)
    return a, T, t / T

# --------------------------------------------------------- recorded fault ----
def retracted_beta3_gain(beta_A, f_p=1.0 / 3.0, d=2.0, a_max=9.8):
    """The refutation of the beta^3 claim, kept executable.

    Returns (M_component_kg, k_actual, gain_claimed, gain_true, overstatement).
    The claim set r_p = f_p * a and asserted Zhang's saturated gain there.
    """
    M = 4.0 * c**3 * beta_A**3 * math.sqrt(d / a_max) / (f_p**1.5 * G)
    k = f_p * separation(M, beta_A) / (2.0 * G * M / c**2)
    claimed = S.gain_per_pass(beta_A)          # Zhang's saturated law, 2.5 beta
    true    = gain_per_pass(beta_A, k)
    return M, k, claimed, true, claimed / true

# ---------------------------------------------------------------- payloads ---
# ASSUMED where marked: each a_max is the acceleration at which the body's own
# binding force is exceeded, F/m with F = (binding energy)/(extent).
PAYLOADS = [
    # label                    d (m)      a_max (m/s^2)   status
    ("proton (1 GeV / 1.7 fm)", 1.7e-15,  5.63461e31,     "DERIVED from binding"),
    ("H atom (13.6 eV / a_0)",  1.06e-10, 4.52e22,        "DERIVED from binding"),
    ("1 mm crystal at 1e6 g",   1.0e-3,   9.8e6,          "ASSUMED"),
    ("2 m person at 1 g",       2.0,      9.8,            "ASSUMED"),
    ("20 m hull at 1 g",        20.0,     9.8,            "ASSUMED"),
]

# ------------------------------------------------------------------ report ---
def selftest():
    ok = True
    def chk(label, got, want, tol=1e-9):
        nonlocal ok
        good = abs(got - want) <= tol * abs(want) if want else abs(got) < 1e-12
        ok &= good
        print("  %-62s %13.6g %13.6g  %s" % (label, got, want, "ok" if good else "FAIL"))

    chi_p = fragility(2.0, 9.8)
    M50   = 50.0 * MSUN
    k50   = pass_distance(M50, chi_p)

    print("Identity -- the group is the only argument")
    # 1. pass_distance and deflector_mass are exact inverses.
    chk("deflector_mass(chi, pass_distance(M, chi)) recovers M (Msun)",
        deflector_mass(chi_p, k50) / MSUN, 50.0)
    # 2. CROSS-MODULE: the tide slingshot.py computes at that pass is exactly a_max.
    chk("slingshot.tidal_accel at k r_s across 2 m  (m/s^2)",
        S.tidal_accel(M50, k50, 2.0), 9.8)
    # 3. Scale invariance: double chi and double M -> identical k.
    chk("k(2M, 2chi) equals k(M, chi)", pass_distance(2 * M50, 2 * chi_p), k50)
    # 4. d and a_max never enter separately: 4x the extent at 4x the tolerance
    #    is the same payload.
    chk("k for (d=8 m, a_max=39.2) equals k for (d=2 m, a_max=9.8)",
        pass_distance(M50, fragility(8.0, 39.2)), k50)
    # 5. M ~ k^{-3/2}.
    chk("deflector_mass(chi, 2k) / deflector_mass(chi, k)",
        deflector_mass(chi_p, 2 * k50) / deflector_mass(chi_p, k50), 2.0**-1.5)
    # 6. k ~ M^{-2/3}.
    chk("pass_distance(8M, chi) / pass_distance(M, chi)",
        pass_distance(8 * M50, chi_p) / pass_distance(M50, chi_p), 0.25)

    print("\nProton and person are the same mission")
    chi_q = fragility(1.7e-15, 5.63461e31)
    Mq    = deflector_mass(chi_q, k50)
    chk("proton's matched deflector (kg)", Mq, 1.20914e9, tol=1e-4)
    chk("chi(person)/chi(proton) equals M(person)/M(proton)",
        chi_p / chi_q, M50 / Mq)
    chk("k is identical for both", pass_distance(Mq, chi_q), k50)
    chk("gain per pass is identical for both  (beta = 0.03)",
        gain_per_pass(0.03, pass_distance(Mq, chi_q)), gain_per_pass(0.03, k50))
    # The clock is the only thing that differs, and it differs as M.
    chk("mission_time ratio equals mass ratio",
        mission_time(2.0, 0.03, k50, M50) / mission_time(2.0, 0.03, k50, Mq),
        M50 / Mq)

    print("\nThe gain law against Zhang 2020 (arXiv:2001.09385)")
    # PINNED: 0.50 at beta = 0.2, saturated.  DERIVED here: 2 beta gamma_A.
    sat = gain_per_pass(0.2, 2.0 / math.pi)     # delta = pi
    chk("saturated gain at beta = 0.2  (derived)", sat, 0.408248, tol=1e-5)
    chk("shortfall against Zhang's printed 0.50", S.GAIN_AT_02 / sat, 1.22474, tol=1e-5)
    # Far field: gain -> 2 beta / k, so gain x k is constant.
    chk("gain(beta,k) * k tends to 2 beta gamma_A at large k",
        gain_per_pass(0.03, 1e6) * 1e6, 2 * 0.03 / math.sqrt(1 - 0.03**2), tol=1e-9)

    print("\nThe merger budget")
    # margin ~ beta^-4 in the small-beta regime where gain ~ 2 beta / k.
    chk("margin(beta/2) / margin(beta) at beta = 0.02",
        margin(2.0, 0.01, k50) / margin(2.0, 0.02, k50), 16.0, tol=2e-3)
    bmax = beta_ceiling(2.0, k50)
    chk("margin at the ceiling is exactly 1", margin(2.0, bmax, k50), 1.0, tol=1e-6)
    # Closed form, independent of the bisection.  In the small-beta regime
    # gain -> 2 beta gamma_A / k, so N -> k ln(gamma) / (2 beta gamma_A) and
    #     margin = (C / beta^5) * 2 beta gamma_A / (k ln gamma) = 1
    # gives  beta^4 = 2 C gamma_A / (k ln gamma), where orbits = C / beta^5 and
    #     C = [5/(16 pi sqrt 2)] / 8^{5/2} = 3.8856e-4   (the 8 is a/r_s = 1/8beta^2).
    C   = 5.0 / (16.0 * math.pi * math.sqrt(2.0)) / 8.0**2.5
    gA  = 1.0 / math.sqrt(1.0 - bmax**2)
    chk("beta ceiling, closed form vs bisection",
        (2.0 * C * gA / (k50 * math.log(2.0)))**0.25, bmax, tol=1e-3)

    print("\nThe mass ratio -- and what actually buys the IMBH")
    chk("Routh threshold (9-sqrt69)/18", ROUTH, 0.0385208965, tol=1e-9)
    chk("largest L4/L5-stable q = m2/m1", routh_q_max(), 0.040064206, tol=1e-6)
    # unequal_binary must reduce to slingshot's equal-mass law at q = 1.
    a1, T1, N1 = unequal_binary(M50, 1.0, 0.03)
    chk("q=1 separation matches separation()", a1, separation(M50, 0.03), tol=1e-12)
    chk("q=1 period matches slingshot", T1, S.orbital_period(0.03, 2 * M50), tol=1e-12)
    chk("q=1 orbits-to-merger matches slingshot", N1, S.orbits_to_merger(0.03), tol=1e-12)
    # The finding: k is blind to q, so the ratio cannot be what the tide asks for.
    chk("heavy component a 50 Msun deflector needs for L4/L5 (Msun)",
        routh_heavy_floor(M50) / MSUN, 1247.9968, tol=1e-4)
    # Both branches clear the merger budget; they differ in inventory and clock.
    Nq  = passes_to(2.0, 0.03, k50)
    _, Tq, Oq = unequal_binary(M50, routh_q_max(), 0.03)
    chk("equal-mass margin", S.orbits_to_merger(0.03) / Nq, 14.66679, tol=1e-4)
    chk("Routh-stable margin", Oq / Nq, 2603.083, tol=1e-3)
    chk("Routh-stable mission time (days)", Nq * Tq / 86400.0, 16.69073, tol=1e-3)

    print("\nThe recorded fault -- beta^3 refuted, not deleted")
    M, k, claimed, true, over = retracted_beta3_gain(0.03)
    chk("its deflector mass (Msun) -- very nearly right", M / MSUN, 51.4573, tol=1e-4)
    chk("its actual pass distance (r_s)", k, 92.5926, tol=1e-4)
    chk("the gain it claimed", claimed, 0.075, tol=1e-9)
    chk("the gain available there", true, 6.48279e-4, tol=1e-4)
    chk("overstatement factor", over, 115.690, tol=1e-4)
    # And the reason the mass looked right: k = 92.6 is within 2% of the correct
    # 94.4 by coincidence at this beta.  The coincidence does not survive.
    chk("its k at beta = 0.10 is NOT near the correct k",
        retracted_beta3_gain(0.10)[1], 8.33333, tol=1e-5)

    print("\n%s" % ("SELFTEST PASS" if ok else "SELFTEST FAIL"))
    return 0 if ok else 1


def report():
    chi_p = fragility(2.0, 9.8)
    M50   = 50.0 * MSUN
    k50   = pass_distance(M50, chi_p)

    print("""
person.py -- from a proton to a person
================================================================================
Zhang's law is a law about test particles.  What extent costs, and what pays it.

-- The group -------------------------------------------------------------------
  chi   = sqrt(extent / survivable tide)        the payload, entire
  tau_s = r_s / c = 2GM/c^3                     the deflector, entire
  k     = r_p / r_s = (chi / tau_s)^(2/3)       how far out you must pass

  Extent and tolerance never enter separately, and neither does the hole's mass:
  only chi / tau_s.  Two missions with the same ratio are the same mission.

-- What each payload needs, to pass at k = 3 r_s (Zhang's deep pass) -----------""")
    print("  %-28s %10s %14s %16s" % ("payload", "chi (s)", "deflector", "status"))
    for lbl, d, amax, st in PAYLOADS:
        x = fragility(d, amax)
        M = deflector_mass(x, 3.0)
        mm = "%.3e kg" % M if M < 1e29 else "%.4g Msun" % (M / MSUN)
        print("  %-28s %10.3e %14s   %s" % (lbl, x, mm, st))
    print("""
  A proton needs a mountain.  A person needs 8823 Msun -- an intermediate-mass
  black hole, and no confirmed binary of them exists.  That is the wall the
  deep pass runs into, and k is the way through it.

-- The exchange rate: mass for passes ------------------------------------------
  M ~ k^-3/2 and N ~ k, so M ~ N^-3/2.  Give up gain, keep the payload, and the
  deflector you need drops faster than the pass count rises.
""")
    print("  %8s %14s %14s %12s" % ("k (r_s)", "deflector", "gain/pass", "passes"))
    for k in (3.0, 10.0, 30.0, 94.383, 300.0):
        M = deflector_mass(chi_p, k)
        print("  %8.1f %11.4g Msun %14.4e %12.0f"
              % (k, M / MSUN, gain_per_pass(0.03, k), passes_to(2.0, 0.03, k)))
    print("""
  At k = 94.4 the deflector is 50 Msun -- GW150914 was 36 + 29 Msun.  The
  found object nobody has found becomes an object the catalogue already holds.

-- Where the binary's patience runs out ----------------------------------------
  Orbits to merger go as beta^-5 and passes go as 1/beta, so the margin goes as
  beta^-4.  A FAST binary is the wrong flywheel: it merges mid-mission.
""")
    print("  %6s %12s %12s %12s %12s %10s"
          % ("beta", "separation", "gain/pass", "passes", "mission", "margin"))
    for beta in (0.2, 0.1, 0.05, 0.03, 0.02, 0.01):
        N = passes_to(2.0, beta, k50)
        t = mission_time(2.0, beta, k50, M50)
        print("  %6.3f %9.4g km %12.4e %12.0f %9.4g s %10.4g"
              % (beta, separation(M50, beta) / 1e3, gain_per_pass(beta, k50),
                 N, t, margin(2.0, beta, k50)))
    bmax = beta_ceiling(2.0, k50)
    print("""
  Ceiling: beta <= %.4f.  Above it the flywheel is gone before the payload is
  fast.  Zhang's headline beta = 0.2 misses by a factor of 132 -- it is not the
  mass that forbids it, it is the clock.

-- WORKED CASE: a person to 0.87 c ---------------------------------------------
  The 1090 passes are available -- a binary can hold a payload for arbitrarily
  many encounters (Shipley & Dolan 2016; Zhang Sec. 3.3), so no delta-v is owed
  for the returns.  What they assume is STEERING: hold Zhang's optimised branch
  every pass, or take Fermi's second-order average and 33x the count.  See
  stationkeep.py.""" % bmax)
    beta = 0.03
    N = passes_to(2.0, beta, k50)
    T = S.orbital_period(beta, 2 * M50)
    a = separation(M50, beta)
    print("""  binary            2 x 50 Msun, circular, beta = %.2f
  separation        %.4g km          (%.1f r_s of the pair)
  pass distance     %.4g km          (k = %.1f r_s of one hole)
  tide on a 2 m body  %.3f m/s^2 = %.3f g
  deflection/pass   %.4f deg
  gain per pass     %.4e
  passes to gamma=2 %.0f            (0.87 c, steered)
  binary period     %.3f s
  mission time      %.4g s = %.2f h
  orbits to merger  %.4g            margin %.1fx
  propellant        0
""" % (beta, a / 1e3, a / (2 * G * 2 * M50 / c**2), k50 * 2 * G * M50 / c**2 / 1e3,
       k50, S.tidal_accel(M50, k50, 2.0), S.tidal_accel(M50, k50, 2.0) / 9.8,
       math.degrees(deflection(k50)), gain_per_pass(beta, k50), N, T,
       N * T, N * T / 3600.0, S.orbits_to_merger(beta), margin(2.0, beta, k50)))

    print("""-- The mass ratio: what actually buys the IMBH ---------------------------------
  k depends on the deflector alone, so nothing above cares about the ratio.  The
  ratio is decided by NAVIGATION: L4/L5 is linearly stable only for
  mu = m2/M_t < (9-sqrt69)/18 = %.7f, i.e. q = m2/m1 < %.6f.  A 50 Msun
  deflector therefore needs a companion of at least %.0f Msun to have a free
  parking point -- and that is an IMBH.
""" % (ROUTH, routh_q_max(), routh_heavy_floor(M50) / MSUN))
    print("  %8s %12s %12s %12s %10s %12s"
          % ("q", "companion", "separation", "period", "margin", "mission"))
    for q in (1.0, 0.5, 0.2, 0.1, routh_q_max()):
        aq, Tq, Oq = unequal_binary(M50, q, beta)
        print("  %8.4f %7.4g Msun %9.4g km %10.4g s %10.4g %9.4g d"
              % (q, M50 / q / MSUN, aq / 1e3, Tq, Oq / N, N * Tq / 86400.0))
    print("""
  So the fork is not tidal, it is a parking problem:

    q = 1     two 50 Msun holes -- IN THE LIGO CATALOGUE (GW150914: 36 + 29).
              No stable co-orbital point.  Station-keeping must be active, and
              its delta-v is the open item below.
    q < 0.04  a 1248 Msun companion -- NOT in any catalogue.  Free parking,
              2603x merger margin, 16.7 day mission.

  The k-lever took the IMBH out of the TIDE.  Routh puts it straight back into
  the NAVIGATION, and only there.  That relocates the project's one unevidenced
  object from a physics requirement to a station-keeping budget -- which is a
  number nobody here has computed, and is now the whole question.

-- What is still open ----------------------------------------------------------
  One pass per binary orbit is ASSUMED, inherited from slingshot.py; a payload
  that can be re-aimed in less than an orbit shortens the mission and nothing
  here forbids it.  The station-keeping delta-v across %.0f passes is ZERO -- the
  binary returns the payload for free -- but the per-pass vanquish probability
  that must be held near zero across them is NOT computed anywhere in this tree
  or in the literature read so far.  Recorded as open; a finding is not a repair.
""" % N)
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
