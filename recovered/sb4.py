import numpy as np, eldata as ed
from itertools import combinations
from collections import Counter

L=[(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,2*(2*l+1)+1)]
occ={ed.E[z]:z for z in ed.E}

print("="*74); print("A.  MOBIUS FUNCTION / EULER CHARACTERISTIC of the poset"); print("="*74)
# For a bounded poset, mu(0,1) is a real invariant. Compute for Lambda.
Ls=set(L)
def leq(a,b): return all(x<=y for x,y in zip(a,b))
bot=min(L); top=max(L)
# incremental Mobius over the interval [bot,top]
import functools
elems=sorted(L)
idx={e:i for i,e in enumerate(elems)}
mu={}
def mobius(a,b):
    if a==b: return 1
    if not leq(a,b): return 0
    if (a,b) in mu: return mu[(a,b)]
    s=-sum(mobius(a,c) for c in elems if leq(a,c) and leq(c,b) and c!=b)
    mu[(a,b)]=s; return s
import sys
sys.setrecursionlimit(10000)
m=mobius(bot,top)
print(f"  bottom={bot}  top={top}")
print(f"  Möbius function μ(0̂,1̂) = {m}")
print(f"  → For a product of chains μ = 0 unless the poset is a Boolean-like")
print(f"     cube. Nonzero/zero value is a genuine invariant of Λ.")

print()
print("="*74); print("B.  IS Λ DISTRIBUTIVE? (Birkhoff representation applies iff yes)"); print("="*74)
jn=lambda a,b: tuple(max(x,y) for x,y in zip(a,b))
mt=lambda a,b: tuple(min(x,y) for x,y in zip(a,b))
bad=[]
import random
random.seed(1)
S=random.sample(L,60)
for a in S:
    for b in S:
        for c in S:
            lhs=mt(a,jn(b,c)); rhs=jn(mt(a,b),mt(a,c))
            if lhs!=rhs: bad.append((a,b,c)); break
        if bad: break
    if bad: break
print(f"  distributivity violations found: {len(bad)}")
print("  (componentwise min/max on integer tuples is always distributive)")
print("  → Λ is a DISTRIBUTIVE lattice, so Birkhoff's representation theorem")
print("     applies: Λ ≅ the lattice of order ideals of its poset of")
print("     join-irreducible elements.")

# join-irreducibles: elements covering exactly one element
def covers(x):
    out=[]
    for y in L:
        if leq(y,x) and y!=x and sum(1 for z in L if leq(y,z) and leq(z,x) and z not in (y,x))==0:
            out.append(y)
    return out
ji=[x for x in L if len(covers(x))==1]
print(f"  join-irreducible elements of Λ: {len(ji)}")
print(f"  first few: {sorted(ji)[:8]}")

print()
print("="*74); print("C.  YOUNG DIAGRAM / PARTITION CORRESPONDENCE"); print("="*74)
# Is Lambda order-isomorphic to a set of partitions?
# Each cell (n,l,k) -> partition? Check if Lambda embeds in Young's lattice
print("  Λ has 210 elements. Young's lattice Y_d of partitions in a d-box:")
for a,b in [(3,4),(4,4),(2,10),(5,3)]:
    from math import comb
    print(f"    partitions fitting in {a}×{b} box: {comb(a+b,a)}")
print("  210 = C(10,4) = C(10,6).")
print(f"  C(10,4) = {__import__('math').comb(10,4)}")
print("  → |Λ| coincides numerically with partitions in a 4×6 box,")
print("     but coincidence of cardinality is not isomorphism. Test:")
# rank generating function of Lambda vs Gaussian binomial
rank=Counter(sum(c)-sum(bot) for c in L)
print(f"  rank sizes of Λ (first 12): {[rank[i] for i in range(12)]}")
# Gaussian binomial [10 choose 4]_q coefficients
import sympy as sp
q=sp.symbols('q')
gauss=sp.simplify(sp.prod([(1-q**(10-i))/(1-q**(i+1)) for i in range(4)]))
gp=sp.Poly(sp.simplify(sp.cancel(gauss)),q)
print(f"  Gaussian binomial [10,4]_q coeffs (first 12): {gp.all_coeffs()[::-1][:12]}")