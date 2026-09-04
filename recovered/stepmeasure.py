import sys, random, time
from itertools import product, permutations, combinations
random.seed(619)
DIMS=tuple(int(x) for x in sys.argv[1].split(','))
NS=int(sys.argv[2]) if len(sys.argv)>2 else 400
d=len(DIMS); cells=list(product(*[range(x) for x in DIMS])); n=len(cells)
CIDX={c:i for i,c in enumerate(cells)}
JO=[[CIDX[tuple(max(x[k],y[k]) for k in range(d))] for y in cells] for x in cells]
ME=[[CIDX[tuple(min(x[k],y[k]) for k in range(d))] for y in cells] for x in cells]
PERM=[[CIDX[tuple(ps[k][c[k]] for k in range(d))] for c in cells]
      for ps in product(*[list(permutations(range(x))) for x in DIMS])]
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
C={}
def reord(mask):
    if mask in C: return C[mask]
    r=False
    for m in PERM:
        nm=0
        for i in range(n):
            if mask>>i & 1: nm|=1<<m[i]
        if sublat(nm): r=True; break
    C[mask]=r; return r
def close(mask):
    cur=mask
    while True:
        idx=[i for i in range(n) if cur>>i & 1]; add=0
        for a in range(len(idx)):
            for b in range(a+1,len(idx)):
                i,j=idx[a],idx[b]
                if not (cur>>JO[i][j] & 1): add|=1<<JO[i][j]
                if not (cur>>ME[i][j] & 1): add|=1<<ME[i][j]
        if not add: return cur
        cur|=add
from collections import Counter
dist=Counter(); t0=time.time(); got=0; tries=0
while got<NS and tries<NS*60 and time.time()-t0<420:
    tries+=1
    k=random.randint(2,min(n,10))
    seed=0
    for i in random.sample(range(n),k): seed|=1<<i
    m=close(seed)
    if bin(m).count('1')<4 or not used(m): continue
    got+=1
    on=[i for i in range(n) if m>>i & 1]
    found=None
    for kk in range(1,min(9,len(on))+1):
        hit=False
        cand=list(combinations(on,kk))
        if len(cand)>4000: cand=random.sample(cand,4000)
        for T in cand:
            p=m
            for i in T: p&=~(1<<i)
            if used(p) and reord(p): hit=True; break
        if hit: found=kk; break
    dist[found if found else '>8']+=1
print("  %-14s samples %4d   step distribution %s   **max %s**   %.0fs"%(
    "×".join(map(str,DIMS)),got,dict(sorted(dist.items(),key=lambda t:(str(t[0])))),
    max([k for k in dist if isinstance(k,int)],default='?'),time.time()-t0))