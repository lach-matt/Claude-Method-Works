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
K=[('unitarity',            lambda c:c[U_]==0),
   ('Lorentz invariance',   lambda c:c[X_]==0),
   ('no signalling',        lambda c:c[IC_]<2),
   ('information causality',lambda c:c[IC_]==0),
   ('microcausality',       lambda c:c[SD_]==0),
   ('linearity',            lambda c:c[L_]==0),
   ('the ANEC',             lambda c:c[NEC_]<2)]
print('  WHAT EACH PRINCIPLE FORBIDS')
excl={}
for kn,kf in K:
    keep=[c for c in V if kf(c)]
    forb=[cn for cn,cf in C if not any(cf(c) for c in keep)]
    excl[kn]=set(forb)
    print('     %-24s keeps %5d cells   forbids: %s' % (kn, len(keep), ', '.join(forb) if forb else 'nothing'))
print()
print('  IS ANY PRINCIPLE REDUNDANT?  (is one exclusion set contained in another?)')
red=[]
for a in excl:
    for b in excl:
        if a!=b and excl[a] and excl[a] <= excl[b]:
            red.append((a,b))
print('     ', red if red else 'no containments - every principle forbids something no other does')
print()
print('  WHICH PRINCIPLE UNIQUELY FORBIDS EACH CAPABILITY?')
for cn,cf in C:
    who=[kn for kn in excl if cn in excl[kn]]
    tag = '  <-- UNIQUE' if len(who)==1 else ''
    print('     %-14s forbidden by: %-58s %s' % (cn, ', '.join(who) if who else 'nothing', tag))
print()
print('  THE ANEC AS A PRINCIPLE')
anec=[c for c in V if c[NEC_]<2]
print('     keeping the ANEC leaves %d of %d cells (%.1f%%)' % (len(anec), len(V), len(anec)/len(V)*100))
print('     it forbids: %s' % ', '.join(sorted(excl['the ANEC'])))
print()
print('  MINIMAL PRINCIPLE SETS THAT FORBID THE MACROSCOPIC WORMHOLE')
mw=[c for c in V if c[NEC_]>=3]
for r in range(1,4):
    hits=[]
    for combo in combinations(K,r):
        if not any(all(kf(c) for _,kf in combo) for c in mw):
            hits.append(tuple(k for k,_ in combo))
    if hits:
        print('     size %d: %s' % (r, hits))
        break