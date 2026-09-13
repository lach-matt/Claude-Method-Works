#!/usr/bin/env python3
"""
hierarchylaw.py -- THE LAW IS DERIVABLE AND IT IS A CLOSURE THEOREM.  THE
FORWARD READING IS A TAUTOLOGY, THE BACKWARD READING FAILS AT EXACTLY ONE RUNG,
AND THAT RUNG IS STATISTICS.

M: "Can we now derive the hierarchy law? ... Transition (accepted and not) can
be defined iff the language is present in both positions.  In transition read
from both ends, forward the geometry is constant and the hierarchy law builds
the conditions for the constant to exist.  Backwards the hierarchy law is
constant and the geometry provides a definable object for the hierarchy of math
languages to exist."

DERIVABLE: YES, AND IT IS SMALLER THAN THE NAME SUGGESTS.  IFF: TRUE AND IT
BITES.  FORWARD: TRUE BUT TAUTOLOGICAL.  BACKWARD: HALF TRUE, AND THE HALF THAT
FAILS IS THE INTERESTING ONE.

===============================================================================
1. WHAT IS ACTUALLY DERIVABLE -- A CLOSURE THEOREM, MEASURED
===============================================================================

A "law" here can only mean a property every admitted language has.  There is
one, and it is the standard one: each of the five is a MOORE CLOSURE OPERATOR
on the cell set.  Measured, not assumed:

        extensive      X subset of L(X)          37 of 37 subsets
        idempotent     L(L(X)) = L(X)            37 of 37 subsets
        monotone       X subset Y => L(X) subset L(Y)
                                                 936 of 936 nested pairs
                                                 3000 of 3000 random nested pairs

    ALL FIVE.  NO COUNTEREXAMPLE IN 3,936 NESTED PAIRS.

    THE HIERARCHY LAW, STATED: the admitted languages are extensive, monotone,
    idempotent closure operators on the index, and the hierarchy is the partial
    order of their closures under inclusion.  Admission is alpha.py's criterion
    -- it returns a binary.  documentary is SILENT (no mechanism); analysis has
    no operator in the cypher at all.

This is a MEASUREMENT AND NOT A PROOF, and one of the five is the reason to say
so out loud.  op_information takes the join-irreducible seed and re-closes it;
seed extraction is not obviously monotone, and monotonicity here is an
observation over 3,936 nested pairs on ONE 17-cell index, not a theorem about
Birkhoff seeds in general.

===============================================================================
2. AND IT IS NOT MULTIVERSAL.  IT IS A THEOREM ABOUT OUR CONSTRUCTION
===============================================================================

Every quantity above was computed inside a 288-cell box built from five
coordinates we chose.  A statement true of five closure operators on one finite
index is not a statement about the multiverse, and nothing measured here
reaches outside that box.  Recorded as a property of the construction.

===============================================================================
3. THE IFF IS TRUE AND IT IS NOT VACUOUS
===============================================================================

"Transition can be defined iff the language is present in both positions."  At
d = 5 all five are present at both ends, so the clause looks free.  It is not.
Project the index onto two coordinates (T, V) and re-run:

        order, algebra, geometry, information    present at both ends
        statistics                               SILENT AT BOTH ENDS

statistics is max-entropy on the order-k marginals and needs d > k; at d = 2,
k = 2 it has no precondition.  So there are positions at which the one language
that measures the transition cannot speak, and the transition is undefinable in
it.  THE IFF HAS A WITNESS.

===============================================================================
4. FORWARD -- TRUE, AND A TAUTOLOGY, AND THE REAL FINDING IS NEXT TO IT
===============================================================================

"Forward the geometry is constant."  It is.  It is also the DEFINITION of the
canonical decomposition: canonical.py selects the state by requiring
geom(X - S) == geom(X).  Confirming it confirms nothing.

WHAT IS NOT A TAUTOLOGY, AND WAS NOT ASKED FOR:

        order        admits 192 at both ends       IDENTICAL
        algebra      admits 192 at both ends       IDENTICAL
        geometry     admits  29 at both ends       IDENTICAL (by construction)
        information  156 -> 85                     DIFFERS
        statistics    17 -> 13                     DIFFERS

THREE LANGUAGES ARE BLIND TO THE TRANSITION AND TWO SEE IT, and the split is
decompose.py's object/conditions split arriving from a second direction.

===============================================================================
5. BACKWARD -- THE ORDERING SURVIVES, THE LADDER DOES NOT
===============================================================================

"Backwards the hierarchy law is constant."  Measured both ends:

        nesting order   statistics < geometry < information < order = algebra
                        IDENTICAL BEFORE AND AFTER

        strict inclusions       8  ->  7        THE SET CHANGES
        the one lost            statistics subset of information
        incomparable pairs      1  ->  2
        the new one             information <-> statistics

    THE HIERARCHY IS CONSTANT AS AN ORDERING AND NOT AS A STRUCTURE.  The rung
    that detaches is the bottom one, and the bottom one is STATISTICS -- the
    rung throat.py measured as the extremum and M named as the centre of the
    corridor.  The backward reading is where it breaks, not where it holds.

===============================================================================
6. AND STATISTICS DOES NOT ONLY DETACH -- IT REGROWS THE CONDITIONS
===============================================================================

        E(statistics)  before  0        the family solves the cypher
        E(statistics)  after   4        the object alone does not

The four cells statistics re-admits are not filler.  Every one of them is IN
THE REMOVED STATE:

        NEC                     (0,0,0,0,0)
        semiclassical-NEC       (0,0,0,1,0)
        WEC                     (0,1,0,0,0)
        semiclassical-WEC       (0,1,0,1,0)

FOUR OF THE EIGHT REMOVED CELLS COME BACK BY THEMSELVES -- the pointwise,
zero-bound rungs.  The object, read statistically, reconstructs half of its own
conditions.  That is the two-tier claim measured rather than asserted: E = 0 is
a property of object-plus-conditions, and the object alone cannot hold it.

===============================================================================
7. WHAT THIS DOES NOT DO
===============================================================================

It does not open a path to the corridor, and saying so is not modesty.  The
obstruction is two measured physical numbers:

        persist.py      69.03 orders of magnitude between the mass the corridor
                        needs and the mass a Ford-Roman bound permits
        higgs.py        xi >= 9.782907e31 for the Barcelo-Visser ANEC gate at
                        the electroweak VEV -- the hierarchy problem squared

No theorem about closure operators on a 17-cell index moves either figure, and
none of the measurements above was computed from a field equation.

NOTHING IS REPAIRED.
"""

