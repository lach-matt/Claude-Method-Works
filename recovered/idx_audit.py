from itertools import product, combinations
from collections import defaultdict, Counter
P=['LEFT','RIGHT','AUTO','OUT']
# LEFT  0 document  1 index/dataset
# RIGHT 0 itself (internal)  1 a companion dataset  2 an external source
# AUTO  0 needs judgement/retrieval  1 automatable
# OUT   0 pass/fail  1 a count  2 a debt (unbounded, never "passes")
A={
 'lattice properties':      (1,0,1,0), 'equation reproduction':  (0,1,1,0),
 'internal consistency':    (0,0,1,0), 'undefined terms':        (0,0,1,0),
 'encoding artefacts':      (0,0,1,0), 'coherence':              (0,0,1,0),
 'attribution':             (0,0,1,0), 'figure coverage':        (0,0,1,0),
 'distinctness':            (0,0,1,0), 'scoping':                (0,0,1,0),
 'antecedents':             (0,0,1,0), 'markup':                 (0,0,1,0),
 'dataset agreement':       (0,1,1,0), 'arithmetic':             (0,1,1,0),
 'enumeration':             (0,0,1,0), 'fidelity':               (0,1,1,0),
 'artifact measure':        (0,0,1,0), 'reproducibility':        (1,1,1,0),
 'sequence':                (0,0,1,0), 'projection':             (1,1,1,0),
 'input':                   (0,1,1,0),
 'AUDIT 22 term match':     (1,2,0,2),
}
X=set(A.values())
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
print('  THE AUDIT INDEX')
print('  letters: LEFT 0 document 1 index/dataset')
print('           RIGHT 0 itself 1 a companion dataset 2 an external source')
print('           AUTO 0 needs judgement 1 automatable')
print('           OUT  0 pass/fail 1 a count 2 a debt')
print()
print('  audits %d   distinct profiles %d' % (len(A),len(X)))
for p in sorted(X):
    who=[k for k,v in A.items() if v==p]
    print('     %s  x%-2d  %s' % (str(p),len(who),', '.join(who[:3])+('...' if len(who)>3 else '')))
print()
e,ex,box=E(X,4,ret=True)
print('  cells %d  box %d  density %.1f%%  E = %d -> %s'
      % (len(X),box,100*len(X)/box,e,'OPEN' if e else 'CLOSED'))
bad=0
for i in range(4):
    for j in range(4):
        if i==j: continue
        m={}
        for c in X: m[c[j]]=max(m.get(c[j],-99),c[i])
        s=[m[v] for v in sorted(m)]
        if s!=sorted(s) and s!=sorted(s,reverse=True): bad+=1
print('  non-monotone pairwise relations: %d of 12' % bad)
print()
print('  THE CLUSTERING')
cnt={i:Counter(c[i] for c in A.values()) for i in range(4)}
for i,p in enumerate(P):
    print('     %-6s %s' % (p, dict(sorted(cnt[i].items()))))
print()
print('     21 of 22 audits have RIGHT<=1, AUTO=1, OUT=0.')
print('     audit 22 is the sole outlier on ALL THREE.')
print()
print('  THE EMPTY DIRECTIONS')
FULL={'LEFT':range(2),'RIGHT':range(3),'AUTO':range(2),'OUT':range(3)}
obs={P[i]:sorted({c[i] for c in X}) for i in range(4)}
for p in P: print('     %-6s observed %-12s full %s' % (p,str(obs[p]),str(list(FULL[p]))))
print()
print('  WHAT IS ABSENT: the (RIGHT=2, AUTO=1) combination')
have=any(c[1]==2 and c[2]==1 for c in X)
print('     an EXTERNAL comparison that IS automatable: %s' % ('present' if have else 'ABSENT'))
print()
print('     that is a real audit and it does not exist here:')
print('        compare a computed number against a PUBLISHED value.')
print('        e.g. 976 cells against a chemistry reference; the 1654/2535/13585 tower')
print('        against spectroscopic tables; the density figures against term counts.')
print('        external, mechanical, and it would have caught a wrong lattice.')
print()
print('  AND (RIGHT<=1, OUT=2): an INTERNAL debt')
have2=any(c[1]<=1 and c[3]==2 for c in X)
print('     an internal comparison producing a DEBT rather than a pass: %s'
      % ('present' if have2 else 'ABSENT'))
print()
print('     also real and also absent:')
print('        count the claims in the paper with no computation behind them.')
print('        the register logs 15 corrections; NOTHING audits whether it is complete.')
print()
print('  SO THE SUITE HAS THREE BLIND SPOTS, NOT ONE')
print('     1  external + judgement  -> audit 22, term match. IDENTIFIED, unfillable by code.')
print('     2  external + mechanical -> checking computed values against published ones. MISSING.')
print('     3  internal + debt       -> counting unbacked claims. MISSING.')
print()
print('     the paper says audit 22 is the gap. it is one of three,')
print('     and the other two ARE automatable, which makes them cheaper to fix')
print('     and worse to have left out.')