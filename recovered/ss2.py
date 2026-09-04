import math
import numpy as np
from scipy.optimize import curve_fit
src=open("shellsum.py",encoding="utf-8").read()
src=src[:src.index("def model(")]
g={}; exec(src,g)
for k_ in ("OC","CAPS","FILL","SN","SL","LL","N0","NE","C","Y","T","ZZ","DL","DN",
           "SAME","BELOW","EMPTYSAME","SHELLS","ROWS","OPEN","sig"): globals()[k_]=g[k_]
# the real threshold for each shell, as a matrix
THR=np.array([OPEN.get((n,l),9999) for (n,l) in SHELLS],float)
def sig(x): return 0.5*(1+np.tanh(0.5*np.clip(x,-60,60)))
def rep(name,f,p0s,npar):
    best=None
    for p0 in p0s:
        try:
            pr,_=curve_fit(f,np.arange(len(Y)),Y,p0=p0,maxfev=900000)
            r=Y-f(None,*pr); s=float(np.sqrt(np.mean(r**2)))
            if best is None or s<best[1]: best=(pr,s)
        except Exception: pass
    if best is None: print(f"      {name:<44}{npar:>3}   failed"); return None
    pr,s=best; r=Y-f(None,*pr)
    print(f"      {name:<44}{npar:>3}{s:>10.4f}{1-np.var(r)/np.var(Y):>9.4f}")
    return pr
print("  THE SHELL SUM, WITH THE REAL PER-SHELL THRESHOLD\n")
print(f"      {'model':<44}{'par':>3}{'rms':>10}{'R²':>9}")
rep("same-ℓ occupied only  (a, s, k)",
    lambda _,a,s,k: (a*SAME*FILL*np.exp(-np.maximum(DN,0)/max(abs(s),1e-6))
                     ).sum(axis=1)*NE**k*T, [[0.35,4.6,0.41]],3)
rep("+ radial damping on the Rydberg n₀",
    lambda _,a,s,q,k: (a*SAME*FILL*np.exp(-np.maximum(DN,0)/max(abs(s),1e-6))
                       ).sum(axis=1)*(1+q*(N0[:,0]-1))*NE**k*T, [[0.35,4.6,0.0,0.41]],4)
pr=rep("+ EMPTY same-ℓ shell, real threshold",
    lambda _,a,s,u,w,k: (a*SAME*FILL*np.exp(-np.maximum(DN,0)/max(abs(s),1e-6))
        + u*EMPTYSAME*sig((ZZ[:,None]-THR[None,:])/max(abs(w),1e-6))
        ).sum(axis=1)*NE**k*T, [[0.35,4.6,0.6,4.0,0.41],[0.4,3,0.8,5,0.47]],5)
pr2=rep("+ EMPTY shell AND radial damping",
    lambda _,a,s,q,u,w,k: (a*SAME*FILL*np.exp(-np.maximum(DN,0)/max(abs(s),1e-6))
        + u*EMPTYSAME*sig((ZZ[:,None]-THR[None,:])/max(abs(w),1e-6))
        ).sum(axis=1)*(1+q*(N0[:,0]-1))*NE**k*T,
        [[0.35,4.6,0.0,0.6,4.0,0.41],[0.4,3,-0.05,0.8,5,0.47]],6)
best=pr2 if pr2 is not None else pr
if best is not None:
    np.save("/tmp/eqss.npy",best)
    print()
    if len(best)==6:
        a,s,q,u,w,k=best
        print(f"      a = {a:.4f}   s = {s:.4f}   q = {q:+.4f}   u = {u:.4f}   "
              f"w = {w:.4f}   k = {k:.4f}")
        print(f"\n      the EMPTY same-ℓ shell contributes u = {u:.3f} once Z passes")
        print(f"      its threshold, over a width of {abs(w):.1f} in Z. It is a TERM")
        print(f"      in the sum, present whether or not the shell holds electrons.")