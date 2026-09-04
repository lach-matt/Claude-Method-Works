from itertools import product
RNG=[range(4),range(3),range(3),range(3),range(5),range(2),range(2),range(3),range(3),range(2)]
NM=['X','Sc','IC','U','NEC','L','SD','DNc','DNd','AC']
X_,Sc_,IC_,U_,NEC_,L_,SD_,DNc_,DNd_,AC_=range(10)
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
        if x[AC_]>=1: rz(4,2)
        if x[0]>=3: rz(AC_,1)
    return tuple(x)
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
# the four charge relations: (name, trigger, currency)
CH = {
 'Buniy'      : (lambda c: c[NEC_]>=3,               lambda c: c[U_]>=1 or c[X_]>=1),
 'Hartman'    : (lambda c: c[NEC_]>=2,               lambda c: c[U_]>=1 or c[X_]>=1 or c[SD_]>=1),
 'Wall-GSL'   : (lambda c: c[AC_]>=1,                lambda c: c[U_]>=1 or c[X_]>=1),
 'Graham-Olum': (lambda c: c[AC_]>=1,                lambda c: c[X_]>=3),
}
allc={close(x) for x in product(*RNG)}
print('  closed cells before any charge: %d' % len(allc))
print()
print('  %-30s %6s %6s %6s  core' % ('charges applied','cells','E','core'))
import itertools as it
def build(names):
    V=set()
    for c in allc:
        ok=True
        for n in names:
            trig,cur=CH[n]
            if trig(c) and not cur(c): ok=False; break
        if ok: V.add(c)
    return V
for r in range(0,5):
    for combo in it.combinations(CH,r):
        if r not in (0,1,4) and combo not in [('Buniy','Hartman'),('Buniy','Wall-GSL'),('Hartman','Wall-GSL'),('Buniy','Hartman','Wall-GSL')]: continue
        V=build(combo)
        if not V: 
            print('  %-30s  EMPTY' % (', '.join(combo) or 'none')); continue
        e,ex=E(V,10,ret=True)
        core={(c[X_],c[U_],c[SD_],c[NEC_],c[AC_]) for c in ex}
        print('  %-30s %6d %6d %6d  %s' % (', '.join(combo) or 'none', len(V), e, len(core), sorted(core)[:2]))
print()
print('  ALL FOUR CHARGES')
V=build(list(CH))
e,ex=E(V,10,ret=True)
print('     cells %d   E %d' % (len(V), e))
core={(c[X_],c[U_],c[SD_],c[NEC_],c[AC_]) for c in ex}
print('     core (X,U,SD,NEC,AC): %s' % sorted(core))
o=close((0,1,0,0,1,0,0,0,0,0))
print('     our cell admissible: %s' % (o in V))
mmp=close((0,1,0,0,2,0,0,0,0,0))
print('     MMP admissible     : %s' % (mmp in V))
print()
print('  WHICH CHARGER IS UNPAID AT EACH CORE CELL')
for cc in sorted(core):
    rep=[c for c in ex if (c[X_],c[U_],c[SD_],c[NEC_],c[AC_])==cc][0]
    unpaid=[n for n,(t,cu) in CH.items() if t(rep) and not cu(rep)]
    print('     X=%d U=%d SD=%d NEC=%d AC=%d  ->  unpaid: %s' % (cc+(', '.join(unpaid),)))