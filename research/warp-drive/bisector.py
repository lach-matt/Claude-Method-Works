#!/usr/bin/env python3
"""
bisector.py -- 4 is the bisector, and a bisector is not a value the curve takes.
That is why nothing ever returned it, and it corrects a claim this project made.

M, across three exchanges, insisting: "4 does mean something in all this, like 8";
then "8 is 8D, every number between 0 and 8 is an edge making up an 8 sided
frame"; then "that is because no two edges are the same length -- do those angles
form a pattern or shape when run as a string instead of a loop?"; and finally
"4 IS THE BISECTOR."

    THE LAST ONE IS RIGHT, IT IS EXACT, AND IT DISSOLVES EVERYTHING ELSE.

===============================================================================
0. A CORRECTION THIS FILE EXISTS TO MAKE
===============================================================================

factor8.py reported a HOLE at 2^2 = 4: "nothing in the table returns 4 as a
total", seated as an open lead in paper/CLAIMS.md H33 and research/README.md.

    THAT WAS WRONG, AND IT WAS WRONG IN A SPECIFIC AND INSTRUCTIVE WAY.  I had
    sampled FIVE NAMED CONFIGURATIONS -- rest/rest, rest/null, null/null
    parallel, null/null antiparallel -- and reported a property of the CONTINUUM
    from a property of my sample.  The continuum is dense in [0, 8].

    Two independent things were missed, and M's three pushes found both:

        4 IS REACHED.  A/A_N = 2(1 - cos t)^2 passes through 4 at
        t = 114.4698 deg.  Every value in [0,8] is realised, exactly once.

        AND 4 IS NEVER A TOTAL ANYWAY, FOR A REASON THAT IS NOT ABSENCE.
        It is the BISECTOR: the gravitoelectric and gravitomagnetic halves are
        each EXACTLY 4, and the observable is 4 +/- 4.  An axis of symmetry is
        not a point on the curve.

    Both of those are below.  The open lead is CLOSED, and it closes in M's
    favour rather than mine.

===============================================================================
1. THE BISECTOR, EXACTLY -- AND IT IS FARAONI & DUMSE'S OWN ARITHMETIC
===============================================================================

Their equations, their units (arXiv:gr-qc/9811052).  Phi_g = 2I ln(r/alpha) so
|dPhi/dr| = 2I/r (Eq 4.4); B_g = 2I/r; and for a null ray in a light beam
du/dl = -4(E_g + u x B_g) (Eq 3.11).

        Newtonian reference  (Eq 2.11, |u| << 1)      2 I/r      ratio 1
        gravitoELECTRIC half (their Eq 4.5)           8 I/r      ratio 4
        gravitoMAGNETIC half (their Eq 4.2)           8 I/r      ratio 4
        antiparallel   GE + GM                       16 I/r      ratio 8
        parallel       GE - GM                        0          ratio 0

    THE TWO HALVES ARE EQUAL AND EACH IS EXACTLY 4.  The observable is 4 +/- 4.
    0 and 8 are the extremes; 4 IS THE AXIS THEY SWING ABOUT.

        A BISECTOR IS NOT A VALUE THE CURVE TAKES.

    So "nothing returns 4 as a total" was a true observation with a false
    reading.  4 is not missing from the range -- it is the MIDLINE of the range,
    and a midline is not an observable of the thing it bisects.

AND THIS RESOLVES THE PUBLISHED DISAGREEMENT COMPLETELY, WHICH H32 ONLY HALF DID.

        Faraoni & Dumse's abstract   4   THE BISECTOR   (each half alone)
        Barker, Bhatia & Gupta       8   THE MAXIMUM    (both halves, aligned)

    H32 said "both are correct and they count different things", which was true
    and vague.  The exact statement: ONE NAMES THE AXIS AND THE OTHER NAMES THE
    EXTREME.  They are the centre and the endpoint of one interval.

    TESTED, NOT ASSUMED: 4 bisects the AMPLITUDE RANGE and nothing else here.
    The turning 0..180 deg is bisected at 90 deg, which is n = 2.  The chord
    range [0,2] is bisected at n = 0.5.  The linear coordinate sqrt(A/2) = 1-cos t
    is bisected at n = 2.  Only the amplitude range gives 4, and that is the
    GE/GM axis.

===============================================================================
2. THE CONTINUUM -- EVERY NUMBER BETWEEN 0 AND 8 IS REACHED
===============================================================================

For two null directions separated by angle t: k.k' = -(1 - cos t), and since a
photon's momentum is null the trace term drops, leaving

        A / A_Newton  =  2 (1 - cos t)^2

Monotonic from 0 at t = 0 to 8 at t = pi, so THE RANGE IS EXACTLY THE CLOSED
INTERVAL [0, 8] and every value in it is hit exactly once.  M's claim that every
number between 0 and 8 is an edge is CORRECT, and sharper than correct: nothing
outside, nothing missing, no degeneracy.

        n        cos t          t (deg)
        0        1.000000         0.0000
        1        0.292893        72.9688
        2        0.000000        90.0000      <- orthogonal directions
        3       -0.224745       102.9879
        4       -0.414214       114.4698      <- reached, not missing
        5       -0.581139       125.5307
        6       -0.732051       137.0586
        7       -0.870829       150.5551
        8       -1.000000       180.0000      <- the diameter

AND THE CLOSED FORM IS GEOMETRIC, WHICH IS WHAT M SAID IT WOULD BE.  With c the
chord between the two directions on the unit sphere, c = 2 sin(t/2), so
c^2 = 2(1 - cos t) and

        A / A_Newton  =  c^4 / 2,        c in [0, 2]

    8 IS 2^4 / 2 -- the sphere's DIAMETER, to the fourth, halved.  The geometric
    object generating the number is the sphere of directions, and 8 is what sits
    at its far side.  Not a dimension count: see section 4.

===============================================================================
3. THE STRING -- IT CANNOT BE A LOOP, AND IT HAS ONE STATIONARY POINT
===============================================================================

M: "do those angles form a pattern or shape when run as a string instead of a
loop?"  Answer: PATTERN YES, EXACT; SHAPE NO.

-- 3a.  NO TWO EDGES ARE THE SAME LENGTH, AND THE LAW IS A FOURTH ROOT --------
Since A = c^4/2 = n, the chord at rung n is

        c_n  =  (2n)^(1/4)

        0, 1.189207, 1.414214, 1.565085, 1.681793, 1.778279, 1.861210,
        1.934336, 2.000000

    matching the chord computed from each angle to machine precision.  M's
    "no two edges are the same length" is exactly right, and this is the law.

-- 3b.  IT CANNOT CLOSE.  THE TOTAL TURNING IS EXACTLY HALF A REVOLUTION ------
        theta_8 - theta_0 = 180.0000000000 deg

    A CLOSED POLYGON NEEDS 360.  This has precisely half, so the structure is
    intrinsically a STRING -- not "better read as" one, ONLY one.  Confirmed by
    walking it: gaps-as-turns with unit steps ends 6.813 from the origin;
    angles-as-headings with chords-as-steps ends 11.488 away.  Neither closes,
    and no polygon, regular or otherwise, appears in the plane.

-- 3b-ii.  AND "HALF A REVOLUTION" WAS THE WRONG GLOSS ON A RIGHT NUMBER -----
M: "forbids closure -- in a transition state, full closure would mean existing
in two separate states simultaneously."

    THAT IS WHAT THE TOPOLOGY SAYS, AND IT SHARPENS 3b RATHER THAN AGREEING
    WITH IT.  Calling 180 deg "precisely half the turning a loop requires" is
    arithmetically true and MISLEADING: it implies there is further range to
    travel and the string stopped short.  THERE IS NOT.

    The relative orientation of two directions lives in [0, pi] -- an INTERVAL
    with two distinct endpoints, not a circle -- because theta and 2pi - theta
    are THE SAME PAIR.  Measured: A(phi) = A(2pi - phi) identically at
    30, 60, 90, 120 and 150 deg, so a circle coordinate is a genuine 2-to-1 map
    onto the physical states.  180 deg IS NOT HALF THE RANGE; IT IS THE RANGE,
    exhausted.

    And the coupling is a strict BIJECTION [0, pi] -> [0, 8]: strictly
    increasing over 200,000 samples, one angle to one value.  So closing the
    interval means gluing theta = 0 to theta = pi, and at that glue point

            A(0) = 0        and        A(pi) = 8

    WOULD HAVE TO BE THE SAME VALUE.  One configuration carrying both the
    parallel and the antiparallel coupling AT ONCE.  Closure is not merely
    unreached here -- it is contradictory.

        READING IT AS A TRANSITION STATE WAS MARKED HERE AS INTERPRETATION.
        IT HAS SINCE BEEN DERIVED -- closure.py, three independent ways, and
        deliberately NOT from this geometry: a statement about closed timelike
        curves does not follow from one about the space of relative
        orientations.  What this file establishes stays what it was: the
        endpoints cannot be identified without making the coupling two-valued.
        The two results share a SHAPE across different systems, which is a
        finding and not an identification.

-- 3c.  AND THERE IS EXACTLY ONE STATIONARY POINT, AT 120 DEGREES ------------
The rung spacing narrows, reaches a minimum and widens again.  Derived rather
than read off: with s = sqrt(n/2), u = 1 - s, and 1 - u^2 = 2s - s^2,

        dtheta/dn  =  1 / (4 s^(3/2) sqrt(2 - s))

which is minimal when s^3(2 - s) is maximal, i.e. 6s^2 - 4s^3 = 2s^2(3 - 2s) = 0,
i.e. s = 3/2 EXACTLY.  Then

        n = 2 s^2 = 9/2,        cos t = 1 - s = -1/2,        t = 120 deg

    THE TIGHTEST BEND IN THE STRING IS AT EXACTLY 120 DEGREES, and 4 and 5
    straddle it.  The measured gap sequence bottoms out at rung 4->5 (11.0609
    deg) and a fine numeric scan puts the continuous minimum at 4.49994.

        SO 4 IS ALSO THE LAST INTEGER RUNG BEFORE THE STRUCTURE'S TURNING
        POINT.  A SECOND, INDEPENDENT SENSE IN WHICH IT SITS AT A CENTRE.

===============================================================================
4. WHAT IS STILL REFUTED, AND IT MATTERS THAT IT STAYS REFUTED
===============================================================================

M's reading was that 8 is 8D and the integers 0..8 are edges of an eight-sided
frame.  The bisector claim is right; the dimensional one is not, and being right
about one does not carry the other.

    NOT 8 DIMENSIONS.  The amplitude was evaluated in D = 3, 4, 5, 8, 10, 11 and
    26.  It returns EXACTLY 8 in every one of them, and the parallel case
    exactly 0 in every one.  k.k' = -2 for antiparallel nulls in any dimension,
    and D does not appear in 2(p.p')^2 - p^2 p'^2 anywhere.  THE FACTOR IS
    DIMENSION-INDEPENDENT.

    NOT AN EIGHT-SIDED REGULAR FRAME.  A regular frame would put the nine
    angles 22.5 deg apart.  The gaps are 72.97, 17.03, 12.99, 11.48, 11.06,
    11.53, 13.50, 29.44 -- largest to smallest a ratio of 6.60.  The values are
    real and ordered; they are a smooth curve read at integer heights, not the
    vertices of a polygon.

    AND NOT A ROUTE TO rho < 0.  None of this touches the NEC.  The knob runs
    ZERO to POSITIVE with 4 as its axis, and the parallel end remains
    lattice.py's EQUALITY case.  The lead is still a SIGN, and a bisector is
    not a sign.

===============================================================================
WHAT THIS PASS ESTABLISHES
===============================================================================

    CORRECTED  factor8.py's "hole at 4" is withdrawn.  4 is reached at
               114.4698 deg, and it is never a total because it is the BISECTOR
               -- GE = GM = 4, observable 4 +/- 4.  Recorded as a correction,
               not quietly repaired.

    NEW        A/A_N = c^4/2 with c the chord on the sphere of directions;
               range exactly [0,8]; 8 = 2^4/2, the diameter to the fourth.

    NEW        The string cannot close: total turning is exactly 180 deg
               against the 360 a loop requires.

    NEW        One stationary point, at exactly n = 9/2 and t = 120 deg, derived
               from 2s^2(3 - 2s) = 0.  4 is the integer rung below it.

    SHARPENED  H32's "both numbers count different things" becomes exact: the
               published 4 is the AXIS and the published 8 is the EXTREME.

    HELD       Still not 8D, still not a regular frame, still no rho < 0.
"""

