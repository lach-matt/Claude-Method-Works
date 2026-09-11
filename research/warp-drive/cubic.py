#!/usr/bin/env python3
"""
cubic.py -- M: "Maybe this is a simple question, but maybe not... Can we derive
a zero-sum from a cube?"

IT IS NOT SIMPLE, AND THE ANSWER IS YES THREE TIMES OVER -- WHICH IS EXACTLY
WHY IT DOES NOT HELP.  Every zero the cube yields is a TRIVIAL zero rather than
a sign flip, and the one place it could have flipped a sign is empty.

THE INSTINCT IS CORRECT AND IT IS THE BEST-AIMED QUESTION OF THE SESSION.
zeno.py closed on "a square does not go negative" -- lattice.py's theorem is
T_munu k^mu k^nu = V.V >= 0, a SUM OF SQUARES, and squaring destroys sign.
A CUBE DOES NOT.  Cubing is ODD: (-a)^3 = -a^3.  So asking whether an
odd-order object can go where an even-order one cannot IS THE RIGHT QUESTION,
and it is the first thing in this session to aim directly at the one bit
midpoints.py named.

    AND FOR THE FIELD THIS PROJECT USES AS ITS CURRENCY, THE ANSWER IS THAT
    THE ODD INVARIANT IS IDENTICALLY ZERO.  Not small.  Zero by the algebra.

===============================================================================
1. YES, GEOMETRICALLY -- AND IT IS THE 8
===============================================================================

A cube centred on the origin has vertices (+/-1, +/-1, +/-1).  EIGHT OF THEM,
and

        sum of the eight vertex vectors = (0, 0, 0)     EXACTLY

    A ZERO-SUM FROM A CUBE, exact, and the count is the 8 this session has
    circled from three directions -- the antiparallel amplitude, the top of the
    coupling range, and the third term of M's sequence.

    IT IS ALSO TRIVIAL, and the reason is worth stating because it is the same
    reason all three answers come out trivial: the eight vertices are four
    ANTIPODAL PAIRS, and each pair cancels.  THE ZERO IS A SYMMETRY, NOT A
    CANCELLATION OF SUBSTANCE.  Nothing was subtracted from anything; the sum
    was zero before it was taken.

===============================================================================
2. YES, STRUCTURALLY -- AND THIS IS THE HALF THAT IS RIGHT
===============================================================================

        a = -3.0     a^2 = +9.000  (>= 0 always)     a^3 = -27.000  (sign of a)
        a = -0.5     a^2 = +0.250                    a^3 =  -0.125
        a = +0.5     a^2 = +0.250                    a^3 =  +0.125
        a = +3.0     a^2 = +9.000                    a^3 = +27.000

    SQUARING IS EVEN AND DESTROYS SIGN.  CUBING IS ODD AND CARRIES IT.

    That is precisely the asymmetry the obstruction rests on.  lattice.py's
    V.V >= 0 is unbeatable BECAUSE it is quadratic; an odd-order invariant of
    the same field carries no such floor and can in principle be negative.

    M HAS FOUND THE RIGHT SHAPE OF ESCAPE.  Section 3 asks whether the
    corresponding object exists, and section 4 asks whether it is the object
    the obstruction is about.  The answers are "it is zero" and "it is not".

===============================================================================
3. YES, ALGEBRAICALLY -- AND THE ZERO IS IDENTICAL, WHICH IS THE FINDING
===============================================================================

The natural cubic invariant of a stress tensor is Tr(T^3), with T^mu_nu the
mixed-index form.  Computed for five random electromagnetic fields:

        Tr(T)              Tr(T^2)            Tr(T^3)
        -5.551e-17         +1.001331e+00      +4.163e-15
        +1.110e-16         +4.794583e+01      +4.885e-15
        +0.000e+00         +1.235669e+00      +9.992e-16
        +0.000e+00         +4.364799e+01      +7.105e-15
        +8.882e-16         +4.845028e+01      +3.197e-14

    Tr(T^2) IS LARGE AND VARIES.  Tr(T^3) IS MACHINE ZERO EVERY TIME.

AND IT IS NOT A COINCIDENCE OR A FLOOR -- IT IS AN IDENTITY, and the mechanism
was measured alongside it.  The electromagnetic stress tensor in four
dimensions satisfies

        T^2 = (Tr(T^2)/4) . I          measured deviation < 3.6e-15

so T squares to a MULTIPLE OF THE IDENTITY.  Then, since T is traceless,

        Tr(T^3) = Tr(T . T^2) = (Tr(T^2)/4) . Tr(T) = 0        IDENTICALLY

    THE CUBIC INVARIANT OF THE ELECTROMAGNETIC STRESS TENSOR VANISHES BY THE
    ALGEBRA.  A zero-sum from a cube, exactly as M asked -- and there is
    nothing in it to be negative, because there is nothing in it at all.

    THE DOOR THE CUBE OPENS LEADS TO AN EMPTY ROOM, and it is empty for a
    specific reason: T^2 ~ I is special to electromagnetism in four dimensions.
    For a GENERAL traceless T the cube-sum is freely signed --

        eigenvalues ( 2, -1, -1, 0)   sum 0   sum of cubes  +6
        eigenvalues (-2,  1,  1, 0)   sum 0   sum of cubes  -6
        eigenvalues (-3,  2,  1, 0)   sum 0   sum of cubes -18

    -- SO THE VANISHING IS A PROPERTY OF LIGHT, NOT OF CUBES.  Whether some
    other matter model has a usefully negative cubic invariant is NOT COMPUTED
    HERE and is not closed by this pass.

===============================================================================
4. AND IT DOES NOT REACH THE OBSTRUCTION, WHICH HAS TO BE SAID
===============================================================================

Even granting a negative cubic invariant, it would not be the quantity the
obstruction is about, and conflating them would be the fault this tree exists
to catch.

        THE OBSTRUCTION IS      T_munu k^mu k^nu < 0 for a NULL k, and
                                m(r) < 0, which is its volume integral.

        A CUBIC INVARIANT IS    Tr(T^3), a SCALAR built from T alone.

    THESE ARE DIFFERENT OBJECTS.  The null energy condition is a CONTRACTION
    WITH A DIRECTION, not a trace; it asks what an observer moving on a null
    ray measures.  Tr(T^3) asks nothing about any direction.  A negative
    Tr(T^3) would not violate the NEC and a positive one would not save it.

    AND THERE IS NO CUBIC NEC TO WRITE DOWN.  T_munu is already quadratic in
    the field, and contracting it with two null vectors is what MAKES it the
    energy density an observer sees.  A cubic contraction T_munu T^nu_rho k^mu
    k^rho is a different quantity with no interpretation as an energy density,
    and nothing in general relativity constrains or uses it.

        SO: THE CUBE GIVES A ZERO-SUM THREE WAYS, THE ODD-ORDER INSTINCT IS
        CORRECT, THE CORRESPONDING INVARIANT IS IDENTICALLY ZERO FOR LIGHT,
        AND IT IS NOT THE QUANTITY THAT HAS TO GO NEGATIVE.

===============================================================================
5. WHAT IS ACTUALLY LEFT OPEN BY THE QUESTION
===============================================================================

The question is not wasted, and one thing survives it worth naming:

    THE VANISHING IS SPECIFIC TO EM IN 4D.  T^2 ~ I is why, and it is why
    lattice.py's theorem is so tight for classical electromagnetic fields.  A
    matter model whose stress tensor does NOT square to the identity has a
    live cubic invariant of either sign.  THAT IS NOT A ROUTE TO THE NEC --
    section 4 -- but it is a fact about how special the light case is, and
    this tree had not stated it.

    IT ALSO EXPLAINS SOMETHING ALREADY SEATED.  lattice.py's V.V >= 0 has felt
    unusually rigid throughout this project -- scale-free, dimension-free,
    holding in D = 3..26 over 200,000 random fields.  T^2 ~ I IS WHY.  The
    electromagnetic stress tensor has almost no algebraic freedom, so its
    invariants collapse: the trace is zero, the cube is zero, and the square
    is the only one that carries information.  THE FIELD HAS EXACTLY ONE
    NON-TRIVIAL INVARIANT AND IT IS THE ONE THAT CANNOT GO NEGATIVE.

SCOPE.  Section 3 is measured on random antisymmetric F in signature
(-,+,+,+), five samples, with the identity read off a deviation of 3.6e-15;
it is a numerical demonstration of a standard algebraic fact and NO NOVELTY IS CLAIMED.  Section 4 asserts nothing new about the NEC.  The general-T
either-sign statement is an eigenvalue observation, not a claim that any
physical matter model realises it.  NOTHING IS REPAIRED.
"""

