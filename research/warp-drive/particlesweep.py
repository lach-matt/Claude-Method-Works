#!/usr/bin/env python3
r"""
particlesweep.py -- DOCKET 29.  EVERY CHART THE THREE PARTICLE MEMBER SETS
ADMIT, SWEPT EXHAUSTIVELY, AND THE ONE THAT SURVIVES.

    python3 particlesweep.py             the reading
    python3 particlesweep.py --selftest  fixtures

DOCKET 25 CLOSED WITH A CONDITION AND DOCKET 27 MET IT.  Its ruling reads:
"Settled for the tree as it stands.  A NEW MEMBER SET WOULD REOPEN IT."  Three
new member sets were seated -- `fundamental`, `mesons`, `baryons` -- so the
census is reopened over exactly those three, and nothing else here has changed.

THE CLAIM DOCKET 27 COULD MAKE was "every particle in the table is a member of
some index".  THE CLAIM THIS DOCKET GOES AFTER is the other one: that every
index those members admit has been found.

===============================================================================
1. THE CENSUS
===============================================================================

Every sub-chart of every particle parent -- each subset of its columns of size
two or more, the parent itself included.  Not a search for a channel: an
enumeration, which is the same procedure the overlap ruling's own six
candidates came from, and the reason this is not DOCKET 23's refused move.

    fundamental   4 columns    11 charts
    mesons        4 columns    11 charts
    baryons       7 columns   120 charts
                              --- 142

THREE OF THE 142 REACH A CHANNEL THE RULING'S CENSUS CALLS UNOCCUPIED.  Two
are refused and one is seated, and the two refusals are as much the result as
the seating is.

===============================================================================
2. THE FIRST REFUSAL: K1 IS NOT EMPTY, AND THE FUNCTION THAT SAID SO IS RIGHT
===============================================================================

`baryons (P, 2I, Q3)` lands at K1 with 30 cells.  `overlaprule.seated_channels()`
reports K1 unoccupied -- and it is correct to, for the question it was written
to answer.  It EXCLUDES the ruling's own rows, because "novel channel" means
novel against the index the ruling was handed, and counting its own seatings
would let the rule eat itself.

    THAT EXCLUSION DOES NOT TRANSFER TO A NEW PARENT.  K1 is held by
    `overlaprule.gravity_bound`, which is seated, and a chart of baryons is
    not competing with a ruling in progress -- it faces the index as it now
    stands.  So the honest occupancy for this docket is the full one, K1 is
    taken, and this chart earns no position the master index does not hold.

    RECORDED AS A SCOPE FINDING, not a bug: `seated_channels()` has one job
    and does it.  `honest_occupancy()` here is the other reading, and the two
    differ on exactly the two channels the ruling itself filled.

===============================================================================
3. THE SECOND REFUSAL: A K4 THAT IS JOIN-CLOSURE WEARING A FREE BIT
===============================================================================

`fundamental (Q3, GEN)` lands at K4 with 24 cells, holds K4 at every
generation, and passes all four of the ruling's grounds.  IT IS STILL REFUSED,
on `overlaprule.py` section 3c, and the ground is measured here rather than
quoted:

    ARITY-2 FREENESS, over every arity-2 sub-chart in the tree
        statistics   105 of 105     FREE -- kdet returns True when k >= d
        geometry      74 of 105     earned
        information   52 of 105     earned
        order         47 of 105     earned
        algebra       47 of 105     earned

    K4 = {information, statistics} is the ONE channel above K1 whose extra
    content over K1 is exactly the bit an arity-2 chart is handed.  Nothing in
    `hlaw.LAWFUL` forces statistics from information.  So what this chart
    demonstrates is join-closure, which is K1, AND K1 IS OCCUPIED.

    IT IS THE THIRD CHART IN THIS TREE TO REACH K4 AND THE THIRD TO BE
    REFUSED, after `ions (sl, tl)` and `madrule (S_a, l_d)`.  All three are
    arity 2.  No chart of arity 3 or more has ever reached K4 here, and
    DOCKET 25's "K4 is reached by nothing" survives this docket intact.

===============================================================================
4. THE SEATING: THE TREE'S ONLY K5
===============================================================================

`baryons (2I, Q3)` -- isospin against charge, flavour dropped.  16 cells from
the 184 the parent separates, at cell (5, 7, 4).

    WHY THE ARITY-2 ARGUMENT DOES NOT TOUCH IT.  Section 3c is explicit: at K5
    the statistics bit is FORCED BY LAW -- `hlaw.LAWFUL` carries
    (statistics, geometry) as Clause G.3 -- so the free pass changes nothing
    and the seating stands on GEOMETRY, which no coordinate count buys.  And
    geometry is not free: 31 of the 105 arity-2 charts fail it.

    THE FOUR GROUNDS, all from `overlaprule.grounds()`:
        novel channel        K5 is held by nothing, in either occupancy reading
        not a relabelling    16 cells against the parent's 184
        reach stable         K5 at every mass cut from 1200 MeV to the top
        coordinate forced    no recoordinatisation reaches it otherwise

    AND IT IS NOT DOCKET 22's MISTAKE REPEATED.  That retraction unseated
    `nucshell (l, sigma)` because an identical partition written as (l, 2j)
    landed at K7 -- the K5 was a fact about the spelling of a coordinate.
    Here both coordinates are read straight from the PDG table, 2I and Q3 are
    what the Review prints, and there is no alternative spelling to fall to.

    WHAT IT SAYS ABOUT BARYONS, and it is a real statement:

        2I = 0   Q3 in {-3, 0, +3}
        2I = 1   Q3 in {-3, 0, +3}
        2I = 2   Q3 in {-6, -3, 0, +3, +6}
        2I = 3   Q3 in {-6, -3, 0, +3, +6}

    Geometry is hull-completeness on coordinate pairs.  The four box points
    the chart does not hold are the corners (0, +-6) and (1, +-6), and they
    fall OUTSIDE the convex hull of the sixteen it does.  A MULTIPLET'S CHARGE
    SPAN WIDENS WITH ITS ISOSPIN, steeply enough to cut the corners off, and
    the chart is that widening and nothing else.

===============================================================================
5. WHAT IS NOW CLAIMED, AND WHAT IS STILL NOT
===============================================================================

CLAIMED.  Over the three particle member sets, every chart their declared
columns admit has been enumerated and adjudicated.  One is seated, two are
refused with reasons, and 139 reach an occupied channel.

NOT CLAIMED, and the distinction is the whole reason this file is separate
from `docket27.py`:

    - THE COLUMNS ARE THE DECLARED ONES.  A chart on a coordinate none of the
      three modules declares -- C-parity, G-parity, lepton number, mass -- is
      not in this census, and each was refused in its own module for a stated
      reason.  Reaching for one now, after seeing which channels are short,
      would be DOCKET 23's fitted move exactly.
    - `registry.COMPLETE` STAYS FALSE.  This docket completes a census over
      three member sets.  It says nothing about member sets nobody has thought
      of, and that is what COMPLETE would mean.
"""

