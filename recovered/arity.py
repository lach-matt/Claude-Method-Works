from itertools import product
RNG=[range(4),range(3),range(3),range(3),range(5),range(2),range(2),range(3),range(3)]
NM=['X','Sc','IC','U','NEC','L','SD','DNc','DNd']
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
print('  BASELINE: the 11 unjurisdicted forcings alone')
V=set(allc); e=E(V,9); print('     cells %d   E %d' % (len(V), e))
print()
JUR=[('X=0',   lambda c: c[X_]==0),
     ('SD=0',  lambda c: c[SD_]==0),
     ('L=0',   lambda c: c[L_]==0),
     ('IC<2',  lambda c: c[IC_]<2),
     ('DNc=0', lambda c: c[DNc_]==0)]
print('  FORCING  NEC>=3 -> U>=1  WITH k JURISDICTION CONDITIONS')
print('  %-3s %-34s %6s %7s %6s %6s' % ('k','jurisdiction','arity','cells','E','core'))
for k in range(0,len(JUR)+1):
    js=JUR[:k]
    def rule(c, js=js):
        if c[NEC_]<3: return True
        if not all(f(c) for _,f in js): return True     # outside jurisdiction: no charge
        return c[U_]>=1
    V={c for c in allc if rule(c)}
    e,ex=E(V,9,ret=True)
    core={(c[X_],c[U_],c[NEC_],c[SD_],c[L_],c[IC_],c[DNc_]) for c in ex}
    print('  %-3d %-34s %6d %7d %6d %6d' % (k, (', '.join(n for n,_ in js) or 'none (universal)'), 2+k, len(V), e, len(core)))
print()
print('  SAME TEST ON A DIFFERENT FORCING:  U>=1 -> NEC>=1')
print('  %-3s %-34s %6s %7s %6s' % ('k','jurisdiction','arity','cells','E'))
for k in range(0,4):
    js=JUR[:k]
    def rule2(c, js=js):
        if c[U_]<1: return True
        if not all(f(c) for _,f in js): return True
        return c[NEC_]>=1
    V={c for c in allc if rule2(c)}
    e=E(V,9)
    print('  %-3d %-34s %6d %7d %6d' % (k,(', '.join(n for n,_ in js) or 'none (universal)'),2+k,len(V),e))