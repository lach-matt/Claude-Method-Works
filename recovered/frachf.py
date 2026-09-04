"""frachf.py -- s28 F26.2 lifted: self-consistent HFSR 'hf' + chain-Z correlation (PZ SIC) along the entrant fractional path f = 0,1/4,1/2,3/4,1,
entrant as ONE spin-orbital at weight f (t7b_hf.frac). Also the HF-only path (CORR=0 style) at the same f. usage: python3 frachf.py Z ...
Appends frachf.jsonl (key Z). Class rows only (entrant alone in its shell). No constant beyond c; no measured input."""
import sys,os,json,time,numpy as np
os.environ.setdefault("SIC_NOCLAMP","1"); os.environ.setdefault("SUBCELL","1")
import hfc2 as H
from t7c_kernel import C0
from t5_scf import ground_occ,minus
import t7c_cuaudit as T
OUT="frachf.jsonl"
SH={21:('Sc','3d'),39:('Y','4d'),55:('Cs','6s'),57:('La','5d'),64:('Gd','5d'),71:('Lu','5d')}
class HFCf(H.HFC):
    ent=None; f=1.0
    def corr_pot(self,P):
        r=self.r; w=4*np.pi*r*r; nu,nd,sp=H.spin_split(self.occ,P); vu,vd=T.v_gbz(nu/w,nd/w); V={}
        for a,b,q in self.occ:
            up,dn=sp[(a,b)]; vs=(up*vu+dn*vd)/q
            ff=self.f if (a,b)==self.ent else 1.0
            V[(a,b)]=vs-T.v_gbz(ff*P[(a,b)]**2/w,0*r)[0]
        return V
    def E_c(self,P):
        r,dr=self.r,self.dr; w=4*np.pi*r*r; nu,nd,_=H.spin_split(self.occ,P)
        E=float(np.sum((nu+nd)*H.eps_c(nu/w,nd/w)*dr))
        for a,b,q in self.occ:
            ff=self.f if (a,b)==self.ent else 1.0
            E-=q*float(np.sum(P[(a,b)]**2*H.eps_c(ff*P[(a,b)]**2/w,0*r)*dr))
        return E
def path(Z,n,l,corr):
    H.CORR=corr; out={}
    occ0=ground_occ(Z); q0=[q for a,b,q in occ0 if (a,b)==(n,l)][0]; assert abs(q0-1.0)<1e-9, "class row only (entrant alone in shell)"
    for f in (0.0,0.25,0.5,0.75,1.0):
        occ=[(a,b,(f if (a,b)==(n,l) else q)) for a,b,q in occ0 if not ((a,b)==(n,l) and f==0.0)]
        h=HFCf(Z,occ,c=C0); h.ent=(n,l); h.f=f
        if f>0: h.frac={(n,l):(0,f)}
        E,Ec,it,eps=h.run2(); out[f]=dict(E=float(E),Ec=float(Ec),eps=(float(eps[(n,l)]) if f>0 else None),it=it)
    return out
done={d['Z'] for d in map(json.loads,open(OUT))} if os.path.exists(OUT) else set()
H27={d['Z']:d for d in map(json.loads,open('hfc2.jsonl')) if d['corr']}
for Z in map(int,sys.argv[1:]):
    if Z in done: print("SKIP",Z); continue
    el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); t0=time.time()
    pc=path(Z,n,l,True); ph=path(Z,n,l,False)
    Et={f:pc[f]['E']+pc[f]['Ec'] for f in pc}
    # eps at f=0: extrapolate not needed for Simpson? Janak needs eps(0): use eps of an f->0 limit = run at f=1e-3? avoid: use 3-point with f=1/4..1 Simpson on [0,1] needs eps(0).
    # Use Simpson 3/8 on f=1/4,1/2,3/4,1 for the last 3/4 plus trapezoid... instead: Janak check as int_0^1 eps df by Simpson on (0,1/2,1) with eps(0):=2eps(1/4)-eps(1/2) (linear extrapolation) -- stated.
    e=lambda p,f:p[f]['eps']; e0c=2*e(pc,0.25)-e(pc,0.5); e0h=2*e(ph,0.25)-e(ph,0.5)
    simp_c=(e0c+4*e(pc,0.5)+e(pc,1.0))/6; simp_h=(e0h+4*e(ph,0.5)+e(ph,1.0))/6
    D_c=Et[1.0]-Et[0.0]; D_h=ph[1.0]['E']-ph[0.0]['E']; DEc=pc[1.0]['Ec']-pc[0.0]['Ec']
    Dc_mid=e(pc,0.5)-e(ph,0.5)
    o=dict(Z=Z,el=el,sh=sh,corr_path={str(f):{k:(round(v,6) if isinstance(v,float) else v) for k,v in d.items()} for f,d in pc.items()},
           hf_path={str(f):{k:(round(v,6) if isinstance(v,float) else v) for k,v in d.items()} for f,d in ph.items()},
           D_tot_corr=round(D_c,6),simpson_eps_corr=round(simp_c,6),janak_gap_corr=round(D_c-simp_c,6),
           D_HF=round(D_h,6),simpson_eps_hf=round(simp_h,6),janak_gap_hf=round(D_h-simp_h,6),
           DEc_sc=round(DEc,6),Delta_c_sc_mid=round(Dc_mid,6),gap_sc=round(DEc-Dc_mid,6),
           eps_mid_corr=round(e(pc,0.5),6),obj2_hfc2=H27.get(Z,{}).get('obj_2'),D_HF_hfc2=H27.get(Z,{}).get('D_HF'),
           Ec_neu_hfc2=H27.get(Z,{}).get('Ec_neu'),Ec_ion_hfc2=H27.get(Z,{}).get('Ec_ion'),sec=int(time.time()-t0))
    open(OUT,"a").write(json.dumps(o)+"\n"); print({k:v for k,v in o.items() if k not in('corr_path','hf_path')},flush=True)
    print(" corr eps:",[o['corr_path'][k]['eps'] for k in ('0.25','0.5','0.75','1.0')]," hf eps:",[o['hf_path'][k]['eps'] for k in ('0.25','0.5','0.75','1.0')])
