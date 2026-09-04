import math
from itertools import product, permutations
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
def minE(cells,axes):
    best=None
    for p in product(*[permutations(range(a)) for a in axes]):
        cs={tuple(p[i].index(x[i]) for i in range(len(axes))) for x in cells}
        E=len(opR(cs,len(axes)))-len(cs)
        if best is None or E<best[0]: best=(E,p)
    return best
KIND=["count","symmetry","size","energy","rate"]
SEAT=["the nucleus","the core","the subvalence shell","the valence shell","the aggregate"]
PCA=["P — a physics parameter","C — a charge role","A — an amplitude integral"]
# name, kind, seat, which of PCA it depends on
C=[("atomic mass",0,0,0),("isotope abundance",0,0,0),("nuclear spin",1,0,0),
   ("radioactive half-life",4,0,0),("neutron cross-section",2,0,0),
   ("nuclear charge Z",0,0,1),
   ("closed core ¹S₀",1,1,0),("core binding energy",3,1,1),
   ("lanthanide contraction",2,2,2),("closed f shell n_f",0,2,2),
   ("ground configuration",0,3,0),("node count p",0,3,0),
   ("oxidation states",0,3,1),("valence electron count",0,3,0),
   ("coordination number",0,3,2),
   ("ionisation energy",3,3,0),("electron affinity",3,3,2),
   ("electronegativity",3,3,1),("successive IEs",3,3,1),
   ("emission spectrum",3,3,0),("colour of the ion",3,3,2),
   ("atomic radius",2,3,0),("ionic radius",2,3,1),("covalent radius",2,3,2),
   ("subshell radius",2,3,2),("relativistic 7s",2,3,0),
   ("centrifugal barrier",1,3,0),("term symbol",1,3,0),
   ("magnetic moment",1,3,2),("paramagnetism",1,3,2),
   ("density",2,4,0),("melting point",3,4,2),("boiling point",3,4,2),
   ("hardness",3,4,2),("crystal structure",1,4,2),
   ("electrical conductivity",4,4,1),("thermal conductivity",4,4,1),
   ("colour of the metal",3,4,2),("smell",4,4,2),("taste",4,4,2),
   ("metallic character",1,4,1),("reactivity",4,4,1)]
print(f"  Λ_chem ⊕ PCA  —  breadth replaced by the PCA dependency\n")
print("      each chemical property depends on one of:")
print("          P  a physics parameter      (the corridor, t(ℓ), the floor)")
print("          C  a charge role            (screening, decay, ordering)")
print("          A  an amplitude integral    (F^k, G^k)\n")
from collections import Counter
print("      by PCA : " + " · ".join(f"{PCA[k][0]}: {v}"
      for k,v in sorted(Counter(c[3] for c in C).items())))
cells={(k,s,p) for _,k,s,p in C}
print(f"\n      {len(C)} properties → {len(cells)} distinct cells\n")
E,pm=minE(cells,[5,5,3])
print(f"  CLOSURE : min E = {E}\n")
print(f"      kind : {' < '.join(KIND[i] for i in pm[0])}")
print(f"      seat : {' < '.join(SEAT[i] for i in pm[1])}")
print(f"      PCA  : {' < '.join(PCA[i][0] for i in pm[2])}\n")
if E>0:
    R=opR({tuple(pm[i].index(x[i]) for i in range(3)) for x in cells},3)
    have={tuple(pm[i].index(x[i]) for i in range(3)) for x in cells}
    print(f"  THE {E} DEFECT CELLS\n")
    for x in sorted(R-have):
        print(f"      {KIND[pm[0][x[0]]]:<10}{SEAT[pm[1][x[1]]]:<22}"
              f"{PCA[pm[2][x[2]]]}")
else:
    print("      CLOSED.\n")
    print(f"      {'':<30}" + "".join(f"{PCA[i][0]:>6}" for i in pm[2]))
    for k in pm[0]:
        for s in pm[1]:
            if not any((k,s,p) in cells for p in range(3)): continue
            row=f"      {KIND[k]:<10}{SEAT[s]:<20}"
            for p in pm[2]:
                row+=f"{('X' if (k,s,p) in cells else '.'):>6}"
            print(row)
