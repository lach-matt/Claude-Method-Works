import math, statistics as st, json
import numpy as np
from scipy import stats as SS
O=[tuple(x) for x in json.load(open("/tmp/step1.json"))]
NEW=[(48,1,1.6381),(49,1,1.6667)]
NE=np.array([o[2] for o in O]+[n for n,_,_ in NEW],float)
C =np.array([o[1] for o in O]+[c for _,c,_ in NEW],float)
A =np.array([o[3] for o in O]+[a for _,_,a in NEW])
LA=np.log(A); u=np.log(NE)-(2/3)*np.log(C)
print("  REFIT WITH THE PEAK CAPTURES INCLUDED\n")
X=np.column_stack([u,u**2,np.ones(len(u))])
b,*_=np.linalg.lstsq(X,LA,rcond=None); r=LA-X@b
u0=-b[0]/(2*b[1]); M=math.exp(b[2]+b[0]*u0+b[1]*u0**2); sg=1/math.sqrt(-2*b[1])
print(f"      ln a = {b[0]:.4f}·u {b[1]:+.4f}·u² {b[2]:+.4f}")
print(f"      r² {1-np.var(r)/np.var(LA):.4f}   rms {float(np.sqrt(np.mean(r**2))):.4f}")
print(f"      u₀ = {u0:.4f} (Nₑ/c^⅔ = {math.exp(u0):.1f})   M = {M:.4f}   σ = {sg:.4f}")
print(f"      before: u₀ = 3.894 (49.1)   M = 1.4907   σ = 1.6908\n")
print("  DOES THE PARABOLA STILL FIT AT THE TOP?\n")
pred=np.exp(X@b); q=A/pred
print(f"      {'u band':>12}{'n':>4}{'median a/pred':>15}")
for lo,hi in ((0,1.5),(1.5,2.5),(2.5,3.2),(3.2,3.7),(3.7,4.2)):
    m=(u>=lo)&(u<hi)
    if m.sum()<2: continue
    print(f"      {f'{lo}–{hi}':>12}{int(m.sum()):>4}{st.median(q[m]):>15.3f}")
print()
print("  THE ℓ-STRUCTURE AT THE PEAK — δ/√p BY ℓ\n")
print("      Cd I : s 1.638  p 1.762  d 1.475")
print("      In I : s 1.667  p 1.869  d 1.609")
print("      Rb I : s 1.526* p 1.534  d 1.331   (*from the 41-set)\n")
print("      p exceeds s by 8% at Cd, 12% at In, 1% at Rb.")
print("      d falls below s by 10% at Cd, 3% at In, 13% at Rb.\n")
print("  SO √p IS RIGHT ON AVERAGE AND WRONG IN DETAIL AT THE TOP.\n")
print("      test: is the ℓ-spread of δ/√p a function of u?\n")
DAT=[("Cd I",3.871,[1.6381,1.7617,1.4753]),("In I",3.892,[1.6667,1.8689,1.6088]),
     ("Rb I",3.611,[1.5254,1.5340,1.3307]),("Sr II",2.914,[1.3720,1.3200,1.4592]),
     ("K I",2.944,[1.2475,1.2110,None]),("Ca II",2.507,[1.0506,1.0500,None])]
print(f"      {'species':<8}{'u':>7}{'spread (max−min)/median':>26}")
for nm,uu,v in DAT:
    vv=[x for x in v if x]
    if len(vv)<2: continue
    print(f"      {nm:<8}{uu:>7.3f}{(max(vv)-min(vv))/st.median(vv):>26.3f}")
print()
xs=[uu for nm,uu,v in DAT if len([x for x in v if x])>=2]
ys=[(max([x for x in v if x])-min([x for x in v if x]))/st.median([x for x in v if x])
    for nm,uu,v in DAT if len([x for x in v if x])>=2]
rr=SS.linregress(xs,ys)
print(f"      spread against u : slope {rr.slope:+.4f}  r² {rr.rvalue**2:.3f}"
      f"  p {rr.pvalue:.3f}")
print(f"      → {'the ℓ-spread GROWS toward the peak' if rr.slope>0 and rr.pvalue<0.1 else 'no clear trend'}")
np.save("/tmp/peakfit.npy",b)
