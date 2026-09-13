#!/usr/bin/env python3
r"""
twoway.py -- HOW THE TWO INDICES TALK, AND IN WHICH LANGUAGE.

M: "look at how the two indices talk to each other.  The communication is two
way.  The language hierarchy instrument may be needed here as well."

    THEY TALK IN EXACTLY ONE LANGUAGE, AND ONLY THERE IS IT TWO-WAY.
    THE CHANNEL SETS ARE STRICTLY NESTED, AND THAT NESTING IS NOT THE
    CONTAINMENT HIERARCHY.

    python3 twoway.py             the reading
    python3 twoway.py --selftest  fixtures

===============================================================================
WHAT A CHANNEL IS HERE
===============================================================================

An earlier pass asked whether the exotic and periodic indices ANTICIPATE each
other -- hide one, close the other, count what is recovered -- and got zero in
both directions under all five languages.  That test asks whether one index
predicts the other's cells.  This one asks something weaker and more useful:

    IN WHICH LANGUAGE CAN A STATEMENT ABOUT ONE INDEX BE MADE AT ALL WITHOUT
    ADMITTING CELLS THAT INDEX DOES NOT HOLD?

A language L CLOSES an index X when L(X) = X, E = 0 -- it says exactly what is
there and nothing more.  A language that over-generates on X cannot carry a
claim about X without importing cells X denies.  So the set of languages that
close an index is the set of channels available to it, and a language closing
BOTH indices is a channel in which the two can speak to each other.

===============================================================================
1. WHICH LANGUAGE CLOSES WHICH INDEX
===============================================================================

                                order  algebra  geometry  information  statistics
    exotic mechanisms (8)        51      51        13         11          **0**
    periodic layout (90)         36      36        36        **0**        **0**
    Janet, (n+l, l) (19)        **0**   **0**     **0**      **0**        **0**

The entries are E = |L(X)| - |X|.  Three indices, and the sets of languages that
close them are STRICTLY NESTED:

    closes(exotic)  =  {statistics}
        subset of
    closes(layout)  =  {statistics, information}
        subset of
    closes(Janet)   =  all five

**AND THAT IS NOT A CHEAP RESULT.**  Over 300 random sets of the same size in
the same box, drawn for each index separately, **every single one was closed by
exactly ONE language -- 300 of 300, both boxes, never two and never five.**  The
periodic layout's two and Janet's five are each unreachable by chance at that
sample size.

===============================================================================
2. THE CHANNELS, AND THE ASYMMETRY IS TOTAL
===============================================================================

    exotic <-> periodic layout
        TWO-WAY   (closes both)      statistics
        one-way   (periodic only)    information
        one-way   (exotic only)      NONE

    exotic <-> Janet
        TWO-WAY   (closes both)      statistics
        one-way   (Janet only)       order, algebra, geometry, information
        one-way   (exotic only)      NONE

**STATISTICS IS THE ONLY TWO-WAY CHANNEL**, against either periodic index.  And
the asymmetry runs one way without exception: there is NO language that closes
the exotic index and fails to close a periodic one.

    THE EXOTIC INDEX IS THE HARDER OF THE TWO TO SPEAK ABOUT.  Its channel set
    is a subset of the periodic index's, so anything sayable about exotic matter
    without over-claiming is also sayable about the periodic table -- and not
    the other way round.

That is a precise sense in which the communication is two-way and also unequal:
two-way in `statistics`, one-way in `information`, and closed in the other
three.

===============================================================================
3. A SECOND ORDERING, ON INDEXES RATHER THAN LANGUAGES
===============================================================================

The nesting in section 1 orders the three indexes by how many languages close
them -- 1, 2, 5.  **That is an ordering of INDEXES, and it is not the
containment hierarchy of the languages.**  The hierarchy law orders the five
operators against each other on a fixed index; this orders indexes against each
other by which operators they admit.  The two are different objects and the
second is not derivable from the first: the law says nothing about which index
any operator will close.

**AND THE JANET LAYOUT IS THE MAXIMALLY AGREEABLE INDEX.**  All five languages
exactly generate it, at a control rate of 0 in 300.  The (n+l, l) coordinate is
already recorded at E = 0 in the corpus; what is added here is that this holds
in EVERY language, not one -- the drawn eighteen-column layout does not, missing
by 36 cells in three of the five.

===============================================================================
WHAT IT REFUSES TO DO
===============================================================================

**It does not call a channel an anticipation.**  A shared closing language means
a claim can be MADE in both without over-claiming; it does not mean either index
predicts the other's cells, and the measurement that asked that returned zero.

**It does not read the nesting as the hierarchy law.**  Section 3 says why they
are different objects; the law orders operators on an index, this orders indexes
by operator.

**It does not report E = 0 without its control.**  A zero in a large box can be
an artefact of size, and the control -- 300 of 300 random sets closed by exactly
one language -- is what makes these two and five worth printing.
"""

