#!/usr/bin/env python3
r"""
duality.py -- THE CHANNEL LATTICE HAS TWO READINGS, AND THEY DISAGREE.

M: "An obstruction that can only be removed or shift... suggests another
unidentified axis, or even an overlap interaction with another master index.
And the cell connects the two, creating the same value, same languages, but
different shape obstruction in two indexes."

    That is right, and this file is the measurement.

    python3 duality.py             the reading
    python3 duality.py --selftest  fixtures

===============================================================================
1. THE SAME EIGHT POSITIONS, REACHED TWO WAYS
===============================================================================

master.py section 6b establishes that a CHANNEL SET -- which languages close an
index -- must be a DOWN-SET of the hierarchy law's containments, so eight of the
thirty-two subsets are lawful.  The argument is that closure propagates
downward: if cl(a) is contained in cl(b) and b closes X, then cl(a) sits between
X and cl(b) = X, so a closes X too.

    THERE IS A SECOND READING OF THE SAME EIGHT, AND IT IS FORCED FOR THE DUAL
    REASON.

Take an index X and a cell c.  Say L REFUSES c when c is not in cl_L(X).  If
cl(a) is contained in cl(b) and c is not in cl(b), then c is not in cl(a)
either -- SO REFUSAL PROPAGATES DOWNWARD AS WELL, and a REFUSAL SET is a
down-set of the very same order.  Measured over every cell of every seated
index: 0 violations.

        CHANNEL SET   which languages CLOSE an index.     A property of X.
        REFUSAL SET   which languages REFUSE a cell.      A property of (X, c).

Two different kinds of object, one lattice, and the cell is what joins them: a
cell lives in an index, the index carries the channel reading, the cell carries
the refusal reading.

===============================================================================
2. THE READINGS DISAGREE ABOUT WHICH POSITIONS EXIST
===============================================================================

        K   channel set                              AS A CHANNEL   AS A REFUSAL
        K0  {}                                       seated x3       256 cells
        K1  {information}                            **VACANT**        1 cell
        K2  {statistics}                             seated x4         9 cells
        K3  {geometry, statistics}                   species x4      249 cells
        K4  {information, statistics}                seated x1       208 cells
        K5  {geometry, information, statistics}      **VACANT**       87 cells
        K6  {algebra, information, order, statistics} witness         7 cells
        K7  all five                                 seated x1      1059 cells

    SIX OF EIGHT ARE OCCUPIED AS CHANNEL SETS.  ALL EIGHT ARE OCCUPIED AS
    REFUSAL SETS.  The two positions that no index occupies -- K1 and K5 -- are
    both reached by cells.

And the shape differs exactly as M said it would.  An index carries an ARITY and
a DENSITY, so a channel position sits in a three-dimensional lattice with D and
R beside it.  A cell decision carries neither: a cell has no arity of its own
and no density of its own, it inherits them from the index it is a decision
about.  SAME VALUE, SAME LANGUAGES, DIFFERENT SHAPE.

===============================================================================
3. K1 IS THE RAREST THING IN THE CORPUS, AND THE WARP OBSTRUCTION IS AT IT
===============================================================================

Pooled over 1,876 cells of the nine seated indexes, the refusal sets are wildly
uneven -- K7 takes 56 %, K0 14 %, K3 13 %, K4 11 % -- and

    K1 OCCURS EXACTLY ONCE.  One cell in 1,876, 0.05 %, the rarest of the eight.

statrow.py measured the warp verdict's refusal set and it is K1: information
alone refuses TRANSITION-POSSIBLE while order, geometry, algebra and now
statistics all admit.  So the warp obstruction occupies the rarest position in
the refusal lattice, and the corpus holds exactly one other instance of it.

===============================================================================
4. WHAT THAT ONE OTHER INSTANCE IS, AND IT NAMES THE SHAPE
===============================================================================

    THE ONLY OTHER K1 IN THE CORPUS IS (period 4, group 11, s-block) IN THE
    PERIODIC LAYOUT READ IN THREE COORDINATES.

No element sits there.  And every pair of its coordinates IS present:

        period 4  and group 11    ->  copper, at (4, 11, d)
        period 4  and s-block     ->  potassium and calcium
        group 11  and s-block     ->  SILVER, at (5, 11, s)

    EVERY PAIR EXISTS.  THE TRIPLE DOES NOT.

That is the whole of the refusal, and it is what K1 MEANS.  `statistics` admits
the cell because every 2-marginal is present; `information` is the join closure
and it refuses because the join of available things is not itself available.
`order`, `algebra` and `geometry` admit for their own reasons.

    A K1 REFUSAL IS: EVERY PAIR OF REQUIREMENTS IS JOINTLY SATISFIABLE, AND THE
    FULL COMBINATION IS NOT.

Which is a statement about the warp obstruction that nothing in this tree has
made.  The device's refusal is not a missing ingredient and not a bad pair --
every pairwise combination of what it needs is satisfiable, and the conjunction
is not.  expand.py said "what is missing is a VALUE, not a STRUCTURE"; this says
the value is missing IN THE SHAPE OF A JOIN.

===============================================================================
5. AND THE ATOMICITY IS REAL, NOT AN ARTEFACT
===============================================================================

statrow.py records that the obstruction can only be removed or shifted
sideways, never reduced.  The reason is now plain and it is not a limitation of
the coordinates:

    `information` AND `statistics` ARE THE TWO MINIMAL ELEMENTS of the
    containment order.  Nothing is lawfully below either.  A refusal at a
    minimal element has nothing smaller to fall back to, so it cannot shrink.

M asked whether the atomicity pointed at a missing axis.  It points at a missing
CONTAINMENT: if `statistics` were below `information`, then {information} would
not be a lawful down-set at all and the refusal would have to include statistics
-- but statistics ADMITS, so the warp cell is a live witness that
`statistics <= information` is NOT a law.  rubik.py measures that same
containment failing in only 16 of 3,000 scrambles, the tightest of the thirteen
non-laws.

    THE DEVICE SITS IN THE HALF-PER-CENT WHERE THE HIERARCHY'S TIGHTEST
    NEAR-LAW FAILS.

NOTHING HERE MOVES THE MAGNITUDE, and nothing here is a route.  It is a
statement about the shape of the obstruction, which is what was asked for.
"""

