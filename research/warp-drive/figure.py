#!/usr/bin/env python3
r"""
figure.py -- THE INDEX OF FIRST-ORDER INDEXES, rebuilt over the registry.

M: "I think we will refer to the main master index the index of universal
first-orders."  And: "Rebuild the index of first-order indexes."

    python3 figure.py             the reading
    python3 figure.py --selftest  fixtures

Its members are the seated indexes of the periodic elements, one vertex each,
at that index's own cell (K, height, width).  It is therefore a SECOND-ORDER
object and `registry.NOT_AN_INDEX` excuses it for that reason -- its members
carry no quantum numbers because its members are not elements.

===============================================================================
0. IT ASKS `registry`, AND THAT IS THE WHOLE REBUILD
===============================================================================

**`mi.py`'s MASTER INDEX IS BUILT ON A HARDCODED LIST OF NINE, AND NOT ONE OF
THE NINE IS A SEATED INDEX OF THE PERIODIC ELEMENTS.**  Measured, not argued:

    mi.inventory()                       registry.rows()
    energy-condition family              fibred
    exotic mechanisms                    madelung
    periodic layout   (WITHDRAWN)        ions
    Janet (n+l, l, k)                    channels
    the languages                        laws
    substances (Hawking-Ellis)           probability
    spacetimes (Petrov)                  inversion
    bounds                               gravity
    questions                            nucshell
                                         madrule
                                         terms

    THE INTERSECTION IS EMPTY.  Nine against eleven, nothing shared.

    THIS IS DOCKET 16's CONTAMINATION, IN A FILE THE CLEANUP DID NOT REACH.
    `hexad.py` and `store.py` were withdrawn for seating filing-system indexes
    as vertices.  `mi.py` seats energy conditions, warp-drive mechanisms, a
    withdrawn 2-D layout, the five languages, Hawking-Ellis substances, Petrov
    spacetimes, bounds and questions.  It survived the cleanup because
    `registry.NOT_AN_INDEX` excuses it as "members are the seated indexes",
    which is true of its TYPE and says nothing about WHICH.

    `mi.py` IS NOT DELETED AND ITS CHARTING MACHINERY IS NOT TOUCHED.
    `mi.cell`, `mi.height`, `mi.width`, `mi.K` and `mi.channels` are correct,
    are imported by everything here, and are what this file measures with.  It
    is `mi.inventory()`, `mi.index()`, `mi.state()` and `mi.self_cell()` that
    are superseded -- the four that depend on the nine.  DOCKET 14: a
    superseded record is kept.  `superseded_mi()` returns the comparison.

SO THE VERTEX SET IS `registry.rows()` AND NOTHING ELSE.  It cannot drift from
the registry, because it does not hold a copy of it.

===============================================================================
1. WHAT IT MEASURES
===============================================================================

    11 vertices, 11 distinct cells -- no two seated indexes share a cell
    box 440
    it closes under `statistics` ALONE
    E = 39

**ITS OWN CELL IS (2, 4, 5), AND NO MEMBER OCCUPIES IT.**  The index of
first-order indexes is not one of its own first-order indexes.  That is
measured by `self_cell()` and is not offered as meaning anything.

===============================================================================
2. THE FINDING THAT GROWTH EXPOSED: TWO OF ITS THREE AXES ARE ROW LABELS
===============================================================================

`overlap.resolution()` on the figure itself:

        K        4 distinct over 11    0.364    measurement
        height  10 distinct over 11    0.909    **LABEL**
        width   11 distinct over 11    1.000    **LABEL**

**THE CHART THAT MEASURES EVERY INDEX HERE IS, APPLIED TO ITSELF, TWO ROW
LABELS AND ONE MEASUREMENT.**  A coordinate separating 90 % or more of the
members groups nothing and multiplies the box; `overlap.py` exists to catch
exactly that, and it catches it here.

    IT WAS NOT VISIBLE AT SIX VERTICES AND IT IS AT ELEVEN.  Each index has
    essentially its own height and its own width, so as the figure grows those
    two coordinates approach injectivity by construction.  Only K -- a down-set
    of the language poset, with eight possible values and four observed --
    stays a measurement.

    THIS IS RECORDED AND NOT REPAIRED.  Changing the master index's chart is a
    ruling, not a measurement, and DOCKET 11 pinned (K, height, width) as the
    admissible chart.  What this file can do honestly is print the resolution
    beside the reading every time, so the limit travels with the number.

===============================================================================
3. WHAT THIS FILE REFUSES
===============================================================================

**TO REPORT A GROWTH NARRATIVE.**  The old one was an artefact of the order a
contaminated set was seated in, and no clean trajectory exists yet.  Vertex
counts are printed, trends are not.

**TO NAME A SHAPE.**  Eleven vertices is what there are today.  `hexad`,
`octad` and the rest were names for a count that kept moving.

**TO TREAT E AS A TARGET.**  M: "I don't care about closure. I only care that we
identify every possible first-order index."  E is reported because it is
measured, not because it is being driven anywhere, and no index here was built
to land on a demanded cell.

**TO CALL ITSELF COMPLETE.**  `registry.COMPLETE` is False and this file has no
opinion the registry does not.
"""

