import pickle, time, numpy as np
from itertools import combinations, product, permutations
D=pickle.load(open('/home/claude/stage/s1.pkl','rb'))
cells=D['cells']; tab=D['tab']; NF=D['nforms']; DIMS=D['dims']; d=len(DIMS); n=len(cells)
CIDX={c:i for i,c in enumerate(cells)}
print("="*88)
print("  SUBLATTICE ENUMERATION WITH POLYNOMIAL DELAY  (Ganter's NextClosure)")
print("="*88)
print("""
  **A sublattice is a closed set of the join/meet closure operator**, so the
  family is a closure system — and closure systems enumerate in lexicographic
  order with POLYNOMIAL DELAY per set. **No subset scanning.**
""")
JO=np.zeros((n,n),dtype=np.int32); ME=np.zeros((n,n),dtype=np.int32)
for i,x in enumerate(cells):
    for j,y in enumerate(cells):
        JO[i,j]=CIDX[tuple(max(x[k],y[k]) for k in range(d))]
        ME[i,j]=CIDX[tuple(min(x[k],y[k]) for k in range(d))]
def close(mask):
    cur=mask
    while True:
        idx=[i for i in range(n) if cur>>i & 1]
        add=0
        for a in range(len(idx)):
            for b in range(a+1,len(idx)):
                i,j=idx[a],idx[b]
                jj=int(JO[i,j]); mm=int(ME[i,j])
                if not (cur>>jj & 1): add|=1<<jj
                if not (cur>>mm & 1): add|=1<<mm
        if not add: return cur
        cur|=add
def next_closure(A):
    """lexicographically next closed set after A, or None"""
    for i in range(n-1,-1,-1):
        if A>>i & 1:
            A &= ~(1<<i)
        else:
            B=close(A | (1<<i))
            if (B & ((1<<i)-1)) == (A & ((1<<i)-1)):
                return B
    return None
t0=time.time()
A=close(0); out=[]
while A is not None:
    out.append(A)
    A=next_closure(A)
    if len(out)>60000: break
te=time.time()-t0
print("     closed sets found (all sublattices, incl. empty) : %d"%len(out))
print("     time : %.2fs      per set : %.5fs"%(te,te/max(len(out),1)))
def alph_mask(m):
    return [sorted({cells[i][k] for i in range(n) if m>>i & 1}) for k in range(d)]
valid=[m for m in out if bin(m).count('1')>=3 and all(len(a)>=2 for a in alph_mask(m))]
print("     with ≥3 cells and ≥2 values per axis            : %d"%len(valid))
print("     **(the subset scan found 1,412)**")
print("="*88)
print("  AND THE SIGNATURES")
print("="*88)
def sig_mask(m):
    idx=[i for i in range(n) if m>>i & 1]
    c=[0]*NF
    for T in combinations(idx,3): c[tab[T]]+=1
    return tuple(c)
ORD=list(product(*[list(permutations(range(x))) for x in DIMS]))
PM=[]
for ps in ORD:
    mp=[0]*n
    for i,c in enumerate(cells): mp[i]=CIDX[tuple(ps[k][c[k]] for k in range(d))]
    PM.append(mp)
t0=time.time()
gen=set()
for m in valid:
    for mp in PM:
        nm=0
        for i in range(n):
            if m>>i & 1: nm|=1<<mp[i]
        if all(len(a)>=2 for a in alph_mask(nm)):
            gen.add(sig_mask(nm))
tg=time.time()-t0
print("\n     YES signatures generated : %d      time %.2fs"%(len(gen),tg))
res=pickle.load(open('/home/claude/stage/s2.pkl','rb'))
cls={}
for mask in range(1,1<<n):
    v=res[mask]
    if not v: continue
    k=sig_mask(mask)
    if k not in cls: cls[k]=v
Yex={k for k,v in cls.items() if v==2}
print("     exhaustive YES          : %d"%len(Yex))
print("     **missing from generation: %d      spurious: %d**"%(len(Yex-gen),len(gen-Yex)))
print("="*88)
print("  COST COMPARISON")
print("="*88)
print("""
     exhaustive scan  : 260,800 subsets × 72 orderings   ~127 s
     **NextClosure**  : %d closed sets, %.5f s each      ~%.2f s
     signatures       : %.2f s

  **Total %.2f s against 127 s — and the scan is 2^n while NextClosure is
  polynomial per output set.**
"""%(len(out),te/max(len(out),1),te,tg,te+tg))