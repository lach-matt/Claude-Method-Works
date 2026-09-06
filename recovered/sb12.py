import numpy as np, eldata as ed
from collections import Counter
from itertools import combinations

L=[(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,2*(2*l+1)+1)]
occ=set(ed.E[z] for z in ed.E)
zs=sorted(ed.E)

print("="*72); print("AA.  SCHRODINGER DEGENERACY vs LATTICE COLUMN SIZE"); print("="*72)
print("  Hydrogenic: states at (n,l) number 2(2l+1) -- same as Lach capacity.")
print("  But hydrogenic DEGENERACY is over all l at fixed n: 2n^2 states.")
print("  Lach column = one (n,l) pair. Test whether column sizes reproduce")
print("  the l-degeneracy pattern 2,6,10,14,18 exactly:")
for l in range(5):
    print(f"    l={l}: Lach cap {2*(2*l+1):2d}   hydrogenic 2(2l+1) = {2*(2*l+1):2d}  match")
print("  -> identical by construction, not an independent finding.")

print()
print("="*72); print("AB.  IS THE OCCUPIED SET A 'GREEDOID' (relaxed matroid)?"); print("="*72)
cols=[(n,l) for n in range(1,8) for l in range(0,min(n,5))]
def cleq(a,b): return a[0]<=b[0] and a[1]<=b[1]
ds=[]
order=sorted(cols)
def enum(i,ch):
    if i==len(order): ds.append(frozenset(ch)); return
    c=order[i]; enum(i+1,ch)
    if all(d in ch for d in cols if cleq(d,c) and d!=c): enum(i+1,ch|{c})
enum(0,frozenset())
S=set(ds)
# greedoid: (1) accessible: every nonempty X has x with X-{x} in S; (2) exchange
acc_bad=[X for X in ds if X and not any((X-{x}) in S for x in X)]
exch_bad=sum(1 for A in ds for B in ds if len(A)<len(B) and not any((A|{x}) in S for x in B-A))
print(f"  accessibility violations: {len(acc_bad)}")
print(f"  exchange violations:      {exch_bad}")
print(f"  -> the down-set family IS a greedoid: {len(acc_bad)==0 and exch_bad==0}")
print("     (matroid failed only on hereditary; greedoid weakens that to")
print("      accessibility, which down-sets satisfy)")

print()
print("="*72); print("AC.  ANTIMATROID / CONVEX GEOMETRY?"); print("="*72)
# antimatroid: accessible + closed under union
uni_bad=sum(1 for A in ds for B in ds if (A|B) not in S)
print(f"  union-closure violations: {uni_bad}")
print(f"  -> the family is an ANTIMATROID: {len(acc_bad)==0 and uni_bad==0}")
int_bad=sum(1 for A in ds for B in ds if (A&B) not in S)
print(f"  intersection-closure violations: {int_bad}")
print("  Antimatroids model 'shelling' or ordered-construction processes.")
print("  Aufbau filling is exactly such a process, so this is the right")
print("  abstraction for the growth of the periodic system.")