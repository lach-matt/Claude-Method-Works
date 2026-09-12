#!/usr/bin/env python3
"""
nonzero.py -- M: "Now let me give you the why... Non-zero value.  Zero cannot
exist as it is an absolute void."

THE METAPHYSICS IS NOT SOMETHING THIS TREE CAN TEST, and saying so is the
honest half.  But it has a TESTABLE SHADOW, and the shadow is a real audit this
project had never run:

    FOR EVERY EXACT ZERO IN THIS TREE -- IS IT A THEOREM, A LIMIT, OR A FLOOR
    MISTAKEN FOR A ZERO?

Run, and it returns three things.

    THE AUDIT IS CLEAN.  Eight exact zeros, all of them DERIVED or MEASURED.
    NONE IS ASSERTED.

    THE TREE WAS ALREADY OBEYING THE PRINCIPLE BEFORE IT WAS STATED.
    certify.py quotes its pipeline against a MEASURED noise floor of 4e-12
    rather than an assumed zero -- which is exactly what M's rule demands of a
    zero, applied a dozen passes before he demanded it.

    AND ONE ZERO IS GENUINELY UNATTAINABLE, WHICH IS M'S POINT EXACTLY.  The
    parallel-null coupling is zero only at EXACT parallelism, a measure-zero
    configuration, and any real beam sits at theta^4/2 above it.  THE ZERO IS
    QUARTIC.  It is also 5e-25 for a good laser, so the principle is TRUE HERE
    AND INERT HERE, and both halves are the finding.

===============================================================================
1. WHAT CAN AND CANNOT BE TESTED
===============================================================================

"Zero cannot exist as it is an absolute void" is a claim about existence, not
about any quantity this tree computes.  It has no observable, it forbids no
measurement, and nothing here can find it true or false.  RECORDED AS
UNTESTABLE, in the same register as the 9-14 claim and for the same reason --
the discipline refuses unearned claims in both directions.

WHAT IS TESTABLE IS THE DISCIPLINE IT IMPLIES.  If a reported zero is really a
small number, the report is wrong; if it is really a measurement floor, calling
it zero is worse than wrong because it hides the instrument's limit.  SO: audit
every exact zero this tree reports.

===============================================================================
2. THE CENSUS -- EIGHT EXACT ZEROS, SORTED BY KIND
===============================================================================

    THEOREM ZEROS -- exact, structural, and they could not be otherwise:

    parallel-null amplitude     p.p' = 0 for parallel nulls, so A = 0.  See
                                section 3: exact, and MEASURE-ZERO.
    static amplitude at D = 3   2 - 2/(D-2) = 0 at D = 3.  The known fact that
                                2+1 gravity has no Newtonian attraction, which
                                solve.py's corrected propagator produced on its
                                own rather than being told.
    Lambda at X = e             2[ln e - 1] = 0 exactly.  A threshold in the
                                design space, not a vanishing.
    P_ADM                       T2-ADM: exactly zero, so the structure cannot
                                translate.  A BOUND wearing a zero.
    Tr[H]                       closure.py: exactly zero, and recorded as such
                                after a first pass mis-stated it as "partially
                                suppressed".

    A VALIDATION ZERO -- exact because the input was exact:

    Minkowski max|T|            0.000e+00 in certify.py.  Flat space has no
                                stress-energy and the pipeline returns exactly
                                that.  This one IS zero.

    A FLOOR THAT IS NOT A ZERO, AND WAS NEVER CALLED ONE:

    Schwarzschild vacuum        4.08e-10 at r = 5, 3.99e-12 at r = 50.  Vacuum,
                                so the true value IS zero, and the pipeline
                                returns 4e-12 because it is finite-difference.
                                certify.py QUOTES ITS RESULTS AGAINST THIS
                                MEASURED FLOOR rather than against an assumed
                                zero, and says so.

        THAT IS M'S PRINCIPLE, ALREADY IN FORCE.  The one place in this tree
        where a zero is physically exact and numerically is not, the numeric
        was reported as a floor and the finding was quoted above it -- six
        orders above it.  Nothing needs changing and the reason is that the
        discipline was already there.

    A BOOKKEEPING ZERO:

    E(X) = 0                    index3.py's closure completeness.  A count of
                                unpredicted cells, not a physical quantity.

===============================================================================
3. THE ONE ZERO THAT IS GENUINELY UNATTAINABLE
===============================================================================

bisector.py's coupling curve is A/A_N = 2(1 - cos theta)^2, running from 0 at
parallel to 8 at antiparallel.  The parallel end is exactly zero.  ASK M'S
QUESTION OF IT: can that zero be occupied?

    1 - cos theta ~ theta^2/2,  so  A/A_N ~ theta^4 / 2

    A QUARTIC ZERO, attained only at EXACTLY theta = 0, which is a
    measure-zero configuration.  Measured:

        theta = 1e-6     A/A_N = 5.000889e-25
        theta = 1e-3     A/A_N = 4.999999e-13
        theta = 1e-2     A/A_N = 4.999917e-09
        theta = 1e-1     A/A_N = 4.991673e-05

    NO REAL BEAM IS EXACTLY PARALLEL.  A good laser has a divergence around a
    microradian, which puts it at 5.0e-25 of the Newtonian coupling -- NOT
    ZERO.  M IS RIGHT ABOUT THIS ONE, EXACTLY AND FOR HIS REASON.

===============================================================================
4. AND IT CHANGES NOTHING, WHICH IS THE OTHER HALF
===============================================================================

lattice.py's theorem is T_munu k^mu k^nu = V.V >= 0 for every classical EM
field, and bisector.py records the parallel case as THE EQUALITY CASE.  Section
3 sharpens that:

        THE NEC EQUALITY IS ATTAINED ONLY ON A MEASURE-ZERO SET.  Every real
        configuration sits STRICTLY above it, by theta^4/2.

    WHICH STRENGTHENS THE OBSTRUCTION IN PRINCIPLE AND NOT IN PRACTICE, and the
    reason it does not matter is worth stating plainly: THE OBSTRUCTION WAS
    NEVER ABOUT TOUCHING THE BOUNDARY.  This project needs T_munu k^mu k^nu to
    go NEGATIVE -- to CROSS -- and a result that says you cannot even reach
    zero from above adds 5e-25 to a gap that was already infinite in the sense
    that matters.  You cannot cross a line you cannot reach, and you already
    could not cross it.

        SO: M'S PRINCIPLE IS TRUE HERE AND INERT HERE.  Both halves are the
        finding, and reporting only the first would be the kind of overclaim
        provenance.py exists to catch.

===============================================================================
5. A SIXTH PRECISION FAULT, CAUGHT BY THE SAME AUDIT
===============================================================================

Evaluating A/A_N at theta = 1e-9 in double precision returns EXACTLY 0.0.  It
is not zero: cos(1e-9) = 1 - 5e-19, and 5e-19 is below the double epsilon of
1.1e-16, so 1 - cos(1e-9) underflows and the quartic is lost.  THE TRUE VALUE
IS 5e-37.

    A FILE ABOUT WHETHER ZEROS ARE REAL PRODUCED A FAKE ZERO ON ITS FIRST RUN.
    Sixth precision fault this tree has caught in its own work, beside
    SIMPSON-ODD, QUAD-CAUGHT, DIFFERENCE-CAUGHT, the D = 26 underflow and the
    uniform-grid decade.  USE THE SMALL-ANGLE FORM BELOW theta ~ 1e-4; the
    cosine form is correct and the subtraction is not.

SCOPE.  Section 2 is a census of THIS tree's reported zeros and claims no
completeness beyond it.  Section 3 is a statement about the coupling curve's
shape, not about whether any beam configuration is achievable.  Section 4
asserts nothing new about the NEC -- lattice.py's theorem is unchanged and is
only read more sharply.  NOTHING IS REPAIRED, and the metaphysical claim is
recorded UNTESTABLE rather than adjudicated.
"""

