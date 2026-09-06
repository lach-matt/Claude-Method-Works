#!/usr/bin/env python3
"""vi_conj.py -- conjunctive bodies, the form T §8.2 actually prints.

vi_best.json reached distance 29 with disjunctive heads and single-literal
bodies. §8.2 prints NEC >= 3 AND X = 0 -> U >= 1: a CONJUNCTIVE BODY at arity 3.
This adds that form and seeds from the recorded best rather than from scratch
(register 591).
"""
import numpy as np, itertools, random, json
from zeno import State, step
R=[4,3,3,3,5,2,2,3,3]; N=["X","S","IC","U","NEC","L","SD","DNc","DNd"]
B=np.array(list(itertools.product(*[range(r) for r in R])),dtype=np.int8)
COL=[B[:,i] for i in range(9)]
T=np.array([2370,2196,1764,1146,1374,558])
def prof(m):
    return np.array([m.sum(),(m&(COL[4]>=1)).sum(),(m&(COL[4]>=2)).sum(),
                     (m&(COL[4]>=3)).sum(),(m&(COL[0]>=2)).sum(),(m&(COL[0]==3)).sum()])
def mk(r):
    body,heads=r
    bm=np.ones(len(B),bool)
    for a,va,op in body:
        bm &= (COL[a]>=va) if op else (COL[a]==va)
    h=np.zeros(len(B),bool)
    for b,vb in heads: h |= COL[b]>=vb
    return ~(bm&~h)
def mask(rs):
    m=np.ones(len(B),bool)
    for r in rs: m&=mk(r)
    return m
d=lambda p:int(np.abs(p-T).sum())
def rand_rule():
    k=random.choice([1,1,1,2,2,3])                     # conjunctive body size
    ba=random.sample(range(9),k)
    body=tuple((a,random.randrange(0,R[a]) if random.random()<0.3 else random.randrange(1,R[a]),
                random.random()<0.75) for a in ba)
    hs=random.sample([b for b in range(9) if b not in ba] or list(range(9)),
                     random.choice([1,1,2,3]))
    return (body, tuple((b,random.randrange(1,R[b])) for b in hs))
def load_seed():
    try:
        j=json.load(open("vi_best.json"))
        out=[]
        for r in j["rules"]:
            if len(r)==3 and isinstance(r[2],(list,tuple)):
                out.append((((r[0],r[1],True),), tuple(tuple(x) for x in r[2])))
        return out
    except Exception: return []
def climb(rs,rounds):
    bd=d(prof(mask(rs))); cur=list(rs)
    for _ in range(rounds):
        moved=False
        for _ in range(38):
            op=random.random()
            if op<0.5 and cur:
                i=random.randrange(len(cur)); t=cur[:i]+[rand_rule()]+cur[i+1:]
            elif op<0.8 and len(cur)<26: t=cur+[rand_rule()]
            elif len(cur)>8:
                i=random.randrange(len(cur)); t=cur[:i]+cur[i+1:]
            else:
                i=random.randrange(len(cur)); t=cur[:i]+[rand_rule()]+cur[i+1:]
            m=mask(t)
            if not m.sum(): continue
            dd=d(prof(m))
            if dd<bd: bd=dd; cur=t; moved=True; break
        if bd==0 or not moved: break
    return bd,cur
def run():
    random.seed(7)
    seed=load_seed()
    best=climb(seed,9000) if seed else (10**9,[])
    for _ in range(240):
        rs=[rand_rule() for _ in range(random.choice([14,17,20]))]
        if not mask(rs).sum(): continue
        r=climb(rs,4000)
        if r[0]<best[0]: best=r
        if best[0]==0: break
    return best
with State("vi_conj") as st:
    bd,rs=step(st,"conjunctive bodies",run,budget=1700)
m=mask(rs); p=prof(m)
print(f"  rules {len(rs)}  distance {bd}   (recorded best with simple bodies: 29)")
print(f"    target {T.tolist()}")
print(f"    found  {p.tolist()}   EXACT: {bd==0}")
if bd<29:
    json.dump({"d":bd,"rules":[[list(map(list,b)),list(map(list,h))] for b,h in rs],
               "prof":p.tolist()},open("vi_best_conj.json","w"))
    print("    saved to vi_best_conj.json")