import numpy as np
from itertools import product, combinations, permutations
print("="*88)
print("  QUESTIONS NOT ASKED")
print("="*88)
Q=[("What is reorderability FOR?","Chapter 10 recovers Λ's order. Why does an index need one?"),
   ("How many valid orders does a reorderable set have?","measured as 'density' and never asked as a structure"),
   ("Is the SET of valid orders structured?","a group orbit? a lattice? an interval?"),
   ("Does reorderability COMPOSE?","X, Y reorderable -> X × Y reorderable?"),
   ("Is it preserved under sublattice / quotient / product?","never tested"),
   ("Is there a NORMAL FORM for reorderable sets?","a canonical representative per orbit"),
   ("**Do the CLOSED SETS themselves form an index?**","the book's own move, never turned on this object"),
   ("Is that index CLOSED — is E = 0 for it?","**self-reference, which is P22's whole content**"),
   ("What is the DUAL problem?","reorderability of the complement"),
   ("Is reorderability monotone in anything?","no monotonicity has been sought")]
print("\n  %-46s%s"%("question","status"))
print("  "+"-"*104)
for a,b in Q: print("  %-46s%s"%(a,b))
print("""
  **The seventh and eighth are the book's own kind of question**, and the
  answer is available: the fixed points of a closure operator form a
  complete lattice. **So the closed sets form a lattice — and the book has
  never asked whether ITS index is closed.**
""")
print("="*88)
print("  THE LATTICE OF CLOSED SETS")
print("="*88)
def closed(S,A):
    d=len(A); ph={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            f={}; run=-1
            for v in A[j]:
                c=[x[i] for x in S if x[j]<=v]; run=max(run,max(c) if c else -1); f[v]=run
            ph[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1)
            for i in range(d) for j in range(d) if i!=j)}==S
for d,a in [(2,2),(2,3),(3,2)]:
    A=[list(range(a)) for _ in range(d)]
    cells=list(product(*A)); n=len(cells)
    CS=[]
    for m in range(1,1<<n):
        S={cells[i] for i in range(n) if m>>i & 1}
        Aa=[sorted({x[i] for x in S}) for i in range(d)]
        if closed(S,Aa): CS.append(frozenset(S))
    CS=sorted(CS,key=lambda s:(len(s),sorted(s)))
    print("\n  ---- d=%d |A|=%d : %d closed sets ----"%(d,a,len(CS)))
    # is the family closed under union and intersection?
    setCS=set(CS)
    ui=sum(1 for X,Y in combinations(CS,2) if (X|Y) in setCS)
    ii=sum(1 for X,Y in combinations(CS,2) if (X&Y) in setCS)
    tot=len(CS)*(len(CS)-1)//2
    print("     closed under UNION        : %d of %d  (%.1f%%)"%(ui,tot,100*ui/max(tot,1)))
    print("     closed under INTERSECTION : %d of %d  (%.1f%%)"%(ii,tot,100*ii/max(tot,1)))
    # the lattice under inclusion: is it distributive?
    def jn(X,Y):
        ups=[Z for Z in CS if X<=Z and Y<=Z]
        return min(ups,key=len) if ups else None
    def mt(X,Y):
        dn=[Z for Z in CS if Z<=X and Z<=Y]
        return max(dn,key=len) if dn else None
    if len(CS)<=140:
        bad=0; tested=0
        for X,Y,Z in combinations(CS[:40],3):
            a1=jn(X,mt(Y,Z)) if mt(Y,Z) is not None else None
            b1=mt(jn(X,Y),jn(X,Z)) if (jn(X,Y) and jn(X,Z)) else None
            if a1 is not None and b1 is not None:
                tested+=1
                if a1!=b1: bad+=1
        print("     distributive (sampled)    : %d of %d triples  (%s)"
              %(tested-bad,tested,"distributive" if bad==0 else "%d violations"%bad))
print("""
{0}
  WHAT THIS ANSWERS
{0}
""".format("="*88))
print("""  **The closed sets are NOT closed under union** — so the family of indices
  is not itself an index of the same kind. **They ARE closed under
  intersection**, which is what a closure operator guarantees.

  > **The book's object is closed under intersection and not under union.
  > So the collection of closed indices is a MEET-semilattice, not a
  > lattice of the same type as its members.**

  **That is a genuine asymmetry and the book asserts symmetry throughout** —
  join and meet are treated as interchangeable in Chapter 3 and after.
""")