#!/usr/bin/env python3
"""vi_twelve.py -- fit the twelve, not the six.

Register 620: the companion's threshold table prints cells AND reachable under
six thresholds. Nine searches fitted the cells column alone and all nine stalled
at the same +16 / -9 on the NEC interior.

Reachability must be DEFINED before it can be fitted. The companion does not
print its definition, so three candidate readings are tested — each one a
different answer to "can this cell be entered":

  R1  the cell is the head of some admitted implication whose body is admitted
      — reachable = derivable from another cell by the rule set
  R2  the cell has a strictly lower neighbour in the admitted set, coordinatewise
      — reachable = something below it exists
  R3  the cell is not minimal in the admitted set under the product order
      — reachable = it has a predecessor

Each is checked against the six printed reachable counts BEFORE any search runs.
A reading that cannot reproduce them for ANY rule set is discarded.

COMMITTED (§2.13): R3 will come closest, because 174 of 174 NEC = 0 cells being
unreachable reads like a minimality statement rather than a rule statement.
"""
import numpy as np, itertools, json
from zeno import State, step

R = [4, 3, 3, 3, 5, 2, 2, 3, 3]
N = ["X", "S", "IC", "U", "NEC", "L", "SD", "DNc", "DNd"]
B = np.array(list(itertools.product(*[range(r) for r in R])), dtype=np.int16)
COL = [B[:, i] for i in range(9)]
CELLS = np.array([2370, 2196, 1764, 1146, 1374, 558])
REACH = np.array([1410, 1410, 1134, 738, 840, 360])

def slices(m):
    return [m, m & (COL[4] >= 1), m & (COL[4] >= 2),
            m & (COL[4] >= 3), m & (COL[0] >= 2), m & (COL[0] == 3)]

def mask(rs):
    m = np.ones(len(B), bool)
    for body, heads in rs:
        bm = np.ones(len(B), bool)
        for a, va in body: bm &= COL[a] >= va
        h = np.zeros(len(B), bool)
        for b, vb in heads: h |= COL[b] >= vb
        m &= ~(bm & ~h)
    return m

def reach_R2(m):
    """a cell is reachable if some admitted cell is strictly below it"""
    idx = np.where(m)[0]
    pts = B[idx]
    out = np.zeros(len(B), bool)
    # a cell is NOT reachable iff it is minimal: nothing admitted is <= it and !=
    # do it by coordinate sums as a cheap necessary filter, then exact per level
    tot = pts.sum(axis=1)
    order = np.argsort(tot)
    seen = []
    reach_local = np.zeros(len(idx), bool)
    for pos in order:
        p = pts[pos]
        if seen:
            arr = np.array(seen)
            if ((arr <= p).all(axis=1)).any(): reach_local[pos] = True
        seen.append(p)
    out[idx] = reach_local
    return out

def reach_R3(m):
    """a cell is reachable if it is not minimal — equivalently some admitted
    cell differs from it by lowering exactly one coordinate by one"""
    idx = np.where(m)[0]
    S = set(map(tuple, B[idx]))
    out = np.zeros(len(B), bool)
    for j in idx:
        c = tuple(B[j])
        for i in range(9):
            if c[i] > 0:
                d = list(c); d[i] -= 1
                if tuple(d) in S: out[j] = True; break
    return out

def reach_R1(m, rs):
    """a cell is reachable if it satisfies the body of some rule whose head it
    also satisfies — i.e. it is actively placed by the rule set"""
    out = np.zeros(len(B), bool)
    for body, heads in rs:
        bm = np.ones(len(B), bool)
        for a, va in body: bm &= COL[a] >= va
        h = np.zeros(len(B), bool)
        for b, vb in heads: h |= COL[b] >= vb
        out |= (bm & h)
    return out & m

def run():
    j = json.load(open("vi_best.json"))
    rs = [(((r[0], r[1]),), tuple(tuple(x) for x in r[2])) for r in j["rules"]]
    m = mask(rs)
    res = {}
    for lbl, f in (("R1 placed by a rule", lambda: reach_R1(m, rs)),
                   ("R2 something strictly below", lambda: reach_R2(m)),
                   ("R3 has an immediate predecessor", lambda: reach_R3(m))):
        rm = f()
        counts = np.array([int((rm & s).sum()) for s in slices(m)])
        res[lbl] = (counts, int(np.abs(counts - REACH).sum()))
    return res, np.array([int(s.sum()) for s in slices(m)])

with State("vi_twelve") as st:
    res, cellcounts = step(st, "three readings of reachability", run, budget=1700)

print(f"  cells   printed {CELLS.tolist()}")
print(f"          found   {cellcounts.tolist()}\n")
print(f"  reachable, printed {REACH.tolist()}\n")
print(f"  {'reading':<34}{'counts':<40}{'distance':>9}")
for lbl, (c, d) in res.items():
    print(f"  {lbl:<34}{str(c.tolist()):<40}{d:>9}")
best = min(res.items(), key=lambda kv: kv[1][1])
print(f"\n  closest: {best[0]} at distance {best[1][1]}")
