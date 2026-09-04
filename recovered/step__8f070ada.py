import sys, time
import numpy as np
from itertools import product, permutations, combinations
DIMS=tuple(int(x) for x in sys.argv[1].split(','))
d=len(DIMS)
cells=list(product(*[range(x) for x in DIMS])); n=len(cells)
CIDX={c:i for i,c in enumerate(cells)}
JO=[[0]*n for _ in range(n)]; ME=[[0]*n for _ in range(n)]
for i,x in enumerate(cells):
    for j,y in enumerate(cells):
        JO[i][j]=CIDX[tuple(max(x[k],y[k]) for k in range(d))]
        ME[i][j]=CIDX[tuple(min(x[k],y[k]) for k in range(d))]
PERM=[]
for ps in product(*[list(permutations(range(x))) for x in DIMS]):
    m=[CIDX[tuple(ps[k][c[k]] for k in range(d))] for c in cells]
    PERM.append(m)
def sublat(mask):
    idx=[i for i in range(n) if mask>>i & 1]
    for a in range(len(idx)):
        ia=idx[a]
        for b in range(a+1,len(idx)):
            ib=idx[b]
            if not (mask>>JO[ia][ib] & 1): return False
            if not (mask>>ME[ia][ib] & 1): return False
    return True
def used(mask):
    for k in range(d):
        s=set()
        for i in range(n):
            if mask>>i & 1: s.add(cells[i][k])
        if len(s)<2: return False
    return True
t0=time.time()
R=bytearray(1<<n)
for mask in range(1,1<<n):
    if bin(mask).count('1')<3: continue
    if not used(mask): continue
    ok=0
    for m in PERM:
        nm=0
        for i in range(n):
            if mask>>i & 1: nm|=1<<m[i]
        if sublat(nm): ok=1; break
    R[mask]=ok+1
YES=[m for m in range(1<<n) if R[m]==2]
t1=time.time()-t0
from collections import Counter
dist=Counter(); mx=0
for m in YES:
    on=[i for i in range(n) if m>>i & 1]
    found=None
    for k in range(1,min(5,len(on))+1):
        for T in combinations(on,k):
            p=m
            for i in T: p&=~(1<<i)
            if R[p]==2: found=k; break
        if found: break
    if found is None:
        dist['base']+=1
    else:
        dist[found]+=1; mx=max(mx,found)
print("  %-12s cells %2d   subsets %8d   YES %6d   **max step %d**   %s   %.0fs"%(
    "×".join(map(str,DIMS)),n,2**n,len(YES),mx,
    dict(sorted((k,v) for k,v in dist.items() if k!='base')),t1))