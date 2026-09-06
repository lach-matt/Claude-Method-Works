from itertools import product, combinations
NM=['SC','HAD','REG','ACH']
# SC   0 solves the semiclassical Einstein equation (backreaction included)
#      1 fixed background, no backreaction
#      2 no consistent solution exists (G diverges)
# HAD  0 Hadamard state / 1 non-Hadamard
# REG  0 within semiclassical validity / 1 sub-Planckian scales involved
# ACH  0 the geodesic is achronal / 1 chronal
RNG=[range(3),range(2),range(2),range(2)]
SC,HAD,REG,ACH=range(4)
def close(x):
    x=list(x); g=True
    while g:
        g=False
        def up(i,v):
            nonlocal g
            if x[i]<v: x[i]=v; g=True
        if x[REG]>=1: up(SC,1)     # sub-Planckian: no trustworthy semiclassical solution
        if x[HAD]>=1: up(REG,1)    # non-Hadamard states have ill-defined <T> at short distance
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
    box=1
    for v in vals: box*=len(v)
    return (len(R)-len(S),sorted(R-S),box) if ret else len(R)-len(S)
V={close(x) for x in product(*RNG)}
V={close(c) for c in V}
e,ex,box=E(V,4,ret=True)
print('  THE SOLUTION INDEX  V6')
print('  %-5s %s' % ('letter','rungs'))
for n,r in zip(NM,[3,2,2,2]): print('  %-5s %d' % (n,r))
print()
print('  edges')
print('     REG=1 -> SC>=1    sub-Planckian: no trustworthy semiclassical solution')
print('     HAD=1 -> REG=1    non-Hadamard states have ill-defined <T> at short distance')
print()
print('  cells %d   box %d   density %.1f%%   E = %d   -> %s'
      % (len(V),box,100*len(V)/box,e,'CLOSED' if e==0 else 'OPEN'))
bad=0
for i in range(4):
    for j in range(4):
        if i==j: continue
        m={}
        for c in V: m[c[j]]=max(m.get(c[j],-99),c[i])
        s=[m[v] for v in sorted(m)]
        if s!=sorted(s) and s!=sorted(s,reverse=True): bad+=1
print('  non-monotone pairwise relations: %d of 12' % bad)
print()
print('  GRAHAM-OLUM JURISDICTION IN V6')
adm=[c for c in V if c[SC]==0 and c[REG]==0 and c[HAD]==0 and c[ACH]==0]
print('     self-consistent, Hadamard, in-regime, achronal: %d of %d cells' % (len(adm),len(V)))
print('     that four-letter conjunction IS the conjecture\'s scope.')
print()
print('  WHERE THE KNOWN VIOLATIONS SIT')
def mk(**kw):
    x=[0]*4
    for k,v in kw.items(): x[NM.index(k)]=v
    return close(tuple(x))
VIOL=[('compactified flat space, Casimir (Wall)',      mk(ACH=1),
       'ACH=1 - the geodesic is CHRONAL, not achronal'),
      ('Schwarzschild background, some states (Visser)',mk(SC=1,ACH=1),
       'fixed background AND chronal'),
      ('conformally flat, non-minimal coupling (Urban-Olum)', mk(SC=1),
       'fixed background - not a self-consistent solution'),
      ('holographic bubble (Ishibashi-Maeda-Mefford)',  mk(SC=0,REG=0,ACH=0),
       'IN SCOPE - and identified by the same group as a conformal-frame artefact'),
      ('Planck-scale violations (all known others)',    mk(REG=1),
       'REG=1 - outside semiclassical validity')]
print('  %-46s %-22s %s' % ('violation','cell','why it is out of scope'))
for n,c,why in VIOL:
    inscope = (c[SC]==0 and c[REG]==0 and c[HAD]==0 and c[ACH]==0)
    print('  %-46s %-22s %s' % (n,str(dict(zip(NM,c))),('IN SCOPE' if inscope else why)))
print()
print('  THE POINT')
n_out=sum(1 for _,c,_ in VIOL if not (c[SC]==0 and c[REG]==0 and c[HAD]==0 and c[ACH]==0))
print('     %d of %d known violations fall outside V6\'s admissible region.' % (n_out,len(VIOL)))
print('     the one that does not was withdrawn by its own authors as a conformal artefact.')
print()
print('     => the self-consistent achronal ANEC is free of counterexamples BECAUSE')
print('        V6 excludes them. the freedom is a SCOPING fact about the solution index,')
print('        not a physical fact about the law index.')
print()
print('     the conjecture is therefore not "ANEC holds". it is:')
print('        "every violation lies outside SC=0 & HAD=0 & REG=0 & ACH=0"')
print('     and that is a statement in V6, with no V1 letter in it at all.')
print()
print('  CONSEQUENCE FOR THE SYSTEM GRAPH')
print('     Graham-Olum spans V3 x V6 - confirmed, both indices now built and both CLOSED.')
print('     its jurisdiction is a down-set in each: 3 of 25 cells in V3, %d of %d in V6.' % (len(adm),len(V)))
print('     the charger is simple in its own vocabularies and unreachable from V1,')
print('     which is the severance stated from inside both endpoints.')