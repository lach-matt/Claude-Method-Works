#!/usr/bin/env python3
"""cycle5.py -- CYCLE 5, STEP 1. The pairwise mechanism.

Pairwise structures are everywhere in this corpus, and ℛ is one: it is DEFINED
by binary projections φ̂_ij over ordered pairs. The question is whether that is a
mechanism or a coincidence — and the way to tell is to find where pairs stop
sufficing, because a mechanism has a boundary and a coincidence does not.

WHERE PAIRS APPEAR, from the corpus
  ℛ                binary envelopes over ordered pairs
  Baker–Pixley     a sublattice of a product is determined by its TWO-fold projections
  2-decomposability E(X) = 0 is exactly this
  d(x,y)           between two cells
  [x∧y, x∨y]       between two cells
  reorderability   arity = the number of axes on which TWO cells differ
  the interval map δ(a∨b) between δa and δb

WHERE THEY DEMONSTRABLY STOP
  the bracket      relates THREE consecutive members
  the three-body   K₃, treewidth 2 — the maximal excluded form
  arity ≥ 4        no Schaefer class covers the reorderability language
  the four-body    K₄, width 3, after reference was added

COMMITTED BEFORE COMPUTING (§2.13)
  (a) k-wise closure for k = 2 already gives everything: closing under TRIPLE
      projections adds nothing ℛ has not, on a closed index
  (b) but on an OPEN index the two differ, and the difference is a measurement
  (c) the gap between 2-wise and 3-wise defect is where the corpus's failures sit
"""
import itertools, sys
from collections import Counter
from zeno import State, step
from method_tower import base

def k_closure(X, d, k):
    """the largest set whose every k-subset of coordinates projects into X's"""
    X = set(X)
    A = [sorted({c[i] for c in X}) for i in range(d)]
    proj = {}
    for S in itertools.combinations(range(d), k):
        proj[S] = {tuple(c[i] for i in S) for c in X}
    out = set()
    for x in itertools.product(*A):
        if all(tuple(x[i] for i in S) in proj[S] for S in proj): out.add(x)
    return out

def R(X, d):
    X = list(X)
    A = [sorted({c[i] for c in X}) for i in range(d)]
    def env(i, j):
        m = {}
        for c in X: m[c[j]] = max(m.get(c[j], -10**9), c[i])
        b, o = -10**9, {}
        for t in sorted(m): b = max(b, m[t]); o[t] = b
        return o
    phi = {(i, j): env(i, j) for i in range(d) for j in range(d) if i != j}
    return {x for x in itertools.product(*A)
            if all(x[i] <= phi[(i, j)][x[j]] for i in range(d) for j in range(d) if i != j)}

def run(name, X, d):
    n = len(set(X))
    r = len(R(X, d)) - n
    k2 = len(k_closure(X, d, 2)) - n
    k3 = len(k_closure(X, d, 3)) - n if d >= 3 else None
    k4 = len(k_closure(X, d, 4)) - n if d >= 4 else None
    return (name, n, r, k2, k3, k4)

def cases():
    out = []
    L8 = base((3, 3, 1, 3, 1))
    L9 = [c + (s,) for c in L8 for s in range(0, c[6] + 1)]
    out.append(run("Λ₈, closed", L8, 8))
    out.append(run("|Δℓ| = 1, the parity rule", [c for c in L9 if abs(c[5]-c[1]) == 1], 9))
    out.append(run("ΔS = 0, the spin rule", [c for c in L9 if c[8] == c[7]], 9))
    # the periodic table, open at 36
    G = {1: [1,18], 2: [1,2]+list(range(13,19)), 3: [1,2]+list(range(13,19))}
    for p in (4,5,6,7): G[p] = list(range(1,19))
    out.append(run("the periodic table", [(p,g) for p in G for g in G[p]], 2))
    # the d=3 counterexample: every proper projection fixed, not closed
    S3 = [(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,1),(1,1,0)]
    out.append(run("§18.4's counterexample", S3, 3))
    return out

with State("cycle5") as st:
    rows = step(st, "2-wise against 3-wise and 4-wise", cases, budget=1200)

print(f"\n  {'object':<28}{'cells':>7}{'E (ℛ)':>8}{'2-wise':>8}{'3-wise':>8}{'4-wise':>8}")
for nm, n, r, k2, k3, k4 in rows:
    f = lambda v: "—" if v is None else f"{v}"
    print(f"  {nm:<28}{n:>7}{r:>8}{f(k2):>8}{f(k3):>8}{f(k4):>8}")
print(f"""
  READING
    E (ℛ)   the defect of the monotone-envelope operator
    k-wise  the defect of closing under k-fold projections — Baker–Pixley's
            object at k = 2, and its refinements above""")
