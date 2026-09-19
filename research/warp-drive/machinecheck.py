#!/usr/bin/env python3
r"""
machinecheck.py -- MACHINE-CHECKED PROOFS of the hierarchy law's core clauses,
discharged by the Z3 SMT solver over ALL subsets of a given box.

This is not enumeration.  Each theorem is stated as a quantified formula whose
variables range over every subset X of the box (and, where needed, every
sublattice S), the NEGATION is asserted, and Z3 reports `unsat` -- which is a
proof that no counterexample exists in that box.  At d = 3 over a 3x3x3 box that
is 2^27 = 134,217,728 subsets, far past what enumeration reached.

THE KEY ENCODING.  phi and max are eliminated entirely:

    x in R(X)   <=>   for all i != j, there is y in X with y_j <= x_j and y_i >= x_i

because x_i <= max{ y_i : y in X, y_j <= x_j } holds exactly when such a witness
exists.  Everything else is first-order over a finite domain.

    <X> is encoded WITHOUT a fixed point, as the intersection of all closed
    supersets:  R(X) subset <X>  iff  for every S with X subset S and S closed
    under meet and join, R(X) subset S.

The reusable harness is prover.py -- see PROOF-ASSISTANT.md for how to obtain
Z3 in this environment and how to state a new obligation.

Requires z3-solver (pip install z3-solver).  Run: python3 machinecheck.py
"""

import itertools
import sys

import prover
from prover import (cells_of, meet, join, observed, in_R, closed, subset_vars,
                    require_z3, HAVE_Z3)

if not HAVE_Z3:
    require_z3()

import z3


def check(name, shape, build):
    """One obligation, discharged by prover.prove over every subset of the box."""
    return prover.prove(name, shape, build)


# ------------------------------------------------------------------ theorems

def lemma4(X, S, cells, d, shape):
    """Lemma 4: X subset R(X), and R(X) is closed under meet and join."""
    ext = z3.And([z3.Implies(X[c], in_R(X, c, cells, d)) for c in cells])
    cl = []
    for a in cells:
        for b in cells:
            pre = z3.And(in_R(X, a, cells, d), in_R(X, b, cells, d))
            cl.append(z3.Implies(pre, in_R(X, meet(a, b), cells, d)))
            cl.append(z3.Implies(pre, in_R(X, join(a, b), cells, d)))
    return z3.Implies(observed(X, cells, shape), z3.And(ext, z3.And(cl)))


def clauseB(X, S, cells, d, shape):
    """Clause B: R(X) = <X>.  The hard half, via 'every closed superset'."""
    hyp = z3.And(observed(X, cells, shape),
                 z3.And([z3.Implies(X[c], S[c]) for c in cells]),
                 closed(S, cells))
    return z3.Implies(hyp, z3.And([z3.Implies(in_R(X, c, cells, d), S[c])
                                   for c in cells]))


def lemmaN1(X, S, cells, d, shape):
    """Lemma N1*: over a box with NO observed hypothesis, every cell of R(X)
    whose coordinates are all realised in X lies in every closed superset.
    (R_B(X) cap Box(X) = <X>, the corollary's engine.)"""
    realised = lambda c: z3.And([z3.Or([X[y] for y in cells if y[i] == c[i]])
                                 for i in range(d)])
    hyp = z3.And(z3.And([z3.Implies(X[c], S[c]) for c in cells]),
                 closed(S, cells))
    return z3.Implies(hyp, z3.And([z3.Implies(z3.And(in_R(X, c, cells, d),
                                                     realised(c)), S[c])
                                   for c in cells]))


def is_seed(X, y, cells, d):
    """y is a join-irreducible ("seed") of X: y in X, and y is NOT the join of
    the elements of X strictly below it.  y is that join exactly when every
    coordinate is attained below it, so y is a seed iff SOME coordinate is
    attained by no z in X with z < y."""
    below = lambda z: (all(z[t] <= y[t] for t in range(d)) and z != y)
    return z3.And(X[y],
                  z3.Or([z3.Not(z3.Or([X[z] for z in cells
                                       if below(z) and z[i] == y[i]]))
                         for i in range(d)]))


