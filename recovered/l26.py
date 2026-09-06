import numpy as np, itertools, time, sys
from tower2mod import STAGES
t0=time.time()
dmax=int(sys.argv[1]) if len(sys.argv)>1 else 11
prev=None
for d in range(8,dmax+1):
    X=STAGES[d](); arr=np.array(X,dtype=np.int16)
    lo=arr.min(0); hi=arr.max(0); shape=tuple(int(h-l+1) for l,h in zip(lo,hi))
    box=int(np.prod(shape))
    # projection onto previous stage
    if prev is not None:
        proj=set(map(tuple,arr[:,:d-1].tolist())); print(f'  L{d} projects onto L{d-1} exactly:', proj==prev)
    prev=set(X)
    # closure test: X closed iff every ambient cell whose all pairwise projections lie in pi_ij(X) is in X
    # count cells passing all pairwise tests
    ok=np.ones(shape,dtype=bool)
    rel=arr-lo
    for i,j in itertools.combinations(range(d),2):
        T=np.zeros((shape[i],shape[j]),dtype=bool); T[rel[:,i],rel[:,j]]=True
        idx=[None]*d; 
        ix=np.arange(shape[i]).reshape([-1 if t==i else 1 for t in range(d)])
        jx=np.arange(shape[j]).reshape([-1 if t==j else 1 for t in range(d)])
        ok&=T[ix,jx]
    R=int(ok.sum())
    print(f'L{d}: |X|={len(X)} box={box} |R(X)|={R} E={R-len(X)}  t={round(time.time()-t0)}s')
    if d==9:
        p=[c for c in X if c[8]<=2*c[5]+1]; cut=[c for c in X if not c[8]<=2*c[5]+1]
        print("  L9' (2S'<=2f+1):",len(p),'cut',len(cut),'all (f=0,g=2,2S\'=2):',all(c[5]==0 and c[6]==2 and c[8]==2 for c in cut))