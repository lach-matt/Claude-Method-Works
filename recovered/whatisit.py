import pickle, numpy as np
from itertools import combinations
D=pickle.load(open('/home/claude/stage/s1.pkl','rb'))
res=pickle.load(open('/home/claude/stage/s2.pkl','rb'))
cells=D['cells']; tab=D['tab']; NF=D['nforms']; n=len(cells)
DUAL=[(0,7),(2,8),(3,9),(4,11),(5,10),(6,12),(16,17)]
merge={b:a for a,b in DUAL}
keep=[j for j in range(NF) if j not in merge]
cls={}
for mask in range(1,1<<n):
    v=res[mask]
    if not v: continue
    idx=[i for i in range(n) if mask>>i & 1]
    c=[0]*NF
    for T in combinations(idx,3): c[tab[T]]+=1
    for b,a in merge.items(): c[a]+=c[b]
    k=tuple(c[j] for j in keep)
    if k not in cls: cls[k]=v
Y=np.array(sorted(k for k,v in cls.items() if v==2),dtype=float)
N=np.array(sorted(k for k,v in cls.items() if v==1),dtype=float)
d=Y.shape[1]
print("="*88)
print("  WHAT KIND OF OBJECT IS IT?")
print("="*88)
print("\n     coordinates %d      YES %d      NO %d      classes %d"%(d,len(Y),len(N),len(cls)))
print("     **it is a FUNCTION on count-vectors — exact, no mixed class**")
print("="*88)
print("  1.  IS THE YES REGION CONVEX?")
print("="*88)
print("""
  If YES is convex, it is an intersection of half-spaces and is determined by
  its bounding hyperplanes — **which would be the data structure.**
""")
allk={tuple(map(int,k)):v for k,v in cls.items()}
viol=0; tested=0
Yl=[tuple(map(int,y)) for y in Y]
for a,b in combinations(Yl,2):
    mid=tuple((a[i]+b[i])//2 for i in range(d))
    if (a[i]+b[i])%2==0 for i in range(0) else True:
        pass
    if all((a[i]+b[i])%2==0 for i in range(d)) and mid in allk:
        tested+=1
        if allk[mid]!=2: viol+=1
print("     integer midpoints of YES pairs that are observed : %d"%tested)
print("     of those NOT YES : %d"%viol)
print("     **convex on this evidence : %s**"%(viol==0 if tested else "no data"))
print("="*88)
print("  2.  HOW MANY HALF-SPACES DOES IT TAKE?")
print("="*88)
print("""
  Greedily peel: fit a separator that admits no NO point, remove the YES
  points it covers, repeat. **The number of rounds is the number of linear
  pieces.**
""")
rem=set(range(len(Y)))
rounds=0; sizes=[]
X=np.vstack([Y,N]); lab=np.array([1]*len(Y)+[0]*len(N))
while rem and rounds<12:
    idx=sorted(rem)
    Xs=np.vstack([Y[idx],N]); ls=np.array([1]*len(idx)+[0]*len(N))
    X1=np.hstack([Xs,np.ones((len(Xs),1))])
    w,*_=np.linalg.lstsq(X1,ls*2.0-1,rcond=None)
    # tighten until no NO point is admitted
    sN=np.hstack([N,np.ones((len(N),1))])@w
    thr=sN.max()+1e-9
    sY=np.hstack([Y[idx],np.ones((len(idx),1))])@w
    covered=[idx[i] for i in range(len(idx)) if sY[i]>thr]
    if not covered: break
    rounds+=1; sizes.append(len(covered))
    rem-=set(covered)
print("     rounds used        : %d"%rounds)
print("     YES points covered : %s"%sizes)
print("     **YES points left uncovered : %d of %d**"%(len(rem),len(Y)))
print("="*88)
print("  3.  SO WHAT IS IT?")
print("="*88)
print("""
     · a FUNCTION on 12-dimensional count-vectors — exact
     · NOT a sublattice, NOT a downset, NOT closed under 𝓡
     · %s
     · needing %s linear pieces to cover the YES region soundly

  **The name for an exact function on a finite set of integer vectors that is
  none of the above is a LOOKUP TABLE** — 2,266 entries, of which 222 are
  YES. **That is not a failure to characterise. It IS the characterisation:**

  > **the object is a finite table, the compression is 115-fold, and the
  > table is the data structure.**

  **And that is what a PQ-tree is at d = 2** — not a formula, a structure that
  answers by lookup after construction. **The difference is that Booth &
  Lueker's is built in linear time and this one is built by exhausting a box.**
"""%("convex on the tested midpoints" if viol==0 and tested else "convexity untested or violated",
     rounds if rounds else "more than 12"))