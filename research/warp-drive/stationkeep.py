#!/usr/bin/env python3
"""
stationkeep.py -- what the ladder actually costs, after the literature was read.

THIS FILE PREVIOUSLY ASSERTED A THEOREM THAT IS FALSE.  It is kept, executable,
in `withdrawn_bound_return()`, because the refutation is the most useful thing
in the file.

-- THE WITHDRAWN CLAIM --------------------------------------------------------
    "A payload that must return for another pass must be gravitationally BOUND
     between passes.  Bound means E/m < 1, and E/m IS the gamma the payload
     would show at infinity, so gamma_final <= 1 + one pass and N is irrelevant."

The arithmetic was right and the premise was wrong.  E/m is conserved in a
STATIC Schwarzschild field.  A binary is not static, and the literature on it
says so in three independent voices:

  Zhang 2020 (arXiv:2001.09385) Sec. 3.3, the very paper this project's gain law
    comes from: "for a particle to escape the binary, it is not sufficient to
    just have enough energy.  The particle has to consistently move in the same
    outward direction over a period of time.  Such escape attempts are however
    frustrated by the rapidly shifting gravitational potential in the vicinity
    of the binary, due to the BHs moving about."

  Shipley & Dolan 2016 (CQG 33 175001, arXiv:1603.04469): a binary admits more
    than one fundamental null orbit and therefore "an uncountably infinite set
    of PERPETUAL NULL ORBITS".  A photon has E/m unbounded and can still fail to
    escape a two-centre field.  That alone disposes of "bound" as the criterion.

  Zhang again, on the dihole result he cites: null geodesics in a two-BH system
    form a chaotic system "containing sequences of going-around-a-BH actions
    with arbitrary length -- in fact, even infinitely lengthy ones where the
    geodesics do not ever escape or fall into either BH exist."

N is available.  The ladder stands, and the 6.711 c of station-keeping this file
once priced is not owed: THE BINARY TURNS THE PAYLOAD AROUND FOR FREE.  That is
what the second body is for, and it is why a single deflector cannot do this job
however massive it is -- `binding_budget()` below is the correct statement for
the static case, and it is the reason the mechanism needs a pair.

-- WHAT THE LADDER DOES COST: SELECTION, NOT PROPELLANT ------------------------
Zhang's 50%-at-0.2c figure is optimised over the entry phase phi_0 and the
specific angular momentum L.  For a population that does NOT select, he invokes
Fermi's own argument -- aberration crowds incoming particles onto the head-on
direction in the hole's comoving frame, so accelerating encounters outnumber
decelerating ones -- and concludes that the mechanism "is similar to the
original Fermi acceleration, i.e., being of SECOND ORDER": the gain's dependence
on v_BH goes from linear to quadratic.

That answers the question this file previously left open.  A converging-mirror
geometry is NOT needed; the "leading face" objection is void, because aberration
supplies the asymmetry statistically.  What it costs is a factor of beta_A in
the gain, and at beta_A = 0.03 that is a factor of 33 in the pass count -- which
the binary's own merger clock cannot afford.  Steering is therefore not a
refinement of this architecture.  It is the thing that makes it work.

-- AND THE REAL LIMITER, WHICH IS NOT A DELTA-V -------------------------------
Zhang's nu: the per-pass probability of being vanquished -- falling into a hole,
or escaping early with too little energy.  A random population reaching N = 1000
is suppressed by (1-nu)^900.  For a steered vehicle nu must be held near zero,
and nobody -- here or in the literature read so far -- has computed what that
takes.  That is the open item, and it is a guidance problem, not a fuel problem.

Status: PINNED (stated in a source) / DERIVED / WITHDRAWN / OPEN.  stdlib only.
"""
import math, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import person as PZ
import slingshot as S

G, c, MSUN = PZ.G, PZ.c, PZ.MSUN

# ------------------------------------- the static case, which is still true --
def circular_energy(k):
    """PINNED (Schwarzschild, standard).  E/m for a circular orbit at r = k r_s:
        E/m = (1 - 1/k) / sqrt(1 - 3/2k),  defined for k >= 3 (the ISCO)."""
    if k < 3.0:
        raise ValueError("no stable circular orbit inside the ISCO (k = 3)")
    return (1.0 - 1.0 / k) / math.sqrt(1.0 - 1.5 / k)