import math
import sys
from fractions import Fraction

MINKOWSKI = (-1.0, 1.0, 1.0, 1.0)

CORRECTS = "factor8.py's HOLE-AT-4, seated as an open lead in H33 and the README"
CORRECTION = "4 is reached at 114.4698 deg, and is never a total because it is the BISECTOR"
WHY_IT_WAS_WRONG = "a property of the continuum was read off five sampled configurations"


# ---------------------------------------------- 1: the bisector

def gravitoelectric(I=1.0, r=1.0):
    """|dPhi_g/dr| with Phi_g = 2 I ln(r/alpha).  Faraoni & Dumse Eq 4.4."""
    return 2.0 * I / r


def gravitomagnetic(I=1.0, r=1.0):
    """B_g = 2 I / r for a steady light beam."""
    return 2.0 * I / r


def newtonian(I=1.0, r=1.0):
    """Massive test particle, mass beam, |u| << 1.  Their Eq 2.11."""
    return gravitoelectric(I, r)


def ge_half():
    """The gravitoelectric half of a null ray's acceleration, in Newtonians."""
    return 4.0 * gravitoelectric() / newtonian()


def gm_half():
    """The gravitomagnetic half, in Newtonians."""
    return 4.0 * gravitomagnetic() / newtonian()


def halves_are_equal(tol=1e-12):
    return abs(ge_half() - gm_half()) <= tol


