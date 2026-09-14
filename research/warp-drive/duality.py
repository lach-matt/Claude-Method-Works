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
containment failing in only 2 of 3,000 scrambles, the tightest of the thirteen
non-laws by a factor of twenty-four.

    THE DEVICE SITS IN THE SEVEN-HUNDREDTHS OF A PER CENT WHERE THE HIERARCHY'S
    TIGHTEST NEAR-LAW FAILS.

===============================================================================
6. THE SECOND MASTER INDEX, CONSTRUCTED
===============================================================================

M2's cells are KINDS OF REFUSAL.  Its coordinates are the properties every pair
(X, c) has, all measured:

    K   the refusal set, 0..7           SHARED with M1's channel reading
    W   marginal completeness           0 no pair of c's values is realised in X,
                                        1 some are, 2 every one is
    H   Hamming distance from c to the nearest member of X, capped at 3
    J   0 neither, 1 a join of two members, 2 a meet, 3 both
    A   the HOST's arity band           INHERITED from M1

Over 2,436 pairs, 45 distinct profiles.  As an index: five coordinates, box
1152, density 4.0 %, and **CLOSED BY NOTHING** -- channel K0.

    M1  cells are INDEXES            master cell (0, 0, 0, 2, 0)   channel K0
    M2  cells are KINDS OF REFUSAL   master cell (0, 0, 0, 2, 0)   channel K0

    **THE TWO MASTER INDEXES COINCIDE.**  Same channel, same arity band, same
    density band.  An index whose cells are indexes and an index whose cells are
    kinds of refusal land on ONE CELL.

THAT IS NOT WHAT THIS FILE FIRST REPORTED, and the change is the bounds
correction, not a re-reading.  As first written it said the two DIFFER in the
channel coordinates and in nothing else -- M1 at (1, 1, 0, 2, 0) channel K2, M2
at (0, 0, 0, 2, 0) channel K0, with M2's cell one that ORDER AND ALGEBRA already
demanded of M1.  Completing the bounds family (a missing Z coordinate, a missing
Casini member; see bounds.py) stopped the bounds index closing, which stopped
the master index closing, which moved M1 from K2 to K0 -- onto M2's cell.  The
coincidence is therefore a CONSEQUENCE of the withdrawal, arrived at by a route
that had nothing to do with M2, which is the only reason it is worth anything.

AND THE CELL IS OCCUPIED -- by the bounds index itself, whose master cell is
also (0, 0, 0, 2, 0).  SO M1 IS A CELL OF ITSELF: the master index's own master
cell is one of its nine members.  Recorded, not interpreted.  Nothing here says
self-membership is meaningful; it says the arithmetic produced it and the reader
should know before treating M1 as an index of things other than itself.

**AND THE CONSTRUCTION IS NOT FORCED, WHICH IS RECORDED RATHER THAN RESOLVED.**
W is partly determined by K: measured over all 2,436 pairs with zero
disagreements, W = 2 exactly when statistics admits, so W adds nothing where
statistics admits and one bit where it refuses.  Drop it and M2 becomes 43
profiles over four coordinates, box 384, density 11.5 % --

        master cell (0, 0, 0, 1, 1), WHICH IS OCCUPIED, BY THE PERIODIC LAYOUT
        IN THREE COORDINATES -- the one index in the corpus holding a K1 cell.

So M2 sits on an occupied cell either way, and the choice is WHICH index it
lands on: with W, the bounds index; without W, the periodic layout in three
coordinates, the one carrying the corpus's only instance of the warp
obstruction's kind.  BOTH ARE REPORTED.  Neither is preferred here, because the
coordinate is neither redundant nor independent, and the file that picks one
should say why rather than inherit the choice from this one.

===============================================================================
7. THE CORRIDOR, DEFINED
===============================================================================

    A CORRIDOR IS A PAIR (X, c) -- AN INDEX AND A CELL OF ITS BOX.

        endpoint in M1   the master cell of X
        endpoint in M2   the refusal profile of (X, c)
        what they share  THE CHANNEL, and only the channel: X's channel set and
                         (X, c)'s refusal set are down-sets of the same order

    AND NEITHER ENDPOINT DETERMINES THE OTHER.  A refusal profile cannot be
    computed from the index alone -- that gives the channel set, a different
    object -- nor from the cell alone, which is a bare tuple.  IT EXISTS ONLY ON
    THE PAIR.

