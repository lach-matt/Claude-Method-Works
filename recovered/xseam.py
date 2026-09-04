"""xseam.py -- s34 PREDICTION-XSEAM: frozen-orbital removal-exchange of the entrant, HF (Slater G^k, average of configuration) vs LSD+PZ-SIC (chain Dirac spin form),
on the chain's spin-averaged HFS neutral orbitals (t5_scf.scf_occ). usage: python3 xseam.py Z ...  appends xseam.jsonl. No constant; no measured input."""
import sys,os,json,numpy as np
from sympy.physics.wigner import wigner_3j
from t5_scf import scf_occ,ground_occ
from hfs import numerov_wf
SH={21:('Sc','3d'),39:('Y','4d'),55:('Cs','6s'),57:('La','5d'),64:('Gd','5d'),71:('Lu','5d')}
CX=-(3.0/4.0)*(6.0/np.pi)**(1.0/3.0)
def Yk(f,r,dr,k):
    a=np.cumsum(f*r**k*dr)-0.5*f*r**k*dr; b=np.cumsum((f/r**(k+1)*dr)[::-1])[::-1]-0.5*f/r**(k+1)*dr
    return a/r**(k+1)+b*r**k
for Z in map(int,sys.argv[1:]):
    el,sh=SH[Z]; occ=ground_occ(Z); na,la=int(sh[0]),"spdf".index(sh[1])
    Vf,Es,Et,it=scf_occ(Z,occ,1)
    x=np.linspace(np.log(1e-6/Z),np.log(300.0),4000); r=np.exp(x); h=x[1]-x[0]; dr=r*h
    P={}
    for n,l,k in occ:
        rr,drr,u,E,nd=numerov_wf(Vf,l,n,1.0,Z); ui=np.interp(r,rr,u,left=0.0,right=0.0); ui/=np.sqrt(np.sum(ui*ui*dr)); P[(n,l)]=ui
    Pi=P[(na,la)]; ni=Pi*Pi
    nc=sum(k*P[(n,l)]**2 for n,l,k in occ if (n,l)!=(na,la))
    w=4*np.pi*r*r
    Ex=lambda nu,nd_: CX*np.sum(((nu/w)**(4/3)+(nd_/w)**(4/3))*w*dr)
    Dx_LSD=Ex(nc/2+ni,nc/2)-Ex(nc/2,nc/2)-Ex(ni,0*ni)
    Dx_HF=0.0; parts={}
    for n,l,k in occ:
        if (n,l)==(na,la): continue
        s=0.0
        for kk in range(abs(la-l),la+l+1,2):
            c=float(wigner_3j(la,kk,l,0,0,0))**2
            G=float(np.sum(Pi*P[(n,l)]*Yk(Pi*P[(n,l)],r,dr,kk)*dr))
            s+=c*G
        parts[f"{n}{'spdf'[l]}"]=round(-0.5*k*s,5); Dx_HF+=-0.5*k*s
    out=dict(Z=Z,el=el,sh=sh,Dx_HF=round(Dx_HF,5),Dx_LSD=round(Dx_LSD,5),Delta_x=round(Dx_LSD-Dx_HF,5),HF_parts=parts,Ex_pol_ent=round(float(Ex(ni,0*ni)),5))
    open('xseam.jsonl','a').write(json.dumps(out)+'\n'); print(out,flush=True)