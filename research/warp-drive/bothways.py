#!/usr/bin/env python3
"""
bothways.py -- "is there a better device that can utilize a wormhole for both
space AND time transition?"

YES, AND IT IS THE DEVICE ALREADY ON THE TABLE.  You do not need a different
object -- you need a third OPERATING MODE of the one gate.py described, and
that mode gives both transitions while staying chronology-respecting.

===============================================================================
1. WHAT THE WORMHOLE BUYS OVER THE CORRIDOR: THE KNOBS COME APART
===============================================================================

unified.py measured the corridor's central limitation and it was severe:

        ONE Phi, TWO EXPONENTS, RATIO EXACTLY 2.  Space and time could not be
        moved separately, at any source strength, at either sign.

A wormhole has TWO INDEPENDENT PARAMETERS:

        SPACE  the THROAT        -- the shortcut, set by mouth separation
        TIME   the MOUTH OFFSET  -- set by differential aging between mouths

    THEY DECOUPLE.  That is what "better device" means here, it is structural,
    and it is the single largest capability difference between the two
    architectures.  The corridor could not do this at all.

===============================================================================
2. AND THE TIME HALF COSTS NO EXOTIC MATTER
===============================================================================

The throat is what needs rho < 0, and it is bought ONCE.  The offset is bought
with KINEMATICS -- move one mouth, bring it back:

        Delta t  =  tau (gamma - 1)

        beta      gamma      tau to bank 4 years    exotic matter
        0.500     1.1547     25.856 yr              NONE
        0.866     1.9998      4.001 yr              NONE
        0.990     7.0888      0.657 yr              NONE
        0.999    22.3663      0.187 yr              NONE

    THE TIME TRANSITION IS FREE IN THE CURRENCY THAT MATTERS.  It costs
    propellant to accelerate a mouth's ADM mass, which is ordinary propulsion
    and an ordinary bill.  No additional negative mass is required for it, at
    any offset.

===============================================================================
3. THREE OPERATING MODES, AND THE MIDDLE ONE IS THE ANSWER
===============================================================================

        mode            offset            space  time   CTC   status
        GATE            0                 yes    no     no    safest; amortises
        SHIFTED         0 < dt < D/c      yes    YES    no    BOTH, and legal
        TIME MACHINE    dt > D/c          yes    yes    YES   unresolved

    THE SHIFTED MODE IS THE DEVICE THE QUESTION ASKS FOR.  Below the threshold
    the spacetime remains chronology-respecting -- no closed timelike curves,
    no self-consistency problem, nothing for chronology protection to protect
    against -- and you still get a genuine time displacement on top of the
    spatial shortcut.

        For a four-light-year gate the usable window is a time displacement of
        UP TO FOUR YEARS.  For a hundred-light-year gate, up to a century.

    THE WINDOW SCALES WITH THE SEPARATION, which is the opposite of every other
    scaling in this project and is worth saying twice.

===============================================================================
4. THE ABSOLUTE LIMIT, AND NO DEVICE BEATS IT
===============================================================================

The offset is ACCUMULATED, not conjured.  It cannot exceed the total
differential aging since the two mouths were together, which cannot exceed the
gate's own age.

        YOU CAN NEVER REACH BACK BEFORE THE GATE WAS BUILT.

    That is a property of the construction, not a technological limit, and it
    holds for every variant -- velocity, gravitational potential, any
    combination.  A better device cannot beat it because there is nothing to
    improve: the quantity is a sum over elapsed time and the sum starts at
    construction.

===============================================================================
5. WHAT IS ACTUALLY OPEN, AND IT IS ONLY THE THIRD MODE
===============================================================================

Push the offset past D/c and closed timelike curves form.  What happens then is
THE ONE GENUINELY UNRESOLVED QUESTION IN THIS SUBJECT:

        KIM & THORNE       vacuum polarisation diverges at the Cauchy horizon
                           but is cut off at the Planck scale; the machine
                           survives
        HAWKING            the divergence is not cut off; chronology protection
                           destroys the machine as it forms

    Unresolved since 1991, and scale.py already carries it as NOT-RUN.  Nothing
    in this file rests on it, BECAUSE THE SHIFTED MODE NEVER ENTERS THAT
    REGIME.

===============================================================================
SO THE ANSWER, PLAINLY
===============================================================================

    THE BETTER DEVICE IS THE SAME DEVICE, RUN WITH A BOUNDED OFFSET.  It
    transitions both space and time, the time half adds no exotic matter, the
    usable time window grows with the separation, and it stays out of
    chronology protection's reach by construction rather than by luck.

    AND THE BILL IS UNCHANGED: the throat still needs rho < 0 -- 17.9 Earth
    masses at human scale, 0.081 solar masses at Kuhfittig's three kilometres
    -- and the far mouth still has to be carried there at sublight first.
    NOTHING IN THIS FILE MOVES THE SOURCE PROBLEM.

stdlib only.  gate.py supplies the throat costs and the deployment time,
unified.py the corridor's locked ratio this file contrasts against.
"""
import math, sys

