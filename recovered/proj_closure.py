# Bergman double-projection closure: sublattice of a product of chains is fixed by
# its 2-fold projections. Polynomial; no min/max fixpoint explosion.
import numpy as np, itertools
def E_proj(cells):
    A=np.array(sorted(set(map(tuple,cells))),dtype=np.int32)
    n,d=A.shape
    los=A.min(0); his=A.max(0)
    proj={}
    for i,j in itertools.combinations(range(d),2):
        proj[(i,j)]=set(map(tuple,A[:,[i,j]].tolist()))
    ranges=[range(int(los[k]),int(his[k])+1) for k in range(d)]
    cnt=0
    for cell in itertools.product(*ranges):
        ok=True
        for (i,j),S in proj.items():
            if (cell[i],cell[j]) not in S: ok=False; break
        if ok: cnt+=1
    return cnt-n, cnt, n