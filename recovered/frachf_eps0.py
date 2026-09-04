"""frachf_eps0.py -- s31 item (2): Sc eps(f=1e-3) by a run (corr and hf paths) in place of the linear extrapolation eps(0):=2eps(1/4)-eps(1/2).
Writes frachf_eps0.jsonl (side file; frachf.jsonl untouched). usage: python3 frachf_eps0.py Z [F]"""
import sys,os,json,time,numpy as np
os.environ.setdefault("SIC_NOCLAMP","1"); os.environ.setdefault("SUBCELL","1")
import hfc2 as H; from t7c_kernel import C0; from t5_scf import ground_occ; import t7c_cuaudit as T
Z=int(sys.argv[1]); F=float(sys.argv[2]) if len(sys.argv)>2 else 1e-3; sys.argv=[sys.argv[0]]
exec(open('frachf.py').read().split('def path')[0].split('import t7c_cuaudit as T')[1])   # HFCf, SH, OUT
OUT="frachf_eps0.jsonl"; done={(d['Z'],d['f']) for d in map(json.loads,open(OUT))} if os.path.exists(OUT) else set()
if (Z,F) in done: print("SKIP",Z,F); sys.exit()
el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); occ0=ground_occ(Z); t0=time.time(); res={}
for corr in (True,False):
    H.CORR=corr; occ=[(a,b,(F if (a,b)==(n,l) else q)) for a,b,q in occ0]
    h=HFCf(Z,occ,c=C0); h.ent=(n,l); h.f=F; h.frac={(n,l):(0,F)}
    E,Ec,it,eps=h.run2(); res['corr' if corr else 'hf']=dict(E=float(E),Ec=float(Ec),eps=float(eps[(n,l)]),it=it)
FR={d['Z']:d for d in map(json.loads,open('frachf.jsonl'))}[Z]
e=lambda p,f:FR[p][str(f)]['eps']
out=dict(Z=Z,el=el,sh=sh,f=F,run=res)
for p,k in (('corr_path','corr'),('hf_path','hf')):
    e0lin=2*e(p,0.25)-e(p,0.5); e0run=res[k]['eps']
    simp_lin=(e0lin+4*e(p,0.5)+e(p,1.0))/6; simp_run=(e0run+4*e(p,0.5)+e(p,1.0))/6
    D=FR['D_tot_corr'] if k=='corr' else FR['D_HF']
    out[k]=dict(eps0_lin=round(e0lin,6),eps0_run=round(e0run,6),simp_lin=round(simp_lin,6),simp_run=round(simp_run,6),D=D,gap_lin=round(D-simp_lin,6),gap_run=round(D-simp_run,6))
out['sec']=int(time.time()-t0)
open(OUT,'a').write(json.dumps(out)+'\n'); print(json.dumps(out))