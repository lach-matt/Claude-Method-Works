from itertools import product
NM=['CYC','MOD','NEST','ANCHOR','THETA','KILL','GEN','TRANS','COND','TRACE','GSL','QFC']
DEF=[
 ('CYC','a cyclic and separating state for the cut algebras','present wherever a Hadamard state exists'),
 ('MOD','the modular flow sigma_t','T1; follows from CYC'),
 ('NEST','cuts partially ordered by causal inclusion','needs no parametrisation'),
 ('ANCHOR','corner edge mode DATA (Gamma_0, Upsilon_0)','Ashtekar NEH structure supplies it'),
 ('THETA','the expansion is NONZERO','a property of the surface'),
 ('KILL','a Killing field tangent to the horizon','a property of the surface'),
 ('GEN','the corner translation charge P_alpha is nonzero',
  'P_alpha proportional to L_l mu = Theta mu.  Theta = 0  =>  P_alpha = 0'),
 ('TRANS','a positive-generator translation U(a)','T2; iff half-sided modular inclusion'),
 ('COND','conditioning on a sharp corner location','reduces the group to R for T3'),
 ('TRACE','a semifinite trace, hence an entropy','T3+T4'),
 ('GSL','d/du S_gen >= 0','monotonicity of tau under unitary nesting'),
 ('QFC','d2/du2 S_gen <= 0','GSL + the Borchers relation'),
]
CY,MO,NE,AN,TH,KI,GE,TR,CO,TA,GS,QF=range(12)
def close(x):
    x=list(x); g=True
    while g:
        g=False
        def off(i):
            nonlocal g
            if x[i]==0: x[i]=1; g=True
        # structural implications, all one-directional
        if x[CY]==1: off(MO)                       # no state, no modular flow
        if x[KI]==0 and x[TH]==0: pass             # Killing horizons ARE non-expanding: consistent
        if x[KI]==0: 
            if x[TH]==0: pass
        if x[TH]==1: off(GE)                       # Theta = 0  =>  P_alpha = 0
        if x[AN]==1: off(GE); off(CO)              # no corner data, no charge and no conditioning
        if x[GE]==1 and x[KI]==1: off(TR)          # neither route to the translation
        if x[MO]==1 or x[CO]==1: off(TA)           # no trace without the modular crossed product
        if x[TR]==1 or x[TA]==1 or x[NE]==1: off(GS)
        if x[GS]==1 or x[TR]==1: off(QF)
    return tuple(x)
def E(S,d):
    S=set(S); vals=[sorted({c[i] for c in S}) for i in range(d)]
    ph={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            m={}
            for c in S:
                if c[i]>m.get(c[j],-99): m[c[j]]=c[i]
            b,o=-99,{}
            for t in sorted(m): b=max(b,m[t]); o[t]=b
            ph[(i,j)]=o
    return sum(1 for x in product(*vals) if all(x[i]<=ph[(i,j)][x[j]] for i in range(d) for j in range(d) if i!=j))-len(S)
V={close(c) for c in {close(x) for x in product(*[range(2)]*12)}}
print('  THE INGREDIENT INDEX, REDEFINED')
print('  0 = present / holds,  1 = absent / fails')
print()
for a,b,c in DEF: print('     %-7s %-46s %s' % (a,b,c))
print()
print('  EDGES')
for e in ['CYC absent    -> MOD absent',
          'THETA = 0     -> GEN absent          (P_alpha vanishes on a non-expanding horizon)',
          'ANCHOR absent -> GEN and COND absent',
          'GEN absent AND KILL absent -> TRANS absent    (both known routes)',
          'MOD or COND absent -> TRACE absent',
          'TRANS, TRACE or NEST absent -> GSL absent',
          'GSL or TRANS absent -> QFC absent']:
    print('     %s' % e)
print()
print('  cells %d of %d   E = %d' % (len(V),2**12,E(V,12)))
print()
print('  THE MAP')
def mk(**kw):
    x=[0]*12
    for k,v in kw.items(): x[NM.index(k)]=v
    return close(tuple(x))
CASES=[
 ('Rindler / Killing horizon',        mk(THETA=1),          'Theta = 0, Killing present'),
 ('perturbed Killing horizon',        mk(),                 'Theta = O(eps) nonzero, Killing approx'),
 ('ISOLATED HORIZON (exact NEH)',     mk(THETA=1,KILL=1),   'Theta = 0 exactly, NO Killing'),
 ('expanding null surface, no Killing',mk(KILL=1),          'Theta nonzero, no Killing'),
 ('finite causal diamond lightsheet', mk(KILL=1),           'expanding/contracting: Theta nonzero'),
 ('bare null hypersurface',           mk(THETA=1,KILL=1,ANCHOR=1),'no corner structure'),
]
print('  %-36s %s' % ('surface',' '.join('%-6s'%n for n in NM)))
for n,c,note in CASES:
    print('  %-36s %s' % (n,' '.join('%-6d'%v for v in c)))
print()
print('  %-36s %-8s %-8s %-8s %s' % ('surface','TRANS','TRACE','GSL','note'))
for n,c,note in CASES:
    f=lambda i:'yes' if c[i]==0 else 'NO'
    print('  %-36s %-8s %-8s %-8s %s' % (n,f(TR),f(TA),f(GS),note))
print()
print('  THE RESULT')
blocked=[n for n,c,_ in CASES if c[TR]==1]
print('     surfaces with TRANS blocked: %s' % ', '.join(blocked))
print()
print('     the gap is NOT a broad region. it is the corner where')
print('        Theta = 0 exactly   AND   no Killing field.')
print('     Theta nonzero  -> the corner charge is nonzero -> a route exists.')
print('     Killing present -> the Killing parameter supplies it directly.')
print('     only the exactly-non-expanding non-Killing case has neither.')
print()
print('  AND THE ENTROPY SURVIVES THERE')
c=mk(THETA=1,KILL=1)
print('     isolated horizon:  TRACE %s,  GSL %s,  QFC %s'
      % ('yes' if c[TA]==0 else 'NO','yes' if c[GS]==0 else 'NO','yes' if c[QF]==0 else 'NO'))
print('     -> an entropy at each cut, and no law relating them.')