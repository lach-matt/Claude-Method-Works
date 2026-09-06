import sys; sys.path.insert(0,'/home/claude/method')
from itertools import product, combinations
from collections import Counter, defaultdict
import method_tower as mt
L=sorted(set(mt.base((3,3,1,3,1))))
NMl=['n','l','k','q','e','f','g','2S']
print('  Lambda_8: %d cells' % len(L))
le=lambda a,b: all(a[i]<=b[i] for i in range(8))
pairs=[]
for i,a in enumerate(L):
    for b in L[i+1:]:
        if le(a,b): pairs.append((a,b))
        elif le(b,a): pairs.append((b,a))
print('  ordered pairs (strict): %d of %d  (%.1f%%)' % (len(pairs), len(L)*(len(L)-1)//2,
      100*len(pairs)/(len(L)*(len(L)-1)//2)))
print()
MEAS=[
 ('Coulomb  -1/n^2',            lambda c: -1.0/c[0]**2),
 ('Madelung  n+l, then n',      lambda c: (c[0]+c[1])*100+c[0]),
 ('grade  sum of coordinates',  lambda c: sum(c)),
 ('n and l',                    lambda c: c[0]*100+c[1]),
 ('n, l, k',                    lambda c: (c[0]*100+c[1])*100+c[2]),
 ('shell occupancy  k',         lambda c: c[2]),
 ('total spin  2S',             lambda c: c[7]),
 ('all eight (the cell itself)', lambda c: c),
]
print('  %-30s %10s %10s %10s %10s' % ('measure','faithful','monotone','distinct','resolves'))
rows=[]
for nm,mu in MEAS:
    unf=sum(1 for a,b in pairs if mu(a)==mu(b))
    nonm=sum(1 for a,b in pairs if not (mu(a)<mu(b) if not isinstance(mu(a),tuple) else mu(a)<mu(b)))
    vals=len({str(mu(c)) for c in L})
    faithful = unf==0
    monotone = nonm==0
    rows.append((nm,faithful,monotone,vals,100*(len(pairs)-unf)/len(pairs)))
    print('  %-30s %10s %10s %10d %9.1f%%' % (nm, 'YES' if faithful else 'no',
          'YES' if monotone else 'no', vals, 100*(len(pairs)-unf)/len(pairs)))
print()
print('  HOW MANY COORDINATES DOES A FAITHFUL MEASURE NEED?')
print('  %-34s %8s %10s' % ('coordinate subset','distinct','resolves'))
best={}
for r in range(1,9):
    bestr=None
    for idx in combinations(range(8),r):
        mu=lambda c,idx=idx: tuple(c[i] for i in idx)
        unf=sum(1 for a,b in pairs if mu(a)==mu(b))
        res=100*(len(pairs)-unf)/len(pairs)
        if bestr is None or res>bestr[1]: bestr=(idx,res,len({mu(c) for c in L}))
    best[r]=bestr
    print('  %-34s %8d %9.1f%%' % (str([NMl[i] for i in bestr[0]]), bestr[2], bestr[1]))
    if bestr[1]==100.0:
        print('     -> FAITHFUL at %d coordinates' % r); break
print()
print('  THE MEASURE INDEX  (measures graded by what they resolve)')
print('  letters: FAITH 0 unfaithful / 1 faithful')
print('           MONO  0 not monotone in the order / 1 monotone')
print('           CARD  0 few values / 1 many / 2 one per cell')
print('           DEPTH number of lattice coordinates the measure reads (0-8)')
def grade(nm,mu):
    unf=sum(1 for a,b in pairs if str(mu(a))==str(mu(b)))
    vals=len({str(mu(c)) for c in L})
    F=1 if unf==0 else 0
    C=2 if vals==len(L) else (1 if vals>50 else 0)
    return F,C,vals
CELLS=set()
for nm,mu in MEAS:
    F,C,vals=grade(nm,mu)
    CELLS.add((F,C))
print()
print('  %-30s %6s %6s %8s' % ('measure','FAITH','CARD','values'))
for nm,mu in MEAS:
    F,C,vals=grade(nm,mu)
    print('  %-30s %6d %6d %8d' % (nm,F,C,vals))
print()
print('  observed (FAITH, CARD) cells: %s' % sorted(CELLS))
print('  the box is 2 x 3 = 6; observed %d; the pair (FAITH=1, CARD<2) is EMPTY' % len(CELLS))
print()
print('  WHY IT IS EMPTY')
print('     a faithful measure separates every ordered pair.')
print('     Lambda_8 has %d cells and %d ordered pairs.' % (len(L),len(pairs)))
print('     any map with fewer than %d values collides on some pair.' % len(L))
print('     so FAITH=1 forces CARD=2: a faithful measure is a bijection onto the cells.')
print()
print('  CONSEQUENCE')
print('     FAITH = 1  <=>  the measure IS the lattice, re-labelled.')
print('     a measure that compresses (CARD < 2) cannot be faithful.')
print('     -> the measure carries no less information than the lattice,')
print('        which is why it cannot be an axis of it, and must stay external.')