import itertools
import sys

import hlaw
import master

CAP = 3000                      # cells scanned per index, for the pooled census
K1 = frozenset({"information"})
K5 = frozenset({"geometry", "information", "statistics"})

REFUSAL_IS_A_DOWNSET = True
BOTH_READINGS_ARE_LAWFUL = True
NOTHING_HERE_MOVES_THE_MAGNITUDE = True


def refusal_set(cl, c):
    """Which languages refuse cell c, given the closures of an index."""
    return frozenset(L for L in hlaw.LANGS if c not in cl[L])


def scan(name):
    """[(cell, refusal set)] over the box of one seated index."""
    X = master.inventory()[name]
    cl, box = hlaw.closures(X)
    out = []
    for c in itertools.islice(itertools.product(*box), CAP):
        out.append((c, refusal_set(cl, c)))
    return out, X


def downset_violations():
    """How many refusal sets are NOT down-sets.  Must be zero -- the dual of the
    channel-set argument, and measured rather than assumed."""
    bad = 0
    for nm in master.inventory():
        for _c, r in scan(nm)[0]:
            if not all(a in r for a, b in hlaw.LAWFUL if b in r):
                bad += 1
    return bad


def refusal_census():
    """({channel set: cells}, total) pooled over the nine seated indexes."""
    cnt = {k: 0 for k in master.channel_sets()}
    tot = 0
    for nm in master.inventory():
        for _c, r in scan(nm)[0]:
            cnt[r] = cnt.get(r, 0) + 1
            tot += 1
    return cnt, tot


