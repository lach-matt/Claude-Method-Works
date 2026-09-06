import numpy as np

def _uniq(A):
    A=np.ascontiguousarray(A.astype(np.int16))
    v=A.view([('',A.dtype)]*A.shape[1])
    _,idx=np.unique(v,return_index=True)
    return A[np.sort(idx)]

def R_closure_chunk(cells, block=256):
    A=_uniq(np.array(sorted(set(cells)),dtype=np.int16))
    while True:
        n=A.shape[0]; d=A.shape[1]
        pieces=[A]
        for s in range(0,n,block):
            blk=A[s:s+block]                     # (b,d)
            mn=np.minimum(blk[:,None,:],A[None,:,:]).reshape(-1,d)
            mx=np.maximum(blk[:,None,:],A[None,:,:]).reshape(-1,d)
            pieces.append(_uniq(np.vstack([mn,mx])))
        U=_uniq(np.vstack(pieces))
        if U.shape[0]==n:
            return U
        A=U

def E_chunk(cells, block=256):
    s=set(map(tuple,cells))
    return R_closure_chunk(s,block).shape[0]-len(s)