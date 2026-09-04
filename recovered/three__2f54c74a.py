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
    for perms in product(*[permutations(range(a)) for a in axes]):
        cs={tuple(perms[i].index(x[i]) for i in range(len(axes))) for x in cells}
        E=len(opR(cs,len(axes)))-len(cs)
        if best is None or E<best: best=E
    return best
print("  TEST 1 · Λ_phys WITHOUT 'source'\n")
# 22 parameters: (kind, source, domain, arity-band)
P=[(0,1,0,0),(0,1,0,0),(1,1,0,0),(1,1,0,0),(1,1,3,0),(2,2,1,2),(2,2,2,1),(2,2,3,0),
   (2,2,1,2),(2,2,2,1),(3,3,1,1),(3,3,1,0),(3,3,2,0),(4,3,2,1),(4,3,2,0),(4,3,2,0),
   (4,3,2,0),(4,3,2,0),(4,3,3,0),(4,3,1,0),(2,2,1,2),(3,3,2,0)]
c4={p for p in P}
print(f"      with source   : {len(c4)} cells · min E = {minE(c4,[5,4,4,3])}")
c3={(a,c,d) for a,b,c,d in P}
print(f"      without source: {len(c3)} cells · min E = {minE(c3,[5,4,3])}")
print()
print("  TEST 2 · Λ_var — THE REMAINING OBSERVER TRACE\n")
V=[("Z","nucleus","integer","input"),("Ne","core","integer","input"),
   ("c","nucleus+core","integer","input"),("l","rydberg","integer","input"),
   ("p","core+rydberg","integer","intermediate"),
   ("n0","core+rydberg","integer","intermediate"),
   ("l_core","core","integer","intermediate"),("n_out","core","integer","intermediate"),
   ("T","core+rydberg","integer","intermediate"),("u","nucleus+core","real","intermediate"),
   ("delta","rydberg","real","output"),("nstar","rydberg","real","output")]
BODY=["nucleus","core","rydberg","nucleus+core","core+rydberg"]
TY=["integer","real"]; RO=["input","intermediate","output"]
cells={(BODY.index(b),TY.index(t),RO.index(r)) for _,b,t,r in V}
print(f"      (body, type, role)      : {len(cells)} cells · min E = {minE(cells,[5,2,3])}")
c2={(BODY.index(b),RO.index(r)) for _,b,t,r in V}
print(f"      drop 'type'             : {len(c2)} cells · min E = {minE(c2,[5,3])}")
c2b={(BODY.index(b),TY.index(t)) for _,b,t,r in V}
print(f"      drop 'role'             : {len(c2b)} cells · min E = {minE(c2b,[5,2])}")
print()
print("      → 'role' is input/intermediate/output — WHERE IT SITS IN OUR")
print("        CALCULATION, not what it is. that is the observer trace.\n")
print("  TEST 3 · Λ_ryd RE-INDEXED ON p\n")
RY=[("Cd I s",5,3.6551,0.3354),("Cd I p",3,3.0522,-0.0082),("Cd I d",2,2.0837,0.1403),
    ("Cd I f",0,0.0393,-0.1808),("In I s",5,3.7193,0.3168),("In I d",2,2.3009,-1.0075),
    ("In I f",0,0.0416,-0.1838),("Rb I s",4,3.1308,0.1980),("Rb I p",3,2.6540,0.3258),
    ("Rb I d",1,1.3504,-0.7418),("Sr II s",4,2.7055,0.3394),("Sr II d",1,1.4514,0.5152),
    ("Sr II f",0,0.0648,-0.4054)]
PB=lambda p: 0 if p==0 else (1 if p<=2 else 2)
cl={(0,PB(p),1 if d0>0 else 0) for _,p,d0,d2 in RY} | \
   {(1,PB(p),1 if d2>0 else 0) for _,p,d0,d2 in RY}
print(f"      (order, p-band, sign)   : {len(cl)} cells · min E = {minE(cl,[2,3,2])}")
LM={"s":0,"p":1,"d":2,"f":3}
cl2={(0,LM[n.split()[-1]],1 if d0>0 else 0) for n,p,d0,d2 in RY} | \
    {(1,LM[n.split()[-1]],1 if d2>0 else 0) for n,p,d0,d2 in RY}
print(f"      (order, ℓ, sign) — old  : {len(cl2)} cells · min E = {minE(cl2,[2,4,2])}")