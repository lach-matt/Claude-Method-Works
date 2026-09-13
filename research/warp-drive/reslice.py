#!/usr/bin/env python3
r"""
reslice.py -- THE BRIDGE.  What the step path on the index has to do with the
phase obstruction in the deformation, and how much of that connection is
derived rather than assumed.

    python3 reslice.py             the reading
    python3 reslice.py --selftest  fixtures

===============================================================================
THE TWO HALVES
===============================================================================

HALF ONE, DERIVED.  The deformation exp[1/2 c! M c!]|0> with

        M = [[ 2v, u ], [ u, -2v ]]      u = the CROSS column  (a!b!)
                                         v = the SAME-SIDE column (a!^2 - b!^2)

is normalizable exactly when every singular value of lam*M is below 1.  Those
singular values are computable in closed form:

        M!M = [[ P, 4i*I ], [ -4i*I, P ]]     P = |u|^2 + 4|v|^2
                                              I = Im(conj(v) u)
        singular values^2 = P +/- 4|I|

        ADMISSIBLE  <=>  lam^2 ( |u|^2 + 4|v|^2 + 4|Im(conj(v)u)| )  <  1

Two things follow, and the second is the bridge's whole content:

  * THE SPLITTING BETWEEN THE TWO SINGULAR VALUES IS 8|Im(conj(v)u)|.  The
    relative phase of the two columns is not one obstruction among several --
    it IS the anisotropy of the deformation.
  * IN PHASE <=> Im(conj(v)u) = 0 <=> THE SINGULAR VALUES ARE DEGENERATE.  An
    in-phase currency is an ISOTROPIC deformation: no preferred direction in
    the (a,b) plane.  An out-of-phase one has a preferred axis, and pays for it.

A DETERMINANT TEST IS NOT ENOUGH AND THIS FILE EXISTS PARTLY TO RECORD WHY.
det(M!M) is the PRODUCT of the two singular values, so both can exceed 1 while
it stays positive.  An earlier pass used the determinant, declared the in-phase
branch unbounded, and was caught only by a Fock-truncation convergence check
that made the entropy wander with N.  The singular-value form is exact and
subsumes it.

HALF TWO, MEASURED.  On the index, the step path phi_ij(a) = max{y_i : y_j <= a}
is FLAT wherever the reachable direction class does not change, and JUMPS where
it does.  A flat stretch singles out no direction.  A jump singles out one.

THE CORRESPONDENCE, AND IT IS AN ASSUMPTION, NOT A THEOREM:

        a flat stretch  <->  no preferred direction  <->  degenerate singular
                             values  <->  in phase  <->  no phase penalty

        a jump          <->  one direction singled out  <->  split singular
                             values  <->  out of phase  <->  penalty

WHAT WOULD MAKE IT A THEOREM, stated so nobody mistakes this for one: a
dictionary from index cells to the deformation's mode pairing.  necindex.py
builds its slots from ENERGY-CONDITION LABELS -- which tensor, which
directions, which measure -- and those are names for conditions, not for
creation operators.  No such dictionary exists in this tree, so the two halves
above are joined by one stated assumption and not by a derivation.  Everything
either side of that assumption is computed here and can be checked.

===============================================================================
WHAT IT REFUSES TO DO
===============================================================================

**It does not report the correspondence as a result.**  The singular-value
algebra is derived and the jumps are measured; the arrow between them is
labelled ASSUMED everywhere it appears.

**It does not search for a re-slicing that gives the answer it wants.**  The
candidate family is fixed in the source, every member is reported including
the ones that fail, and the count of failures is printed.
"""

import math
import sys

import decomposable as D
import hlaw
import necindex

VN = {0: "null", 1: "timelike", 2: "causal(BOTH)"}
MN = {0: "Dirac", 1: "smeared", 2: "averaged", 3: "achronal"}
MNR = {3: "Dirac", 2: "smeared", 1: "averaged", 0: "achronal"}


# ------------------------------------------------- half one: the derived side

def singular_values(lam, u, v):
    """(largest, smallest) of lam*M, in closed form.  Verified against a
    numerical SVD in the selftest."""
    P = abs(u) ** 2 + 4 * abs(v) ** 2
    I = abs((v.conjugate() * u).imag)
    return (math.sqrt(lam * lam * (P + 4 * I)), math.sqrt(lam * lam * max(P - 4 * I, 0.0)))


def admissible(lam, u, v):
    """The exact criterion: every singular value below 1."""
    return singular_values(lam, u, v)[0] < 1.0


def splitting(lam, u, v):
    """The gap between the two singular values SQUARED, which is 8|Im(conj(v)u)|
    times lam^2 -- the anisotropy, and the whole of the phase penalty."""
    return 8 * lam * lam * abs((v.conjugate() * u).imag)


