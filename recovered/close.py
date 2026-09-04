import math, statistics as st
import numpy as np
from collections import defaultdict
from scipy import stats as SS
src=open("/tmp/xlim2.py",encoding="utf-8").read()
src=src[:src.index('print("  x AT EVERY ELECTRON COUNT')]
g={}; exec(src,g)
seq=g["seq"]; pm=g["pm"]; L="spdfg"
print("  OPEN CELL 1 · DOES THE CHARGE EXPONENT DEPEND ON p ?\n")
P=[]
for k in sorted(seq):
    d=seq[k]
    if len(d)<3 or pm[k]==0: continue
    cs=sorted(d)
    rr=SS.linregress(np.log(cs),np.log([d[c] for c in cs]))
    if rr.rvalue**2<0.80: continue
    ne=k[0]; u=st.median([math.log(ne)-(2/3)*math.log(c) for c in cs])
    P.append((ne,k[1],pm[k],u,-rr.slope))
NE=np.array([a for a,_,_,_,_ in P],float); LL=np.array([b for _,b,_,_,_ in P],float)
PP=np.array([c for _,_,c,_,_ in P],float); U=np.array([d for _,_,_,d,_ in P])
X=np.array([e for _,_,_,_,e in P])
print(f"      {'Nₑ':>5}{'ℓ':>3}{'p':>3}{'u':>8}{'x':>9}{'x·e^(u/2)':>12}")
for ne,l,p,u,x in P:
    print(f"      {ne:>5}{L[l]:>3}{p:>3}{u:>8.3f}{x:>9.4f}{x*math.exp(u/2):>12.4f}")
print()
r0=SS.linregress(np.exp(-U/2),X)
print(f"      x vs e^(−u/2) alone      : r² {r0.rvalue**2:.4f}  slope {r0.slope:.4f}")
M=np.column_stack([np.exp(-U/2),PP,np.ones(len(X))])
b,*_=np.linalg.lstsq(M,X,rcond=None); r=X-M@b
print(f"      + p                       : r² {1-np.var(r)/np.var(X):.4f}"
      f"   slope_p {b[1]:+.5f}")
t=b[1]/ (np.sqrt(np.sum(r**2)/(len(X)-3)) * np.sqrt(np.linalg.inv(M.T@M)[1,1]))
print(f"      t-statistic on p          : {t:+.3f}"
      f"   → {'p MATTERS' if abs(t)>2 else 'p does NOT matter — CELL CLOSED'}")
C2=X*np.exp(U/2)
rp=SS.linregress(PP,C2)
print(f"\n      C′ = x·e^(u/2) against p : slope {rp.slope:+.4f}  r² {rp.rvalue**2:.4f}"
      f"  p {rp.pvalue:.3f}")
print(f"      → {'C′ drifts with p' if rp.pvalue<0.05 else 'C′ is INDEPENDENT of p — the cell closes'}")
print()
print("  OPEN CELL 2 · DOES h SCALE WITH ℓ − ℓ_core ?\n")
print("      h(d) = 0.40 measured at K→Ca · h(f) = 0.468 from La's ⟨r⟩")
print(f"      ratio {0.468/0.40:.4f}\n")
for nm,v in (("√(ℓ(ℓ+1)) ratio d→f",math.sqrt(12/6)),
             ("ℓ(ℓ+1) ratio",12/6),
             ("(ℓ+1)/(ℓ+1) ratio",4/3),
             ("√((ℓ+1)/(ℓ+1))",math.sqrt(4/3)),
             ("(2ℓ+1) ratio",7/5),
             ("√((2ℓ+1)/(2ℓ+1))",math.sqrt(7/5)),
             ("ℓ/ℓ",3/2),("√(ℓ/ℓ)",math.sqrt(1.5))):
    print(f"      {nm:<26}{v:>8.4f}   measured/pred = {(0.468/0.40)/v:.3f}")
print()
print("      → the measured 1.170 sits closest to √((2ℓ+1)/(2ℓ+1)) = 1.183")
print("        and √((ℓ+1)/(ℓ+1)) = 1.155.  the BARRIER scaling √(ℓ(ℓ+1)) = 1.414")
print("        is far off, so h does NOT follow the barrier.\n")
print("      h(ℓ) = h₀·√(2ℓ+1)  ⇒  h₀ = {:.4f} from d, {:.4f} from f".format(
      0.40/math.sqrt(5), 0.468/math.sqrt(7)))
print("      h(ℓ) = h₀·√(ℓ+1)   ⇒  h₀ = {:.4f} from d, {:.4f} from f".format(
      0.40/math.sqrt(3), 0.468/math.sqrt(4)))