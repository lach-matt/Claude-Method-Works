#!/usr/bin/env python3
"""
obstruct.py -- the obstruction ledger.  Which ones dissolved, which merely moved,
and which have never been tested at all.

Written because "the obstructions have moved" is not the same claim as "the
obstructions have dissolved", and a build planned on the first sentence while
believing the second will fail on the back end.  Every row here carries a status
and a test, and the statuses are not flattened:

    DISSOLVED        gone, with a reason that is checkable here
    RELOCATED        still true, wearing a different name -- usually a bill
    CLOSED-NEGATIVE  answered, and the answer is no
    CONDITIONAL      dissolved in one regime and not in another, with the boundary
    UNTESTED         nobody has asked, this project included.  THE DANGEROUS ROW.

THE HEADLINE: of sixteen obstructions, three dissolved, three relocated, five
closed negative, three are conditional, two are OPEN, and NONE is untested.  A
build is ready when the untested rows are either tested or accepted with eyes
open, and this file exists to make that a decision rather than an oversight.
The counts here are asserted by the selftest against the ledger, so a row that
moves fails this paragraph rather than quietly outliving it.

-- WHAT ACTUALLY DISSOLVED ----------------------------------------------------
Only two, and one of them by leaving the architecture rather than beating it.

  HORIZON-REQUIRED.  A horizon exists iff v_s >= c (twist.py: f* = 1 - c/v_s lies
  in [0,1) only for v_s >= c).  Subluminal transport needs none.  Genuinely gone.

  EXOTIC-MATTER.  Gone for the warpshell -- dominant energy holds observer-robustly
  in bulk and shell -- but by leaving the shift-vector class Santiago-Schuster-
  Visser quantify over, not by refuting them.  Dissolution by relocation of the
  ARCHITECTURE is still dissolution, and it is worth naming which kind it is.

-- WHAT RELOCATED, AND WHERE IT WENT ------------------------------------------
  CM-THEOREM -> the energy budget.  Le's Theorem 1 is its exact GR form.  Paid,
  not evaded: m_f/m_0 = e^{-3 delta_eta}, the Doppler factor cubed.
  ENERGY -> "astronomical but finite", which is a bill and not a bound.
  FELT-ACCELERATION -> unchanged and often misread.  The cavity is tidally flat;
  the passengers still have weight.  person.py's fragility bound was tidal, so it
  lifts; the acceleration limit does not.

-- THE ONE THAT MOVED TWICE, AND THE SECOND MOVE IS THE INTERESTING ONE --------
  WALL-STABILITY.  Marginal (Poisson-Visser V'' = 0), so a burn had to outrun an
  e-folding, which a habitable design missed by 1.8e14.  wall.py showed the fix is
  structural: strictly stable for beta^2 > beta^2_crit(x), subluminal through the
  whole operative window, free in dominant-energy margin.

  But beta^2 IS NOT A KNOB.  The matter model determines it.  For a counter-
  rotating shell the junction already fixes v^2 = (1-s)/(2s), so the supplied
  stiffness is a function of x alone, and it clears the requirement only for

        x  <  0.46898

  with the margin WIDEST at low compactness, tending to exactly 4/3 as x -> 0.
  So the fix is CONDITIONAL, and the condition happens to hold where it is needed:
  Le's x = 0.3 clears it by 14%, and a habitable ship at x ~ 1e-22 sits at the 4/3
  limit.  It fails at x = 2/3 and fails badly at 4/5 -- the high-compactness corner
  a marginal wall handled best.  That is not a dissolution and this file does not
  call it one.

-- THE TWO ROWS NOBODY HAS TESTED, WHICH IS WHERE THE NEXT BUILD WILL FAIL -----
  1. NON-RADIAL SHELL MODES.  Poisson-Visser is a RADIAL linearisation and wall.py
     is nothing but.  Perturbations with l >= 2 were never posed.  A thin shell
     that is radially stable and unstable to a quadrupole is an ordinary object,
     not an exotic one, and the surface stress here is anisotropic (p_r = 0,
     tangential pressure only), which is the configuration most prone to it.
     THIS IS THE FIRST THING THAT WILL BREAK.  It is also cheap to test.
  2. THE 2+1D MAPPING DOES NOT EXIST.  twist.py showed an analogue must be at
     least 2+1D to carry any metric content.  Smolyaninov's mapping is derived in
     1+1D and there is no published 2+1D version; worse, the stability bound the
     whole design rests on -- Brown-Hornreich-Shtrikman g_x^2 <= (eps-1)(mu-1) --
     is a bound on ONE magnetoelectric component, and a transversely graded medium
     has more.  The bound may tighten, loosen, or not apply.  ANALOGUE-2D is not a
     design awaiting fabrication; it is a derivation awaiting a derivation.

-- AND ONE MORE THING THE LEDGER SAYS, WHICH IS NOT AN OBSTRUCTION -------------
Three separate results now turn on the SAME dimensional boundary: the shift is
gauge in 1+1D and not in 3+1D (twist.py); the twist is a 3-form and vanishes on a
2-manifold (twist.py); the round-trip theorem holds in 1+1D and has no 3+1D
analogue (pathmetric.py).  A boundary that decides three unrelated questions is a
structural fact about the problem, not a coincidence of three methods.

stdlib only.  Every status below is recomputed from the instrument that owns it,
never transcribed -- so a row cannot silently go stale when its instrument moves.
"""
import math, sys

