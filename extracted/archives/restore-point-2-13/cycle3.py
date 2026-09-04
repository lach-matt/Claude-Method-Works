#!/usr/bin/env python3
"""cycle3.py -- CYCLE 3, STEP 1. The family of all closed sets.

Register 458 established that a closed index contains open ones — 300 of 300
random subsets of Λ₉ are open. The converse is the standing question: WHICH
subsets are closed, how many, and what shape do they form?

WHAT IS KNOWN GOING IN
  · the closed sets of a closure operator form a MOORE FAMILY: closed under
    intersection, containing the top. So they are a lattice under ⊆.
  · §17.3's criterion gives an infinite supply: δ⁻¹(T) is closed whenever T is
    convex in the attained range.
  · nothing in the corpus counts them.

COMMITTED BEFORE COMPUTING (§2.13)
  (a) the closed subsets are closed under intersection and NOT under union
  (b) their number is far smaller than 2^|Λ| but far larger than the number of
      convex preimages, so §17.3 supplies a proper subfamily and not all of them
  (c) the count grows faster than |Λ| but slower than 2^|Λ|
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
closed = lambda X, d: R(X, d) == frozenset(X)

def toy(shape):
    """a small closed index: the full box of the given shape, which is closed"""
    return [tuple(v) for v in itertools.product(*[range(n) for n in shape])]

def enumerate_closed(shape):
    """every closed subset of a small ambient, by brute force"""
    d = len(shape); U = toy(shape); n = len(U)
    out = []
    for m in range(1 << n):
        S = [U[i] for i in range(n) if m >> i & 1]
        if not S: continue
        if closed(S, d): out.append(frozenset(S))
    return out, n

def convex_preimages(shape):
    """the family §17.3 supplies: δ⁻¹(T) for T convex in the attained range,
    with δ the difference of the first two coordinates"""
    d = len(shape); U = toy(shape)
    dl = lambda c: c[1] - c[0]
    rng = sorted({dl(c) for c in U})
    fam = set()
    for a in range(len(rng)):
        for b in range(a, len(rng)):
            T = set(rng[a:b+1])
            S = frozenset(c for c in U if dl(c) in T)
            if S: fam.add(S)
    return fam

def run(shape):
    fam, n = enumerate_closed(shape)
    F = set(fam)
    d = len(shape)
    # (a) intersection- and union-closure of the family
    inter = uni = 0; itot = utot = 0
    for A, B in itertools.combinations(fam, 2):
        I = A & B; U_ = A | B
        if I: itot += 1; inter += I in F
        utot += 1; uni += U_ in F
    conv = convex_preimages(shape)
    return dict(cells=n, closed=len(fam), power=1 << n,
                inter=(inter, itot), union=(uni, utot),
                convex=len(conv), convex_in=sum(1 for c in conv if c in F))

with State("cycle3") as st:
    A = step(st, "shape (2,2,2)", lambda: run((2,2,2)), budget=300)
    B = step(st, "shape (3,3)",   lambda: run((3,3)),   budget=300)
    C = step(st, "shape (2,2,2,2)", lambda: run((2,2,2,2)), budget=900)

print(f"  {'ambient':<14}{'cells':>6}{'closed subsets':>16}{'of 2^n':>14}{'share':>9}")
for nm, r in (("(2,2,2)", A), ("(3,3)", B), ("(2,2,2,2)", C)):
    print(f"  {nm:<14}{r['cells']:>6}{r['closed']:>16,}{r['power']:>14,}"
          f"{100*r['closed']/r['power']:>8.3f}%")

print(f"\n  (a) IS THE FAMILY A MOORE FAMILY?")
for nm, r in (("(2,2,2)", A), ("(3,3)", B), ("(2,2,2,2)", C)):
    i, it = r['inter']; u, ut = r['union']
    print(f"    {nm:<12}intersections closed {i:>6}/{it:<6} {100*i/max(it,1):>5.1f}%"
          f"   unions closed {u:>6}/{ut:<6} {100*u/max(ut,1):>5.1f}%")

print(f"\n  (b) HOW MUCH OF THE FAMILY DOES §17.3's CRITERION SUPPLY?")
for nm, r in (("(2,2,2)", A), ("(3,3)", B), ("(2,2,2,2)", C)):
    print(f"    {nm:<12}convex preimages {r['convex']:>5}, of which closed {r['convex_in']:>5}"
          f"   — {100*r['convex_in']/max(r['closed'],1):>5.1f}% of all closed subsets")
