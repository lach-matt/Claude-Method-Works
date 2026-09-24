#!/usr/bin/env python3
"""hfs_pol.py -- session 9 Test D. hfs.scf made spin-polarised: Hund occupation, per-channel Dirac exchange."""
import numpy as np, tfd, warnings; warnings.filterwarnings("ignore")
import ground as G
from hfs import numerov_wf, L
def split(occ):
    up,dn=[],[]
    for n,l,k in occ:
        ku=min(k,2*l+1); kd=k-ku
        if ku: up.append((n,l,ku))
        if kd: dn.append((n,l,kd))
    return up,dn
def scf_pol(Z, charge=1, occ=None, npts=4000, beta=0.3, tol=2e-5, maxit=80):
    N=Z-charge; q=charge
    if occ is None: occ=list(G.expand(N)) if N>0 else []
    up,dn=split(occ)
    x=np.linspace(np.log(1e-6/Z),np.log(300.0),npts); r=np.exp(x); h=x[1]-x[0]; dr=r*h
    Vt,_=tfd.potential(Z,charge); Vg={s:Vt(r).copy() for s in "ud"}
    Vf={s:(lambda rr,V=Vg[s]:np.interp(np.log(np.asarray(rr,float)),x,V)) for s in "ud"}
    hist=[]
    for it in range(maxit):
        nsig={}; Es={}
        for s,lst in (("u",up),("d",dn)):
            n_r=np.zeros(npts)
            for n,l,k in lst:
                rr,drr,u,E,nd=numerov_wf(Vf[s],l,n,1.0,Z)
                if nd!=n-l-1: raise RuntimeError(f"Z={Z} {n}{L[l]}{s} nodes {nd}")
                ui=np.interp(r,rr,u,left=0.0,right=0.0); ui/=np.sqrt(np.sum(ui*ui*dr))
                n_r+=k*ui*ui; Es[(n,l,s)]=E
            nsig[s]=n_r
        ntot=nsig["u"]+nsig["d"]
        cum=np.cumsum(ntot*dr)-0.5*ntot*dr; outer=np.cumsum((ntot/r*dr)[::-1])[::-1]-0.5*ntot/r*dr
        VH=cum/r+outer; d=0.0; Vn={}
        for s in "ud":
            rho=nsig[s]/(4*np.pi*r*r); Vx=-(6.0*rho/np.pi)**(1.0/3.0)
            Vn[s]=np.minimum(-Z/r+VH+Vx,-q/r)
            d=max(d,float(np.max(np.abs(r*(Vn[s]-Vg[s]))[r<60])))
        hist.append(d)
        for s in "ud":
            Vg[s]=(1-beta)*Vg[s]+beta*Vn[s]
        Vf={s:(lambda rr,V=Vg[s]:np.interp(np.log(np.asarray(rr,float)),x,V)) for s in "ud"}
        if d<tol: break
    occd={(n,l):k for n,l,k in occ}
    def probe(n,l):
        s="d" if occd.get((n,l),0)>=2*l+1 else "u"
        return float(numerov_wf(Vf[s],l,n,1.0,Z)[3]),s
    return probe,Es,hist
if __name__=="__main__":
    import sys,time
    t=time.time(); pr,Es,h=scf_pol(25,1)
    print("Mn it",len(h),h[-1],round(time.time()-t,1),"s")
    for c in ((3,2),(4,0),(4,1),(4,2)): print(c,pr(*c))
