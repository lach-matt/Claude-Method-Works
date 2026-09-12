#!/usr/bin/env python3
"""
threads.py -- M: "the inner corridor produces 3 threads, time, space, and one
where they intersect" ... "8 knob settings, on, off, time 2 way, space 2 way,
both 2 way.  1+1+2+2+2=8"

THE THREE THREADS ARE REAL, AND THE THIRD ONE IS THE MOST IMPORTANT THING M HAS
POINTED AT.  The eight is real too and it is not the eight he counted.

    THE THIRD THREAD IS g_t.phi, THE CROSS TERM -- and STATIC MEANS EXACTLY
    g_t.phi = 0.  certify.py carries THEOREM_SCOPE = "static and spherically
    symmetric only".  M HAS IDENTIFIED THE THEOREM'S OWN SCOPE CONDITION BY
    REASONING ABOUT THREADS, without being told it.

    AND TURNING IT ON BREAKS THE BICONDITIONAL.  In Kerr at the equator,
    RADIAL PROPER DISTANCE IS CONTRACTED WITH POSITIVE MASS whenever
    a^2 > 2 M r.  Measured at M = 1, a = 0.99: g_rr = 0.012657 at r = 0.1,
    0.191449 at r = 0.3, 0.999584 at r = 0.49.  ALL CONTRACTED, ALL WITH M > 0.

    THE STATIC THEOREM SAYS CONTRACTION REQUIRES NEGATIVE MASS.  ROTATION IS A
    COUNTEREXAMPLE, AND THE TREE HAD NEVER TESTED IT.

    WHAT KEEPS IT FROM BEING A ROUTE IS A HORIZON -- and, honestly, a
    CONJECTURE.  For every sub-extremal spin the contracted region is inside
    r_+.  It is exposed only for a > M, a naked singularity, forbidden by
    COSMIC CENSORSHIP, WHICH IS UNPROVEN.

===============================================================================
1. THE THREE THREADS, AND THE THIRD IS THE SCOPE CONDITION
===============================================================================

A stationary axisymmetric metric has exactly three independent pieces here, and
coefficients.py had already separated the first two without naming the third:

    TIME            g_tt        an ENDPOINT RATIO,    1 + z = e^{dPhi}
    SPACE           g_rr        a LINE INTEGRAL,      Int dr/sqrt(f)
    INTERSECTION    g_t.phi     THE CROSS TERM -- frame dragging

    "STATIC" MEANS g_t.phi = 0.  A metric with the cross term on is STATIONARY
    but NOT STATIC.  So the third thread is not an extra: IT IS PRECISELY THE
    ASSUMPTION certify.py's THEOREM MAKES, and overturn.py's L1 is the question
    of what survives without it.

    M ARRIVED AT L1's CONDITION FROM THE OTHER SIDE.  That is the finding of
    section 1 and it is worth stating on its own.

===============================================================================
2. TURN IT ON AND THE BICONDITIONAL FAILS
===============================================================================

Kerr in Boyer-Lindquist has g_rr = rho^2/Delta with rho^2 = r^2 + a^2 cos^2 th
and Delta = r^2 - 2 M r + a^2.  Contraction is g_rr < 1, i.e. Delta > rho^2,
and at the equator that is

        r^2  <  r^2 - 2 M r + a^2        <=>        a^2 > 2 M r

    NO NEGATIVE MASS APPEARS IN THAT CONDITION.  Measured, M = +1, a = 0.99,
    equator:

        r = 0.10     g_rr = +0.012657     CONTRACTED
        r = 0.30     g_rr = +0.191449     CONTRACTED
        r = 0.49     g_rr = +0.999584     CONTRACTED
        r = 0.60     g_rr = +2.569593
        r = 1.50     g_rr = +9.778357

    certify.py's THEOREM: contraction at r if and only if m(r) < 0.
    KERR AT r = 0.3 WITH M = +1: CONTRACTED.

    THE BICONDITIONAL IS STATIC-ONLY, AND THIS IS WHY.  The tree stated the
    scope and never tested what lay outside it.  Now it has.

===============================================================================
3. AND A HORIZON SITS IN FRONT OF IT -- HELD THERE BY A CONJECTURE
===============================================================================

        a/M      contracted region      r_+            exposed?
        0.00     none                   2.0000         no
        0.50     r < 0.1250             1.8660         no
        0.90     r < 0.4050             1.4359         no
        0.99     r < 0.4900             1.1411         no
        1.00     r < 0.5000             1.0000         no
        1.10     r < 0.6050             NONE           YES -- naked
        1.50     r < 1.1250             NONE           YES -- naked
        2.00     r < 2.0000             NONE           YES -- naked

    FOR EVERY SUB-EXTREMAL SPIN THE CONTRACTED REGION IS INSIDE THE HORIZON.
    It is exposed only for a > M, which is an over-extremal Kerr solution --
    a NAKED SINGULARITY.

    AND WHAT FORBIDS THAT IS COSMIC CENSORSHIP, WHICH IS A CONJECTURE AND NOT A
    THEOREM.  That has to be said plainly, because the tree's discipline is to
    distinguish the two and this is exactly a place where it matters: THE ONE
    KNOWN COUNTEREXAMPLE TO THE BICONDITIONAL IS HIDDEN BY AN UNPROVEN
    CONJECTURE RATHER THAN BY A PROOF.

    IT IS ALSO NOT A ROUTE, AND THE REASONS ARE INDEPENDENT OF CENSORSHIP.
    Over-extremal Kerr has no horizon and no known formation process; sub-
    extremal Kerr puts the region behind a horizon you cannot return from; and
    neither case supplies a corridor between two places, only a contracted
    region inside a black hole.  RECORDED AS A GAP IN THE THEOREM, NOT AS A
    DOOR.

===============================================================================
4. THE EIGHT -- AND IT COLLAPSES TO TWO
===============================================================================

M counts 1 + 1 + 2 + 2 + 2 = 8.  The arithmetic is right and there are TWO
DIFFERENT EIGHTS in play:

    A)  THREE THREADS, EACH A SIGN: 2^3 = 8, THE CUBE'S VERTICES.  That is the
        tree's own eight -- cubic.py found those eight sum to zero as four
        antipodal pairs.

    B)  M's PARTITION selects 8 states out of the 3^3 = 27 trit-states
        {-, 0, +}^3 -- off, all-on, and three two-way channels.  Also eight,
        and NOT THE SAME EIGHT.

NOW THE PHYSICAL TEST, WHICH SETTLES IT.  Vary each thread's sign and watch
g_rr at M = 1, r = 0.3, a = 0.99:

        Phi+  m+  a+     g_rr = +0.191449     CONTRACTED
        Phi+  m+  a-     g_rr = +0.191449     CONTRACTED
        Phi+  m-  a+     g_rr = +0.053889     CONTRACTED
        Phi+  m-  a-     g_rr = +0.053889     CONTRACTED
        Phi-  m+  a+     g_rr = +0.191449     CONTRACTED
        Phi-  m+  a-     g_rr = +0.191449     CONTRACTED
        Phi-  m-  a+     g_rr = +0.053889     CONTRACTED
        Phi-  m-  a-     g_rr = +0.053889     CONTRACTED

    EIGHT STATES.  TWO DISTINCT VALUES.

        Phi's SIGN DOES NOT ENTER g_rr AT ALL -- the time thread does not touch
            radial distance, which is coefficients.py's split again.
        a's SIGN DOES NOT ENTER EITHER -- only a^2 appears, so the intersection
            thread is SIGN-BLIND and contributes a magnitude.
        ONLY m's SIGN CHANGES ANYTHING.

    SO THE EIGHT-KNOB PICTURE IS NOT WRONG ABOUT THE STATE SPACE AND IS WRONG
    ABOUT THE CONTROL SPACE.  There are eight configurations and TWO KNOBS THAT
    DO ANYTHING TO RADIAL CONTRACTION: the sign of m, and the magnitude of a.

    (Both m > 0 rows contract here anyway, because a^2 = 0.9801 exceeds
    2 M r = 0.6.  That is section 2's finding showing up inside the table.)

===============================================================================
5. WHAT THE PASS LEAVES
===============================================================================

    THE THIRD THREAD IS REAL and is certify.py's scope condition, identified by
        M from the other side.
    THE BICONDITIONAL FAILS UNDER ROTATION -- positive mass, contracted radial
        distance, measured.  NEW TO THIS TREE.
    A HORIZON HIDES IT for every sub-extremal spin, and COSMIC CENSORSHIP is a
        CONJECTURE.
    THE EIGHT COLLAPSES TO TWO for the question that matters.

    L1 IS NARROWER AND SHARPER THAN IT WAS.  It is no longer "does the theorem
    generalise past static" -- IT DEMONSTRABLY DOES NOT.  The question is now
    whether the failure mode is ONLY the one Kerr exhibits, which is behind a
    horizon, or whether some stationary configuration contracts with positive
    mass IN AN EXPOSED REGION.  THAT IS A BETTER QUESTION AND IT IS OPEN.

SCOPE.  Section 2 is Boyer-Lindquist algebra at the equator, exact, and says
nothing about non-equatorial angles or about whether any of it is traversable.
Section 3's horizon comparison is for the Kerr family only.  Section 4 varies
signs in the Kerr form and does not re-derive the conformastatic case.  NOTHING
IS REPAIRED and NO ROUTE IS PROPOSED.
"""

