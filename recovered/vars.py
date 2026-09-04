import math
from itertools import product, permutations
# name, BODY (which of the three it describes), ORIGIN, TYPE, ROLE
V=[("Z","nucleus","given","integer","input"),
   ("Ne","core","given","integer","input"),
   ("c","nucleus+core","given","integer","input"),
   ("l","rydberg","given","integer","input"),
   ("p","core+rydberg","read","integer","intermediate"),
   ("n0","core+rydberg","derived","integer","intermediate"),
   ("l_core","core","read","integer","intermediate"),
   ("n_out","core","read","integer","intermediate"),
   ("T","core+rydberg","read","integer","intermediate"),
   ("u","nucleus+core","derived","real","intermediate"),
   ("delta","rydberg","measured","real","output"),
   ("nstar","rydberg","derived","real","output")]
BODY=["nucleus","core","rydberg","nucleus+core","core+rydberg"]
ORIG=["given","read","derived","measured"]
TYPE=["integer","real"]
ROLE=["input","intermediate","output"]
def opR(X,d):
    X=set(X); vals=[sorted({x[i] for x in X}) for i in range(d)]
    def env(i,j):
        m={}
        for x in X: m[x[j]]=max(m.get(x[j],-10**9),x[i])
        b,o=-10**9,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    return {x for x in product(*vals) if all(x[i]<=phi[(i,j)][x[j]]
            for i in range(d) for j in range(d) if i!=j)}
print("  Λ_var — THE VARIABLE INDEX\n")
print("      three bodies: nucleus (Z) · core (Nₑ−1) · Rydberg electron (n, ℓ)")
print("      and the pairwise relations between them.\n")
print(f"      {'variable':<9}{'body':<16}{'origin':<10}{'type':<9}{'role'}")
for n,b,o,t,r in V: print(f"      {n:<9}{b:<16}{o:<10}{t:<9}{r}")
print()
from collections import Counter
print("      by body : " + " · ".join(f"{k} {v}" for k,v in Counter(b for _,b,_,_,_ in V).most_common()))
print("      by origin: " + " · ".join(f"{k} {v}" for k,v in Counter(o for _,_,o,_,_ in V).most_common()))
print()
print("  DOES IT CLOSE?  (body, origin, type, role) — four coordinates\n")
best=None; hits=0; tot=0
for bp in permutations(BODY):
    bi={x:i for i,x in enumerate(bp)}
    for op in permutations(ORIG):
        oi={x:i for i,x in enumerate(op)}
        cells={(bi[b],oi[o],TYPE.index(t),ROLE.index(r)) for _,b,o,t,r in V}
        E=len(opR(cells,4))-len(cells); tot+=1
        if E==0: hits+=1
        if best is None or E<best[0]: best=(E,bp,op,cells)
E,bp,op,cells=best
print(f"      {tot} orderings (body × origin; type and role are already ordered)")
print(f"      minimum E = {E} · {hits} reach zero\n")
print(f"      body   order : {' < '.join(bp)}")
print(f"      origin order : {' < '.join(op)}\n")
print(f"      {len(cells)} distinct cells from {len(V)} variables")
if E>0:
    R=opR(cells,4)
    print(f"\n  THE {E} DEFECT CELLS\n")
    for x in sorted(R-cells)[:14]:
        print(f"      body {bp[x[0]]:<15} origin {op[x[1]]:<9} "
              f"{TYPE[x[2]]:<8} {ROLE[x[3]]}")