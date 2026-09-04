import math, statistics as st, json
import numpy as np
from scipy import stats as SS
O=[tuple(x) for x in json.load(open("/tmp/step1.json"))]
NE=np.array([o[2] for o in O],float); C=np.array([o[1] for o in O],float)
A=np.array([o[3] for o in O]); LA=np.log(A)
print("  IS ln a A FUNCTION OF ONE COMBINATION OF Nₑ AND c ?\n")
print("      scan u = ln Nₑ − β·ln c and ask how well ln a collapses onto u\n")
print(f"      {'β':>6}{'r² (linear in u)':>20}{'r² (quadratic)':>18}")
best=None
for be in np.arange(0.0,3.01,0.05):
    u=np.log(NE)-be*np.log(C)
    r=SS.linregress(u,LA)
    X=np.column_stack([u,u**2,np.ones(len(u))])
    b,*_=np.linalg.lstsq(X,LA,rcond=None); res=LA-X@b
    q=1-np.var(res)/np.var(LA)
    if best is None or q>best[0]: best=(q,be,r.rvalue**2,b)
    if abs(be*20-round(be*20))<1e-9 and round(be*4)==be*4:
        print(f"      {be:>6.2f}{r.rvalue**2:>20.4f}{q:>18.4f}")
q,be,rl,b=best
print(f"\n      best β = {be:.2f}   quadratic r² = {q:.4f}   linear r² = {rl:.4f}\n")
u=np.log(NE)-be*np.log(C)
print(f"      u = ln Nₑ − {be:.2f}·ln c  =  ln( Nₑ / c^{be:.2f} )\n")
print(f"      ln a = {b[0]:.4f}·u {b[1]:+.4f}·u² {b[2]:+.4f}\n")
print("  THE VARIABLE ITSELF\n")
print(f"      Nₑ/c^{be:.2f}  —  the electron count divided by a power of the charge.")
print(f"      For β = 1 that is Nₑ/c; for β = ½ it is Nₑ/√c.\n")
print(f"      {'species':>4}{'Nₑ':>5}{'c':>3}{'Nₑ/c^β':>10}{'a':>9}{'pred':>9}")
X=np.column_stack([u,u**2,np.ones(len(u))]); pred=np.exp(X@b)
idx=np.argsort(u)
for i in idx[::4]:
    print(f"      {O[i][0]:>4}{int(NE[i]):>5}{int(C[i]):>3}"
          f"{NE[i]/C[i]**be:>10.2f}{A[i]:>9.4f}{pred[i]:>9.4f}")
print()
print("  AND HOW IT COMPARES WITH THE TWO-TERM FORMS\n")
print(f"      {'model':<40}{'par':>4}{'r²':>9}{'rms':>9}")
def sc(nm,cols):
    Xm=np.column_stack(cols+[np.ones(len(LA))])
    bb,*_=np.linalg.lstsq(Xm,LA,rcond=None); rr=LA-Xm@bb
    print(f"      {nm:<40}{len(cols)+1:>4}{1-np.var(rr)/np.var(LA):>9.4f}"
          f"{float(np.sqrt(np.mean(rr**2))):>9.4f}")
sc("k·lnNₑ − C·lnc/√Nₑ",[np.log(NE),-np.log(C)/np.sqrt(NE)])
sc(f"u and u², u = ln(Nₑ/c^{be:.2f})",[u,u**2])
sc(f"u alone",[u])
np.save("/tmp/step3b.npy",np.array([be,*b]))
