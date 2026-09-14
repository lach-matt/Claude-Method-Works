#!/usr/bin/env python3
r"""
shells.py -- THE PERIOD DETECTOR, AND THE CALIBRATION IT GIVES THE WHOLE TREE.

M: "Chase the period. Let's see if the MI can indeed give us a list of
unwitnessed, realizable elements."  And then: "the detector now happens to be
our calibration tool. We should calibrate to that and reread the index."

    python3 shells.py             the reading
    python3 shells.py --selftest  fixtures

===============================================================================
0. WHAT HAPPENED, AND WHY IT IS NOT CIRCULAR
===============================================================================

A first attempt swept the (period, group) chart and found the master cell moving
at Z = 118 and Z = 168.  THAT WAS CIRCULAR: the construction hardcoded where
period 8 ends, so the index reflecting the boundary back proved nothing.

JANET'S CHART IS NOT CIRCULAR.  Its cell is (n+l, l, k) straight out of the
Madelung fill order -- no drawn layout, no set-aside, no period boundary put in
by hand.  The n+l shells END WHERE MADELUNG SAYS and the chart is never told.
So sweep the reach and watch the master cell.

===============================================================================
1. THE DETECTOR, EXACT OVER NINE BOUNDARIES
===============================================================================

    K = 7 at reach R  AND  K = 3 at reach R + 1   IFF   R is a shell boundary

        detector fires at   4, 12, 20, 38, 56, 88, 120, 170, 220
        true shell ends     4, 12, 20, 38, 56, 88, 120, 170, 220
        misses 0            false positives 0        over 239 reaches

K = 7 alone is not the detector (41 reaches), nor is K = 3 alone (73).  It is
the TRANSITION, and every other K7 is followed by K0 rather than K3.

===============================================================================
2. THE THREE-ROW PATTERN, AND WHICH LANGUAGES SPEAK AT A LIMIT
===============================================================================

At every one of the eight boundaries in range, without exception:

                     order  algebra  geometry  information  statistics    K
    one short          1       1        1           1            1       K0
    at the boundary    0       0        0           0            0       K7
    one past         5/9/13/17  same    0        same            0       K3

    ONE SHORT: all five demand, unanimously, E = 1 each -- THE SAME ONE CELL.
    AT IT:     all five close.  Nothing left to ask for.
    ONE PAST:  geometry and statistics still close; order, algebra and
               information break, and by more as the shells deepen.

THE PAIR THAT SURVIVES IS EXACTLY K3 = down(geometry), the principal down-set of
geometry in the language poset.  M read the split as {order, algebra, geometry}
against {statistics, information}; the measurement says otherwise, and the true
split is the same asymmetry Birkhoff gives for K6 running the other way:

    {geometry, statistics} HOLD -- {order, algebra, information} BREAK

because geometry sits above statistics alone, while the order/algebra block sits
above BOTH minimal languages and takes information down with it.

    AND THE STOPPING IS NOT SILENCE.  The languages speak LOUDEST one short of
    the limit -- all five at once, naming the missing element -- then fall silent
    at the boundary because there is nothing left to ask for.  The shell does not
    tell the object to stop.  The object tells the languages it is finished.

===============================================================================
3. NINE OF NINE.  THE DEMAND NAMES THE NEXT ELEMENT, CORRECTLY.
===============================================================================

One short of a boundary the five demand exactly one cell.  Is it the RIGHT cell?

    R = 11  -> (3,0,1)    element 12    YES        R = 87  -> (7,0,1)   YES
    R = 19  -> (4,0,1)    element 20    YES        R = 119 -> (8,0,1)   YES
    R = 37  -> (5,0,1)    element 38    YES        R = 169 -> (9,0,1)   YES
    R = 55  -> (6,0,1)    element 56    YES        R = 219 -> (10,0,1)  YES

NINE OF NINE, INCLUDING Z = 170 AND Z = 220, both far beyond anything
observed.  THIS IS THE FIRST DEMAND IN THIS TREE EVER CHECKED AGAINST AN
INDEPENDENT GROUND TRUTH AND FOUND RIGHT.

===============================================================================
4. THE PERIOD ENDS, AND THE UNWITNESSED ELEMENTS
===============================================================================

A Janet shell is the standard period plus the next s-shell, so the offset is
exactly 2 and the detector gives the standard period ends directly:

    2, 10, 18, 36, 54, 86, 118, 168, 218, 290
    |________ the seven known _______| |_ derived _|

    PERIOD 8 ENDS AT Z = 168.       PERIOD 9 ENDS AT Z = 218.

Oganesson at 118 is the heaviest observed, so:

    period 8   Z = 119..168   50 elements
               8s(119-120) 5g(121-138) 6f(139-152) 7d(153-162) 8p(163-168)
    period 9   Z = 169..218   50 elements
               9s(169-170) 6g(171-188) 7f(189-202) 8d(203-212) 9p(213-218)

    A CORPUS DEFECT FOUND ON THE WAY, AND NOT REPAIRED HERE.
    `tools/populate.MADELUNG` is INCOMPLETE -- it omits (9,0), (9,1), (10,0),
    (6,5) and (9,2).  Its n+l = 9 shell therefore ends at 168 instead of 170,
    and ANY FIGURE THIS TREE COMPUTES PAST n+l = 8 FROM IT IS WRONG.  This file
    builds the true order itself and leaves tools/ untouched; the defect is
    RECORDED, not fixed, because tools/ is corpus tooling with a pinned selftest.

===============================================================================
5. THE CALIBRATION, AND THE RE-READ IT FORCES
===============================================================================

This tree has now checked exactly two demands against an independent truth:

    CORRECT   Janet one short of a boundary   5 of 5 languages, 1 cell   8/8
    WRONG     the 2-D chart at Z <= 118       3 of 5 languages, 36 cells

and the 36 were the short-period gaps -- positions where no element exists or
can.  So the signature of a demand worth trusting is:

        ALL FIVE LANGUAGES DEMAND, AND THEIR INTERSECTION IS EXACTLY ONE CELL.

Re-read against that, the whole tree has THREE candidates and no more:

    bounds                      (2, 1, 0, 0, 1, 2)
    substances (Hawking-Ellis)  (0, 1, 2, 1)
    the languages               (1, 0, 2, 1, 0)

Everything else fails it: six indexes have a language that closes, so their
intersection is empty by definition; periodic layout 3-D has all five demanding
but EIGHT unanimous cells, not one.

    AND THE MASTER INDEX ITSELF FAILS IT.  Four of five languages demand, 18
    cells, ZERO unanimous.  The cell (1,1,0,2,1) that three separate
    constructions chased and that DOCKET 5 deleted WAS NEVER A CALIBRATED
    DEMAND, and now there is a standard by which to say so.

Nothing is seated on the strength of the three.  They are the demands that pass
the only calibration this tree has, which is a reason to test them and not a
reason to believe them.
"""

