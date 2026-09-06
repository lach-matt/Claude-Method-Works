from itertools import product
from collections import Counter
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
o=close((0,1,0,0,1,0,0,0,0))
print('  GUARANTEED-PAULI REGION, TWO READINGS')
withU=[c for c in V if c[X_]==0 and c[SD_]==0 and c[U_]==0]
noU  =[c for c in V if c[X_]==0 and c[SD_]==0]
print('     including U=0 as a hypothesis (last turn) : %4d of %d  (%.1f%%)' % (len(withU),len(V),len(withU)/len(V)*100))
print('     CORRECTED, U not a hypothesis             : %4d of %d  (%.1f%%)' % (len(noU),len(V),len(noU)/len(V)*100))
print('     difference                                : %4d cells' % (len(noU)-len(withU)))
print('     our cell in both: %s / %s' % (o in withU, o in noU))
print()
print('     the extra cells have U =', sorted({c[U_] for c in noU if c not in withU}))
print('     i.e. Lindblad or locality-breaking non-unitarity with Lorentz invariance and microcausality intact')
print()
print('  WHICH SPIN-STATISTICS HYPOTHESES ARE INDEXABLE, CORRECTED')
rows=[('Lorentz invariance',       'X = 0',   'YES'),
      ('spacelike commutativity',  'SD = 0',  'YES'),
      ('positive-definite metric', 'no ghosts','NO - not a coordinate; U=1 is CPTP and preserves it'),
      ('vacuum is lowest energy',  '-',       'NO'),
      ('vacuum not annihilated',   '-',       'NO')]
for a,b,c in rows: print('     %-26s %-11s %s' % (a,b,c))
print()
print('     indexable: 2 of 5 hypotheses; plus Sc>=3 breaking the conclusion directly')
print('     coordinates with demonstrated lattice action: X, Sc, SD  = 3 of 9')
print()
print('  P4 : U >= 1 -> X >= 1')
print('     ghosts (indefinite metric)   : supported - Lorentz invariance must break spontaneously')
print('     Lindblad (U = 1 in this index): NOT supported - CPTP on a positive-definite space')
print('     verdict: FALSE as stated on this axis; the true statement is about a rung the axis lacks')
print()
print('  P6 : NEC>=3 -> SD      single disjunct of Hartman  -> not assertable')
print('  P7 : NEC>=3 -> IC=2    single disjunct of Hartman  -> not assertable')
print()
print('  ALL SEVEN PROPOSITIONS, FINAL')
final=[('P1','X>=1 -> U>=1','REFUTED - ordinary second law survives Lorentz violation'),
       ('P2','NEC>=3 -> X>=1','REFUTED - Buniy scoped to Lorentz-invariant theories'),
       ('P3','U>=1 -> IC=2','REFUTED - the U=1 rung is occupied, operators computed'),
       ('P4','U>=1 -> X>=1','FALSE on this axis - true only for ghosts, which are not a rung'),
       ('P5','NEC>=3 -> U>=1','CONDITIONAL - flat space proven, curved conjectural'),
       ('P6','NEC>=3 -> SD','NOT ASSERTABLE - single disjunct'),
       ('P7','NEC>=3 -> IC=2','NOT ASSERTABLE - single disjunct')]
for a,b,c in final: print('     %-3s %-16s %s' % (a,b,c))