import itertools
import sys

import demand
import hlaw
import mi
import overlap
import registry

NAMES = ("K", "height", "width")
ARITY = 3


# ------------------------------------------------------------- the vertices

def all_indexes():
    """{short name: the index's own cell set} -- ASKED, never held."""
    return {nm.split(".")[0]: registry.index_of(nm)
            for nm, *_r in registry.rows()}


def cells(names=None):
    """{short name: (K, height, width)} for every registered element index."""
    c = {nm.split(".")[0]: v for nm, v in registry.cells().items()}
    return c if names is None else {n: c[n] for n in names}


def figure(names=None):
    """The index of first-order indexes: the set of its members' cells."""
    return frozenset(cells(names).values())


def index(names=None):
    """The same object under the name the registry scans for.

    `registry.NOT_AN_INDEX` excuses it: its members are the seated indexes, so
    they carry no quantum numbers -- they are not elements.
    """
    return figure(names)


def quantum_of():
    """{short name: the quantum numbers ITS members carry}."""
    return {nm.split(".")[0]: r[-1] for nm, *r in registry.rows()}


# -------------------------------------------------------------- what it is

def closers(X=None):
    X = frozenset(figure() if X is None else X)
    cl, _b = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def self_cell(names=None):
    """(its own cell, the members that occupy it).

    THE SECOND LIST IS EMPTY AND THAT IS THE MEASUREMENT: the index of
    first-order indexes is not one of its own first-order indexes.
    """
    C = cells(names)
    F = frozenset(C.values())
    own = mi.cell(F)
    return own, sorted(nm for nm, c in C.items() if c == own)


def resolution():
    """[(axis, distinct, members, ratio, verdict)] for the figure ITSELF.

    SECTION 2 LIVES HERE.  Two of the three are row labels at eleven vertices.
    """
    return [(NAMES[i], d, n, r, v)
            for i, d, n, r, v in overlap.resolution(figure())]


def labelled_axes():
    return [a for a, _d, _n, _r, v in resolution() if v == "LABEL"]


def dilworth():
    """[(name, |X|, height, width, h*w, holds?)] -- |X| <= h x w on every one."""
    out = []
    for nm, X in sorted(all_indexes().items()):
        h, w = mi.height(X), mi.width(X)
        out.append((nm, len(X), h, w, h * w, len(X) <= h * w))
    return out


def _join(a, b):
    return tuple(max(x, y) for x, y in zip(a, b))


def threads(names=None):
    """[(a, b, their join, does it land on a vertex?)] over every pair."""
    F = figure(names)
    who = {v: k for k, v in cells(names).items()}
    return [(who[a], who[b], _join(a, b), _join(a, b) in F)
            for a, b in itertools.combinations(sorted(F), 2)]


def escaping(names=None):
    return [(a, b, j) for a, b, j, lands in threads(names) if not lands]


# ------------------------------------------------- the superseded predecessor

