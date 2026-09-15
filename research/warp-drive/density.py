#!/usr/bin/env python3
r"""
density.py -- IS THE DEMAND PALINDROMIC?  The E trajectory, the mechanism that
would turn it over, and the density that decides.

M: "The demand for information is likely palendromatic. Once we reach a density
of information the demand should lessen."

    python3 density.py             the reading
    python3 density.py --selftest  fixtures

===============================================================================
0. THE PREDICTION IS FALSIFIABLE, WHICH IS WHY IT GETS AN INSTRUMENT
===============================================================================

Seating indexes has driven E from 5 to 110.  M predicts that is the first half of
a curve: past some density of information the demand lessens and E comes back
down.  That is not a hope -- it names a shape, and a shape can be wrong.

    THIS FILE DOES NOT ARGUE THE PREDICTION EITHER WAY.  It states the mechanism
    that would produce the shape, measures the quantity that mechanism turns on,
    and records the trajectory so the turn can be seen if it comes.

===============================================================================
1. THE MECHANISM, AND IT IS ALREADY PROVED
===============================================================================

`demand.py` L2: seating a cell that is ALREADY IN J(F) drops E by exactly one.
L3: seating one outside raises it.  So which way a new index moves E is decided
by one question -- does its cell land inside the closure?

    AND J(F) GROWS FASTER THAN F.  Every disruptive vertex adds itself AND the
    joins it makes with everything already there.  At ten vertices J(F) was 20
    cells; at twenty-three it is 133.  So the TARGET a new index has to hit is
    getting bigger, while the box it is aimed into grows only as fast as the
    coordinate ranges do.

        density = |J(F)| / |box|

    is the probability that a cell placed anywhere in the box lands inside the
    closure -- which is exactly the chance the next index is DEMANDED rather
    than disruptive.  **If density rises toward 1, the demand must eventually
    lessen, and M's shape follows.  If it falls, it cannot.**

    THAT IS THE WHOLE TEST AND IT IS ONE NUMBER PER STEP.

===============================================================================
2. WHY THE ANSWER IS NOT OBVIOUS EITHER WAY
===============================================================================

Both terms grow.  A disruptive vertex adds joins, which grows |J(F)|.  But a
vertex with a coordinate outside the current range WIDENS THE BOX, and the box
grows multiplicatively where the closure grows additively.

    THE DRIVE MANIFEST IS THE CASE TO WATCH.  Its height is 216 against a
    figure whose tallest was 52, so seating it multiplies the box by roughly
    four while adding a bounded number of joins.  A single tall index can undo
    many steps of density.  `box_growth()` reports the two terms separately at
    every step so the competition is visible rather than summarised.

===============================================================================
3. WHAT THIS FILE REFUSES
===============================================================================

To extrapolate.  The trajectory is what was measured; no curve is fitted to it
and no turning point is predicted from the rows so far.  `trajectory()` prints
and stops.

To call a rise a refutation.  M's claim is about the completed set, and the set
is not complete -- `store.py` found seven sources nobody had listed while
building six.  A rising E over an incomplete set refutes nothing.

To call a fall a confirmation.  One step down is one step; the shape is
palindromic or it is not, and that needs the far side.  `dipped()` and
`turned()` are kept apart for exactly this reason: E HAS dipped once, at the
demanded seating, and it has NOT turned.  An earlier draft of this file
conflated the two and asserted no dip at all, which was wrong about the very
trajectory it prints.
"""

import json
import os
import sys

import demand

SEATING = os.path.join(
    "/tmp/claude-0/-home-user-Claude-Method-Works/"
    "6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad", "seating.tsv")

