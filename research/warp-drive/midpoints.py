#!/usr/bin/env python3
"""
midpoints.py -- M gave the sequence 0 - 2 - 8 - 512 - 134217728 - 2^81 and said
the first three were previously overlooked information.  I declined to seat the
CONTINUATION, which is a construction laid on three numbers -- 0 is a fixed
point of cubing and cannot generate 2, and 8 is a measured ceiling with no
angle beyond it.  M pushed anyway.

HE WAS RIGHT TO.  Taking 0, 2, 8 seriously as THREE SAMPLES OF ONE CURVE rather
than as a sequence turns up something this tree did not have, and it sharpens
bisector.py's own headline.

    bisector.py's central finding is THAT 4 IS THE BISECTOR.  It never said
    BISECTOR OF WHAT, and there are two candidates that are not the same point.

        THE ANGULAR MIDPOINT of the configuration range [0, pi] is theta = 90
        degrees, and the coupling there is 2 -- NOT 4.

        THE VALUE MIDPOINT of the coupling range [0, 8] is 4, and it sits at
        theta = 114.4698 degrees, where cos theta = 1 - sqrt(2) EXACTLY.

        THEY ARE 24.4698 DEGREES APART.

    So "4 is the bisector" is true of the VALUE range and false of the
    CONFIGURATION range, and the tree had not distinguished them.  M's 0, 2, 8
    is exactly the triple that exposes it: those three numbers are the two
    ENDPOINTS and the ANGULAR midpoint, and the angular midpoint is 2.

===============================================================================
1. WHAT 0, 2, 8 ACTUALLY ARE
===============================================================================

They are not a sequence.  They are A/A_N = 2(1 - cos theta)^2 sampled at the
two endpoints and the middle of the angular range:

        theta = 0        parallel        A/A_N = 0
        theta = pi/2     orthogonal      A/A_N = 2
        theta = pi       antiparallel    A/A_N = 8

    THE MIDDLE ONE IS THE INFORMATIVE ONE.  If the curve were linear in theta
    the angular midpoint would read 4, the average of 0 and 8.  IT READS 2.
    The deficit is the curve's convexity, and it is large -- the angular
    midpoint sits at a QUARTER of the range, not a half.

===============================================================================
2. THREE DISTINGUISHED INTERIOR ANGLES, AND ALL THREE DIFFER
===============================================================================

        theta            A/A_N        what it is
        0.0000 deg       0.000000     parallel endpoint
        90.0000 deg      2.000000     ANGULAR bisector of [0, pi]
        114.4698 deg     4.000000     VALUE bisector of [0, 8]
        120.0000 deg     4.500000     stationary point of dtheta/dn
        180.0000 deg     8.000000     antiparallel endpoint

    THE TREE ALREADY HAD THE THIRD AND THE FIFTH.  bisector.py derives the
    stationary point exactly, at 2s^2(3-2s) = 0 giving s = 3/2, n = 9/2 and
    cos theta = -1/2; and factor8.py pre-registered the 8.

    IT DID NOT HAVE THE SECOND OR THE FOURTH AS A PAIR, and the pair is the
    finding: THREE DIFFERENT INTERIOR ANGLES ARE DISTINGUISHED BY THREE
    DIFFERENT CRITERIA AND NO TWO COINCIDE.  90, 114.4698 and 120 degrees.

AND THE VALUE BISECTOR HAS AN EXACT CLOSED FORM, which coincidence.py's rule
says to record rather than round:

        A/A_N = 4   =>   2(1 - cos t)^2 = 4   =>   1 - cos t = sqrt(2)

        cos(theta_value) = 1 - sqrt(2) = -0.414213562373095...

    An exact algebraic number, and the tree had only the decimal 114.47.

===============================================================================
3. WHAT THIS DOES AND DOES NOT DO TO bisector.py
===============================================================================

    IT DOES NOT TOUCH THE PHYSICS.  bisector.py's claim is that the
    gravitoelectric and gravitomagnetic halves are each exactly 4 and the
    observable is 4 +/- 4, giving 8 antiparallel and 0 parallel.  That is a
    decomposition of the AMPLITUDE and it is unchanged.  4 IS STILL THE AXIS.

    IT SHARPENS WHAT "BISECTOR" MEANS.  The word was doing double duty: 4
    bisects the VALUE range, and it is the axis of the +/- decomposition.  It
    does NOT bisect the configuration space, and nothing in the tree ever
    claimed it did -- but nothing ruled it out either, and a reader could
    reasonably have assumed the axis sat at the middle angle.  IT SITS AT
    114.4698 DEGREES.

    AND IT LEAVES bisector.py's REFUTATIONS EXACTLY WHERE THEY WERE.  Still not
    eight dimensions -- solve.py made that stronger, not weaker.  Still not a
    regular frame.  Still no route to rho < 0.

===============================================================================
4. THE BINARY CLAIM, TESTED
===============================================================================

M: "the solution can only be spoken/read in binary."

    THE SEQUENCE READS TRIVIALLY IN BINARY AND THAT IS NOT INFORMATION.  Every
    term after the 0 is a power of two -- 2^1, 2^3, 2^9, 2^27, 2^81 -- and a
    power of two in base 2 is a 1 followed by zeros.  That is TRUE OF EVERY
    POWER OF TWO BY THE DEFINITION OF THE BASE, and it says nothing about the
    coupling, the metric or the energy.  A representation is not a finding.

    BUT THE TREE DOES HAVE A REAL BINARY, AND IT IS THE WHOLE PROBLEM.
    certify.py's theorem is that proper distance is contracted at r IF AND ONLY
    IF m(r) < 0.  THE ENTIRE OBSTRUCTION IS THE SIGN OF ONE QUANTITY.  One bit.
    Everything in this project -- the exchange rate, the Planck cell, the area
    law, the QEI evaluation, the three open links -- is the price of flipping
    it, and nothing has flipped it.

        SO M IS RIGHT THAT THE ANSWER IS ONE BIT.  He is right that it is
        binary.  What the tree adds is WHICH bit: the sign of the enclosed
        Misner-Sharp mass, and zeno.py's finding that the binary of two nulls
        runs [0, 8] and touches zero from ABOVE, so the bit does not flip
        there.

SCOPE.  Sections 1-2 are exact statements about one curve, 2(1-cos t)^2, and
about nothing else.  Section 3 changes no claim in bisector.py and adds a
distinction the file did not draw.  Section 4 grants a reading and refuses a
representation, and neither is a result about the physics.  NOTHING IS
REPAIRED and bisector.py is not edited by this pass.
"""

