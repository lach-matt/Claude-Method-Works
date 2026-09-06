import numpy as np
from math import gcd
from itertools import product
def Rop(S,d):
    Ls=sorted(S);A=[sorted({x[i] for x in Ls}) for i in range(d)];ph={}
    for i in range(d):
        for j in range(d):
            if i==j:continue
            f={};run=-1
            for v in A[j]:
                c=[x[i] for x in Ls if x[j]<=v];run=max(run,max(c) if c else -1);f[v]=run
            ph[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1) for i in range(d) for j in range(d) if i!=j)}
print("="*86)
print("  CAN AN INDEX TELL A DEFECT FROM A FEATURE?  TEST, DO NOT ASSERT")
print("="*86)
print("""
  Give R only the OCCUPIED cells. If it recovers bounds that EXCLUDE the
  absences, the index has judged them inadmissible. If it admits them,
  E > 0 and the index is silent.
""")
aJ=5.2028
OCC=[(4,1),(7,2),(10,3),(3,1),(11,4),(8,3),(5,2),(12,5),(7,3),(9,4),(11,5),(13,6),(2,1)]
ABS=[(15,4),(11,3),(13,4),(14,5),(13,5),(15,7)]
X={(p,q) for p,q in OCC}
R=Rop(X,2)
print("  THE BELT\n")
print("     occupied cells given to R : %d"%len(X))
print("     |R(X)|                    : %d"%len(R))
print("     **E(X)                    : %d**"%(len(R)-len(X)))
adm=[c for c in ABS if c in R]
print("     of the 6 absences, R admits: %d  %s"%(len(adm),adm))
print("     of the 6 absences, R refuses: %d"%(6-len(adm)))
print("\n  THE PERIODIC TABLE\n")
PT=set()
for g in (1,18): PT.add((1,g))
for p in (2,3):
    for g in list(range(1,3))+list(range(13,19)): PT.add((p,g))
for p in (4,5,6,7):
    for g in range(1,19): PT.add((p,g))
RP=Rop(PT,2)
print("     occupied cells given to R : %d"%len(PT))
print("     |R(X)|                    : %d"%len(RP))
print("     **E(X)                    : %d**"%(len(RP)-len(PT)))
print("     R ADMITS all 36 absences  : %s"%(len(RP-PT)==36))
print("="*86)
print("  SO THE INDEX DOES DISTINGUISH — BY WHETHER E IS REMOVABLE")
print("="*86)
print("""
  Two tests, both internal, neither needing the world:

     TEST 1  does R, given the occupied cells alone, ADMIT the absences?
     TEST 2  is E removable by re-coordinatisation?
""")
print("  TEST 2 — the periodic table under three layouts:\n")
def E_of(S,d=2):
    return len(Rop(S,d))-len(S)
JAN=set()
for p in range(1,9):
    w={1:2,2:2,3:8,4:8,5:18,6:18,7:32,8:32}[p]
    for g in range(1,w+1): JAN.add((p,g))
C32=set()
for g in (1,32): C32.add((1,g))
for p in (2,3):
    for g in [1,2]+list(range(27,33)): C32.add((p,g))
for p in (4,5):
    for g in [1,2]+list(range(17,33)): C32.add((p,g))
for p in (6,7):
    for g in range(1,33): C32.add((p,g))
for nm,S in [('18-column',PT),('32-column',C32),('Janet left-step',JAN)]:
    print("     %-18s E = %d"%(nm,E_of(S)))
print("\n  and the belt under three coordinatisations:\n")
B1={(p,q) for p,q in OCC}
B2={(p-q,p) for p,q in OCC}
B3={(p,p-q) for p,q in OCC}
for nm,S in [('(p, q)',B1),('(order, p)',B2),('(p, order)',B3)]:
    print("     %-18s E = %d"%(nm,E_of(S)))
print("="*86)
print("  VERDICT")
print("="*86)
print("""
  **THE CLAIM WAS WRONG. AN INDEX CAN TELL, AND BY TWO INTERNAL TESTS.**

     the periodic table : E = 36 in one layout, 106 in another, **0 in a
                          third**. E is REMOVABLE, so the absences are a
                          property of the drawing.

     the belt          : E = %d under (p,q), %d under (order,p), %d under
                          (p,order). **E is not removable**, and R refuses
                          the absences outright rather than admitting them.

  **REMOVABILITY IS THE TEST**, and it is computable from the cells alone.
  A defect of the index vanishes under some re-coordinatisation. A feature
  of the world survives every one.

  **CORRECTION 108.** 'An index cannot tell you which kind you are looking
  at. Only a second, external route can.' It can, and Chapter 1 already
  contains the demonstration -- the Janet table is exactly this test, run
  once, on one example, and never named as a test.
"""%(E_of(B1),E_of(B2),E_of(B3)))