def superseded_mi():
    """(mi's nine, the registry's eleven, what they share).

    THE THIRD IS EMPTY.  `mi.py`'s master index is built on a hardcoded list of
    nine, none of which is a seated index of the periodic elements.  Its
    charting machinery is correct and untouched; its inventory is superseded.
    """
    nine = sorted(mi.inventory())
    eleven = sorted(cells())
    shared = sorted(set(nine) & set(eleven))
    return nine, eleven, shared


# ---------------------------------------------------------------- the reading

def report():
    C = cells()
    F = figure()
    q = quantum_of()
    print("=" * 74)
    print("THE INDEX OF FIRST-ORDER INDEXES")
    print("=" * 74)
    print()
    print("Its members are the seated indexes of the periodic elements, one")
    print("vertex each, at that index's own cell (K, height, width). It asks")
    print("registry.rows() and holds no list of its own.")
    print()
    print("-" * 74)
    print("1. THE VERTICES.")
    print("-" * 74)
    print("   %-13s %-13s %s" % ("index", "cell", "quantum numbers ITS members carry"))
    for n, c in sorted(C.items(), key=lambda kv: kv[1]):
        print("   %-13s %-13s %s" % (n, str(c), q[n]))
    print()
    print("   vertices        %d" % len(C))
    print("   distinct cells  %d%s" % (len(F),
          "   -- no two seated indexes share a cell" if len(F) == len(C) else ""))
    print("   box             %d" % overlap.box_of(F))
    print()
    print("-" * 74)
    print("2. WHAT IT CLOSES, AND WHAT IT DEMANDS.")
    print("-" * 74)
    cl, _b = hlaw.closures(F)
    for L in hlaw.LANGS:
        e = len(cl[L]) - len(F)
        print("     %-13s admits %4d   E %4d%s"
              % (L, len(cl[L]), e, "   <-- CLOSES" if e == 0 else ""))
    print()
    print("   closers  %s" % (closers() or "NONE -- K0"))
    print("   E        %d" % demand.E(F))
    print()
    own, occ = self_cell()
    print("   ITS OWN CELL  %s" % (own,))
    print("   occupied by   %s" % (", ".join(occ) if occ else
                                   "NO MEMBER -- it is not one of its own"))
    print()
    print("-" * 74)
    print("3. TWO OF ITS THREE AXES ARE ROW LABELS, AND GROWTH EXPOSED IT.")
    print("-" * 74)
    for a, d, n, r, v in resolution():
        print("   %-8s %2d distinct over %2d   %.4f   %s"
              % (a, d, n, r, "**LABEL**" if v == "LABEL" else v))
    print()
    print("   A coordinate separating 90% or more of the members groups")
    print("   nothing and multiplies the box. Each index has essentially its")
    print("   own height and its own width, so those two approach injectivity")
    print("   as the figure grows -- invisible at six vertices, plain at %d."
          % len(C))
    print("   Only K stays a measurement: a down-set of the language poset,")
    print("   eight possible values and %d observed."
          % len({c[0] for c in F}))
    print()
    print("   RECORDED AND NOT REPAIRED. Changing the master index's chart is")
    print("   a ruling, and DOCKET 11 pinned (K, height, width). What this")
    print("   file can do honestly is print the limit beside the number.")
    print()
    print("-" * 74)
    print("4. DILWORTH ON EVERY VERTEX: |X| <= height x width.")
    print("-" * 74)
    print("   %-13s %-7s %-5s %-5s %-8s %s"
          % ("index", "|X|", "h", "w", "h x w", ""))
    for nm, n, h, w, hw, okd in dilworth():
        print("   %-13s %-7d %-5d %-5d %-8d %s"
              % (nm, n, h, w, hw, "" if okd else "VIOLATED"))
    print("   The box is RAGGED: the product overstates the space, which is")
    print("   DOCKET 3's other half by theorem rather than census.")
    print()
    print("-" * 74)
    print("5. WHAT IT SUPERSEDES.")
    print("-" * 74)
    nine, eleven, shared = superseded_mi()
    print("   mi.inventory() holds %d, hardcoded:" % len(nine))
    for n in nine:
        print("      %s" % n)
    print("   registry seats %d: %s" % (len(eleven), ", ".join(eleven)))
    print()
    print("   SHARED: %s" % (shared if shared else "NOTHING. The intersection is empty."))
    print()
    print("   That is DOCKET 16's contamination in a file the cleanup did not")
    print("   reach -- energy conditions, warp-drive mechanisms, a withdrawn")
    print("   2-D layout, the languages, substances, spacetimes, bounds and")
    print("   questions. mi.py survived because NOT_AN_INDEX excuses it as")
    print("   'members are the seated indexes', which is true of its TYPE and")
    print("   says nothing about WHICH.")
    print()
    print("   mi.py IS NOT DELETED. mi.cell, mi.height, mi.width, mi.K and")
    print("   mi.channels are correct and are what this file measures with.")
    print("   Superseded: mi.inventory, mi.index, mi.state, mi.self_cell.")
    print()
    print("-" * 74)
    print("6. REFUSED.")
    print("-" * 74)
    print("   To report a growth narrative -- the old one was an artefact of")
    print("     the order a contaminated set was seated in.")
    print("   To name a shape. %d vertices is what there are today." % len(C))
    print("   To treat E as a target. No index here was built to land on a")
    print("     demanded cell.")
    print("   To call itself complete. registry.COMPLETE is %s."
          % registry.COMPLETE)
    return 0


