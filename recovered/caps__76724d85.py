from itertools import product
from collections import deque
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
V={c for c in allc if not(c[4]>=3 and not(c[2]>=2 or c[3]>=1 or c[0]>=1))}
o=close((0,1,0,0,1,0,0,0,0))
CAPS=[('evaporating black hole',     'NEC>=1', lambda c:c[NEC_]>=1),
      ('Planck-scale wormhole',      'NEC>=2', lambda c:c[NEC_]>=2),
      ('macroscopic wormhole',       'NEC>=3', lambda c:c[NEC_]>=3),
      ('universal horizon',          'X>=2',   lambda c:c[X_]>=2),
      ('time machine',               'X=3',    lambda c:c[X_]>=3),
      ('trivial comm. complexity',   'Sc=2',   lambda c:c[Sc_]>=2),
      ('superluminal signalling',    'IC=2',   lambda c:c[IC_]>=2),
      ('information loss',           'U>=1',   lambda c:c[U_]>=1),
      ('NP-complete in P',           'L=1',    lambda c:c[L_]>=1),
      ('perfect cloning',            'DNc=2',  lambda c:c[DNc_]>=2),
      ('perfect discrimination',     'DNd=2',  lambda c:c[DNd_]>=2)]
# BFS over unit coordinate steps within V
adj={}
for c in V:
    n=[]
    for i in range(9):
        for d in (1,-1):
            t=list(c); t[i]+=d
            if 0<=t[i]<len(RNG[i]):
                tc=close(tuple(t))
                if tc in V and tc!=c: n.append(tc)
    adj[c]=n
dist={o:0}; q=deque([o])
while q:
    c=q.popleft()
    for n in adj[c]:
        if n not in dist: dist[n]=dist[c]+1; q.append(n)
print('  reachable from our cell by unit steps: %d of %d' % (len(dist), len(V)))
print()
print('  %-28s %-8s %6s %6s  cheapest cell' % ('capability','threshold','here?','steps'))
for nm,th,f in CAPS:
    have = f(o)
    cands=[(dist[c],c) for c in dist if f(c)]
    if not cands:
        print('  %-28s %-8s %6s %6s' % (nm,th,'no','unreach')); continue
    d,c=min(cands)
    print('  %-28s %-8s %6s %6d  %s' % (nm,th,('YES' if have else 'no'),d,str(c)))
print()
print('  THE MACROSCOPIC WORMHOLE: cheapest routes')
cands=sorted((dist[c],c) for c in dist if c[NEC_]>=3)
best=cands[0][0]
tied=[c for d,c in cands if d==best]
print('     minimum %d steps; %d distinct cells at that cost' % (best,len(tied)))
for c in tied[:6]:
    payer=[]
    if c[X_]>0: payer.append('preferred frame X=%d'%c[X_])
    if c[U_]>0: payer.append('non-unitarity U=%d'%c[U_])
    if c[IC_]>=2: payer.append('signalling IC=2')
    print('       %s   pays with: %s' % (c, ', '.join(payer)))
print()
print('  COST TO EACH CAPABILITY, SORTED')
rows=sorted(((min(dist[c] for c in dist if f(c)) if any(f(c) for c in dist) else 99), nm, th) for nm,th,f in CAPS)
for d,nm,th in rows:
    print('     %2d  %-28s %s' % (d,nm,th))