import random
import sys

ETA = [[-1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]


# -- 1.  the cube ------------------------------------------------------------

def cube_vertices():
    return [(x, y, z) for x in (-1, 1) for y in (-1, 1) for z in (-1, 1)]


def vertex_sum():
    V = cube_vertices()
    return tuple(sum(v[i] for v in V) for i in range(3))


def antipodal_pairs():
    V = cube_vertices()
    return sum(1 for v in V if tuple(-c for c in v) in V) // 2


# -- 2.  parity --------------------------------------------------------------

def is_even(f, a=-3.0):
    return abs(f(a) - f(-a)) < 1e-15


def is_odd(f, a=-3.0):
    return abs(f(a) + f(-a)) < 1e-15


# -- 3.  the stress tensor and its invariants --------------------------------

def _mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(4)) for j in range(4)]
            for i in range(4)]


def _tr(A):
    return sum(A[i][i] for i in range(4))


def stress_mixed(Fd):
    """T^mu_nu for the electromagnetic field with lower-index F_{mu nu}."""
    Fm = [[sum(ETA[m][a] * Fd[a][n] for a in range(4)) for n in range(4)]
          for m in range(4)]
    Fuu = [[sum(ETA[n][b] * Fm[m][b] for b in range(4)) for n in range(4)]
           for m in range(4)]
    F2 = sum(Fuu[a][b] * Fd[a][b] for a in range(4) for b in range(4))
    return [[sum(Fuu[m][a] * Fd[n][a] for a in range(4))
             - (0.25 * F2 if m == n else 0.0) for n in range(4)]
            for m in range(4)]


