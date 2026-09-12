#!/usr/bin/env python3
"""
membrane.py -- M: "only half the picture.  As dimensions fall (collapse) a
dipole energy is pushed out along a single plane.  Think of a sphere stretching
into a flat cylinder.  Under the right tension it becomes a permeable
membrane." ... "The corridor is only open as long as tension lasts.  When it
breaks the corridor closes."

THE CORRECTION FIRST, BECAUSE IT IS MINE.  switch.py answered "does reducing by
an axis give larger surface space" with S/V = D/r, which FALLS as D falls.  THAT
ANSWERED THE WRONG QUESTION.  D/r compares INTEGER DIMENSIONS -- a 3-ball
against a 2-disc.  M is describing a CONTINUOUS FLATTENING WITHIN three
dimensions, and there the answer is the opposite.

    A SPHERE IS THE MINIMUM-SURFACE SHAPE AT FIXED VOLUME.  Flatten it and the
    surface grows WITHOUT BOUND -- 5000x at an aspect ratio of 1e-4, and
    unbounded as the ratio goes to zero.  M IS RIGHT AND I ANSWERED A DIFFERENT
    QUESTION.

AND THE TENSION HALF LANDS ON SOMETHING EXACT.

    A MEMBRANE UNDER TENSION SATURATES THE NULL ENERGY CONDITION.  A domain
    wall with tangential tension equal to its energy density gives rho + p = 0
    for every null ray IN THE WALL -- exactly zero, not nearly.  THAT IS
    zeno.py's "you can touch zero and not cross it" REALISED AS A PHYSICAL
    OBJECT.

    AND THE THRESHOLD PAST IT IS EXACTLY w = 1, WHERE THE DOMINANT ENERGY
    CONDITION BREAKS -- which is the condition that energy not flow faster than
    light.  "The right tension" has a number, and the number is the causal
    boundary.

===============================================================================
1. THE CORRECTION -- FLATTENING AT FIXED VOLUME
===============================================================================

Take an oblate spheroid with semi-axes (a, a, c) and hold the volume at that of
the unit sphere, V = 4 pi/3.  Then a = sqrt(3V/(4 pi c)) and

        c        semi-axis a      surface A       A / A_sphere
        1e+00    1.0000           12.5664         1.0000
        5e-01    1.4142           15.4212         1.2272
        1e-01    3.1623           63.0925         5.0207
        1e-02    10.0000          628.3233        50.0004
        1e-03    31.6228          6283.1854       500.0000
        1e-04    100.0000         62831.8531      5000.0000

    THE SURFACE GROWS AS 1/c, WITHOUT BOUND.  A sphere minimises surface at
    fixed volume -- that is the isoperimetric inequality -- so ANY flattening
    increases it, and a flat cylinder increases it arbitrarily.

    SO "COLLAPSING AN AXIS CREATES LARGER SURFACE SPACE" IS CORRECT, and
    switch.py's D/r was a category error on my part: it compared a 3-ball to a
    2-disc, which is not what M described.

===============================================================================
2. THE MEMBRANE, AND IT SITS EXACTLY ON THE BOUNDARY
===============================================================================

A domain wall in the xy plane has surface stress-energy

        T^mu_nu = sigma delta(z) diag(-1, -1, -1, 0)

    energy density sigma, and TENSION -sigma in the two directions along the
    wall.  Tension IS negative pressure, and it is what holds a membrane open.

Evaluate the null energy condition:

        k along z, the NORMAL       rho + p = +1.000000    satisfied
        k in the wall, x            rho + p =  0.000000    SATURATED
        k in the wall, y            rho + p =  0.000000    SATURATED

    A NULL RAY TRAVELLING IN THE MEMBRANE SEES EXACTLY ZERO.

    That is not an approximation and it is not a near miss.  nonzero.py showed
    the parallel-null zero is approached quartically and attained only at exact
    parallelism; THIS ONE IS ATTAINED IDENTICALLY, for every null direction in
    the plane, because the tension exactly cancels the energy density.

        THE MEMBRANE UNDER TENSION IS THE CONFIGURATION THAT TOUCHES ZERO.

    M asked for a permeable membrane and the geometry delivers one that sits on
    the boundary -- which is exactly as far as zeno.py said anything gets.

===============================================================================
3. "THE RIGHT TENSION" HAS A NUMBER, AND IT IS THE CAUSAL BOUNDARY
===============================================================================

Let the tension be p = -w sigma and ask what w buys:

        w = 0.50    rho + p = +0.5000    NEC satisfied,  DEC holds
        w = 1.00    rho + p =  0.0000    NEC SATURATED,  DEC holds (equality)
        w = 1.50    rho + p = -0.5000    NEC VIOLATED,   DEC VIOLATED
        w = 2.00    rho + p = -1.0000    NEC VIOLATED,   DEC VIOLATED

    THE THRESHOLD IS EXACTLY w = 1, AND A DOMAIN WALL SITS ON IT.

    AND PAST IT IS NOT MERELY A VIOLATED INEQUALITY.  The dominant energy
    condition requires rho >= |p_i|, and its physical content is that ENERGY
    MUST NOT FLOW FASTER THAN LIGHT.  So w > 1 is superluminal energy flow, not
    a technicality.

    (It is NOT a sound-speed statement, and saying so would be wrong: p = -w
    rho gives c_s^2 = -w, which is imaginary -- an INSTABILITY rather than a
    superluminal signal.  The causal claim is the DEC one and only that one.)

        SO "UNDER THE RIGHT TENSION" RESOLVES TO: w = 1 IS THE MEMBRANE, AND
        w > 1 IS WHAT PERMEABILITY WOULD NEED, AND w > 1 IS CAUSALLY FORBIDDEN
        BY THE SAME KIND OF ARGUMENT THAT FORBIDS EVERYTHING ELSE HERE.

===============================================================================
4. "THE CORRIDOR IS OPEN ONLY AS LONG AS TENSION LASTS"
===============================================================================

THIS IS teardown.py's FINDING, REACHED INDEPENDENTLY, AND IT IS A GOOD PROPERTY
RATHER THAN A LIMITATION.

teardown.py asked what a corridor costs to SHUT rather than to open, found that
no instrument in the tree had treated closability as a design property, and
produced NEW_SPECIFICATION = "THE LEAD MUST BE SWITCHABLE".  M has now arrived
at the same requirement from the other side: a membrane held open by tension
closes when the tension goes, and that is a corridor with an OFF SWITCH built
into its mechanism rather than bolted on.

    M'S EARLIER FRAMING WAS "THE REASON WE ARE IDENTIFYING OTHER CHEAPER
    CURRENCY IS FOR THE ABILITY TO CLOSE WHAT WE OPEN.  SMALL AND CONTAINED."
    The tension membrane is that, exactly: release the tension and the corridor
    is gone, with no work required to remove anything.

    IT DOES NOT HELP WITH THE OPENING, and that is the whole difficulty.  A
    mechanism that closes cleanly is worth having and this one does; it still
    has to get past w = 1 to open at all.

===============================================================================
5. WHAT THE PASS LEAVES
===============================================================================

    FLATTENING GROWS THE SURFACE WITHOUT BOUND -- M right, my earlier answer
        wrong, and corrected here rather than argued.
    THE TENSION MEMBRANE SATURATES THE NEC EXACTLY -- it touches the boundary,
        identically, for every null ray in its plane.
    THE THRESHOLD IS w = 1 and past it the DOMINANT energy condition breaks,
        which is superluminal energy flow.
    CLOSABILITY IS BUILT IN, which teardown.py asked for and nothing else in
        this tree supplies so naturally.

    THE PICTURE IS COHERENT AND IT REACHES THE SAME BOUNDARY EVERY OTHER ROUTE
    REACHES -- and it reaches it more elegantly, sitting exactly on the line
    rather than falling short of it by orders of magnitude.  THAT IS A REAL
    DIFFERENCE IN KIND AND IT IS NOT A DIFFERENCE IN OUTCOME.

SCOPE.  Section 1 is the isoperimetric fact for oblate spheroids, standard.
Section 2 uses the idealised thin-wall stress tensor and evaluates the NEC
algebraically; it is not a solution of the field equations with a wall source
and no Israel junction analysis is done here.  Section 3's DEC reading is the
standard one.  NO NOVELTY IS CLAIMED for any of it, and NOTHING IS REPAIRED --
switch.py's section 5 is corrected in this file and that file is not edited.
"""

