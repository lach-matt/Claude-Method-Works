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
BREADTH=["every species","a block","a period","one subshell"]
# name, kind, seat, breadth
C=[
 # nuclear
 ("atomic mass",            0,0,0),("isotope abundance",      0,0,0),
 ("nuclear spin",           1,0,0),("radioactive half-life",  4,0,0),
 ("neutron cross-section",  2,0,0),("nuclear charge Z",       0,0,0),
 # core
 ("closed core ¹S₀",        1,1,1),("core binding energy",    3,1,0),
 ("lanthanide contraction", 2,2,2),("closed f shell n_f",     0,2,2),
 # valence — count
 ("ground configuration",   0,3,0),("node count p",           0,3,0),
 ("oxidation states",       0,3,1),("valence electron count", 0,3,0),
 ("coordination number",    0,3,1),
 # valence — energy
 ("ionisation energy",      3,3,0),("electron affinity",      3,3,0),
 ("electronegativity",      3,3,0),("successive IEs",         3,3,0),
 ("emission spectrum",      3,3,0),("colour of the ion",      3,3,1),
 # valence — size
 ("atomic radius",          2,3,0),("ionic radius",           2,3,0),
 ("covalent radius",        2,3,0),("subshell radius",        2,3,3),
 ("relativistic 7s",        2,3,2),
 # valence — symmetry
 ("centrifugal barrier",    1,3,1),("term symbol",            1,3,0),
 ("magnetic moment",        1,3,0),("paramagnetism",          1,3,1),
 # aggregate — properties of BULK matter, not of one atom
 ("density",                2,4,0),("melting point",          3,4,0),
 ("boiling point",          3,4,0),("hardness",               3,4,1),
 ("crystal structure",      1,4,1),("electrical conductivity",4,4,1),
 ("thermal conductivity",   4,4,1),("colour of the metal",    3,4,1),
 ("smell",                  4,4,1),("taste",                  4,4,1),
 ("metallic character",     1,4,2),("reactivity",             4,4,1),
]
print(f"  Λ_chem, FULL  —  {len(C)} properties\n")
print("      KIND    : count · symmetry · size · energy · rate")
print("      SEAT    : nucleus · core · subvalence · valence · THE AGGREGATE")
print("      BREADTH : every species · a block · a period · one subshell\n")
print("      the fifth SEAT is new: density, melting point, smell, hardness")
print("      are not properties of an isolated atom at all. they belong to")
print("      matter in bulk, and the index must say so.\n")
from collections import Counter
print("      by seat : " + " · ".join(f"{SEAT[k]}: {v}"
      for k,v in sorted(Counter(c[2] for c in C).items())))
print("      by kind : " + " · ".join(f"{KIND[k]}: {v}"
      for k,v in sorted(Counter(c[1] for c in C).items())))
cells={(k,s,b) for _,k,s,b in C}
print(f"\n      {len(C)} properties → {len(cells)} distinct cells\n")
E,p=minE(cells,[5,5,4])
print(f"  CLOSURE : min E = {E}\n")
print(f"      kind    : {' < '.join(KIND[i] for i in p[0])}")
print(f"      seat    : {' < '.join(SEAT[i] for i in p[1])}")
print(f"      breadth : {' < '.join(BREADTH[i] for i in p[2])}\n")
if E>0:
    R=opR({tuple(p[i].index(x[i]) for i in range(3)) for x in cells},3)
    have={tuple(p[i].index(x[i]) for i in range(3)) for x in cells}
    print(f"  THE {E} DEFECT CELLS\n")
    for x in sorted(R-have)[:20]:
        print(f"      {KIND[p[0][x[0]]]:<10}{SEAT[p[1][x[1]]]:<22}{BREADTH[p[2][x[2]]]}")
