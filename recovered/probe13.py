"""probe13.py -- session 13. Rebuild of the (unbanked) session-12 eigenvalue probe.
Core N=Z-2 from tfdw3.solve (TFDlamW ground branch); probe electron sees V=-Z/r+Q/r+Vx(rho), Vx=-(4/3)CX rho^{1/3};
outside R Coulomb tail -(Z-N)/r. Verified: TFD baseline via tfd.potential(Z,2) regenerates RUN-12 Ca II line."""
import numpy as np, io, contextlib, sys
with contextlib.redirect_stdout(io.StringIO()):
    import step2_run, eigen_fix, tfd, tfdw3
CX=tfdw3.CX
def V_from(sol,Z,N,R):
    x=sol.x; S,dS,Q,dQ=sol.y; r=np.exp(x); rho=np.exp(2*S)/(r*r)
    Vin=-Z/r+Q/r-(4/3)*CX*rho**(1/3)
    def V(rr):
        rr=np.asarray(rr,float); v=np.interp(np.log(rr),x,Vin); return np.where(rr<R,v,-(Z-N)/rr)
    return V
def probe(Z,lam,R,pairs,zeta=2.0):
    s=tfdw3.solve(Z,Z-2,lam,R=R); V=V_from(s,Z,Z-2,R)
    out=[eigen_fix.eigen(V,l,n,zeta,Z) for (n,l) in pairs]
    return s.p[0],out
if __name__=="__main__":
    Z=int(sys.argv[1]); lam=float(sys.argv[2]); R=float(sys.argv[3])
    pairs=[(int(p[0]),"spdf".index(p[1])) for p in sys.argv[4:]]
    mu,e=probe(Z,lam,R,pairs)
    print(Z,"lam",round(lam,3),"mu",round(mu,3)," ".join(f"{p}={v:.4f}" for p,v in zip(sys.argv[4:],e)),"d=%.4f"%(e[1]-e[0]))