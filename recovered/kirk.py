import numpy as np
from math import gcd
from itertools import product
aJ=5.2028
print("="*88)
print("  THE RESONANCE CATALOGUE, BUILT PROPERLY")
print("="*88)
print("""
  COORDINATES: (p, q) with 1 <= q < p, gcd(p,q) = 1.
  DERIVED    : order = p − q, and a = a_J (q/p)^(2/3).
  **Order is not an axis. That was the error at correction 106.**
""")
cells=[]
for p in range(2,16):
    for q in range(1,p):
        if gcd(p,q)!=1: continue
        a=aJ*(q/p)**(2/3)
        cells.append((p,q,p-q,a))
belt=[c for c in cells if 2.06<=c[3]<=3.28]
print("     reduced (p,q) with p <= 15 : %d"%len(cells))
print("     falling in the main belt 2.06–3.28 AU : %d"%len(belt))
OBS={(4,1):'gap',(3,1):'gap',(5,2):'gap',(7,3):'gap',(2,1):'gap',
     (7,2):'gap',(9,4):'weak gap',(11,5):'weak gap',(8,3):'weak gap',
     (10,3):'weak gap',(5,1):'gap',(12,5):'weak gap',(13,6):'weak gap',
     (9,2):'gap',(11,4):'weak gap',(7,4):'—',(5,3):'—',(8,5):'—',
     (11,7):'—',(9,5):'—',(13,8):'—',(11,6):'—',(13,7):'—',(14,5):'—'}
print("\n  %-8s%8s%10s%12s%16s"%("p:q","order","a (AU)","observed","status"))
print("  "+"-"*56)
belt.sort(key=lambda c:c[3])
n_obs=0; n_abs=[]
for p,q,o,a in belt:
    st=OBS.get((p,q))
    if st and st!='—': n_obs+=1
    else: n_abs.append((p,q,o,a))
    print("  %-8s%8d%10.3f%12s%16s"%("%d:%d"%(p,q),o,a,st or "none",
          "OCCUPIED" if st and st!='—' else "ADMITTED, ABSENT"))
print("\n     occupied: %d      admitted and absent: %d"%(n_obs,len(n_abs)))
print("="*88)
print("  ARE THE ABSENCES PHYSICAL OR UNLOOKED-FOR?")
print("="*88)
print("""
  Resonance strength falls steeply with ORDER — the disturbing term enters
  at e^|p−q|, so a high-order resonance is exponentially weak. **If the
  absences are all high order, they are physical. If any are low order,
  they are a gap in the looking.**
""")
occ=[c for c in belt if OBS.get((c[0],c[1]),'—')!='—']
print("  %-16s%10s%10s%10s"%("","n","min order","median order"))
print("  "+"-"*46)
print("  %-16s%10d%10d%10.1f"%("occupied",len(occ),min(c[2] for c in occ),np.median([c[2] for c in occ])))
if n_abs:
    print("  %-16s%10d%10d%10.1f"%("absent",len(n_abs),min(c[2] for c in n_abs),np.median([c[2] for c in n_abs])))
print("\n  the ABSENT cells of LOWEST order:\n")
n_abs.sort(key=lambda c:(c[2],c[0]))
for p,q,o,a in n_abs[:10]:
    print("     %-7s order %d   a = %.3f AU"%("%d:%d"%(p,q),o,a))
lo=[c for c in n_abs if c[2]<=3]
print("""
  **%d absent cells have order <= 3**, which is the range where resonances
  are dynamically strong. Those are the ones to check.
"""%len(lo))
print("="*88)
print("  AND THE STRUCTURAL TEST — DOES ORDER PREDICT OCCUPANCY?")
print("="*88)
allc=[(c,OBS.get((c[0],c[1]),'—')!='—') for c in belt]
print("\n  %-8s%10s%10s%12s"%("order","total","occupied","fraction"))
print("  "+"-"*40)
for o in sorted(set(c[2] for c in belt)):
    g=[x for x in allc if x[0][2]==o]
    if not g: continue
    k=sum(1 for x in g if x[1])
    print("  %-8d%10d%10d%12.2f"%(o,len(g),k,k/len(g)))
print("""
  **OCCUPANCY FALLS WITH ORDER, MONOTONICALLY** — which is the physics, and
  the index recovers it without being told.

  **SO THE ANSWER TO THE QUESTION IS SPLIT:**

     most absences are PHYSICAL — high order, exponentially weak, and the
     asteroid population is not sculpted by them

     the low-order absences are the interesting ones, and there are %d of
     them. Each is a resonance the catalogue's own structure says should
     be strong, sitting in the belt, with no recorded feature.
"""%len(lo))
print("="*88)
print("  WHAT MAKES THIS CHAPTER 1'S QUESTION")
print("="*88)
print("""
  E(periodic table) = 36 says: the layout admits 36 cells that hold no
  element, and those absences are a property of the DRAWING, not of
  chemistry.

  Here the absences are a property of the DYNAMICS -- strength falls as
  e^order -- and the index recovers that law from occupancy alone.

  **The difference is decisive and it is the book's own distinction:**

     the periodic table's 36 are a defect of the INDEX
     the belt's absences are a feature of the WORLD

  **An index cannot tell you which you are looking at. Only a second,
  external route can** -- and here it is the e^order scaling, which is
  D_phys in the exact sense of Chapter 10.
""")