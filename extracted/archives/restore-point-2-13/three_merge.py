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
L="spdfg"
print("  ADDING Λ_amp TO THE MERGED Λ_phys ⊕ Λ_charge\n")
print("      the merged index closed on (source, domain) with domain refined")
print("      by the charge regime. Λ_amp closes on (sequence, kind, ℓ).\n")
print("      the shared axis: an integral's ℓ IS a domain statement — F⁰(s,s)")
print("      holds for every atom, G²(s,d) only where a d subshell exists.\n")
SRC=["mathematics","standard","literature","this work"]
DOM=["universal","all elements","low","neutral","hydrogenic","one species"]
# merged phys+charge, (source, domain)
PC={(1,0),(0,0),(2,1),(0,1),(2,2),(3,1),(3,2),(3,3),(3,4)}
# Lambda_amp as (source, domain): every integral is MATHEMATICS in origin
# (the multipole expansion) and its domain is set by which l it needs
AMP=set()
for l in range(4):
    for i in range(l+1):
        for kind in (0,1):
            dom = 0 if l==0 else 1        # s integrals universal, others all-elements
            AMP.add((0,dom))
print(f"      Λ_phys ⊕ Λ_charge : {len(PC)} cells · E = {minE(PC,[4,6])[0]}")
print(f"      Λ_amp as (src,dom): {len(AMP)} cells · E = {minE(AMP,[4,6])[0]}")
M=PC|AMP
E,p=minE(M,[4,6])
print(f"      ALL THREE         : {len(M)} cells · E = {E}\n")
if E==0:
    print("      CLOSED.\n")
print(f"      source order : {' < '.join(SRC[i] for i in p[0])}")
print(f"      domain order : {' < '.join(DOM[i] for i in p[1])}\n")
print(f"      {'':<14}" + "".join(f"{DOM[i][:11]:>13}" for i in p[1]))
for s in p[0]:
    row=f"      {SRC[s]:<14}"
    for d in p[1]:
        row+=f"{('X' if (s,d) in M else '.'):>13}"
    print(row)
print()
print("  DOES THIS SOLVE THE PROBLEM?\n")
print("      what the merged index now states, for any atom (Z, c):")
print("          · which parameters apply to it        (domain ≡ regime)")
print("          · which integrals its competition uses (Λ_amp's triangle)")
print("          · where each came from                 (source)")
print()
print("      what it does NOT state: the VALUE of a.")
print()
print("      an index says which cells exist and how they order. it cannot")
print("      say what number sits in a cell. F⁰(4s,3d) and G²(4s,3d) are")
print("      named, their domain is fixed, their provenance is mathematics —")
print("      and their magnitudes are radial integrals over wavefunctions the")
print("      index does not contain.")
print()
print("      → the indexes have reduced the problem to two definite integrals.")
print("        computing them is not an indexing operation.")
