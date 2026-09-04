#!/usr/bin/env python3
"""cycle7.py -- CYCLE 7, STEP 1. Is ℛ the staircase closure?

§14.5.4 says ℛ(X) is the smallest set cut out by pairwise monotone envelopes and
identifies that with Deville, Barták and Van Hentenryck's connected row-convex
class. **Deville's class is (α,β)-monotone with α,β ∈ {≤,≥} — FOUR orientations.
ℛ uses one.**

  ℛ            x_i ≤ φ̂_ij(x_j)   with φ̂ non-decreasing        the (≤,≤) corner
  staircase    all four corners: (≤,≤), (≤,≥), (≥,≤), (≥,≥)

COMMITTED BEFORE COMPUTING (§2.13)
  (a) the full four-orientation closure is a subset of ℛ(X), so its defect is ≤
  (b) the ANTI-DIAGONAL is a staircase under mixed orientation, so the parity
      rule — 750 under ℛ — should come out at or near zero under the full class
  (c) if so, §14.5.4's identification with Deville OVER-CLAIMS, and what ℛ
      measures is distance from a one-orientation SUBCLASS
"""
import itertools, sys
from collections import Counter
from zeno import State, step
from method_tower import base

def env_pair(X, i, j, up_i, up_j):
    """the tightest bound of the chosen orientation on coordinate i given j.
    up_i / up_j say whether the bound is an upper (True) or lower (False) one."""
    m = {}
    for c in X:
        key = c[j]
        v = c[i]
        if key not in m: m[key] = [v, v]
        m[key][0] = min(m[key][0], v); m[key][1] = max(m[key][1], v)
    keys = sorted(m)
    out = {}
    if up_j:                       # accumulate over increasing j
        run = None
        for t in keys:
            v = m[t][1] if up_i else m[t][0]
            run = v if run is None else (max(run, v) if up_i else min(run, v))
            out[t] = run
    else:                          # accumulate over decreasing j
        run = None
        for t in reversed(keys):
            v = m[t][1] if up_i else m[t][0]
            run = v if run is None else (max(run, v) if up_i else min(run, v))
            out[t] = run
    return out

def stair_closure(X, d, corners):
    """intersect every admissible staircase bound of the given orientations"""
    X = list(X); A = [sorted({c[i] for c in X}) for i in range(d)]
    cons = []
    for i in range(d):
        for j in range(d):
            if i == j: continue
            for (up_i, up_j) in corners:
                e = env_pair(X, i, j, up_i, up_j)
                cons.append((i, j, up_i, dict(e)))
    n = 0
    for x in itertools.product(*A):
        ok = True
        for (i, j, up_i, e) in cons:
            b = e.get(x[j])
            if b is None: ok = False; break
            if up_i and x[i] > b: ok = False; break
            if (not up_i) and x[i] < b: ok = False; break
        if ok: n += 1
    return n

R_CORNERS  = [(True, True)]                                    # ℛ: upper bound, non-decreasing
ALL_CORNERS = [(True, True), (True, False), (False, True), (False, False)]

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

def cases():
    L8 = base((3, 3, 1, 3, 1))
    L9 = [c + (s,) for c in L8 for s in range(0, c[6] + 1)]
    out = []
    for nm, X, d in [
        ("Λ₈, closed",                 L8, 8),
        ("|Δℓ| = 1, the anti-diagonal",[c for c in L9 if abs(c[5]-c[1]) == 1], 9),
        ("ΔS = 0, the diagonal",       [c for c in L9 if c[8] == c[7]], 9),
        ("|Δℓ| = 1 ∧ ΔS = 0",          [c for c in L9 if abs(c[5]-c[1]) == 1 and c[8] == c[7]], 9),
        ("§18.4's counterexample",     [(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,1),(1,1,0)], 3),
    ]:
        n = len(set(X))
        out.append((nm, n, Rn(X, d) - n,
                    stair_closure(X, d, R_CORNERS) - n,
                    stair_closure(X, d, ALL_CORNERS) - n))
    return out

with State("cycle7") as st:
    rows = step(st, "one orientation against four", cases, budget=1800)

print(f"\n  {'object':<30}{'cells':>7}{'E(ℛ)':>8}{'(≤,≤) only':>12}{'all four':>10}")
for nm, n, r, one, four in rows:
    print(f"  {nm:<30}{n:>7}{r:>8}{one:>12}{four:>10}")
