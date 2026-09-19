#!/usr/bin/env python3
r"""
bosonqp.py -- THE COMPOSITE BOSONIC EXCITATIONS, AS A SUBLATTICE OF THE
BOSONS.  DOCKET 31.

    python3 bosonqp.py             the reading
    python3 bosonqp.py --selftest  fixtures
    python3 bosonqp.py --prove     the z3 pass (needs `pip install z3-solver`)

===============================================================================
0. TWO RULINGS, AND THE SECOND THREW OUT THE FIRST DRAFT
===============================================================================

M, first: "The universal quantum numbers of the textbook kinds are almost
nothing -- but not nothing, which means measurable ... it is a sub index/
sublattice of bosons."

    That corrected DOCKET 28, which wrote "almost nothing" and then treated it
    as nothing.  Low resolution is not no resolution: `overlap.py` calls a
    coordinate a LABEL at 0.9 and these do not reach it.

M, second: "Do not add declared.  Nothing less than computed or measured.
Declared still requires proof."

    THE FIRST DRAFT OF THIS FILE LISTED ELEVEN KINDS WITH THEIR SPINS AND
    CHARGES WRITTEN OUT FROM TEXTBOOK KNOWLEDGE, and called that provenance
    DECLARED.  It was a table of assertions with reasons attached, which is
    not the same thing as a derivation, and `registry.py` had grown a whole
    provenance category to accommodate it.  Both are gone.

    NOTHING HERE IS WRITTEN DOWN AS A VALUE.  A member is defined by WHAT IT
    IS MADE OF, and every quantum number is COMPUTED from that by the two
    rules below, with the constituent's own numbers read out of a seated
    index.  The only input is the composition, which is the definition of the
    object rather than a measurement of it.

===============================================================================
1. THE TWO RULES, AND THE ONE CONSTITUENT
===============================================================================

    CHARGE IS ADDITIVE.  Q(composite) = sum of the constituents' Q.
    SPIN COMBINES.  Two spins s1, s2 give every S from |s1 - s2| to s1 + s2 in
    integer steps, and a composite of n spins is that rule applied n-1 times.

Every constituent here is one particle and one anti-particle-like absence:

    the ELECTRON, read from `fundamental.rows()` -- 2J = 1, Q3 = -3, which is
        the PDG capture's value and this file does not restate it
    a HOLE, the absence of an electron from a filled band: charge NEGATED,
        spin magnitude unchanged.  That is the definition of a hole, and the
        negation is arithmetic on the seated value rather than a new one.

A MEMBER IS A COMPOSITE IN ONE OF ITS ALLOWED SPIN STATES.  The spin states
are not listed either -- they come out of the addition rule, so the biexciton
contributing three members and the exciton two is a computed fact.

===============================================================================
2. WHAT IS NOT HERE, AND BOTH EXCLUSIONS ARE FORCED RATHER THAN CHOSEN
===============================================================================

    THE TRION EXCLUDES ITSELF.  Two electrons and a hole compose to 2J in
    {1, 3} -- half-integer spin, a FERMION -- and a sublattice of the bosons
    holds no fermion.  Nothing in this file decides that; the addition rule
    returns it.  `excluded()` shows the computation.

    THE COLLECTIVE MODES ARE NOT MEMBERS, and this is the cost of the second
    ruling.  A phonon, a plasmon, a roton, a phason, a magnon, a polariton and
    an amplitude mode are all real bosonic excitations and all were in the
    first draft.  THEY ARE NOT COMPOSITES OF CONSTITUENTS, so their quantum
    numbers cannot be computed the way these are -- they would have to be
    written down, which is exactly what the ruling forbids.  They are named in
    `NOT_COMPOSITE` so their absence is visible, and seating them needs a
    derivation nobody here has.

===============================================================================
3. THE FINDING: A SUBLATTICE THAT EXTENDS THE BOSONS BY TWO CELLS
===============================================================================

    the tree's own bosons on (2J, Q3)    15 cells, and ALREADY a sublattice
    the composite excitations             5 cells, and a sublattice
    is the second a SUBSET of the first?  NO
    what lies outside                     (0, -6) and (2, -6) -- BOTH COOPER
                                          PAIR SPIN STATES
    the union                            17 cells, and STILL a sublattice

THE COOPER PAIR CARRIES CHARGE -2e AND NOTHING ELSE IN THE TREE DOES.  Every
meson and every gauge boson is charged -1, 0 or +1.  Two electrons bound in a
metal reach a charge no elementary or composite boson here reaches, in BOTH
the singlet and the triplet spin state -- the second being the p-wave pairing
of helium-3 and the candidate triplet superconductors.  So the composites are
a sublattice of the bosons only once the lattice is extended to hold them, and
the extension is two cells wide.

===============================================================================
4. THE CHANNEL IS K7, AND THIS TIME IT IS NOT FREE
===============================================================================

The first draft was a three-cell CHAIN, and a chain closes almost everything
by being one -- that draft said so and proved it with z3.  THIS CHART IS NOT A
CHAIN: it is five cells at width 2, and the measurement changes with it.

    over the 3x2 box this chart lives in, of the 6 five-cell subsets only 2
    close all five languages, and of all 57 subsets only 31 do

So K7 here is earned by two-thirds of the alternatives failing, not handed
over by shape.  `--prove` runs the same z3 pass as before, and the chain
theorem it proves is now a statement about what this chart ISN'T.

    IT IS STILL FIVE CELLS.  That is a small index and the channel should be
    read with that in mind.  The sublattice relation in section 3 is the
    finding; the channel is a measurement beside it.
"""