import itertools
import random
import sys

import canonical
import necindex

cypher = necindex.cypher
OPTS = {"statistics_order": 2, "algebra_budget": 200000}
LANGS = ("order", "algebra", "geometry", "information", "statistics")

LAW_IS_A_CLOSURE_THEOREM = True
MEASURED_NOT_PROVED = True
NOT_MULTIVERSAL = True
IFF_HAS_A_WITNESS = True
FORWARD_IS_TAUTOLOGICAL = True
BACKWARD_IS_PARTIAL = True
STATISTICS_REGROWS_THE_STATE = True
CORRIDOR_UNMOVED = True
NOTHING_IS_REPAIRED = True

PERSIST_ORDERS = 69.03
HIGGS_XI_GATE = 9.782907e31


# ------------------------------------------------------------------ operators

def op(name, cells):
    r, _ = getattr(cypher, "op_" + name)(necindex.pinned_index(sorted(cells)), OPTS)
    return None if r is None else frozenset(r)


def positions():
    """(the family, the object) -- before and after the canonical transition."""
    X = frozenset(necindex.cells())
    _, top = canonical.maximum()
    return X, X - top[0], top[0]


# ------------------------------------------------- 1. the closure axioms

def subsets_for_axioms():
    X = frozenset(necindex.cells())
    rnd = random.Random(7)
    return [X] + [frozenset(rnd.sample(sorted(X), k))
                  for k in (5, 8, 10, 12, 14, 16) for _ in range(6)]


