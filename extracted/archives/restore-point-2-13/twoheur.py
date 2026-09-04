#!/usr/bin/env python3
"""twoheur.py -- never one heuristic.

Twelve cycles fitted expressions to prune-greedy's output and checked each fit
against numbers from the same source. §4.6's forbidden shape. The repair is to
run several and report the spread, and to carry a LOWER bound so the gap is
visible rather than assumed away.

  H1  prune-greedy        start from the witness set, drop while it still closes
  H2  greedy set cover    take the cell covering most uncovered elements
  H3  H2 then prune       the standard pairing
  H4  randomised H2       ties broken at random, best of many restarts
  H5  reverse-delete      start from all cells, drop the least-covering first
  LB  disjoint witnesses  elements with pairwise-disjoint witness sets
  BB  branch and bound    exact, where the instance is small enough
"""
import itertools, random, sys
from zeno import State, step

def elements(L, d):
    A = [sorted({c[i] for c in L}) for i in range(d)]
    el, wit = [], {}
    for i in range(d):
        for j in range(d):
            if i == j: continue
            m = {}
            for c in L: m[c[j]] = max(m.get(c[j], -10**9), c[i])
            run = -10**9
            for v in sorted(m):
                if m[v] > run:
                    run = m[v]; e = ("s", i, j, v, run); el.append(e)
                    wit[e] = frozenset(c for c in L if c[j] == v and c[i] == run)
    for i in range(d):
        for v in A[i]:
            e = ("a", i, v); el.append(e); wit[e] = frozenset(c for c in L if c[i] == v)
    return el, wit

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

def prune(G, S, d):
    G = list(G); i = 0
    while i < len(G):
        c = G[:i] + G[i+1:]
        if len(c) >= 2 and clos(c, d) == S: G = c
        else: i += 1
    return G

def H1(L, d, rng):
    S = set(L); el, wit = elements(L, d)
    W = set().union(*[list(wit[e])[:1] for e in el])
    W = {list(wit[e])[0] for e in el}
    G = list(W); rng.shuffle(G)
    return len(prune(G, S, d))

def cover_map(L, el, wit):
    return {c: {e for e in el if c in wit[e]} for c in L}

def H2(L, d, rng, randomised=False, restarts=1):
    S = set(L); el, wit = elements(L, d); cov = cover_map(L, el, wit)
    best = None
    for _ in range(restarts):
        un = set(el); G = []
        while un:
            k = max(len(cov[c] & un) for c in L)
            if k == 0: break
            cands = [c for c in L if len(cov[c] & un) == k]
            G.append(rng.choice(cands) if randomised else cands[0])
            un -= cov[G[-1]]
        if best is None or len(G) < len(best): best = G
    return best, S

def H5(L, d, rng):
    S = set(L); el, wit = elements(L, d); cov = cover_map(L, el, wit)
    G = sorted(L, key=lambda c: -len(cov[c]))
    return len(prune(G[:40], S, d))

def LB(L, d):
    el, wit = elements(L, d)
    chosen, used = 0, set()
    for e in sorted(el, key=lambda e: len(wit[e])):
        if not (wit[e] & used): chosen += 1; used |= set(wit[e])
    return chosen

def BB(L, d, ub, cap=9):
    """exact minimum by branch and bound over the rarest uncovered element"""
    el, wit = elements(L, d); el = sorted(el, key=lambda e: len(wit[e]))
    best = [ub]
    def rec(un, k, chosen):
        if k >= best[0]: return
        if not un: best[0] = k; return
        e = min(un, key=lambda e: len(wit[e]))
        for c in wit[e]:
            rec({x for x in un if c not in wit[x]}, k + 1, chosen + [c])
    if len(el) <= 60:
        rec(set(el), 0, [])
    return best[0]

def run(name, L, d):
    rng = random.Random(5); S = set(L)
    h1 = H1(L, d, rng)
    g2, _ = H2(L, d, rng); h2 = len(g2)
    h3 = len(prune(g2, S, d))
    g4, _ = H2(L, d, rng, randomised=True, restarts=6); h4 = len(prune(g4, S, d))
    h5 = H5(L, d, rng)
    lb = LB(L, d)
    bb = BB(L, d, min(h1, h2, h3, h4, h5))
    return name, len(L), h1, h2, h3, h4, h5, lb, bb

from method_tower import base
L8 = base((3,3,1,3,1))
CASES = [("Λ₈", L8, 8),
         ("down-set d=4 c=4", [v for v in itertools.product(range(4),repeat=4)
                               if all(v[i]>=v[i+1] for i in range(3))], 4),
         ("full box 3^3", [tuple(v) for v in itertools.product(range(3),repeat=3)], 3),
         ("full box 4^3", [tuple(v) for v in itertools.product(range(4),repeat=3)], 3)]

with State("twoheur") as st:
    rows = [step(st, nm, (lambda nm=nm, L=L, d=d: run(nm, L, d)), budget=900)
            for nm, L, d in CASES]

print(f"\n  {'object':<20}{'cells':>7}{'H1':>5}{'H2':>5}{'H3':>5}{'H4':>5}{'H5':>5}"
      f"{'LB':>5}{'EXACT':>7}{'spread':>8}")
for nm, n, h1, h2, h3, h4, h5, lb, bb in rows:
    sp = max(h1,h2,h3,h4,h5) - min(h1,h2,h3,h4,h5)
    print(f"  {nm:<20}{n:>7}{h1:>5}{h2:>5}{h3:>5}{h4:>5}{h5:>5}{lb:>5}{bb:>7}{sp:>8}")
print(f"""
  H1 prune-greedy · H2 greedy set cover · H3 H2+prune · H4 randomised, 25 restarts
  H5 reverse-delete · LB disjoint-witness lower bound · EXACT branch and bound""")
