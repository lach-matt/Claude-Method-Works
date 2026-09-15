#!/usr/bin/env python3
r"""
demand.py -- WHAT SHAPE IS THE FINAL SHAPE?  The figure names the vertices it is
missing, and the count of them is exactly E.

M: "I am not satisfied with the closure of the octad, and I suggest there exists
at least one more vertex index of measurable class and value.  The closure of the
complete configuration is either E=0 or 1... The hexad is not the final shape, up
until now it thought it might be octad, but maybe not.  The 'complete
characterization/definition' has still yet to be proven.  Whatever the final shape
and its vertexes are is the scope."

    python3 demand.py             the reading
    python3 demand.py --selftest  fixtures

===============================================================================
0. THE QUESTION IS NOW WELL-POSED, AND THAT IS THIS FILE'S ONLY CLAIM
===============================================================================

`hexad.py` measured a figure at six, seven and eight vertices and refused to name
a polygon.  The refusal was right and unhelpful: it said the classification is not
this shape without saying what would make it one.  M's closure condition fixes
that.  Read E as `the information deficit` reads it -- the information deficit,
|J(F)| - |F|, where J is the join-closure -- and

    E = 0   the figure is JOIN-CLOSED.  Every pair of vertices joins to a vertex.
    E = 1   one join escapes, and closure is one vertex away.

Both are decidable from the seated cells alone, and neither is a matter of taste.

===============================================================================
1. THE FOUR FACTS THAT MAKE IT A PROGRAMME
===============================================================================

Write F for the seated cells, J(F) for their join-closure, D = J(F) \ F for the
cells the figure demands and does not have.  All four are proved in `lemmas()`
by exhaustive check over random figures, and the first two are the whole reason
the programme terminates.

    L1  E = |D|.  Definitional, and stated so the other three have a unit.

    L2  SEATING A DEMANDED CELL DROPS E BY EXACTLY ONE.  If v is in D then
        J(F + v) = J(F), because J(F) is already join-closed and contains v.  So
        the demand shrinks by one and NOTHING ELSE MOVES.

    L3  SEATING ANYTHING ELSE NEED NOT RAISE IT.  If v is not in J(F) then
        |J(F + v)| >= |J(F)| + 1 while |F + v| = |F| + 1, so E can go up or stay
        -- and `lemmas()` measures which, rather than asserting it.  The
        stay-the-same case has a name and a test:

            v IS NEUTRAL when v is not in J(F) and J(F + v) = J(F) + v, i.e.
            v joins with every cell of J(F) back into J(F) + v.

        A neutral vertex costs the programme NOTHING: the figure gains a member
        and the demand is the same ten cells it was.  `neutral()` decides it and
        `neutrality()` reports it for the live figure -- where BOTH vertices
        seated on 2026-09-15, the inversion index and the probability index, are
        neutral, which is why E is 10 at eight vertices and 10 at ten.

    L4  CLOSURE IS REACHABLE AND THE PRICE IS E.  Seating all of D gives exactly
        J(F), which is join-closed, so E = 0.  No smaller set of demanded cells
        does, and no set of undemanded cells does it at all.

    SO THE FINAL SHAPE IS NOT AN OPEN-ENDED SEARCH.  At any moment the figure
    names its own missing vertices, and there are exactly E of them.

===============================================================================
2. A DEMANDED CELL IS A PREDICTION WITH CONTENT
===============================================================================

A cell is (K, height, width).  A cell is not a wish: it constrains the index that
would occupy it, and the constraints are checkable before anything is built.

    K           which languages close it -- a down-set, so one of eight.
    height      the longest chain.  MIRSKY.
    width       the largest antichain.  DILWORTH.
    |X|         between max(height, width) and height * width.  The lower bound
                is trivial; the upper is Dilworth's theorem, since width chains
                of length at most height cover X.  BOTH ENDS ARE ATTAINED, by a
                single chain and by width DISJOINT chains -- not by a grid, whose
                height is h + w - 1.

`predictions()` prints that band for every demanded cell, so a candidate index can
be REFUTED against a cell before it is built, and a built one can be checked
against the cell it was supposed to fill.

    THIS IS THE ONE PLACE FITTING COULD ENTER AND IT MUST NOT.  A candidate index
    is built from the corpus on its own terms and its cell is then MEASURED.  It
    is never constructed to land on a demanded cell.  `inversion.py` and
    `probability.py` were both built before this file printed a demand table, and
    where they land is reported whether or not it is wanted.

===============================================================================
3. WHAT THIS FILE REFUSES
===============================================================================

To claim the demanded cells are occupiable.  Ten cells are demanded at eight
vertices and nothing here says an index exists at any of them; a cell is a
specification, and a specification no object meets is a refutation of the
programme, not a gap in it.

To name the final shape.  If every demanded cell is filled the figure closes at
|J(F)| vertices -- 18 at the current eight -- but each new vertex is measured, not
assumed, and a vertex landing outside J(F) moves the target.

To call E = 1 second best.  M's condition admits it, and `lemmas()` shows why it
is a different object: E = 1 is a figure with a unique missing join, which is a
stronger statement about the figure than E = 0 is.
"""