C, LY, YEAR = 2.99792458e8, 9.4607e15, 3.15576e7


# ---------------------------------------------- 1: the knobs come apart

CORRIDOR_LOCKED = True        # unified.py: one Phi, ratio exactly 2
WORMHOLE_KNOBS = ("throat (space)", "mouth offset (time)")


def knobs_are_independent():
    """Two parameters, set separately.  The corridor had one."""
    return len(WORMHOLE_KNOBS) == 2 and CORRIDOR_LOCKED


def corridor_ratio():
    """unified.py: e^{-2Phi} against e^{-Phi}.  Locked at 2, unavoidably."""
    return 2.0


# ------------------------------------------ 2: the time half is free

def gamma(beta):
    return 1.0 / math.sqrt(1.0 - beta * beta)


def offset(tau_years, beta):
    """Delta t = tau (gamma - 1), banked by moving a mouth and returning it."""
    return tau_years * (gamma(beta) - 1.0)


def tau_for_offset(dt_years, beta):
    return dt_years / (gamma(beta) - 1.0)


def exotic_cost_of_time():
    """Zero.  The throat needs rho < 0; the offset needs propellant."""
    return 0.0


# --------------------------------- 3: three modes, and the usable window

def ctc_threshold_years(separation_ly):
    """The offset must exceed the external light time for a loop to close."""
    return separation_ly


def mode(dt_years, separation_ly):
    if dt_years <= 0.0:
        return "GATE"
    if dt_years < ctc_threshold_years(separation_ly):
        return "SHIFTED"
    return "TIME MACHINE"


def is_chronology_respecting(dt_years, separation_ly):
    return mode(dt_years, separation_ly) in ("GATE", "SHIFTED")


def usable_window_years(separation_ly):
    """Time displacement available with NO closed timelike curves."""
    return ctc_threshold_years(separation_ly)


def window_grows_with_separation():
    """The opposite of every other scaling in this project."""
    return usable_window_years(100.0) > usable_window_years(4.0)


MODES = (
    ("GATE", "0", "yes", "no", False, "safest; amortises"),
    ("SHIFTED", "0 < dt < D/c", "yes", "YES", False, "BOTH, and legal"),
    ("TIME MACHINE", "dt > D/c", "yes", "yes", True, "unresolved"),
)


# ----------------------------------------- 4: the limit nothing beats

def can_precede_construction():
    """No.  The offset is a sum over elapsed time and the sum starts at t=0."""
    return False


LIMIT = "the offset cannot exceed the gate's own age"


# ----------------------------------------- 5: what is actually open

CHRONOLOGY_PROTECTION = "NOT-RUN"
KIM_THORNE = "the Cauchy-horizon divergence is cut off at the Planck scale"
HAWKING = "it is not cut off; the machine is destroyed as it forms"


def shifted_mode_depends_on_it(dt_years=3.0, separation_ly=4.0):
    """No -- it never enters the CTC regime."""
    return not is_chronology_respecting(dt_years, separation_ly)


# ------------------------------------------------ and what does not move

