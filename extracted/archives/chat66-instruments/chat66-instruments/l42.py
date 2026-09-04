import collections, math, itertools
from tower2mod import L8
from l33b import E
L=L8(); S=set(L)
# 42: adjunction closure  — L x h closed under join/meet?
def closedJM(X):
    Xs=set(X)
    for i in range(len(X)):
        x=X[i]
        for y in X[i+1:]:
            if tuple(map(max,x,y)) not in Xs or tuple(map(min,x,y)) not in Xs: return False
    return True
H={'projection e':lambda c:c[4],'minimum(k,e)':lambda c:min(c[2],c[4]),'constant 1':lambda c:1,'difference e-l':lambda c:c[4]-c[1],'sum n+e':lambda c:c[0]+c[4],'product k*g':lambda c:c[2]*c[6]}
for name,h in H.items(): print(f'42 L x {name}: closed {closedJM([c+(h(c),) for c in L])}')
# 45: direct join/meet closure of L8 over all unordered pairs
print('45 closed under join and meet, all 475,800 pairs:',closedJM(L))
# 44: J(Λ) covers, words
up=collections.defaultdict(list)
for c in L:
    for i in range(8):
        d=list(c); d[i]+=1; d=tuple(d)
        if d in S: up[c].append(d)
down=collections.defaultdict(list)
for c,v in up.items():
    for w in v: down[w].append(c)
JI=sorted(c for c in L if len(down[c])==1); m=len(JI)
le=lambda a,b: all(p<=q for p,q in zip(a,b))
cov=[(i,j) for i in range(m) for j in range(m) if i!=j and le(JI[i],JI[j]) and not any(k not in (i,j) and le(JI[i],JI[k]) and le(JI[k],JI[j]) for k in range(m))]
print('44 |J|',m,'covers',len(cov))
acc=[w for w in range(1<<m) if all((not w>>j&1) or (w>>i&1) for i,j in cov)]
img=set(sum(1<<i for i in range(m) if le(JI[i],c)) for c in L)
print('   words accepted',len(acc),'of',1<<m,'equal to image of Λ:',set(acc)==img)
fi=collections.Counter(j for i,j in cov); fo=collections.Counter(i for i,j in cov)
print('   max forced-by',max(fi.values()),'max forces',max(fo.values()),'ceil log2 20 =',math.ceil(math.log2(len(cov))))
# longest chain in J
import functools
@functools.lru_cache(None)
def ch(i): return 1+max([ch(j) for j in range(m) if j!=i and le(JI[j],JI[i])],default=0)
print('   longest chain in J(Λ): generators',max(ch(i) for i in range(m)),'covering steps',max(ch(i) for i in range(m))-1)
# 46
rk=collections.Counter(sum(c) for c in L); mean=sum(r*n for r,n in rk.items())/len(L)
print(f'46 mean rank (sum) {mean:.4f}; void {6912-len(L)}; rank sizes: r4={rk[4]} r19={rk[19]} r11={rk[11]} r10={rk[10]}; F(-1)={sum((-1)**sum(c) for c in L)}; log2 976={math.log2(976):.2f}')
print('   palindromic:',[rk[r] for r in range(3,21)]==[rk[r] for r in range(20,2,-1)])
# gcd/lcm embedding
P=[2,3,5,7,11,13,17,19]; N=lambda c:math.prod(p**x for p,x in zip(P,c)); vals=set(N(c) for c in L); ok=True
for i in range(len(L)):
    for y in L[i+1:]:
        x=L[i]
        if math.gcd(N(x),N(y))!=N(tuple(map(min,x,y))) or N(x)*N(y)//math.gcd(N(x),N(y))!=N(tuple(map(max,x,y))): ok=False;break
    if not ok: break
print('   gcd/lcm = meet/join on all pairs:',ok)
# 47: parity band on L9
from tower2mod import L9
A=L9(); band=[c for c in A if abs(c[5]-c[1])<=1]; print('47 band |dl|<=1:',len(band),'cells E=',E(band))
