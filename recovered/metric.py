import numpy as np, eldata as ed
from itertools import combinations

print("="*74)
print("WOULD A METRIC FOURTH AXIS PRESERVE THE ORDER STRUCTURE?")
print("="*74)
print("""  Proposal: Λ⁴ = {(n, ℓ, k, E)} where E is a discretised energy-like
  quantity. Test whether componentwise order remains closed.""")

# Use a real metric quantity: Slater-like orbital energy proxy, discretised.
# E depends on (n,l,k) -- that's the point of adding it.
def Eproxy(n,l,k):
    # crude hydrogenic + screening: deeper for large Zeff/n^2
    return -1.0/(n**2) * (1 + 0.3*l) * (1 + 0.05*k)

L3=[(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,2*(2*l+1)+1)]
# discretise E into integer levels so componentwise order is well-defined
vals=sorted(set(round(Eproxy(*c),3) for c in L3))
lut={v:i for i,v in enumerate(vals)}
L4=[(n,l,k,lut[round(Eproxy(n,l,k),3)]) for (n,l,k) in L3]
S4=set(L4)
def jn(a,b): return tuple(max(x,y) for x,y in zip(a,b))
def mt(a,b): return tuple(min(x,y) for x,y in zip(a,b))
bj=sum(1 for a,b in combinations(L4,2) if jn(a,b) not in S4)
bm=sum(1 for a,b in combinations(L4,2) if mt(a,b) not in S4)
print(f"\n  |Λ⁴| = {len(L4)}")
print(f"  join failures: {bj:,}")
print(f"  meet failures: {bm:,}")
print(f"  closed: {bj==0 and bm==0}")
print()
print("""  Why it fails: E is a FUNCTION of (n,ℓ,k), so the fourth coordinate is
  determined by the first three. The set is a graph of a function, not a
  product region. Taking a join raises n,ℓ,k independently but E must then
  take the value the function dictates — which is generally not the
  componentwise max. The tuple lands off the graph.""")

# how badly?
ex=[(a,b,jn(a,b)) for a,b in combinations(L4[:60],2) if jn(a,b) not in S4][:3]
for a,b,j in ex:
    print(f"    {a} ∨ {b} = {j}")
    correct = (j[0],j[1],j[2], lut[round(Eproxy(j[0],j[1],j[2]),3)])
    print(f"      but the graph requires E = {correct[3]}, not {j[3]}")

print()
print("="*74)
print("THE GENERAL OBSTRUCTION")
print("="*74)
print("""  Any metric axis worth adding is a function of the existing coordinates
  — that is what makes it informative about (n,ℓ,k). But a coordinate
  determined by the others cannot be an independent axis of a product
  order. Adding it turns Λ from a product region into a functional graph,
  and functional graphs are not sublattices of the ambient product.

  So the choice is stark:
    - a metric axis INDEPENDENT of (n,ℓ,k) carries no information about
      the lattice, and the fourth coordinate is decorative;
    - a metric axis DEPENDENT on (n,ℓ,k) destroys the closure that every
      result in Part II relies on.

  This is not the same obstruction as §19 (dimensionlessness). It is an
  order-theoretic one, and it is arguably sharper: even granting a metric
  quantity for free, it cannot be added as a coordinate without loss.""")