# ------------------------------------------------ half two: the measured side

def steps(cells, i, j):
    """Jumps in phi_ij.  Each jump is (at, from, to)."""
    vals = sorted({c[j] for c in cells})
    out, prev = [], None
    for a in vals:
        p = D.phi(cells, i, j, a)
        if prev is not None and p != prev:
            out.append((a, prev, p))
        prev = p
    return out


# The candidate re-slicings.  FIXED IN SOURCE, and every one is reported --
# including the six that fail -- so this cannot be a search that stopped when
# it found what it liked.
CANDIDATES = (
    ("identity", lambda c: c),
    ("inverse M  (3-M)", lambda c: (c[0], c[1], 3 - c[2], c[3], c[4])),
    ("inverse V  (2-V)", lambda c: (c[0], 2 - c[1], c[2], c[3], c[4])),
    ("inverse both", lambda c: (c[0], 2 - c[1], 3 - c[2], c[3], c[4])),
    ("diagonal V+M", lambda c: (c[0], c[1] + c[2], c[2], c[3], c[4])),
    ("diagonal V-M", lambda c: (c[0], c[1] - c[2] + 3, c[2], c[3], c[4])),
    ("diagonal V+(3-M)", lambda c: (c[0], c[1] + 3 - c[2], c[2], c[3], c[4])),
    ("swap to strength pair", lambda c: (c[0], 3 - c[2], 2 - c[1], c[3], c[4])),
)


def search():
    """Which re-slicings make V and M positively coupled.  [(name, jumps)]."""
    X0 = sorted(necindex.cells())
    return [(nm, steps([f(c) for c in X0], 1, 2)) for nm, f in CANDIDATES]


def reversed_index():
    return frozenset((c[0], c[1], 3 - c[2], c[3], c[4]) for c in necindex.cells())


# --------------------------------------------------------------- the reading

def report():
    print("=" * 74)
    print("THE BRIDGE: THE STEP PATH AND THE PHASE OBSTRUCTION")
    print("=" * 74)
    print()

    print("HALF ONE -- DERIVED.  The phase IS the anisotropy.")
    print("   %-26s %-10s %-10s %s" % ("deformation", "sv max", "sv min", "splitting"))
    for nm, lam, u, v in (("undeformed", 0.5, 1 + 0j, 0j),
                          ("Janus  d=0.2 (90 apart)", 0.5, math.cosh(.2) + 0j, 1j * math.sinh(.2)),
                          ("in-phase d=0.2", 0.5, 1j * math.cosh(.2), 1j * math.sinh(.2)),
                          ("in-phase d=0.4", 0.5, 1j * math.cosh(.4), 1j * math.sinh(.4))):
        hi, lo = singular_values(lam, u, v)
        print("   %-26s %-10.6f %-10.6f %.6f%s" % (nm, hi, lo, splitting(lam, u, v),
              "   <- DEGENERATE" if splitting(lam, u, v) < 1e-12 else ""))
    print()
    print("   In phase the two singular values coincide: the deformation is")
    print("   ISOTROPIC. Out of phase it has a preferred axis, and the penalty")
    print("   is exactly that splitting.")
    print()

    print("HALF TWO -- MEASURED.  Which re-slicings couple V and M positively.")
    res = search()
    for nm, js in res:
        print("   %-24s %-6s %s" % (nm, "JUMPS" if js else "flat",
              "  ".join("at %d: %s->%s" % (a, VN.get(f, f), VN.get(t, t)) for a, f, t in js)))
    nfail = sum(1 for _, js in res if not js)
    print("   %d of %d candidates fail. Reported, not hidden." % (nfail, len(res)))
    print()

    XR = reversed_index()
    print("THE WINNER, inverse M -- two jumps, each locating a direction:")
    for a, f, t in steps(sorted(XR), 1, 2):
        print("   at M'=%d (%s): %s -> %s" % (a, MNR[a], VN[f], VN[t]))
    print("   The space/time intersection is reached at the LAST step, and only")
    print("   at the weakest measure.")
    print()

    X0 = frozenset(necindex.cells())
    c0, _ = hlaw.closures(X0)
    cR, _ = hlaw.closures(XR)
    print("CLAUSE F, checked against the re-slicing it did not know about:")
    for L in hlaw.LANGS:
        print("   %-12s %3d -> %-3d  %s" % (L, len(c0[L]), len(cR[L]),
              "unmoved" if len(c0[L]) == len(cR[L]) else "moved"))
    print("   statistics unmoved -- Clause F, as proved.")
    print("   geometry also unmoved, and that is NOT a violation: a reversal is")
    print("   a REFLECTION, and the convex hull is reflection-invariant. Clause F")
    print("   says these four need the order, not that they need its sign.")
    print()

    f0 = c0["geometry"] - X0
    fR = cR["geometry"] - XR
    print("FORGERY is invariant under the re-slicing: %d -> %d cells."
          % (len(f0), len(fR)))
    print("   at the space/time intersection V=2 : %d -> %d"
          % (sum(1 for c in f0 if c[1] == 2), sum(1 for c in fR if c[1] == 2)))
    print("   So the forgeable region is a property of the index's CONTENT,")
    print("   not of its labelling.")
    print()
    print("THE ARROW BETWEEN THE HALVES IS ASSUMED. See the docstring for the")
    print("one dictionary that would make it a theorem, and why it does not exist")
    print("in this tree.")
    return 0


