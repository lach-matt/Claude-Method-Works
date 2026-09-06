import numpy as np

def _unique_rows(A):
    # A: (n,d) int array -> unique rows
    A = np.ascontiguousarray(A)
    v = A.view([('', A.dtype)] * A.shape[1])
    _, idx = np.unique(v, return_index=True)
    return A[np.sort(idx)]

def R_closure_np(cells):
    A = _unique_rows(np.array(sorted(set(cells)), dtype=np.int16))
    while True:
        n = A.shape[0]
        # all pairwise via broadcasting: (n,1,d) vs (1,n,d)
        P = A[:,None,:]; Q = A[None,:,:]
        mn = np.minimum(P,Q).reshape(-1, A.shape[1])
        mx = np.maximum(P,Q).reshape(-1, A.shape[1])
        cand = np.vstack([A, mn, mx])
        U = _unique_rows(cand)
        if U.shape[0] == n:
            return U
        A = U

def E_np(cells):
    s = set(map(tuple, cells))
    U = R_closure_np(s)
    return U.shape[0] - len(s)