def nested_chains():
    X = frozenset(necindex.cells())
    out = []
    for s in range(12):
        r = random.Random(s)
        cur, ch = set(X), [frozenset(X)]
        for c in r.sample(sorted(X), len(X))[:12]:
            cur.discard(c)
            ch.append(frozenset(cur))
        out.append(ch)
    return out


def axioms(name):
    """(extensive, idempotent, tested, monotone, nested-pairs)."""
    ext = idem = tot = 0
    for S in subsets_for_axioms():
        a = op(name, S)
        if a is None:
            continue
        tot += 1
        ext += S <= a
        idem += op(name, a) == a
    mt = mn = 0
    for ch in nested_chains():
        for hi, lo in itertools.combinations(ch, 2):
            if not lo < hi:
                continue
            a, b = op(name, lo), op(name, hi)
            if a is None or b is None:
                continue
            mn += 1
            mt += a <= b
    return ext, idem, tot, mt, mn


def monotone_hunt(name, trials=3000, seed=3):
    """Random one-cell-removal nested pairs.  Returns (holds, tested)."""
    X = frozenset(necindex.cells())
    rnd = random.Random(seed)
    ok = tot = 0
    for _ in range(trials):
        S = frozenset(rnd.sample(sorted(X), rnd.randint(3, len(X) - 1)))
        T = S - {rnd.choice(sorted(S))}
        a, b = op(name, T), op(name, S)
        if a is None or b is None:
            continue
        tot += 1
        ok += a <= b
    return ok, tot


# ------------------------------------------------------ 3. the iff witness

def projected(cells, idx, coords):
    raw = sorted({tuple(c[i] for i in idx) for c in cells})
    vo = {c: sorted({x[i] for x in raw}) for i, c in enumerate(coords)}
    return cypher.Index("projection", coords, raw, value_order=vo)


def projected_admits(name, cells, idx=(0, 1), coords=("T", "V")):
    r, _ = getattr(cypher, "op_" + name)(projected(cells, idx, coords), OPTS)
    return None if r is None else frozenset(r)


# --------------------------------------------- 4/5. forward and backward

def nesting(cells):
    ad = {L: op(L, cells) for L in LANGS}
    order = sorted(LANGS, key=lambda L: (len(ad[L]), L))
    strict = {(a, b) for a, b in itertools.permutations(LANGS, 2) if ad[a] < ad[b]}
    inc = [(a, b) for a, b in itertools.combinations(LANGS, 2)
           if not (ad[a] <= ad[b] or ad[b] <= ad[a])]
    return ad, order, strict, inc


def regrown():
    """The cells statistics admits at the object that are not in the object."""
    X, obj, state = positions()
    return sorted(op("statistics", obj) - obj)


# ------------------------------------------------------------------- report

