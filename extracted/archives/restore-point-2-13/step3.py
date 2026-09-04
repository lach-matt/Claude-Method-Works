import math, statistics as st, json
import numpy as np
from scipy import stats as SS
O=[tuple(x) for x in json.load(open("/tmp/step1.json"))]
NE=np.array([o[2] for o in O],float); C=np.array([o[1] for o in O],float)
A=np.array([o[3] for o in O]); LA=np.log(A)
LN=np.log(NE); LC=np.log(C)
print("  STEP 3 · THE SINGULAR EQUATION FROM THE 41 CONSTANTS\n")
print(f"      {'model for ln a':<44}{'par':>4}{'r²':>9}{'rms':>9}")
def go(nm,cols):
    X=np.column_stack(cols+[np.ones(len(LA))])
    b,*_=np.linalg.lstsq(X,LA,rcond=None); r=LA-X@b
    print(f"      {nm:<44}{len(cols)+1:>4}{1-np.var(r)/np.var(LA):>9.4f}"
          f"{float(np.sqrt(np.mean(r**2))):>9.4f}")
    return b,r
b1,_=go("k·lnNₑ − C·lnc/√Nₑ", [LN, -LC/np.sqrt(NE)])
b2,r2=go("+ k₁·c·lnNₑ  (the cross term)", [LN, -LC/np.sqrt(NE), C*LN])
b3,_=go("k·lnNₑ − x·lnc  (x constant)", [LN, -LC])
b4,_=go("k·lnNₑ + k₁·c·lnNₑ − x·lnc", [LN, C*LN, -LC])
b5,r5=go("k·lnNₑ − C·lnc/√Nₑ + k₁·c·lnNₑ − m·lnc·lnNₑ",
         [LN, -LC/np.sqrt(NE), C*LN, -LC*LN])
print()
print("  THE CROSS-TERM MODEL, WRITTEN OUT\n")
k,Cv,k1,q=b2[0],b2[1],b2[2],b2[3]
print(f"      ln a = {k:.4f}·lnNₑ − {Cv:.4f}·lnc/√Nₑ + {k1:.4f}·c·lnNₑ {q:+.4f}\n")
print(f"      a = {math.exp(q):.4f} · Nₑ^({k:.4f} + {k1:.4f}·c) · c^(−{Cv:.4f}/√Nₑ)\n")
print(f"      and since δ = a·√p :\n")
print(f"      δ = {math.exp(q):.4f}·√p · Nₑ^({k:.4f} + {k1:.4f}·c) · c^(−{Cv:.4f}/√Nₑ)\n")
print(f"      C = {Cv:.4f}   against 1.324 (a-grid) and 1.362 (ladder slopes)")
print(f"      k(1) = {k+k1:.3f}   k(2) = {k+2*k1:.3f}   k(3) = {k+3*k1:.3f}"
      f"   k(4) = {k+4*k1:.3f}")
print(f"      measured   0.572          0.705          0.828          1.132\n")
print("  RESIDUALS OF THE CROSS-TERM MODEL\n")
X=np.column_stack([LN,-LC/np.sqrt(NE),C*LN,np.ones(len(LA))])
pred=np.exp(X@b2); qq=A/pred
print(f"      {'charge':>7}{'n':>4}{'median a/pred':>15}")
for c in (1,2,3,4,5):
    m=C==c
    if m.sum()<3: continue
    print(f"      {c:>7}{int(m.sum()):>4}{st.median(qq[m]):>15.3f}")
print()
print(f"      {'Nₑ band':>9}{'n':>4}{'median a/pred':>15}")
for lo,hi in ((2,6),(6,15),(15,32),(32,60)):
    m=(NE>=lo)&(NE<hi)
    if m.sum()<3: continue
    print(f"      {f'{lo}–{hi}':>9}{int(m.sum()):>4}{st.median(qq[m]):>15.3f}")
np.save("/tmp/step3.npy",b2)
