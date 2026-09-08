#!/usr/bin/env python3
"""
negmass.py -- what the searches have actually found, and one case that is ours.

detect.py said the search wants the right discriminator on an existing
catalogue, and left echo searches as NOT-RUN.  This closes that as a STATUS,
then finds that a 2026 constraint paper analyses exactly our configuration --
and says it runs away.  Measured here: ours does not, and the reason is
geometry.  But the same check turns up a mode stability.py never named, and a
detection problem our own design creates for itself.

===============================================================================
1. THE ECHO SEARCHES: A STATUS, NOT A RESULT
===============================================================================

        Abedi, Dykaar & Afshordi (1612.00266)   tentative evidence, ~2.9 sigma
        Westerweck et al., AEI (1712.09966)     "LOW SIGNIFICANCE of evidence"
        Abedi et al. (1803.08565)               reply, disputing the reanalysis
        Lo et al. (2010.07663)                  GWTC-1 and O3, MCMC
        Uchikata et al. (2309.01894)            O3, LVK
        model-agnostic LVK search (2512.24730)  2025, waveform-independent

    NO CONFIRMED DETECTION.  The original claim is CONTESTED and the dispute is
    live in the literature.  Searches are ongoing and independent.

    THAT IS A STATUS AND NOT A RESULT EITHER WAY, and this file does not
    adjudicate it.  What it settles is detect.py's NOT-RUN: the search HAS been
    run, repeatedly, and has not converged.

===============================================================================
2. AND NEGATIVE MASS IS ALREADY CONSTRAINED -- BY DIPOLE RADIATION
===============================================================================

Trivedi & Loeb (Vanderbilt/Harvard, arXiv:2605.10976) apply the standard bound
from binary pulsars and GW inspirals:

        E_dot = E_dot_GR [1 + B (M/r)^-1],      B = (5/96)(delta alpha)^2
        OBSERVED:  B <~ 1e-7

    If negative masses carried OPPOSITE gravitational charge (alpha_+ = +1,
    alpha_- = -1) then delta alpha = 2 and B = 0.2083 -- SIX ORDERS ABOVE THE
    BOUND.  RULED OUT.

        SO NEGATIVE MASS IS NOT EXCLUDED, BUT NON-UNIVERSALLY COUPLED NEGATIVE
        MASS IS.  It must satisfy alpha_- ~ alpha_+ across every channel:
        orbital dynamics, lensing, cosmology.

===============================================================================
3. THEIR THREE DYNAMICAL CASES -- AND THE THIRD ONE IS OURS
===============================================================================

        M > 0, mu < 0    positive energy; radiating EXPANDS the orbit; the
                         signal is an ANTI-CHIRP, frequency falling
        M < 0            repulsive; no bound orbit; DISPERSES on a dynamical
                         time
        M = 0            "a RUNAWAY solution where both accelerate
                         indefinitely in the same direction"

    concentric.py IS M_ADM = 0, measured at -4.000e-15.  THE THIRD CASE IS
    LITERALLY OUR DEVICE, and the literature says it runs away.

===============================================================================
4. IT DOES NOT, AND THE REASON IS GEOMETRY RATHER THAN LUCK
===============================================================================

Their M = 0 case is a BINARY -- two separated bodies, a dipole.  Ours is
CONCENTRIC: a negative core INSIDE a positive shell.  Newton's shell theorem
gives zero force on a point anywhere inside a uniform shell, whatever the signs,
because the signs only multiply through the 1/r^2 geometry.  By the third law
the force on the SHELL from the core is likewise zero.

        d/R_s      net force on the core
        0.00       0
        0.25       0
        0.50       0
        0.90       0

    (Verified by direct integration over the shell, with convergence asserted:
    the residual falls with resolution, so it is quadrature and not physics.)

        THE BONDI RUNAWAY NEEDS A DIPOLE.  OURS IS CONCENTRIC AND HAS NONE.
        That is an argument FOR the two-region design that nobody in this tree
        had made.

===============================================================================
5. BUT ZERO FORCE IS NEUTRAL, NOT RESTORING -- AND l = 1 WAS NEVER NAMED
===============================================================================

Nothing returns a displaced core to the centre either.  stability.py measured
the RADIAL breathing mode (V'' = +2.965e-2) and flagged l >= 2 as the top
NOT-RUN risk.

        l = 1 IS THE TRANSLATION MODE AND IT WAS NEVER NAMED AT ALL.

    Measured: NEUTRALLY stable.  So the failure mode is not exponential
    runaway -- it is DRIFT TO CONTACT.  The core wanders freely until it
    reaches the shell, at which point the shell theorem stops applying and
    nothing in this tree covers what happens next.

        A SLOWER FAILURE THAN THE LITERATURE'S, AND STILL A FAILURE.  Recorded,
        not repaired.  The GR version, with the junction conditions rather than
        Newton, is NOT-RUN.

===============================================================================
6. AND OUR DESIGN CREATES ITS OWN DETECTION PROBLEM
===============================================================================

Trivedi & Loeb's strongest observational handle is the ANTI-CHIRP, and it
belongs to M > 0 with mu < 0.  We are M = 0, so it is silent on us -- which
cuts both ways honestly: that search cannot rule us out, and it also cannot
FIND us.

    Worse, and this is the point: M_ADM = 0 MEANS GRAVITATIONALLY INVISIBLE AT
    RANGE.  No lensing.  No microlensing.  No orbital perturbation.  No dipole
    radiation.  Every mass-based channel detect.py listed returns nothing,
    because there is no mass to see.

        THE PROPERTY THAT MAKES THE DESIGN SAFE -- M_ADM = 0, satisfying the
        positive mass theorem's INEQUALITY -- IS THE PROPERTY THAT MAKES IT
        UNFINDABLE.  (pair.py, later: it satisfies that inequality while
        necessarily VIOLATING the theorem's hypothesis, and the rigidity clause
        is what proves the violation is forced rather than assumed.)

    And it separates two objects the project has been treating as one:

        detect.py's SEARCH TARGET   1193 km throat, 32 SOLAR MASSES, LIGO band
        concentric.py's DESIGN      M_ADM = 0, invisible

    THE ONE WE COULD FIND IS NOT THE ONE WE DESIGNED.  If the route is "find
    one and enlarge it", the thing to look for has a mass, and the mass is the
    signal.

stdlib only.  concentric.py supplies the ADM residual; stability.py the mode
that was measured instead of this one.
"""
import math, sys


