#!/usr/bin/env python3
"""
selfindex.py -- THE CHAIN, THE FINITENESS, AND THE CYPHER RUN ON ITSELF.

M: "anything stated in a mathematical language can be translated to binary,
which means it is also cited in its current condition using logic, which is
provided by NECs, which is determined by its statistical position, which is
determined by the geometry, which is the shape of the algebra, which is the
expression of the order, which is the organization of binary ... If the index
has order, the progression through it is an algebraic expression, which means
the index has a geometric shape, which means it has statistical positions ...
this suggests the hierarchy law of mathematical languages is the only multiverse
constant."

THREE CLAIMS ARE MEASURABLE AND ALL THREE COME BACK NEGATIVE.  The fourth is not
measurable by anything here and is declined.  This file is the measurements.

===============================================================================
1. THE CHAIN HAS NO DIRECTION.  EVERY LINK IN IT COMMUTES
===============================================================================

The chain asserts a sequence of determinations:

        order -> algebra -> geometry -> statistics

For that to mean anything, applying one language then another must differ from
applying them the other way round.  alpha.py measured exactly that.  RESULT:

        order    -> algebra      COMMUTES on every seed
        algebra  -> geometry     COMMUTES on every seed
        geometry -> statistics   COMMUTES on every seed

ALL THREE OF THE CHAIN'S OWN LINKS ARE ORDER-INDEPENDENT.  And the hierarchy
does contain exactly one directed pair -- information against statistics,
disagreeing on 9 of 16 seeds -- BUT IT IS NOT A LINK IN THE CHAIN, and
information does not appear in the chain at all.

    THE ONE PLACE THE HIERARCHY HAS A DIRECTION IS THE ONE PLACE THE CHAIN DOES
    NOT GO.  A ladder whose every rung commutes is not a ladder; it is a set.

===============================================================================
2. ENCODABILITY IS NOT DECIDABILITY, AND THE CYPHER SHOWS IT ITSELF
===============================================================================

"Anything stated in a mathematical language can be translated to binary" is
nearly a theorem and it does not carry the weight placed on it.  Any FINITE
STRING over a finite alphabet encodes to binary.  That is not the same as being
DETERMINED by an operator on binary, and the gap between them has a name.

THE CYPHER EXHIBITS THE GAP IN ITS OWN SOURCE.  op_algebra carries a BUDGET:

    budget = opts.get("algebra_budget", 20000)
    if len(S) > budget:
        return None, f"sublattice closure exceeded {budget} cells; ..."

    IT RETURNS None.  IT GOES SILENT.  Measured below: the same index that
    closes at budget 200 goes SILENT at budget 10.  So the closure law is not
    universal even inside the cypher -- IT IS BOUNDED BY A PARAMETER, and past
    that parameter the language stops answering.

And every operator enumerates ix.ambient() exhaustively, which is a FINITE
product.  The energy-condition box is 288 cells; the language box below is 48.
THE LAW HOLDS ON THESE INDICES BECAUSE THEY ARE FINITE, and a law that holds
because its domain is finite is not a law about mathematics.

===============================================================================
3. THE SELF-APPLICATION, RUN.  IT DOES NOT CLOSE
===============================================================================

"If the index has order, the progression through it is an algebraic expression,
which means the index has a geometric shape ..."  THAT IS TESTABLE, and the test
is to build an index whose cells ARE the languages and hand it to the cypher.

Described by the properties the corpus itself uses to admit them -- has an
operator, returns a binary, PINNED/ADOPTED/DECLARED, declared operator-bearing
in roster 1173, and whether it speaks on the energy-condition index -- the seven
languages of roster 1173 give FIVE distinct cells, because

    ALGEBRA, GEOMETRY AND INFORMATION LAND ON THE SAME CELL, (1, 1, 1, 1, 1).

Three of the seven are indistinguishable under the corpus's own admission
criteria.  And handed to the cypher, THE SELF-INDEX DOES NOT CLOSE:

        order 5 | algebra 5 | geometry 2 | information 1 | statistics 1
        K.langclose holds: LANGUAGES DISAGREE AND E > 0.

    RUN ON ITSELF, THE HIERARCHY FAILS ITS OWN TEST IN EVERY LANGUAGE THAT CAN
    SPEAK.  Not narrowly -- the two PINNED languages are the worst, at E = 5 out
    of a 48-cell box holding 5 cells.

THE COORDINATES ARE A CHOICE AND THAT IS CARRIED, NOT HIDDEN.  A different
description of a language might close.  What is measured is that under the most
natural description -- the one the corpus uses to decide membership -- it does
not, and three languages stop being distinguishable.

===============================================================================
4. THE FOURTH CLAIM, DECLINED ONCE
===============================================================================

"The hierarchy law of mathematical languages is the only multiverse constant."

NOT MEASURABLE BY ANYTHING IN THIS TREE OR ANY TREE, and the decline does not
rest on that.  It rests on something nearer to hand: adjudicate.py, three
commits ago, ran the closure against the field equations and THE CLOSURE
CERTIFIED A FAMILY THAT EXCLUDES A PUBLISHED ENERGY CONDITION -- at E = 0, in
all five languages, wrongly.

    A CRITERION THAT CERTIFIED A FALSE FAMILY LAST WEEK IS NOT A CANDIDATE FOR A
    COSMIC CONSTANT.  That is not a philosophical objection.  It is the tree's
    own most recent measurement, and it points the other way.

WHAT SURVIVES IS WHAT ALREADY SURVIVED, AND IT IS NOT SMALL: every language in
this hierarchy is a closure operator, and membership is granted iff the language
returns a binary.  True, proved, and true BY THE ADMISSION CRITERION -- a
theorem about a construction of ours.  The distance from that to a multiverse
constant is the whole of the claim.

NOTHING IS REPAIRED.
"""

