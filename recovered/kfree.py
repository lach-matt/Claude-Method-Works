import math, statistics as st
import numpy as np
from scipy.optimize import curve_fit
src=open("/tmp/AC.py",encoding="utf-8").read()
src=src[:src.index('print("  THE TWO-CONSTANT FORM')]
g={}; exec(src,g)
P,NE,D,C,LL,k=g["P"],g["NE"],g["D"],g["C"],g["LL"],g["k"]
L="spdfg"
Pk,Nk,Ck,Dk,Lk=P[k],NE[k],C[k],D[k],LL[k]
print("  ONE PARAMETER MOVED: the Nₑ exponent, with C = 1.362 LOCKED\n")
def M(_,A,kk): return A*np.sqrt(Pk)*Nk**kk*Ck**(-1.362/np.sqrt(Nk))
best=None
for p0 in ([0.26,0.5],[0.3,0.45],[0.25,0.4]):
    try:
        pr,_=curve_fit(M,np.arange(len(Dk)),Dk,p0=p0,maxfev=800000)
        r=Dk-M(None,*pr); s=float(np.sqrt(np.mean(r**2)))
        if best is None or s<best[1]: best=(pr,s)
    except Exception: pass
pr,s=best; r=Dk-M(None,*pr)
print(f"      δ = A·√p·Nₑ^k·c^(−1.362/√Nₑ)")
print(f"      A = {pr[0]:.4f}   k = {pr[1]:.4f}")
print(f"      rms {s:.4f} · R² {1-np.var(r)/np.var(Dk):.4f}")
print(f"      (k = ½ locked gave rms 0.1736 · R² 0.9649)\n")
pred=M(None,*pr)
print(f"      {'Nₑ band':>9}{'n':>5}{'median δ/pred':>15}")
for lo,hi in ((3,10),(10,20),(20,45),(45,90)):
    m=(Nk>=lo)&(Nk<hi)
    if m.sum()<5: continue
    print(f"      {f'{lo}–{hi}':>9}{int(m.sum()):>5}{st.median(Dk[m]/pred[m]):>15.3f}")
print()
print(f"      {'ℓ':>3}{'n':>5}{'median δ/pred':>15}")
for l in range(5):
    m=Lk==l
    if m.sum()<5: continue
    print(f"      {L[l]:>3}{int(m.sum()):>5}{st.median(Dk[m]/pred[m]):>15.3f}")
print()
print(f"      {'charge':>7}{'n':>5}{'median δ/pred':>15}")
for c_ in (1,2,3,4):
    m=Ck==c_
    if m.sum()<5: continue
    print(f"      {c_:>7}{int(m.sum()):>5}{st.median(Dk[m]/pred[m]):>15.3f}")
print()
print("  WHAT k IMPLIES FOR THE CORE RADIUS\n")
kk=pr[1]
print(f"      the WKB phase is √(Z·r_core), so δ ∝ Nₑ^k means r_core ∝ Nₑ^(2k−1)")
print(f"      k = {kk:.4f}  ⇒  r_core ∝ Nₑ^{2*kk-1:+.4f}")
print(f"      k = ½ exactly ⇒ r_core constant")
print(f"      Thomas–Fermi (k = ⅓) ⇒ r_core ∝ Nₑ^(−1/3)\n")
for n_ in (3,20,80):
    print(f"          Nₑ = {n_:>3} :  r_core ratio to Nₑ=3 = {(n_/3)**(2*kk-1):.3f}")
print()
print("      atomic radii across the table vary by roughly a factor of 2–3,")
print("      not 10, so a small positive exponent is what the chemistry says.")
np.save("/tmp/kfree.npy",pr)