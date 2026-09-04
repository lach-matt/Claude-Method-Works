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
# (name, test, axes it lives on)
CAP=[('evaporating black hole',   lambda c:c[Np]>=1,{Np}),
     ('Planck-scale long wormhole',lambda c:c[Np]>=2 and c[Na]==0,{Np,Na}),
     ('macroscopic LONG wormhole',lambda c:c[Np]>=3 and c[Na]==0,{Np,Na}),
     ('macroscopic SHORT wormhole',lambda c:c[Np]>=3 and c[Na]>=1,{Np,Na}),
     ('universal horizon',        lambda c:c[Xe]>=2,{Xe}),
     ('time machine',             lambda c:c[Xe]>=3,{Xe}),
     ('trivial comm. complexity', lambda c:c[Sc]>=2,{Sc}),
     ('superluminal signalling',  lambda c:c[IC]>=2,{IC}),
     ('information loss',         lambda c:c[Uo]>=1,{Uo}),
     ('ghosts',                   lambda c:c[Ug]>=1,{Ug}),
     ('NP-complete in P',         lambda c:c[Ld]>=1,{Ld}),
     ('no superposition',         lambda c:c[Lk]>=1,{Lk}),
     ('perfect cloning',          lambda c:c[Dc]>=2,{Dc}),
     ('perfect discrimination',   lambda c:c[Dd]>=2,{Dd})]
PRE=[('no explicit Lorentz viol.',lambda c:c[Xe]==0,{Xe}),
     ('no spontaneous Lorentz viol.',lambda c:c[Xs]==0,{Xs}),
     ('unitary (open-system)',    lambda c:c[Uo]==0,{Uo}),
     ('no ghosts',                lambda c:c[Ug]==0,{Ug}),
     ('no signalling',            lambda c:c[IC]<2,{IC}),
     ('information causality',    lambda c:c[IC]==0,{IC}),
     ('microcausality (obs)',     lambda c:c[So]==0,{So}),
     ('linear dynamics',          lambda c:c[Ld]==0,{Ld}),
     ('linear state space',       lambda c:c[Lk]==0,{Lk}),
     ('the ANEC',                 lambda c:c[Np]<2,{Np}),
     ('the achronal ANEC',        lambda c:c[Na]==0,{Na}),
     ('second-order EOM',         lambda c:c[EO]==0,{EO})]
print('  CROSS-AXIS EXCLUSION ONLY (same-axis preservations dropped as tautological)')
print('  %-28s %8s %7s  minimal cross-axis exclusion set' % ('capability','cells','here?'))
for cn,cf,cax in CAP:
    n=sum(1 for c in V if cf(c))
    pool=[(p,pf) for p,pf,pax in PRE if not (pax & cax)]
    best=None
    for r in range(1,4):
        hits=[]
        for combo in combinations(pool,r):
            if not any(cf(c) and all(pf(c) for _,pf in combo) for c in V):
                hits.append(tuple(p for p,_ in combo))
        if hits: best=(r,hits); break
    if best:
        print('  %-28s %8d %7s  size %d : %s' % (cn,n,('YES' if cf(o) else 'no'),best[0],
              ' | '.join(' + '.join(h) for h in best[1][:2])))
    else:
        print('  %-28s %8d %7s  none of size <= 3' % (cn,n,('YES' if cf(o) else 'no')))
print()
print('  THE MACROSCOPIC LONG WORMHOLE, IN DETAIL')
cf=[f for n,f,a in CAP if n=='macroscopic LONG wormhole'][0]
cax={Np,Na}
pool=[(p,pf) for p,pf,pax in PRE if not (pax & cax)]
for r in (1,2,3):
    hits=[tuple(p for p,_ in combo) for combo in combinations(pool,r)
          if not any(cf(c) and all(pf(c) for _,pf in combo) for c in V)]
    print('     size %d: %d set(s)  %s' % (r,len(hits),
          '; '.join(' + '.join(h) for h in hits[:3]) if hits else ''))
    if hits: break
print()
print('  HOW MANY CELLS SURVIVE EACH SINGLE PRESERVATION')
for p,pf,pax in PRE:
    if pax & cax: continue
    n=sum(1 for c in V if cf(c) and pf(c))
    print('     macroscopic long wormhole + %-30s : %5d' % (p,n))