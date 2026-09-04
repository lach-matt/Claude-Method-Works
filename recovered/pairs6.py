from itertools import combinations
AX=['rungs','exposure','lattice','conflation','measured','in-deg','out-deg']
NINE={'X':(4,8,2,2,2,2,1),'Sc':(3,4,2,0,2,0,1),'IC':(3,6,0,0,2,4,1),'U':(3,8,0,2,1,0,2),
 'NEC':(5,7,1,2,1,2,1),'L':(2,4,0,2,2,1,1),'SD':(2,5,2,2,2,0,1),
 'DNc':(3,4,0,1,2,1,3),'DNd':(3,2,0,1,2,2,1)}
SIX={'CPT':(2,2,2,0,2,0,1),'E-p conservation':(2,1,0,0,2,1,0),'GSL':(2,3,0,0,0,1,1),
 'EOM order':(2,2,0,0,2,0,1),'equivalence pr.':(2,1,0,0,2,0,0),'global symmetry':(2,1,0,0,1,0,0)}
v9=[sorted({c[i] for c in NINE.values()}) for i in range(7)]
full=[range(2,6),range(1,9),range(0,3),range(0,3),range(0,3),range(0,5),range(0,4)]
UNOCC={}
for i,a in enumerate(AX):
    miss=[v for v in full[i] if v not in v9[i]]
    if miss: UNOCC[a]=(i,miss)
print('  UNOCCUPIED DIRECTIONS IN THE NINE')
for a,(i,m) in UNOCC.items(): print('     %-11s missing values %s' % (a,m))
print('     -> %d directions, C(%d,2) = %d pairs' % (len(UNOCC),len(UNOCC),len(list(combinations(UNOCC,2)))))
print()
def dirs(p):
    return tuple(a for a,(i,m) in UNOCC.items() if p[i] in m)
print('  WHERE THE SIX HAND-FOUND AXES SIT')
occ={}
for n,p in SIX.items():
    d=dirs(p); occ.setdefault(d,[]).append(n)
    print('     %-20s %s' % (n, ', '.join(d) or 'inside the observed box'))
print()
print('  THE SIX PAIRS, OCCUPIED AND EMPTY')
print('  %-34s %s' % ('pair','status'))
preds={}
for a,b in combinations(UNOCC,2):
    key=tuple(sorted((a,b)))
    got=[n for d,ns in occ.items() if set(d)==set(key) for n in ns]
    if got:
        print('  %-34s OCCUPIED : %s' % (a+' + '+b, ', '.join(got)))
    else:
        preds[key]=(a,b)
        print('  %-34s EMPTY - predicts an axis' % (a+' + '+b))
print()
print('  WHAT EACH EMPTY PAIR PREDICTS')
DESC={
 ('exposure','in-deg')  : ('rarely theorised, but forced by three other coordinates',
    'a law-class few papers name yet many things imply'),
 ('measured','out-deg') : ('unmeasured and terminal, but heavily theorised',
    'weak cosmic censorship - named by Penrose, Landsman, Senovilla, Ishibashi-Maeda-Mefford; no experimental bound; nothing in the edge set follows from it'),
 ('in-deg','measured')  : ('unmeasured, and forced by three other coordinates',
    'a conjecture that many broken laws would entail - candidate: the holographic/Bekenstein bound'),
 ('in-deg','out-deg')   : ('a pure sink: three things force it, it forces nothing',
    'candidate: black-hole information recovery / Page-curve unitarity'),
 ('exposure','measured'): ('',''),
 ('exposure','out-deg') : ('',''),
}
for key,(a,b) in preds.items():
    d=DESC.get(key) or DESC.get((key[1],key[0])) or ('','')
    print('     %-26s %s' % (a+' + '+b, d[0]))
    if d[1]: print('     %-26s candidate: %s' % ('', d[1]))
print()
print('  TALLY')
print('     directions unoccupied : %d' % len(UNOCC))
print('     pairs                 : %d' % len(list(combinations(UNOCC,2))))
print('     occupied by hand-found axes : %d' % (len(list(combinations(UNOCC,2)))-len(preds)))
print('     EMPTY, each predicting an axis : %d' % len(preds))
print('     law-classes now: 9 indexed + 6 hand-found + %d predicted = %d' % (len(preds), 9+6+len(preds)))