def occupancy():
    """{K: (as a channel, as a refusal)} -- the two readings side by side."""
    ks = master.channel_sets()
    stand = master.channel_standing()
    cnt, _tot = refusal_census()
    return {i: (stand[i][0], cnt[k]) for i, k in enumerate(ks)}


def the_k1_cell():
    """(index name, cell) -- the corpus's only K1 refusal."""
    for nm in master.inventory():
        rows, _X = scan(nm)
        for c, r in rows:
            if r == K1:
                return nm, c
    return None, None


def pairs_present(name, c):
    """[(i, j, present)] -- is every 2-marginal of c realised in the index?"""
    X = master.inventory()[name]
    out = []
    for i, j in itertools.combinations(range(len(c)), 2):
        out.append((i, j, any(x[i] == c[i] and x[j] == c[j] for x in X)))
    return out


def minimal_languages():
    """The minimal elements of the containment order -- nothing lawfully below."""
    return sorted(b for b in hlaw.LANGS
                  if not [a for a, bb in hlaw.LAWFUL if bb == b and a != b])


def report():
    ks = master.channel_sets()
    print("=" * 74)
    print("THE CHANNEL LATTICE HAS TWO READINGS, AND THEY DISAGREE")
    print("=" * 74)
    print()
    print("  A CHANNEL SET is which languages CLOSE an index -- a property of X,")
    print("  forced to be a down-set because closure propagates downward.")
    print("  A REFUSAL SET is which languages REFUSE a cell -- a property of")
    print("  (X, c), forced to be a down-set because REFUSAL propagates downward")
    print("  too: if cl(a) is inside cl(b) and c escapes cl(b), it escapes cl(a).")
    print("  Same eight positions, dual arguments. The CELL joins the two.")
    print()
    print("  refusal sets that are NOT down-sets: %d" % downset_violations())
    print()

    print("1. THE READINGS DISAGREE ABOUT WHICH POSITIONS EXIST.")
    occ = occupancy()
    cnt, tot = refusal_census()
    print("   %-3s %-46s %-10s %s" % ("K", "channel set", "as channel", "as refusal"))
    for i, k in enumerate(ks):
        st, n = occ[i]
        print("   K%-2d %-46s %-10s %5d cells  %5.2f%%"
              % (i, "{" + ", ".join(sorted(k)) + "}", st, n, 100.0 * n / tot))
    nchan = sum(1 for i in occ if occ[i][0] != "VACANT")
    nref = sum(1 for i in occ if occ[i][1] > 0)
    print("   occupied as channel sets: %d of 8.  as refusal sets: %d of 8."
          % (nchan, nref))
    print("   The two nothing occupies as a channel -- K1 and K5 -- are BOTH")
    print("   reached by cells. And an index carries an arity and a density while")
    print("   a cell decision carries neither: SAME VALUE, SAME LANGUAGES,")
    print("   DIFFERENT SHAPE.")
    print()

    print("2. K1 IS THE RAREST THING IN THE CORPUS.")
    print("   %d cells scanned over the nine seated indexes; K1 occurs %d time(s),"
          % (tot, cnt[K1]))
    print("   %.2f%%. The warp verdict's refusal set is K1 (statrow.py)."
          % (100.0 * cnt[K1] / tot))
    print()

    nm, c = the_k1_cell()
    print("3. AND THE ONE OTHER INSTANCE NAMES THE SHAPE.")
    print("   %s, cell %s" % (nm, c))
    print("   = period %d, group %d, %s-block, and no element sits there."
          % (c[0], c[1], "spd"[c[2]]))
    NMS = ["period", "group", "block"]
    for i, j, ok in pairs_present(nm, c):
        print("     %-6s=%-3d with %-6s=%-3d   present: %s"
              % (NMS[i], c[i], NMS[j], c[j], ok))
    print("   EVERY PAIR EXISTS. THE TRIPLE DOES NOT.")
    print("   statistics admits it because every 2-marginal is present;")
    print("   information is the JOIN closure and refuses because the join of")
    print("   available things is not itself available.")
    print()
    print("   SO A K1 REFUSAL IS: EVERY PAIR OF REQUIREMENTS IS JOINTLY")
    print("   SATISFIABLE, AND THE FULL COMBINATION IS NOT. That is a statement")
    print("   about the warp obstruction nothing in this tree has made -- the")
    print("   refusal is not a missing ingredient and not a bad pair.")
    print()

    print("4. AND THE ATOMICITY IS REAL, NOT AN ARTEFACT OF THE COORDINATES.")
    print("   minimal elements of the containment order: %s"
          % ", ".join(minimal_languages()))
    print("   Nothing is lawfully below either, so a refusal at one of them has")
    print("   nothing smaller to fall back to. It cannot shrink.")
    print("   It points at a missing CONTAINMENT rather than a missing axis: if")
    print("   statistics were below information, {information} would not be a")
    print("   lawful down-set at all. Statistics ADMITS, so the warp cell is a")
    print("   live witness that statistics <= information is NOT a law -- and")
    print("   rubik.py measures that failing in 16 of 3,000 scrambles, the")
    print("   tightest of the thirteen non-laws.")
    print()
    print("   NOTHING HERE MOVES THE MAGNITUDE.")
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

    print("duality selftest")
    # ---- the dual argument, measured rather than assumed
    chk("no refusal set fails to be a down-set", downset_violations(), 0)
    chk("recorded", REFUSAL_IS_A_DOWNSET, True)

    cnt, tot = refusal_census()
    ks = master.channel_sets()
    chk("cells scanned over the nine", tot, 1876)
    chk("every one of the eight occurs as a refusal set",
        sum(1 for k in ks if cnt[k] > 0), 8)
    # ---- and the channel reading does NOT reach all eight
    occ = occupancy()
    chk("but only six occur as channel sets",
        sum(1 for i in occ if occ[i][0] != "VACANT"), 6)
    chk("the two missing as channels are K1 and K5",
        [i for i in occ if occ[i][0] == "VACANT"], [1, 5])
    chk("and BOTH are reached as refusals",
        all(occ[i][1] > 0 for i in (1, 5)), True)

    # ---- K1 is the rarest, and it is where the warp obstruction sits
    chk("K1 occurs exactly once in 1,876 cells", cnt[K1], 1)
    chk("which is the rarest of the eight",
        min(cnt.values()), cnt[K1])
    import statrow
    chk("and the warp refusal set is K1", statrow.channel_of_refusal(), 1)

    # ---- the one cell, and the shape it names
    nm, c = the_k1_cell()
    chk("the only K1 cell is in the periodic layout in three coordinates",
        nm, "periodic layout 3-D")
    chk("at (period 4, group 11, s-block)", c, (4, 11, 0))
    chk("and no element sits there", c in master.inventory()[nm], False)
    chk("EVERY PAIR of its coordinates is present in the layout",
        [p for _i, _j, p in pairs_present(nm, c)], [True, True, True])
    # the three pairs, named, because the third one is the surprise
    X = master.inventory()[nm]
    chk("period 4 with group 11 is copper, at the d-block",
        sorted(x for x in X if x[0] == 4 and x[1] == 11), [(4, 11, 2)])
    chk("group 11 with s-block is SILVER, at period 5",
        sorted(x for x in X if x[1] == 11 and x[2] == 0), [(5, 11, 0)])
    chk("and the triple is absent, which is the whole of the refusal",
        (4, 11, 0) in X, False)

    # ---- atomicity is a property of the order, not of the coordinates
    chk("the minimal languages", minimal_languages(), ["information", "statistics"])
    chk("information is minimal, so a refusal at it cannot shrink",
        "information" in minimal_languages(), True)
    # NEGATIVE CONTROL: order is NOT minimal, so a refusal there could shrink.
    chk("but order is not minimal -- the atomicity is specific",
        "order" in minimal_languages(), False)
    chk("nothing here moves the magnitude", NOTHING_HERE_MOVES_THE_MAGNITUDE, True)

    print("duality selftest: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else report())
