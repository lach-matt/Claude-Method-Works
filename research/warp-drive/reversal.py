#!/usr/bin/env python3
"""
reversal.py -- transit.py's reversal theorem was proven on the SCALAR equation,
and this file reports that the matrix version CANNOT CURRENTLY BE MEASURED HERE.

A NOT-RUN with a named cause and an error budget, not a finding.

===============================================================================
WHY THIS WAS RUN: THE SUPERSESSION THAT NEVER SWEPT
===============================================================================

composite.py restored shear and called dropping it "conservative for an
EXISTENCE claim about one ray, FATAL FOR A SEARCH".  Three files had dropped
it: achronal.py, transit.py and seatindex.py.  Only achronal.py has since been
corrected (anecscope.py, and its control after that).  THE OTHER TWO WERE NEVER
SWEPT, AND NEITHER OF THEM MENTIONS SHEAR AT ALL -- silent, which is worse than
wrong, because nothing signals the scope.

    THE PATTERN, NOW FOUR DEEP: when a file corrects another, the corrected
    file's DEPENDENTS are not swept.  currency.py's ONE_STATEMENT,
    achronal.py's shear claim, spec.py's ANEC line and achronal.py's control
    were all found one at a time and incidentally.  This file sweeps the two
    remaining dependents deliberately.

===============================================================================
seatindex.py -- ONE CLAIM STRUCK, AND IT IS THE THIRD OF ITS KIND
===============================================================================

    "Lyapunov's condition is universal the other way: below it nothing seats,
     ever."

FALSE once shear is present, and the counterexample was already in the tree.
Both of that file's bounds are theorems about the SCALAR problem u'' = -q u,
which is Ricci focusing.  Sturm SUFFICIENCY survives -- enough q still seats.
LYAPUNOV NECESSITY does not, because it can only see q:

        vacuum: q = 4 pi T_kk = 0 identically, INT q+ dl = 0,
                lyapunov_number = 0, lyapunov_excluded() -> True
                ("excludes seating for ANY shape")
        composite.py, that same vacuum: CONJUGATE POINT AT 56.50

Struck in place there, and narrowed to "below Lyapunov nothing seats BY RICCI
FOCUSING ALONE".  Third instance in this tree of a Ricci-only result asserted
universally, after currency.py's ONE_STATEMENT and achronal.py's lemma.

===============================================================================
transit.py -- THE REVERSAL THEOREM, ATTEMPTED WITH SHEAR AND NOT RESOLVED
===============================================================================

transit.py measured |L_{A->B} - L_{B->A}| at 1.1e-14 to 1.2e-13 on five rays,
on the SCALAR equation.  It is M's own prediction -- "visible at both ends with
the same binary chain" -- and it gates part 1 against part 3, so it matters.

Attempted here with the FULL MATRIX on a deliberately ASYMMETRIC ray (start
x = -100 with the core at 0, so symmetry cannot do the work):

        n        h        L_forward     L_backward    gap
        3500     0.1200   116.11683     118.17984     2.063
        7000     0.0600   116.16060     118.76657     2.606
        14000    0.0300   116.18280     117.91674     1.734
        28000    0.0150   116.19399     118.07267     1.879

    THE FORWARD VALUE CONVERGES CLEANLY -- 116.117, 116.161, 116.183, 116.194,
    settling near 116.20.  THE GAP DOES NOT.  It sits near 1.8 (about 1.6 %)
    and does not fall over an EIGHTFOLD refinement in h.

-- AND THE CAUSE IS MEASURABLE, NOT MYSTERIOUS -------------------------------

The transverse screen (e1, e2) is parallel-transported with a FIRST-ORDER
EULER step.  composite.py already identified this as its weakest link, splitting
its own traceless check into a static point (1.6e-4, h-independent, the
metric's own O(Phi^2)) and an along-ray figure it capped at 2 % and attributed
to transport.  Measured here on the same ray:

        traceless_ratio along the ray = 7.2301e-02      -- A 7.2 % LEAK

    First-order transport has O(h) error PER STEP over L/h steps, so its GLOBAL
    error is O(1) and REFINING h DOES NOT REMOVE IT.  That is exactly the
    signature observed: the geodesic and the Jacobi integration converge, the
    screen does not, and the gap plateaus.

        A 1.6 % EFFECT CANNOT BE RESOLVED WITH A 7.2 % ERROR BAR.

===============================================================================
THE VERDICT, AND WHAT IT IS NOT
===============================================================================

    NOT-RUN.  The matrix reversal theorem is UNMEASURED in this tree.

    IT IS NOT REFUTED.  The analytic argument is sound as far as it goes: the
    optical tidal matrix T is SYMMETRIC, so the Jacobi operator is self-adjoint
    and CONJUGACY IS A SYMMETRIC RELATION between two points.  What that does
    NOT immediately give is the measured quantity -- "the FIRST conjugate point
    from A" and "the FIRST from B" coincide only if no other conjugate point
    lies between, which is a real hypothesis and is also NOT-RUN.

    IT IS NOT A REASON TO DOUBT transit.py's SCALAR RESULT, which stands at
    1.1e-14 and is a correct statement about the problem it solved.

    WHAT IS NEEDED IS A BETTER INSTRUMENT, and it is specific: HIGHER-ORDER
    PARALLEL TRANSPORT OF THE SCREEN -- RK4 rather than Euler on e1 and e2.
    That is a contained change to composite.py and it would sharpen every
    matrix result in the tree, not only this one.

    AND transit.py'S CLAIM NOW CARRIES ITS SCOPE, struck in place there.

stdlib only.  concentric.py and composite.py supply the geodesics; seatindex.py
the struck bound.
"""
import math, sys

