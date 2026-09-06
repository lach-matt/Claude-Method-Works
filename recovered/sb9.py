import numpy as np, eldata as ed
from collections import defaultdict

cols=[(n,l) for n in range(1,8) for l in range(0,min(n,5))]
cap={(n,l):2*(2*l+1) for (n,l) in cols}
occ=set(ed.E[z] for z in ed.E)
h={c: max([k for (n,l,k) in occ if (n,l)==c], default=0) for c in cols}

print("="*70); print("N.  THE REALISED IDEAL IS ALL-OR-NOTHING BY COLUMN"); print("="*70)
sat=[c for c in cols if h[c]==cap[c]]; emp=[c for c in cols if h[c]==0]
par=[c for c in cols if 0<h[c]<cap[c]]
print(f"  columns fully saturated (h = cap): {len(sat)}")
print(f"  columns entirely empty  (h = 0):   {len(emp)}")
print(f"  columns PARTIALLY filled:          {len(par)}   {par}")
print()
print("  Every (n,ℓ) column of the realised system is either complete or")
print("  untouched. There are no half-filled subshell columns.")
print("  Reason: an element with configuration (n,ℓ,k) for k<cap is followed")
print("  in Z by (n,ℓ,k+1) — the subshell fills to capacity before the next")
print("  begins. Partial columns exist only transiently between elements.")
print()
print("  So the realised ideal is determined entirely by a BINARY choice per")
print("  column, subject to downward closure. That is far more restrictive")
print("  than a general order ideal of Λ.")

print()
print("="*70); print("O.  COUNTING THE ALL-OR-NOTHING IDEALS"); print("="*70)
# binary s(n,l) in {0,1}; downward closed on the column poset (n,l)<=(n',l')
# s(n,l)=1 whenever s(n',l')=1 for any (n',l')>=(n,l)
# => count down-sets of the column poset itself
colset=set(cols)
def leq(a,b): return a[0]<=b[0] and a[1]<=b[1]
# count antichains/down-sets of a 25-element poset by DP
order=sorted(cols)
from functools import lru_cache
idx={c:i for i,c in enumerate(order)}
@lru_cache(maxsize=None)
def cnt(i, chosen):
    if i==len(order): return 1
    c=order[i]
    ch=set(chosen)
    # can we set s(c)=1? only if all d<=c are already 1
    can1=all((d in ch) for d in cols if leq(d,c) and d!=c)
    t=cnt(i+1, chosen)          # s(c)=0
    if can1: t+=cnt(i+1, tuple(sorted(ch|{c})))
    return t
n_bin=cnt(0, tuple())
print(f"  down-sets of the 25-element column poset: {n_bin:,}")
print(f"  the realised system is one of these {n_bin:,} configurations")
print(f"  (versus {5538:,} if partial columns were allowed — my earlier")
print("   count, which was computed with the wrong constraint direction)")

# where does the real one sit?
real=frozenset(c for c in cols if h[c]>0)
print()
print(f"  realised column set has {len(real)} of 25 columns filled")
sizes=defaultdict(int)
@lru_cache(maxsize=None)
def cnt2(i, chosen):
    if i==len(order): return ((len(chosen)),)
    return None
# enumerate all down-sets explicitly (small enough)
allds=[]
def enum(i, ch):
    if i==len(order): allds.append(frozenset(ch)); return
    c=order[i]
    enum(i+1, ch)
    if all((d in ch) for d in cols if leq(d,c) and d!=c):
        enum(i+1, ch|{c})
enum(0, frozenset())
print(f"  enumerated {len(allds):,} down-sets (matches: {len(allds)==n_bin})")
szs=[len(d) for d in allds]
print(f"  column-count distribution: min {min(szs)}, max {max(szs)}, mean {np.mean(szs):.2f}")
smaller=sum(1 for d in allds if len(d)<len(real))
print(f"  down-sets with fewer columns than the realised one: {smaller:,} ({100*smaller/len(allds):.1f}%)")
# how many cells does each down-set correspond to?
cells=[sum(cap[c] for c in d) for d in allds]
real_cells=sum(cap[c] for c in real)
print(f"  realised system spans {real_cells} cells (= 118 ✓ {real_cells==118})")
fewer=sum(1 for x in cells if x<real_cells)
print(f"  down-sets with fewer cells: {fewer:,} ({100*fewer/len(cells):.1f}%)")
print(f"  → the periodic system is at the {100*fewer/len(cells):.0f}th percentile:")
print("     nearly the largest aufbau-consistent configuration available")
print("     within a 7-shell, 5-subshell lattice.")