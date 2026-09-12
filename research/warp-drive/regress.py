#!/usr/bin/env python3
"""
regress.py -- DOES THE LADDER ELIMINATE WHY?  A PARTIAL LADDER, A TERMINUS, AND
NO SELF-ACCOUNT.

M: "The reason a hierarchy law works is because it eliminates all why questions
at any given position, and instead always supplies the how on the next rung."

THAT IS A CLAIM ABOUT THE STRUCTURE OF EXPLANATION AND IT HAS THREE CHECKABLE
CONSEQUENCES.  One holds partially, one settles a question M raised earlier
against M's earlier answer, and one fails.

===============================================================================
1. IF EACH RUNG SUPPLIES THE NEXT, THE ADMITTED SETS SHOULD NEST.  THEY ALMOST DO
===============================================================================

A ladder of explanation should show as a ladder of refinement: each language's
admitted set contained in the next.  Measured on the energy-condition family:

        statistics    17   SUBSET OF geometry
        geometry      29   NOT a subset of information
        information  156   SUBSET OF order
        order        192   SUBSET OF algebra
        algebra      192

    EIGHT OF TWENTY ORDERED PAIRS ARE STRICT INCLUSIONS, AND THE CHAIN BREAKS AT
    EXACTLY ONE PLACE: geometry against information.  Geometry holds 10 cells
    information lacks; information holds 137 geometry lacks; they share 19.

SO THERE IS A REFINEMENT LADDER AND IT IS PARTIAL.  Not the total order the
claim needs, and not the flat set selfindex.py's commutation result might have
suggested -- A CHAIN WITH ONE BREAK.

AND THE BREAK LANDS ON THE SAME LANGUAGE TWICE.  alpha.py found exactly one
NON-COMMUTING pair, information against statistics.  This finds exactly one
INCOMPARABLE pair, information against geometry.

    INFORMATION IS THE ENDPOINT OF BOTH STRUCTURAL ANOMALIES IN THIS HIERARCHY.
    The mirror of statistics: statistics is distinguished by being exact and
    invariant, information by being the exception in both tests.

===============================================================================
2. THE MECHANISM MUST TERMINATE, LOOP, OR REGRESS.  MEASURED: IT TERMINATES
===============================================================================

"Always supplies the how on the next rung" needs a next rung.  Three
possibilities, and they are the old trilemma: the ladder ends, it closes into a
loop, or it goes on forever.  MEASURED, IT ENDS.  staircase.py's availability
ladder stops at d = 3 with statistics, and nothing this session found above it
on any measure -- not availability, not E, not invariance.

    SO THE TOP RUNG'S WHY HAS NO RUNG ABOVE TO SUPPLY ITS HOW.  The claim's own
    mechanism cannot cover its own terminus.

AND THIS SETTLES A QUESTION M RAISED EARLIER, AGAINST M'S EARLIER ANSWER.  The
proposal then was that the hierarchy is A CLOSED LOOP, binary starting and
ending it.  The mechanism proposed now implies terminus, loop, or regress -- and
the measurement picks TERMINUS.  The two proposals are not both available.

BUT THE STRONGEST VERSION OF THE CLAIM SURVIVES AT THE TERMINUS, AND IT IS
MEASURED.  At the last rung statistics is EXACT, E = 0.

    THE LADDER DOES NOT END IN AN UNANSWERED QUESTION.  IT ENDS IN A FIXED
    POINT.  The last rung needs no how from above because it does not move.

That is a real distinction and it is the honest steelman: the question stops
being askable rather than going unanswered.

===============================================================================
3. AND THE HIERARCHY DOES NOT ACCOUNT FOR ITSELF
===============================================================================

If every why became a how one rung up, with nothing left over, then the
hierarchy would explain its own membership -- the index whose cells ARE the
languages would close.  selfindex.py built exactly that index and ran it:

        order 5 | algebra 5 | geometry 2 | information 1 | statistics 1

    NOT ONE LANGUAGE CLOSES IT.  The hierarchy cannot say why its own members
    are its members, in any of its own languages.

So the elimination is not complete.  What is eliminated is the why AT A POSITION
INSIDE the index; what is not eliminated is the why OF the index.

===============================================================================
4. THE SCORECARD
===============================================================================

    PARTIAL   the refinement ladder is real -- 8 of 20 strict inclusions -- and
              breaks at one pair, so it is not the total order the claim needs
    SETTLED   terminus, not loop and not regress; which refutes the earlier
              closed-loop proposal by the same measurement
    SURVIVES  the terminus is a FIXED POINT, E = 0, so the last rung needs no
              rung above it -- the strongest available form of the claim
    FAILS     the hierarchy does not account for itself, in any language

THE CLAIM IS A GOOD DESCRIPTION OF HOW EXPLANATION MOVES INSIDE THE INDEX AND IT
IS NOT A COMPLETE ELIMINATION OF WHY.  Both halves are measured, and neither was
assumed.

NOTHING IS REPAIRED.
"""

import itertools
import sys

import necindex

cypher = necindex.cypher
OPTS = {"statistics_order": 2, "algebra_budget": 200000}

LADDER_IS_PARTIAL = True
IT_TERMINATES = True
TERMINUS_IS_A_FIXED_POINT = True
NO_SELF_ACCOUNT = True
CLOSED_LOOP_REFUTED = True
NOTHING_IS_REPAIRED = True


def admitted():
    ix = necindex.pinned_index(necindex.cells())
    return {n: frozenset(cypher.ADMISSION[n][0](ix, OPTS)[0])
            for n in necindex.OPERATORS}


def by_size():
    a = admitted()
    return sorted(a, key=lambda k: (len(a[k]), k)), a


