import numpy as np, eldata as ed
from scipy import stats
MN={21:19,22:51,23:54,24:57,26:61,27:64,28:67,29:72,39:20,40:49,41:53,42:56,
44:62,45:65,46:69,47:71,57:33,58:32,59:31,60:30,62:28,63:18,64:27,65:26,66:25,
67:24,68:23,69:22,70:17,71:21,72:50,73:52,74:55,75:58,77:63,78:66,79:70,90:47,92:45,
1:92,3:1,4:77,5:86,6:95,7:100,8:101,9:102,11:11,12:73,13:80,14:85,15:90,16:94,17:99,
19:10,20:16,30:76,31:81,32:84,33:89,34:93,35:98,37:9,38:15,48:75,49:79,50:83,51:88,
52:92,53:97,55:8,56:14,80:74,81:78,82:82,83:87,84:91,85:96}
com=sorted(z for z in MN if z in ed.E)

print("="*80)
print("THE OBSTRUCTION, STATED AS A THEOREM")
print("="*80)
print("""  A function F(n,ℓ,k) = a + b·n + c·ℓ + d·k has ∂F/∂k = d, a CONSTANT
  independent of ℓ. Equivalently its mixed second difference vanishes:

        Δ_ℓ Δ_k F  =  F(ℓ+1,k+1) − F(ℓ+1,k) − F(ℓ,k+1) + F(ℓ,k)  =  0

  So: MN is linear in (n,ℓ,k)  ⟺  all mixed second differences vanish.
  Measured slope ∂MN/∂k by block:""")
for lv,nm in [(1,'p'),(2,'d'),(3,'f')]:
    pts=sorted((ed.E[z][2],MN[z]) for z in com if ed.E[z][1]==lv)
    ks=np.array([p[0] for p in pts],float); ms=np.array([p[1] for p in pts],float)
    slope,inter,r,p,se=stats.linregress(ks,ms)
    print(f"    ℓ={lv} ({nm}): ∂MN/∂k = {slope:+.2f} ± {se:.2f}   (p={p:.1e})")
print("""
  The slope changes SIGN between ℓ=2 and ℓ=3. A constant d cannot be both
  positive and negative. Therefore no linear function of (n,ℓ,k) reproduces
  MN. This is a proof, not a fit — no search over coefficients can succeed.""")

print()
print("="*80)
print("HOW FAR CAN LINEARITY GO? — the exact ceiling")
print("="*80)
mn=np.array([MN[z] for z in com],float)
n=np.array([ed.E[z][0] for z in com],float)
l=np.array([ed.E[z][1] for z in com],float)
k=np.array([ed.E[z][2] for z in com],float)
X=np.column_stack([np.ones(len(mn)),n,l,k])
b,res,rank,sv=np.linalg.lstsq(X,mn,rcond=None)
pred=X@b
R2=1-np.sum((mn-pred)**2)/np.sum((mn-np.mean(mn))**2)
print(f"  best possible linear fit (OLS is optimal by construction):")
print(f"    MN ≈ {b[0]:+.2f} {b[1]:+.2f}·n {b[2]:+.2f}·ℓ {b[3]:+.2f}·k")
print(f"    R² = {R2:.4f}   — this is the CEILING for any linear model")
print(f"    residual SD = {np.std(mn-pred):.1f} on an MN range of {mn.max()-mn.min():.0f}")

print()
print("="*80)
print("GENERALISATION 1 — ADDITIVE MODELS (linear after recoding each axis)")
print("="*80)
print("""  Relax 'linear' to 'additively separable':  MN ≈ f(n) + g(ℓ) + h(k)
  with f,g,h arbitrary. This is the widest class that is still free of
  interaction terms. Fit by one-hot encoding each axis (a saturated
  additive model — the best any additive model can do).""")
def onehot(v):
    u=sorted(set(v)); return np.column_stack([(v==x).astype(float) for x in u[1:]])
Xa=np.column_stack([np.ones(len(mn)),onehot(n),onehot(l),onehot(k)])
ba,*_=np.linalg.lstsq(Xa,mn,rcond=None); pa=Xa@ba
R2a=1-np.sum((mn-pa)**2)/np.sum((mn-np.mean(mn))**2)
# LOO
pr=np.zeros(len(mn))
for i in range(len(mn)):
    m=np.ones(len(mn),bool); m[i]=False
    bb,*_=np.linalg.lstsq(Xa[m],mn[m],rcond=None); pr[i]=Xa[i]@bb
L2a=1-np.sum((mn-pr)**2)/np.sum((mn-np.mean(mn))**2)
print(f"    saturated additive model: {Xa.shape[1]} params")
print(f"    fit R² = {R2a:.4f}   LOO R² = {L2a:.4f}")
print(f"  → even the BEST additive model is capped here. Interaction is required.")