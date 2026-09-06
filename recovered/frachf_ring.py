"""frachf_ring.py -- s30 candidate C (PREDICTION-RING): the s28 sc path (frachf.HFCf) with the correlation form R (corr_ring: full RPA ring + E0B) patched in
for T.v_gbz and H.eps_c. f=1 and f=0 only (DEc_R = Ec(1)-Ec(0); the HF path is form-independent and taken from frachf.jsonl). usage: python3 frachf_ring.py Z ..."""
import sys,os,json,time,numpy as np
os.environ.setdefault("SIC_NOCLAMP","1"); os.environ.setdefault("SUBCELL","1")
import hfc2 as H; from t7c_kernel import C0; from t5_scf import ground_occ; import t7c_cuaudit as T; import corr_ring as CR
T.v_gbz=CR.v_R; H.eps_c=CR.eps_R                     # the ONLY change: the correlation form
Zs=[int(a) for a in sys.argv[1:]]; sys.argv=[sys.argv[0]]
exec(open('frachf.py').read().split('def path')[0].split('import t7c_cuaudit as T')[1])
SH={21:('Sc','3d'),39:('Y','4d'),55:('Cs','6s'),57:('La','5d'),64:('Gd','5d'),71:('Lu','5d')}
so={21:0.0,39:0.0,55:0.0,57:-0.0046,64:-0.0073,71:-0.0083}; meas={21:0.2946,39:0.2285,55:0.14310,57:0.2386,64:0.2417,71:0.1994}
FR={d['Z']:d for d in map(json.loads,open('frachf.jsonl'))}; CF={d['Z']:d for d in map(json.loads,open('cutfrac.jsonl'))}
OUT="frachf_ring.jsonl"; done={d['Z'] for d in map(json.loads,open(OUT))} if os.path.exists(OUT) else set()
for Z in Zs:
    if Z in done: print("SKIP",Z); continue
    el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); ent=(n,l); H.CORR=True; occ0=ground_occ(Z); t0=time.time(); res={}
    for f in (1.0,0.0):
        occ=[(a,b,(f if (a,b)==ent else q)) for a,b,q in occ0 if not ((a,b)==ent and f==0.0)]
        h=HFCf(Z,occ,c=C0); h.ent=ent; h.f=f
        if f>0: h.frac={ent:(0,f)}
        E,Ec,it,eps=h.run2(); res[f]=dict(E=float(E),Ec=float(Ec),it=it)
        if f==1.0:
            r,dr=h.r,h.dr; w=4*np.pi*r*r; nu,nd,_=H.spin_split(occ,h.P); e_tot=H.eps_c(nu/w,nd/w); qe=h.P[ent]**2*dr
            idx=np.where(e_tot<0)[0]; r_cut=float(r[idx[-1]]) if len(idx) else 0.0; F_out=float(qe[r>r_cut].sum()/qe.sum())
    DEc=res[1.0]['Ec']-res[0.0]['Ec']; Dtot=(res[1.0]['E']+res[1.0]['Ec'])-(res[0.0]['E']+res[0.0]['Ec'])
    d=FR[Z]; req=meas[Z]-(-d["D_HF"])+so[Z]; deliv=(-DEc)/req; c=CF[Z]
    o=dict(Z=Z,el=el,sh=sh,form='R',it=[res[1.0]['it'],res[0.0]['it']],DEc_R=round(DEc,6),DEc_Z=d['DEc_sc'],D_tot_R=round(Dtot,6),D_tot_Z=d['D_tot_corr'],
           D_HF=d['D_HF'],required=round(req,4),delivered_R=round(deliv,3),delivered_Z=c['delivered'],F_out_R=round(F_out,4),F_out_Z=c['F_out'],
           excess_R=round((1-deliv-F_out)*req,5),excess_Z=round((c['missing_over_req']-c['F_out'])*c['required'],5),
           resid_R=round(meas[Z]+so[Z]-(-Dtot),5),sec=int(time.time()-t0))
    open(OUT,"a").write(json.dumps(o)+"\n"); print(o,flush=True)