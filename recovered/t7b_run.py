"""t7b_run.py -- T7b run: HF-TS (Janak-consistent: g = eps_a(N-1/2) + J~_aa/2, J~ = F0_aa - w sum_k c_k F^k_aa; verified exact
against E0-E1 by Simpson on Yb, session 18) and HF-dSCF (E(N) - E(N-1), average-of-configuration HF, both integer occupations)
on the T7 species. Raw Fock eps(N-1/2) kept as hf_eps_half (NOT the observable's TS). Appends t7b.jsonl (resume-safe)."""
import sys, json, os, io, contextlib, time, numpy as np, warnings; warnings.filterwarnings("ignore")
with contextlib.redirect_stdout(io.StringIO()): import tfd
from t5_scf import ground_occ, minus
from t7b_hf import HF, _c3j0sq
T5 = {json.loads(l)['Z']: json.loads(l) for l in open('t5.jsonl')}
T6 = {json.loads(l)['Z']: json.loads(l) for l in open('t6.jsonl')} if os.path.exists('t6.jsonl') else {}
T7C = {json.loads(l)['Z']: json.loads(l) for l in open('t7c.jsonl')} if os.path.exists('t7c.jsonl') else {}
SPECIES = [66,68,69,70, 26, 57,64,71, 21,29]     # Dy Er Tm Yb | Fe | La Gd Lu | Sc Cu  (T7-BUILD-SPEC)
done = set()
if os.path.exists('t7b.jsonl'):
    for l in open('t7b.jsonl'): done.add(json.loads(l)['Z'])
want = set(int(a) for a in sys.argv[1:]) if len(sys.argv) > 1 else None
for Z in SPECIES:
    if Z in done or (want and Z not in want): continue
    t0 = time.time(); t = T5[Z]; sh = t['sh']; n, l = int(sh[0]), "spdf".index(sh[1]); g = ground_occ(Z); w = (2*l+1)/(4*l+1)
    h = HF(Z, minus(g,n,l,0.5)); eps, _, it1, _ = h.run('hf', qtail=1)
    P = h.P[(n,l)]; r, dr = h.r, h.dr
    Fk = lambda k: float(np.sum(P*P*h.Yk(P,P,k)/r*dr))
    J = Fk(0) - w*sum(_c3j0sq(l,k,l)*Fk(k) for k in range(2,2*l+1,2))
    e_half = float(eps[(n,l)]); ts = e_half + 0.5*J
    h0 = HF(Z, g); _, E0, it2, _ = h0.run('hf', qtail=1)
    h1 = HF(Z, minus(g,n,l,1.0)); _, E1, it3, _ = h1.run('hf', qtail=2)
    c = T7C.get(Z, {})
    row = dict(Z=Z, el=t['el'], sh=sh, meas=t['meas'], hfs_ts=t['hfs_ts'], dscf=t['dscf'], ts_pol=T6.get(Z,{}).get('ts_pol'),
               t7c_ts=c.get('t7c_ts'), t7c_dscf=c.get('t7c_dscf'),
               hf_eps_half=round(e_half,4), hf_J=round(J,4), hf_ts=round(ts,4), hf_dscf=round(float(E0-E1),4), E0=round(float(E0),4),
               shift_ts=round(ts-t['hfs_ts'],4), shift_dscf=round(float(E0-E1)-t['dscf'],4), it=[it1,it2,it3], sec=round(time.time()-t0))
    open('t7b.jsonl','a').write(json.dumps(row)+'\n'); print(row, flush=True)
