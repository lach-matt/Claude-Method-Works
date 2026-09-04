import numpy as np, io, contextlib, sys
with contextlib.redirect_stdout(io.StringIO()):
    import step2_run, eigen_fix, tfdw4
from probe13 import V_from
Z=int(sys.argv[1]); R=float(sys.argv[2]); pairs=[(int(p[0]),"spdf".index(p[1])) for p in sys.argv[3:]]
s=tfdw4.solve(Z,Z-2,R=R); V=V_from(s,Z,Z-2,R)
e=[eigen_fix.eigen(V,l,n,2.0,Z) for n,l in pairs]
r=np.exp(s.x); lam=tfdw4.lam_of(s.y[0],s.y[1],r); rsw=r[np.argmin(np.abs(lam-0.55))]
print(Z,"status",s.status,"mu",round(s.p[0],3),"r_switch %.3f"%rsw," ".join(f"{p}={v:.4f}" for p,v in zip(sys.argv[3:],e)),"d=%.4f"%(e[1]-e[0]))