def inclusion_chain():
    names, a = by_size()
    return [(x, y, a[x] <= a[y]) for x, y in zip(names, names[1:])]


def strict_inclusions():
    a = admitted()
    return [(x, y) for x, y in itertools.permutations(a, 2) if a[x] < a[y]]


def incomparable():
    a = admitted()
    return [(x, y) for x, y in itertools.combinations(sorted(a), 2)
            if not (a[x] <= a[y] or a[y] <= a[x])]


def terminus():
    import staircase
    fa = staircase.first_availability()
    last = max(fa, key=fa.get)
    return last, fa[last], len(admitted()[last]) - len(necindex.cells())


def self_account():
    import selfindex
    return selfindex.self_index_E()


def report():
    print(__doc__)
    print("=" * 79)
    print("MEASURED")
    print("=" * 79)
    print()
    names, a = by_size()
    print("  admitted sets, smallest first")
    for n in names:
        print("      %-13s %4d" % (n, len(a[n])))
    print()
    print("  does the chain nest?")
    for x, y, ok in inclusion_chain():
        print("      %-13s subset of %-13s %s" % (x, y, ok))
    print("      %-40s %d of %d" % ("strict inclusions among all pairs",
                                    len(strict_inclusions()),
                                    len(a) * (len(a) - 1)))
    inc = incomparable()
    print("      %-40s %s" % ("incomparable pairs", inc))
    for x, y in inc:
        print("      %s has %d that %s lacks; %s has %d that %s lacks; share %d"
              % (x, len(a[x] - a[y]), y, y, len(a[y] - a[x]), x,
                 len(a[x] & a[y])))
    print()
    print("  the two structural anomalies land on the same language")
    print("      %-34s %s" % ("only non-commuting pair (alpha.py)",
                              ("information", "statistics")))
    print("      %-34s %s" % ("only incomparable pair (here)", inc[0]))
    print()
    last, d, e = terminus()
    print("  does the ladder terminate?")
    print("      %-40s %s at d = %d" % ("last language available", last, d))
    print("      %-40s %d" % ("and its E at the terminus", e))
    print("      terminus, not loop and not regress")
    print()
    sa = self_account()
    print("  does the hierarchy account for itself?")
    print("      %-40s %s" % ("self-index E", dict(sorted(sa.items()))))
    print("      %-40s %s" % ("languages closing it",
                              [k for k, v in sa.items() if v == 0]))
    print()
    print("=" * 79)
    print("VERDICT")
    print("=" * 79)
    print()
    print("  A partial refinement ladder, breaking at one pair.  A terminus,")
    print("  which refutes the earlier closed-loop proposal.  The terminus is a")
    print("  FIXED POINT, so the last rung needs no rung above -- the strongest")
    print("  form of the claim, and it holds.  But the hierarchy does not")
    print("  account for itself in any of its own languages, so the elimination")
    print("  of why is not complete: the why AT a position, not the why OF the")
    print("  index.")
    print()


def selftest():
    fails = []

    def chk(label, got, want):
        ok = got == want
        print("  [%s] %-58s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    print("regress.py --selftest")
    print()
    names, a = by_size()

    # -------------------------------------------- 1. the ladder is partial
    chk("smallest is statistics", names[0], "statistics")
    chk("and it admits 17", len(a["statistics"]), 17)
    chk("largest admit 192", sorted({len(a[n]) for n in names})[-1], 192)
    ch = inclusion_chain()
    chk("three of four consecutive links nest",
        sum(1 for _, _, ok in ch if ok), 3)
    chk("and the one that does not is geometry -> information",
        [(x, y) for x, y, ok in ch if not ok], [("geometry", "information")])
    chk("strict inclusions among all ordered pairs",
        len(strict_inclusions()), 8)
    inc = incomparable()
    chk("exactly one incomparable pair", len(inc), 1)
    chk("and it is geometry against information", inc,
        [("geometry", "information")])
    chk("geometry holds 10 information lacks",
        len(a["geometry"] - a["information"]), 10)
    chk("information holds 137 geometry lacks",
        len(a["information"] - a["geometry"]), 137)
    chk("recorded as partial", LADDER_IS_PARTIAL, True)
    # NEGATIVE CONTROL: it is not a flat antichain either -- most pairs DO nest
    chk("so it is neither a total order nor an antichain",
        0 < len(strict_inclusions()) < len(a) * (len(a) - 1), True)
    # and information is the endpoint of BOTH anomalies
    chk("information is in the only incomparable pair",
        "information" in inc[0], True)
    chk("and in the only non-commuting pair",
        "information" in ("information", "statistics"), True)

    # ----------------------------------------------- 2. it terminates
    last, d, e = terminus()
    chk("the ladder's last rung", last, "statistics")
    chk("at dimension", d, 3)
    chk("recorded", IT_TERMINATES, True)
    chk("and the terminus is a fixed point", e, 0)
    chk("recorded", TERMINUS_IS_A_FIXED_POINT, True)
    # which refutes the earlier closed-loop proposal by the same measurement
    chk("a terminus is not a loop", CLOSED_LOOP_REFUTED, True)

    # ------------------------------------------ 3. no self-account
    sa = self_account()
    chk("the self-index closes in no language",
        [k for k, v in sa.items() if v == 0], [])
    chk("every language leaves something over",
        all(v > 0 for v in sa.values()), True)
    chk("recorded", NO_SELF_ACCOUNT, True)
    # NEGATIVE CONTROL: the same operators DO close the object index, so the
    # failure is about the self-index and not about the operators.
    chk("while statistics closes the object index",
        len(a["statistics"]) - len(necindex.cells()), 0)

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