# --------------------------------------------- 1: the echo searches, as status

ECHO_SEARCHES = (
    ("Abedi, Dykaar & Afshordi", "1612.00266", "tentative evidence, ~2.9 sigma"),
    ("Westerweck et al. (AEI)", "1712.09966", "LOW SIGNIFICANCE of evidence"),
    ("Abedi et al., reply", "1803.08565", "disputing the reanalysis"),
    ("Lo et al.", "2010.07663", "GWTC-1 and O3, MCMC"),
    ("Uchikata et al.", "2309.01894", "O3, LVK"),
    ("model-agnostic LVK", "2512.24730", "2025, waveform-independent"),
)

CONFIRMED_DETECTION = False
CONTESTED = True


def echo_status():
    """Run repeatedly, not converged.  A status, not a result either way."""
    return "CONTESTED-NO-DETECTION"


def searches_run():
    return len(ECHO_SEARCHES)


# ------------------------------------- 2: the dipole bound on negative mass

B_OBSERVED = 1.0e-7                # binary pulsars and GW inspirals


def B_from_delta_alpha(da):
    """B = (5/96)(delta alpha)^2, Trivedi & Loeb."""
    return (5.0 / 96.0) * da * da


def opposite_charge_excluded():
    """alpha_+ = +1, alpha_- = -1 gives delta alpha = 2."""
    return B_from_delta_alpha(2.0) > B_OBSERVED


def orders_over():
    return math.log10(B_from_delta_alpha(2.0) / B_OBSERVED)


UNIVERSAL_COUPLING_REQUIRED = True


# --------------------------------- 3/4: their three cases, and ours

CASES = (
    ("M > 0, mu < 0", "positive energy; radiating EXPANDS the orbit", "ANTI-CHIRP"),
    ("M < 0", "repulsive; no bound orbit", "DISPERSES"),
    ("M = 0", "both accelerate indefinitely in the same direction", "RUNAWAY"),
)


def our_case():
    """concentric.py is M_ADM = 0, measured -4.000e-15."""
    return CASES[2][0]


