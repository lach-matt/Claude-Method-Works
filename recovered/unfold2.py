import numpy as np
from itertools import combinations
from collections import Counter

def test(name, cells, note=""):
    S=set(cells)
    def jn(a,b): return tuple(max(x,y) for x,y in zip(a,b))
    def mt(a,b): return tuple(min(x,y) for x,y in zip(a,b))
    bj=sum(1 for a,b in combinations(cells,2) if jn(a,b) not in S)
    bm=sum(1 for a,b in combinations(cells,2) if mt(a,b) not in S)
    ok = (bj==0 and bm==0)
    print(f"  {name:<42} |Λ|={len(cells):4d}  join fail={bj:5d}  meet fail={bm:5d}  {'LATTICE' if ok else 'not a lattice'}")
    if note: print(f"      {note}")
    return ok

print("="*74)
print("VARIANTS OF THE UNFOLDING")
print("="*74)

# original 3-axis
L3=[(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,2*(2*l+1)+1)]
test("(n, ℓ, k)  — original", L3)

# 4-axis with signed m
L4=[(n,l,m,s) for n in range(1,8) for l in range(0,min(n,5))
    for m in range(-l,l+1) for s in (-1,1)]
test("(n, ℓ, m, s)  — signed m", L4)

# 4-axis with shifted m (m' = m + l, so 0 <= m' <= 2l)
L4b=[(n,l,m+l,s) for n in range(1,8) for l in range(0,min(n,5))
     for m in range(-l,l+1) for s in (0,1)]
test("(n, ℓ, m+ℓ, s)  — shifted to one-sided", L4b,
     "one-sided bound m' <= 2ℓ mirrors k's structure")

# 4-axis: (n, l, j, s) where j = occupancy within m-subshell
L4c=[(n,l,mi,s) for n in range(1,8) for l in range(0,min(n,5))
     for mi in range(1,2*l+2) for s in (0,1)]
test("(n, ℓ, m-index 1..2ℓ+1, s)", L4c)

print()
print("="*74)
print("WHY THE ONE-SIDED FORM WORKS AND THE SIGNED FORM DOES NOT")
print("="*74)
print("""  A componentwise poset on integer tuples is closed under join and meet
  iff every constraint is of the form  x_i <= f(x_j)  with f monotone
  non-decreasing, and every lower bound is a constant.

    ℓ <= n-1          upper bound, monotone in n            OK
    k <= 2(2ℓ+1)      upper bound, monotone in ℓ            OK
    k >= 1            constant lower bound                  OK
    |m| <= ℓ    ==    m <= ℓ  AND  m >= -ℓ
                      the second is a lower bound that
                      DEPENDS on ℓ  ->  breaks meet closure  FAIL

  Substituting m' = m + ℓ converts the pair into
    m' <= 2ℓ  and  m' >= 0,
  restoring a constant lower bound. Closure is recovered.""")

print()
print("="*74)
print("BUT: does the shifted form buy anything?")
print("="*74)
c=Counter(n for n,l,m,s in L4b)
print("  cells per shell:", {k:c[k] for k in sorted(c)})
print("  2n² holds:", all(c[n]==2*n*n for n in range(1,8) if n<=4))
print("""
  The shifted coordinate m' = m + ℓ is not the magnetic quantum number.
  It is m displaced by a value that itself varies across the lattice.
  So the 'unfolded' axis is no longer the hydrogenic label whose
  representation theory motivated the unfolding in the first place.
  We recover closure by giving up the thing we unfolded FOR.""")