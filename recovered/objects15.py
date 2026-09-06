from itertools import product, combinations
NM=['X_exp','X_spon','Sc','IC','U_open','U_ghost','NEC_pt','NEC_ach',
    'L_dyn','L_kin','SD_obs','SD_field','DNc','DNd','EOM']
RNG=[range(4),range(2),range(3),range(3),range(3),range(2),range(5),range(2),
     range(2),range(2),range(2),range(2),range(3),range(3),range(2)]
Xe,Xs,Sc,IC,Uo,Ug,Np,Na,Ld,Lk,So,Sf,Dc,Dd,EO=range(15)
def close(x):
    x=list(x); g=True
    while g:
        g=False
        def rz(i,v):
            nonlocal g
            if x[i]<v: x[i]=v; g=True
        if x[Xe]>=3: rz(Np,2); rz(Na,1)
        if x[Sc]>=2: rz(IC,1)
        if x[Uo]>=2: rz(IC,2)
        if x[Uo]>=1: rz(Np,1)
        if x[Np]>=4: rz(Xe,1)
        if x[Ld]>=1: rz(Dd,1)
        if x[So]>=1: rz(IC,2)
        if x[Dc]>=2: rz(IC,2); rz(Ld,1); rz(Dd,2)
        if x[Dd]>=2: rz(Dc,2)
        if x[Na]>=1: rz(Np,2)
        if x[Ug]>=1: rz(Xs,1)
        if x[Lk]>=1: rz(Dd,2)
        if x[EO]>=1: rz(Ug,1)
    return tuple(x)
allc={c for c in {close(x) for x in product(*RNG)} if c[Sf]==0}
V={c for c in allc if not(c[Np]>=3 and c[Xe]==0 and c[EO]==0 and c[Ug]<1)}
o=close(tuple([0,0,1,0,0,0,1,0,0,0,0,0,0,0,0]))
CAP=[('evaporating black hole',   lambda c:c[Np]>=1),
     ('Planck-scale long wormhole',lambda c:c[Np]>=2 and c[Na]==0),
     ('macroscopic LONG wormhole',lambda c:c[Np]>=3 and c[Na]==0),
     ('macroscopic SHORT wormhole',lambda c:c[Np]>=3 and c[Na]>=1),
     ('universal horizon',        lambda c:c[Xe]>=2),
     ('time machine',             lambda c:c[Xe]>=3),
     ('trivial comm. complexity', lambda c:c[Sc]>=2),
     ('superluminal signalling',  lambda c:c[IC]>=2),
     ('information loss',         lambda c:c[Uo]>=1),
     ('ghosts',                   lambda c:c[Ug]>=1),
     ('NP-complete in P',         lambda c:c[Ld]>=1),
     ('no superposition',         lambda c:c[Lk]>=1),
     ('perfect cloning',          lambda c:c[Dc]>=2),
     ('perfect discrimination',   lambda c:c[Dd]>=2)]
PRE=[('no explicit Lorentz viol.',lambda c:c[Xe]==0),
     ('no spontaneous Lorentz viol.',lambda c:c[Xs]==0),
     ('unitary evolution (open)', lambda c:c[Uo]==0),
     ('no ghosts',                lambda c:c[Ug]==0),
     ('no signalling',            lambda c:c[IC]<2),
     ('information causality',    lambda c:c[IC]==0),
     ('microcausality (obs)',     lambda c:c[So]==0),
     ('linear dynamics',          lambda c:c[Ld]==0),
     ('linear state space',       lambda c:c[Lk]==0),
     ('the ANEC',                 lambda c:c[Np]<2),
     ('the achronal ANEC',        lambda c:c[Na]==0),
     ('second-order EOM',         lambda c:c[EO]==0)]
print('  %-28s %7s %6s %9s' % ('capability','cells','here?','minimal exclusion set size'))
for cn,cf in CAP:
    n=sum(1 for c in V if cf(c))
    best=None
    for r in range(1,4):
        hits=[]
        for combo in combinations(PRE,r):
            if not any(cf(c) and all(pf(c) for _,pf in combo) for c in V):
                hits.append(tuple(p for p,_ in combo))
        if hits: best=(r,hits); break
    sz = best[0] if best else '-'
    print('  %-28s %7d %6s %9s' % (cn,n,('YES' if cf(o) else 'no'),sz))
print()
print('  THE MACROSCOPIC LONG WORMHOLE - ITS MINIMAL EXCLUSION SETS')
cf=[f for n,f in CAP if n=='macroscopic LONG wormhole'][0]
for r in range(1,4):
    hits=[]
    for combo in combinations(PRE,r):
        if not any(cf(c) and all(pf(c) for _,pf in combo) for c in V):
            hits.append(tuple(p for p,_ in combo))
    if hits:
        print('     size %d: %d set(s)' % (r,len(hits)))
        for h in hits[:6]: print('        %s' % ' + '.join(h))
        break
    else:
        print('     size %d: none' % r)
print()
print('  CAPABILITIES REQUIRING MORE THAN ONE PRESERVATION TO EXCLUDE')
multi=[]
for cn,cf2 in CAP:
    one=[p for p,pf in PRE if not any(cf2(c) and pf(c) for c in V)]
    if not one: multi.append(cn)
print('     %s' % (', '.join(multi) if multi else 'none'))