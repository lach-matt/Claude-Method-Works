# Sub-pass segmentation: one CALL processes a bounded range of source-blocks
# against the full current set A, appending new min/max rows to a growth buffer.
# When a pass's blocks are exhausted, fold buffer into A and start next pass.
import numpy as np, json, os, time, sys

def _uniq(A):
    A=np.ascontiguousarray(A.astype(np.int32))
    v=A.view([('',A.dtype)]*A.shape[1])
    _,idx=np.unique(v,return_index=True)
    return A[np.sort(idx)]

def process(state, nblocks, block=64, budget=200.0):
    A=np.load(state+'.npy')
    meta=json.load(open(state+'.json'))
    if meta.get('done'):
        print('done: n=',meta['n'],'iter',meta['iter']); return
    n,d=A.shape
    cursor=meta.get('cursor',0)
    # growth buffer file
    gb=state+'_grow.npy'
    grow = np.load(gb) if os.path.exists(gb) else np.zeros((0,d),dtype=np.int32)
    t=time.time(); did=0
    while cursor<n and did<nblocks and (time.time()-t)<budget:
        blk=A[cursor:cursor+block]
        mn=np.minimum(blk[:,None,:],A[None,:,:]).reshape(-1,d)
        mx=np.maximum(blk[:,None,:],A[None,:,:]).reshape(-1,d)
        u=_uniq(np.vstack([mn,mx]))
        grow=_uniq(np.vstack([grow,u]))
        cursor+=block; did+=1
    if cursor>=n:
        # pass complete: fold grow into A
        U=_uniq(np.vstack([A,grow]))
        meta['iter']+=1; meta['last_add']=int(U.shape[0]-n); meta['n']=int(U.shape[0])
        meta['cursor']=0
        if U.shape[0]==n: meta['done']=True
        np.save(state+'.npy', U)
        if os.path.exists(gb): os.remove(gb)
        json.dump(meta, open(state+'.json','w'))
        print(f"PASS {meta['iter']} complete: n {n}->{U.shape[0]} (+{U.shape[0]-n}) done={meta.get('done',False)} [{time.time()-t:.0f}s]")
    else:
        np.save(gb, grow)
        meta['cursor']=cursor
        json.dump(meta, open(state+'.json','w'))
        print(f"pass {meta['iter']+1} partial: cursor {cursor}/{n}, grow={grow.shape[0]} [{time.time()-t:.0f}s]")

if __name__=='__main__':
    state=sys.argv[1]; nblocks=int(sys.argv[2])
    process(state, nblocks)