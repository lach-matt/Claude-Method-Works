#!/usr/bin/env python3
"""lam10_gap.py -- what are the 485 non-composable cells of Lambda-10?

Register 625: composability peaks at Lambda-10, 2,050 of 2,535 = 80.87%. This
defines the other 19.13% — the cells whose target signature is no cell's source.

PREDICTION (§2.13): they will concentrate at the caps. A target that no source
matches is a target the tower cannot re-enter, and the tower's boundary is where
re-entry fails.
"""
import itertools
from collections import Counter
from zeno import State, step
from method_tower import base

def run():
    L8=[tuple(c) for c in base((3,3,1,3,1))]
    L9=[c+(s,) for c in L8 for s in range(0,c[6]+1)]
    L10=[c+(v,) for c in L9 for v in range(c[8],c[6]+1)]
    SRC={(c[0],c[1],c[2],c[7]) for c in L10}
    bad=[c for c in L10 if (c[4],c[5],c[6],c[8]) not in SRC]
    N=["n","l","k","q","e","f","g","2S","2S'","v"]
    A=[sorted({c[i] for c in L10}) for i in range(10)]
    out={"cells":len(L10),"bad":len(bad),"src signatures":len(SRC)}
    # which target signatures are missing, and why
    miss=Counter((c[4],c[5],c[6],c[8]) for c in bad)
    out["distinct missing targets"]=len(miss)
    out["top missing"]=miss.most_common(6)
    # is each missing target missing because of e, f, g or 2S'?
    srcE={s[0] for s in SRC}; srcF={s[1] for s in SRC}
    srcK={s[2] for s in SRC}; srcS={s[3] for s in SRC}
    why=Counter()
    for (e,f,g,sp) in miss:
        r=[]
        if e not in srcE: r.append("e")
        if f not in srcF: r.append("l")
        if g not in srcK: r.append("k")
        if sp not in srcS: r.append("2S")
        why["+".join(r) if r else "combination only"]+=miss[(e,f,g,sp)]
    out["why"]=dict(why)
    # cap concentration
    out["at g cap"]=sum(1 for c in bad if c[6]==max(A[6]))
    out["at e cap"]=sum(1 for c in bad if c[4]==max(A[4]))
    out["g distribution"]=dict(Counter(c[6] for c in bad))
    out["all g distribution"]=dict(Counter(c[6] for c in L10))
    return out,N

with State("lam10_gap") as st:
    O,N=step(st,"define the non-composable cells of Lambda-10",run,budget=600)

print(f"  Λ₁₀: {O['cells']:,} cells, {O['bad']:,} non-composable ({100*O['bad']/O['cells']:.2f}%)")
print(f"  distinct source signatures (n,l,k,2S): {O['src signatures']}")
print(f"  distinct target signatures that match none: {O['distinct missing targets']}\n")
print(f"  WHY each target fails to be a source:")
for k,v in sorted(O['why'].items(),key=lambda x:-x[1]):
    print(f"    {k:<20}{v:>6,} cells")
print(f"\n  the missing targets, most common first  (e, f, g, 2S'):")
for t,c in O['top missing']: print(f"    {t}   {c:,} cells")
print(f"\n  g distribution among the non-composable: {O['g distribution']}")
print(f"  g distribution over all of Λ₁₀:          {O['all g distribution']}")
print(f"\n  at the g cap: {O['at g cap']:,} of {O['bad']:,}   at the e cap: {O['at e cap']:,}")
