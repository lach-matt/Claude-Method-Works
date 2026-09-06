# Zeno-segmented sublattice closure.
# One CALL = one iteration (one full min/max pass). State persisted to disk.
# Never runs to fixpoint in a single call; each pass reports |S|, additions, time.
import numpy as np, json, os, time, sys

def _uniq(A):
    A=np.ascontiguousarray(A.astype(np.int32))
    v=A.view([('',A.dtype)]*A.shape[1])
    _,idx=np.unique(v,return_index=True)
    return A[np.sort(idx)]

def one_pass(A, block=128):
    n,d=A.shape
    pieces=[A]
    for s in range(0,n,block):
        blk=A[s:s+block]
        mn=np.minimum(blk[:,None,:],A[None,:,:]).reshape(-1,d)
        mx=np.maximum(blk[:,None,:],A[None,:,:]).reshape(-1,d)
        pieces.append(_uniq(np.vstack([mn,mx])))
    return _uniq(np.vstack(pieces))

def load(state):
    A=np.load(state+'.npy')
    meta=json.load(open(state+'.json'))
    return A, meta

def save(state, A, meta):
    np.save(state+'.npy', A)
    json.dump(meta, open(state+'.json','w'))

if __name__=='__main__':
    # args: state_prefix  [init_module init_func]  [max_passes]
    state=sys.argv[1]
    max_passes=int(sys.argv[-1]) if sys.argv[-1].isdigit() else 1
    if not os.path.exists(state+'.npy'):
        # initialize from a seed file state_prefix_seed.npy
        A=np.load(state+'_seed.npy')
        A=_uniq(A)
        save(state,A,{'iter':0,'n':int(A.shape[0]),'seed_n':int(A.shape[0]),'done':False})
        print(f'init {state}: n={A.shape[0]}')
    for _ in range(max_passes):
        A,meta=load(state)
        if meta.get('done'): 
            print('already done at iter',meta['iter'],'n',meta['n']); break
        n0=A.shape[0]; t=time.time()
        U=one_pass(A)
        dt=time.time()-t
        meta['iter']+=1; meta['n']=int(U.shape[0]); meta['last_add']=int(U.shape[0]-n0); meta['last_dt']=round(dt,1)
        if U.shape[0]==n0: meta['done']=True
        save(state,U,meta)
        print(f"iter {meta['iter']}: n {n0}->{U.shape[0]} (+{U.shape[0]-n0}) {dt:.1f}s done={meta.get('done',False)}")
        if meta.get('done'): break