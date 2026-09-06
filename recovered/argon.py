import math, statistics as st
from itertools import product
L="spdfg"; R=13.605693122994
def cap(l): return 2*(2*l+1)
# Ar ladder: charge c (the charge the departing electron sees), config of the
# species BEFORE ionisation as {(n,l):occ}, and the ionisation energy in eV
AR=[(1,{(1,0):2,(2,0):2,(2,1):6,(3,0):2,(3,1):6},15.7596,(3,1)),
    (2,{(1,0):2,(2,0):2,(2,1):6,(3,0):2,(3,1):5},27.6297,(3,1)),
    (3,{(1,0):2,(2,0):2,(2,1):6,(3,0):2,(3,1):4},40.74,(3,1)),
    (4,{(1,0):2,(2,0):2,(2,1):6,(3,0):2,(3,1):3},59.81,(3,1)),
    (5,{(1,0):2,(2,0):2,(2,1):6,(3,0):2,(3,1):2},75.02,(3,1)),
    (6,{(1,0):2,(2,0):2,(2,1):6,(3,0):2,(3,1):1},91.009,(3,1)),
    (7,{(1,0):2,(2,0):2,(2,1):6,(3,0):2},124.323,(3,0)),
    (8,{(1,0):2,(2,0):2,(2,1):6,(3,0):1},143.460,(3,0)),
    (9,{(1,0):2,(2,0):2,(2,1):6},422.45,(2,1)),
    (10,{(1,0):2,(2,0):2,(2,1):5},478.69,(2,1)),
    (11,{(1,0):2,(2,0):2,(2,1):4},538.96,(2,1)),
    (12,{(1,0):2,(2,0):2,(2,1):3},618.26,(2,1)),
    (13,{(1,0):2,(2,0):2,(2,1):2},686.10,(2,1)),
    (14,{(1,0):2,(2,0):2,(2,1):1},755.74,(2,1)),
    (15,{(1,0):2,(2,0):2},854.77,(2,0)),
    (16,{(1,0):2,(2,0):1},918.03,(2,0)),
    (17,{(1,0):2},4120.89,(1,0)),
    (18,{(1,0):1},4426.23,(1,0))]
print("  THE ARGON LADDER — eighteen charges, one species\n")
print("      ν = c√(R/IE);  a = (n − ν)/√(p + q/2(2ℓ+1))")
print("      p = n − ℓ − 1;  q = occupancy BEFORE the electron leaves, minus 1\n")
print(f"      {'c':>3}{'shell':>7}{'q':>3}{'p':>3}{'IE eV':>10}{'ν':>9}{'δ':>9}{'a':>9}")
D=[]
for c,cfg,ie,(gn,gl) in AR:
    q=cfg[(gn,gl)]-1
    p=gn-gl-1
    nu=c*math.sqrt(R/ie); d=gn-nu
    rad=p+q/cap(gl)
    a=d/math.sqrt(rad) if rad>0 else float("nan")
    print(f"      {c:>3}{f'{gn}{L[gl]}':>7}{q:>3}{p:>3}{ie:>10.3f}{nu:>9.4f}"
          f"{d:>9.4f}{a:>9.4f}")
    D.append((c,gn,gl,q,p,a,d))
print()
print("  a BY SUBSHELL — the protocol's list, per cell\n")
from collections import defaultdict
BY=defaultdict(list)
for c,gn,gl,q,p,a,d in D:
    if p<1 or a!=a: continue
    BY[(gn,gl)].append((c,q,a))
for k in sorted(BY):
    v=BY[k]
    print(f"      {k[0]}{L[k[1]]} : " + "  ".join(f"c={c} {a:.4f}" for c,q,a in v))
    aa=[x[2] for x in v]
    print(f"          {len(aa)} charges · median {st.median(aa):.4f}"
          f" · sd {st.pstdev(aa):.4f} · range {min(aa):.4f}–{max(aa):.4f}\n")
print("  AND a AGAINST CHARGE WITHIN 3p\n")
v=[(c,a) for c,q,a in BY[(3,1)]]
print(f"      {'c':>3}{'a':>10}{'Δa':>10}")
prev=None
for c,a in v:
    print(f"      {c:>3}{a:>10.4f}" + (f"{a-prev:>10.4f}" if prev else ""))
    prev=a