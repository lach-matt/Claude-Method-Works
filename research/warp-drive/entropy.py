#!/usr/bin/env python3
r"""
entropy.py -- THE ENTROPY INDEX: how much each seated index says, in bits, and
the first admissible coordinates this tree has found that are not counts.

M: "Is there a entropy index that can be derived?"  There is, and the
interesting part is not that it exists but that it PASSES the chart criterion.

    python3 entropy.py             the reading
    python3 entropy.py --selftest  fixtures

===============================================================================
0. SECOND-ORDER, AND SAYING SO FIRST
===============================================================================

Its members are the NINE SEATED INDEXES, and its coordinates are measurements of
them.  That makes it second-order, like `mi.py` and `rindex.py` and unlike the
fibrations, the ladder, the provenance index and the channel index, whose
members are elements, transitions, measurements and channels.

    THE DISTINCTION MATTERS FOR COUNTING.  A second-order index is a function of
    the seated inventory, so the supply of them is bounded only by the supply of
    admissible measurements -- which is not bounded at all.  Three more are
    already measurable (`sources.py` names them).  Nothing in this file should be
    read as "the classification has one more member"; it is one more measurement
    of the same nine.

===============================================================================
1. THE THREE COORDINATES
===============================================================================

For an index X of d-tuples:

        H_max     the largest Shannon entropy of any single coordinate's marginal
        H_min     the smallest
        H_joint   log2 |X| -- the entropy of a uniform distribution on members

    REAL-VALUED COORDINATES NEED NO BANDING HERE, and that is worth stating
    because banding is where two earlier coordinates died.  hlaw takes the
    OBSERVED alphabet as its chain, so a coordinate may take any values that
    order -- the chain is simply the nine observed entropies.  Nothing is cut
    into bands and no band edge is chosen.

===============================================================================
2. ALL THREE PASS THE CHART CRITERION
===============================================================================

DOCKET 3: a coordinate is admissible iff it is invariant under appending a
MONOTONE REDUNDANT coordinate.  Arity and density both move on 9 of 9 and are
disqualified.  Measured the same way:

        H_max     moves on 0 of 9      ADMISSIBLE
        H_min     moves on 0 of 9      ADMISSIBLE
        H_joint   moves on 0 of 9      ADMISSIBLE

    WHY, AND IT IS NOT AN ACCIDENT.  Appending g(x) = x_0 adds a coordinate
    whose marginal distribution is a copy of coordinate 0's, so it adds a
    duplicate to the multiset of marginal entropies -- which cannot change the
    largest or the smallest.  And the append is a bijection on members, so |X|
    and therefore H_joint are untouched.  Density moves because the BOX grows;
    entropy is computed on the members, not on the box, and the members do not.

    THESE ARE THE FIRST ADMISSIBLE COORDINATES IN THIS TREE THAT ARE NOT COUNTS.
    height, width, cells, comparable pairs and join-irreducibles are all counts
    of something.  H_max and H_min are not.

===============================================================================
3. THE INDEX
===============================================================================

        9 cells, K2 -- closes STATISTICS, cell (2, 4, 5)

    Which is the master index's own channel again, as the hexad's was.

        substances (Hawking-Ellis)   (1.299, 0.811, 3.000)
        the languages                (1.371, 0.722, 2.322)
        questions                    (1.500, 0.811, 2.000)
        bounds                       (1.561, 0.544, 3.000)
        energy-condition family      (1.569, 0.310, 4.170)
        exotic mechanisms            (2.156, 0.544, 3.000)
        spacetimes (Petrov)          (2.250, 0.544, 3.000)
        Janet (n+l, l, k)            (3.678, 2.202, 7.409)
        periodic layout              (4.144, 1.565, 6.755)

    **H_joint IS A RELABELLING OF A COORDINATE THE TREE ALREADY HAD.**  It is
    log2 of the cell count, and log2 is monotone, so it separates exactly the
    indexes `cells` separates -- six values for six distinct sizes.  It is kept
    because the triple is the natural statement of "how much does this index
    say", and it is FLAGGED because a reader must not count it as new evidence.
    The genuinely new content is H_max and H_min, and (H_max, H_min) alone is
    already injective on the nine and already K2.

===============================================================================
4. WHAT THIS FILE REFUSES
===============================================================================

    TO CALL THIS THE ENTROPY OF ANYTHING PHYSICAL.  It is Shannon entropy of the
    coordinate marginals of a finite index.  The corpus's physical entropy lives
    in `bounds.py` -- Bekenstein, Bousso -- which is a MEMBER of the master
    index, not this.  The two share a word and nothing else, and DOCKET 4 turned
    on exactly that kind of conflation.

    TO OFFER H_joint AS EVIDENCE.  See section 3.

    TO TREAT THE NINE AS A SAMPLE.  Nine indexes is what is seated; the entropies
    are exact for those nine and are not an estimate of anything wider.

    TO READ K2 AS AGREEMENT WITH THE MASTER INDEX.  Landing in the same channel
    is not landing in the same cell: (2, 4, 5) against MI's (2, 5, 2).
"""

