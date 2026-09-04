import math, statistics as st
import numpy as np
from scipy import stats as SS
print("  CAN a(c) BE WRITTEN FROM Λ's OWN COUNTS ALONE?\n")
print("      the five exact crossing points, and the charge at which each")
print("      ladder reaches them:\n")
D=[(20,(4,0),(3,2),0.5774,2),(38,(5,0),(4,2),1.0000,2),
   (56,(6,0),(5,2),1.2168,2),(70,(6,0),(5,2),1.2168,3),
   (88,(7,0),(6,2),1.3938,3),(102,(7,0),(6,2),1.3938,5)]
L="spdfg"
print(f"      {'Nₑ':>4}{'occ':>6}{'riv':>6}{'a_cross':>10}{'at c':>7}"
      f"{'p_occ':>7}{'p_riv':>7}{'period':>8}")
for ne,(gn,gl),(rn,rl),ac,cc in D:
    per=1+sum(1 for b in (2,10,18,36,54,86) if ne>b)
    print(f"      {ne:>4}{f'{gn}{L[gl]}':>6}{f'{rn}{L[rl]}':>6}{ac:>10.4f}"
          f"{cc:>7}{gn-gl-1:>7}{rn-rl-1:>7}{per:>8}")
print()
print("  THE CROSSING CHARGE, AGAINST Λ's COUNTS\n")
NE=np.array([d[0] for d in D],float)
CC=np.array([d[4] for d in D],float)
PG=np.array([d[1][0]-d[1][1]-1 for d in D],float)
PR=np.array([d[2][0]-d[2][1]-1 for d in D],float)
PER=np.array([1+sum(1 for b in (2,10,18,36,54,86) if d[0]>b) for d in D],float)
# the number of electrons OUTSIDE the last noble gas closure
NOB=[2,10,18,36,54,86]
OUT=np.array([d[0]-max([b for b in NOB if b<d[0]],default=0) for d in D],float)
print(f"      {'Nₑ':>5}{'crosses at c':>14}{'p_occ':>7}{'p_riv':>7}"
      f"{'period':>8}{'Nₑ−closure':>12}")
for i,d in enumerate(D):
    print(f"      {d[0]:>5}{int(CC[i]):>14}{int(PG[i]):>7}{int(PR[i]):>7}"
          f"{int(PER[i]):>8}{int(OUT[i]):>12}")
print()
print(f"      {'model for crossing charge':<32}{'r²':>9}{'exact hits':>12}")
for nm,X in (("p_occ",PG),("p_riv",PR),("p_occ − p_riv",PG-PR),
             ("period",PER),("Nₑ − closure",OUT),("ln Nₑ",np.log(NE)),
             ("p_occ − p_riv, and period",None)):
    if X is None:
        M=np.column_stack([PG-PR,PER,np.ones(len(CC))])
        b,*_=np.linalg.lstsq(M,CC,rcond=None); pr=M@b
        r2=1-np.var(CC-pr)/np.var(CC)
        hits=sum(1 for a,b_ in zip(CC,pr) if abs(a-b_)<0.5)
        print(f"      {nm:<32}{r2:>9.4f}{hits:>9}/{len(CC)}")
        continue
    r=SS.linregress(X,CC); pr=r.intercept+r.slope*X
    hits=sum(1 for a,b_ in zip(CC,pr) if abs(a-b_)<0.5)
    print(f"      {nm:<32}{r.rvalue**2:>9.4f}{hits:>9}/{len(CC)}")
print()
print("  THE ANGULAR RATIO — is G²/F⁰ enumerable?\n")
print("      the angular part of G^k(l1,l2) is a 3j symbol squared:")
print("          ( l1 k l2 ; 0 0 0 )²")
print("      and F⁰'s angular part is 1 identically. so the RATIO's angular")
print("      factor is a pure Racah number — integers and surds.\n")
def tj(l1,k,l2):
    """(l1 k l2 ; 0 0 0)^2 by the standard closed form"""
    J=l1+k+l2
    if J%2: return 0.0
    g=J//2
    from math import factorial as f
    try:
        v=((-1)**g)*math.sqrt(f(J-2*l1)*f(J-2*k)*f(J-2*l2)/f(J+1))*\
          f(g)/(f(g-l1)*f(g-k)*f(g-l2))
    except ValueError: return 0.0
    return v*v
print(f"      {'pair':>7}{'k':>4}{'(l1 k l2;000)²':>18}{'  1/value'}")
for (l1,l2,k) in ((0,2,2),(0,1,1),(0,0,0),(2,2,2),(3,3,2)):
    v=tj(l1,k,l2)
    print(f"      {L[l1]+'/'+L[l2]:>7}{k:>4}{v:>18.6f}"
          f"{(1/v if v>1e-12 else float('inf')):>10.4f}")
print()
print("      s/d at k=2 : 1/5 exactly.  s/p at k=1 : 1/3.  s/s at k=0 : 1.")
print("      → the angular ratios ARE (2ℓ+1)^(−1) — pure enumeration.")
