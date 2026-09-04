"""tfdw4.py -- session 13, T0(a). REGION-SPLIT gradient term, no constant.
lam(s): s = |grad rho| / (2 (3 pi^2)^{1/3} rho^{4/3}) is Kirzhnits' expansion parameter (log-mesh: |grad rho|=|dS-... | rho (2 dS - 2)/r).
Kirzhnits second-order (lam=1/9) is kept where s<1 (series converges); at s>=1 the series has no meaning and the full
Weizsaecker term (lam=1) is used. The switch is a smooth step in s centred on 1 with width from the series itself:
w = 1/9 (the next term's coefficient ratio) -- no free number.  BC as tfdw3 with lam(cusp)=1 at a, lam(edge)=1/9 at R."""
import numpy as np
from scipy.integrate import solve_bvp
CF=(3/10)*(3*np.pi**2)**(2/3); CX=(3/4)*(3/np.pi)**(1/3); K=2*(3*np.pi**2)**(1/3)
def lam_of(S,dS,r):
    rho=np.exp(2*S)/(r*r); grad=np.abs(rho*(2*dS-2)/r); s=grad/(K*rho**(4/3)+1e-300)
    return 1/9+(1-1/9)*0.5*(1+np.tanh((s-1)/(1/9)))
def solve(Z,N,R=10.0,npts=1200):
    a=1e-4/Z; x=np.linspace(np.log(a),np.log(R),npts)
    def f(x,y,p):
        mu=p[0]; r=np.exp(x); S,dS,Q,dQ=y; rho=np.exp(2*S)/(r*r); lam=lam_of(S,dS,r)
        g=(5/3)*CF*rho**(2/3)-(4/3)*CX*rho**(1/3)+Q/r-Z/r-mu
        return np.vstack([dS, r*r*(2/lam)*g-dS*dS+dS, dQ, dQ-4*np.pi*r*np.exp(2*S)])
    def bc(ya,yb,p):
        mu=p[0]; k=np.sqrt(max(-2*mu/(1/9),1e-6))
        return np.array([ya[1]-(1-Z*a/1.0), ya[2], yb[2]-N, yb[3], yb[1]-(1-R*k)])
    r=np.exp(x); al=Z**(1/3); psi=np.sqrt(N*al**3/(8*np.pi))*np.exp(-al*r/2)
    S0=np.log(r*psi); Q0=N*(1-np.exp(-al*r)*(1+al*r+(al*r)**2/2))
    y0=np.vstack([S0,np.gradient(S0,x),Q0,np.gradient(Q0,x)])
    return solve_bvp(f,bc,x,y0,p=[-1.0],tol=1e-7,max_nodes=150000,verbose=0)