# The trajectory as measured, oldest first.  (vertices, E, what was seated).
# The first five are hexad.growth(); the rest are the incremental seating run.
MEASURED = (
    (6, 5, "the original six"),
    (7, 5, "entropy index"),
    (8, 10, "channel index"),
    (9, 10, "inversion index"),
    (10, 10, "probability index"),
    (11, 9, "filled (2,5,4)            DEMANDED"),
    (12, 9, "obstruction index         neutral"),
    (13, 9, "currency index            neutral"),
    (13, 9, "exotic-matter index       DUPLICATE CELL"),
    (14, 19, "pending list              disruptive"),
    (15, 22, "retraction audit          disruptive"),
    (16, 23, "coverage census           disruptive"),
    (17, 32, "dockets                   disruptive"),
    (18, 45, "handoff gap               disruptive"),
    (19, 52, "extracted ledger          disruptive"),
    (20, 67, "prose-only list           disruptive"),
    (21, 81, "build series              disruptive"),
    (22, 97, "register gaps             disruptive"),
    (23, 110, "recovered ledger          disruptive"),
)


def trajectory():
    """[(vertices, E, what)] as measured.  Nothing fitted, nothing projected."""
    return list(MEASURED)


def seated_rows():
    """The incremental seating log, if the run that writes it has got there."""
    if not os.path.exists(SEATING):
        return []
    out = []
    for line in open(SEATING):
        p = line.rstrip("\n").split("\t")
        if len(p) >= 6:
            out.append((p[0], tuple(json.loads(p[1])), p[2], int(p[3]),
                        int(p[4]), int(p[5])))
    return out


def box(F):
    return [sorted({c[i] for c in F}) for i in range(3)]


def box_size(F):
    b = box(F)
    return len(b[0]) * len(b[1]) * len(b[2])


def density(F):
    """|J(F)| / |box| -- the chance a cell in the box is already demanded."""
    J, _r = demand.closure(F)
    return len(J) / box_size(F)


def box_growth():
    """[(step, |F|, |J(F)|, |box|, density)] replayed over the seating log.

    Both terms are reported because they compete: a disruptive vertex grows
    J(F) additively and can grow the box MULTIPLICATIVELY, and which wins is
    the whole question.
    """
    import hexad
    F = frozenset(hexad.figure(list(hexad.SIX) + list(hexad.ADDED)))
    out = [("start", len(F), len(demand.closure(F)[0]), box_size(F), density(F))]
    for name, cell, _v, _b, _a, _n in seated_rows():
        F = F | {cell}
        out.append((name, len(F), len(demand.closure(F)[0]), box_size(F),
                    density(F)))
    return out


def dipped(traj=None):
    """(has E ever fallen after rising?, the first step where it did).

    TRUE, AND THE FILE SAID OTHERWISE BEFORE THE FIXTURE RAN.  E rose 5 -> 10
    over steps 0-2, held at 10, and fell to 9 at step 5 when `filled` seated a
    cell the figure already demanded.  That IS a fall after a rise.  The
    docstring here first claimed the fall came BEFORE the rise, which is simply
    wrong about the trajectory this file prints.
    """
    t = traj or trajectory()
    peak = 0
    for i, (_v, e, _w) in enumerate(t):
        if e > peak:
            peak = e
        elif e < peak:
            return True, i
    return False, None


def turned(traj=None):
    """(is there a PALINDROMIC turn?, the peak step).

    A dip is not a turn.  The palindrome M predicts needs the peak to be the
    GLOBAL maximum with a sustained descent after it -- not a single step down
    inside a plateau, which is what step 5 is.  So this asks the stricter
    question: is the maximum in the interior, with E lower at the end than at
    the peak?
    """
    t = traj or trajectory()
    es = [e for _v, e, _w in t]
    peak = max(es)
    at = es.index(peak)
    return (at < len(es) - 1 and es[-1] < peak), at


def falls(traj=None):
    """[(index, from, to, what)] every step where E went down."""
    t = traj or trajectory()
    return [(i, t[i - 1][1], e, w)
            for i, (_v, e, w) in enumerate(t) if i and e < t[i - 1][1]]


# ---------------------------------------------------------------------------