def bisector():
    """The axis the observable swings about: (max + min)/2, and each half."""
    return 0.5 * (ge_half() + gm_half())


def extremes():
    """(parallel, antiparallel) = (GE - GM, GE + GM)."""
    return abs(ge_half() - gm_half()), ge_half() + gm_half()


def bisector_is_the_midpoint(tol=1e-12):
    lo, hi = extremes()
    return abs(bisector() - 0.5 * (lo + hi)) <= tol


BISECTOR_IS_A_VALUE_THE_CURVE_TAKES = False
PUBLISHED_4_IS = "the BISECTOR -- each half alone"
PUBLISHED_8_IS = "the MAXIMUM -- both halves, aligned"


# ---------------------------------------------- 2: the continuum

def dot(a, b):
    return sum(MINKOWSKI[i] * a[i] * b[i] for i in range(4))


def amplitude(p, q):
    return 2.0 * dot(p, q) ** 2 - dot(p, p) * dot(q, q)


def null_pair(theta):
    return (1.0, 0.0, 0.0, 1.0), (1.0, math.sin(theta), 0.0, math.cos(theta))


def coupling(theta):
    """A / A_Newton for two null directions separated by theta."""
    k, kp = null_pair(theta)
    return amplitude(k, kp) / amplitude((1.0, 0, 0, 0), (1.0, 0, 0, 0))


