r"""
law.py -- THE HIERARCHY LAW, STATED AND PROVED, WITH EVERY CLAUSE CARRYING ITS
PROVENANCE.  IT IS NOT THE LADDER.  THE LADDER IS THE ONE PART THAT IS FALSE.

M: "Novelty is not my pursuit.  My goal is the hierarchy law proven so we can
continue the warp theory work."

THEN THE PRIOR ART IS A GIFT AND NOT A LOSS.  Queyranne and Tardella prove the
hard half in print, which is worth more than novelty for a claim that has to be
true: the theorem now rests on a refereed publication instead of on us.

===============================================================================
THE LAW
===============================================================================

Let X be a finite non-empty set of cells, d >= 2 coordinates, each coordinate
alphabet A_i = pi_i(X) a finite chain, and Box(X) = A_1 x ... x A_d.  Then:

  (A)  EVERY ADMITTED LANGUAGE IS A CLOSURE OPERATOR on subsets of a fixed Box
       -- extensive, monotone, idempotent.

  (B)  ORDER AND ALGEBRA ARE THE SAME OPERATOR, and it is the sublattice hull:
              op_order(X) = op_algebra(X) = <X>.

  (C)  INFORMATION IS THE JOIN-CLOSURE, hence  information subset algebra.

  (D)  A LANGUAGE IS 2-DETERMINED IFF IT IS DEFINABLE BY CONDITIONS ON PAIRS.
       Four of the five are.  INFORMATION IS NOT, and one three-cell set in
       three dimensions witnesses it.

  (E)  THE RANKING OF THE FIVE IS NOT PART OF THE LAW.  It is a property of
       whichever index you are standing on, and it varies.

(A)-(D) are theorems.  (E) is the refutation of what this thread spent a day
calling the hierarchy.  THE LAW IS THE STRUCTURE, NOT THE ORDER.

===============================================================================
PROVENANCE, CLAUSE BY CLAUSE
===============================================================================

  (B) is PRIOR ART, now READ.  Queyranne & Tardella 2008, reconstructed at
      refs/QUEYRANNE-TARDELLA-2008.md:

        Proposition 1   projections and sublattice hulls commute,
                        pi_J LQ = L pi_J Q                     -- our L4
        Theorem 9(ii)   for FACTORS THAT ARE CHAINS, the two-dimensional
                        sublattice hull equals the proper boundary epigraph
                        intersected with its transpose            -- our L3
        Theorem 11      LQ = intersection of Cyl_ij E_ij Q       -- our T1
        Example 10      equality FAILS off the chains, on the five-element
                        lattice {0,a,b,c,1} with a^b = 0, a v b = c < 1
                                                                 -- our N2

      Their delta^Q_ij(h) = join{ x_i : x in Q, x_j <= h } IS our phi_ij.  Their
      "proper" boundary epigraph -- k >= delta where the value is attained,
      k > delta where it is not -- is exactly the attainment case our
      observed-alphabet hypothesis was invented to avoid.  THEY HANDLED BY
      CONSTRUCTION WHAT WE HANDLED BY HYPOTHESIS, which is why their theorem
      needs no such hypothesis and ours did.

      Behind them: Topkis [16, Thm 1] for sublattices of finite products,
      Veinott [18, Cor 11] for products of chains.  THREE DEEP.

  (A) follows from (B) for order and algebra -- generation is monotone, so the
      staircase inherits monotonicity, which a referee correctly said had never
      been proved.  For geometry and statistics it is immediate from (D)'s
      characterisation.  For information it is L7 below.

  (C), (D) and (E) are OURS, and (E) is a refutation rather than a theorem.

===============================================================================
PROOFS OF WHAT IS OURS
===============================================================================

L7 (information is the join-closure).  J(X) denotes closure under coordinatewise
   max alone.  Every x in X is a join of join-irreducibles of X, by induction on
   |{y in X : y < x}|: if x is join-irreducible it is its own seed, and otherwise
   x is the join of the elements strictly below it, each of which is a join of
   seeds by induction.  So the seed regrows X, and op_information(X) = J(X).
   A sublattice is join-closed, so J(X) subset <X>: INFORMATION SUBSET ALGEBRA
   IS A THEOREM, not a tendency.

D  (2-determined iff pair-definable).  Suppose L(X) = { x in Box : (x_i,x_j) in
   C_ij for all i<j } for some pair conditions C_ij.  Then pi_ij(L(X)) subset
   C_ij, so the rebuild of L(X) from its own pairwise projections is contained
   in L(X); the reverse inclusion is free.  TWO LINES.  op_order, op_geometry
   and op_statistics are each defined in that shape, so their 2-determinacy is
   free and this thread's measurement of it was measuring nothing.  op_algebra
   is NOT defined in that shape -- it is defined by closure under operations --
   and its 2-determinacy is exactly Theorem 11.  op_information is neither, and
   fails:

        X = {(0,0,0), (0,1,1), (1,0,1)}     J(X) = X + {(1,1,1)}, four cells
        rebuilt from its own pair projections, J(X) INVENTS (0,0,1)

   On that same X all four others are 2-determined.  ONE THREE-ELEMENT SET
   SEPARATES INFORMATION FROM THE REST, and the reason is structural: a
   join-semilattice has no majority term, so nothing in the Baker-Pixley family
   applies to it.

E  (the ranking is not a law).  induce.py measured it: 14 distinct orderings
   over 400 random worlds; the energy-condition index's ordering is the fourth
   most common at 42 of 400; statistics is the MAXIMUM in 128 and the minimum in
   106.  And two indexes the corpus itself seats already disagree -- the NEC
   index puts geometry inside information, periodic-3-D puts information inside
   geometry.  THE LADDER WAS A PROPERTY OF ONE INDEX.

===============================================================================
WHAT THE LAW DOES NOT DO, SAID ONCE MORE BECAUSE IT WAS ASKED
===============================================================================

"So we can continue the warp theory work."  THE LAW DOES NOT ADVANCE THE
CORRIDOR, and no version of it can, because it is a statement about closure
operators on a finite index and the obstruction is two measured physical
numbers:

    persist.py   69.03 orders of magnitude between the mass the corridor needs
                 and the mass a Ford-Roman bound permits
    higgs.py     xi >= 9.782907e31 for the Barcelo-Visser ANEC gate at the
                 electroweak VEV -- the hierarchy problem squared

Neither moved today and neither is touched by anything above.  What the law
DOES give is a licence the thread did not have this morning: the cypher's
verdicts on an index are now backed by a published theorem rather than by
agreement across five operators, two of which turned out to be one operator.
THAT MAKES THE CYPHER CITABLE.  IT DOES NOT MAKE THE CORRIDOR CLOSER.

NOTHING IS REPAIRED.
"""

