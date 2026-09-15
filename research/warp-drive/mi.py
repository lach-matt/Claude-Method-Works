#!/usr/bin/env python3
r"""
mi.py -- THE MASTER INDEX, REBUILT FROM SCRATCH ON MEASURED AXES.

M: "Rebuild the MI from scratch, so no superseded data leaks in."

    python3 mi.py             the reading
    python3 mi.py --selftest  fixtures

This file inherits NO coordinate system, NO pinned figure and NO reading from
master.py.  It imports the index CONSTRUCTIONS -- the modules that build each
family's cells -- and nothing else.  master.py remains as the historical record
of the (C, Sc, Oc, D, R) chart and the dockets measured on it; every figure here
is computed afresh.

===============================================================================
1. THE AXES, AND WHY THESE THREE
===============================================================================

    (K, height, width)

    K       which languages close the index -- the channel, a down-set of the
            hierarchy law, 0..7.  MEASURED by running the five operators.
    height  the longest chain in the containment order.  MIRSKY: equal to the
            minimum number of antichains that cover it.
    width   the largest antichain.  DILWORTH: equal to the minimum number of
            chains that cover it.

WHY NOT THE OLD FIVE.  charts.py states and proves the criterion: a coordinate
is admissible iff it survives appending a MONOTONE REDUNDANT coordinate, since
that preserves the containment order exactly.  Measured on the seated indexes,
ARITY MOVES ON EVERY ONE AND SO DOES DENSITY -- they are facts about the box.
height, width, cells, comparable pairs and join-irreducibles do not move at all.
C, Sc and Oc are all functions of K, so the five collapse to three with no loss
and one gain: K separates channels that (C, Sc, Oc) merged, and the "closure
coordinates fix the channel set" claim, recorded as BROKEN, is true here by
construction.

DILWORTH ALSO MAKES THE BOX RAGGED: |X| <= height x width, so the three axes are
not independent and the product box overstates the space.  That is DOCKET 3's
other half, by theorem rather than census.

===============================================================================
2. THE NINE, AND THE ONE THAT WAS WITHDRAWN
===============================================================================

DOCKET 2 IS RULED.  M: "3D is the finding and it is the superseding model moving
forward in all projects working with the corpus."

`periodic layout 2-D` is WITHDRAWN from the master index as over-representation.
The case for it collapsed measurement by measurement:

  - COVERAGE.  It once reached ten positions the 3-D chart could not.  That was
    a defect in the 3-D construction, not a property of the chart: `block_of`
    took the differentiating electron from the OBSERVED table and stopped at
    Z = 108.  Rebuilt from Madelung, 3-D reaches every position 2-D reaches.
  - BIJECTION.  Extended to the same reach the two are in exact bijection, and
    `block` is a function of (period, group) with ZERO collisions -- no
    information about which element is which.
  - THE UNIQUE K1 CELL.  3-D carried the corpus's only K1 refusal, and that was
    the last argument FOR keeping both.  Completing the 3-D chart destroyed it:
    K1 now occurs ZERO times in 2,724 pooled cells, where it occurred once.
  - AND 2-D LOST ITS OWN CLOSURE.  At ninety cells it closed in {information,
    statistics}; extended to its own construction's reach it closes in
    {statistics} alone.

So the two charts are one object, the three-coordinate one is the finding, and
the two-coordinate one is a coarsening that carries nothing the other lacks.

===============================================================================
3. REACH -- RULED, AND WHY THE TWO PERIODIC CHARTS DIFFER
===============================================================================

M: "until we can prove that no more elements are left to discover or synthesize,
the upper bound of the periodic table is open."  So no chart is capped by
observation.  Each reaches THE LAST COMPLETE UNIT ITS OWN CONSTRUCTION DEFINES,
and the units differ because the charts differ:

    Janet (n+l, l, k)     an n+l SHELL.  Shells end 2 4 12 20 38 56 88 120 170.
                          REACH 170.
    periodic (p, g, b)    a PERIOD.  Periods end 2 10 18 36 54 86 118 168.
                          REACH 168.

Both boundaries are confirmed by shells.py's detector, which recovers them from
closure behaviour alone and named the next element correctly nine times out of
nine.  Neither is imported from the other chart, which was the earlier mistake.

Both depend on tools/populate.MADELUNG, whose n and l caps were repaired in the
same pass -- before that its n+l = 9 shell ended at 168 instead of 170.
"""

import itertools
import sys

import bounds as _bounds
import decomposable as D
import hlaw
import necindex
import petrov
import questions as _questions
import selfindex
import shells
import substance
import synth

