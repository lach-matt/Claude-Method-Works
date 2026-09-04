#!/usr/bin/env python3
"""tfdw.py -- session 12. TFD ion + Weizsaecker gradient term (TFDlamW). No fitted constant:
lam = 1/9 (Kirzhnits 1957, derived) or lam = 1 (von Weizsaecker 1935). Same nucleus/Hartree/Dirac exchange
as tfd.py; probe potential V = -Z/r + V_e + V_x(local Dirac), Latter clamp min(V, -q/r). Interface = tfd.potential.
Euler-Lagrange for psi=sqrt(rho), P=r*psi, Q=r*V_e:
  P'' = (2/lam)[(5/3)C_F rho^{2/3} - (4/3)C_x rho^{1/3} + Q/r - Z/r - mu] P ,  Q'' = -4 pi P^2 / r
BC: P(a)=0, Q(a)=0, P(b)=0, Q(b)=N, Q'(b)=0 ; mu is the solve_bvp parameter (N electrons).
"""
import numpy as np
from scipy.integrate import solve_bvp
CF=(3/10)*(3*np.pi**2)**(2/3); CX=(3/4)*(3/np.pi)**(1/3)
_cache={}
def solve(Z,N,lam,R=None,npts=600):
    key=(Z,N,lam)
    if key in _cache: return _cache[key]
    R = R or 12.0+8.0*(N/ max(Z-N,1))**0.5   # generous box
    a=1e-4
    r=np.geomspace(a,R,npts)
    def f(r,y,p):
        mu=p[0]; P,dP,Q,dQ=y
        rho=np.maximum(P/r,1e-30)**2
        g=(5/3)*CF*rho**(2/3)-(4/3)*CX*rho**(1/3)+Q/r-Z/r-mu
        return np.vstack([dP,(2/lam)*g*P,dQ,-4*np.pi*P*P/r])
    def bc(ya,yb,p): return np.array([ya[0],ya[2],yb[0],yb[2]-N,yb[3]])
    al=1.4*Z**(1/3)
    psi=np.sqrt(N*al**3/(8*np.pi))*np.exp(-al*r/2)
    P0=r*psi; dP0=np.gradient(P0,r)
    Q0=N*(1-np.exp(-al*r)*(1+al*r+ (al*r)**2/2)); dQ0=np.gradient(Q0,r)
    y0=np.vstack([P0,dP0,Q0,dQ0])
    sol=solve_bvp(f,bc,r,y0,p=[-0.5],tol=1e-6,max_nodes=60000,verbose=0)
    _cache[key]=sol; return sol
def potential(Z,charge,lam=1/9):
    N=Z-charge; q=charge
    sol=solve(Z,N,lam)
    if sol.status!=0: raise RuntimeError(f"bvp Z={Z} N={N} lam={lam}: {sol.message}")
    R=sol.x[-1]
    def V(r):
        r=np.asarray(r,float); rr=np.clip(r,sol.x[0],R)
        y=sol.sol(rr); P,Q=y[0],y[2]
        rho=np.maximum(P/rr,0.0)**2
        inner=-Z/r+Q/r-(3*rho/np.pi)**(1/3)
        out=np.where(r<R,np.minimum(inner,-q/r),-q/r)
        return out
    return V,R
if __name__=="__main__":
    import sys,time
    for Z,N,lam in [(20,18,1/9),(38,36,1/9),(58,54,1/9)]:
        t=time.time(); s=solve(Z,N,lam)
        print(Z,N,lam,"status",s.status,"mu",s.p[0],"nodes",len(s.x),"Q(R)",s.y[2][-1],"t",round(time.time()-t,1))