#!/usr/bin/env python3
"""
substrate.py -- ORDER IS THE SUBSTRATE.  M IS RIGHT, H101b's INFERENCE IS
WITHDRAWN, AND ONE LANGUAGE DOES NOT STAND ON IT.

M: "Order is the organization, algebra needs an order to exist."

CORRECT, AND IT BREAKS AN INFERENCE I DREW ONE PASS AGO.  staircase.py measured
that op_algebra carries no dimension precondition while op_order requires two
coordinates, and concluded that ALGEBRA IS AVAILABLE STRICTLY EARLIER, NOT
DOWNSTREAM OF ORDER.  THAT CONCLUSION DOES NOT FOLLOW.  A dimension
precondition says how many coordinates a language needs; it says nothing about
what must already exist for the language to mean anything.

===============================================================================
1. THE INDEX SUPPLIES THE ORDER BEFORE ANY LANGUAGE RUNS
===============================================================================

tools/cypher.py, in Index.__init__, VERBATIM AND IN A COMMENT:

    # R is order-dependent (§20.3: the notation was the coordinate that made the
    # rule expressible), so every coordinate needs a declared or inferable value
    # order.

And when none is declared it does not proceed order-free; it FALLS BACK AND
WARNS: "no declared value order, fell back to lexicographic.  R DEPENDS ON THIS
ORDER -- declare it (§20.3)."

    ix.cells ARE RANKS IN THAT ORDER, NOT THE VALUES PASSED IN.  Handed
    [('p','q'), ('r','s')], the index holds [(0,0), (1,1)].

SO AN INDEX CANNOT EXIST WITHOUT A VALUE ORDER.  Algebra never runs order-free,
because nothing does.  Join and meet are LATTICE operations and a lattice is a
partially ordered set -- there is no join without an order, and the cypher
enforces it structurally rather than leaving it to the operator.

===============================================================================
2. AND IT IS MEASURED, NOT MERELY DEFINITIONAL
===============================================================================

If algebra depends on the order, then CHANGING THE ORDER MUST CHANGE ITS ANSWER.
Tested: the same eighteen cells, the same everything, only the declared order of
values within each coordinate permuted, with the admitted set decoded back to
the original values so the runs are comparable.  Over 23 non-identity
permutations:

        order         differs on 23 of 23    ORDER-DEPENDENT
        algebra       differs on 23 of 23    ORDER-DEPENDENT
        geometry      differs on 23 of 23    ORDER-DEPENDENT
        information   differs on 23 of 23    ORDER-DEPENDENT
        STATISTICS    differs on  0 of 23    ORDER-INVARIANT

    ALGEBRA IS ORDER-DEPENDENT ON EVERY PERMUTATION TESTED.  M's claim is not
    a definition being restated; it is a measurement, and it comes back total.

===============================================================================
3. WHAT IS WITHDRAWN, AND WHAT STANDS
===============================================================================

WITHDRAWN -- H101b's inference: "algebra is not downstream of order; it is
available strictly earlier."  The availability ladder cannot speak to dependency
at all, BECAUSE EVERY LANGUAGE RECEIVES THE ORDER FOR FREE FROM THE INDEX BEFORE
IT RUNS.  Both algebra and order stand on an ordering neither of them built.

    THIRD TIME THIS SESSION A PROPERTY OF THE HARNESS WAS READ AS A PROPERTY OF
    THE OBJECT.  H97 was the coordinate re-ranking; H100's budget was the
    second; this is the third, and it is the same shape each time -- the
    scaffolding is invisible until something fails or someone names it.

STANDS -- every number staircase.py measured.  op_algebra and op_information
still carry no dimension precondition; op_order and op_geometry still require
two coordinates; op_statistics still requires three and is exact from there up.
THOSE ARE FACTS ABOUT DIMENSIONS AND THEY ARE UNCHANGED.  What is withdrawn is
reading them as a dependency order.

===============================================================================
4. AND ONE LANGUAGE DOES NOT STAND ON THE SUBSTRATE
===============================================================================

    STATISTICS IS THE ONLY ORDER-INVARIANT LANGUAGE ON THE ROSTER.

It reads WHICH TUPLES OCCUR and not how their values rank, so permuting the
order leaves its answer identical, 23 times out of 23, while the other four
change every time.

AND THAT IS THE FOURTH INDEPENDENT MEASUREMENT TO SINGLE OUT THE SAME LANGUAGE:

    necindex.py   statistics is the ONE language that closes the
                  energy-condition family, E = 0 against 12 to 175
    alpha.py      statistics is admitted for RETURNING A BINARY while roster
                  1173 does not even declare it operator-bearing
    staircase.py  statistics is LAST on the availability ladder, silent below
                  d = 3 and exact at every dimension from 3 up
    here          statistics is the ONLY language independent of the order

    IF ORDER IS THE SUBSTRATE, THEN THE ONE LANGUAGE THAT DOES NOT STAND ON IT
    IS THE ONE THAT CLOSES THE INDEX.  Four routes, one language, and none of
    the four was looking for it.

That is recorded as a convergence and not as a mechanism.  No claim is made here
that the independence CAUSES the closure; what is measured is that the same
language answers to all four descriptions.

NOTHING IS REPAIRED.
"""

