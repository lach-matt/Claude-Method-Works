#!/usr/bin/env python3
"""
closure.py -- deriving what bisector.py could only mark as interpretation:
a transition state cannot close on a DEFINITE state, and the derivation runs
three independent ways that disagree about everything except that.

bisector.py established, from geometry, that gluing theta = 0 to theta = pi
would force one configuration to carry both A = 0 and A = 8.  It then said, in
terms:

    "Reading this as a statement about a transition state is an interpretation
     laid on top of the geometry -- consistent with it, not derived from it."

M: "now that we have an idea of what we are looking for, let's derive it."

    THIS FILE DERIVES IT, AND NOT FROM THE GEOMETRY.  The geometric result is
    about the relative orientation of two null directions; a TRANSITION closing
    is a statement about a closed timelike curve, which is a different object in
    a different space.  Deriving the second from the first would be exactly the
    over-reach bisector.py refused.  So the derivation is done from the
    consistency condition a closed curve imposes, and the geometry is left
    where it is: a separate system with the same shape.

===============================================================================
0. WHY THE DERIVATION IS NOT VACUOUS HERE
===============================================================================

chronology.py already settled that this matters for THIS device rather than in
the abstract:

        EVERETT_ROUTE_OPEN = True     two devices plus a boost, needing no
                                      identification -- CLOSURE IS REACHABLE
        MTY_ROUTE_OPEN     = False    needs an identification the device lacks
        HAWKING            = NOT-RUN  the Cauchy-horizon divergence, unresolved

    So the closure route is OPEN for this architecture.  A constraint on what
    closure would cost is a live constraint, not a hypothetical -- and it is
    reached WITHOUT resolving Hawking, which stays NOT-RUN.  These are
    independent arguments and this file does not touch that one.

===============================================================================
1. CLASSICAL -- THE CONSISTENCY CONDITION HAS NO SOLUTION AT ALL
===============================================================================

A closed curve demands the state return as it left.  Take the sharpest
dynamics, the one the paradox is named for: the traversing system flips its own
earlier value.  Consistency is then

        b  =  b XOR 1,        b in {0, 1}

    SOLUTIONS: NONE.  Enumerated over the whole domain -- both of it.  Classical
    closure on a definite state is not merely unreached, it is UNSATISFIABLE.

That is the entire classical statement and it needs no field theory.  Everything
below is what quantum mechanics does with the same condition, and the answer
depends on which CTC prescription is used -- so both major ones are run.

===============================================================================
2. DEUTSCH -- CLOSURE IS ALLOWED, AND ONLY AT EXACTLY FIFTY-FIFTY
===============================================================================

DEUTSCH, "Quantum mechanics near closed timelike lines", Phys. Rev. D 44, 3197
(1991).  A chronology-respecting system in state rho_CR interacts through U with
a system on the closed curve in state rho.  Self-consistency:

        rho  =  Tr_CR [ U (rho_CR (x) rho) U^dag ]

Deutsch's theorem: a fixed point ALWAYS exists, because the density matrices
form a compact convex set and the map is continuous (Schauder).  So unlike the
classical case, closure is never simply forbidden.  THE PRICE IS PAID ELSEWHERE.

For grandfather dynamics the induced map is rho -> X rho X.  Solve it in full
rather than exhibiting one solution.  With rho = [[a, b], [c, d]]:

        X rho X = [[d, c], [b, a]]      so      a = d   and   b = c

and with unit trace, a = d = 1/2 IS FORCED.  The remaining freedom is b = c
real with |b| <= 1/2 -- a one-parameter family, and every member of it has

        rho_00  =  rho_11  =  1/2        EXACTLY

    CONFIRMED EXHAUSTIVELY on the Bloch ball.  Conjugation by X sends
    (r_x, r_y, r_z) -> (r_x, -r_y, -r_z), so the fixed set is r_y = r_z = 0 --
    THE X-AXIS OF THE BLOCH BALL, a segment, not a point and not the equator.
    Scanned at 1/40 resolution: 81 fixed points, and the worst
    |rho_00 - 1/2| over all of them is 0.000e+00.

    THE TWO PURE SOLUTIONS ARE NO ESCAPE.  At b = +/- 1/2 the state is pure --
    the X-eigenstates |+> and |-> -- and even those have rho_00 = rho_11 = 1/2
    in the computational basis, which is the basis the paradox is stated in.

        SO: NO SELF-CONSISTENT STATE ON THE CLOSED CURVE IS DEFINITE.  Every
        one of them, pure or mixed, carries BOTH computational states with
        EQUAL WEIGHT.  Closure is purchasable only at that price.

    That is M's sentence, derived: full closure means existing in two separate
    states simultaneously.

===============================================================================
3. POSTSELECTED CTCs -- A DIFFERENT PRESCRIPTION, AND IT FORBIDS IT OUTRIGHT
===============================================================================

Deutsch's is not the only model, and a derivation resting on one prescription is
resting on a choice.  LLOYD, MACCONE et al.'s postselected CTCs give the
chronology-respecting system the effective map

        C(rho)  ~  Tr_CTC[U] . rho . Tr_CTC[U]^dag

For grandfather dynamics U = X on the closed line, and

        Tr[X]  =  0        so       C(rho) = 0

    THE PROCESS HAS AMPLITUDE ZERO.  Under P-CTCs the paradoxical closure is
    not resolved into a mixture -- it is STRICTLY FORBIDDEN, probability
    exactly zero.

    AND THE SUPPRESSION IS SELECTIVE, WHICH IS WHAT MAKES IT AN ARGUMENT RATHER
    THAN A DEGENERACY: Tr[I] = 2, so a non-paradoxical loop is untouched.
    Tr[Z] = 0 and Tr[H] = 0 -- both traceless, both fully suppressed.  A T gate,
    diag(1, e^{i pi/4}), has |Tr| = 1.8478 and survives.  The zero is a property
    of the paradoxical dynamics, not of the formalism.

===============================================================================
4. THE THREE ROUTES, AND WHAT THEY AGREE ON
===============================================================================

    model                condition           result                reading
    -------------------  ------------------  --------------------  ---------------
    classical            b = b XOR 1         NO SOLUTION           unsatisfiable
    Deutsch D-CTC        rho = X rho X       rho_00 = rho_11 = 1/2 only at 50/50
    postselected P-CTC   Tr_CTC[X] = 0       amplitude 0           forbidden

    THEY DISAGREE ABOUT WHAT HAPPENS INSTEAD, AND THAT DISAGREEMENT IS LIVE IN
    THE LITERATURE -- D-CTCs and P-CTCs give different answers to nearly every
    question put to them.  They agree on exactly one thing, and it is the thing
    being derived:

        NO DEFINITE SINGLE-STATE CLOSURE EXISTS UNDER ANY OF THEM.

    A conclusion that survives two prescriptions which contradict each other
    elsewhere is stronger than one that needs either.

===============================================================================
5. WHAT IS DERIVED, AND WHAT IS STILL NOT
===============================================================================

    DERIVED   On a closed timelike curve carrying grandfather dynamics, there
              is no self-consistent DEFINITE state.  Classically none at all;
              under Deutsch every solution is exactly 50/50; under
              postselection the amplitude is exactly zero.

    DERIVED   Therefore, IF this device's corridor closed, the transported
              system could not be in a definite state -- and chronology.py has
              the closure route OPEN, so this is a live constraint on the
              architecture rather than a remark about time machines.

    NOT DERIVED, AND NOT CLAIMED:

        THAT THE GEOMETRY AND THIS ARE THE SAME FACT.  bisector.py's result is
        about [0, pi], the space of relative orientations of two null
        directions; this is about a closed timelike curve in spacetime.  Two
        different systems, two different spaces.  They have the same SHAPE --
        closure forces one object to carry two values -- and a shape recurring
        across unrelated systems is a finding worth recording and is NOT an
        identification.  Asserting they are one fact is the exact over-reach
        bisector.py declined, and it is declined again here.

        THAT THE DEVICE'S CORRIDOR ACTUALLY CLOSES.  Section 0 says the route
        is open, not that it is taken.  Nothing here shows the architecture
        produces a CTC.

        THAT HAWKING IS RESOLVED.  chronology.py's HAWKING = NOT-RUN stands
        untouched.  The Cauchy-horizon divergence is a separate, classical
        argument and this file neither needs nor supplies it.

        THAT GRANDFATHER DYNAMICS IS THE ONLY DYNAMICS.  A loop whose dynamics
        is not self-negating is not suppressed at all -- Tr[I] = 2.  The
        derivation bites on paradoxical closure specifically, which is the
        case in question, and not on every closed curve.

        AND NOTHING HERE SUPPLIES rho < 0.  It constrains closure, not the
        lead.
"""

