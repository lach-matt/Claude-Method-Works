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
print("  THE SINGLETON-OUTPUT TEST, APPLIED TO ALL SEVEN\n")
print("      an index is closed when its OUTPUT class is a singleton.\n")
print(f"      {'index':<12}{'outputs':<28}{'count':>6}{'  verdict'}")
IX=[("Λ","the transfer q",1,"closed"),
    ("Λ_spectra","δ  (and n* derived)",2,"NOT closed — same fault"),
    ("Λ_phys","the parameter value",1,"closed by this test, E=6 by ℛ"),
    ("Λ_law","the law's form",1,"closed"),
    ("Λ_const","the constant's value",1,"closed"),
    ("Λ_var","δ and n*",2,"NOT closed — the fault found"),
    ("Λ_ryd","δ₀ and δ₂",2,"NOT closed — two Ritz orders")]
for n,o,c,v in IX:
    print(f"      {n:<12}{o:<28}{c:>6}   {v}")
print()
print("  Λ_var WITH δ ALONE\n")
V=[("Z","nucleus","input"),("Ne","core","input"),("c","nucleus+core","input"),
   ("l","rydberg","input"),("p","core+rydberg","intermediate"),
   ("n0","core+rydberg","intermediate"),("l_core","core","intermediate"),
   ("n_out","core","intermediate"),("T","core+rydberg","intermediate"),
   ("u","nucleus+core","intermediate"),("delta","rydberg","output")]
B=["nucleus","core","rydberg","nucleus+core","core+rydberg"]; R=["input","intermediate","output"]
c1={(B.index(b),R.index(r)) for _,b,r in V}
print(f"      δ alone : {len(c1)} cells · min E = {minE(c1,[5,3])}")
V2=V+[("nstar","rydberg","output")]
c2={(B.index(b),R.index(r)) for _,b,r in V2}
print(f"      + n*    : {len(c2)} cells · min E = {minE(c2,[5,3])}")
print()
print("  Λ_ryd WITH δ₀ ALONE  —  is δ₂ a second output or an intermediate?\n")
print("      δ₂ is not measured independently: it is fitted FROM the series.")
print("      so it is an INTERMEDIATE, not an output. reclassifying:\n")
RY=[("order0","series","output"),("order2","series","intermediate"),
    ("n","series","input"),("E","series","input"),("limit","series","input"),
    ("l","channel","input"),("p","channel","intermediate")]
BB=["series","channel"]
c3={(BB.index(b),R.index(r)) for _,b,r in RY}
print(f"      δ₀ output, δ₂ intermediate : {len(c3)} cells · min E = {minE(c3,[2,3])}")
c4={(BB.index(b),R.index(r)) for _,b,r in RY} | {(0,2)}
print()
print("  AND THE CONSEQUENCE FOR THE EQUATION\n")
print("      every result built in n* must be restated in δ:")
print("        · the Demkov–Ostrovsky slope-½ comparison — WAS AN IDENTITY (r.1273)")
print("        · the closure-cost tests — n* cost 0.327, δ 1.695 per element")
print("        · the n* = ℓ+1 non-penetrating result — restate as δ = 0")
print()
print("      the LAST of these survives restatement: for p = 0 and no collapse,")
print("      δ = 0 exactly, which is the hydrogenic statement and needs no n*.")
print("      the first two do not survive: both were about n*, and n* is")
print("      not an output of the index.")
