"""corr_ring.py -- s30 candidate C: eps_c^R(nu,nd) = eps_r(r_s,zeta)/2 + E0B  [Ha] from ring_table.json; v^R = d(n eps)/dn (spin-resolved) by table gradients.
Same interface as t7c_cuaudit.v_gbz / hfc2.eps_c so it can be patched in: T.v_gbz = v_R; H.eps_c = eps_R. Small-r_s: below table, chain form (lam0 ln rs+eps0+E0B)."""
import numpy as np, json, t7c_cuaudit as T
_tab=json.load(open('ring_table.json')); RS=np.array(_tab['rs']); ZS=np.array(_tab['z']); LR=np.log(RS)
E=np.array([_tab['eps'][str(i)] for i in range(len(ZS))])/2.0+T.E0B          # (nz, nrs) Ha
dE_dlnrs=np.gradient(E,LR,axis=1); dE_dz=np.gradient(E,ZS,axis=0)
def _interp(A,lr,z):
    iz=np.clip(np.searchsorted(ZS,z)-1,0,len(ZS)-2); tz=(z-ZS[iz])/(ZS[iz+1]-ZS[iz])
    ir=np.clip(np.searchsorted(LR,lr)-1,0,len(LR)-2); tr=(lr-LR[ir])/(LR[ir+1]-LR[ir])
    a=A[iz,ir]*(1-tr)+A[iz,ir+1]*tr; b=A[iz+1,ir]*(1-tr)+A[iz+1,ir+1]*tr
    return a*(1-tz)+b*tz
def _chain(rs,z): return T._lam0(z)*np.log(rs)+T._e0a(z)+T.E0B
def eps_R(nu,nd):
    n=nu+nd; n=np.maximum(n,1e-30); z=np.clip((nu-nd)/n,0.0,1.0); rs=(3.0/(4*np.pi*n))**(1.0/3.0); lr=np.log(rs)
    lo=lr<LR[0]; hi=lr>LR[-1]
    e=_interp(E,np.clip(lr,LR[0],LR[-1]),z)
    e=np.where(lo,_chain(rs,z),e); e=np.where(hi,_interp(E,LR[-1]*np.ones_like(lr),z),e)   # beyond r_s=100: clamp (negligible density)
    return e
def v_R(nu,nd):
    n=nu+nd; n=np.maximum(n,1e-30); z=np.clip((nu-nd)/n,0.0,1.0); rs=(3.0/(4*np.pi*n))**(1.0/3.0); lr=np.log(rs); lrc=np.clip(lr,LR[0],LR[-1])
    eps=eps_R(nu,nd); de_dl=_interp(dE_dlnrs,lrc,z); de_dz=_interp(dE_dz,lrc,z)
    lo=lr<LR[0]
    de_dl=np.where(lo,T._lam0(z),de_dl)
    h=1e-4; de_dz=np.where(lo,(_chain(rs,np.clip(z+h,0,1))-_chain(rs,np.clip(z-h,0,1)))/(np.clip(z+h,0,1)-np.clip(z-h,0,1)+1e-300),de_dz)
    base=eps-de_dl/3.0                              # -(r_s/3) d eps/d r_s = -(1/3) d eps/d ln r_s
    vu=base+(1-z)*de_dz; vd=base-(1+z)*de_dz
    if T._SUBCELL: w=T._frac_neg(eps); return vu*w, vd*w
    ok=eps<0; return np.where(ok,vu,0.0), np.where(ok,vd,0.0)
if __name__=="__main__":
    for rs in (1e-3,1e-2,0.1,1,2,3,5,10):
        n=3/(4*np.pi*rs**3)
        for z in (0.0,1.0):
            print(f"rs {rs} z {z}: R {float(eps_R(n*(1+z)/2*np.ones(1),n*(1-z)/2*np.ones(1))[0]):+.5f}  Z {float(_chain(rs,z)):+.5f} Ha")