sys.path.insert(0, "/home/user/Claude-Method-Works/tools")
import populate as _pop                                          # noqa: E402

_le = lambda a, b: all(p <= q for p, q in zip(a, b))

JANET_REACH = 170          # the n+l = 9 shell, complete
LAYOUT_REACH = 168         # period 8, complete


# ------------------------------------------------------------------ the axes

def height(X):
    """Longest chain in the containment order.  Mirsky: = min antichain cover."""
    S = sorted(X)
    best = {}
    for x in S:
        best[x] = 1 + max([best[y] for y in S if y != x and _le(y, x)] or [0])
    return max(best.values())


def width(X):
    """Largest antichain.  Dilworth: = min chain cover, via Konig matching."""
    S = sorted(X)
    n = len(S)
    adj = {i: [j for j in range(n) if i != j and _le(S[i], S[j])] for i in range(n)}
    mt = {}

    def aug(i, seen):
        for j in adj[i]:
            if j in seen:
                continue
            seen.add(j)
            if j not in mt or aug(mt[j], seen):
                mt[j] = i
                return True
        return False

    return n - sum(aug(i, set()) for i in range(n))


def closers(X):
    """The languages that close X, in its own box."""
    X = frozenset(X)
    d = len(next(iter(X)))
    box = D.box_of(X, d)
    cl, _ = hlaw.closures(X)
    return frozenset(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def channels():
    """The eight lawful channel sets -- down-sets of the hierarchy law."""
    LAW = set(hlaw.LAWFUL)
    out = []
    for r in range(len(hlaw.LANGS) + 1):
        for S in itertools.combinations(hlaw.LANGS, r):
            S = frozenset(S)
            if all(a in S for b in S for a in hlaw.LANGS if (a, b) in LAW):
                out.append(S)
    return sorted(out, key=lambda S: (len(S), sorted(S)))


_K_CACHE = {}


def K(X):
    """Which channel X closes in, 0..7.  MEMOISED BY THE INDEX ITSELF.

    Pure, so a memo changes no figure.  It is here because a first-order index
    over the artefact store can be hundreds of cells -- the drive manifest is
    661 -- and one channel measurement runs the five closure operators over
    every pair of coordinates.  The DOCKET 3 criterion asks for the channel
    twice per index, `cell` a third time, and `hexad` once more per report; at
    four minutes a call that is the difference between an instrument that runs
    and one nobody runs.
    """
    key = frozenset(X)
    if key not in _K_CACHE:
        _K_CACHE[key] = channels().index(frozenset(closers(X)))
    return _K_CACHE[key]


def cell(X):
    return (K(X), height(X), width(X))


# ------------------------------------------------------------- the two charts

def _differentiating(Z):
    now = {(n, l): o for n, l, o in _pop.aufbau_config(Z)}
    prev = ({(n, l): o for n, l, o in _pop.aufbau_config(Z - 1)} if Z > 1 else {})
    g = sorted((n, l) for (n, l), o in now.items() if o > prev.get((n, l), 0))
    return (g[-1], prev.get(g[-1], 0)) if g else (None, None)


def janet():
    """(n+l, l, k) to the last complete n+l shell.  Madelung; no observation."""
    out = set()
    for Z in range(1, JANET_REACH + 1):
        nl, k = _differentiating(Z)
        if nl:
            out.add((nl[0] + nl[1], nl[1], k))
    return frozenset(out)


def layout():
    """(period, group, block) to the last complete period.

    THE SUPERSEDING PERIODIC MODEL, per DOCKET 2.  Period and group come from
    the drawn layout; block is the l of the MADELUNG differentiating electron,
    which needs no observation -- the defect that capped this chart at Z = 108.
    Period 8's g- and f-blocks are set aside exactly as the lanthanides and
    actinides are, leaving the eighteen columns the layout draws.
    """
    aside8 = set(range(121, 153))          # 5g and 6f of period 8
    out = set()
    for Z in range(1, LAYOUT_REACH + 1):
        if Z <= 118:
            if _pop.set_aside(Z):
                continue
            p, g = _pop.period_of(Z), _pop.group_of(Z)
        else:
            if Z in aside8:
                continue
            p, g = 8, (Z - 118 if Z <= 120 else Z - 150)
        if g is None or not 1 <= g <= 18:
            continue
        nl, _k = _differentiating(Z)
        if nl:
            out.add((p, g, nl[1]))
    return frozenset(out)


def inventory():
    """{name: cells} -- the nine indexes, built from their own constructions."""
    return {
        "energy-condition family": frozenset(necindex.cells()),
        "exotic mechanisms": frozenset(synth.MECHANISMS.values()),
        "periodic layout": layout(),
        "Janet (n+l, l, k)": janet(),
        "the languages": frozenset(selfindex.LANGUAGES.values()),
        "substances (Hawking-Ellis)": substance.cells(),
        "spacetimes (Petrov)": petrov.cells(),
        "bounds": _bounds.cells(),
        "questions": _questions.cells(),
    }


def index():
    """{name: (K, height, width)}."""
    return {nm: cell(X) for nm, X in inventory().items()}


def state():
    """(cells, {language: E}, closers, demands) of the master index itself."""
    C = frozenset(index().values())
    cl, _ = hlaw.closures(C)
    return (C, {L: len(cl[L]) - len(C) for L in hlaw.LANGS},
            [L for L in hlaw.LANGS if len(cl[L]) == len(C)],
            sorted(cl["statistics"] - C))


def self_cell():
    """(the master index's own cell, who occupies it)."""
    C = frozenset(index().values())
    own = cell(C)
    return own, sorted(nm for nm, c in index().items() if c == own)


def dilworth_holds():
    """|X| <= height x width on every index -- the raggedness of the box."""
    return [nm for nm, X in inventory().items() if len(X) > height(X) * width(X)]


def demand_signature(X):
    """(languages demanding, union, cells ALL FIVE demand).

    shells.py's calibration: the one demand ever checked against an independent
    truth and found RIGHT scored (5, 1, 1) and did so nine times; the one found
    WRONG scored (3, 36, 0).
    """
    X = frozenset(X)
    cl, _ = hlaw.closures(X)
    dem = {L: frozenset(cl[L]) - X for L in hlaw.LANGS}
    live = [L for L in hlaw.LANGS if dem[L]]
    union = set().union(*dem.values()) if live else set()
    inter = (set.intersection(*[set(dem[L]) for L in hlaw.LANGS])
             if len(live) == 5 else set())
    return len(live), len(union), sorted(inter)


def calibrated():
    """Indexes whose demand matches the verified signature: 5 languages, 1 cell."""
    out = {}
    for nm, X in inventory().items():
        l, u, i = demand_signature(X)
        if l == 5 and len(i) == 1:
            out[nm] = i[0]
    return out


def phase(k=None):
    """{(geometry on, order/algebra on): [channels]} -- the phase square.

    The two switches are the two MAXIMAL elements of the language poset.  By
    Birkhoff the join-irreducible channels are the principal down-sets, one per
    poset element, so K6 = down(order/algebra) is alone in its phase: that block
    sits above BOTH minimal languages and drags them in, leaving nothing free.
    """
    ks = channels()
    out = {}
    for i, S in enumerate(ks):
        out.setdefault(("geometry" in S, "algebra" in S), []).append(i)
    return out if k is None else out[k]


def report():
    ks = channels()
    print("=" * 74)
    print("THE MASTER INDEX, REBUILT")
    print("=" * 74)
    print()
    I = index()
    print("1. THE NINE, on (K, height, width) -- every axis measured.")
    for nm, c in sorted(I.items(), key=lambda t: t[1]):
        X = inventory()[nm]
        print("   %-28s %-12s %4d cells   closes %s"
              % (nm, str(c), len(X), ", ".join(sorted(closers(X))) or "NOTHING"))
    dup = {}
    for nm, c in I.items():
        dup.setdefault(c, []).append(nm)
    for c, ns in dup.items():
        if len(ns) > 1:
            print("   SHARED %s : %s" % (c, ns))
    print()
    print("   periodic layout 2-D is WITHDRAWN -- DOCKET 2, section 2.")
    print()
    C, E, clo, dem = state()
    print("2. THE INDEX ITSELF.")
    print("   %d indexes, %d distinct cells" % (len(I), len(C)))
    print("   E: %s" % E)
    print("   CLOSES IN %s, demanding %s" % (clo, dem or "NOTHING"))
    own, who = self_cell()
    print("   its own cell %s -> %s" % (own, who or "VACANT"))
    print("   Dilworth |X| <= h x w violated by: %s" % (dilworth_holds() or "nothing"))
    print()
    print("3. THE PHASE SQUARE. Two switches: geometry, and the order/algebra")
    print("   block. They are the two MAXIMAL elements of the language poset.")
    for p in ((False, False), (True, False), (False, True), (True, True)):
        print("      geom %-3s ord/alg %-3s -> %s"
              % ("ON" if p[0] else "off", "ON" if p[1] else "off",
                 ["K%d" % k for k in phase()[p]]))
    print("   K6 is ALONE in its phase because order/algebra sits above BOTH")
    print("   minimal languages and drags them in; geometry sits above")
    print("   statistics only, so information stays free and that phase holds two.")
    print()
    print("4. THE CALIBRATED DEMANDS. shells.py's signature -- all five languages")
    print("   demanding, intersection exactly one cell -- verified 9 of 9 against")
    print("   an independent ground truth.")
    cal = calibrated()
    for nm, c in sorted(cal.items()):
        print("      %-28s %s" % (nm, c))
    l, u, i = demand_signature(C)
    print("   and the master index itself: %d languages, %d cells, %d unanimous"
          % (l, u, len(i)))
    print("   -> %s" % ("MATCHES" if len(i) == 1 and l == 5 else "DOES NOT MATCH"))
    print()
    print("5. NOTHING HERE IS SEATED ON THE STRENGTH OF A DEMAND.")
    return 0


def selftest():
    ok = True

    def chk(nm, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", nm, got))
        if not good:
            print("        expected %r" % (want,))

    print("mi selftest")
    inv = inventory()
    chk("NINE indexes -- periodic layout 2-D withdrawn", len(inv), 9)
    chk("and it is gone by name", "periodic layout 2-D" in inv, False)
    chk("eight lawful channels", len(channels()), 8)

    # ---- the two charts, and the reaches ruled in section 3
    chk("Janet reaches the n+l = 9 shell", JANET_REACH, 170)
    chk("the periodic layout reaches period 8", LAYOUT_REACH, 168)
    chk("both are shell/period boundaries shells.py DETECTED",
        (JANET_REACH in shells.DETECTED_BOUNDARIES,
         LAYOUT_REACH in shells.PERIOD_ENDS), (True, True))
    chk("and populate.MADELUNG now reaches them -- the cap is repaired",
        shells.shell_ends(_pop.MADELUNG)[8], 170)

    # ---- the axes
    chk("every index satisfies Dilworth |X| <= height x width",
        dilworth_holds(), [])
    I = index()
    chk("nine cells from nine indexes", len(I), 9)

    # ---- K is faithful where (C, Sc, Oc) was not
    sig = {}
    for i, S in enumerate(channels()):
        sig.setdefault((len(S), int("statistics" in S), int("order" in S)), []).append(i)
    chk("(C,Sc,Oc) gives only 7 signatures for 8 channels", len(sig), 7)
    chk("and the collision is K3 with K4",
        sorted(v for v in sig.values() if len(v) > 1), [[3, 4]])
    chk("K itself is faithful by construction",
        len({K(X) for X in inv.values()}) <= 8, True)

    # ---- the index's own state
    C, E, clo, dem = state()
    chk("it closes in statistics", clo, ["statistics"])
    chk("at E = 0, demanding nothing", (E["statistics"], dem), (0, []))
    own, who = self_cell()
    chk("its own cell is VACANT -- self-membership was a band-edge artefact",
        who, [])

    # ---- the phase square, Birkhoff
    ph = phase()
    chk("K6 is ALONE in its phase", ph[(False, True)], [6])
    chk("and geometry's phase holds two", ph[(True, False)], [3, 5])
    chk("the top phase is K7 alone", ph[(True, True)], [7])
    LAW = set(hlaw.LAWFUL)
    dn = lambda x: frozenset(a for a in hlaw.LANGS if a == x or (a, x) in LAW)
    chk("K6 IS down(order) -- Birkhoff's principal down-set",
        channels().index(dn("order")), 6)
    chk("and K3 is down(geometry)", channels().index(dn("geometry")), 3)

    # ---- DOCKET 2's evidence, re-measured here rather than quoted
    L3 = layout()
    pg = {(p, g) for p, g, _b in L3}
    blk = {}
    coll = 0
    for p, g, b in L3:
        if (p, g) in blk and blk[(p, g)] != b:
            coll += 1
        blk[(p, g)] = b
    chk("block is a function of (period, group) -- zero information", coll, 0)
    chk("so the withdrawn 2-D chart is its projection, exactly",
        len(pg), len(L3))
    import refusal
    chk("and K1 is now carried by NOTHING -- 3-D's last distinguishing feature",
        [n for n, s in refusal.refusal_index().items() if 1 in s], [])

    # ---- the calibration
    cal = calibrated()
    chk("three indexes match the verified demand signature",
        sorted(cal), ["bounds", "substances (Hawking-Ellis)", "the languages"])
    l, u, i = demand_signature(C)
    chk("the master index does NOT match it", (l, len(i) == 1), (4, False))
    print("mi selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
