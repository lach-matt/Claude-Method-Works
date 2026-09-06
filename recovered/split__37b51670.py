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
SEAT=["nucleus","core","subvalence","valence","aggregate"]; PCA=["P","C","A"]
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
AX=[5,5,3]
base={(k,s,p) for _,k,s,p in C if s in (2,3)}
print("  DOES PCA WANT THE ENERGY AND THE SPLITTING ON DIFFERENT AXES?\n")
print(f"      {'Ka energy':<22}{'Ka splitting':<22}{'cells':>6}{'E':>4}")
best=[]
for pe in range(3):
    for ps in range(3):
        for se in (2,3):
            for ss in (2,3):
                cells = base | {(3,se,pe),(1,ss,ps)}
                E=minE(cells,AX)
                lab_e=f"{SEAT[se]}·{PCA[pe]}"; lab_s=f"{SEAT[ss]}·{PCA[ps]}"
                best.append((E,lab_e,lab_s,len(cells)))
best.sort()
seen=set()
for E,le,ls,n in best:
    if E>0: break
    print(f"      {le:<22}{ls:<22}{n:>6}{E:>4}")
print(f"\n      {sum(1 for b in best if b[0]==0)} of {len(best)} placements close.")
print("\n  and if BOTH are forced onto the SAME axis:")
for p in range(3):
    for s in (2,3):
        cells = base | {(3,s,p),(1,s,p)}
        print(f"      both at {SEAT[s]}·{PCA[p]:<3} cells {len(cells):>3}  E = {minE(cells,AX)}")