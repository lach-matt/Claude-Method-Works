#!/usr/bin/env python3
"""machinecheck-vacancy.py -- Z3 discharge of vacancy.py's two lemmas.

MACHINE-CHECK the two claims an 88,087-case exhaustion suggested.

    L1.  Every sublattice of a finite product of chains is 2-DETERMINED.
    L2.  Every sublattice of a finite product of chains is STAIRCASE-CLOSED.

Together: for a SUBLATTICE the only free coordinate is hull-completeness, so
K6 versus K7 is decided entirely by whether its 2-D shadows are convex.

The claim quantifies over EVERY subset of the box, which is what makes this a
proof over the box rather than a sample of it: at 3x3x3 that is 2^27 subsets.
"""
import itertools, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import prover as P
import z3


def pairwise_consistent(X, x, cells, d):
    """x agrees with some member of X on every PAIR of coordinates."""
    return z3.And([z3.Or([X[y] for y in cells if y[i] == x[i] and y[j] == x[j]])
                   for i, j in itertools.combinations(range(d), 2)])


def claim_2determined(X, S, cells, d, shape):
    # X closed under meet and join  =>  every pairwise-consistent cell is in X
    return z3.Implies(
        P.closed(X, cells),
        z3.And([z3.Implies(pairwise_consistent(X, x, cells, d), X[x])
                for x in cells]))


def claim_staircase(X, S, cells, d, shape):
    # X closed under meet and join, alphabet observed  =>  staircase adds nothing
    return z3.Implies(
        z3.And(P.closed(X, cells), P.observed(X, cells, shape)),
        z3.And([z3.Implies(P.in_R(X, x, cells, d), X[x]) for x in cells]))


# ---- GUARD 1: the hypotheses must be SATISFIABLE, or unsat proves nothing.
print("GUARD -- hypotheses non-vacuous (a closed, observed X with >1 cell exists)")
for shape in [(3, 3), (2, 2, 2), (3, 3, 3)]:
    cells = P.cells_of(shape)
    X = P.subset_vars(cells, "X")
    s = z3.Solver()
    s.add(P.closed(X, cells), P.observed(X, cells, shape))
    s.add(z3.PbGe([(X[c], 1) for c in cells], 2))
    print("   %-10s %s" % ("x".join(map(str, shape)), s.check()))
print()

# ---- GUARD 2: the encoding is the operator the tree actually runs. A
# machine-check of the wrong formula proves the wrong thing, and PROOF-ASSISTANT.md
# names encoding drift as one of the two guards that must run first.
print("GUARD -- in_R encoding matches decomposable.stair on random indexes")
import decomposable as D, random
rnd = random.Random(3); ok = 0; n = 0
for _ in range(400):
    d = rnd.choice([2, 3]); v = rnd.choice([2, 3])
    allc = list(itertools.product(range(v), repeat=d))
    X = frozenset(rnd.sample(allc, rnd.randint(2, min(6, len(allc)))))
    box = [sorted({c[i] for c in X}) for i in range(d)]
    if any(len(b) < 2 for b in box):
        continue
    n += 1
    ref = D.stair(X, box)
    enc = {x for x in itertools.product(*box)
           if all(any(y[j] <= x[j] and y[i] >= x[i] for y in X)
                  for i in range(d) for j in range(d) if i != j)}
    ok += (ref == enc)
print("   witness-form staircase == decomposable.stair on %d/%d indexes" % (ok, n))
print()

print("=" * 70)
print("L1  every sublattice is 2-DETERMINED")
print("=" * 70)
r1 = [P.prove("2-determined over %s" % ("x".join(map(str, s)),), s, claim_2determined)
      for s in [(3, 3), (4, 4), (2, 2, 2), (3, 3, 3), (2, 2, 2, 2), (3, 3, 3, 3)]]
print()
print("=" * 70)
print("L2  every sublattice is STAIRCASE-CLOSED")
print("=" * 70)
r2 = [P.prove("staircase-closed over %s" % ("x".join(map(str, s)),), s, claim_staircase)
      for s in [(3, 3), (4, 4), (2, 2, 2), (3, 3, 3), (2, 2, 2, 2), (3, 3, 3, 3)]]
print()
print("L1 discharged on %d of %d boxes; L2 on %d of %d."
      % (sum(map(bool, r1)), len(r1), sum(map(bool, r2)), len(r2)))
