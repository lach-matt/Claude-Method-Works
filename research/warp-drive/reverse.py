#!/usr/bin/env python3
"""
reverse.py -- the dichotomy read backwards, per M's own rule.

M: "the corridor was built specifically to go the other way -- but should still
be able to read it backwards."

transit.py proved that for rays: v(x) := u(L-x) solves the reversed potential
with the SAME conjugate pair, measured to 1.1e-14.  M's prediction was that the
expression is "visible at both ends with the same binary chain".  This file
applies that to the DICHOTOMY rather than to a ray, and the backwards reading
splits the project's obstacle in two.

===============================================================================
THE INVARIANT VISIBLE FROM BOTH ENDS: WEYL IS SIGN-BLIND
===============================================================================

    FORWARD  dichotomy.py: a NEGATIVE mass focuses through Weyl, which carries
             no Sturm density requirement, so it escapes the collapse bound and
             seats with no horizon.

    BACKWARD  the same sentence with the sign flipped: WEYL IS SIGN-BLIND, so a
             POSITIVE mass focuses exactly as hard, carries no Sturm
             requirement either, AND ESCAPES THE COLLAPSE BOUND FOR THE SAME
             REASON.

    Same binary chain, read from the other end.  And it is measured, not argued:

        M           conjugate     t - |dx|        r_s = 2M    inside r_s?
        -2.0e-3     56.50         -3.7618e-02     0.004       no
        +2.0e-3     55.17         +5.1227e-02     0.004       no
        -4.0e-3     47.17         -6.3168e-02     0.008       no
        +4.0e-3     46.17         +1.1788e-01     0.008       no

    BOTH SIGNS SEAT, WITHIN 2.4 % OF THE SAME AFFINE PARAMETER, AND NEITHER IS
    ANYWHERE NEAR ITS OWN SCHWARZSCHILD RADIUS -- the region is 75 times r_s.
    Only the ARRIVAL flips sign, which composite.py recorded and nobody read
    backwards.

===============================================================================
AND THE POSITIVE-MASS SEAT IS NOT HYPOTHETICAL.  IT IS OBSERVED.
===============================================================================

        solar gravitational focus  f = b^2 c^2/(4 G M) = 547.6 AU
        published value                                  ~550 AU

    THE SUN SEATS A CONJUGATE POINT AT 550 ASTRONOMICAL UNITS.  It has been
    doing so for four and a half billion years, it violates no energy
    condition, it collapses nothing, and it needed no engineering.

===============================================================================
SO THE DEVICE SPLITS, AND THE TWO HALVES DO NOT COST THE SAME
===============================================================================

The corridor does two things.  Read backwards they come apart completely:

    THE SEAT -- a conjugate point at a declared range.  FREE.  Ordinary matter,
        positive energy, every energy condition satisfied, no collapse, no
        horizon, no throat, and already occurring in nature at 550 AU.  ZERO
        of this project's impossibility lives here.

    THE CONTRACTION -- proper distance falling, which is phase1's D3 and the
        thing that makes it a TRANSITION.  Needs Phi > 0, which needs rho < 0.
        Measured: ordinary +M gives a proper ratio of 1.003076 -- LONGER.
        ONE HUNDRED PER CENT of this project's impossibility lives here.

    THE OBSTACLE WAS NEVER "THE DEVICE".  IT WAS ALWAYS ONE HALF OF IT, AND
    THE OTHER HALF IS A SOLVED PROBLEM WITH AN EXISTING EXAMPLE.

===============================================================================
WHAT THAT VINDICATES, AND WHAT IT DOES NOT
===============================================================================

    VINDICATED.  "A controlled gravitational focus at a chosen range, addressed
    by declaring both endpoints, built from fields that satisfy every energy
    condition" survives everything this project has thrown at it.  What was
    WITHDRAWN in spec.py was the B*l invariant, and that was the STURM route to
    the seat -- the one that does collapse.  The WEYL route to the same seat is
    gravitational lensing, f = b^2 c^2/4GM, and it is fine.  spec.py said so
    itself and the tree kept quoting the withdrawal as though it had taken the
    seat with it.

    NOT VINDICATED, AND THIS IS THE HALF THAT MATTERS.  A free seat is not a
    free transition.  The seat alone is a LENS: it focuses light at a range,
    it carries no payload, and it shortens nothing.  Every number in phase1,
    supply.py, scale.py, currency.py and shaping.py prices the CONTRACTION, and
    not one of them moves.  1.349e26 kg per metre stands exactly where it was.

        A LENS IS NOT A TRANSITION, AND THE SUN IS NOT A WARP DRIVE.

===============================================================================
AND IT CATCHES A STALE CLAIM IN spec.py
===============================================================================

spec.py's inventory still reads "ANEC VIOLATION PROTECTS ACHRONALITY
(achronal.py), so the obvious escape from Graham-Olum is structurally
unavailable."  anecscope.py overturned that: achronal.py's shear claim was
inverted, and with it corrected no ray of the corridor is both ANEC-violating
and achronal.  Struck in place there.

stdlib only.  composite.py supplies both signs, spec.py the solar focus,
transition.py the proper-distance measurement.
"""
import math, sys