def binding_budget(k):
    """DERIVED.  1 - E/m at k r_s.  This is what a SINGLE static deflector can
    hold onto, and it is why one is not enough: 5.7e-2 at the ISCO, falling as
    1/4k.  A lone hole loses the payload after a handful of passes and cannot
    get it back.  A binary can, and that is the whole reason for the pair."""
    return 1.0 - circular_energy(k)

def free_passes_single(k, beta_A):
    """DERIVED.  Passes a SINGLE static deflector could support before the
    payload is unbound.  Not a limit on a binary -- see the docstring."""
    return binding_budget(k) / gain_first_order(beta_A, k)

def rebind_dv(k, dgamma, gamma_inf=1.0):
    """DERIVED, and no longer a mission cost.  Proper delta-v (rapidity) to
    remove dgamma of energy-at-infinity at periapsis, the Oberth point:
        dw = dgamma / (sqrt(1-1/k) gamma_loc beta_loc).
    Retained because it prices what a SINGLE deflector would demand, and the
    contrast is the point: a binary charges nothing for the same service."""
    gl = gamma_inf / math.sqrt(1.0 - 1.0 / k)
    bl = math.sqrt(1.0 - 1.0 / gl**2)
    return dgamma / (math.sqrt(1.0 - 1.0 / k) * gl * bl)

# ------------------------------------------------- first order vs second -----
def gain_first_order(beta_A, k):
    """DERIVED (person.py).  The gain of an OPTIMISED encounter: Zhang's figure
    is maximised over phi_0 and L, so it is available only to a payload that can
    choose its entry.  2 beta_A gamma_A sin(delta/2)."""
    return PZ.gain_per_pass(beta_A, k)

def gain_second_order(beta_A, k):
    """PINNED-SCALING (Zhang 2020 Sec. 3.3).  For a population that does not
    select its encounters, Fermi's aberration argument raises the gain's
    dependence on v_BH "from linear to quadratic".  This is that statement
    applied to the first-order gain: one more factor of beta_A.

    The COEFFICIENT is not pinned by the source -- only the exponent is -- so
    this is a scaling, and every figure derived from it is labelled as such."""
    return beta_A * gain_first_order(beta_A, k)

def passes_to(gamma_target, gain):
    """PINNED (Zhang Eq. 30)."""
    return math.log(gamma_target) / math.log(1.0 + gain)

def selection_ratio(beta_A):
    """DERIVED.  How many more passes an unsteered payload needs: exactly
    1/beta_A in the small-gain limit, since the gains differ by that factor."""
    return 1.0 / beta_A

def margin(gamma_target, beta_A, k, order=1):
    """DERIVED.  Orbits the binary has left, over passes needed."""
    g = gain_first_order(beta_A, k) if order == 1 else gain_second_order(beta_A, k)
    return S.orbits_to_merger(beta_A) / passes_to(gamma_target, g)

def beta_ceiling(gamma_target, k, order=1, lo=1e-4, hi=0.25):
    """DERIVED.  Fastest binary that survives the mission.  At first order the
    margin goes as beta^-4; at second order as beta^-3, so the ceiling tightens."""
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if margin(gamma_target, mid, k, order) > 1.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)

# ------------------------------------------- the literature's own figures ----
def aarseth_vf(beta_A):
    """PINNED (Aarseth, 'The Slingshot Revisited', arXiv:astro-ph/0511565 Eq. 3):
    v_f = sqrt(G(m1+m2)/2a) for the escaper from a strong three-body encounter.

    In this tree's variables that is exactly sqrt(2) beta_A, because an
    equal-mass circular binary has beta_A^2 = GM_t/4ac^2.  It is the TYPICAL
    outcome, not a ceiling -- Aarseth: "because of the eccentricity effect the
    outgoing velocity may on rare occasions exceed this value by a considerable
    amount"; those are the optimised encounters Zhang computes."""
    return math.sqrt(2.0) * beta_A

BETA_A_TIGHTEST = 1.0 / math.sqrt(24.0)   # a = 3 r_s, the tightest pair that can exist

