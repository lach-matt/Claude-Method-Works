import sys; sys.path.insert(0,'/home/claude/method')
from itertools import product
import method_tower as mt
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
SS=[('Lorentz invariance', X_, 0),('microcausality', SD_, 0),('positive metric (unitarity)', U_, 0)]
print('  SPIN-STATISTICS HYPOTHESES PRESENT IN THE INDEX')
for n,i,v in SS:
    print('     %-30s coordinate %-4s  our value %d  satisfied: %s' % (n,NM[i],o[i],o[i]==v))
print('     (Sc >= 3 would break the conclusion directly; our grading tops at 2)')
print()
guar=[c for c in V if all(c[i]==v for _,i,v in SS)]
print('  UNIVERSES WITH THE PAULI LATTICE GUARANTEED')
print('     all three hypotheses hold: %d of %d  (%.1f%%)' % (len(guar),len(V),len(guar)/len(V)*100))
print('     our cell among them: %s' % (o in guar))
from collections import Counter
print('     which hypothesis fails, across the rest:')
cnt=Counter()
for c in V:
    f=tuple(n for n,i,v in SS if c[i]!=v)
    if f: cnt[f]+=1
for k,n in cnt.most_common(): print('        %-52s %5d' % (', '.join(k), n))
print()
def cap(l,m): return m*(4*l+2)
def base_m(caps,m):
    nn,ee,ll,kk,ff=caps; cells=[]
    for n in range(1,nn+1):
      for l in range(0,min(n-1,ll)+1):
        for k in range(1,min(cap(l,m),kk)+1):
          for q in range(0,k+1):
            for S2 in range(0,k+1):
              for e in range(1,ee+1):
                for f in range(0,min(e-1,ff)+1):
                  for g in range(0,min(cap(f,m),q)+1):
                    cells.append((n,l,k,q,e,f,g,S2))
    return cells
CAPS=(3,3,1,3,1)
print('  THE LATTICE, BY WHETHER SPIN-STATISTICS HOLDS')
print('     hypotheses all hold  -> Pauli forced   -> m = 1  -> |Lambda_8| = %d' % len(set(base_m(CAPS,1))))
for m in (2,3):
    print('     any hypothesis fails -> parastatistics possible -> m = %d -> |Lambda_8| = %d' % (m,len(set(base_m(CAPS,m)))))
print()
print('  THE NINE COORDINATES, BY ACTION ON THE LATTICE')
rows=[('X',   'lattice','spin-statistics hypothesis (Lorentz invariance); also the l-bound'),
      ('Sc',  'lattice','post-quantum correlation breaks the spin-statistics conclusion'),
      ('U',   'lattice','spin-statistics hypothesis (positive-definite metric)'),
      ('SD',  'lattice','spin-statistics hypothesis (spacelike commutativity)'),
      ('NEC', 'measure','shifts energies (Casimir, Lamb-type); no quantum number moves'),
      ('IC',  'none',   'concerns correlations between separated systems, not bound states'),
      ('L',   'candidate','without superposition, vector coupling has no basis - UNCOMPUTED'),
      ('DNc', 'none',   'state manipulation, not structure'),
      ('DNd', 'none',   'state manipulation, not structure')]
for n,k,why in rows: print('     %-5s %-10s %s' % (n,k,why))
print()
print('     lattice action demonstrated: 4 of 9   measure only: 1   none: 3   candidate: 1')