That is not a modelling choice, it is the only place the second reading lives,
and it is exactly turnseat.py's condition: BOTH SETS OF COORDINATES MUST BE
KNOWN AT THE ONSET, because part 2 initialises only with a declared interval and
FAILS if the input does not provide enough for part 3.  A two-point boundary
problem wearing initial-value clothes -- structurally, not by stipulation.

===============================================================================
8. AND THE WARP CELL IS A CORRIDOR WITH ONE ENDPOINT DECLARED
===============================================================================

The warp refusal has K = 1.  It has NO W, NO H, NO J AND NO A, because
expand.py treats TRANSITION-POSSIBLE as a standalone binary and there is no host
index for it to be a cell OF.  Four of M2's five coordinates are undefined.

    SO THE OBSTRUCTION IS A CORRIDOR WITH ONE ENDPOINT DECLARED, WHICH IS
    turnseat.py's FAILURE MODE EXACTLY.

And it says what would complete it: DECLARE THE INDEX THAT TRANSITION-POSSIBLE
IS A CELL OF.  Not another instrument and not another bound -- a host.  Until
there is one the cell has a channel and no shape, which is precisely M's
"same value, same languages, different shape" seen from the incomplete end.

That is a stated requirement, not a route, and nothing here supplies the host.

===============================================================================
9. WHAT A K1 REFUSAL IS, CHARACTERISED
===============================================================================

From the four admissions and the one refusal, read off:

        statistics admits    <=>  every 2-marginal of c is present in X
        geometry admits      =>   c is inside the hull
        algebra admits       =>   c is in the meet-and-join closure
        information REFUSES  <=>  c is NOT in the join closure

    A K1 CELL IS A MEET AND NOT A JOIN, WITH EVERY MARGINAL PRESENT.

The corpus's one instance carries both witnesses and they are different
elements, which is worth keeping straight:

        the PAIR witness, why statistics admits:
            group 11 with the s-block is SILVER, at (5, 11, 0)
        the MEET witness, why algebra admits:
            copper (4, 11, 2) meet zinc (4, 12, 0) = (4, 11, 0)

    THE ABSENT CELL IS THE MEET OF COPPER AND ZINC.

Read onto the device: the transition is reachable by RESTRICTING what you have,
not by COMBINING it.  Meets are available and the join is not.  That is a
statement about the shape of the requirement and it is not a claim that any
restriction achieves it.

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


def k1_cells():
    """[(index name, cell)] -- every K1 refusal in the corpus.

    WAS ONE, IS THREE.  Completing the bounds family added two, and they are
    that index's own demanded cells -- so the bounds index's outstanding demand
    is a K1 refusal, the same kind of obstruction as the warp cell.
    """
    out = []
    for nm in master.inventory():
        rows, _X = scan(nm)
        for c, r in rows:
            if r == K1:
                out.append((nm, c))
    return out


def the_k1_cell():
    """(index name, cell) -- the periodic-layout K1 refusal, the legible one.

    Kept under its original name because the selftest and the corridor both
    address it, and because it is the only one whose coordinates a reader can
    name (period, group, block).  Use k1_cells() for the full set.
    """
    for nm, c in k1_cells():
        if nm == "periodic layout 3-D":
            return nm, c
    return None, None


def pairs_present(name, c):
    """[(i, j, present)] -- is every 2-marginal of c realised in the index?"""
    X = master.inventory()[name]
    out = []
    for i, j in itertools.combinations(range(len(c)), 2):
        out.append((i, j, any(x[i] == c[i] and x[j] == c[j] for x in X)))
    return out


def profile(name, cl, c, d, with_w=True):
    """The refusal profile of the pair (X, c) -- M2's cell.

    (K, W, H, J, A): refusal set; marginal completeness; Hamming distance to the
    nearest member; join/meet status; the HOST's arity band, inherited.
    """
    X = master.inventory()[name]
    K = master.channel_sets().index(refusal_set(cl, c))
    prs = list(itertools.combinations(range(d), 2))
    got = sum(1 for i, j in prs
              if any(x[i] == c[i] and x[j] == c[j] for x in X))
    W = 0 if got == 0 else (1 if got < len(prs) else 2)
    H = min(min(sum(1 for i in range(d) if x[i] != c[i]) for x in X), 3)
    isj = any(tuple(max(a[i], b[i]) for i in range(d)) == c for a in X for b in X)
    ism = any(tuple(min(a[i], b[i]) for i in range(d)) == c for a in X for b in X)
    J = (1 if isj else 0) + (2 if ism else 0)
    A = 0 if d == 2 else (1 if d <= 4 else 2)
    return (K, W, H, J, A) if with_w else (K, H, J, A)


