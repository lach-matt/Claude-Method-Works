import math
from itertools import product
from collections import Counter
# constant, value, ROLE, CARRIER, STANDING, ARITY (how many laws use it)
K=[("M",1.5451,"scale","u","fitted",1),
   ("u0",3.9854,"centre","u","fitted",1),
   ("sigma",1.7206,"width","u","fitted",1),
   ("C'",1.0065,"scale","u","measured",1),
   ("beta",0.6667,"exponent","u","attributed",3),
   ("half",0.5,"exponent","p","confirmed",2),
   ("s_l",0.113,"scale","u","measured",1),
   ("u_l",2.5,"centre","u","measured",1),
   ("h_d",0.40,"scale","Z-T","measured",1),
   ("h_f",0.468,"scale","Z-T","derived",1),
   ("m_sw",-1.5,"centre","Z-T","measured",1),
   ("w_sw",0.40,"width","Z-T","measured",1),
   ("two_f",2.0,"centre","p","derived",1),
   ("two_g",2.0,"centre","l-lcore","measured",1)]
ROLE=["exponent","scale","centre","width"]
CARR=["p","l-lcore","Z-T","u"]
STAND=["attributed","derived","confirmed","measured","fitted"]
cells={(ROLE.index(r),CARR.index(c),STAND.index(s),min(a,3))
       for _,_,r,c,s,a in K}
def op_R(X,d):
    X=set(X); vals=[sorted({x[i] for x in X}) for i in range(d)]
    def env(i,j):
        m={}
        for x in X: m[x[j]]=max(m.get(x[j],-10**9),x[i])
        b,o=-10**9,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    return {x for x in product(*vals)
            if all(x[i]<=phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i!=j)}
R=op_R(cells,4)
box=1
for i in range(4): box*=len({c[i] for c in cells})
print("  THE CONSTANT INDEX  Λ_const\n")
print("      coordinates: role (exponent→width) · carrier · standing · arity\n")
print(f"      {len(K)} constants · {len(cells)} distinct cells")
print(f"      |ℛ(X)| = {len(R)}   E = {len(R)-len(cells)}   box = {box}\n")
print("  THE (ROLE × CARRIER) GRID\n")
print(f"      {'':<10}" + "".join(f"{c:>12}" for c in CARR))
for r in ROLE:
    row=f"      {r:<10}"
    for c in CARR:
        got=[n for n,_,rr,cc,_,_ in K if rr==r and cc==c]
        row+=f"{(','.join(got) if got else '.'):>12}"
    print(row)
print()
print("  WHAT THE EMPTY CELLS WOULD BE\n")
W={("exponent","p"):"HELD — the ½ on √p",
   ("exponent","l-lcore"):"an exponent in the gate variable — none known",
   ("exponent","Z-T"):"an exponent in the collapse distance — none known",
   ("scale","p"):"a scale per core shell — subsumed into M",
   ("scale","l-lcore"):"a scale in the gate — the gate is binary, so none",
   ("centre","Z-T"):"HELD — the switch centre",
   ("width","p"):"a width in p — where √p blurs, which is LAW 2 in another carrier",
   ("width","l-lcore"):"a width on the gate — how sharp the ℓ−ℓ_core ≥ 2 cut is",
   ("width","Nₑ"):"—"}
for r in ROLE:
    for c in CARR:
        if not [1 for _,_,rr,cc,_,_ in K if rr==r and cc==c]:
            print(f"      {r:<10}× {c:<10}{W.get((r,c),'—')}")
print()
print("  WHAT THE LATTICE SAYS\n")
print("      1 · every WIDTH we hold is in u or Z−T. There is no width in p and")
print("          no width on the gate — yet law 2 IS a width in p, written in u.")
print("          the same law appears in two carriers and we hold only one.")
print()
print("      2 · every CENTRE is a small integer or half-integer: 2, 2, −1.5, 2.5,")
print("          and u₀ ≈ 4. The centres are quantised; the scales are not.")
print()
print("      3 · β is the only constant with arity 3 — it appears in the amplitude,")
print("          the exponent and the validity. It is the load-bearing constant,")
print("          and it is the one that is ATTRIBUTED.")
