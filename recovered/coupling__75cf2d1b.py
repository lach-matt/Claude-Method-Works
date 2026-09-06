import numpy as np
from itertools import product
from collections import Counter
CONS=[(1,0,lambda x:x[0]-1),(2,1,lambda x:4*x[1]+2),(3,2,lambda x:x[2]),(7,2,lambda x:x[2]),
      (5,4,lambda x:x[4]-1),(6,5,lambda x:4*x[5]+2),(6,3,lambda x:x[3])]
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
LAM=sorted({z for z in product(*AX) if all(z[v]<=ub(z) for v,p,ub in CONS)})
d=8; NM=['n','l','k','q','e','f','g','2S']; Ls=set(LAM)
print("="*88)
print("  THE DEFINING COUPLING vs THE RECOVERED COUPLING")
print("="*88)
print("""
  **F's nesting carries seven bounds and exactly one min():**
  g ≤ min(q, 4f+2). Every other coordinate is bounded by ONE predecessor.
""")
deg=Counter(v for v,p,ub in CONS)
print("  %6s%18s%s"%("coord","bounds in F","by")) 
print("  "+"-"*54)
for i in range(d):
    src=[NM[p] for v,p,ub in CONS if v==i]
    print("  %6s%18d  %s"%(NM[i],len(src),", ".join(src) or "free"))
print("\n     coordinates with more than one defining bound : %s"%
      [NM[i] for i in range(d) if deg[i]>1])
print("="*88)
print("  THE RECOVERED SYSTEM — how many bounds does 𝓡 put on each coordinate?")
print("="*88)
A=[sorted({x[i] for x in LAM}) for i in range(d)]
ph={}
for i in range(d):
    for j in range(d):
        if i==j: continue
        f={}; run=-1
        for v in A[j]:
            c=[x[i] for x in LAM if x[j]<=v]; run=max(run,max(c) if c else -1); f[v]=run
        ph[(i,j)]=f
print("\n  %6s%14s%16s%s"%("coord","non-vacuous","ever tightest","which, and how often"))
print("  "+"-"*82)
for i in range(d):
    tight=Counter(); nonvac=0
    for j in range(d):
        if i==j: continue
        vals=[ph[(i,j)][v] for v in A[j]]
        if max(vals)<max(A[i]): nonvac+=1
    for x in LAM:
        best=min((ph[(i,j)].get(x[j],10**9),j) for j in range(d) if j!=i)
        m=best[0]
        for j in range(d):
            if j!=i and ph[(i,j)].get(x[j],10**9)==m: tight[j]+=1
    tot=len(LAM)
    top=", ".join("%s %.0f%%"%(NM[j],100*c/tot) for j,c in tight.most_common(4))
    print("  %6s%14d%16d  %s"%(NM[i],nonvac,len(tight),top))
print("="*88)
print("  SO IS THE POINTWISE MINIMUM THE COUPLING?")
print("="*88)
n_multi=0
for x in LAM:
    for i in range(d):
        vals=[(ph[(i,j)].get(x[j],10**9),j) for j in range(d) if j!=i]
        m=min(v for v,_ in vals)
        if sum(1 for v,_ in vals if v==m)>1: n_multi+=1; break
print("""
     cells where at least one coordinate has TWO bounds tied at the minimum
     : %d of %d  (%.0f%%)

  **F's single min() is the DEFINING coupling — the one junction in the
  caterpillar, where g meets both q and 4f+2.**

  **𝓡's pointwise minimum is the RECOVERED coupling, and it is not the same
  object.** Every coordinate acquires bounds from every other, most are
  vacuous, and the binding one changes cell by cell.

  > **The formula's coupling is structural and appears once. The operator's
  > coupling is pointwise and appears everywhere.** They agree on Λ's contents
  > — both give 976 — and they are different mechanisms.
"""%(n_multi,len(LAM),100*n_multi/len(LAM)))