"""exfr.py -- E_x^LSD of the entrant one-spin density at the f=1/2 reference SCF, chain Z or x-only. E_x = (3/4) int rho v_x, v_x=-(6 rho/pi)^(1/3)."""
import sys,os,json,numpy as np
assert os.environ.get("SIC_NOCLAMP")=="1"; os.environ["FOCC"]="0.5"; os.environ["FENT"]="0.5"
import t7c_cuaudit as T
from t5_scf import ground_occ,minus
CORR=os.environ.get("CORR","Z"); CORR=None if CORR=="none" else CORR
SH={21:('Sc','3d'),70:('Yb','4f'),26:('Fe','3d'),55:('Cs','6s')}
for Z in map(int,sys.argv[1:]):
    el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); hole=minus(ground_occ(Z),n,l,1.0)
    Es,h,s=T.scf_sic_corr(Z,1,occ=hole,entrant=(n,l),corr=CORR,mode="all"); L=T.scf_sic_corr.last
    ent=[c for c in L["chans"] if c[5]=="ent"][0]; r,dr=L["r"],L["dr"]; ni=L["dens"][ent]  # normalised to 1 electron
    rho=ni/(4*np.pi*r*r); Ex=0.75*float(np.sum(ni*(-(6*rho/np.pi)**(1/3))*dr))
    print(json.dumps(dict(Z=Z,el=el,corr=CORR or "none",Ex_ent_ref=round(Ex,5),eps_half=round(float(Es[(n,l,s,"ent")]),5),it=len(h))))