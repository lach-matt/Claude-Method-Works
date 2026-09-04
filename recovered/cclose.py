import math
from itertools import product, permutations
# name, value, ROLE, CARRIER, STANDING
K=[("M",1.5451,"scale","u","fitted"),
   ("u0",3.9854,"centre","u","fitted"),
   ("sigma",1.7206,"width","u","fitted"),
   ("C'",1.0065,"scale","u","measured"),
   ("beta",0.6667,"exponent","u","attributed"),
   ("half",0.5,"exponent","p","confirmed"),
   ("s_p",-0.069,"width","p","measured"),
   ("p_0",5.4,"centre","p","measured"),
   ("h_0",0.1779,"scale","Z-T","measured"),
   ("half_h",0.5,"exponent","l-lc","derived"),
   ("m_sw",-1.5,"centre","Z-T","measured"),
   ("w_sw",0.40,"width","Z-T","measured"),
   ("two_f",2.0,"centre","p","derived"),
   ("two_g",2.0,"centre","l-lc","measured")]
ROLE=["exponent","scale","centre","width"]
CARR=["u","p","l-lc","Z-T"]
STAND=["attributed","derived","confirmed","measured","fitted"]
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
print("  THE CONSTANT INDEX — h(ℓ) = h₀·√(2ℓ+1) replaces h(d) and h(f)\n")
print("      14 constants, but h_d and h_f collapse into h₀ and an exponent ½.\n")
best=None; hits=0; tot=0
for rp in permutations(ROLE):
    ri={r:i for i,r in enumerate(rp)}
    for cp in permutations(CARR):
        ci={c:i for i,c in enumerate(cp)}
        for sp in permutations(STAND):
            si={s:i for i,s in enumerate(sp)}
            cells={(ri[r],ci[c],si[s]) for _,_,r,c,s in K}
            E=len(opR(cells,3))-len(cells); tot+=1
            if E==0: hits+=1
            if best is None or E<best[0]: best=(E,rp,cp,sp,cells)
E,rp,cp,sp,cells=best
print(f"      {tot} orderings tested · minimum E = {E} · {hits} reach zero\n")
print(f"      role    order : {' < '.join(rp)}")
print(f"      carrier order : {' < '.join(cp)}")
print(f"      standing order: {' < '.join(sp)}\n")
print(f"      {len(cells)} distinct cells from 14 constants\n")
print("  THE GRID AT THE MINIMUM  (role × carrier)\n")
print(f"      {'':<11}" + "".join(f"{c:>10}" for c in cp))
for r in rp:
    row=f"      {r:<11}"
    for c in cp:
        got=[n for n,_,rr,cc,_ in K if rr==r and cc==c]
        row+=f"{(','.join(got) if got else '.'):>10}"
    print(row)
print()
if E>0:
    R=opR(cells,3)
    print(f"  THE {E} DEFECT CELLS\n")
    for x in sorted(R-cells):
        print(f"      role {rp[x[0]]:<10} carrier {cp[x[1]]:<8} standing {sp[x[2]]}")