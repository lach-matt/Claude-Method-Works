import itertools
from collections import Counter

def report(name, got, want):
    print(f"{'PASS' if got==want else 'FAIL'}  {name}: {got}  (committed {want})")

print("="*64); print("Lambda_cav — rectangular cavity mode index"); print("="*64)
M=N=L=4
def nu(m,n,l): return (m>0)+(n>0)+(l>0)
cav=[(m,n,l,s) for m in range(M+1) for n in range(N+1) for l in range(L+1)
     for s in range(1,nu(m,n,l))]
Sc=set(cav)
report("|L_cav|", len(cav), 2*M*N*L+M*N+M*L+N*L)
report("  = 176", len(cav), 176)
te=((M+1)*(N+1)-1)*L; tm=M*N*(L+1)
report("  = direct TE+TM count", len(cav), te+tm)
jf=mf=0; ex=[]
for x,y in itertools.combinations(cav,2):
    if tuple(map(max,x,y)) not in Sc: jf+=1
    m_=tuple(map(min,x,y))
    if m_ not in Sc:
        mf+=1
        if len(ex)<3: ex.append((x,y,m_))
report("pairs", len(cav)*(len(cav)-1)//2, 15400)
report("join failures", jf, 0)
report("meet failures", mf, 768)
for e in ex: print("     meet fail example:", e)
core=[(m,n,l) for m in range(M+1) for n in range(N+1) for l in range(L+1)]
Sk=set(core); jf2=mf2=mv2=dv2=0
for x,y in itertools.combinations(core,2):
    J=tuple(map(max,x,y)); Mt=tuple(map(min,x,y))
    if J not in Sk: jf2+=1
    if Mt not in Sk: mf2+=1
    if sum(J)+sum(Mt)!=sum(x)+sum(y): mv2+=1
report("core (m,n,l): join+meet failures", jf2+mf2, 0)
report("core: rank-modularity violations", mv2, 0)

print(); print("="*64); print("Lambda_sph — spherical multipole index"); print("="*64)
LC,NC=5,4
sph=[(t,l,m,n) for t in range(2) for l in range(LC+1)
     for m in range(2*l+3) for n in range(NC+1)]
Ss=set(sph)
report("|L_sph|", len(sph), 480)
report("pairs", len(sph)*(len(sph)-1)//2, 114960)
rk=lambda c: sum(c)
report("height", max(map(rk,sph))-min(map(rk,sph)), 22)
jf=mf=mv=0
for x,y in itertools.combinations(sph,2):
    J=tuple(map(max,x,y)); Mt=tuple(map(min,x,y))
    if J not in Ss: jf+=1
    if Mt not in Ss: mf+=1
    if sum(J)+sum(Mt)!=sum(x)+sum(y): mv+=1
report("join failures", jf, 0)
report("meet failures", mf, 0)
report("rank-modularity violations", mv, 0)
import random; random.seed(1); sm=random.sample(sph,45)
dv=sum(1 for x in sm for y in sm for z in sm
       if tuple(max(p,min(q,r)) for p,q,r in zip(x,y,z))
       != tuple(min(max(p,q),max(p,r)) for p,q,r in zip(x,y,z)))
report("distributivity violations /91,125 triples", dv, 0)
lev=Counter(map(rk,sph))
report("Sperner width (widest rank level)", max(lev.values()), 41)
report("F(-1)", sum((-1)**rk(c) for c in sph), 0)
print(f"\n  cav rank profile: {[lev2 for lev2 in [Counter(map(sum,cav))[r] for r in sorted(Counter(map(sum,cav)))]]}")
print(f"  sph rank profile: {[lev[r] for r in sorted(lev)]}")