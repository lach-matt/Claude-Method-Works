#!/usr/bin/env python3
"""cycle2.py -- CYCLE 2, STEP 1. Fill to the limit from what exists.

Cycle 1 established that E prices a LAYOUT CHOICE — 36 with helium at group 18,
20 at group 2 — and that the criterion needs a closed ambient. Both open the
same question, which is the one to fill:

  WHICH LAYOUT CHOICES DOES E PRICE, AND BY HOW MUCH?

Helium is one argued placement. The literature has others, and each is a drawn
decision the same operator can price:

  hydrogen        group 1 (alkali) or group 17 (halogen) — argued as long as He
  lanthanum       group 3, or lutetium in group 3 — the IUPAC 2021 question
  the f-block     detached below, or inline as a 32-column table
  period 1        two cells, or the eight the row could hold

Each is a re-drawing of the SAME 118 elements. E is a fact about the drawing, so
each placement has a price and the prices are comparable. Nothing here is new
theory; it is the operator applied to variants the chemistry literature already
argues about.
"""
import itertools, sys
from collections import Counter
from zeno import State, step

def R(X, d=2):
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
E = lambda X: len(R(X)) - len(X)
join = lambda a, b: tuple(max(x, y) for x, y in zip(a, b))
meet = lambda a, b: tuple(min(x, y) for x, y in zip(a, b))
def sublattice(X):
    S = set(X)
    return all(join(a, b) in S and meet(a, b) in S
               for a, b in itertools.combinations(sorted(X), 2))

def table18(h_group=1, he_group=18, lu_in_3=False):
    """the drawn eighteen-column table, f-block detached, with the two argued
    placements as parameters."""
    G = {1: [h_group, he_group],
         2: [1, 2] + list(range(13, 19)),
         3: [1, 2] + list(range(13, 19))}
    for p in (4, 5, 6, 7): G[p] = list(range(1, 19))
    return {(p, g) for p in G for g in G[p]}

def table32():
    """the 32-column table: the f-block inline, so periods 6 and 7 run to 32"""
    G = {1: [1, 32], 2: [1, 2] + list(range(27, 33)),
         3: [1, 2] + list(range(27, 33))}
    G[4] = G[5] = [1, 2] + list(range(17, 33))
    G[6] = G[7] = list(range(1, 33))
    return {(p, g) for p in G for g in G[p]}

def janet():
    return {(pr, g) for pr, w in ((1,2),(2,2),(3,8),(4,8),(5,18),(6,18),(7,32),(8,32))
            for g in range(1, w + 1)}

def run():
    out = []
    for name, T in [
        ("18-col, H at 1, He at 18   (IUPAC)",     table18(1, 18)),
        ("18-col, H at 1, He at 2    (left-step)", table18(1, 2)),
        ("18-col, H at 17, He at 18  (H halogen)", table18(17, 18)),
        ("18-col, H at 17, He at 2",               table18(17, 2)),
        ("32-column, f-block inline",              table32()),
        ("Janet left-step (n+ℓ, position)",        janet()),
    ]:
        out.append((name, len(T), E(T), sublattice(T)))
    return out

with State("cycle2") as st:
    rows = step(st, "price every argued layout", run, budget=600)

print(f"\n  {'layout':<40}{'cells':>7}{'E':>6}{'closed':>9}")
for n, c, e, cl in rows:
    print(f"  {n:<40}{c:>7}{e:>6}{str(cl):>9}")

base = next(r for r in rows if r[0].startswith("18-col, H at 1, He at 18"))
print(f"\n  the price of each choice, against the IUPAC drawing at E = {base[2]}")
for n, c, e, cl in rows:
    if n is not base[0]:
        print(f"    {n:<40}{e - base[2]:+6}")