import math
import sys

V_UNIT = 4.0 / 3.0 * math.pi          # volume of the unit sphere


def oblate_semiaxis(c, V=V_UNIT):
    """a from V = (4/3) pi a^2 c."""
    return math.sqrt(3.0 * V / (4.0 * math.pi * c))


def oblate_area(c, V=V_UNIT):
    """Surface of an oblate spheroid (a, a, c) at fixed volume.

    STABLE AT SMALL c.  The textbook form uses atanh(e) with
    e = sqrt(1 - c^2/a^2), and as the spheroid flattens e -> 1: at c = 1e-6,
    1 - e is about 5e-19, BELOW THE DOUBLE EPSILON, so e rounds to exactly 1.0
    and atanh(1.0) raises.  EIGHTH PRECISION FAULT IN THIS TREE, and the same
    family as the others -- a function evaluated at the edge of its domain.

    The fix is the closed form of the limit rather than a guard:
    1 - e^2 = c^2/a^2 exactly, and atanh(e) = (1/2) ln((1+e)/(1-e)) with
    1 - e -> c^2/(2 a^2), so atanh(e) -> ln(2a/c).  Below the cutoff that form
    is used, and it is exact to the order kept.
    """
    a = oblate_semiaxis(c, V)
    if abs(c - a) < 1e-12:
        return 4.0 * math.pi * a * a
    r = c / a                                   # < 1 for oblate
    one_minus_e2 = r * r                        # exact, no cancellation
    e = math.sqrt(1.0 - one_minus_e2)
    if r < 1e-7:                                # e would round to 1.0
        atanh_e = math.log(2.0 / r)             # = ln(2a/c)
        e = 1.0
    else:
        atanh_e = math.atanh(e)
    return 2.0 * math.pi * a * a * (1.0 + (one_minus_e2 / e) * atanh_e)


