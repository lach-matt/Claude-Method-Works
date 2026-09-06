from itertools import product, combinations
NM=['FLAT','CONN','HYP','GEN','ASYM']
# FLAT 0 exactly flat, 1 asymptotically flat, 2 curved/compact
# CONN 0 simply connected, 1 not
# HYP  0 globally hyperbolic, 1 not
# GEN  0 generic condition holds, 1 fails
# ASYM 0 has an asymptotic region, 1 spatially compact (no infinity)
RNG=[range(3),range(2),range(2),range(2),range(2)]
FLAT,CONN,HYP,GEN,ASYM=range(5)
EDGES=[
 ('FLAT=0 -> CONN=0',      lambda x: x[FLAT]==0, CONN, 0, 'exactly flat space is simply connected'),
 ('FLAT=0 -> HYP=0',       lambda x: x[FLAT]==0, HYP,  0, 'Minkowski is globally hyperbolic'),
 ('FLAT=0 -> GEN=0',       lambda x: x[FLAT]==0, GEN,  0, 'flat space satisfies the generic condition trivially'),
 ('FLAT=0 -> ASYM=0',      lambda x: x[FLAT]==0, ASYM, 0, 'Minkowski is spatially non-compact'),
 ('CONN=1 -> FLAT>=1',     lambda x: x[CONN]>=1, FLAT, 1, 'a handle requires curvature'),
 ('HYP=1  -> FLAT>=1',     lambda x: x[HYP]>=1,  FLAT, 1, 'loss of global hyperbolicity requires curvature'),
 ('ASYM=1 -> FLAT>=2',     lambda x: x[ASYM]>=1, FLAT, 2, 'spatially compact is not asymptotically flat'),
]
def close(x):
    x=list(x); g=True
    while g:
        g=False
        for lab,trig,ci,cv,why in EDGES:
            if trig(x):
                if cv==0 and x[ci]>cv: x[ci]=cv; g=True     # forcing DOWN
                if cv>0 and x[ci]<cv:  x[ci]=cv; g=True     # forcing UP
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
    return (len(R)-len(S), sorted(R-S), box) if ret else len(R)-len(S)
print('  THE GEOMETRY INDEX  V3')
print('  %-6s %s' % ('letter','rungs'))
for n,r in zip(NM,[3,2,2,2,2]): print('  %-6s %d' % (n,r))
print()
print('  EDGES (all binary forcings)')
for lab,_,_,_,why in EDGES: print('     %-22s %s' % (lab,why))
print()
raw=set(product(*RNG))
V={close(x) for x in raw}
# a "forcing down" makes closure non-monotone in the usual sense; check idempotence
V={close(c) for c in V}
e,ex,box=E(V,5,ret=True)
print('  cells %d of %d raw   box %d   density %.1f%%   E = %d'
      % (len(V),len(raw),box,100*len(V)/box,e))
print('  => the geometry index is %s' % ('CLOSED' if e==0 else 'OPEN'))
if ex:
    print('  excess:')
    for t in ex[:10]: print('     ',dict(zip(NM,t)))
print()
# monotonicity
bad=[]
for i in range(5):
    for j in range(5):
        if i==j: continue
        m={}
        for c in V: m[c[j]]=max(m.get(c[j],-99),c[i])
        s=[m[v] for v in sorted(m)]
        if s!=sorted(s) and s!=sorted(s,reverse=True): bad.append((NM[i],NM[j],s))
print('  non-monotone pairwise relations: %d of 20' % len(bad))
for a,b,s in bad[:5]: print('     max %s given %s = %s' % (a,b,s))
print()
print('  MINIMAL FAILING SUBSETS')
mins=[]
for r in (2,3,4):
    found=[]
    for idx in combinations(range(5),r):
        if any(set(m)<=set(idx) for m in mins): continue
        P={tuple(c[i] for i in idx) for c in V}
        if E(P,r)>0: found.append(idx)
    for idx in found:
        if not any(set(m)<set(idx) for m in mins): mins.append(idx)
    if found:
        for idx in found:
            P={tuple(c[i] for i in idx) for c in V}
            print('     size %d  %-34s E = %d' % (r,str([NM[i] for i in idx]),E(P,r)))
        break
else:
    print('     none at any size')
print()
print('  WHERE THE OBJECTS SIT')
def mk(**kw):
    x=[0]*5
    for k,v in kw.items(): x[NM.index(k)]=v
    return close(tuple(x))
CASES=[('Minkowski',mk()),
       ('our universe (asymptotically flat)',mk(FLAT=1)),
       ('a wormhole spacetime',mk(FLAT=1,CONN=1)),
       ('a time machine',mk(FLAT=1,HYP=1)),
       ('the compact-universe counterexample',mk(FLAT=2,ASYM=1)),
       ('MMP (one asymptotic region, handle)',mk(FLAT=1,CONN=1))]
for n,c in CASES:
    print('     %-38s %-26s %s' % (n,str(dict(zip(NM,c))),'admissible' if c in V else 'EXCESS'))
print()
print('  GRAHAM-OLUM JURISDICTION IN THIS INDEX')
go=[c for c in V if c[FLAT]<=1 and c[CONN]==0 and c[ASYM]==0 and c[GEN]==0]
print('     asymptotically flat, simply connected, generic, has infinity: %d of %d cells' % (len(go),len(V)))
print('     the jurisdiction is a DOWN-SET on four of five letters, and it is expressible here.')
print('     it was not expressible in V1 at all - that is the severance, seen from the other side.')