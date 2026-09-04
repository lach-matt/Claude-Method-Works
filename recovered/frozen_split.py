"""frozen_split.py -- s26 item (1): term-by-term midpoint defects of the frozen mask on the f=1/2 reference SCF.
usage: SIC_NOCLAMP=1 [CORR=Z|none] python3 frozen_split.py Z ...    Appends frozen_split.jsonl with done-tracking (Z,corr).
Same reference SCF as frozen_scan3.py (t7c_cuaudit, FOCC=FENT=0.5, mode all). No eigen-solve: every quantity is <n_ent|v_T(f)>.
M_T(grid) uses the 7-pt f grid + f^(1/3) interpolation exactly as janak_table.py; M_T(fine) uses 201 points in f^(1/3). No constant."""
import sys, os, json, time
assert os.environ.get("SIC_NOCLAMP")=="1"
os.environ["FOCC"]="0.5"; os.environ["FENT"]="0.5"
import numpy as np
from scipy.integrate import trapezoid
import t7c_cuaudit as T
from t5_scf import ground_occ, minus
from hfs_sic import hartree
CORRENV=os.environ.get("CORR","Z"); CORR=None if CORRENV=="none" else CORRENV
OUT="frozen_split.jsonl"
SH={21:('Sc','3d'),22:('Ti','3d'),24:('Cr','3d'),26:('Fe','3d'),28:('Ni','3d'),29:('Cu','3d'),39:('Y','4d'),55:('Cs','6s'),57:('La','5d'),
    64:('Gd','5d'),66:('Dy','4f'),68:('Er','4f'),69:('Tm','4f'),70:('Yb','4f'),71:('Lu','5d')}
GRID=[0.001,0.05,0.15,0.25,0.5,0.75,1.0]
def midpoint(fs,vals):
    """DE_J-style integral minus value at f=1/2, janak_table convention (interp in f^(1/3), trapezoid over f)."""
    fs=np.asarray(fs,float); vals=np.asarray(vals,float); o=np.argsort(fs); fs=fs[o]; vals=vals[o]
    x=fs**(1/3); xs=np.linspace(0,1,20001); Ei=np.interp(xs,x,vals); I=float(trapezoid(Ei,xs**3))
    return I-float(vals[list(fs).index(0.5)])
def eps_c_pointwise(nu,nd):
    """same eps_c as v_gbz (chain Z, LAM1 off), masked at eps<0"""
    n=nu+nd; n=np.maximum(n,1e-30); z=np.clip((nu-nd)/n,0.0,1.0)
    rs=(3.0/(4*np.pi*n))**(1.0/3.0); L=np.log(rs)
    eps=T._lam0(z)*L+T._e0a(z)+T.E0B
    return np.where(eps<0,eps,0.0)
done={(d['Z'],d['corr']) for d in map(json.loads,open(OUT))} if os.path.exists(OUT) else set()
for Z in map(int,sys.argv[1:]):
    if (Z,CORRENV) in done: print("SKIP",Z,CORRENV); continue
    el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); hole=minus(ground_occ(Z),n,l,1.0); t0=time.time()
    Es,h,s=T.scf_sic_corr(Z,1,occ=hole,entrant=(n,l),corr=CORR,mode="all")
    L=T.scf_sic_corr.last; chans,dens,r,dr=L["chans"],L["dens"],L["r"],L["dr"]; npts=len(r); w=4*np.pi*r*r
    ent=[c for c in chans if c[5]=="ent"][0]; s_ent=ent[3]; ne=dens[ent]; rhoe=ne/w
    E_ref=float(Es[(n,l,s,"ent")])
    n0={"u":np.zeros(npts),"d":np.zeros(npts)}
    for c in chans:
        if c is ent: continue
        n0[c[3]]+=c[2]*dens[c]
    Ex_ent=0.75*float(np.sum(ne*(-(6*rhoe/np.pi)**(1/3))*dr))
    rmean=float(np.sum(r*ne*dr))
    def terms(f):
        ns={"u":n0["u"].copy(),"d":n0["d"].copy()}; ns[s_ent]=ns[s_ent]+f*ne
        rho_s=ns[s_ent]/w
        vxtot=-(6.0*rho_s/np.pi)**(1.0/3.0)
        vu,vd=T.v_gbz(ns["u"]/w,ns["d"]/w); vctot=(vu if s_ent=="u" else vd)
        rhoi=f*rhoe; vxsic=-(-(6.0*rhoi/np.pi)**(1.0/3.0)); vcsic=-T.v_gbz(rhoi,0*rhoi)[0]
        # SIC-x term uses only the entrant's own scaled density (spin-polarised, other spin zero)
        return dict(xtot=float(np.sum(ne*vxtot*dr)), ctot=float(np.sum(ne*vctot*dr)),
                    xsic=float(np.sum(ne*vxsic*dr)), csic=float(np.sum(ne*vcsic*dr)))
    keys=["xtot","ctot","xsic","csic"]
    G={k:[terms(f)[k] for f in GRID] for k in keys}
    fine=list(np.linspace(0,1,201)**3); fine[0]=1e-9
    if 0.5 not in fine: fine.append(0.5); fine.sort()
    F={k:[terms(f)[k] for f in fine] for k in keys}
    o=dict(Z=Z,el=el,sh=sh,corr=CORRENV,eps_half=round(E_ref,5),it_ref=len(h),Ex_ent=round(Ex_ent,5),rmean=round(rmean,4),
           law=round(((4/3)*2**(-1/3)-1)*Ex_ent,5))
    for k in keys:
        o["M_%s_grid"%k]=round(midpoint(GRID,G[k]),5); o["M_%s_fine"%k]=round(midpoint(fine,F[k]),5)
    o["M_exp_grid"]=round(sum(o["M_%s_grid"%k] for k in keys),5); o["M_exp_fine"]=round(sum(o["M_%s_fine"%k] for k in keys),5)
    o["sec"]=int(time.time()-t0)
    open(OUT,"a").write(json.dumps(o)+"\n"); print(o,flush=True)
