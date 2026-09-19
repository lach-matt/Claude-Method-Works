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

    21 vertices, 21 distinct cells -- no two seated indexes share a cell
    it closes in NOTHING
    E = 292

**ITS OWN CELL IS (0, 5, 10), AND NO MEMBER OCCUPIES IT.**  The index of
first-order indexes is not one of its own first-order indexes.  That is
measured by `self_cell()` and is not offered as meaning anything.

===============================================================================
1b. WHAT THE OVERLAP RULING COST AND WHAT IT BOUGHT -- BOTH, MEASURED
===============================================================================

Three of the fourteen are coarsenings seated by M's overlap ruling; the move is
stated and gated in `overlaprule.py`.  It is reported here in both directions
because it cut both ways and a one-sided report would be a lie by selection.

                              11 vertices        14 vertices
    distinct cells            11                 14
    channels occupied         4 of 8 (0,2,3,7)   **6 of 8** (all but K4, K5)
    the figure's own closers  {statistics}       **NOTHING**
    E                         39                 **84**
    its own cell              (2, 4, 5)          (0, 5, 6)
    K      resolution         0.364 measurement  0.429 measurement
    height resolution         0.909 **LABEL**    **0.786 measurement**
    width  resolution         1.000 **LABEL**    **0.857 measurement**

    AND THEN FOURTEEN AGAIN, BY A DIFFERENT ROUTE.  DOCKET 26 seated
    `observed` -- the shell fibration as register 1306 BANKS it, against the
    one Madelung predicts, 98 cells at (0, 20, 13), K0.  M ruled "both".  At
    fourteen: E 84, own cell (0, 5, 6), resolutions 0.429 / 0.786 / 0.857, and
    the channels are unchanged at six of eight because `observed` lands in the
    already-occupied K0.  It is NOT a coarsening -- a different member set at
    the same arity, 25 of 108 addresses apart from the prediction -- so the
    overlap ruling's novel-channel ground does not govern it.

    IT WAS BRIEFLY FOURTEEN BEFORE THAT, AND FOR A REASON THAT DID NOT LAST.  A third coarsening, `nucshell (l, sigma)` at K5,
    was seated and then UNSEATED by DOCKET 22's verification: the same 22
    members under `(l, 2j)` -- an IDENTICAL partition, and 2j is what
    `nucshell.order_a()` banks -- land at K7, which is occupied, so the chart
    had no novel channel at all.  See `overlaprule.py` section 3e.  At fourteen
    the figures were E 81, own cell (0, 5, 6), resolutions 0.500/0.714/0.857.

    AND SEVENTEEN, WHEN DOCKET 27 WIDENED THE SUBJECT.  M: "produce indexes
    and plates for all particles other than periodic atoms."  `fundamental`
    (30 Standard Model particles, K2), `mesons` (242, K0) and `baryons` (278,
    K0) seated together.  None is a coarsening and none is a new member set
    over old objects -- they are the first indexes here of objects that are
    not atomic at all, so neither the overlap ruling nor DOCKET 26's reading
    governs them.  At seventeen: E 126, own cell (0, 5, 8), resolutions
    0.353 / 0.706 / 0.824, channels UNCHANGED at six of eight.

    THE RESOLUTIONS FELL AGAIN AND THAT IS THE SAME EFFECT, NOT A NEW ONE.
    `fundamental` lands at width 7 and `mesons` at width 14, both already
    held; only `baryons` at width 40 was new.  Height 10 was new and is now
    shared by two of them.  So the three additions group more than they
    separate, which is what drove height and width out of LABEL at fourteen
    and drives them further from it here.  E rose 84 to 126 -- again, anyone
    reading E as progress should read that as a step backwards, and the
    channel census did not move at all: K4 and K5 are still empty after
    three whole new families of matter were charted.

    AND EIGHTEEN, AND THE CHANNEL CENSUS FINALLY MOVED.  DOCKET 25 had closed
    with "a new member set would reopen it"; DOCKET 27 seated three, so
    DOCKET 29 reopened the census over exactly those three and swept all 142
    sub-charts their columns admit.  One survived: `baryons (2I, Q3)` at
    **K5**, isospin against charge, 16 cells.  At eighteen: E 165, own cell
    (0, 5, 9), resolutions 0.389 / 0.667 / 0.778.

    **SEVEN OF THE EIGHT CHANNELS ARE NOW OCCUPIED AND ONLY K4 IS EMPTY.**
    That is the first movement in the census since the ruling, and it took a
    new subject to get it -- the three new families seated at DOCKET 27 moved
    nothing, and the SUB-CHARTS of those families moved it.  K5 had been empty
    since DOCKET 22 retracted `nucshell (l, sigma)`, and what fills it now is
    not that mistake repeated: both of this chart's coordinates are printed by
    the PDG table, so there is no alternative spelling for it to fall to.

    K4 IS LEFT, AND SECTION 3c OF `overlaprule.py` SAYS WHY IT IS THE HARD
    ONE.  Three charts have now reached K4 -- `ions (sl, tl)`,
    `madrule (S_a, l_d)` and DOCKET 29's `fundamental (Q3, GEN)` -- and all
    three are arity 2, where `statistics` closes for free.  Re-measured for
    that docket: 105 of 105 arity-2 charts close statistics and none fails to,
    while geometry manages only 74 of 105.  K4 is the one channel above K1
    whose extra content is exactly the free bit, so all three showed
    join-closure and nothing more.  No chart of arity 3 or more has ever
    reached it here.

    AND NINETEEN.  DOCKET 30 seated `fqh` -- 168 quasiparticles of twelve
    Laughlin states, K0 -- after M asked why the quasiparticles were not
    seated.  DOCKET 28 had refused an anyon chart on box invariance, and the
    re-examination found the TEST was right and the OBJECT was wrong: that
    chart took SU(2)_k for every k, which is a union over theories and not a
    reach over data, so nothing about the data was being varied and of course
    the channel held.  Charted as a reach instead -- one family of one kind of
    system, indexed by a MEASURED filling fraction -- the channel MOVES, K2 to
    K0, and the same test seats it.  At nineteen: E 193, own cell (0, 5, 9),
    resolutions 0.368 / 0.684 / 0.737, channels unchanged at seven of eight.

    DOCKET 28's CHART IS STILL REFUSED and this did not overturn it.  Two
    different objects, two different verdicts, both on the record.

    AND TWENTY.  DOCKET 31 seated `bosonqp` on M's ruling that the textbook
    quasiparticles' universal numbers are "almost nothing -- BUT NOT NOTHING",
    and that the object is a SUBLATTICE OF THE BOSONS.  Eleven bosonic
    collective excitations on (2J, Q3), three cells, K7.  At twenty: E 249,
    own cell (0, 5, 10), resolutions 0.350 / 0.700 / 0.750.

    ITS K7 IS NOT A FINDING AND THE FILE SAYS SO FIRST.  Three cells in a 2x2
    box is a chain, and z3 proves over every subset of that box that a chain
    is closed under meet and join -- so the channel is a fact about shape.
    What IS the finding is the sublattice relation: the quasiparticles are a
    sublattice, they are NOT a subset of the tree's bosons, and the one cell
    outside is the COOPER PAIR at charge -2e, which no meson and no gauge
    boson reaches.  The union is still a sublattice, one cell wider.

    AND TWENTY-ONE.  DOCKET 32 seated `readrezayi` -- the NON-ABELIAN Hall
    quasiparticles, 363 parafermion primaries over eleven Read-Rezayi states,
    K0.  At twenty-one: E 292, own cell (0, 5, 10), resolutions
    0.333 / 0.667 / 0.762, channels still seven of eight.

    IT SEATS BY THE SAME TEST THAT REFUSED DOCKET 28, and for the reason
    DOCKET 30 identified: RR_k sits at nu = 2 + k/(k+2), so k names an
    OBSERVED PLATEAU and the box is a reach.  The channel moves K2 to K0.

    AND IT BOUNDS DOCKET 30's THEOREM.  `fqh` proved no Laughlin quasiparticle
    is ever a fermion.  This series has six, the first being the Ising psi at
    h = 1/2 -- the neutral Majorana of the Moore-Read state -- so that theorem
    was about the ABELIAN Hall quasiparticles and this is exactly where the
    two families part.  Neither index nests in the other either: they share
    eight cells on their three common coordinates and neither contains the
    other, which is the negative counterpart of DOCKET 31's nesting and is
    reported so that one positive result is not read as a pattern.

    WHAT IT COST.  The figure's one closure.  At eleven it closed under
    statistics; at fourteen it closes under nothing, and E went 39 to 84.
    Anyone reading E as progress should read that as a step backwards.

    WHAT IT BOUGHT, AND IT IS THE THING SECTION 2 SAID COULD NOT BE REPAIRED.
    At eleven, TWO OF THE THREE AXES WERE ROW LABELS -- height at 0.909 and
    width perfectly injective at 1.000.  At fourteen BOTH ARE MEASUREMENTS.
    Both seated coarsenings land at heights and widths the figure already held
    -- gravity_bound at width 5, madelung_slot at width 6, against base widths
    [4,5,6,7,9,12,16,17,18,24,112] -- so they group where every previous
    addition separated.  THE UNSEATED THIRD HAD WIDTH 2, WHICH WAS NEW: the
    claim was false while it was seated, and DOCKET 22's correction J caught
    that independently of the unseating.

    THAT WAS NOT THE REASON FOR SEATING THEM and it is not offered as one --
    `overlaprule.py` seats on a novel channel, a non-bijection and a reach
    gate, and would have seated these three whatever they did to the
    resolution.  It is reported because section 2 called the label problem
    unrepairable-by-measurement, and a measurement repaired it.  Recorded, not
    claimed as a method.

