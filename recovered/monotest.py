from itertools import product
RNG=[range(4),range(3),range(3),range(3),range(5),range(2),range(2),range(3),range(3)]
NM=['X','Sc','IC','U','NEC','L','SD','DNc','DNd']
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
V=sorted({c for c in allc if not(c[4]>=3 and not(c[2]>=2 or c[3]>=1 or c[0]>=1))})
print('  MONOTONICITY OF EVERY PAIRWISE RELATION IN THE VIOLATION INDEX')
print('  (for each ordered pair (i,j): is max{x_i : x_j = v} monotone in v?)')
bad=[]
for i in range(9):
    for j in range(9):
        if i==j: continue
        m={}
        for c in V:
            m[c[j]]=max(m.get(c[j],-99), c[i])
        seq=[m[v] for v in sorted(m)]
        if seq!=sorted(seq) and seq!=sorted(seq,reverse=True):
            bad.append((NM[i],NM[j],seq))
print('     non-monotone pairwise relations: %d' % len(bad))
for a,b,s in bad[:8]: print('        max %s given %s = %s' % (a,b,s))
print()
print('  SAME TEST ON THE 18-COLUMN PERIODIC TABLE')
occ=set()
for g in (1,18): occ.add((1,g))
for p in (2,3):
    for g in [1,2,13,14,15,16,17,18]: occ.add((p,g))
for p in (4,5,6,7):
    for g in range(1,19): occ.add((p,g))
def block18(g):
    if g in (1,2): return 0
    if 3<=g<=12: return 2
    return 1
P3={(p,g,block18(g)) for p,g in occ}
NM3=['period','group','l']
badp=[]
for i in range(3):
    for j in range(3):
        if i==j: continue
        m={}
        for c in P3: m[c[j]]=max(m.get(c[j],-99), c[i])
        seq=[m[v] for v in sorted(m)]
        if seq!=sorted(seq) and seq!=sorted(seq,reverse=True):
            badp.append((NM3[i],NM3[j],seq))
print('     non-monotone pairwise relations: %d' % len(badp))
for a,b,s in badp: print('        max %s given %s = %s' % (a,b,s))
print()
print('  THE ARITY OF EACH DEFECT')
print('     violation index : minimal support {X, U, NEC}, size 3  -> ARITY')
print('     periodic table  : l determined by group but non-monotone -> ORDERING')
print()
print('  CROSS-CHECK: does the periodic table have an arity problem too?')
print('     minimal failing subsets of (period, group, l):')
def E(X,d):
    X=set(X); vals=[sorted({c[i] for c in X}) for i in range(d)]
    def env(i,j):
        m={}
        for c in X:
            if c[i]>m.get(c[j],-99): m[c[j]]=c[i]
        b,o=-99,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    return sum(1 for x in product(*vals) if all(x[i]<=phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i!=j))-len(X)
from itertools import combinations
for r in (2,):
    for idx in combinations(range(3),r):
        S={tuple(c[i] for i in idx) for c in P3}
        print('        %-22s E = %d' % (str([NM3[i] for i in idx]), E(S,r)))
print('        %-22s E = %d' % ("['period','group','l']", E(P3,3)))