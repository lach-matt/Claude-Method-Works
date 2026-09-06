import numpy as np
from math import erf,sqrt
rng=np.random.default_rng(5)
Phi=lambda z: 0.5*(1+erf(z/sqrt(2)))

print("=== 1. closed form P = Phi(r)^2 + (1-Phi(r))^2 vs Monte Carlo ===")
def mc(r,N=2000000):
    lo=-r+rng.normal(0,1,N); hi=r+rng.normal(0,1,N)
    return np.mean((np.minimum(lo,hi)<=0)&(0<=np.maximum(lo,hi)))
for r in [0,0.5,1.0,1.3,2.0,3.0,4.0,5.0]:
    cf=Phi(r)**2+(1-Phi(r))**2
    print(f"  r={r:4.1f}  closed {100*cf:11.6f}%   MC {100*mc(r):11.6f}%   diff {100*abs(cf-mc(r)):.4f} pp")

print("\n=== 2. is min(r-,r+) a lower bound on the two-sided form? ===")
bad=0
for _ in range(200000):
    a,b=rng.uniform(0,6,2)
    two=Phi(a)*Phi(b)+(1-Phi(a))*(1-Phi(b)); m=min(a,b)
    one=Phi(m)**2+(1-Phi(m))**2
    if one>two+1e-12: bad+=1
print(f"  violations in 200k random (r-,r+): {bad}   [proof: f=1-u-v+2uv, df/dv=2u-1>=0 for u>=1/2]")

print("\n=== 3. Theorem 12.6 exhaustive check: 3x3 grid, 3 values ===")
import itertools
cells=[(i,j) for i in range(3) for j in range(3)]
def Hinv(f):
    for (x1,y1) in cells:
        for (x2,y2) in cells:
            A={f[(x1,y1)],f[(x2,y2)]}; B={f[(x1,y2)],f[(x2,y1)]}
            if sorted([f[(x1,y1)],f[(x2,y2)]])!=sorted([f[(x1,y2)],f[(x2,y1)]]): return False
    return True
n=0; nonconst=0
for vals in itertools.product(range(3),repeat=9):
    f=dict(zip(cells,vals))
    if Hinv(f):
        n+=1
        ci=all(f[(i,j)]==f[(0,j)] for i in range(3) for j in range(3))
        cj=all(f[(i,j)]==f[(i,0)] for i in range(3) for j in range(3))
        if not(ci or cj): nonconst+=1
print(f"  H-invariant functions: {n} (paper says 51);  of those not constant in a coordinate: {nonconst}")

print("\n=== 4. Theorem 12.3 witness ===")
a,b=np.array([1,5,2]),np.array([4,3,6]); a2,b2=np.array([1,3,2]),np.array([4,5,6])
f=lambda a,b: sum(a[i]*b[j]+a[j]*b[i] for i in range(3) for j in range(3) if i<j)
print(f"  meet/join (a,b)  = {np.minimum(a,b)} / {np.maximum(a,b)}")
print(f"  meet/join (a',b')= {np.minimum(a2,b2)} / {np.maximum(a2,b2)}   identical: "
      f"{np.array_equal(np.minimum(a,b),np.minimum(a2,b2)) and np.array_equal(np.maximum(a,b),np.maximum(a2,b2))}")
print(f"  f(a,b) = {f(a,b)}, f(a',b') = {f(a2,b2)}   (paper says 73 and 59)")
print(f"  dot product a.b = {a@b}, a'.b' = {a2@b2}   (paper says this does NOT witness)")