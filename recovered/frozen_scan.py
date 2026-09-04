"""frozen_scan.py -- s25 item (2): frozen-orbital f-scan around the f=1/2 reference. usage: SIC_NOCLAMP=1 python3 frozen_scan.py Z [f ...]
Reference SCF via t7c_cuaudit.scf_sic_corr (FOCC=FENT=0.5, mode all, corr Z). All densities frozen; entrant weight f varied; one solve per f.
Appends frozen_scan.jsonl (Z, f, E_fr) with done-tracking. No constant, no measured input."""
import sys, os, json, time
assert os.environ.get("SIC_NOCLAMP")=="1"
os.environ["FOCC"]="0.5"; os.environ["FENT"]="0.5"
import numpy as np
import t7c_cuaudit as T
from t5_scf import ground_occ, minus
from hfs_sic import hartree
from t7c_kernel import numerov_wf_sr, _derivs, C0
OUT="frozen_scan.jsonl"
SH={21:('Sc','3d'),22:('Ti','3d'),24:('Cr','3d'),26:('Fe','3d'),28:('Ni','3d'),29:('Cu','3d'),39:('Y','4d'),55:('Cs','6s'),57:('La','5d'),
    64:('Gd','5d'),66:('Dy','4f'),68:('Er','4f'),69:('Tm','4f'),70:('Yb','4f'),71:('Lu','5d')}
Z=int(sys.argv[1]); el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); hole=minus(ground_occ(Z),n,l,1.0)
fs=[float(a) for a in sys.argv[2:]] or [0.001,0.05,0.15,0.25,0.5,0.75,1.0]
done={(d['Z'],d['f']) for d in map(json.loads,open(OUT))} if os.path.exists(OUT) else set()
if all((Z,f) in done for f in fs): print("SKIP",Z); sys.exit()
t0=time.time(); Es,h,s=T.scf_sic_corr(Z,1,occ=hole,entrant=(n,l),corr="Z",mode="all")
L=T.scf_sic_corr.last; chans,dens,r,dr=L["chans"],L["dens"],L["r"],L["dr"]; x=np.log(r); npts=len(r)
ent=[c for c in chans if c[5]=="ent"][0]; s_ent=ent[3]
E_ref=float(Es[(n,l,s,"ent")])
def solve(f):
    nsig={"u":np.zeros(npts),"d":np.zeros(npts)}
    for c in chans:
        k=f if c is ent else c[2]
        nsig[c[3]]+=k*dens[c]
    ntot=nsig["u"]+nsig["d"]; VH=hartree(ntot,r,dr)
    rho=nsig[s_ent]/(4*np.pi*r*r); Vx=-(6.0*rho/np.pi)**(1.0/3.0)
    vu,vd=T.v_gbz(nsig["u"]/(4*np.pi*r*r),nsig["d"]/(4*np.pi*r*r)); Vc=vu if s_ent=="u" else vd
    Vraw=-Z/r+VH+Vx+Vc
    ni=f*dens[ent]; rhoi=ni/(4*np.pi*r*r)
    vHi=hartree(ni,r,dr); vxi=-(6.0*rhoi/np.pi)**(1.0/3.0); vci=T.v_gbz(rhoi,0*rhoi)[0]
    Vsic=-(vHi+vxi+vci)
    Vtot=Vraw+Vsic
    Vp,Vpp=_derivs(x,Vtot)
    Vf=lambda rr,V=Vtot: np.interp(np.log(np.asarray(rr,float)),x,V)
    Vfp=lambda rr,V=Vp: np.interp(np.log(np.asarray(rr,float)),x,V)
    Vfpp=lambda rr,V=Vpp: np.interp(np.log(np.asarray(rr,float)),x,V)
    rr,drr,u,E,nd=numerov_wf_sr(Vf,l,n,1.0,Z,C0,Vp=Vfp,Vpp=Vfpp)
    assert nd==n-l-1
    return float(E)
for f in fs:
    if (Z,f) in done: continue
    E=solve(f)
    o=dict(Z=Z,el=el,sh=sh,f=f,E_fr=round(E,5),E_ref_half=round(E_ref,5),it_ref=len(h),sec=int(time.time()-t0))
    open(OUT,"a").write(json.dumps(o)+"\n"); print(o,flush=True)