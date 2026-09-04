import pickle, random, time
from itertools import product, permutations, combinations
random.seed(617)
DIMS=(2,2,2,2,2); d=5
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
def reord(mask):
    for m in PERM:
        nm=0
        for i in range(n):
            if mask>>i & 1: nm|=1<<m[i]
        if sublat(nm): return True
    return False
T1=set(pickle.load(open('/home/claude/stage/tbl_2x2x2x2x2_1.pkl','rb'))['table'])
print("="*84)
print("  WITNESS SEARCH AT d = 5")
print("="*84)
print("\n     step-1 table : %d sets"%len(T1))
print("""
  **A witness that step 1 is insufficient:** a set p, reorderable, not in the
  step-1 table, reachable from a table member by adding TWO cells.
""")
t0=time.time(); tried=0; found=[]
pool=random.sample(sorted(T1),min(4000,len(T1)))
for m in pool:
    off=[i for i in range(n) if not (m>>i & 1)]
    for a,b in combinations(off,2):
        p=m | (1<<a) | (1<<b)
        tried+=1
        if p in T1: continue
        if reord(p):
            found.append((m,p))
            if len(found)>=3: break
    if found and len(found)>=3: break
    if time.time()-t0>420: break
print("     2-cell additions tested : %d      time %.0fs"%(tried,time.time()-t0))
print("     **witnesses found       : %d**"%len(found))
if found:
    for m,p in found[:3]:
        print("        from %d cells to %d cells, escaping the table"%(bin(m).count('1'),bin(p).count('1')))
    print("\n     -> **step 1 is INSUFFICIENT at d = 5**")
else:
    print("""
     -> **no witness found. On this sample the step-1 fixed point is closed
        under 2-cell additions**, which is evidence that step 1 suffices at
        d = 5 — and that would REFUTE step = 2^(d−2).""")