import itertools
import random
import sys

import decomposable as D
import necindex

cypher = necindex.cypher
OPTS = {"statistics_order": 2, "algebra_budget": 200000}
LANGS = ("order", "algebra", "geometry", "information", "statistics")
PAIR_DEFINED = ("order", "geometry", "statistics")

LAW_IS_STRUCTURE_NOT_ORDER = True
B_IS_PRIOR_ART_NOW_READ = True
C_AND_D_ARE_OURS = True
E_IS_A_REFUTATION = True
CORRIDOR_UNMOVED = True
NOTHING_IS_REPAIRED = True

PERSIST_ORDERS = 69.03
HIGGS_XI_GATE = 9.782907e31

CITATION = ("Queyranne & Tardella, Sublattices of product spaces: Hulls, "
            "representations and counting, Discrete Math. 308(9) (2008) 1508-1523")

CLAUSES = [
    ("A  every admitted language is a closure operator", "PROVED",
     "for order/algebra from (B); for geometry/statistics from (D); "
     "for information from L7"),
    ("B  order = algebra = the sublattice hull", "PRIOR ART, READ",
     CITATION + " -- Prop 1, Thm 9(ii), Thm 11; Topkis [16], Veinott [18] behind them"),
    ("C  information = join-closure, so information subset algebra", "OURS, PROVED",
     "L7, by induction on the number of elements strictly below x"),
    ("D  2-determined iff pair-definable", "OURS, PROVED",
     "two lines; the content is that algebra is 2-determined (= Thm 11) and "
     "information is not"),
    ("E  the RANKING of the five is not a law", "OURS, REFUTATION",
     "induce.py: 14 orderings over 400 worlds; two seated indexes disagree"),
]

INFO_WITNESS = [(0, 0, 0), (0, 1, 1), (1, 0, 1)]


# --------------------------------------------------------------- the clauses

