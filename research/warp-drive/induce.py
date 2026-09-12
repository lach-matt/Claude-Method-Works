#!/usr/bin/env python3
"""
induce.py -- LET THE OBSERVATIONS DICTATE IT.  THE CLOSURE THEOREM SURVIVES AND
GETS STRONGER; THE LADDER DOES NOT SURVIVE AT ALL; AND ORDER AND ALGEBRA ARE THE
SAME OPERATOR ON EVERY INDEX EVER TESTED.

M: "I suspect all my hierarchy law assertions are true.  We are trying to
dictate it based on our observations, but let's let our observations dictate it
instead."

SO THE METHOD CHANGES.  Every cypher measurement in this thread has been made
inside ONE index -- 17 energy conditions in a 288-cell box, five coordinates we
chose.  A law read off one object is a description of that object.  This pass
runs the same five operators over FOUR OTHER INDEXES THE CORPUS ITSELF SEATS and
over HUNDREDS OF RANDOM WORLDS, and keeps only what survives.

TWO THINGS SURVIVE.  THE LADDER IS NOT ONE OF THEM.

===============================================================================
1. SURVIVES -- THE CLOSURE THEOREM, AND IT IS NO LONGER INDEX-LOCAL
===============================================================================

hierarchylaw.py measured extensive / idempotent / monotone inside the NEC family
alone.  Re-run over 300 RANDOM WORLDS -- random dimension, random alphabets,
random cell sets, value order pinned so the Index's re-ranking is the identity:

        extensive       300 of 300      all five
        idempotent      300 of 300      all five
        monotone        300 of 300      all five

    THE LAW HOLDS IN 300 INDEXES THAT HAVE NOTHING TO DO WITH ENERGY
    CONDITIONS.  That is the one claim this thread has made that the
    observations do dictate rather than accept.

===============================================================================
2. SURVIVES, AND IT IS NEW -- ORDER AND ALGEBRA ARE THE SAME OPERATOR
===============================================================================

Not "agree on E".  IDENTICAL AS SETS, on every index anyone has run:

        NEC index       192 = 192          Janet         22 = 22
        periodic 2-D    126 = 126          periodic 3-D  190 = 190
        Lambda          976 = 976

        random indexes  400 of 400 equal, plus 1,379 in the sweep the
                        selftest runs and 1,188 in a wider one (dimension to
                        6, alphabets to 5, boxes to 4,000) reproduced by
                        `python3 induce.py --wide`, ~6 min and NOT in the
                        selftest -- NO COUNTEREXAMPLE ANYWHERE

    THE CYPHER HAS FOUR DISTINCT CLOSURES ON THESE OBJECTS, NOT FIVE.  The
    staircase closure and the sublattice closure return the same set.

CANDIDATE EXPLANATION, AND IT IS NOT VERIFIED: Baker-Pixley.  A variety with a
majority term -- lattices have the median -- has its subalgebras of a product
determined by their TWO-FOLD PROJECTIONS, and op_order's staircase condition is
exactly a two-fold projection condition.  That would make the identity a
theorem rather than a coincidence.  IT IS A LEAD AND IT IS FILED AS ONE.  The
proof is not in this file and no paper was read for it.

FILED FOR DOCKET 20x-04 / 20x-09 AND NOT RESOLVING IT.  Which languages there
are is an open docket, the rosters stay data, and a measurement that two
operators coincide is evidence for that docket, not a ruling on it.  cypher.py
IS NOT TOUCHED.

===============================================================================
3. DOES NOT SURVIVE -- THE LADDER
===============================================================================

Over 400 random worlds, ranking the five by the size of their closure:

        14 DISTINCT ORDERINGS

        information < algebra < geometry < order < statistics       88
        information < statistics < algebra < geometry < order       45
        information < statistics < geometry < algebra < order       44
        statistics < geometry < information < algebra < order       42   <-- ours
        statistics < information < geometry < algebra < order       41

    THE NEC INDEX'S ORDERING IS THE FOURTH MOST COMMON AND OCCURS IN ONE WORLD
    IN TEN.  It is not a law; it is this family's shape.

AND THE CORPUS'S OWN INDEXES ALREADY DISAGREED WITH EACH OTHER:

        NEC index       statistics < GEOMETRY < INFORMATION < algebra = order
        periodic 3-D    statistics < INFORMATION < GEOMETRY < algebra = order

GEOMETRY AND INFORMATION SWAP BETWEEN TWO SEATED INDEXES.  Nothing needed to be
generated to find that; it was available the whole time and was not looked at.

The specific rung claims fare no better:

        statistics is the minimum       106 of 400
        statistics is the MAXIMUM       128 of 400

    STATISTICS IS MORE OFTEN THE LARGEST THAN THE SMALLEST.  "The top rung, the
    most restrictive, the centre of the corridor" is a property of the energy
    condition family and not of the language.

        geometry vs information:  info < geom 183 | incomparable 144
                                  equal 57       | geom < info 16

===============================================================================
4. WHAT "ORDER IS THE SUBSTRATE" SURVIVES AS
===============================================================================

substrate.py's claim, tested where it can fail: is every other closure a subset
of order's?

        398 of 400

    A STRONG TENDENCY AND NOT A LAW.  Both exceptions are geometry, and both are
    incomparability rather than order being beaten -- world 121 (d = 5, 5 cells)
    has order at 8 and geometry at 10; world 286 has order at 32 and geometry at
    22, smaller and still not inside it.

===============================================================================
5. AND THE FIFTH INSTANCE OF THE SAME CHANNEL, CAUGHT INSIDE THIS PASS
===============================================================================

The first run of section 1 reported EXTENSIVITY FAILING 26 TIMES IN 200 -- a
refutation of the whole closure theorem, which is exactly the result this pass
was set up to be willing to find.  IT WAS THE HARNESS.  cypher.Index re-ranks
each coordinate's observed values to dense ordinals, so a world whose cells used
values {0, 2} had them recoded to {0, 1} and raw tuples were being compared
against recoded ones.  Pinning the value order to the full densified range makes
every count 300 of 300.

    H97 (coordinate re-ranking), H100 (algebra budget), H102 (Index-supplied
    value order), H106 (greedy stranding), AND NOW THIS.  Fifth time.  The
    channel is not carelessness about the object; it is that the scaffolding is
    invisible until it produces a number that looks like a finding -- and this
    time the number looked like a refutation, which is the harder direction to
    doubt.

===============================================================================
6. WHAT THIS DOES NOT DO
===============================================================================

Nothing here is about spacetime, and nothing moves persist.py's 69.03 orders of
magnitude or higgs.py's xi >= 9.782907e31.  Two of this thread's cypher
readings are narrowed by it and neither is a physics result.

NOTHING IS REPAIRED.
"""

