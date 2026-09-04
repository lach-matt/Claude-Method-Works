import math, statistics as st, json
import numpy as np
from collections import defaultdict
from scipy import stats as SS
src=open("/tmp/xlim2.py",encoding="utf-8").read()
src=src[:src.index('print("  x AT EVERY ELECTRON COUNT')]
g={}; exec(src,g)
seq=g["seq"]; pm=g["pm"]; L="spdfg"
P=[]
for k in sorted(seq):
    d=seq[k]
    if len(d)<3 or pm[k]==0: continue
    cs=sorted(d)
    rr=SS.linregress(np.log(cs),np.log([d[c] for c in cs]))
    if rr.rvalue**2<0.80: continue
    ne=k[0]
    u=st.median([math.log(ne)-(2/3)*math.log(c) for c in cs])
    P.append((ne,k[1],u,-rr.slope,len(cs)))
NE=np.array([a for a,_,_,_,_ in P],float); U=np.array([c for _,_,c,_,_ in P])
X=np.array([d for _,_,_,d,_ in P])
print("  IS THE CHARGE EXPONENT A FUNCTION OF u RATHER THAN OF Nₑ?\n")
print(f"      {'Nₑ':>5}{'ℓ':>3}{'u':>8}{'x':>9}{'x·√Nₑ':>9}{'x·e^(u/2)':>12}")
for ne,l,u,x,n in P:
    print(f"      {ne:>5}{L[l]:>3}{u:>8.3f}{x:>9.4f}{x*math.sqrt(ne):>9.3f}"
          f"{x*math.exp(u/2):>12.3f}")
print()
print(f"      {'model':<28}{'r²':>9}{'rms':>9}")
for nm,V in (("x vs 1/√Nₑ",1/np.sqrt(NE)),("x vs e^(−u/2)",np.exp(-U/2)),
             ("x vs 1/√Nₑ and e^(−u/2)",None)):
    if V is None:
        M=np.column_stack([1/np.sqrt(NE),np.exp(-U/2),np.ones(len(X))])
        b,*_=np.linalg.lstsq(M,X,rcond=None); r=X-M@b
        print(f"      {nm:<28}{1-np.var(r)/np.var(X):>9.4f}"
              f"{float(np.sqrt(np.mean(r**2))):>9.4f}   [{b[0]:+.3f} {b[1]:+.3f}]")
    else:
        r=SS.linregress(V,X)
        print(f"      {nm:<28}{r.rvalue**2:>9.4f}"
              f"{float(np.std(X-(r.intercept+r.slope*V))):>9.4f}   slope {r.slope:+.3f}")
print()
C1=[x*math.sqrt(ne) for ne,_,_,x,_ in P]
C2=[x*math.exp(u/2) for ne,_,u,x,_ in P]
print(f"      C = x·√Nₑ      : median {st.median(C1):.4f}  sd {st.pstdev(C1):.4f}")
print(f"      C' = x·e^(u/2) : median {st.median(C2):.4f}  sd {st.pstdev(C2):.4f}")
print()
print("  THE SELF-REFERENCE\n")
print("      if x = C'·e^(−u/2) and u = ln(Nₑ) − ⅔·ln c, then")
print("          x = C'·(c^(2/3)/Nₑ)^(1/2) = C'·c^(1/3)/√Nₑ")
print("      and δ ∝ c^(−x) means the exponent of c depends on c itself.\n")
print("      solving:  ln δ ⊃ −C'·c^(1/3)·ln c / √Nₑ")
print("      the charge enters as c^(1/3)·ln c — a self-referential term.\n")
r1=SS.linregress(1/np.sqrt(NE),X); r2=SS.linregress(np.exp(-U/2),X)
print(f"      which carrier wins:  1/√Nₑ r² {r1.rvalue**2:.4f}"
      f"   ·   e^(−u/2) r² {r2.rvalue**2:.4f}")
print(f"      → {'u is the better carrier — the exponent IS self-referential' if r2.rvalue**2>r1.rvalue**2 else 'Nₑ is the better carrier — no self-reference'}")