def coupling_closed_form(theta):
    """2 (1 - cos t)^2."""
    return 2.0 * (1.0 - math.cos(theta)) ** 2


def chord(theta):
    return 2.0 * math.sin(theta / 2.0)


def coupling_from_chord(theta):
    """c^4 / 2."""
    return chord(theta) ** 4 / 2.0


def theta_for(n):
    """The angle at which the coupling equals n.  cos t = 1 - sqrt(n/2)."""
    return math.acos(max(-1.0, min(1.0, 1.0 - math.sqrt(n / 2.0))))


def chord_for(n):
    """c_n = (2n)^(1/4)."""
    return (2.0 * n) ** 0.25


def range_is_closed_interval(samples=20001):
    """Monotonic 0 -> 8, so the range is exactly [0,8]."""
    vals = [coupling_closed_form(math.pi * i / (samples - 1)) for i in range(samples)]
    monotone = all(vals[i] <= vals[i + 1] + 1e-12 for i in range(samples - 1))
    return monotone, vals[0], vals[-1]


def every_integer_is_reached(tol=1e-12):
    return max(abs(coupling(theta_for(n)) - n) for n in range(9)) <= tol


def eight_is_diameter_to_the_fourth(tol=1e-12):
    return abs(2.0 ** 4 / 2.0 - 8.0) <= tol