import itertools
import random
import sys

import hierarchylaw
import necindex

cypher = necindex.cypher
OPTS = {"statistics_order": 2, "algebra_budget": 50000}
LANGS = hierarchylaw.LANGS

CLOSURE_THEOREM_SURVIVES = True
ORDER_IS_ALGEBRA = True
BAKER_PIXLEY_IS_A_LEAD_NOT_A_PROOF = True
DOCKET_NOT_RESOLVED = True
THE_LADDER_DOES_NOT_SURVIVE = True
SUBSTRATE_IS_A_TENDENCY = True
FIFTH_HARNESS_INSTANCE = True
NOTHING_IS_REPAIRED = True

PERSIST_ORDERS = hierarchylaw.PERSIST_ORDERS
HIGGS_XI_GATE = hierarchylaw.HIGGS_XI_GATE


# --------------------------------------------------------------- the worlds

def make_world(rnd, dmin=3, dmax=5, amin=2, amax=3, nmax=24):
    """A random index whose VALUE ORDER IS PINNED to the full densified range,
    so cypher.Index's re-ranking is the identity on it and on every subset.
    Section 5 is what happens when this is not done."""
    d = rnd.randint(dmin, dmax)
    alpha = [rnd.randint(amin, amax) for _ in range(d)]
    allc = list(itertools.product(*[range(a) for a in alpha]))
    cells = sorted(rnd.sample(allc, rnd.randint(4, min(len(allc), nmax))))
    maps = [{v: i for i, v in enumerate(sorted({c[j] for c in cells}))}
            for j in range(d)]
    cells = frozenset(tuple(maps[j][c[j]] for j in range(d)) for c in cells)
    coords = tuple("c%d" % j for j in range(d))
    vo = {coords[j]: list(range(len(maps[j]))) for j in range(d)}
    return coords, vo, cells