import itertools
import sys

import baryons
import fundamental
import hlaw
import mesons
import mi
import overlaprule as OR
import registry

PARENTS = ("fundamental", "mesons", "baryons")

# What the census found, stated here so a fixture can hold the file to it.
SEATED = ("baryons", ("2I", "Q3"), 5)
REFUSED = (
    ("baryons", ("P", "2I", "Q3"), 1,
     "K1 is held by overlaprule.gravity_bound -- section 2"),
    ("fundamental", ("Q3", "GEN"), 4,
     "arity 2, so statistics is free and what it shows is K1 -- section 3"),
)


def _mod(name):
    return {"fundamental": fundamental, "mesons": mesons,
            "baryons": baryons}[name]


def subcharts(parent):
    """[(cols, cells, K)] -- every subset of the parent's columns, size >= 2."""
    mod = _mod(parent)
    names = mod.NAMES
    X = mod.index()
    out = []
    for r in range(2, len(names) + 1):
        for pick in itertools.combinations(range(len(names)), r):
            P = frozenset(tuple(c[i] for i in pick) for c in X)
            out.append((tuple(names[i] for i in pick), len(P), mi.K(P)))
    return out


def census():
    """{parent: [(cols, cells, K)]} -- all 142."""
    return {p: subcharts(p) for p in PARENTS}


# The row THIS docket seated.  Excluded from the occupancy it adjudicates
# against, for the same reason `overlaprule.seated_channels()` excludes the
# ruling's own rows -- see `honest_occupancy()`.
OWN_ROWS = ("overlaprule.baryon_isomultiplet",)


def current_occupancy():
    """The channels the index holds right now, this docket's seating included."""
    return frozenset(c[0] for _nm, c in registry.cells().items()
                     if c != "UNMEASURED")


