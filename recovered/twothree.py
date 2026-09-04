import numpy as np, random
from itertools import product, permutations
random.seed(61)
print("="*88)
print("  THE 2/3 BOUNDARY — FIVE APPEARANCES.  ARE THEY THE SAME FACT?")
print("="*88)
CASES=[
 ("§6.7  constraint arity","every bound couples 2 variables -> tree -> closed form","3 variables -> cycles -> no closed form"),
 ("§16.x the pole","2 points determine a line -> V = infinite, exact","3 points needed for curvature -> V finite, a bracket is needed"),
 ("§23.4 reorderability","d = 2 -> chain certificate, in P","d = 3 -> slice-chain fails, open"),
 ("clause width","2 literals -> 2-SAT -> P","3 literals -> 3-SAT -> NP-complete"),
 ("§23.6 bodies","2 bodies -> separable, closed form","3 bodies -> Poincare, not integrable"),
]
print("\n  %-24s%-44s%s"%("where","two","three"))
print("  "+"-"*104)
for a,b,c in CASES: print("  %-24s%-44s%s"%(a,b[:44],c[:52]))
print("="*88)
print("  TEST 1 — DOES A THREE-VARIABLE CONSTRAINT ACTUALLY BREAK Λ?")
print("="*88)
CONS2=[(1,0,lambda x:x[0]-1),(2,1,lambda x:4*x[1]+2),(3,2,lambda x:x[2]),(7,2,lambda x:x[2]),
       (5,4,lambda x:x[4]-1),(6,5,lambda x:4*x[5]+2),(6,3,lambda x:x[3])]
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
BOX=list(product(*AX))
LAM={x for x in BOX if all(x[v]<=ub(x) for v,p,ub in CONS2)}
jn=lambda a,b: tuple(max(p,q) for p,q in zip(a,b)); mt=lambda a,b: tuple(min(p,q) for p,q in zip(a,b))
def Rop(S,d=8):
    Ls=sorted(S);A=[sorted({x[i] for x in Ls}) for i in range(d)];ph={}
    for i in range(d):
        for j in range(d):
            if i==j:continue
            f={};run=-1
            for v in A[j]:
                c=[x[i] for x in Ls if x[j]<=v];run=max(run,max(c) if c else -1);f[v]=run
            ph[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1) for i in range(d) for j in range(d) if i!=j)}
print("\n  add a genuine THREE-variable bound and measure what breaks:\n")
TRIPLES=[("g <= q + f",       lambda x: x[6]<=x[3]+x[5]),
         ("g <= k - q",       lambda x: x[6]<=x[2]-x[3]),
         ("q + g <= k",       lambda x: x[3]+x[6]<=x[2]),
         ("2S <= k + l - n",  lambda x: x[7]<=x[2]+x[1]-x[0])]
print("  %-20s%10s%10s%10s%12s"%("added constraint","cells","closed","E(X)","tree?"))
print("  "+"-"*64)
for nm,f in TRIPLES:
    S={x for x in LAM if f(x)}
    if not S: continue
    cl=all(jn(a,b) in S and mt(a,b) in S for a in S for b in S)
    E=len(Rop(S))-len(S)
    print("  %-20s%10d%10s%10d%12s"%(nm,len(S),cl,E,"no — 3 vars"))
print("""
  **A three-variable bound does NOT necessarily break join/meet closure.**
  What it breaks is the FACTORISATION: 𝓡 recovers only pairwise bounds, so
  a genuine triple constraint cannot be recovered — E(X) > 0 measures
  exactly the part 𝓡 cannot see.
""")
print("="*88)
print("  TEST 2 — SO THE FIVE CASES SPLIT INTO TWO GROUPS")
print("="*88)
print("""
  **Group A — 'pairwise structure is recoverable, triple structure is not.'**

     §6.7  R recovers pairwise bounds; a triple bound leaves E(X) > 0
     §23.4 d = 2 constraints are binary; d = 3 are ternary
     clause width  2-SAT is closed under resolution; 3-SAT is not

  **These are one fact in three notations: a binary relation has a
  transitive closure computable in polynomial time, and a ternary one
  does not.**

  **Group B — 'two points determine, three points do not.'**

     §16.x V = infinite when the second difference vanishes
     §23.6 two bodies separate; three do not

  **These are a different fact: a 2-parameter family is exactly
  determined by 2 observations, and adding a third parameter adds a
  degree of freedom that no finite set of pairwise facts fixes.**
""")
print("="*88)
print("  AND THE TEST THAT SEPARATES THEM")
print("="*88)
print("""
  Group A is about RECOVERY — what an operator can reconstruct.
  Group B is about DETERMINATION — what data can pin down.

  **They coincide numerically at 2/3 and they are not the same claim.**
  Evidence: Λ has 8 coordinates and is fully recoverable (Group A holds at
  d = 8), while its bracket still needs 3 points for curvature (Group B
  binds at 3 regardless of d).
""")
print("     Λ dimension                     : 8")
print("     𝓡 recovers it exactly           : %s"%(Rop(LAM)==LAM))
print("     bracket still needs 3 points    : yes — w and e are defined on {v-h, v, v+h}")
print("""
  **CORRECTION 126.** The five appearances of 2/3 in this work are not one
  pattern. **Three are the arity of a relation; two are the order of a
  derivative.** Calling them a single principle would be the kind of
  unification this book's own P21 exists to refuse — true in one language
  and false in another.
""")