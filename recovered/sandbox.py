import numpy as np
from itertools import combinations, product
from collections import Counter

def is_lattice(cells, name, verbose=True):
    S=set(cells)
    def jn(a,b): return tuple(max(x,y) for x,y in zip(a,b))
    def mt(a,b): return tuple(min(x,y) for x,y in zip(a,b))
    bj=sum(1 for a,b in combinations(cells,2) if jn(a,b) not in S)
    bm=sum(1 for a,b in combinations(cells,2) if mt(a,b) not in S)
    ok=(bj==0 and bm==0)
    if verbose:
        print(f"  {name:<46} |S|={len(cells):5d}  join✗={bj:5d} meet✗={bm:5d}  {'LATTICE' if ok else 'no'}")
    return ok

print("="*78)
print("SANDBOX 1 — Does the criterion predict correctly on OTHER structures?")
print("="*78)
print("Criterion: closed iff every upper bound monotone-nondecreasing in others,")
print("           and every lower bound constant.\n")

tests=[]

# A. Young diagrams / partitions: lambda_1 >= lambda_2 >= ... (order ideals)
# constraint: x_{i+1} <= x_i  -> upper bound monotone in x_i, lower bound 0 const. PREDICT LATTICE
P=[(a,b,c) for a in range(6) for b in range(6) for c in range(6) if a>=b>=c]
tests.append(("Young diagrams  x1≥x2≥x3 (≤5)", P, True))

# B. Staircase with VARYING lower bound: x2 >= x1  (lower bound depends on x1)
Q=[(a,b) for a in range(6) for b in range(6) if b>=a]
# note: b>=a is a lower bound on b varying with a -> predict FAIL on meet
tests.append(("varying lower bound  x2 ≥ x1", Q, False))

# C. Divisor lattice of 60 as tuples of exponents (2^a 3^b 5^c), a<=2,b<=1,c<=1
D=[(a,b,c) for a in range(3) for b in range(2) for c in range(2)]
tests.append(("divisor lattice of 60 (box)", D, True))

# D. Simplex: x+y+z <= N  -> upper bound on a SUM, not a single coord
Simp=[(x,y,z) for x in range(5) for y in range(5) for z in range(5) if x+y+z<=6]
tests.append(("simplex  x+y+z ≤ 6", Simp, True))

# E. Sphere-ish: x^2+y^2 <= 9  (nonlinear, still downward closed)
Sph=[(x,y) for x in range(5) for y in range(5) if x*x+y*y<=9]
tests.append(("disc  x²+y² ≤ 9  (downward closed)", Sph, True))

# F. Annulus: 4 <= x^2+y^2 <= 16 -> has a varying-ish lower constraint
Ann=[(x,y) for x in range(6) for y in range(6) if 4<=x*x+y*y<=16]
tests.append(("annulus 4 ≤ x²+y² ≤ 16", Ann, False))

# G. Lambda itself
Lam=[(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,2*(2*l+1)+1)]
tests.append(("Λ  (n,ℓ,k)", Lam, True))

# H. hydrogenic
Hyd=[(n,l,m,s) for n in range(1,8) for l in range(0,min(n,5)) for m in range(-l,l+1) for s in (-1,1)]
tests.append(("Λ′ (n,ℓ,m,s)  signed m", Hyd, False))

print("  structure                                        result vs prediction")
print("  " + "-"*74)
ok_count=0
for name,cells,pred in tests:
    got=is_lattice(cells,name,verbose=False)
    mark = "✓ predicted" if got==pred else "✗ MISPREDICTED"
    if got==pred: ok_count+=1
    print(f"  {name:<44} {'LATTICE' if got else 'not    '}   {mark}")
print(f"\n  criterion correct on {ok_count}/{len(tests)} test structures")