import importlib.util
import itertools
import os
import random
import sys

import hlaw

_POP = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                     "..", "..", "tools", "populate.py"))


def _populate():
    """Import the seated instrument by path. It owns the periodic layout and the
    Janet coordinate; nothing here recomputes either."""
    spec = importlib.util.spec_from_file_location("populate", _POP)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# The exotic index, as synth.py seats it: (T, Q, S, D, E, G).
EXOTIC = frozenset({
    (0, 1, 0, 1, 0, 1), (0, 1, 1, 1, 0, 1), (0, 1, 2, 1, 0, 0),
    (0, 1, 3, 1, 0, 0), (0, 1, 3, 1, 1, 0), (0, 0, 2, 2, 0, 2),
    (0, 0, 2, 2, 2, 2), (1, 0, 4, 0, 2, 1),
})


def periodic_indexes():
    """(layout, janet) from the seated instrument."""
    pop = _populate()
    held, _admitted = pop.layout_closure()
    janet = frozenset(pop.janet_cell(Z) for Z in range(1, 109)
                      if pop.janet_cell(Z))
    return frozenset(held), janet


def closers(S):
    """The set of languages that CLOSE S -- L(S) = S, E = 0.

    This is the channel set: a language that over-generates cannot carry a claim
    about S without importing cells S denies.
    """
    S = frozenset(S)
    cl, _ = hlaw.closures(S)
    return frozenset(L for L in hlaw.LANGS if len(cl[L]) == len(S))


def defects(S):
    S = frozenset(S)
    cl, _ = hlaw.closures(S)
    return {L: len(cl[L]) - len(S) for L in hlaw.LANGS}


def observed_box(S):
    d = len(next(iter(S)))
    return [sorted({c[i] for c in S}) for i in range(d)]


def control(S, n=300, seed=7):
    """(distribution of channel-set sizes, count closed by all five).

    Without this a zero means nothing: a set in a large box can close for no
    reason but its shape, and the question is whether THIS set closes in more
    languages than an arbitrary one of the same size.
    """
    allc = list(itertools.product(*observed_box(S)))
    rnd = random.Random(seed)
    dist, five = {}, 0
    for _ in range(n):
        k = len(closers(rnd.sample(allc, len(S))))
        dist[k] = dist.get(k, 0) + 1
        five += (k == 5)
    return dist, five, n


def channels(a, b):
    """(two-way, one-way-b, one-way-a) between two indexes."""
    ca, cb = closers(a), closers(b)
    return ca & cb, cb - ca, ca - cb


# --------------------------------------------------------------- the reading