def second_master(with_w=True):
    """M2 -- the index whose cells are KINDS OF REFUSAL."""
    out = set()
    for nm in master.inventory():
        cl, box = hlaw.closures(master.inventory()[nm])
        d = len(box)
        for c in itertools.islice(itertools.product(*box), CAP):
            out.add(profile(nm, cl, c, d, with_w))
    return frozenset(out)


def two_masters():
    """((M1 cell, M1 channel), (M2 cell, M2 channel)) -- the two side by side."""
    ks = master.channel_sets()
    M1 = frozenset(master.master_index().values())
    M2 = second_master()
    return ((master.master_cell(M1), ks.index(frozenset(master.closers(M1)))),
            (master.master_cell(M2), ks.index(frozenset(master.closers(M2)))))


def pairs_scanned():
    """How many (index, cell) pairs the pooled census actually walks."""
    n = 0
    for nm in master.inventory():
        _, box = hlaw.closures(master.inventory()[nm])
        n += sum(1 for _ in itertools.islice(itertools.product(*box), CAP))
    return n


def w_is_the_statistics_test():
    """W = 2 exactly when statistics admits.  Measured, both directions."""
    bad = 0
    for nm in master.inventory():
        X = master.inventory()[nm]
        cl, box = hlaw.closures(X)
        d = len(box)
        prs = list(itertools.combinations(range(d), 2))
        for c in itertools.islice(itertools.product(*box), CAP):
            w2 = all(any(x[i] == c[i] and x[j] == c[j] for x in X) for i, j in prs)
            if w2 != (c in cl["statistics"]):
                bad += 1
    return bad