def honest_occupancy():
    """The occupancy this docket ADJUDICATES AGAINST -- section 2.

    Two exclusions, and they are different exclusions:

    IT INCLUDES the overlap ruling's own rows, which
    `overlaprule.seated_channels()` leaves out.  That omission is right for
    the question that function answers -- novelty against the index the ruling
    was handed -- and wrong here, because a chart of baryons is not competing
    with a ruling in progress.  K1 is held by `gravity_bound` and K6 by
    `madelung_slot`, and both are seated.

    IT EXCLUDES THE ROW THIS DOCKET ITSELF SEATED, for exactly the reason that
    function excludes its own: count it and the test eats itself the moment it
    succeeds.  K5 is occupied NOW because `baryons (2I, Q3)` was seated into
    it, so measuring novelty against a set that already contains it would
    retroactively refuse the seating that put it there.  A census adjudicates
    against the index it was handed.
    """
    return frozenset(c[0] for nm, c in registry.cells().items()
                     if c != "UNMEASURED" and nm not in OWN_ROWS)


def occupancy_gap():
    """[K] the ruling's census calls empty and the honest one does not."""
    return sorted(honest_occupancy() - OR.seated_channels())


def hits(occupancy=None):
    """[(parent, cols, cells, K)] reaching a channel the occupancy lacks."""
    occ = OR.seated_channels() if occupancy is None else occupancy
    out = []
    for p, rows in census().items():
        for cols, n, k in rows:
            if k not in occ:
                out.append((p, cols, n, k))
    return sorted(out, key=lambda t: (t[3], t[0]))


def arity2_freeness():
    """Section 3's table.  overlaprule's measurement, imported not copied."""
    return OR.arity2_freeness()


def isomultiplet_rows():
    """[(2I, [Q3])] -- section 4's reading of the seated chart."""
    X = OR.baryon_isomultiplet()
    out = {}
    for i, q in X:
        out.setdefault(i, []).append(q)
    return [(i, sorted(v)) for i, v in sorted(out.items())]


def corners_outside_hull():
    """([box points not held], all of them outside the hull?) -- section 4.

    Geometry closing IS the statement that they are outside, so this recomputes
    it the other way round: which box points the chart lacks, and that the
    geometry closure does not put any of them back.
    """
    X = OR.baryon_isomultiplet()
    Is = sorted({i for i, _q in X})
    Qs = sorted({q for _i, q in X})
    missing = sorted(set(itertools.product(Is, Qs)) - set(X))
    cl, _b = hlaw.closures(X)
    return (missing, not (set(cl["geometry"]) - set(X)))


