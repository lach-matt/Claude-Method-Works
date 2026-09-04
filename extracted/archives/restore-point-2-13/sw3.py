import math, statistics as st
import numpy as np
from scipy import stats as SS
src=open("/tmp/sw2.py",encoding="utf-8").read()
src=src[:src.index('print("  THE SWITCH, CHARGE-NORMALISED')]
g={}; exec(src,g)
rows=g["rows"]; L="spdfgh"
for r in rows:
    ne=r["ne"]; t=math.log(r["c"]+1)/r["c"]
    den=((ne-1)/ne)*math.sqrt(ne)*t
    r["y"]=r["d"]/den if den>1e-9 else float("nan")
print("  THE SWITCH AS BARRIER TUNNELLING:   y = A·exp(D/w)\n")
print("      An orbital below its threshold sits in the outer well. Its amplitude")
print("      inside the core is set by tunnelling through the centrifugal barrier,")
print("      which is EXPONENTIAL in the barrier's thickness — and the thickness")
print("      falls linearly as Z rises toward the threshold.\n")
print(f"      {'ℓ':>3}{'n':>5}{'A':>10}{'w':>9}{'r²':>8}{'  A = y at D = 0'}")
P={}
for l in (2,3):
    v=[x for x in rows if x["l"]==l and x["y"]==x["y"] and x["y"]>1e-4]
    if len(v)<8: continue
    D=np.array([x["D"] for x in v],float); ly=np.log(np.array([x["y"] for x in v]))
    r=SS.linregress(D,ly)
    A=math.exp(r.intercept); w=1/r.slope
    print(f"      {L[l]:>3}{len(v):>5}{A:>10.4f}{w:>9.3f}{r.rvalue**2:>8.4f}")
    P[l]=(A,w)
print()
print("  AND THE TWO ℓ TOGETHER — is w the same?\n")
allv=[x for x in rows if x["l"] in (2,3) and x["y"]==x["y"] and x["y"]>1e-4]
D=np.array([x["D"] for x in allv],float)
LV=np.array([x["l"] for x in allv],float)
ly=np.log(np.array([x["y"] for x in allv]))
X=np.column_stack([D,LV,np.ones(len(allv))])
b,*_=np.linalg.lstsq(X,ly,rcond=None)
res=ly-X@b
print(f"      ln y = {b[0]:+.5f}·D {b[1]:+.4f}·ℓ {b[2]:+.4f}")
print(f"      w = 1/{b[0]:.5f} = {1/b[0]:.3f}   ·   r² {1-np.var(res)/np.var(ly):.4f}"
      f"   ·   {len(allv)} channels")
print()
print("  THE FORM, MEASURED\n")
print(f"      δ = A·exp((Z−T)/w) · (Nₑ−1)/Nₑ · √Nₑ · ln(c+1)/c")
print(f"      A = {math.exp(b[2]+2*b[1]):.4f} at ℓ = d, {math.exp(b[2]+3*b[1]):.4f} at ℓ = f")
print(f"      w = {1/b[0]:.2f} in Z — the collapse e-folds every {1/b[0]:.1f} protons")
np.save("/tmp/tunnel.npy",b)
print()
print("  CHECK: does it reproduce the measured values at the threshold?\n")
print(f"      {'ℓ':>3}{'D':>5}{'species':>10}{'measured δ':>13}{'form':>9}")
for x in sorted([z for z in allv if -3<=z["D"]<=1],key=lambda z:(z["l"],z["D"])):
    ne=x["ne"]; t=math.log(x["c"]+1)/x["c"]
    pred=math.exp(b[2]+b[1]*x["l"]+b[0]*x["D"])*((ne-1)/ne)*math.sqrt(ne)*t
    print(f"      {L[x['l']]:>3}{x['D']:>5}{g['EL'].get(x['Z'],x['Z']):>7}"
          f"{g['RO'].get(x['c'],x['c']):>3}{x['d']:>13.4f}{pred:>9.4f}")
