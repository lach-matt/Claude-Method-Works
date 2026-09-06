"""onefunc.py -- s28 item (2): E_c(f) on the frozen neutral HFSR 'hf' orbitals; five points f=0,1/4,1/2,3/4,1; analytic slopes at 0,1/2,1.
E_c(f) = E_c[n_c+f n_e] - f E_c^pol[f n_e]  (other-shell SIC dropped: f-independent). eps_c exactly as v_gbz (SUBCELL honoured if set).
usage: python3 onefunc.py Z ...  appends onefunc.jsonl (key Z). No constant beyond c; no measured input."""
import sys,os,json,time,numpy as np
os.environ.setdefault("SIC_NOCLAMP","1")
from t7c_hfsr import HFSR
from t7c_kernel import C0
from t5_scf import ground_occ,minus
import t7c_cuaudit as T
from cellcut import SUBCELL, frac_neg
OUT="onefunc.jsonl"
SH={21:('Sc','3d'),39:('Y','4d'),55:('Cs','6s'),57:('La','5d'),64:('Gd','5d'),71:('Lu','5d'),22:('Ti','3d'),70:('Yb','4f')}
def eps_c(nu,nd):
    n=nu+nd; n=np.maximum(n,1e-30); z=np.clip((nu-nd)/n,0.0,1.0)
    rs=(3.0/(4*np.pi*n))**(1.0/3.0); L=np.log(rs)
    e=T._lam0(z)*L+T._e0a(z)+T.E0B+((T._lam1(z)*rs*L) if T.LAM1 else 0.0)
    return e*frac_neg(e) if SUBCELL else np.where(e<0,e,0.0)
done={d['Z'] for d in map(json.loads,open(OUT))} if os.path.exists(OUT) else set()
H26={d['Z']:d for d in map(json.loads,open('hfdscf.jsonl'))}
H27={d['Z']:d for d in map(json.loads,open('hfc2.jsonl')) if d['corr']}
for Z in map(int,sys.argv[1:]):
    if Z in done: print("SKIP",Z); continue
    el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); t0=time.time()
    occ0=ground_occ(Z); h0=HFSR(Z,occ0,c=C0); e0,E0,it0,_=h0.run('hf',qtail=1)
    r,dr=h0.r,h0.dr; w=4*np.pi*r*r; P=h0.P; Q={(a,b):q for a,b,q in occ0}; ne=P[(n,l)]**2
    def dens(f):
        nu=np.zeros_like(r); nd=np.zeros_like(r)
        for (a,b),q in Q.items():
            cap=2*(2*b+1); d=P[(a,b)]**2; qs=q-(1-f) if (a,b)==(n,l) else q
            up=min(qs,cap/2); nu+=up*d; nd+=max(qs-cap/2,0)*d
        return nu,nd
    def Ec(f):
        nu,nd=dens(f); tot=float(np.sum((nu+nd)*eps_c(nu/w,nd/w)*dr))
        sic=f*float(np.sum(ne*eps_c(f*ne/w,0*ne)*dr)) if f>0 else 0.0
        return tot-sic
    def slope(f):
        nu,nd=dens(f); vu,vd=T.v_gbz(nu/w,nd/w)
        # entrant's own half-electron is spin-up first (as hfdscf); its spin channel:
        cap=2*(2*l+1); qs=Q[(n,l)]-(1-f); vs=vu if qs<=cap/2 else vd
        vsic=T.v_gbz(f*ne/w,0*ne)[0] if f>0 else 0*ne
        return float(np.sum(ne*(vs-vsic)*dr))
    fs=[0.0,0.25,0.5,0.75,1.0]; E=[Ec(f) for f in fs]; S={f:slope(f) for f in (0.0,0.5,1.0)}
    hh=0.25
    d1=(E[3]-E[1])/(2*hh)                          # central first derivative at 1/2
    d3=(E[4]-2*E[3]+2*E[1]-E[0])/(2*hh**3)         # central third derivative at 1/2
    D=E[4]-E[0]; gap=D-S[0.5]; simpson=(S[0.0]+4*S[0.5]+S[1.0])/6
    # closed-form SIC f^2 ln f piece: (lam0(1)/3)(ln2-1/2) N_e^- ; N_e^- = entrant density in the eps<0 region of its OWN density at f=1/2
    e_own=eps_c(0.5*ne/w,0*ne); Nneg=float(np.sum(ne*(e_own<0)*dr)); sicpiece=T._lam0(1.0)/3*(np.log(2)-0.5)*Nneg
    o=dict(Z=Z,el=el,sh=sh,subcell=SUBCELL,E_path=[round(x,6) for x in E],slope_0=round(S[0.0],6),slope_half=round(S[0.5],6),slope_1=round(S[1.0],6),
           fd_slope_half=round(d1,6),Delta_c_s26=H26.get(Z,{}).get('Delta_c'),D_frozen=round(D,6),
           D_hfc2=(round(H27[Z]['Ec_ion']-H27[Z]['Ec_neu'],6) if Z in H27 else None),gap=round(gap,6),simpson_slopes=round(simpson,6),
           curv24=round(d3/24,6),curv_share=round(d3/24/gap,3) if abs(gap)>1e-9 else None,sic_f2lnf=round(sicpiece,6),Nneg=round(Nneg,4),
           it=it0,sec=int(time.time()-t0))
    open(OUT,"a").write(json.dumps(o)+"\n"); print(o,flush=True)