import sys

import alpha
import necindex

cypher = necindex.cypher

# The chain M states, as ordered pairs of its own links.
CHAIN = [("order", "algebra"), ("algebra", "geometry"),
         ("geometry", "statistics")]

# Each roster-1173 language by the properties the corpus uses to admit it.
#   OP  has an admission operator
#   BIN returns a binary (documentary returns a citation; analysis a magnitude)
#   STA 0 DECLARED, 1 ADOPTED, 2 PINNED
#   DEC declared operator-bearing in roster 1173
#   SPK speaks on the energy-condition index
LANG_COORDS = ("OP", "BIN", "STA", "DEC", "SPK")
LANG_VALUE_ORDER = {"OP": [0, 1], "BIN": [0, 1], "STA": [0, 1, 2],
                    "DEC": [0, 1], "SPK": [0, 1]}
LANGUAGES = {
    "order":       (1, 1, 2, 1, 1),
    "algebra":     (1, 1, 1, 1, 1),
    "analysis":    (0, 0, 0, 1, 0),
    "geometry":    (1, 1, 1, 1, 1),
    "information": (1, 1, 1, 1, 1),
    "statistics":  (1, 1, 2, 0, 1),
    "documentary": (1, 0, 2, 0, 0),
}

CHAIN_HAS_NO_DIRECTION = True
ENCODABILITY_IS_NOT_DECIDABILITY = True
SELF_INDEX_DOES_NOT_CLOSE = True
COORDINATES_ARE_A_CHOICE = True
MULTIVERSE_CLAIM_DECLINED = True
NOTHING_IS_REPAIRED = True


def chain_directions(seeds=None):
    seeds = seeds if seeds is not None else alpha.commutation_seeds()
    return {(a, b): alpha.commutes(a, b, seeds) for a, b in CHAIN}


def directed_pairs(seeds=None):
    import itertools
    seeds = seeds if seeds is not None else alpha.commutation_seeds()
    return [p for p in itertools.combinations(necindex.OPERATORS, 2)
            if alpha.commutes(p[0], p[1], seeds)]


def budget_behaviour(budgets=(200000, 200, 10)):
    ix = necindex.pinned_index(necindex.cells())
    out = {}
    for b in budgets:
        adm, note = cypher.op_algebra(ix, {"algebra_budget": b})
        out[b] = (None if adm is None else len(adm), note)
    return out


def self_index():
    cells = sorted(set(LANGUAGES.values()))
    return cypher.Index("the languages, indexed by themselves",
                        LANG_COORDS, cells, value_order=LANG_VALUE_ORDER)


def collapses():
    d = {}
    for k, v in LANGUAGES.items():
        d.setdefault(v, []).append(k)
    return {v: sorted(ks) for v, ks in d.items() if len(ks) > 1}


def self_index_E():
    ix = self_index()
    opts = {"statistics_order": 2, "algebra_budget": 200000}
    out = {}
    for n in necindex.OPERATORS:
        adm, _ = cypher.ADMISSION[n][0](ix, opts)
        out[n] = None if adm is None else len(set(adm) - set(ix.cells))
    return out


