import numpy as np
from itertools import product, permutations
print("="*88)
print("  THE FAILED REPAIR, AND WHAT IT POINTS AT")
print("="*88)
print("""
  Adding period WIDTH as a third coordinate left E at 36, because width is
  a FUNCTION of period — a redundant axis carries no information and the
  closure admits exactly what it did before.  CORRECTION 127.

  **The right question is the one §23.4 just answered: is the classroom
  table REORDERABLE?** Apply the chain criterion.
""")
PT=set()
for g in (1,18): PT.add((1,g))
for p in (2,3):
    for g in list(range(1,3))+list(range(13,19)): PT.add((p,g))
for p in (4,5,6,7):
    for g in range(1,19): PT.add((p,g))
sup={p:frozenset(g for (q,g) in PT if q==p) for p in range(1,8)}
print("  row supports (the group set of each period):\n")
for p in sorted(sup): print("     period %d : %d groups  %s"%(p,len(sup[p]),sorted(sup[p])[:6]+(['...'] if len(sup[p])>6 else [])))
chain=all(a<=b or b<=a for a in sup.values() for b in sup.values())
print("\n     supports form a chain under inclusion : **%s**"%chain)
def Rop(S,d=2):
    Ls=sorted(S);A=[sorted({x[i] for x in Ls}) for i in range(d)];ph={}
    for i in range(d):
        for j in range(d):
            if i==j:continue
            f={};run=-1
            for v in A[j]:
                c=[x[i] for x in Ls if x[j]<=v];run=max(run,max(c) if c else -1);f[v]=run
            ph[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1) for i in range(d) for j in range(d) if i!=j)}
print("     E in the printed order                : %d"%(len(Rop(PT))-len(PT)))
print("="*88)
print("  SO REORDER THE GROUP AXIS AS THE CRITERION PRESCRIBES")
print("="*88)
print("""
  Sort periods by support size, and groups by how many periods contain
  them. **That is the constructive half of the d = 2 result.**
""")
cnt={g:sum(1 for (p,q) in PT if q==g) for g in range(1,19)}
order=sorted(range(1,19),key=lambda g:(-cnt[g],g))
print("  group occupancy count, descending:\n")
print("     ",[(g,cnt[g]) for g in order])
gmap={g:i+1 for i,g in enumerate(order)}
PT2={(p,gmap[g]) for (p,g) in PT}
R2=Rop(PT2)
print("\n     after reordering groups : |X| = %d   |R(X)| = %d   **E = %d**"%(len(PT2),len(R2),len(R2)-len(PT2)))
print("="*88)
print("  WHICH SETTLES WHAT THE 36 ARE")
print("="*88)
if len(R2)-len(PT2)==0:
    print("""
  **THE 36 VANISH UNDER A REORDERING OF THE GROUP AXIS ALONE.** No new
  coordinate, no new constraint, no different layout — **the same 90 cells,
  the group labels permuted.**

     the chain criterion PREDICTED it: the period supports are nested,
     {1,18} ⊂ {1,2,13..18} ⊂ {1..18}

     and the construction DELIVERED it: sort groups by occupancy

  **So E(periodic table) = 36 measures a property of the PRINTING ORDER of
  the group axis, and nothing else.** Chapter 1 says the defect belongs to
  the drawing; **this says which feature of the drawing, and repairs it.**
""")
    print("     the repaired group order (old label -> new position):\n")
    for g in order[:9]: print("        group %2d -> %d"%(g,gmap[g]))
    print("        ...")
else:
    print("""
  **STILL NOT ZERO — E = %d.** The chain criterion says a valid ordering
  exists; the occupancy sort is not it. **The criterion is a decision
  procedure, and the constructive step needs the right sort key.**
"""%(len(R2)-len(PT2)))
    for pr in permutations(range(1,19)):
        pass
print("="*88)
print("  AND THE GENERAL LESSON FOR E(X)")
print("="*88)
print("""
  **Three diagnoses, distinguished by what the excess set contains:**

     a separating form exists in the excess   -> a missing CONSTRAINT,
                                                 recoverable (§ the triples)
     no form, but the supports form a chain   -> a bad ORDER,
                                                 repairable by sorting
     no form and no chain                     -> a missing COORDINATE,
                                                 and the axis must be found

  **E(X) alone does not say which. The excess set does**, and the test is
  two lines of arithmetic.
""")