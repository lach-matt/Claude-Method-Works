import math, statistics as st
import numpy as np
print("  THE STATISTICS LANGUAGE, ASKED OF a(c)\n")
print("      brackets from the four ladders, one per (Nₑ, c):\n")
B={(20,1):(0.577,None),(20,2):(0.0,0.707),(20,3):(None,0.577),(20,4):(None,0.577),
   (38,1):(1.000,None),(38,2):(0.0,1.366),(38,3):(None,1.000),(38,4):(None,1.000),
   (56,1):(1.217,None),(56,2):(0.707,1.217),(56,3):(None,0.707),
   (88,1):(1.394,None),(88,2):(1.394,None),(88,3):(None,1.380)}
print(f"      {'Nₑ':>4}{'c':>3}{'a >':>9}{'a <':>9}{'midpoint':>11}")
MID={}
for k in sorted(B):
    lo,hi=B[k]
    m = (lo+hi)/2 if (lo is not None and hi is not None) else None
    if m is not None: MID[k]=m
    print(f"      {k[0]:>4}{k[1]:>3}"
          f"{(lo if lo is not None else float('-inf')):>9.3f}"
          f"{(hi if hi is not None else float('inf')):>9.3f}"
          f"{(m if m is not None else float('nan')):>11.3f}")
print()
print("  IS a(c) A STATISTIC OF THE CORE?  —  test 1: does it scale with Nₑ?\n")
print("      the two-sided brackets are the only ones that pin a value.\n")
print(f"      {'Nₑ':>4}{'c':>3}{'a (mid)':>10}{'Nₑ^(1/3)':>11}{'a·Nₑ^(-1/3)':>14}")
for k in sorted(MID):
    ne,c=k; m=MID[k]
    print(f"      {ne:>4}{c:>3}{m:>10.4f}{ne**(1/3):>11.4f}{m/ne**(1/3):>14.4f}")
print()
v=[MID[k]/k[0]**(1/3) for k in MID]
print(f"      a·Nₑ^(−1/3) : median {st.median(v):.4f}  sd {st.pstdev(v):.4f}"
      f"  range {min(v):.3f}–{max(v):.3f}")
print()
print("  TEST 2 — THE BRACKETS AS A DISTRIBUTION IN c\n")
print("      at c = 1 every bracket is a LOWER bound; at c = 3 every one is UPPER.")
print("      the bounds themselves, ordered by c:\n")
print(f"      {'c':>3}{'bounds':>34}{'median':>10}")
for c in (1,2,3):
    b=[]
    for k in sorted(B):
        if k[1]!=c: continue
        lo,hi=B[k]
        b.append(lo if lo is not None else hi)
    print(f"      {c:>3}{'  '.join(f'{x:.3f}' for x in b):>34}{st.median(b):>10.4f}")
print()
print("      c = 1 : the bounds are 0.577, 1.000, 1.217, 1.394 — RISING with Nₑ")
print("      c = 3 : the bounds are 0.577, 1.000, 0.707, 1.380 — NOT monotone")
print()
print("  TEST 3 — ARE THE c = 1 BOUNDS A FUNCTION OF Nₑ ?\n")
from scipy import stats as SS
NE=np.array([20,38,56,88],float); LB=np.array([0.577,1.000,1.217,1.394])
for nm,X in (("Nₑ",NE),("ln Nₑ",np.log(NE)),("Nₑ^(1/3)",NE**(1/3)),
             ("√Nₑ",np.sqrt(NE))):
    r=SS.linregress(X,LB)
    print(f"      lower bound vs {nm:<10}r² {r.rvalue**2:.4f}"
          f"   slope {r.slope:+.4f}   intercept {r.intercept:+.4f}")
print()
r=SS.linregress(np.log(NE),LB)
print(f"      best: a_min(c=1) = {r.intercept:.4f} + {r.slope:.4f}·ln Nₑ")
for ne in (20,38,56,88,108):
    print(f"          Nₑ = {ne:>3} : {r.intercept+r.slope*math.log(ne):.4f}")
print()
print("  READING\n")
print("      the c = 1 lower bounds ARE a smooth function of Nₑ — that is the")
print("      statistics language answering yes. the c = 3 upper bounds are not,")
print("      because three of the four are the SAME surds as the c = 1 bounds:")
print("      0.577 and 1.000 appear twice. those are the crossing values, and")
print("      they belong to the arithmetic half, not to the descent.")