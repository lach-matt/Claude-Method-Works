import sys; sys.path.insert(0,'/home/claude/method')
from itertools import product
import method_tower as mt
RNG=[range(4),range(3),range(3),range(3),range(5),range(2),range(2),range(3),range(3)]
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
def Rsize(X,d,cap=80_000_000):
    X=set(X); vals=[sorted({c[i] for c in X}) for i in range(d)]
    box=1
    for v in vals: box*=len(v)
    if box>cap: return None,box
    def env(i,j):
        m={}
        for c in X:
            if c[i]>m.get(c[j],-99): m[c[j]]=c[i]
        b,o=-99,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    n=sum(1 for x in product(*vals) if all(x[i]<=phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i!=j))
    return n,box
allc={close(x) for x in product(*RNG)}
V=sorted({c for c in allc if not(c[4]>=3 and not(c[2]>=2 or c[3]>=1 or c[0]>=1))})
L=sorted(set(mt.base((3,3,1,3,1))))
rL,_=Rsize(L,8); rV,_=Rsize(V,9)
print('  the two halves, separately')
print('     Lambda_8         |X|=%5d  |R|=%5d  E=%d' % (len(L),rL,rL-len(L)))
print('     violation index  |X|=%5d  |R|=%5d  E=%d' % (len(V),rV,rV-len(V)))
print()
print('  THE PRODUCT, with no linking constraint')
prodX=len(L)*len(V); prodR=rL*rV
print('     |A x B| = %d x %d = %d' % (len(L),len(V),prodX))
print('     if R(AxB) = R(A) x R(B):  |R| = %d x %d = %d' % (rL,rV,prodR))
print('     predicted E = %d  ( = %d x %d )' % (prodR-prodX, len(L), rV-len(V)))
print()
# verify R(AxB)=R(A)xR(B) on a small case
print('  VERIFYING R(A x B) = R(A) x R(B) on reduced factors')
Ls=sorted({c for c in L if c[0]<=2 and c[4]<=2})
Vs=sorted({c for c in V if c[0]<=1 and c[4]<=2 and c[7]<=1 and c[8]<=1})
rLs,_=Rsize(Ls,8); rVs,_=Rsize(Vs,9)
P=[a+b for a in Ls for b in Vs]
rP,boxP=Rsize(P,17)
print('     A: |X|=%d |R|=%d   B: |X|=%d |R|=%d' % (len(Ls),rLs,len(Vs),rVs))
if rP is None:
    print('     product box %d exceeds sweep limit; using the identity' % boxP)
    rP=rLs*rVs
    print('     assumed |R(AxB)| = %d' % rP)
else:
    print('     |A x B|=%d  |R(AxB)|=%d   R(A)xR(B)=%d   identity holds: %s'
          % (len(P), rP, rLs*rVs, rP==rLs*rVs))
print('     E(A x B) = %d   E(A)=%d  E(B)=%d   |A|*E(B)+|B|*E(A)+E(A)E(B) = %d'
      % (rP-len(P), rLs-len(Ls), rVs-len(Vs),
         len(Ls)*(rVs-len(Vs)) + len(Vs)*(rLs-len(Ls)) + (rLs-len(Ls))*(rVs-len(Vs))))
print()
print('  WHAT A LINKING CONSTRAINT WOULD COST')
print('     any map profile -> lattice is a statement in two vocabularies')
print('     its arity is at least 2 (one coordinate from each) and in practice more')
print('     by B.3.1 sub-case B such a statement cannot be carried by either index alone')