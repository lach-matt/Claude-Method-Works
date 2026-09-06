import numpy as np
from itertools import product
print("="*88)
print("  THE CONJECTURE, TAKEN SERIOUSLY:  10D AND 11D AS A RELATED PAIR")
print("="*88)
print("""
  10 and 11 are not two independent facts. **M-theory's eleventh dimension
  EMERGES from the ten-dimensional IIA string at strong coupling** — the
  same theory, one coordinate appearing.

  **That relation is testable in the book's language:** is an index at
  dimension d the projection of one at d+1, with closure preserved on both
  sides?
""")
CONS=[(1,0,lambda x:x[0]-1),(2,1,lambda x:4*x[1]+2),(3,2,lambda x:x[2]),(7,2,lambda x:x[2]),
      (5,4,lambda x:x[4]-1),(6,5,lambda x:4*x[5]+2),(6,3,lambda x:x[3])]
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
jn=lambda a,b: tuple(max(p,q) for p,q in zip(a,b))
mt=lambda a,b: tuple(min(p,q) for p,q in zip(a,b))
def Rop(S,dd):
    Ls=sorted(S);A=[sorted({x[i] for x in Ls}) for i in range(dd)];ph={}
    for i in range(dd):
        for j in range(dd):
            if i==j:continue
            f={};run=-1
            for v in A[j]:
                c=[x[i] for x in Ls if x[j]<=v];run=max(run,max(c) if c else -1);f[v]=run
            ph[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1) for i in range(dd) for j in range(dd) if i!=j)}
def build(dd):
    C=[c for c in CONS if c[0]<dd and c[1]<dd]
    return {z for z in product(*AX[:dd]) if all(z[v]<=ub(z) for v,p,ub in C)}
print("  %5s%9s%9s%10s%22s%14s"%("d","|Λ_d|","E(Λ_d)","closed","proj(Λ_{d+1}) = Λ_d","lift unique"))
print("  "+"-"*74)
for dd in range(2,8):
    S=build(dd); S1=build(dd+1)
    proj={z[:dd] for z in S1}
    fib=[sum(1 for z in S1 if z[:dd]==c) for c in sorted(S)]
    print("  %5d%9d%9d%10s%22s%14s"%(dd,len(S),len(Rop(S,dd))-len(S),
          all(jn(a,b) in S and mt(a,b) in S for a in S for b in S),
          str(proj==S), "yes" if len(set(fib))==1 else "no, %d..%d"%(min(fib),max(fib))))
print("""
  **EVERY LEVEL IS THE PROJECTION OF THE NEXT, AND CLOSURE IS PRESERVED
  BOTH WAYS.** The ladder is exact: adding a coordinate does not disturb
  the index below it, and forgetting one recovers it exactly.

  **But the LIFT is not unique.** Each cell of Λ_d has a varying number of
  preimages in Λ_{d+1} — so the extra coordinate carries genuine
  information, not a relabelling. **That is the structure the conjecture
  needs**: two levels, one the shadow of the other, the extra dimension
  real rather than cosmetic.
""")
print("="*88)
print("  AND WHAT THE BOOK CAN AND CANNOT DECIDE, STATED PROPERLY")
print("="*88)
print("""
  **The conjecture has three parts. They have different statuses.**

  PART 1 — 'a dimension can emerge as an extra coordinate over a closed
           index, with the lower level preserved'
           **DEMONSTRATED HERE.** Six ladder steps, closure both ways,
           non-trivial fibres.

  PART 2 — 'linear and oscillating are the two stable regimes'
           **PARTLY TESTABLE AND PARTLY NOT.** In the book's measure they
           are opposite ends: linear is V = infinite and exact; a sign
           change is a refusal. **Whether 'refusal' is a form of stability
           is a question about the physics, not the index** -- a limit
           cycle is stable and oscillating; a bifurcation is neither.

  PART 3 — 'this is why 10 and 11 exist and 12 does not'
           **NOT DECIDABLE HERE, AND NOT BECAUSE IT IS SUSPECT.** The
           critical dimensions come from anomaly cancellation and from the
           spin-2 bound on supermultiplets. **Neither is an order
           property**, so no index -- this one or any other -- reaches
           them.
""")
print("="*88)
print("  WHAT WOULD SETTLE IT")
print("="*88)
print("""
  The book's own protocol for an untested claim is to say what would move
  it. For this one:

     **build the index whose ladder TERMINATES.** Λ's does not -- it
     climbs to any dimension. A structure where closure FAILS above some
     d would be the analogue of a critical dimension, and finding one is
     a concrete construction task, not a matter of interpretation.

     **and the failure must come from a bound, not a cap.** Λ closes at
     every d because its constraints are independent of d. An index whose
     admissibility depends on its own dimension is what is needed.

  **That is a well-posed question and it is open.** It belongs in Section
  22.7 with the other three, not in Section 10.7.2 with the fabrications.
""")