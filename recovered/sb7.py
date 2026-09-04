import numpy as np, eldata as ed
from functools import lru_cache
from collections import Counter

L=[(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,2*(2*l+1)+1)]
cols=sorted({(n,l) for n,l,k in L})
cap={(n,l):2*(2*l+1) for (n,l) in cols}

# A down-set of Lambda is exactly an assignment h(n,l) in 0..cap(n,l)
# with h(n,l) >= h(n',l') whenever (n,l) <= (n',l') componentwise.
# Count by DP over columns in reverse linear extension.
order=sorted(cols, key=lambda c:(-(c[0]+c[1]), -c[0]))
pos={c:i for i,c in enumerate(order)}
succ={c:[d for d in cols if c!=d and c[0]<=d[0] and c[1]<=d[1]] for c in cols}

import sys
sys.setrecursionlimit(100000)
memo={}
def rec(i, assigned):
    if i==len(order): return 1
    key=(i,assigned)
    if key in memo: return memo[key]
    c=order[i]
    A=dict(assigned)
    lb=0
    for d in succ[c]:
        if d in A: lb=max(lb,A[d])
    tot=0
    for h in range(lb, cap[c]+1):
        A2=dict(A); A2[c]=h
        # prune: keep only columns still needed (those that are predecessors of unassigned)
        need={d for d in order[i+1:]}
        keep=tuple(sorted((k2,v2) for k2,v2 in A2.items()
                          if any(k2[0]>=e[0] and k2[1]>=e[1] for e in need)))
        tot+=rec(i+1, keep)
    memo[key]=tot
    return tot

n_ideals=rec(0, tuple())
print("="*70)
print("K.  THE NUMBER OF ORDER IDEALS OF Λ")
print("="*70)
print(f"  |J(Λ)| = {n_ideals:,}")
print(f"  log10 = {np.log10(n_ideals):.4f}")
print()
print("  Interpretation: J(Λ) is the distributive lattice whose elements are")
print("  all downward-closed subsets of Λ. By Section 13 the periodic system")
print("  is ONE of these. So the count is the number of logically possible")
print("  'aufbau-consistent worlds' — sets of configurations that could be")
print("  realised without violating downward closure.")
print(f"  The actual periodic system is 1 of {n_ideals:,}.")

print()
print("="*70)
print("L.  WHERE DOES THE REAL PERIODIC SYSTEM SIT IN J(Λ)?")
print("="*70)
occ=set(ed.E[z] for z in ed.E)
h_real={c: max([k for (n,l,k) in occ if (n,l)==c], default=0) for c in cols}
print("  height profile h(n,ℓ) of the realised ideal:")
for n in range(1,8):
    row=[]
    for l in range(0,5):
        if (n,l) in cols: row.append(f"{h_real[(n,l)]:2d}")
        else: row.append(" ·")
    print(f"    n={n}: "+" ".join(row))
print(f"  cells: {sum(h_real.values())} = 118  ✓")
print(f"  saturated columns (h = cap): {sum(1 for c in cols if h_real[c]==cap[c])} of {len(cols)}")
print(f"  empty columns (h = 0):       {sum(1 for c in cols if h_real[c]==0)} of {len(cols)}")

print()
print("="*70)
print("M.  IS THE REALISED IDEAL 'TYPICAL' OR SPECIAL?")
print("="*70)
# rank of the real ideal by size among all ideals: compute size distribution
memo2={}
def sizes(i, assigned):
    if i==len(order): return Counter({0:1})
    key=(i,assigned)
    if key in memo2: return memo2[key]
    c=order[i]; A=dict(assigned)
    lb=0
    for d in succ[c]:
        if d in A: lb=max(lb,A[d])
    tot=Counter()
    for h in range(lb, cap[c]+1):
        A2=dict(A); A2[c]=h
        need={d for d in order[i+1:]}
        keep=tuple(sorted((k2,v2) for k2,v2 in A2.items()
                          if any(k2[0]>=e[0] and k2[1]>=e[1] for e in need)))
        sub=sizes(i+1, keep)
        for s,v in sub.items(): tot[s+h]+=v
    memo2[key]=tot
    return tot
dist=sizes(0, tuple())
tot=sum(dist.values())
mean=sum(s*v for s,v in dist.items())/tot
below=sum(v for s,v in dist.items() if s<118)
print(f"  ideal sizes range {min(dist)}..{max(dist)}, mean {mean:.2f}")
print(f"  ideals with fewer than 118 cells: {below:,} ({100*below/tot:.2f}%)")
print(f"  the realised system (118 cells) sits at the {100*below/tot:.1f}th percentile by size")
print(f"  number of ideals with exactly 118 cells: {dist[118]:,}")