def joinclosed(T, cells):
    return z3.And([z3.Implies(z3.And(T[a], T[b]), T[join(a, b)])
                   for a in cells for b in cells])


def clauseC_engine(X, T, cells, d, shape):
    """CLAUSE C's ENGINE (Lemma 8): the join-irreducibles REGROW X.  For every
    join-closed T containing every seed of X, X subset T -- so X lies in the
    join-closure of its own seeds, which is exactly what makes
    op_information(X) = J(X).

    This is the obligation the first draft's clauseC did NOT discharge: that one
    expanded X by a single join and never mentioned seeds at all."""
    hyp = z3.And(joinclosed(T, cells),
                 z3.And([z3.Implies(is_seed(X, y, cells, d), T[y])
                         for y in cells]))
    return z3.Implies(hyp, z3.And([z3.Implies(X[c], T[c]) for c in cells]))


def clauseC_subset(X, S, cells, d, shape):
    """information subset algebra: a meet-and-join-closed S containing X is in
    particular join-closed, so it contains every join of elements of X."""
    hyp = z3.And(z3.And([z3.Implies(X[c], S[c]) for c in cells]),
                 closed(S, cells))
    return z3.Implies(hyp, z3.And([z3.Implies(z3.Or([z3.And(X[a], X[b])
                                                     for a in cells for b in cells
                                                     if join(a, b) == c] + [X[c]]),
                                              S[c]) for c in cells]))


def lemmaN1_reverse(X, S, cells, d, shape):
    """The OTHER direction of Lemma N1*: R_B(X) cap Box(X) contains X and is
    closed, hence contains <X>, the least such.  With lemmaN1 this makes the
    machine-checked statement an EQUALITY rather than one inclusion."""
    realised = lambda c: z3.And([z3.Or([X[y] for y in cells if y[i] == c[i]])
                                 for i in range(d)])
    mem = lambda c: z3.And(in_R(X, c, cells, d), realised(c))
    contains_X = z3.And([z3.Implies(X[c], mem(c)) for c in cells])
    is_closed = z3.And([z3.Implies(z3.And(mem(a), mem(b)), mem(meet(a, b)))
                        for a in cells for b in cells] +
                       [z3.Implies(z3.And(mem(a), mem(b)), mem(join(a, b)))
                        for a in cells for b in cells])
    return z3.And(contains_X, is_closed)



