from itertools import product, combinations
print('  V5  COUPLING  -- is it one term?')
print()
XI=[('minimal',        'xi = 0',       'Kontou-Olum, Wall (GSL): ANEC proved here'),
    ('conformal',      'xi = 1/6 (4d)','Urban-Olum: ANEC VIOLATED in conformally flat spacetime'),
    ('general non-min','xi arbitrary', 'Fewster: state-independent QEIs can FAIL here'),
    ('improved / other','xi < 0 etc',  'no result located')]
print('  %-18s %-16s %s' % ('rung','parameter','status of the ANEC'))
for a,b,c in XI: print('  %-18s %-16s %s' % (a,b,c))
print()
print('  -> V5 is NOT a single term. it is a graded axis with at least three rungs,')
print('     and the ANEC changes truth value across them. filing it as one term was wrong.')
print()
NM5=['XI','STATEIND']
# XI 0 minimal 1 conformal 2 general non-minimal
# STATEIND 0 state-independent QEI available / 1 not
R5=[range(3),range(2)]
def close5(x):
    x=list(x)
    if x[0]>=1 and x[1]<1: x[1]=1     # non-minimal: state-independent QEIs can fail (Fewster)
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
V5={close5(x) for x in product(*R5)}
e,ex,box=E(V5,2,ret=True)
print('  V5 as a two-letter index: cells %d, box %d, E = %d -> %s'
      % (len(V5),box,e,'CLOSED' if e==0 else 'OPEN'))
print()
print('  V4  ALGEBRA  -- a provenance audit before any construction')
print()
SRC=[('determinism',            'Wall, GSL proof axioms',            'GSL programme'),
     ('ultralocality',          'Wall, GSL proof axioms',            'GSL programme'),
     ('stability',              'Wall, GSL proof axioms',            'GSL programme'),
     ('vacuum is lowest energy','Luders-Zumino spin-statistics',     'spin-statistics programme'),
     ('vacuum not annihilated', 'Luders-Zumino spin-statistics',     'spin-statistics programme'),
     ('CPT',                    'Wall, stated auxiliary assumption', 'GSL programme'),
     ('renormalisation scheme for generalised entropy',
                                'Wall, stated auxiliary assumption', 'GSL programme')]
print('  %-46s %-34s %s' % ('term','source','programme'))
for a,b,c in SRC: print('  %-46s %-34s %s' % (a,b,c))
from collections import Counter
prog=Counter(c for _,_,c in SRC)
print()
print('  programmes represented: %s' % dict(prog))
print('  -> V4 as I defined it merges terms from TWO unrelated programmes.')
print('     they share only that both are conditions on the algebra of observables.')
print('     that is my grouping, not anyone else\'s, and it is the weakest link')
print('     in the vocabulary partition (already on the HOLD list).')
print()
print('  WHAT A HONEST PARTITION WOULD DO')
print('     split V4 into V4a (GSL axioms) and V4b (Wightman/spin-statistics axioms).')
print('     consequences for the system graph:')
print('        Wall spans V1 + V4a + V5      (3 vocabularies, unchanged)')
print('        spin-statistics spans V1 + V4b (2, unchanged)')
print('        but V4a and V4b are now separate NODES, so:')
print('           nodes 7 -> 8')
print('           edges: Wall gives V1-V4a, V1-V5, V4a-V5 ; spin-stat gives V1-V4b')
print('        Wall still triangulates. the second cycle survives the split.')
print()
print('  AND CPT IS MISSING FROM THE ALPHABET ENTIRELY')
print('     Wall lists CPT as an auxiliary assumption of the ANEC-from-GSL derivation.')
print('     Greenberg gives CPT violation -> Lorentz violation, an EDGE into X_exp.')
print('     so CPT is BOTH a V4a hypothesis AND a would-be V1 letter.')
print('     it is the one term identified that belongs to two vocabularies at once.')
print()
print('  TALLY OF THE VOCABULARIES, HONESTLY')
ROWS=[('V1 laws','15 letters','BUILT','E = 816, arity 3, OPEN'),
      ('V2 theory','4 terms','sourced','2 of 4 shown non-operative'),
      ('V3 geometry','5 letters','BUILT','E = 0, CLOSED'),
      ('V4 algebra','7 terms','UNSOUND','merges two programmes; should split'),
      ('V5 coupling','2 letters','BUILT','E = 0, CLOSED; NOT a single term'),
      ('V6 solution','4 letters','BUILT','E = 0, CLOSED; carries the conjecture'),
      ('V7 degeneracy','1 term','trivial','non-degenerate higher-derivative')]
print('  %-14s %-12s %-10s %s' % ('vocabulary','size','status','note'))
for r in ROWS: print('  %-14s %-12s %-10s %s' % r)