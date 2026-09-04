"""lwalk_hf.py -- s35 PREDICTION-LWALK bound (ii): HF (hfc2, SR, no correlation) for the frontier pair: Koopmans eigenvalues of the ground neutral (frozen HF field)
and DSCF removal of the s partner (swap). Ground-entrant DSCF from hfdscf.jsonl (record). usage: python3 lwalk_hf.py Z ... appends lwalk_hf.jsonl. No constant."""
import sys,os,json,time
os.environ.setdefault("SIC_NOCLAMP","1"); os.environ.setdefault("SUBCELL","1")
import hfc2 as H; from t7c_kernel import C0; from t5_scf import ground_occ,minus
H.CORR=False
SH={21:('Sc',(3,2),(4,0)),39:('Y',(4,2),(5,0)),57:('La',(5,2),(6,0)),71:('Lu',(5,2),(6,0)),55:('Cs',(6,0),None)}
HD={d['Z']:d for d in map(json.loads,open('hfdscf.jsonl'))}
OUT='lwalk_hf.jsonl'; done={d['Z'] for d in map(json.loads,open(OUT))} if os.path.exists(OUT) else set()
for Z in map(int,sys.argv[1:]):
    if Z in done: print("SKIP",Z); continue
    el,g,s=SH[Z]; t0=time.time(); occ0=ground_occ(Z)
    h0=H.HFC(Z,occ0,c=C0); E0,_,it0,eps0=h0.run2()
    o=dict(Z=Z,el=el,eps_g=round(float(eps0[g]),5),E_neu=round(E0,5),D_g_rel=-HD[Z]['D_HF'],eps_koop_rec=HD[Z]['eps_koop'],it=[it0])
    if s:
        o['eps_s']=round(float(eps0[s]),5); hs=H.HFC(Z,minus(occ0,s[0],s[1],1.0),c=C0); Es,_,its,_=hs.run2(); o['D_s_rel']=round(E0-Es,5); o['it'].append(its)
    o['sec']=int(time.time()-t0); open(OUT,'a').write(json.dumps(o)+'\n'); print(o,flush=True)