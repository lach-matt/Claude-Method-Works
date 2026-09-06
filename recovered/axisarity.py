from itertools import product, combinations
AX=['rungs','exposure','lattice','conflation','measured','in-deg','out-deg']
NINE={'X':(4,8,2,2,2,2,1),'Sc':(3,4,2,0,2,0,1),'IC':(3,6,0,0,2,4,1),'U':(3,8,0,2,1,0,2),
 'NEC':(5,7,1,2,1,2,1),'L':(2,4,0,2,2,1,1),'SD':(2,5,2,2,2,0,1),
 'DNc':(3,4,0,1,2,1,3),'DNd':(3,2,0,1,2,2,1)}
SIX={'CPT':(2,2,2,0,2,0,1),'E-p conservation':(2,1,0,0,2,1,0),'GSL':(2,3,0,0,0,1,1),
 'EOM order':(2,2,0,0,2,0,1),'equivalence pr.':(2,1,0,0,2,0,0),'global symmetry':(2,1,0,0,1,0,0)}
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
    return sum(1 for x in product(*vals) if all(x[i]<=phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i!=j))-len(S)
def minimal_support(D):
    X=set(D.values()); mins=[]
    for r in range(2,8):
        found=[]
        for idx in combinations(range(7),r):
            P={tuple(c[i] for i in idx) for c in X}
            if E(P,r)>0: found.append(idx)
        # keep those with no failing proper subset
        for idx in found:
            if not any(set(m)<set(idx) for m in mins): mins.append(idx)
        if mins and r>=2: break
    return mins
print('  MINIMAL FAILING SUBSETS OF THE AXIS INDEX (nine axes)')
mins=minimal_support(NINE)
for idx in mins:
    P={tuple(c[i] for i in idx) for c in set(NINE.values())}
    print('     size %d  %-42s E = %d' % (len(idx), str([AX[i] for i in idx]), E(P,len(idx))))
print('     minimum size found: %d' % min(len(m) for m in mins))
print()
print('  IS {exposure, measured, out-deg} AMONG THEM?')
tgt=(AX.index('exposure'),AX.index('measured'),AX.index('out-deg'))
P={tuple(c[i] for i in tgt) for c in set(NINE.values())}
print('     %s  E = %d' % (str([AX[i] for i in tgt]), E(P,3)))
print('     is a minimal failing subset: %s' % (tgt in mins))
print()
print('  ALL SIZE-2 SUBSETS (do any fail?)')
bad2=[]
for idx in combinations(range(7),2):
    P={tuple(c[i] for i in idx) for c in set(NINE.values())}
    e=E(P,2)
    if e>0: bad2.append((idx,e))
print('     failing pairs: %d of 21' % len(bad2))
for idx,e in bad2[:6]: print('        %-34s E = %d' % (str([AX[i] for i in idx]),e))
print()
print('  THE THREE PROPERTIES, AND WHERE THE SIX SIT')
print('  %-20s %-10s %-10s %-10s  new directions' % ('axis','exposure','measured','out-deg'))
v9=[sorted({c[i] for c in set(NINE.values())}) for i in range(7)]
for n,p in SIX.items():
    newd=[]
    for a,i in (('exposure',1),('measured',4),('out-deg',6)):
        if p[i] not in v9[i]: newd.append(a)
    print('  %-20s %-10d %-10d %-10d  %s' % (n,p[1],p[4],p[6], ', '.join(newd) or 'none'))
print()
from collections import Counter
cnt=Counter()
for n,p in SIX.items():
    newd=tuple(a for a,i in (('exposure',1),('measured',4),('out-deg',6)) if p[i] not in v9[i])
    cnt[newd]+=1
print('  GROUPED BY WHICH NEW DIRECTIONS THEY OCCUPY')
for k,v in sorted(cnt.items(), key=lambda kv:-len(kv[0])):
    print('     %-34s %d axes' % (', '.join(k) or 'none - inside the observed box', v))