import itertools, collections, time, numpy as np
from tower2mod import L8
t0=time.time()
B=L8()
def ext(spcap=None):
    out=[]
    for c in B:
        n,l,k,q,e,f,g,S2=c
        for G in range(g,4*f+2+1):
            for sp in range(0,G+1):
                if spcap is None or sp<=spcap: out.append(c+(sp,G))
    return out
def closed(X):
    arr=np.array(X,dtype=np.int16); lo=arr.min(0); hi=arr.max(0); shape=tuple(int(h-l+1) for l,h in zip(lo,hi)); d=arr.shape[1]
    ok=np.ones(shape,dtype=bool); rel=arr-lo
    for i,j in itertools.combinations(range(d),2):
        T=np.zeros((shape[i],shape[j]),dtype=bool); T[rel[:,i],rel[:,j]]=True
        ix=np.arange(shape[i]).reshape([-1 if t==i else 1 for t in range(d)]); jx=np.arange(shape[j]).reshape([-1 if t==j else 1 for t in range(d)])
        ok&=T[ix,jx]
    return int(ok.sum())-len(X)
if __name__=="__main__":
  for cap in (None,3):
     X=ext(cap); print(f"extended index, 2S' cap {cap}: {len(X)} cells, E={closed(X)}")
 X=ext(None); S=set(X)
 # composition: b's source (n,l,k,2S) == a's (e,f,G,2S')
 by=collections.defaultdict(list)
 for c in X: by[(c[0],c[1],c[2],c[7])].append(c)
 pairs=0; raise_=0
 for a in X:
     bs=by.get((a[4],a[5],a[9],a[8]),[]); pairs+=len(bs)
     if a[9]>a[2]: raise_+=len(bs)
 print('composable pairs',pairs,'raising occupancy (G>k)',raise_,f'{100*raise_/pairs:.1f}%')
 # arrows
 W={'shell':lambda c:c[4]<=c[0],'subshell':lambda c:c[5]<=c[1],'occupancy':lambda c:c[9]<=c[2],'spin':lambda c:c[8]<=c[7]}
 for name,w in W.items():
     Y=[c for c in X if w(c)]; print(f' arrow {name}: {len(Y)} cells E={closed(Y)}')
 # sum / max / min weights over (n,l,k,2S) vs (e,f,G,2S')
 def jm(Y):
     S=set(Y); Y=list(Y); jf=mf=0
     for i in range(len(Y)):
         x=Y[i]
         for j in range(i+1,len(Y)):
             y=Y[j]
             if tuple(map(max,x,y)) not in S: jf+=1
             if tuple(map(min,x,y)) not in S: mf+=1
     return jf,mf
 for name,w in {'sum':lambda c:c[4]+c[5]+c[9]+c[8]<=c[0]+c[1]+c[2]+c[7],'max':lambda c:max(c[4],c[5],c[9],c[8])<=max(c[0],c[1],c[2],c[7]),'min':lambda c:min(c[4],c[5],c[9],c[8])<=min(c[0],c[1],c[2],c[7])}.items():
     Y=[c for c in X if w(c)]; print(f' weight {name}: {len(Y)} cells, E(pairwise)={closed(Y)}; join/meet failures (sample of first 2500 cells) {jm(Y[:2500])}')
 print('time',round(time.time()-t0))
