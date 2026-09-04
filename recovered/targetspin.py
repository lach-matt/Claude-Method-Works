import numpy as np
from itertools import product, combinations
print("="*88)
print("  ITEM E — THE TARGET-SPIN AXIS")
print("="*88)
print("""
  §7.10: the index records the PARENT's spin (2S ≤ k) and not the TARGET's.
  **By the same construction the target's spin is bounded by the target's
  own capacity coordinate: 2S' ≤ g.**

  Build Λ₉ = Λ × {2S'} with that bound and test everything Λ was tested for.
""")
AX8=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
     list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
C8=[(1,0,lambda x:x[0]-1),(2,1,lambda x:4*x[1]+2),(3,2,lambda x:x[2]),(7,2,lambda x:x[2]),
    (5,4,lambda x:x[4]-1),(6,5,lambda x:4*x[5]+2),(6,3,lambda x:x[3])]
LAM8={z for z in product(*AX8) if all(z[v]<=ub(z) for v,p,ub in C8)}
AX9=AX8+[list(range(0,4))]
C9=C8+[(8,6,lambda x:x[6])]
LAM9={z for z in product(*AX9) if all(z[v]<=ub(z) for v,p,ub in C9)}
NM=['n','l','k','q','e','f','g','2S','2S\'']
def E(S,d):
    Ls=sorted(S); A=[sorted({x[i] for x in Ls}) for i in range(d)]
    ph={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            f={}; run=-1
            for v in A[j]:
                c=[x[i] for x in Ls if x[j]<=v]; run=max(run,max(c) if c else -1); f[v]=run
            ph[(i,j)]=f
    adm={x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1)
         for i in range(d) for j in range(d) if i!=j)}
    return len(adm)-len(S)
def sublat(S,d):
    Ss=set(S)
    for x,y in combinations(sorted(S),2):
        if tuple(max(x[i],y[i]) for i in range(d)) not in Ss: return False
        if tuple(min(x[i],y[i]) for i in range(d)) not in Ss: return False
    return True
def rank_mod(S,d,cap=200000):
    Ls=sorted(S); n=0; bad=0
    for x,y in combinations(Ls,2):
        j=tuple(max(x[i],y[i]) for i in range(d)); m=tuple(min(x[i],y[i]) for i in range(d))
        n+=1
        if sum(j)+sum(m)!=sum(x)+sum(y): bad+=1
        if n>=cap: break
    return n,bad
print("="*88)
print("  1.  SIZE AND CLOSURE")
print("="*88)
print("\n     |Λ₈| = %d      |Λ₉| = %d      ratio %.3f"%(len(LAM8),len(LAM9),len(LAM9)/len(LAM8)))
print("     box₉ = %d      density %.4f"%(int(np.prod([len(a) for a in AX9])),len(LAM9)/np.prod([len(a) for a in AX9])))
print("\n     **E(Λ₉) = %d**"%E(LAM9,9))
print("     sublattice : %s"%sublat(LAM9,9))
n,bad=rank_mod(LAM9,9)
print("     rank modular : %d pairs tested, %d violations"%(n,bad))
print("="*88)
print("  2.  DOES Λ₈ SURVIVE AS A PROJECTION?")
print("="*88)
proj={tuple(x[:8]) for x in LAM9}
print("\n     projection of Λ₉ onto the first 8 axes : %d cells"%len(proj))
print("     **equals Λ₈ : %s**"%(proj==LAM8))
fib={}
for x in LAM9: fib.setdefault(x[:8],0)
for x in LAM9: fib[x[:8]]+=1
print("     fibre sizes : min %d  max %d  mean %.2f"%(min(fib.values()),max(fib.values()),np.mean(list(fib.values()))))
print("="*88)
print("  3.  THE CONSTRAINT GRAPH")
print("="*88)
print("""
     Λ₈ : 7 bounds, 8 variables -> k = 0, a tree
     Λ₉ : 8 bounds, 9 variables -> k = %d
"""%(8-9+1))
print("     the new edge 2S' — g attaches a LEAF. **Still a tree.**")
print("="*88)
print("  4.  AND THE SINGLE EXPRESSION")
print("="*88)
print("""
  §6: F(z) = Σ over Λ of ∏ z_i^{x_i}. The 2S' factor is a pendant on g, so
  it contributes Σ_{2S'=0}^{g} z₉^{2S'} — **the same shape as the 2S pendant
  on k.** The expression extends by one factor of the identical form.
""")
def F_at(S,d,z):
    return sum(np.prod([z**x[i] for i in range(d)]) for x in S)
print("     F₈(1) = %d      F₉(1) = %d"%(int(F_at(LAM8,8,1)),int(F_at(LAM9,9,1))))
print("     F₈(-1) = %d     **F₉(-1) = %d**"%(int(round(F_at(LAM8,8,-1))),int(round(F_at(LAM9,9,-1)))))
print("="*88)
print("  5.  RANK STRUCTURE")
print("="*88)
from collections import Counter
r8=Counter(sum(x) for x in LAM8); r9=Counter(sum(x) for x in LAM9)
print("\n     Λ₈ : %d rank levels, widest %d at rank %d"%(len(r8),max(r8.values()),max(r8,key=r8.get)))
print("     Λ₉ : %d rank levels, widest %d at rank %d"%(len(r9),max(r9.values()),max(r9,key=r9.get)))
lc=all(r9[k]**2>=r9.get(k-1,0)*r9.get(k+1,0) for k in sorted(r9)[1:-1])
print("     Λ₉ rank sequence log-concave : %s"%lc)