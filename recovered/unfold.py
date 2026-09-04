import numpy as np
from itertools import combinations
from collections import Counter

print("="*70)
print("UNFOLDING k -> (m, s):  does the 4-axis lattice have better structure?")
print("="*70)

# Lambda' : (n, l, m, s) with -l <= m <= l, s in {-1,+1}
Lp=[(n,l,m,s) for n in range(1,8) for l in range(0,min(n,5))
     for m in range(-l,l+1) for s in (-1,1)]
print(f"  |Λ′| = {len(Lp)}   (was |Λ| = 210)")
c=Counter(n for n,l,m,s in Lp)
print("  cells per shell:", {k:c[k] for k in sorted(c)})
print("  2n² check:", all(c[n]==2*n*n for n in range(1,8)))

print()
print("-- Is Λ′ still a bounded lattice under componentwise order? --")
Ls=set(Lp)
def jn(a,b): return tuple(max(x,y) for x,y in zip(a,b))
def mt(a,b): return tuple(min(x,y) for x,y in zip(a,b))
bj=[(a,b) for a,b in combinations(Lp,2) if jn(a,b) not in Ls]
bm=[(a,b) for a,b in combinations(Lp,2) if mt(a,b) not in Ls]
print(f"  join failures: {len(bj)}    meet failures: {len(bm)}")
if bj[:3]:
    for a,b in bj[:3]:
        print(f"    {a} v {b} = {jn(a,b)}  NOT admissible")
print()
if bj or bm:
    print("  → Λ′ is NOT closed. The constraint |m| <= l couples m to l in")
    print("     BOTH directions (upper and lower), unlike k which had only")
    print("     an upper bound. Raising l is fine, but raising m without")
    print("     raising l breaks admissibility, and lowering l below |m| too.")
    print("  → The 4-axis unfolding DESTROYS the algebraic lattice property")
    print("     that was Section 10.1's main result.")
else:
    print("  → Λ′ remains a bounded lattice.")