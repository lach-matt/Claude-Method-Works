from itertools import product
# law coords: X Sc IC U NEC L SD DNc DNd AC   |  setting coords: FLAT CONN COUP
LR=[range(4),range(3),range(3),range(3),range(5),range(2),range(2),range(3),range(3),range(2)]
SR=[range(3),range(2),range(2)]     # FLAT 0 exact,1 asympt,2 curved/compact ; CONN 0 simple,1 not ; COUP 0 minimal,1 non
NM=['X','Sc','IC','U','NEC','L','SD','DNc','DNd','AC','FLAT','CONN','COUP']
X_,Sc_,IC_,U_,NEC_,L_,SD_,DNc_,DNd_,AC_,FLAT_,CONN_,COUP_=range(13)
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
        if x[4]>=2: rz(FLAT_,1)      # any ANEC violation needs at least curvature somewhere
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
CH={
 'Buniy'      : (lambda c: c[NEC_]>=3,  lambda c: True,
                 lambda c: c[U_]>=1 or c[X_]>=1),
 'Hartman'    : (lambda c: c[NEC_]>=2,  lambda c: c[FLAT_]==0,
                 lambda c: c[U_]>=1 or c[X_]>=1 or c[SD_]>=1),
 'Wall-GSL'   : (lambda c: c[AC_]>=1,   lambda c: c[COUP_]==0,
                 lambda c: c[U_]>=1 or c[X_]>=1),
 'Graham-Olum': (lambda c: c[AC_]>=1,   lambda c: c[FLAT_]<=1 and c[CONN_]==0,
                 lambda c: c[X_]>=3),
}
allc={close(x) for x in product(*(LR+SR))}
print('  closed cells (13 coords): %d' % len(allc))
def build(withjur):
    V=set()
    for c in allc:
        ok=True
        for n,(trig,jur,cur) in CH.items():
            if trig(c) and (jur(c) if withjur else True) and not cur(c): ok=False; break
        if ok: V.add(c)
    return V
for lab,wj in [('charges WITHOUT jurisdiction', False),('charges WITH jurisdiction', True)]:
    V=build(wj); e,ex=E(V,13,ret=True)
    core={(c[X_],c[U_],c[SD_],c[NEC_],c[AC_],c[FLAT_],c[CONN_],c[COUP_]) for c in ex}
    print('  %-32s |X|=%5d  E=%5d  core=%d' % (lab,len(V),e,len(core)))
print()
V=build(True); ex=set(E(V,13,ret=True)[1])
def mk(X,U,NEC,AC,FLAT,CONN,COUP,SD=0):
    return close((X,1,0,U,NEC,0,SD,0,0,AC,FLAT,CONN,COUP))
cases=[('us',                                     mk(0,0,1,0,1,0,0)),
       ('MMP long wormhole (asympt flat, curved)',mk(0,0,2,0,1,0,0)),
       ('macroscopic LONG wormhole',              mk(0,0,3,0,1,0,0)),
       ('macroscopic SHORT wormhole',             mk(0,0,3,1,1,0,0)),
       ('short WH, not simply connected',         mk(0,0,3,1,1,1,0)),
       ('ANEC violation in EXACTLY flat space',   mk(0,0,2,0,0,0,0))]
print('  %-42s %-46s %s' % ('case','cell','status'))
for nm,c in cases:
    st='ADMISSIBLE' if c in V else ('BLIND SPOT' if c in ex else 'closed away')
    print('  %-42s %-46s %s' % (nm, str(c), st))
print()
print('  THE CORE, WITH JURISDICTION')
core={}
for c in ex:
    k=(c[X_],c[U_],c[SD_],c[NEC_],c[AC_],c[FLAT_],c[CONN_],c[COUP_])
    core.setdefault(k,c)
for k,rep in sorted(core.items())[:8]:
    unpaid=[n for n,(t,j,cu) in CH.items() if t(rep) and j(rep) and not cu(rep)]
    print('     X=%d U=%d SD=%d NEC=%d AC=%d FLAT=%d CONN=%d COUP=%d -> unpaid: %s'
          % (k+(', '.join(unpaid) if unpaid else 'NONE - no charger has standing',)))