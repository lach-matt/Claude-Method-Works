#!/usr/bin/env python3
"""vi_edges.py -- the violation index's edge list, derived.

Under zeno. Register 588 reached distance 288 at eight rules with disjunctive
heads, closing NEC >= 3 to within six of the printed 1,146. The residual sits in
NEC >= 1 at 2,112 against 2,196. This widens past eight rules and seeds from the
two-disjunction candidate.

ACCEPTANCE, stated by the companion itself
  2,370 cells in a box of 19,440 . E = 30 collapsing as 1 x 30 .
  core at (X=0, U=0, NEC=3) . none of 414 subsets failing .
  multiplicities 3, 5, 10, 30 at 4, 5, 7, 9 coordinates
"""
import numpy as np, itertools, random
from zeno import State, step

R = [4, 3, 3, 3, 5, 2, 2, 3, 3]
N = ["X", "S", "IC", "U", "NEC", "L", "SD", "DNc", "DNd"]
B = np.array(list(itertools.product(*[range(r) for r in R])), dtype=np.int8)
COL = [B[:, i] for i in range(9)]
T = np.array([2370, 2196, 1764, 1146, 1374, 558])

def prof(m):
    return np.array([m.sum(), (m & (COL[4] >= 1)).sum(), (m & (COL[4] >= 2)).sum(),
                     (m & (COL[4] >= 3)).sum(), (m & (COL[0] >= 2)).sum(),
                     (m & (COL[0] == 3)).sum()])

def mk(r):
    a, va, heads = r
    h = np.zeros(len(B), bool)
    for b, vb in heads: h |= COL[b] >= vb
    return ~((COL[a] >= va) & ~h)

def mask(rs):
    m = np.ones(len(B), bool)
    for r in rs: m &= mk(r)
    return m

d = lambda p: int(np.abs(p - T).sum())

# register 588's best candidate, as the seed
SEED = [(5,1,((4,2),)), (6,1,((2,2),)), (4,4,((2,1),)), (8,1,((0,1),(1,1))),
        (0,2,((8,1),(3,2),(4,1))), (3,2,((8,1),)), (1,1,((6,1),)), (6,1,((7,2),))]

def rand_rule():
    a = random.randrange(9); va = random.randrange(1, R[a])
    k = random.choice([1, 1, 1, 2, 3])
    hs = random.sample([b for b in range(9) if b != a], k)
    return (a, va, tuple((b, random.randrange(1, R[b])) for b in hs))

def climb(rs, rounds):
    bd = d(prof(mask(rs))); cur = list(rs)
    for _ in range(rounds):
        moved = False
        op = random.random()
        for _ in range(34):
            if op < 0.55 and cur:                       # replace a rule
                i = random.randrange(len(cur)); t = cur[:i] + [rand_rule()] + cur[i+1:]
            elif op < 0.8 and len(cur) < 26:            # add a rule
                t = cur + [rand_rule()]
            elif len(cur) > 5:                          # drop a rule
                i = random.randrange(len(cur)); t = cur[:i] + cur[i+1:]
            else:
                i = random.randrange(len(cur)); t = cur[:i] + [rand_rule()] + cur[i+1:]
            m = mask(t)
            if not m.sum(): continue
            dd = d(prof(m))
            if dd < bd: bd = dd; cur = t; moved = True; break
        if bd == 0: break
        if not moved and random.random() < 0.75: break
    return bd, cur

def run():
    random.seed(131)
    best = climb(SEED, 9000)
    pool = []
    for _ in range(40000):
        k = random.choice([12,14,16,18,20])
        rs = [rand_rule() for _ in range(k)]
        m = mask(rs)
        if m.sum(): pool.append((d(prof(m)), rs))
    pool.sort(key=lambda t: t[0])
    for d0, rs in pool[:300]:
        r = climb(rs, 9000)
        if r[0] < best[0]: best = r
        if best[0] == 0: break
    return best

with State("vi_edges3") as st:
    bd, rs = step(st, "widen the disjunctive edge search", run, budget=3000)

m = mask(rs); p = prof(m)
print(f"  rules {len(rs)}   distance {bd:,}   (register 588 reached 288 at eight rules)")
print(f"    target {T.tolist()}")
print(f"    found  {p.tolist()}")
print(f"    EXACT PROFILE: {bd == 0}\n")
for a, va, hs in rs:
    print(f"      {N[a]} >= {va}  ->  " + " or ".join(f"{N[b]} >= {vb}" for b, vb in hs))
if bd == 0:
    print("\n  *** running the companion's remaining acceptance figures ***")
    cells = B[m]
    core = (cells[:, 0] == 0) & (cells[:, 3] == 0) & (cells[:, 4] == 3)
    print(f"    cells at the core (X=0, U=0, NEC=3): {core.sum()}")