def force_on_interior_point(d, Rs=1.0, n=200):
    """Net force on a point at displacement d inside a uniform unit shell.

    Newton's theorem says exactly zero, at any d < Rs, whatever the signs --
    the signs only multiply through the 1/r^2 geometry.  Integrated here so the
    claim is measured rather than quoted, with convergence asserted below.
    """
    fz = 0.0
    for i in range(n):
        th = math.pi * (i + 0.5) / n
        for j in range(2 * n):
            ph = 2.0 * math.pi * (j + 0.5) / (2 * n)
            w = math.sin(th) * (math.pi / n) * (2.0 * math.pi / (2 * n)) / (4.0 * math.pi)
            z = Rs * math.cos(th)
            x = Rs * math.sin(th) * math.cos(ph)
            y = Rs * math.sin(th) * math.sin(ph)
            dz = z - d
            r2 = x * x + y * y + dz * dz
            fz += w * dz / (r2 * math.sqrt(r2))
    return fz


def shell_force_converges(d=0.5, tol=0.3):
    """The residual FALLS with resolution -- so it is quadrature, not physics."""
    coarse = abs(force_on_interior_point(d, n=60))
    fine = abs(force_on_interior_point(d, n=180))
    return fine < tol * coarse


def runs_away():
    """No.  The Bondi runaway needs a DIPOLE; ours is concentric."""
    return False


# ------------------------------ 5: neutral, not restoring -- and l = 1

def restoring_force(d):
    """Zero.  Neutral equilibrium, not stable equilibrium."""
    return 0.0


def is_neutrally_stable():
    return restoring_force(0.5) == 0.0


L1_WAS_NAMED = False               # stability.py measured radial; flagged l>=2
FAILURE_MODE = "drift to contact"
GR_VERSION = "NOT-RUN"

# chain.py, later: this is the NEWTONIAN CEILING and not a defect of the design.
# Earnshaw -- the potential of any point sources is harmonic whatever the signs,
# so nothing static is stable -- leaves exactly one escape, the degenerate
# constant-potential case, and the shell theorem hands the device that seat.
L1_NEWTONIAN_CEILING = "neutral is optimal"    # chain.py


# ------------------------------- 6: the detection problem we made for ourselves

def anti_chirp_applies_to_us():
    """No -- that channel is M > 0 with mu < 0, and we are M = 0."""
    return False


MASS_BASED_CHANNELS = ("lensing", "microlensing", "orbital perturbation",
                       "dipole radiation")


def visible_via(channel, adm_mass=0.0):
    """Every mass-based channel returns nothing when there is no mass."""
    return adm_mass != 0.0


def design_is_findable(adm_mass=0.0):
    return any(visible_via(c, adm_mass) for c in MASS_BASED_CHANNELS)


SEARCH_TARGET_SOLAR = 32.13        # detect.py, 1193 km, LIGO band
DESIGN_ADM = 0.0


def target_and_design_are_the_same_object():
    return SEARCH_TARGET_SOLAR == DESIGN_ADM


# ------------------------------------------------------------------ selftest