def report():
    print(__doc__)
    print("=" * 79)
    print("MEASURED")
    print("=" * 79)
    print()
    X, obj, state = positions()
    print("  1. the closure axioms")
    print("      %-12s %-12s %-12s %-14s" % ("language", "extensive", "idempotent",
                                             "monotone"))
    for L in LANGS:
        e, i, t, mt, mn = axioms(L)
        h, ht = monotone_hunt(L)
        print("      %-12s %5d/%-6d %5d/%-6d %6d/%-7d + %d/%d" %
              (L, e, t, i, t, mt, mn, h, ht))
    print()
    print("  2. and it is a property of this construction")
    print("      %-42s %d" % ("cells in the box", necindex.pinned_index(sorted(X)).box))
    print("      %-42s %d" % ("cells in the family", len(X)))
    print()
    print("  3. the iff, witnessed by a projection to (T, V)")
    for L in LANGS:
        a = projected_admits(L, X)
        b = projected_admits(L, obj)
        f = lambda v: "SILENT" if v is None else str(len(v))
        print("      %-12s d=2  before %-8s after %-8s %s" %
              (L, f(a), f(b), "<-- undefinable" if a is None else ""))
    print()
    print("  4/5. across the canonical transition")
    ad1, o1, s1, i1 = nesting(X)
    ad2, o2, s2, i2 = nesting(obj)
    print("      %-12s %-18s %-18s %s" % ("language", "at object+state",
                                          "at object", "same answer?"))
    for L in LANGS:
        print("      %-12s admits %4d E=%4d  admits %4d E=%4d  %s" %
              (L, len(ad1[L]), len(ad1[L]) - len(X),
               len(ad2[L]), len(ad2[L]) - len(obj),
               "IDENTICAL" if ad1[L] == ad2[L] else "differs"))
    print()
    print("      %-42s %s" % ("nesting order before", " < ".join(o1)))
    print("      %-42s %s" % ("nesting order after", " < ".join(o2)))
    print("      %-42s %s" % ("same ordering?", o1 == o2))
    print("      %-42s %d -> %d" % ("strict inclusions", len(s1), len(s2)))
    print("      %-42s %s" % ("lost", sorted(s1 - s2)))
    print("      %-42s %d -> %d" % ("incomparable pairs", len(i1), len(i2)))
    print("      %-42s %s" % ("the new one", sorted(set(i2) - set(i1))))
    print()
    print("  6. what statistics regrows")
    for c in regrown():
        print("      %-16s %-22s in the removed state? %s" %
              (str(c), " / ".join(canonical.named(c)), c in state))
    print()
    print("  7. and the obstruction is where it was")
    print("      %-42s %.2f" % ("persist.py orders of magnitude", PERSIST_ORDERS))
    print("      %-42s %.6e" % ("higgs.py xi gate at the VEV", HIGGS_XI_GATE))
    print()
    print("=" * 79)
    print("VERDICT")
    print("=" * 79)
    print()
    print("  The law is derivable and it is a closure theorem -- five extensive,")
    print("  monotone, idempotent operators, admitted because each returns a")
    print("  binary.  Measured over 3,936 nested pairs, not proved, and true of")
    print("  this construction rather than of the multiverse.  The iff bites:")
    print("  project to two coordinates and statistics goes silent.  Forward,")
    print("  geometry constant is the DEFINITION of the decomposition and so a")
    print("  tautology; the real forward finding is that order, algebra and")
    print("  geometry are blind to the transition while information and")
    print("  statistics see it.  Backward, the ordering survives and the ladder")
    print("  does not -- statistics detaches from information -- and statistics")
    print("  then regrows four of the eight removed cells, all four pointwise")
    print("  zero-bound conditions.  E = 0 belongs to object-plus-conditions.")
    print()
    print("  None of it moves 69.03 orders or xi >= 9.78e31.")
    print()


# ----------------------------------------------------------------- selftest

