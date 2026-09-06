import math, statistics as st
import numpy as np
from collections import defaultdict
from scipy import stats as SS
src=open("regimes.py",encoding="utf-8").read()
src=src[:src.index("from collections import Counter")]
g={}; exec(src,g)
ROWS=list(g["ROWS"])+[
  dict(Z=81,c=2,l=1,d=3.7167,ne=80,p=4,n0=6,non=6,T=9999,reg=2,b24=0.0),
  dict(Z=82,c=3,l=1,d=3.5402,ne=80,p=4,n0=6,non=6,T=9999,reg=2,b24=0.0),
  dict(Z=83,c=4,l=1,d=3.3684,ne=80,p=4,n0=6,non=6,T=9999,reg=2,b24=0.0)]
L="spdfg"
seq=defaultdict(dict); pm={}
for r in ROWS:
    if r["d"]>0.02:
        seq[(r["ne"],r["l"])][r["c"]]=r["d"]; pm[(r["ne"],r["l"])]=r["p"]
print("  x AT THE SMALL-Nₑ LIMIT — the largest coefficient any species can have\n")
print(f"      {'Nₑ':>4}{'ℓ':>3}{'p':>3}{'chg':>5}{'x':>9}{'r²':>8}   species")
EL={2:"He-like",3:"Li-like",4:"Be-like",5:"B-like",6:"C-like",11:"Na-like",
    12:"Mg-like",13:"Al-like",19:"K-like",30:"Zn-like",37:"Rb-like",80:"Hg-like"}
PTS=[]
for k in sorted(seq):
    d=seq[k]
    if len(d)<3 or pm[k]==0: continue
    cs=sorted(d)
    rr=SS.linregress(np.log(cs),np.log([d[c] for c in cs]))
    if rr.rvalue**2<0.80: continue
    PTS.append((k[0],k[1],pm[k],-rr.slope,rr.rvalue**2,len(cs)))
    print(f"      {k[0]:>4}{L[k[1]]:>3}{pm[k]:>3}{len(cs):>5}{-rr.slope:>9.4f}"
          f"{rr.rvalue**2:>8.4f}   {EL.get(k[0],'')}")
print()
print("  THE SEQUENCE, BY Nₑ — one value per electron count\n")
by=defaultdict(list)
for ne,l,p,x,r2,n in PTS: by[ne].append(x)
S=[(ne,st.median(v)) for ne,v in sorted(by.items())]
print(f"      {'Nₑ':>4}{'x':>9}{'1/x':>9}{'x·Nₑ':>9}{'x·√Nₑ':>9}{'x·Nₑ^(1/3)':>12}")
for ne,x in S:
    print(f"      {ne:>4}{x:>9.4f}{1/x:>9.3f}{x*ne:>9.3f}{x*math.sqrt(ne):>9.3f}"
          f"{x*ne**(1/3):>12.3f}")
print()
print("  IS 1/x LINEAR IN SOMETHING?\n")
ne=np.array([a for a,_ in S],float); x=np.array([b for _,b in S])
for nm,X in (("Nₑ",ne),("√Nₑ",np.sqrt(ne)),("Nₑ^(1/3)",ne**(1/3)),
             ("ln Nₑ",np.log(ne))):
    r=SS.linregress(X,1/x)
    print(f"      1/x vs {nm:<10}{r.intercept:>9.3f} {r.slope:+.4f}·{nm:<9}"
          f"r² {r.rvalue**2:.4f}")
print()
print("  AND WHAT 1/x PREDICTS AT THE LIMITS\n")
r=SS.linregress(np.sqrt(ne),1/x)
print(f"      1/x = {r.intercept:.3f} {r.slope:+.4f}·√Nₑ    r² {r.rvalue**2:.4f}")
for n_ in (1,2,3,12,20,40,80,118):
    v=1/(r.intercept+r.slope*math.sqrt(n_))
    print(f"          Nₑ = {n_:>3} :  x = {v:>7.3f}")