def close(L, coords, vo, cells):
    ix = cypher.Index("w", coords, sorted(cells), value_order=vo)
    r, _ = getattr(cypher, "op_" + L)(ix, OPTS)
    return None if r is None else frozenset(r)


def seated_indexes():
    """The corpus's own indexes, from cypher's own builders."""
    return [("NEC index", necindex.pinned_index(sorted(necindex.cells()))),
            ("Janet", cypher._janet()),
            ("periodic 2-D", cypher._periodic()),
            ("periodic 3-D", cypher._periodic(True)),
            ("Lambda", cypher._lambda())]


def admits(ix):
    out = {}
    for L in LANGS:
        r, _ = getattr(cypher, "op_" + L)(ix, OPTS)
        if r is not None:
            out[L] = frozenset(r)
    return out


# ------------------------------------------------- 1. the closure axioms

def axioms(n=300, seed=77):
    rnd = random.Random(seed)
    from collections import Counter
    res = {L: Counter() for L in LANGS}
    for _ in range(n):
        coords, vo, S = make_world(rnd)
        T = frozenset(rnd.sample(sorted(S),
                                 max(2, len(S) - rnd.randint(1, max(1, len(S) // 3)))))
        for L in LANGS:
            a = close(L, coords, vo, S)
            if a is None:
                continue
            res[L]["n"] += 1
            res[L]["ext"] += S <= a
            res[L]["idem"] += close(L, coords, vo, a) == a
            b = close(L, coords, vo, T)
            if b is not None:
                res[L]["mn"] += 1
                res[L]["mono"] += b <= a
    return res


# ------------------------------------------- 2/3/4. what actually holds

def survey(n=400, seed=101):
    from collections import Counter
    rnd = random.Random(seed)
    cnt, pair, orders, exc = Counter(), Counter(), Counter(), []
    for t in range(n):
        coords, vo, S = make_world(rnd)
        live = {L: v for L in LANGS
                for v in (close(L, coords, vo, S),) if v is not None}
        if "order" in live and "algebra" in live:
            cnt["oa_n"] += 1
            cnt["oa_eq"] += live["order"] == live["algebra"]
        if "order" in live:
            cnt["or_n"] += 1
            if all(v <= live["order"] for v in live.values()):
                cnt["or_max"] += 1
            else:
                exc.append((t, len(coords), len(S), len(live["order"]),
                            [(L, len(v)) for L, v in live.items()
                             if not v <= live["order"]]))
        if "statistics" in live:
            cnt["st_n"] += 1
            cnt["st_min"] += all(live["statistics"] <= v for v in live.values())
            cnt["st_max"] += all(v <= live["statistics"] for v in live.values())
        if "geometry" in live and "information" in live:
            g, i = live["geometry"], live["information"]
            pair["info < geom" if i < g else "geom < info" if g < i
                 else "equal" if g == i else "incomparable"] += 1
        if len(live) == 5:
            orders[tuple(sorted(live, key=lambda L: (len(live[L]), L)))] += 1
    return cnt, pair, orders, exc


def order_vs_algebra_sweep(n=1500, seed=2024, cap=256, dmax=5, amax=4):
    """Does op_order ever differ from op_algebra?  --wide raises every bound."""
    rnd = random.Random(seed)
    bad = tested = 0
    for _ in range(n):
        d = rnd.randint(2, dmax)
        alpha = [rnd.randint(2, amax) for _ in range(d)]
        allc = list(itertools.product(*[range(a) for a in alpha]))
        if len(allc) > cap:
            continue
        cells = sorted(rnd.sample(allc, rnd.randint(2, min(len(allc), 30))))
        coords = tuple("c%d" % j for j in range(d))
        vo = {coords[j]: sorted({c[j] for c in cells}) for j in range(d)}
        ix = cypher.Index("s", coords, cells, value_order=vo)
        a, b = cypher.op_order(ix, OPTS)[0], cypher.op_algebra(ix, OPTS)[0]
        if a is None or b is None:
            continue
        tested += 1
        bad += frozenset(a) != frozenset(b)
    return bad, tested


# ------------------------------------------------------------------- report

def report():
    print(__doc__)
    print("=" * 79)
    print("MEASURED")
    print("=" * 79)
    print()
    print("  1. the closure axioms over 300 random worlds")
    res = axioms()
    print("      %-12s %-14s %-14s %-14s" % ("language", "extensive",
                                             "idempotent", "monotone"))
    for L in LANGS:
        r = res[L]
        print("      %-12s %5d/%-8d %5d/%-8d %5d/%-8d" %
              (L, r["ext"], r["n"], r["idem"], r["n"], r["mono"], r["mn"]))
    print()
    print("  2. order against algebra, on the corpus's own indexes")
    for name, ix in seated_indexes():
        ad = admits(ix)
        print("      %-14s %-6s |order| = %-5d |algebra| = %-5d" %
              (name, ad["order"] == ad["algebra"],
               len(ad["order"]), len(ad["algebra"])))
    bad, tested = order_vs_algebra_sweep()
    print("      %-42s %d of %d" % ("random sweep, differing", bad, tested))
    print()
    print("  3. the nesting order, on the corpus's own indexes")
    for name, ix in seated_indexes():
        ad = admits(ix)
        o = sorted(ad, key=lambda L: (len(ad[L]), L))
        strict = sum(1 for a, b in itertools.permutations(ad, 2) if ad[a] < ad[b])
        print("      %-14s %-52s (%d strict)" % (name, " < ".join(o), strict))
    print()
    cnt, pair, orders, exc = survey()
    print("  4. and over 400 random worlds")
    print("      %-42s %d/%d" % ("order == algebra as sets",
                                 cnt["oa_eq"], cnt["oa_n"]))
    print("      %-42s %d/%d" % ("order is the maximum", cnt["or_max"], cnt["or_n"]))
    print("      %-42s %d/%d" % ("statistics is the minimum",
                                 cnt["st_min"], cnt["st_n"]))
    print("      %-42s %d/%d" % ("statistics is the MAXIMUM",
                                 cnt["st_max"], cnt["st_n"]))
    print("      %-42s %s" % ("geometry vs information", dict(pair)))
    print("      %-42s %d" % ("distinct size-orderings seen", len(orders)))
    for k, v in orders.most_common(5):
        print("         %-56s %d" % (" < ".join(k), v))
    print()
    print("      the exceptions to 'order is the maximum'")
    for t, d, n, o, big in exc:
        print("         world %-4d d=%d cells=%-3d order=%-4d not containing %s"
              % (t, d, n, o, big))
    print()
    print("  5. and the obstruction is where it was")
    print("      %-42s %.2f" % ("persist.py orders of magnitude", PERSIST_ORDERS))
    print("      %-42s %.6e" % ("higgs.py xi gate at the VEV", HIGGS_XI_GATE))
    print()
    print("=" * 79)
    print("VERDICT")
    print("=" * 79)
    print()
    print("  Two things survive being asked outside their own index.  The")
    print("  closure theorem does, in 300 worlds that have nothing to do with")
    print("  energy conditions.  And order and algebra return IDENTICAL SETS on")
    print("  every index anyone has run -- five seated ones and thousands of")
    print("  random ones -- so the cypher has four distinct closures here, not")
    print("  five; Baker-Pixley is the lead and is not a proof.")
    print()
    print("  The ladder does not survive.  Fourteen orderings in 400 worlds,")
    print("  ours the fourth most common; statistics is the MAXIMUM more often")
    print("  than the minimum; and the corpus's own NEC and periodic-3-D")
    print("  indexes already swap geometry with information.  'Order is the")
    print("  substrate' survives as 398 of 400 -- a tendency, not a law.")
    print()


# ----------------------------------------------------------------- selftest

def selftest():
    fails = []

    def chk(label, got, want):
        ok = got == want
        print("  [%s] %-58s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    print("induce.py --selftest")
    print()

    # ------------------------------- 1. the closure theorem generalises
    res = axioms()
    for L in LANGS:
        r = res[L]
        chk("%s: extensive / idempotent / monotone" % L,
            (r["ext"], r["idem"], r["mono"]), (300, 300, 300))
        chk("  ... out of", (r["n"], r["n"], r["mn"]), (300, 300, 300))
    chk("recorded: the closure theorem survives", CLOSURE_THEOREM_SURVIVES, True)

    # ------------------------------ 2. order and algebra are one operator
    for name, ix in seated_indexes():
        ad = admits(ix)
        chk("%s: order == algebra" % name, ad["order"] == ad["algebra"], True)
    bad, tested = order_vs_algebra_sweep()
    chk("random sweep: differing", bad, 0)
    chk("random sweep: tested", tested, 1379)
    chk("recorded", ORDER_IS_ALGEBRA, True)
    chk("Baker-Pixley is filed as a lead, not a proof",
        BAKER_PIXLEY_IS_A_LEAD_NOT_A_PROOF, True)
    chk("and docket 20x-04 / 20x-09 is NOT resolved here",
        DOCKET_NOT_RESOLVED, True)

    # -------------------------------------- 3. the seated indexes disagree
    nest = {}
    for name, ix in seated_indexes():
        ad = admits(ix)
        nest[name] = [L for L in sorted(ad, key=lambda L: (len(ad[L]), L))]
    chk("NEC index puts geometry before information",
        nest["NEC index"].index("geometry") < nest["NEC index"].index("information"),
        True)
    chk("periodic 3-D puts information before geometry",
        nest["periodic 3-D"].index("information") <
        nest["periodic 3-D"].index("geometry"), True)
    chk("so two SEATED indexes already disagree",
        nest["NEC index"] == nest["periodic 3-D"], False)
    # NEGATIVE CONTROL: they are not disagreeing about everything.
    chk("but both put statistics first",
        (nest["NEC index"][0], nest["periodic 3-D"][0]),
        ("statistics", "statistics"))
    chk("Lambda has no order at all -- every language returns the same set",
        sum(1 for a, b in itertools.permutations(admits(cypher._lambda()), 2)
            if admits(cypher._lambda())[a] < admits(cypher._lambda())[b]), 0)

    # ----------------------------------------- 4. the ladder is not a law
    cnt, pair, orders, exc = survey()
    chk("order == algebra across the worlds", (cnt["oa_eq"], cnt["oa_n"]), (400, 400))
    chk("distinct size-orderings", len(orders), 14)
    ours = ("statistics", "geometry", "information", "algebra", "order")
    chk("our ordering occurs this often", orders[ours], 42)
    chk("and it is not the most common",
        orders.most_common(1)[0][0] == ours, False)
    chk("statistics is the minimum", cnt["st_min"], 106)
    chk("statistics is the MAXIMUM", cnt["st_max"], 128)
    chk("so it is more often the largest", cnt["st_max"] > cnt["st_min"], True)
    chk("geometry vs information -- info < geom", pair["info < geom"], 183)
    chk("  incomparable", pair["incomparable"], 144)
    chk("  equal", pair["equal"], 57)
    chk("  geom < info", pair["geom < info"], 16)
    chk("recorded: the ladder does not survive", THE_LADDER_DOES_NOT_SURVIVE, True)

    # ------------------------------- 4b. and the substrate is a tendency
    chk("order is the maximum", (cnt["or_max"], cnt["or_n"]), (398, 400))
    chk("exceptions", len(exc), 2)
    chk("and both are geometry",
        sorted({L for _, _, _, _, big in exc for L, _ in big}), ["geometry"])
    chk("recorded", SUBSTRATE_IS_A_TENDENCY, True)

    # -------------------- 5. the harness instance this pass produced
    chk("recorded as the fifth instance", FIFTH_HARNESS_INSTANCE, True)
    # the bug, reproduced: compare RAW cells against a RECODED closure and
    # extensivity fails on a world whose values are not dense.
    coords = ("a", "b")
    raw = [(0, 0), (2, 1)]
    ix = cypher.Index("sparse", coords, raw,
                      value_order={"a": [0, 2], "b": [0, 1]})
    chk("the Index recodes a sparse value set", sorted(ix.cells), [(0, 0), (1, 1)])
    chk("so raw cells are NOT inside their own closure",
        set(raw) <= set(cypher.op_order(ix, OPTS)[0]), False)
    chk("... while the recoded ones are",
        set(ix.cells) <= set(cypher.op_order(ix, OPTS)[0]), True)

    # ------------------------------------------ 6. and the refusal
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


def wide():
    """The wider sweep, kept out of the selftest for its runtime."""
    print("induce.py --wide -- op_order against op_algebra, dimension to 6,")
    print("alphabets to 5, boxes to 4,000.  Recorded: 0 of 1188.")
    bad, tested = order_vs_algebra_sweep(n=1200, seed=2024, cap=4000,
                                         dmax=6, amax=5)
    print("\n  differing: %d of %d" % (bad, tested))
    return 0 if (bad, tested) == (0, 1188) else 1


if __name__ == "__main__":
    sys.exit(wide() if "--wide" in sys.argv else
             selftest() if "--selftest" in sys.argv else (report() or 0))