def soundness_guards():
    """A machine-check is worthless if the encoding is wrong or the hypotheses
    are unsatisfiable.  Both are checked here BEFORE any obligation is reported.
    The reusable forms live in prover.py."""
    import random
    import decomposable as D
    ok = True
    print("SOUNDNESS GUARDS (run before the obligations)")

    # (a) NON-VACUITY: each obligation's hypothesis must be satisfiable, and
    #     satisfiable non-trivially -- with S strictly inside the box.
    for shape in ((3, 3), (3, 3, 3)):
        cells = cells_of(shape)
        X = {c: z3.Bool("x_%s" % (c,)) for c in cells}
        S = {c: z3.Bool("s_%s" % (c,)) for c in cells}
        hyp = z3.And(observed(X, cells, shape),
                     z3.And([z3.Implies(X[c], S[c]) for c in cells]),
                     closed(S, cells))
        s1 = z3.Solver(); s1.add(hyp)
        s2 = z3.Solver(); s2.add(hyp); s2.add(z3.Or([z3.Not(S[c]) for c in cells]))
        good = (s1.check() == z3.sat and s2.check() == z3.sat)
        ok &= good
        print("  [%s] hypotheses satisfiable, non-trivially, box %s"
              % ("ok" if good else "XX", "x".join(map(str, shape))))

    # (b) THE ENCODING IS THE OPERATOR.  Delegated to prover.encoding_matches,
    #     which builds the real in_R expression with X pinned to concrete
    #     booleans and simplifies it.  Re-typing the formula inline would test
    #     the typist, not the encoding, and could not catch a bug in in_R.
    tot, bad = prover.encoding_matches(lambda Xs, box, dd: D.stair(Xs, box),
                                       [(3, 3), (4, 4), (3, 3, 3), (2, 2, 2, 2)],
                                       trials=120)
    ok &= bad == 0
    print("  [%s] prover.in_R EVALUATED == the staircase: %d cells, %d disagreements"
          % ("ok" if bad == 0 else "XX", tot, bad))
    _, nbad = prover.encoding_matches(lambda Xs, box, dd: frozenset(Xs),
                                      [(3, 3)], trials=20)
    ok &= nbad > 0
    print("  [%s] negative control -- the guard detects a wrong reference (%d)"
          % ("ok" if nbad > 0 else "XX", nbad))

    # (c) THE HULL ENCODING.  'in every closed superset' == 'in <X>', brute forced.
    rnd = random.Random(9); bad = tot = 0
    for _ in range(60):
        shape = rnd.choice([(3, 3), (2, 2, 2)])
        cells = cells_of(shape)
        Xs = frozenset(rnd.sample(cells, rnd.randint(2, min(len(cells), 6))))
        inter = set(cells)
        for mask in range(1 << len(cells)):
            Sset = {cells[i] for i in range(len(cells)) if mask >> i & 1}
            if not Xs <= Sset:
                continue
            if all(meet(a, b) in Sset and join(a, b) in Sset
                   for a in Sset for b in Sset):
                inter &= Sset
        tot += 1
        bad += frozenset(inter) != D.gen(Xs)
    ok &= bad == 0
    print("  [%s] <X> == intersection of closed supersets: %d sets, %d disagreements"
          % ("ok" if bad == 0 else "XX", tot, bad))
    print()
    return ok


def main():
    print(__doc__)
    print("=" * 79)
    print("MACHINE-CHECKED BY Z3 %s" % z3.get_version_string())
    print("=" * 79)
    print()
    guards = soundness_guards()
    if not guards:
        print("SOUNDNESS GUARDS FAILED -- obligations not reported")
        return 1
    results = []
    print("Lemma 4 -- R(X) is a sublattice containing X")
    for shape in ((3, 3), (4, 4), (2, 2, 2), (3, 3, 3)):
        results.append(check("d=%d, box %s" % (len(shape), "x".join(map(str, shape))),
                             shape, lemma4))
    print()
    print("Clause B -- R(X) = <X>, the hard inclusion")
    for shape in ((2, 2), (3, 3), (4, 4), (2, 2, 2), (3, 3, 3)):
        results.append(check("d=%d, box %s" % (len(shape), "x".join(map(str, shape))),
                             shape, clauseB))
    print()
    print("Lemma N1* -- R_B(X) cap Box(X) subset <X>, no observed hypothesis")
    for shape in ((3, 3), (4, 4), (3, 3, 3)):
        results.append(check("d=%d, box %s" % (len(shape), "x".join(map(str, shape))),
                             shape, lemmaN1))
    print()
    print("Lemma N1* -- the REVERSE inclusion, making it an equality")
    for shape in ((3, 3), (4, 4), (3, 3, 3)):
        results.append(check("d=%d, box %s" % (len(shape), "x".join(map(str, shape))),
                             shape, lemmaN1_reverse))
    print()
    print("Clause C ENGINE (Lemma 8) -- the seeds regrow X")
    for shape in ((3, 3), (2, 2, 2), (3, 3, 3)):
        results.append(check("d=%d, box %s" % (len(shape), "x".join(map(str, shape))),
                             shape, clauseC_engine))
    print()
    print("Clause C -- join-closure subset every closed superset")
    for shape in ((3, 3), (2, 2, 2), (3, 3, 3)):
        results.append(check("d=%d, box %s" % (len(shape), "x".join(map(str, shape))),
                             shape, clauseC_subset))
    print()
    print("=" * 79)
    n = len(results)
    print("%d of %d obligations discharged by Z3, encoding guards passed"
          % (sum(results), n))
    print("=" * 79)
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
