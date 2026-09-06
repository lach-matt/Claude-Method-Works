import sys, math
sys.path.insert(0,"/home/claude/work")
import ground as G
from itertools import product, permutations, combinations
LS="spdfg"; cap=lambda l:2*(2*l+1); INF=1e9
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
    return dict(Z=Z,g=(gn,gl),p=gp,blo=blo,bhi=bhi,lo=lo,hi=hi,
                q=cu[(gn,gl)]-pr.get((gn,gl),0))
S=[s for s in (step(Z) for Z in range(3,109)) if s]
# LANDING coordinates — where the electron arrives relative to its bounds
def land(s):
    gn,gl=s['g']
    return dict(
      ceil = 0 if s['bhi'] is None else (sum(s['bhi'])-(gn+gl))+1,
      floor= 0 if s['blo'] is None else (sum(s['blo'])-(gn+gl))+1,
      sides= (0 if s['lo']<-INF/2 else 1)+(0 if s['hi']>INF/2 else 1),
      lrival = 0 if s['bhi'] is None else s['bhi'][1]+1,
      q    = s['q'],
    )
L=[land(s) for s in S]
NM=list(L[0])
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
print("  THE LANDING AXES — every combination gives E = 1. IS IT THE SAME CELL?\n")
for tri in combinations(NM,3):
    cells={tuple(c[t] for t in tri) for c in L}
    rel=[{v:i for i,v in enumerate(sorted({c[k] for c in cells}))} for k in range(3)]
    inv=[{i:v for v,i in r.items()} for r in rel]
    cs={tuple(rel[i][c[i]] for i in range(3)) for c in cells}
    ax=[len({c[i] for c in cs}) for i in range(3)]
    best=None
    for p in product(*[permutations(range(a)) for a in ax]):
        m={tuple(p[i].index(x[i]) for i in range(3)) for x in cs}
        ex=opR(m,3)-m
        if best is None or len(ex)<len(best[0]): best=(ex,p)
    ex,p=best
    if len(ex)>2: continue
    pinv=[{p[i].index(v):v for v in range(ax[i])} for i in range(3)]
    named=[tuple(inv[i][pinv[i][x[i]]] for i in range(3)) for x in ex]
    print(f"  {' x '.join(tri):<28} cells {len(cs):>2}  E = {len(ex)}")
    for nc in named:
        print(f"        defect: " + ", ".join(f"{t}={v}" for t,v in zip(tri,nc)))