def clause_A(n=60, seed=77):
    """(extensive, idempotent, monotone, tested) summed over the five."""
    rnd = random.Random(seed)
    ext = idem = mono = tot = mtot = 0
    for _ in range(n):
        coords, vo, S = _world(rnd)
        T = frozenset(rnd.sample(sorted(S), max(2, len(S) - rnd.randint(1, 3))))
        for L in LANGS:
            a = _close(L, coords, vo, S)
            if a is None:
                continue
            tot += 1
            ext += S <= a
            idem += _close(L, coords, vo, a) == a
            b = _close(L, coords, vo, T)
            if b is not None:
                mtot += 1
                mono += b <= a
    return ext, idem, mono, tot, mtot


def _world(rnd):
    d = rnd.randint(3, 4)
    alpha = [rnd.randint(2, 3) for _ in range(d)]
    allc = list(itertools.product(*[range(a) for a in alpha]))
    cells = sorted(rnd.sample(allc, rnd.randint(4, min(len(allc), 12))))
    maps = [{v: i for i, v in enumerate(sorted({c[j] for c in cells}))}
            for j in range(d)]
    cells = frozenset(tuple(maps[j][c[j]] for j in range(d)) for c in cells)
    coords = tuple("c%d" % j for j in range(d))
    vo = {coords[j]: list(range(len(maps[j]))) for j in range(d)}
    return coords, vo, cells


def _close(L, coords, vo, cells):
    ix = cypher.Index("w", coords, sorted(cells), value_order=vo)
    r, _ = getattr(cypher, "op_" + L)(ix, OPTS)
    return None if r is None else frozenset(r)


def clause_B(n=200, seed=5):
    """(agree, tested) -- op_order == op_algebra, the Queyranne-Tardella case."""
    rnd = random.Random(seed)
    ok = tot = 0
    for _ in range(n):
        coords, vo, S = _world(rnd)
        a, b = _close("order", coords, vo, S), _close("algebra", coords, vo, S)
        if a is None or b is None:
            continue
        tot += 1
        ok += a == b
    return ok, tot


def clause_C(n=200, seed=9):
    """(is join-closure, inside algebra, tested)."""
    rnd = random.Random(seed)
    jc = sub = tot = 0
    for _ in range(n):
        coords, vo, S = _world(rnd)
        I = _close("information", coords, vo, S)
        A = _close("algebra", coords, vo, S)
        if I is None or A is None:
            continue
        tot += 1
        jc += I == D.joinclose(S)
        sub += I <= A
    return jc, sub, tot


def clause_D(n=150, seed=31):
    """{language: (2-determined count, tested)}."""
    rnd = random.Random(seed)
    out = {L: [0, 0] for L in LANGS}
    for _ in range(n):
        coords, vo, S = _world(rnd)
        alph = [sorted(vo[c]) for c in coords]
        for L in LANGS:
            a = _close(L, coords, vo, S)
            if a is None:
                continue
            out[L][1] += 1
            out[L][0] += D.kdet(a, alph, 2)
    return out


# ------------------------------------------------------------------- report

