# Finer Zeno segmentation: process B source-blocks per call against the frozen
# current set A; accumulate new cells; persist cursor. One call = bounded blocks.
import numpy as np, json, os, time, sys

def _uniq(A):
    A=np.ascontiguousarray(A.astype(np.int32))
    v=A.view([('',A.dtype)]*A.shape[1]); _,idx=np.unique(v,return_index=True)
    return A[np.sort(idx)]

st=sys.argv[1]; nblocks=int(sys.argv[2]); BLK=int(sys.argv[3]) if len(sys.argv)>3 else 64
A=np.load(st+'.npy'); meta=json.load(open(st+'.json'))
cur=meta.get('cursor',0); n=A.shape[0]; d=A.shape[1]
acc=[np.load(st+'_acc.npy')] if os.path.exists(st+'_acc.npy') else []
t=time.time(); done_sweep=False
for _ in range(nblocks):
    if cur>=n: done_sweep=True; break
    blk=A[cur:cur+BLK]
    mn=np.minimum(blk[:,None,:],A[None,:,:]).reshape(-1,d)
    mx=np.maximum(blk[:,None,:],A[None,:,:]).reshape(-1,d)
    acc.append(_uniq(np.vstack([mn,mx]))); cur+=BLK
acc=[_uniq(np.vstack(acc))] if acc else acc
if acc: np.save(st+'_acc.npy', acc[0])
meta['cursor']=cur; json.dump(meta, open(st+'.json','w'))
newn=acc[0].shape[0] if acc else n
print(f"cursor {cur}/{n}  acc_uniq={newn}  {time.time()-t:.1f}s  sweep_done={done_sweep or cur>=n}")
# if sweep done, fold acc into A -> next iteration
if done_sweep or cur>=n:
    U=_uniq(np.vstack([A, acc[0]])) if acc else A
    grew = U.shape[0]!=n
    np.save(st+'.npy', U)
    meta['cursor']=0; meta['iter']=meta.get('iter',0)+1; meta['n']=int(U.shape[0]); meta['grew']=bool(grew)
    if os.path.exists(st+'_acc.npy'): os.remove(st+'_acc.npy')
    json.dump(meta, open(st+'.json','w'))
    print(f"  FOLD iter={meta['iter']} n->{U.shape[0]} grew={grew}")