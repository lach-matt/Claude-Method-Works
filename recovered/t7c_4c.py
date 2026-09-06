"""t7c_4c.py -- s22 4c: untailed SR dSCF and TS on 5d rows. usage: Z"""
import sys,json,io,contextlib
with contextlib.redirect_stdout(io.StringIO()): import tfd
from t7c_kernel import scf_occ_sr
from t5_scf import ground_occ,minus
Z=int(sys.argv[1]); g=ground_occ(Z); out={}
for tag,k in (('N',0.0),('half',0.5),('ion',1.0)):
    Vf,Es,Etot,it=scf_occ_sr(Z,minus(g,5,2,k),0.0)
    out[tag]=dict(eps=round(float(Es[(5,2)]),5),Etot=round(float(Etot),5),it=it)
T={json.loads(l)['Z']:json.loads(l) for l in open('t7c.jsonl')}[Z]
row=dict(Z=Z,sh='5d',eps_ut=out['half']['eps'],dscf_ut=round(out['N']['Etot']-out['ion']['Etot'],5),ts_tailed=T['t7c_ts'],dscf_tailed=T['t7c_dscf'],
         split_tailed=round(T['t7c_ts']-T['t7c_dscf'],4),split_ut=round(out['half']['eps']-(out['N']['Etot']-out['ion']['Etot']),4),
         dscfut_minus_tstailed=round((out['N']['Etot']-out['ion']['Etot'])-T['t7c_ts'],4),it=[out[t]['it'] for t in ('N','half','ion')])
open('t7c_4c.jsonl','a').write(json.dumps(row)+'\n'); print(row,flush=True)