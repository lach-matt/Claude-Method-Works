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
    return {x for x in product(*vals) if all(x[i]<=phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i!=j)}
def minE(cells,axes):
    b=None
    for p in product(*[permutations(range(a)) for a in axes]):
        cs={tuple(p[i].index(x[i]) for i in range(len(axes))) for x in cells}
        E=len(opR(cs,len(axes)))-len(cs)
        b=E if b is None else min(b,E)
        if b==0: return 0
    return b
KIND=["count","symmetry","size","energy","rate"]
SEAT=["the nucleus","the core","the subvalence shell","the valence shell","the aggregate"]
PCA=["P","C","A"]
C=[("atomic mass",0,0,0),("isotope abundance",0,0,0),("nuclear spin",1,0,0),
   ("radioactive half-life",4,0,0),("neutron cross-section",2,0,0),("nuclear charge Z",0,0,1),
   ("closed core 1S0",1,1,0),("core binding energy",3,1,1),
   ("lanthanide contraction",2,2,2),("closed f shell n_f",0,2,2),
   ("ground configuration",0,3,0),("node count p",0,3,0),("oxidation states",0,3,1),
   ("valence electron count",0,3,0),("coordination number",0,3,2),
   ("ionisation energy",3,3,0),("electron affinity",3,3,2),("electronegativity",3,3,1),
   ("successive IEs",3,3,1),("emission spectrum",3,3,0),("colour of the ion",3,3,2),
   ("atomic radius",2,3,0),("ionic radius",2,3,1),("covalent radius",2,3,2),
   ("subshell radius",2,3,2),("relativistic 7s",2,3,0),("centrifugal barrier",1,3,0),
   ("term symbol",1,3,0),("magnetic moment",1,3,2),("paramagnetism",1,3,2),
   ("density",2,4,0),("melting point",3,4,2),("boiling point",3,4,2),("hardness",3,4,2),
   ("crystal structure",1,4,2),("electrical conductivity",4,4,1),("thermal conductivity",4,4,1),
   ("colour of the metal",3,4,2),("smell",4,4,2),("taste",4,4,2),
   ("metallic character",1,4,1),("reactivity",4,4,1)]
def cells(props, seats):
    return {(k,s,p) for _,k,s,p in props if s in seats}
AX=[5,5,3]
print("  BASELINE — Λ_chem ⊕ PCA, PCA's own domain\n")
for lab,seats in (("subvalence + valence",{2,3}),("+ the core",{1,2,3}),
                  ("+ the nucleus",{0,1,2,3}),("+ the aggregate",{0,1,2,3,4})):
    cs=cells(C,seats); print(f"      {lab:<24}{len(cs):>3} cells   E = {minE(cs,AX)}")

print("\n  ADDING THE X-RAY OBSERVABLES — which seat keeps PCA closed?\n")
# Ka energy is an ENERGY; the doublet splits by j, which is a SYMMETRY.
XR=[("Ka transition energy",3),("Ka doublet splitting",1),("Moseley slope a",3)]
print(f"      {'seat':<24}{'PCA':<6}{'cells':>6}{'E':>5}")
for s in (1,2,3):
    for p in (0,1,2):
        cs=cells(C,{2,3}) | {(k,s,p) for _,k in XR}
        if s==1: cs = cells(C,{1,2,3}) | {(k,s,p) for _,k in XR}
        E=minE(cs,AX)
        mark = "  <-- closes" if E==0 else ""
        print(f"      {SEAT[s]:<24}{PCA[p]:<6}{len(cs):>6}{E:>5}{mark}")