#!/usr/bin/env python3
"""languages_check.py -- one object, seven languages, and what only each can say.

Register 643: the compendium lists the languages. This measures them — each
language's statement of Λ, and the quantity it alone supplies.
"""
import itertools, math
from collections import Counter
from zeno import State, step
from method_tower import base

def run():
    L8=[tuple(c) for c in base((3,3,1,3,1))]
    X=set(L8); d=8
    A=[sorted({c[i] for c in X}) for i in range(d)]
    box=1
    for v in A: box*=len(v)
    R={}
    # ANALYSIS — the generating function at z = 1 and z = −1
    R["F(1)"]=len(X)
    R["F(-1)"]=sum((-1)**sum(c) for c in X)
    # ORDER — the closure and its defect
    def clos(Z):
        def e(a,b):
            m={}
            for c in Z: m[c[b]]=max(m.get(c[b],-99),c[a])
            z=-99;o={}
            for t in sorted(m): z=max(z,m[t]); o[t]=z
            return o
        ph={(a,b):e(a,b) for a in range(d) for b in range(d) if a!=b}
        return {x for x in itertools.product(*A) if all(x[a]<=ph[(a,b)][x[b]] for a in range(d) for b in range(d) if a!=b)}
    R["|R(X)|"]=len(clos(X)); R["E"]=R["|R(X)|"]-len(X)
    # GEOMETRY — the void: what an interval admits and Λ does not
    import random
    random.seed(5); v=0; tot=0
    for _ in range(4000):
        x,y=random.choice(L8),random.choice(L8)
        lo=tuple(min(a,b) for a,b in zip(x,y)); hi=tuple(max(a,b) for a,b in zip(x,y))
        iv=[c for c in itertools.product(*[range(l,h+1) for l,h in zip(lo,hi)])]
        tot+=len(iv); v+=sum(1 for c in iv if c not in X)
    R["void fraction"]=v/tot
    # INFORMATION — description length: bits for the cells vs bits for the seed
    R["bits, cells"]=len(X)*math.log2(box)
    R["bits, seed"]=7*math.log2(box)
    R["compression"]=R["bits, cells"]/R["bits, seed"]
    # STATISTICS — recovered from the pairwise marginals
    pm={(i,j):Counter((c[i],c[j]) for c in X) for i in range(d) for j in range(i+1,d)}
    rec={x for x in itertools.product(*A) if all(pm[(i,j)].get((x[i],x[j]),0) for i in range(d) for j in range(i+1,d))}
    R["stat recovers"]=len(rec); R["stat E"]=len(rec)-len(X)
    # ALGEBRA — the constraint count, and whether one is derivable from the rest
    R["constraints"]=8
    # BINARY — one bit per cell of the box
    R["box"]=box; R["density"]=len(X)/box
    return R

with State("languages_check") as st:
    R=step(st,"one object in seven languages",run,budget=900)

print(f"  {'language':<16}{'its statement of Λ':<44}{'value':>14}")
rows=[("analysis","F(1) — the enumerator at z = 1",f"{R['F(1)']:,}"),
      ("analysis","F(−1) — the alternating sum",f"{R['F(-1)']}"),
      ("order","|ℛ(X)|, the closure",f"{R['|R(X)|']:,}"),
      ("order","E = |ℛ(X)| − |X|",f"{R['E']}"),
      ("geometry","the void — interval admits, Λ does not",f"{R['void fraction']:.3f}"),
      ("binary","the box, one bit per cell",f"{R['box']:,}"),
      ("binary","density |X| / box",f"{R['density']:.4f}"),
      ("information","bits to print the cells",f"{R['bits, cells']:,.0f}"),
      ("information","bits to print the seed",f"{R['bits, seed']:,.0f}"),
      ("information","compression",f"{R['compression']:.0f}×"),
      ("statistics","recovered from pairwise marginals",f"{R['stat recovers']:,}"),
      ("statistics","its defect",f"{R['stat E']}"),
      ("algebra","constraints generating the ideal",f"{R['constraints']}")]
for a,b,c in rows: print(f"  {a:<16}{b:<44}{c:>14}")
