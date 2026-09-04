#!/usr/bin/env python3
"""vi_nec3.py -- seed the search at the threshold no rule uses.

Register 617: the seventeen rules use NEC thresholds 1, 2 and 4 and never 3,
while NEC ranges 0-4 and the companion's own printed constraint has its core at
NEC = 3. The transport needed — 17 cells from NEC=2 to NEC=1 and 9 to NEC>=3 —
crosses exactly the boundary no rule can see.

This seeds the search WITH rules at NEC = 3, including the companion's own
printed form NEC >= 3 AND X = 0 -> U >= 1, and searches from there.

COMMITTED (§2.13): distance will fall below 29. If it does not, the missing
threshold is not the obstruction and register 617's diagnosis is wrong.
"""
import numpy as np, itertools, random, json
from zeno import State, step

R=[4,3,3,3,5,2,2,3,3]; N=["X","S","IC","U","NEC","L","SD","DNc","DNd"]
B=np.array(list(itertools.product(*[range(r) for r in R])),dtype=np.int8)
COL=[B[:,i] for i in range(9)]
T=np.array([2370,2196,1764,1146,1374,558])
W=np.array([4,1,3,3,1,1])          # the two NEC-interior counts carry the residual

def mk(r):
    body,heads=r
    bm=np.ones(len(B),bool)
    for a,va,ge in body:
        bm &= (COL[a]>=va) if ge else (COL[a]==va)
    h=np.zeros(len(B),bool)
    for b,vb in heads: h|=COL[b]>=vb
    return ~(bm&~h)
def mask(rs):
    m=np.ones(len(B),bool)
    for r in rs: m&=mk(r)
    return m
def prof(m):
    return np.array([m.sum(),(m&(COL[4]>=1)).sum(),(m&(COL[4]>=2)).sum(),
                     (m&(COL[4]>=3)).sum(),(m&(COL[0]>=2)).sum(),(m&(COL[0]==3)).sum()])
raw=lambda p:int(np.abs(p-T).sum()); wt=lambda p:int((np.abs(p-T)*W).sum())

# the companion's own printed constraint, T §8.2
PRINTED=(((4,3,True),(0,0,False)), ((3,1),))     # NEC>=3 AND X==0 -> U>=1
NEC3=[(((4,3,True),), ((b,1),)) for b in (0,1,2,3,5,6,7,8)]

def seeded():
    j=json.load(open("vi_best.json"))
    return [(((r[0],r[1],True),), tuple(tuple(x) for x in r[2])) for r in j["rules"]]

def rand_rule(force3=False):
    if force3 and random.random()<0.45:
        body=[(4,3,True)]
        if random.random()<0.5:
            a=random.choice([0,1,2,3,5,6,7,8]); body.append((a,random.randrange(0,R[a]),random.random()<0.6))
        hs=random.sample([b for b in range(9) if b!=4], random.choice([1,1,2]))
        return (tuple(body), tuple((b,random.randrange(1,R[b])) for b in hs))
    k=random.choice([1,1,1,2,2,3]); ba=random.sample(range(9),k)
    body=tuple((a,random.randrange(1,R[a]),random.random()<0.85) for a in ba)
    pool=[b for b in range(9) if b not in ba] or list(range(9))
    hs=random.sample(pool,random.choice([1,1,2,3]))
    return (body, tuple((b,random.randrange(1,R[b])) for b in hs))

def climb(rs,rounds,T0=5.0):
    cur=list(rs); m=mask(cur); bw=wt(prof(m)); best=(raw(prof(m)),list(cur))
    for t in range(rounds):
        temp=T0*(1-t/rounds)+0.02
        op=random.random(); i=random.randrange(len(cur))
        if op<0.5: trial=cur[:i]+[rand_rule(True)]+cur[i+1:]
        elif op<0.8 and len(cur)<28: trial=cur+[rand_rule(True)]
        elif len(cur)>10: trial=cur[:i]+cur[i+1:]
        else: trial=cur[:i]+[rand_rule(True)]+cur[i+1:]
        m2=mask(trial)
        if not m2.sum(): continue
        p2=prof(m2); w2=wt(p2)
        if w2<=bw or random.random()<pow(2.718,-(w2-bw)/temp):
            cur,bw=trial,w2
            if raw(p2)<best[0]: best=(raw(p2),list(trial))
    return best

def run():
    random.seed(71)
    base=seeded()
    best=(raw(prof(mask(base))),base)
    starts=[base+[PRINTED], base+NEC3[:3], base+[PRINTED]+NEC3[:2], base]
    for s0 in starts:
        if not mask(s0).sum(): continue
        g=climb(s0,7000)
        if g[0]<best[0]: best=g
    for _ in range(18):
        s0=best[1] if random.random()<0.6 else [rand_rule(True) for _ in range(random.choice([17,20,23]))]
        if not mask(s0).sum(): continue
        g=climb(s0,6000)
        if g[0]<best[0]: best=g
        if best[0]==0: break
    return best

with State("vi_nec3") as st:
    d,rs=step(st,"seed the search at NEC = 3",run,budget=1700)

m=mask(rs); p=prof(m)
print(f"  rules {len(rs)}   distance {d}   (recorded best: 29)")
print(f"    target {T.tolist()}")
print(f"    found  {p.tolist()}")
print(f"    miss   {(p-T).tolist()}")
n3=sum(1 for body,_ in rs if any(a==4 and va==3 for a,va,_ in body))
print(f"    rules using NEC = 3 in the body: {n3}")
print(f"    IMPROVED: {d<29}")
if d<29:
    json.dump({"d":d,"rules":[[list(map(list,b)),list(map(list,h))] for b,h in rs],
               "prof":p.tolist()},open("vi_best3.json","w"))
    print("    saved to vi_best3.json")
