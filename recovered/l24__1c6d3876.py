import itertools, collections, time
from tower2mod import L8, PHI
t0=time.time()
L=L8(); S=set(L); N=len(L); print('N',N)
# constraints as (u, v, phi): u <= phi(v)
CON=[('l<=n-1',1,0,lambda x:x-1),('k<=4l+2',2,1,lambda x:4*x+2),('q<=k',3,2,lambda x:x),
     ('f<=e-1',5,4,lambda x:x-1),('g<=4f+2',6,5,lambda x:4*x+2),('g<=q',6,3,lambda x:x),('2S<=k',7,2,lambda x:x)]
# rank
rk=[sum(c) for c in L]; mn=min(rk); levels=collections.Counter(r-mn for r in rk)
print('rank levels',len(levels),'largest',max(levels.values()),'at rank',max(levels,key=levels.get),'976/122=',N/max(levels.values()))
# covers: y covers x iff x<y and rank diff 1 (graded)
idx={c:i for i,c in enumerate(L)}
up=collections.defaultdict(list)
for c in L:
    for i in range(8):
        d=list(c); d[i]+=1; d=tuple(d)
        if d in S: up[c].append(d)
E=sum(len(v) for v in up.values()); print('cover edges',E)
# comparable pairs & box criterion
comp=0; box_direct=0; box_crit=0; agree=0
bind=collections.Counter()
Ls=sorted(L)
for x in L:
    for y in L:
        if x!=y and all(a<=b for a,b in zip(x,y)):
            comp+=1
            crit=all(y[u]<=phi(x[v]) for _,u,v,phi in CON)
            # direct: box size == interval size ; interval = cells between
            bsz=1
            for a,b in zip(x,y): bsz*=(b-a+1)
            # count cells in S within box
            cnt=0
            for z in itertools.product(*[range(a,b+1) for a,b in zip(x,y)]):
                if z in S: cnt+=1
            direct=(cnt==bsz)
            box_crit+=crit; box_direct+=direct; agree+=(crit==direct)
print('comparable',comp,'boxes(crit)',box_crit,'boxes(direct)',box_direct,'agree',agree,'pct',round(100*box_crit/comp,1))
# binding rates over meet-join intervals of all unordered pairs
tot=0
for i in range(N):
    x=L[i]
    for j in range(i+1,N):
        y=L[j]; tot+=1
        m=tuple(map(min,x,y)); J=tuple(map(max,x,y))
        for name,u,v,phi in CON:
            if J[u]>phi(m[v]): bind[name]+=1
print('unordered pairs',tot)
for name,_,_,_ in CON: print(' bind',name,round(100*bind[name]/tot,1))
# join-irreducibles: elements with exactly one lower cover
down=collections.defaultdict(list)
for c,vs in up.items():
    for v in vs: down[v].append(c)
JI=[c for c in L if len(down[c])==1]
print('join-irreducibles',len(JI),'max chain length (levels)',len(levels))
# linear extensions of JI poset: DP over down-sets
JI.sort(); m=len(JI); pos={c:i for i,c in enumerate(JI)}
below=[0]*m
for i,a in enumerate(JI):
    for j,b in enumerate(JI):
        if i!=j and all(p<=q for p,q in zip(b,a)): below[i]|=1<<j
from functools import lru_cache
import sys; sys.setrecursionlimit(10000)
@lru_cache(None)
def f(mask):
    if mask==(1<<m)-1: return 1
    return sum(f(mask|1<<i) for i in range(m) if not mask>>i&1 and below[i]&mask==below[i])
print('e(P)',f(0))
# constraint graph
edges=set((min(u,v),max(u,v)) for _,u,v,_ in CON); print('constraint graph vertices 8 edges',len(edges))
print('time',round(time.time()-t0))