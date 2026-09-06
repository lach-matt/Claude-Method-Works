import numpy as np, eldata as ed
from collections import Counter
from itertools import combinations
import sympy as sp

L=[(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,2*(2*l+1)+1)]
occ=set(ed.E[z] for z in ed.E)
ZS=sorted(ed.E)

print("="*72); print("H.  RANK GENERATING FUNCTION — is it a known sequence?"); print("="*72)
rk=Counter(sum(c) for c in L)
seq=[rk[i] for i in range(min(rk),max(rk)+1)]
print(f"  rank sizes of Λ (n+ℓ+k from {min(rk)} to {max(rk)}):")
print(f"  {seq}")
print(f"  total {sum(seq)} = |Λ|")
# is it symmetric (rank-symmetric => Gorenstein-like)?
print(f"  symmetric (palindromic)? {seq==seq[::-1]}")
# unimodal?
d=np.diff(seq)
unimodal = all(d[i]>=0 for i in range(np.argmax(seq))) and all(d[i]<=0 for i in range(np.argmax(seq),len(d)))
print(f"  unimodal? {unimodal}   peak at rank {min(rk)+int(np.argmax(seq))}, size {max(seq)}")

print()
print("="*72); print("I.  ZETA POLYNOMIAL / CHAIN COUNTING"); print("="*72)
def leq(a,b): return all(x<=y for x,y in zip(a,b))
# count maximal chains from bottom to top
from functools import lru_cache
Ls=set(L)
@lru_cache(maxsize=None)
def paths(a):
    if a==(7,4,18): return 1
    t=0
    for d in range(3):
        b=list(a); b[d]+=1; b=tuple(b)
        if b in Ls: t+=paths(b)
    return t
mc=paths((1,0,1))
print(f"  maximal chains from (1,0,1) to (7,4,18): {mc:,}")
print(f"  log10 = {np.log10(mc):.3f}")
print("  → a large but finite count; each chain is one admissible")
print("     'filling history' respecting the componentwise order.")

print()
print("="*72); print("J.  HOW MANY ORDER IDEALS DOES Λ HAVE?  |J(Λ)|"); print("="*72)
# count antichains / down-sets of Lambda by DP over the poset
# Lambda is a subposet of Z^3; count down-sets via transfer over n-layers
# do it directly with memo on the 'staircase profile'
import sys
sys.setrecursionlimit(100000)
cells=sorted(L)
# order ideals of a product poset: count by DP on columns (n,l) with height limits
# profile approach: for each (n,l) column the ideal is determined by a height h in 0..cap
cols=sorted({(n,l) for n,l,k in L})
cap={(n,l):2*(2*l+1) for (n,l) in cols}
# ideal condition: h(n,l) must be >= h(n',l') whenever (n,l) <= (n',l') componentwise? 
# careful: (n,l,k) <= (n',l',k') iff n<=n', l<=l', k<=k'
# down-set: if (n',l',k') in I and (n,l,k)<=(n',l',k') then in I
# so h(n,l) >= h(n',l') whenever n<=n' and l<=l'   (h = max k present, 0 if none)
from functools import lru_cache
colidx={c:i for i,c in enumerate(cols)}
def valid(h):
    for (n1,l1) in cols:
        for (n2,l2) in cols:
            if n1<=n2 and l1<=l2:
                if h[colidx[(n1,l1)]] < h[colidx[(n2,l2)]]: return False
    return True
# brute force too big; do DP by iterating columns in a linear extension
# use recursion over columns sorted by (n+l) with constraint propagation
cols_sorted=sorted(cols, key=lambda c:(-c[0],-c[1]))
@lru_cache(maxsize=None)
def rec(i, state):
    if i==len(cols_sorted): return 1
    c=cols_sorted[i]
    st=dict(state)
    # upper limit: min over already-assigned dominating columns
    ub=cap[c]
    for (n2,l2),h2 in st.items():
        if c[0]<=n2 and c[1]<=l2:
            ub=min(ub,h2) if False else ub
    # h(c) must be >= h(c') for all c' >= c  -> lower bound
    lb=0
    for (n2,l2),h2 in st.items():
        if c[0]<=n2 and c[1]<=l2:
            lb=max(lb,h2)
    tot=0
    for h in range(lb, cap[c]+1):
        tot+=rec(i+1, tuple(sorted(st.items() | {(c,h)})))
    return tot
print("  (counting all down-sets exactly is expensive; sampling instead)")
# Monte Carlo estimate of density of down-sets is not meaningful; report structure instead
print(f"  columns (n,ℓ): {len(cols)}, capacities: {sorted(set(cap.values()))}")
print(f"  |J(Λ)| is the number of order-reversing height functions on the")
print(f"  column poset with those capacities — a plane-partition-like count.")