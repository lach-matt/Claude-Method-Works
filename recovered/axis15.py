from itertools import product
AX=['rungs','exposure','lattice','conflation','measured','in-deg','out-deg']
NINE={
 'X':(4,8,2,2,2,2,1),'Sc':(3,4,2,0,2,0,1),'IC':(3,6,0,0,2,4,1),'U':(3,8,0,2,1,0,2),
 'NEC':(5,7,1,2,1,2,1),'L':(2,4,0,2,2,1,1),'SD':(2,5,2,2,2,0,1),
 'DNc':(3,4,0,1,2,1,3),'DNd':(3,2,0,1,2,2,1)}
SIX={
 'CPT'             :(2,2,2,0,2,0,1),
 'E-p conservation':(2,1,0,0,2,1,0),
 'GSL'             :(2,3,0,0,0,1,1),
 'EOM order'       :(2,2,0,0,2,0,1),
 'equivalence pr.' :(2,1,0,0,2,0,0),
 'global symmetry' :(2,1,0,0,1,0,0)}
def RR(S,d):
    S=set(S); vals=[sorted({c[i] for c in S}) for i in range(d)]
    def env(i,j):
        m={}
        for c in S:
            if c[i]>m.get(c[j],-99): m[c[j]]=c[i]
        b,o=-99,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    return {x for x in product(*vals) if all(x[i]<=phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i!=j)}
def report(lab,D):
    X=set(D.values()); vals=[sorted({c[i] for c in X}) for i in range(7)]
    box=1
    for v in vals: box*=len(v)
    R=RR(X,7)
    print('  %-34s cells %3d  box %6d  |R| %5d  E %5d  density %6.2f%%'
          % (lab,len(X),box,len(R),len(R)-len(X),100*len(X)/box))
    return vals
print('  THE AXIS INDEX, BEFORE AND AFTER')
v9 =report('nine axes as built',NINE)
ALL=dict(NINE); ALL.update(SIX)
v15=report('plus six known-missing axes',ALL)
print()
print('  VALUE SETS, BEFORE -> AFTER')
for i,a in enumerate(AX):
    print('     %-11s %-24s -> %s' % (a,str(v9[i]),str(v15[i])))
print()
print('  DIRECTIONS THE NINE NEVER REACHED, NOW OCCUPIED')
for i,a in enumerate(AX):
    new=[x for x in v15[i] if x not in v9[i]]
    if new: print('     %-11s new values %s' % (a,new))
print()
print('  CLUSTERING: fraction of each axis-property range actually used')
for i,a in enumerate(AX):
    r9=max(v9[i])-min(v9[i])+1; r15=max(v15[i])-min(v15[i])+1
    print('     %-11s nine: %d of %d values used   fifteen: %d of %d'
          % (a,len(v9[i]),r9,len(v15[i]),r15))
print()
X15=set(ALL.values()); R15=RR(X15,7); ex=sorted(R15-X15)
print('  the fifteen-axis index is %s (E = %d)' % ('OPEN' if ex else 'CLOSED', len(ex)))
print()
print('  DENSITY AND WHETHER E IS INFORMATIVE')
for lab,n,b in [('Lambda_8',976,6912),('violation index',2370,59400),
                ('axis index, nine',9,None),('axis index, fifteen',len(X15),None)]:
    if b is None:
        D=NINE if n==9 else ALL
        vals=[sorted({c[i] for c in set(D.values())}) for i in range(7)]
        b=1
        for v in vals: b*=len(v)
    print('     %-22s %6d cells / %8d box = %6.2f%%' % (lab,n,b,100*n/b))
print()
print('     E is informative above roughly a few percent; below that it measures sparsity.')