"""xseam_relax.py -- s35 PREDICTION-B2: candidate (b). (b1) core relaxation of the E-path local+SIC removal-exchange: relaxed (t5_scf ion SCF, qtail 2)
minus FROZEN (xseam.jsonl Dx_LSD, same functional, same neutral orbitals). (b2) correlation difference between the paths under ONE form S: DEc_O of record
(frachf_S.jsonl DEc_R field, HF orbitals, hfc2 E_c convention: per-electron SIC on P^2) minus DEc_E = the SAME expression on the relaxed E-path (HFS) orbitals,
hfc2.spin_split (Hund) as on the O path. Exchange conventions as xseam (core spin-averaged, entrant polarised, entrant SIC; core SIC per electron on P^2 both sides).
rem := b2 - b1; seam_pred := -(Delta_x + b1 - b2); compare rem with target Delta_x + seam. usage: python3 xseam_relax.py Z ...  appends xseam_relax.jsonl (resumable).
No constant; no measured input (seam of record enters only in the comparison column)."""
import sys,os,json,time,numpy as np
from t5_scf import scf_occ,ground_occ,minus
from hfs import numerov_wf
import corr_sosex as CS, hfc2 as H
SH={21:('Sc','3d'),39:('Y','4d'),55:('Cs','6s'),57:('La','5d'),64:('Gd','5d'),71:('Lu','5d')}
SEAM={21:0.045,39:0.025,57:0.018,64:0.015,71:0.023,55:0.015}     # O_DSCF - E_DSCF, FINDING-B s34 (record; comparison only)
XS={d['Z']:d for d in map(json.loads,open('xseam.jsonl'))}
FS={d['Z']:d for d in map(json.loads,open('frachf_S.jsonl'))}
OUT='xseam_relax.jsonl'; done={d['Z'] for d in map(json.loads,open(OUT))} if os.path.exists(OUT) else set()
CX=-(3.0/4.0)*(6.0/np.pi)**(1.0/3.0)
def orbs(Z,occ,qtail):
    Vf,Es,Et,it=scf_occ(Z,occ,qtail)
    x=np.linspace(np.log(1e-6/Z),np.log(300.0),4000); r=np.exp(x); h=x[1]-x[0]; dr=r*h; P={}
    for n,l,k in occ:
        rr,drr,u,E,nd=numerov_wf(Vf,l,n,1.0,Z); ui=np.interp(r,rr,u,left=0.0,right=0.0); ui/=np.sqrt(np.sum(ui*ui*dr)); P[(n,l)]=ui
    return r,dr,P,it
def Ex(nu,nd,w,dr): return CX*np.sum(((nu/w)**(4/3)+(nd/w)**(4/3))*w*dr)
def Ec(nu,nd,w,dr): return float(np.sum((nu+nd)*CS.eps_S(nu/w,nd/w)*dr))
def ex_tot(occ,P,ent,w,dr):
    """xseam convention: core spin-averaged, entrant (if present, k>=1) polarised one electron in up; SIC per electron on P^2 for every shell."""
    nc=sum(k*P[(n,l)]**2 for n,l,k in occ if (n,l)!=ent); ni=P[ent]**2 if ent in P else 0*nc
    E=Ex(nc/2+ni,nc/2,w,dr)
    for n,l,k in occ: E-=k*Ex(P[(n,l)]**2,0*nc,w,dr)
    return float(E)
def ec_tot(occ,P,w,dr):
    nu,nd,_=H.spin_split(occ,P); E=Ec(nu,nd,w,dr)
    for n,l,k in occ: E-=k*Ec(P[(n,l)]**2,0*nu,w,dr)
    return float(E)
for Z in map(int,sys.argv[1:]):
    if Z in done: print("SKIP",Z); continue
    el,sh=SH[Z]; ent=(int(sh[0]),"spdf".index(sh[1])); t0=time.time()
    occ0=ground_occ(Z); occ1=minus(occ0,ent[0],ent[1],1.0)
    r,dr,P0,it0=orbs(Z,occ0,1); w=4*np.pi*r*r
    r,dr,P1,it1=orbs(Z,occ1,2)
    Ex0=ex_tot(occ0,P0,ent,w,dr); Ex1r=ex_tot(occ1,P1,ent,w,dr); Ex1f=ex_tot(occ1,P0,ent,w,dr)
    Dx_rel=Ex0-Ex1r; Dx_frz=Ex0-Ex1f; xs=XS[Z]
    Ec0=ec_tot(occ0,P0,w,dr); Ec1r=ec_tot(occ1,P1,w,dr); Ec1f=ec_tot(occ1,P0,w,dr)
    DEc_E=Ec0-Ec1r; DEc_Ef=Ec0-Ec1f; DEc_O=FS[Z]['DEc_R']
    b1=Dx_rel-Dx_frz; b2=DEc_O-DEc_E; Dx=xs['Delta_x']; rem=b2-b1; seam_pred=-(Dx+b1-b2)
    o=dict(Z=Z,el=el,sh=sh,it=[it0,it1],Dx_frz=round(Dx_frz,5),Dx_frz_xseam=xs['Dx_LSD'],Dx_rel=round(Dx_rel,5),b1=round(b1,5),
           DEc_E=round(DEc_E,5),DEc_E_frozen=round(DEc_Ef,5),DEc_O=DEc_O,b2=round(b2,5),Delta_x=Dx,rem=round(rem,5),
           rem_target=round(Dx+SEAM[Z],5),seam_pred=round(seam_pred,5),seam=SEAM[Z],resid=round(seam_pred-SEAM[Z],5),sec=int(time.time()-t0))
    open(OUT,'a').write(json.dumps(o)+'\n'); print(o,flush=True)