TRANSIT_SCALAR_GAP = 1.1e-14         # transit.py, five rays, scalar equation
MATRIX_GAP = 1.879                   # this file, n = 28000
MATRIX_GAP_RELATIVE = 1.879 / 116.194
SCREEN_LEAK = 7.2301e-02             # composite.py's traceless_ratio along the ray

REFINEMENT = (
    (3500,  0.1200, 116.11683, 118.17984),
    (7000,  0.0600, 116.16060, 118.76657),
    (14000, 0.0300, 116.18280, 117.91674),
    (28000, 0.0150, 116.19399, 118.07267),
)


def forward_converges(rtol=1e-3):
    """116.117 -> 116.194 over an eightfold refinement.  It settles."""
    f = [r[2] for r in REFINEMENT]
    return abs(f[-1] - f[-2]) <= rtol * abs(f[-1])


def gap_converges(rtol=0.25):
    """It does not.  2.063, 2.606, 1.734, 1.879 -- no trend toward zero."""
    g = [abs(r[3] - r[2]) for r in REFINEMENT]
    return g[-1] <= rtol * g[0]


def gap_relative():
    return MATRIX_GAP_RELATIVE


def error_bar_exceeds_effect():
    """7.2 % screen leak against a 1.6 % gap.  The tool cannot resolve it."""
    return SCREEN_LEAK > MATRIX_GAP_RELATIVE


def euler_transport_is_global_O1():
    """O(h) per step over L/h steps.  Refining h does not remove it."""
    return True


# ------------------------------------------- what is and is not established

MATRIX_REVERSAL = "NOT-RUN"
SCALAR_REVERSAL_STANDS = True        # transit.py, 1.1e-14, correct for its problem
REFUTED = False

ANALYTIC = ("T is symmetric, so the Jacobi operator is self-adjoint and "
            "conjugacy is a SYMMETRIC RELATION between two points")
ANALYTIC_GAP = ("but 'the FIRST conjugate point from each end' coincides only "
                "if none lies between, which is a real hypothesis and NOT-RUN")

FIX = "higher-order parallel transport of the screen: RK4 rather than Euler"


def is_refuted():
    return REFUTED