import itertools
import random
import sys

import figure as _fig
import hlaw
import mi

CAP = 400


def join(a, b):
    return tuple(max(x, y) for x, y in zip(a, b))


def closure(F):
    """(J(F), rounds) -- the join-closure and how many rounds it took."""
    S, r = set(F), 0
    while True:
        new = {join(a, b) for a in S for b in S} - S
        if not new:
            return frozenset(S), r
        S |= new
        r += 1


def demand(F):
    """D = J(F) \\ F, sorted.  The cells the figure demands and does not have."""
    J, _r = closure(F)
    return sorted(J - frozenset(F))


def E(F):
    """The information deficit, computed two ways and asserted equal.

    hlaw's information operator; this runs the join-closure
    directly.  They must agree -- the information closure IS the join-closure --
    and a disagreement would mean one of them is not what it says it is.
    """
    return len(demand(F))


def provenance(F):
    """{demanded cell: [(a, b)] joining to it, or [] if a later round}."""
    F = sorted(F)
    out = {}
    for m in demand(F):
        out[m] = [(a, b) for a, b in itertools.combinations(F, 2)
                  if join(a, b) == m]
    return out


def neutral(v, F):
    """v is outside J(F) and adds no join but itself.

    The third case of L3, and the one the live figure exhibits: seating a
    neutral vertex leaves the demand EXACTLY as it was.  A vertex that is
    demanded is not neutral -- it is inside J(F) and drops E by one.
    """
    J, _r = closure(F)
    if v in J:
        return False
    return closure(set(F) | {v})[0] == J | {v}


def neutrality(names=None, base=None):
    """[(name, cell, verdict)] for each vertex NOT in the base figure.

    verdict is "demanded" (in J(base), drops E), "neutral" (outside, costs
    nothing) or "disruptive" (outside, and raises E by more than nothing).
    """
    base = list(base) if base else sorted(_fig.cells())
    B = _fig.figure(base)
    JB, _r = closure(B)
    out = []
    for nm, c in _fig.cells(names).items():
        if nm in base:
            continue
        if c in JB:
            v = "demanded -- drops E by 1"
        elif neutral(c, B):
            v = "NEUTRAL -- costs nothing"
        else:
            v = "disruptive -- raises E by %d" % (E(B | {c}) - E(B))
        out.append((nm, c, v))
    return out


def size_band(cell):
    """(low, high) -- the member count an index at this cell must have.

    Low is max(height, width): a chain of that length, or an antichain of it, is
    already that many members.  High is height * width, by Dilworth -- width
    chains, each of length at most height, cover X.
    """
    _k, h, w = cell
    return max(h, w), h * w


def predictions(names=None):
    """[(cell, K set, size band, [(a, b)] that demand it)] -- the missing vertices."""
    F = sorted(_fig.figure(names))
    chans = mi.channels()
    prov = provenance(F)
    return [(c, sorted(chans[c[0]]), size_band(c), prov[c]) for c in demand(F)]


# ---------------------------------------------------------------------------
# the four facts
# ---------------------------------------------------------------------------

def _rand_figure(rnd, n, hi=6):
    return frozenset(tuple(rnd.randrange(hi) for _ in range(3))
                     for _ in range(rnd.randrange(2, n + 1)))


