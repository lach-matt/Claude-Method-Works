import numpy as np, eldata as ed
from collections import defaultdict

# Columns (n,l) with cap 2(2l+1). Down-set <-> height h(n,l) in [0,cap]
# with h(n,l) >= h(n',l') whenever n<=n' and l<=l'.
# Process n = 7 down to 1. Within a fixed n, h must be non-increasing in l
# (since (n,l) <= (n,l') for l<=l'). Across n: h(n,l) >= h(n+1,l).
# So state = the vector (h(n,0..4)) for the current n; transfer to n-1
# requires h(n-1,l) >= h(n,l) and h(n-1,·) non-increasing in l.

def caps(n):
    return [2*(2*l+1) for l in range(0,min(n,5))]

def nonincreasing_vectors(cap, floor):
    """all v with v[l] in [floor[l], cap[l]] and v non-increasing in l"""
    res=[]
    def rec(l, prev, cur):
        if l==len(cap):
            res.append(tuple(cur)); return
        lo=floor[l]; hi=min(cap[l], prev)
        for v in range(lo, hi+1):
            rec(l+1, v, cur+[v])
    rec(0, 10**9, [])
    return res

# start at n=7
n=7
c7=caps(7)
states=defaultdict(int)
for v in nonincreasing_vectors(c7, [0]*len(c7)):
    states[v]+=1

for n in range(6,0,-1):
    cn=caps(n)
    new=defaultdict(int)
    for v,cnt in states.items():
        floor=[v[l] if l < len(v) else 0 for l in range(len(cn))]
        # also need cap respected
        if any(floor[l]>cn[l] for l in range(len(cn))): continue
        for w in nonincreasing_vectors(cn, floor):
            new[w]+=cnt
    states=new

total=sum(states.values())
print("="*70)
print("K.  THE NUMBER OF ORDER IDEALS OF Λ")
print("="*70)
print(f"  |J(Λ)| = {total:,}")
print(f"  log10  = {np.log10(total):.4f}")
print()
print("  J(Λ) is the distributive lattice of all downward-closed subsets.")
print("  By Section 13 the realised periodic system is exactly one of these.")

# now size distribution
def sizedist():
    n=7; c7=caps(7)
    st=defaultdict(lambda: defaultdict(int))
    for v in nonincreasing_vectors(c7,[0]*len(c7)):
        st[v][sum(v)]+=1
    for n in range(6,0,-1):
        cn=caps(n); new=defaultdict(lambda: defaultdict(int))
        for v,dd in st.items():
            floor=[v[l] if l<len(v) else 0 for l in range(len(cn))]
            if any(floor[l]>cn[l] for l in range(len(cn))): continue
            for w in nonincreasing_vectors(cn,floor):
                s_add=sum(w)
                for s,c in dd.items(): new[w][s+s_add]+=c
        st=new
    out=defaultdict(int)
    for v,dd in st.items():
        for s,c in dd.items(): out[s]+=c
    return out

dist=sizedist()
tot=sum(dist.values())
mean=sum(s*c for s,c in dist.items())/tot
below=sum(c for s,c in dist.items() if s<118)
print()
print("="*70)
print("L.  WHERE THE REALISED SYSTEM SITS AMONG ALL IDEALS")
print("="*70)
print(f"  sizes range {min(dist)}..{max(dist)}, mean {mean:.2f}")
print(f"  ideals of size exactly 118: {dist[118]:,}")
print(f"  ideals smaller than 118:    {below:,}  ({100*below/tot:.2f}%)")
print(f"  → the realised system sits at the {100*below/tot:.1f}th percentile by size")

occ=set(ed.E[z] for z in ed.E)
cols=sorted({(n,l) for (n,l,k) in [(a,b,c) for a in range(1,8) for b in range(0,min(a,5)) for c in [1]]})
h={c: max([k for (n,l,k) in occ if (n,l)==c], default=0) for c in cols}
print()
print("  height profile of the realised ideal:")
for n in range(1,8):
    row=[]
    for l in range(0,5):
        row.append(f"{h[(n,l)]:2d}" if (n,l) in h else " ·")
    print(f"    n={n}: "+" ".join(row))
sat=sum(1 for c in cols if h[c]==2*(2*c[1]+1))
emp=sum(1 for c in cols if h[c]==0)
print(f"  saturated columns: {sat}/{len(cols)}   empty columns: {emp}/{len(cols)}")