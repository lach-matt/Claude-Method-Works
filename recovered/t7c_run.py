"""t7c_run.py -- T7c run: scalar-relativistic HFS-TS and HFS-DSCF (c = 137.035999) on the T7 species; SR shift = T7c - t5 nonrel
column. Appends t7c.jsonl per species (resume-safe). Session 17."""
import sys, json, os, io, contextlib, numpy as np, warnings; warnings.filterwarnings("ignore")
with contextlib.redirect_stdout(io.StringIO()): import tfd
from t5_scf import ground_occ, minus
from t7c_kernel import scf_occ_sr, C0
T5 = {json.loads(l)['Z']: json.loads(l) for l in open('t5.jsonl')}
T6 = {json.loads(l)['Z']: json.loads(l) for l in open('t6.jsonl')} if os.path.exists('t6.jsonl') else {}
SPECIES = [66,68,69,70, 26, 57,64,71, 21,29]     # Dy Er Tm Yb | Fe | La Gd Lu | Sc Cu  (T7-BUILD-SPEC)
done = set()
if os.path.exists('t7c.jsonl'):
    for l in open('t7c.jsonl'): done.add(json.loads(l)['Z'])
want = set(int(a) for a in sys.argv[1:]) if len(sys.argv) > 1 else None
for Z in SPECIES:
    if Z in done or (want and Z not in want): continue
    t = T5[Z]; sh = t['sh']; n, l = int(sh[0]), "spdf".index(sh[1]); g = ground_occ(Z)
    _, Es, _, it1 = scf_occ_sr(Z, minus(g,n,l,0.5), 1, c=C0); ts = Es[(n,l)]
    _, _, E0, it2 = scf_occ_sr(Z, g, 1, c=C0); _, _, E1, it3 = scf_occ_sr(Z, minus(g,n,l,1.0), 2, c=C0)
    r = dict(Z=Z, el=t['el'], sh=sh, meas=t['meas'], hfs_ts=t['hfs_ts'], dscf=t['dscf'],
             ts_pol=T6.get(Z,{}).get('ts_pol'),
             t7c_ts=round(float(ts),4), t7c_dscf=round(float(E0-E1),4),
             shift_ts=round(float(ts)-t['hfs_ts'],4), shift_dscf=round(float(E0-E1)-t['dscf'],4), it=[it1,it2,it3])
    open('t7c.jsonl','a').write(json.dumps(r)+'\n'); print(r, flush=True)