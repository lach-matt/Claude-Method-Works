"""xfock.py -- s26 item (2)(a): first-order replacement of the entrant's LSD(+SIC) exchange by exact Fock exchange with the other same-spin
occupied electrons, at the standing f=1/2 chain-Z orbitals. usage: SIC_NOCLAMP=1 python3 xfock.py Z ...  Appends xfock.jsonl. No constant."""
import sys, os, json, time
assert os.environ.get("SIC_NOCLAMP")=="1"
os.environ["FOCC"]="0.5"; os.environ["FENT"]="0.5"
import numpy as np
import t7c_cuaudit as T
from t5_scf import ground_occ, minus
from hfs_sic import hartree
from t7b_hf import _c3j0sq
OUT="xfock.jsonl"
SH={21:('Sc','3d'),22:('Ti','3d'),24:('Cr','3d'),26:('Fe','3d'),28:('Ni','3d'),29:('Cu','3d'),39:('Y','4d'),55:('Cs','6s'),57:('La','5d'),
    64:('Gd','5d'),66:('Dy','4f'),68:('Er','4f'),69:('Tm','4f'),70:('Yb','4f'),71:('Lu','5d')}
def Yk(Pa,Pb,k,r,dr):
    w=Pa*Pb*dr; A=np.cumsum(w*r**k)-0.5*w*r**k; B=np.cumsum((w/r**(k+1))[::-1])[::-1]-0.5*w/r**(k+1); return A/r**k+B*r**(k+1)
def Gk(Pa,Pb,k,r,dr): return float(np.sum(Pa*Pb*Yk(Pa,Pb,k,r,dr)/r*dr))
done={d['Z'] for d in map(json.loads,open(OUT))} if os.path.exists(OUT) else set()
for Z in map(int,sys.argv[1:]):
    if Z in done: print("SKIP",Z); continue
    el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); hole=minus(ground_occ(Z),n,l,1.0); t0=time.time()
    Es,h,s=T.scf_sic_corr(Z,1,occ=hole,entrant=(n,l),corr="Z",mode="all")
    L=T.scf_sic_corr.last; chans,dens,r,dr=L["chans"],L["dens"],L["r"],L["dr"]; npts=len(r); w=4*np.pi*r*r
    ent=[c for c in chans if c[5]=="ent"][0]; s_ent=ent[3]; ne=dens[ent]; Pe=np.sqrt(np.maximum(ne,0)); f=ent[2]
    nsig=np.zeros(npts)
    for c in chans:
        if c[3]==s_ent: nsig+=c[2]*dens[c]
    # LSD exchange treatment of the entrant in the chain (Janak derivative at f): v_x[n_sigma] - v_x[f n_ent]
    vx_tot=-(6.0*(nsig/w)/np.pi)**(1/3); vx_self=-(6.0*(f*ne/w)/np.pi)**(1/3)
    lsd=float(np.sum(ne*(vx_tot-vx_self)*dr))
    # exact exchange with the other same-spin occupied electrons (spherical average), own channel excluded
    ex=0.0; terms={}
    for c in chans:
        if c[3]!=s_ent or c is ent: continue
        lb=c[1]; qb=c[2]; Pb=np.sqrt(np.maximum(dens[c],0)); t=0.0
        for k in range(abs(l-lb),l+lb+1,2):
            cf=_c3j0sq(l,k,lb)
            if cf: t+=qb*cf*Gk(Pe,Pb,k,r,dr)
        ex-=t; terms["%d%s%s"%(c[0],"spdf"[lb],c[5])]=round(-t,5)
    G0self=Gk(Pe,Pe,0,r,dr); vHself=float(np.sum(ne*hartree(ne,r,dr)*dr))
    o=dict(Z=Z,el=el,sh=sh,eps_half=round(float(Es[(n,l,s,"ent")]),5),it_ref=len(h),lsd_x=round(lsd,5),exact_x=round(ex,5),Delta_x=round(ex-lsd,5),
           G0self=round(G0self,5),vHself=round(vHself,5),terms=terms,sec=int(time.time()-t0))
    open(OUT,"a").write(json.dumps(o)+"\n"); print(o,flush=True)
