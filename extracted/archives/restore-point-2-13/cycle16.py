#!/usr/bin/env python3
"""cycle16.py -- the seed cost of an axis, swept.

§14.5.8 has three datapoints and says no formula is fitted to them. This gets
enough to fit one honestly: a fixed base, one axis added, with the PARENT COUNT
and the ALPHABET SIZE varied independently.

  base      a down-set in 4 coordinates over 0..3 — 35 cells, seed 7
  axis      y ≤ min(cap, x₀ + … + x_{p−1})   for p = 1, 2, 3
  alphabet  controlled by the cap

COMMITTED BEFORE FITTING (§2.13)
  (a) cost rises with the alphabet at fixed p
  (b) cost rises with p at fixed alphabet
  (c) the leading term is multiplicative — about (alphabet − 1) × p — rather than
      additive, because each parent multiplies the number of envelope steps the
      witnesses must cover
"""
import itertools, sys
from zeno import State, step

def clos(X, d):
    X = list(X); A = [sorted({c[i] for c in X}) for i in range(d)]
    def env(i, j):
        m = {}
        for c in X: m[c[j]] = max(m.get(c[j], -10**9), c[i])
        b, o = -10**9, {}
        for t in sorted(m): b = max(b, m[t]); o[t] = b
        return o
    phi = {(i, j): env(i, j) for i in range(d) for j in range(d) if i != j}
    return {x for x in itertools.product(*A)
            if all(x[i] <= phi[(i, j)][x[j]] for i in range(d) for j in range(d) if i != j)}

def wit(L, d):
    W = set()
    for i in range(d):
        for j in range(d):
            if i == j: continue
            best = {}
            for c in L:
                if c[j] not in best or c[i] > best[c[j]][0]: best[c[j]] = (c[i], c)
            run = -10**9
            for t in sorted(best):
                v, c = best[t]
                if v > run: run = v; W.add(c)
    for i in range(d):
        for v in {c[i] for c in L}:
            if not any(c[i] == v for c in W): W.add(next(c for c in L if c[i] == v))
    return W

def seed(L, d):
    S = set(L); G = list(wit(L, d)); i = 0
    while i < len(G):
        c = G[:i] + G[i+1:]
        if len(c) >= 2 and clos(c, d) == S: G = c
        else: i += 1
    return len(G)

BASE = [v for v in itertools.product(range(4), repeat=4) if all(v[i] >= v[i+1] for i in range(3))]
D0 = 4
S0 = None

def sweep():
    global S0
    S0 = seed(BASE, D0)
    rows = []
    for p in (1, 2, 3):
        for cap in (2, 3, 4, 5, 6, 7):
            L = [c + (y,) for c in BASE
                 for y in range(0, min(cap, sum(c[:p])) + 1)]
            if not L or len(L) > 3000: continue
            a = len({c[-1] for c in L})
            if a < 2: continue
            rows.append((p, cap, a, len(L), seed(L, D0 + 1)))
    return rows

with State("cycle16") as st:
    rows = step(st, "sweep parents x alphabet", sweep, budget=1800)

print(f"\n  base: {len(BASE)} cells, seed {S0}\n")
print(f"  {'parents':>8}{'cap':>5}{'alphabet':>10}{'cells':>8}{'seed':>6}{'cost':>7}"
      f"{'(a−1)·p':>10}{'residual':>10}")
data = []
for p, cap, a, n, sd in rows:
    cost = sd - S0; pred = (a - 1) * p
    data.append((p, a, cost))
    print(f"  {p:>8}{cap:>5}{a:>10}{n:>8,}{sd:>6}{cost:>+7}{pred:>10}{cost-pred:>+10}")

# least squares on cost = A·(a−1)·p + B·(a−1) + C·p + D
import itertools as it
best = None
for A in [x/4 for x in range(0, 13)]:
    for B in [x/4 for x in range(-8, 13)]:
        for C in [x/4 for x in range(-8, 13)]:
            for Dd in [x/2 for x in range(-8, 9)]:
                e = sum((c - (A*(a-1)*p + B*(a-1) + C*p + Dd))**2 for p, a, c in data)
                if best is None or e < best[0]: best = (e, A, B, C, Dd)
e, A, B, C, Dd = best
print(f"\n  least squares over {len(data)} points:")
print(f"    cost ≈ {A}·(a−1)·p + {B}·(a−1) + {C}·p + {Dd}")
print(f"    residual sum of squares {e:.2f}   rms {(e/len(data))**0.5:.2f}")