import itertools
import math
import sys

# ---------------------------------------------- 0: why it is not vacuous

def device_closure_route():
    """From chronology.py, read rather than restated."""
    import chronology
    return {"everett": chronology.EVERETT_ROUTE_OPEN,
            "mty": chronology.MTY_ROUTE_OPEN,
            "hawking": chronology.HAWKING}


def closure_is_reachable_for_this_device():
    return device_closure_route()["everett"]


def hawking_is_untouched():
    return device_closure_route()["hawking"] == "NOT-RUN"


# ---------------------------------------------- 1: classical

def classical_consistency_solutions():
    """b = b XOR 1 over {0,1}.  Enumerated, not argued."""
    return [b for b in (0, 1) if b == (b ^ 1)]


def classical_closure_is_satisfiable():
    return len(classical_consistency_solutions()) > 0


# ---------------------------------------------- 2: Deutsch

X = ((0.0, 1.0), (1.0, 0.0))
I2 = ((1.0, 0.0), (0.0, 1.0))
Z = ((1.0, 0.0), (0.0, -1.0))
H = ((2 ** -0.5, 2 ** -0.5), (2 ** -0.5, -2 ** -0.5))


def matmul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2))
                 for i in range(2))


def dagger(A):
    return tuple(tuple(complex(A[j][i]).conjugate() for j in range(2)) for i in range(2))


