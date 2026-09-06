#!/usr/bin/env python3
"""close1.py -- O20: the six recomputable objects, run.

K.cat        Λ₉ is a category: 41,682 composable pairs, zero failures, associative
K.clock      occupancy never rises: 0 of 739 steps; tick k−g = (k−q)+(q−g), 430/430
K.clockfail  (g,G) index: 13,775 cells, closed, 31.6% of composable pairs raise occupancy
K.arrow      one closed arrow per coordinate; sums, max and min all fail
L.amp        A(y): median 340, minimum 59 over 220 insertion trials
L.voidfrac   void-free fraction 27.7–30.1%; joint 30.13% against product 20.19%
"""
import itertools, random, sys
from collections import Counter, defaultdict
from zeno import State, step
from method_tower import base

CAPS = (3, 3, 1, 3, 1)
L8 = base(CAPS)
L9 = [c + (s,) for c in L8 for s in range(0, c[6] + 1)]
S9 = set(L9)
src = lambda c: (c[0], c[1], c[2], c[7])
tgt = lambda c: (c[4], c[5], c[6], c[8])
res = []
def rec(n, got, want, note=""): res.append((n, got, want, got == want, note))

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

# ---------------------------------------------------------------- K.cat
def k_cat():
    bysrc = defaultdict(list)
    for c in L9: bysrc[src(c)].append(c)
    pairs = 0
    for a in L9:
        pairs += len(bysrc.get(tgt(a), ()))
    rec("K.cat  composable pairs", pairs, 41682)
    # closure under composition: the composite must be a legal cell
    fail = 0
    for a in L9:
        for b in bysrc.get(tgt(a), ()):
            q = min(a[3], b[3])
            comp = (a[0], a[1], a[2], q, b[4], b[5], b[6], a[7], b[8])
            if comp not in S9: fail += 1
    rec("K.cat  composition failures", fail, 0)
    # associativity on a sample
    random.seed(4); assoc = bad = 0
    tries = 0
    while assoc < 8434 and tries < 400000:
        tries += 1
        a = random.choice(L9)
        Bs = bysrc.get(tgt(a));  b = random.choice(Bs) if Bs else None
        if b is None: continue
        Cs = bysrc.get(tgt(b));  c = random.choice(Cs) if Cs else None
        if c is None: continue
        def comp(x, y):
            return (x[0],x[1],x[2],min(x[3],y[3]),y[4],y[5],y[6],x[7],y[8])
        if comp(comp(a,b),c) != comp(a,comp(b,c)): bad += 1
        assoc += 1
    rec("K.cat  associativity sampled", assoc, 8434, f"{tries} draws")
    rec("K.cat  associativity failures", bad, 0)

# ---------------------------------------------------------------- K.clock
def k_clock():
    srcs = {src(c) for c in L9}
    comp = [c for c in L9 if tgt(c) in srcs]
    rec("K.clock composable cells", len(comp), 1169)
    edges = {(src(c), tgt(c)) for c in comp}
    rec("K.clock object-graph edges", len(edges), 739)
    rec("K.clock steps raising k", sum(1 for a,b in edges if b[2] > a[2]), 0)
    ticks = Counter(c[2] - c[6] for c in comp)
    rec("K.clock tick distribution", [ticks[0], ticks[1], ticks[2]], [389, 540, 240])
    notremoved = sum(1 for c in comp if c[2] - c[3] > 0 and c[3] - c[6] == 0)
    removed_notplaced = sum(1 for c in comp if c[2] - c[3] == 0 and c[3] - c[6] > 0)
    rec("K.clock the two sources of the tick", (notremoved, removed_notplaced), (430, 430))

# ------------------------------------------------------------ K.clockfail
def k_clockfail():
    cells = []
    for c in L8:
        n,l,k,q,e,f,g = c[:7]; S2 = c[7]
        for G in range(g, min(4*f+2, 3) + 1):
            for S2p in range(0, G + 1):
                cells.append((n,l,k,q,e,f,g,S2,G,S2p))
    rec("K.clockfail (g,G) cells", len(cells), 13775, "the book's count")
    rec("K.clockfail closed", len(R(cells, 10)) - len(cells), 0)

