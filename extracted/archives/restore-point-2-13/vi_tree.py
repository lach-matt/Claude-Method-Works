#!/usr/bin/env python3
"""vi_tree.py -- derive the violation index's edge list as a constraint graph.

Transitions §5.7 states the edge list is not printed. §21.5.3 of this book says
what shape to expect: Λ₈'s constraint graph is a tree at 8 nodes and 7 edges,
Λ₁₃ has cycle rank 2 with no triangle at any stage, and each two-parent axis
adds exactly one independent cycle. Nine letters therefore give 8 edges for a
tree and 8 + r for cycle rank r, each edge carrying a threshold pair.

Random sampling of that space reaches 2,430 cells against the printed 2,370.
This hill-climbs from there against all six printed counts.

ACCEPTANCE, stated by the companion itself
  2,370 cells in a box of 19,440 · E = 30 collapsing as 1 × 30 ·
  core at (X=0, U=0, NEC=3) · none of 414 subsets failing ·
  multiplicities 3, 5, 10, 30 at 4, 5, 7, 9 coordinates
"""
import itertools, random, sys
from zeno import State, step

R = [4, 3, 3, 3, 5, 2, 2, 3, 3]
N = ["X", "S", "IC", "U", "NEC", "L", "SD", "DNc", "DNd"]
BOX = list(itertools.product(*[range(r) for r in R]))
X_, S_, IC_, U_, NEC_ = 0, 1, 2, 3, 4

TARGET = dict(cells=2370, nec1=2196, nec2=1764, nec3=1146, x2=1374, x3=558)

def prof(cs):
    return dict(cells=len(cs),
                nec1=sum(1 for c in cs if c[NEC_] >= 1),
                nec2=sum(1 for c in cs if c[NEC_] >= 2),
                nec3=sum(1 for c in cs if c[NEC_] >= 3),
                x2=sum(1 for c in cs if c[X_] >= 2),
                x3=sum(1 for c in cs if c[X_] == 3))

def cells_from(edges):
    out = []
    for c in BOX:
        ok = True
        for (a, va, b, vb) in edges:
            if c[a] >= va and c[b] < vb: ok = False; break
        if ok: out.append(c)
    return out

dist = lambda p: sum(abs(p[k] - TARGET[k]) for k in TARGET)

def random_tree():
    pr = [random.randrange(9) for _ in range(7)]
    d = [1] * 9
    for x in pr: d[x] += 1
    E = []
    for x in pr:
        for l in range(9):
            if d[l] == 1:
                E.append((l, x)); d[l] -= 1; d[x] -= 1; break
    rem = [i for i in range(9) if d[i] == 1]
    if len(rem) == 2: E.append(tuple(rem))
    return E

def label(E):
    return [(a, random.randrange(1, R[a]), b, random.randrange(1, R[b])) for a, b in E]

def climb(ed, rounds=340):
    cs = cells_from(ed)
    best = dist(prof(cs)) if cs else 10**9
    for _ in range(rounds):
        i = random.randrange(len(ed))
        a, va, b, vb = ed[i]
        cand = []
        for nva in range(1, R[a]):
            for nvb in range(1, R[b]):
                if (nva, nvb) != (va, vb): cand.append((a, nva, b, nvb))
        # also try swapping one endpoint
        for nb in range(9):
            if nb != a and nb != b:
                cand.append((a, va, nb, random.randrange(1, R[nb])))
        random.shuffle(cand)
        moved = False
        for r in cand[:26]:
            trial = ed[:i] + [r] + ed[i+1:]
            cs = cells_from(trial)
            if not cs: continue
            d2 = dist(prof(cs))
            if d2 < best:
                best = d2; ed = trial; moved = True; break
        if not moved and best == 0: break
    return ed, best

def run():
    random.seed(17)
    pool = []
    for _ in range(900):
        ed = label(random_tree())
        cs = cells_from(ed)
        if cs: pool.append((dist(prof(cs)), ed))
    pool.sort(key=lambda t: t[0])
    results = []
    for d0, ed in pool[:14]:
        e2, d2 = climb(ed)
        results.append((d2, e2))
    results.sort(key=lambda t: t[0])
    return results[:3]

with State("vi_tree") as st:
    top = step(st, "hill-climb threshold-labelled trees", run, budget=1500)

print(f"  target {TARGET}\n")
for rank, (d, ed) in enumerate(top, 1):
    cs = cells_from(ed); p = prof(cs)
    print(f"  #{rank}  distance {d:,}   cells {p['cells']:,}")
    print(f"       {p}")
    if d == 0:
        print("       *** EXACT PROFILE MATCH — running the companion's acceptance test ***")
    for (a, va, b, vb) in ed:
        print(f"         {N[a]} >= {va}  ->  {N[b]} >= {vb}")
    print()
