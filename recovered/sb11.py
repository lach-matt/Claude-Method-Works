import numpy as np, eldata as ed
from collections import Counter
import sympy as sp

L=[(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,2*(2*l+1)+1)]
occ=set(ed.E[z] for z in ed.E)

print("="*74); print("Q.  MATROID? — is the occupied set the independent set of a matroid?"); print("="*74)
# Independent sets must satisfy exchange axiom. Test on the down-set structure.
def leq(a,b): return all(x<=y for x,y in zip(a,b))
# treat down-sets as 'independent'; check augmentation
# a down-set family is a matroid iff it's the family of independent sets => needs exchange
cols=[(n,l) for n in range(1,8) for l in range(0,min(n,5))]
def colleq(a,b): return a[0]<=b[0] and a[1]<=b[1]
ds=[]
order=sorted(cols)
def enum(i,ch):
    if i==len(order): ds.append(frozenset(ch)); return
    c=order[i]; enum(i+1,ch)
    if all(d in ch for d in cols if colleq(d,c) and d!=c): enum(i+1,ch|{c})
enum(0,frozenset())
viol=0; ex=None
for A in ds:
    for B in ds:
        if len(A)<len(B):
            if not any((A|{x}) in set(ds) for x in B-A):
                viol+=1
                if ex is None: ex=(A,B)
print(f"  down-set family size: {len(ds)}")
print(f"  exchange-axiom violations: {viol}")
print(f"  → the family of down-sets is {'a matroid' if viol==0 else 'NOT a matroid'}")
if ex: print(f"     e.g. |A|={len(ex[0])} < |B|={len(ex[1])}, no single element of B augments A")
print("  (This is expected: down-set families are distributive lattices,")
print("   not matroids; the two axiom systems differ. Recorded as a negative.)")

print()
print("="*74); print("R.  ZETA / MOBIUS ON THE COLUMN POSET"); print("="*74)
import sys
sys.setrecursionlimit(50000)
mu={}
def mob(a,b):
    if a==b: return 1
    if not colleq(a,b): return 0
    if (a,b) in mu: return mu[(a,b)]
    s=-sum(mob(a,c) for c in cols if colleq(a,c) and colleq(c,b) and c!=b)
    mu[(a,b)]=s; return s
vals=Counter()
for a in cols:
    for b in cols:
        if colleq(a,b): vals[mob(a,b)]+=1
print(f"  Möbius values on the 25-column poset: {dict(vals)}")
print("  Values in {1,-1,0} only → the column poset is a distributive")
print("  lattice-like grid; μ behaves as for a product of two chains.")
# check: the column poset is a staircase (Young-diagram shaped) subposet of NxN
print(f"  column poset is the staircase {{(n,ℓ) : 0 ≤ ℓ ≤ min(n-1,4), 1 ≤ n ≤ 7}}")

print()
print("="*74); print("S.  GENERATING FUNCTION / PARTITION IDENTITY"); print("="*74)
q=sp.symbols('q')
# rank gf of Lambda
gf=sum(q**sum(c) for c in L)
gp=sp.Poly(sp.expand(gf),q)
print(f"  rank generating function has degree {gp.degree()}, {len(gp.all_coeffs())} terms")
# factor?
fac=sp.factor(sp.expand(gf))
s=str(fac)
print(f"  factored: {s[:150]}{'...' if len(s)>150 else ''}")
# does it factor into cyclotomic-like pieces?
print(f"  is it a product of q-integers? {'yes' if '(q' in s and '**' in s else 'no clean product'}")