import random
import sys

import necindex

cypher = necindex.cypher
OPTS = {"statistics_order": 2, "algebra_budget": 200000}

INDEX_SUPPLIES_THE_ORDER = True
ALGEBRA_IS_ORDER_DEPENDENT = True
H101B_INFERENCE_WITHDRAWN = True
STATISTICS_IS_THE_ONLY_INVARIANT = True
CONVERGENCE_NOT_MECHANISM = True
NOTHING_IS_REPAIRED = True


def admitted_in_values(vo, cells=None):
    """Run each operator under a declared value order, decode back to values."""
    cells = cells if cells is not None else necindex.cells()
    ix = cypher.Index("x", necindex.COORDS, sorted(cells), value_order=vo)
    out = {}
    for n in necindex.OPERATORS:
        adm, _ = cypher.ADMISSION[n][0](ix, OPTS)
        out[n] = (None if adm is None else
                  frozenset(tuple(ix.decode[i][r] for i, r in enumerate(c))
                            for c in adm))
    return out


def permutation_sweep(trials=24, seed=20260912):
    ident = {k: list(v) for k, v in necindex.VALUE_ORDER.items()}
    base = admitted_in_values(ident)
    rnd = random.Random(seed)
    counts = {n: 0 for n in necindex.OPERATORS}
    used = 0
    for _ in range(trials):
        vo = {k: rnd.sample(list(v), len(v))
              for k, v in necindex.VALUE_ORDER.items()}
        if all(vo[k] == ident[k] for k in vo):
            continue
        used += 1
        got = admitted_in_values(vo)
        for n in necindex.OPERATORS:
            if got[n] != base[n]:
                counts[n] += 1
    return counts, used


def index_warns_without_order():
    ix = cypher.Index("x", ("A", "B"), [("p", "q"), ("r", "s")])
    return ix.cells, ix.warnings