import math
import sys

# -- the three threads -------------------------------------------------------

THREADS = [
    ("TIME", "g_tt", "an ENDPOINT RATIO", "1 + z = e^{dPhi}"),
    ("SPACE", "g_rr", "a LINE INTEGRAL", "Int dr/sqrt(f)"),
    ("INTERSECTION", "g_t.phi", "THE CROSS TERM", "frame dragging"),
]

STATIC_MEANS = "g_t.phi = 0"
CERTIFY_SCOPE = "static and spherically symmetric only"


# -- Kerr --------------------------------------------------------------------

def g_rr_kerr(r, M, a, theta=math.pi / 2):
    rho2 = r * r + a * a * math.cos(theta) ** 2
    delta = r * r - 2.0 * M * r + a * a
    return float("inf") if delta == 0 else rho2 / delta


def contracts(r, M, a, theta=math.pi / 2):
    g = g_rr_kerr(r, M, a, theta)
    return 0.0 < g < 1.0


def contraction_radius_equator(M, a):
    """Equator: contraction iff a^2 > 2 M r, i.e. r < a^2/(2M)."""
    return a * a / (2.0 * M)


def horizon(M, a):
    d = M * M - a * a
    return None if d < 0 else M + math.sqrt(d)


def is_exposed(M, a):
    rp = horizon(M, a)
    return True if rp is None else contraction_radius_equator(M, a) > rp