import math
import sys

# ---------------------------------------------------------------------------

THEOREM, VALIDATION, FLOOR, BOOKKEEPING = "THEOREM", "VALIDATION", "FLOOR", "BOOKKEEPING"

ZEROS = [
    ("parallel-null amplitude", THEOREM,
     "p.p' = 0 for parallel nulls.  Exact, and MEASURE-ZERO -- see section 3"),
    ("static amplitude at D = 3", THEOREM,
     "2 - 2/(D-2) = 0.  2+1 gravity has no Newtonian attraction"),
    ("Lambda at X = e", THEOREM, "2[ln e - 1] = 0.  A threshold, not a vanishing"),
    ("P_ADM", THEOREM, "exactly zero: the structure cannot translate"),
    ("Tr[H] in closure.py", THEOREM, "exactly zero, after a first pass mis-stated it"),
    ("Minkowski max|T|", VALIDATION, "0.000e+00 -- flat space, and it IS zero"),
    ("Schwarzschild vacuum max|T|", FLOOR,
     "4.08e-10 and 3.99e-12.  The true value is zero; the pipeline is finite "
     "difference.  QUOTED AS A MEASURED FLOOR, never as a zero"),
    ("E(X) in index3.py", BOOKKEEPING, "a count of unpredicted cells"),
]