import itertools
import sys

import decomposable as D
import fundamental
import hlaw
import mesons
import mi

SOURCE = (
    "COMPUTED.  Charge is additive and spin combines by angular-momentum "
    "addition; the electron's own 2J and Q3 are read from the seated "
    "`fundamental` index, which reads the PDG capture.  No quantum number is "
    "written down in this file.  The BOSON frame is read from the seated "
    "`fundamental` and `mesons` indexes.",
    (),
)

NAMES = ("2J", "Q3")
ARITY = len(NAMES)

# A composite is its CONSTITUENT MULTISET.  That is the definition of the
# object; every number below is computed from it.  "hole" is the absence of an
# electron from a filled band -- charge negated, spin magnitude unchanged.
COMPOSITES = (
    ("Cooper pair", ("e-", "e-")),
    ("exciton", ("e-", "hole")),
    ("biexciton", ("e-", "e-", "hole", "hole")),
)

# Composed here too, and EXCLUDED BY THE COMPUTATION rather than by choice.
CANDIDATES_EXCLUDED = (
    ("trion", ("e-", "e-", "hole")),
)

# Real bosonic excitations that are NOT composites of constituents, so their
# quantum numbers cannot be computed the way these are.  Section 2.
NOT_COMPOSITE = ("phonon", "magnon", "plasmon", "polariton", "roton",
                 "phason", "amplitude (Higgs) mode", "magnon-polaron")

_C = {}


def electron():
    """(2J, Q3) for the electron, READ from the seated index."""
    for n, _p, j, q, _c, _g in fundamental.rows():
        if n == "e-":
            return (j, q)
    raise AssertionError("the seated fundamental index has no electron")


def constituent(name):
    """(2J, Q3) of one constituent.  A hole negates the electron's charge."""
    j, q = electron()
    return (j, q) if name == "e-" else (j, -q)


def compose(parts):
    """(Q3, [2J]) -- charge added, spin combined.  Section 1's two rules."""
    Q = sum(constituent(p)[1] for p in parts)
    tot = {0}
    for p in parts:
        s = constituent(p)[0]
        tot = {abs(t - s) for t in tot} | {t + s for t in tot}
    return Q, sorted(tot)