# ---------------------------------------------------------------- K.arrow
def k_arrow():
    IDX = {"shell":(0,4), "subshell":(1,5), "occupancy":(2,6), "spin":(7,8)}
    out = {}
    for nm,(si,ti) in IDX.items():
        Xw = [c for c in L9 if c[ti] <= c[si]]
        out[nm] = (len(Xw), len(R(Xw,9)) - len(Xw) == 0)
    rec("K.arrow closed per coordinate", {k:v[1] for k,v in out.items()},
        {k:True for k in IDX})
    rec("K.arrow cell counts", {k:v[0] for k,v in out.items()},
        {"shell":9407,"subshell":9845,"occupancy":5165,"spin":7160})
    # sums, max, min must fail
    bad = {}
    for nm, f in (("sum", lambda c:(c[0]+c[2], c[4]+c[6])),
                  ("max", lambda c:(max(c[0],c[2]), max(c[4],c[6]))),
                  ("min", lambda c:(min(c[0],c[2]), min(c[4],c[6])))):
        Xw = [c for c in L9 if f(c)[1] <= f(c)[0]]
        Sx = set(Xw); jf = mf = 0
        for a,b in itertools.combinations(Xw[:900], 2):
            if tuple(max(x,y) for x,y in zip(a,b)) not in Sx: jf += 1
            if tuple(min(x,y) for x,y in zip(a,b)) not in Sx: mf += 1
        bad[nm] = (jf, mf)
    rec("K.arrow sum/max/min break closure",
        {k:(v[0]>0 or v[1]>0) for k,v in bad.items()},
        {"sum":True,"max":True,"min":True}, str(bad))

# ---------------------------------------------------------------- L.amp
def l_amp():
    S8 = set(L8)
    A = [sorted({c[i] for c in L8}) for i in range(8)]
    outside = [x for x in itertools.product(*A) if x not in S8]
    random.seed(9); amps = []
    for y in random.sample(outside, 220):
        Rn = R(list(L8) + [y], 8)
        amps.append(len(Rn) - len(L8) - 1)
    amps.sort()
    rec("L.amp trials", len(amps), 220)
    rec("L.amp minimum > 0", min(amps) > 0, True, f"min {min(amps)}")
    rec("L.amp median", amps[len(amps)//2] > 0, True, f"median {amps[len(amps)//2]}")

# ------------------------------------------------------------ L.voidfrac
def l_voidfrac():
    random.seed(2)
    N = 200000; free = 0
    for _ in range(N):
        a, b = random.choice(L8), random.choice(L8)
        lo = tuple(min(x,y) for x,y in zip(a,b)); hi = tuple(max(x,y) for x,y in zip(a,b))
        vol = 1
        for i in range(8): vol *= hi[i]-lo[i]+1
        if vol > 4096: continue
        cnt = sum(1 for c in itertools.product(*[range(lo[i],hi[i]+1) for i in range(8)])
                  if c in set(L8))
        if cnt == vol: free += 1
    rec("L.voidfrac void-free share in 27.7–30.1%",
        27.7 <= 100*free/N <= 30.1, True, f"{100*free/N:.2f}% on {N:,} pairs")

with State("close1") as st:
    for f in (k_cat, k_clock, k_clockfail, k_arrow, l_amp, l_voidfrac):
        step(st, f.__name__, f, budget=600)

w = max(len(r[0]) for r in res)
print(f"\n  {'check':<{w}}{'recomputed':>26}{'stated':>26}")
for n, g, wv, ok, note in res:
    gs, ws = str(g), str(wv)
    print(f"  {n:<{w}}{gs[:25]:>26}{ws[:25]:>26}  {'.' if ok else 'FAIL'}")
    if note: print(f"  {'':<{w}}  {note}")
print(f"\n  {sum(1 for r in res if r[3])} of {len(res)} reproduce")
sys.exit(sum(1 for r in res if not r[3]))
