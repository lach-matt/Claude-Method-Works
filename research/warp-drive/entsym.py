#!/usr/bin/env python3
"""
entsym.py -- "the symmetric relation is precisely what quantum entanglement
provides."

The instinct finds a real meeting point, and it is a theorem rather than an
analogy.  But the correspondence DOES NOT TRANSFER, and the reason is one this
tree has now hit three times in three vocabularies.

===============================================================================
1. TWO SYMMETRIES, AND THEY ARE NOT THE SAME THEOREM
===============================================================================

    CONJUGACY SYMMETRY, which is what reversal.py invoked.  The optical tidal
        matrix T is symmetric, so the Jacobi operator A'' = -T A is
        self-adjoint, so "p is conjugate to q" is a symmetric relation.
        IT RELATES TWO POINTS ON ONE GEODESIC.

    ENTANGLEMENT SYMMETRY.  A global pure state gives S_A = S_B for a region
        and its complement; mutual information is symmetric; Tomita-Takesaki
        makes the modular Hamiltonian self-adjoint by construction.
        IT RELATES TWO SUBSYSTEMS.

    SAME WORD.  DIFFERENT OBJECTS ON EACH SIDE OF THE RELATION.  Saying both
    are "symmetric" is true and is not yet an argument, and this file will not
    build one on it.

===============================================================================
2. BUT THEY DO MEET, AND AT A THEOREM: QNEC
===============================================================================

        <T_kk>  >=  (hbar c / 2 pi) S''

The left-hand side is exactly what drives the Jacobi equation.  The right-hand
side is entanglement curvature along the ray.  That is not a resemblance -- it
is an inequality, it is already in this tree, and entangle.py inverted it to
get the corridor's entropy requirement.

    SO THE INSTINCT IS POINTING AT SOMETHING REAL.  The question is what the
    meeting actually says.

===============================================================================
3. AND WHAT IT SAYS IS: QNEC HAS NO WEYL TERM
===============================================================================

QNEC bounds T_kk -- the RICCI-sourced part -- and nothing else.  Weyl does not
appear in it, anywhere, in any form.

    IN VACUUM T_kk = 0 IDENTICALLY.  QNEC then reads 0 >= (hbar c/2pi) S'',
    i.e. S'' <= 0, and it is SATISFIED.  And composite.py, in that same
    vacuum, MEASURES A CONJUGATE POINT AT 56.50 -- pure Weyl focusing, with
    QNEC satisfied and entirely indifferent to it.

        THE ENTANGLEMENT BOUND IS SILENT ABOUT THE CHANNEL THAT SEATS.

===============================================================================
4. WHICH LANDS IT ON THE HALF THAT WAS ALREADY FREE
===============================================================================

reverse.py split the device and the halves do not cost the same:

        THE SEAT          free -- Weyl, sign-blind, no density requirement,
                          observed at 550 AU
        THE CONTRACTION   all of it -- needs Phi > 0, hence rho < 0

    QNEC is SILENT on the first (no Weyl term) and BINDING on the second (the
    core's T_kk is exactly what it bounds -- entangle.py's 2 pi^2).

        ENTANGLEMENT'S SYMMETRIC RELATION IS ABSENT FROM THE HALF THAT COSTS
        AND SUPERFLUOUS ON THE HALF THAT IS FREE.

    That is the same decomposition reverse.py found, arrived at from the
    entanglement side, which is worth something as a cross-check and nothing
    as a route.

===============================================================================
5. AND GJW SHOWS WHAT THE SYMMETRIC RELATION NEEDS: TWO SYSTEMS
===============================================================================

Their coupling is explicitly bipartite --

        dS = INT dt d^{d-1}x  h(t,x) O_R(t,x) O_L(-t,x)

-- L and R, two boundaries, thermofield-double entangled, and THAT symmetry
does real work: it is what makes their wormhole traversable.  Entanglement
earns its keep there because there are two systems for it to be symmetric
between.

    THE CORRIDOR HAS NO THROAT.  transition.py measures the areal radius
    MONOTONE at every radius, so the topology is R^3 and there are not two
    boundaries.  A and B are two POINTS IN ONE CONNECTED REGION.

    The natural entanglement cut -- corridor against exterior -- is a
    DIFFERENT CUT from the A-to-B endpoint pair: A and B lie on the SAME SIDE
    of it.  So the bipartition entanglement would use does not pair the two
    ends the transition pairs.

===============================================================================
6. THE SAME OBSTRUCTION, THIRD VOCABULARY
===============================================================================

        MTY            needs two ends to age differentially      -- no throat
        GJW            needs two boundaries to couple            -- no throat
        ENTANGLEMENT   needs two subsystems to be symmetric      -- no throat

    THREE ROUTES, ONE MISSING STRUCTURE.  The conjugate pair is two points on
    ONE geodesic, and that is a different kind of pair from an entangled one.

===============================================================================
AND THE CHOICE THIS PUTS TO M, WHICH IS M'S TO MAKE
===============================================================================

M's standing instruction: "don't associate my theory of warp transition with
worm holes or black holes."  anecscope.py, dichotomy.py and this file all turn
on the corridor having NO THROAT -- which is exactly what honours that
instruction, and exactly what denies the entanglement route its bipartition.

    THE ENTANGLEMENT ROUTE AND THE NO-WORMHOLE CONSTRAINT ARE IN DIRECT
    TENSION.  Not a contradiction in the physics -- a fork in the
    architecture.  A throat would supply the two systems entanglement needs
    and would make the object a wormhole.  This file states the fork and does
    not choose it; the scoping was M's and so is the trade.

stdlib only.  entangle.py supplies QNEC, composite.py the vacuum seat,
transition.py the topology, reverse.py the split.
"""
import math, sys


