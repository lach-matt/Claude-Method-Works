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
THE CLAUSE F REFINEMENT -- FOUR INVARIANCE GROUPS, NOT ONE DICHOTOMY
===============================================================================

Clause F says four of the five languages need an order on each coordinate and
`statistics` does not.  That is right and it is coarse: **"relabelling" is not
one operation**, and the four that "need the order" do not need the same thing.
Three distinct relabellings live inside the word, and the five languages sort
differently under each:

    FULL REVERSAL      every coordinate reversed at once -- the LATTICE DUAL
    ONE REVERSAL       a single coordinate reversed, the others left alone
    PERMUTATION        an arbitrary bijection of each coordinate's values

Measured over 600 random indexes (seed 11), invariant counts:

                      full reversal   one reversal   permutation
        order            600/600         135/600        165/600
        algebra          600/600         135/600        165/600
        geometry         591/600         597/600        278/600
        information      121/600         128/600        151/600
        statistics       600/600         600/600        600/600

Every number there is explained, and the explanation is the finding: each
language is invariant under a GROUP, the four groups are DIFFERENT, and they
form a strict chain that is not the containment hierarchy.

  * `statistics` -- the FULL SYMMETRIC group, every bijection of every
    coordinate.  It reads no order at all.  That is Clause F, and 600/600 is
    a theorem showing up as a count.

  * `geometry` -- the REVERSAL HYPERCUBE, all 2^d patterns of reversing each
    coordinate independently.  The hull commutes with any AFFINE relabelling,
    and a rank reversal is affine exactly when the coordinate's observed values
    are equally spaced.  Of the nine full-reversal failures above, NINE have a
    non-equally-spaced box and ZERO have an equally-spaced one; restricted to
    equally-spaced boxes it is 400/400 under both reversals, and 1952/1952
    under every MIXED pattern.  Its misses are an artefact of rank-encoding a
    reversal, not a property of the hull.

  * `order` and `algebra` -- the DIAGONAL pair {identity, full reversal}, two
    elements.  Full reversal is an order-ANTIautomorphism of the product: it
    swaps meet with join, and the sublattice hull closes under both, so it
    commutes.  600/600, and again a theorem.  A single reversal is neither an
    automorphism nor an antiautomorphism, and they break: 600/600 on the
    diagonal patterns against 350 of 1952 on the mixed ones.

  * `information` -- the TRIVIAL group.  It is the JOIN-closure, and the dual
    turns join-closure into MEET-closure, which is a different operator.  It is
    the only one of the five that the lattice dual moves, and its ~20 % hit
    rate is coincidence, not invariance.

So the chain is

        symmetric  >  hypercube {id,rev}^d  >  diagonal {id,rev}  >  trivial
        statistics    geometry                 order = algebra      information

and Clause F's "four need the order" is the statement that the first of those
four groups is proper.  It is true.  It is also the weakest of four separate
facts, and reading it as "the other four behave alike" is wrong: `geometry`
survives a reversal `order` cannot, and `information` survives neither.

===============================================================================
WHAT IT REFUSES TO DO
===============================================================================

**It does not report the correspondence as a result.**  The singular-value
algebra is derived and the jumps are measured; the arrow between them is
labelled ASSUMED everywhere it appears.

**It does not search for a re-slicing that gives the answer it wants.**  The
candidate family is fixed in the source, every member is reported including
the ones that fail, and the count of failures is printed.

