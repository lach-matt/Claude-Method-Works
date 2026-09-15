#!/usr/bin/env python3
r"""
figure.py -- THE FIGURE THE ELEMENT INDEXES MAKE.

M: "Remove any index in the project whose members do not have quantum numbers."

    python3 figure.py             the reading
    python3 figure.py --selftest  fixtures

===============================================================================
0. THIS REPLACES hexad.py, AND IT IS A WITHDRAWAL RATHER THAN A REFACTOR
===============================================================================

`hexad.py` measured a figure at six, eight, ten and twenty-five vertices and
reported three findings about how it changed as it grew: that the channel was
not stable, that the escaping diagonals equalled the information deficit only at
six, and that self-seating cycled at eight.

    EVERY ONE OF THOSE WAS MEASURED ON A CONTAMINATED SET.  The vertices
    included thirteen filing-system indexes -- mirrored files, BUILD snapshots,
    conversations, archives, artefact names, handoff documents, numbering gaps,
    and this tree's own dockets -- plus three indexes of warp-drive obstructions
    and four re-charts of the seated indexes.  Not one of those members carries
    a quantum number.  E ran from 9 to 133 on the mixture, and every one of the
    twelve disruptive vertices was repository metadata.

    SO THE FILE IS WITHDRAWN, NOT PATCHED.  A measurement taken on the wrong
    member set is not a measurement of the right one with an error bar.  DOCKET
    16 records it.

===============================================================================
1. THE FIGURE
===============================================================================

One vertex per index of the periodic elements.  `registry.py` decides what that
means and enforces it with `enforce()`; this file ASKS registry rather than
keeping its own list, so the two cannot drift apart -- which is how the
contamination survived as long as it did.

===============================================================================
2. WHAT THIS FILE REFUSES
===============================================================================

To report a growth narrative.  The old one was an artefact of the order a
contaminated set happened to be seated in.  No clean trajectory exists: the
element indexes were never seated one at a time against each other, and
producing that is work rather than a re-read of a log.

To name a shape.  Seven vertices is what there are today, not a finding.
"""

import itertools
import sys

import demand
import hlaw
import mi
import registry


def all_indexes():
    """{name: the index itself} over every registered element index."""
    return {nm.split(".")[0]: registry.index_of(nm)
            for nm, *_r in registry.rows()}


def cells(names=None):
    """{name: its cell}."""
    c = {nm.split(".")[0]: v for nm, v in registry.cells().items()}
    return c if names is None else {n: c[n] for n in names}


def figure(names=None):
    return frozenset(cells(names).values())


def closers(X):
    X = frozenset(X)
    cl, _b = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def _join(a, b):
    return tuple(max(x, y) for x, y in zip(a, b))


def threads(names=None):
    F = figure(names)
    who = {v: k for k, v in cells(names).items()}
    return [(who[a], who[b], _join(a, b), _join(a, b) in F)
            for a, b in itertools.combinations(sorted(F), 2)]


def escaping(names=None):
    return [(a, b, j) for a, b, j, lands in threads(names) if not lands]


def report():
    F = figure()
    C = cells()
    q = {nm.split(".")[0]: r[-1] for nm, *r in registry.rows()}
    print("=" * 74)
    print("THE FIGURE THE ELEMENT INDEXES MAKE")
    print("=" * 74)
    print()
    print("1. THE VERTICES. Every member of every one carries quantum numbers.")
    print("   %-20s %-13s %s" % ("index", "cell", "quantum numbers"))
    for n, c in sorted(C.items(), key=lambda kv: kv[1]):
        print("   %-20s %-13s %s" % (n, str(c), q[n]))
    print()
    print("2. THE FIGURE.")
    print("   vertices   %d" % len(F))
    print("   closes     %s" % (", ".join(closers(F)) or "nothing"))
    print("   own cell   %s" % (mi.cell(F),))
    print("   E          %d" % demand.E(F))
    print()
    print("3. WHAT IT DEMANDS.")
    for c in demand.demand(F):
        lo, hi = demand.size_band(c)
        print("   %-13s needs %d..%d members" % (str(c), lo, hi))
    print()
    print("4. REFUSED: to report a growth narrative -- the old one was an")
    print("   artefact of the order a contaminated set was seated in, and no")
    print("   clean trajectory exists yet. To name a shape: seven vertices is")
    print("   what there are today, not a finding.")
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-54s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    chk("the criterion holds on every vertex", registry.enforce(), [])
    C = cells()
    chk("seven vertices", len(C), 7)
    chk("and seven distinct cells", len(figure()), 7)
    chk("every vertex is a registered element index",
        sorted(C) == sorted(n.split(".")[0] for n, *_r in registry.rows()), True)
    chk("no filing-system index is present",
        [n for n in C if n in ("store", "dockets", "manifest", "cross")], [])
    F = figure()
    chk("every cell is a 3-tuple", {len(c) for c in F}, {3})
    chk("the join-closure contains the figure", F <= demand.closure(F)[0], True)
    chk("E equals the demand it names", demand.E(F), len(demand.demand(F)))
    t = threads()
    chk("every pair is a thread", len(t), len(F) * (len(F) - 1) // 2)
    chk("escapes and landings partition the pairs",
        len(escaping()) + len([1 for *_x, l in t if l]), len(t))
    print("figure selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