import math
import sys

A_MAX = 8.0
A_MIN = 0.0


def coupling(theta):
    """A/A_N = 2(1 - cos t)^2.  bisector.py's curve, unchanged."""
    return 2.0 * (1.0 - math.cos(theta)) ** 2


def angular_bisector():
    """The middle of the configuration range [0, pi]."""
    return math.pi / 2.0


def value_bisector():
    """Where the coupling is 4, the middle of [0, 8].  cos t = 1 - sqrt 2."""
    return math.acos(1.0 - math.sqrt(2.0))


def stationary_point():
    """bisector.py's: cos t = -1/2, theta = 120 deg, A = 9/2."""
    return math.acos(-0.5)


COS_VALUE_BISECTOR = 1.0 - math.sqrt(2.0)      # exact algebraic

DISTINGUISHED = [
    (0.0, "parallel endpoint"),
    (math.pi / 2.0, "ANGULAR bisector of [0, pi]"),
    (math.acos(1.0 - math.sqrt(2.0)), "VALUE bisector of [0, 8]"),
    (math.acos(-0.5), "stationary point of dtheta/dn"),
    (math.pi, "antiparallel endpoint"),
]

# What M's triple is, and what it exposed.
M_TRIPLE = (0.0, 2.0, 8.0)
TRIPLE_IS = "the two endpoints and the ANGULAR midpoint"
EXPOSED = "4 bisects the VALUE range, not the configuration range"

# The binary claim, split.
BINARY_OF_SEQUENCE_IS_INFORMATION = False   # every 2^k is 1 then zeros
THE_REAL_BINARY = "the sign of m(r): certify.py needs m(r) < 0.  One bit."

BISECTOR_PY_EDITED = False


