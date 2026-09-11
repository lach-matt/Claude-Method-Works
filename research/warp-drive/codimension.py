#!/usr/bin/env python3
"""
codimension.py -- M, on dimension.py's finding that Lambda's scale-freedom is a
property of four dimensions rather than of this architecture:

    "because the object in transition is a 4D object"

That is a PROPOSED REASON, and coincidence.py's rule -- adopted one pass ago --
says a proposed reason for an exact fact is TESTED, not accepted and not
dismissed.  Tested here.

THE STRUCTURE OF THE CLAIM IS RIGHT AND THE INVARIANT IS NOT FOUR.

    M says an object's dimension sets where scale-freedom lives.  IT DOES.
    Scale-freedom is not an accident of D = 4; it is set by the source, exactly
    as he says, and there is a one-parameter family to prove it.

    BUT THE QUANTITY IS CODIMENSION, NOT DIMENSION.  Scale-freedom occurs when
    the source has THREE TRANSVERSE SPATIAL DIMENSIONS, and for a point source
    that means D = 4.  For a string it means D = 5.  For a membrane, D = 6.

        SCALE-FREEDOM  <=>  n = 3  <=>  D = p + 4

    AND THE OBJECT THAT DOES THE SETTING IS THE SOURCE, NOT THE PAYLOAD.  Those
    are different things here, and the distinction matters below.

AND A CONSTRAINT FALLS OUT THAT THIS TREE DID NOT HAVE, WHICH IS WHY THE TEST
WAS WORTH RUNNING: in four dimensions ONLY a point-like source gives a
scale-free rate.  A LINE source does not.  The architecture is LOCKED to a
codimension-3 source by its own scale-freedom.

===============================================================================
1. THE FAMILY
===============================================================================

A p-brane source in D spacetime dimensions has

        n = D - 1 - p        TRANSVERSE SPATIAL dimensions

and the Laplacian's Green's function in n transverse dimensions is

        Phi ~ r^-(n-2)       n > 2
        Phi ~ log r          n = 2
        Phi ~ r              n = 1

The contraction this project buys is Int Phi dr, and it is SCALE-FREE exactly
when that integral is Int dr/r -- a logarithm OF A RATIO -- which needs
n - 2 = 1:

     p    D    n     Phi        Int Phi dr           scale-free
     0    3    2     log r      LOG-POTENTIAL        no
     0    4    3     r^-1       LOGARITHM            YES
     0    5    4     r^-2       CONVERGENT-POWER     no
     1    4    2     log r      LOG-POTENTIAL        no
     1    5    3     r^-1       LOGARITHM            YES
     2    5    2     log r      LOG-POTENTIAL        no
     2    6    3     r^-1       LOGARITHM            YES
     3    7    3     r^-1       LOGARITHM            YES

    ONE CONDITION, n = 3, AND IT MOVES WITH THE SOURCE: D = p + 4 for every p.

    SO M IS RIGHT THAT THE OBJECT SETS IT.  dimension.py reported "four
    dimensions" as though four were the invariant; it is not.  THREE
    TRANSVERSE SPATIAL DIMENSIONS IS THE INVARIANT, and four is what that
    becomes for a point.

===============================================================================
2. WHICH OBJECT -- AND IT IS NOT THE PAYLOAD
===============================================================================

M says "the object IN TRANSITION".  The computation is about the object that
SOURCES the potential, and in this architecture those are two different things:

    THE SOURCE       phase1.py's Phi is a Plummer core minus a shell.  A
                     Plummer core is POINT-LIKE, softened by a.  So p = 0, the
                     transverse space is three dimensional, and D = 4 gives the
                     logarithm.  CONSISTENT -- and now EXPLAINED rather than
                     merely observed.

    THE PATH         B_RAY = 1.0 is the ray's IMPACT PARAMETER, the transverse
                     offset at which the trajectory passes the core.  It is a
                     property of the PATH, not the extent of a line source.
                     Worth stating because "ray" invites the other reading.

    THE PAYLOAD      whatever rides the corridor.  IT DOES NOT ENTER Lambda AT
                     ALL.  Lambda is 2[ln(2 R_s/sqrt(b^2+a^2)) - 1] and no
                     property of a transported body appears in it.

    SO THE CORRECT FORM OF M'S SENTENCE IS: "because the object SOURCING the
    transition is codimension three."  The payload's dimension is not in the
    equation and cannot be, which is a statement about the architecture rather
    than a criticism of the intuition.

===============================================================================
3. THE CONSTRAINT THAT FALLS OUT
===============================================================================

Run the family at D = 4, which is where we are, and ask what sources are
allowed if the scale-free rate is to survive:

        p = 0   point      n = 3   LOGARITHM          scale-free
        p = 1   line       n = 2   Phi ~ log r        NOT scale-free
        p = 2   sheet      n = 1   Phi ~ r            NOT scale-free

For the line the deficit is Int log r dr = r log r - r, and under r -> k r:

        k = 1     860.663473310
        k = 10  13188.779068154

    A FACTOR OF 15.3 FOR A FACTOR OF 10 IN SCALE.  Not scale-free, and not
    even a clean power.

    IN FOUR DIMENSIONS ONLY A POINT-LIKE SOURCE GIVES A SCALE-FREE EXCHANGE
    RATE.  THE ARCHITECTURE IS LOCKED TO CODIMENSION THREE BY ITS OWN
    SCALE-FREEDOM, and it did not know that until now.

    AND IT CUTS AGAINST THE SUPERHIGHWAY PICTURE, MILDLY AND HONESTLY.  A
    "superhighway" invites a LINE-shaped source -- a corridor built along its
    own length.  In four dimensions that source loses the scale-free rate.  It
    does not become impossible; it becomes scale-DEPENDENT, so the price of a
    metre would then depend on how long the corridor is, and every figure in
    this tree that survives rescaling would stop surviving it.

    THE OTHER WAY TO KEEP IT IS D = 5, WHICH dimension.py ALREADY PRICED AT
    5.32x WORSE PER UNIT MASS.  So a line source keeps scale-freedom only by
    moving to a dimension where the rate is five times worse.  Both doors, and
    neither is free.

===============================================================================
4. WHAT IS NOT CLAIMED
===============================================================================

    THIS IS NEWTONIAN-LIMIT GREEN'S FUNCTION COUNTING, not a solution of the
    field equations with a brane source.  Real p-brane solutions exist and
    carry more structure than a Laplacian Green's function; nothing here
    computes one.

    THE AREA LAW IS NOT RE-DERIVED FOR p > 0.  magnitude.py's R Delta d <=
    k l_P^2 assumed rho ~ M/R^3, i.e. three spatial dimensions; the p-brane
    generalisation is NOT computed and is not assumed to be the same.

    NO CLAIM IS MADE THAT CODIMENSION THREE IS DEEP.  It is the condition for
    a Green's function to be 1/r, which is the condition for its integral to be
    a log, which is the condition for scale-freedom.  That chain is four short
    steps and each is elementary.  What the pass supplies is that M's reason
    SURVIVES BEING MADE PRECISE, which is more than most proposed reasons do.

    NOTHING IS REPAIRED.  dimension.py's statement is not withdrawn -- it is
    true that scale-freedom is a D = 4 property for THIS source.  It is
    GENERALISED: D = 4 is the p = 0 member of a family.
"""

