import numpy as np
from math import comb, log2
from itertools import product
def Rop(S,d):
    L=sorted(S); A=[sorted({x[i] for x in L}) for i in range(d)]
    phi={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            f={}; run=-1
            for v in A[j]:
                c=[x[i] for x in L if x[j]<=v]
                run=max(run,max(c) if c else -1); f[v]=run
            phi[(i,j)]=f
    return {x for x in product(*A)
            if all(x[i]<=phi[(i,j)].get(x[j],-1) for i in range(d) for j in range(d) if i!=j)}
print("="*76)
print("  WHAT IS SLACK, MATHEMATICALLY?")
print("="*76)
print("""
  SLACK(S) = mu(ambient)/mu(S). For a COUNTING measure that is |R(X)|/|X|,
  and its logarithm is  log|R(X)| - log|X|.

  THAT IS AN INFORMATION QUANTITY. Given the closure R(X), how many bits
  are needed to say WHICH subset X is?

        E_bits(X) = log2 C( |R(X)| , E(X) )

  the cost of naming which E(X) of the admitted cells are absent.
""")
PT=set()
for g in (1,18): PT.add((1,g))
for p in (2,3):
    for g in list(range(1,3))+list(range(13,19)): PT.add((p,g))
for p in (4,5,6,7):
    for g in range(1,19): PT.add((p,g))
DAYS={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
CAL={(m,d) for m in range(1,13) for d in range(1,DAYS[m]+1)}
IP={(a,b) for a in range(0,16) for b in range(0,16) if not (a==10 and b>7)}
BOX={(l,w,h) for l in range(1,7) for w in range(1,7) for h in range(1,7) if l>=w>=h}
JAN=set()
for p in range(1,9):
    w={1:2,2:2,3:8,4:8,5:18,6:18,7:32,8:32}[p]
    for g in range(1,w+1): JAN.add((p,g))
print("  %-24s%7s%9s%6s%10s%11s"%("index","|X|","|R(X)|","E","E_bits","bits/cell"))
for nm,S,d in [('periodic table 18-col',PT,2),('calendar',CAL,2),
               ('subnet with a hole',IP,2),('Janet left-step',JAN,2),
               ('box l>=w>=h',BOX,3)]:
    R=Rop(S,d); E=len(R)-len(S)
    b=log2(comb(len(R),E)) if E>0 else 0.0
    print("  %-24s%7d%9d%6d%10.1f%11.3f"%(nm,len(S),len(R),E,b,b/len(S)))
print("""
==========================================================================
  AND THAT IS A KNOWN OBJECT
==========================================================================

  log2 C(|R(X)|, E) IS THE DESCRIPTION LENGTH OF X GIVEN ITS CLOSURE.

  E(X) = 0 does not merely mean 'nothing is missing'. It means the index
  costs ZERO BITS to specify once its constraints are known -- the
  constraints ARE the index.

  E(X) = 36 means the periodic table costs 106 bits beyond its own
  coordinate structure. Someone must transmit those bits; in practice a
  chemistry teacher does.

  THAT IS MINIMUM DESCRIPTION LENGTH APPLIED TO AN INDEX RATHER THAN A
  MODEL. Rissanen 1978; Kolmogorov complexity; the two-part code.
""")
print("="*76)
print("  WHICH SHARPENS THE THREE-LANGUAGE CLAIM")
print("="*76)
print("""
     ORDER        E(X)   = cells admitted minus carried
     GEOMETRY     void   = box minus lattice
     CALCULUS     V      = bracket width over estimate error
     INFORMATION  E_bits = bits to specify X given R(X)

  THE FOURTH IS NOT A FOURTH LANGUAGE. IT IS THE COMMON CURRENCY.
  A count becomes bits by a logarithm; a ratio becomes bits by a logarithm.
""")
R=109737.3
T=lambda v: R/v**2
print("  %5s%10s%15s"%("nu","V","log2 V (bits)"))
for v in (5,10,20,40):
    a,m,b=T(v-1),T(v),T(v+1)
    V=abs(b-a)/abs(m-(a+b)/2)
    print("  %5d%10.3f%15.3f"%(v,V,log2(V)))
print("""
  log2 V IS THE NUMBER OF BITS OF PRECISION GIVEN UP FOR CERTAINTY.
  At nu = 40 the bracket costs 5.74 bits: the estimate resolves the level
  53x finer than the guarantee does, and 53 = 2^5.74.
""")
print("="*76)
print("  AND THE FLOOR BECOMES A BIT-FLOOR")
print("="*76)
print("""
     Prop 14.1:  V > 2      =>  log2 V > 1
     Rydberg:    V >= 32/11 =>  log2 V >= %.4f

  A GUARANTEE ALWAYS COSTS MORE THAN ONE BIT. Never less. The cheapest
  possible certainty costs one binary digit of resolution, and a Rydberg
  series charges %.2f.
"""%(log2(32/11),log2(32/11)))