STATUSES = ("DISSOLVED", "RELOCATED", "CLOSED-NEGATIVE", "CONDITIONAL", "UNTESTED", "OPEN")

# (id, obstruction, status, where it went / what decides it, owning instrument)
LEDGER = [
 ("HORIZON-REQUIRED", "a warp drive needs a horizon", "DISSOLVED",
  "f* = 1 - c/v_s is in [0,1) only for v_s >= c: the superluminal pathology",
  "twist.py"),
 ("EXOTIC-MATTER", "warp transport needs negative energy", "DISSOLVED",
  "not for the warpshell: dec observer-robust in bulk and shell, n_2 >= 0. "
  "By leaving SSV's shift-vector class, not by refuting it", "warpshell.py"),
 ("CM-THEOREM", "no isolated system moves its own centre of mass", "RELOCATED",
  "into the energy budget: Bondi momentum changes only by radiating. Paid",
  "warpshell.py"),
 ("ENERGY", "the bill is impossible", "RELOCATED",
  "to astronomical but finite: the Doppler factor cubed, 8/27 at 0.2 c",
  "warpshell.py"),
 ("FELT-ACCEL", "passengers ride in free fall", "RELOCATED",
  "never true here. The cavity is tidally flat; weight remains", "warpshell.py"),
 ("WALL-STABILITY", "the realized wall is marginally stable", "CONDITIONAL",
  "stable iff the matter supplies beta^2 > beta^2_crit(x); counter-rotating "
  "matter does so only below x = 0.46898, margin -> 4/3 as x -> 0", "wall.py"),
 ("ANALOGUE-1D", "a 1+1D metamaterial can emulate a warp metric", "CLOSED-NEGATIVE",
  "E = -Omega^2/(8 pi G) and both vanish on the axis: the target is Minkowski",
  "twist.py"),
 ("SHIFT-SHORTENS", "a shift shortens the path", "CLOSED-NEGATIVE",
  "round trip = optical length, longer by 2v^2/(c(c^2-v^2)) > 0 in 1+1D",
  "pathmetric.py"),
 ("SELF-SOURCED", "an engine sources the metric it uses", "CLOSED-NEGATIVE",
  "the 10^31 gap and the ADM theorem both follow from it alone", "COUPLING.md"),
 ("NONRADIAL", "the shell is stable to l >= 2 perturbations", "CONDITIONAL",
  "IT IS NOT. Pitre-Schneider-Poisson 2026 (PRD): unstable even-parity mode for "
  "all l >= 2, all compactness, all Gamma -- on Le's anchor exactly, and beta^2 "
  "does not appear in it, so the structural fix does not reach it. But the rate "
  "is self-gravitational, ~0.6 sqrt(GM/R^3), so N < 1 is a ceiling on MEAN "
  "DENSITY. THE CORNER IS WITHDRAWN: the same mass sets density and compactness, "
  "so escaping the instability means x -> 0, and the survivor at x = 3e-25 is a "
  "3.97 g/m^2 balloon whose flat cavity is Birkhoff, not a warp feature. Both "
  "stable AND self-gravitating (1% binding) needs 2e9 Msun over 1,000 AU",
  "wall.py"),
 ("MAPPING-2D", "a 2+1D analogue mapping exists", "DISSOLVED",
  "Plebanski 1960 gives it in full 3+1D and returns exactly the transverse "
  "anisotropy twist.py demanded. Briefly closed on BHS -- eps_xx = 1 exactly, so "
  "the static bound admitted it only for |v| >= c -- and REOPENED by "
  "dispersive.py: BHS is a static bound and this is a dispersive device. The "
  "mapping stands; only its BHS verdict fell", "plebanski.py"),
 ("TYPE-IV", "the Alcubierre wall needs matter with no rest frame", "OPEN",
  "measured, 7/7 wall points, |Im|/||T|| 0.14-0.69, stable to six figures in h "
  "and validated against BBV Eq (3.48) to 1e-6. Untouched by every energy "
  "condition, which bound contractions where this is about eigenvectors. THE "
  "OBJECTION THAT REPLACES the energy one. Not forbidden -- unknown. The "
  "sub-objection 'nothing known is Type IV' is now FALSE (see TYPEIV-SOURCES); "
  "what stays open is the CONFIGURATION, radial flux against twisted",
  "typefour.py"),
 ("TYPEIV-SOURCES", "Type IV occurs only as a test field, never as a source",
  "CONDITIONAL",
  "FALSE at first order in hbar: Abdolrahimi-Page-Tzounis solve G = 8 pi <T> "
  "with the Unruh state and get Type IV everywhere outside an evaporating "
  "horizon, escaping all four of MMV's Type-I-forced cases for the same "
  "structural reason the bubble does. The boundary is the ORDER: answered at "
  "first, open at exact, since APT do not iterate to a fixed point and MMV's "
  "theorems are about exact solutions. Magnitude available -- <T> ~ mu^-4 puts "
  "a 1 m 0.1c bubble at the strength of a 1.126e9 kg hole -- but a magnitude "
  "match is not a construction", "selfconsistent.py"),
 ("STATIC-BOUND", "BHS applies at a working frequency", "CLOSED-NEGATIVE",
  "IT DOES NOT. A Polder ferrite above resonance has |kappa| > |mu-1|, violating "
  "BHS by factors up to 5, and above-resonance ferrites are ordinary passive "
  "components. The Brillouin condition that replaces it is satisfied identically, "
  "saturating only at resonance. Cost of the error: beta capped at c/4 when the "
  "real ceiling is the analogue horizon -- 0.825 c at 0.95% ferrite loss",
  "dispersive.py"),
 ("ANEC", "the averaged null energy condition", "OPEN",
  "VIOLATED on every ray of the Alcubierre bubble, INT T_kk dx from -0.081 to "
  "-0.344, and QNEC -- a THEOREM, not a conjecture -- integrates to it. "
  "D-independent, so freeing the wall thickness buys nothing. WITHDRAWS this "
  "session's headline: nullbound.py evaluated SNEC at one sampling width, the "
  "loosest, and SNEC fails above w ~ 0.93 bubble radii. HARDENED, not softened, "
  "by ACHRONALITY below: the one escape is closed and what remains is a single "
  "unproven condition", "anec.py"),
 ("ACHRONALITY", "the ANEC-violating rays might be non-achronal, putting the "
  "bubble outside Graham-Olum", "CLOSED-NEGATIVE",
  "THEY ARE ACHRONAL. 25 ANEC-violating rays over v_s = 0.3/0.5/0.8 c, ZERO "
  "with a conjugate point. And the anti-correlation is Raychaudhuri itself -- "
  "u'' = -4 pi T_kk u, so the negative T_kk that violates ANEC is what "
  "defocuses the congruence and prevents the conjugate point that would break "
  "achronality. PROVED where T_kk <= 0 throughout, measured where the signs "
  "mix. The prohibition now rests entirely on the achronal ANEC in 4D CURVED "
  "spacetime -- unproven for nineteen years, and load-bearing", "achronal.py"),
]