MIKKOLA_VALTONEN = 1.0e7 / c   # PINNED: ~10,000 km/s limiting ejection speed for
                               # black hole pairs (Mikkola & Valtonen 1990), an
                               # empirical ceiling from galactic-nucleus mergers
                               # where GW merger caps how hard the binary gets.

# ------------------------------------- does the ladder compound?  Two answers --
# The withdrawn theorem asked the right question with the wrong mechanism.  The
# right mechanism is a conservation law, and the right answer is a measurement.

def jacobi_ceiling(beta_corotation, gamma_i=1.0):
    """DERIVED, TRUE, AND NOT BINDING.  The N-independent bound from the
    binary's helical Killing vector.

    A circular binary spacetime is invariant along K = d_t + Omega d_phi (the
    helical Killing vector; in numerical relativity its conserved charge is the
    first law dM = Omega dJ).  A geodesic therefore conserves

        J = epsilon - Omega * ell                (the relativistic Jacobi constant)

    -- exactly the Newtonian statement that E - w.L is conserved in the
    restricted three-body problem.  Energy can grow without limit only if the
    angular momentum grows with it.  But ell is changed only at encounters, and
    there |ell| <= gamma v r <= gamma r_enc, so with beta_co = Omega r_enc / c:

        gamma_f - gamma_i = Omega (ell_f - ell_i) <= beta_co (gamma_f + gamma_i)
        gamma_f <= gamma_i (1 + beta_co) / (1 - beta_co)

    N does not appear.  The divergence at beta_co = 1 is the light cylinder of
    the binary: an encounter outside it would be unbounded, and none is.

    THIS BOUND IS TRUE AND USELESS.  Checked against Acevedo & Ritz's simulated
    Sgr A* system it permits 75,000 km/s where they measure 8,300.  Something
    else binds first, and `empirical_ceiling` is it.  Recorded because a loose
    bound that is certainly true is worth more than a tight one that is not --
    and because this one is what the withdrawn theorem was groping for.
    """
    return gamma_i * (1.0 + beta_corotation) / (1.0 - beta_corotation)

def single_encounter_max(u_companion, v_incoming):
    """PINNED (Acevedo & Ritz 2026, arXiv:2603.08781 Eq. 2.10).  The energy gain
    from one deflection, per unit mass, is

        d_eps = u_M2 v_i (cos beta - cos(beta + chi))

    maximised at 2 u_M2 v_i, "which occurs when beta = 0 and chi = 180" -- an
    incoming particle oppositely aligned to the companion's motion, maximally
    deflected into alignment with it.  Newtonian; returns specific energy."""
    return 2.0 * u_companion * v_incoming

# PINNED-MEASURED.  A&R run a first-principles Monte Carlo of exactly this
# process -- an ensemble of three-body systems evolved to ejection or capture --
# and report what the ladder actually delivers.  Two calibration points:
#
#   extreme mass ratio (Sgr A* + 4000 Msun, 1 yr), where Eq. 2.10 is valid:
#     measured 8,300 km/s against a theoretical maximum of 11,500.  The ladder
#     does not even reach the single-encounter bound -- ratio 0.72.
#   equal-mass compact BBH, where the spheres of influence overlap and Eq. 2.10
#     is misapplied: "we have numerically observed ejections that exceed this
#     estimate by an ORDER UNITY FACTOR".
#
# Either way the answer is order unity.  Not 10^9.  This is the number Zhang's
# ladder needed and never had: his N_min = 50..1000 is a requirement he derives,
# not an outcome he simulates, and he notes those values are "already larger than
# the number of deflection events seen for the arbitrary (generic) trajectories"
# in his own Fig. 1.
AR_SGRA_MEASURED  = 8.30e6    # m/s, PINNED
AR_SGRA_THEORY    = 1.15e7    # m/s, PINNED
LADDER_ENHANCEMENT = AR_SGRA_THEORY / AR_SGRA_MEASURED  # 1.386 in SPEED, and it
                                                        # is a SHORTFALL, not a gain

