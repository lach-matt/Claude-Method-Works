from itertools import product, combinations
from collections import defaultdict
P=['GEOM','FIELD','COUP','BACK']
# GEOM  0 flat  1 maximally symmetric (dS/AdS)  2 general curved
# FIELD 0 free  1 interacting / strongly coupled
# COUP  0 minimal  1 non-minimal
# BACK  0 fixed background  1 self-consistent / backreacting
RNG=[range(3),range(2),range(2),range(2)]
PROOFS={
 'Klinkhammer / Wald-Yurtsever':   [(0,0,0,0)],
 'Faulkner-Leigh-Parrikar-Wang':   [(0,0,0,0),(0,1,0,0)],
 'Hartman-Kundu-Tajdini':          [(0,1,0,0)],
 'Kelly-Wall (holographic)':       [(0,1,0,0)],
 'Rosso (dS/AdS)':                 [(1,0,0,0),(1,1,0,0)],
 'Kontou-Olum (null-proj QI)':     [(2,0,0,0)],
 'Wall (from the GSL)':            [(2,0,0,1),(2,1,0,1)],
 'Iizuka-Ishibashi-Maeda (CANEC)': [(2,1,0,0)],
}
COV=set()
for k,v in PROOFS.items(): COV|=set(v)
BOX=set(product(*RNG))
print('  THE ANEC PROOF INDEX')
print('  axes: %s' % ', '.join(P))
print('  total cases %d   covered %d   uncovered %d   coverage %.1f%%'
      % (len(BOX),len(COV),len(BOX)-len(COV),100*len(COV)/len(BOX)))
print()
print('  %-34s %s' % ('proof','cases'))
for k,v in PROOFS.items(): print('  %-34s %s' % (k,v))
print()
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
e,ex,box=E(COV,4,ret=True)
print('  COVERED SET AS AN INDEX')
print('     cells %d   box %d   density %.1f%%   E = %d  -> %s'
      % (len(COV),box,100*len(COV)/box,e,'OPEN' if e else 'CLOSED'))
if ex:
    print('     EXCESS - cases the envelope reaches and no proof covers:')
    for t in ex:
        print('        GEOM=%d FIELD=%d COUP=%d BACK=%d   %s' % (t+(
          'curved, ' if t[0]==2 else ('max-symmetric, ' if t[0]==1 else 'flat, '),)))
print()
bad=0
for i in range(4):
    for j in range(4):
        if i==j: continue
        m={}
        for c in COV: m[c[j]]=max(m.get(c[j],-99),c[i])
        s=[m[v] for v in sorted(m)]
        if s!=sorted(s) and s!=sorted(s,reverse=True): bad+=1
print('  non-monotone pairwise relations: %d of 12' % bad)
mins=[]
for r in (2,3,4):
    found=[]
    for idx in combinations(range(4),r):
        if any(set(m)<=set(idx) for m in mins): continue
        Pj={tuple(c[i] for i in idx) for c in COV}
        if E(Pj,r)>0: found.append(idx)
    for idx in found:
        if not any(set(m)<set(idx) for m in mins): mins.append(idx)
    if found:
        for idx in found:
            Pj={tuple(c[i] for i in idx) for c in COV}
            print('  minimal failing subset size %d: %-30s E = %d' % (r,str([P[i] for i in idx]),E(Pj,r)))
        break
else:
    print('  no failing subset at any size')
print()
print('  THE ARTICULATION CLAIM')
curved=[c for c in COV if c[0]==2]
print('     curved-space cases covered: %d' % len(curved))
for c in sorted(curved): print('        GEOM=2 FIELD=%d COUP=%d BACK=%d' % c[1:])
allmin=all(c[2]==0 for c in curved)
print('     every curved case has COUP = 0 (minimal): %s' % allmin)
free=[c for c in curved if c[1]==0]
print('     curved AND free: %d;  curved AND interacting: %d' % (len(free),len(curved)-len(free)))
print()
print('     NON-MINIMAL COUPLING IS COVERED NOWHERE: %s' % (not any(c[2]==1 for c in COV)))
print('     -> COUP = 1 is not an articulation point. it is a WALL.')
print('        the entire half-box COUP = 1 (%d cases) has no proof at all.' % sum(1 for c in BOX if c[2]==1))
print()
print('  WHAT THE UNCOVERED CASES ARE')
unc=sorted(BOX-COV)
byc=defaultdict(list)
for c in unc: byc[c[2]].append(c)
print('     COUP = 0 (minimal), uncovered: %d' % len(byc[0]))
for c in byc[0]: print('        GEOM=%d FIELD=%d BACK=%d' % (c[0],c[1],c[3]))
print('     COUP = 1 (non-minimal), uncovered: %d  - the whole half' % len(byc[1]))
print()
print('  CROSS-CHECK: the known counterexamples')
print('     Urban-Olum: conformally flat, NON-MINIMALLY coupled scalar -> ANEC violated.')
print('     that lands in the COUP = 1 half, which no proof covers.')
print('     Fewster: state-independent QEIs "can even fail in the nonminimally coupled theory".')
print('     -> the wall is not an absence of effort. it is where the condition is FALSE.')