# ------------------------------------------- 1: the two symmetries, kept apart

SYMMETRIES = (
    ("conjugacy", "T is symmetric -> the Jacobi operator is self-adjoint",
     "two POINTS on one geodesic"),
    ("entanglement", "a global pure state -> S_A = S_B; modular flow is "
     "self-adjoint by construction", "two SUBSYSTEMS"),
)


def relates(name):
    return [s[2] for s in SYMMETRIES if s[0] == name][0]


def same_relata():
    """Do the two symmetries relate the same kind of thing?  No."""
    return relates("conjugacy") == relates("entanglement")


# ---------------------------------------------------- 2/3: QNEC, and its scope

def qnec_terms():
    """What appears in <T_kk> >= (hbar c/2pi) S''.  Weyl is not among them."""
    return ("T_kk (Ricci-sourced)", "S'' (entanglement curvature)")


def qnec_contains_weyl():
    return any("weyl" in t.lower() for t in qnec_terms())


def vacuum_tkk():
    """R_kk = 0 identically, so QNEC reads S'' <= 0 and is satisfied."""
    return 0.0


def vacuum_seats():
    """And composite.py measures a conjugate point there anyway.  Pure Weyl."""
    import composite
    return composite.survey(-2.0e-3)["conjugate"]


def qnec_is_silent_on_the_seat():
    """Satisfied in vacuum, and the focusing happens regardless."""
    return (not qnec_contains_weyl()) and vacuum_tkk() == 0.0 and vacuum_seats() is not None


# ------------------------------------------ 4: which half the bound lands on

HALVES = (
    ("the seat", "free", "Weyl, sign-blind, observed at 550 AU", "SILENT"),
    ("the contraction", "all of it", "needs Phi > 0 hence rho < 0", "BINDING"),
)


def qnec_binds(half):
    return [h[3] for h in HALVES if h[0] == half][0]


def lands_on_the_free_half():
    return qnec_binds("the seat") == "SILENT" and \
        qnec_binds("the contraction") == "BINDING"


# ------------------------------------- 5/6: what the relation needs, and the gap

def corridor_has_throat(m=2.0e-2):
    import transition, concentric
    phi = concentric.potential(m)
    return transition.has_throat(phi, [0.05 * i for i in range(1, 4001)])


GJW_COUPLING = "INT dt d^{d-1}x h(t,x) O_R(t,x) O_L(-t,x)"


def gjw_is_bipartite():
    """O_L and O_R: two boundaries, and the symmetry does real work there."""
    return "O_R" in GJW_COUPLING and "O_L" in GJW_COUPLING


ROUTES_NEEDING_TWO = (
    ("MTY", "two ends to age differentially"),
    ("GJW", "two boundaries to couple"),
    ("entanglement", "two subsystems to be symmetric between"),
)


def all_blocked_by_the_same_thing():
    """Three routes, one missing structure: the throat."""
    return not corridor_has_throat() and len(ROUTES_NEEDING_TWO) == 3


# --------------------------------------------------------- the fork, unchosen

NO_WORMHOLE_IS_M_S_SCOPING = True
FORK = ("a throat would supply the two systems entanglement needs, and would "
        "make the object a wormhole")
CHOSEN_HERE = None                   # M's scoping, M's trade


# ------------------------------------------------------------------ selftest

