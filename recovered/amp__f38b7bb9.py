import numpy as np, random
from itertools import product
from collections import Counter
random.seed(5)
CAP=lambda l:2*(2*l+1)
LAM=set()
for n in range(1,4):
  for l in range(0,min(n,2)):
    for k in range(1,min(CAP(l),3)+1):
      for q in range(0,k+1):
        for e in range(1,4):
          for f in range(0,min(e,2)):
            for g in range(0,min(q,CAP(f))+1):
              for S2 in range(0,k+1): LAM.add((n,l,k,q,e,f,g,S2))
d=8; LL=sorted(LAM)
AX=[sorted({x[i] for x in LL}) for i in range(d)]
grid=np.array(list(product(*AX)),dtype=np.int32)
arr=np.array(LL,dtype=np.int32)
def cons_of(A,amax=6):
    C=[]
    for i in range(d):
        for j in range(d):
            if i==j: continue
            for a in range(0,amax+1):
                C.append((i,j,a,int((A[:,i]-a*A[:,j]).max())))
    return C
def size(A):
    m=np.ones(len(grid),dtype=bool)
    for i,j,a,b in cons_of(A): m &= grid[:,i] <= a*grid[:,j]+b
    return int(m.sum())
base=size(arr)
print("="*84)
print("  IS A SINGLE FABRICATED CELL DETECTABLE FROM INSIDE?")
print("="*84)
print("""
  Additions are absorbed -- but at what cost? If inserting ONE cell forces
  the closure to admit MANY, the insertion leaves a signature. Measure the
  AMPLIFICATION:

        A(y) = |C(Lambda + y)| - |Lambda| - 1

  A(y) = 0 means the fabrication is invisible. A(y) > 0 means the index
  had to invent A(y) further cells to accommodate it.
""")
print("     |Lambda| = %d   |C(Lambda)| = %d   (fixed point: %s)"%(len(LAM),base,base==len(LAM)))
outside=[tuple(int(v) for v in g) for g in grid if tuple(int(v) for v in g) not in LAM]
print("     cells outside Lambda in the box: %d"%len(outside))
samp=random.sample(outside,220)
amps=[]
for y in samp:
    sup=np.array(LL+[y],dtype=np.int32)
    amps.append(size(sup)-len(LAM)-1)
amps=np.array(amps)
print("\n  AMPLIFICATION OVER %d RANDOM FABRICATIONS\n"%len(samp))
print("     minimum   %d"%amps.min())
print("     median    %.0f"%np.median(amps))
print("     mean      %.1f"%amps.mean())
print("     maximum   %d"%amps.max())
print("     A(y) = 0 (undetectable) : %d of %d   = %.1f%%"%((amps==0).sum(),len(amps),100*(amps==0).mean()))
print("     A(y) > 0 (detectable)   : %d of %d   = %.1f%%"%((amps>0).sum(),len(amps),100*(amps>0).mean()))
h=Counter(np.clip(amps,0,10))
print("\n     %-14s%s"%("amplification","count"))
for k in sorted(h): print("     %-14s%d"%(("%d"%k) if k<10 else ">=10",h[k]))
print("="*84)
print("  AND WHAT THE UNDETECTABLE ONES HAVE IN COMMON")
print("="*84)
inv=[y for y,a in zip(samp,amps) if a==0]
det=[y for y,a in zip(samp,amps) if a>0]
if inv:
    print("     invisible fabrications: %d"%len(inv))
    print("     their ranks:",sorted(Counter(sum(y) for y in inv).items())[:8])
    mx=[max(a) for a in AX]
    onface=sum(1 for y in inv if any(y[i]==mx[i] for i in range(d)))
    print("     on a box face: %d of %d"%(onface,len(inv)))
else:
    print("     **NONE. EVERY FABRICATION AMPLIFIES.**")
print("""
{0}
  THE ANSWER
{0}
""".format("="*84))
if (amps==0).sum()==0:
    print("""  **EVERY SINGLE FABRICATION IS DETECTABLE FROM INSIDE.**

  Inserting one cell forces the closure to admit a median of %.0f more.
  An index that grows by %.0f when told about one new cell is announcing
  that the cell does not belong.

  **SO THE ASYMMETRY IS WEAKER THAN CHAPTER 9 ASSUMES.** Self-consistency
  does defend against invention -- of a SINGLE cell. What it cannot detect
  is a fabricator who also supplies the amplification: add y AND its whole
  induced closure, and the index is consistent and silent.

  **THE REQUIRED FORGERY IS THEREFORE NOT ONE CELL BUT %.0f**, and that is
  a quantitative bound on how much work an undetectable fabrication costs.
"""%(np.median(amps),np.median(amps),np.median(amps)+1))
else:
    print("""  **NOT EVERY FABRICATION AMPLIFIES: %d of %d were invisible.**

  Those cells are absorbed with no trace, so the index cannot distinguish
  them from genuine ones. Chapter 9's D_phys is required for exactly this
  class, and the class is now measured rather than assumed.
"""%((amps==0).sum(),len(amps)))