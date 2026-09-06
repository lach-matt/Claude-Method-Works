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
print("  MERGING Λ_charge AND Λ_phys\n")
print("      Λ_charge : the roles c plays — screening, decay base, decay rate,")
print("                 ordering — on (role, carrier, sign, regime).  E = 0.")
print("      Λ_phys   : the parameters — on (kind, source, domain, arity). E = 6.\n")
print("      the claim: each is a product of the other. if so, merging them")
print("      should close, because the defect in one is supplied by the other.\n")
# Lambda_charge cells: (role, carrier, sign, regime)
CH=[(0,0,0,0),(0,0,0,1),(0,0,0,2),(1,1,0,0),(1,1,0,1),(1,1,0,2),
    (2,2,0,1),(2,2,0,2),(3,3,1,2)]
# Lambda_phys cells: (kind, domain, arity) -- source dropped, it did not help
PH=[(0,0,0),(1,0,0),(1,3,0),(2,1,2),(2,2,1),(2,3,0),(3,1,1),(3,1,0),(3,2,0),
    (4,2,1),(4,2,0),(4,3,0),(4,1,0)]
print(f"      Λ_charge alone : {len(set(CH))} cells · E = {minE(set(CH),[4,4,2,3])[0]}")
print(f"      Λ_phys alone   : {len(set(PH))} cells · E = {minE(set(PH),[5,4,3])[0]}")
print()
print("  THE MERGE — a parameter's ROLE and its DOMAIN are the shared axes\n")
print("      Λ_charge's 'role' and Λ_phys's 'kind' both say what a quantity DOES.")
print("      Λ_charge's 'regime' and Λ_phys's 'domain' both say WHERE it holds.")
print("      so the merge is on (does, where, and one axis from each).\n")
# merged: (does, where, carrier-or-arity)
M=set()
for r,c,s,g in CH: M.add((r,g,c))
for k,d,a in PH:   M.add((min(k,3),d,min(a,3)))
E,p=minE(M,[4,4,4])
print(f"      merged : {len(M)} cells · min E = {E}")
print(f"      does  order : {p[0]}")
print(f"      where order : {p[1]}")
print(f"      third order : {p[2]}\n")
R=opR({tuple(p[i].index(x[i]) for i in range(3)) for x in M},3)
have={tuple(p[i].index(x[i]) for i in range(3)) for x in M}
print(f"      |ℛ| = {len(R)}   held = {len(have)}   defect = {len(R)-len(have)}\n")
print("  AND THE READING\n")
print("      if E_merged < E_phys, the charge index SUPPLIES what the parameter")
print("      index was missing. if E_merged > both, they are not one object.")
print()
Ep=minE(set(PH),[5,4,3])[0]
print(f"      E(Λ_phys) = {Ep}   E(merged) = {E}")
if E<Ep: print("      → the merge REDUCES the defect. Λ_charge supplies Λ_phys.")
elif E==Ep: print("      → no change. they are independent, not products.")
else: print("      → the merge INCREASES it. they are not one index.")