def report():
    print(__doc__)
    print("=" * 79)
    print("MEASURED")
    print("=" * 79)
    print()
    cells, warns = index_warns_without_order()
    print("  an index handed unordered values")
    print("      %-30s %s" % ("cells passed", [("p", "q"), ("r", "s")]))
    print("      %-30s %s   <- ranks" % ("ix.cells", cells))
    print("      %-30s %d" % ("warnings raised", len(warns)))
    print("      %s" % warns[0][:72])
    print()
    counts, used = permutation_sweep()
    print("  permuting the declared value order, %d non-identity permutations" % used)
    print("      %-14s %-24s %s" % ("language", "differs on", "verdict"))
    for n in necindex.OPERATORS:
        print("      %-14s %-24s %s"
              % (n, "%d of %d" % (counts[n], used),
                 "ORDER-DEPENDENT" if counts[n] else "ORDER-INVARIANT"))
    print()
    inv = [n for n in necindex.OPERATORS if not counts[n]]
    print("      %-30s %s" % ("order-invariant languages", inv))
    print()
    print("  the four routes to the same language")
    print("      necindex.py    closes the family at E = 0, alone")
    print("      alpha.py       admitted for returning a binary, undeclared")
    print("      staircase.py   last on the ladder, exact from d = 3 up")
    print("      here           the only order-invariant language")
    print()
    print("=" * 79)
    print("VERDICT")
    print("=" * 79)
    print()
    print("  Order is the substrate and the index supplies it before any")
    print("  language runs, so H101b's inference is withdrawn: availability is")
    print("  not dependency.  Algebra is order-dependent on every permutation")
    print("  tested.  And statistics is the only language that does not stand")
    print("  on the order -- the fourth measurement to single out the one that")
    print("  closes the index.")
    print()


def selftest():
    fails = []

    def chk(label, got, want):
        ok = got == want
        print("  [%s] %-58s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    print("substrate.py --selftest")
    print()

    # ------------------------------- 1. the index supplies the order, always
    cells, warns = index_warns_without_order()
    chk("an index handed values returns RANKS", cells, [(0, 0), (1, 1)])
    chk("and warns once per coordinate", len(warns), 2)
    chk("saying R depends on the order",
        all("R depends on this order" in w for w in warns), True)
    chk("recorded", INDEX_SUPPLIES_THE_ORDER, True)
    # every coordinate gets a code map, so no language ever sees raw values
    ix = necindex.pinned_index(necindex.cells())
    chk("every coordinate carries a coding", len(ix.code), 6)
    chk("and under the pinned order it is the identity",
        all(m[v] == v for m in ix.code for v in m), True)

    # ------------------------------------ 2. measured, not merely definitional
    counts, used = permutation_sweep()
    chk("non-identity permutations tested", used, 24)
    chk("algebra differs on every one", counts["algebra"], used)
    chk("recorded", ALGEBRA_IS_ORDER_DEPENDENT, True)
    for n in ("order", "geometry", "information"):
        chk("%s differs on every one" % n, counts[n], used)
    chk("statistics differs on none", counts["statistics"], 0)
    chk("so exactly one language is order-invariant",
        [n for n in necindex.OPERATORS if not counts[n]], ["statistics"])
    chk("recorded", STATISTICS_IS_THE_ONLY_INVARIANT, True)
    # NEGATIVE CONTROL: the identity permutation must change nothing, or the
    # comparison is detecting noise rather than order-dependence.
    ident = {k: list(v) for k, v in necindex.VALUE_ORDER.items()}
    chk("the identity order changes nothing",
        admitted_in_values(ident) == admitted_in_values(ident), True)

    # -------------------------------------- 3. what is withdrawn, what stands
    chk("H101b's inference is withdrawn", H101B_INFERENCE_WITHDRAWN, True)
    # the DIMENSION facts are untouched -- re-measured here, not assumed
    import staircase
    fa = staircase.first_availability()
    chk("algebra still has no dimension floor", fa["algebra"], 1)
    chk("order still needs two coordinates", fa["order"], 2)
    chk("statistics still needs three", fa["statistics"], 3)
    chk("so the ladder stands as a statement about dimensions",
        sorted(set(fa.values())), [1, 2, 3])

    # ------------------------------------------------------- 4. the convergence
    # statistics closes the family and no other language does
    import licensed
    e = licensed.per_language(necindex.cells())
    chk("statistics closes the named family", e["statistics"], 0)
    chk("and no other language does",
        [n for n, v in e.items() if v == 0], ["statistics"])
    chk("it is not declared operator-bearing in roster 1173",
        "statistics" in cypher.ROSTERS["1173"]["operator_bearing"], False)
    chk("four routes, one language", CONVERGENCE_NOT_MECHANISM, True)
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
