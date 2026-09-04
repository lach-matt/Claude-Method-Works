"""exent.py -- s24: |E_x^LSD[n_ent]| of the converged f=1/2 entrant orbital (t7c_cuaudit standing settings), PO14. Appends exent.jsonl."""
import sys,json,os,numpy as np,time
assert os.environ.get("SIC_NOCLAMP")=="1"
from t7c_cuaudit import scf_sic_corr
from t5_scf import ground_occ,minus
SH={55:('Cs','6s'),21:('Sc','3d'),22:('Ti','3d'),24:('Cr','3d'),26:('Fe','3d'),28:('Ni','3d'),29:('Cu','3d'),39:('Y','4d'),57:('La','5d'),64:('Gd','5d'),71:('Lu','5d'),66:('Dy','4f'),68:('Er','4f'),69:('Tm','4f'),70:('Yb','4f')}
done={json.loads(l)['Z'] for l in open('exent.jsonl')} if os.path.exists('exent.jsonl') else set()
for Z in map(int,sys.argv[1:]):
    if Z in done: continue
    el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); t0=time.time()
    Es,h,s=scf_sic_corr(Z,1,occ=minus(ground_occ(Z),n,l,1.0),entrant=(n,l),mode="all",corr="Z")
    L=scf_sic_corr.last; r=L['r']; dr=L['dr']; c=[c for c in L['chans'] if c[5]=='ent'][0]; ni=L['dens'][c]; rho=ni/(4*np.pi*r*r)
    Ex=float(-(3/4)*(6/np.pi)**(1/3)*np.sum(rho**(4/3)*4*np.pi*r*r*dr)); U=float(0.5*np.sum(ni*np.cumsum(ni*dr)/r*dr)*2)  # rough U not used
    out=dict(Z=Z,el=el,sh=sh,Ex_ent=round(Ex,4),rmean=round(float(np.sum(r*ni*dr)),3),it=len(h),sec=int(time.time()-t0))
    open('exent.jsonl','a').write(json.dumps(out)+'\n'); print(out,flush=True)