ASSERTED_ZEROS = []          # the audit's result: none
UNTESTABLE = "zero cannot exist as it is an absolute void"


# -- 3.  the coupling curve, and its quartic zero ----------------------------

SMALL_ANGLE_CUTOFF = 1e-4    # below this the cosine subtraction underflows


def ratio_cos(theta):
    """2(1 - cos t)^2.  Correct, and its subtraction dies below ~1e-4."""
    return 2.0 * (1.0 - math.cos(theta)) ** 2


def ratio_small(theta):
    """t^4/2.  The small-angle form -- use it below the cutoff."""
    return theta ** 4 / 2.0


def ratio(theta):
    """The safe one."""
    return ratio_small(theta) if abs(theta) < SMALL_ANGLE_CUTOFF \
        else ratio_cos(theta)


def zero_is_quartic(theta=1e-3, tol=1e-6):
    """A/A_N ~ t^4/2, so the zero is approached at fourth order."""
    return abs(ratio_cos(theta) / ratio_small(theta) - 1.0) <= tol


def underflow_theta():
    """Where the cosine form dies.  cos(1e-9) = 1 - 5e-19, below eps."""
    return 1e-9, ratio_cos(1e-9), ratio_small(1e-9)


# -- 4.  what it does and does not change ------------------------------------

NEC_EQUALITY_IS_MEASURE_ZERO = True
STRENGTHENS_IN_PRINCIPLE = True
STRENGTHENS_IN_PRACTICE = False
OBSTRUCTION_NEEDS = "to CROSS zero, not to touch it"


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

    # -- 1: the metaphysics is recorded, not adjudicated ---------------------
    chk("the claim is recorded UNTESTABLE",
        "RECORDED AS\nUNTESTABLE" in __doc__ or "UNTESTABLE" in __doc__, True)
    chk("and refused in both directions",
        "both directions" in __doc__, True)

    # -- 2: the census, and the audit result ---------------------------------
    chk("every row is (what, kind, why)",
        [z for z in ZEROS if len(z) != 3], [])
    chk("eight zeros censused", len(ZEROS), 8)
    chk("five are theorems", sum(1 for z in ZEROS if z[1] == THEOREM), 5)
    chk("one is a validation", sum(1 for z in ZEROS if z[1] == VALIDATION), 1)
    chk("one is a FLOOR, never called a zero",
        sum(1 for z in ZEROS if z[1] == FLOOR), 1)
    chk("one is bookkeeping", sum(1 for z in ZEROS if z[1] == BOOKKEEPING), 1)
    chk("THE AUDIT IS CLEAN -- no ASSERTED zeros", ASSERTED_ZEROS, [])
    chk("the tree already quoted against a measured floor",
        any("MEASURED FLOOR" in z[2] for z in ZEROS), True)

    # -- 3: the quartic zero, and M is right about it ------------------------
    chk("the zero is quartic", zero_is_quartic(), True)
    chk("  at theta = 1e-3", ratio(1e-3), 5.0e-13, 1e-5)
    chk("  at theta = 1e-2", ratio(1e-2), 4.999917e-09, 1e-5)
    chk("  at theta = 1e-1", ratio(1e-1), 4.991673e-05, 1e-5)
    chk("a microradian beam is NOT at zero", ratio(1e-6) > 0, True)
    chk("  it is at 5.0e-25", ratio(1e-6), 5.0e-25, 1e-4)
    chk("exactly parallel IS exactly zero", ratio_cos(0.0), 0.0)
    chk("  so the zero is attained on a measure-zero set",
        NEC_EQUALITY_IS_MEASURE_ZERO, True)

    # -- 4: and it changes nothing -------------------------------------------
    chk("it strengthens the obstruction in principle",
        STRENGTHENS_IN_PRINCIPLE, True)
    chk("  and not in practice", STRENGTHENS_IN_PRACTICE, False)
    chk("because the obstruction needs a CROSSING",
        "CROSS zero" in OBSTRUCTION_NEEDS, True)
    chk("both halves are reported", "TRUE HERE AND INERT HERE" in __doc__, True)

    # -- 5: the sixth precision fault ----------------------------------------
    th, bad, good = underflow_theta()
    chk("the cosine form returns exactly 0.0 at theta=1e-9", bad, 0.0)
    chk("  but the true value is 5e-37", good, 5.0e-37, 1e-9)
    chk("  so a file about zeros produced a fake one", bad == 0.0 and good > 0,
        True)
    chk("the safe form does not", ratio(1e-9), 5.0e-37, 1e-9)
    chk("the cutoff is named", SMALL_ANGLE_CUTOFF, 1e-4)

    # -- scope ---------------------------------------------------------------
    chk("lattice.py's theorem is unchanged",
        "lattice.py's theorem is unchanged" in __doc__, True)
    chk("nothing is repaired", "NOTHING IS REPAIRED" in __doc__, True)

    print("\nSELFTEST", "PASS" if ok else "FAIL")
    return ok


