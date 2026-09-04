import math, statistics as st
import numpy as np
from scipy import stats as SS
src=open("/tmp/xlim2.py",encoding="utf-8").read()
src=src[:src.index('print("  x AT EVERY ELECTRON COUNT')]
g={}; exec(src,g)
H=g["H"]; cfg=g["cfg"]; cp_=g["cp_"]; par=g["par"]; L="spdfg"
R=[]
for (Z,c,l,S),d in H.items():
    ne=Z-c+1
    if Z>92 or c>10 or l>5 or d<=0.02: continue
    if par(cfg(ne-1,c))>1: continue
    p=cp_(ne-1,l,c)
    if p<1: continue
    R.append((ne,c,l,p,d))
for ne,l,p,d in [(36,0,4,3.0417),(36,1,3,3.0827),(36,2,1,1.5208),
                 (54,0,5,4.0260),(54,1,4,3.5609),(54,2,2,2.4874),
                 (86,0,6,5.0477),(86,1,5,4.5082),(86,2,3,3.4146)]:
    R.append((ne,1,l,p,d))
NE=np.array([r[0] for r in R],float); C=np.array([r[1] for r in R],float)
P=np.array([r[3] for r in R],float); D=np.array([r[4] for r in R])
u=np.log(NE)-(2/3)*np.log(C)
Y=np.log(D/np.sqrt(P))
print(f"  IS THE CHARGE TERM REDUNDANT?   {len(R)} penetrating channels\n")
print("      δ = √p · F(u)          — ONE law in one variable")
print("      δ = √p · A(u)·c^(−x(u)) — TWO laws, the day's form\n")
print(f"      {'model':<40}{'par':>4}{'r²':>9}{'rms in ln':>11}")
def go(nm,X):
    Xm=np.column_stack(X+[np.ones(len(Y))])
    b,*_=np.linalg.lstsq(Xm,Y,rcond=None); r=Y-Xm@b
    print(f"      {nm:<40}{len(X)+1:>4}{1-np.var(r)/np.var(Y):>9.4f}"
          f"{float(np.sqrt(np.mean(r**2))):>11.4f}")
    return b,r
b1,r1=go("F(u): linear in u",[u])
b2,r2=go("F(u): quadratic in u",[u,u**2])
b3,r3=go("F(u): cubic in u",[u,u**2,u**3])
x=np.exp(-u/2)
b4,r4=go("A(u) quad + c^(−e^(−u/2))",[u,u**2,-x*np.log(np.maximum(C,1.0001))])
b5,r5=go("A(u) linear + c^(−e^(−u/2))",[u,-x*np.log(np.maximum(C,1.0001))])
print()
print("      the charge term's coefficient in the last two:")
print(f"          with quadratic A : {b4[2]:+.4f}")
print(f"          with linear A    : {b5[1]:+.4f}")
print("      (1.000 would mean the term is exactly as law 3 states it)")
print()
print("  AND THE TEST THAT MATTERS — does adding c help at all?\n")
n=len(Y)
for nm,rr,k in (("quadratic in u alone",r2,3),("quadratic + charge term",r4,4)):
    rss=float(np.sum(rr**2))
    print(f"      {nm:<28}RSS {rss:.4f}   AIC {n*math.log(rss/n)+2*k:.2f}")
F=((np.sum(r2**2)-np.sum(r4**2))/1)/(np.sum(r4**2)/(n-4))
print(f"\n      F-test for the charge term : F = {F:.3f}"
      f"   → {'the charge term EARNS its place' if F>4 else 'REDUNDANT — u alone suffices'}")
print()
print("  THE SINGLE PARAMETER\n")
b,r=b2,r2
u0=-b[0]/(2*b[1]) if b[1]<0 else float('nan')
print(f"      ln(δ/√p) = {b[0]:.4f}·u {b[1]:+.4f}·u² {b[2]:+.4f}")
print(f"      r² {1-np.var(r)/np.var(Y):.4f}   rms {float(np.sqrt(np.mean(r**2))):.4f}")
print(f"      u = ln(Nₑ/c^(2/3))  —  ONE variable carrying both Nₑ and c")
