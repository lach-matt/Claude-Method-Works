import math
from itertools import product, permutations
K=[("M","scale","u"),("u0","centre","u"),("sigma","width","u"),("C'","scale","u"),
   ("beta","exponent","u"),("half","exponent","p"),("s_p","width","p"),
   ("p_0","centre","p"),("h_0","scale","Z-T"),("half_h","exponent","l-lc"),
   ("m_sw","centre","Z-T"),("w_sw","width","Z-T"),("two_f","centre","p"),
   ("two_g","centre","l-lc")]
ROLE=["exponent","scale","centre","width"]; CARR=["u","p","l-lc","Z-T"]
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
print("  DROPPING 'STANDING' — it is a coordinate of our EVIDENCE, not of the object\n")
best=None; hits=0; tot=0
for rp in permutations(ROLE):
    ri={r:i for i,r in enumerate(rp)}
    for cp in permutations(CARR):
        ci={c:i for i,c in enumerate(cp)}
        cells={(ri[r],ci[c]) for _,r,c in K}
        E=len(opR(cells,2))-len(cells); tot+=1
        if E==0: hits+=1
        if best is None or E<best[0]: best=(E,rp,cp,cells)
E,rp,cp,cells=best
print(f"      {tot} orderings · minimum E = {E} · {hits} reach zero\n")
print(f"      role    order : {' < '.join(rp)}")
print(f"      carrier order : {' < '.join(cp)}\n")
print(f"      {'':<11}" + "".join(f"{c:>12}" for c in cp))
for r in rp:
    row=f"      {r:<11}"
    for c in cp:
        got=[n for n,rr,cc in K if rr==r and cc==c]
        row+=f"{(','.join(got) if got else '.'):>12}"
    print(row)
print()
if E>0:
    R=opR(cells,2)
    print(f"  THE {E} DEFECT CELLS\n")
    for x in sorted(R-cells):
        print(f"      {rp[x[0]]:<10} × {cp[x[1]]}")
print()
print("  WHY 'STANDING' BREAKS IT\n")
print("      role and carrier are properties of the CONSTANT.")
print("      standing is a property of what WE KNOW about the constant.")
print("      an index whose coordinates mix the object with the observer")
print("      cannot close, because the observer's axis has no order the")
print("      object respects. Register A.derived's condition fails.")