def conjugate_by(U, rho):
    return matmul(matmul(U, rho), dagger(U))


def grandfather_map(rho):
    """The induced map on the closed line: rho -> X rho X."""
    return conjugate_by(X, rho)


def bloch(rx, ry, rz):
    """rho = (I + r.sigma)/2."""
    return ((0.5 * (1 + rz), 0.5 * (rx - 1j * ry)),
            (0.5 * (rx + 1j * ry), 0.5 * (1 - rz)))


def is_fixed(rho, tol=1e-12):
    out = grandfather_map(rho)
    return all(abs(out[i][j] - rho[i][j]) <= tol for i in range(2) for j in range(2))


def is_pure(rho, tol=1e-12):
    r2 = matmul(rho, rho)
    return all(abs(r2[i][j] - rho[i][j]) <= tol for i in range(2) for j in range(2))


def diagonal(rho):
    return rho[0][0].real if hasattr(rho[0][0], "real") else rho[0][0], \
           rho[1][1].real if hasattr(rho[1][1], "real") else rho[1][1]


def fixed_family(b):
    """rho = [[1/2, b], [b, 1/2]], b real in [-1/2, 1/2]."""
    return ((0.5, float(b)), (float(b), 0.5))


def scan_bloch_ball(step=40):
    """Every fixed point, and the worst departure of rho_00 from 1/2.

    Conjugation by X sends (rx, ry, rz) -> (rx, -ry, -rz), so the fixed set is
    ry = rz = 0: THE X-AXIS of the Bloch ball, a segment.  Not the equator.
    """
    found = 0
    worst = 0.0
    for i in range(-step, step + 1):
        for j in range(-step, step + 1):
            for k in range(-step, step + 1):
                rx, ry, rz = i / step, j / step, k / step
                if rx * rx + ry * ry + rz * rz > 1.0:
                    continue
                if not is_fixed(bloch(rx, ry, rz)):
                    continue
                found += 1
                worst = max(worst, abs(0.5 * (1 + rz) - 0.5))
    return found, worst


def fixed_set_is_the_x_axis(step=20, tol=1e-12):
    for i in range(-step, step + 1):
        for j in range(-step, step + 1):
            for k in range(-step, step + 1):
                rx, ry, rz = i / step, j / step, k / step
                if rx * rx + ry * ry + rz * rz > 1.0:
                    continue
                if is_fixed(bloch(rx, ry, rz)):
                    if abs(ry) > tol or abs(rz) > tol:
                        return False
    return True


