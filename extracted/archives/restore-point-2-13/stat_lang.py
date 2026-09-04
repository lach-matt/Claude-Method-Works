#!/usr/bin/env python3
"""stat_lang.py -- statistics as a sixth language, tested on Λ.

§20 measures five languages with closure operators — order (ℛ), geometry
(monotone polyhedron), algebra/logic (Gröbner), analysis (coefficients of F),
information (description length) — and records that six agree on Λ at 976 with
ten combinations holding, C(5,2), a complete graph.

None of the five closes on a DISTRIBUTION. This tests whether statistics is a
sixth language in the same sense: does it have a closure operator, does it
recover 976, and does it agree with the others?

A language qualifies, by §20's own standard, if it has
  (1) a closure operator,
  (2) delete-then-restore behaviour,
  (3) add-then-absorb behaviour,
and agrees on the same object.

COMMITTED BEFORE COMPUTING (§2.13)
  Statistics WILL recover 976 — the marginal distributions of a product-like
  set carry the counts — but it will FAIL the delete test, because deleting one
  cell of 976 moves a marginal by 1/976 and no closure can restore which cell.
"""
import itertools, random
from collections import Counter
from zeno import State, step
from method_tower import base

L8 = [tuple(c) for c in base((3, 3, 1, 3, 1))]
D = 8
N = ["n", "l", "k", "q", "e", "f", "g", "2S"]

def marginals(X):
    """the statistical description: one distribution per coordinate"""
    return [Counter(c[i] for c in X) for i in range(D)]

def pair_marginals(X):
    return {(i, j): Counter((c[i], c[j]) for c in X)
            for i in range(D) for j in range(i + 1, D)}

def stat_closure(marg, pair):
    """the closure operator of the statistical language: the maximum-entropy
    set consistent with the stated marginals — here, every cell whose pairwise
    values all have positive pair-marginal support"""
    A = [sorted(m) for m in marg]
    out = set()
    for x in itertools.product(*A):
        ok = True
        for (i, j), pm in pair.items():
            if pm.get((x[i], x[j]), 0) == 0: ok = False; break
        if ok: out.add(x)
    return out

def run():
    R = {}
    X = set(L8)
    marg, pair = marginals(X), pair_marginals(X)
    R["cells"] = len(X)
    R["total from marginals"] = sum(marg[0].values())
    C = stat_closure(marg, pair)
    R["|closure|"] = len(C)
    R["E_stat"] = len(C) - len(X)

    # delete test: remove one cell, re-close, is it restored?
    victim = sorted(X)[len(X) // 2]
    Y = X - {victim}
    C2 = stat_closure(marginals(Y), pair_marginals(Y))
    R["delete: restored"] = victim in C2
    R["delete: |closure|"] = len(C2)

    # add test: put in a cell Λ excludes, is it absorbed or does it show?
    box = [sorted({c[i] for c in X}) for i in range(D)]
    outside = [x for x in itertools.product(*box) if x not in X]
    random.seed(11)
    add = random.choice(outside)
    Z = X | {add}
    C3 = stat_closure(marginals(Z), pair_marginals(Z))
    R["add: absorbed"] = len(C3) == len(C)
    R["add: |closure|"] = len(C3)
    return R, marg

with State("stat_lang") as st:
    R, marg = step(st, "statistics as a sixth language", run, budget=600)

print(f"  Λ₈ has {R['cells']} cells\n")
print(f"  THE STATISTICAL LANGUAGE — closure = max-entropy set on the marginals\n")
print(f"    total recovered from a marginal   {R['total from marginals']:>6}"
      f"   {'AGREES at 976' if R['total from marginals'] == 976 else 'DISAGREES'}")
print(f"    |closure|                         {R['|closure|']:>6}")
print(f"    E_stat = |closure| - |X|          {R['E_stat']:>6}\n")
print(f"  THE TWO TESTS §20 REQUIRES OF A LANGUAGE\n")
print(f"    delete one cell, re-close: restored?   {R['delete: restored']}"
      f"    (|closure| {R['delete: |closure|']})")
print(f"    add an excluded cell:      absorbed?   {R['add: absorbed']}"
      f"    (|closure| {R['add: |closure|']})")
