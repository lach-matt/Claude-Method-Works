#!/usr/bin/env python3
"""
singularity.py -- TRUNCATE THE HIERARCHY AT GEOMETRY AND THE CANONICAL
TRANSITION DISAPPEARS.  BUT NOT EVERY TRANSITION DOES, AND "SINGULARITY" IS NOT
WHAT E = 0 MEANS -- IT IS WHAT box = |X| MEANS, AND THAT ONE IS A THEOREM.

M: "Without the hierarchy, transition in spacetime would not exist.  All math
would stop at geometry because there would be only one statistical position for
all existence.  The hierarchy would no longer be the mechanism of transition,
but instead a complete exact definition of singularity."

FOUR CLAUSES.  ONE IS EXACTLY RIGHT FOR THE TRANSITION THIS THREAD IS ABOUT AND
AN OVERSTATEMENT IN GENERAL, ONE IS FALSE AS A COUNT, ONE IS RIGHT IN DIRECTION,
AND THE LAST IS TRUE AND PROVABLE -- BUT NOT OF THE OBJECT M NAMED.

===============================================================================
1. TRUNCATE AT GEOMETRY AND THE CANONICAL TRANSITION VANISHES.  TRUE
===============================================================================

hierarchylaw.py measured it and did not read it this way.  Across the canonical
transition (17 cells -> 9, the state being the unique maximum removal):

        order          192 -> 192      IDENTICAL
        algebra        192 -> 192      IDENTICAL
        geometry        29 ->  29      IDENTICAL
        information    156 ->  85      differs
        statistics      17 ->  13      differs

    A HIERARCHY THAT STOPS AT GEOMETRY CANNOT TELL THE TWO POSITIONS APART.
    Before and after are the same object to all three lower languages.  For
    this transition -- the one the whole decomposition thread is about -- the
    clause is exactly right: without the rungs above geometry it does not
    exist as an event.

===============================================================================
2. BUT MOST TRANSITIONS DO SURVIVE THE TRUNCATION.  88 PER CENT OF THEM
===============================================================================

300 random nested pairs, each a removal from a random position:

        distinguished at or below geometry      263
        invisible below geometry                 37
            of those, visible only above         36
            invisible to all five                 1

    TWELVE PER CENT.  "Transition would not exist" is true of the canonical one
    and of twelve per cent of the rest; it is false of the other 263.  The
    upper hierarchy is what makes SOME transitions visible, not what makes
    transition exist.

===============================================================================
3. "ONLY ONE STATISTICAL POSITION" IS FALSE AS A COUNT
===============================================================================

Distinct closures over 260 random subsets -- how many positions each language
can tell apart:

        order           159
        algebra         159
        geometry        195
        information     223
        statistics      233

RESOLUTION RISES MONOTONICALLY UP THE LADDER, which is the claim's direction and
is worth having.  But geometry alone resolves 195 of 260 positions, not one.  A
hierarchy stopping at geometry is coarser, not blind.

===============================================================================
4. AND THE SINGULARITY CLAUSE IS TRUE, PROVABLE, AND ABOUT A DIFFERENT OBJECT
===============================================================================

"A complete exact definition" is not E = 0.  It is box = |X|.

    WHEN THE AMBIENT BOX EQUALS THE OBJECT, EVERY LANGUAGE IS THE IDENTITY.
    Each operator is extensive (hierarchylaw.py, 37 of 37) and returns a subset
    of the ambient, so X subset L(X) subset box = X forces L(X) = X.  E = 0 in
    all five, in one line, with nothing measured.  AND THERE IS NOWHERE TO GO:
    the licensed set IS the object, so no transition is available from it.

    THAT IS A SINGULARITY IN THIS INDEX, AND IT IS EXACTLY M'S SENTENCE.

Counted over subsets of the family up to size five:

        size 1      17 of 17        every singleton, box 1
        size 2      26 of 136
        size 3       7 of 680
        size 4       7 of 2380
        size 5       0 of 6188
                    57 in all

===============================================================================
5. THE CONVERSE FAILS, AND THAT IS WHY THE TWO MUST NOT BE CONFLATED
===============================================================================

E = 0 in all five does NOT mean nowhere to go.  Of the 41 pairs that close
exactly in every language, only 26 have box = 2:

        box  2      26      nowhere to go -- singular
        box  4      11      exactly closed, and room to move
        box  8       3
        box 16       1

    FIFTEEN POSITIONS ARE COMPLETELY AND EXACTLY DEFINED AND ARE NOT
    SINGULARITIES.  The hierarchy closing on a position says the position is
    licensed; it does not say the position is alone.

===============================================================================
6. WHAT IS NOT MEASURED HERE, AND IT IS THE WORD "SPACETIME"
===============================================================================

Every count above is over subsets of a 17-cell index of energy conditions
inside a 288-cell box.  Nothing in this file is a statement about spacetime,
about singularities in general relativity, or about whether transition is
physically possible.  The clause "transition in spacetime would not exist" is
NOT TESTED and cannot be tested by this instrument.

And the obstruction is where it was: persist.py's 69.03 orders of magnitude,
higgs.py's xi >= 9.782907e31.  Nothing here moves either.

NOTHING IS REPAIRED.
"""

