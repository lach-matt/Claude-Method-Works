#!/usr/bin/env python3
"""tfdw2.py -- session 12. TFDlamW ion by fixed-point iteration (single-orbital SCF), same physics as tfdw.py:
psi=sqrt(rho) solves -(lam/2) psi'' + [T(rho) + V_e - Z/r] psi = mu psi, T=(5/3)C_F rho^{2/3} - (4/3)C_x rho^{1/3},
normalised to N; V_e from Poisson. Numerov kernel (numerov_wf, ell=0, nodeless) on V_eff=(T+V_e-Z/r)/lam, mu=lam*E.
Cross-check: BVP (tfdw.py) Ca II core mu=-0.8517 Ha at lam=1/9. Probe potential as tfd.py: -Z/r+V_e+V_x, Latter clamp.
"""
import numpy as np, step2_run, eigen_fix
from derive_P_fix import numerov_wf
CF=(3/10)*(3*np.pi**2)**(2/3); CX=(3/4)*(3/np.pi)**(1/3)
_cache={}
def solve(Z,N,lam,mix=0.25,iters=400,tol=1e-7):
    key=(Z,N,lam)
    if key in _cache: return _cache[key]
    # start from a hydrogenic-ish density
    r=None; rho=None; Ve=None; mu=None
    def Ve_of(u,r,dr):
        cum=np.cumsum(u*u*dr); tot=cum[-1]
        inner=cum/r
        outer=np.cumsum((u*u*dr/r)[::-1])[::-1]
        return N*(inner+outer-u*u*dr/r)  # avoid double count of the cell
    for it in range(iters):
        if rho is None:
            V=lambda rr: -Z/rr/lam*0+(-Z/np.asarray(rr,float))*(1/lam)*0.5   # gentle start
        else:
            T=(5/3)*CF*rho**(2/3)-(4/3)*CX*rho**(1/3)
            arr=(T+Ve-Z/r)/lam
            V=lambda rr,arr=arr,r=r: np.interp(np.log(np.asarray(rr,float)),np.log(r),arr,left=arr[0],right=arr[-1]*r[-1]/np.maximum(np.asarray(rr,float),r[-1]))
        rr,dr,u,E,nd=numerov_wf(V,0,1,1,Z)
        rho_new=N*u*u/(4*np.pi*rr*rr)
        if rho is None: rho=rho_new; r=rr
        else:
            d=np.sum(np.abs(rho_new-rho)*4*np.pi*rr*rr*dr)/N
            rho=(1-mix)*rho+mix*rho_new
            if d<tol: break
        Ve=Ve_of(np.sqrt(4*np.pi*rho)*r,r,dr) if False else Ve_of(np.sqrt(np.maximum(rho,0)*4*np.pi)*r,r,dr)
        mu=lam*E
    out=dict(r=r,rho=rho,Ve=Ve,mu=mu,iters=it+1,conv=d if it else None)
    _cache[key]=out; return out
def potential(Z,charge,lam=1/9):
    N=Z-charge; q=charge; s=solve(Z,N,lam); r=s['r']
    inner=-Z/r+s['Ve']/r*0+s['Ve']-(3*np.maximum(s['rho'],0)/np.pi)**(1/3)
    lr=np.log(r)
    def V(rr):
        rr=np.asarray(rr,float)
        v=np.interp(np.log(rr),lr,inner,left=inner[0],right=0.0)
        v=np.where(rr>r[-1],-q/rr,v)
        return np.minimum(v,-q/rr)
    return V,r[-1]
if __name__=="__main__":
    import time
    for Z,N,lam in [(20,18,1/9),(38,36,1/9),(58,54,1/9)]:
        t=time.time(); s=solve(Z,N,lam)
        print(Z,N,round(lam,4),"mu",round(s['mu'],5),"iters",s['iters'],"conv %.1e"%(s['conv'] or 0),"t",round(time.time()-t,1))