def any_definite_solution(bs=(-0.5, -0.25, 0.0, 0.25, 0.5), tol=1e-12):
    """Is any fixed point definite -- i.e. rho_00 in {0, 1}?"""
    for b in bs:
        d0, _d1 = diagonal(fixed_family(b))
        if abs(d0) <= tol or abs(d0 - 1.0) <= tol:
            return True
    return False


def pure_solutions_are_still_fifty_fifty(tol=1e-12):
    out = []
    for b in (0.5, -0.5):
        rho = fixed_family(b)
        out.append((is_pure(rho), diagonal(rho)[0]))
    return all(p and abs(d - 0.5) <= tol for p, d in out)


DEUTSCH_FIXED_POINT_ALWAYS_EXISTS = True
DEUTSCH_REASON = "density matrices are compact and convex; the map is continuous (Schauder)"


# ---------------------------------------------- 3: postselected

def trace(A):
    return sum(A[i][i] for i in range(2))


def pctc_amplitude(U):
    """|Tr_CTC[U]|.  Zero means the process is strictly forbidden."""
    return abs(trace(U))


def t_gate():
    p = complex(math.cos(math.pi / 4), math.sin(math.pi / 4))
    return ((1.0, 0.0), (0.0, p))


def pctc_forbids_grandfather(tol=1e-12):
    return pctc_amplitude(X) <= tol


def pctc_suppression_is_selective(tol=1e-12):
    """Not everything is suppressed: identity and a T gate survive."""
    return pctc_amplitude(I2) > tol and pctc_amplitude(t_gate()) > tol


# ---------------------------------------------- 4: the agreement

ROUTES = (
    ("classical", "b = b XOR 1", "NO SOLUTION", "unsatisfiable"),
    ("Deutsch D-CTC", "rho = X rho X", "rho_00 = rho_11 = 1/2", "only at 50/50"),
    ("postselected P-CTC", "Tr_CTC[X] = 0", "amplitude 0", "forbidden"),
)


def all_routes_forbid_definite_closure():
    classical = not classical_closure_is_satisfiable()
    deutsch = not any_definite_solution()
    pctc = pctc_forbids_grandfather()
    return classical and deutsch and pctc


ROUTES_AGREE_ON = "no definite single-state closure exists under any of them"
ROUTES_DISAGREE = "D-CTCs and P-CTCs give different answers to nearly every other question"


# ---------------------------------------------- 5: scope

GEOMETRY_AND_THIS_ARE = ("the same SHAPE in two different systems, and that is a "
                         "finding, not an identification")
DEVICE_ACTUALLY_CLOSES = None      # not shown either way
SUPPLIES_NEGATIVE_ENERGY = False