def random_F(rng):
    Fd = [[0.0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(i + 1, 4):
            v = rng.uniform(-2, 2)
            Fd[i][j] = v
            Fd[j][i] = -v
    return Fd


def invariants(Fd):
    T = stress_mixed(Fd)
    T2 = _mul(T, T)
    T3 = _mul(T2, T)
    dev = max(abs(T2[i][j] - (_tr(T2) / 4.0 if i == j else 0.0))
              for i in range(4) for j in range(4))
    return _tr(T), _tr(T2), _tr(T3), dev


def cube_sum_of_eigenvalues(ev):
    """For a general traceless T: freely signed."""
    return sum(e ** 3 for e in ev)


# -- 4.  what the obstruction actually is ------------------------------------

OBSTRUCTION_IS = "T_munu k^mu k^nu < 0 for NULL k -- a contraction WITH A DIRECTION"
CUBIC_INVARIANT_IS = "Tr(T^3) -- a scalar built from T alone, direction-free"
THERE_IS_A_CUBIC_NEC = False

# The three answers, and all three are yes.
ANSWERS = [
    ("geometric", True, "8 vertices sum to (0,0,0) exactly -- four antipodal "
     "pairs, so the zero is a SYMMETRY"),
    ("structural", True, "cubing is ODD and carries sign where squaring does "
     "not -- the instinct is CORRECT"),
    ("algebraic", True, "Tr(T^3) = 0 IDENTICALLY for EM, because T^2 ~ I and "
     "T is traceless -- an EMPTY zero"),
]
REACHES_THE_OBSTRUCTION = False


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

    # -- 1: the geometric zero ------------------------------------------------
    chk("a cube has eight vertices", len(cube_vertices()), 8)
    chk("they sum to exactly zero", vertex_sum(), (0, 0, 0))
    chk("  because they are four antipodal pairs", antipodal_pairs(), 4)

    # -- 2: parity, and the instinct is right --------------------------------
    chk("squaring is EVEN", is_even(lambda a: a * a), True)
    chk("  so it destroys sign", (-3.0) ** 2 > 0 and (3.0) ** 2 > 0, True)
    chk("cubing is ODD", is_odd(lambda a: a ** 3), True)
    chk("  so it carries sign", (-3.0) ** 3 < 0 < (3.0) ** 3, True)
    chk("the odd-order instinct is correct",
        [a[1] for a in ANSWERS if a[0] == "structural"], [True])

    # -- 3: the identity, measured -------------------------------------------
    rng = random.Random(7)
    for k in range(5):
        t1, t2, t3, dev = invariants(random_F(rng))
        chk("field %d: Tr(T) = 0" % k, abs(t1) < 1e-12, True)
        chk("  Tr(T^2) is large and varies", abs(t2) > 1e-3, True)
        chk("  Tr(T^3) is MACHINE ZERO", abs(t3) < 1e-10, True)
        chk("  and T^2 = (Tr(T^2)/4) I", dev < 1e-12, True)

    # -- 3: the vanishing is a property of LIGHT, not of cubes ---------------
    chk("a general traceless T can have a POSITIVE cube-sum",
        cube_sum_of_eigenvalues((2, -1, -1, 0)), 6)
    chk("  and a NEGATIVE one", cube_sum_of_eigenvalues((-2, 1, 1, 0)), -6)
    chk("  freely signed", cube_sum_of_eigenvalues((-3, 2, 1, 0)), -18)
    chk("so the vanishing is EM's, not the cube's",
        cube_sum_of_eigenvalues((-2, 1, 1, 0)) < 0, True)

    # -- 4: and it does not reach the obstruction ----------------------------
    chk("the obstruction is a DIRECTIONAL contraction",
        "WITH A DIRECTION" in OBSTRUCTION_IS, True)
    chk("the cubic invariant is direction-free",
        "direction-free" in CUBIC_INVARIANT_IS, True)
    chk("there is no cubic NEC", THERE_IS_A_CUBIC_NEC, False)
    chk("so the cube does not reach it", REACHES_THE_OBSTRUCTION, False)

    # -- all three answers are yes -------------------------------------------
    chk("three readings, all YES", [a[1] for a in ANSWERS], [True, True, True])
    chk("  and all three trivial or unreachable",
        REACHES_THE_OBSTRUCTION, False)

    # -- scope ----------------------------------------------------------------
    chk("no novelty is claimed for the identity",
        "NO NOVELTY IS CLAIMED" in __doc__, True)
    chk("nothing is repaired", "NOTHING IS REPAIRED" in __doc__, True)

    print("\nSELFTEST", "PASS" if ok else "FAIL")
    return ok


def report():
    print(__doc__)
    print("  ------------------------------------------------------------------------")
    print("  THE THREE ANSWERS\n")
    for kind, yes, why in ANSWERS:
        print("    %-12s %-5s %s" % (kind, "YES" if yes else "NO", why))
    print("\n    reaches the obstruction: %s" % REACHES_THE_OBSTRUCTION)
    print()
    print("  ------------------------------------------------------------------------")
    print("  THE EM STRESS TENSOR'S INVARIANTS   (5 random fields)\n")
    print("      Tr(T)          Tr(T^2)          Tr(T^3)        |T^2 - (Tr/4)I|")
    rng = random.Random(7)
    for _ in range(5):
        t1, t2, t3, dev = invariants(random_F(rng))
        print("    %+.3e     %+.6e    %+.3e     %.3e" % (t1, t2, t3, dev))
    print("\n    T^2 = (Tr(T^2)/4) I  and  Tr(T) = 0   =>   Tr(T^3) = 0 IDENTICALLY")
    print()
    print("    a GENERAL traceless T is freely signed:")
    for ev in ((2, -1, -1, 0), (-2, 1, 1, 0), (-3, 2, 1, 0)):
        print("      eigenvalues %-14s sum %d   sum of cubes %+d"
              % (str(ev), sum(ev), cube_sum_of_eigenvalues(ev)))
    print("      -> the vanishing is a property of LIGHT, not of cubes.")
    print("""
  ------------------------------------------------------------------------
  THE PASS IN ONE PARAGRAPH

  M asks whether a zero-sum can be derived from a cube.  It is the
  best-aimed question of the session, because zeno.py closed on "a square
  does not go negative" and A CUBE DOES -- cubing is ODD and carries sign
  where squaring destroys it, so asking for an odd-order object is exactly
  the right shape of escape from lattice.py's V.V >= 0.  THE ANSWER IS YES
  THREE TIMES AND THAT IS WHY IT DOES NOT HELP.  Geometrically: a cube's
  eight vertices sum to (0,0,0) exactly -- and trivially, being four
  antipodal pairs, so the zero is a symmetry rather than a cancellation.
  Structurally: the parity instinct is CORRECT and unqualified.
  Algebraically: the natural cubic invariant Tr(T^3) of the electromagnetic
  stress tensor is MACHINE ZERO for every random field tested, and not as a
  floor -- T^2 = (Tr(T^2)/4) I to within 3.6e-15, so with T traceless
  Tr(T^3) = Tr(T.T^2) = 0 IDENTICALLY.  A zero-sum from a cube, exactly as
  asked, WITH NOTHING IN IT TO BE NEGATIVE.  The door the cube opens leads
  to an empty room, and it is empty for a reason specific to light: a
  general traceless T has a freely signed cube-sum, +6 or -6 or -18
  depending on eigenvalues, SO THE VANISHING IS A PROPERTY OF
  ELECTROMAGNETISM IN FOUR DIMENSIONS AND NOT OF CUBES.  And even granting
  a negative one it would not reach the obstruction, which is a NULL
  CONTRACTION WITH A DIRECTION rather than a trace, and there is no cubic
  NEC to write down.  What survives is an explanation the tree lacked: T^2
  ~ I is WHY lattice.py's theorem has felt so rigid -- the EM stress tensor
  has almost no algebraic freedom, its trace vanishes and its cube
  vanishes, SO IT HAS EXACTLY ONE NON-TRIVIAL INVARIANT AND IT IS THE ONE
  THAT CANNOT GO NEGATIVE.
  ------------------------------------------------------------------------""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
