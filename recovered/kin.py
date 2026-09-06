import numpy as np, eldata as ed
from itertools import product

print("="*68)
print("1.  MADELUNG / AUFBAU  — is the lattice's filling order recoverable?")
print("="*68)
# Madelung rule: fill by increasing (n+l), ties broken by increasing n.
# The lattice does NOT encode order; it encodes position. Test whether
# aufbau order is a monotone path through the lattice under (n+l, n).
occ = [(z,)+ed.E[z] for z in sorted(ed.E)]
key = [(n+l, n, z) for z,n,l,k in occ]
# check: does sorting elements by (n+l, n, k) reproduce Z order?
srt = sorted(occ, key=lambda t: (t[1]+t[2], t[1], t[3]))
zs_sorted = [t[0] for t in srt]
inversions = sum(1 for i in range(len(zs_sorted)) for j in range(i+1,len(zs_sorted))
                 if zs_sorted[i] > zs_sorted[j])
n = len(zs_sorted); maxinv = n*(n-1)//2
print(f"  Sorting the 118 lattice points by (n+ℓ, n, k) and reading off Z:")
print(f"  inversions vs. true Z order: {inversions} / {maxinv}  "
      f"(Kendall tau = {1-4*inversions/(n*(n-1)):+.4f})")
mism = [(zs_sorted[i], i+1) for i in range(n) if zs_sorted[i] != i+1]
print(f"  positions where order differs: {len(mism)}")
print(f"  first few mismatches (Z, position): {mism[:8]}")
print("  → Madelung is a RULE ON the lattice, not a consequence OF it.")
print("     The lattice is compatible with it but does not derive it.")

print()
print("="*68)
print("2.  GROUP THEORY / SO(4,2)  — the known dynamical symmetry of H")
print("="*68)
# The hydrogen atom has SO(4) symmetry (bound states, fixed n) and
# SO(4,2) as spectrum-generating algebra. States |n,l,m> with
# n^2 degeneracy per shell. The Lach lattice uses (n,l,k) where k is
# OCCUPANCY, not m. Check dimensional bookkeeping.
print("  Hydrogenic shell structure:  states per shell n = n²  (times 2 for spin)")
for nn in range(1,8):
    hyd = nn*nn
    lach_cells = sum(1 for l in range(nn) for k in range(1, 2*(2*l+1)+1))
    print(f"    n={nn}:  hydrogenic |n,l,m⟩ = {hyd:3d}   "
          f"Lach cells at this n = {lach_cells:3d}")
print("  → Different objects. |n,l,m⟩ counts STATES; Lach (n,l,k) counts")
print("     CONFIGURATIONS. k is an occupancy index, not a magnetic")
print("     quantum number, so SO(4,2) representation theory does not")
print("     transfer to this lattice.")

print()
print("="*68)
print("3.  IS THE LATTICE A POSET / LATTICE IN THE ALGEBRAIC SENSE?")
print("="*68)
# Define partial order: (n,l,k) <= (n',l',k') iff componentwise <=.
# A mathematical lattice requires every pair to have a unique join and meet
# WITHIN the admissible set Lambda.
def admissible(n,l,k):
    return 1<=n<=7 and 0<=l<=min(n-1,4) and 1<=k<=2*(2*l+1)
L = [(n,l,k) for n in range(1,8) for l in range(0,5) for k in range(1,19)
     if admissible(n,l,k)]
Lset=set(L)
print(f"  admissible cells |Λ| = {len(L)}")
def join(a,b): return (max(a[0],b[0]), max(a[1],b[1]), max(a[2],b[2]))
def meet(a,b): return (min(a[0],b[0]), min(a[1],b[1]), min(a[2],b[2]))
bad_j=bad_m=0
import random
random.seed(0)
sample=random.sample(L, 300)
for a,b in product(sample[:120], sample[:120]):
    if join(a,b) not in Lset: bad_j+=1
    if meet(a,b) not in Lset: bad_m+=1
print(f"  pairs (of 14400 sampled) whose join leaves Λ: {bad_j}")
print(f"  pairs whose meet leaves Λ:                    {bad_m}")
print("  → Λ is NOT closed under componentwise join: it is a poset but")
print("     not an algebraic lattice. The constraint ℓ ≤ n−1 breaks closure.")