**It does not report an invariance rate as an invariance.**  `information`
holds under the dual about a fifth of the time and is not invariant under it;
`geometry` misses nine of six hundred and IS invariant under the operation the
encoding was meant to express.  A rate and a group are different claims, and
the census prints the rate while the reading names the group.
"""

import itertools
import math
import random
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
    ("inverse M  (3-M)", lambda c: c[:2] + (3 - c[2],) + c[3:]),
    ("inverse V  (2-V)", lambda c: (c[0], 2 - c[1]) + c[2:]),
    ("inverse both", lambda c: (c[0], 2 - c[1], 3 - c[2]) + c[3:]),
    ("diagonal V+M", lambda c: (c[0], c[1] + c[2]) + c[2:]),
    ("diagonal V-M", lambda c: (c[0], c[1] - c[2] + 3) + c[2:]),
    ("diagonal V+(3-M)", lambda c: (c[0], c[1] + 3 - c[2]) + c[2:]),
    ("swap to strength pair", lambda c: (c[0], 3 - c[2], 2 - c[1]) + c[3:]),
)


def search():
    """Which re-slicings make V and M positively coupled.  [(name, jumps)]."""
    X0 = sorted(necindex.cells())
    return [(nm, steps([f(c) for c in X0], 1, 2)) for nm, f in CANDIDATES]


def reversed_index():
    """Invert the M slot, leaving every other coordinate alone. Written
    positionally so it survives the index gaining coordinates -- it gained the
    arity slot after this file was written."""
    return frozenset(c[:2] + (3 - c[2],) + c[3:] for c in necindex.cells())


# ------------------------------------------- the Clause F refinement: 3 groups

def relabel(X, maps):
    """Apply a per-coordinate bijection to every cell."""
    d = len(maps)
    return frozenset(tuple(maps[i][x[i]] for i in range(d)) for x in X)


def commutes(X, maps):
    """{lang: does the closure commute with this relabelling?}

    Pull the closure of the relabelled index back through the inverse and
    compare.  This is the only correct test: comparing SIZES would call
    `information` invariant whenever the join- and meet-closures happen to be
    equinumerous, which they often are and which is not the same claim.
    """
    d = len(maps)
    inv = [{v: k for k, v in m.items()} for m in maps]
    c0, _ = hlaw.closures(X)
    cp, _ = hlaw.closures(relabel(X, maps))
    return {L: frozenset(tuple(inv[i][y[i]] for i in range(d)) for y in cp[L]) == c0[L]
            for L in hlaw.LANGS}


def reversal(box, pattern):
    """The relabelling that reverses coordinate i exactly where pattern[i]."""
    return [dict(zip(v, list(reversed(v)))) if pattern[i] else {x: x for x in v}
            for i, v in enumerate(box)]


def equally_spaced(v):
    """A rank reversal of this coordinate is AFFINE iff this is true."""
    return len(v) < 3 or len({v[i + 1] - v[i] for i in range(len(v) - 1)}) == 1


def random_index(rnd):
    """The same family hlaw.sweep draws from, so the two censuses agree."""
    d = rnd.randint(2, 4)
    alpha = [rnd.randint(2, 4) for _ in range(d)]
    allc = list(itertools.product(*[range(a) for a in alpha]))
    return frozenset(rnd.sample(allc, rnd.randint(2, min(len(allc), 10))))


def invariance_census(n=600, seed=11):
    """{op: {lang: count}}, plus the spacing split for geometry's misses.

    op is one of 'full', 'one', 'perm'.  Returns (counts, n, geometry_misses)
    where geometry_misses is (with_equally_spaced_box, without).
    """
    rnd = random.Random(seed)
    tal = {k: {L: 0 for L in hlaw.LANGS} for k in ("full", "one", "perm")}
    geo_miss = [0, 0]
    for _ in range(n):
        X = random_index(rnd)
        d = len(next(iter(X)))
        box = D.box_of(X, d)
        rf = commutes(X, reversal(box, (1,) * d))
        for L in hlaw.LANGS:
            tal["full"][L] += rf[L]
        if not rf["geometry"]:
            geo_miss[0 if all(equally_spaced(v) for v in box) else 1] += 1
        k = rnd.randrange(d)
        r1 = commutes(X, reversal(box, tuple(int(i == k) for i in range(d))))
        for L in hlaw.LANGS:
            tal["one"][L] += r1[L]
        pm = []
        for v in box:
            sh = v[:]
            rnd.shuffle(sh)
            pm.append(dict(zip(v, sh)))
        rp = commutes(X, pm)
        for L in hlaw.LANGS:
            tal["perm"][L] += rp[L]
    return tal, n, tuple(geo_miss)


def hypercube_census(n=300, seed=23):
    """Every reversal pattern on equally-spaced boxes, split diagonal/mixed.

    Returns {'geom_mixed': (inv, moved), 'oa_mixed': ..., 'oa_diag': ...}.
    This is the test that separates `geometry`'s group from `order`'s: both
    survive the diagonal, only `geometry` survives the mixed patterns.
    """
    rnd = random.Random(seed)
    out = {k: [0, 0] for k in ("geom_mixed", "oa_mixed", "oa_diag")}
    got = 0
    while got < n:
        X = random_index(rnd)
        d = len(next(iter(X)))
        box = D.box_of(X, d)
        if not all(equally_spaced(v) for v in box):
            continue                      # a non-affine encoding, excluded by name
        got += 1
        for pat in itertools.product((0, 1), repeat=d):
            r = commutes(X, reversal(box, pat))
            if sum(pat) in (0, d):
                out["oa_diag"][r["order"]] += 1
            else:
                out["geom_mixed"][r["geometry"]] += 1
                out["oa_mixed"][r["order"]] += 1
    return {k: (v[1], v[0]) for k, v in out.items()}


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
    print("   geometry also unmoved, and that is NOT a violation: see the")
    print("   refinement below, which says exactly which group each one has.")
    print()

    print("THE CLAUSE F REFINEMENT -- \"relabelling\" is three operations.")
    tal, n, geo = invariance_census()
    print("   %-12s %-14s %-14s %s" % ("", "full reversal", "one reversal", "permutation"))
    for L in hlaw.LANGS:
        print("   %-12s %-14s %-14s %s"
              % (L, "%d/%d" % (tal["full"][L], n), "%d/%d" % (tal["one"][L], n),
                 "%d/%d" % (tal["perm"][L], n)))
    print()
    print("   geometry's %d misses under full reversal: %d have an equally-spaced"
          % (sum(geo), geo[0]))
    print("   box, %d do not -- a rank reversal is AFFINE only when the values are" % geo[1])
    print("   equally spaced, so the misses are the encoding, not the hull.")
    print()
    hc = hypercube_census()
    print("   On equally-spaced boxes, every reversal pattern:")
    print("     geometry, MIXED patterns      %d invariant, %d moved" % hc["geom_mixed"])
    print("     order,    MIXED patterns      %d invariant, %d moved" % hc["oa_mixed"])
    print("     order,    DIAGONAL patterns   %d invariant, %d moved" % hc["oa_diag"])
    print()
    print("   FOUR GROUPS, A STRICT CHAIN, AND IT IS NOT THE HIERARCHY:")
    print("     statistics   the full symmetric group -- reads no order at all")
    print("     geometry     the reversal hypercube {id,rev}^d -- affine-invariant")
    print("     order=algebra  the diagonal {id,rev} -- the lattice dual, which")
    print("                  swaps meet and join and the sublattice hull has both")
    print("     information  trivial -- join-closure, and the dual makes it MEET")
    print("   Clause F is the claim that the first of these is proper. True, and")
    print("   the weakest of the four: it does not say the other four behave alike.")
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

    # The Clause F refinement.  These are GROUP facts, so the structural pins
    # are exact and the rate pins are only the census reproducing itself.
    tal, n, geo = invariance_census()
    chk("statistics invariant under all three relabellings",
        (tal["full"]["statistics"], tal["one"]["statistics"], tal["perm"]["statistics"]),
        (n, n, n))
    chk("order and algebra invariant under the full reversal (the dual)",
        (tal["full"]["order"], tal["full"]["algebra"]), (n, n))
    chk("and NOT under a single reversal", tal["one"]["order"] < n // 2, True)
    chk("information moved by the dual too -- it is the only one",
        tal["full"]["information"] < n // 2, True)
    chk("every geometry miss has a non-equally-spaced box", geo, (0, 9))

    hc = hypercube_census()
    chk("geometry survives every MIXED reversal pattern", hc["geom_mixed"][1], 0)
    chk("order survives every DIAGONAL pattern", hc["oa_diag"][1], 0)
    chk("order does not survive the mixed ones", hc["oa_mixed"][1] > 0, True)
    chk("so geometry's group is strictly larger than order's",
        hc["geom_mixed"][0] > hc["oa_mixed"][0], True)

    print("reslice selftest: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else report())
