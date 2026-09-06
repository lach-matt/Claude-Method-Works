import numpy as np, eldata as ed
from collections import Counter
from itertools import combinations

L=[(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,2*(2*l+1)+1)]
ZS=sorted(ed.E)

print("="*74); print("D.  INFORMATION CONTENT: how much does (n,ℓ,k) compress?"); print("="*74)
# Entropy of the coordinate distribution over the 118 occupied cells
def H(vals):
    c=Counter(vals); N=len(vals)
    return -sum((v/N)*np.log2(v/N) for v in c.values())
hn=H([ed.E[z][0] for z in ZS]); hl=H([ed.E[z][1] for z in ZS]); hk=H([ed.E[z][2] for z in ZS])
hjoint=H([ed.E[z] for z in ZS])
print(f"  H(n)={hn:.3f}  H(ℓ)={hl:.3f}  H(k)={hk:.3f} bits")
print(f"  H(n,ℓ,k) joint = {hjoint:.3f} bits   (= log2(118) = {np.log2(118):.3f}, injective)")
print(f"  sum of marginals = {hn+hl+hk:.3f}")
print(f"  redundancy = {hn+hl+hk-hjoint:.3f} bits  → coordinates are correlated")
print(f"  H(Z) for a flat list of 118 = {np.log2(118):.3f} bits")
print("  → The lattice is a lossless recoding of the element list, not a")
print("     compression. It reorganises information rather than reducing it.")

print()
print("="*74); print("E.  MUTUAL INFORMATION between coordinates"); print("="*74)
def MI(a,b):
    ca=Counter(a); cb=Counter(b); cab=Counter(zip(a,b)); N=len(a)
    s=0
    for (x,y),v in cab.items():
        s+= (v/N)*np.log2((v/N)/((ca[x]/N)*(cb[y]/N)))
    return s
ns=[ed.E[z][0] for z in ZS]; ls=[ed.E[z][1] for z in ZS]; ks=[ed.E[z][2] for z in ZS]
print(f"  I(n;ℓ) = {MI(ns,ls):.3f} bits")
print(f"  I(n;k) = {MI(ns,ks):.3f} bits")
print(f"  I(ℓ;k) = {MI(ls,ks):.3f} bits   ← the constraint k ≤ 2(2ℓ+1) shows up here")

print()
print("="*74); print("F.  HASSE DIAGRAM as a NETWORK — graph invariants"); print("="*74)
def leq(a,b): return all(x<=y for x,y in zip(a,b))
Ls=set(L)
# covers: b covers a if a<b and no c strictly between
cov=[]
for a in L:
    for d in range(3):
        b=list(a); b[d]+=1; b=tuple(b)
        if b in Ls: cov.append((a,b))
print(f"  Hasse edges (covering relations): {len(cov)}")
deg=Counter()
for a,b in cov: deg[a]+=1; deg[b]+=1
print(f"  mean degree = {np.mean(list(deg.values())):.3f}")
print(f"  max degree  = {max(deg.values())}")
# graded? check rank function consistency
rk={c: sum(c) for c in L}
graded=all(rk[b]-rk[a]==1 for a,b in cov)
print(f"  graded by n+ℓ+k: {graded}")
# longest chain
print(f"  rank range: {min(rk.values())} .. {max(rk.values())}  → longest chain length {max(rk.values())-min(rk.values())+1}")

print()
print("="*74); print("G.  WHERE DO THE 118 ELEMENTS SIT IN THE POSET?"); print("="*74)
occ=set(ed.E[z] for z in ZS)
# is the occupied set an order ideal (downward closed)? a filter? an antichain?
down = all(any(leq(y,x) for y in occ) for x in occ)
is_ideal = all( (y in occ) for x in occ for y in L if leq(y,x) )
anti = not any(leq(a,b) and a!=b for a,b in combinations(sorted(occ),2))
print(f"  occupied set is a down-set (order ideal): {is_ideal}")
print(f"  occupied set is an antichain:             {anti}")
chains=0
for a,b in combinations(sorted(occ),2):
    if leq(a,b): chains+=1
print(f"  comparable pairs among the 118 occupied cells: {chains} of {len(occ)*(len(occ)-1)//2}")
print("  → the elements form neither an ideal nor an antichain; they are a")
print("     sparse, irregular subset. This is why the lattice ORDERS the")
print("     elements but does not by itself SELECT which cells are occupied.")