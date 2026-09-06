import itertools, numpy as np
def E(X):
    arr=np.array(X); lo=arr.min(0); hi=arr.max(0); shape=tuple(int(h-l+1) for l,h in zip(lo,hi)); d=arr.shape[1]
    ok=np.ones(shape,dtype=bool); rel=arr-lo
    for i,j in itertools.combinations(range(d),2):
        T=np.zeros((shape[i],shape[j]),dtype=bool); T[rel[:,i],rel[:,j]]=True
        ix=np.arange(shape[i]).reshape([-1 if t==i else 1 for t in range(d)]); jx=np.arange(shape[j]).reshape([-1 if t==j else 1 for t in range(d)])
        ok&=T[ix,jx]
    return int(ok.sum())-len(X)