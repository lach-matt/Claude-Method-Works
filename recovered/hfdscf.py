"""hfdscf.py -- s26 (a'): exact-exchange DSCF removal energy of the entrant (HFSR 'hf', c=C0, integer occupations, average of configuration)
+ first-order chain-Z correlation (v_gbz with PZ SIC) on the neutral HF orbitals at entrant weight 1/2. usage: python3 hfdscf.py Z ... No constant beyond c."""
import sys,os,json,time,numpy as np
os.environ.setdefault("SIC_NOCLAMP","1")
from t7c_hfsr import HFSR
from t7c_kernel import C0
from t5_scf import ground_occ,minus
import t7c_cuaudit as T
OUT="hfdscf.jsonl"
SH={21:('Sc','3d'),22:('Ti','3d'),24:('Cr','3d'),26:('Fe','3d'),28:('Ni','3d'),29:('Cu','3d'),39:('Y','4d'),55:('Cs','6s'),57:('La','5d'),
    64:('Gd','5d'),66:('Dy','4f'),68:('Er','4f'),69:('Tm','4f'),70:('Yb','4f'),71:('Lu','5d')}
done={d['Z'] for d in map(json.loads,open(OUT))} if os.path.exists(OUT) else set()
for Z in map(int,sys.argv[1:]):
    if Z in done: print("SKIP",Z); continue
    el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); t0=time.time()
    occ0=ground_occ(Z); occ1=minus(occ0,n,l,1.0); occ1=[(a,b,q) for a,b,q in occ1 if q>0]
    h0=HFSR(Z,occ0,c=C0); e0,E0,it0,_=h0.run('hf',qtail=1)
    h1=HFSR(Z,occ1,c=C0); e1,E1,it1,_=h1.run('hf',qtail=1)
    D=float(E1-E0)
    r,dr=h0.r,h0.dr; w=4*np.pi*r*r; P=h0.P; Q={(a,b):q for a,b,q in occ0}; ne=P[(n,l)]**2; f=0.5
    nu=np.zeros_like(r); nd=np.zeros_like(r)
    for (a,b),q in Q.items():
        cap=2*(2*b+1); dens=P[(a,b)]**2; qs=q-(1-f) if (a,b)==(n,l) else q   # entrant shell at weight q-1/2 (TS), entrant's own 1/2 counted spin-up first
        up=min(qs,cap/2); nu+=up*dens; nd+=max(qs-cap/2,0)*dens
    vu,vd=T.v_gbz(nu/w,nd/w); vsic=T.v_gbz(f*ne/w,0*ne)[0]; Dc=float(np.sum(ne*(vu-vsic)*dr))
    o=dict(Z=Z,el=el,sh=sh,E_neu=round(float(E0),5),E_ion=round(float(E1),5),D_HF=round(D,5),eps_koop=round(float(e0[(n,l)]),5),it=[it0,it1],
           Delta_c=round(Dc,5),obj=round(-D+Dc,5),sec=int(time.time()-t0))
    open(OUT,"a").write(json.dumps(o)+"\n"); print(o,flush=True)