from itertools import product
# coords: X Sc IC U NEC L SD DNc DNd AC
RNG=[range(4),range(3),range(3),range(3),range(5),range(2),range(2),range(3),range(3),range(2)]
NM=['X','Sc','IC','U','NEC','L','SD','DNc','DNd','AC']
X_,Sc_,IC_,U_,NEC_,L_,SD_,DNc_,DNd_,AC_=range(10)
def mkclose(with_ac):
    def close(x):
        x=list(x); g=True
        while g:
            g=False
            def rz(i,v):
                nonlocal g
                if x[i]<v: x[i]=v; g=True
            if x[0]>=3: rz(4,2)
            if x[1]>=2: rz(2,1)
            if x[2]>=2: rz(0,1)
            if x[3]>=2: rz(2,2)
            if x[3]>=1: rz(4,1)
            if x[4]>=4: rz(0,1)
            if x[5]>=1: rz(8,1)
            if x[6]>=1: rz(2,2)
            if x[7]>=2: rz(2,2); rz(5,1); rz(8,2)
            if x[8]>=2: rz(7,2)
            if with_ac:
                if x[AC_]>=1: rz(4,2)          # achronal violation needs ANEC violation
                if x[0]>=3: rz(AC_,1)          # chronology violation needs achronal violation (Graham-Olum)
        return tuple(x)
    return close
def E(S,d,ret=False):
    S=set(S); vals=[sorted({c[i] for c in S}) for i in range(d)]
    def env(i,j):
        m={}
        for c in S:
            if c[i]>m.get(c[j],-99): m[c[j]]=c[i]
        b,o=-99,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    R={x for x in product(*vals) if all(x[i]<=phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i!=j)}
    return (len(R)-len(S), sorted(R-S)) if ret else len(R)-len(S)
paid=lambda c: c[IC_]>=2 or c[U_]>=1 or c[X_]>=1
VARIANTS=[
 ('A  9 coords, disjunction on NEC>=3 (baseline)', False, lambda c: not(c[4]>=3 and not paid(c))),
 ('B  10 coords, disjunction on NEC>=3',           True,  lambda c: not(c[4]>=3 and not paid(c))),
 ('C  10 coords, disjunction on AC=1',             True,  lambda c: not(c[AC_]>=1 and not paid(c))),
 ('D  10 coords, disjunction on AC=1 AND NEC>=3',  True,  lambda c: not(c[AC_]>=1 and c[4]>=3 and not paid(c))),
]
for lab,wac,filt in VARIANTS:
    cl=mkclose(wac); d=10 if wac else 9
    rng=RNG if wac else RNG[:9]
    allc={cl(tuple(list(x)+([0] if not wac else []))) [:d] if False else cl(x if wac else tuple(list(x)+[0]))[:d] for x in product(*rng)}
    V={c for c in allc if filt(c+((0,) if len(c)<10 else ()))}
    e,ex=E(V,d,ret=True)
    core=set()
    for c in ex:
        core.add((c[X_],c[U_],c[NEC_])+((c[AC_],) if d==10 else ()))
    print('  %-46s |X|=%5d  E=%4d  core=%d  %s' % (lab,len(V),e,len(core),sorted(core)[:3]))
print()
print('  WHERE THE KNOWN SOLUTIONS SIT  (10-coordinate index, variant C)')
cl=mkclose(True)
allc={cl(x) for x in product(*RNG)}
V={c for c in allc if not(c[AC_]>=1 and not paid(c))}
o=cl((0,1,0,0,1,0,0,0,0,0))
cases=[('us (Casimir measured)',            (0,1,0,0,1,0,0,0,0,0)),
       ('MMP long wormhole, sub-electroweak',(0,1,0,0,2,0,0,0,0,0)),
       ('a short wormhole (achronal viol.)', (0,1,0,0,2,0,0,0,0,1)),
       ('macroscopic long wormhole',         (0,1,0,0,3,0,0,0,0,0)),
       ('macroscopic short wormhole',        (0,1,0,0,3,0,0,0,0,1)),
       ('time machine',                      (3,1,0,0,2,0,0,0,0,0))]
ex=set(E(V,10,ret=True)[1])
for nm,raw in cases:
    c=cl(raw)
    st = 'ADMISSIBLE' if c in V else ('BLIND SPOT' if c in ex else 'excluded/closed away')
    print('     %-36s %s  %s' % (nm, c, st))