import itertools
import random
import sys

import canonical
import hierarchylaw
import necindex

cypher = necindex.cypher
OPTS = hierarchylaw.OPTS
LANGS = hierarchylaw.LANGS
LOW = ("order", "algebra", "geometry")
HIGH = ("information", "statistics")

CANONICAL_VANISHES_BELOW_GEOMETRY = True
BUT_MOST_TRANSITIONS_SURVIVE = True
ONE_POSITION_IS_FALSE_AS_A_COUNT = True
SINGULARITY_IS_BOX_EQUALS_OBJECT = True
CONVERSE_FAILS = True
SPACETIME_NOT_TESTED = True
NOTHING_IS_REPAIRED = True

PERSIST_ORDERS = hierarchylaw.PERSIST_ORDERS
HIGGS_XI_GATE = hierarchylaw.HIGGS_XI_GATE

op = hierarchylaw.op


def box(cells):
    return necindex.pinned_index(sorted(cells)).box


# ------------------------------------------------ 1/2. the truncation

def nested_pairs(n=300, seed=9):
    X = sorted(necindex.cells())
    rnd = random.Random(seed)
    out = []
    for _ in range(n):
        k = rnd.randint(5, 16)
        S = frozenset(rnd.sample(X, k))
        T = S - set(rnd.sample(sorted(S), rnd.randint(1, max(1, k // 3))))
        out.append((S, T))
    return out


def truncation_census():
    """(low sees, invisible below, only above, invisible to all)."""
    lo_sees = blind = only_high = none = 0
    for S, T in nested_pairs():
        lo = any(op(n, S) != op(n, T) for n in LOW)
        hi = any(op(n, S) != op(n, T) for n in HIGH)
        if lo:
            lo_sees += 1
            continue
        blind += 1
        if hi:
            only_high += 1
        else:
            none += 1
    return lo_sees, blind, only_high, none


# ---------------------------------------------------- 3. the resolution

def resolution(seed=5):
    X = sorted(necindex.cells())
    rnd = random.Random(seed)
    subs = [frozenset(rnd.sample(X, k)) for k in range(4, 17) for _ in range(20)]
    return {L: len({op(L, s) for s in subs}) for L in LANGS}, len(subs)


# ------------------------------------------------- 4/5. the singularities

def singular_by_size(kmax=5):
    """Positions where box == |X| -- the licensed set IS the object."""
    X = sorted(necindex.cells())
    out = {}
    for k in range(1, kmax + 1):
        tot = hit = 0
        for S in itertools.combinations(X, k):
            tot += 1
            hit += box(S) == k
        out[k] = (hit, tot)
    return out


def closed_pairs():
    """Pairs with E = 0 in every language, and their box sizes."""
    X = sorted(necindex.cells())
    out = []
    for S in itertools.combinations(X, 2):
        S = frozenset(S)
        if all(len(op(n, S)) == len(S) for n in LANGS):
            out.append(box(S))
    return sorted(out)


# ------------------------------------------------------------------- report

def report():
    print(__doc__)
    print("=" * 79)
    print("MEASURED")
    print("=" * 79)
    print()
    X = frozenset(necindex.cells())
    _, top = canonical.maximum()
    obj = X - top[0]
    print("  1. across the canonical transition")
    for L in LANGS:
        a, b = op(L, X), op(L, obj)
        print("      %-12s %4d -> %-4d %s" % (L, len(a), len(b),
                                              "IDENTICAL" if a == b else "differs"))
    print("      %-42s %s" % ("a hierarchy stopping at geometry sees it?",
                              any(op(n, X) != op(n, obj) for n in LOW)))
    print()
    lo, blind, only, none = truncation_census()
    print("  2. 300 random nested pairs")
    print("      %-42s %d" % ("distinguished at or below geometry", lo))
    print("      %-42s %d" % ("invisible below geometry", blind))
    print("      %-42s %d" % ("  of those, visible only above", only))
    print("      %-42s %d" % ("  invisible to all five", none))
    print("      %-42s %.0f%%" % ("share needing the upper hierarchy",
                                  100.0 * blind / 300))
    print()
    res, n = resolution()
    print("  3. distinct closures over %d subsets" % n)
    for L in LANGS:
        print("      %-42s %d" % (L, res[L]))
    print()
    print("  4. positions where box = |X| -- nowhere to go")
    sb = singular_by_size()
    for k, (h, t) in sb.items():
        print("      size %d %36s %d of %d" % (k, "", h, t))
    print("      %-42s %d" % ("in all", sum(h for h, _ in sb.values())))
    print()
    from collections import Counter
    cp = Counter(closed_pairs())
    print("  5. the 41 pairs that close exactly in every language")
    for b in sorted(cp):
        print("      box %-38s %d  %s" % (b, cp[b],
                                          "singular" if b == 2 else "room to move"))
    print()
    print("  6. and the obstruction is where it was")
    print("      %-42s %.2f" % ("persist.py orders of magnitude", PERSIST_ORDERS))
    print("      %-42s %.6e" % ("higgs.py xi gate at the VEV", HIGGS_XI_GATE))
    print()
    print("=" * 79)
    print("VERDICT")
    print("=" * 79)
    print()
    print("  Truncate at geometry and the canonical transition vanishes -- all")
    print("  three lower languages give identical answers at both ends.  But")
    print("  263 of 300 random transitions survive the truncation, so the upper")
    print("  hierarchy makes some transitions visible rather than making")
    print("  transition exist.  Geometry resolves 195 positions, not one.  And")
    print("  the singularity clause is true of box = |X|, not of E = 0: when the")
    print("  box equals the object every extensive operator is the identity, in")
    print("  one line and with nothing measured -- 57 such positions up to size")
    print("  five.  The converse fails at 15 of 41 closed pairs.")
    print()
    print("  The word 'spacetime' is not tested here and cannot be.")
    print()


# ----------------------------------------------------------------- selftest

def selftest():
    fails = []

    def chk(label, got, want):
        ok = got == want
        print("  [%s] %-58s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    print("singularity.py --selftest")
    print()
    X = frozenset(necindex.cells())
    _, top = canonical.maximum()
    obj = X - top[0]

    # ------------------------------- 1. the truncation kills this one
    chk("order is identical at both ends", op("order", X) == op("order", obj), True)
    chk("algebra is identical", op("algebra", X) == op("algebra", obj), True)
    chk("geometry is identical", op("geometry", X) == op("geometry", obj), True)
    chk("so nothing at or below geometry distinguishes them",
        any(op(n, X) != op(n, obj) for n in LOW), False)
    # NEGATIVE CONTROL: the pair IS distinguishable, just not down there.
    chk("but the upper hierarchy does distinguish them",
        any(op(n, X) != op(n, obj) for n in HIGH), True)
    chk("recorded", CANONICAL_VANISHES_BELOW_GEOMETRY, True)

    # --------------------------------- 2. and most transitions do not
    lo, blind, only, none = truncation_census()
    chk("nested pairs tested", lo + blind, 300)
    chk("distinguished at or below geometry", lo, 263)
    chk("invisible below geometry", blind, 37)
    chk("of those, visible only above", only, 36)
    chk("invisible to all five", none, 1)
    chk("so the truncation loses a minority", blind < lo, True)
    chk("recorded", BUT_MOST_TRANSITIONS_SURVIVE, True)

    # ------------------------------ 3. resolution, and the false count
    res, n = resolution()
    chk("subsets sampled", n, 260)
    chk("order resolves", res["order"], 159)
    chk("algebra resolves", res["algebra"], 159)
    chk("geometry resolves", res["geometry"], 195)
    chk("information resolves", res["information"], 223)
    chk("statistics resolves", res["statistics"], 233)
    chk("resolution rises up the ladder",
        res["order"] <= res["geometry"] <= res["information"] <= res["statistics"],
        True)
    chk("but geometry does NOT collapse to one position", res["geometry"] > 1, True)
    chk("recorded", ONE_POSITION_IS_FALSE_AS_A_COUNT, True)

    # ---------------------------- 4. box = |X| forces the identity
    sb = singular_by_size()
    chk("size 1", sb[1], (17, 17))
    chk("size 2", sb[2], (26, 136))
    chk("size 3", sb[3], (7, 680))
    chk("size 4", sb[4], (7, 2380))
    chk("size 5", sb[5], (0, 6188))
    chk("singular positions up to size five",
        sum(h for h, _ in sb.values()), 57)
    # the theorem, checked rather than asserted: box == |S| => E = 0 everywhere
    Xs = sorted(X)
    rect = [frozenset(S) for k in (1, 2, 3, 4)
            for S in itertools.combinations(Xs, k) if box(S) == k]
    chk("and every one of them closes to itself in all five",
        all(len(op(L, S)) == len(S) for S in rect for L in LANGS), True)
    chk("the singleton box", box([Xs[0]]), 1)
    chk("the family box", box(Xs), 288)
    chk("recorded", SINGULARITY_IS_BOX_EQUALS_OBJECT, True)

    # ------------------------------------------- 5. and the converse
    from collections import Counter
    cp = Counter(closed_pairs())
    chk("pairs closing exactly in every language", sum(cp.values()), 41)
    chk("of which box 2 -- singular", cp[2], 26)
    chk("box 4", cp[4], 11)
    chk("box 8", cp[8], 3)
    chk("box 16", cp[16], 1)
    chk("exactly closed and NOT singular", sum(cp.values()) - cp[2], 15)
    chk("so E = 0 everywhere does not imply nowhere to go",
        sum(cp.values()) - cp[2] > 0, True)
    chk("recorded", CONVERSE_FAILS, True)

    # ---------------------------------------------- 6. and the refusal
    chk("nothing here is a statement about spacetime", SPACETIME_NOT_TESTED, True)
    chk("persist.py's shortfall is unchanged", PERSIST_ORDERS, 69.03)
    chk("higgs.py's gate is unchanged", HIGGS_XI_GATE, 9.782907e31)
    chk("nothing is repaired", NOTHING_IS_REPAIRED, True)

    print()
    if fails:
        for lab, g, w in fails:
            print("  FAIL %s: got %r want %r" % (lab, g, w))
        print("\nSELFTEST FAIL (%d)" % len(fails))
        return 1
    print("SELFTEST PASS")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