import itertools
import sys

import decomposable as D
import hlaw
import master

# The TRUE Madelung order, built here because tools/populate.MADELUNG is
# truncated (section 4). Sorted by (n+l, n), which is the Madelung rule itself.
TRUE_MADELUNG = tuple(sorted(((n, l) for n in range(1, 12) for l in range(0, n)),
                             key=lambda t: (t[0] + t[1], t[0])))

DETECTED_BOUNDARIES = (4, 12, 20, 38, 56, 88, 120, 170, 220)
PERIOD_ENDS = (2, 10, 18, 36, 54, 86, 118, 168, 218, 290)
MADELUNG_OMITS = ((9, 0), (9, 1), (10, 0), (6, 5), (9, 2))
CALIBRATED = {"bounds", "substances (Hawking-Ellis)", "the languages"}


def cap(l):
    return 2 * (2 * l + 1)


def config(Z, order=TRUE_MADELUNG):
    rem, out = Z, []
    for n, l in order:
        if rem <= 0:
            break
        t = min(cap(l), rem)
        out.append((n, l, t))
        rem -= t
    return out


def cell_of(Z, order=TRUE_MADELUNG):
    """Janet's cell for element Z: (n+l, l, k) of the differentiating electron."""
    now = {(n, l): o for n, l, o in config(Z, order)}
    prev = ({(n, l): o for n, l, o in config(Z - 1, order)} if Z > 1 else {})
    g = sorted((n, l) for (n, l), o in now.items() if o > prev.get((n, l), 0))
    if not g:
        return None
    n, l = g[-1]
    return (n + l, l, prev.get((n, l), 0))


def janet(R, order=TRUE_MADELUNG):
    return frozenset(c for Z in range(1, R + 1)
                     for c in [cell_of(Z, order)] if c)


def shell_ends(order=TRUE_MADELUNG):
    out, tot, cur = [], 0, None
    for n, l in order:
        if cur is not None and n + l != cur:
            out.append(tot)
        cur = n + l
        tot += cap(l)
    out.append(tot)
    return out


def channel(X):
    return master.channel_sets().index(frozenset(master.closers(X)))


def detect(lo=2, hi=240):
    """[R] where K = 7 at R and K = 3 at R+1 -- the shell-boundary signature."""
    K = {}
    for R in range(lo, hi + 1):
        X = janet(R)
        if len(X) >= 3:
            K[R] = channel(X)
    return sorted(R for R in K if K.get(R) == 7 and K.get(R + 1) == 3), K


def profile(R):
    """{language: E} at reach R."""
    X = janet(R)
    cl, _ = hlaw.closures(X)
    return {L: len(cl[L]) - len(X) for L in hlaw.LANGS}


