from rop import *
import pickle
for dims in [(2,2),(3,2),(2,2,2),(3,3),(4,3),(2,2,3),(2,2,2,2)]:
    U=box(dims); n=len(U)
    C=pickle.load(open('cl16.pkl','rb')) if dims==(2,2,2,2) else moore(U)
    vecs=[tuple(1 if u in c else 0 for u in U) for c in C]     # characteristic vectors over U
    memE=sum(1 for c in C if c and len(R(c))!=len(c))           # every member E=0 ?
    RC=R(vecs); EF=len(RC)-len(vecs)
    sep=sum(1 for a in U for b in U if a!=b and any((a in c) and (b not in c) for c in C))
    print(dims,'members',len(vecs),'members with E>0:',memE,'|ℛ(Cl)|',len(RC),'= 2^n?',len(RC)==2**n,'E(Cl)',EF,'separating ordered pairs %d of %d'%(sep,n*(n-1)))