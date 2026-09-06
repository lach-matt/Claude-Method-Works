#!/usr/bin/env python3
"""vi_sum.py -- the alphabet the companion actually prints.

Register 619: W.frontier states d(c) = X_exp + U_ghost + |NEC_pt - 3| + EOM +
d_P. That is a SUM, and |NEC - 3| is a DISTANCE with NEC = 3 at its centre.
No conjunction of two-variable implications can express either.

Every attack so far used implications. This adds two forms from the analysis
language: weighted sums bounded above, and absolute deviations from a centre.

COMMITTED (§2.13): the +16 / -9 residual on the NEC interior will move. It has
survived seven attacks in the implication alphabet; if a sum does not touch it
either, the obstruction is not the alphabet.
"""
import numpy as np, itertools, random, json
from zeno import State, step
R=[4,3,3,3,5,2,2,3,3]; N=["X","S","IC","U","NEC","L","SD","DNc","DNd"]
B=np.array(list(itertools.product(*[range(r) for r in R])),dtype=np.int16)
COL=[B[:,i] for i in range(9)]
T=np.array([2370,2196,1764,1146,1374,558]); W=np.array([4,1,3,3,1,1])

def mk(r):
    kind=r[0]
    if kind=="imp":
        _,body,heads=r
        bm=np.ones(len(B),bool)
        for a,va in body: bm&=COL[a]>=va
        h=np.zeros(len(B),bool)
        for b,vb in heads: h|=COL[b]>=vb
        return ~(bm&~h)
    if kind=="sum":                       # weighted sum bounded above
        _,w,cap=r
        s=np.zeros(len(B),np.int32)
        for i,c in w: s+=c*COL[i].astype(np.int32)
        return s<=cap
    if kind=="dev":                       # |x_i - centre| bounded, gated
        _,i,centre,tol,gate=r
        m=np.abs(COL[i].astype(np.int32)-centre)<=tol
        if gate is None: return m
        g,gv=gate
        return ~((COL[g]>=gv)&~m)
    raise ValueError(kind)

def mask(rs):
    m=np.ones(len(B),bool)
    for r in rs: m&=mk(r)
    return m
def prof(m):
    return np.array([m.sum(),(m&(COL[4]>=1)).sum(),(m&(COL[4]>=2)).sum(),
                     (m&(COL[4]>=3)).sum(),(m&(COL[0]>=2)).sum(),(m&(COL[0]==3)).sum()])
raw=lambda p:int(np.abs(p-T).sum()); wt=lambda p:int((np.abs(p-T)*W).sum())

def seeded():
    j=json.load(open("vi_best.json"))
    return [("imp",((r[0],r[1]),),tuple(tuple(x) for x in r[2])) for r in j["rules"]]

def rand_rule():
    k=random.random()
    if k<0.34:                                     # a sum
        n=random.choice([2,2,3,3,4])
        idx=random.sample(range(9),n)
        w=tuple((i,random.choice([1,1,1,2])) for i in idx)
        cap=random.randrange(2,sum(c*(R[i]-1) for i,c in w)+1)
        return ("sum",w,cap)
    if k<0.55:                                     # a deviation, maybe gated
        i=random.randrange(9); centre=random.randrange(R[i]); tol=random.randrange(0,R[i])
        gate=None
        if random.random()<0.6:
            g=random.choice([x for x in range(9) if x!=i]); gate=(g,random.randrange(1,R[g]))
        return ("dev",i,centre,tol,gate)
    a=random.randrange(9); va=random.randrange(1,R[a])
    body=((a,va),)
    if random.random()<0.3:
        b=random.choice([x for x in range(9) if x!=a]); body=body+((b,random.randrange(1,R[b])),)
    used={x for x,_ in body}
    hs=random.sample([b for b in range(9) if b not in used],random.choice([1,1,2]))
    return ("imp",body,tuple((b,random.randrange(1,R[b])) for b in hs))

def climb(rs,rounds,T0=5.0):
    cur=list(rs); m=mask(cur); bw=wt(prof(m)); best=(raw(prof(m)),list(cur))
    for t in range(rounds):
        temp=T0*(1-t/rounds)+0.02
        op=random.random(); i=random.randrange(len(cur))
        if op<0.5: trial=cur[:i]+[rand_rule()]+cur[i+1:]
        elif op<0.8 and len(cur)<28: trial=cur+[rand_rule()]
        elif len(cur)>10: trial=cur[:i]+cur[i+1:]
        else: trial=cur[:i]+[rand_rule()]+cur[i+1:]
        m2=mask(trial)
        if not m2.sum(): continue
        p2=prof(m2); w2=wt(p2)
        if w2<=bw or random.random()<pow(2.718,-(w2-bw)/temp):
            cur,bw=trial,w2
            if raw(p2)<best[0]: best=(raw(p2),list(trial))
    return best

def run():
    random.seed(89)
    base=seeded(); best=(raw(prof(mask(base))),base)
    # the companion's own frontier form, as a gated deviation on NEC centred at 3
    PRINT=[("dev",4,3,1,(0,1)), ("dev",4,3,2,None), ("sum",((0,1),(3,1),(4,1)),6)]
    for extra in ([],[PRINT[0]],[PRINT[1]],[PRINT[2]],PRINT):
        s0=base+extra
        if not mask(s0).sum(): continue
        g=climb(s0,7000)
        if g[0]<best[0]: best=g
    for _ in range(16):
        s0=best[1] if random.random()<0.65 else [rand_rule() for _ in range(random.choice([17,20]))]
        if not mask(s0).sum(): continue
        g=climb(s0,6000)
        if g[0]<best[0]: best=g
        if best[0]==0: break
    return best

with State("vi_sum") as st:
    d,rs=step(st,"the sum and deviation alphabet",run,budget=1700)
m=mask(rs); p=prof(m)
kinds={}
for r in rs: kinds[r[0]]=kinds.get(r[0],0)+1
print(f"  rules {len(rs)} {kinds}   distance {d}   (implications alone: 28)")
print(f"    target {T.tolist()}")
print(f"    found  {p.tolist()}")
print(f"    miss   {(p-T).tolist()}")
print(f"    IMPROVED: {d<28}")
if d<28:
    json.dump({"d":d,"prof":p.tolist(),"rules":[list(map(str,r)) for r in rs]},
              open("vi_best4.json","w"))
    print("    saved to vi_best4.json")
    for r in rs:
        if r[0]=="sum": print(f"      SUM  " + " + ".join(f"{c}·{N[i]}" for i,c in r[1]) + f" <= {r[2]}")
        elif r[0]=="dev": print(f"      DEV  |{N[r[1]]} - {r[2]}| <= {r[3]}" + (f"  when {N[r[4][0]]}>={r[4][1]}" if r[4] else ""))