def predicts_next(bounds=None):
    """[(R, demanded cell, true cell of R+1, match)] one short of each boundary."""
    bounds = DETECTED_BOUNDARIES if bounds is None else bounds
    out = []
    for b in bounds:
        R = b - 1
        X = janet(R)
        if len(X) < 3:
            continue
        cl, _ = hlaw.closures(X)
        dem = set()
        for L in hlaw.LANGS:
            dem |= (cl[L] - X)
        truth = cell_of(R + 1)
        out.append((R, sorted(dem), truth,
                    len(dem) == 1 and next(iter(dem)) == truth))
    return out


def demand_signature(X):
    """(languages demanding, cells in the union, cells ALL FIVE demand).

    THE CALIBRATION. The one demand checked against truth and found right scored
    (5, 1, 1); the one found wrong scored (3, 36, 0).
    """
    X = frozenset(X)
    cl, _ = hlaw.closures(X)
    dem = {L: frozenset(cl[L]) - X for L in hlaw.LANGS}
    live = [L for L in hlaw.LANGS if dem[L]]
    union = set().union(*dem.values()) if live else set()
    inter = (set.intersection(*[set(dem[L]) for L in hlaw.LANGS])
             if len(live) == 5 else set())
    return len(live), len(union), sorted(inter)


def reread():
    """{name: (languages, union, unanimous cells)} over the whole tree."""
    import charts
    out = {nm: demand_signature(X) for nm, X in master.inventory().items()}
    out["THE MASTER INDEX itself"] = demand_signature(
        frozenset(charts.cell(X) for X in master.inventory().values()))
    return out


