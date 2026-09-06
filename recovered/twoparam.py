import itertools, math
from fractions import Fraction as F
LN="spdfghik"
ORDER=[(1,0,F(1,2)),(1,1,F(3,2)),(1,1,F(1,2)),(1,2,F(5,2)),(2,0,F(1,2)),
       (1,2,F(3,2)),(1,3,F(7,2)),(2,1,F(3,2)),(1,3,F(5,2)),(2,1,F(1,2)),
       (1,4,F(9,2)),(2,2,F(5,2)),(3,0,F(1,2)),(2,2,F(3,2)),(1,4,F(7,2)),
       (1,5,F(11,2)),(2,3,F(7,2)),(3,1,F(3,2)),(1,5,F(9,2)),(3,1,F(1,2)),
       (2,3,F(5,2)),(1,6,F(13,2))]
def N(nr,l): return 2*(nr-1)+l
def LS(l,j): return F(1,2)*(j*(j+1)-l*(l+1)-F(3,4))
print("  THE TWO-TERM FAMILY  E = (N+3/2) + β·ℓ(ℓ+1) − α·⟨L·S⟩\n")
print("      each consecutive pair gives  β·Δ[ℓ(ℓ+1)] − α·Δ⟨L·S⟩ < −ΔN")
print("      the feasible set is a polygon in (β, α).  scanning it:\n")
CON=[]
for i in range(len(ORDER)-1):
    n1,l1,j1=ORDER[i]; n2,l2,j2=ORDER[i+1]
    a=float(l2*(l2+1)-l1*(l1+1))        # coeff of beta
    b=-float(LS(l2,j2)-LS(l1,j1))       # coeff of alpha
    c=-float(N(n2,l2)-N(n1,l1))         # RHS
    CON.append((a,b,c,f"{n1}{LN[l1]}{j1}→{n2}{LN[l2]}{j2}"))
best=None; hits=0
for bi in range(-400,401):
    for ai in range(0,401):
        be=bi/2000.0; al=ai/200.0
        if all(a*be+b*al < c-1e-12 for a,b,c,_ in CON):
            hits+=1
            if best is None: best=(be,al)
print(f"      grid 801×401 · FEASIBLE points: {hits}")
if hits:
    print(f"      → the two-term family CAN produce the observed order.")
    print(f"      an example: β = {best[0]:.4f}, α = {best[1]:.4f}\n")
    bs=[];als=[]
    for bi in range(-400,401):
        for ai in range(0,401):
            be=bi/2000.0; al=ai/200.0
            if all(a*be+b*al < c-1e-12 for a,b,c,_ in CON):
                bs.append(be); als.append(al)
    print(f"      β range {min(bs):+.4f} to {max(bs):+.4f}")
    print(f"      α range {min(als):+.4f} to {max(als):+.4f}")
    print(f"      α/β at the corners: "
          f"{max(als)/max(bs) if max(bs)!=0 else float('nan'):.2f}")
else:
    print("      → EMPTY. even two terms cannot produce it.")
print()
print("  AND WHICH PAIRS FORCE β ≠ 0\n")
viol=[]
for a,b,c,nm in CON:
    # can this pair be satisfied with beta = 0 and some alpha > 0?
    if abs(b)<1e-12:
        if not (0 < c): viol.append((nm,"needs β"))
    else:
        lim=c/b
        if b>0 and lim<=0: viol.append((nm,f"α < {lim:.3f} — needs β"))
for nm,w in viol: print(f"      {nm:<18}{w}")
if not viol: print("      none — β = 0 suffices for every pair individually")