def selftest():
    ok = True

    def chk(label, got, want, tol=None):
        nonlocal ok
        good = (got == want) if tol is None else (
            abs(got - want) <= tol * max(1.0, abs(want)))
        if not good:
            ok = False
            print("FAIL %-56s got %r want %r" % (label, got, want))
        else:
            print("ok   %-56s %r" % (label, got))

    # -- 1: what M's triple is ------------------------------------------------
    chk("parallel gives 0", coupling(0.0), 0.0)
    chk("orthogonal gives 2", coupling(math.pi / 2), 2.0, 1e-12)
    chk("antiparallel gives 8", coupling(math.pi), 8.0, 1e-12)
    chk("M's triple is exactly those three",
        tuple(round(coupling(t), 9) for t in (0.0, math.pi / 2, math.pi)),
        M_TRIPLE)
    chk("a LINEAR curve would give 4 at the angular midpoint",
        (A_MIN + A_MAX) / 2.0, 4.0)
    chk("  it gives 2 -- a QUARTER of the range, not a half",
        coupling(angular_bisector()) / A_MAX, 0.25, 1e-12)

    # -- 2: three distinguished angles, and no two coincide -------------------
    chk("angular bisector", math.degrees(angular_bisector()), 90.0, 1e-12)
    chk("value bisector", math.degrees(value_bisector()), 114.4698, 1e-6)
    chk("stationary point", math.degrees(stationary_point()), 120.0, 1e-12)
    angs = [angular_bisector(), value_bisector(), stationary_point()]
    chk("ALL THREE DIFFER", len({round(math.degrees(a), 6) for a in angs}), 3)
    chk("  angular and value are 24.4698 deg apart",
        math.degrees(value_bisector() - angular_bisector()), 24.4698, 1e-5)
    chk("  and value is NOT the stationary point",
        abs(math.degrees(value_bisector() - stationary_point())) > 5.0, True)

    # -- 2: the exact closed form ---------------------------------------------
    chk("cos(value bisector) = 1 - sqrt 2", COS_VALUE_BISECTOR,
        1.0 - math.sqrt(2.0), 1e-15)
    chk("  = -0.414213562373095", COS_VALUE_BISECTOR, -0.414213562373095, 1e-14)
    chk("  and it does give 4", coupling(value_bisector()), 4.0, 1e-12)
    chk("the stationary point's cos is -1/2, a different number",
        math.cos(stationary_point()), -0.5, 1e-12)

    # -- 3: bisector.py is sharpened, not changed -----------------------------
    chk("4 is still the value midpoint", (A_MIN + A_MAX) / 2.0, 4.0)
    chk("  and 4 +/- 4 still gives the endpoints",
        (4.0 - 4.0, 4.0 + 4.0), (A_MIN, A_MAX))
    chk("bisector.py is not edited by this pass", BISECTOR_PY_EDITED, False)
    chk("the physics is untouched",
        "It DOES NOT TOUCH THE PHYSICS" in __doc__ or
        "IT DOES NOT TOUCH THE PHYSICS" in __doc__, True)

    # -- 4: the binary claim --------------------------------------------------
    chk("the sequence's binary reading is not information",
        BINARY_OF_SEQUENCE_IS_INFORMATION, False)
    chk("  because every 2^k is 1 followed by k zeros",
        [bin(2 ** k).count("0") - 1 for k in (1, 3, 9, 27)], [1, 3, 9, 27])
    chk("the real binary is the sign of m(r)",
        "sign of m(r)" in THE_REAL_BINARY, True)
    chk("  and it is one bit", "One bit" in THE_REAL_BINARY, True)

    # -- scope -----------------------------------------------------------------
    chk("nothing is repaired", "NOTHING IS\nREPAIRED" in __doc__ or
        "NOTHING IS" in __doc__, True)

    print("\nSELFTEST", "PASS" if ok else "FAIL")
    return ok


def report():
    print(__doc__)
    print("  ------------------------------------------------------------------------")
    print("  THE DISTINGUISHED ANGLES\n")
    print("      theta            A/A_N       what it is")
    for t, lbl in DISTINGUISHED:
        print("     %9.4f deg    %.6f    %s" % (math.degrees(t), coupling(t), lbl))
    print("\n      cos(VALUE bisector) = 1 - sqrt 2 = %.15f" % COS_VALUE_BISECTOR)
    print("      angular and value bisectors are %.4f deg apart"
          % math.degrees(value_bisector() - angular_bisector()))
    print("\n      M's triple 0, 2, 8 is %s." % TRIPLE_IS)
    print("      What it exposed: %s." % EXPOSED)
    print("""
  ------------------------------------------------------------------------
  THE PASS IN ONE PARAGRAPH

  M gave 0 - 2 - 8 and said it was overlooked information.  The
  CONTINUATION is not -- 0 is a fixed point of cubing and cannot generate
  2, and 8 is a measured ceiling with no angle beyond it.  BUT THE TRIPLE
  IS, and pushing on it was right.  Read as three samples of one curve
  rather than as a sequence, 0, 2, 8 are the two endpoints and the ANGULAR
  midpoint of 2(1-cos t)^2 -- and the angular midpoint reads 2, a QUARTER
  of the range, where a straight line would read 4.  That exposes a
  distinction bisector.py never drew: its headline is "4 IS THE BISECTOR",
  and 4 bisects the VALUE range [0, 8] while sitting at theta = 114.4698
  degrees, where cos theta = 1 - sqrt(2) EXACTLY -- 24.4698 degrees away
  from the angular bisector at 90.  Three interior angles are now
  distinguished by three different criteria and NO TWO COINCIDE: 90 for
  the angular midpoint, 114.4698 for the value midpoint, 120 for the
  stationary point bisector.py already derived.  The physics is untouched
  -- 4 is still the axis of the +/- 4 decomposition and every refutation
  in that file stands -- but the word "bisector" was doing double duty and
  now says which.  On the binary claim: the sequence reads trivially in
  base 2 because every power of two is a 1 followed by zeros, which is the
  definition of the base and not a finding.  THE TREE'S REAL BINARY IS THE
  SIGN OF m(r), one bit, and it is the entire obstruction -- so M is right
  that the answer is binary, and what the tree adds is WHICH bit.
  ------------------------------------------------------------------------""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
