#!/usr/bin/env python3
"""tfdw3.py -- session 12. TFDlamW ion BVP in S=ln(P) (P=r*psi>0 by construction: ground branch only).
log mesh x=ln r: S''+S'^2-S' = r^2 (2/lam) g ,  Q''-Q' = -4 pi r e^{2S} ; g=(5/3)C_F rho^{2/3}-(4/3)C_x rho^{1/3}+Q/r-Z/r-mu
BC: S'(a)=1-Z a/lam (nuclear cusp), Q(a)=0, Q(b)=N, Q'(b)=0, S'(b)=1-b*sqrt(-2 mu/lam). Parameter mu."""
import numpy as np
from scipy.integrate import solve_bvp
CF=(3/10)*(3*np.pi**2)**(2/3); CX=(3/4)*(3/np.pi)**(1/3)
def solve(Z,N,lam,R=10.0,npts=1200,guess=None):
    a=1e-4/Z; x=np.linspace(np.log(a),np.log(R),npts); r=np.exp(x)
    def f(x,y,p):
        mu=p[0]; r=np.exp(x); S,dS,Q,dQ=y
        rho=np.exp(2*S)/(r*r)
        g=(5/3)*CF*rho**(2/3)-(4/3)*CX*rho**(1/3)+Q/r-Z/r-mu
        return np.vstack([dS, r*r*(2/lam)*g-dS*dS+dS, dQ, dQ-4*np.pi*r*np.exp(2*S)])
    def bc(ya,yb,p):
        mu=p[0]; k=np.sqrt(max(-2*mu/lam,1e-6))
        return np.array([ya[1]-(1-Z*a/lam), ya[2], yb[2]-N, yb[3], yb[1]-(1-R*k)])
    if guess is None:
        al=Z**(1/3); psi=np.sqrt(N*al**3/(8*np.pi))*np.exp(-al*r/2)
        S0=np.log(r*psi); Q0=N*(1-np.exp(-al*r)*(1+al*r+(al*r)**2/2)); mu0=-1.0
        y0=np.vstack([S0,np.gradient(S0,x),Q0,np.gradient(Q0,x)])
    else:
        y0=guess.sol(x); mu0=guess.p[0]
    return solve_bvp(f,bc,x,y0,p=[mu0],tol=1e-7,max_nodes=150000,verbose=0)
if __name__=="__main__":
    import time
    for Z,N,lam,R in [(20,18,1.0,10),(20,18,1/9,10),(20,18,1/9,6),(38,36,1/9,8),(58,54,1/9,8)]:
        t=time.time(); s=solve(Z,N,lam,R=R)
        P=np.exp(s.y[0]); print(Z,N,round(lam,3),"R",R,"status",s.status,"mu",round(s.p[0],5),"nodes",len(s.x),"Q(R)",round(s.y[2][-1],4),"t",round(time.time()-t,1))