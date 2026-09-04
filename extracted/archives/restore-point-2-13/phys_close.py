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
# name, source(0=math 1=standard 2=literature 3=this work), domain, arity, REAL?
# domain: 0 universal, 1 all elements, 2 a region, 3 one species
P=[("R∞",1,0,3,True),("R_M",1,0,3,True),("a₀",1,0,2,True),("α",1,0,1,True),
   ("m_e/m_p",1,0,1,True),("2(2ℓ+1) Pauli",0,0,3,True),("n−ℓ−1 nodes",0,0,3,True),
   ("ℓ(ℓ+1) centrifugal",0,0,2,True),("Madelung n+ℓ",2,1,2,True),
   ("Janet boundary",2,1,3,True),("aufbau order",2,1,3,True),
   ("ionisation limit",2,1,3,True),("Seaton δ₂/δ₀",2,2,1,True),
   ("TF length Z^(−1/3)",2,1,2,True),("Slater σ",2,1,2,True),
   ("Hund's rules",2,1,2,True),("5σ threshold",2,0,1,False),
   ("a amplitude",3,1,3,True),("h₀ collapse",3,2,2,True),
   ("β = ⅔",3,1,3,True),("C′ = 1",3,1,2,True),("bracket surds",0,1,3,True)]
print("  Λ_phys REBUILT ON THE PERSON'S RULINGS\n")
print("      kind = source (one axis, not two)")
print("      parameters that are artefacts of the METHOD are excluded\n")
out=[p for p in P if not p[4]]
print(f"      excluded as method-physics: {', '.join(p[0] for p in out)}")
R=[p for p in P if p[4]]
print(f"      {len(R)} parameters of real atoms\n")
SRC=["mathematics","standard","literature","this work"]
DOM=["universal","all elements","a region","one species"]
cells={(s,d,a) for _,s,d,a,_ in R}
E,pm=minE(cells,[4,4,4])
print(f"  (source, domain, arity) : {len(cells)} cells · min E = {E}\n")
print(f"      source order : {' < '.join(SRC[i] for i in pm[0])}")
print(f"      domain order : {' < '.join(DOM[i] for i in pm[1])}")
print(f"      arity order  : {pm[2]}\n")
print(f"      {'':<14}" + "".join(f"{DOM[i][:12]:>14}" for i in pm[1]))
for s in pm[0]:
    row=f"      {SRC[s]:<14}"
    for d in pm[1]:
        got=[n for n,ss,dd,aa,_ in R if ss==s and dd==d]
        row+=f"{(str(len(got)) if got else '.'):>14}"
    print(row)
print()
if E>0:
    Rr=opR({tuple(pm[i].index(x[i]) for i in range(3)) for x in cells},3)
    have={tuple(pm[i].index(x[i]) for i in range(3)) for x in cells}
    print(f"  THE {E} DEFECT CELLS\n")
    for x in sorted(Rr-have):
        print(f"      source {SRC[pm[0][x[0]]]:<12} domain {DOM[pm[1][x[1]]]:<14}"
              f" arity {pm[2][x[2]]}")
print()
print("  AND WITHOUT ARITY  —  it is a property of the BOOK, not the parameter\n")
c2={(s,d) for _,s,d,a,_ in R}
E2,p2=minE(c2,[4,4])
print(f"      (source, domain) : {len(c2)} cells · min E = {E2}")
if E2==0: print("      → CLOSED.")