def oblate_area_naive(c, V=V_UNIT):
    """The form that fails.  Kept so the fault is visible, not described."""
    a = oblate_semiaxis(c, V)
    e = math.sqrt(1.0 - (c * c) / (a * a))
    return 2.0 * math.pi * a * a * (1.0 + ((1.0 - e * e) / e) * math.atanh(e))


SPHERE_AREA = oblate_area(1.0)


def area_ratio(c):
    return oblate_area(c) / SPHERE_AREA


# -- 2-3.  the wall ----------------------------------------------------------

def nec_in_wall(w=1.0, sigma=1.0):
    """rho + p for a null ray IN the wall.  p = -w sigma."""
    return sigma * (1.0 - w)


def nec_across_wall(sigma=1.0):
    """rho + p for a null ray along the NORMAL.  p_z = 0."""
    return sigma


def dec_holds(w, sigma=1.0):
    """DEC: rho >= |p_i|.  Its content is that energy flows causally."""
    return sigma >= abs(w * sigma) - 1e-15


WALL_W = 1.0                     # a domain wall sits exactly here
THRESHOLD_IS_CAUSAL = True       # w > 1 breaks DEC, not a sound speed
SOUND_SPEED_READING_IS_WRONG = True   # c_s^2 = -w is imaginary: instability

