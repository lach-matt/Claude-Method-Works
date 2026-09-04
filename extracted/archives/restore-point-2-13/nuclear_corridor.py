from fractions import Fraction as F
LN="spdfghik"
# CORRECTED standard order, capacities verified to close at 2,8,20,28,50,82,126
ORD=[(1,0,F(1,2)),(1,1,F(3,2)),(1,1,F(1,2)),
     (1,2,F(5,2)),(2,0,F(1,2)),(1,2,F(3,2)),
     (1,3,F(7,2)),
     (2,1,F(3,2)),(1,3,F(5,2)),(2,1,F(1,2)),(1,4,F(9,2)),
     (1,4,F(7,2)),(2,2,F(5,2)),(2,2,F(3,2)),(3,0,F(1,2)),(1,5,F(11,2)),
     (1,5,F(9,2)),(2,3,F(7,2)),(1,6,F(13,2)),(3,1,F(3,2)),(2,3,F(5,2)),(3,1,F(1,2))]
def N(nr,l): return 2*(nr-1)+l
def LS(l,j): return F(1,2)*(j*(j+1)-l*(l+1)-F(3,4))
def nm(nr,l,j): return f"{nr}{LN[l]}{2*j.numerator//j.denominator if False else int(2*j)}/2"
print("  THE CORRECTED ORDER — capacities check\n")
c=0; MAG=[]
for nr,l,j in ORD:
    d=int(2*j+1); c+=d
    if c in (2,8,20,28,50,82,126): MAG.append(c)
    print(f"      {nm(nr,l,j):>9}  N={N(nr,l):<2} d={d:<3} cum={c:<4}"
          f"{'  ← MAGIC' if c in (2,8,20,28,50,82,126) else ''}")
print(f"\n      closures reached: {MAG}   {'ALL SEVEN' if len(MAG)==7 else 'INCOMPLETE'}\n")
CON=[]
for i in range(len(ORD)-1):
    n1,l1,j1=ORD[i]; n2,l2,j2=ORD[i+1]
    a=float(l1*(l1+1)-l2*(l2+1)); b=float(LS(l2,j2)-LS(l1,j1)); cc=float(N(n2,l2)-N(n1,l1))
    CON.append((a,b,cc,f"{nm(n1,l1,j1)}→{nm(n2,l2,j2)}"))
print("  THE CORRIDOR  —  β(ℓ₁(ℓ₁+1) − ℓ₂(ℓ₂+1)) + α(S₂ − S₁) < N₂ − N₁\n")
def scan(bmin,bmax):
    P=[]
    for bi in range(bmin,bmax+1):
        for ai in range(1,601):
            be=bi/2000.0; al=ai/200.0
            if all(a*be+b*al < cc-1e-9 for a,b,cc,_ in CON): P.append((be,al))
    return P
p0=[p for p in scan(0,0)]
p1=scan(-600,600)
print(f"      ONE term  (β = 0, L·S only)  : {len(p0)} feasible α")
print(f"      TWO terms (β free, L·S)      : {len(p1)} feasible (β, α)\n")
if p0:
    al=[x[1] for x in p0]
    print(f"      → L·S ALONE reproduces the observed order, α ∈ "
          f"[{min(al):.3f}, {max(al):.3f}]")
    print(f"        Laubscher's s = 1/12 = 0.0833 inside: "
          f"{'YES' if min(al)<=1/12<=max(al) else 'NO'}")
elif p1:
    bs=[x[0] for x in p1]; als=[x[1] for x in p1]
    print(f"      → needs BOTH terms. β ∈ [{min(bs):+.4f}, {max(bs):+.4f}], "
          f"α ∈ [{min(als):.3f}, {max(als):.3f}]")
    print(f"        β = 0 is {'inside' if 0.0 in bs else 'EXCLUDED'} "
          f"→ the ℓ² term is {'optional' if 0.0 in bs else 'REQUIRED'}")
else:
    print("      → EMPTY for both. the binding pairs:")
    for a,b,cc,n_ in CON:
        print(f"        {n_:<20}{a:>6.0f}β +{b:>7.2f}α < {cc:>4.0f}")