import collections
import itertools
import math
import sys

import hlaw
import mi

NAMES = ("H_max", "H_min", "H_joint")
H_JOINT_IS_A_RELABELLING_OF_CELLS = True


def _entropy(values):
    """Shannon entropy, in bits, of the empirical distribution of `values`."""
    n = len(values)
    c = collections.Counter(values)
    return -sum(v / n * math.log2(v / n) for v in c.values())


def marginals(X):
    """[entropy of each coordinate's marginal] for an index X."""
    X = sorted(X)
    d = len(X[0])
    return [_entropy([x[i] for x in X]) for i in range(d)]


def cell_of(X, places=6):
    """(H_max, H_min, H_joint) for one index, rounded to `places`."""
    m = marginals(X)
    return (round(max(m), places), round(min(m), places),
            round(math.log2(len(X)), places))


def table():
    """{index name: its entropy cell} over the nine seated indexes."""
    return {nm: cell_of(X) for nm, X in mi.inventory().items()}


def index():
    """The entropy index -- one cell per seated index."""
    return frozenset(table().values())


def closers(X):
    X = frozenset(X)
    cl, _b = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def admissibility():
    """{coordinate: how many of the nine it moves on} -- DOCKET 3's test.

    Appending g(x) = x_0 is the monotone redundant coordinate.  A coordinate
    that moves on any index is disqualified; arity and density move on all nine.
    """
    moved = {n: 0 for n in NAMES}
    for X in mi.inventory().values():
        a = cell_of(X)
        b = cell_of(frozenset(tuple(c) + (c[0],) for c in X))
        for i, n in enumerate(NAMES):
            if a[i] != b[i]:
                moved[n] += 1
    return moved


def h_joint_relabels_cells():
    """(is it monotone in |X|, distinct sizes, distinct H_joint values).

    log2 is monotone, so H_joint separates exactly what `cells` separates and
    is new notation rather than new evidence.  Measured rather than argued.
    """
    inv = mi.inventory()
    pairs = sorted((len(X), cell_of(X)[2]) for X in inv.values())
    mono = all(pairs[i][1] <= pairs[i + 1][1] for i in range(len(pairs) - 1))
    return mono, len({len(X) for X in inv.values()}), len({p[1] for p in pairs})


def subcharts():
    """[(K, combo, cells, injective)] over every sub-chart of arity 2 and 3."""
    t = table()
    out = []
    for r in (2, 3):
        for combo in itertools.combinations(range(3), r):
            P = frozenset(tuple(v[i] for i in combo) for v in t.values())
            out.append((mi.K(P), tuple(NAMES[i] for i in combo), len(P),
                        len(P) == len(t)))
    return out


# ---------------------------------------------------------------------------