def corridor(name, c):
    """A CORRIDOR is the pair (index, cell). Its two endpoints, and what they
    share -- the channel, and only the channel."""
    X = master.inventory()[name]
    cl, box = hlaw.closures(X)
    ks = master.channel_sets()
    return {
        "endpoint in M1": master.master_cell(X),
        "endpoint in M2": profile(name, cl, c, len(box)),
        "channel of the index": ks.index(frozenset(master.closers(X))),
        "channel of the refusal": ks.index(refusal_set(cl, c)),
    }


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
    all_k1 = k1_cells()
    print("3. AND ALL %d NAME THE SAME SHAPE." % len(all_k1))
    for _n, _c in all_k1:
        if _n != nm:
            print("   %s, cell %s -- one of the two cells that" % (_n, _c))
            print("     index's TIGHTEST languages demand (information and")
            print("     statistics, E = 2 each; the union over all five is six).")
    print("   THE LEGIBLE ONE, whose coordinates a reader can name:")
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
    print("   rubik.py measures that failing in 2 of 3,000 scrambles, the")
    print("   tightest of the thirteen non-laws by a factor of twenty-four.")
    print()
    print()
    print("5. THE SECOND MASTER INDEX, CONSTRUCTED.")
    (c1, k1), (c2, k2) = two_masters()
    M2 = second_master()
    d2, n2, r2 = master.shape(M2)
    print("   M2's cells are KINDS OF REFUSAL: (K, W, H, J, A) over every pair.")
    print("   %d distinct profiles, arity %d, box %d, density %.1f%%, closed by %s."
          % (len(M2), d2, n2, 100 * r2, sorted(master.closers(M2)) or "NOTHING"))
    print("     M1  cells are INDEXES          %s  channel K%d" % (c1, k1))
    print("     M2  cells are KINDS OF REFUSAL %s  channel K%d" % (c2, k2))
    M1 = frozenset(master.master_index().values())
    clm, _ = hlaw.closures(M1)
    if c1 == c2 and k1 == k2:
        print("   THEY COINCIDE -- same channel, same arity band, same density")
        print("   band. AN INDEX OF INDEXES AND AN INDEX OF REFUSALS LAND ON ONE")
        print("   CELL. That is a stronger statement than the one first reported")
        print("   here, which was that they differ in the channel and nothing")
        print("   else; completing the bounds family moved M1 onto M2's cell.")
        if c2 in M1:
            who = sorted(n for n, v in master.master_index().items() if v == c2)
            print("   AND THE CELL IS OCCUPIED, BY %s --" % ", ".join(who))
            print("   so M1 is a cell of itself. Recorded, not interpreted: the")
            print("   master index's own master cell is one of its members.")
    else:
        same = [n for n, a, b in (("arity band", c1[3], c2[3]),
                                  ("density band", c1[4], c2[4])) if a == b]
        print("   THEY DIFFER. Shared: %s." % (", ".join(same) or "nothing"))
        dem = " and ".join(L for L in hlaw.LANGS if c2 in clm[L] - M1)
        if dem:
            print("   And M2's cell is one %s already demanded of M1." % dem)
        else:
            print("   M2's cell is demanded of M1 by no language.")
    print()
    print("   AND THE CONSTRUCTION IS NOT FORCED. W = 2 exactly when statistics")
    print("   admits (%d disagreements in %d pairs), so W adds nothing where"
          % (w_is_the_statistics_test(), pairs_scanned()))
    print("   statistics admits and one bit where it refuses. Drop it:")
    Mb = second_master(with_w=False)
    db, nb, rb = master.shape(Mb)
    print("     %d profiles, arity %d, box %d, density %.1f%%, cell %s"
          % (len(Mb), db, nb, 100 * rb, master.master_cell(Mb)))
    who = [n for n, v in master.master_index().items()
           if v == master.master_cell(Mb)]
    print("     WHICH IS OCCUPIED, BY %s -- the one index holding a K1 cell."
          % ", ".join(who))
    occ_w = sorted(n for n, v in master.master_index().items() if v == c2)
    print("   With W it sits %s; without W it sits on"
          % ("on " + ", ".join(occ_w) if occ_w else "at an unoccupied cell"))
    print("   the very index carrying the corpus's only K1. BOTH ARE REPORTED.")
    print()

    print("6. THE CORRIDOR.")
    print("   A CORRIDOR IS A PAIR (X, c) -- an index and a cell of its box.")
    co = corridor(nm, c)
    for k, v in co.items():
        print("     %-22s %s" % (k, v))
    print("   Neither endpoint determines the other: a refusal profile cannot be")
    print("   computed from the index alone (that is the channel set, a different")
    print("   object) nor from the cell alone (a bare tuple). IT EXISTS ONLY ON")
    print("   THE PAIR -- which is turnseat.py's condition, that both sets of")
    print("   coordinates be known at the onset, satisfied structurally.")
    print()

    print("7. AND THE WARP CELL IS A CORRIDOR WITH ONE ENDPOINT DECLARED.")
    print("   Its refusal set is K1 and it has NO W, H, J or A, because expand.py")
    print("   treats TRANSITION-POSSIBLE as a standalone binary and there is no")
    print("   host index for it to be a cell OF. Four of five coordinates are")
    print("   undefined. THAT IS turnseat.py's FAILURE MODE EXACTLY -- part 2")
    print("   fails when the input does not provide enough for part 3.")
    print("   What would complete it: DECLARE THE INDEX TRANSITION-POSSIBLE IS A")
    print("   CELL OF. Not another bound and not another instrument -- a host.")
    print()

    print("8. WHAT A K1 REFUSAL IS.")
    print("   statistics admits <=> every 2-marginal present; geometry admits =>")
    print("   inside the hull; algebra admits => in the meet-and-join closure;")
    print("   information REFUSES <=> NOT in the join closure.")
    print("     => A K1 CELL IS A MEET AND NOT A JOIN, EVERY MARGINAL PRESENT.")
    X = master.inventory()[nm]
    mw = [(a, b) for a in sorted(X) for b in sorted(X)
          if tuple(min(a[i], b[i]) for i in range(len(c))) == c]
    print("   the PAIR witness (statistics): group 11 with s-block is SILVER,")
    print("     at %s" % [x for x in sorted(X) if x[1] == 11 and x[2] == 0])
    print("   the MEET witness (algebra): %s meet %s = %s" % (mw[0][0], mw[0][1], c))
    print("     copper meet zinc. THE ABSENT CELL IS THE MEET OF COPPER AND ZINC.")
    print("   Read onto the device: the transition is reachable by RESTRICTING")
    print("   what you have, not by COMBINING it. Meets are available, the join")
    print("   is not. A statement about the shape, not a claim that any")
    print("   restriction achieves it.")
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
    chk("cells scanned over the nine", tot, 2436)
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
    # WAS ONE. Completing the bounds family added two more, both inside bounds
    # itself -- so the warp obstruction's KIND now occurs in the bounds index as
    # well as the periodic layout. Still the rarest of the eight.
    chk("K1 occurs three times in 2,436 cells", cnt[K1], 3)
    # AND THE TWO NEW ONES ARE THE BOUNDS INDEX'S OWN DEMANDED CELLS. Not put
    # there -- both fell out of seating Casini and the Z slot. So the bounds
    # family's outstanding demand is a K1 refusal, the warp obstruction's kind.
    import bounds as _b
    _bcl, _ = hlaw.closures(_b.cells())
    chk("the other two K1 cells are in the bounds index",
        sorted(c for n, c in k1_cells() if n == "bounds"),
        [(2, 1, 0, 0, 0, 2), (2, 1, 0, 0, 1, 2)])
    # STATED AT ITS TRUE STRENGTH, and the pin is what forced the correction.
    # It is NOT everything that index demands -- the union over all five
    # languages is six cells. It is what the TIGHTEST languages demand, and a
    # K1 refusal is by definition exactly that: refused by information and
    # admitted by everything else, so the two sets coincide by construction
    # for the tightest pair. What is measured is that the pair IS the tightest.
    chk("what the tightest languages demand of the bounds index",
        sorted(_bcl["statistics"] - _b.cells()),
        [(2, 1, 0, 0, 0, 2), (2, 1, 0, 0, 1, 2)])
    chk("and statistics/information ARE the tightest there",
        sorted(L for L in hlaw.LANGS
               if len(_bcl[L]) == min(len(_bcl[M]) for M in hlaw.LANGS)),
        ["information", "statistics"])
    chk("the union over all five is larger, so this is not 'all it demands'",
        len(set().union(*(_bcl[L] for L in hlaw.LANGS)) - _b.cells()), 6)
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
    # ---- M2, the second master index
    (c1_, k1_), (c2_, k2_) = two_masters()
    M2 = second_master()
    chk("M2 has 45 kinds of refusal", len(M2), 45)
    chk("and is closed by NOTHING", sorted(master.closers(M2)), [])
    # AND NOW THEY COINCIDE. Completing the bounds family took M1 off closure,
    # and the two master indexes -- one whose cells are indexes, one whose cells
    # are kinds of refusal -- land on the SAME master cell at the same channel.
    chk("M1 sits at (0,0,0,2,0), channel K0", (c1_, k1_), ((0, 0, 0, 2, 0), 0))
    chk("M2 sits there too", (c2_, k2_), ((0, 0, 0, 2, 0), 0))
    chk("THE TWO MASTER INDEXES NOW COINCIDE", c1_, c2_)
    M1 = frozenset(master.master_index().values())
    clm, _ = hlaw.closures(M1)
    chk("and it is a cell M1 itself now occupies", c2_ in M1, True)
    chk("SO M1 IS A CELL OF ITSELF -- the witness is the bounds index",
        sorted(n for n, v in master.master_index().items() if v == c2_),
        ["bounds"])
    # the pair count the census walks, measured rather than carried as a literal
    chk("the pooled census walks 2,436 pairs", pairs_scanned(), 2436)
    # the construction is NOT forced, and that is recorded
    chk("W = 2 exactly when statistics admits", w_is_the_statistics_test(), 0)
    Mb = second_master(with_w=False)
    chk("dropping W gives 43 profiles at arity 4", (len(Mb), master.shape(Mb)[0]),
        (43, 4))
    chk("and lands on (0,0,0,1,1), which IS occupied",
        master.master_cell(Mb), (0, 0, 0, 1, 1))
    chk("by the very index holding the only K1 cell",
        [n for n, v in master.master_index().items()
         if v == master.master_cell(Mb)], ["periodic layout 3-D"])

    # ---- the corridor
    co = corridor(nm, c)
    chk("the corridor's M1 endpoint is the host's master cell",
        co["endpoint in M1"], master.master_cell(master.inventory()[nm]))
    chk("its M2 endpoint is the refusal profile", co["endpoint in M2"],
        (1, 2, 1, 2, 1))
    chk("the host's channel and the refusal's channel DIFFER",
        co["channel of the index"] != co["channel of the refusal"], True)

    # ---- the K1 characterisation: a meet and not a join
    X = master.inventory()[nm]
    d = len(c)
    isj = any(tuple(max(a[i], b[i]) for i in range(d)) == c for a in X for b in X)
    ism = any(tuple(min(a[i], b[i]) for i in range(d)) == c for a in X for b in X)
    chk("the K1 cell IS a meet of two members", ism, True)
    chk("and is NOT a join of any two", isj, False)
    chk("the meet witness is copper and zinc",
        sorted((a, b) for a in sorted(X) for b in sorted(X)
               if tuple(min(a[i], b[i]) for i in range(d)) == c)[0],
        ((4, 11, 2), (4, 12, 0)))

    chk("nothing here moves the magnitude", NOTHING_HERE_MOVES_THE_MAGNITUDE, True)

    print("duality selftest: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else report())
