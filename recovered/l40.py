from tower2mod import L9
from l33b import E
A=L9(); dl=lambda c:c[5]-c[1]; ds=lambda c:c[8]-c[7]
V={'dl':dl,'dS':ds,'|dl|':lambda c:abs(dl(c)),'|dS|':lambda c:abs(ds(c)),'dl+dS':lambda c:dl(c)+ds(c),'de':lambda c:c[4]-c[0],'dk':lambda c:c[6]-c[2],'dS(half)':lambda c:(c[8]-c[7])//2 if (c[8]-c[7])%2==0 else (c[8]-c[7]),'M=|dl|+1':lambda c:abs(dl(c))+1}
import itertools
res={}
for r in (1,2,3):
    for combo in itertools.combinations(V,r):
        X=[c+tuple(V[k](c) for k in combo) for c in A]; e=E(X); res[combo]=e
        if e in (3900,): print('HIT',combo,e)
print(sorted(res.items(),key=lambda t:t[1])[:12])
print('single-coordinate adjunctions:',{k:v for k,v in res.items() if len(k)==1})