from itertools import product
NM=['X','Sc','IC','U','NEC','L','SD','DNc','DNd']
THMS={'Buniy':['X','NEC','U'],'Hartman':['U','X','SD','NEC'],'Wall':['X','U','NEC'],
 'GrahamOlum':['NEC'],'spinstat':['X','SD','U','Sc'],'Burgoyne':['SD'],'Tsirelson':['Sc'],
 'PopescuRohrlich':['Sc','IC'],'Pawlowski':['IC','Sc'],'BSP':['U','IC'],'Nikolic':['U'],
 'Polchinski':['L','IC'],'AbramsLloyd':['L'],'Weinberg':['L'],'WoottersZurek':['DNc'],
 'Rastegin':['DNc','DNd'],'SimonBuzekGisin':['DNc','IC'],'Soulas':['SD','IC'],'Sorkin':['SD'],
 'Creminelli':['NEC','X'],'FordRoman':['NEC'],'DubovskySibiryakov':['X','U'],
 'DeutschLloyd':['X','U','L','DNc','DNd'],'IshibashiMaeda':['NEC','X']}
EDGES=[('X','NEC'),('Sc','IC'),('IC','X'),('U','IC'),('U','NEC'),('NEC','X'),
       ('L','DNd'),('SD','IC'),('DNc','IC'),('DNc','L'),('DNc','DNd'),('DNd','DNc')]
RUNGS={'X':4,'Sc':3,'IC':3,'U':3,'NEC':5,'L':2,'SD':2,'DNc':3,'DNd':3}
LATT ={'X':2,'Sc':2,'SD':2,'NEC':1,'U':0,'L':0,'IC':0,'DNc':0,'DNd':0}
CONF ={'X':2,'U':2,'NEC':2,'L':2,'SD':2,'DNc':1,'DNd':1,'Sc':0,'IC':0}
MEAS ={'X':2,'Sc':2,'IC':2,'L':2,'SD':2,'DNc':2,'DNd':2,'U':1,'NEC':1}
expo={n:sum(1 for t,cs in THMS.items() if n in cs) for n in NM}
ind ={n:sum(1 for a,b in EDGES if b==n) for n in NM}
outd={n:sum(1 for a,b in EDGES if a==n) for n in NM}
AX=['rungs','exposure','lattice','conflation','measured','in-deg','out-deg']
def prof(n): return (RUNGS[n],expo[n],LATT[n],CONF[n],MEAS[n],ind[n],outd[n])
X={prof(n) for n in NM}
print('  THE AXIS INDEX')
print('  %-5s %s' % ('axis',' '.join('%-10s'%a for a in AX)))
for n in NM: print('  %-5s %s' % (n,' '.join('%-10d'%v for v in prof(n))))
print()
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
R=RR(X,7); ex=sorted(R-X)
box=1
for i in range(7): box*=len({c[i] for c in X})
print('  cells (axes) %d   ambient box %d   |R| %d   E = %d' % (len(X),box,len(R),len(ex)))
print('  => the axis index is %s' % ('OPEN' if ex else 'CLOSED'))
print()
if ex:
    print('  EXCESS PROFILES  (axis-shapes the structure admits that no axis realises)')
    print('  %s' % ' '.join('%-10s'%a for a in AX))
    for t in ex[:24]: print('  %s' % ' '.join('%-10d'%v for v in t))
    if len(ex)>24: print('  ... %d more' % (len(ex)-24))
    print()
    print('  DO THE KNOWN-MISSING AXES MATCH ANY EXCESS PROFILE?')
    CAND={
     'CPT'            : (2, 2, 2, 0, 2, 0, 1),   # binary, 2 theorems, lattice via spin-stat, clean, measured, edge into X
     'E-p conservation':(2, 1, 0, 0, 2, 1, 0),
     'GSL'            : (2, 3, 0, 0, 0, 1, 1),
     'EOM order'      : (2, 2, 0, 0, 2, 0, 1),
     'equivalence pr.' : (2, 1, 0, 0, 2, 0, 0),
     'global symmetry' : (2, 1, 0, 0, 1, 0, 0),
    }
    exs=set(ex)
    for n,p in CAND.items():
        inR = p in exs
        inX = p in X
        vals=[sorted({c[i] for c in X}) for i in range(7)]
        inbox = all(p[i] in vals[i] for i in range(7))
        tag = 'EXCESS - predicted' if inR else ('already an axis' if inX else
              ('outside the observed box' if not inbox else 'excluded by the envelopes'))
        print('     %-18s %s   %s' % (n, str(p), tag))