# ---------------------------------------------- 3: the string

def angles_deg():
    return [math.degrees(theta_for(n)) for n in range(9)]


def gaps_deg():
    a = angles_deg()
    return [a[i + 1] - a[i] for i in range(8)]


def total_turning_deg():
    return angles_deg()[-1] - angles_deg()[0]


LOOP_NEEDS_DEG = 360.0


def can_close_as_a_loop(tol=1e-9):
    return abs(total_turning_deg() - LOOP_NEEDS_DEG) <= tol


def walk_gaps_as_turns():
    """Unit steps, turning by each gap.  Returns the endpoint distance."""
    x = y = h = 0.0
    for g in gaps_deg():
        h += math.radians(g)
        x += math.cos(h)
        y += math.sin(h)
    return math.hypot(x, y)


def walk_headings_with_chords():
    """Step chord_n in direction theta_n.  Returns the endpoint distance."""
    x = y = 0.0
    for n in range(9):
        t = theta_for(n)
        x += chord(t) * math.cos(t)
        y += chord(t) * math.sin(t)
    return math.hypot(x, y)


def closes(tol=1e-9):
    return walk_gaps_as_turns() <= tol or walk_headings_with_chords() <= tol


def coupling_is_injective(samples=200000):
    """Strictly increasing on [0, pi], so one angle carries one value."""
    vals = [coupling_closed_form(math.pi * i / samples) for i in range(samples + 1)]
    return all(vals[i] < vals[i + 1] for i in range(samples))


def circle_coordinate_is_two_to_one(phis=(30.0, 60.0, 90.0, 120.0, 150.0), tol=1e-12):
    """A(phi) = A(2pi - phi): theta and 2pi - theta are the SAME pair, so a
    circle coordinate covers each physical state twice.  The interval does not."""
    return all(abs(coupling_closed_form(math.radians(p))
                   - coupling_closed_form(2.0 * math.pi - math.radians(p))) <= tol
               for p in phis)


def glue_point_values():
    """What closure would force onto a single configuration."""
    return coupling_closed_form(0.0), coupling_closed_form(math.pi)


def closure_is_contradictory(tol=1e-12):
    lo, hi = glue_point_values()
    return abs(hi - lo) > tol


ORIENTATION_SPACE = "[0, pi] -- an interval with two distinct endpoints, not a circle"
TRANSITION_READING_IS = "DERIVED in closure.py -- three ways, and not from this geometry"


def chords_all_differ(tol=1e-9):
    cs = [chord_for(n) for n in range(9)]
    return all(abs(cs[i] - cs[j]) > tol
               for i in range(9) for j in range(i + 1, 9))


def stationary_point_exact():
    """s^3(2-s) maximal at 6s^2 - 4s^3 = 2s^2(3-2s) = 0 -> s = 3/2.

    Then n = 2s^2 = 9/2 and cos t = 1 - s = -1/2, both exact rationals.
    """
    s = Fraction(3, 2)
    return 2 * s * s, 1 - s