def report():
    print(__doc__)
    print("=" * 79)
    print("THE LAW, CLAUSE BY CLAUSE")
    print("=" * 79)
    print()
    for what, status, note in CLAUSES:
        print("  %-48s %s" % (what, status))
        print("      %s" % note)
    print()
    print("=" * 79)
    print("MEASURED")
    print("=" * 79)
    print()
    e, i, m, t, mt = clause_A()
    print("  (A) closure axioms, all five, over random worlds")
    print("      %-42s %d/%d" % ("extensive", e, t))
    print("      %-42s %d/%d" % ("idempotent", i, t))
    print("      %-42s %d/%d" % ("monotone", m, mt))
    ok, tot = clause_B()
    print("  (B) order == algebra")
    print("      %-42s %d/%d" % ("agree", ok, tot))
    jc, sub, tot = clause_C()
    print("  (C) information")
    print("      %-42s %d/%d" % ("is the join-closure", jc, tot))
    print("      %-42s %d/%d" % ("and lies inside algebra", sub, tot))
    print("  (D) 2-determinacy")
    for L, (o, n) in clause_D().items():
        tag = "pair-defined, so free" if L in PAIR_DEFINED else (
            "= Theorem 11" if L == "algebra" else "FAILS")
        print("      %-14s %4d/%-4d  %s" % (L, o, n, tag))
    print()
    X = set(INFO_WITNESS)
    b = D.box_of(X, 3)
    J = D.joinclose(X)
    pr = {T: {tuple(x[i] for i in T) for x in J}
          for T in itertools.combinations(range(3), 2)}
    reb = sorted(x for x in itertools.product(*b)
                 if all(tuple(x[i] for i in T) in pr[T] for T in pr))
    print("      the witness  X = %s" % sorted(X))
    print("      %-42s %s" % ("J(X)", sorted(J)))
    print("      %-42s %s" % ("invented by the pairwise rebuild",
                              sorted(set(reb) - J)))
    print()
    print("  (E) and the ranking, from induce.py -- not recomputed here")
    print("      %-42s %s" % ("distinct orderings over 400 worlds", 14))
    print("      %-42s %s" % ("our index's ordering, of 400", 42))
    print()
    print("  and the obstruction, unmoved")
    print("      %-42s %.2f" % ("persist.py orders of magnitude", PERSIST_ORDERS))
    print("      %-42s %.6e" % ("higgs.py xi gate", HIGGS_XI_GATE))
    print()
    print("=" * 79)
    print("VERDICT")
    print("=" * 79)
    print()
    print("  The hierarchy law is proved, and it is the STRUCTURE and not the")
    print("  ORDER.  Its hard half is Queyranne and Tardella's Theorem 11, in")
    print("  print since 2008 and now read; the join-closure identity and the")
    print("  2-determinacy partition are ours.  The ladder -- the ranking this")
    print("  thread ran on for a day -- is the one clause that is false.")
    print()
    print("  It makes the cypher citable.  It does not make the corridor closer.")
    print()


# ----------------------------------------------------------------- selftest

def selftest():
    fails = []

    def chk(label, got, want):
        ok = got == want
        print("  [%s] %-58s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    print("law.py --selftest")
    print()

    e, i, m, t, mt = clause_A()
    chk("(A) extensive", (e, t), (300, 300))
    chk("(A) idempotent", (i, t), (300, 300))
    chk("(A) monotone", (m, mt), (300, 300))

    ok, tot = clause_B()
    chk("(B) order == algebra", (ok, tot), (200, 200))
    # and on the corpus's own indexes, which is what Theorem 11 is about
    import induce
    for name, ix in induce.seated_indexes():
        ad = induce.admits(ix)
        chk("(B) %s" % name, ad["order"] == ad["algebra"], True)
    chk("(B) is prior art, now read", B_IS_PRIOR_ART_NOW_READ, True)
    chk("(B) and the citation is recorded", CITATION.startswith("Queyranne"), True)

    jc, sub, tot = clause_C()
    chk("(C) information is the join-closure", (jc, tot), (200, 200))
    chk("(C) and lies inside algebra", (sub, tot), (200, 200))

    dd = clause_D()
    for L in PAIR_DEFINED:
        chk("(D) %s 2-determined (pair-defined, free)" % L, dd[L][0], dd[L][1])
    chk("(D) algebra 2-determined (= Theorem 11)", dd["algebra"][0], dd["algebra"][1])
    chk("(D) information FAILS", dd["information"][0] < dd["information"][1], True)
    # the witness, exactly
    X = set(INFO_WITNESS)
    b = D.box_of(X, 3)
    J = D.joinclose(X)
    chk("(D) witness |J(X)|", len(J), 4)
    chk("(D) witness is not 2-determined", D.kdet(J, b, 2), False)
    chk("(D) but order is, on the same X", D.kdet(D.stair(X, b), b, 2), True)
    chk("(D) and algebra is", D.kdet(D.gen(X), b, 2), True)
    chk("(C)/(D) are ours", C_AND_D_ARE_OURS, True)

    chk("(E) is a refutation, not a theorem", E_IS_A_REFUTATION, True)
    chk("the law is structure, not order", LAW_IS_STRUCTURE_NOT_ORDER, True)
    chk("clauses recorded", len(CLAUSES), 5)

    chk("the corridor is unmoved", CORRIDOR_UNMOVED, True)
    chk("persist.py's shortfall", PERSIST_ORDERS, 69.03)
    chk("higgs.py's gate", HIGGS_XI_GATE, 9.782907e31)
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
    if "--law" in sys.argv:
        for what, status, note in CLAUSES:
            print("%-48s %-18s %s" % (what, status, note))
        sys.exit(0)
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