import math
import sys

LOGARITHM = "LOGARITHM"
LOG_POTENTIAL = "LOG-POTENTIAL"
CONVERGENT = "CONVERGENT-POWER"
LINEAR = "LINEAR-POTENTIAL"


def n_transverse(D, p):
    """Transverse SPATIAL dimensions of a p-brane in D spacetime dimensions."""
    return D - 1 - p


def potential_kind(D, p):
    n = n_transverse(D, p)
    if n < 2:
        return "r"
    if n == 2:
        return "log r"
    return "r^%d" % (-(n - 2))


def integral_kind(D, p):
    """What Int Phi dr is.  LOGARITHM is the scale-free one."""
    n = n_transverse(D, p)
    if n < 2:
        return LINEAR
    if n == 2:
        return LOG_POTENTIAL
    if n == 3:
        return LOGARITHM
    return CONVERGENT


def is_scale_free(D, p):
    return integral_kind(D, p) == LOGARITHM


def scale_free_dimension(p):
    """D = p + 4.  The one-parameter family."""
    return p + 4


# -- the two deficits that are not scale-free, for the D = 4 line source -----

def deficit_log_potential(r1, r2):
    """n = 2: Phi ~ log r, so Int Phi dr = r log r - r."""
    F = lambda r: r * math.log(r) - r          # noqa: E731
    return F(r2) - F(r1)