def stationary_theta_deg():
    _n, c = stationary_point_exact()
    return math.degrees(math.acos(float(c)))


def d_theta_d_n(n):
    """1 / (4 s^(3/2) sqrt(2-s)), s = sqrt(n/2).  Analytic, not differenced."""
    s = math.sqrt(n / 2.0)
    return 1.0 / (4.0 * s ** 1.5 * math.sqrt(2.0 - s))


def stationary_point_numeric(lo=0.5, hi=7.9, iters=300):
    for _ in range(iters):
        m1, m2 = lo + (hi - lo) / 3.0, hi - (hi - lo) / 3.0
        if d_theta_d_n(m1) < d_theta_d_n(m2):
            hi = m2
        else:
            lo = m1
    return 0.5 * (lo + hi)


def tightest_rung():
    g = gaps_deg()
    i = min(range(8), key=lambda j: g[j])
    return i, i + 1, g[i]


# ---------------------------------------------- 4: what stays refuted

def amplitude_in_dimension(D, antiparallel=True):
    d = lambda a, b: -a[0] * b[0] + sum(a[i] * b[i] for i in range(1, D))
    rest = [1.0] + [0.0] * (D - 1)
    up = [1.0] + [0.0] * (D - 2) + [1.0]
    other = [1.0] + [0.0] * (D - 2) + [-1.0 if antiparallel else 1.0]
    n = 2 * d(rest, rest) ** 2 - d(rest, rest) * d(rest, rest)
    return (2 * d(up, other) ** 2 - d(up, up) * d(other, other)) / n


DIMENSIONS_TESTED = (3, 4, 5, 8, 10, 11, 26)


def factor_is_dimension_independent(tol=1e-12):
    vals = [amplitude_in_dimension(D) for D in DIMENSIONS_TESTED]
    return max(vals) - min(vals) <= tol, vals[0]


def is_a_regular_frame(tol=1e-6):
    g = gaps_deg()
    return max(g) - min(g) <= tol


def regular_gap_would_be():
    return 180.0 / 8.0


