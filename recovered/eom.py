from itertools import product
# X Sc IC U NEC L SD DNc DNd EOM   (EOM: 0 = second-order, 1 = higher-derivative)
RNG=[range(4),range(3),range(3),range(3),range(5),range(2),range(2),range(3),range(3),range(2)]
NM=['X','Sc','IC','U','NEC','L','SD','DNc','DNd','EOM']
X_,Sc_,IC_,U_,NEC_,L_,SD_,DNc_,DNd_,EOM_=range(10)
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
allc={close(x) for x in product(*RNG)}
CASES=[
 ('A  jurisdiction on X=0 (as built, WRONG proxy)',
   lambda c: (c[NEC_]<3) or (c[X_]>=1) or c[U_]>=1),
 ('B  no jurisdiction (silent universalisation)',
   lambda c: (c[NEC_]<3) or c[U_]>=1),
 ('C  jurisdiction on EOM=2nd-order (CORRECT)',
   lambda c: (c[NEC_]<3) or (c[EOM_]>=1) or c[U_]>=1),
 ('D  both X=0 and EOM=2nd-order',
   lambda c: (c[NEC_]<3) or (c[X_]>=1) or (c[EOM_]>=1) or c[U_]>=1),
]
print('  %-46s %7s %6s %6s  core (X,U,NEC,EOM)' % ('reading','cells','E','core'))
for lab,rule in CASES:
    V={c for c in allc if rule(c)}
    e,ex=E(V,10,ret=True)
    core={(c[X_],c[U_],c[NEC_],c[EOM_]) for c in ex}
    print('  %-46s %7d %6d %6d  %s' % (lab,len(V),e,len(core),sorted(core)[:3]))
print()
print('  WHERE THE CORE SITS, READING C')
V={c for c in allc if (c[NEC_]<3) or (c[EOM_]>=1) or c[U_]>=1}
e,ex=E(V,10,ret=True)
core=sorted({(c[X_],c[U_],c[NEC_],c[EOM_]) for c in ex})
for k in core:
    print('     X=%d U=%d NEC=%d EOM=%s' % (k[0],k[1],k[2],'2nd-order' if k[3]==0 else 'higher'))
o=close((0,1,0,0,1,0,0,0,0,0))
print()
print('     our cell %s' % str(o))
print('     our EOM value: 0 (the Standard Model is second-order)')
print('     is the core overhead of us (same X, U)? %s'
      % any(k[0]==o[X_] and k[1]==o[U_] for k in core))
print()
print('  COMPARISON')
print('     reading A put the core at X=0, U=0, NEC=3 - directly overhead')
print('     reading C puts it at %s' % (', '.join('X=%d U=%d NEC=%d EOM=%d'%k for k in core)))
print('     the defect exists in both; its LOCATION depends on which hypothesis is indexed')