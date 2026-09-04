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
# property : KIND (what it measures) · SHELL (which it concerns) · BREADTH (class)
KIND=["count","symmetry","size","energy"]
SHELL=["the nucleus","the core","the subvalence shell","the valence shell"]
BREADTH=["every species","a block","a period","one subshell"]
C=[("ionisation energy",       3,3,0),
   ("ground configuration",    0,3,0),
   ("node count p",            0,3,0),
   ("closed f shell n_f",      0,2,2),
   ("subshell radius",         2,3,3),
   ("oxidation state +2",      0,3,1),
   ("closed core ¹S₀",         1,1,1),
   ("centrifugal barrier",     1,3,1),
   ("lanthanide contraction",  2,2,2),
   ("relativistic 7s",         2,3,2),
   ("electron affinity",       3,3,0),
   ("electronegativity",       3,3,0)]
print("  Λ_chem REINDEXED  —  property is a NAME, not a coordinate\n")
print("      the object coordinates of a chemical property:")
print("          KIND    what it measures : count · symmetry · size · energy")
print("          SHELL   which it concerns: nucleus · core · subvalence · valence")
print("          BREADTH which species    : every · a block · a period · one subshell\n")
print(f"      {'property':<24}{'kind':<11}{'shell':<22}{'breadth'}")
for nm,k,s,b in C:
    print(f"      {nm:<24}{KIND[k]:<11}{SHELL[s]:<22}{BREADTH[b]}")
cells={(k,s,b) for _,k,s,b in C}
print(f"\n      {len(C)} properties → {len(cells)} distinct cells\n")
E,p=minE(cells,[4,4,4])
print(f"  CLOSURE : min E = {E}\n")
print(f"      kind order    : {' < '.join(KIND[i] for i in p[0])}")
print(f"      shell order   : {' < '.join(SHELL[i] for i in p[1])}")
print(f"      breadth order : {' < '.join(BREADTH[i] for i in p[2])}\n")
if E>0:
    R=opR({tuple(p[i].index(x[i]) for i in range(3)) for x in cells},3)
    have={tuple(p[i].index(x[i]) for i in range(3)) for x in cells}
    print(f"  THE {E} DEFECT CELLS\n")
    for x in sorted(R-have):
        print(f"      {KIND[p[0][x[0]]]:<11}{SHELL[p[1][x[1]]]:<22}"
              f"{BREADTH[p[2][x[2]]]}")
else:
    print("      CLOSED.\n")
    print(f"      {'':<12}" + "".join(f"{BREADTH[i][:11]:>13}" for i in p[2]))
    for k in p[0]:
        for s in p[1]:
            row=f"      {KIND[k][:6]:<6}{SHELL[s][:5]:<6}"
            for b in p[2]:
                row+=f"{('X' if (k,s,b) in cells else '.'):>13}"
            if any((k,s,b) in cells for b in p[2]): print(row)
