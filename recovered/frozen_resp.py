"""frozen_resp.py -- s26 item (1) addendum: is M_resp the linear (second-order) response of the entrant orbital to dV_f = V_fr(f)-V_fr(1/2)?
usage: SIC_NOCLAMP=1 [CORR=Z|none] python3 frozen_resp.py Z ...   Appends frozen_resp.jsonl (Z,corr). Same reference SCF and frozen potentials
as frozen_scan3.py; eigen-solves at V_ref +/- d*dV_f (d=0.1, 0.05) and along the SIC-x shape -v_x[n_ent]. No constant, no measured input."""
import sys, os, json, time
assert os.environ.get("SIC_NOCLAMP")=="1"
os.environ["FOCC"]="0.5"; os.environ["FENT"]="0.5"
import numpy as np
from scipy.integrate import trapezoid
import t7c_cuaudit as T
from t5_scf import ground_occ, minus
from hfs_sic import hartree
from t7c_kernel import numerov_wf_sr, _derivs, C0
CORRENV=os.environ.get("CORR","Z"); CORR=None if CORRENV=="none" else CORRENV
OUT="frozen_resp.jsonl"
SH={21:('Sc','3d'),22:('Ti','3d'),24:('Cr','3d'),26:('Fe','3d'),28:('Ni','3d'),29:('Cu','3d'),39:('Y','4d'),55:('Cs','6s'),57:('La','5d'),
    64:('Gd','5d'),66:('Dy','4f'),68:('Er','4f'),69:('Tm','4f'),70:('Yb','4f'),71:('Lu','5d')}
GRID=[0.001,0.05,0.15,0.25,0.5,0.75,1.0]
K=3/5-(3/2)*2**(-1/3)+2**(-2/3)   # int_0^1 (f^(1/3)-2^(-1/3))^2 df
def integ(fs,vals):
    fs=np.asarray(fs,float); vals=np.asarray(vals,float); o=np.argsort(fs); fs=fs[o]; vals=vals[o]
    x=fs**(1/3); xs=np.linspace(0,1,20001); return float(trapezoid(np.interp(xs,x,vals),xs**3))
done={(d['Z'],d['corr']) for d in map(json.loads,open(OUT))} if os.path.exists(OUT) else set()
for Z in map(int,sys.argv[1:]):
    if (Z,CORRENV) in done: print("SKIP",Z,CORRENV); continue
    el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); hole=minus(ground_occ(Z),n,l,1.0); t0=time.time()
    Es,h,s=T.scf_sic_corr(Z,1,occ=hole,entrant=(n,l),corr=CORR,mode="all")
    L=T.scf_sic_corr.last; chans,dens,r,dr=L["chans"],L["dens"],L["r"],L["dr"]; x=np.log(r); npts=len(r); w=4*np.pi*r*r
    ent=[c for c in chans if c[5]=="ent"][0]; s_ent=ent[3]; ne=dens[ent]; rhoe=ne/w
    def Vfr(f):
        nsig={"u":np.zeros(npts),"d":np.zeros(npts)}
        for c in chans:
            k=f if c is ent else c[2]; nsig[c[3]]+=k*dens[c]
        ntot=nsig["u"]+nsig["d"]; VH=hartree(ntot,r,dr)
        rho=nsig[s_ent]/w; Vx=-(6.0*rho/np.pi)**(1.0/3.0)
        if CORR=="Z":
            vu,vd=T.v_gbz(nsig["u"]/w,nsig["d"]/w); Vc=(vu if s_ent=="u" else vd)
        else: Vc=np.zeros(npts)
        ni=f*ne; rhoi=ni/w
        vHi=hartree(ni,r,dr); vxi=-(6.0*rhoi/np.pi)**(1.0/3.0); vci=T.v_gbz(rhoi,0*rhoi)[0] if CORR=="Z" else np.zeros(npts)
        return -Z/r+VH+Vx+Vc-(vHi+vxi+vci)
    def eig(V):
        Vp,Vpp=_derivs(x,V)
        Vf=lambda rr,V=V: np.interp(np.log(np.asarray(rr,float)),x,V)
        Vfp=lambda rr,V=Vp: np.interp(np.log(np.asarray(rr,float)),x,V)
        Vfpp=lambda rr,V=Vpp: np.interp(np.log(np.asarray(rr,float)),x,V)
        rr,drr,u,E,nd=numerov_wf_sr(Vf,l,n,1.0,Z,C0,Vp=Vfp,Vpp=Vfpp); assert nd==n-l-1; return float(E)
    Vref=Vfr(0.5); e_ref=eig(Vref); e_scan={}
    def e2(dV,d): return (eig(Vref+d*dV)+eig(Vref-d*dV)-2*e_ref)/(2*d*d)
    E2={0.1:[],0.05:[]}
    for f in GRID:
        dV=Vfr(f)-Vref
        for d in E2: E2[d].append(e2(dV,d) if f!=0.5 else 0.0)
    vx_ent=-(6.0*rhoe/np.pi)**(1.0/3.0)   # SIC-x direction: dV = -(f^(1/3)-2^(-1/3)) v_x[n_ent]  ->  chi_x from curvature along -v_x
    chi_x={d:-e2(-vx_ent,d) for d in (0.1,0.05)}
    o=dict(Z=Z,el=el,sh=sh,corr=CORRENV,eps_ref=round(e_ref,5),it_ref=len(h),
           Mresp2_d10=round(integ(GRID,E2[0.1]),5),Mresp2_d05=round(integ(GRID,E2[0.05]),5),
           chi_x_d10=round(chi_x[0.1],5),chi_x_d05=round(chi_x[0.05],5),Mx2_d10=round(-K*chi_x[0.1],5),K=round(K,5),
           e2_grid_d10=[round(v,5) for v in E2[0.1]],sec=int(time.time()-t0))
    open(OUT,"a").write(json.dumps(o)+"\n"); print(o,flush=True)