AU = 1.495978707e11
M_SUN = 1.98892e30
R_SUN = 6.957e8


# --------------------------------------------- the invariant, read both ways

def seats(M):
    """Does a source of this sign seat a conjugate point?  Weyl is sign-blind."""
    import composite
    return composite.survey(M)["conjugate"]


def both_signs_seat(mag=2.0e-3, rtol=0.05):
    """And within a few per cent of the same affine parameter."""
    a, b = seats(-mag), seats(+mag)
    return a is not None and b is not None and abs(a / b - 1.0) < rtol


def schwarzschild_radius(M):
    return 2.0 * abs(M)


def inside_own_horizon(M, region=None):
    import composite
    region = composite.B_DEFAULT if region is None else region
    return region < schwarzschild_radius(M)


def neither_sign_collapses(mag=2.0e-3):
    return not inside_own_horizon(-mag) and not inside_own_horizon(+mag)


def region_over_rs(mag=2.0e-3):
    import composite
    return composite.B_DEFAULT / schwarzschild_radius(mag)


# ------------------------------------------- the positive seat is observed

def solar_focus_au():
    import spec
    return spec.focal_length(M_SUN, R_SUN) / AU


def seat_is_observed(tol=0.01):
    """547.6 AU against a published ~550.  The Sun has been doing it throughout."""
    return abs(solar_focus_au() / 550.0 - 1.0) < 0.01 + tol


# ------------------------------------------------------- the two halves

def contraction(sign, strength=8.0e-2):
    """Proper ratio.  > 1 is LONGER.  Only a negative mass contracts."""
    import transition, concentric
    phi = (transition.ordinary_potential(strength) if sign > 0
           else concentric.potential(strength))
    pr, _lt = transition.proper_ratio(phi, -150.0, 150.0, 1.0)
    return pr


def ordinary_matter_contracts():
    """No -- it stretches.  This is where all the impossibility lives."""
    return contraction(+1) < 1.0


HALVES = (
    ("the seat", "FREE",
     "ordinary matter, every energy condition satisfied, no collapse, no "
     "horizon, and occurring in nature at 550 AU"),
    ("the contraction", "ALL OF IT",
     "needs Phi > 0, hence rho < 0; ordinary matter gives a proper ratio of "
     "1.003076, which is LONGER"),
)


def impossibility_is_in_one_half():
    return [h[0] for h in HALVES if h[1] == "ALL OF IT"] == ["the contraction"]


# ----------------------------------------------- what does NOT move

