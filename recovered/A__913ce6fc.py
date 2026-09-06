import random, pickle, time
from itertools import product, permutations, combinations
random.seed(631)
DIMS=(2,)*5; d=5
cells=list(product(*[range(2)]*5)); n=len(cells)
CIDX={c:i for i,c in enumerate(cells)}
JO=[[CIDX[tuple(max(x[k],y[k]) for k in range(d))] for y in cells] for x in cells]
ME=[[CIDX[tuple(min(x[k],y[k]) for k in range(d))] for y in cells] for x in cells]
PERM=[[CIDX[tuple(ps[k][c[k]] for k in range(d))] for c in cells]
      for ps in product(*[list(permutations(range(2)))]*5)]
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
print("="*84)
print("  STAGE A — COLLECT THE OVER-CAP CASES AT d = 5  (step > 4)")
print("="*84)
t0=time.time(); over=[]; got=0
while got<400 and time.time()-t0<300:
    k=random.randint(2,7); seed=0
    for i in random.sample(range(n),k): seed|=1<<i
    m=close(seed)
    if bin(m).count('1')<5 or not used(m): continue
    got+=1
    on=[i for i in range(n) if m>>i & 1]
    ok=False
    for kk in range(1,5):
        for T in combinations(on,kk):
            p=m
            for i in T: p&=~(1<<i)
            if used(p) and reord(p): ok=True; break
        if ok: break
    if not ok: over.append(m)
print("\n     sampled %d closed sets    over-cap (step > 4) : %d    %.0fs"%(got,len(over),time.time()-t0))
over=sorted(set(over))
pickle.dump({'over':over,'cells':cells},open('/home/claude/stage/over5.pkl','wb'))
print("     distinct over-cap sets saved : %d"%len(over))
print("\n  their sizes :",sorted(bin(m).count('1') for m in over))
from collections import Counter
print("  size distribution :",dict(sorted(Counter(bin(m).count('1') for m in over).items())))
print("\n  and the sizes of ALL sampled closed sets, for comparison:")