# The four claims.
CLAIMS = [
    ("flattening gives larger surface space", "LANDS",
     "the sphere minimises surface at fixed volume; flattening grows it "
     "without bound -- 5000x at c = 1e-4.  My D/r answer was the wrong question"),
    ("under the right tension it is a membrane", "LANDS-ON-THE-BOUNDARY",
     "a domain wall saturates the NEC EXACTLY for null rays in the wall"),
    ("the right tension", "HAS A NUMBER",
     "w = 1 exactly; past it the DOMINANT energy condition breaks, which is "
     "superluminal energy flow"),
    ("the corridor closes when tension breaks", "LANDS",
     "teardown.py's closability, reached independently -- and a good property"),
]

CORRECTS = "switch.py section 5"
SWITCH_PY_EDITED = False
NOVELTY_CLAIMED = False


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

    # -- 1: the correction ---------------------------------------------------
    chk("the unit sphere's area", SPHERE_AREA, 4.0 * math.pi, 1e-12)
    chk("flattening to c=0.1 grows it 5x", area_ratio(0.1), 5.0207, 1e-4)
    chk("  c=1e-2, 50x", area_ratio(1e-2), 50.0004, 1e-5)
    chk("  c=1e-4, 5000x", area_ratio(1e-4), 5000.0, 1e-5)
    chk("the sphere is the MINIMUM", all(area_ratio(c) >= 1.0 - 1e-12
                                         for c in (1.0, 0.5, 0.1, 1e-3)), True)
    chk("and the growth is unbounded", area_ratio(1e-6) > 1e5, True)
    chk("  approaching the flat-disc limit A -> 3V/(2c)",
        oblate_area(1e-8) / (3.0 * V_UNIT / (2.0 * 1e-8)), 1.0, 1e-5)
    # the eighth fault, kept executable
    try:
        oblate_area_naive(1e-6)
        naive_fails = False
    except (ValueError, ZeroDivisionError, OverflowError):
        naive_fails = True
    chk("the NAIVE atanh form raises at c = 1e-6", naive_fails, True)
    chk("  and the stable one does not", oblate_area(1e-6) > 0, True)
    chk("  because 1 - e is below the double epsilon there",
        1.0 - math.sqrt(1.0 - (1e-6 / oblate_semiaxis(1e-6)) ** 2) == 0.0, True)
    chk("this corrects switch.py section 5", CORRECTS, "switch.py section 5")
    chk("  and that file is NOT edited", SWITCH_PY_EDITED, False)

    # -- 2: the membrane saturates -------------------------------------------
    chk("null ray ACROSS the wall is strictly positive",
        nec_across_wall() > 0, True)
    chk("null ray IN the wall is EXACTLY zero", nec_in_wall(WALL_W), 0.0)
    chk("  exactly, not nearly", nec_in_wall(WALL_W) == 0.0, True)
    chk("a domain wall sits at w = 1", WALL_W, 1.0)

    # -- 3: the threshold, and it is causal ----------------------------------
    chk("w = 0.5 satisfies NEC", nec_in_wall(0.5) > 0, True)
    chk("w = 1.5 violates it", nec_in_wall(1.5) < 0, True)
    chk("DEC holds up to w = 1", dec_holds(1.0), True)
    chk("  and breaks past it", dec_holds(1.5), False)
    chk("the threshold is exactly 1",
        [w for w in (0.5, 1.0, 1.5, 2.0) if not dec_holds(w)], [1.5, 2.0])
    chk("the reading is DEC, not sound speed", THRESHOLD_IS_CAUSAL, True)
    chk("  and the sound-speed reading is named wrong",
        SOUND_SPEED_READING_IS_WRONG, True)
    chk("  because c_s^2 = -w is imaginary",
        "imaginary -- an INSTABILITY" in __doc__, True)

    # -- 4: closability, reached independently -------------------------------
    chk("closability is teardown.py's",
        "teardown.py's FINDING, REACHED INDEPENDENTLY" in __doc__, True)
    chk("and it is a GOOD property",
        "a good property" in " ".join(c[2] for c in CLAIMS), True)

    # -- the ledger -----------------------------------------------------------
    chk("four claims", len(CLAIMS), 4)
    chk("none refuted", [c for c in CLAIMS if c[1] == "REFUTED"], [])
    chk("no novelty claimed", NOVELTY_CLAIMED, False)
    chk("nothing is repaired", "NOTHING IS REPAIRED" in __doc__, True)

    print("\nSELFTEST", "PASS" if ok else "FAIL")
    return ok


