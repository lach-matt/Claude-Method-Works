"""t0b_rs.py -- T0(b) step 1: K-shell crossing radius r_s and moved charge, per ion.
rho_TFD from tfd.py's own equation: rho = Z/(4 pi b^3) (sqrt(phi/x)+beta)^3, x=r/b, x<x0.
rho_K  = 2|psi_1s(Z)|^2 = 2 Z^3/pi exp(-2 Z r).  r_s = INNER crossing (rho_TFD > rho_K as r->0)."""
import numpy as np, io, contextlib, sys
from scipy.integrate import quad
from scipy.optimize import brentq
with contextlib.redirect_stdout(io.StringIO()): import tfd
def rho_tfd(Z,N):
    sol,x0,beta=tfd.tfd_ion(Z,N); b=0.88534*Z**(-1/3)
    def rho(r):
        r=np.asarray(r,float); x=r/b
        phi=np.where(x<x0,np.clip(sol.sol(np.minimum(x,x0))[0],0,None),0.0)
        return np.where(x<x0, Z/(4*np.pi*b**3)*(np.sqrt(phi/np.maximum(x,1e-30))+beta)**3, 0.0)
    return rho,b*x0
def rho_K(Z): return lambda r: 2*Z**3/np.pi*np.exp(-2*Z*np.asarray(r,float))
def rs(Z,N):
    rt,r0=rho_tfd(Z,N); rk=rho_K(Z)
    f=lambda r: np.log(rt(r))-np.log(rk(r))
    rr=np.geomspace(1e-5,r0*0.999,4000); v=f(rr); i=np.argmax(v<0)
    assert v[0]>0 and i>0
    r_s=brentq(f,rr[i-1],rr[i])
    Ntot=quad(lambda r:4*np.pi*r*r*rt(r),0,r0,limit=400)[0]
    Nin_t=quad(lambda r:4*np.pi*r*r*rt(r),0,r_s,limit=200)[0]
    Nin_k=quad(lambda r:4*np.pi*r*r*rk(r),0,r_s,limit=200)[0]
    return r_s,r0,Ntot,Nin_t,Nin_k
if __name__=="__main__":
    print(f"{'ion':<7}{'Z':>4}{'N':>4}{'r_s':>9}{'Z*r_s':>7}{'r0':>8}{'N_TFD':>8}{'Nin_TFD':>9}{'Nin_K':>8}{'dN':>8}")
    for lab,Z,N in [("Ca II",20,18),("Sr II",38,36),("Ra II",88,86),("Ce IV",58,54),("Pr V",59,54),("Th IV",90,86)]:
        r_s,r0,Nt,Nit,Nik=rs(Z,N)
        print(f"{lab:<7}{Z:>4}{N:>4}{r_s:>9.5f}{Z*r_s:>7.3f}{r0:>8.3f}{Nt:>8.3f}{Nit:>9.4f}{Nik:>8.4f}{Nik-Nit:>8.4f}")