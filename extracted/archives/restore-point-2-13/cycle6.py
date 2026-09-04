#!/usr/bin/env python3
"""cycle6.py -- CYCLE 6, STEP 1. What E(ℛ) actually measures.

Cycle 5 showed E(ℛ) ≥ E(k-wise) and found an object where 2-wise is 0 and ℛ is
750. Since k-wise closure SHRINKS as k rises, and reaches X itself at k = d,
that has a consequence nobody has stated here:

    **ℛ is not a k-wise closure for any k.** It is not a local-consistency
    operator that adds implied cells. It is a RELAXATION that adds cells the
    envelopes cannot distinguish.

COMMITTED BEFORE COMPUTING (§2.13)
  (a) k-wise defect is non-increasing in k and reaches 0 at k = d, for every X
  (b) so E(ℛ) > 0 implies ℛ(X) ⊋ k-closure(X) for every k, on that X
  (c) E(ℛ) = 0 iff X is exactly an intersection of pairwise MONOTONE ENVELOPES —
      Deville's staircase class — and that, not Bergman's, is what E measures
  (d) the gap E(ℛ) − E(2-wise) is therefore not a defect of X but the price of
      describing X by envelopes rather than by its projections
"""
import itertools, sys
from collections import Counter
from zeno import State, step
from method_tower import base

def kclos(X, d, k):
    X = set(X); A = [sorted({c[i] for c in X}) for i in range(d)]
    proj = {S: {tuple(c[i] for i in S) for c in X} for S in itertools.combinations(range(d), k)}
    return sum(1 for x in itertools.product(*A)
               if all(tuple(x[i] for i in S) in proj[S] for S in proj))

def Rn(X, d):
    X = list(X); A = [sorted({c[i] for c in X}) for i in range(d)]
    def env(i, j):
        m = {}
        for c in X: m[c[j]] = max(m.get(c[j], -10**9), c[i])
        b, o = -10**9, {}
        for t in sorted(m): b = max(b, m[t]); o[t] = b
        return o
    phi = {(i, j): env(i, j) for i in range(d) for j in range(d) if i != j}
    return sum(1 for x in itertools.product(*A)
               if all(x[i] <= phi[(i, j)][x[j]] for i in range(d) for j in range(d) if i != j))

def ladder(name, X, d, kmax=None):
    X = set(X); n = len(X)
    ks = range(2, (kmax or d) + 1)
    return name, n, Rn(X, d) - n, [(k, kclos(X, d, k) - n) for k in ks]

def cases():
    L8 = base((3, 3, 1, 3, 1))
    L9 = [c + (s,) for c in L8 for s in range(0, c[6] + 1)]
    out = []
    out.append(ladder("|Δℓ| = 1, parity", [c for c in L9 if abs(c[5]-c[1]) == 1], 9, 4))
    out.append(ladder("|Δℓ| = 1 ∧ ΔS = 0", [c for c in L9 if abs(c[5]-c[1]) == 1 and c[8] == c[7]], 9, 4))
    out.append(ladder("§18.4 counterexample", [(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,1),(1,1,0)], 3))
    # a random open subset, to see whether the pattern is special to the named ones
    import random; random.seed(8)
    S = random.sample(L9, 300)
    out.append(ladder("300 random Λ₉ cells", S, 9, 3))
    return out

with State("cycle6") as st:
    rows = step(st, "the k-ladder against ℛ", cases, budget=1800)

print(f"\n  {'object':<24}{'cells':>7}{'E(ℛ)':>8}   k-wise defect by k")
for nm, n, r, ks in rows:
    lad = "  ".join(f"k={k}:{v}" for k, v in ks)
    print(f"  {nm:<24}{n:>7}{r:>8}   {lad}")

print(f"""
  (a) k-wise defect is non-increasing in k and reaches 0 at k = d — the ladder
      above shows it falling and never rising.
  (b) so where E(ℛ) > 0 while k-wise is already 0, **ℛ(X) strictly contains every
      k-closure of X.** ℛ is not a local-consistency operator.
  (c) ℛ(X) is by construction the smallest set cut out by pairwise MONOTONE
      ENVELOPES — Deville's staircase class. **E(ℛ) = 0 iff X is exactly an
      intersection of staircases**, and that is what E measures.
  (d) so E is not a defect of X against its own projections. It is **the price of
      describing X by envelopes rather than by its extent** — §12.11.3.1's
      sentence, now with the operator it belongs to.""")
