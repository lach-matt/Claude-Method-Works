#!/usr/bin/env python3
"""vi_r15.py -- is rule 15 inert, or is it placing something?

Register 618: nothing in this structure is inert. A rule whose removal changes
nothing may still be a redundant GENERATOR — implied by the others, and standing
in for one of them if that one goes.

Test: remove rule 15 alone (no change). Then remove each OTHER rule alone, and
each other rule TOGETHER with 15. If 15 is inert the two costs are equal. If it
is a backup, removing 15 first makes the second removal cost more.
"""
import numpy as np, itertools, json
from zeno import State, step
R=[4,3,3,3,5,2,2,3,3]; N=["X","S","IC","U","NEC","L","SD","DNc","DNd"]
B=np.array(list(itertools.product(*[range(r) for r in R])),dtype=np.int8)
COL=[B[:,i] for i in range(9)]
T=np.array([2370,2196,1764,1146,1374,558])
def mask(rs):
    m=np.ones(len(B),bool)
    for body,heads in rs:
        bm=np.ones(len(B),bool)
        for a,va in body: bm&=COL[a]>=va
        h=np.zeros(len(B),bool)
        for b,vb in heads: h|=COL[b]>=vb
        m&=~(bm&~h)
    return m
def prof(m):
    return np.array([m.sum(),(m&(COL[4]>=1)).sum(),(m&(COL[4]>=2)).sum(),
                     (m&(COL[4]>=3)).sum(),(m&(COL[0]>=2)).sum(),(m&(COL[0]==3)).sum()])
d=lambda m:int(np.abs(prof(m)-T).sum())
def run():
    j=json.load(open("vi_best.json"))
    rs=[(((r[0],r[1]),),tuple(tuple(x) for x in r[2])) for r in j["rules"]]
    full=mask(rs); base=d(full)
    no15=[r for i,r in enumerate(rs) if i!=15]
    out=[]
    for i in range(len(rs)):
        if i==15: continue
        a=[r for k,r in enumerate(rs) if k!=i]
        b=[r for k,r in enumerate(rs) if k not in (i,15)]
        ma,mb=mask(a),mask(b)
        out.append((i, int(ma.sum()), int(mb.sum()), int(mb.sum())-int(ma.sum()), d(ma), d(mb)))
    # and: is rule 15 implied by a SUBSET of the others?
    r15=rs[15]
    implied=[]
    for k in range(1,4):
        for combo in itertools.combinations([i for i in range(len(rs)) if i!=15], k):
            sub=[rs[i] for i in combo]
            m=mask(sub)
            if (m & ~mask([r15])).sum()==0:
                implied.append(combo); break
        if implied: break
    return base, int(full.sum()), int(mask(no15).sum()), out, implied
with State("vi_r15") as st:
    base,nfull,n15,out,implied=step(st,"is rule 15 placing something",run,budget=900)
print(f"  full set: {nfull:,} cells, distance {base}")
print(f"  without rule 15 alone: {n15:,} cells   change {n15-nfull}\n")
print(f"  {'rule':>5}{'drop it':>10}{'drop it AND 15':>16}{'extra':>7}")
diff=[r for r in out if r[3]!=0]
for i,a,b,delta,da,db in out:
    tag="  ← 15 was covering for it" if delta else ""
    print(f"  {i:>5}{a:>10,}{b:>16,}{delta:>+7}{tag}")
print(f"\n  rules where removing 15 first costs MORE: {len(diff)}")
print(f"  smallest subset implying rule 15: {implied or 'none up to size 3'}")