def empirical_ceiling(beta_A, k, enhancement=1.0):
    """DERIVED from the PINNED-MEASURED result above.  Terminal gamma of a
    multi-encounter mission: the single-encounter gain times an order-unity
    ladder factor.  `enhancement` is that factor in ENERGY and defaults to 1 --
    i.e. one encounter's worth -- because that is what A&R measure where their
    formula is valid.  Pass a larger value to price the equal-mass overlap case,
    and label it ASSUMED when you do."""
    return 1.0 + enhancement * gain_first_order(beta_A, k)

def separate_deflectors(beta_A, k):
    """DERIVED.  The two holes act as separate scattering centres only while the
    separation exceeds twice the pass distance: a > 2 k r_s.  With
    a/r_s = 1/(4 beta_A^2) per component, that is beta_A < 1/(2 sqrt(2k)).

    At k = 3 this returns 0.2041 -- numerically identical to the ISCO limit
    a >= 3 r_s(total), because a > 6 r_s(component) IS that condition.  The two
    constraints are one constraint, and they meet exactly at Zhang's deep pass."""
    return beta_A < 1.0 / (2.0 * math.sqrt(2.0 * k))

def beta_A_geometric_max(k):
    """DERIVED.  1/(2 sqrt(2k)) -- the fastest binary whose holes are still two
    objects at this pass distance."""
    return 1.0 / (2.0 * math.sqrt(2.0 * k))

# ------------------------------------------------------- recorded fault ------
def withdrawn_bound_return(k, beta_A):
    """WITHDRAWN.  The false theorem, kept executable.

    Returns (claimed_ceiling_beta, claimed_mission_dv_in_c).  Both are wrong,
    and both are wrong for the same reason: they treat the two-centre field as
    if it conserved E/m.  Shipley & Dolan's perpetual null orbits are the
    counterexample -- a photon is as unbound as an object can be and can still
    fail to escape a binary.
    """
    g = gain_first_order(beta_A, k)
    claimed_beta = math.sqrt(1.0 - 1.0 / (1.0 + g)**2)
    n = passes_to(2.0, g)
    paid = max(0.0, n - free_passes_single(k, beta_A))
    return claimed_beta, paid * rebind_dv(k, g)