def report():
    print(__doc__)
    print("=" * 79)
    print("MEASURED")
    print("=" * 79)
    print()
    seeds = alpha.commutation_seeds()
    print("  the chain's own links")
    for (a, b), d in chain_directions(seeds).items():
        print("      %-12s -> %-12s differs on %2d of %d   %s"
              % (a, b, d, len(seeds),
                 "DIRECTED" if d else "COMMUTES -- no direction"))
    dp = directed_pairs(seeds)
    print("      %-40s %s" % ("directed pairs in the whole hierarchy", dp))
    print("      %-40s %s" % ("any of them a link in the chain",
                              any({a, b} == set(p) for a, b in CHAIN
                                  for p in dp)))
    print()
    print("  the budget: the law is bounded by a parameter")
    for b, (k, note) in sorted(budget_behaviour().items()):
        print("      budget %-8d %-12s %s"
              % (b, "SILENT" if k is None else "admits %d" % k, note[:44]))
    print()
    print("  the cypher run on its own languages")
    print("      %-40s %d" % ("roster 1173 languages", len(LANGUAGES)))
    print("      %-40s %d" % ("distinct cells they occupy",
                              len(set(LANGUAGES.values()))))
    for v, ks in collapses().items():
        print("      COLLAPSED %-18s %s" % (str(v), ", ".join(ks)))
    ix = self_index()
    print("      %-40s %d" % ("ambient box", ix.box))
    for n, e in sorted(self_index_E().items()):
        print("      %-20s E = %s" % (n, e))
    print("      it does NOT close, in any language that can speak")
    print()
    print("=" * 79)
    print("VERDICT")
    print("=" * 79)
    print()
    print("  The chain's every link commutes, so it is a set and not a ladder.")
    print("  The law is bounded by a budget and a finite box, so it is not a")
    print("  law about mathematics.  And run on its own languages the hierarchy")
    print("  fails its own test in every language that speaks.  The multiverse")
    print("  claim is declined -- on the tree's own most recent measurement,")
    print("  which is that this closure certified a false family.")
    print()


def selftest():
    fails = []

    def chk(label, got, want):
        ok = got == want
        print("  [%s] %-58s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    print("selfindex.py --selftest")
    print()
    seeds = alpha.commutation_seeds()

    # ------------------------------------------------ 1. the chain has no direction
    cd = chain_directions(seeds)
    chk("the chain has three links", len(CHAIN), 3)
    chk("every one of them commutes", sorted(set(cd.values())), [0])
    chk("recorded", CHAIN_HAS_NO_DIRECTION, True)
    dp = directed_pairs(seeds)
    chk("the hierarchy has exactly one directed pair", len(dp), 1)
    chk("and it is information against statistics", dp,
        [("information", "statistics")])
    # NEGATIVE CONTROL: a directed pair EXISTS, so commutation is a real test
    # and the chain's links failing it is a finding, not a vacuous pass.
    chk("so commuting is not vacuously true of every pair",
        alpha.commutes("information", "statistics", seeds) > 0, True)
    chk("and the directed pair is NOT in the chain",
        any({a, b} == set(p) for a, b in CHAIN for p in dp), False)

    # -------------------------------------- 2. the law is bounded by a parameter
    bb = budget_behaviour()
    chk("at a large budget algebra speaks", bb[200000][0], 192)
    chk("at 200 it still speaks", bb[200][0], 192)
    chk("at 10 it goes SILENT", bb[10][0], None)
    chk("and says so", "exceeded 10 cells" in bb[10][1], True)
    chk("recorded", ENCODABILITY_IS_NOT_DECIDABILITY, True)
    ix_ec = necindex.pinned_index(necindex.cells())
    chk("the energy-condition box is finite", ix_ec.box, 288)

    # ----------------------------------------- 3. the self-application, run
    chk("roster 1173 languages", len(LANGUAGES), 7)
    chk("distinct cells", len(set(LANGUAGES.values())), 5)
    coll = collapses()
    chk("one cell holds three languages", len(coll), 1)
    chk("and they are algebra, geometry, information",
        list(coll.values()), [["algebra", "geometry", "information"]])
    ix = self_index()
    chk("the self-index builds", ix.d, 5)
    chk("its box", ix.box, 48)
    e = self_index_E()
    chk("order does not close it", e["order"], 5)
    chk("algebra does not close it", e["algebra"], 5)
    chk("geometry does not close it", e["geometry"], 2)
    chk("information does not close it", e["information"], 1)
    chk("statistics does not close it", e["statistics"], 1)
    chk("NOT ONE language closes it", [n for n, v in e.items() if v == 0], [])
    chk("recorded", SELF_INDEX_DOES_NOT_CLOSE, True)
    # NEGATIVE CONTROL: the same operators DO close the energy-condition family
    # at 192, so failing here is a property of this index and not of the tools.
    import licensed
    chk("while the same operators close the 192 at zero",
        sorted(set(licensed.per_language(licensed.licensed()).values())), [0])
    chk("the coordinates are a choice, and it is carried",
        COORDINATES_ARE_A_CHOICE, True)

    # ------------------------------------------------ 4. the declined claim
    chk("the multiverse claim is declined", MULTIVERSE_CLAIM_DECLINED, True)
    # and the reason is a measurement, not a preference: revoke.py's family
    import revoke
    chk("the closure certified a family excluding a published condition",
        revoke.EQ86 in set(licensed.licensed()), False)
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
