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
def E(S,d):
    S=set(S); vals=[sorted({c[i] for c in S}) for i in range(d)]
    def env(i,j):
        m={}
        for c in S:
            if c[i]>m.get(c[j],-99): m[c[j]]=c[i]
        b,o=-99,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    tot=0; cur=[None]*d
    def rec(i):
        nonlocal tot
        if i==d: tot+=1; return
        for v in vals[i]:
            ok=True
            for j in range(i):
                if v>phi[(i,j)][cur[j]] or cur[j]>phi[(j,i)][v]: ok=False; break
            if ok: cur[i]=v; rec(i+1)
        cur[i]=None
    rec(0)
    return tot-len(S)
allc={c for c in {close(x) for x in product(*RNG)} if c[Sf]==0}
V={c for c in allc if not(c[Np]>=3 and c[Xe]==0 and c[EO]==0 and c[Ug]<1)}
print('  cells %d' % len(V))
print()
print('  MINIMAL FAILING SUBSETS')
mins=[]
for r in (2,3,4):
    found=[]
    for idx in combinations(range(15),r):
        if any(set(m)<=set(idx) for m in mins): continue
        P={tuple(c[i] for i in idx) for c in V}
        if E(P,r)>0: found.append(idx)
    for idx in found:
        if not any(set(m)<set(idx) for m in mins): mins.append(idx)
    print('     size %d : %d minimal failing subsets' % (r,len(found)))
    for idx in found[:4]:
        P={tuple(c[i] for i in idx) for c in V}
        print('        %-46s E = %d' % (str([NM[i] for i in idx]), E(P,r)))
    if found: break
print()
tgt=tuple(sorted((Xe,Ug,Np,EO)))
P={tuple(c[i] for i in tgt) for c in V}
print('  {X_exp, U_ghost, NEC_pt, EOM}  E = %d   is minimal: %s'
      % (E(P,4), tgt in [tuple(sorted(m)) for m in mins]))
print()
print('  THE COLLAPSE')
def excess(S,d):
    S=set(S); vals=[sorted({c[i] for c in S}) for i in range(d)]
    def env(i,j):
        m={}
        for c in S:
            if c[i]>m.get(c[j],-99): m[c[j]]=c[i]
        b,o=-99,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    out=[]; cur=[None]*d
    def rec(i):
        if i==d:
            t=tuple(cur)
            if t not in S: out.append(t)
            return
        for v in vals[i]:
            ok=True
            for j in range(i):
                if v>phi[(i,j)][cur[j]] or cur[j]>phi[(j,i)][v]: ok=False; break
            if ok: cur[i]=v; rec(i+1)
        cur[i]=None
    rec(0)
    return out
ex=excess(V,15)
CORE=[Xe,Ug,Np,EO]; FREE=[i for i in range(15) if i not in CORE]
co={tuple(c[i] for i in CORE) for c in ex}
fr={tuple(c[i] for i in FREE) for c in ex}
print('     excess %d   core values %d   free configs %d   product %d   exact: %s'
      % (len(ex),len(co),len(fr),len(co)*len(fr),len(co)*len(fr)==len(ex)))
print('     core: %s' % sorted(co))
print()
print('  THE LATTICE MAP, NOW EXACT')
print('     spin-statistics hypotheses = X_exp=0, SD_obs=0, U_ghost=0  (three letters, no proxies)')
guar=[c for c in V if c[Xe]==0 and c[So]==0 and c[Ug]==0]
print('     guaranteed-Pauli cells: %d of %d  (%.1f%%)' % (len(guar),len(V),100*len(guar)/len(V)))
o=close(tuple([0,0,1,0,0,0,1,0,0,0,0,0,0,0,0]))
print('     our cell among them: %s' % (o in guar))
print('     lattice-acting letters: X_exp, SD_obs, U_ghost, Sc  = 4 of 15')
print('     (U_open and L_dyn now provably inert; their partners U_ghost and L_kin act)')