#!/usr/bin/env python3
"""vi_transport.py -- the targeted question the statistical language supplied.

Register 617: 26 cells must move — 25 out of NEC = 2, of which 17 to NEC = 1 and
9 to NEC >= 3, plus 1 out of NEC = 0. Which single rule edit does that?

Rather than searching rule sets blind, this asks the order language a question
it can answer: for each rule, what does narrowing, widening or removing it do to
the NEC histogram?
"""
import numpy as np, itertools, json
from zeno import State, step

R=[4,3,3,3,5,2,2,3,3]; N=["X","S","IC","U","NEC","L","SD","DNc","DNd"]
B=np.array(list(itertools.product(*[range(r) for r in R])),dtype=np.int8)
COL=[B[:,i] for i in range(9)]
TGT={0:174,1:432,2:618,3:1146}          # 3 means "3 or more"
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

def hist(m):
    n=COL[4][m]
    return {0:int((n==0).sum()),1:int((n==1).sum()),
            2:int((n==2).sum()),3:int((n>=3).sum())}

def prof(m):
    return np.array([m.sum(),(m&(COL[4]>=1)).sum(),(m&(COL[4]>=2)).sum(),
                     (m&(COL[4]>=3)).sum(),(m&(COL[0]>=2)).sum(),(m&(COL[0]==3)).sum()])
d=lambda m:int(np.abs(prof(m)-T).sum())

def run():
    j=json.load(open("vi_best.json"))
    rs=[(((r[0],r[1]),),tuple(tuple(x) for x in r[2])) for r in j["rules"]]
    base=mask(rs); out=[]
    # every single-rule edit: remove, or shift one threshold by ±1
    for i,(body,heads) in enumerate(rs):
        cand=[("remove", rs[:i]+rs[i+1:])]
        for k,(a,va) in enumerate(body):
            for nv in (va-1,va+1):
                if 1<=nv<R[a]:
                    nb=list(body); nb[k]=(a,nv)
                    cand.append((f"body {N[a]}>={va}→{nv}", rs[:i]+[(tuple(nb),heads)]+rs[i+1:]))
        for k,(b,vb) in enumerate(heads):
            for nv in (vb-1,vb+1):
                if 1<=nv<R[b]:
                    nh=list(heads); nh[k]=(b,nv)
                    cand.append((f"head {N[b]}>={vb}→{nv}", rs[:i]+[(body,tuple(nh))]+rs[i+1:]))
        for lbl,t in cand:
            m=mask(t)
            if not m.sum(): continue
            out.append((d(m), i, lbl, hist(m), int(m.sum())))
    out.sort(key=lambda r:r[0])
    return d(base), hist(base), out[:12]

with State("vi_transport") as st:
    d0,h0,top=step(st,"single-rule edits against the NEC histogram",run,budget=900)

print(f"  base: distance {d0}   NEC histogram {h0}")
print(f"  target                              {TGT}\n")
print(f"  {'dist':>5}  {'rule':>4}  {'edit':<26}{'cells':>7}   NEC histogram")
for dd,i,lbl,h,n in top:
    print(f"  {dd:>5}  {i:>4}  {lbl:<26}{n:>7,}   {h}")