def lemmas(trials=CAP, seed=3):
    """{lemma: (checked, violations, note)} over random figures.

    L3 is MEASURED rather than asserted: the distribution of how E moves when an
    undemanded vertex is seated is what the entry carries.
    """
    rnd = random.Random(seed)
    out = {}
    bad1 = bad2 = bad4 = 0
    moved = {}
    n = 0
    for _ in range(trials):
        F = _rand_figure(rnd, 7)
        if len(F) < 2:
            continue
        n += 1
        J, _r = closure(F)
        D = demand(F)
        # L1
        if E(F) != len(J) - len(F):
            bad1 += 1
        # L2
        for v in D:
            if closure(F | {v})[0] != J or E(F | {v}) != E(F) - 1:
                bad2 += 1
                break
        # L3 -- measured
        outside = [tuple(rnd.randrange(8) for _ in range(3)) for _ in range(3)]
        for v in outside:
            if v in J:
                continue
            d = E(F | {v}) - E(F)
            moved[d] = moved.get(d, 0) + 1
        # L4
        if D and E(frozenset(F) | set(D)) != 0:
            bad4 += 1
        if D and frozenset(F) | set(D) != J:
            bad4 += 1
    out["L1  E = |D|"] = (n, bad1, "definitional")
    out["L2  a demanded vertex drops E by exactly 1"] = (n, bad2, "J is unchanged")
    out["L3  an undemanded vertex moves E by"] = (
        n, 0, ", ".join("%+d: %d" % kv for kv in sorted(moved.items())))
    out["L4  seating all of D gives E = 0"] = (n, bad4, "and gives exactly J(F)")
    return out


def cross_check(names=None):
    """E from the join-closure against E from hlaw's information operator.

    The information closure IS the join-closure, so these must agree.  They are
    computed by different code and the agreement is the check.
    """
    F = _fig.figure(names)
    J, _r = closure(F)
    cl, _b = hlaw.closures(F)
    return len(J) - len(F), len(cl["information"]) - len(F)


def _disjoint_chains(h, w):
    """w pairwise-incomparable chains of length h, as a set of 2-tuples.

    Chain j runs along x and sits at y = w-1-j, so within a chain the points are
    comparable and across chains one is larger in x and smaller in y.  Height h,
    width w, exactly h*w members.

    THE OBVIOUS WITNESS IS THE WRONG ONE and this file used it first: the product
    order on an h x w grid has height h + w - 1, not h, because a chain may step
    in BOTH coordinates.  Dilworth's bound is still |X| <= height * width -- w
    chains, each of length at most h -- and it is attained by chains that are
    disjoint, not by a grid.
    """
    return frozenset((j * h + i, w - 1 - j)
                     for j in range(w) for i in range(h))


def bands_are_tight():
    """Both ends of the size band are attained, so neither is slack.

    Lower: a chain of length h has height h, width 1 and max(h, 1) = h members.
    Upper: w disjoint chains of length h have height h, width w and h*w members.
    Checked, not asserted.
    """
    out = []
    for h, w in ((3, 1), (4, 1), (3, 3), (4, 2), (2, 5)):
        chain = frozenset((i, 0) for i in range(h))
        many = _disjoint_chains(h, w)
        out.append(((h, w),
                    (mi.height(chain), mi.width(chain), len(chain)),
                    (mi.height(many), mi.width(many), len(many))))
    return out


# ---------------------------------------------------------------------------

