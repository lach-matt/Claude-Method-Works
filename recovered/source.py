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
    gn,gl=got[0]; gp=gn-gl-1
    lost=[k for k in pr if pr[k]>cu.get(k,0)]
    cand=[]
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
    src = lost[0] if lost else None
    return dict(g=(gn,gl),p=gp,blo=blo,bhi=bhi,lo=lo,hi=hi,
                q=cu[(gn,gl)]-pr.get((gn,gl),0), src=src, pr=pr)
S=[s for s in (step(Z) for Z in range(3,109)) if s]
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
def minE(cells,d,cap_=8000):
    rel=[{v:i for i,v in enumerate(sorted({c[k] for c in cells}))} for k in range(d)]
    cs={tuple(rel[i][c[i]] for i in range(d)) for c in cells}
    ax=[len({c[i] for c in cs}) for i in range(d)]
    b=None;k=0
    for p in product(*[permutations(range(a)) for a in ax]):
        m={tuple(p[i].index(x[i]) for i in range(d)) for x in cs}
        E=len(opR(m,d))-len(m)
        b=E if b is None else min(b,E)
        if b==0: return 0,len(cs),ax
        k+=1
        if k>cap_: break
    return b,len(cs),ax
# LANDING coords, and the SOURCE the day's work says is missing
def L(s):
    gn,gl=s['g']
    return dict(ceil = 0 if s['bhi'] is None else (sum(s['bhi'])-(gn+gl))+1,
                sides= (0 if s['lo']<-INF/2 else 1)+(0 if s['hi']>INF/2 else 1),
                q    = s['q'],
                srcl = 0 if s['src'] is None else s['src'][1]+1,   # source's l, 0 = none
                srco = 0 if s['src'] is None else s['pr'].get(s['src'],0), # its occupancy
                srcd = 0 if s['src'] is None else (sum(s['src'])-(gn+gl))+2)
C=[L(s) for s in S]
NM=list(C[0])
print("  ADDING THE SOURCE — does the q = 2 defect close?\n")
print(f"  {'axes':<40}{'cells':>6}{'E':>4}")
res=[]
for k in (3,4):
    for tri in combinations(NM,k):
        cells={tuple(c[t] for t in tri) for c in C}
        E,n,ax=minE(cells,k)
        res.append((E,k,n,tri))
res.sort(key=lambda r:(r[0],-r[2]))
for E,k,n,tri in res[:14]:
    print(f"  {' x '.join(tri):<40}{n:>6}{E:>4}")
print(f"\n  3-axis closing: {sum(1 for r in res if r[0]==0 and r[1]==3)}"
      f" of {sum(1 for r in res if r[1]==3)}")
print(f"  4-axis closing: {sum(1 for r in res if r[0]==0 and r[1]==4)}"
      f" of {sum(1 for r in res if r[1]==4)}")
print("\n  does ANY arrangement WITH a source coordinate and q close?")
ok=[r for r in res if r[0]==0 and any(t.startswith('src') for t in r[3]) and 'q' in r[3]]
for E,k,n,tri in ok[:8]:
    print(f"      {' x '.join(tri)}   cells {n}")