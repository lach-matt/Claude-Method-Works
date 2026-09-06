import sys, math, random
sys.path.insert(0,"/home/claude/work")
import ground as G
from itertools import product, permutations, combinations
LS="spdfg"; cap=lambda l:2*(2*l+1); INF=1e9
JAN=[(1,2),(3,4),(5,12),(13,20),(21,38),(39,56),(57,88),(89,118)]
blk=lambda Z: next(i for i,(a,b) in enumerate(JAN) if a<=Z<=b)
def step(Z):
    if Z<3 or Z>108: return None
    pr={(n,l):o for n,l,o in G.expand(Z-1)}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    got=[k for k in cu if cu[k]>pr.get(k,0)]
    if len(got)!=1: return None
    gn,gl=got[0]; gp=gn-gl-1; cand=[]
    for l in range(5):
        for n in range(l+1,9):
            if pr.get((n,l),0)>=cap(l): continue
            cand.append((n,l))
            if pr.get((n,l),0)==0: break
    if (gn,gl) not in cand or len(cand)<2: return None
    lo,hi=-INF,INF; blo=bhi=None
    for n,l in cand:
        if (n,l)==(gn,gl): continue
        rp=n-l-1; d=math.sqrt(rp)-math.sqrt(gp); r=n-gn
        if abs(d)<1e-12: continue
        if d>0 and r/d<hi: hi,bhi=r/d,(n,l)
        if d<0 and r/d>lo: lo,blo=r/d,(n,l)
    lost=[k for k in pr if pr[k]>cu.get(k,0)]
    return dict(Z=Z,g=(gn,gl),p=gp,lo=lo,hi=hi,blo=blo,bhi=bhi,
                q=cu[(gn,gl)]-pr.get((gn,gl),0),lost=len(lost),pr=pr)
S=[step(Z) for Z in range(3,109)]; S=[s for s in S if s]
print(f"  Λ_traj — the 106 steps as cells\n")
# ---- coordinates, each READ from the step, each a monotone chain -----------
def coords(s):
    gn,gl=s['g']
    return dict(
      nodes   = min(s['p'],3),                       # entrant's node count, 0..3+
      L       = gl,                                  # entrant's l: s<p<d<f
      ceil    = (0 if s['bhi'] is None else
                 (sum(s['bhi'])-(gn+gl))+1),         # 0 none, 1 own block, 2 next
      floor   = (0 if s['blo'] is None else
                 (sum(s['blo'])-(gn+gl))+1),         # 0 none, 1 own, 2 next, 3 +2
      q       = min(s['q'],2),                       # electrons arriving, 1 or 2
      sides   = (0 if s['lo']<-INF/2 else 1)+(0 if s['hi']>INF/2 else 1),
    )
C=[coords(s) for s in S]
NAMES=list(C[0])
for nm in NAMES:
    vals=sorted({c[nm] for c in C})
    print(f"      {nm:<8} values {vals}   ({len(vals)} rungs)")
def opR(X,d):
    X=set(X); vals=[sorted({x[i] for x in X}) for i in range(d)]
    def env(i,j):
        m={}
        for x in X: m[x[j]]=max(m.get(x[j],-10**9),x[i])
        b,o=-10**9,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    return {x for x in product(*vals) if all(x[i]<=phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i!=j)}
def minE(cells,axes,cap_=4000):
    b=None;k=0
    for p in product(*[permutations(range(a)) for a in axes]):
        cs={tuple(p[i].index(x[i]) for i in range(len(axes))) for x in cells}
        E=len(opR(cs,len(axes)))-len(cs)
        b=E if b is None else min(b,E)
        if b==0: return 0
        k+=1
        if k>cap_: break
    return b
print(f"\n  {'axes':<34}{'cells':>6}{'box':>6}{'minE':>6}")
res=[]
for tri in combinations(NAMES,3):
    cells={tuple(c[t] for t in tri) for c in C}
    rel=[{v:i for i,v in enumerate(sorted({c[k] for c in cells}))} for k in range(3)]
    cells={tuple(rel[i][c[i]] for i in range(3)) for c in cells}
    axes=[len({c[i] for c in cells}) for i in range(3)]
    if max(axes)>6: continue
    E=minE(cells,axes); box=axes[0]*axes[1]*axes[2]
    res.append((E,len(cells),box,tri))
res.sort()
for E,n,box,tri in res[:10]:
    print(f"  {' x '.join(tri):<34}{n:>6}{box:>6}{E:>6}")
print(f"\n  {sum(1 for r in res if r[0]==0)} of {len(res)} reach E = 0")