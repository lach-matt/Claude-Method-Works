import math, statistics as st
import numpy as np
from collections import defaultdict
from scipy import stats as SS
src=open("/tmp/xlim2.py",encoding="utf-8").read()
src=src[:src.index('print("  x AT EVERY ELECTRON COUNT')]
g={}; exec(src,g)
seq=g["seq"]; pm=g["pm"]; L="spdfg"
PTS=[]
for k in sorted(seq):
    d=seq[k]
    if len(d)<3 or pm[k]==0: continue
    cs=sorted(d)
    rr=SS.linregress(np.log(cs),np.log([d[c] for c in cs]))
    if rr.rvalue**2<0.80: continue
    PTS.append((k[0],k[1],pm[k],-rr.slope,len(cs)))
print("  C = x·√Nₑ  ON EVERY PENETRATING MEASUREMENT\n")
print(f"      {'Nₑ':>4}{'ℓ':>3}{'p':>3}{'chg':>5}{'x':>8}{'C = x√Nₑ':>11}")
CC=[]
for ne,l,p,x,n in PTS:
    C=x*math.sqrt(ne)
    flag="  ← outer-well d" if (l>=2 and p<=1) else ""
    print(f"      {ne:>4}{L[l]:>3}{p:>3}{n:>5}{x:>8.4f}{C:>11.4f}{flag}")
    if not (l>=2 and p<=1): CC.append((ne,l,C,n))
print()
v=[c for _,_,c,_ in CC]; w=[n for _,_,_,n in CC]
print(f"      excluding outer-well d : {len(v)} measurements")
print(f"      C = {st.median(v):.4f}   mean {st.mean(v):.4f}   sd {st.pstdev(v):.4f}")
print(f"      weighted mean = {sum(a*b for a,b in zip(v,w))/sum(w):.4f}")
print(f"      range {min(v):.3f} – {max(v):.3f}\n")
ne=np.array([a for a,_,_,_ in CC],float); C=np.array([c for _,_,c,_ in CC])
r=SS.linregress(np.log(ne),C)
print(f"      C against ln Nₑ : slope {r.slope:+.4f}  r² {r.rvalue**2:.4f}"
      f"  p {r.pvalue:.4f}")
print(f"      → {'C DRIFTS with Nₑ' if r.pvalue<0.05 else 'C is CONSTANT — no trend'}\n")
print("  AND WHAT C MIGHT BE\n")
Cm=st.median(v)
for nm,val in (("4/π",4/math.pi),("√φ",math.sqrt((1+5**0.5)/2)),("2/√e",2/math.sqrt(math.e)),
               ("π/√6",math.pi/math.sqrt(6)),("5/4",1.25),("√(3/2)",math.sqrt(1.5)),
               ("e/2",math.e/2),("2√2/π·π/2",math.sqrt(2))):
    print(f"      {nm:<10}{val:>8.4f}   C/val = {Cm/val:.3f}")
print()
print("  THE HELIUM-LIKE LIMIT — x at Nₑ = 2\n")
print(f"      predicted x(2) = C/√2 = {Cm/math.sqrt(2):.4f}\n")
d2=seq.get((2,0)) or {}
print(f"      measured He-like s sequence: {len(d2)} charge states")
if len(d2)>=3:
    cs=sorted(d2)
    rr=SS.linregress(np.log(cs),np.log([d2[c] for c in cs]))
    print(f"      x = {-rr.slope:.4f}   r² {rr.rvalue**2:.4f}   C = {-rr.slope*math.sqrt(2):.4f}")
for l in (1,2,3):
    dd=seq.get((2,l)) or {}
    if len(dd)<3: continue
    cs=sorted(dd)
    rr=SS.linregress(np.log(cs),np.log([dd[c] for c in cs]))
    print(f"      ℓ={L[l]}: x = {-rr.slope:.4f}   r² {rr.rvalue**2:.4f}"
          f"   C = {-rr.slope*math.sqrt(2):.4f}   ({len(dd)} charges)")