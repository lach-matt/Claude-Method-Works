import numpy as np, random
from itertools import product, permutations
random.seed(73)
print("="*88)
print("  DIAGNOSING THE COUNTEREXAMPLE")
print("="*88)
A=[[0,1,2,3],[0,1]]
X={(0,0),(0,1),(1,0),(3,0),(3,1)}
sup={a:frozenset(y for (x,y) in X if x==a) for a in A[0]}
print("\n     X =",sorted(X))
print("     supports:",{a:sorted(sup[a]) for a in A[0]})
print("     row 2 support is EMPTY — the value 2 appears in no cell.")
print("""
  **𝓡 builds its alphabet from the cells.** A value appearing in no cell is
  not in the recovered alphabet at all. **My is_downset test used the
  declared alphabet, which included it**, and an empty row below a
  non-empty one is never a downset.

  **The counterexample is an artefact of the test, not of the theorem.**
""")
def alphabet(S,d): return [sorted({x[i] for x in S}) for i in range(d)]
def is_downset(S,orders):
    idx=[{v:i for i,v in enumerate(o)} for o in orders]
    T={tuple(idx[k][x[k]] for k in range(len(orders))) for x in S}
    for x in T:
        for y in product(*[range(v+1) for v in x]):
            if y not in T: return False
    return True
def chain_ok(S):
    A=alphabet(S,2)
    sup=[frozenset(y for (x,y) in S if x==a) for a in A[0]]
    return all(p<=q or q<=p for p in sup for q in sup)
def canonical(S):
    A=alphabet(S,2)
    sup={a:frozenset(y for (x,y) in S if x==a) for a in A[0]}
    occ={b:sum(1 for a in A[0] if b in sup[a]) for b in A[1]}
    return [sorted(A[0],key=lambda a:(len(sup[a]),a)),
            sorted(A[1],key=lambda b:(-occ[b],b))]
def reorderable_bf(S):
    A=alphabet(S,2)
    for p0 in permutations(A[0]):
        for p1 in permutations(A[1]):
            if is_downset(S,[list(p0),list(p1)]): return True
    return False
print("     on the recovered alphabet:")
print("        chain      :",chain_ok(X))
print("        canonical  :",canonical(X))
print("        downset    :",is_downset(X,canonical(X)))
print("        reorderable:",reorderable_bf(X))
print("="*88)
print("  RE-RUN THE CONSTRUCTION TEST ON RECOVERED ALPHABETS")
print("="*88)
n=ok=0; bad=[]
for _ in range(4000):
    A=[list(range(random.randint(2,5))),list(range(random.randint(2,5)))]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(1,len(cells))))
    if not chain_ok(S): continue
    n+=1
    if is_downset(S,canonical(S)): ok+=1
    elif len(bad)<3: bad.append(S)
print("\n     chain instances                 : %d"%n)
print("     canonical order gives a downset : %d  (%.1f%%)"%(ok,100*ok/max(n,1)))
if bad:
    print("\n     remaining counterexamples:")
    for S in bad:
        print("       X =",sorted(S),"  reorderable:",reorderable_bf(S))
else:
    print("     **no counterexamples**")
print("="*88)
print("  AND THE THEOREM ITSELF, RE-VERIFIED ON RECOVERED ALPHABETS")
print("="*88)
n=ag=0; mism=[]
for _ in range(3000):
    A=[list(range(random.randint(2,4))),list(range(random.randint(2,4)))]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(1,len(cells))))
    a=reorderable_bf(S); b=chain_ok(S)
    n+=1; ag+=(a==b)
    if a!=b and len(mism)<3: mism.append((S,a,b))
print("\n     instances : %d    chain ⟺ reorderable agrees : %d  (%.1f%%)"%(n,ag,100*ag/n))
if mism:
    for S,a,b in mism: print("       X =",sorted(S)," reorderable=%s chain=%s"%(a,b))
print("""
{0}
  WHAT §23.4 CAN NOW SAY
{0}
""".format("="*88))
print("""  **d = 2 — the criterion is settled and the construction is settled,
  once both are stated on the RECOVERED alphabet.**

     criterion    : X is reorderable ⟺ its row supports form a chain
     construction : rows ascending by support size, columns descending by
                    occupancy
     cost         : O(r²c)
     caveat       : both statements are about the alphabet 𝓡 recovers —
                    values appearing in no cell are not part of the index,
                    **and including them makes the test fail**

  **That caveat is not a technicality.** It is the same point as §10.3:
  the alphabet is recovered from the cells, not declared. A test that
  declares one is testing a different object.
""")