def rows():
    """[(name, parts, 2J, Q3)] -- a member is a composite in one spin state."""
    if "r" not in _C:
        out = []
        for nm, parts in COMPOSITES:
            Q, spins = compose(parts)
            for j in spins:
                out.append((nm, parts, j, Q))
        _C["r"] = out
    return _C["r"]


def excluded():
    """[(name, parts, [2J], why)] -- the computation that refuses them."""
    out = []
    for nm, parts in CANDIDATES_EXCLUDED:
        Q, spins = compose(parts)
        odd = [j for j in spins if j % 2]
        out.append((nm, parts, spins,
                    "half-integer spin %s -- a FERMION, and a sublattice of "
                    "the bosons holds none" % odd if odd else "boson"))
    return out


def index():
    return frozenset((j, q) for _n, _p, j, q in rows())


def boson_frame():
    """The cells the tree's OWN bosons occupy on (2J, Q3).  Read, never typed."""
    B = {(j, q) for _n, _p, j, q, _c, _g in fundamental.rows() if j % 2 == 0}
    B |= {(j, q) for _n, _p, j, _P, _i, q in mesons.rows()}
    return frozenset(B)


def is_sublattice(S):
    S = frozenset(S)
    return D.gen(S) == S


def relation():
    """(boson cells, qp cells, boson sub, qp sub, subset, outside, union,
    union sub) -- the whole of section 3."""
    B, Q = boson_frame(), index()
    return (len(B), len(Q), is_sublattice(B), is_sublattice(Q), Q <= B,
            sorted(Q - B), len(B | Q), is_sublattice(B | Q))


def outside():
    """[(cell, [members there])] -- what the tree's bosons do not hold."""
    B = boson_frame()
    out = {}
    for nm, _p, j, q in rows():
        if (j, q) not in B:
            out.setdefault((j, q), []).append(nm)
    return [(k, sorted(set(v))) for k, v in sorted(out.items())]


def box_freeness():
    """(all subsets, closing all five, five-cell subsets, of those closing).

    SECTION 4, measured over the chart's own box rather than over the tree's
    sample.  The first draft was a chain and its K7 was free; this one is not,
    and the difference is measured rather than asserted.
    """
    X = index()
    Js = sorted({j for j, _q in X})
    Qs = sorted({q for _j, q in X})
    box = [(j, q) for j in Js for q in Qs]
    tot = full = n5 = f5 = 0
    for r in range(2, len(box) + 1):
        for S in itertools.combinations(box, r):
            cl, _b = hlaw.closures(frozenset(S))
            ok = all(len(cl[L]) == len(S) for L in hlaw.LANGS)
            tot += 1
            full += ok
            if r == len(X):
                n5 += 1
                f5 += ok
    return (tot, full, n5, f5)


def closers(X=None):
    X = frozenset(index() if X is None else X)
    cl, _b = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def cell():
    return mi.cell(index())


def is_chain(X=None):
    return mi.cell(index() if X is None else X)[2] == 1


