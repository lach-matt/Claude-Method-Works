#!/usr/bin/env python3
"""vi_marg.py -- the edge list restated in the statistical language.

Register 616: the six printed counts are CUMULATIVE MARGINALS on NEC and X.
Differencing them gives the exact per-value marginal, which turns a search over
rule sets into a transport problem: how many cells must move between NEC values.

Under zeno, per §2.20.
"""
import numpy as np, itertools, json
from zeno import State, step

R=[4,3,3,3,5,2,2,3,3]; N=["X","S","IC","U","NEC","L","SD","DNc","DNd"]
B=np.array(list(itertools.product(*[range(r) for r in R])),dtype=np.int8)
COL=[B[:,i] for i in range(9)]

def mask(rs):
    m=np.ones(len(B),bool)
    for body,heads in rs:
        bm=np.ones(len(B),bool)
        for a,va in body: bm&=COL[a]>=va
        h=np.zeros(len(B),bool)
        for b,vb in heads: h|=COL[b]>=vb
        m&=~(bm&~h)
    return m

def run():
    # printed: total, NEC>=1, NEC>=2, NEC>=3, X>=2, X==3
    P=[2370,2196,1764,1146,1374,558]
    necP={0:P[0]-P[1], 1:P[1]-P[2], 2:P[2]-P[3], "3+":P[3]}
    xP={"<=1":P[0]-P[4], 2:P[4]-P[5], 3:P[5]}
    j=json.load(open("vi_best.json"))
    rs=[(((r[0],r[1]),),tuple(tuple(x) for x in r[2])) for r in j["rules"]]
    m=mask(rs)
    nec=COL[4][m]; x=COL[0][m]
    necG={0:int((nec==0).sum()),1:int((nec==1).sum()),
          2:int((nec==2).sum()),"3+":int((nec>=3).sum())}
    xG={"<=1":int((x<=1).sum()),2:int((x==2).sum()),3:int((x==3).sum())}
    return P,necP,necG,xP,xG,int(m.sum())

with State("vi_marg") as st:
    P,necP,necG,xP,xG,tot=step(st,"restate the counts as marginals",run,budget=200)

print(f"  the six printed counts are CUMULATIVE. Differenced:\n")
print(f"  {'NEC value':<12}{'printed':>9}{'candidate':>11}{'move':>7}")
for k in [0,1,2,"3+"]:
    print(f"  {str(k):<12}{necP[k]:>9,}{necG[k]:>11,}{necG[k]-necP[k]:>+7}")
print(f"\n  {'X value':<12}{'printed':>9}{'candidate':>11}{'move':>7}")
for k in ["<=1",2,3]:
    print(f"  {str(k):<12}{xP[k]:>9,}{xG[k]:>11,}{xG[k]-xP[k]:>+7}")
print(f"\n  total  printed {P[0]:,}   candidate {tot:,}   difference {tot-P[0]}")
d=sum(abs(necG[k]-necP[k]) for k in necP)+sum(abs(xG[k]-xP[k]) for k in xP)
print(f"\n  cells that must MOVE between NEC values: "
      f"{sum(abs(necG[k]-necP[k]) for k in necP)//2}")
print(f"  cells that must MOVE between X values:   "
      f"{sum(abs(xG[k]-xP[k]) for k in xP)//2}")
print(f"""
  So the problem is TRANSPORT, not search: the candidate holds the right total
  and distributes it wrongly across NEC. In the statistical language that is a
  marginal-matching problem; in the order language it was 17 rules and a
  distance of 29.""")