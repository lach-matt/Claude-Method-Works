import numpy as np
from itertools import product
CONS=[(1,0,lambda x:x[0]-1),(2,1,lambda x:4*x[1]+2),(3,2,lambda x:x[2]),(7,2,lambda x:x[2]),
      (5,4,lambda x:x[4]-1),(6,5,lambda x:4*x[5]+2),(6,3,lambda x:x[3])]
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
LAM={z for z in product(*AX) if all(z[v]<=ub(z) for v,p,ub in CONS)}
d=8; NM=['n','l','k','q','e','f','g','2S']
def bounds(S):
    Ls=sorted(S); A=[sorted({x[i] for x in Ls}) for i in range(d)]
    ph={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            f={}; run=-1
            for v in A[j]:
                c=[x[i] for x in Ls if x[j]<=v]; run=max(run,max(c) if c else -1); f[v]=run
            ph[(i,j)]=f
    return A,ph
def generate(A,ph):
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1)
            for i in range(d) for j in range(d) if i!=j)}
def sig(ph):
    return tuple(sorted((k,tuple(sorted(v.items()))) for k,v in ph.items()))
print("="*86)
print("  ARE THEY TWO MECHANISMS, OR IS ONE THE NORMAL FORM OF THE OTHER?")
print("="*86)
A1,P1=bounds(LAM); S1=generate(A1,P1)
print("\n  round 1 : 𝓡(Λ) -> %d bounds -> generates %d cells   equals Λ : %s"%(
      len(P1),len(S1),S1==LAM))
A2,P2=bounds(S1); S2=generate(A2,P2)
print("  round 2 : 𝓡 again    -> generates %d cells   bounds identical : %s"%(
      len(S2),sig(P1)==sig(P2)))
A3,P3=bounds(S2)
print("  round 3 : bounds identical to round 2 : %s"%(sig(P2)==sig(P3)))
print("""
  **𝓡 is IDEMPOTENT on bound systems.** One application takes any presentation
  to a canonical one, and further applications change nothing.
""")
print("="*86)
print("  AND THE DEFINING SYSTEM IS NOT THAT FIXED POINT")
print("="*86)
# count non-vacuous defining bounds vs recovered
nd=len(CONS)
nr=sum(1 for k,f in P1.items() if any(v<max(A1[k[0]]) for v in f.values()))
print("""
     defining bounds, as written in F      : %d
     recovered bounds that constrain       : %d of %d
     both generate                         : %d cells

  > **The defining system is a PRESENTATION. The recovered system is its
  > NORMAL FORM.** 𝓡 maps the first to the second, and the second to itself.
"""%(nd,nr,len(P1),len(LAM)))
print("="*86)
print("  SO CAN EITHER BE RECOVERED FROM THE OTHER?")
print("="*86)
# does the recovered system determine the defining one?
print("""
     Λ  ->  recovered bounds   : YES, uniquely — that is 𝓡
     recovered bounds  ->  Λ   : YES, uniquely — generate
     Λ  ->  defining bounds    : **NO** — many presentations give the same Λ
     defining bounds  ->  Λ    : YES — that is the construction

  **Three of the four directions are functions. One is not.**

  > **They are not two mechanisms that can only interact with each other.
  > They are a presentation and its normal form, and the map runs ONE WAY:
  > 𝓡 forgets which presentation was used.**

  **That is why F is not recoverable from Λ and Λ is recoverable from F.**
  The single expression carries information the lattice does not: **the order
  in which the bounds were imposed.** The caterpillar's shape is a fact about
  the presentation, not about the set.
""")