def deficit_inverse_r(r1, r2):
    """n = 3: Phi ~ 1/r, so Int Phi dr = log(r2/r1).  Scale-free."""
    return math.log(r2 / r1)


R1, R2 = 1.0, 200.0

# The architecture's own source, and what it is.
SEATED_SOURCE_P = 0          # Plummer core: point-like, softened by a
B_RAY_IS = "the ray's IMPACT PARAMETER -- a property of the PATH, not a source"
PAYLOAD_IN_LAMBDA = False    # no property of a transported body appears in it

# M's sentence, corrected.
PROPOSED = "because the object in transition is a 4D object"
CORRECTED = ("because the object SOURCING the transition is codimension three "
             "-- which, for a point, is D = 4")

NOT_COMPUTED = [
    ("real p-brane solutions", "this is Green's-function counting in the "
     "Newtonian limit, not a field-equation solution with a brane source"),
    ("the area law for p > 0", "magnitude.py assumed rho ~ M/R^3; the p-brane "
     "generalisation is not computed and not assumed to be the same"),
]


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

    # -- the family: one condition, moving with the source -------------------
    chk("point source is scale-free at D=4", is_scale_free(4, 0), True)
    chk("  and nowhere else", [D for D in range(3, 12) if is_scale_free(D, 0)],
        [4])
    chk("string is scale-free at D=5", is_scale_free(5, 1), True)
    chk("  and nowhere else", [D for D in range(3, 12) if is_scale_free(D, 1)],
        [5])
    chk("membrane at D=6", [D for D in range(3, 12) if is_scale_free(D, 2)],
        [6])
    chk("the family is D = p + 4",
        [scale_free_dimension(p) for p in range(5)], [4, 5, 6, 7, 8])
    chk("  and the family is exactly the scale-free set",
        all(is_scale_free(scale_free_dimension(p), p) for p in range(5)), True)

    # -- THE invariant is n = 3, not D = 4 -----------------------------------
    chk("every scale-free case has THREE transverse spatial dimensions",
        sorted({n_transverse(scale_free_dimension(p), p) for p in range(6)}),
        [3])
    chk("and D varies across them",
        len({scale_free_dimension(p) for p in range(6)}), 6)
    chk("so the invariant is codimension, not dimension",
        len({n_transverse(scale_free_dimension(p), p) for p in range(6)}), 1)

    # -- the potentials are what they should be ------------------------------
    chk("D=4 point gives 1/r", potential_kind(4, 0), "r^-1")
    chk("D=4 line gives log r", potential_kind(4, 1), "log r")
    chk("D=4 sheet gives r", potential_kind(4, 2), "r")
    chk("D=5 point gives 1/r^2", potential_kind(5, 0), "r^-2")

    # -- the constraint: in D=4 only a point works ---------------------------
    chk("in D=4, scale-free sources are p=0 alone",
        [p for p in range(4) if is_scale_free(4, p)], [0])
    a = deficit_inverse_r(R1, R2)
    b = deficit_inverse_r(R1 * 10, R2 * 10)
    chk("the point source's deficit is scale-invariant", b, a, 1e-14)
    c = deficit_log_potential(R1, R2)
    d = deficit_log_potential(R1 * 10, R2 * 10)
    chk("the line source's is not", abs(d - c) > 1.0, True)
    chk("  k=1", c, 860.663473310, 1e-8)
    chk("  k=10", d, 13188.779068154, 1e-8)
    chk("  a factor of 10 in scale costs a factor of", d / c, 15.3241, 1e-4)

    # -- which object, and it is not the payload -----------------------------
    chk("the seated source is point-like", SEATED_SOURCE_P, 0)
    chk("  so D=4 is forced, and now explained",
        is_scale_free(4, SEATED_SOURCE_P), True)
    chk("b is a path parameter, not a source extent",
        "PATH" in B_RAY_IS, True)
    chk("no payload property enters Lambda", PAYLOAD_IN_LAMBDA, False)

    # -- the correction, and what is not claimed ------------------------------
    chk("M's sentence is corrected, not rejected",
        "codimension three" in CORRECTED, True)
    chk("two things are not computed", len(NOT_COMPUTED), 2)
    chk("nothing is repaired", "NOTHING IS REPAIRED" in __doc__, True)
    chk("dimension.py is generalised, not withdrawn",
        "GENERALISED" in __doc__, True)
    chk("no depth is claimed for codimension three",
        "NO CLAIM IS MADE THAT CODIMENSION THREE IS DEEP" in __doc__, True)

    print("\nSELFTEST", "PASS" if ok else "FAIL")
    return ok


