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
print("  MERGING ON  domain ≡ regime  ALONE\n")
print("      Λ_phys  domain : universal · all elements · a region · one species")
print("      Λ_charge regime: neutral · low charge · hydrogenic\n")
print("      the claim: regime is 'a region' at finer resolution. so the merged")
print("      axis is  universal < all elements < neutral < low < hydrogenic <")
print("      one species — six levels, the middle three refining 'a region'.\n")
D=["universal","all elements","neutral","low","hydrogenic","one species"]
# (source, merged-domain) for the 21 real parameters
PH=[(1,0),(1,0),(1,0),(1,0),(1,0),(0,0),(0,0),(0,0),(2,1),(2,1),(2,1),(2,1),
    (2,3),(2,1),(2,1),(2,1),(3,1),(3,3),(3,1),(3,3),(0,1)]
# Λ_charge's four roles, each at its regime — source is 'this work' (3) for all
CH=[(3,2),(3,3),(3,4),(3,2),(3,3),(3,4),(3,3),(3,4),(3,4)]
print(f"      Λ_phys alone  : {len(set(PH))} cells · E = {minE(set(PH),[4,6])[0]}")
print(f"      Λ_charge alone: {len(set(CH))} cells · E = {minE(set(CH),[4,6])[0]}")
M=set(PH)|set(CH)
E,p=minE(M,[4,6])
print(f"      MERGED        : {len(M)} cells · E = {E}\n")
SRC=["mathematics","standard","literature","this work"]
print(f"      source order : {' < '.join(SRC[i] for i in p[0])}")
print(f"      domain order : {' < '.join(D[i] for i in p[1])}\n")
print(f"      {'':<14}" + "".join(f"{D[i][:11]:>13}" for i in p[1]))
for s in p[0]:
    row=f"      {SRC[s]:<14}"
    for d in p[1]:
        n=sum(1 for a,b in list(PH)+list(CH) if a==s and b==d)
        row+=f"{(str(n) if n else '.'):>13}"
    print(row)
print()
if E>0:
    R=opR({(p[0].index(a),p[1].index(b)) for a,b in M},2)
    have={(p[0].index(a),p[1].index(b)) for a,b in M}
    print(f"  THE {E} DEFECT CELLS\n")
    for x in sorted(R-have):
        print(f"      {SRC[p[0][x[0]]]:<14}{D[p[1][x[1]]]}")
else:
    print("  CLOSED — the charge regime IS the physics domain, refined.")
print()
print("  AND THE CALIBRATION TO EACH ATOM\n")
print("      a parameter's domain now reads as a SET OF ATOMS:")
print("          universal    : every atom and ion")
print("          all elements : every neutral")
print("          neutral      : c = 1 only")
print("          low          : c = 2")
print("          hydrogenic   : c ≥ 3")
print("          one species  : a single (Z, c)")
print()
print("      so for any atom the index says which parameters apply to IT —")
print("      which is the per-atom calibration the law needs.")