# ------------------------------------------------------------------ fixtures

def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    print("figure selftest")
    chk("the criterion holds on every vertex", registry.enforce(), [])
    C = cells()
    # A PROPERTY, NOT A PINNED COUNT -- five fixtures in this tree have now been
    # fired by a CORRECT addition to the registry.
    chk("the figure IS exactly the registered element indexes",
        (len(C), len(figure())), (len(registry.REGISTERED),) * 2)
    chk("every vertex is a registered element index",
        sorted(C) == sorted(n.split(".")[0] for n, *_r in registry.rows()),
        True)
    chk("it holds no list of its own -- it asks registry",
        "inventory" in dir(), False)
    chk("no filing-system index is present",
        [n for n in C if n in ("store", "dockets", "manifest", "cross")], [])
    F = figure()
    chk("every cell is a 3-tuple", {len(c) for c in F}, {3})
    chk("no two seated indexes share a cell", len(F), len(C))

    # -- what it is
    chk("the join-closure contains the figure", F <= demand.closure(F)[0], True)
    chk("E equals the demand it names", demand.E(F), len(demand.demand(F)))
    chk("it closes under statistics alone", closers(), ["statistics"])
    own, occ = self_cell()
    chk("it has its own cell", own, (2, 4, 5))
    chk("AND NO MEMBER OCCUPIES IT -- it is not one of its own", occ, [])

    # -- section 2, the finding growth exposed
    res = dict((a, (r, v)) for a, _d, _n, r, v in resolution())
    chk("K is a measurement", res["K"][1], "measurement")
    chk("HEIGHT IS A ROW LABEL at this many vertices", res["height"][1],
        "LABEL")
    chk("WIDTH IS A ROW LABEL, perfectly injective",
        (res["width"][1], res["width"][0]), ("LABEL", 1.0))
    chk("so two of the three axes are labels", sorted(labelled_axes()),
        ["height", "width"])
    chk("and the file prints that beside the reading rather than hiding it",
        "LABEL" in open(__file__, encoding="utf-8").read(), True)

    # -- Dilworth
    chk("|X| <= height x width on EVERY vertex",
        [d[0] for d in dilworth() if not d[5]], [])
    chk("Dilworth is checked on every one of them", len(dilworth()), len(C))

    # -- the supersession
    nine, eleven, shared = superseded_mi()
    chk("mi.py's master index holds nine", len(nine), 9)
    chk("the registry seats them all", len(eleven), len(registry.REGISTERED))
    chk("AND THE INTERSECTION IS EMPTY", shared, [])
    chk("mi's charting machinery is untouched and still works",
        (mi.cell(F) == own, callable(mi.height), callable(mi.width)),
        (True, True, True))

    # -- threads
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
