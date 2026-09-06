from itertools import product
RNG=[range(4),range(3),range(3),range(3),range(5),range(2),range(2),range(3),range(3)]
NM=['X','Sc','IC','U','NEC','L','SD','DNc','DNd']
X_,Sc_,IC_,U_,NEC_,L_,SD_,DNc_,DNd_=range(9)
HYP={
 'Buniy-Hsu-Murray': [('causal', False), ('Lorentz invariant', 'X'), ('2nd-order EOM', False),
                      ('scalar/gauge/fermion content', False)],
 'Hartman-Kundu-Tajdini': [('unitary','U'), ('Lorentz invariant','X'), ('interacting', False),
                           ('d > 2', False), ('flat spacetime', False)],
 'Wall (GSL)': [('determinism', False), ('ultralocality', False), ('local Lorentz invariance','X'),
                ('stability', False), ('minimal coupling', False)],
 'Graham-Olum': [('asymptotically flat', False), ('simply connected', False), ('generic', False),
                 ('globally hyperbolic', False), ('self-consistent semiclassical', False)],
}
print('  HYPOTHESES OF EACH CHARGER, AND WHETHER THE INDEX CAN EXPRESS THEM')
from collections import Counter
appear=Counter()
for ch,hs in HYP.items():
    idx=[h for h,a in hs if a]; non=[h for h,a in hs if not a]
    for h,a in hs:
        if a: appear[a]+=1
    print('     %-24s  %d hypotheses:  %d indexable (%s), %d not'
          % (ch, len(hs), len(idx), ', '.join(a for _,a in hs if a) or '-', len(non)))
    print('        %-21s  outside the index: %s' % ('', '; '.join(non)))
print()
print('  COORDINATE EXPOSURE  (how many chargers name it as a hypothesis)')
for i,n in enumerate(NM):
    k=appear.get(n,0)
    tag = '  <-- unique multi-charger hypothesis' if k>1 else ''
    print('     %-5s appears as a hypothesis in %d charger(s)%s' % (n,k,tag))
print()
print('  OUR OWN VALUES AT THOSE COORDINATES')
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
o=close((0,1,0,0,1,0,0,0,0))
for n in ('X','U'):
    i=NM.index(n)
    print('     %-5s = %d   (hypothesis satisfied: %s)' % (n,o[i], o[i]==0))
print()
def E(S,d):
    S=set(S); vals=[sorted({c[i] for c in S}) for i in range(d)]
    def env(i,j):
        m={}
        for c in S:
            if c[i]>m.get(c[j],-99): m[c[j]]=c[i]
        b,o2=-99,{}
        for t in sorted(m): b=max(b,m[t]); o2[t]=b
        return o2
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    return sum(1 for x in product(*vals) if all(x[i]<=phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i!=j))-len(S)
allc={close(x) for x in product(*RNG)}
print('  DEFECT AS A FUNCTION OF HOW MANY OF BUNIY\'S HYPOTHESES THE INDEX CAN APPLY')
print('  %-46s %7s %6s' % ('hypotheses applied','cells','E'))
for lab,extra in [('Lorentz invariance only (the index as built)', lambda c: True),
                  ('+ a hypothetical 2nd indexable hypothesis (SD=0)', lambda c: c[SD_]==0),
                  ('+ a 3rd (L=0)', lambda c: c[SD_]==0 and c[L_]==0),
                  ('+ a 4th (IC<2)', lambda c: c[SD_]==0 and c[L_]==0 and c[IC_]<2)]:
    V={c for c in allc if (c[NEC_]<3) or (c[X_]>=1) or (not extra(c)) or c[U_]>=1}
    print('  %-46s %7d %6d' % (lab,len(V),E(V,9)))