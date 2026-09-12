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


def clauseC(X, S, cells, d, shape):
    """Clause C: the join-closure lies in every closed superset (info subset alg)."""
    inJ = {}
    for c in cells:
        inJ[c] = z3.Or([z3.And(X[a], X[b]) for a in cells for b in cells
                        if join(a, b) == c] + [X[c]])
    hyp = z3.And(z3.And([z3.Implies(X[c], S[c]) for c in cells]),
                 closed(S, cells))
    return z3.Implies(hyp, z3.And([z3.Implies(inJ[c], S[c]) for c in cells]))


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

    # (b) THE ENCODING IS THE OPERATOR.  Z3's witness form of in_R against the
    #     staircase the repository actually computes.
    rnd = random.Random(5); bad = tot = 0
    for _ in range(200):
        shape = rnd.choice([(3, 3), (4, 4), (3, 3, 3), (2, 2, 2, 2)])
        d = len(shape)
        Xs = frozenset(rnd.sample(cells_of(shape),
                                  rnd.randint(2, min(len(cells_of(shape)), 8))))
        box = D.box_of(Xs, d); R = D.stair(Xs, box)
        for x in itertools.product(*box):
            tot += 1
            enc = all(any(y[j] <= x[j] and y[i] >= x[i] for y in Xs)
                      for i in range(d) for j in range(d) if i != j)
            bad += enc != (x in R)
    ok &= bad == 0
    print("  [%s] in_R encoding == the staircase: %d cells, %d disagreements"
          % ("ok" if bad == 0 else "XX", tot, bad))

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
    print("Clause C -- join-closure subset every closed superset")
    for shape in ((3, 3), (2, 2, 2), (3, 3, 3)):
        results.append(check("d=%d, box %s" % (len(shape), "x".join(map(str, shape))),
                             shape, clauseC))
    print()
    print("=" * 79)
    n = len(results)
    print("%d of %d obligations discharged by Z3, encoding guards passed"
          % (sum(results), n))
    print("=" * 79)
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
