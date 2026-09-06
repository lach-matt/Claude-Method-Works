import numpy as np, random
from itertools import product, permutations
random.seed(79)
print("="*88)
print("  THE SIGN, DERIVED RATHER THAN GUESSED")
print("="*88)
print("""
  X is a downset iff (a',b') <= (a,b) in X implies (a',b') in X.

  Put b' = b. Then for every a' <= a:  b in S(a)  =>  b in S(a').

     **S(a) ⊆ S(a')  whenever a' <= a**

  **So supports DECREASE as the row index rises.** Rows must be sorted
  DESCENDING by support size. I sorted ascending — twice, once here and
  once on the calendar.  CORRECTION 131.
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
def canon(S,desc=True):
    A=alphabet(S,2)
    sup={a:frozenset(y for (x,y) in S if x==a) for a in A[0]}
    occ={b:sum(1 for a in A[0] if b in sup[a]) for b in A[1]}
    k=(lambda a:(-len(sup[a]),a)) if desc else (lambda a:(len(sup[a]),a))
    return [sorted(A[0],key=k), sorted(A[1],key=lambda b:(-occ[b],b))]
def reorderable_bf(S):
    A=alphabet(S,2)
    for p0 in permutations(A[0]):
        for p1 in permutations(A[1]):
            if is_downset(S,[list(p0),list(p1)]): return True
    return False
X={(0,1),(0,2),(0,3),(1,1)}
print("  the counterexample, both directions:\n")
for lab,d in [("ascending",False),("DESCENDING",True)]:
    print("     %-12s order %s  -> downset: %s"%(lab,canon(X,d),is_downset(X,canon(X,d))))
print("="*88)
print("  FULL RE-TEST")
print("="*88)
res={}
for lab,d in [("ascending",False),("descending",True)]:
    n=ok=0; bad=[]
    for _ in range(5000):
        A=[list(range(random.randint(2,5))),list(range(random.randint(2,5)))]
        cells=list(product(*A))
        S=set(random.sample(cells,random.randint(1,len(cells))))
        if not chain_ok(S): continue
        n+=1
        if is_downset(S,canon(S,d)): ok+=1
        elif len(bad)<2: bad.append(S)
    res[lab]=(n,ok,bad)
    print("     rows %-12s: %d of %d chain instances give a downset  (%.1f%%)"%(lab,ok,n,100*ok/max(n,1)))
n,ok,bad=res["descending"]
if bad:
    print("\n     remaining failures:")
    for S in bad: print("       X =",sorted(S)," reorderable:",reorderable_bf(S))
else:
    print("\n     **rows descending: no failures**")
print("="*88)
print("  AND THE CALENDAR / TABLE, RE-DERIVED FROM THE SAME SIGN")
print("="*88)
print("""
  The rule is one rule, not two: **sort BOTH axes descending — the parent
  by support size, the child by occupancy.**
""")
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
DAYS={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
CAL={(m,d) for m in range(1,13) for d in range(1,DAYS[m]+1)}
PT=set()
for g in (1,18): PT.add((1,g))
for p in (2,3):
    for g in list(range(1,3))+list(range(13,19)): PT.add((p,g))
for p in (4,5,6,7):
    for g in range(1,19): PT.add((p,g))
print("  %-22s%12s%16s"%("index","as printed","canon (desc)"))
print("  "+"-"*52)
for nm,S in [("periodic table",PT),("calendar",CAL)]:
    o=canon(S,True); idx=[{v:i for i,v in enumerate(p)} for p in o]
    T={(idx[0][x],idx[1][y]) for (x,y) in S}
    print("  %-22s%12d%16d"%(nm,len(Rop(S))-len(S),len(Rop(T))-len(T)))
print("""
  **One rule, derived from the definition, and it closes both.** The
  earlier claim that the table needed descending and the calendar ascending
  was an artefact of sorting the wrong axis in each case.
  CORRECTION 132.
""")