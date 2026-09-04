from itertools import product
LR=[range(4),range(3),range(3),range(3),range(5),range(2),range(2),range(3),range(3),range(2)]
SR=[range(3),range(2),range(2)]
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
        if x[4]>=2: rz(FLAT_,1)
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
# jurisdictions now stated fully; currencies tested for coherence
JUR={'Buniy':      lambda c: c[X_]==0,                       # scoped to Lorentz-invariant theories
     'Hartman':    lambda c: c[FLAT_]==0 and c[X_]==0 and c[U_]==0,   # flat, unitary, Lorentz-invariant
     'Wall-GSL':   lambda c: c[COUP_]==0,
     'Graham-Olum':lambda c: c[FLAT_]<=1 and c[CONN_]==0}
TRIG={'Buniy': lambda c: c[NEC_]>=3, 'Hartman': lambda c: c[NEC_]>=2,
      'Wall-GSL': lambda c: c[AC_]>=1, 'Graham-Olum': lambda c: c[AC_]>=1}
RAW={'Buniy':      [('U',lambda c:c[U_]>=1),('X',lambda c:c[X_]>=1)],
     'Hartman':    [('U',lambda c:c[U_]>=1),('X',lambda c:c[X_]>=1),('SD',lambda c:c[SD_]>=1)],
     'Wall-GSL':   [('U',lambda c:c[U_]>=1),('X',lambda c:c[X_]>=1)],
     'Graham-Olum':[('X3',lambda c:c[X_]>=3)]}
# coherence test: does paying currency k exit the charger's jurisdiction?
allc={close(x) for x in product(*(LR+SR))}
print('  COHERENCE OF EACH CURRENCY  (does paying it exit the jurisdiction?)')
COH={}
for n in RAW:
    keep=[]
    for kn,kf in RAW[n]:
        # sample cells where the currency is paid; is the jurisdiction still satisfied?
        pays=[c for c in allc if kf(c)]
        instd=sum(1 for c in pays if JUR[n](c))
        exits = instd==0
        print('     %-12s currency %-3s : jurisdiction still holds in %6d of %6d  %s'
              % (n,kn,instd,len(pays),'EXITS - incoherent' if exits else 'coherent'))
        if not exits: keep.append((kn,kf))
    COH[n]=keep
print()
def build(cur):
    V=set()
    for c in allc:
        ok=True
        for n in TRIG:
            if TRIG[n](c) and JUR[n](c) and not any(f(c) for _,f in cur[n]): ok=False; break
        if ok: V.add(c)
    return V
for lab,cur in [('raw currencies', RAW), ('jurisdiction-coherent currencies', COH)]:
    V=build(cur); e,ex=E(V,13,ret=True)
    core={(c[X_],c[U_],c[SD_],c[NEC_],c[AC_]) for c in ex}
    print('  %-36s |X|=%6d  E=%5d  core=%d' % (lab,len(V),e,len(core)))
print()
V=build(COH); ex=set(E(V,13,ret=True)[1])
def mk(X,U,NEC,AC,FLAT,CONN,COUP):
    return close((X,1,0,U,NEC,0,0,0,0,AC,FLAT,CONN,COUP))
for nm,c in [('us',mk(0,0,1,0,1,0,0)),
             ('MMP long wormhole',mk(0,0,2,0,1,0,0)),
             ('macroscopic LONG wormhole',mk(0,0,3,0,1,0,0)),
             ('macroscopic SHORT wormhole',mk(0,0,3,1,1,0,0))]:
    st='ADMISSIBLE' if c in V else ('BLIND SPOT' if c in ex else 'closed away')
    print('     %-30s %s' % (nm,st))