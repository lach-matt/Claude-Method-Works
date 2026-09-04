#!/usr/bin/env python3
"""redundancy.py -- how much of each index determines the rest?

Register 1119. Today's spectra work produced a measurement that applies to every index
the book holds and has never been made for any of them: REDUNDANCY UNDER R.

Remove cells at random and ask whether R puts them back. Lambda recovers exactly after
61% of its cells are gone; the spectra index tolerates about 25%. The difference is the
number of coordinate pairs that actually constrain each other — Lambda's coordinates are
tightly coupled (l < n, k <= 4l+2, e <= k) so every envelope phi(i,j) carries a great
deal, while the spectra index has one constraint, charge < Z, and an l free of both.

This measures it for every index that can be reconstructed here, and reports two numbers:

    REDUNDANCY   the largest fraction that can be removed with exact recovery in
                 at least 8 of 10 trials
    COUPLING     the fraction of ordered coordinate pairs (i,j) whose envelope
                 phi(i,j) is non-trivial — that is, actually constrains

The conjecture the spectra work suggests is that these two track each other. That is
tested here rather than assumed, and on indices built for entirely different purposes.
"""
import random, math, statistics as st
from itertools import product
from zeno import State, step

def RR(X, d):
    X = set(X)
    if not X: return X
    vals = [sorted({c[i] for c in X}) for i in range(d)]
    def env(i, j):
        m = {}
        for c in X: m[c[j]] = max(m.get(c[j], -99), c[i])
        b, o = -99, {}
        for t in sorted(m): b = max(b, m[t]); o[t] = b
        return o
    phi = {(i,j): env(i,j) for i in range(d) for j in range(d) if i != j}
    return {x for x in product(*vals)
            if all(x[i] <= phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i != j)}

def coupling(X, d):
    """the fraction of ordered coordinate pairs whose envelope actually constrains.

    An envelope phi(i,j) is TRIVIAL if it equals max(coordinate i) everywhere — it
    then admits every value of i regardless of j, and carries nothing.
    """
    X = set(X); live = 0; tot = 0
    for i in range(d):
        hi = max(c[i] for c in X)
        for j in range(d):
            if i == j: continue
            tot += 1
            m = {}
            for c in X: m[c[j]] = max(m.get(c[j], -99), c[i])
            b, o = -99, []
            for t in sorted(m): b = max(b, m[t]); o.append(b)
            if any(v < hi for v in o): live += 1
    return live / tot if tot else 0.0

def redundancy(X, d, seed=20260809):
    """the largest removable fraction with exact recovery in 8 of 10 trials"""
    random.seed(seed); X = sorted(set(X)); N = len(X); best = 0.0
    for frac in (0.05,0.10,0.20,0.30,0.41,0.50,0.61,0.70,0.82,0.90):
        k = int(N*frac)
        if k < 1 or N-k < d: break
        ok = 0
        T = 10 if N < 3000 else 5
        for _ in range(T):
            if RR(random.sample(X, N-k), d) == set(X): ok += 1
        if ok >= (0.8*T): best = frac
        else: break
    return best

def indices():
    """every index this session can reconstruct, with its dimension"""
    out = {}
    from method_tower import base
    L = base((3,3,1,3,1))
    out["Λ  (the elemental index)"] = (set(L), 8)
    # the spectra index
    import re
    from collections import defaultdict
    ZN = {"H":1,"He":2,"Li":3,"Be":4,"B":5,"C":6,"N":7,"O":8,"F":9,"Ne":10,"Na":11,
          "Mg":12,"Al":13,"Si":14,"P":15,"S":16,"Cl":17,"Ar":18,"K":19,"Ca":20,
          "Sc":21,"Ti":22,"Fe":26,"Zn":30,"Ga":31,"Ge":32,"Cd":48,"Ba":56,"Hg":80,"Bi":83}
    LM = {"s":0,"p":1,"d":2,"f":3,"g":4,"h":5,"i":6,"k":7}
    held = set()
    for line in open("SPECTRA-DATA.tsv", encoding="utf-8").read().split("\n")[1:]:
        r = line.rstrip().split("\t")
        if len(r) < 11: continue
        m = re.search(r"n([spdfghik])\b", r[1]); el = re.match(r"([A-Z][a-z]?)", r[0].strip())
        if not (m and el) or el.group(1) not in ZN: continue
        try: held.add((ZN[el.group(1)], int(r[9]), LM[m.group(1)]))
        except Exception: pass
    Zs = sorted({k[0] for k in held}); Cs = sorted({k[1] for k in held}); Ls = sorted({k[2] for k in held})
    out["Λ_spectra"] = ({(Z,c,l) for Z in Zs for c in Cs for l in Ls if c < Z}, 3)
    # the periodic table, (period, group)
    out["the periodic table"] = ({(p,g) for p in range(1,8) for g in range(1,19)
                                  if not (p==1 and 2<=g<=17)}, 2)
    # Janet, (n+l, Z)
    jan = set()
    for Z in range(1,119):
        nl = 1
        c = Z
        while c > 0:
            for n in range(1, nl+1):
                l = nl - n
                if l >= n: continue
                cap = 2*(2*l+1)
                if c <= 0: break
                jan.add((nl, Z)); c -= cap
            nl += 1
            if nl > 8: break
    out["Janet"] = (jan, 2)
    # the calendar
    D = [31,29,31,30,31,30,31,31,30,31,30,31]
    out["the calendar"] = ({(m+1,d+1) for m in range(12) for d in range(D[m])}, 2)
    # a box ordering, l >= w >= h
    out["a box ordering"] = ({(a,b,c) for a in range(1,6) for b in range(1,6)
                              for c in range(1,6) if a>=b>=c}, 3)
    return out

with State("redundancy") as s:
    IX  = step(s, "reconstruct every index", indices, budget=600)
    res = step(s, "measure coupling and redundancy",
               lambda: {k: (len(v[0]), v[1], coupling(v[0],v[1]),
                            len(RR(v[0],v[1]))-len(v[0]), redundancy(v[0],v[1]))
                        for k,v in IX.items()}, budget=1700)

print("  REDUNDANCY AND COUPLING, FOR EVERY INDEX THE BOOK HOLDS\n")
print("  coupling  = the fraction of ordered coordinate pairs whose envelope constrains")
print("  redundancy = the largest fraction removable with exact recovery\n")
print(f"  {'index':<28}{'cells':>8}{'dim':>5}{'E':>8}{'coupling':>10}{'redundancy':>12}")
for k,(n,d,cp,E,rd) in sorted(res.items(), key=lambda x:-x[1][4]):
    print(f"  {k:<28}{n:>8,}{d:>5}{E:>8,}{100*cp:>9.0f}%{100*rd:>11.0f}%")
print()
xs = [v[2] for v in res.values()]; ys = [v[4] for v in res.values()]
if len(xs) > 2:
    from scipy import stats
    r = stats.linregress(xs, ys)
    print(f"  redundancy against coupling: r² = {r.rvalue**2:.3f}, p = {r.pvalue:.4f}")
    print(f"      {'they track each other' if r.pvalue < 0.05 else 'no relation established'}")