# -------------------------------------------------------------------- checks

def selftest():
    ok = True

    def chk(name, got, want, tol=None):
        nonlocal ok
        good = (abs(got - want) <= tol) if tol is not None else (got == want)
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", name, got))
        if not good:
            print("        expected %r" % (want,))

    print("reslice selftest")

    # The closed-form singular values against a numerical SVD.
    try:
        import numpy as np
        worst = 0.0
        for lam, u, v in ((0.5, 1 + 0j, 0.3j), (0.7, 1 + 0j, 0.3j),
                          (0.3, math.cosh(.5) + 0j, 1j * math.sinh(.5)),
                          (0.5, 1j * math.cosh(.8), 1j * math.sinh(.8))):
            M = np.array([[2 * v, u], [u, -2 * v]], dtype=complex)
            sv = sorted(np.linalg.svd(lam * M, compute_uv=False), reverse=True)
            hi, lo = singular_values(lam, u, v)
            worst = max(worst, abs(sv[0] - hi), abs(sv[1] - lo))
        chk("closed-form singular values match a numerical SVD", worst < 1e-12, True)
    except ImportError:
        print("  [--] numpy absent; SVD cross-check skipped (closed form still used)")

    # The criterion must reproduce the Fock-convergence verdicts that caught the
    # earlier determinant-only error.
    for nm, lam, u, v, want in (("in-phase d=0.20", 0.5, 1j * math.cosh(.2), 1j * math.sinh(.2), True),
                                ("in-phase d=0.40", 0.5, 1j * math.cosh(.4), 1j * math.sinh(.4), True),
                                ("in-phase d=0.80", 0.5, 1j * math.cosh(.8), 1j * math.sinh(.8), False),
                                ("Janus    d=0.20", 0.5, math.cosh(.2) + 0j, 1j * math.sinh(.2), True)):
        chk("criterion agrees with convergence: %s" % nm, admissible(lam, u, v), want)

    # In phase means degenerate, and that is the whole claim of half one.
    chk("in phase => singular values degenerate",
        splitting(0.5, 1j * math.cosh(.4), 1j * math.sinh(.4)) < 1e-15, True)
    chk("Janus line => split", splitting(0.5, math.cosh(.4) + 0j, 1j * math.sinh(.4)) > 1e-3, True)
    chk("undeformed is admissible", admissible(0.5, 1 + 0j, 0j), True)

    # The re-slicing search: the two that work, and the count that does not.
    res = dict(search())
    chk("identity is flat", res["identity"], [])
    chk("inverse M gives two jumps", len(res["inverse M  (3-M)"]), 2)
    chk("and they climb null->timelike->causal",
        [(f, t) for _, f, t in res["inverse M  (3-M)"]], [(0, 1), (1, 2)])
    chk("diagonal V+M gives one jump", len(res["diagonal V+M"]), 1)
    chk("six of eight candidates fail", sum(1 for js in res.values() if not js), 6)

    # Clause F, and the reflection refinement.
    X0 = frozenset(necindex.cells()); XR = reversed_index()
    c0, _ = hlaw.closures(X0); cR, _ = hlaw.closures(XR)
    chk("statistics unmoved by the relabelling", len(cR["statistics"]), len(c0["statistics"]))
    chk("geometry unmoved too (reflection-invariant hull)",
        len(cR["geometry"]), len(c0["geometry"]))
    chk("order moved", len(cR["order"]) != len(c0["order"]), True)
    chk("information moved", len(cR["information"]) != len(c0["information"]), True)
    chk("the law still holds after re-slicing",
        all(cR[a] <= cR[b] for a, b in hlaw.LAWFUL), True)

    # Forgery invariance, and the intersection staying clean.
    chk("forgery count invariant", len(cR["geometry"] - XR), len(c0["geometry"] - X0))
    chk("nothing forged at the space/time intersection, before",
        sum(1 for c in c0["geometry"] - X0 if c[1] == 2), 0)
    chk("nothing forged at the space/time intersection, after",
        sum(1 for c in cR["geometry"] - XR if c[1] == 2), 0)

    print("reslice selftest: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else report())
