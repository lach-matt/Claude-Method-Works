import math, statistics as st
import numpy as np
from scipy.optimize import curve_fit
from scipy import stats as SS
src=open("/tmp/AC.py",encoding="utf-8").read()
src=src[:src.index('print("  THE TWO-CONSTANT FORM')]
g={}; exec(src,g)
P,NE,D,C,LL,k=g["P"],g["NE"],g["D"],g["C"],g["LL"],g["k"]
L="spdfg"
Pk,Nk,Ck,Dk,Lk=P[k],NE[k],C[k],D[k],LL[k]
def M(_,A,kk): return A*np.sqrt(Pk)*Nk**kk*Ck**(-1.362/np.sqrt(Nk))
pr,_=curve_fit(M,np.arange(len(Dk)),Dk,p0=[0.26,0.45],maxfev=800000)
A,kk=pr; r=Dk-M(None,*pr)
print("  THE EQUATION, WITH k FREE AND C LOCKED\n")
print(f"      δ = A·√p·Nₑ^k·c^(−C/√Nₑ)      C = 1.362 locked\n")
print(f"      A = {A:.4f}   k = {kk:.4f}")
print(f"      {len(Dk)} channels · rms {float(np.sqrt(np.mean(r**2))):.4f}"
      f" · R² {1-np.var(r)/np.var(Dk):.4f}\n")
print("  IS k A RECOGNISABLE NUMBER?\n")
for nm,v in (("⅓",1/3),("⅖",0.4),("3/8",0.375),("0.3876 measured",kk),
             ("½",0.5),("5/13",5/13),("2/5.16",0.3876)):
    print(f"      {nm:<18}{v:>8.4f}   k − v = {kk-v:+.4f}")
print()
print("  NOW: DOES √p STILL HOLD WITH k FREE?\n")
def M2(_,A_,e_,kk_): return A_*Pk**e_*Nk**kk_*Ck**(-1.362/np.sqrt(Nk))
p2,_=curve_fit(M2,np.arange(len(Dk)),Dk,p0=[0.26,0.5,0.39],maxfev=800000)
r2=Dk-M2(None,*p2)
print(f"      A = {p2[0]:.4f}   e(p) = {p2[1]:.4f}   k = {p2[2]:.4f}")
print(f"      rms {float(np.sqrt(np.mean(r2**2))):.4f}"
      f" · R² {1-np.var(r2)/np.var(Dk):.4f}")
print(f"      (e = ½ locked gave rms {float(np.sqrt(np.mean(r**2))):.4f})\n")
print("  AND THE REMAINING ℓ STRUCTURE\n")
pred=M(None,*pr)
print(f"      {'ℓ':>3}{'n':>5}{'median δ/pred':>15}{'sd':>8}")
for l in range(5):
    m=Lk==l
    if m.sum()<5: continue
    print(f"      {L[l]:>3}{int(m.sum()):>5}{st.median(Dk[m]/pred[m]):>15.3f}"
          f"{st.pstdev(Dk[m]/pred[m]):>8.3f}")
q=Dk/pred
rr=SS.linregress(Lk,q)
print(f"\n      δ/pred against ℓ: slope {rr.slope:+.4f}  r² {rr.rvalue**2:.4f}"
      f"  p {rr.pvalue:.4f}")
print(f"      → {'a real ℓ trend remains' if rr.pvalue<0.05 else 'no significant ℓ trend'}")
print()
print("  THE FORM, SUMMARISED\n")
print(f"      δ = {A:.4f}·√p · Nₑ^{kk:.4f} · c^(−1.362/√Nₑ)")
print(f"      two fitted numbers (A, k) · one measured constant (C)")
print(f"      rms {float(np.sqrt(np.mean(r**2))):.4f} · R² {1-np.var(r)/np.var(Dk):.4f}"
      f" on {len(Dk)} penetrating channels")
np.save("/tmp/eqFINAL.npy",np.array([A,kk,1.362]))