from itertools import product, combinations
AX=['rungs','exposure','lattice','conflation','measured','in-deg','out-deg']
NINE={'X':(4,8,2,2,2,2,1),'Sc':(3,4,2,0,2,0,1),'IC':(3,6,0,0,2,4,1),'U':(3,8,0,2,1,0,2),
 'NEC':(5,7,1,2,1,2,1),'L':(2,4,0,2,2,1,1),'SD':(2,5,2,2,2,0,1),
 'DNc':(3,4,0,1,2,1,3),'DNd':(3,2,0,1,2,2,1)}
X=set(NINE.values())
print('  MONOTONICITY OF THE AXIS INDEX')
bad=[]
for i in range(7):
    for j in range(7):
        if i==j: continue
        m={}
        for c in X: m[c[j]]=max(m.get(c[j],-99),c[i])
        seq=[m[v] for v in sorted(m)]
        if seq!=sorted(seq) and seq!=sorted(seq,reverse=True): bad.append((AX[i],AX[j],seq))
print('     non-monotone pairwise relations: %d of 42' % len(bad))
for a,b,s in bad[:5]: print('        max %-11s given %-11s = %s' % (a,b,s))
print()
print('     => sub-case A (ordering), not a new failure mode')
print('     unlike the periodic table, unrepairable: nine axes have no natural re-placement')
print()
print('  THE THREE OBJECTS, BY FAILURE MODE')
rows=[('Lambda_8','all monotone','arity 2','E = 0','null case'),
      ('periodic table','2 non-monotone','arity 2','E = 36','sub-case A, REPAIRED by re-placement'),
      ('violation index','all monotone (72/72)','arity 3','E = 30','sub-case B, six repairs failed'),
      ('molecular transit','-','Helly >= 5','-','sub-case B at higher arity'),
      ('axis index','%d non-monotone'%len(bad),'arity 2','E = 499','sub-case A, unrepairable, and sparse')]
print('  %-18s %-22s %-9s %-9s %s' % ('object','ordering','arity','E','verdict'))
for r in rows: print('  %-18s %-22s %-9s %-9s %s' % r)
print()
print('  DENSITY, ALL OBJECTS')
dens=[('Lambda_8',976,6912),('Lambda_13',199130,47775744),('violation index',2370,59400),
      ('periodic table',90,126),('axis index',9,5184)]
for n,c,b in dens:
    print('     %-18s %7d / %9d = %6.2f%%   %s' % (n,c,b,100*c/b,
          'E informative' if 100*c/b>1 else 'E measures sparsity'))
print()
print('  PROMOTION LEDGER')
P=[('the two failure modes (ordering / arity)',
    'PROMOTE','four objects, each demonstrated computationally; the third candidate resolved to sub-case A'),
   ('E requires density to be informative',
    'PROMOTE','measured on five objects; clean separation at roughly 1%'),
   ('audit 22 is necessary and cannot be automated',
    'PROMOTE','21 audits passed on a document containing 5 conflations; the comparison is external by construction'),
   ('five of nine coordinates are conflated',
    'PROMOTE','each shown against a named theorem with a quoted hypothesis'),
   ('the axis set is open',
    'PROMOTE','computed at nine and at fifteen; E > 0 both times'),
   ('B.3.1 as a general law about all indices',
    'HOLD','three instances, all built by me, all in one session'),
   ('pair-completion predicts missing axes',
    'HOLD','one confirmation (cosmic censorship) from six hand-chosen cases'),
   ('the four predicted axes',
    'HOLD','candidates; three have plausible occupants, none verified against the literature'),
   ('the six-vocabulary partition',
    'HOLD','mine; no source draws those lines; every count depends on it'),
   ('the defect of 30 and core of 1',
    'HOLD','computed over NINE coordinates; adding CPT or EOM order would move it')]
for a,b,c in P: print('     %-46s %-7s %s' % (a,b,c))
print()
print('     promote: %d    hold: %d' % (sum(1 for _,b,_ in P if b=='PROMOTE'),sum(1 for _,b,_ in P if b=='HOLD')))