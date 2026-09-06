import math, statistics as st, json
import numpy as np
from scipy import stats as SS
O=[tuple(x) for x in json.load(open("/tmp/step1.json"))]
NE=np.array([o[2] for o in O],float); C=np.array([o[1] for o in O],float)
A=np.array([o[3] for o in O]); LA=np.log(A)
print("  IS β = ⅔ ?   a fine scan, and the log-likelihood profile\n")
print(f"      {'β':>7}{'r²':>10}{'rms':>9}")
best=None
for be in np.arange(0.50,0.85,0.01):
    u=np.log(NE)-be*np.log(C)
    X=np.column_stack([u,u**2,np.ones(len(u))])
    b,*_=np.linalg.lstsq(X,LA,rcond=None); r=LA-X@b
    q=1-np.var(r)/np.var(LA); s=float(np.sqrt(np.mean(r**2)))
    if best is None or s<best[0]: best=(s,be,b,q)
    if abs(be*100-round(be*100))<1e-9 and round(be*100)%2==0:
        m="  ← ⅔" if abs(be-2/3)<0.006 else ("  ← best" if abs(be-0.65)<0.001 else "")
        print(f"      {be:>7.2f}{q:>10.4f}{s:>9.4f}{m}")
s,be,b,q=best
print(f"\n      minimum at β = {be:.2f}, rms {s:.4f}")
for tst in (0.5,2/3,0.75,1.0):
    u=np.log(NE)-tst*np.log(C)
    X=np.column_stack([u,u**2,np.ones(len(u))])
    bb,*_=np.linalg.lstsq(X,LA,rcond=None); r=LA-X@bb
    print(f"      β = {tst:.4f} : rms {float(np.sqrt(np.mean(r**2))):.4f}"
          f"   r² {1-np.var(r)/np.var(LA):.4f}")
print()
print("  THE FORM WITH β = ⅔ EXACTLY\n")
u=np.log(NE)-(2/3)*np.log(C)
X=np.column_stack([u,u**2,np.ones(len(u))])
b,*_=np.linalg.lstsq(X,LA,rcond=None); r=LA-X@b
print(f"      ln a = {b[0]:.4f}·u {b[1]:+.4f}·u² {b[2]:+.4f}   u = ln(Nₑ/c^(2/3))")
print(f"      r² {1-np.var(r)/np.var(LA):.4f}   rms {float(np.sqrt(np.mean(r**2))):.4f}\n")
print(f"      and δ = a·√p, so:\n")
print(f"      δ = √p · exp[ {b[2]:.4f} {b[0]:+.4f}·u {b[1]:+.4f}·u² ]\n")
print("  WHAT ⅔ MIGHT MEAN\n")
print("      Nₑ/c^(2/3) — and the Thomas–Fermi length is b = 0.885·Z^(−1/3),")
print("      so a volume goes as Z^(−1), an area as Z^(−2/3).")
print("      Nₑ/c^(2/3) is an electron count per unit AREA of the core boundary.\n")
print("  AND THE k-DRIFT REPRODUCED WITH NO CROSS TERM\n")
print(f"      k(c) = ∂ln a/∂ln Nₑ = {b[0]:.4f} {2*b[1]:+.4f}·u\n")
print(f"      {'charge':>7}{'median u':>10}{'k predicted':>13}{'k measured':>12}")
MEAS={1:0.572,2:0.705,3:0.828,4:1.132}
for c in (1,2,3,4):
    m=C==c
    if m.sum()<3: continue
    uu=st.median(u[m])
    print(f"      {c:>7}{uu:>10.3f}{b[0]+2*b[1]*uu:>13.3f}{MEAS[c]:>12.3f}")
np.save("/tmp/beta.npy",b)