import random, numpy as np
from mc10 import build, CONS
random.seed(11)
def stats(cells, nsamp=400000):
    N=len(cells); tot=N*(N-1)//2
    if tot<=600000:
        from itertools import combinations
        it=combinations(cells,2); n=tot
    else:
        it=((cells[random.randrange(N)],cells[random.randrange(N)]) for _ in range(nsamp)); n=nsamp
    cnt=np.zeros(7); joint=0; m=0
    for a,b in it:
        lo=tuple(min(u,v) for u,v in zip(a,b)); hi=tuple(max(u,v) for u,v in zip(a,b))
        ok=True; m+=1
        for i,(_,f) in enumerate(CONS):
            if f(lo,hi): cnt[i]+=1
            else: ok=False
        if ok: joint+=1
    p=cnt/m; prod=float(np.prod(p))
    return N, tot, p.min(), p.max(), prod, joint/m, (joint/m)/prod
caps=[(3,3,1,3,1),(4,4,1,3,1),(4,4,2,5,1),(5,5,2,6,1),(5,5,2,8,2),(6,6,3,10,2),(7,7,3,14,3)]
print(f"{'caps':22s}{'cells':>7s}{'pairs':>12s}{'min%':>7s}{'max%':>7s}{'prod%':>8s}{'joint%':>8s}{'factor':>8s}")
for c in caps:
    cells=build(*c); N,tot,mn,mx,prod,j,f=stats(cells)
    print(f"{str(c):22s}{N:7d}{tot:12d}{mn*100:7.1f}{mx*100:7.1f}{prod*100:8.2f}{j*100:8.2f}{f:8.3f}")