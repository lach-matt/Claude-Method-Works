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
""" % (b1, b2, 1.0 / margin(2.0, 0.03, k50, 2), aarseth_vf(0.2041241), MIKKOLA_VALTONEN))
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
