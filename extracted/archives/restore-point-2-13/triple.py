#!/usr/bin/env python3
"""triple.py -- S, W and R: the three parts of the method, and their self-consistency.

Register 1132. The Method equation E(X) = |R(X)| - |X| is ORDINAL. It says which cells an
index admits and does not hold. It cannot say what a cell holds, because its envelopes are
maxima and a value is a magnitude.

Today's spectra work supplied the metric half by hand: a set of steps with measured
factors — 1.07 along Ne, 1.12 along l through Seaton, 1.21 along the isoelectronic
direction. Those were not imposed. They were MEASURED FROM THE INDEX ITSELF, on pairs
where both cells were known.

So the method has three parts, not one:

    S(X)        derive the STEP SET: for every coordinate direction, the ratio between
                adjacent valued cells, its median and its scatter. A direction earns a
                step when its scatter is tight enough to carry a value.

    W(X, S)     the VALUATION closure: every cell reachable from a valued one by steps
                in S, with the accumulated error below a threshold, by the least-error
                route. Extensive and idempotent; monotone except at multiplicative zeros.

    R(X)        the PLACEMENT closure, the book's own operator. Ordinal.

And two defects rather than one:

    E(X)   = |R(X)| - |X|      what the index admits and does not hold      ORDINAL
    E_W(X) = |W(X)| - |X|      what the steps reach and the index has not   METRIC

For Lambda the second is empty, because a cell of Lambda carries no value. That is why
the book never needed it. For an index whose cells carry numbers it is the whole
difficulty.

THE TEST HERE is self-consistency: derive S from the measured cells, run W, then RE-DERIVE
S from the walked result. If the steps come back the same, the triple is stable — the
walk has not invented a structure that its own measurement would not confirm. If they
drift, the walk is manufacturing the regularity it claims to find.
"""
import re, math, statistics as st
from itertools import product
from collections import defaultdict, deque
from zeno import State, step

ZN = {"H":1,"He":2,"Li":3,"Be":4,"B":5,"C":6,"N":7,"O":8,"F":9,"Ne":10,"Na":11,"Mg":12,
      "Al":13,"Si":14,"P":15,"S":16,"Cl":17,"Ar":18,"K":19,"Ca":20,"Sc":21,"Ti":22,
      "Fe":26,"Zn":30,"Ga":31,"Ge":32,"Cd":48,"Ba":56,"Hg":80,"Bi":83}
LM = {"s":0,"p":1,"d":2,"f":3,"g":4,"h":5,"i":6,"k":7}
SUP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹","0123456789")

# the directions a step may take, as coordinate deltas on (Z, charge, l, 2S+1)
DIRS = {"iso":  (1,1,0,0),      # isoelectronic: electron count held
        "elem": (0,1,0,0),      # one element, next charge state
        "ne":   (1,0,0,0),      # one charge state, next element
        "l":    (0,0,1,0),      # next orbital
        "mult": (0,0,0,1)}      # next multiplicity

def load():
    H = defaultdict(list)
    for line in open("SPECTRA-DATA.tsv", encoding="utf-8").read().split("\n")[1:]:
        r = line.rstrip().split("\t")
        if len(r) < 11: continue
        m = re.search(r"n([spdfghik])\b", r[1]); el = re.match(r"([A-Z][a-z]?)", r[0].strip())
        if not (m and el) or el.group(1) not in ZN: continue
        mu = re.search(r"(\d)[SPDFG]", r[1][m.end():].translate(SUP))
        try:
            H[(ZN[el.group(1)], int(r[9]), LM[m.group(1)],
               int(mu.group(1)) if mu else 0)].append(float(r[7]))
        except Exception: pass
    return {k: st.mean(v) for k, v in H.items()}

def S(V, floor=1e-3, tight=1.5, minpairs=4):
    """THE STEP OPERATOR. Measure every direction, at every l, on pairs where both
    cells are valued. Return the ones tight enough to carry a value.

    The threshold is stated, not tuned: a scatter of 1.5 means a walked value is good
    to 50%, and two such steps to a factor of 1.8, which is inside the halt.
    """
    out = {}
    for nm, dv in DIRS.items():
        for l in range(8):
            R = []
            for k, d in V.items():
                if k[2] != l or d <= floor: continue
                t = tuple(k[i] + dv[i] for i in range(4))
                u = V.get(t)
                if u and u > floor: R.append(d/u)
            if len(R) < minpairs: continue
            lg = [math.log(x) for x in R]
            med, sd = math.exp(st.median(lg)), math.exp(st.pstdev(lg))
            if sd <= tight: out[(nm, l)] = (med, sd, len(R))
    return out

def W(V0, steps, ALL, tau=math.log(2.5)):
    """THE VALUATION CLOSURE. Least-error route from the valued set."""
    val = {k: (v, 0.0) for k, v in V0.items()}
    q = deque(V0)
    while q:
        k = q.popleft(); d, lg = val[k]
        if lg > tau: continue
        for nm, dv in DIRS.items():
            s = steps.get((nm, k[2]))
            if not s: continue
            med, sd, _ = s
            for sgn in (1, -1):
                t = tuple(k[i] + sgn*dv[i] for i in range(4))
                if t not in ALL: continue
                nd = d/med if sgn > 0 else d*med
                if nd <= 0: continue
                nl = math.sqrt(lg**2 + math.log(sd)**2)
                if nl > tau: continue
                if t in val and val[t][1] <= nl + 1e-12: continue
                val[t] = (nd, nl); q.append(t)
    return val

def run():
    V = load()
    A = [sorted({x[i] for x in V}) for i in range(4)]
    ALL = {x for x in product(*A) if x[1] < x[0]}
    S1 = S(V)
    W1 = W(V, S1, ALL)
    S2 = S({k: v[0] for k, v in W1.items()})      # re-derive from the walked result
    W2 = W({k: v[0] for k, v in W1.items()}, S2, ALL)
    return V, ALL, S1, W1, S2, W2

with State("triple") as s:
    V, ALL, S1, W1, S2, W2 = step(s, "derive S, run W, re-derive S", run, budget=900)

print("  THE STEP OPERATOR S, DERIVED FROM THE INDEX ITSELF\n")
print(f"  {'direction':<8}{'l':>3}{'pairs':>7}{'median':>9}{'scatter':>9}"
      f"{'  |  re-derived after walking':<30}")
for k in sorted(S1):
    m1, s1, n1 = S1[k]
    r = S2.get(k)
    tail = f"  |  {r[1]:.2f} on {r[2]} pairs" if r else "  |  not re-derived"
    print(f"  {k[0]:<8}{'spdfghik'[k[1]]:>3}{n1:>7}{m1:>9.3f}{s1:>9.2f}{tail}")
print()
print(f"  steps derived from the measured index : {len(S1)}")
print(f"  steps re-derived from the walked one  : {len(S2)}")
kept = len(set(S1) & set(S2))
print(f"  the same direction and l in both      : {kept}")
print()
print(f"  |X| = {len(V)}   |W(X)| = {len(W1)}   |W(W(X))| = {len(W2)}")
print(f"  E_W(X) = |W(X)| - |X| = {len(W1)-len(V)}")
print(f"  idempotent: {set(W2) == set(W1)}")