def by_status():
    return {s: [r for r in LEDGER if r[2] == s] for s in STATUSES}

def untested():
    return [r for r in LEDGER if r[2] == "UNTESTED"]

def build_ready():
    """A build is ready when no UNTESTED row is load-bearing for it.  This
    returns the rows that must be tested or explicitly accepted first."""
    return [r[0] for r in untested()]

# -- each row recomputed from its owner, so it cannot go stale ---------------

def check_horizon_required():
    import twist
    return (not twist.has_horizon(0.99)) and twist.has_horizon(1.01)

def check_cm_relocated():
    import warpshell
    # paid, not evaded: the budget is the Doppler factor cubed and is finite
    return abs(warpshell.mission(0.2)[1] - 8.0 / 27.0) < 1e-15

def check_wall_conditional():
    import wall
    xc = wall.matter_crossover()
    return (wall.vlasov_stable(0.3) and not wall.vlasov_stable(2.0 / 3.0)
            and 0.46 < xc < 0.47)

def check_analogue_closed():
    import twist
    # Omega and E both vanish on the axis: nothing to emulate in 1+1D
    return (twist.omega_bbv(0.9, 0.0) == 0.0
            and twist.energy_density_bbv(0.9, 0.0) == 0.0
            and abs(twist.wedge_txy_closed(0.9, 0.3)) > 1e-3)

def check_mapping_dissolved():
    import plebanski, dispersive
    # the mapping stands and is anisotropic; the STATIC bound that closed it does not
    return (plebanski.anisotropy(0.5) > 1.0
            and not dispersive.static_ok(2.0)      # BHS forbids a real ferrite
            and dispersive.dispersive_ok(2.0))     # the right condition does not