def prove():
    """z3 over every subset of the chart's box -- section 4.

    THE CHAIN THEOREM IS NOW A STATEMENT ABOUT WHAT THIS CHART IS NOT.  The
    first draft was a chain and leaned on this to disclaim its own channel;
    this one has width 2, so the same proof says the free pass does not reach
    it.
    """
    try:
        import z3
    except ImportError:
        return [("z3 is not installed -- pip install z3-solver", None)]
    X = index()
    Js = sorted({j for j, _q in X})
    Qs = sorted({q for _j, q in X})
    box = [(j, q) for j in Js for q in Qs]
    V = {c: z3.Bool("c_%d_%d" % c) for c in box}
    mt = lambda a, b: (min(a[0], b[0]), min(a[1], b[1]))
    jn = lambda a, b: (max(a[0], b[0]), max(a[1], b[1]))
    comparable, closed = [], []
    for a, b in itertools.combinations(box, 2):
        comparable.append(z3.Implies(
            z3.And(V[a], V[b]),
            z3.Or(z3.And(a[0] <= b[0], a[1] <= b[1]),
                  z3.And(b[0] <= a[0], b[1] <= a[1]))))
        closed.append(z3.Implies(z3.And(V[a], V[b]),
                                 z3.And(V[mt(a, b)], V[jn(a, b)])))
    out = []
    s = z3.Solver()
    s.add(z3.Not(z3.Implies(z3.And(*comparable), z3.And(*closed))))
    out.append(("every chain in the box is closed -- so a chain's K7 is free",
                s.check() == z3.unsat))
    g = z3.Solver()
    g.add(z3.And(*comparable))
    g.add(z3.Sum([z3.If(V[c], 1, 0) for c in box]) == 3)
    out.append(("and chains exist here, so that is not vacuous",
                g.check() == z3.sat))
    t = z3.Solver()
    t.add(z3.Not(z3.And(*closed)))
    out.append(("some subset is NOT closed -- the box is not trivially a "
                "lattice", t.check() == z3.sat))
    # AND THE ONE THAT MATTERS FOR THIS CHART
    w = z3.Solver()
    for c in box:
        w.add(V[c] if c in X else z3.Not(V[c]))
    w.add(z3.Not(z3.And(*comparable)))
    out.append(("THIS chart is NOT a chain, so the free pass does not reach it",
                w.check() == z3.sat))
    return out