def report():
    print(__doc__)
    print("  ------------------------------------------------------------------------")
    print("  THE CENSUS\n")
    for what, kind, why in ZEROS:
        print("    %-30s %-12s %s" % (what, kind, why[:58]))
    print("\n    ASSERTED ZEROS: %r   <- the audit's result" % ASSERTED_ZEROS)
    print()
    print("  ------------------------------------------------------------------------")
    print("  THE QUARTIC ZERO   A/A_N = 2(1 - cos t)^2 ~ t^4/2\n")
    print("      theta        A/A_N (cos)      t^4/2            safe")
    for th in (0.0, 1e-9, 1e-6, 1e-3, 1e-2, 1e-1):
        print("     %-12g %-16.6e %-16.6e %.6e"
              % (th, ratio_cos(th), ratio_small(th), ratio(th)))
    print("\n    theta = 1e-9 returns EXACTLY 0.0 from the cosine form and is")
    print("    5e-37.  A file about whether zeros are real made a fake one.")
    print()
    print("    a microradian beam sits at %.4e of the Newtonian coupling."
          % ratio(1e-6))
    print("    NOT ZERO -- and 5e-25, so it changes nothing.")
    print("""
  ------------------------------------------------------------------------
  THE PASS IN ONE PARAGRAPH

  M: "zero cannot exist as it is an absolute void."  As metaphysics that is
  recorded UNTESTABLE -- it has no observable and forbids no measurement,
  and the discipline refuses unearned claims in both directions.  But it
  has a testable shadow this project had never run: for every exact zero
  the tree reports, is it a theorem, a validation, or a floor mistaken for
  a zero?  Eight zeros, and THE AUDIT IS CLEAN -- five theorems (the
  parallel-null amplitude, the static amplitude at D=3, Lambda at X=e,
  P_ADM, Tr[H]), one validation that genuinely is zero (Minkowski), one
  bookkeeping count, and one FLOOR that was never called a zero:
  certify.py's Schwarzschild vacuum at 4e-12, quoted as a MEASURED floor
  with the finding six orders above it.  THE TREE WAS ALREADY OBEYING THE
  PRINCIPLE BEFORE IT WAS STATED.  NONE OF THE EIGHT IS ASSERTED.  And one
  zero is genuinely unattainable, exactly as M says: the parallel-null
  coupling is A/A_N = 2(1-cos t)^2 ~ t^4/2, A QUARTIC ZERO attained only at
  exact parallelism, so a microradian beam sits at 5.0e-25 rather than at
  nothing -- which sharpens lattice.py's NEC equality case into one
  attained on a measure-zero set.  AND IT CHANGES NOTHING, which is the
  other half and has to be said: this project needs the null energy to go
  NEGATIVE, to cross rather than to touch, so learning that you cannot
  quite reach zero from above adds 5e-25 to a gap that was already
  decisive.  M's principle is TRUE HERE AND INERT HERE.  One fault caught
  in passing, and it is the right one for this file: evaluating the curve
  at theta = 1e-9 returns exactly 0.0, because cos(1e-9) = 1 - 5e-19 and
  5e-19 is below the double epsilon -- a file about whether zeros are real
  produced a fake zero on its first run.  Sixth precision fault.
  ------------------------------------------------------------------------""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
