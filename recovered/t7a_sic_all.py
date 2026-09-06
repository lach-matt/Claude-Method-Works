"""t7a_sic_all.py -- PZ-SIC (t7a_sic.scf_sic_orb) sic=False/True on every banked entrant row. Session 21. Appends t7a_all.jsonl; resumable."""
import sys, json, os, time
from t7a_sic import scf_sic_orb
from t5_scf import ground_occ, minus
SH={json.loads(l)['Z']:(json.loads(l)['el'],json.loads(l)['sh']) for l in open('t5.jsonl')}; SH.update({39:('Y','4d'),55:('Cs','6s')})
done={json.loads(l)['Z'] for l in open('t7a_all.jsonl')} if os.path.exists('t7a_all.jsonl') else set()
for Z in map(int,sys.argv[1:]):
    if Z in done: continue
    el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); hole=minus(ground_occ(Z),n,l,1.0); t0=time.time()
    Es0,h0,s0=scf_sic_orb(Z,1,occ=hole,entrant=(n,l),sic=False)
    Es1,h1,s1=scf_sic_orb(Z,1,occ=hole,entrant=(n,l),sic=True)
    e0=float(Es0[(n,l,s0,"ent")]); e1=float(Es1[(n,l,s1,"ent")])
    out=dict(Z=Z,el=el,sh=sh,ts_pol=round(e0,4),ts_sic=round(e1,4),shift=round(e1-e0,4),chan=s1,it=[len(h0),len(h1)],sec=round(time.time()-t0))
    open('t7a_all.jsonl','a').write(json.dumps(out)+'\n'); print(out,flush=True)