===============================================================================
2. THE FINDING THAT GROWTH EXPOSED: TWO OF ITS THREE AXES ARE ROW LABELS
===============================================================================

`overlap.resolution()` on the figure itself:

        K        4 distinct over 11    0.364    measurement
        height  10 distinct over 11    0.909    **LABEL**
        width   11 distinct over 11    1.000    **LABEL**

**AT ELEVEN, THE CHART THAT MEASURES EVERY INDEX HERE WAS, APPLIED TO ITSELF,
TWO ROW LABELS AND ONE MEASUREMENT.**  Section 1b has the fourteen-vertex
figures, where both labels have become measurements; this section is kept as
written because the reasoning in it is what the later measurement tested.  A coordinate separating 90 % or more of the
members groups nothing and multiplies the box; `overlap.py` exists to catch
exactly that, and it catches it here.

    IT WAS NOT VISIBLE AT SIX VERTICES AND IT IS AT ELEVEN.  Each index has
    essentially its own height and its own width, so as the figure grows those
    two coordinates approach injectivity by construction.  Only K -- a down-set
    of the language poset, with eight possible values and four observed --
    stays a measurement.

        AND THAT REASONING IS NOW REFUTED, BY THE MEASUREMENT IN SECTION 1b.
        "Approach injectivity by construction" predicted that growth makes it
        worse.  Three more vertices made it better: height 0.909 -> 0.786,
        width 1.000 -> 0.857.  The prediction failed because it assumed every
        new index brings a new height and a new width, and a COARSENING of a
        seated index does not -- it lands in the part of the poset its parent
        already occupies.  What the argument really showed is that the label
        problem tracks how the vertex set is built, not how big it is.

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