def report():
    t = trajectory()
    print("=" * 74)
    print("IS THE DEMAND PALINDROMIC?")
    print("=" * 74)
    print()
    print("1. THE TRAJECTORY AS MEASURED.")
    print("   %-10s %-6s %s" % ("vertices", "E", "seated"))
    for v, e, w in t:
        bar = "#" * min(e, 60)
        print("   %-10d %-6d %-38s %s" % (v, e, w, bar))
    print()
    print("2. HAS IT DIPPED, AND HAS IT TURNED?  THEY ARE NOT THE SAME.")
    dip, dat = dipped()
    print("   a fall after a rise (a DIP): %s"
          % ("yes, at step %d" % dat if dip else "no"))
    for i, a, b, w in falls():
        print("   step %2d  E %d -> %d   %s" % (i, a, b, w))
    turn, at = turned()
    print("   a PALINDROMIC turn -- peak in the interior, lower after: %s"
          % ("YES, peak at step %d" % at if turn else "NO"))
    print("   The peak is the LAST step, so nothing has turned. The one fall")
    print("   is a single demanded seating inside a plateau, and a dip inside")
    print("   a plateau is not the far side of a palindrome.")
    print()
    print("3. THE MECHANISM, AND THE NUMBER IT TURNS ON.")
    print("   L2: a cell already in J(F) drops E by one. L3: one outside raises")
    print("   it. So density = |J(F)| / |box| IS the chance the next index is")
    print("   demanded rather than disruptive. If it rises toward 1 the demand")
    print("   must lessen and M's shape follows; if it falls it cannot.")
    print()
    g = box_growth()
    if len(g) > 1:
        print("   %-20s %-6s %-8s %-10s %s"
              % ("after seating", "|F|", "|J(F)|", "|box|", "density"))
        for nm, f, j, b, d in g:
            print("   %-20s %-6d %-8d %-10d %.4f" % (nm[:20], f, j, b, d))
    else:
        print("   (the incremental seating log is not yet written; run the")
        print("    seating pass to populate box_growth())")
    print()
    print("4. REFUSED: to extrapolate -- no curve is fitted and no turning")
    print("   point is predicted. To call a rise a refutation: M's claim is")
    print("   about the COMPLETED set, and store.py found seven sources nobody")
    print("   had listed while building six, so the set is not complete. To")
    print("   call a fall a confirmation: one step down is one step, and a")
    print("   palindrome needs the far side.")
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-54s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    t = trajectory()
    chk("the trajectory has nineteen steps", len(t), 19)
    chk("it starts at six vertices, E 5", t[0][:2], (6, 5))
    chk("and stands at twenty-three, E 110", t[-1][:2], (23, 110))
    chk("vertices never decrease",
        all(t[i][0] >= t[i - 1][0] for i in range(1, len(t))), True)
    chk("E is never negative", [e for _v, e, _w in t if e < 0], [])
    f = falls()
    chk("exactly one step lowered E", len(f), 1)
    chk("it went from 10 to 9", f[0][1:3], (10, 9))
    chk("and it was the DEMANDED seating", "DEMANDED" in f[0][3], True)
    # A DIP IS NOT A TURN, and the file claimed no dip before the fixture ran.
    dip, dat = dipped()
    chk("E HAS dipped after rising -- at the demanded seating", dip, True)
    chk("and the dip is at step 5", dat, 5)
    turn, at = turned()
    chk("but there is NO palindromic turn: the peak is the last step",
        turn, False)
    chk("the peak is at the end of the record", at, len(t) - 1)
    # the density measure, on cases computable by hand.
    # (0,0,0) and (1,1,1) are COMPARABLE -- their join is (1,1,1), a member --
    # so that pair is a CHAIN, not a diagonal.  The fixture said otherwise and
    # was wrong about its own arithmetic.
    C2 = frozenset({(0, 0, 0), (1, 1, 1)})
    chk("a comparable pair is already closed", len(demand.closure(C2)[0]), 2)
    F = frozenset({(0, 1, 0), (1, 0, 1)})
    chk("an INCOMPARABLE pair is the diagonal", len(demand.closure(F)[0]), 3)
    chk("its box is 2x2x2", box_size(F), 8)
    chk("so its density is 3/8", round(density(F), 6), 0.375)
    C = frozenset({(0, 0, 0), (0, 0, 1)})
    chk("a chain is already closed", len(demand.closure(C)[0]), 2)
    chk("and a closed figure has density |F|/|box|",
        round(density(C), 6), round(2 / box_size(C), 6))
    chk("density is at most 1 on any figure", density(F) <= 1, True)
    print("density selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
