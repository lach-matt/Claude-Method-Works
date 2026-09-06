import numpy as np, itertools
from functools import lru_cache

# ---- Lambda: (n, l, k) cells for the 118 ground-state electrons -------------
# subshell filling order, k = 1..2(2l+1) within each subshell
SUB = [(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),(5,1),
       (6,0),(4,3),(5,2),(6,1),(7,0),(5,3),(6,2),(7,1)]
cells=[]
for (n,l) in SUB:
    for k in range(1,2*(2*l+1)+1): cells.append((n,l,k))
cells=sorted(set(cells)); N=len(cells)
idx={c:i for i,c in enumerate(cells)}
A=np.array(cells)

le = np.all(A[:,None,:] <= A[None,:,:], axis=2)   # le[i,j] : cell i <= cell j
np.fill_diagonal(le, True)
comp = le | le.T
print(f"|Lambda| = {N} cells")
print(f"comparability density = {(comp.sum()-N)/(N*(N-1)):.3f}   (chain would be 1.000)")
print(f"maximal elements: {sum(1 for i in range(N) if le[i].sum()==1)}")
print(f"minimal elements: {sum(1 for i in range(N) if le[:,i].sum()==1)}")
# max antichain (poset width) via LP-free greedy bound: largest rank level
rank = A.sum(1)
print(f"largest level (antichain lower bd) = {max(np.bincount(rank)):d}")