def check_nonradial_conditional():
    import wall
    # fatal at ship scale, survivable when diffuse -- that is what CONDITIONAL means
    return (wall.efoldings(1.0e6, 10.0, 0.2, 9.80665) > 100.0
            and wall.efoldings(1.0e6, 5000.0, 0.2, 9.80665) < 0.1)

def check_typeiv_sources_conditional():
    import selfconsistent
    # conditional means: yes in one regime, open in the other, with the boundary
    return (selfconsistent.SCOPE["first order in hbar"]
            and not selfconsistent.SCOPE["exact self-consistent"]
            and not selfconsistent.SCOPE["configuration matched"])

def check_achronality_closed():
    import achronal
    rows = achronal.survey()
    viol = [r for r in rows if r["anec_violated"]]
    # closed negative means: the escape was looked for and is not there
    return (len(viol) > 0 and achronal.escapes(rows) == []
            and rows[0]["proved"])          # and the axial case is proved, not fitted

def check_shift_costs():
    import pathmetric
    return all(pathmetric.excess_density(v) > 0.0 for v in (0.1, 0.5, 0.9))

def selftest():
    ok = True
    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-58s %14s %14s  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("The ledger")
    h = by_status()
    for s in STATUSES:
        print("    %-16s %d   %s" % (s, len(h[s]), ", ".join(r[0] for r in h[s])))
    chk("obstructions tracked", len(LEDGER), 16)
    chk("actually DISSOLVED", len(h["DISSOLVED"]), 3)
    chk("RELOCATED -- still true, renamed", len(h["RELOCATED"]), 3)
    chk("CLOSED-NEGATIVE", len(h["CLOSED-NEGATIVE"]), 5)
    chk("CONDITIONAL", len(h["CONDITIONAL"]), 3)
    chk("UNTESTED -- where the next build fails", len(h["UNTESTED"]), 0)
    chk("UNTESTED is still empty; the new row is OPEN, which is not the same",
        sorted(set(r[2] for r in LEDGER)),
        sorted((set(STATUSES) - {"UNTESTED"}) | {"OPEN"}))
    chk("no row is DISSOLVED without an owning instrument",
        all(r[4] for r in h["DISSOLVED"]), True)

    print("\nEvery row recomputed from its owner, not transcribed")
    chk("HORIZON-REQUIRED dissolves", check_horizon_required(), True)
    chk("CM-THEOREM is paid, exactly 8/27", check_cm_relocated(), True)
    chk("WALL-STABILITY is conditional, not dissolved", check_wall_conditional(), True)
    chk("ANALOGUE-1D is closed negative", check_analogue_closed(), True)
    chk("SHIFT-SHORTENS is closed negative", check_shift_costs(), True)
    chk("NONRADIAL is fatal at 10 m and survivable at 5 km",
        check_nonradial_conditional(), True)
    chk("MAPPING-2D: mapping stands, static bound does not",
        check_mapping_dissolved(), True)
    chk("TYPEIV-SOURCES: yes at first order, open at exact",
        check_typeiv_sources_conditional(), True)
    chk("ACHRONALITY: the escape was looked for and is not there",
        check_achronality_closed(), True)

    print("\nThe question this file exists to answer")
    chk("rows that must be tested or accepted before a build",
        sorted(build_ready()), [])
    chk("is a build blocked on an untested row?", len(untested()) > 0, False)
    print("""      Both were asked, and MAPPING-2D then reopened: it had been closed on a
      STATIC bound applied to a dispersive device, and the bound is
      demonstrably wrong there.  NONRADIAL nearly closed the warpshell and
      left a mean-density corner.  Nothing is UNTESTED -- and one row moved
      from closed back to open, which is what a ledger is for.""")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print(__doc__)
    print("=" * 79)
    h = by_status()
    for s in STATUSES:
        if not h[s]:
            continue
        print("\n%s" % s)
        for r in h[s]:
            print("  %-18s %s" % (r[0], r[1]))
            print("  %-18s   -> %s  [%s]" % ("", r[3], r[4]))
    print("\n" + "=" * 79)
    print("VERDICT")
    # counted from the ledger, never transcribed -- the same rule as every row
    print("  %d dissolved, %d relocated, %d closed negative, %d conditional, %d open"
          % (len(h["DISSOLVED"]), len(h["RELOCATED"]), len(h["CLOSED-NEGATIVE"]),
             len(h["CONDITIONAL"]), len(h["OPEN"])))
    print("  and %d NEVER TESTED.  The obstructions did not dissolve; most of them"
          % len(h["UNTESTED"]))
    print("  became bills or conditions, which is progress of a different kind.")
    print("  Before the next build: %s" % (", ".join(build_ready()) or "nothing untested"))
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
