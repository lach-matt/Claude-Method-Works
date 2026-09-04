#!/usr/bin/env python3
"""vi_final.py -- the edge list, searched against a confirmed space.

Register 615: the printed rungs (4,3,3,3,5,2,2,3,3) and the >= reading are
correct — every alternative is two orders of magnitude worse. So the residual of
29 is a different RULE SET, not a misread axis.

The recorded best holds cells at exactly 2,370 and misses only on the NEC
interior: NEC>=2 at 1,780 against 1,764 (sixteen too high) and NEC>=3 at 1,137
against 1,146 (nine too low). This search is targeted at that: it weights the
two NEC counts and preserves the exact cell total.

Seeded from vi_best.json (register 591: never search this blind).
"""
import numpy as np, itertools, random, json
from zeno import State, step

R = [4, 3, 3, 3, 5, 2, 2, 3, 3]
N = ["X", "S", "IC", "U", "NEC", "L", "SD", "DNc", "DNd"]
B = np.array(list(itertools.product(*[range(r) for r in R])), dtype=np.int8)
COL = [B[:, i] for i in range(9)]
T = np.array([2370, 2196, 1764, 1146, 1374, 558])
# the two counts carrying the whole residual get triple weight; cells stays exact
W = np.array([4, 1, 3, 3, 1, 1])

def prof(m):
    return np.array([m.sum(), (m & (COL[4] >= 1)).sum(), (m & (COL[4] >= 2)).sum(),
                     (m & (COL[4] >= 3)).sum(), (m & (COL[0] >= 2)).sum(),
                     (m & (COL[0] == 3)).sum()])

def mk(r):
    body, heads = r
    bm = np.ones(len(B), bool)
    for a, va in body: bm &= COL[a] >= va
    h = np.zeros(len(B), bool)
    for b, vb in heads: h |= COL[b] >= vb
    return ~(bm & ~h)

def mask(rs):
    m = np.ones(len(B), bool)
    for r in rs: m &= mk(r)
    return m

raw = lambda p: int(np.abs(p - T).sum())
wt  = lambda p: int((np.abs(p - T) * W).sum())

def load():
    j = json.load(open("vi_best.json"))
    return [(((r[0], r[1]),), tuple(tuple(x) for x in r[2])) for r in j["rules"]]

def rand_rule():
    k = random.choice([1, 1, 1, 2, 2, 3])
    ba = random.sample(range(9), k)
    body = tuple((a, random.randrange(1, R[a])) for a in ba)
    pool = [b for b in range(9) if b not in ba] or list(range(9))
    hs = random.sample(pool, random.choice([1, 1, 2, 3]))
    return (body, tuple((b, random.randrange(1, R[b])) for b in hs))

def climb(rs, rounds, T0=6.0):
    cur = list(rs); m = mask(cur)
    bw = wt(prof(m)); best = (raw(prof(m)), list(cur))
    for t in range(rounds):
        temp = T0 * (1 - t / rounds) + 0.01
        i = random.randrange(len(cur))
        op = random.random()
        if op < 0.55: trial = cur[:i] + [rand_rule()] + cur[i+1:]
        elif op < 0.82 and len(cur) < 30: trial = cur + [rand_rule()]
        elif len(cur) > 10: trial = cur[:i] + cur[i+1:]
        else: trial = cur[:i] + [rand_rule()] + cur[i+1:]
        m2 = mask(trial)
        if not m2.sum(): continue
        p2 = prof(m2); w2 = wt(p2)
        if w2 <= bw or random.random() < pow(2.718, -(w2 - bw) / temp):
            cur, bw = trial, w2
            if raw(p2) < best[0]: best = (raw(p2), list(trial))
    return best

def run():
    random.seed(53)
    seed = load()
    best = (raw(prof(mask(seed))), seed)
    for r in range(26):
        start = best[1] if r % 3 else [rand_rule() for _ in range(random.choice([17, 20, 24]))]
        if not mask(start).sum(): continue
        got = climb(start, 6000)
        if got[0] < best[0]: best = got
        if best[0] == 0: break
    return best

with State("vi_final") as st:
    d, rs = step(st, "targeted search on the confirmed space", run, budget=1700)

m = mask(rs); p = prof(m)
print(f"  rules {len(rs)}   distance {d}   (recorded best: 29)")
print(f"    target {T.tolist()}")
print(f"    found  {p.tolist()}")
print(f"    per-count miss: {(p - T).tolist()}")
print(f"    EXACT: {d == 0}")
if d < 29:
    json.dump({"d": d, "rules": [[list(map(list, b)), list(map(list, h))] for b, h in rs],
               "prof": p.tolist()}, open("vi_best2.json", "w"))
    print("    improved — saved to vi_best2.json")
    for body, heads in rs:
        print("      " + " and ".join(f"{N[a]}>={va}" for a, va in body)
              + "  ->  " + " or ".join(f"{N[b]}>={vb}" for b, vb in heads))
