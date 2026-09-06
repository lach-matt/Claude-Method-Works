"""cutfrac.py -- s29 mechanism-B diagnostic (PREDICTION-CUTFRAC-SESSION-29). One neutral SCF per class row on the s28 sc path (frachf.HFCf f=1)."""
import sys,os,json,numpy as np
os.environ.setdefault("SIC_NOCLAMP","1"); os.environ.setdefault("SUBCELL","1")
import hfc2 as H; from t7c_kernel import C0; from t5_scf import ground_occ; import t7c_cuaudit as T
sys.argv=[sys.argv[0]]; exec(open('frachf.py').read().split('def path')[0].split('import t7c_cuaudit as T')[1])   # HFCf class only
SH={21:('Sc','3d'),39:('Y','4d'),55:('Cs','6s'),57:('La','5d'),64:('Gd','5d'),71:('Lu','5d')}
so={21:0.0,39:0.0,55:0.0,57:-0.0046,64:-0.0073,71:-0.0083}; meas={21:0.2946,39:0.2285,55:0.14310,57:0.2386,64:0.2417,71:0.1994}
FR={d['Z']:d for d in map(json.loads,open('frachf.jsonl'))}
OUT="cutfrac.jsonl"; done={d['Z'] for d in map(json.loads,open(OUT))} if os.path.exists(OUT) else set()
for Z in [55,21,39,57,71,64]:
    if Z in done: print("SKIP",Z); continue
    el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); H.CORR=True
    occ=ground_occ(Z); h=HFCf(Z,occ,c=C0); h.ent=(n,l); h.f=1.0; E,Ec,it,eps=h.run2()
    r,dr=h.r,h.dr; w=4*np.pi*r*r; nu,nd,_=H.spin_split(occ,h.P); ntot=(nu+nd)/w; ne=h.P[(n,l)]**2/w
    e_tot=H.eps_c(nu/w,nd/w); e_self=H.eps_c(ne,0*r)
    qe=h.P[(n,l)]**2*dr; Q=qe.sum()
    idx=np.where(e_tot<0)[0]; r_cut=float(r[idx[-1]]) if len(idx) else 0.0
    F_out=float(qe[r>r_cut].sum()/Q); F_self=float(qe[e_self>=0].sum()/Q)
    rmean=float((qe*r).sum()/Q); rs_out=float((3/(4*np.pi*max(ntot[r>r_cut].max() if (r>r_cut).any() else 1e-30,1e-30)))**(1/3))
    d=FR[Z]; req=meas[Z]+d['D_HF']-so[Z]   # D_HF stored negative: req = meas - (-D_HF) - so... D_HF = E(1)-E(0) <0 -> IP_HF = -D_HF
    req=meas[Z]-(-d['D_HF'])-so[Z]; deliv=(-d['DEc_sc'])/req; missing=req-(-d['DEc_sc'])
    o=dict(Z=Z,el=el,sh=sh,it=it,E=round(float(E),5),Ec=round(float(Ec),5),r_cut=round(r_cut,3),rmean=round(rmean,3),F_out=round(F_out,4),F_self=round(F_self,4),
           required=round(req,4),delivered=round(deliv,3),missing=round(missing,4),missing_over_req=round(missing/req,3))
    open(OUT,"a").write(json.dumps(o)+"\n"); print(o,flush=True)