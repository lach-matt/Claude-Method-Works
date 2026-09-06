import math, statistics as st
import numpy as np
from collections import defaultdict
from itertools import product
src=open("/tmp/xlim2.py",encoding="utf-8").read()
src=src[:src.index('print("  x AT EVERY ELECTRON COUNT')]
g={}; exec(src,g)
H=g["H"]; cfg=g["cfg"]; cp_=g["cp_"]; par=g["par"]; L="spdfg"
R=defaultdict(dict)
for (Z,c,l,S),d in H.items():
    ne=Z-c+1
    if Z>92 or c>10 or l>5: continue
    if par(cfg(ne-1,c))>1: continue
    R[(ne,l)][c]=d
print("  Λ_ion — THE NEUTRAL AGAINST ITS OWN ISOELECTRONIC ION\n")
print("      same Nₑ, same ℓ, same core CONFIGURATION — only c differs.")
print("      everything chemical that changes on ionisation is in this ratio.\n")
print(f"      {'Nₑ':>5}{'ℓ':>3}{'δ(c=1)':>10}{'δ(c=2)':>10}{'ratio':>9}{'δ(c=3)':>10}{'ratio':>9}")
P=[]
for (ne,l),d in sorted(R.items()):
    if 1 not in d or 2 not in d: continue
    r2=d[2]/d[1] if d[1]>0.02 else float("nan")
    r3=d[3]/d[1] if 3 in d and d[1]>0.02 else float("nan")
    print(f"      {ne:>5}{L[l]:>3}{d[1]:>10.4f}{d[2]:>10.4f}{r2:>9.4f}"
          f"{(d.get(3,float('nan'))):>10.4f}{r3:>9.4f}")
    P.append((ne,l,d[1],d[2],r2,r3))
print()
v2=[x[4] for x in P if x[4]==x[4]]
v3=[x[5] for x in P if x[5]==x[5]]
print(f"      δ(2)/δ(1) : {len(v2)} pairs · median {st.median(v2):.4f} · sd {st.pstdev(v2):.4f}")
if v3: print(f"      δ(3)/δ(1) : {len(v3)} pairs · median {st.median(v3):.4f} · sd {st.pstdev(v3):.4f}")
print()
print("  WHAT THE RATIO SHOULD BE, FROM THE EQUATION\n")
print("      δ ∝ c^(−x) with x = c^(1/3)/√Nₑ")
print(f"      {'Nₑ':>5}{'x(c=1)':>10}{'predicted 2^(−x)':>19}{'measured':>11}")
for ne,l,d1,d2,r2,r3 in P:
    if r2!=r2: continue
    x1=1/math.sqrt(ne); x2=2**(1/3)/math.sqrt(ne)
    pred=2**(-x2)
    print(f"      {ne:>5}{x1:>10.4f}{pred:>19.4f}{r2:>11.4f}")
print()
print("  THE CHEMICAL DIFFERENCE, STATED\n")
print("      a NEUTRAL atom is the unique species whose Rydberg series converges")
print("      to a HYDROGENIC limit: the outer electron sees exactly −1/r.")
print("      every neutral, Li to Rn, shares that asymptote.")
print()
print("      an ION never does. c ≥ 2 is a different asymptotic problem, and")
print("      the two are not connected by a continuous coordinate — which is")
print("      why the defect sits BETWEEN the sets and not inside either.")
print()
print("      chemically: the neutral has an electron affinity and can form an")
print("      anion; the ion is already a bonding product. the neutral is where")
print("      the periodic table's chemistry is defined, and it is exactly the")
print("      case Carcassés & González flag as failing Thomas–Fermi scaling.")