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
        if x[Xe]>=3: rz(Np,2); rz(Na,1)          # chronology needs ANEC and achronal violation
        if x[Sc]>=2: rz(IC,1)
        if x[Uo]>=2: rz(IC,2)
        if x[Uo]>=1: rz(Np,1)
        if x[Np]>=4: rz(Xe,1)
        if x[Ld]>=1: rz(Dd,1)
        if x[So]>=1: rz(IC,2)
        if x[Dc]>=2: rz(IC,2); rz(Ld,1); rz(Dd,2)
        if x[Dd]>=2: rz(Dc,2)
        if x[Na]>=1: rz(Np,2)                    # achronal violation implies ANEC violation
        if x[Ug]>=1: rz(Xs,1)                    # ghosts require spontaneous Lorentz breaking (Sbisa)
        if x[Lk]>=1: rz(Dd,2)                    # no superposition -> perfect discrimination
        if x[EO]>=1: rz(Ug,1)                    # Ostrogradsky (degenerate cases excepted - see note)
    return tuple(x)
def E(S,d,ret=False,cap=3_000_000):
    S=set(S); vals=[sorted({c[i] for c in S}) for i in range(d)]
    box=1
    for v in vals: box*=len(v)
    def env(i,j):
        m={}
        for c in S:
            if c[i]>m.get(c[j],-99): m[c[j]]=c[i]
        b,o=-99,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    tot=0; ex=[]; cur=[None]*d
    def rec(i):
        nonlocal tot
        if i==d:
            tot+=1
            if ret:
                t=tuple(cur)
                if t not in S: ex.append(t)
            return
        for v in vals[i]:
            ok=True
            for j in range(i):
                if v>phi[(i,j)][cur[j]] or cur[j]>phi[(j,i)][v]: ok=False; break
            if ok:
                cur[i]=v; rec(i+1)
        cur[i]=None
    rec(0)
    return (tot-len(S), ex, box) if ret else tot-len(S)
allc={close(x) for x in product(*RNG)}
print('  closed cells (15 letters): %d' % len(allc))
# SD_field = 1 marks a non-theory: excluded
allc={c for c in allc if c[Sf]==0}
print('  after removing SD_field=1 (Burgoyne: no such theory): %d' % len(allc))
# Buniy: jurisdicted forcing, single currency
V={c for c in allc if not(c[Np]>=3 and c[Xe]==0 and c[EO]==0 and c[Ug]<1)}
e,ex,box=E(V,15,ret=True)
print()
print('  THE FIFTEEN-LETTER INDEX')
print('     cells %d   ambient box %d   density %.2f%%   E = %d' % (len(V),box,100*len(V)/box,e))
core={(c[Xe],c[Uo],c[Ug],c[Np],c[Na],c[EO]) for c in ex}
print('     core (X_exp,U_open,U_ghost,NEC_pt,NEC_ach,EOM): %d distinct' % len(core))
for k in sorted(core)[:6]: print('        %s' % str(k))
print()
o=close(tuple([0,0,1,0,0,0,1,0,0,0,0,0,0,0,0]))
print('  our cell: %s' % str(o))
print('     admissible: %s' % (o in V))
print()
print('  KNOWN SOLUTIONS')
def mk(**kw):
    x=[0]*15; x[Sc]=1; x[Np]=1
    for k,v in kw.items(): x[NM.index(k)]=v
    return close(tuple(x))
CASES=[('us',mk()),
       ('MMP long wormhole',mk(NEC_pt=2)),
       ('macroscopic long wormhole',mk(NEC_pt=3)),
       ('macroscopic short wormhole',mk(NEC_pt=3,NEC_ach=1)),
       ('ghost condensate',mk(X_spon=1,EOM=1,NEC_pt=2)),
       ('time machine',mk(X_exp=3))]
exs=set(ex)
for n,c in CASES:
    st='ADMISSIBLE' if c in V else ('BLIND SPOT' if c in exs else 'closed away')
    print('     %-28s %s' % (n,st))
print()
print('  BUNIY IN THE NEW ALPHABET')
print('     NEC_pt >= 3  AND  X_exp = 0  AND  EOM = 2nd-order  ->  U_ghost = 1')
print('     trigger 1 letter, jurisdiction 2 letters, currency 1 letter -> ARITY 4')
print('     it is a FORCING, not a disjunction: the currency is single')
print()
print('  NOTE ON OSTROGRADSKY')
print('     EOM=1 -> U_ghost=1 holds for NON-DEGENERATE higher-derivative theories.')
print('     Galileons are degenerate and escape. Degeneracy is not a letter.')
print('     -> a jurisdiction condition outside the alphabet, exactly as before.')