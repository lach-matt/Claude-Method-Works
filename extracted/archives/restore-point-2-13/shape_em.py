#!/usr/bin/env python3
"""shape_em.py -- the mathematical shape of the electromagnetic index in Λ.

CLAIM 1  (the interval property).  For δ = f − ℓ on a sublattice of a product of
chains, and for any two cells a, b:

        min(δa, δb)  ≤  δ(a ∨ b)  ≤  max(δa, δb)
        min(δa, δb)  ≤  δ(a ∧ b)  ≤  max(δa, δb)

PROOF.  δ(a∨b) = max(f_a,f_b) − max(ℓ_a,ℓ_b).  Take f_a ≥ f_b without loss.
Then δ(a∨b) = f_a − max(ℓ_a,ℓ_b) ≤ f_a − ℓ_a = δa.  And δ(a∨b) ≥ f_a − ℓ_a when
ℓ_a ≥ ℓ_b, giving δa; otherwise δ(a∨b) = f_a − ℓ_b ≥ f_b − ℓ_b = δb.  Either way
δ(a∨b) lies between δa and δb.  The meet is dual.  ∎

CLAIM 2  (convexity is the criterion).  δ⁻¹(T) is a sublattice of Λ if and only
if T is CONVEX — an interval of integers with no hole.

  ⟸  if T is convex and δa, δb ∈ T then δ(a∨b) lies between them, hence in T.
  ⟹  if T has a hole at c, exhibit a, b with δa, δb ∈ T and δ(a∨b) = c.

WHAT IT DECIDES.
  the spin rule  ΔS = 0   is  σ⁻¹({0})       — CONVEX     → sublattice
  the parity rule |Δℓ| = 1 is  δ⁻¹({−1, +1}) — NOT CONVEX → not a sublattice

The parity rule fails for one reason and it is stated exactly: it is a set with a
hole at zero.
"""
import itertools, sys, random
from collections import Counter
from zeno import State, step
from method_tower import base

CAPS = (3, 3, 1, 3, 1)
def lam9(caps=CAPS):
    L8 = base(caps)
    return [c + (s,) for c in L8 for s in range(0, c[6] + 1)]
join = lambda a, b: tuple(max(x, y) for x, y in zip(a, b))
meet = lambda a, b: tuple(min(x, y) for x, y in zip(a, b))
dl   = lambda c: c[5] - c[1]          # f − ℓ, SIGNED
ds   = lambda c: c[8] - c[7]          # 2S′ − 2S, SIGNED

def R(X, d):
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
E = lambda X, d: len(R(X, d)) - len(X)

# ---- CLAIM 1, exhaustively on the widest set the budget allows --------------
def claim1(caps):
    L = lam9(caps); bad = 0; n = 0
    for a, b in itertools.combinations(L, 2):
        n += 1
        for m in (join(a, b), meet(a, b)):
            for g in (dl, ds):
                lo, hi = sorted((g(a), g(b)))
                if not (lo <= g(m) <= hi): bad += 1
    return n, bad

# ---- CLAIM 2, both directions ----------------------------------------------
CONVEX = {"{0}": {0}, "{-1..1}": {-1,0,1}, "{-2..2}": set(range(-2,3)),
          "{0,1}": {0,1}, "{1}": {1}, "{-1}": {-1}}
HOLED  = {"{-1,+1}  |Δ| = 1": {-1,1}, "{-2,0,2} even": {-2,0,2},
          "{-2,-1,1,2}  |Δ| in 1..2": {-2,-1,1,2}, "{0,2}": {0,2}}

def sub_ok(L, g, T):
    """is g^-1(T) closed under join and meet inside Λ?"""
    X = [c for c in L if g(c) in T]
    S = set(X); bad = 0
    for a, b in itertools.combinations(X, 2):
        if join(a, b) not in S: bad += 1
        if meet(a, b) not in S: bad += 1
    return len(X), bad

def claim2(caps):
    L = lam9(caps); rows = []
    for name, T in list(CONVEX.items()) + list(HOLED.items()):
        conv = (not T) or (max(T) - min(T) + 1 == len(T))
        for gname, g in (("Δℓ", dl), ("ΔS", ds)):
            n, bad = sub_ok(L, g, T)
            if n:
                rows.append((name, conv, gname, n, bad, E([c for c in L if g(c) in T], 9)))
    return rows

with State("shape_em") as st:
    n1, bad1 = step(st, "claim 1: the interval property", lambda: claim1(CAPS), budget=600)
    rows = step(st, "claim 2: convexity as the criterion", lambda: claim2(CAPS), budget=900)

print(f"\n  CLAIM 1 — the interval property, on all {n1:,} pairs of Λ₉")
print(f"    violations of  min ≤ δ(a∨b), δ(a∧b) ≤ max   for Δℓ and ΔS: {bad1}")

print(f"\n  CLAIM 2 — δ⁻¹(T) is a sublattice iff T is convex")
print(f"  {'T':<24}{'convex':>7}{'on':>5}{'cells':>7}{'∨∧ failures':>13}{'E':>7}")
for name, conv, gname, n, bad, e in rows:
    mark = "." if (bad == 0) == conv else "COUNTEREXAMPLE"
    print(f"  {name:<24}{str(conv):>7}{gname:>5}{n:>7,}{bad:>13,}{e:>7}   {mark}")
agree = sum(1 for r in rows if (r[4] == 0) == r[1])
print(f"\n  the criterion agrees with the outcome in {agree} of {len(rows)} cases")
sys.exit(len(rows) - agree)