def report():
    X = index()
    print("=" * 74)
    print("THE COMPOSITE BOSONIC EXCITATIONS -- a sublattice.  DOCKET 31")
    print("=" * 74)
    print()
    print("M: \"Do not add declared.  Nothing less than computed or measured.\"")
    print("NOTHING BELOW IS WRITTEN DOWN AS A VALUE.  A member is defined by")
    print("what it is made of; every number is computed from that.")
    print()
    print("   the electron, READ from the seated index: 2J = %d, Q3 = %d"
          % electron())
    print()
    print("1. THE MEMBERS: %d, over %d composites." % (len(rows()), len(COMPOSITES)))
    print("   %-14s %-26s %-5s %s" % ("composite", "made of", "2J", "Q3"))
    for nm, parts, j, q in rows():
        print("   %-14s %-26s %-5d %d" % (nm, "+".join(parts), j, q))
    print()
    print("2. EXCLUDED BY THE COMPUTATION, not by choice.")
    for nm, parts, spins, why in excluded():
        print("   %-10s %-22s 2J in %s" % (nm, "+".join(parts), spins))
        print("              %s" % why)
    print()
    print("   NOT COMPOSITES, so not computable here and therefore not seated:")
    print("   %s" % ", ".join(NOT_COMPOSITE))
    print("   Real excitations, and seating them needs a derivation nobody")
    print("   here has.  The first draft wrote their numbers down; the ruling")
    print("   forbids that.")
    print()
    nb, nq, bsub, qsub, subset, out, nu, usub = relation()
    print("3. THE FINDING.")
    print("   the tree's bosons on (2J, Q3)   %2d cells, sublattice: %s" % (nb, bsub))
    print("   the composite excitations       %2d cells, sublattice: %s" % (nq, qsub))
    print("   is the second inside the first? %s" % subset)
    for k, ns in outside():
        print("     outside: %s  %s" % (k, ", ".join(ns)))
    print("   the union                       %2d cells, sublattice: %s" % (nu, usub))
    print("   so the extension is %d cells wide." % (nu - nb))
    print()
    print("   THE COOPER PAIR CARRIES -2e AND NOTHING ELSE HERE DOES, in both")
    print("   spin states -- the triplet being helium-3's p-wave pairing.")
    print()
    tot, full, n5, f5 = box_freeness()
    print("4. THE CHANNEL: %s, cell %s." % (", ".join(closers()), cell()))
    print("   chain? %s   (the first draft was, and its K7 was free)" % is_chain())
    print("   over this chart's own box: %d of %d subsets close all five," % (full, tot))
    print("   and of the %d subsets its own size, only %d do." % (n5, f5))
    print("   So the K7 is earned here.  It is still five cells, and the")
    print("   sublattice in section 3 is the finding.")
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    # -- nothing is written down: the electron comes from the seated index
    chk("the electron is READ from the seated fundamental index, not typed",
        electron(), (1, -3))
    chk("and a hole is its charge negated, spin unchanged",
        constituent("hole"), (1, 3))

    # -- the two rules
    chk("charge is additive: two electrons carry -2e, which is Q3 = -6",
        compose(("e-", "e-"))[0], -6)
    chk("two spin-halves combine to spin 0 or 1 -- 2J in {0, 2}",
        compose(("e-", "e-"))[1], [0, 2])
    chk("an exciton is neutral because the hole cancels the electron",
        compose(("e-", "hole"))[0], 0)
    chk("four spin-halves give 2J in {0, 2, 4}",
        compose(("e-", "e-", "hole", "hole"))[1], [0, 2, 4])

    R = rows()
    chk("seven members over three composites", (len(R), len(COMPOSITES)),
        (7, 3))
    chk("and the member count is COMPUTED -- the biexciton contributes three",
        sorted((nm, len([1 for n2, _p, _j, _q in R if n2 == nm]))
               for nm in {n for n, _p, _j, _q in R}),
        [("Cooper pair", 2), ("biexciton", 3), ("exciton", 2)])

    # -- section 2: both exclusions forced
    E = excluded()
    chk("the trion composes to half-integer spin and excludes itself",
        [(nm, spins) for nm, _p, spins, _w in E], [("trion", [1, 3])])
    chk("every seated member is a boson -- 2J even, by computation",
        sorted({j % 2 for _n, _p, j, _q in R}), [0])
    chk("eight real excitations are named as not-composites, not omitted",
        len(NOT_COMPOSITE), 8)

    # -- section 3: the finding
    nb, nq, bsub, qsub, subset, out, nu, usub = relation()
    chk("the tree's bosons are 15 cells and already a sublattice",
        (nb, bsub), (15, True))
    chk("THE COMPOSITES ARE A SUBLATTICE -- M's first ruling, measured",
        (nq, qsub), (5, True))
    chk("but they are NOT a subset of the bosons", subset, False)
    chk("and what lies outside is BOTH Cooper pair spin states",
        (out, [n for _k, ns in outside() for n in ns]),
        ([(0, -6), (2, -6)], ["Cooper pair", "Cooper pair"]))
    chk("the union is 17 cells and STILL a sublattice", (nu, usub), (17, True))
    chk("so the extension is two cells wide", nu - nb, 2)

    # -- section 4: the channel, and the disclaimer that no longer applies
    X = index()
    chk("arity 2", len(next(iter(X))), 2)
    chk("it closes all five -- K7", closers(),
        ["algebra", "geometry", "information", "order", "statistics"])
    chk("AND IT IS NOT A CHAIN, unlike the first draft", is_chain(), False)
    tot, full, n5, f5 = box_freeness()
    chk("over its own box only 31 of 57 subsets close all five",
        (full, tot), (31, 57))
    chk("and of the six subsets its own size, only two do -- so K7 is earned",
        (f5, n5), (2, 6))
    import overlap
    chk("no coordinate is a row LABEL", 
        [a for a, _d, _n, _r, v in overlap.resolution(X) if v == "LABEL"], [])

    # -- the ruling itself
    chk("the source is COMPUTED, and the word DECLARED appears nowhere in it",
        ("COMPUTED" in SOURCE[0], "DECLARED" in SOURCE[0]), (True, False))

    print("bosonqp selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--prove" in sys.argv:
        print("z3, over every subset of the chart's own box:")
        good = True
        for lab, r in prove():
            print("  [%s] %s" % ("PROVED" if r else "  XX  " if r is False
                                 else " SKIP ", lab))
            good &= (r is not False)
        sys.exit(0 if good else 1)
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