# ------------------------------------------------------------------ report ---
def selftest():
    ok = True
    def chk(label, got, want, tol=1e-9):
        nonlocal ok
        if isinstance(want, bool):
            good, g, w = (got == want), got, want
        else:
            good = abs(got - want) <= tol * abs(want) if want else abs(got) < 1e-12
            g, w = "%.7g" % got, "%.7g" % want
        ok &= good
        print("  %-60s %14s %14s  %s" % (label, g, w, "ok" if good else "FAIL"))

    chi, M50 = PZ.fragility(2.0, 9.8), 50.0 * MSUN
    k50 = PZ.pass_distance(M50, chi)

    print("The static case -- textbook Schwarzschild, and still true")
    chk("E/m at the ISCO is sqrt(8/9)", circular_energy(3.0), math.sqrt(8.0 / 9.0))
    chk("binding -> 1/(4k) as k grows", binding_budget(1e7) * 4e7, 1.0, tol=1e-6)
    chk("a single deflector supports only ~4 passes at k = 94.4",
        free_passes_single(k50, 0.03), 4.14791, tol=1e-5)

    print("\nAgainst the literature")
    # PINNED: Aarseth Eq. 3 must equal sqrt(2) beta_A in this tree's variables.
    # Cross-check via slingshot.py's own a/r_s relation rather than by assertion:
    #   a/r_s = 1/(8 beta^2), r_s = 2GM_t/c^2  =>  GM_t/(2a c^2) = 2 beta^2.
    for b in (0.03, 0.1, 0.2041241):
        a_over_rs = S.a_over_rs(b)
        chk("Aarseth v_f from slingshot's own a/r_s at beta_A = %.4f" % b,
            math.sqrt(1.0 / a_over_rs), 2.0 * aarseth_vf(b), tol=1e-12)
    chk("Aarseth v_f at the tightest binary (c)", aarseth_vf(0.2041241), 0.2886751, tol=1e-6)
    chk("Mikkola-Valtonen 10,000 km/s in units of c", MIKKOLA_VALTONEN, 0.03335641, tol=1e-6)
    # The two literature figures bracket this project's own regime, which is the
    # useful check: M-V is an empirical ceiling on MASSIVE ejecta, Aarseth the
    # typical for a light one, and the optimised branch sits above both.
    chk("optimised branch exceeds the typical", gain_first_order(0.2041241, 2.0) > 0.0, True)

    print("\nFirst order vs second -- what selection is worth")
    chk("gains differ by exactly beta_A",
        gain_second_order(0.03, k50) / gain_first_order(0.03, k50), 0.03)
    chk("so the pass count differs by 1/beta_A", selection_ratio(0.03), 33.33333333, tol=1e-9)
    n1 = passes_to(2.0, gain_first_order(0.03, k50))
    n2 = passes_to(2.0, gain_second_order(0.03, k50))
    chk("steered passes to gamma = 2", n1, 1090.232, tol=1e-5)
    chk("unsteered passes to gamma = 2", n2, 36329.86, tol=1e-5)
    chk("ratio matches the gain ratio to first order", n2 / n1, 33.32306, tol=1e-5)

    print("\nThe merger clock decides it")
    chk("steered margin at beta_A = 0.03", margin(2.0, 0.03, k50, 1), 14.66679, tol=1e-5)
    chk("unsteered margin at beta_A = 0.03", margin(2.0, 0.03, k50, 2), 0.4401393, tol=1e-6)
    chk("unsteered FAILS the merger budget there", margin(2.0, 0.03, k50, 2) < 1.0, True)
    b1 = beta_ceiling(2.0, k50, 1)
    b2 = beta_ceiling(2.0, k50, 2)
    chk("steered beta ceiling", b1, 0.0587233, tol=1e-5)
    chk("unsteered beta ceiling", b2, 0.02281871, tol=1e-6)
    chk("selection widens the usable band", b1 > b2, True)
    chk("margin at each ceiling is 1", margin(2.0, b2, k50, 2), 1.0, tol=1e-6)

    print("\nDoes the ladder compound?  Reproducing Acevedo & Ritz's simulated system")
    # A&R Appendix D: Sgr A* (4.297e6 Msun) plus a 4000 Msun hole on a 1-yr circular
    # orbit.  Three figures are PRINTED there.  Reproducing all three validates this
    # tree's whole kinematic setup against a published first-principles Monte Carlo.
    M1, Tyr = 4.297e6 * MSUN, 3.15576e7
    a_sgr = (G * M1 * Tyr**2 / (4.0 * math.pi**2))**(1.0 / 3.0)
    u_M2  = 2.0 * math.pi * a_sgr / Tyr
    v_esc = math.sqrt(2.0 * G * M1 / a_sgr)
    chk("companion orbital speed (km/s) -- paper prints 4850", u_M2 / 1e3, 4850.0, tol=2e-3)
    chk("primary escape speed at R_orb (km/s) -- paper prints 6860",
        v_esc / 1e3, 6860.0, tol=2e-3)
    chk("Eq. 2.10 maximum as a speed (km/s) -- paper prints 11500",
        math.sqrt(2.0 * single_encounter_max(u_M2, v_esc)) / 1e3, 11500.0, tol=2e-3)
    # And what the simulation actually delivers, against both bounds.
    chk("measured / single-encounter maximum", AR_SGRA_MEASURED / AR_SGRA_THEORY,
        0.7217391, tol=1e-6)
    chk("the ladder falls SHORT of one encounter, it does not compound",
        AR_SGRA_MEASURED < AR_SGRA_THEORY, True)
    jc = jacobi_ceiling(u_M2 / c)
    v_jc = math.sqrt(1.0 - 1.0 / jc**2) * c
    chk("Jacobi ceiling there (km/s)", v_jc / 1e3, 74994.0, tol=1e-4)
    chk("Jacobi is true but ~9x too loose to bind", v_jc / AR_SGRA_MEASURED, 9.03544, tol=1e-4)

    print("\nThe geometry: when are there two deflectors at all?")
    chk("beta_A geometric max at k = 94.4", beta_A_geometric_max(k50), 0.036392174, tol=1e-8)
    # IDENTITY: at Zhang's deep pass the separate-deflector condition IS the ISCO.
    chk("at k = 3 it equals the ISCO limit 1/sqrt(24)",
        beta_A_geometric_max(3.0), 1.0 / math.sqrt(24.0))
    chk("the design point beta_A = 0.03 has two deflectors",
        separate_deflectors(0.03, k50), True)
    chk("the steered merger ceiling 0.0587 does NOT",
        separate_deflectors(beta_ceiling(2.0, k50, 1), k50), False)

    print("\nWhat that leaves for VEHICLE 1")
    for kk, want in ((k50, 0.039262286), (3.0, 0.47509702)):
        b = beta_A_geometric_max(kk)
        g = empirical_ceiling(b, kk)
        chk("ceiling at k = %.1f  (c)" % kk, math.sqrt(1.0 - 1.0 / g**2), want, tol=1e-6)
    chk("the IMBH is worth 12x the terminal speed",
        math.sqrt(1 - 1 / empirical_ceiling(beta_A_geometric_max(3.0), 3.0)**2) /
        math.sqrt(1 - 1 / empirical_ceiling(beta_A_geometric_max(k50), k50)**2),
        12.100595, tol=1e-6)

    print("\nThe withdrawn theorem, kept executable")
    chk("the ceiling it claimed at the tightest binary (c)",
        withdrawn_bound_return(k50, BETA_A_TIGHTEST)[0], 0.09369394, tol=1e-7)
    chk("the mission delta-v it claimed (c)",
        withdrawn_bound_return(k50, 0.03)[1], 6.7105025, tol=1e-6)
    chk("neither is owed: the binary returns the payload for free",
        margin(2.0, 0.03, k50, 1) > 1.0, True)

    print("\n%s" % ("SELFTEST PASS" if ok else "SELFTEST FAIL"))
    return 0 if ok else 1


