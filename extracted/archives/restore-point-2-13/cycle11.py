#!/usr/bin/env python3
"""cycle11.py -- the seed of every index this book holds.

§21.5 says the repair for an unprintable construction is to print the SEED. That
is a proposal until the seeds exist. This computes them, and checks each one
reconstructs its index exactly — same cells, same E.

The construction (§14.5.7): take, for each ordered pair (i,j) and each step of
φ̂_ij, one cell witnessing that step, plus one cell per alphabet value; then prune
while the closure still returns the index.
"""
import itertools, sys
from collections import Counter
from zeno import State, step
from method_tower import base

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

def witnesses(L, d):
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
    S = set(L); G = list(witnesses(L, d)); i = 0
    while i < len(G):
        c = G[:i] + G[i+1:]
        if len(c) >= 2 and clos(c, d) == S: G = c
        else: i += 1
    return G

# ---- the indexes this book holds --------------------------------------------
L8 = base((3,3,1,3,1))
L9 = [c + (s,) for c in L8 for s in range(0, c[6]+1)]
AR = [("object","a computation","wrong","nothing"),("source","a computation","wrong","nothing"),
("source","other places","unreadable","claims true"),("source","other places","unreadable","mutually"),
("artefact","itself","unusable","mutually"),("source","other places","unusable","claims true"),
("outside","other places","dishonest","claims true"),("object","itself","wrong","nothing"),
("object","other places","wrong","nothing"),("source","itself","wrong","claims true"),
("source","itself","unreadable","claims true"),("source","itself","unusable","nothing"),
("source","other places","wrong","claims true"),("source","a computation","unreadable","claims true"),
("source","a computation","unusable","claims true"),("artefact","other places","unusable","mutually"),
("artefact","a computation","unusable","mutually"),("outside","a computation","dishonest","claims true"),
("source","a computation","unusable","nothing"),("artefact","other places","unusable","claims true"),
("source","itself","unusable","claims true")]
AO = [["object","source","artefact","outside"],["itself","other places","a computation"],
      ["wrong","unreadable","unusable","dishonest"],["nothing","claims true","mutually"]]
AUD = [tuple(AO[i].index(r[i]) for i in range(4)) for r in AR]
JAN = [(pr,g) for pr,w in ((1,2),(2,2),(3,8),(4,8),(5,18),(6,18),(7,32),(8,32)) for g in range(1,w+1)]
D = [31,28,31,30,31,30,31,31,30,31,30,31]
O = sorted(range(12), key=lambda m: D[m])
CALR = [(O.index(m)+1, d) for m in range(12) for d in range(1, D[m]+1)]
BOX = [(l,w,h) for l in range(1,6) for w in range(1,6) for h in range(1,6) if l>=w>=h]

CASES = [("Λ₈, the lattice", L8, 8), ("Λ₉, the tower's first stage", L9, 9),
         ("Janet's left-step table", JAN, 2), ("the calendar, relabelled", CALR, 2),
         ("a box ordering", BOX, 3), ("the audit index", AUD, 4)]

def run():
    out = []
    for nm, L, d in CASES:
        S = set(L); G = seed(L, d)
        out.append((nm, len(S), len(G), clos(G, d) == S, G if len(G) <= 14 else None))
    return out

with State("cycle11") as st:
    rows = step(st, "the seed of every index held", run, budget=1500)

print(f"\n  {'index':<30}{'cells':>8}{'seed':>7}{'reconstructs':>14}{'ratio':>9}")
for nm, n, k, ok, G in rows:
    print(f"  {nm:<30}{n:>8,}{k:>7}{str(ok):>14}{n/k:>8.0f}x")
print(f"\n  every seed under 25: {all(r[2] < 25 for r in rows)}")
print(f"  every seed reconstructs: {all(r[3] for r in rows)}")
for nm, n, k, ok, G in rows:
    if G and len(G) <= 10:
        print(f"\n  {nm} — the whole index, printed:")
        for c in sorted(G): print(f"    {c}")
