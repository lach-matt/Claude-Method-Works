"""t0b_pot.py -- T0(b) potential builder. V = -Z/r + V_H[rho] + Vx[rho], Latter tail min(V,-q/r), -q/r beyond r0.
GATE: from rho_TFD this must regenerate tfd.potential eigenvalues (RUN-12 TFD column)."""
import numpy as np, io, contextlib, sys
from scipy.integrate import cumulative_trapezoid as ctz
with contextlib.redirect_stdout(io.StringIO()): import tfd, eigen_fix, tfdw3, step2_run
from t0b_rs import rho_tfd, rho_K, rs
CX=tfdw3.CX
def V_from_rho(Z,N,rho,r0):
    r=np.geomspace(1e-7,r0,20000); q=Z-N
    d=rho(r); w=4*np.pi*r*r*d
    Qin=ctz(w,r,initial=0.0); Qin=Qin+0.0
    Vout=ctz((4*np.pi*r*d)[::-1],r[::-1],initial=0.0)[::-1]*(-1)   # int_r^r0 4 pi r' rho
    VH=Qin/r+Vout
    Vin=-Z/r+VH-(4/3)*CX*np.maximum(d,0)**(1/3)
    Ntot=Qin[-1]
    def V(rr):
        rr=np.asarray(rr,float); v=np.interp(np.log(rr),np.log(r),Vin)
        return np.where(rr<r0,np.minimum(v,-q/rr),-q/rr)
    return V,Ntot
IONS=[("Ca II",20,18,[(4,0),(3,2)]),("Sr II",38,36,[(5,0),(4,2)]),("Ra II",88,86,[(7,0),(6,2)]),
      ("Ce IV",58,54,[(5,2),(4,3)]),("Pr V",59,54,[(5,2),(4,3)]),("Th IV",90,86,[(6,2),(5,3)])]
def probe(V,Z,pairs): return [eigen_fix.eigen(V,l,n,2.0,Z) for (n,l) in pairs]
if __name__=="__main__":
    print("GATE: Poisson reconstruction of rho_TFD vs tfd.potential baseline")
    for lab,Z,N,pairs in IONS:
        Vb,_=tfd.potential(Z,Z-N); eb=probe(Vb,Z,pairs)
        rho,r0=rho_tfd(Z,N); Vr,Nt=V_from_rho(Z,N,rho,r0); er=probe(Vr,Z,pairs)
        print(f"{lab:<7} base {eb[0]:.4f} {eb[1]:.4f} d={eb[1]-eb[0]:+.4f} | recon {er[0]:.4f} {er[1]:.4f} d={er[1]-er[0]:+.4f}  N={Nt:.3f}")