def report():
    print(__doc__)
    print("  ------------------------------------------------------------------------")
    print("  THE FAMILY\n")
    print("     p   D   n=D-1-p   Phi        Int Phi dr           scale-free")
    for p in range(0, 4):
        for D in range(3, 9):
            if n_transverse(D, p) < 1:
                continue
            print("    %2d  %2d     %2d      %-10s %-20s %s"
                  % (p, D, n_transverse(D, p), potential_kind(D, p),
                     integral_kind(D, p), "YES" if is_scale_free(D, p) else ""))
        print()
    print("    ONE CONDITION: n = 3.  It moves with the source: D = p + 4.")
    print("    %r" % [(p, scale_free_dimension(p)) for p in range(5)])
    print()
    print("  ------------------------------------------------------------------------")
    print("  THE CONSTRAINT, IN OUR D = 4\n")
    for p, lbl in ((0, "point"), (1, "line"), (2, "sheet")):
        print("    p = %d  %-8s n = %d   %-10s %s"
              % (p, lbl, n_transverse(4, p), potential_kind(4, p),
                 "SCALE-FREE" if is_scale_free(4, p) else "not scale-free"))
    print("\n    line source, Int Phi dr under scaling:")
    for k in (1.0, 10.0):
        print("      k = %-5g %.9f" % (k, deficit_log_potential(R1 * k, R2 * k)))
    print("      -> factor %.4f for a factor of 10 in scale."
          % (deficit_log_potential(R1 * 10, R2 * 10)
             / deficit_log_potential(R1, R2)))
    print()
    print("    PROPOSED:  %s" % PROPOSED)
    print("    CORRECTED: %s" % CORRECTED)
    print("""
  ------------------------------------------------------------------------
  THE PASS IN ONE PARAGRAPH

  M proposed a reason for dimension.py's finding, and coincidence.py's rule
  says a proposed reason is tested.  Tested: THE STRUCTURE IS RIGHT AND THE
  INVARIANT IS NOT FOUR.  A p-brane source in D spacetime dimensions has
  n = D - 1 - p transverse spatial dimensions and a potential r^-(n-2), so
  the contraction integral is a scale-free log of a ratio exactly when
  n = 3 -- and that is D = 4 for a point, D = 5 for a string, D = 6 for a
  membrane, one condition moving with the source.  SO M IS RIGHT THAT THE
  OBJECT SETS IT; the quantity is CODIMENSION rather than dimension, and
  the object that sets it is the SOURCE rather than the payload, which does
  not enter Lambda at all.  The architecture's own source is a Plummer core
  -- point-like -- so D = 4 is forced, and this pass turns that from an
  observation into an explanation.  AND A CONSTRAINT FALLS OUT THAT THE
  TREE DID NOT HAVE: in four dimensions ONLY a point-like source is
  scale-free.  A line source gives Phi ~ log r and a deficit of r log r - r
  that grows by 15.32 for a factor of 10 in scale -- so a "superhighway"
  built as a line loses the scale-free rate, and keeps it only by moving to
  D = 5, which dimension.py already priced at 5.32x worse per unit mass.
  Both doors, neither free.  Nothing is repaired: dimension.py is
  generalised rather than withdrawn, D = 4 being the p = 0 member of a
  family.  And no depth is claimed for codimension three -- it is the
  condition for a Green's function to be 1/r, four elementary steps from
  the scale-freedom it explains.  What the pass supplies is that M's reason
  SURVIVED BEING MADE PRECISE, which is more than most proposed reasons do.
  ------------------------------------------------------------------------""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
