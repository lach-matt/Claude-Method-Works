from itertools import product, combinations
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
allc={close(x) for x in product(*RNG)}
V={c for c in allc if not(c[4]>=3 and not(c[2]>=2 or c[3]>=1 or c[0]>=1))}
C=[('evap BH',      lambda c:c[NEC_]>=1),
   ('Planck WH',    lambda c:c[NEC_]>=2),
   ('macro WH',     lambda c:c[NEC_]>=3),
   ('univ horizon', lambda c:c[X_]>=2),
   ('time machine', lambda c:c[X_]>=3),
   ('trivial CC',   lambda c:c[Sc_]>=2),
   ('signalling',   lambda c:c[IC_]>=2),
   ('info loss',    lambda c:c[U_]>=1),
   ('NP in P',      lambda c:c[L_]>=1),
   ('perfect clone',lambda c:c[DNc_]>=2),
   ('perfect disc', lambda c:c[DNd_]>=2)]
# also the PRESERVATIONS (things you might want to keep)
K=[('unitary',      lambda c:c[U_]==0),
   ('Lorentz inv.', lambda c:c[X_]==0),
   ('no signalling',lambda c:c[IC_]<2),
   ('microcausal',  lambda c:c[SD_]==0),
   ('linear',       lambda c:c[L_]==0)]
print('  PAIRWISE COMPATIBILITY AMONG THE 11 CAPABILITIES')
bad=[]
for (n1,f1),(n2,f2) in combinations(C,2):
    n=sum(1 for c in V if f1(c) and f2(c))
    if n==0: bad.append((n1,n2))
print('     incompatible pairs: %s' % (bad if bad else 'NONE - all 55 pairs realisable'))
print()
print('  CAPABILITY vs PRESERVATION  (can you have it and keep that?)')
hdr='  %-14s' % '' + ''.join('%-15s'%k for k,_ in K)
print(hdr)
for nm,f in C:
    row='  %-14s' % nm
    for kn,kf in K:
        n=sum(1 for c in V if f(c) and kf(c))
        row += '%-15s' % (str(n) if n else 'IMPOSSIBLE')
    print(row)
print()
print('  TRIPLES: macroscopic wormhole with combinations of preservations')
mw=[c for c in V if c[NEC_]>=3]
print('     cells with a macroscopic wormhole: %d' % len(mw))
for r in range(1,4):
    for combo in combinations(K,r):
        n=sum(1 for c in mw if all(kf(c) for _,kf in combo))
        tag='' if n else '   <-- IMPOSSIBLE'
        if n==0 or r==3:
            print('     keep %-46s : %5d%s' % (' + '.join(k for k,_ in combo), n, tag))
print()
print('  THE MINIMAL IMPOSSIBLE COMBINATION')
for r in range(1,6):
    found=[]
    for combo in combinations(K,r):
        n=sum(1 for c in mw if all(kf(c) for _,kf in combo))
        if n==0: found.append(tuple(k for k,_ in combo))
    if found:
        print('     smallest size: %d  ->  %s' % (r, found))
        break