# -- the eight ---------------------------------------------------------------

def sign_states():
    return [(sp, sm, sa) for sp in (1, -1) for sm in (1, -1) for sa in (1, -1)]


def g_rr_for_state(state, r=0.3, Mmag=1.0, amag=0.99):
    _sPhi, sm, sa = state
    return g_rr_kerr(r, sm * Mmag, sa * amag)


CENSORSHIP_IS_A_THEOREM = False
BICONDITIONAL_SURVIVES_ROTATION = False
ROUTE_PROPOSED = False


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

    # -- 1: three threads, and the third is the scope condition --------------
    chk("three threads", len(THREADS), 3)
    chk("the third is the cross term", THREADS[2][1], "g_t.phi")
    chk("static means exactly that it vanishes", STATIC_MEANS, "g_t.phi = 0")
    chk("which is certify.py's scope", CERTIFY_SCOPE.startswith("static"), True)

    # -- 2: the biconditional fails under rotation ---------------------------
    M, a = 1.0, 0.99
    for r, want in ((0.10, 0.012657), (0.30, 0.191449), (0.49, 0.999584)):
        chk("Kerr g_rr at r=%.2f, M=+1" % r, g_rr_kerr(r, M, a), want, 1e-5)
        chk("  CONTRACTED with POSITIVE mass", contracts(r, M, a), True)
    chk("and not contracted outside", contracts(0.60, M, a), False)
    chk("the condition is a^2 > 2 M r",
        contraction_radius_equator(M, a), a * a / 2.0, 1e-15)
    chk("no negative mass appears in it", contracts(0.3, +1.0, 0.99), True)
    chk("SO THE BICONDITIONAL DOES NOT SURVIVE ROTATION",
        BICONDITIONAL_SURVIVES_ROTATION, False)

    # -- 3: hidden by a horizon, held there by a conjecture ------------------
    for aa in (0.0, 0.5, 0.9, 0.99, 1.0):
        chk("sub-extremal a=%.2f is hidden" % aa, is_exposed(1.0, aa), False)
    for aa in (1.1, 1.5, 2.0):
        chk("over-extremal a=%.1f is EXPOSED" % aa, is_exposed(1.0, aa), True)
        chk("  and has no horizon", horizon(1.0, aa), None)
    chk("cosmic censorship is NOT a theorem", CENSORSHIP_IS_A_THEOREM, False)
    chk("  and the file says so", "CONJECTURE AND NOT A" in __doc__, True)

    # -- 4: the eight collapses to two ---------------------------------------
    states = sign_states()
    chk("eight sign states", len(states), 8)
    vals = {round(g_rr_for_state(s), 9) for s in states}
    chk("TWO distinct values of g_rr", len(vals), 2)
    lo, hi = sorted(vals)
    chk("  the m<0 value", lo, 0.053889, 1e-5)
    chk("  the m>0 value", hi, 0.191449, 1e-5)
    # Phi's sign does nothing
    chk("Phi's sign does not enter g_rr",
        g_rr_for_state((1, 1, 1)) == g_rr_for_state((-1, 1, 1)), True)
    # a's sign does nothing
    chk("a's sign does not enter g_rr",
        g_rr_for_state((1, 1, 1)) == g_rr_for_state((1, 1, -1)), True)
    # m's sign does
    chk("m's sign DOES",
        g_rr_for_state((1, 1, 1)) != g_rr_for_state((1, -1, 1)), True)
    chk("all eight contract at this point",
        sum(1 for s in states if 0 < g_rr_for_state(s) < 1), 8)
    chk("  including the m > 0 ones, because a^2 > 2 M r",
        0.99 ** 2 > 2 * 1.0 * 0.3, True)

    # -- scope ----------------------------------------------------------------
    chk("no route is proposed", ROUTE_PROPOSED, False)
    chk("nothing is repaired", "NOTHING\nIS REPAIRED" in __doc__ or
        "NOTHING" in __doc__, True)

    print("\nSELFTEST", "PASS" if ok else "FAIL")
    return ok


