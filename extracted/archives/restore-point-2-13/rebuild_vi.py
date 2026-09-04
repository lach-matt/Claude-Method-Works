#!/usr/bin/env python3
"""rebuild_vi.py -- reconstruct the violation index from its printed figures.

Transitions §5.1 prints the nine axes and their rungs; §5.3, §5.6 and §5.7 print
eleven counts. §5.7 states that the edge list constrains the free letters and does
not print it. This searches the space of implication sets for one that reproduces
every printed figure.

  box        4·3·3·3·5·2·2·3·3 = 19,440
  cells      2,370
  E          30, collapsing as 1 × 30, core (X=0, U=0, NEC=3)
  thresholds NEC≥1 2,196 · NEC≥2 1,764 · NEC≥3 1,146 · X≥2 1,374 · X=3 558
  payers     of the 1,146 at NEC≥3: 1,116 preferred frame, 714 non-unitary,
             756 signalling, 0 none
"""
import itertools, sys
from zeno import State, step

R = [4, 3, 3, 3, 5, 2, 2, 3, 3]
N = ["X", "S", "IC", "U", "NEC", "L", "SD", "DNc", "DNd"]
X, S, IC, U, NEC, L, SD, DNc, DNd = range(9)
BOX = [c for c in itertools.product(*[range(r) for r in R])]

TARGET = dict(cells=2370, nec1=2196, nec2=1764, nec3=1146, x2=1374, x3=558)

def profile(cells):
    return dict(cells=len(cells),
                nec1=sum(1 for c in cells if c[NEC] >= 1),
                nec2=sum(1 for c in cells if c[NEC] >= 2),
                nec3=sum(1 for c in cells if c[NEC] >= 3),
                x2=sum(1 for c in cells if c[X] >= 2),
                x3=sum(1 for c in cells if c[X] == 3))

# candidate implications: (a, va) -> (b, vb)  meaning  c[a] >= va implies c[b] >= vb
CAND = []
for a in range(9):
    for b in range(9):
        if a == b: continue
        for va in range(1, R[a]):
            for vb in range(1, R[b]):
                CAND.append((a, va, b, vb))

def apply(rules, cells):
    out = []
    for c in cells:
        ok = True
        for (a, va, b, vb) in rules:
            if c[a] >= va and c[b] < vb: ok = False; break
        if ok: out.append(c)
    return out

def run():
    # single rules first: which come closest to the NEC/X profile shape?
    singles = []
    for r in CAND:
        cs = apply([r], BOX)
        if 2370 <= len(cs) <= 19440:
            singles.append((len(cs), r))
    singles.sort()
    # a rule set must cut 19,440 to 2,370 — a factor of 8.2
    # search pairs and triples of the most-cutting rules for the exact profile
    strong = [r for n, r in singles if n <= 12000][:120]
    hits = []
    for k in (2, 3):
        for combo in itertools.combinations(strong, k):
            cs = apply(list(combo), BOX)
            if len(cs) != 2370: continue
            p = profile(cs)
            if p == TARGET: hits.append((combo, p))
            elif p["cells"] == 2370: hits.append((combo, p))
        if hits: break
    return singles[:8], hits

with State("rebuild_vi") as st:
    singles, hits = step(st, "search implication sets", run, budget=1500)

print(f"  box {len(BOX):,}   target {TARGET}\n")
print(f"  single rules cutting hardest:")
for n, r in singles[:8]:
    a, va, b, vb = r
    print(f"    {N[a]} ≥ {va} → {N[b]} ≥ {vb}   leaves {n:,}")
print(f"\n  rule sets reaching exactly 2,370 cells: {len(hits)}")
for combo, p in hits[:6]:
    print(f"    {[f'{N[a]}≥{va}→{N[b]}≥{vb}' for a,va,b,vb in combo]}")
    print(f"      profile {p}")
    print(f"      matches every printed count: {p == TARGET}")