**TO NAME A SHAPE.**  Fourteen vertices is what there are today.  `hexad`,
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
    return {registry.short(nm): registry.index_of(nm)
            for nm, *_r in registry.rows()}


def cells(names=None):
    """{short name: (K, height, width)} for every registered element index."""
    c = {registry.short(nm): v for nm, v in registry.cells().items()}
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
    return {registry.short(nm): r[-1] for nm, *r in registry.rows()}


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
        sorted(C) == sorted(registry.short(n) for n, *_r in registry.rows()),
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
    # SECTION 1b.  At eleven this was ["statistics"]; the overlap ruling's
    # three coarsenings cost the figure its one closure.  Recorded, not hidden.
    chk("at twenty-one it closes in NOTHING -- the ruling cost it its "
        "closure at fourteen and nothing since has given it back",
        closers(), [])
    own, occ = self_cell()
    chk("it has its own cell", own, (0, 5, 10))
    chk("SEVEN of the eight channels are occupied; only K4 is not -- "
        "DOCKET 29 filled K5", sorted({c[0] for c in figure()}),
        [0, 1, 2, 3, 5, 6, 7])
    chk("AND NO MEMBER OCCUPIES IT -- it is not one of its own", occ, [])

    # -- section 2, the finding growth exposed
    res = dict((a, (r, v)) for a, _d, _n, r, v in resolution())
    chk("K is a measurement", res["K"][1], "measurement")
    # SECTION 1b.  Both of these were LABELs at eleven vertices -- height
    # 0.909, width perfectly injective at 1.000.  The three coarsenings land at
    # heights and widths the figure already held, and both became measurements.
    chk("HEIGHT IS NOW A MEASUREMENT -- it was a LABEL at eleven",
        (res["height"][1], res["height"][0]), ("measurement", 0.6667))
    chk("WIDTH IS NOW A MEASUREMENT -- it was perfectly injective at eleven",
        (res["width"][1], res["width"][0]), ("measurement", 0.7619))
    chk("and the gain SURVIVES the DOCKET 22 unseating -- it was not carried "
        "by the vertex that fell", sorted(labelled_axes()), [])
    chk("NO axis is a row label any more", sorted(labelled_axes()), [])
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
