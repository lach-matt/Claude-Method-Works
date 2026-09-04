import pickle, time, numpy as np
from itertools import product, permutations, combinations
D=pickle.load(open('/home/claude/stage/s1.pkl','rb'))
DIMS=D['dims']; cells=D['cells']; d=len(DIMS); n=len(cells)
print("="*80)
print("  STAGE 2 — REORDERABILITY OF EVERY SUBSET")
print("="*80)
ORD=[]
for ps in product(*[list(permutations(range(x))) for x in DIMS]):
    ORD.append(ps)
print("\n     orderings of the box : %d"%len(ORD))
# precompute, for each ordering, the permuted index of every cell
CIDX={c:i for i,c in enumerate(cells)}
PERM=[]
for ps in ORD:
    m=[0]*n
    for i,c in enumerate(cells):
        m[i]=CIDX[tuple(ps[k][c[k]] for k in range(d))]
    PERM.append(m)
# precompute join/meet tables on cell indices
JOIN=np.zeros((n,n),dtype=np.int16); MEET=np.zeros((n,n),dtype=np.int16)
for i,x in enumerate(cells):
    for j,y in enumerate(cells):
        JOIN[i,j]=CIDX[tuple(max(x[k],y[k]) for k in range(d))]
        MEET[i,j]=CIDX[tuple(min(x[k],y[k]) for k in range(d))]
print("     join/meet tables     : %dx%d"%(n,n))
t0=time.time()
def is_sublat_mask(mask):
    idx=[i for i in range(n) if mask>>i & 1]
    for a in range(len(idx)):
        for b in range(a+1,len(idx)):
            i,j=idx[a],idx[b]
            if not (mask>>int(JOIN[i,j]) & 1): return False
            if not (mask>>int(MEET[i,j]) & 1): return False
    return True
def used_all(mask):
    for k in range(d):
        vals={cells[i][k] for i in range(n) if mask>>i & 1}
        if len(vals)<2: return False
    return True
res=bytearray(1<<n)
done=0
for mask in range(1,1<<n):
    if bin(mask).count('1')<3: continue
    if not used_all(mask): continue
    ok=0
    for m in PERM:
        nm=0
        for i in range(n):
            if mask>>i & 1: nm |= 1<<m[i]
        if is_sublat_mask(nm): ok=1; break
    res[mask]=ok+1   # 1 = not reorderable, 2 = reorderable
    done+=1
    if done%20000==0: print("        %d processed  %.0fs"%(done,time.time()-t0))
print("\n     subsets qualifying   : %d"%done)
print("     reorderable          : %d"%sum(1 for m in range(1<<n) if res[m]==2))
print("     time                 : %.1fs"%(time.time()-t0))
pickle.dump(bytes(res),open('/home/claude/stage/s2.pkl','wb'))
print("\n     saved  /home/claude/stage/s2.pkl")