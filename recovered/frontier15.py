from itertools import product
import random
from collections import Counter
NM=['X_exp','X_spon','Sc','IC','U_open','U_ghost','NEC_pt','NEC_ach',
    'L_dyn','L_kin','SD_obs','SD_field','DNc','DNd','EOM']
RNG=[range(4),range(2),range(3),range(3),range(3),range(2),range(5),range(2),
     range(2),range(2),range(2),range(2),range(3),range(3),range(2)]
Xe,Xs,Sc,IC,Uo,Ug,Np,Na,Ld,Lk,So,Sf,Dc,Dd,EO=range(15)
def close(x):
    x=list(x); g=True
    while g:
        g=False
        def rz(i,v):
            nonlocal g
            if x[i]<v: x[i]=v; g=True
        if x[Xe]>=3: rz(Np,2); rz(Na,1)
        if x[Sc]>=2: rz(IC,1)
        if x[Uo]>=2: rz(IC,2)
        if x[Uo]>=1: rz(Np,1)
        if x[Np]>=4: rz(Xe,1)
        if x[Ld]>=1: rz(Dd,1)
        if x[So]>=1: rz(IC,2)
        if x[Dc]>=2: rz(IC,2); rz(Ld,1); rz(Dd,2)
        if x[Dd]>=2: rz(Dc,2)
        if x[Na]>=1: rz(Np,2)
        if x[Ug]>=1: rz(Xs,1)
        if x[Lk]>=1: rz(Dd,2)
        if x[EO]>=1: rz(Ug,1)
    return tuple(x)
def excess(S,d):
    S=set(S); vals=[sorted({c[i] for c in S}) for i in range(d)]
    def env(i,j):
        m={}
        for c in S:
            if c[i]>m.get(c[j],-99): m[c[j]]=c[i]
        b,o=-99,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    out=[]; cur=[None]*d
    def rec(i):
        if i==d:
            t=tuple(cur)
            if t not in S: out.append(t)
            return
        for v in vals[i]:
            ok=True
            for j in range(i):
                if v>phi[(i,j)][cur[j]] or cur[j]>phi[(j,i)][v]: ok=False; break
            if ok: cur[i]=v; rec(i+1)
        cur[i]=None
    rec(0)
    return out
allc={c for c in {close(x) for x in product(*RNG)} if c[Sf]==0}
V=sorted({c for c in allc if not(c[Np]>=3 and c[Xe]==0 and c[EO]==0 and c[Ug]<1)})
ex=excess(V,15)
PIN=[Xe,Ug,Np,EO]; FREE=[i for i in range(15) if i not in PIN]
P=sorted({tuple(e[i] for i in FREE) for e in ex})
print('  pinned letters : %s' % [NM[i] for i in PIN])
print('  free letters   : %d, with %d admissible patterns' % (len(FREE),len(P)))
print('  excess         : %d = %d core x %d patterns' % (len(ex),len({tuple(e[i] for i in PIN) for e in ex}),len(P)))
Pset=P
def dP(c):
    v=tuple(c[i] for i in FREE)
    return min(sum(abs(v[k]-p[k]) for k in range(len(FREE))) for p in Pset)
def sP(c):
    v=tuple(c[i] for i in FREE)
    return min(sum(1 for k in range(len(FREE)) if v[k]!=p[k]) for p in Pset)
def d_f(c): return c[Xe]+c[Ug]+abs(c[Np]-3)+c[EO]+dP(c)
def s_f(c): return (1 if c[Xe]>0 else 0)+(1 if c[Ug]>0 else 0)+(1 if c[Np]!=3 else 0)+(1 if c[EO]>0 else 0)+sP(c)
rng=random.Random(0); samp=rng.sample(V,1500)
bd=bs=0
for c in samp:
    bt=min(sum(abs(e[i]-c[i]) for i in range(15)) for e in ex)
    bk=min(sum(1 for i in range(15) if e[i]!=c[i]) for e in ex)
    if d_f(c)!=bt: bd+=1
    if s_f(c)!=bk: bs+=1
print()
print('  FORMULA CHECK on %d sampled cells' % len(samp))
print('     distance mismatches: %d' % bd)
print('     support  mismatches: %d' % bs)
o=close(tuple([0,0,1,0,0,0,1,0,0,0,0,0,0,0,0]))
print()
print('  OUR POSITION')
print('     cell %s' % str(o))
print('     pinned : X_exp=%d + U_ghost=%d + |NEC_pt-3|=%d + EOM=%d = %d'
      % (o[Xe],o[Ug],abs(o[Np]-3),o[EO],o[Xe]+o[Ug]+abs(o[Np]-3)+o[EO]))
print('     pattern: dP = %d, sP = %d' % (dP(o),sP(o)))
print('     total  : d = %d, s = %d      (nine letters gave d = 2, s = 1)' % (d_f(o),s_f(o)))
print()
print('  DISTRIBUTION over the index')
print('     s: %s' % dict(sorted(Counter(s_f(c) for c in samp).items())))
print('     mean s = %.2f, mean d = %.2f' % (sum(s_f(c) for c in samp)/len(samp),
                                              sum(d_f(c) for c in samp)/len(samp)))
one=[c for c in samp if s_f(c)==1]
print('     cells seeing the frontier along a single letter: %d of %d (%.1f%%)'
      % (len(one),len(samp),100*len(one)/len(samp)))