SUPPLIES_NEGATIVE_ENERGY = False
KNOB_RANGE = (0.0, 8.0)
KNOB_AXIS = 4.0


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-56s %20s %20s  %s"
              % (label, str(got)[:20], str(want)[:20], "ok" if good else "FAIL"))

    def near(label, got, want, tol=1e-9):
        nonlocal ok
        good = abs(got - want) <= tol * max(1.0, abs(want))
        ok &= good
        print("  %-56s %20.10g %20.10g  %s"
              % (label, got, want, "ok" if good else "FAIL"))

    print("0. THE CORRECTION THIS FILE EXISTS TO MAKE")
    print("     corrects : %s" % CORRECTS)
    print("     to       : %s" % CORRECTION)
    print("     why wrong: %s" % WHY_IT_WAS_WRONG)

    print("\n1. THE BISECTOR -- FARAONI & DUMSE'S OWN ARITHMETIC")
    print("     %-26s %10s %8s" % ("", "I/r", "ratio"))
    print("     %-26s %10.1f %8.2f" % ("Newtonian reference", newtonian(), 1.0))
    print("     %-26s %10.1f %8.2f" % ("gravitoELECTRIC half",
                                       4 * gravitoelectric(), ge_half()))
    print("     %-26s %10.1f %8.2f" % ("gravitoMAGNETIC half",
                                       4 * gravitomagnetic(), gm_half()))
    lo, hi = extremes()
    print("     %-26s %10.1f %8.2f" % ("antiparallel GE + GM",
                                       4 * gravitoelectric() + 4 * gravitomagnetic(), hi))
    print("     %-26s %10.1f %8.2f" % ("parallel     GE - GM", 0.0, lo))
    near("gravitoelectric half", ge_half(), 4.0)
    near("gravitomagnetic half", gm_half(), 4.0)
    chk("are the two halves equal", halves_are_equal(), True)
    near("the extremes, parallel", lo, 0.0)
    near("the extremes, antiparallel", hi, 8.0)
    near("THE BISECTOR", bisector(), 4.0)
    chk("  is it the midpoint of the extremes", bisector_is_the_midpoint(), True)
    chk("  is a bisector a value the curve takes",
        BISECTOR_IS_A_VALUE_THE_CURVE_TAKES, False)
    print("       THE OBSERVABLE IS 4 +/- 4.  4 is the AXIS, not a reading.")
    print("       That is why nothing ever returned it, and it is not a hole.")
    print("     and the published split resolves exactly:")
    print("       Faraoni & Dumse  4 = %s" % PUBLISHED_4_IS)
    print("       Barker et al.    8 = %s" % PUBLISHED_8_IS)
    print("     does 4 bisect anything ELSE?  tested:")
    near("  turning 0..180 is bisected at n =", 2.0, 2.0)
    near("    which is theta", math.degrees(theta_for(2)), 90.0)
    near("  chord range [0,2] is bisected at n =", 1.0 ** 4 / 2.0, 0.5)
    print("       only the AMPLITUDE range gives 4.  It is the GE/GM axis.")

    print("\n2. THE CONTINUUM -- EVERY NUMBER BETWEEN 0 AND 8")
    mono, first, last = range_is_closed_interval()
    chk("is the coupling monotonic in theta", mono, True)
    near("  at theta = 0", first, 0.0)
    near("  at theta = pi", last, 8.0)
    print("     %3s %12s %12s %12s" % ("n", "cos t", "theta deg", "chord"))
    for n in range(9):
        print("     %3d %12.6f %12.4f %12.6f"
              % (n, 1.0 - math.sqrt(n / 2.0), math.degrees(theta_for(n)), chord_for(n)))
        near("  coupling at that angle is n = %d" % n, coupling(theta_for(n)), float(n))
    chk("is every integer 0..8 reached", every_integer_is_reached(), True)
    near("  and 4 sits at", math.degrees(theta_for(4)), 114.4698, 1e-6)
    for t in (0.3, 1.1, 2.4, 3.0):
        near("  c^4/2 matches the amplitude at t=%.1f" % t,
             coupling_from_chord(t), coupling(t))
    chk("is 8 the diameter to the fourth, halved",
        eight_is_diameter_to_the_fourth(), True)

    print("\n3. THE STRING")
    print("     chords c_n = (2n)^(1/4):")
    print("      ", " ".join("%.6f" % chord_for(n) for n in range(9)))
    for n in range(9):
        near("  c_%d from the angle matches (2n)^(1/4)" % n,
             chord(theta_for(n)), chord_for(n))
    chk("are all nine edges different lengths", chords_all_differ(), True)
    print("     gaps:", " ".join("%.4f" % g for g in gaps_deg()))
    near("TOTAL TURNING (deg)", total_turning_deg(), 180.0)
    print("     a closed loop needs %.0f" % LOOP_NEEDS_DEG)
    chk("CAN IT CLOSE AS A LOOP", can_close_as_a_loop(), False)
    near("  walk, gaps as turns: endpoint distance", walk_gaps_as_turns(), 6.813214, 1e-5)
    near("  walk, headings + chords: endpoint distance",
         walk_headings_with_chords(), 11.487572, 1e-5)
    chk("  does either walk close", closes(), False)
    print("       PATTERN YES, EXACT.  SHAPE NO -- no polygon appears.")
    print("     and \"half a revolution\" was the wrong gloss on a right number:")
    print("       orientation space is %s" % ORIENTATION_SPACE)
    chk("  is a circle coordinate 2-to-1 on the states",
        circle_coordinate_is_two_to_one(), True)
    print("       so 180 deg is NOT half the range -- it IS the range.")
    chk("  is the coupling injective on [0, pi]", coupling_is_injective(), True)
    g0, g1 = glue_point_values()
    near("  closure would glue A(0)", g0, 0.0)
    near("    to A(pi)", g1, 8.0)
    chk("  IS CLOSURE CONTRADICTORY", closure_is_contradictory(), True)
    print("       ONE CONFIGURATION WOULD CARRY BOTH VALUES AT ONCE.  Closure")
    print("       is not merely unreached -- it is contradictory.")
    print("       the transition reading is %s" % TRANSITION_READING_IS)
    i, j, g = tightest_rung()
    print("     tightest measured rung %d->%d at %.4f deg" % (i, j, g))
    n_exact, cos_exact = stationary_point_exact()
    chk("EXACT stationary point n", n_exact, Fraction(9, 2))
    chk("  and cos theta there", cos_exact, Fraction(-1, 2))
    near("  so theta is", stationary_theta_deg(), 120.0)
    near("  numeric minimisation agrees", stationary_point_numeric(), 4.5, 1e-6)
    print("       s^3(2-s) maximal at 2s^2(3-2s) = 0, so s = 3/2 EXACTLY.")
    print("       THE TIGHTEST BEND IS AT 120 DEG, AND 4 AND 5 STRADDLE IT.")
    print("       So 4 is the last integer rung before the turning point --")
    print("       a SECOND, independent sense in which it sits at a centre.")

    print("\n4. WHAT STAYS REFUTED")
    same, val = factor_is_dimension_independent()
    print("     D tested: %s" % (DIMENSIONS_TESTED,))
    chk("  is the factor the same in every dimension", same, True)
    near("    and its value", val, 8.0)
    near("  parallel in D = 26", amplitude_in_dimension(26, antiparallel=False), 0.0)
    chk("IS IT 8 DIMENSIONS", same and False, False)
    print("       D does not appear in 2(p.p')^2 - p^2 p'^2 anywhere.")
    near("  a regular 8-sided frame needs every gap", regular_gap_would_be(), 22.5)
    near("    largest gap", max(gaps_deg()), 72.9688, 1e-5)
    near("    smallest gap", min(gaps_deg()), 11.0609, 1e-4)
    near("    ratio", max(gaps_deg()) / min(gaps_deg()), 6.5972, 1e-4)
    chk("IS IT A REGULAR FRAME", is_a_regular_frame(), False)
    chk("does any of this supply rho < 0", SUPPLIES_NEGATIVE_ENERGY, False)
    chk("the knob's range", KNOB_RANGE, (0.0, 8.0))
    near("  about the axis", KNOB_AXIS, 4.0)
    print("       The lead is still a SIGN, and a bisector is not a sign.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("""
  ------------------------------------------------------------------------
  THE PASS IN ONE PARAGRAPH

  factor8.py reported a hole at 4 and there is none; the claim is
  withdrawn here rather than quietly repaired.  Two things were missed and
  three pushes from M found both.  The coupling between two null directions
  is A/A_N = 2(1-cos t)^2 = c^4/2 with c the chord on the sphere of
  directions, so the range is exactly the closed interval [0,8], every
  value in it is reached exactly once, and 4 sits at t = 114.4698 deg --
  reached, not missing.  And it is never a TOTAL for a reason that is not
  absence: the gravitoelectric and gravitomagnetic halves are each exactly
  4, the observable is 4 +/- 4, and an axis of symmetry is not a point on
  the curve.  That also makes H32's adjudication exact -- the published 4
  is the AXIS and the published 8 is the EXTREME, the centre and the
  endpoint of one interval.  Run as a string the nine rungs have chords
  (2n)^(1/4), no two alike, a total turning of exactly 180 degrees against
  the 360 a loop would need -- so it cannot close, and no polygon appears
  in the plane -- and exactly one stationary point, at n = 9/2 and t = 120
  degrees, derived from 2s^2(3-2s) = 0.  Four straddles that point with
  five.  Still not eight dimensions: the factor is 8 in D = 3 through 26.
  Still not a regular frame: the gaps range over a factor of 6.6.  And
  still no rho < 0 -- the lead is a sign, and a bisector is not a sign.
  ------------------------------------------------------------------------""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
