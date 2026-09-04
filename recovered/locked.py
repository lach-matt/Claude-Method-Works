import math, statistics as st
import numpy as np
src=open("regimes.py",encoding="utf-8").read()
src=src[:src.index("from collections import Counter")]
g={}; exec(src,g)
ROWS=list(g["ROWS"])+[
  dict(Z=81,c=2,l=1,d=3.7167,ne=80,p=4,n0=6,non=6,T=9999,reg=2,b24=0.0),
  dict(Z=82,c=3,l=1,d=3.5402,ne=80,p=4,n0=6,non=6,T=9999,reg=2,b24=0.0),
  dict(Z=83,c=4,l=1,d=3.3684,ne=80,p=4,n0=6,non=6,T=9999,reg=2,b24=0.0)]
L="spdfg"
print("  LOCKED QUANTITIES — measured independently, never refitted\n")
print("      x(Nₑ) = 0.8600 − 0.1802·ln Nₑ    19 isoelectronic sequences")
print("      exponent ½ on √(p·Nₑ)             derived, WKB phase")
print("      regime-2 factor 1.234             four independent routes")
print("      h(d) = 0.40                       K → Ca, charge-normalised")
print("      h(f) = 0.468                      La ⟨r⟩ = 0.7 a₀")
print("      switch centre −1.5, width 0.40    the d table at D = −2…+1\n")
print("  FREE — one number\n")
print("      A, the amplitude\n")
P=np.array([r["p"] for r in ROWS],float); NE=np.array([r["ne"] for r in ROWS],float)
D=np.array([r["d"] for r in ROWS]); C=np.array([r["c"] for r in ROWS],float)
RG=np.array([r["reg"] for r in ROWS]); LL=np.array([r["l"] for r in ROWS],float)
k=(P>0)&(D>0.02)
X=np.maximum(0.8600-0.1802*np.log(NE),0.02)
G=np.where(RG==2,1.234,1.0)
BASIS=G*np.sqrt(P*NE)*C**(-X)
A=float(np.sum(BASIS[k]*D[k])/np.sum(BASIS[k]**2))
pred=A*BASIS
r=D[k]-pred[k]
print(f"      A = {A:.4f}")
print(f"      {int(k.sum())} channels · rms {float(np.sqrt(np.mean(r**2))):.4f}"
      f" · R² {1-np.var(r)/np.var(D[k]):.4f}\n")
print("  THE RESIDUAL STRUCTURE — where a locked fit is still wrong\n")
print(f"      {'ℓ':>3}{'n':>5}{'median δ/pred':>15}{'sd':>8}")
for l in range(5):
    m=k&(LL==l)
    if m.sum()<5: continue
    q=D[m]/pred[m]
    print(f"      {L[l]:>3}{int(m.sum()):>5}{st.median(q):>15.3f}{st.pstdev(q):>8.3f}")
print()
print(f"      {'regime':>7}{'n':>5}{'median δ/pred':>15}{'sd':>8}")
for rg in (1,2):
    m=k&(RG==rg)
    if m.sum()<5: continue
    q=D[m]/pred[m]
    print(f"      {rg:>7}{int(m.sum()):>5}{st.median(q):>15.3f}{st.pstdev(q):>8.3f}")
print()
print(f"      {'charge':>7}{'n':>5}{'median δ/pred':>15}")
for c in (1,2,3,4,5,6):
    m=k&(C==c)
    if m.sum()<5: continue
    print(f"      {c:>7}{int(m.sum()):>5}{st.median(D[m]/pred[m]):>15.3f}")
print()
print(f"      {'Nₑ band':>9}{'n':>5}{'median δ/pred':>15}")
for lo,hi in ((1,10),(10,20),(20,40),(40,90)):
    m=k&(NE>=lo)&(NE<hi)
    if m.sum()<5: continue
    print(f"      {f'{lo}–{hi}':>9}{int(m.sum()):>5}{st.median(D[m]/pred[m]):>15.3f}")
np.save("/tmp/A_locked.npy",np.array([A]))