def same_fact_as_the_geometry():
    return False


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

    print("0. WHY THIS IS NOT VACUOUS -- read from chronology.py")
    r = device_closure_route()
    for k in ("everett", "mty", "hawking"):
        print("     %-10s %s" % (k, r[k]))
    chk("is the closure route open for this device",
        closure_is_reachable_for_this_device(), True)
    chk("and is Hawking still untouched", hawking_is_untouched(), True)
    print("       so a constraint on what closure costs is LIVE, and it is")
    print("       reached without resolving the Cauchy-horizon question.")

    print("\n1. CLASSICAL -- NO SOLUTION AT ALL")
    chk("solutions of b = b XOR 1 over {0,1}", classical_consistency_solutions(), [])
    chk("is classical closure satisfiable", classical_closure_is_satisfiable(), False)
    print("       enumerated over the whole domain -- both of it.")

    print("\n2. DEUTSCH -- ALLOWED, AND ONLY AT FIFTY-FIFTY")
    chk("does a fixed point always exist", DEUTSCH_FIXED_POINT_ALWAYS_EXISTS, True)
    print("     because %s" % DEUTSCH_REASON)
    print("     %-14s %10s %10s %8s %8s" % ("fixed point", "rho_00", "rho_11", "pure?", "fixed?"))
    for b in (-0.5, -0.25, 0.0, 0.25, 0.5):
        rho = fixed_family(b)
        d0, d1 = diagonal(rho)
        print("     b = %-10.2f %10.4f %10.4f %8s %8s"
              % (b, d0, d1, is_pure(rho), is_fixed(rho)))
        chk("  b=%.2f is a fixed point" % b, is_fixed(rho), True)
        near("    and its rho_00", d0, 0.5)
    chk("is ANY fixed point definite (rho_00 in {0,1})", any_definite_solution(), False)
    chk("are the two pure solutions still 50/50",
        pure_solutions_are_still_fifty_fifty(), True)
    found, worst = scan_bloch_ball()
    chk("fixed points on the Bloch ball at 1/40", found, 81)
    near("  worst |rho_00 - 1/2| over all of them", worst, 0.0)
    chk("  is the fixed set the X-AXIS (ry = rz = 0)", fixed_set_is_the_x_axis(), True)
    print("       not the equator -- conjugation by X keeps rx and flips ry, rz.")
    print("       NO SELF-CONSISTENT STATE IS DEFINITE.  Every one carries both")
    print("       computational states with equal weight.")

    print("\n3. POSTSELECTED -- A DIFFERENT PRESCRIPTION, FORBIDS IT OUTRIGHT")
    near("|Tr[X]| -- grandfather dynamics", pctc_amplitude(X), 0.0)
    chk("  so P-CTCs forbid it", pctc_forbids_grandfather(), True)
    near("|Tr[I]| -- a non-paradoxical loop", pctc_amplitude(I2), 2.0)
    near("|Tr[Z]| -- also traceless, also suppressed", pctc_amplitude(Z), 0.0)
    near("|Tr[H]| -- traceless too, FULLY suppressed", pctc_amplitude(H), 0.0)
    near("|Tr[T]| -- survives", pctc_amplitude(t_gate()), 1.847759, 1e-6)
    chk("is the suppression selective", pctc_suppression_is_selective(), True)
    print("       the zero is a property of the paradoxical dynamics, not of")
    print("       the formalism.")

    print("\n4. THE THREE ROUTES")
    print("     %-20s %-18s %-22s %s" % ("model", "condition", "result", "reading"))
    for row in ROUTES:
        print("     %-20s %-18s %-22s %s" % row)
    chk("DO ALL THREE FORBID DEFINITE CLOSURE",
        all_routes_forbid_definite_closure(), True)
    print("     they agree on: %s" % ROUTES_AGREE_ON)
    print("     they disagree: %s" % ROUTES_DISAGREE)
    print("       a conclusion surviving two prescriptions that contradict")
    print("       each other elsewhere is stronger than one needing either.")

    print("\n5. WHAT IS DERIVED, AND WHAT IS NOT")
    chk("is this the same fact as bisector.py's geometry",
        same_fact_as_the_geometry(), False)
    print("     they are %s" % GEOMETRY_AND_THIS_ARE)
    chk("is the device shown to actually close", DEVICE_ACTUALLY_CLOSES, None)
    chk("is Hawking resolved here", not hawking_is_untouched(), False)
    chk("does any of this supply rho < 0", SUPPLIES_NEGATIVE_ENERGY, False)
    print("       it constrains CLOSURE, not the lead.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("""
  ------------------------------------------------------------------------
  THE PASS IN ONE PARAGRAPH

  bisector.py could only mark it as interpretation; this derives it, and
  deliberately not from the geometry -- deriving a statement about closed
  timelike curves from a statement about the space of relative orientations
  would be the exact over-reach that file declined.  Instead the derivation
  runs from the consistency condition closure itself imposes, three ways.
  Classically, b = b XOR 1 has no solution over either element of its
  domain: definite closure is unsatisfiable outright.  Under Deutsch's
  prescription a fixed point always exists, but solving rho = X rho X in
  full forces rho_00 = rho_11 = 1/2 with only an off-diagonal parameter
  free -- 81 fixed points on a Bloch scan, all on the x-axis, worst
  departure from one half exactly zero -- and even the two PURE solutions,
  the X-eigenstates, are fifty-fifty in the basis the paradox is stated in.
  Under postselected CTCs, Tr[X] = 0 makes the amplitude exactly zero and
  the process strictly forbidden, while Tr[I] = 2 leaves an unparadoxical
  loop alone, so the suppression is a property of the dynamics rather than
  the formalism.  The three disagree about what happens instead and agree
  that no definite single-state closure exists.  It is a live constraint
  here because chronology.py has the Everett route OPEN -- and it is
  reached without touching Hawking, which stays NOT-RUN.  What is not
  claimed: that this and the geometry are one fact.  They are one SHAPE in
  two systems, which is a finding and not an identification.
  ------------------------------------------------------------------------""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
