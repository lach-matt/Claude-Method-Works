import numpy as np, time
def subclose(U, tmax=250):
    t0=time.time()
    C=np.unique(np.array(U,dtype=np.int16),axis=0); seen=set(map(tuple,C.tolist())); N=C.copy()
    while len(N):
        add=set()
        for i in range(0,len(N),64):
            blk=N[i:i+64]
            J=np.maximum(blk[:,None,:],C[None,:,:]).reshape(-1,C.shape[1]); M=np.minimum(blk[:,None,:],C[None,:,:]).reshape(-1,C.shape[1])
            for z in map(tuple,np.unique(np.concatenate([J,M]),axis=0).tolist()):
                if z not in seen: add.add(z)
            if time.time()-t0>tmax: return None,len(seen)-len(U)
        if not add: break
        N=np.array(sorted(add),dtype=np.int16); seen|=add; C=np.concatenate([C,N])
    return len(seen)-len(U), len(seen)
if __name__=='__main__':
    from tower2mod import L9
    A=L9(); dl=lambda c:c[5]-c[1]; ds=lambda c:c[8]-c[7]
    for name,fs in {'(dl,dS)':[dl,ds],'dl':[dl],'dS':[ds]}.items():
        X=[c+tuple(f(c) for f in fs) for c in A]; e,n=subclose(X,tmax=80); print(f'adjoin {name}: sublattice E={e} (closure size {n})',flush=True)