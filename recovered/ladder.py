import math, json
import numpy as np
from scipy import stats as SS
D=json.load(open("/tmp/kr.json"))
K={}
for k,v in D.items():
    Z,c,l=[int(x) for x in k.split(",")]; K[(c,l)]=v
# Rb I redone with the published limit
K[(1,0)],K[(1,1)],K[(1,2)],K[(1,3)]=3.1357,2.6566,1.3307,0.0143
L="spdfgh"
print("  THE LADDER ON A THIRD SEQUENCE — Nₑ = 37, Kr core\n")
print("      δ(c) = B·ln(c+1)/c   with A ≡ 0 at the hydrogenic edge\n")
print(f"      {'ℓ':>3}{'c=1':>9}{'c=2':>9}{'c=3':>9}{'B':>9}{'r²':>9}{'rms':>9}")
Bs={}
for l in range(4):
    d={c:K[(c,l)] for c in (1,2,3) if (c,l) in K}
    if len(d)<3: continue
    xs=np.array([math.log(c+1)/c for c in sorted(d)])
    ys=np.array([d[c] for c in sorted(d)])
    B=float(np.sum(xs*ys)/np.sum(xs*xs))
    r=ys-B*xs
    r2=1-np.sum(r**2)/max(np.sum((ys-ys.mean())**2),1e-12)
    print(f"      {L[l]:>3}" + "".join(f"{d[c]:>9.4f}" for c in (1,2,3)) +
          f"{B:>9.4f}{r2:>9.4f}{float(np.sqrt(np.mean(r**2))):>9.4f}")
    Bs[l]=B
print()
print("  AND B AGAINST THE TWO COORDINATES\n")
print("      the eight-sequence fit gave B ≈ α·p + β·Nₑ^(1/3) + γ.")
print("      Nₑ = 37 so Nₑ^(1/3) = 3.332, and p is the Kr core's count at each ℓ:\n")
P={0:4,1:3,2:1,3:0}          # Kr core 1s2s3s4s / 2p3p4p / 3d / no f
print(f"      {'ℓ':>3}{'p':>4}{'B measured':>13}{'p + 3.332':>12}")
for l in sorted(Bs):
    print(f"      {L[l]:>3}{P[l]:>4}{Bs[l]:>13.4f}{P[l]+3.332:>12.3f}")
print()
xs=np.array([P[l] for l in sorted(Bs)],float)
ys=np.array([Bs[l] for l in sorted(Bs)])
r=SS.linregress(xs,ys)
print(f"      B against p, this sequence alone: slope {r.slope:+.4f}, "
      f"intercept {r.intercept:+.4f}, r² {r.rvalue**2:.4f}")
print()
print("  THE PREDICTION TEST — what did the eight-sequence fit say for Nₑ = 37?\n")
print("      α ≈ +1.16 per p, β from Nₑ^(1/3), γ the intercept — refitting with")
print("      these three points added is the next step, not a claim here.")