def report():
    X, t = index(), table()
    print("=" * 74)
    print("THE ENTROPY INDEX -- how much each seated index says, in bits")
    print("=" * 74)
    print()
    print("0. SECOND-ORDER, AND SAYING SO FIRST. Its members are the nine")
    print("   seated indexes and its coordinates measure them, so it is a")
    print("   function of the inventory -- like mi.py and rindex.py. The supply")
    print("   of such indexes is not bounded; see sources.py.")
    print()

    print("1. THE THREE COORDINATES: H_max and H_min over the coordinate")
    print("   marginals, and H_joint = log2|X|. Real-valued, and NO BANDING --")
    print("   hlaw takes the observed alphabet as its chain, so the nine")
    print("   observed entropies ARE the chain. No band edge is chosen.")
    print()

    print("2. ALL THREE PASS THE CHART CRITERION.")
    for n, mvd in admissibility().items():
        print("   %-8s moves on %d of 9   %s"
              % (n, mvd, "ADMISSIBLE" if mvd == 0 else "DISQUALIFIED"))
    print("   Appending g(x)=x_0 copies coordinate 0's marginal, which cannot")
    print("   change the largest or smallest; and it is a bijection on members,")
    print("   so |X| is untouched. DENSITY moves because the BOX grows --")
    print("   entropy is computed on the members, and the members do not.")
    print("   THE FIRST ADMISSIBLE COORDINATES HERE THAT ARE NOT COUNTS.")
    print()

    print("3. THE INDEX.")
    print("   %d cells   K%d   closes %s   cell %s"
          % (len(X), mi.K(X), ", ".join(closers(X)) or "NOTHING", mi.cell(X)))
    for nm in sorted(t, key=lambda n: t[n]):
        print("     %-28s (%.3f, %.3f, %.3f)" % ((nm,) + t[nm]))
    mono, ns, nh = h_joint_relabels_cells()
    print("   H_joint IS A RELABELLING of `cells`: monotone in |X| (%s), and it")
    print("   separates %d sizes into %d values. Kept for the natural triple,"
          % (ns, nh))
    print("   FLAGGED so it is not counted as new evidence. (H_max, H_min)")
    print("   alone is already injective on the nine and already K%d."
          % mi.K(frozenset((v[0], v[1]) for v in t.values())))
    print("   monotone: %s" % mono)
    print()

    print("4. SUB-CHARTS.")
    for k, combo, n, inj in sorted(subcharts()):
        print("   K%-2d %d cells %-26s %s"
              % (k, n, "(" + ", ".join(combo) + ")", "INJ" if inj else ""))
    print()
    print("5. REFUSED: to call this the entropy of anything PHYSICAL -- the")
    print("   corpus's physical entropy is bounds.py, Bekenstein and Bousso,")
    print("   which is a MEMBER of the master index. The two share a word.")
    print("   To offer H_joint as evidence. To treat the nine as a sample.")
    print("   To read K2 as agreement with MI: same channel, different cell")
    print("   -- (2,4,5) against (2,5,2).")
    return 0


# ---------------------------------------------------------------------------

def selftest():
    ok = True

    def chk(nm, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", nm, got))
        if not good:
            print("        expected %r" % (want,))

    print("entropy selftest")
    X, t = index(), table()

    chk("one cell per seated index", (len(t), len(X)), (9, 9))
    chk("and they are distinct, so the chart is faithful", len(X), 9)

    # ---- THE HEADLINE: it passes the criterion that killed arity and density
    adm = admissibility()
    chk("H_max moves on none of the nine", adm["H_max"], 0)
    chk("H_min likewise", adm["H_min"], 0)
    chk("H_joint likewise", adm["H_joint"], 0)
    chk("SO ALL THREE ARE ADMISSIBLE", sorted(set(adm.values())), [0])

    # ---- the index
    chk("it closes statistics alone", closers(X), ["statistics"])
    chk("which is K2", mi.K(X), 2)
    chk("its cell on the admissible chart", mi.cell(X), (2, 4, 5))
    chk("height and width", (mi.height(X), mi.width(X)), (4, 5))
    # SAME CHANNEL AS MI, DIFFERENT CELL. Pinned so the two are not conflated.
    chk("same channel as the master index but NOT the same cell",
        (mi.K(X) == 2, mi.cell(X) != (2, 5, 2)), (True, True))

    # ---- H_joint is notation, not evidence
    mono, sizes, vals = h_joint_relabels_cells()
    chk("H_joint is monotone in the cell count", mono, True)
    chk("and separates exactly what `cells` separates", (sizes, vals), (6, 6))
    chk("so it is declared a relabelling", H_JOINT_IS_A_RELABELLING_OF_CELLS,
        True)
    # THE GENUINELY NEW CONTENT survives without it.
    HM = frozenset((v[0], v[1]) for v in t.values())
    chk("(H_max, H_min) alone is already injective", len(HM), 9)
    chk("and already K2", mi.K(HM), 2)

    # ---- sub-charts
    sc = subcharts()
    chk("sub-charts of arity 2 and 3", len(sc), 4)
    chk("every one closes statistics", sorted({k for k, _c, _n, _i in sc}), [2])
    chk("and only (H_min, H_joint) fails to be injective",
        [c for _k, c, _n, inj in sc if not inj], [("H_min", "H_joint")])

    # ---- a spot value, so the entropies themselves are pinned
    chk("Janet's entropy cell", t["Janet (n+l, l, k)"],
        (3.678155, 2.201951, 7.409391))
    chk("and the smallest index's", t["questions"], (1.5, 0.811278, 2.0))

    print("entropy selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