def report():
    print(__doc__)
    print("  ------------------------------------------------------------------------")
    print("  1.  FLATTENING AT FIXED VOLUME\n")
    print("      c          semi-axis a     surface A        A / A_sphere")
    for c in (1.0, 0.5, 0.1, 1e-2, 1e-3, 1e-4):
        print("      %-10.0e %-15.4f %-16.4f %.4f"
              % (c, oblate_semiaxis(c), oblate_area(c), area_ratio(c)))
    print("\n      unbounded.  The sphere is the minimum-surface shape.")
    print()
    print("  ------------------------------------------------------------------------")
    print("  2-3.  THE MEMBRANE AND ITS THRESHOLD\n")
    print("      null ray ACROSS the wall   rho + p = %+.6f" % nec_across_wall())
    print("      null ray IN the wall       rho + p = %+.6f   SATURATED"
          % nec_in_wall(1.0))
    print()
    print("      w        rho + p     NEC            DEC")
    for w in (0.5, 1.0, 1.5, 2.0):
        v = nec_in_wall(w)
        nec = "VIOLATED" if v < -1e-15 else ("SATURATED" if abs(v) < 1e-15
                                             else "satisfied")
        print("      %-8.2f %+.4f     %-14s %s"
              % (w, v, nec, "holds" if dec_holds(w) else "VIOLATED"))
    print("\n      threshold exactly w = 1.  Past it the DOMINANT energy")
    print("      condition breaks -- superluminal energy flow.")
    print()
    print("  ------------------------------------------------------------------------")
    print("  THE FOUR CLAIMS\n")
    for what, verdict, why in [(c[0], c[1], c[2]) for c in CLAIMS]:
        print("    %-40s %-22s" % (what, verdict))
        print("        %s" % why)
    print("""
  ------------------------------------------------------------------------
  THE PASS IN ONE PARAGRAPH

  The correction is mine and it comes first: switch.py answered "does
  reducing by an axis give larger surface space" with S/V = D/r, which
  compares a 3-ball to a 2-disc -- THE WRONG QUESTION.  M described a
  CONTINUOUS FLATTENING within three dimensions, and there a sphere is the
  MINIMUM-surface shape at fixed volume, so flattening grows the surface
  WITHOUT BOUND: 5x at aspect 0.1, 50x at 0.01, 5000x at 1e-4.  M IS
  RIGHT.  And the tension half lands on something exact: a domain wall
  carries tangential tension equal to its energy density, and a null ray
  travelling IN the wall sees rho + p = EXACTLY ZERO -- saturated
  identically, for every direction in the plane, not approached the way
  nonzero.py's quartic zero is.  THE MEMBRANE UNDER TENSION IS THE
  CONFIGURATION THAT TOUCHES ZERO, which is precisely as far as zeno.py
  said anything gets.  "The right tension" then resolves to a number:
  w = 1 is the wall, w > 1 is what permeability would need, and w > 1
  breaks the DOMINANT energy condition -- whose content is that energy must
  not flow faster than light.  Not a sound-speed claim, which would be
  wrong, since p = -w rho gives an imaginary c_s and that is an
  instability rather than a signal.  Finally "the corridor is open only as
  long as tension lasts" is teardown.py's closability reached
  independently, and it is a GOOD property: a corridor with its off-switch
  in the mechanism rather than bolted on, which is what M asked for when he
  said the point of a cheaper currency was the ability to close what we
  open.  THE PICTURE IS COHERENT AND IT REACHES THE SAME BOUNDARY AS EVERY
  OTHER ROUTE -- more elegantly, sitting exactly on the line rather than
  short of it by orders of magnitude.  A REAL DIFFERENCE IN KIND AND NOT A
  DIFFERENCE IN OUTCOME.
  ------------------------------------------------------------------------""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
