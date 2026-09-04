from itertools import product, combinations
NM=['THETA','SIGMA','STAT','COMP','ACH','TOP']
# THETA 0 non-expanding (theta=0) 1 expanding/contracting
# SIGMA 0 shear-free 1 sheared
# STAT  0 a Killing field is tangent to N 1 none
# COMP  0 generators complete 1 incomplete
# ACH   0 N is achronal 1 chronal
# TOP   0 N has cuts of spherical/planar topology 1 other
RNG=[range(2),range(2),range(2),range(2),range(2),range(2)]
TH,SG,ST,CM,AC,TP=range(6)
def close(x):
    x=list(x); g=True
    while g:
        g=False
        def up(i,v):
            nonlocal g
            if x[i]<v: x[i]=v; g=True
        # a Killing horizon is non-expanding and shear-free (Raychaudhuri + zero law)
        if x[ST]==0:
            if x[TH]>0: x[TH]=0; g=True
            if x[SG]>0: x[SG]=0; g=True
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
V={close(x) for x in product(*RNG)}
V={close(c) for c in V}
e,ex,box=E(V,6,ret=True)
print('  THE LOCAL NULL-SURFACE INDEX')
print('  letters: THETA expansion | SIGMA shear | STAT a Killing field tangent to N')
print('           COMP generators complete | ACH achronal | TOP cut topology')
print()
print('  edge: STAT=0 -> THETA=0 and SIGMA=0   (a Killing horizon is non-expanding and shear-free)')
print()
print('  cells %d   box %d   density %.1f%%   E = %d -> %s'
      % (len(V),box,100*len(V)/box,e,'CLOSED' if e==0 else 'OPEN'))
bad=0
for i in range(6):
    for j in range(6):
        if i==j: continue
        m={}
        for c in V: m[c[j]]=max(m.get(c[j],-99),c[i])
        s=[m[v] for v in sorted(m)]
        if s!=sorted(s) and s!=sorted(s,reverse=True): bad+=1
print('  non-monotone pairwise relations: %d of 30' % bad)
print()
print('  THE NAMED SURFACES AS CELLS')
def mk(**kw):
    x=[0]*6
    for k,v in kw.items(): x[NM.index(k)]=v
    return close(tuple(x))
CASES=[('Killing horizon (Kay-Wald)',              mk(),
        'HSMI established; every curved-space ANEC/QNEC route lives here'),
       ('non-expanding horizon',                    mk(STAT=1),
        'theta = 0, no Killing field required'),
       ('isolated horizon (Ashtekar et al)',        mk(STAT=1),
        'a non-expanding horizon with additional structure on the connection'),
       ('dynamical / sheared null surface',         mk(STAT=1,SIGMA=1),
        'generic'),
       ('expanding null cone',                      mk(STAT=1,THETA=1),
        'a light cone from a point'),
       ('finite causal diamond null segment',       mk(STAT=1,THETA=1,COMP=1),
        '2026 corner-edge-mode work targets this'),
       ('the Rindler horizon in Minkowski',         mk(),
        'the flat-space case; Bisognano-Wichmann')]
print('  %-38s %-26s %s' % ('surface','cell','status'))
for n,c,s in CASES:
    print('  %-38s %-26s %s' % (n,str(list(c)),s))
print()
print('  WHERE HSMI IS ESTABLISHED, AS A REGION')
est=[c for c in V if c[ST]==0]
print('     STAT = 0 (Killing): %d of %d cells -- established for interacting QFT' % (len(est),len(V)))
nex=[c for c in V if c[TH]==0]
print('     THETA = 0 (non-expanding, Killing or not): %d of %d cells' % (len(nex),len(V)))
print('     the gap between them is %d cells: non-expanding WITHOUT a Killing field.' % (len(nex)-len(est)))
print()
print('  THE TARGET, NAMED')
print('     the extension is: does HSMI hold on a NON-EXPANDING horizon that is not Killing?')
print('     that region has a name in general relativity - the ISOLATED HORIZON')
print('     (Ashtekar, Beetle, Lewandowski) - defined quasi-locally, no Killing field,')
print('     no asymptotic structure required.')
print()
print('     so the open question is not "general null surfaces". it is:')
print('        HSMI on isolated horizons.')
print('     which is one cell away from where it is proved, and the cell is standard.')
print()
print('  AND THE PAPER IS RIGHT THAT THE NEIGHBOURHOOD DEFINES IT')
print('     every letter here is neighbourhood data: expansion and shear of the generators,')
print('     completeness, achronality, cut topology, and whether a Killing field is tangent.')
print('     none is global. V3 supplies asymptotics and topology of the SPACETIME;')
print('     this index supplies the local structure of the SURFACE.')
print('     they are different vocabularies, and only the second bears on modular theory.')