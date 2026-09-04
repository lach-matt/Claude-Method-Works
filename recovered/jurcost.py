from itertools import product
RNG=[range(4),range(3),range(3),range(3),range(5),range(2),range(2),range(3),range(3)]
X_,Sc_,IC_,U_,NEC_,L_,SD_,DNc_,DNd_=range(9)
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
def build(rule):
    return {c for c in allc if rule(c)}
CASES=[
 ('unjurisdicted forcing:  NEC>=3 -> U>=1',
   lambda c: (c[NEC_]<3) or c[U_]>=1),
 ('jurisdicted forcing:    NEC>=3 and X=0 -> U>=1',
   lambda c: (c[NEC_]<3) or c[X_]>=1 or c[U_]>=1),
 ('unjurisdicted forcing:  NEC>=3 -> X>=1',
   lambda c: (c[NEC_]<3) or c[X_]>=1),
 ('jurisdicted forcing:    NEC>=3 and U=0 -> X>=1',
   lambda c: (c[NEC_]<3) or c[U_]>=1 or c[X_]>=1),
 ('the original disjunction (3 currencies)',
   lambda c: (c[NEC_]<3) or c[IC_]>=2 or c[U_]>=1 or c[X_]>=1),
]
print('  %-52s %6s %6s %6s' % ('constraint','cells','E','core'))
for lab,rule in CASES:
    V=build(rule); e,ex=E(V,9,ret=True)
    core={(c[X_],c[U_],c[NEC_]) for c in ex}
    print('  %-52s %6d %6d %6d  %s' % (lab,len(V),e,len(core),sorted(core)[:2]))
print()
print('  arity of each form (coordinates named in the constraint):')
print('     NEC>=3 -> U>=1                        : 2  (NEC, U)          BINARY')
print('     NEC>=3 and X=0 -> U>=1                : 3  (NEC, X, U)       TERNARY')
print('     NEC>=3 -> (IC=2 or U>=1 or X>=1)      : 4  (NEC, IC, U, X)   QUATERNARY')
print()
o=close((0,1,0,0,1,0,0,0,0))
for lab,rule in CASES:
    V=build(rule)
    print('     %-52s our cell admissible: %s' % (lab, o in V))