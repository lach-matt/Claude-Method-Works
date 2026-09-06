"""t7a_sicdec_run.py -- direct/indirect SIC decomposition, all rows. Appends t7a_dec.jsonl; resumable. Gate: mode=all == t7a_all.jsonl ts_sic."""
import sys, json, os
from t7a_sic_dec import scf_sic_dec
from t5_scf import ground_occ, minus
SH={json.loads(l)['Z']:(json.loads(l)['el'],json.loads(l)['sh']) for l in open('t5.jsonl')}; SH.update({39:('Y','4d'),55:('Cs','6s')})
A={json.loads(l)['Z']:json.loads(l) for l in open('t7a_all.jsonl')}
done={json.loads(l)['Z'] for l in open('t7a_dec.jsonl')} if os.path.exists('t7a_dec.jsonl') else set()
for Z in map(int,sys.argv[1:]):
    if Z in done: continue
    el,sh=SH[Z]; n,l=int(sh[0]),"spdf".index(sh[1]); hole=minus(ground_occ(Z),n,l,1.0)
    Es1,h1,s=scf_sic_dec(Z,1,occ=hole,entrant=(n,l),mode="ent"); e_ent=float(Es1[(n,l,s,"ent")])
    e0=A[Z]['ts_pol']; e_all=A[Z]['ts_sic']
    out=dict(Z=Z,el=el,sh=sh,e_none=e0,e_ent=round(e_ent,4),e_all=e_all,direct=round(e_ent-e0,4),indirect=round(e_all-e_ent,4),shift=A[Z]['shift'],it=len(h1))
    open('t7a_dec.jsonl','a').write(json.dumps(out)+'\n'); print(out,flush=True)