"""t7c_occ_diag.py -- F21.1 test. scf_occ verbatim + returns tail term  int n (V_tailed - V_HFS) dr  and E_HFS[n] = Etot - tail term.
Usage: python3 t7c_occ_diag.py Z sh q qtail"""
import sys, json, numpy as np, warnings; warnings.filterwarnings("ignore")
import tfd, ground as G
from hfs import numerov_wf, L
from t5_scf import ground_occ, minus
def scf_occ_diag(Z, occ, qtail, npts=4000, beta=0.3, tol=2e-5, maxit=80):
    N=sum(k for _,_,k in occ)
    x=np.linspace(np.log(1e-6/Z),np.log(300.0),npts); r=np.exp(x); h=x[1]-x[0]; dr=r*h
    Vt,_=tfd.potential(Z,max(int(round(Z-N)),1)); Vg=Vt(r); Vf=lambda rr,Vg=Vg: np.interp(np.log(np.asarray(rr,float)),x,Vg)
    for it in range(maxit):
        n_r=np.zeros(npts); Es={}
        for n,l,k in occ:
            rr,drr,u,E,nd=numerov_wf(Vf,l,n,1.0,Z)
            ui=np.interp(r,rr,u,left=0.0,right=0.0); ui/=np.sqrt(np.sum(ui*ui*dr)); n_r+=k*ui*ui; Es[(n,l)]=E
        cum=np.cumsum(n_r*dr)-0.5*n_r*dr; outer=np.cumsum((n_r/r*dr)[::-1])[::-1]-0.5*n_r/r*dr; VH=cum/r+outer
        rho=n_r/(4*np.pi*r*r); Vx=-(3.0*rho/np.pi)**(1.0/3.0)
        Vhfs=-Z/r+VH+Vx; Vn=np.minimum(Vhfs,-qtail/r); d=float(np.max(np.abs(r*(Vn-Vg))[r<60]))
        Vg=(1-beta)*Vg+beta*Vn; Vf=lambda rr,Vg=Vg: np.interp(np.log(np.asarray(rr,float)),x,Vg)
        if d<tol: break
    Etot=sum(k*Es[(n,l)] for n,l,k in occ)-0.5*np.sum(n_r*VH*dr)-0.25*np.sum(n_r*Vx*dr)
    tail=float(np.sum(n_r*(Vg-Vhfs)*dr))       # int n (V_tailed - V_HFS); Vg is the converged tailed potential
    return Es,Etot,tail,it+1
if __name__=="__main__":
    Z=int(sys.argv[1]); sh=sys.argv[2]; q=float(sys.argv[3]); qt=float(sys.argv[4]); n,l=int(sh[0]),"spdf".index(sh[1])
    occ=minus(ground_occ(Z),n,l,1.0-q)
    if q==0.0: occ=occ+[(n,l,1e-9)]
    Es,Et,tail,it=scf_occ_diag(Z,occ,qt)
    out=dict(Z=Z,sh=sh,q=q,qtail=qt,eps=round(Es[(n,l)],6),Etot=round(Et,6),tail=round(tail,6),E_hfs=round(Et-tail,6),it=it)
    open('t7c_occ_diag.jsonl','a').write(json.dumps(out)+'\n'); print(out)
