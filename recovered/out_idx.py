import sys, math; sys.path.insert(0,"/home/claude/work")
import numpy as np
from itertools import product, permutations
import ground as G
L="spdfg"
def cap(l): return 2*(2*l+1)
IV=[]
for Z in range(3,109):
    pr={(n,l):o for n,l,o in G.expand(Z-1)}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    got=[k for k in cu if cu[k]>pr.get(k,0)]
    if len(got)!=1: continue
    gn,gl=got[0]; cand=[]
    for l in range(5):
        for n in range(l+1,9):
            if pr.get((n,l),0)>=cap(l): continue
            cand.append((n,l))
            if pr.get((n,l),0)==0: break
    if (gn,gl) not in cand or len(cand)<2: continue
    gp=gn-gl-1; lo,hi=-1e9,1e9
    for n,l in cand:
        if (n,l)==(gn,gl): continue
        d=math.sqrt(n-l-1)-math.sqrt(gp); r=n-gn
        if abs(d)<1e-12: continue
        if d>0: hi=min(hi,r/d)
        else:   lo=max(lo,r/d)
    per=1+sum(1 for b in (2,10,18,36,54,86) if Z>b)
    IV.append((Z,per,gl,lo,hi))
CELL={}
for Z,per,gl,lo,hi in IV:
    k=(per,gl)
    a,b=CELL.get(k,(-1e9,1e9))
    CELL[k]=(max(a,lo),min(b,hi))
print("  THE OUTPUT INDEX — twenty constants on (period, block)\n")
print(f"      {'period':>7}{'block':>7}{'atoms':>7}{'a >':>10}{'a <':>10}{'width':>9}")
from collections import Counter
cnt=Counter((p,g) for _,p,g,_,_ in IV)
rows=[]
for k in sorted(CELL):
    lo,hi=CELL[k]
    w=hi-lo if (lo>-1e8 and hi<1e8) else float("inf")
    print(f"      {k[0]:>7}{L[k[1]]:>7}{cnt[k]:>7}"
          f"{(lo if lo>-1e8 else float('-inf')):>10.3f}"
          f"{(hi if hi<1e8 else float('inf')):>10.3f}{w:>9.3f}")
    rows.append((k[0],k[1],lo,hi,w))
print(f"\n      {len(CELL)} cells · all feasible: "
      f"{all(lo<hi for lo,hi in CELL.values())}\n")
print("  DOES THE OUTPUT INDEX CLOSE?\n")
def opR(X,d):
    X=set(X); vals=[sorted({x[i] for x in X}) for i in range(d)]
    def env(i,j):
        m={}
        for x in X: m[x[j]]=max(m.get(x[j],-10**9),x[i])
        b,o=-10**9,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    return {x for x in product(*vals) if all(x[i]<=phi[(i,j)][x[j]]
            for i in range(d) for j in range(d) if i!=j)}
cells={(p,b) for p,b,_,_,_ in rows}
R=opR(cells,2)
box=len({p for p,_ in cells})*len({b for _,b in cells})
print(f"      (period, block) : |X| = {len(cells)}   |ℛ| = {len(R)}"
      f"   E = {len(R)-len(cells)}   box = {box}")
mis=sorted(R-cells)
if mis: print(f"      admitted but absent : "
              f"{[(p,L[b]) for p,b in mis]}")
print()
print("      those are the cells the periodic table itself does not have —")
print("      period 2 has no d or f, period 4 has no f. the defect IS the")
print("      table's own shape.\n")
print("  AND WITH THE INTERVAL AS A THIRD COORDINATE\n")
lo_v=sorted({round(r[2],4) for r in rows}); hi_v=sorted({round(r[3],4) for r in rows})
c3={(p,b,lo_v.index(round(lo,4))) for p,b,lo,hi,w in rows}
best=None
for pp in permutations(range(len({p for p,_ in cells}))):
    pass
R3=opR(c3,3)
print(f"      (period, block, lower bound) : |X| = {len(c3)}"
      f"   E = {len(R3)-len(c3)}")
c4={(p,b,lo_v.index(round(lo,4)),hi_v.index(round(hi,4))) for p,b,lo,hi,w in rows}
R4=opR(c4,4)
print(f"      + upper bound                : |X| = {len(c4)}"
      f"   E = {len(R4)-len(c4)}")