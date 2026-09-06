"""rz_mech.py -- s31 PREDICTION-RZMECH: per row, the entrant's correlation-weighted r_s window and the local shortfall estimate of R and Z against a RECALLED
benchmark eps_c (Ceperley-Alder/PW92 zeta=0; Loos-Gill Tab.II zeta=1) -- comparison only, NOT ENTERED. Appends rz_mech.jsonl. usage: Z ..."""
import sys,os,json,time,numpy as np
assert os.environ.get("SIC_NOCLAMP")=="1" and os.environ.get("SUBCELL")=="1"
from t7c_corrz import scf_sic_corr; from t5_scf import ground_occ,minus; import corr_ring as CR, t7c_cuaudit as T
SH={55:('Cs','6s'),21:('Sc','3d'),22:('Ti','3d'),24:('Cr','3d'),26:('Fe','3d'),28:('Ni','3d'),29:('Cu','3d'),39:('Y','4d'),57:('La','5d'),64:('Gd','5d'),71:('Lu','5d'),66:('Dy','4f'),68:('Er','4f'),69:('Tm','4f'),70:('Yb','4f')}
# RECALLED benchmark (Ha): zeta=0 rs 1,2,3,5,10 ; zeta=1 rs 2,5,10 (interpolated linearly in ln rs, held at ends); z-interp linear
B0=dict(rs=np.log([1,2,3,5,10]),e=[-0.0600,-0.0448,-0.0369,-0.0281,-0.0186]); B1=dict(rs=np.log([2,5,10]),e=[-0.0240,-0.0154,-0.0105])
def bench(rs,z):
    l=np.log(rs); e0=np.interp(l,B0['rs'],B0['e']); e1=np.interp(l,B1['rs'],B1['e']); return (1-z)*e0+z*e1
OUT="rz_mech.jsonl"; done={json.loads(l)['Z'] for l in open(OUT)} if os.path.exists(OUT) else set()
for Z in map(int,sys.argv[1:]):
    if Z in done: print("SKIP",Z); continue
    el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); hole=minus(ground_occ(Z),n,l,1.0); t0=time.time()
    Es,h,s=scf_sic_corr(Z,1,occ=hole,entrant=(n,l),mode="all",corr="R"); L=scf_sic_corr.last; r,dr=L['r'],L['dr']
    nsig={'u':np.zeros_like(r),'d':np.zeros_like(r)}; nent=None
    for c in L['chans']:
        nn,ll,k,ss,f,tag=c; nsig[ss]+=k*L['dens'][c]
        if tag=='ent': nent=L['dens'][c]
    w=4*np.pi*r*r; nu,nd=nsig['u']/w,nsig['d']/w; ntot=nu+nd; z=np.clip((nu-nd)/np.maximum(ntot,1e-30),0,1)
    rs=(3/(4*np.pi*np.maximum(ntot,1e-30)))**(1/3)
    eR=CR.eps_R(nu,nd); eZ=CR._chain(rs,z); eB=bench(rs,z); ok=(rs>=0.5)&(rs<=10)
    W=nent*dr; Wc=nent*np.abs(eR)*dr
    rs_w=float(np.sum(W*rs)/np.sum(W)); rs_wc=float(np.sum(Wc*rs)/np.sum(Wc)); z_wc=float(np.sum(Wc*z)/np.sum(Wc))
    frac_win=float(np.sum(W[ok])/np.sum(W))
    dR=float(np.sum((W*(eB-eR))[ok])); dZ=float(np.sum((W*(eB-eZ))[ok]))     # entrant-weighted local shortfall (Ha), window 0.5<=rs<=10 only
    ER=float(Es[(n,l,s,'ent')])
    out=dict(Z=Z,el=el,sh=sh,ER=round(ER,4),rs_w=round(rs_w,3),rs_wc=round(rs_wc,3),z_wc=round(z_wc,3),frac_win=round(frac_win,3),dR_loc=round(dR,5),dZ_loc=round(dZ,5),sec=int(time.time()-t0))
    open(OUT,'a').write(json.dumps(out)+'\n'); print(out,flush=True)