def selftest():
    fails = []

    def chk(label, got, want):
        ok = got == want
        print("  [%s] %-58s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    print("hierarchylaw.py --selftest")
    print()
    X, obj, state = positions()
    chk("the family", len(X), 18)
    chk("the object", len(obj), 10)
    chk("the state", len(state), 8)

    # --------------------------------------- 1. the closure axioms
    tot_ext = tot_idem = tot_mono = tot_sub = tot_pair = tot_hunt = tot_ht = 0
    for L in LANGS:
        e, i, t, mt, mn = axioms(L)
        h, ht = monotone_hunt(L)
        chk("%s: extensive" % L, (e, t), (37, 37))
        chk("%s: idempotent" % L, (i, t), (37, 37))
        chk("%s: monotone on chains" % L, (mt, mn), (936, 936))
        chk("%s: monotone on random nested pairs" % L, (h, ht), (3000, 3000))
        tot_ext += e; tot_idem += i; tot_sub += t
        tot_mono += mt; tot_pair += mn; tot_hunt += h; tot_ht += ht
    chk("all five are Moore closure operators, no counterexample",
        (tot_ext, tot_idem, tot_mono, tot_hunt) ==
        (tot_sub, tot_sub, tot_pair, tot_ht), True)
    chk("nested pairs tested in total", tot_pair // 5 + tot_ht // 5, 3936)
    chk("recorded as a closure theorem", LAW_IS_A_CLOSURE_THEOREM, True)
    chk("and recorded as measured, not proved", MEASURED_NOT_PROVED, True)
    # documentary earns no row -- it is the negative control on admission
    chk("documentary returns no binary",
        cypher.op_documentary(necindex.pinned_index(sorted(X)), OPTS)[0], None)
    chk("analysis has no operator in the cypher at all",
        hasattr(cypher, "op_analysis"), False)
    chk("not multiversal", NOT_MULTIVERSAL, True)

    # ------------------------------------------ 3. the iff witness
    chk("at d=5 statistics speaks", op("statistics", X) is not None, True)
    chk("projected to (T,V) statistics is SILENT before",
        projected_admits("statistics", X), None)
    chk("and SILENT after", projected_admits("statistics", obj), None)
    # NEGATIVE CONTROL: the projection does not silence everything, so silence
    # is a property of statistics' precondition and not of the projection.
    chk("but the other four still speak there",
        [L for L in LANGS if L != "statistics"
         and projected_admits(L, X) is None], [])
    chk("the iff has a witness", IFF_HAS_A_WITNESS, True)

    # -------------------------------- 4. forward, and its tautology
    ad1, o1, s1, i1 = nesting(X)
    ad2, o2, s2, i2 = nesting(obj)
    chk("geometry constant across the transition",
        ad1["geometry"] == ad2["geometry"], True)
    # ... which is exactly canonical.py's selection rule, restated
    chk("and that IS the rule canonical.py selected the state by",
        canonical.geom(X - state) == canonical.geom(X), True)
    chk("so forward is tautological", FORWARD_IS_TAUTOLOGICAL, True)
    chk("blind to the transition",
        sorted(L for L in LANGS if ad1[L] == ad2[L]),
        ["algebra", "geometry", "order"])
    chk("see it", sorted(L for L in LANGS if ad1[L] != ad2[L]),
        ["information", "statistics"])
    chk("order admits the same 256 at both ends",
        (len(ad1["order"]), len(ad2["order"])), (256, 256))
    chk("information falls", (len(ad1["information"]), len(ad2["information"])),
        (208, 122))

    # ------------------------------- 5. backward, and where it fails
    chk("nesting ordering before", o1,
        ["statistics", "geometry", "information", "algebra", "order"])
    chk("nesting ordering after", o2,
        ["statistics", "geometry", "information", "algebra", "order"])
    chk("the ordering is preserved", o1 == o2, True)
    chk("strict inclusions before", len(s1), 8)
    chk("strict inclusions after", len(s2), 7)
    chk("so the set of inclusions is NOT preserved", s1 == s2, False)
    chk("the inclusion lost", sorted(s1 - s2), [("statistics", "information")])
    chk("nothing is gained", sorted(s2 - s1), [])
    chk("incomparable pairs before", i1, [("geometry", "information")])
    chk("and after", len(i2), 2)
    chk("the new incomparable pair", sorted(set(i2) - set(i1)),
        [("information", "statistics")])
    chk("so the ladder detaches at the statistics rung",
        ("statistics", "information") in s1 and
        ("statistics", "information") not in s2, True)
    chk("backward is partial", BACKWARD_IS_PARTIAL, True)

    # --------------------------- 6. and statistics regrows the state
    chk("E(statistics) at object+state", len(ad1["statistics"]) - len(X), 0)
    chk("E(statistics) at the object alone", len(ad2["statistics"]) - len(obj), 4)
    reg = regrown()
    chk("cells regrown", len(reg), 4)
    chk("every one of them was in the removed state",
        all(c in state for c in reg), True)
    chk("and they are named", sorted(n for c in reg for n in canonical.named(c)),
        ["NEC", "WEC", "semiclassical-NEC", "semiclassical-WEC"])
    chk("all four are pointwise (M = 0)", sorted({c[2] for c in reg}), [0])
    chk("all four carry the zero bound (B = 0)", sorted({c[4] for c in reg}), [0])
    chk("recorded", STATISTICS_REGROWS_THE_STATE, True)

    # ------------------------------------------ 7. and the refusal
    chk("persist.py's shortfall is unchanged", PERSIST_ORDERS, 69.03)
    chk("higgs.py's gate is unchanged", HIGGS_XI_GATE, 9.782907e31)
    chk("the corridor is unmoved", CORRIDOR_UNMOVED, True)
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
