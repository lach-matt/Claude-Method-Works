from fractions import Fraction as F
LN="spdfghik"
ORDER=[(1,0,F(1,2)),(1,1,F(3,2)),(1,1,F(1,2)),(1,2,F(5,2)),(2,0,F(1,2)),
       (1,2,F(3,2)),(1,3,F(7,2)),(2,1,F(3,2)),(1,3,F(5,2)),(2,1,F(1,2)),
       (1,4,F(9,2)),(2,2,F(5,2)),(3,0,F(1,2)),(2,2,F(3,2)),(1,4,F(7,2)),
       (1,5,F(11,2)),(2,3,F(7,2)),(3,1,F(3,2)),(1,5,F(9,2)),(3,1,F(1,2)),
       (2,3,F(5,2)),(1,6,F(13,2))]
def N(nr,l): return 2*(nr-1)+l
def LS(l,j): return F(1,2)*(j*(j+1)-l*(l+1)-F(3,4))
# E = N + 3/2 + beta*l(l+1) - alpha*LS ;  E1 < E2  =>
#   beta(L1-L2) + alpha(S2-S1) < N2-N1
CON=[]
for i in range(len(ORDER)-1):
    n1,l1,j1=ORDER[i]; n2,l2,j2=ORDER[i+1]
    a=float(l1*(l1+1)-l2*(l2+1)); b=float(LS(l2,j2)-LS(l1,j1))
    c=float(N(n2,l2)-N(n1,l1))
    CON.append((a,b,c,f"{n1}{LN[l1]}{'%d/2'%(2*j1)}→{n2}{LN[l2]}{'%d/2'%(2*j2)}"))
print("  E = (N + 3/2) + β·ℓ(ℓ+1) − α·⟨L·S⟩   —  the standard two-term family\n")
def feas(use_beta):
    pts=[]
    for bi in range(0,301):
        for ai in range(0,301):
            be=(-bi/1000.0) if use_beta else 0.0
            al=ai/100.0
            if all(a*be+b*al < c-1e-9 for a,b,c,_ in CON): pts.append((be,al))
    return pts
p0=feas(False); p1=feas(True)
print(f"      ONE term  (β = 0, only L·S) : {len(p0)} feasible α")
print(f"      TWO terms (β ≤ 0 and L·S)  : {len(p1)} feasible (β, α)\n")
if p0:
    al=[x[1] for x in p0]
    print(f"      α alone works for α ∈ [{min(al):.3f}, {max(al):.3f}]")
    print(f"      → the L·S term ALONE reproduces the observed order.")
    print(f"        1/12 = 0.0833 inside: {'YES' if min(al)<=1/12<=max(al) else 'no'}")
if p1:
    bs=[x[0] for x in p1]; als=[x[1] for x in p1]
    print(f"      with β : β ∈ [{min(bs):.4f}, {max(bs):.4f}], "
          f"α ∈ [{min(als):.3f}, {max(als):.3f}]")
print()
if not p0 and not p1:
    print("  THE BINDING CONSTRAINTS\n")
    for a,b,c,nm in CON:
        print(f"      {nm:<20}{a:>6.0f}·β +{b:>6.2f}·α < {c:>4.0f}")