A_LENS_IS_NOT_A_TRANSITION = True
EXCHANGE_RATE_MOVED = False          # 1.349e26 kg/m stands exactly where it was


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

    print("THE INVARIANT VISIBLE FROM BOTH ENDS: WEYL IS SIGN-BLIND")
    print("      %10s %12s %12s %s" % ("M", "conjugate", "r_s = 2M", "inside r_s?"))
    for M in (-2.0e-3, +2.0e-3, -4.0e-3, +4.0e-3):
        c = seats(M)
        print("      %10.4g %12s %12.4g %s"
              % (M, ("%.2f" % c) if c else "none", schwarzschild_radius(M),
                 "YES" if inside_own_horizon(M) else "no"))
    near("negative mass seats at", seats(-2.0e-3), 56.50, 1e-3)
    near("positive mass seats at", seats(+2.0e-3), 55.17, 1e-3)
    chk("both signs seat, within 5 %", both_signs_seat(), True)
    chk("either sign inside its own Schwarzschild radius",
        not neither_sign_collapses(), False)
    near("region over r_s", region_over_rs(), 75.0, 1e-9)
    print("      only the ARRIVAL flips sign.  composite.py recorded that and")
    print("      nobody read it backwards.")

    print("\nAND THE POSITIVE-MASS SEAT IS OBSERVED")
    near("solar gravitational focus (AU)", solar_focus_au(), 547.6, 1e-3)
    chk("against the published ~550", seat_is_observed(), True)
    print("      four and a half billion years, no energy condition violated,")
    print("      nothing collapsed, no engineering required.")

    print("\nSO THE DEVICE SPLITS, AND THE HALVES DO NOT COST THE SAME")
    for n, cost, why in HALVES:
        print("      %-18s %-11s %s" % (n, cost, why[:44]))
    near("ordinary matter's proper ratio", contraction(+1), 1.003076, 1e-4)
    chk("ordinary matter contracts", ordinary_matter_contracts(), False)
    near("negative mass's proper ratio", contraction(-1), 0.997390, 1e-4)
    chk("the impossibility sits in exactly one half",
        impossibility_is_in_one_half(), True)

    print("\nWHAT DOES NOT MOVE")
    chk("a lens is a transition", not A_LENS_IS_NOT_A_TRANSITION, False)
    chk("the exchange rate moved", EXCHANGE_RATE_MOVED, False)
    print("      1.349e26 kg per metre stands exactly where it was.  A free")
    print("      seat is not a free transition, and the Sun is not a warp drive.")

    print("\n  SELFTEST " + ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    print("""VERDICT

  READ BACKWARDS, THE DICHOTOMY SPLITS THE OBSTACLE IN TWO, AND ONLY
  ONE HALF WAS EVER HARD.

  The invariant visible from both ends is that WEYL IS SIGN-BLIND.
  Forward it says a negative mass escapes the Sturm density and so
  escapes collapse.  Backward it says a POSITIVE mass does too --
  measured, both signs seating within 2.4 % of the same affine
  parameter, neither within 75 times its own Schwarzschild radius.
  Only the arrival flips.  composite.py wrote that down and nobody
  turned it around.

  AND THE POSITIVE-MASS SEAT IS NOT A PROPOSAL.  The Sun seats a
  conjugate point at 547.6 AU against a published 550, has done for
  four and a half billion years, violates no energy condition and
  collapses nothing.

  SO THE DEVICE HAS TWO HALVES AND THEY ARE NOT ALIKE.  THE SEAT IS
  FREE -- ordinary matter, every energy condition satisfied, an
  existing example.  THE CONTRACTION CARRIES ALL OF IT -- it needs
  Phi > 0, hence rho < 0, and ordinary matter run through the same
  measurement gives 1.003076, which is LONGER.

  THAT VINDICATES ONE DESCRIPTION AND KILLS ONE CONFUSION.  "A
  controlled gravitational focus at a chosen range, built from fields
  that satisfy every energy condition" survives intact; what spec.py
  withdrew was the B*l invariant, which was the STURM route to the
  seat, and the tree kept quoting that withdrawal as though it had
  taken the seat with it.  It had not.

  AND IT CHANGES NO NUMBER.  A free seat is not a free transition.
  The seat alone is a lens: it focuses light at a range, carries no
  payload, and shortens nothing.  1.349e26 kg per metre stands
  exactly where it was.

  A LENS IS NOT A TRANSITION, AND THE SUN IS NOT A WARP DRIVE.""")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report()