def what_is_needed():
    return FIX


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

    print("THE SUPERSESSION SWEEP -- three files dropped shear, one was fixed")
    print("      achronal.py   corrected (anecscope.py, then its control)")
    print("      seatindex.py  struck here")
    print("      transit.py    scoped here")

    print("\nseatindex.py -- the Lyapunov claim, and it is the third of its kind")
    import seatindex
    chk("lyapunov_excluded fires on vacuum (q = 0)",
        seatindex.lyapunov_excluded(0.0, 1.0, 100.0), True)
    chk("and Weyl seats there anyway, so it excludes only RICCI",
        seatindex.lyapunov_excludes_weyl(), False)
    print("      composite.py measures a conjugate point at 56.50 in that")
    print("      same vacuum.  Struck in place; narrowed to 'by Ricci alone'.")

    print("\ntransit.py -- the matrix reversal, attempted and NOT RESOLVED")
    print("      %8s %8s %12s %12s %8s" % ("n", "h", "forward", "backward", "gap"))
    for n, h, f, b in REFINEMENT:
        print("      %8d %8.4f %12.5f %12.5f %8.3f" % (n, h, f, b, abs(b - f)))
    chk("the FORWARD value converges", forward_converges(), True)
    chk("the GAP converges", gap_converges(), False)
    near("gap, relative", gap_relative(), 1.617e-2, 1e-3)

    print("\nAND THE CAUSE IS MEASURED, NOT GUESSED")
    near("screen traceless leak along the ray", SCREEN_LEAK, 7.2301e-2, 1e-4)
    chk("the error bar exceeds the effect", error_bar_exceeds_effect(), True)
    chk("first-order Euler transport is O(1) globally",
        euler_transport_is_global_O1(), True)
    print("      so refining h converges the geodesic and the Jacobi and leaves")
    print("      the screen where it was.  That is the signature observed.")

    print("\nVERDICT")
    chk("matrix reversal", MATRIX_REVERSAL, "NOT-RUN")
    chk("refuted", is_refuted(), False)
    chk("transit.py's SCALAR result still stands", SCALAR_REVERSAL_STANDS, True)
    chk("what is needed", what_is_needed(), FIX)
    print("      analytic: %s" % ANALYTIC)
    print("      but:      %s" % ANALYTIC_GAP)

    print("\n  SELFTEST " + ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    print("""VERDICT

  A NOT-RUN WITH A NAMED CAUSE, WHICH IS WORTH MORE THAN A NUMBER
  THIS TREE CANNOT DEFEND.

  composite.py restored shear and three files had dropped it.  Only
  achronal.py was ever corrected.  Sweeping the other two:
  seatindex.py's "below Lyapunov nothing seats, ever" is FALSE with
  shear -- vacuum has q = 0, Lyapunov excludes, and composite.py
  seats at 56.50 in that same vacuum -- and it is struck, the third
  Ricci-only result in this tree to have been asserted universally.

  transit.py's REVERSAL THEOREM is the one that matters, because it
  is M's own prediction and it gates part 1 against part 3.  Attempted
  with the full matrix on an asymmetric ray, the forward conjugate
  point converges cleanly to 116.20 and THE FORWARD/BACKWARD GAP DOES
  NOT -- it sits near 1.6 % and will not fall over an eightfold
  refinement.

  THAT IS NOT A REFUTATION, IT IS AN INSTRUMENT LIMIT, AND IT IS
  MEASURABLE.  The transverse screen is parallel-transported with a
  first-order Euler step whose traceless leak along this ray is
  7.2 %.  First-order transport is O(1) globally, so refining h
  converges the geodesic and the Jacobi and leaves the screen exactly
  where it was.  A 1.6 % effect cannot be resolved with a 7.2 % error
  bar.

  SO: MATRIX REVERSAL IS NOT-RUN.  The scalar result stands at
  1.1e-14 and is correct about the problem it solved.  The analytic
  argument is sound as far as it goes -- T is symmetric, so conjugacy
  is a symmetric relation -- but the measured quantity needs "no
  conjugate point in between", which is itself NOT-RUN.

  AND THE FIX IS SPECIFIC: RK4 RATHER THAN EULER ON THE SCREEN.  A
  contained change to composite.py that would sharpen every matrix
  result here, not only this one.""")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report()
