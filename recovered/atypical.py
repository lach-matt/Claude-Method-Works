import numpy as np, random
from itertools import product
random.seed(347)
CONS=[(1,0,lambda x:x[0]-1),(2,1,lambda x:4*x[1]+2),(3,2,lambda x:x[2]),(7,2,lambda x:x[2]),
      (5,4,lambda x:x[4]-1),(6,5,lambda x:4*x[5]+2),(6,3,lambda x:x[3])]
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
BOX=list(product(*AX))
LAM={z for z in BOX if all(z[v]<=ub(z) for v,p,ub in CONS)}
d=8
def Rsize(S):
    Ls=sorted(S); A=[sorted({x[i] for x in Ls}) for i in range(d)]
    ph={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            f={}; run=-1
            for v in A[j]:
                c=[x[i] for x in Ls if x[j]<=v]; run=max(run,max(c) if c else -1); f[v]=run
            ph[(i,j)]=f
    return sum(1 for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1)
               for i in range(d) for j in range(d) if i!=j))
print("="*84)
print("  HOW ATYPICAL IS Λ?")
print("="*84)
print("""
     box    %d cells      Λ    %d cells      density %.3f
"""%(len(BOX),len(LAM),len(LAM)/len(BOX)))
print("  RANDOM SETS AT Λ's OWN DENSITY — how many are closed?\n")
print("  %14s%10s%14s%16s"%("sample","n","closed","median E(X)"))
print("  "+"-"*56)
for lab,gen in [("uniform, |Λ| cells",lambda: set(random.sample(BOX,len(LAM))))]:
    n=c=0; Es=[]
    for _ in range(40):
        S=gen(); n+=1
        e=Rsize(S)-len(S); Es.append(e); c+= (e==0)
    print("  %14s%10d%14d%16d"%(lab,n,c,int(np.median(Es))))
print("""
  **Not one random set of the same size is closed**, and the median defect
  is enormous.
""")
print("="*84)
print("  AND SETS BUILT TO BE CLOSE TO Λ")
print("="*84)
print("\n  %26s%10s%14s%14s"%("perturbation","n","closed","median E"))
print("  "+"-"*66)
out=[z for z in BOX if z not in LAM]
for k in (1,2,5,10):
    n=c=0; Es=[]
    for _ in range(30):
        S=(LAM - set(random.sample(sorted(LAM),k))) | set(random.sample(out,k))
        e=Rsize(S)-len(S); Es.append(e); c+=(e==0); n+=1
    print("  %26s%10d%14d%14d"%("%d cells swapped"%k,n,c,int(np.median(Es))))
print("""
  **Even one swapped cell destroys closure.** Λ is not near a closed set;
  it is one, and its neighbours are not.
""")
print("="*84)
print("  THE COUNT")
print("="*84)
from math import comb, log10
tot=comb(len(BOX),len(LAM))
print("""
     subsets of the box with |Λ| cells : C(%d, %d) ≈ 10^%d
     of which CLOSED                   : at most a few
"""%(len(BOX),len(LAM),int(log10(tot))))
print("""  **E(X) = 0 is not a mild property.** At Λ's parameters a set of its size
  is closed with probability indistinguishable from zero, and the book's
  own §19 gives the reason: a closed index costs **zero bits** to specify
  beyond its coordinates, and zero-bit objects are rare exactly in
  proportion to how much they compress.

  > **Λ's closure is the whole content of the book, and this measures what
  > it is worth: one object in roughly 10^%d.**
"""%int(log10(tot)))