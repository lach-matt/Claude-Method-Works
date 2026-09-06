from itertools import product, combinations
from collections import defaultdict
P=['TRIG','CUR','JUR','VOC','V1','FIRE']
# TRIG trigger arity (letters in the antecedent)
# CUR  number of currencies accepted
# JUR  number of jurisdiction conditions
# VOC  vocabularies spanned
# V1   hypotheses expressible in the law index
# FIRE 0 vacuous in the law index, 1 fires
CH={
 'Buniy-Hsu-Murray'      :(1,1,4,2,2,1),
 'Hartman-Kundu-Tajdini' :(1,3,3,3,2,0),
 'Wall (GSL)'            :(1,2,5,3,1,1),
 'Graham-Olum'           :(1,1,5,2,0,1),
 'spin-statistics'       :(1,1,5,2,3,1),
 'Ostrogradsky'          :(1,1,1,2,1,1),
}
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
print('  THE CHARGER INDEX')
print('  %-24s %s' % ('charger',' '.join('%-5s'%p for p in P)))
for k,v in CH.items(): print('  %-24s %s' % (k,' '.join('%-5d'%x for x in v)))
X=set(CH.values())
e,ex,box=E(X,6,ret=True)
print()
print('  cells %d   box %d   density %.1f%%   E = %d   -> %s'
      % (len(X),box,100*len(X)/box,e,'OPEN' if e else 'CLOSED'))
print('  (density far below the informativeness threshold: E here counts empty room)')
print()
bad=0
for i in range(6):
    for j in range(6):
        if i==j: continue
        m={}
        for c in X: m[c[j]]=max(m.get(c[j],-99),c[i])
        s=[m[v] for v in sorted(m)]
        if s!=sorted(s) and s!=sorted(s,reverse=True): bad+=1
print('  non-monotone pairwise relations: %d of 30' % bad)
print()
print('  THE CLUSTERING - which values no charger takes')
FULL={'TRIG':range(1,4),'CUR':range(0,5),'JUR':range(0,7),'VOC':range(1,5),
      'V1':range(0,6),'FIRE':range(0,2)}
UN={}
for i,p in enumerate(P):
    seen=sorted({c[i] for c in X}); miss=[v for v in FULL[p] if v not in seen]
    if miss: UN[p]=miss
    print('     %-5s observed %-18s missing %s' % (p,str(seen),str(miss) if miss else '-'))
print()
print('  THE TWO STRUCTURAL ABSENCES')
print('     TRIG : every charger has trigger arity 1. NONE is triggered by a conjunction.')
print('     JUR  : every charger has at least one jurisdiction condition. NONE is universal.')
print()
print('  WHY THE SECOND ONE MATTERS')
print('     Part VIII computes: an UNJURISDICTED forcing NEC >= 3 -> U >= 1 gives E = 0.')
print('     so the empty direction JUR = 0 is exactly the charger-shape that would')
print('     close the law index. the missing cell in the charger index and the')
print('     defect in the law index are the same absence, seen from two levels.')
print()
print('  PAIR-COMPLETION OVER THE UNOCCUPIED DIRECTIONS')
ds=list(UN)
print('     unoccupied directions: %s  -> %d pairs' % (ds, len(list(combinations(ds,2)))))
def dirs(v):
    return tuple(p for p in UN if v[P.index(p)] in UN[p])
occ=defaultdict(list)
for k,v in CH.items(): occ[dirs(v)].append(k)
for a,b in combinations(ds,2):
    got=[k for d,ks in occ.items() if set(d)=={a,b} for k in ks]
    print('     %-16s %s' % (a+' + '+b, ', '.join(got) if got else 'EMPTY'))
print()
print('  WHAT EACH SINGLE ABSENCE PREDICTS')
print('     JUR = 0            a universal theorem: no scope condition at all.')
print('                        would make its constraint binary and close the index.')
print('                        no such theorem exists in the energy-condition literature.')
print('     TRIG >= 2          a theorem triggered by a CONJUNCTION of law-violations.')
print('                        would raise arity from the trigger side rather than the')
print('                        jurisdiction side - a shape not represented at all.')
print()
print('  A CONSISTENCY CHECK AGAINST PART VIII')
print('  %-24s %-6s %-8s %s' % ('charger','VOC','fires','severance role'))
ROLE={'Buniy-Hsu-Murray':'the only charger reaching the core cell',
      'Hartman-Kundu-Tajdini':'VACUOUS - trigger and jurisdiction mutually exclusive',
      'Wall (GSL)':'creates the second cycle via V5',
      'Graham-Olum':'inside the unreachable component',
      'spin-statistics':'the lattice map; no bearing on the core',
      'Ostrogradsky':'absorbs the EOM jurisdiction into U_ghost'}
for k,v in CH.items():
    print('  %-24s %-6d %-8s %s' % (k,v[3],'yes' if v[5] else 'NO',ROLE[k]))