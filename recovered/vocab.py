from itertools import product
VOC={
 'V1 laws'      : ['Lorentz invariant','unitary'],
 'V2 theory'    : ['causal','2nd-order EOM','field content','interacting','d > 2'],
 'V3 geometry'  : ['flat spacetime','asymptotically flat','simply connected','globally hyperbolic','generic'],
 'V4 algebra'   : ['determinism','ultralocality','stability'],
 'V5 coupling'  : ['minimal coupling'],
 'V6 solution'  : ['self-consistent semiclassical'],
}
WHERE={h:v for v,hs in VOC.items() for h in hs}
CH={
 'Buniy-Hsu-Murray'     : ['causal','Lorentz invariant','2nd-order EOM','field content'],
 'Hartman-Kundu-Tajdini': ['unitary','Lorentz invariant','interacting','d > 2','flat spacetime'],
 'Wall (GSL)'           : ['determinism','ultralocality','Lorentz invariant','stability','minimal coupling'],
 'Graham-Olum'          : ['asymptotically flat','simply connected','generic','globally hyperbolic',
                           'self-consistent semiclassical'],
}
VK=sorted(VOC)
print('  THE VOCABULARIES')
for v in VK: print('     %-14s %d terms: %s' % (v,len(VOC[v]),', '.join(VOC[v])))
print()
print('  EACH CHARGER, BY VOCABULARY')
print('  %-24s %s  span  in V1  outside V1' % ('charger',''.join('%-6s'%v.split()[0] for v in VK)))
rows={}
for ch,hs in CH.items():
    cnt={v:0 for v in VK}
    for h in hs: cnt[WHERE[h]]+=1
    span=sum(1 for v in VK if cnt[v])
    rows[ch]=cnt
    print('  %-24s %s  %4d  %4d  %6d' % (ch, ''.join('%-6d'%cnt[v] for v in VK), span, cnt['V1 laws'],
                                          len(hs)-cnt['V1 laws']))
print()
print('  minimum span across chargers: %d' % min(sum(1 for v in VK if rows[c][v]) for c in CH))
print('  chargers expressible in one vocabulary: %d of %d'
      % (sum(1 for c in CH if sum(1 for v in VK if rows[c][v])==1), len(CH)))
print()
# index the chargers by their vocabulary profile and compute E
X={tuple(rows[c][v] for v in VK) for c in CH}
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
    return (len(R)-len(S), sorted(R-S)) if ret else len(R)-len(S)
e,ex=E(X,len(VK),ret=True)
print('  THE VOCABULARY INDEX OF THE CHARGERS')
print('     cells (chargers) %d   |R| %d   E = %d' % (len(X), len(X)+e, e))
if ex:
    print('     excess profiles the envelope admits but no charger realises:')
    for t in ex[:6]:
        print('        %s  =  %s' % (t, ', '.join('%s:%d'%(v.split()[1],n) for v,n in zip(VK,t) if n)))
print()
print('  WHAT A SINGLE-VOCABULARY INDEX CAN HOLD')
for v in VK:
    holds=[c for c in CH if all(WHERE[h]==v for h in CH[c])]
    print('     %-14s can fully state: %s' % (v, ', '.join(holds) if holds else 'no charger'))