import math, statistics as st
import numpy as np
from collections import defaultdict
from scipy import stats as SS
src=open("/tmp/xlim2.py",encoding="utf-8").read()
src=src[:src.index('print("  x AT EVERY ELECTRON COUNT')]
g={}; exec(src,g)
H=g["H"]; cfg=g["cfg"]; cp_=g["cp_"]; par=g["par"]; L="spdfg"
ROWS=[]
for (Z,c,l,S),d in H.items():
    ne=Z-c+1
    if Z>92 or c>10 or l>5: continue
    if par(cfg(ne-1,c))>1: continue
    p=cp_(ne-1,l,c)
    ROWS.append(dict(Z=Z,c=c,l=l,d=d,ne=ne,p=p))
P=np.array([r["p"] for r in ROWS],float); NE=np.array([r["ne"] for r in ROWS],float)
D=np.array([r["d"] for r in ROWS]); C=np.array([r["c"] for r in ROWS],float)
LL=np.array([r["l"] for r in ROWS],float)
k=(P>0)&(D>0.02)&(NE>=3)
print("  THE TWO-CONSTANT FORM   δ = A·√(pNₑ)·c^(−C/√Nₑ)\n")
print("      C is LOCKED at its measured value; only A is fitted.\n")
print(f"      {'C':>8}{'A':>9}{'rms':>9}{'R²':>9}")
best=None
for Cv in (1.25,1.30,1.3591,1.362,1.40,1.4163,1.45):
    x=Cv/np.sqrt(NE)
    B=np.sqrt(P*NE)*C**(-x)
    A=float(np.sum(B[k]*D[k])/np.sum(B[k]**2))
    r=D[k]-A*B[k]; s=float(np.sqrt(np.mean(r**2)))
    tag="  ← e/2" if abs(Cv-math.e/2)<0.002 else ("  ← median" if abs(Cv-1.362)<0.002 else "")
    print(f"      {Cv:>8.4f}{A:>9.4f}{s:>9.4f}{1-np.var(r)/np.var(D[k]):>9.4f}{tag}")
    if best is None or s<best[0]: best=(s,Cv,A)
s,Cv,A=best
print(f"\n      best on this data: C = {Cv:.4f}, A = {A:.4f}, rms {s:.4f}\n")
print("  NOW FIT BOTH FREELY AND SEE IF C MOVES\n")
from scipy.optimize import curve_fit
Pk,Nk,Ck,Dk,Lk=P[k],NE[k],C[k],D[k],LL[k]
def M(_,A_,C_): return A_*np.sqrt(Pk*Nk)*Ck**(-C_/np.sqrt(Nk))
pr,_=curve_fit(M,np.arange(len(Dk)),Dk,p0=[0.26,1.36],maxfev=800000)
r=Dk-M(None,*pr)
print(f"      A = {pr[0]:.4f}   C = {pr[1]:.4f}")
print(f"      rms {float(np.sqrt(np.mean(r**2))):.4f} · R² {1-np.var(r)/np.var(Dk):.4f}")
print(f"      C from the independent slope measurements: 1.362 ± 0.164")
print(f"      agreement: {abs(pr[1]-1.362)/0.164:.2f} sd\n")
print("  RESIDUALS OF THE LOCKED FORM\n")
x=1.362/np.sqrt(NE); B=np.sqrt(P*NE)*C**(-x)
A0=float(np.sum(B[k]*D[k])/np.sum(B[k]**2)); pred=A0*B
print(f"      A = {A0:.4f} with C = 1.362 locked\n")
print(f"      {'ℓ':>3}{'n':>5}{'median δ/pred':>15}{'sd':>8}")
for l in range(5):
    m=k&(LL==l)
    if m.sum()<5: continue
    print(f"      {L[l]:>3}{int(m.sum()):>5}{st.median(D[m]/pred[m]):>15.3f}{st.pstdev(D[m]/pred[m]):>8.3f}")
print()
print(f"      {'charge':>7}{'n':>5}{'median δ/pred':>15}")
for c_ in (1,2,3,4,5,6):
    m=k&(C==c_)
    if m.sum()<5: continue
    print(f"      {c_:>7}{int(m.sum()):>5}{st.median(D[m]/pred[m]):>15.3f}")
print()
print(f"      {'Nₑ band':>9}{'n':>5}{'median δ/pred':>15}")
for lo,hi in ((3,10),(10,20),(20,45),(45,90)):
    m=k&(NE>=lo)&(NE<hi)
    if m.sum()<5: continue
    print(f"      {f'{lo}–{hi}':>9}{int(m.sum()):>5}{st.median(D[m]/pred[m]):>15.3f}")
np.save("/tmp/AC.npy",np.array([A0,1.362]))