def report():
    print("=" * 74)
    print("DOCKET 29 -- every chart the particle member sets admit")
    print("=" * 74)
    print()
    C = census()
    print("1. THE CENSUS.")
    tot = 0
    for p in PARENTS:
        n = len(C[p])
        tot += n
        ks = {}
        for _c, _n, k in C[p]:
            ks[k] = ks.get(k, 0) + 1
        print("   %-13s %3d charts   channels %s"
              % (p, n, {("K%d" % k): v for k, v in sorted(ks.items())}))
    print("   %-13s %3d" % ("total", tot))
    print()
    print("   occupancy, the ruling's census   %s"
          % sorted(OR.seated_channels()))
    print("   occupancy, as it was handed      %s" % sorted(honest_occupancy()))
    print("   occupancy, after this docket     %s"
          % sorted(current_occupancy()))
    print("   they differ on                   %s  (the ruling's own rows)"
          % occupancy_gap())
    print()
    print("2-4. THE THREE THAT REACH AN UNOCCUPIED CHANNEL.")
    for p, cols, n, k in hits():
        mark = "SEATED " if (p, cols, k) == SEATED else "refused"
        why = next((w for pp, cc, kk, w in REFUSED
                    if (pp, cc, kk) == (p, cols, k)), "section 4")
        print("   [%s] %-12s %-16s K%d  %3d cells" % (mark, p, str(cols), k, n))
        print("             %s" % why)
    print()
    print("   ARITY-2 FREENESS, measured over every arity-2 chart in the tree:")
    for L, (c, n) in sorted(arity2_freeness().items(),
                            key=lambda t: -t[1][0]):
        print("     %-12s %3d of %3d   %s"
              % (L, c, n, "FREE" if c == n else "earned"))
    print()
    print("4. THE SEATING: baryons (2I, Q3), the tree's only K5.")
    for i, qs in isomultiplet_rows():
        print("     2I = %d   Q3 in %s" % (i, qs))
    missing, outside = corners_outside_hull()
    print("   box points not held: %s" % missing)
    print("   all outside the hull: %s -- which IS geometry closing" % outside)
    print("   grounds: %s" % OR.grounds(*SEATED[:2]))
    print()
    print("5. NOT CLAIMED.  The columns are the DECLARED ones; a chart on a")
    print("   coordinate the modules refused is not in this census, and")
    print("   reaching for one now would be DOCKET 23's fitted move.")
    print("   registry.COMPLETE is %s." % registry.COMPLETE)
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    C = census()
    chk("142 sub-charts over the three parents",
        sum(len(v) for v in C.values()), 142)
    chk("and the three parents contribute 11, 11 and 120",
        [len(C[p]) for p in PARENTS], [11, 11, 120])
    chk("every chart has arity 2 or more",
        sorted({len(c) for v in C.values() for c, _n, _k in v})[0], 2)

    # section 2: the two occupancy readings, and what they differ on
    chk("the ruling's census calls K1 and K6 empty; the index holds both",
        occupancy_gap(), [1, 6])
    chk("and the honest occupancy leaves exactly K4 and K5 empty",
        [k for k in range(8) if k not in honest_occupancy()], [4, 5])
    chk("while the CURRENT occupancy leaves only K4 -- because this docket "
        "filled K5", [k for k in range(8) if k not in current_occupancy()],
        [4])
    chk("and that is the whole reason honest_occupancy() excludes its own row",
        sorted(current_occupancy() - honest_occupancy()), [5])

    H = hits()
    chk("three charts reach a channel the ruling's census calls empty",
        len(H), 3)
    chk("and against the HONEST occupancy only two do",
        len(hits(honest_occupancy())), 2)
    chk("the one that falls away is the K1", sorted(
        {(p, c) for p, c, _n, k in H} - {(p, c) for p, c, _n, k
                                         in hits(honest_occupancy())}),
        [("baryons", ("P", "2I", "Q3"))])

    # section 3: arity-2 freeness, the ground both refusals rest on
    F = arity2_freeness()
    chk("statistics closes EVERY arity-2 chart in the tree -- it is free",
        F["statistics"], (105, 105))
    chk("geometry does NOT -- 31 of 105 fail it, so it is earned",
        F["geometry"], (74, 105))
    chk("and so does every other language fail some arity-2 chart",
        sorted(L for L, (c, n) in F.items() if c == n), ["statistics"])
    chk("the K4 candidate is arity 2, which is why it is refused",
        len(REFUSED[1][1]), 2)
    chk("and DOCKET 25's finding survives: no chart of arity 3+ reaches K4",
        sorted({len(c) for v in C.values() for c, _n, k in v if k == 4}), [2])

    # section 4: the seating
    chk("exactly one chart is seated by this docket",
        [(p, c, k) for p, c, _n, k in H if (p, c, k) == SEATED], [SEATED])
    chk("it is in the registry, under the ruling",
        sorted(a for m, a, *_r in registry.REGISTERED
               if m == "overlaprule"),
        ["baryon_isomultiplet", "gravity_bound", "madelung_slot"])
    chk("all four grounds pass", sorted(OR.grounds(*SEATED[:2]).items()),
        [("coordinate forced", True), ("not a relabelling", True),
         ("novel channel", True), ("reach stable", True)])
    chk("16 cells from the 184 the parent separates",
        (len(OR.baryon_isomultiplet()), len(baryons.index())), (16, 184))
    chk("K5, and it is the only K5 in the whole index",
        sorted(nm for nm, c in registry.cells().items()
               if c != "UNMEASURED" and c[0] == 5),
        ["overlaprule.baryon_isomultiplet"])
    chk("the reach sweep holds K5 at every mass cut",
        sorted({k for _l, _n, k in OR.reach_sweep(*SEATED[:2])}), [5])

    # section 4's physical reading, checked rather than asserted
    chk("the charge span widens with isospin",
        [(i, len(q)) for i, q in isomultiplet_rows()],
        [(0, 3), (1, 3), (2, 5), (3, 5)])
    missing, outside = corners_outside_hull()
    chk("the four box points it lacks are the corners at 2I = 0 and 1",
        missing, [(0, -6), (0, 6), (1, -6), (1, 6)])
    chk("and every one is outside the hull, which IS geometry closing",
        outside, True)

    # section 5
    chk("COMPLETE stays False", registry.COMPLETE, False)
    chk("and the file says the census is over the DECLARED columns only",
        "The columns are the declared ones" in " ".join(__doc__.split())
        or "THE COLUMNS ARE THE DECLARED ONES" in " ".join(__doc__.split()),
        True)

    print("particlesweep selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
