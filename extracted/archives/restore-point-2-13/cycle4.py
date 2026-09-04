#!/usr/bin/env python3
"""cycle4.py -- CYCLE 4, STEP 1. The meet-irreducibles of ℛ.

§14.5 named the route and did not take it. A Moore family is generated under
intersection by its MEET-IRREDUCIBLE members, so if those are few the count is
reachable where brute force is not.

  a closed set M is meet-irreducible when it is not the intersection of the
  closed sets strictly above it

COMMITTED BEFORE COMPUTING (§2.13)
  (a) every closed set is an intersection of meet-irreducibles, so the family is
      determined by them — the standard fact, verified here rather than assumed
  (b) the meet-irreducibles are FEW relative to the family: their count grows
      like the ambient, not like the family
  (c) their number is a better handle on |Cl(ℛ)| for Λ than 2^976
"""
import itertools, sys
from collections import Counter
from zeno import State, step

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
    return frozenset(x for x in itertools.product(*A)
                     if all(x[i] <= phi[(i, j)][x[j]] for i in range(d) for j in range(d) if i != j))

def family(shape):
    d = len(shape); U = [tuple(v) for v in itertools.product(*[range(n) for n in shape])]
    n = len(U); fam = set()
    for m in range(1, 1 << n):
        S = frozenset(U[i] for i in range(n) if m >> i & 1)
        if R(S, d) == S: fam.add(S)
    return fam, frozenset(U), d

def meet_irreducible(fam, top):
    """M is meet-irreducible iff the intersection of everything strictly above it
    is strictly larger than M"""
    mi = []
    for M in fam:
        above = [F for F in fam if M < F]
        if not above:                      # the top is not counted
            continue
        I = above[0]
        for F in above[1:]: I = I & F
        if I != M: mi.append(M)
    return mi

def generated(mi, top):
    """everything reachable by intersecting meet-irreducibles, plus the top"""
    got = {top}; frontier = {top}
    while frontier:
        new = set()
        for A in frontier:
            for M in mi:
                I = A & M
                if I not in got: new.add(I); got.add(I)
        frontier = new
    return got

def run(shape):
    fam, top, d = family(shape)
    mi = meet_irreducible(fam, top)
    gen = generated(mi, top)
    return dict(cells=len(top), closed=len(fam), mi=len(mi),
                generated=len(gen), agree=gen == fam | {top})

with State("cycle4") as st:
    A = step(st, "(2,2,2)",   lambda: run((2,2,2)),   budget=300)
    B = step(st, "(3,3)",     lambda: run((3,3)),     budget=300)
    C = step(st, "(2,2,2,2)", lambda: run((2,2,2,2)), budget=1200)

print(f"\n  {'ambient':<12}{'cells':>6}{'closed':>9}{'meet-irred':>12}"
      f"{'generated':>11}{'agree':>8}")
for nm, r in (("(2,2,2)", A), ("(3,3)", B), ("(2,2,2,2)", C)):
    print(f"  {nm:<12}{r['cells']:>6}{r['closed']:>9,}{r['mi']:>12}"
          f"{r['generated']:>11,}{str(r['agree']):>8}")

print(f"\n  (b) HOW FEW ARE THEY?")
for nm, r in (("(2,2,2)", A), ("(3,3)", B), ("(2,2,2,2)", C)):
    print(f"    {nm:<12}meet-irreducibles per cell {r['mi']/r['cells']:>6.2f}"
          f"   per closed set {r['mi']/r['closed']:>7.4f}")
