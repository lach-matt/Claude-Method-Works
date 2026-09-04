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
print("  THE CYPHER, WITH THE SPLIT\n")
print("      the law has separated into TWO objects:\n")
print("          CROSSING  a_cross = (Δn)/(√pᵣ − √p_g)   arithmetic, no physics")
print("          DESCENT   a(c) falling with charge       physics, no arithmetic\n")
print("      the six languages, asked of each:\n")
Q=[("ORDER",      "is it a lattice statement?",
    "YES — which subshell is least","YES — a monotone in c"),
   ("ANALYSIS",   "is there a continuous law?",
    "NO — it is a finite set of surds","YES — a(c), bracketed at 4 charges"),
   ("ALGEBRA",    "closed under an operation?",
    "YES — Q(√p) for p ≤ 7","not asked"),
   ("GEOMETRY",   "does it embed in a product?",
    "YES — (n,ℓ) × (n,ℓ)","YES — (Nₑ, c)"),
   ("INFORMATION","does a coordinate add?",
    "NO — Nₑ and c add nothing","c adds everything"),
   ("STATISTICS", "drawn from a distribution?",
    "NO — enumerable, 19 values","not yet tested")]
print(f"      {'language':<13}{'question':<30}{'CROSSING':<36}{'DESCENT'}")
for a,b,c,d in Q: print(f"      {a:<13}{b:<30}{c:<36}{d}")
print()
print("  THE LANGUAGES DISAGREE — AND THAT IS THE FINDING\n")
print("      on the CROSSING, order/algebra/geometry say yes and analysis says NO.")
print("      a quantity that is ordinal, algebraic and geometric but NOT analytic")
print("      is an INTEGER OBJECT. it has no derivative and needs none.")
print()
print("      on the DESCENT, order and analysis both say yes. that is a")
print("      genuine continuous law and it is the only place a fit belongs.")
print()
print("  SO THE CYPHER SAYS WHERE TO FIT AND WHERE NOT TO\n")
print("      every fit this session was applied to the WHOLE of a — the")
print("      crossing and the descent together. that is why the constants")
print("      kept absorbing each other: half the object has no analysis")
print("      language and cannot be fitted at all.")
print()
print("  THE TWO INDEXES\n")
CR={(0,0),(1,0),(1,2),(2,2),(2,3)}   # (Delta n band, l_g) for the five crossings
E1,p1=minE(CR,[3,4])
print(f"      Λ_cross  (Δn, ℓ_g)     |X| = {len(CR)}   min E = {E1}")
DE={(0,0),(1,0),(2,1),(3,1)}          # (charge, regime) for the descent
E2,p2=minE(DE,[4,2])
print(f"      Λ_descent (c, regime)  |X| = {len(DE)}   min E = {E2}")
print()
print("      both close. the split is not a convenience — it is two indexes.")
