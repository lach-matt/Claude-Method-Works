import math, collections, itertools
from extmod import ext
from tower2mod import L9
X=ext(None); N=len(X)
A={'shell':lambda c:c[4]<=c[0],'subshell':lambda c:c[5]<=c[1],'occupancy':lambda c:c[9]<=c[2],'spin':lambda c:c[8]<=c[7]}
P={k:sum(1 for c in X if f(c))/N for k,f in A.items()}
def H(counts):
    n=sum(counts.values()); return -sum(v/n*math.log2(v/n) for v in counts.values() if v)
def MI(fu,fv):
    j=collections.Counter((fu(c),fv(c)) for c in X); u=collections.Counter(fu(c) for c in X); v=collections.Counter(fv(c) for c in X)
    return H(u)+H(v)-H(j)
coord={'shell':0,'subshell':1,'occupancy':2,'spin':7}
for u,v in [('occupancy','spin'),('subshell','occupancy'),('shell','subshell'),('subshell','spin'),('shell','occupancy'),('shell','spin')]:
    both=sum(1 for c in X if A[u](c) and A[v](c))/N
    print(f'{u}∩{v}: overlap {both/(P[u]*P[v]):.3f}  MI(arrows) {MI(A[u],A[v]):.3f}  MI(coords {coord[u]},{coord[v]}) {MI(lambda c:c[coord[u]],lambda c:c[coord[v]]):.3f} bits')
# falsifier: 2S' ⊥ f | g on L9 and L9'
def ci_test(Y,label):
    ct=collections.Counter((c[6],c[8],c[5]) for c in Y); g_=collections.Counter(c[6] for c in Y); gs=collections.Counter((c[6],c[8]) for c in Y); gf=collections.Counter((c[6],c[5]) for c in Y)
    viol=0; cells=0
    for g in range(4):
        for s in range(4):
            cells+=1
            for f in range(2):
                lhs=ct[(g,s,f)]*g_[g]; rhs=gs[(g,s)]*gf[(g,f)]
                if lhs!=rhs: viol+=1; break
    print(f'{label}: (g,2S\') cells {cells}, violations of 2S\'⊥f|g: {viol}')
L=L9(); ci_test(L,'L9'); ci_test([c for c in L if c[8]<=2*c[5]+1],"L9'")