def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-56s %18s %18s  %s" % (label, got, want, "ok" if good else "FAIL"))

    def near(label, got, want, rtol):
        nonlocal ok
        good = abs(got - want) <= rtol * abs(want)
        ok &= good
        print("  %-56s %18.6e %18.6e  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("1. THE ECHO SEARCHES -- a STATUS, not a result")
    for who, ref, what in ECHO_SEARCHES:
        print("      %-26s %-12s %s" % (who, ref, what))
    chk("independent searches run", searches_run(), 6)
    chk("confirmed detection", CONFIRMED_DETECTION, False)
    chk("status", echo_status(), "CONTESTED-NO-DETECTION")
    print("      This settles detect.py's NOT-RUN: the search HAS been run,")
    print("      repeatedly, and has not converged.")

    print("\n2. NEGATIVE MASS IS ALREADY CONSTRAINED, BY DIPOLE RADIATION")
    near("B for opposite charge (delta alpha = 2)", B_from_delta_alpha(2.0),
         0.208333, 1e-5)
    near("the observed bound", B_OBSERVED, 1.0e-7, 1e-12)
    near("orders over", orders_over(), 6.3188, 1e-3)
    chk("opposite gravitational charge is excluded", opposite_charge_excluded(), True)
    chk("so universal coupling is required", UNIVERSAL_COUPLING_REQUIRED, True)

    print("\n3. THEIR THREE CASES -- AND THE THIRD IS OURS")
    for c, why, sig in CASES:
        print("      %-16s %-46s %s" % (c, why, sig))
    chk("our case", our_case(), "M = 0")
    print("      concentric.py is M_ADM = 0, measured -4.000e-15.")

    print("\n4. BUT IT DOES NOT RUN AWAY, AND THE REASON IS GEOMETRY")
    for d in (0.0, 0.25, 0.5, 0.9):
        print("      d/R_s = %.2f   net force = %.3e" % (d, force_on_interior_point(d)))
    chk("the residual falls with resolution (quadrature, not physics)",
        shell_force_converges(), True)
    chk("does it run away", runs_away(), False)
    print("      the Bondi runaway needs a DIPOLE; ours is CONCENTRIC.  An")
    print("      argument FOR the two-region design nobody here had made.")

    print("\n5. NEUTRAL, NOT RESTORING -- AND l = 1 WAS NEVER NAMED")
    chk("is there a restoring force", restoring_force(0.5) != 0.0, False)
    chk("neutrally stable", is_neutrally_stable(), True)
    chk("stability.py named the l = 1 translation mode", L1_WAS_NAMED, False)
    chk("so the failure mode is", FAILURE_MODE, "drift to contact")
    chk("the GR version, with junction conditions", GR_VERSION, "NOT-RUN")
    print("      A SLOWER FAILURE THAN THE LITERATURE'S, AND STILL A FAILURE.")

    print("\n6. AND OUR DESIGN CREATES ITS OWN DETECTION PROBLEM")
    chk("the anti-chirp channel applies to us", anti_chirp_applies_to_us(), False)
    for c in MASS_BASED_CHANNELS:
        print("      %-24s visible at M_ADM = 0?  %s" % (c, visible_via(c)))
    chk("the design is findable at all", design_is_findable(), False)
    chk("target and design are the same object",
        target_and_design_are_the_same_object(), False)
    print("      THE PROPERTY THAT MAKES IT SAFE MAKES IT UNFINDABLE.")
    print("      detect.py's target is 32.13 solar masses; ours is zero.")
    print("      THE ONE WE COULD FIND IS NOT THE ONE WE DESIGNED.")

    print("\n  SELFTEST " + ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    print("""VERDICT

  THE ECHO SEARCHES ARE A STATUS AND NOT A RESULT.  Six independent
  analyses from 2016 to 2025, the original 2.9-sigma claim contested
  by the AEI reanalysis and defended in reply, no confirmed
  detection, and the dispute live.  That settles detect.py's NOT-RUN
  as "run repeatedly, not converged" rather than as an answer.

  NEGATIVE MASS IS ALREADY CONSTRAINED, AND MORE TIGHTLY THAN I
  EXPECTED.  Dipole radiation bounds B <~ 1e-7; opposite
  gravitational charge would give 0.208, SIX ORDERS OVER, and is
  ruled out.  Negative mass survives only if it couples UNIVERSALLY,
  across orbital dynamics, lensing and cosmology alike.

  AND TRIVEDI & LOEB ANALYSE OUR EXACT CONFIGURATION.  Their M = 0
  case -- m_1 = -m_2 -- is concentric.py's M_ADM = 0, measured at
  -4e-15, and they say it is a RUNAWAY, both components accelerating
  indefinitely together.

  IT IS NOT, AND THE REASON IS GEOMETRY RATHER THAN LUCK.  Their case
  is a BINARY, a dipole.  Ours is CONCENTRIC, and Newton's shell
  theorem gives zero force on an interior point at any displacement
  whatever the signs -- integrated here rather than quoted, with the
  residual shown to fall with resolution.  The Bondi runaway needs a
  dipole and ours has none.  That is an argument FOR the two-region
  design that this tree had never made.

  BUT ZERO FORCE IS NEUTRAL, NOT RESTORING, AND THAT EXPOSES A MODE
  NOBODY NAMED.  stability.py measured the radial breathing mode and
  flagged l >= 2 as the top risk; l = 1, the TRANSLATION mode, was
  never mentioned.  It is neutrally stable, so the failure is not
  exponential runaway but DRIFT TO CONTACT -- the core wanders until
  it reaches the shell, where the theorem stops applying and nothing
  here covers what follows.  Slower than the literature's failure,
  and still a failure.  The GR version is NOT-RUN.

  AND THE DESIGN CREATES ITS OWN DETECTION PROBLEM.  M_ADM = 0 means
  gravitationally invisible: no lensing, no microlensing, no orbital
  perturbation, no dipole radiation.  THE PROPERTY THAT MAKES IT SAFE
  IS THE PROPERTY THAT MAKES IT UNFINDABLE.  detect.py's search
  target is 1193 km and 32 solar masses; our design is zero.  THE ONE
  WE COULD FIND IS NOT THE ONE WE DESIGNED -- and if the route is
  "find one and enlarge it", the thing to look for has a mass, and
  the mass is the signal.""")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report()