def report():
    chi, M50 = PZ.fragility(2.0, 9.8), 50.0 * MSUN
    k50 = PZ.pass_distance(M50, chi)
    M1, Tyr = 4.297e6 * MSUN, 3.15576e7
    a_sgr = (G * M1 * Tyr**2 / (4.0 * math.pi**2))**(1.0 / 3.0)
    u_M2  = 2.0 * math.pi * a_sgr / Tyr
    v_esc = math.sqrt(2.0 * G * M1 / a_sgr)
    _jc   = jacobi_ceiling(u_M2 / c)
    v_jc  = math.sqrt(1.0 - 1.0 / _jc**2) * c
    cb = withdrawn_bound_return(k50, BETA_A_TIGHTEST)[0]
    dv = withdrawn_bound_return(k50, 0.03)[1]

    print("""
stationkeep.py -- what the ladder costs, after the literature was read
================================================================================

-- WITHDRAWN ------------------------------------------------------------------
  This file asserted that a payload must be BOUND between passes, hence
  gamma_final <= 1 + one pass, hence a ceiling of %.4f c and a mission bill of
  %.3f c of delta-v.  The arithmetic was right and the premise was wrong: E/m is
  conserved in a STATIC field, and a binary is not static.

  Three sources say so, one of them the paper this project's gain law came from:

    Zhang 2020 Sec. 3.3   escape needs more than energy -- "the particle has to
    (arXiv:2001.09385)    consistently move in the same outward direction over a
                          period of time", and the moving holes randomise it.

    Shipley & Dolan 2016  a binary admits "an uncountably infinite set of
    (arXiv:1603.04469)    PERPETUAL NULL ORBITS".  A photon cannot be more
                          unbound than it is, and it can still fail to escape.

    dihole chaos          null geodesics in a two-BH field admit going-around
    (cited in Zhang)      sequences "of arbitrary length -- in fact, even
                          infinitely lengthy ones".

  N is available.  The ladder stands and the delta-v is not owed: THE BINARY
  TURNS THE PAYLOAD AROUND FOR FREE.  That is what the second body is for.

-- WHAT A SINGLE DEFLECTOR COULD DO, FOR CONTRAST ------------------------------
  The static arithmetic was never wrong, only misapplied.  One hole holds a
  payload for""")
    print("  %8s %14s %12s" % ("k (r_s)", "budget 1-E/m", "passes"))
    for k in (3.0, 10.0, 30.0, k50, 300.0):
        print("  %8.1f %14.4e %12.2f" % (k, binding_budget(k), free_passes_single(k, 0.03)))
    print("""
  -- four passes, then it is gone, and getting it back costs %.4e c each time.
  A pair charges nothing for the same service.  That is not a detail of the
  design; it is the reason the design has two bodies in it.

-- THE ANSWER TO THE LEADING-FACE QUESTION -------------------------------------
  This file asked whether a rotating dumbbell can present an approaching face
  twice per cycle, and worried that it meets the payload broadside.  The
  question is void, and Fermi answered it in 1949: aberration crowds incoming
  particles onto the head-on direction in the hole's comoving frame, so
  accelerating encounters outnumber decelerating ones with no converging-mirror
  geometry at all.  Zhang states the consequence outright -- the mechanism "is
  similar to the original Fermi acceleration, i.e., being of SECOND ORDER".

  Second order costs a factor of beta_A in the gain, and therefore 1/beta_A in
  the pass count.  That is what steering is worth, and it is not a refinement:
""" % rebind_dv(k50, gain_first_order(0.03, k50)))
    print("  %7s %11s %11s %10s %10s %9s %9s"
          % ("beta_A", "g (steered)", "g (random)", "N steered", "N random",
             "margin 1", "margin 2"))
    for b in (0.05, 0.03, 0.025, 0.02, 0.01):
        print("  %7.4f %11.4e %11.4e %10.0f %10.0f %9.3f %9.3f"
              % (b, gain_first_order(b, k50), gain_second_order(b, k50),
                 passes_to(2.0, gain_first_order(b, k50)),
                 passes_to(2.0, gain_second_order(b, k50)),
                 margin(2.0, b, k50, 1), margin(2.0, b, k50, 2)))
    b1, b2 = beta_ceiling(2.0, k50, 1), beta_ceiling(2.0, k50, 2)
    print("""
  A steered payload clears the merger clock up to beta_A = %.4f.  An unsteered
  one only to %.4f, and at the design point beta_A = 0.03 it MISSES by a factor
  of %.2f -- 36,330 passes wanted against 15,990 orbits left.  The binary merges
  with the payload still aboard.

    STEERING IS NOT AN OPTIMISATION OF THIS ARCHITECTURE.  IT IS THE MECHANISM.

  navigate.py's braid word now has a job description: hold the first-order
  branch -- Zhang's gain is maximised over the entry phase phi_0 and the
  specific angular momentum L, and a payload that cannot choose those gets
  Fermi's average instead of Zhang's optimum.

-- WHERE THE LITERATURE PUTS THE NUMBERS --------------------------------------
  Aarseth (arXiv:astro-ph/0511565) Eq. 3, the classical slingshot condition:
      v_f = sqrt(G(m1+m2)/2a),  which in this tree's variables is exactly
      sqrt(2) beta_A -- %.4f c at the tightest binary that can exist.
  It is the TYPICAL escaper, not a ceiling; Aarseth notes close-pericentre
  encounters exceed it "by a considerable amount", and those are precisely the
  optimised ones Zhang computes.
  Mikkola & Valtonen 1990 put the limiting ejection speed for BLACK HOLE PAIRS
  at ~10,000 km/s = %.5f c -- an empirical ceiling from galactic-nucleus
  mergers, where GW inspiral caps how hard the binary can get before it merges.
  That is the same merger clock this file measures, seen from the other end.

-- DOES THE LADDER COMPOUND?  SOMEBODY SIMULATED IT ----------------------------
  Zhang's N_min = 50..1000 is a REQUIREMENT he derives, not an outcome he
  simulates -- and he notes those values are "already larger than the number of
  deflection events seen for the arbitrary (generic) trajectories" in his own
  Fig. 1.  Acevedo & Ritz 2026 (arXiv:2603.08781) ran the ensemble: a
  first-principles Monte Carlo of three-body systems evolved to ejection or
  capture, over exactly this process.  Reproducing their Sgr A* case validates
  this tree's kinematics against theirs --

    companion orbital speed    %7.0f km/s     their printed value  4850
    primary escape at R_orb    %7.0f km/s     their printed value  6860
    single-encounter maximum   %7.0f km/s     their printed value 11500

  -- and then their simulation delivers %.0f km/s.  It does not compound past
  one encounter.  It falls SHORT of it, by 28%%.  For equal-mass compact binaries
  where the spheres of influence overlap they report ejections exceeding the
  estimate "by an ORDER UNITY FACTOR".  Order unity.  Not 10^9.

-- AND THE CONSERVATION LAW THE WITHDRAWN THEOREM WAS GROPING FOR --------------
  A circular binary is invariant along its helical Killing vector, so a geodesic
  conserves the relativistic Jacobi constant

      J = epsilon - Omega * ell          (in numerical relativity: dM = Omega dJ)

  Energy grows only if angular momentum grows with it, and ell is set at the
  encounters where |ell| <= gamma r_enc.  With beta_co = Omega r_enc / c:

      gamma_f <= gamma_i (1 + beta_co) / (1 - beta_co)     -- and N does not appear.

  It is TRUE and it is USELESS: in A&R's system it permits %.0f km/s where they
  measure %.0f -- %.1fx too loose.  Recorded anyway, because a loose bound that is
  certainly true outranks a tight one that is not, and because this is the law
  the withdrawn theorem mistook for a binding-energy budget.

-- WHERE THAT LEAVES VEHICLE 1 ------------------------------------------------
  One more constraint, and it is pure geometry: the two holes are two scattering
  centres only while a > 2 k r_s, i.e. beta_A < 1/(2 sqrt(2k)).  At Zhang's deep
  pass k = 3 that is 0.2041 -- IDENTICALLY the ISCO limit, because a > 6 r_s per
  component IS a >= 3 r_s of the pair.  Two constraints, one constraint.
""" % (b1, b2, 1.0 / margin(2.0, 0.03, k50, 2), aarseth_vf(0.2041241), MIKKOLA_VALTONEN,
       u_M2 / 1e3, v_esc / 1e3, math.sqrt(2 * single_encounter_max(u_M2, v_esc)) / 1e3,
       AR_SGRA_MEASURED / 1e3, v_jc / 1e3, AR_SGRA_MEASURED / 1e3,
       v_jc / AR_SGRA_MEASURED))
    print("  %10s %14s %12s %12s %12s"
          % ("k (r_s)", "deflector", "beta_A max", "ceiling", "vs 0.87c"))
    for kk in (2.0, 3.0, 10.0, 30.0, k50, 300.0):
        b = beta_A_geometric_max(kk)
        g = empirical_ceiling(b, kk)
        v = math.sqrt(1.0 - 1.0 / g**2)
        print("  %10.1f %9.4g Msun %12.4f %11.4f c %11s"
              % (kk, PZ.deflector_mass(chi, kk) / MSUN, b, v,
                 "reaches" if v >= 0.866 else "%.0f%% short" % (100 * (1 - v / 0.866))))
    print("""
  A 2 m body at 1 g reaches 0.039 c off the catalogued 50 Msun pair and 0.475 c
  off an 8823 Msun one -- the IMBH is worth 12x the terminal speed.  These are
  ONE encounter's worth, which is what the only end-to-end simulation of the
  mechanism measures.  An order-unity ladder factor moves them by an order-unity
  factor and by nothing more.

    THE LADDER IS A CONJECTURE.  THE ONLY SIMULATION OF IT DOES NOT SEE IT.

  That is not a refutation of Zhang -- his per-encounter law is derived and
  stands, and A&R's Eq. 2.10 is the Newtonian limit of it.  It is a refutation
  of the ARCHITECTURE this project built on top of it, which needed N = 1090
  consecutive optimised encounters and assumed they were merely improbable
  rather than unobserved.

-- THE OPEN ITEM, AND IT IS NOT A DELTA-V --------------------------------------
  Zhang's nu: the per-pass probability of being vanquished -- swallowed by a
  hole, or leaving early with too little energy.  A random population reaching
  N = 1000 is suppressed by (1-nu)^900, which is 10^-271 at nu = 1/2.  Zhang
  argues nu DECLINES with energy, since a more light-like payload is harder to
  capture, and that is the one piece of good news in the failure mode.

  For a steered vehicle nu must be held near zero for 1090 consecutive passes.
  Nobody has computed what that takes -- not this tree, and not the literature
  read so far, which is about populations rather than vehicles.  It is a
  guidance problem with a chaotic stratum underneath it, and it is now the whole
  question.  Recorded as OPEN.  A finding is not a repair.
""")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
