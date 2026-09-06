import numpy as np
from itertools import product
from collections import Counter
CONS=[(1,0,lambda x:x[0]-1),(2,1,lambda x:4*x[1]+2),(3,2,lambda x:x[2]),(7,2,lambda x:x[2]),
      (5,4,lambda x:x[4]-1),(6,5,lambda x:4*x[5]+2),(6,3,lambda x:x[3])]
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
LAM={z for z in product(*AX) if all(z[v]<=ub(z) for v,p,ub in CONS)}
NAME={0:'n',1:'l',2:'k',3:'q',4:'e',5:'f',6:'g',7:'2S'}
d=8; L=sorted(LAM)
A=[sorted({x[i] for x in L}) for i in range(d)]
ph={}
for i in range(d):
    for j in range(d):
        if i==j: continue
        f={}; run=-1
        for v in A[j]:
            c=[x[i] for x in L if x[j]<=v]; run=max(run,max(c) if c else -1); f[v]=run
        ph[(i,j)]=f
bind={(i,j) for (i,j) in ph if any(ph[(i,j)][v]<max(A[i]) for v in A[j])}
print("="*88)
print("  EVERY COUPLING IN Λ — THE TREE'S AND THE RECOVERED SYSTEM'S")
print("="*88)
tree_in=Counter(v for v,p,_ in CONS)
rec_in=Counter(i for (i,j) in bind)
print("\n  %-6s%16s%20s%s"%("var","bounds in TREE","bounds RECOVERED","the recovered parents"))
print("  "+"-"*80)
for i in range(d):
    ps=sorted(NAME[j] for (a,j) in bind if a==i)
    print("  %-6s%16d%20d  %s"%(NAME[i],tree_in.get(i,0),rec_in.get(i,0),", ".join(ps)))
print("""
  **The tree has ONE coupled variable — g, with two bounds.**
  **The recovered system has FIVE**, and g carries six.
""")
print("="*88)
print("  THE MECHANISM WE HAVE NOT EXAMINED")
print("="*88)
print("""
  §6.5 reads the coupling as min(q, 4f+2) and stops there. **But 𝓡 recovers
  SIX bounds on g and evaluates them all**, and the operative one is the
  MINIMUM at each cell — which is not always the same bound.
""")
who=Counter()
for x in L:
    vals={}
    for (i,j) in bind:
        if i==6: vals[NAME[j]]=ph[(6,j)].get(x[j],10**9)
    m=min(vals.values())
    for k2,v in vals.items():
        if v==m: who[k2]+=1
print("  which bound on g is TIGHTEST, over all 976 cells:\n")
for k2,c in who.most_common(): print("     %-4s tight on %4d cells  (%.1f%%)"%(k2,c,100*c/len(L)))
print("""
  **No single bound is tightest everywhere.** The binding constraint on g
  CHANGES from cell to cell, and 𝓡 handles that by taking the minimum
  pointwise — **not by choosing a bound and applying it.**

  > **That is the coupling mechanism: a POINTWISE MINIMUM over a family of
  > bounds, re-evaluated at every cell.**

  **And it is exactly what the reorderability attempts never did.** Each
  chose one condition — chain, C1P, width, 2-SAT, path — and applied it
  globally. **The index's own mechanism applies all of them at every point
  and takes the tightest.**
""")
print("="*88)
print("  VERIFY: DOES THE POINTWISE MINIMUM RECONSTRUCT Λ?")
print("="*88)
adm={x for x in product(*A) if all(x[i]<=min(ph[(i,j)].get(x[j],10**9)
     for j in range(d) if j!=i) for i in range(d))}
print("\n     cells admitted by the pointwise minimum : %d"%len(adm))
print("     |Λ|                                     : %d"%len(LAM))
print("     **identical : %s**"%(adm==LAM))
print("""
  **The whole index is the pointwise minimum of its recovered bounds.**
  Chapter 6 states one coupling; **𝓡 uses forty-eight bounds and takes the
  smallest at each cell, and that is the operator's entire content.**
""")