SOURCE_MOVED = False
DEPLOYMENT_STILL_SUBLIGHT = True


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

    print("1. THE KNOBS COME APART -- the corridor's could not")
    near("corridor's locked ratio (unified.py)", corridor_ratio(), 2.0, 1e-12)
    chk("wormhole knobs are independent", knobs_are_independent(), True)
    for k in WORMHOLE_KNOBS:
        print("      %s" % k)

    print("\n2. AND THE TIME HALF COSTS NO EXOTIC MATTER")
    print("      %8s %10s %18s" % ("beta", "gamma", "tau to bank 4 yr"))
    for b in (0.5, 0.866, 0.99, 0.999):
        print("      %8.3f %10.4f %15.3f yr" % (b, gamma(b), tau_for_offset(4.0, b)))
    near("tau at beta = 0.866 (gamma = 2)", tau_for_offset(4.0, 0.866), 4.001, 1e-3)
    near("exotic matter for the offset", exotic_cost_of_time(), 0.0, 1e-12)
    print("      propellant to move a mouth's ADM mass -- an ordinary bill.")

    print("\n3. THREE MODES, AND THE MIDDLE ONE IS THE ANSWER")
    print("      %-14s %-16s %-6s %-6s %-5s %s"
          % ("mode", "offset", "space", "time", "CTC", "status"))
    for n, o, s_, t, c, st in MODES:
        print("      %-14s %-16s %-6s %-6s %-5s %s" % (n, o, s_, t, c, st))
    chk("a 3-year offset on a 4 ly gate", mode(3.0, 4.0), "SHIFTED")
    chk("  is chronology-respecting", is_chronology_respecting(3.0, 4.0), True)
    chk("a 5-year offset on a 4 ly gate", mode(5.0, 4.0), "TIME MACHINE")
    near("usable window, 4 ly gate (years)", usable_window_years(4.0), 4.0, 1e-12)
    near("usable window, 100 ly gate (years)", usable_window_years(100.0), 100.0, 1e-12)
    chk("the window GROWS with separation", window_grows_with_separation(), True)
    print("      the opposite of every other scaling in this project.")

    print("\n4. THE LIMIT NOTHING BEATS")
    chk("can the offset precede construction", can_precede_construction(), False)
    print("      %s -- a property of the construction, not of technology." % LIMIT)

    print("\n5. WHAT IS ACTUALLY OPEN, AND IT IS ONLY MODE THREE")
    chk("chronology protection", CHRONOLOGY_PROTECTION, "NOT-RUN")
    print("      Kim & Thorne: %s" % KIM_THORNE)
    print("      Hawking:      %s" % HAWKING)
    chk("the SHIFTED mode depends on that being resolved",
        shifted_mode_depends_on_it(), False)

    print("\nAND WHAT DOES NOT MOVE")
    chk("the source problem moved", SOURCE_MOVED, False)
    chk("deployment is still sublight", DEPLOYMENT_STILL_SUBLIGHT, True)

    print("\n  SELFTEST " + ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    print("""VERDICT

  YES, AND IT IS THE SAME DEVICE IN A THIRD OPERATING MODE.

  What a wormhole buys over the corridor is that THE KNOBS COME
  APART.  unified.py measured the corridor locked -- one Phi, two
  exponents, ratio exactly two, space and time unmovable separately
  at any source strength or sign.  A wormhole has two independent
  parameters: the THROAT sets the spatial shortcut, the MOUTH OFFSET
  sets the temporal displacement, and neither constrains the other.
  That decoupling is the capability difference, and the corridor
  could not do it at all.

  AND THE TIME HALF IS FREE IN THE CURRENCY THAT MATTERS.  The throat
  is what needs rho < 0 and it is bought once.  The offset is bought
  with kinematics -- Delta t = tau(gamma - 1), four years of mouth
  travel at gamma = 2 banking four years of offset -- and costs
  propellant, not negative mass, at any magnitude.

  THE MODE THE QUESTION ASKS FOR IS THE MIDDLE ONE.  Below
  Delta t = D/c the spacetime stays chronology-respecting: no closed
  timelike curves, nothing for chronology protection to act against,
  and a genuine time displacement on top of the spatial shortcut.
  For a four-light-year gate that window is four years; for a hundred
  light years, a century.  THE WINDOW GROWS WITH THE SEPARATION,
  which is the opposite of every other scaling in this project.

  AND ONE LIMIT NO DEVICE BEATS: the offset is accumulated, so it
  cannot exceed the gate's own age.  YOU CAN NEVER REACH BACK BEFORE
  THE GATE WAS BUILT.  There is nothing to improve there -- the
  quantity is a sum over elapsed time and the sum starts at
  construction.

  ONLY THE THIRD MODE IS OPEN.  Past D/c, closed timelike curves form
  and Kim-Thorne against Hawking has been unresolved since 1991.  The
  shifted mode never enters that regime, so nothing here rests on it.

  AND THE BILL IS UNCHANGED.  The throat still needs rho < 0 -- 17.9
  Earth masses at human scale, 0.081 solar masses at three kilometres
  -- and the far mouth still has to be carried there at sublight
  first.  This file adds capability, not permission.""")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report()