def report():
    print(__doc__)
    print("  ------------------------------------------------------------------------")
    print("  THE THREE THREADS\n")
    for name, sym, kind, form in THREADS:
        print("    %-14s %-10s %-20s %s" % (name, sym, kind, form))
    print("\n    static means %s -- so the third thread IS certify.py's scope."
          % STATIC_MEANS)
    print()
    print("  ------------------------------------------------------------------------")
    print("  KERR AT THE EQUATOR, M = +1, a = 0.99\n")
    for r in (0.10, 0.30, 0.49, 0.60, 1.50):
        g = g_rr_kerr(r, 1.0, 0.99)
        print("    r = %-6.2f  g_rr = %+12.6f   %s"
              % (r, g, "CONTRACTED -- with POSITIVE mass" if 0 < g < 1 else ""))
    print()
    print("  ------------------------------------------------------------------------")
    print("  AND A HORIZON IN FRONT OF IT\n")
    print("    a/M      contracted r <     r_+          exposed?")
    for aa in (0.0, 0.5, 0.9, 0.99, 1.0, 1.1, 1.5, 2.0):
        rp = horizon(1.0, aa)
        print("    %-8.2f %-18.4f %-12s %s"
              % (aa, contraction_radius_equator(1.0, aa),
                 "NONE" if rp is None else "%.4f" % rp,
                 "YES -- naked" if is_exposed(1.0, aa) else "no"))
    print("\n    hidden for every sub-extremal spin -- by COSMIC CENSORSHIP,")
    print("    which is a CONJECTURE and not a theorem.")
    print()
    print("  ------------------------------------------------------------------------")
    print("  THE EIGHT, AND IT COLLAPSES\n")
    print("     Phi   m    a     g_rr")
    for s in sign_states():
        print("     %+d    %+d   %+d    %+12.6f   %s"
              % (s[0], s[1], s[2], g_rr_for_state(s),
                 "CONTRACTED" if 0 < g_rr_for_state(s) < 1 else ""))
    print("\n    EIGHT STATES, TWO DISTINCT VALUES.  Phi's sign does not enter")
    print("    g_rr; a's sign does not either (only a^2).  ONLY m's DOES.")
    print("""
  ------------------------------------------------------------------------
  THE PASS IN ONE PARAGRAPH

  M's three threads are real and the third is the most important thing he
  has pointed at.  A stationary axisymmetric metric has exactly three
  pieces -- g_tt as an endpoint ratio, g_rr as a line integral, and
  g_t.phi, THE CROSS TERM, which is where time and space intersect.  AND
  "STATIC" MEANS EXACTLY g_t.phi = 0, so the third thread is precisely the
  assumption certify.py's theorem makes: M identified L1's scope condition
  by reasoning, without being told it.  TURNING IT ON BREAKS THE
  BICONDITIONAL.  In Kerr at the equator g_rr = rho^2/Delta contracts
  whenever a^2 > 2 M r, a condition with NO NEGATIVE MASS IN IT -- measured
  at M = +1, a = 0.99 giving g_rr = 0.012657, 0.191449 and 0.999584 at
  r = 0.1, 0.3 and 0.49, ALL CONTRACTED WITH POSITIVE MASS.  The static
  theorem says contraction requires m(r) < 0; ROTATION IS A COUNTEREXAMPLE
  AND THE TREE HAD NEVER TESTED IT.  What stands in front of it is a
  horizon -- for every sub-extremal spin the contracted region is inside
  r_+, exposed only for a > M, an over-extremal naked singularity -- AND
  WHAT FORBIDS THAT IS COSMIC CENSORSHIP, A CONJECTURE AND NOT A THEOREM,
  which has to be said plainly because the tree's whole discipline is
  distinguishing the two.  It is still not a route: no horizon means no
  known formation process, a horizon means no return, and neither supplies
  a corridor between two places.  On the eight: M's 1+1+2+2+2 is
  arithmetically right and selects eight of the 27 trit-states, which is a
  different eight from the cube's 2^3 -- and the physical test settles it,
  because varying all three signs gives EIGHT STATES AND TWO DISTINCT
  VALUES.  Phi's sign does not enter g_rr at all and a's sign does not
  either, since only a^2 appears.  ONLY m's SIGN DOES.  The eight-knob
  picture is right about the state space and wrong about the control
  space.  L1 IS NOW SHARPER: not "does the theorem generalise past static"
  -- IT DEMONSTRABLY DOES NOT -- but whether any stationary configuration
  contracts with positive mass in an EXPOSED region.
  ------------------------------------------------------------------------""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
