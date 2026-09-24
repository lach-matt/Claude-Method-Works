"""t5_scf.py -- hfs.scf with an explicit occupation (fractional k allowed) and explicit Latter tail charge; returns
eigenvalues and the HFS total energy E = sum n eps - 1/2 int n V_H - 1/4 int n V_x (Dirac).  Copy of hfs.scf, session 16."""
import numpy as np, warnings; warnings.filterwarnings("ignore")
import tfd, ground as G
from hfs import numerov_wf, L
def scf_occ(Z, occ, qtail, npts=4000, beta=0.3, tol=2e-5, maxit=80):
    N=sum(k for _,_,k in occ)
    x=np.linspace(np.log(1e-6/Z),np.log(300.0),npts); r=np.exp(x); h=x[1]-x[0]; dr=r*h
    Vt,_=tfd.potential(Z,max(int(round(Z-N)),1)); Vg=Vt(r); Vf=lambda rr,Vg=Vg: np.interp(np.log(np.asarray(rr,float)),x,Vg)
    for it in range(maxit):
        n_r=np.zeros(npts); Es={}
        for n,l,k in occ:
            rr,drr,u,E,nd=numerov_wf(Vf,l,n,1.0,Z)
            if nd!=n-l-1: raise RuntimeError(f"Z={Z} {n}{L[l]} nodes {nd}")
            ui=np.interp(r,rr,u,left=0.0,right=0.0); ui/=np.sqrt(np.sum(ui*ui*dr)); n_r+=k*ui*ui; Es[(n,l)]=E
        cum=np.cumsum(n_r*dr)-0.5*n_r*dr; outer=np.cumsum((n_r/r*dr)[::-1])[::-1]-0.5*n_r/r*dr; VH=cum/r+outer
        rho=n_r/(4*np.pi*r*r); Vx=-(3.0*rho/np.pi)**(1.0/3.0)
        Vn=np.minimum(-Z/r+VH+Vx,-qtail/r); d=float(np.max(np.abs(r*(Vn-Vg))[r<60]))
        Vg=(1-beta)*Vg+beta*Vn; Vf=lambda rr,Vg=Vg: np.interp(np.log(np.asarray(rr,float)),x,Vg)
        if d<tol: break
    Etot=sum(k*Es[(n,l)] for n,l,k in occ)-0.5*np.sum(n_r*VH*dr)-0.25*np.sum(n_r*Vx*dr)
    return Vf,Es,Etot,it+1
def ground_occ(Z): return [tuple(t) for t in G.expand(Z)]
def minus(occ,n,l,k):
    o=[list(t) for t in occ]
    for t in o:
        if t[0]==n and t[1]==l: t[2]-=k
    return [tuple(t) for t in o if t[2]>1e-9]
if __name__=="__main__":
    # GATE: probe eigenvalue on ground(Z-1) core, tail -1/r, vs T0b_pairs SCF (Sc 3d -0.4866, La 5d -0.3581)
    import json
    K={(r[0],r[1]):r[3] for r in json.load(open('../pack9/T0b_pairs.json'))}
    for Z,n,l in [(21,3,2),(57,5,2)]:
        Vf,Es,E,it=scf_occ(Z,ground_occ(Z-1),1)
        e=float(numerov_wf(Vf,l,n,1.0,Z)[3]); print(Z,f"{n}{L[l]}",f"probe {e:.4f}  banked {K[(Z,f'{n}{L[l]}')]:.4f}  it {it}")
