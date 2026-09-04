"""cand_i.py -- s33 PREDICTION-CAND: candidate (i) PBE-form gradient correction on the chain's own eps_c^S, on both lines of the SIC-cancellation law,
plus A_half (bench-vs-S on the f=1/2 one-orbital line, bench RECALLED comparison only). Appends cand_i.jsonl. usage: Z ..."""
import sys,os,json,time,numpy as np
assert os.environ.get("SIC_NOCLAMP")=="1" and os.environ.get("SUBCELL")=="1"
from t7c_corrz import scf_sic_corr; from t5_scf import ground_occ,minus; import corr_sosex as CS
SH={55:('Cs','6s'),21:('Sc','3d'),22:('Ti','3d'),24:('Cr','3d'),26:('Fe','3d'),28:('Ni','3d'),29:('Cu','3d'),39:('Y','4d'),57:('La','5d'),64:('Gd','5d'),71:('Lu','5d'),66:('Dy','4f'),68:('Er','4f'),69:('Tm','4f'),70:('Yb','4f')}
B0=dict(rs=np.log([1,2,3,5,10]),e=[-0.0600,-0.0448,-0.0369,-0.0281,-0.0186]); B1=dict(rs=np.log([2,5,10]),e=[-0.0240,-0.0154,-0.0105])
def bench1(rs): return np.interp(np.log(rs),B1['rs'],B1['e'])
GAM=(1-np.log(2))/np.pi**2; BET=0.066725   # gamma derived; beta Ma-Brueckner RECALLED (comparison only)
def H_pbe(n,z,gn,eps):
    n=np.maximum(n,1e-30); phi=((1+z)**(2/3)+(1-z)**(2/3))/2; kf=(3*np.pi**2*n)**(1/3); ks=np.sqrt(4*kf/np.pi)
    t2=(gn/(2*phi*ks*n))**2; A=(BET/GAM)/np.expm1(np.clip(-eps/(GAM*phi**3),1e-12,700))
    x=(BET/GAM)*t2*(1+A*t2)/(1+A*t2+A*A*t2*t2); return GAM*phi**3*np.log1p(x)
OUT="cand_i.jsonl"; done={json.loads(l)['Z'] for l in open(OUT)} if os.path.exists(OUT) else set()
for Z in map(int,sys.argv[1:]):
    if Z in done: print("SKIP",Z); continue
    el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); hole=minus(ground_occ(Z),n,l,1.0); t0=time.time()
    Es,h,s=scf_sic_corr(Z,1,occ=hole,entrant=(n,l),mode="all",corr="S"); L=scf_sic_corr.last; r,dr=L['r'],L['dr']
    nsig={'u':np.zeros_like(r),'d':np.zeros_like(r)}; nent=None
    for c in L['chans']:
        nn,ll,k,ss,f,tag=c; nsig[ss]+=k*L['dens'][c]
        if tag=='ent': nent=L['dens'][c]
    w=4*np.pi*r*r; nu,nd=nsig['u']/w,nsig['d']/w; ntot=nu+nd; z=np.clip((nu-nd)/np.maximum(ntot,1e-30),0,1)
    ne=np.maximum(0.5*nent/w,1e-30); zero=np.zeros_like(ne); one=np.ones_like(ne); rse=(3/(4*np.pi*ne))**(1/3)
    W=nent*dr; W=W/np.sum(W)
    eS_tot=CS.eps_S(nu,nd); eS_ent=CS.eps_S(ne,zero)
    gtot=np.abs(np.gradient(ntot,r)); gent=np.abs(np.gradient(ne,r))
    Ht=H_pbe(ntot,z,gtot,eS_tot); He=H_pbe(ne,one,gent,eS_ent)
    okE=(rse>=1)&(rse<=10); Ah=float(np.sum((W*(bench1(rse)-eS_ent))[okE]))
    o=dict(Z=Z,el=el,sh=sh,rs_w_ent2=round(float(np.sum(W*rse)),3),eps_ent_line=round(float(np.sum(W*eS_ent)),5),eps_tot_line=round(float(np.sum(W*eS_tot)),5),
      H_tot=round(float(np.sum(W*Ht)),5),H_ent=round(float(np.sum(W*He)),5),Delta_i=round(float(np.sum(W*(Ht-He))),5),
      t2_ent=round(float(np.sum(W*(gent/(2*0.7937*np.sqrt(4*(3*np.pi**2*ne)**(1/3)/np.pi)*ne))**2)),3),A_half=round(Ah,5),frac_E=round(float(np.sum(W[okE])),3),sec=int(time.time()-t0))
    open(OUT,'a').write(json.dumps(o)+'\n'); print(o,flush=True)