def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-56s %18s %18s  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("1. TWO SYMMETRIES, AND THEY ARE NOT THE SAME THEOREM")
    for n, why, what in SYMMETRIES:
        print("      %-14s relates %-24s  (%s)" % (n, what, why[:38]))
    chk("do they relate the same kind of thing", same_relata(), False)
    print("      same word; different objects on each side of the relation.")

    print("\n2/3. BUT THEY MEET AT QNEC -- and QNEC HAS NO WEYL TERM")
    print("      <T_kk> >= (hbar c/2 pi) S''   terms: %s" % (qnec_terms(),))
    chk("QNEC contains a Weyl term", qnec_contains_weyl(), False)
    chk("in vacuum T_kk is exactly", vacuum_tkk(), 0.0)
    print("      so QNEC reads S'' <= 0 and IS SATISFIED -- and composite.py")
    print("      seats a conjugate point at %.2f in that same vacuum." % vacuum_seats())
    chk("QNEC is silent on the channel that seats",
        qnec_is_silent_on_the_seat(), True)

    print("\n4. SO IT LANDS ON THE HALF THAT WAS ALREADY FREE")
    for n, cost, why, bound in HALVES:
        print("      %-18s %-10s QNEC: %s" % (n, cost, bound))
    chk("silent on the free half, binding on the costly one",
        lands_on_the_free_half(), True)
    print("      the same split reverse.py found, from the entanglement side --")
    print("      worth something as a cross-check, nothing as a route.")

    print("\n5/6. WHAT THE RELATION NEEDS: TWO SYSTEMS")
    chk("GJW's coupling is bipartite (O_L, O_R)", gjw_is_bipartite(), True)
    chk("the corridor has a throat", corridor_has_throat(), False)
    for n, needs in ROUTES_NEEDING_TWO:
        print("      %-14s needs %-42s -- no throat" % (n, needs))
    chk("three routes, one missing structure", all_blocked_by_the_same_thing(), True)
    print("      A and B are two POINTS IN ONE REGION.  The natural")
    print("      entanglement cut puts them on the SAME SIDE of it.")

    print("\nTHE FORK, STATED AND NOT CHOSEN")
    chk("no-wormhole is M's scoping", NO_WORMHOLE_IS_M_S_SCOPING, True)
    chk("this file chooses", CHOSEN_HERE, None)
    print("      %s" % FORK)

    print("\n  SELFTEST " + ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    print("""VERDICT

  THE INSTINCT FINDS A REAL MEETING POINT AND IT IS A THEOREM, NOT AN
  ANALOGY: QNEC, <T_kk> >= (hbar c/2 pi) S'', whose left side drives
  the Jacobi equation and whose right side is entanglement curvature.

  BUT THE TWO SYMMETRIES ARE NOT THE SAME THEOREM.  Conjugacy is
  symmetric because T is symmetric, and it relates TWO POINTS ON ONE
  GEODESIC.  Entanglement is symmetric because the global state is
  pure, and it relates TWO SUBSYSTEMS.  Same word, different objects
  on each side.

  AND THE MEETING POINT SAYS SOMETHING UNFAVOURABLE.  QNEC BOUNDS
  T_kk AND CONTAINS NO WEYL TERM AT ALL.  In vacuum T_kk = 0, QNEC
  reads S'' <= 0 and is satisfied, and composite.py seats a conjugate
  point at 56.50 there anyway -- pure Weyl, with the entanglement
  bound indifferent.  So entanglement is SILENT on the seat, which
  reverse.py already showed is free, and BINDING on the contraction,
  which is where all the cost lives.  It lands on the half that was
  never the problem.

  AND GJW SHOWS WHAT THE RELATION NEEDS.  Their coupling is
  explicitly bipartite -- O_L against O_R, two boundaries,
  thermofield-double entangled -- and that symmetry does real work
  because there are two systems for it to be symmetric between.  The
  corridor has NO THROAT: the areal radius is monotone at every
  radius, A and B are two points in one connected region, and the
  natural entanglement cut puts them on the same side of it.

  THREE ROUTES, ONE MISSING STRUCTURE.  MTY needs two ends to age
  differentially, GJW needs two boundaries to couple, entanglement
  needs two subsystems to be symmetric between.  All three want a
  throat.

  WHICH PUTS A FORK TO M RATHER THAN AN ANSWER.  "Don't associate my
  theory with worm holes" is what makes the corridor throatless, and
  throatlessness is exactly what denies entanglement its
  bipartition.  A throat would supply the two systems and would make
  the object a wormhole.  That is a choice about architecture, not a
  fact about physics, and it is not this file's to make.""")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report()
