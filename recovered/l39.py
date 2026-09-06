import math, collections, itertools
from tower2mod import L9
from l33b import E
A=L9()
spin=[c for c in A if c[8]==c[7]]; print('spin rule dS=0:',len(spin),'cells E=',E(spin))
par=[c for c in A if abs(c[5]-c[1])==1]; print('parity rule |dl|=1:',len(par),'cells E=',E(par))
# entry 40: adjoin derived EM coordinates to L9
dl=lambda c:c[5]-c[1]; ds=lambda c:c[8]-c[7]
for name,fs in {'(dl,dS)':[dl,ds],'(|dl|,dS)':[lambda c:abs(dl(c)),ds],'(dl,dS,|dl|)':[dl,ds,lambda c:abs(dl(c))],'(dl,dS,multipole=max(|dl|,1))':[dl,ds,lambda c:max(abs(dl(c)),1)],'(dl,|dS|)':[dl,lambda c:abs(ds(c))]}.items():
    X=[c+tuple(f(c) for f in fs) for c in A]; print(f'adjoin {name}: E={E(X)}')
# image onto (multipole, dS)
for name,fs in {'(|dl|,dS)':[lambda c:abs(dl(c)),ds],'(dl,dS)':[dl,ds]}.items():
    img=sorted(set(tuple(f(c) for f in fs) for c in A)); box=1
    for i in range(len(img[0])): box*=len(set(x[i] for x in img))
    print(f'image {name}: {len(img)} values, box {box}, full rectangle {len(img)==box}, E={E(img)}')
# near-independence: EM predicate vs composition predicate on the same cells
src=set((c[0],c[1],c[2],c[7]) for c in A)
compP=lambda c:(c[4],c[5],c[6],c[8]) in src
def H(cnt):
    n=sum(cnt.values()); return -sum(v/n*math.log2(v/n) for v in cnt.values() if v)
def MI(f,g):
    j=collections.Counter((f(c),g(c)) for c in A); return H(collections.Counter(f(c) for c in A))+H(collections.Counter(g(c) for c in A))-H(j), H(collections.Counter(f(c) for c in A)), H(collections.Counter(g(c) for c in A))
for name,em in {'|dl|=1 & dS=0':lambda c:abs(dl(c))==1 and ds(c)==0,'|dl|=1':lambda c:abs(dl(c))==1,'dS=0':lambda c:ds(c)==0}.items():
    mi,he,hc=MI(em,compP); print(f'EM {name} vs composition: MI {mi:.4f} bits; H(EM) {he:.3f} H(comp) {hc:.3f} min {min(he,hc):.3f}')