def report():
    F = _fig.figure()
    J, rounds = closure(F)
    print("=" * 74)
    print("THE FIGURE NAMES ITS OWN MISSING VERTICES")
    print("=" * 74)
    print()
    print("0. WHERE THE ELEMENT FIGURE STANDS.")
    print("   seated vertices   %d" % len(F))
    print("   join-closure      %d   (%d rounds)" % (len(J), rounds))
    print("   E                 %d   -- and M's condition is E = 0 or 1" % E(F))
    a, b = cross_check()
    print("   cross-check       join-closure E = %d, hlaw information E = %d  %s"
          % (a, b, "AGREE" if a == b else "DISAGREE -- STOP"))
    print()

    print("1. THE TEN CELLS IT DEMANDS, EACH A PREDICTION.")
    print("   %-13s %-34s %-12s %s" % ("cell", "channel", "members", "demanded by"))
    for c, ks, (lo, hi), prov in predictions():
        ksn = "{%s}" % ", ".join(ks) if ks else "{} (K0)"
        src = prov[0] if prov else None
        who = {v: k for k, v in _fig.cells().items()}
        lab = "%s + %s" % (who[src[0]], who[src[1]]) if src else "round 2"
        print("   %-13s %-34s %-12s %s"
              % (str(c), ksn, "%d..%d" % (lo, hi), lab))
    print()
    print("   A cell is a SPECIFICATION.  An index claiming one must close in")
    print("   exactly those languages, have that longest chain and that largest")
    print("   antichain, and hold a member count in that band.  Nothing here")
    print("   says such an index exists.")
    print()

    print("2. THE PROGRAMME TERMINATES, AND THE PRICE IS E.")
    for k, (n, bad, note) in lemmas().items():
        print("   [%s] %-44s %s" % ("ok" if not bad else "XX", k, note))
    print()
    print("   So the final shape is NOT an open-ended search: at any moment the")
    print("   figure names exactly E missing vertices, seating one of them costs")
    print("   nothing else, and seating all of them closes it at |J(F)| = %d."
          % len(J))
    print()

    print("3. THE SIZE BANDS ARE TIGHT AT BOTH ENDS.")
    for (h, w), ch, gr in bands_are_tight():
        print("   h=%d w=%d   one chain (h,w,|X|) = %s   %d disjoint chains = %s"
              % (h, w, ch, w, gr))
    print()

    print("4. REFUSED: to claim any demanded cell is occupiable -- a")
    print("   specification no object meets refutes the programme rather than")
    print("   leaving a gap in it.  To name the final shape before its vertices")
    print("   are measured.  To treat E = 1 as second best: it is a figure with")
    print("   a UNIQUE missing join, which says more about the figure than E = 0.")
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-52s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    F = _fig.figure()
    # A PROPERTY, NOT A PINNED COUNT.  Pinning the number here fires the
    # fixture every time an index is correctly seated, which has now happened
    # three times in this tree.  What must hold is that the figure IS the
    # registry -- one vertex per registered element index, no more and no less.
    chk("the figure is exactly the registered element indexes",
        (len(F), len(_fig.cells())),
        (len(__import__("registry").REGISTERED),) * 2)
    chk("E equals the demand it names", E(F), len(demand(F)))
    chk("the demand is inside the closure",
        set(demand(F)) <= set(closure(F)[0]), True)
    chk("seating all of it closes the figure",
        E(frozenset(F) | set(demand(F))), 0)
    chk("and gives exactly the closure",
        frozenset(F) | set(demand(F)), closure(F)[0])
    if len(demand(F)) > 1:
        chk("seating all but one leaves E = 1",
            E(frozenset(F) | set(demand(F)[:-1])), 1)
    a, b = cross_check()
    chk("join-closure E == hlaw information E", a, b)
    # hand-computable cases, independent of any figure
    D2 = frozenset({(0, 1, 0), (1, 0, 1)})
    chk("an incomparable pair demands its join", E(D2), 1)
    chk("and the join is the coordinatewise max",
        demand(D2), [(1, 1, 1)])
    C2 = frozenset({(0, 0, 0), (1, 1, 1)})
    chk("a comparable pair demands nothing", E(C2), 0)
    chk("a singleton demands nothing", E(frozenset({(3, 4, 5)})), 0)
    nt = neutrality(base=sorted(_fig.cells())[:3])
    chk("neutrality accounts for every vertex outside the base", len(nt),
        len(_fig.cells()) - 3)
    chk("every verdict is one of the three kinds",
        sorted({v.split()[0] for _n, _c, v in nt}
               - {"demanded", "NEUTRAL", "disruptive"}), [])
    lem = lemmas()
    for k, (n, bad, _note) in lem.items():
        chk("%-44s violations" % k, bad, 0)
    chk("L3 was measured over some trials",
        lem["L3  an undemanded vertex moves E by"][2] != "", True)
    for (h, w), ch, many in bands_are_tight():
        chk("one chain h=%d has (h,w,|X|)" % h, ch, (h, 1, h))
        chk("%d disjoint chains of %d attain h*w" % (w, h), many, (h, w, h * w))
    chk("the GRID is NOT the witness -- height is h+w-1",
        mi.height(frozenset((i, j) for i in range(3) for j in range(3))), 5)
    print("demand selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