def report():
    layout, janet = periodic_indexes()
    idx = [("exotic mechanisms", EXOTIC), ("periodic layout (period,group)", layout),
           ("Janet (n+l, l)", janet)]
    print("=" * 74)
    print("HOW THE TWO INDICES TALK, AND IN WHICH LANGUAGE")
    print("=" * 74)
    print()
    print("A language CLOSES an index when L(X) = X: it says exactly what is")
    print("there and nothing more. A language that over-generates cannot carry a")
    print("claim about that index without importing cells the index denies. So")
    print("the languages that close an index ARE its available channels.")
    print()

    print("1. WHICH LANGUAGE CLOSES WHICH INDEX   (entries are E = |L(X)| - |X|)")
    print("   %-30s %s" % ("index", "  ".join("%-11s" % L for L in hlaw.LANGS)))
    for nm, S in idx:
        d = defects(S)
        print("   %-30s %s" % ("%s (%d)" % (nm, len(S)),
              "  ".join("%-11s" % ("**0**" if d[L] == 0 else str(d[L]))
                        for L in hlaw.LANGS)))
    print()
    print("   STRICTLY NESTED:")
    for nm, S in idx:
        print("     closes(%-28s) = %s" % (nm, sorted(closers(S))))
    print()

    print("2. AND IT IS NOT A CHEAP RESULT.")
    for nm, S in idx[1:]:
        dist, five, n = control(S)
        print("   %-28s random sets of the same size, same box:" % nm)
        print("      channel-set sizes %s ; all five in %d of %d"
              % (dict(sorted(dist.items())), five, n))
    print("   Every random set is closed by exactly ONE language. The layout's")
    print("   two and Janet's five are each unreachable by chance at this sample.")
    print()

    print("3. THE CHANNELS, AND THE ASYMMETRY IS TOTAL.")
    for nm, S in idx[1:]:
        two, one_b, one_a = channels(EXOTIC, S)
        print("   exotic <-> %s" % nm)
        print("      TWO-WAY (closes both)   %s" % (sorted(two) or "NONE"))
        print("      one-way (%-14s) %s" % (nm.split()[0] + " only", sorted(one_b) or "NONE"))
        print("      one-way (exotic only)   %s" % (sorted(one_a) or "NONE"))
    print()
    print("   STATISTICS IS THE ONLY TWO-WAY CHANNEL, against either. And there")
    print("   is NO language closing the exotic index that fails to close a")
    print("   periodic one -- the asymmetry runs one way without exception.")
    print("   THE EXOTIC INDEX IS THE HARDER OF THE TWO TO SPEAK ABOUT: anything")
    print("   sayable about it without over-claiming is also sayable about the")
    print("   periodic table, and not the other way round.")
    print()

    print("4. A SECOND ORDERING, ON INDEXES RATHER THAN LANGUAGES.")
    print("   The nesting orders three indexes by how many languages close them")
    print("   -- 1, 2, 5. THE HIERARCHY LAW ORDERS OPERATORS ON A FIXED INDEX;")
    print("   THIS ORDERS INDEXES BY WHICH OPERATORS THEY ADMIT. Different")
    print("   objects, and the second does not follow from the first: the law")
    print("   says nothing about which index any operator will close.")
    print()
    print("   AND JANET IS THE MAXIMALLY AGREEABLE INDEX -- all five exactly")
    print("   generate it, at a control rate of 0 in 300. The corpus already")
    print("   records (n+l, l) at E = 0; what is added is that this holds in")
    print("   EVERY language. The drawn eighteen-column layout does not, missing")
    print("   by 36 cells in three of the five.")
    return 0


# -------------------------------------------------------------------- checks

def selftest():
    ok = True

    def chk(name, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", name, got))
        if not good:
            print("        expected %r" % (want,))

    print("twoway selftest")
    layout, janet = periodic_indexes()
    chk("the layout is the corpus's 90 held cells", len(layout), 90)
    chk("the Janet index over LW1's table", len(janet), 19)
    chk("the exotic index is synth.py's eight", len(EXOTIC), 8)

    chk("statistics closes the exotic index, alone",
        sorted(closers(EXOTIC)), ["statistics"])
    chk("the layout is closed by information and statistics",
        sorted(closers(layout)), ["information", "statistics"])
    chk("and Janet by all five", len(closers(janet)), 5)

    chk("the channel sets are STRICTLY nested",
        closers(EXOTIC) < closers(layout) < closers(janet), True)

    two, one_b, one_a = channels(EXOTIC, layout)
    chk("the only two-way channel is statistics", sorted(two), ["statistics"])
    chk("information is one-way, periodic only", sorted(one_b), ["information"])
    chk("and NOTHING is exotic-only", sorted(one_a), [])
    two2, one_b2, one_a2 = channels(EXOTIC, janet)
    chk("against Janet the two-way channel is still statistics alone",
        sorted(two2), ["statistics"])
    chk("and still nothing is exotic-only", sorted(one_a2), [])

    # The layout's own recorded figure, from the seated instrument.
    chk("the layout misses by 36 in order, as the corpus records",
        defects(layout)["order"], 36)

    # The controls are what make the zeros mean anything.
    for nm, S in (("layout", layout), ("Janet", janet)):
        dist, five, n = control(S)
        chk("%s: every random set is closed by exactly one language" % nm,
            sorted(dist), [1])
        chk("%s: none of %d random sets is closed by all five" % (nm, n), five, 0)

    print("twoway selftest: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else report())
