import math
from itertools import product, permutations
V=[("Z","nucleus","integer","input"),("Ne","core","integer","input"),
   ("c","nucleus+core","integer","input"),("l","rydberg","integer","input"),
   ("p","core+rydberg","integer","intermediate"),
   ("n0","core+rydberg","integer","intermediate"),
   ("l_core","core","integer","intermediate"),
   ("n_out","core","integer","intermediate"),
   ("T","core+rydberg","integer","intermediate"),
   ("u","nucleus+core","real","intermediate"),
   ("delta","rydberg","real","output"),("nstar","rydberg","real","output")]
BODY=["nucleus","core","rydberg","nucleus+core","core+rydberg"]
TYPE=["integer","real"]; ROLE=["input","intermediate","output"]
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
print("  Λ_var WITHOUT 'origin' — how we got it is not what it is\n")
best=None; hits=0
for bp in permutations(BODY):
    bi={x:i for i,x in enumerate(bp)}
    cells={(bi[b],TYPE.index(t),ROLE.index(r)) for _,b,t,r in V}
    E=len(opR(cells,3))-len(cells)
    if E==0: hits+=1
    if best is None or E<best[0]: best=(E,bp,cells)
E,bp,cells=best
print(f"      120 body orderings · minimum E = {E} · {hits} reach zero\n")
print(f"      body order : {' < '.join(bp)}\n")
print(f"      {'':<15}" + "".join(f"{r:>14}" for r in ROLE))
for b in bp:
    row=f"      {b:<15}"
    for r in ROLE:
        got=[n for n,bb,tt,rr in V if bb==b and rr==r]
        row+=f"{(','.join(got) if got else '.'):>14}"
    print(row)
print()
if E>0:
    R=opR(cells,3)
    print(f"  THE {E} DEFECT CELLS\n")
    for x in sorted(R-cells):
        print(f"      body {bp[x[0]]:<15} {TYPE[x[1]]:<9} {ROLE[x[2]]}")
print()
print("  THE THREE-BODY READING\n")
print("      nucleus alone      : Z                     — one variable")
print("      core alone         : Nₑ, ℓ_core, n_out     — three")
print("      Rydberg alone      : ℓ, δ, n*              — three")
print("      nucleus + core     : c, u                  — two")
print("      core + Rydberg     : p, n₀, T              — three")
print("      nucleus + Rydberg  : —                     — NONE\n")
print("      the empty pair is the finding: the Rydberg electron never")
print("      couples to the nucleus except THROUGH the core. every variable")
print("      relating them (c, u) is a nucleus-core quantity that the")
print("      Rydberg electron then reads. that is the screening statement,")
print("      and it is a structural fact of the index, not a fit.")