def report():
    print("=" * 74)
    print("THE PERIOD DETECTOR, AND THE CALIBRATION IT GIVES THE TREE")
    print("=" * 74)
    print()
    fired, K = detect()
    ends = [e for e in shell_ends() if e in K and e + 1 in K]
    print("1. THE DETECTOR.  K = 7 at reach R and K = 3 at R + 1.")
    print("   fires at          %s" % fired)
    print("   true shell ends   %s" % ends)
    print("   EXACT: %s   misses %d   false positives %d"
          % (fired == ends, len([e for e in ends if e not in fired]),
             len([r for r in fired if r not in ends])))
    print("   Janet's chart is never told where a shell ends. It is (n+l, l, k)")
    print("   straight out of Madelung, and the boundary falls out of the")
    print("   CLOSURE BEHAVIOUR of the resulting set.")
    print()
    print("2. THE THREE-ROW PATTERN, at every boundary:")
    print("   %-8s %-5s %6s %8s %9s %12s %11s  K" % ("bound", "R", "order",
          "algebra", "geom", "information", "statistics"))
    for b in fired[:4] + fired[-2:]:
        for R in (b - 1, b, b + 1):
            X = janet(R)
            if len(X) < 3:
                continue
            E = profile(R)
            print("   %-8s %-5d %6d %8d %9d %12d %11d  K%d"
                  % (b if R == b else "", R, E["order"], E["algebra"],
                     E["geometry"], E["information"], E["statistics"], channel(X)))
        print()
    print("   {geometry, statistics} HOLD past the limit -- that is K3, the")
    print("   principal down-set of geometry. {order, algebra, information} BREAK.")
    print()
    print("3. NINE OF NINE.  One short of a boundary the five demand exactly")
    print("   one cell. It is the cell of the next element, every time.")
    P = predicts_next()
    for R, dem, truth, ok in P:
        print("      R=%-4d demanded %-14s next element %-14s %s"
              % (R, str(dem), str(truth), "YES" if ok else "NO"))
    print("   %d of %d." % (sum(1 for *_x, ok in P if ok), len(P)))
    print()
    print("4. THE PERIOD ENDS.  A Janet shell is the standard period plus the")
    print("   next s-shell, so the offset is 2 and the detector gives them directly.")
    print("   %s" % (PERIOD_ENDS,))
    print("   PERIOD 8 ENDS AT Z = 168.   PERIOD 9 ENDS AT Z = 218.")
    print("   unwitnessed and realizable: Z = 119..168 and Z = 169..218,")
    print("   fifty elements each.")
    print("   AND A CORPUS DEFECT: tools/populate.MADELUNG omits %s," % (MADELUNG_OMITS,))
    print("   so its n+l = 9 shell ends at 168 instead of 170. RECORDED, not fixed.")
    print()
    print("5. THE CALIBRATION, AND THE RE-READ.")
    print("   CORRECT demand, checked against truth: 5 languages, 1 unanimous cell")
    print("   WRONG   demand, checked against truth: 3 languages, 36 cells")
    print()
    print("   %-30s %6s %6s  %s" % ("index", "langs", "union", "UNANIMOUS"))
    for nm, (l, u, i) in sorted(reread().items()):
        tag = "  <-- MATCHES THE CALIBRATION" if len(i) == 1 and l == 5 else ""
        print("   %-30s %6d %6d  %-8s%s" % (nm, l, u, len(i), tag))
    print()
    print("   THREE CANDIDATES IN THE WHOLE TREE, and the master index is not")
    print("   one of them: four of five languages, 18 cells, ZERO unanimous.")
    print("   The cell three constructions chased was never a calibrated demand.")
    print("   NOTHING IS SEATED ON THE STRENGTH OF THE THREE.")
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

    print("shells selftest")
    chk("tools/populate.MADELUNG is INCOMPLETE -- omitted subshells",
        [t for t in MADELUNG_OMITS
         if tuple(t) not in [tuple(x) for x in master._populate().MADELUNG]],
        list(MADELUNG_OMITS))
    chk("and its n+l=9 shell therefore ends at 168, not 170",
        (shell_ends(master._populate().MADELUNG)[8], shell_ends()[8]), (168, 170))

    fired, K = detect()
    ends = [e for e in shell_ends() if e in K and e + 1 in K]
    chk("THE DETECTOR IS EXACT", fired, ends)
    chk("and it is these nine boundaries", tuple(fired), DETECTED_BOUNDARIES)
    chk("K7 alone is not the detector -- it occurs far more often",
        sum(1 for v in K.values() if v == 7) > len(fired), True)
    chk("nor is K3 alone", sum(1 for v in K.values() if v == 3) > len(fired), True)
    # A non-boundary K7 is followed by K0 or by K7 -- NEVER by K3. That is what
    # makes the transition the detector rather than either value alone.
    chk("no non-boundary K7 is followed by K3",
        3 in {K.get(R + 1) for R in K if K.get(R) == 7 and R not in ends}, False)
    chk("they are followed by K0 or K7 only",
        sorted({K.get(R + 1) for R in K if K.get(R) == 7 and R not in ends}
               - {None}), [0, 7])

    # THE FIRST BOUNDARY IS THE ONE EXCEPTION AND IT IS A SIZE EFFECT. At R = 3
    # the index has three cells, geometry and statistics already close, and the
    # unanimity has nothing to be unanimous over. From b = 12 on it is exact.
    E3 = profile(3)
    chk("at the FIRST boundary the unanimity fails -- 3 cells is too few",
        sorted(set(E3.values())), [0, 1])
    for b in DETECTED_BOUNDARIES[1:7]:
        E0, E1, E2 = profile(b - 1), profile(b), profile(b + 1)
        chk("at %d-1 all five demand exactly one cell" % b,
            sorted(set(E0.values())), [1])
        chk("at %d all five close" % b, sorted(set(E1.values())), [0])
        chk("at %d+1 geometry and statistics still close" % b,
            (E2["geometry"], E2["statistics"]), (0, 0))
        chk("and order, algebra and information do not",
            all(E2[L] > 0 for L in ("order", "algebra", "information")), True)

    P = predicts_next()
    # NINE, not eight: the earlier count ran over boundaries >= 10 and dropped
    # b = 4. It matches there too, so the record is 9 of 9.
    chk("NINE OF NINE -- the demand names the next element",
        (sum(1 for *_x, o in P if o), len(P)), (9, 9))
    chk("including at R = 169 and R = 219, beyond all observation",
        [R for R, _d, _t, o in P if o and R > 160], [169, 219])

    chk("the period ends, derived", PERIOD_ENDS[:10],
        tuple(e - 2 for e in shell_ends()[:11] if e - 2 > 0)[:10])
    chk("period 8 ends at 168 and period 9 at 218",
        (PERIOD_ENDS[7], PERIOD_ENDS[8]), (168, 218))

    # ---- the calibration
    X = janet(DETECTED_BOUNDARIES[-1] - 1)
    chk("the CORRECT demand scores (5 languages, 1 union, 1 unanimous)",
        (demand_signature(X)[0], demand_signature(X)[1],
         len(demand_signature(X)[2])), (5, 1, 1))
    R = reread()
    match = sorted(nm for nm, (l, _u, i) in R.items() if l == 5 and len(i) == 1)
    chk("and THREE indexes in the tree match it", sorted(match), sorted(CALIBRATED))
    chk("the master index does NOT -- 4 languages, 18 cells, 0 unanimous",
        (R["THE MASTER INDEX itself"][0], R["THE MASTER INDEX itself"][1],
         len(R["THE MASTER INDEX itself"][2])), (4, 18, 0))
    chk("periodic layout 3-D has all five demanding but EIGHT unanimous, not one",
        (R["periodic layout 3-D"][0], len(R["periodic layout 3-D"][2])), (5, 8))
    chk("NOTHING IS SEATED ON THE STRENGTH OF THE THREE",
        set(master.inventory()) & {"shells"}, set())
    print("shells selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
